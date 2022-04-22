import { API, Modules } from "../modules";
import * as utils from "../utils";
import * as path from "path";
import { Interceptor2, ArrayBuffer2 } from "../utils";
import { DWriteRenderer } from "../dwrite/renderer";
import { AT9Decoder, AT9DecodeResult } from "../codec/at9";
import { DirectSound, DirectSoundBuffer } from "../dsound/dsound";
import { Addrs } from "./addrs";
import { ED6PseudoCompress } from "./utils";
import { ED6FC } from "./types";
import ExeText from "./ed6fc.text.json"
import { VoiceIdOffset, VoiceIdMapping } from "./voice_id_map"

const TextEncoding = 'gbk';

function hookSteamAndMisc() {
    const patches: any = [
        // _set_se_translator
        // [Addrs.ED6FC.ExceptionHandler,      [0xEB]],

        // 004AEF09      /76 3E               jbe     short 0x4AEF49
        [Addrs.ED6FC.GetTextWidth,          [0x05]],

        [Addrs.ED6FC.AsciiCharWidth,        new Array(0x200).fill(0)],
        [Addrs.ED6FC.AsciiFontSizeScale,    [0x00, 0x00, 0x80, 0x3E]],  // 0.25
    ];

    let min: NativePointer = NULL.sub(1);
    let max: NativePointer = NULL;

    for (let p of patches) {
        const addr = p[0] as NativePointer;
        if (addr.compare(min) < 0) {
            min = addr
        }

        if (addr.compare(max) > 0)
            max = addr;
    }

    Memory.patchCode(min, max.sub(min).add(0x30).toUInt32(), () => {
        for (let p of patches) {
            p[0].writeByteArray(p[1]);
        }
    });

    const CreateFileW = new NativeCallback(
        function(fileName: NativePointer, desiredAccess: number, shareMode: number, securityAttributes: NativePointer, creationDisposition: number, flagsAndAttributes: number, templateFile: NativePointer): NativePointer {
            const name = fileName.readUtf16String();

            switch (name) {
                case 'steam_api.dll':
                case 'Galaxy.dll':
                    return NULL.sub(1);

                case 'dll\\lang_jpn.dll':
                    fileName.writeUtf16String('dll\\ogg.dll');
                    break;
            }

            return API.WIN32.CreateFileW(fileName, desiredAccess, shareMode, securityAttributes, creationDisposition, flagsAndAttributes, templateFile);
        },
        'pointer', ['pointer', 'uint32', 'uint32', 'pointer', 'uint32', 'uint32', 'pointer'], 'stdcall'
    );

    Memory.patchCode(Addrs.IAT.CreateFileW, Process.pointerSize, (code) => {
        code.writePointer(CreateFileW);
    });
}

