use std::io::{Cursor, Read, Write};
use std::fs::File;
use std::ops::Range;
use std::path::Path;
use ml::io::ReadExt;
use anyhow::{Result, Context};
use cipher::{KeyIvInit, StreamCipher};
use clap::Parser;

#[derive(Parser, Debug)]
struct Args {
    /// game
    #[arg(short, long, default_value_t = GameType::ED9)]
    game: GameType,

    /// input files
    #[arg(trailing_var_arg = true)]
    files: Vec<String>,
}

#[derive(Clone, Debug, clap::ValueEnum)]
enum GameType {
    ED8,
    ED9,
}

impl std::fmt::Display for GameType {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", match *self {
            GameType::ED8 => "ed8",
            GameType::ED9 => "ed9",
        })
    }
}

struct Blowfish128 {
    inner: blowfish::Blowfish,
}

impl cipher::KeyInit for Blowfish128 {
    fn new(key: &cipher::Key<Self>) -> Self {
        Self::new_from_slice(&key[..]).unwrap()
    }

    fn new_from_slice(key: &[u8]) -> std::result::Result<Self, cipher::InvalidLength> {
        Ok(Blowfish128{
            inner: blowfish::Blowfish::new_from_slice(key)?,
        })
    }
}

impl cipher::BlockSizeUser for Blowfish128 {
    type BlockSize = cipher::consts::U8;
}

impl cipher::BlockEncrypt for Blowfish128 {
    fn encrypt_with_backend(&self, f: impl cipher::BlockClosure<BlockSize = Self::BlockSize>) {
        self.inner.encrypt_with_backend(f)
    }
}

impl cipher::BlockCipher for Blowfish128 {}

impl cipher::KeySizeUser for Blowfish128 {
    type KeySize = cipher::consts::U16;
}

fn decrypt_ed9(input: &str, output: &str) -> Result<bool> {
    type LE = ml::io::LittleEndian;
    type Blowfish128Ctr64 = ctr::Ctr64BE::<Blowfish128>;

    const KEY: &[u8] = b"\x16\x4B\x7D\x0F\x4F\xA7\x4C\xAC\xD3\x7A\x06\xD9\xF8\x6D\x20\x94";
    const IV: &[u8] = b"\x9D\x8F\x9D\xA1\x49\x60\xCC\x4C";

    let mut fs = File::open(input).with_context(|| format!("open input failed: {}", input))?;
    let mut buffer = Vec::new();

    fs.read_to_end(&mut buffer)?;

    let mut buffer_size = buffer.len();
    let mut decrypted_or_decompressed = false;

    loop {
        let mut cursor = Cursor::new(&buffer[..buffer_size]);
        let magic = cursor.u32::<LE>();
        let size = cursor.u32::<LE>() as usize;

        match magic {
            0x41423943 | 0x41423946 => {
                let mut cipher = Blowfish128Ctr64::new_from_slices(KEY, IV).unwrap();

                cipher.apply_keystream(&mut buffer[8..buffer_size]);

                buffer.copy_within(8..size + 8, 0);
                buffer_size = size;

                decrypted_or_decompressed = true;
            },

            0x41423944 => {
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

                decrypted_or_decompressed = true;
            },

            _ => {
                if !decrypted_or_decompressed {
                    return Ok(false);
                }

                std::fs::create_dir_all(Path::new(output).parent().unwrap())?;
                let mut fs = File::create(output)?;
                fs.write_all(&buffer)?;
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
    let processed = f(input, output).context("decrypt failed")?;

    if processed {
        println!("decrypted ({:04}/{:04}): {} -> {}", idx.start, idx.end, input, output);
    } else {
        println!("untouched ({:04}/{:04}): {}", idx.start, idx.end, input);
    }

    Ok(processed)
}

fn run() -> Result<()> {
    let args = Args::parse();

    for f in args.files.iter() {
        let input = Path::new(f);
        let input_is_dir = input.is_dir();

        let output = if input_is_dir {
            input.with_file_name(format!("{input}_decrypted", input = input.file_name().unwrap().to_str().unwrap()))
        } else {
            input.with_extension("decrypted")
        };

        match args.game {
            GameType::ED8 => todo!(),
            GameType::ED9 => {
                if input_is_dir {
                    let output_dir = output;

                    let files: Vec<_> = walkdir::WalkDir::new(input).into_iter().filter_map(|e| if e.as_ref().is_ok_and(|f| !f.file_type().is_dir()) { e.ok() } else { None }).collect();
                    let file_count = files.len();

                    for (idx, entry) in files.into_iter().enumerate() {
                        let output = output_dir.join(entry.path().strip_prefix(input)?);

                        // println!("{} -> {}", entry.path().to_str().unwrap(), output.to_str().unwrap());
                        do_decrypt(idx + 1..file_count, entry.path().to_str().unwrap(), output.to_str().unwrap(), decrypt_ed9)?;
                    }

                } else {
                    do_decrypt(1..1, input.to_str().unwrap(), output.to_str().unwrap(), decrypt_ed9)?;
                }
            },
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
