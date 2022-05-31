import { Modules } from "../modules";

export const Addrs = {
    ED6SC: {
        DirCacheTable       : Modules.ED6SC.base.add(0x03FA730),        // ED6_DT%02x.dir
        SEVolumeTable       : Modules.ED6SC.base.add(0x192260),         // 0FFFFF254h 0FFFFF574h
        SEVolumeIndex       : Modules.ED6SC.base.add(0x1BB460),         // scena_op_24
        DirectSound         : Modules.ED6SC.base.add(0x406AAC),

        FontSizeIndex       : Modules.ED6SC.base.add(0x2AF8C44),
        JPFontSizeLimit     : Modules.ED6SC.base.add(0x0FC20B),         // font192._da
        GetTextWidth        : Modules.ED6SC.base.add(0x0F68C9),         // set ascii width to fontSize / 2, ED6_GetTextWidth -> ED6_DrawText
        AsciiCharWidth      : Modules.ED6SC.base.add(0x192548),         // 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 10 00 00 00 0A 00 00 00 06 00 00 00 08 00 00 00 0C 00 00 00 0B 00 00 00 0F 00 00 00 0D 00 00 00 05 00 00 00 08 00 00 00 07 00 00 00 09 00 00 00 0C 00 00 00 06 00 00 00 08 00 00 00 06 00 00 00 09 00 00 00 0B 00 00 00 09 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 06 00 00 00 06 00 00 00 0B 00 00 00 0C 00 00 00 0B 00 00 00 0A 00 00 00 10 00 00 00 0D 00 00 00 0C 00 00 00 0D 00 00 00 0D 00 00 00 0C 00 00 00 0B 00 00 00 0D 00 00 00 0D 00 00 00 07 00 00 00 09 00 00 00 0D 00 00 00 0B 00 00 00 10 00 00 00 0D 00 00 00 0E 00 00 00 0C 00 00 00 0E 00 00 00 0C 00 00 00 0B 00 00 00 0C 00 00 00 0D 00 00 00 0D 00 00 00 10 00 00 00 0C 00 00 00 0C 00 00 00 0C 00 00 00 08 00 00 00 09 00 00 00 07 00 00 00 0B 00 00 00 0C 00 00 00 07 00 00 00 0A 00 00 00 0B 00 00 00 0A 00 00 00 0B 00 00 00 0A 00 00 00 09 00 00 00 0B 00 00 00 0B 00 00 00 06 00 00 00 06 00 00 00 0B 00 00 00 06 00 00 00 0F 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 0B 00 00 00 09 00 00 00 09 00 00 00 07 00 00 00 0B 00 00 00 0B 00 00 00 0E 00 00 00 0A 00 00 00 0A 00 00 00 09 00 00 00 08 00 00 00 07 00 00 00 08 00 00 00 0C 00 00 00 0A 00 00 00
        AsciiFontSizeScale  : Modules.ED6SC.base.add(0x1A52A4),         // GetGlyphsBitmap

        LoadFileFromDAT     : Modules.ED6SC.base.add(0x097210),         // ED6_DT%02x.DAT
        GetGlyphsBitmap     : Modules.ED6SC.base.add(0x0F6A60),         // cmp     dword ptr [0x2EF8C48], 0x2BC
        DrawTalkText        : Modules.ED6SC.base.add(0x12CCE0),         // 04 04 04 04 02 03
        ShowTalkText        : Modules.ED6SC.base.add(0x12F4E0),
    },

    IAT: {
        SetWindowPos        : Modules.ED6SC.base.add(0x181238),
        CreateFileW         : Modules.ED6SC.base.add(0x181074),
    },
};