function hookEncodingCheck() {
    const patterns: any = [
        /*
            004E1DE2   |.  80F9 80             |cmp     cl, 0x80
            004E1DE5   |.  73 04               |jnb     short 0x4E1DEB
            004E1DE7   |.  33C9                |xor     ecx, ecx
            004E1DE9   |.  EB 12               |jmp     short 0x4E1DFD
            004E1DEB   |>  80F9 A0             |cmp     cl, 0xA0
            004E1DEE   |.  73 07               |jnb     short 0x4E1DF7
            004E1DF0   |.  B9 01000000         |mov     ecx, 0x1
            004E1DF5   |.  EB 06               |jmp     short 0x4E1DFD
        */
        ['80 ?? 80 73 ?? 33 ?? EB ?? 80 ?? A0 73', 0x0D, [0x00]],

        /*
            004DEA26    > /3C 80               cmp     al, 0x80
            004DEA28    . |73 04               jnb     short 0x4DEA2E
            004DEA2A    . |33C9                xor     ecx, ecx
            004DEA2C    . |EB 10               jmp     short 0x4DEA3E
            004DEA2E    > |3C A0               cmp     al, 0xA0
            004DEA30    . |73 07               jnb     short 0x4DEA39
            004DEA32    . |B9 01000000         mov     ecx, 0x1
        */
        ['3C 80 73 ?? 33 ?? EB ?? 3C A0 73', 0x0B, [0x00]],

        /*
            004AEF0B   |.  80F9 80             cmp     cl, 0x80
            004AEF0E   |.  73 04               jnb     short 0x4AEF14
            004AEF10   |.  32C0                xor     al, al
            004AEF12   |.  EB 0F               jmp     short 0x4AEF23
            004AEF14   |>  80F9 A0             cmp     cl, 0xA0
            004AEF17   |.  73 04               jnb     short 0x4AEF1D
        */
        ['80 ?? 80 73 ?? 32 ?? EB ?? 80 ?? A0 73', 0x0D, [0x00]],

        /*
            0041BBB3    .  3C 80               cmp     al, 0x80
            0041BBB5    .  73 04               jnb     short 0x41BBBB
            0041BBB7    .  32C9                xor     cl, cl
            0041BBB9    .  EB 0D               jmp     short 0x41BBC8
            0041BBBB    >  3C A0               cmp     al, 0xA0
            0041BBBD    .  73 04               jnb     short 0x41BBC3
            0041BBBF    .  B1 01               mov     cl, 0x1
        */
        ['3? 80 73 ?? 32 ?? EB ?? ?? A0 73', 0x0B, [0x00]],

        /*
            004A8877   |> \3C 80               |cmp     al, 0x80
            004A8879   |.  72 15               |jb      short 0x4A8890
            004A887B   |.  3C A0               |cmp     al, 0xA0
            004A887D   |.  72 04               |jb      short 0x4A8883
            004A887F   |.  3C E0               |cmp     al, 0xE0
            004A8881   |.  72 0D               |jb      short 0x4A8890
        */
        ['80 72 ?? ?? A0 72 ?? ?? E0 72', 0x05, [0xEB]],

        /*
            004D2DC0    .  3C 80               cmp     al, 0x80
            004D2DC2    .  0F82 34010000       jb      0x4D2EFC
            004D2DC8    .  3C A0               cmp     al, 0xA0
            004D2DCA    .  72 08               jb      short 0x4D2DD4
            004D2DCC    .  3C E0               cmp     al, 0xE0
            004D2DCE    .  0F82 28010000       jb      0x4D2EFC
        */
        ['80 0F 82 ?? ?? ?? ?? ?? A0 72 ?? ?? E0 0F 82', 0x09, [0xEB]],

        /*
            004AF0E6   |> /80F9 80             /cmp     cl, 0x80
            004AF0E9   |. |72 46               |jb      short 0x4AF131
            004AF0EB   |. |80F9 A0             |cmp     cl, 0xA0
            004AF0EE   |. |72 05               |jb      short 0x4AF0F5
            004AF0F0   |. |80F9 E0             |cmp     cl, 0xE0
            004AF0F3   |. |72 3C               |jb      short 0x4AF131
        */
        ['80 ?? 80 72 ?? 80 ?? A0 72 ?? 80 ?? E0 72', 0x08, [0xEB]],

        /*
            004E1BE5    .  3C 80               cmp     al, 0x80
            004E1BE7    .  73 07               jnb     short 0x4E1BF0
            004E1BE9    .  B8 01000000         mov     eax, 0x1
            004E1BEE    .  EB 12               jmp     short 0x4E1C02
            004E1BF0    >  3C A0               cmp     al, 0xA0
            004E1BF2    .  73 07               jnb     short 0x4E1BFB
            004E1BF4    .  B8 02000000         mov     eax, 0x2
        */
        ['80 73 ?? ?? ?? ?? ?? ?? EB ?? ?? A0 73', 0x0D, [0x00]],
    ];

    const textSection = utils.getSectionHeaders(Modules.ED6FC.base)[0];
    const textStart = Modules.ED6FC.base.add(textSection.add(0x0C).readU32());
    const textSize  = textSection.add(0x10).readU32();

    for (let p of patterns) {
        const pattern = p[0];
        const offset = p[1];
        const data = p[2];

        for (let addr of Memory.scanSync(textStart, textSize, pattern)) {
            Memory.patchCode(addr.address.add(offset), 1, (code) => {
                code.writeByteArray(data);
            })
        }
    }

    Memory.patchCode(Addrs.ED6FC.JPFontSizeLimit, 1, (code) => {
        code.writeU8(0xEB);
    });
}

