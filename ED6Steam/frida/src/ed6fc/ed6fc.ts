import { API, Modules } from "../modules";
import * as utils from "../utils";
import * as path from "path";
import { Interceptor2 } from "../utils";
import { DWriteRenderer } from "../dwrite/renderer";
import { Addrs } from "./addrs";
import { ED6PseudoCompress } from "./utils";
import { ED6FC } from "./types";
import ExeText from "./ed6fc.json"

const TextEncoding = 'gbk';

function hookSteamAndMisc() {
    const patches: any = [
        [Addrs.Steam.Init,                  [0xE9, 0x81, 0x00, 0x00, 0x00, 0x90, 0x90]],
        [Addrs.Steam.InitLang,              [0x33, 0xC3]],
        [Addrs.Steam.Init,                  [0xE9, 0x81, 0x00, 0x00, 0x00, 0x90, 0x90]],
        [Addrs.Steam.InitLang,              [0x33, 0xC3]],
        [Addrs.Steam.CheckCloudSave,        [0x83, 0xC4, 0x0C, 0xE9, 0x53, 0x04, 0x00, 0x00]],
        [Addrs.Steam.CheckCloudSave2,       [0x83, 0xC4, 0x0C, 0xE9, 0xD4, 0x00, 0x00, 0x00]],
        [Addrs.Steam.CheckCloudSave3,       [0x83, 0xC4, 0x0C, 0xE9, 0x28, 0x01, 0x00, 0x00]],
        [Addrs.Steam.CheckCloudSave4,       [0x83, 0xC4, 0x10, 0xEB, 0x2B, 0x90]],
        [Addrs.Steam.CheckAchievements,     [0xC3]],
        [Addrs.Steam.CheckAchievements2,    [0xC3]],
        [Addrs.Steam.CheckAchievements3,    [0xC3]],
        [Addrs.Steam.CheckAchievements4,    [0xC3]],
        [Addrs.Steam.CheckAchievements5,    [0xC3]],
        [Addrs.Steam.CheckAchievements6,    [0xC3]],
        [Addrs.Steam.CheckAchievements7,    [0xC3]],
        [Addrs.Steam.CheckAchievements8,    [0xC3]],
        [Addrs.Steam.CheckAchievements9,    [0xC3]],
        [Addrs.Steam.CheckAchievements10,   [0xC3]],
        [Addrs.Steam.CheckAchievements11,   [0xC3]],
        [Addrs.Steam.CheckAchievements12,   [0xC3]],
        [Addrs.Steam.CheckAchievements13,   [0xC3]],
        [Addrs.Steam.CheckAchievements14,   [0xC3]],
        [Addrs.Steam.CheckAchievements15,   [0xC3]],
        [Addrs.Steam.CheckAchievements16,   [0xC3]],
        [Addrs.Steam.CheckAchievements17,   [0xC3]],
        [Addrs.Steam.CheckAchievements18,   [0xC3]],
        [Addrs.Steam.RunCallbacks,          [0x8D, 0x80, 0x00, 0x00, 0x00, 0x00]],

        // 004B1D0A      /76 0F               jbe     short 0x4B1D1B
        [Addrs.ED6FC.GetTextWidth,          [0x76, 0x0F]],
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
}

function hookEncodingCheck() {
    const patterns: any = [

        /*
            char width
            004B1A31   |.  56                  push    esi
            004B1A32   |.  8D71 E0             lea     esi, dword ptr [ecx-0x20]
            004B1A35   |.  83FE 5F             cmp     esi, 0x5F
            004B1A38   |.  5E                  pop     esi
            004B1A39   |.  76 29               jbe     short 0x4B1A64
            004B1A3B   |.  3C 80               cmp     al, 0x80
            004B1A3D   |.  72 08               jb      short 0x4B1A47
            004B1A3F   |.  3C A0               cmp     al, 0xA0
            004B1A41   |.  72 18               jb      short 0x4B1A5B
            004B1A43   |.  3C E0               cmp     al, 0xE0
            004B1A45   |.  73 14               jnb     short 0x4B1A5B
        */
        ['76 ?? ?? 80 72 ?? ?? A0 72 ?? ?? E0 73', 1, [0x0C]],

        /*
            004667DA    .  80F9 80             cmp     cl, 0x80
            004667DD    .  72 31               jb      short 0x466810
            004667DF    .  80F9 A0             cmp     cl, 0xA0
            004667E2    .  72 05               jb      short 0x4667E9
            004667E4    .  80F9 E0             cmp     cl, 0xE0
            004667E7    .  72 4B               jb      short 0x466834
        */
        ['80 ?? 80 72 ?? 80 ?? A0 72 ?? 80 ?? E0', 8, [0xEB]],

        /*
            004837F0    .  3C 80               cmp     al, 0x80
            004837F2    .  72 0F               jb      short 0x483803
            004837F4    .  3C A0               cmp     al, 0xA0
            004837F6    .  72 04               jb      short 0x4837FC
            004837F8    .  3C E0               cmp     al, 0xE0
            004837FA    .  72 07               jb      short 0x483803
        */
        ['3C 80 72 ?? 3C A0 72 ?? 3C E0', 6, [0xEB]],

        /*
            00476198   |.  3C 80               |cmp     al, 0x80
            0047619A   |.  0F82 50010000       |jb      0x4762F0
            004761A0   |.  3C A0               |cmp     al, 0xA0
            004761A2       72 08               |jb      short 0x4761AC
            004761A4   |.  3C E0               |cmp     al, 0xE0
            004761A6   |.  0F82 44010000       |jb      0x4762F0
        */
        ['3C 80 0F ?? ?? ?? ?? ?? 3C A0 72 ?? 3C E0', 0x0A, [0xEB]],

        /*
            copy chr name
            00483950   |> /8801                /mov     byte ptr [ecx], al
            00483952   |. |3C 80               |cmp     al, 0x80
            00483954   |. |73 04               |jnb     short 0x48395A
            00483956   |. |33C0                |xor     eax, eax
            00483958   |. |EB 10               |jmp     short 0x48396A
            0048395A   |> |3C A0               |cmp     al, 0xA0
            0048395C   |. |73 07               |jnb     short 0x483965
            0048395E   |. |B8 01000000         |mov     eax, 0x1
            00483963   |. |EB 05               |jmp     short 0x48396A
        */
        ['3C 80 73 ?? 33 C0 EB ?? 3C A0 73 ?? ?? 01 00 00 00 EB', 0xB, [0x00]],

        /*
            00480F0C   |.  8A18                mov     bl, byte ptr [eax]
            00480F0E   |.  0FB6D3              movzx   edx, bl
            00480F11   |.  83C2 C0             add     edx, -0x40                                        ;  Switch (cases 40..A3)
            00480F14   |.  83FA 63             cmp     edx, 0x63
            00480F17   |.  77 4A               ja      short 0x480F63
            00480F19   |.  0FB692 CC0F4800     movzx   edx, byte ptr [edx+0x480FCC]
            00480F20   |.  FF2495 B80F4800     jmp     dword ptr [edx*4+0x480FB8]                        ;  ed6_win_.00480F63
        */
        ['00 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 01 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 04 02 03', 0x62, [0x04, 0x04]],
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
        function(buffer: NativePointer, datIndex: number, datOffset: number, fileSize: number): number {
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

            return LoadFileFromDAT(buffer, datIndex, datOffset, fileSize);
        },
        'int32', ['pointer', 'uint32', 'uint32', 'uint32'],
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
        asciiRenderer[index] = new DWriteRenderer(fontSize, undefined, 'SIMHEI');
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
        function(thiz: NativePointer, buffer: NativePointer, stride: number, text: NativePointer, colorIndex: number): NativePointer {
            const s = utils.readMBCS(text, TextEncoding, text.readU8() >= 0x80 ? 2 : 1);
            return GetGlyphsBitmap(s, text, buffer, stride * 2, colorIndex);
        },
        'pointer', ['pointer', 'pointer', 'uint32', 'pointer', 'uint32'],
        'thiscall',
    );
}

export function main() {
    console.log('patchModuleText');
    utils.patchModuleText(Modules.ED6FC, ExeText);

    console.log('bypassSteam');
    hookSteamAndMisc();

    console.log('hookEncodingCheck');
    hookEncodingCheck();

    console.log('hookWindow');
    hookWindow();

    console.log('hookFileIo');
    hookFileIo();

    console.log('hookTextRenderer');
    hookTextRenderer();
}
