use std::io::{Cursor, Read, Write};
use std::fs::File;
use std::ops::Range;
use std::path::Path;
use std::marker::PhantomData;
use ml::io::ReadExt;
use anyhow::{Result, Context};
use cipher::{KeyInit, KeyIvInit, StreamCipher, BlockDecryptMut};
use cipher::generic_array::ArrayLength;
use cipher::consts::{U8, U13, U16};
use cipher::block_padding::NoPadding;
use clap::Parser;

#[derive(Parser, Debug)]
#[command(arg_required_else_help(true))]
struct Args {
    /// game
    #[arg(short, long, default_value_t = ArgsGameType::Auto)]
    game: ArgsGameType,

    /// input files
    #[arg(trailing_var_arg = true)]
    files: Vec<String>,
}

#[derive(Copy, Clone, Debug, clap::ValueEnum)]
enum ArgsGameType {
    Auto,
    ED8,
    ED9,
}

impl std::fmt::Display for ArgsGameType {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", match self {
            ArgsGameType::Auto => "auto",
            ArgsGameType::ED8 => "ed8",
            ArgsGameType::ED9 => "ed9",
        })
    }
}

enum GameType {
    Unknown,
    ED8,
    ED9,
}

struct Blowfish128<U: ArrayLength<u8>> {
    inner: blowfish::Blowfish,
    phantom: PhantomData<U>,
}

impl<U: ArrayLength<u8>> cipher::KeyInit for Blowfish128<U> {
    fn new(key: &cipher::Key<Self>) -> Self {
        Self::new_from_slice(&key[..]).unwrap()
    }

    fn new_from_slice(key: &[u8]) -> std::result::Result<Self, cipher::InvalidLength> {
        Ok(Blowfish128{
            phantom: PhantomData,
            inner: blowfish::Blowfish::new_from_slice(key)?,
        })
    }
}

impl<U: ArrayLength<u8>> cipher::BlockSizeUser for Blowfish128<U> {
    type BlockSize = U8;
}

impl<U: ArrayLength<u8>> cipher::BlockEncrypt for Blowfish128<U> {
    fn encrypt_with_backend(&self, f: impl cipher::BlockClosure<BlockSize = Self::BlockSize>) {
        self.inner.encrypt_with_backend(f)
    }
}

impl<U: ArrayLength<u8>> cipher::BlockDecrypt for Blowfish128<U> {
    fn decrypt_with_backend(&self, f: impl cipher::BlockClosure<BlockSize = Self::BlockSize>) {
        self.inner.decrypt_with_backend(f)
    }
}

impl<U: ArrayLength<u8>> cipher::BlockCipher for Blowfish128<U> {}

impl<U: ArrayLength<u8>> cipher::KeySizeUser for Blowfish128<U> {
    type KeySize = U;
}

const ED8_MAGIC_ENCRYPTED: u32 = 0x40104241;
const ED9_MAGIC_ENCRYPTED1: u32 = 0x41423943;
const ED9_MAGIC_ENCRYPTED2: u32 = 0x41423946;
const ED9_MAGIC_COMPRESSED: u32 = 0x41423944;

fn detect_game_type(input: &str, game: ArgsGameType) -> Result<GameType> {
    type LE = ml::io::LittleEndian;

    match game {
        ArgsGameType::ED8 => Ok(GameType::ED8),
        ArgsGameType::ED9 => Ok(GameType::ED9),
        ArgsGameType::Auto => {
            let mut fs = File::open(input)?;
            let magic = fs.read_u64::<LE>()?;

            Ok(match magic as u32 {
                ED8_MAGIC_ENCRYPTED => GameType::ED8,
                ED9_MAGIC_ENCRYPTED1 | ED9_MAGIC_ENCRYPTED2 | ED9_MAGIC_COMPRESSED => GameType::ED9,
                _ => GameType::Unknown,
            })
        }
    }
}

fn decrypt_ed8(input: &str, output: &str) -> Result<bool> {
    type LE = ml::io::LittleEndian;
    type Blowfish = ecb::Decryptor<Blowfish128<U13>>;

    const KEY: &[u8] = b"ed8psv5_steam";

    let mut fs = File::open(input).context("open input failed")?;

    if fs.metadata()?.len() < 8 {
        return Ok(false);
    }

    if fs.u32::<LE>() != ED8_MAGIC_ENCRYPTED {
        return Ok(false);
    }

    let size = fs.u32::<LE>() as usize;
    let mut buffer = vec![0u8; size];

    fs.read_exact(&mut buffer)?;

    let cipher = Blowfish::new_from_slice(KEY).unwrap();
    cipher.decrypt_padded_mut::<NoPadding>(&mut buffer[..size - size % 8]).unwrap();

    std::fs::create_dir_all(Path::new(output).parent().unwrap()).context("create dirs failed")?;

    File::create(output).with_context(|| format!("create output failed: {output}"))?.write_all(&buffer)?;

    Ok(true)

}