function hookWindow() {
    const SWP_NOMOVE = 2;
    const SPI_GETWORKAREA = 0x30;
    const SetWindowPos = new NativeCallback(
        function(hWnd: NativePointer, hWndInsertAfter: NativePointer, X: number, Y: number, cx: number, cy: number, Flags: number): number {

            if (Flags == SWP_NOMOVE) {
                const workArea = Memory.alloc(0x10);

                API.USER32.SystemParametersInfoW(SPI_GETWORKAREA, 0, workArea, 0);

                X = ((workArea.add(8).readU32() - workArea.readU32()) - cx) / 2;
                Y = ((workArea.add(12).readU32() - workArea.add(4).readU32()) - cy) / 2;

                Flags = 0;
            }

            return API.USER32.SetWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, Flags);
        },
        'uint32', ['pointer', 'pointer', 'int32', 'int32', 'int32', 'int32', 'uint32'], 'stdcall'
    );

    Memory.patchCode(Addrs.IAT.SetWindowPos, Process.pointerSize, (code) => {
        code.writePointer(SetWindowPos);
    });
}

function hookFileIo() {
    const LoadFileFromDAT = Interceptor2.jmp(
        Addrs.ED6FC.LoadFileFromDAT,
        function(datOffset: number, fileSize: number): number {
            const ctx = this.context as Ia32CpuContext;
            const buffer = ctx.ecx;
            const datIndex = ctx.edx.toUInt32();

            for (let dir = ED6FC.dirCacheTable[datIndex]; dir; dir = dir.next) {
                if (dir.offset != datOffset || dir.size != fileSize)
                    continue;

                const filePath = path.join(Modules.ExePath, 'DAT', `ED6_DT${datIndex.toString(16).padStart(2, '0')}`, dir.fileName);
                const content = utils.readFileContent(filePath);

                if (!content)
                    break;

                console.log(`load ${filePath}`);
                buffer.writeByteArray(ED6PseudoCompress(content));

                return 1;
            }

            const fp = API.crt.wfopen(utils.UTF16(`ED6_DT${datIndex.toString(16).padStart(2, '0')}.DAT`), utils.UTF16('rb'));

            if (fp.isNull())
                return 0;

            if (API.crt.fseek(fp, datOffset, 0) != 0) {
                API.crt.fclose(fp);
                return 0;
            }

            API.crt.fread(buffer, fileSize, 1, fp);
            API.crt.fclose(fp);

            return 1;

            // return LoadFileFromDAT(buffer, datIndex, datOffset, fileSize);
        },
        'int32', ['uint32', 'uint32'],
        'mscdecl',
    );
}

