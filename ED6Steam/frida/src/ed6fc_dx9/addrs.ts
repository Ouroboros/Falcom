import { Modules } from "../modules";

export const Addrs = {
    ED6FC: {
        DirCacheTable       : Modules.ED6FC.base.add(0x39B010),         // ED6_DT%02x.dir
        SEVolumeTable       : Modules.ED6FC.base.add(0x13B670),
        SEVolumeIndex       : Modules.ED6FC.base.add(0x158D1C),

        FontSizeIndex       : Modules.ED6FC.base.add(0x141E094),
        JPFontSizeLimit     : Modules.ED6FC.base.add(0x0B37CB),         // font192._da
        GetTextWidth        : Modules.ED6FC.base.add(0x0AEF0A),         // set ascii width to fontSize / 2, ED6_GetTextWidth -> ED6_DrawText
        AsciiCharWidth      : Modules.ED6FC.base.add(0x13B958),         // 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 0A 00 00 00 06 00 00 00 08 00 00 00 0C 00 00 00 0B 00 00 00 0F 00 00 00 0D 00 00 00 05 00 00 00 08 00 00 00 07 00 00 00 09 00 00 00 0C 00 00 00 06 00 00 00 08 00 00 00 06 00 00 00 09 00 00 00 0B 00 00 00 09 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 06 00 00 00 06 00 00 00 0B 00 00 00 0C 00 00 00 0B 00 00 00 0A 00 00 00 10 00 00 00 0D 00 00 00 0C 00 00 00 0D 00 00 00 0D 00 00 00 0C 00 00 00 0B 00 00 00 0D 00 00 00 0D 00 00 00 07 00 00 00 09 00 00 00 0D 00 00 00 0B 00 00 00 10 00 00 00 0D 00 00 00 0E 00 00 00 0C 00 00 00 0E 00 00 00 0C 00 00 00 0B 00 00 00 0C 00 00 00 0D 00 00 00 0D 00 00 00 10 00 00 00 0C 00 00 00 0C 00 00 00 0C 00 00 00 08 00 00 00 09 00 00 00 07 00 00 00 0B 00 00 00 0C 00 00 00 07 00 00 00 0A 00 00 00 0B 00 00 00 0A 00 00 00 0B 00 00 00 0A 00 00 00 09 00 00 00 0B 00 00 00 0B 00 00 00 06 00 00 00 06 00 00 00 0B 00 00 00 06 00 00 00 0F 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 09 00 00 00 09 00 00 00 07 00 00 00 0B 00 00 00 0B 00 00 00 0E 00 00 00 0A 00 00 00 0A 00 00 00 09 00 00 00 08 00 00 00 07 00 00 00 08 00 00 00 0C 00 00 00 0A 00 00 00
        AsciiFontSizeScale  : Modules.ED6FC.base.add(0x146998),

        ExceptionHandler    : Modules.ED6FC.base.add(0x0B6B20),
        LoadFileFromDAT     : Modules.ED6FC.base.add(0x077180),         // ED6_DT%02x.DAT
        GetGlyphsBitmap     : Modules.ED6FC.base.add(0x0AF0A0),         // cmp     dword ptr [0x185E388], 0x2BC
        DrawTalkText        : Modules.ED6FC.base.add(0x0DEF80),         // 04 04 04 04 02 03
    },

    IAT: {
        SetWindowPos        : Modules.ED6FC.base.add(0x12C238),
        CreateFileW         : Modules.ED6FC.base.add(0x12C074),
    },
};