fn decrypt_ed9(input: &str, output: &str) -> Result<bool> {
    type LE = ml::io::LittleEndian;
    type Blowfish128Ctr64 = ctr::Ctr64BE::<Blowfish128<U16>>;

    const KEY: &[u8] = b"\x16\x4B\x7D\x0F\x4F\xA7\x4C\xAC\xD3\x7A\x06\xD9\xF8\x6D\x20\x94";
    const IV: &[u8] = b"\x9D\x8F\x9D\xA1\x49\x60\xCC\x4C";

    let mut fs = File::open(input).context("open input failed")?;

    if fs.metadata()?.len() < 8 {
        return Ok(false);
    }

    let mut buffer = vec![0u8; 4];

    fs.read_exact(&mut buffer)?;

    match Cursor::new(&buffer).u32::<LE>() {
        ED9_MAGIC_ENCRYPTED1 | ED9_MAGIC_ENCRYPTED2 | ED9_MAGIC_COMPRESSED => (),
        _ => return Ok(false),
    }

    fs.read_to_end(&mut buffer)?;

    let mut buffer_size = buffer.len();

    loop {
        let mut cursor = Cursor::new(&buffer[..buffer_size]);
        let magic = cursor.u32::<LE>();
        let size = cursor.u32::<LE>() as usize;

        match magic {
            ED9_MAGIC_ENCRYPTED1 | ED9_MAGIC_ENCRYPTED2 => {
                let mut cipher = Blowfish128Ctr64::new_from_slices(KEY, IV).unwrap();

                cipher.apply_keystream(&mut buffer[8..buffer_size]);

                buffer.copy_within(8..size + 8, 0);
                buffer_size = size;
            },

            ED9_MAGIC_COMPRESSED => {
                // {
                //     let mut fs = File::create(r".\c0000.dec.bin")?;
                //     fs.write_all(&buffer[..buffer_size]).unwrap();
                // }

                let mut cursor = Cursor::new(&buffer[8..size + 8]);
                let decompressed = zstd::decode_all(&mut cursor).context("zstd decompress failed")?;

                buffer_size = decompressed.len();
                if buffer.capacity() < buffer_size {
                    buffer.resize(buffer_size, 0);
                }

                buffer[..buffer_size].copy_from_slice(&decompressed);
            },

            _ => {
                std::fs::create_dir_all(Path::new(output).parent().unwrap()).context("create dirs failed")?;
                File::create(output).with_context(|| format!("create output failed: {output}"))?.write_all(&buffer)?;
                break;
            },
        }
    }

    Ok(true)

}

fn do_decrypt<F>(idx: Range<usize>, input: &str, output: &str, f: F) -> Result<bool>
where
    F: FnOnce(&str, &str) -> Result<bool>
{
    let processed = f(input, output).with_context(|| format!("decrypt failed: {}", input))?;

    if processed {
        println!("decrypted ({:04}/{:04}): {} -> {}", idx.start, idx.end, input, output);
    } else {
        println!("untouched ({:04}/{:04}): {}", idx.start, idx.end, input);
    }

    Ok(processed)
}

fn run() -> Result<()> {
    let args = Args::parse();

    println!("game type: {}", args.game);

    for f in args.files.iter() {
        let input = Path::new(f);
        let input_is_dir = input.is_dir();

        let output = if input_is_dir {
            input.with_file_name(format!("{input}_decrypted", input = input.file_name().unwrap().to_str().unwrap()))
        } else {
            let mut buf = input.to_path_buf();
            buf.set_file_name(format!("{}.decrypted", input.file_name().unwrap().to_str().unwrap()));
            buf
        };

        let input_str = input.to_str().unwrap();

        if input_is_dir {
            let output_dir = output;

            let files: Vec<_> = walkdir::WalkDir::new(input).into_iter().filter_map(|e| if e.as_ref().is_ok_and(|f| !f.file_type().is_dir()) { e.ok() } else { None }).collect();
            let file_count = files.len();

            for (idx, entry) in files.into_iter().enumerate() {
                let input_str = entry.path().to_str().unwrap();

                let output = output_dir.join(entry.path().strip_prefix(input)?);

                let game_type = detect_game_type(input_str, args.game).or::<anyhow::Error>(Ok(GameType::Unknown))?;
                let decrypter = match game_type {
                    GameType::Unknown => continue,
                    GameType::ED8 => decrypt_ed8,
                    GameType::ED9 => decrypt_ed9,
                };

                do_decrypt(idx + 1..file_count, entry.path().to_str().unwrap(), output.to_str().unwrap(), decrypter)?;
            }

        } else {
            let game_type = detect_game_type(input_str, args.game).or::<anyhow::Error>(Ok(GameType::Unknown))?;
            let decrypter = match game_type {
                GameType::Unknown => continue,
                GameType::ED8 => decrypt_ed8,
                GameType::ED9 => decrypt_ed9,
            };

            do_decrypt(1..1, input_str, output.to_str().unwrap(), decrypter)?;
        }
    }

    Ok(())
}

fn main() {
    if let Err(err) = run() {
        // let root_cause = err.root_cause();

        // if let Some(io_error) = root_cause.downcast_ref::<std::io::Error>() {
        //     println!("error kind: {}\n", io_error.kind());
        // }

        for (i, e) in err.chain().enumerate() {
            if i != 0 {
                print!(" -> {}", e);
            } else {
                print!("{}", e);
            }
        }
        println!();
    }
}