function hookTextRenderer() {
    const FontSizeTable = [
        0x08, 0x0C, 0x10, 0x14,
        0x18, 0x20, 0x12, 0x1A,
        0x1E, 0x24, 0x28, 0x2C,
        0x30, 0x32, 0x36, 0x3C,
        0x40, 0x48, 0x50, 0x60,
        0x80, 0x90, 0xA0, 0xC0,
    ];

    const TextColorTable = [
        0x0FFF, 0x0FC7, 0x0F52, 0x08CF,
        0x0FB4, 0x08FA, 0x0888, 0x0FEE,
        0x0853, 0x0333, 0x0CA8, 0x0FDB,
        0x0ACE, 0x0CFF, 0x056B, 0x0632,
        0x0135, 0x0357, 0x0BBB,
    ];

    const asciiRenderer: DWriteRenderer[] = new Array(FontSizeTable.length);
    const mbcsRenderer : DWriteRenderer[] = new Array(FontSizeTable.length);
    const sjisRenderer : DWriteRenderer[] = new Array(FontSizeTable.length);

    for (let index in FontSizeTable) {
        const fontSize = FontSizeTable[index];
        asciiRenderer[index] = new DWriteRenderer(fontSize, undefined, 'consolas');
        mbcsRenderer[index] = new DWriteRenderer(fontSize, 'font.ttf', undefined);
        sjisRenderer[index] = new DWriteRenderer(fontSize, 'jpfont.ttf', undefined);
    }

    function translateChar(ch: number): number | undefined {
        return {
            0xA181: '■',
            0xF6A1: '■',
            0x4881: '？',
            0x9F81: '◆',
            0xAA84: '━',
            0x4081: '　',
            0xA1A1: '　',
            0x9A81: '★',
            0x4C87: '⑬',
            0x4D87: '⑭',
            0x5C81: '―',   // 手册
            0x5AA9: '♥',
            0xD1A1: '♪',
            0xADA1: '…',
            0xA4A1: '・',
        }[ch]?.codePointAt(0)!;
    }

    function GetGlyphsBitmap(s: string | undefined, text: NativePointer, buffer: NativePointer, stride: number, colorIndex: number): NativePointer {
        if (s === undefined) {
            s = utils.readMBCS(text, TextEncoding);
        }

        if (!s)
            return buffer;

        // console.log(s);

        let   width         = 0;
        const fontSizeIndex = ED6FC.fontSizeIndex;
        const fontSize      = FontSizeTable[fontSizeIndex];
        const color         = TextColorTable[colorIndex >= TextColorTable.length ? 0 : colorIndex];
        const mbcs          = mbcsRenderer[fontSizeIndex];
        const ascii         = asciiRenderer[fontSizeIndex];
        const sjis          = sjisRenderer[fontSizeIndex];

        for (let ch of s) {
            const codePoint = ch.codePointAt(0)!;

            if (codePoint == 0x20) {
                width = fontSize / 2;
                text = text.add(1);

            } else if (codePoint < 0x80) {
                ascii.drawRune(codePoint, color, buffer, stride);
                width = fontSize / 2;
                text = text.add(1);

            } else {
                const trans = translateChar(text.readU16());
                (trans ? sjis : mbcs).drawRune(trans ? trans : codePoint, color, buffer, stride);
                width = fontSize;
                text = text.add(2);
            }

            buffer = buffer.add(width * 2);
        }

        return buffer;
    }

    Interceptor2.jmp(
        Addrs.ED6FC.GetGlyphsBitmap,
        function(text: NativePointer, buffer: NativePointer, stride: number, colorIndex: number) {
            GetGlyphsBitmap(undefined, text, buffer, stride, colorIndex);
        },
        'void', ['pointer', 'pointer', 'uint32', 'uint32'],
        'stdcall',
    );

    Interceptor2.jmp(
        Addrs.ED6FC.DrawTalkText,
        function(thiz: NativePointer, buffer: NativePointer, stride: number, text: NativePointer): NativePointer {
            // console.log(`${DrawTalkText}(${thiz}, ${buffer}, ${stride}, ${text})`);

            const p = text.readPointer();

            const colorIndex = thiz.add(4).readU16();
            const ch = p.readU8();

            switch (ch) {
                case 0x40:  // @
                    thiz.add(0x0C).writeU32(3);
                    return buffer;

                case 0x7C:  // |
                    thiz.add(0x0C).writeU32(2);
                    return buffer;

                default:
                    if (ch >= 0x80)
                        text.writePointer(p.add(1));

                    return GetGlyphsBitmap(utils.readMBCS(p, TextEncoding, ch < 0x80 ? 1 : 2), p, buffer, stride * 2, colorIndex);
            }
        },
        'pointer', ['pointer', 'pointer', 'uint32', 'pointer'],
        'thiscall',
    );
}

function hookTalk() {
    let ds: DirectSound | undefined = undefined;
    let sb: DirectSoundBuffer | undefined = undefined;

    function loadVoice(voiceId: string): AT9DecodeResult | undefined {
        const id = VoiceIdMapping[parseInt(voiceId, 10) + VoiceIdOffset[voiceId.length]];
        const idstr = id.toString().padStart(10, '0');

        // ch 001 000 0001
        const voicePath = path.join(Modules.ExePath, 'voice', 'at9', `${idstr.slice(3, 6)}`, `ch${idstr}.at9`);

        console.log(`voice path: ${voicePath}`);

        // const voicePath2 = 'E:\\Game\\Steam\\steamapps\\common\\Trails in the Sky FC\\DAT\\talk\\ch0081040004.at9';
        const at9 = utils.readFileContent(voicePath);

        if (!at9) {
            console.log('wtf');
            return undefined;
        }

        const ret = AT9Decoder.decode(at9)
        if (!ret)
            return undefined;

        return ret;
    }

    function playVoice(voiceId: string) {
        console.log('playVoice');
        if (Addrs.ED6FC.DirectSound.readPointer().isNull())
            return;

        if (ds === undefined) {
            ds = new DirectSound(Addrs.ED6FC.DirectSound.readPointer());
        }

        stopVoice();

        const voice = loadVoice(voiceId);

        if (!voice) {
            console.log('invalid voice id');
            return;
        }

        sb = ds.CreateSoundBuffer({
            flags       : 0x82,
            bufferBytes : voice.dataSize,
            wfxFormat   : voice.wfxFormat,
        });

        if (!sb) {
            console.log('create sb failed');
            return;
        }

        const dsb = sb.lock(ptr(0), ptr(voice.dataSize), 0);

        if (!dsb) {
            console.log('dsb lock failed');
            stopVoice();
            return;
        }

        dsb.audioPtr1.writeByteArray(voice.data.readByteArray(dsb.audioBytes1.toInt32())!);
        const audioPtr2 = dsb.audioPtr2;
        if (!audioPtr2.isNull()) {
            audioPtr2.writeByteArray(voice.data.add(dsb.audioBytes1.toUInt32()).readByteArray(dsb.audioBytes2.toUInt32())!);
        }

        sb.unlock(dsb);
        sb.setVolume(ED6FC.seVolume);

        sb.play(0);

        console.log('success');
    }

    function stopVoice() {
        console.log('stopVoice');
        sb?.stop();
        sb?.release();
        sb = undefined;
    }

    // const scena_op_5b = Interceptor2.jmp(
    //     ptr(0x4A3FF0),
    //     function(thiz: NativePointer, context: NativePointer): number {
    //         console.log('ChrTalk');

    //         return scena_op_5b(thiz, context);
    //     },
    //     'int32', ['pointer', 'pointer'], 'thiscall',
    // );

    let lastTerminator = NULL;

    const showTalkText = Interceptor2.jmp(
        Addrs.ED6FC.ShowTalkText,
        function(thiz: NativePointer, text: NativePointer, arg3: number, arg4: number): NativePointer {
            let p = text;

            // console.log(`** ShowTalkText(${(this.context as Ia32CpuContext).esp.readPointer()}) ** ${text}: "${utils.readMBCS(text, TextEncoding)!}"`);

            const firstCh = p.readU8();

            switch (firstCh) {
                case 0x00:
                    // utils.log(`firstCh: 0x${firstCh.toString(16).padStart(2, '0')}`);
                    if (!p.equals(lastTerminator)) {
                        stopVoice();
                        lastTerminator = p;
                    }
                    return showTalkText(thiz, text, arg3, arg4);
                    // break;

                case 0x03:
                    stopVoice();
                    break;
            }

            for (;; p = p.add(1)) {
                const ch = p.readU8();

                // utils.log(`char: 0x${ch.toString(16).padStart(2, '0')}`);

                switch (ch) {
                    default:
                        break;

                    case 0x00:
                    case 0x02:
                        break;

                    case 0x03:
                        continue;

                    case 0x23:  // #
                    {
                        const start = p.add(1);

                        for (p = start;; p = p.add(1)) {
                            const ch = p.readU8();
                            if (ch < 0x30 || ch > 0x39)
                                break;
                        }

                        if (p.readU8() != 0x76) {
                            // #12345v
                            continue;
                        }

                        const voiceId = Buffer.from(start.readByteArray(p.sub(start).toUInt32())!).toString('ascii');

                        console.log(`voiceId: ${voiceId}`);

                        playVoice(voiceId);

                        break;
                    }
                }

                break;
            }

            return showTalkText(thiz, text, arg3, arg4);
        },
        'pointer', ['pointer', 'pointer', 'uint32', 'uint32'], 'thiscall',
    );

    // Interceptor.attach(ptr(0x4E1690), function() {
    //         const ctx = this.context as Ia32CpuContext;
    //         const text = ctx.esi;
    //         const ch = text.readU8();

    //         switch (ch) {
    //             case 0x02:
    //                 playVoice();
    //                 break;

    //             case 0x03:
    //                 onTalkEnd();
    //                 break;
    //         }
    //     },
    // );

    // const scena_op_58 = Interceptor2.jmp(
    //     ptr(0x4A3DD0),
    //     function(thiz: NativePointer, context: NativePointer): number {
    //         const closed = scena_op_58(thiz, context) & 0xFF;

    //         utils.log(`scena_op_58: ${closed}`);
    //         if (closed != 0) {
    //             onTalkEnd();
    //         }

    //         return closed;
    //     },
    //     'int32', ['pointer', 'pointer'], 'thiscall',
    // );

    // const scena_op_53 = Interceptor2.jmp(
    //     ptr(0x4A3A40),
    //     function(thiz: NativePointer, context: NativePointer): number {
    //         const closed = scena_op_53(thiz, context) & 0xFF;
    //         console.log(`TalkEnd: ${closed}`);
    //         onTalkEnd();
    //         return closed;
    //     },
    //     'int32', ['pointer', 'pointer'], 'thiscall',
    // );

    // const clearTextBox = Interceptor2.jmp(
    //     ptr(0x4E1E20),
    //     function(thiz: NativePointer) {
    //         console.log('clearTextBox');
    //         onTalkEnd();
    //         clearTextBox(thiz);
    //     },
    //     'void', ['pointer'], 'thiscall',
    // );
}

function dump() {
    const fp = API.crt.wfopen(utils.UTF16('ed6_win_dump'), utils.UTF16('wb'));
    API.crt.fwrite(Modules.ED6FC.base, Modules.ED6FC.size, 1, fp);
    API.crt.fclose(fp);
}

export function main() {
    // (new NativeFunction(Process.getModuleByName('KERNEL32.dll').getExportByName('AllocConsole'), 'bool', []))();

    console.log('fc dx9 patchModuleText');
    utils.patchModuleText(Modules.ED6FC, ExeText);

    console.log('hookSteamAndMisc');
    hookSteamAndMisc();

    console.log('hookEncodingCheck');
    hookEncodingCheck();

    console.log('hookWindow');
    hookWindow();

    console.log('hookFileIo');
    hookFileIo();

    console.log('hookTextRenderer');
    hookTextRenderer();

    console.log('hookTalk');
    hookTalk();

    console.log('done');
}
