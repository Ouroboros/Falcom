import { Modules } from "../modules";

export const Addrs = {
    ED6FC: {
        SharedInstance  : NULL,

        DirCacheTable   : Modules.ED6FC.base.add(0x1D5D50),         // ED6_DT%02x.dir

        FontSizeIndex   : Modules.ED6FC.base.add(0x145e384),
        JPFontSizeLimit : Modules.ED6FC.base.add(0x0D6FA4),         // font192._da
        GetTextWidth    : Modules.ED6FC.base.add(0x0B1D0A),         // set ascii width to fontSize / 2, ED6_GetTextWidth -> ED6_DrawText

        LoadFileFromDAT : Modules.ED6FC.base.add(0x062090),         // ED6_DT%02x.DAT
        DecompressData  : Modules.ED6FC.base.add(0x064FC0),
        GetGlyphsBitmap : Modules.ED6FC.base.add(0x0B1D90),         // cmp     dword ptr [0x185E388], 0x2BC
        DrawTalkText    : Modules.ED6FC.base.add(0x0809B0),         // 8B E9 0F B6 08 C1 E1 08 0B CA 81 F9 40 81 00 00
        DrawDialogText  : Modules.ED6FC.base.add(0x080A00),         // 8B F8 80 FB 20
    },

    IAT: {
        SetWindowPos    : Modules.ED6FC.base.add(0x14624C),
    },

    Steam: {
        Init                : Modules.ED6FC.base.add(0x0B85F5),
        InitLang            : Modules.ED6FC.base.add(0x0B868A),
        CheckCloudSave      : Modules.ED6FC.base.add(0x07A91A),
        CheckCloudSave2     : Modules.ED6FC.base.add(0x07B371),
        CheckCloudSave3     : Modules.ED6FC.base.add(0x06441B),
        CheckCloudSave4     : Modules.ED6FC.base.add(0x0646BD),
        CheckAchievements   : Modules.ED6FC.base.add(0x0DD160),     // SteamInternal_ContextInit
        CheckAchievements2  : Modules.ED6FC.base.add(0x0DE4C0),
        CheckAchievements3  : Modules.ED6FC.base.add(0x0DE3D0),
        CheckAchievements4  : Modules.ED6FC.base.add(0x0DEAC0),
        CheckAchievements5  : Modules.ED6FC.base.add(0x0DCCF0),
        CheckAchievements6  : Modules.ED6FC.base.add(0x0DCDE0),
        CheckAchievements7  : Modules.ED6FC.base.add(0x0DCE60),
        CheckAchievements8  : Modules.ED6FC.base.add(0x0DE680),
        CheckAchievements9  : Modules.ED6FC.base.add(0x0DE6C0),
        CheckAchievements10 : Modules.ED6FC.base.add(0x0DE8B0),
        CheckAchievements11 : Modules.ED6FC.base.add(0x0DEE80),
        CheckAchievements12 : Modules.ED6FC.base.add(0x0DEF80),
        CheckAchievements13 : Modules.ED6FC.base.add(0x0DF150),
        CheckAchievements14 : Modules.ED6FC.base.add(0x0DF290),
        CheckAchievements15 : Modules.ED6FC.base.add(0x0DF340),
        CheckAchievements16 : Modules.ED6FC.base.add(0x0DF380),
        CheckAchievements17 : Modules.ED6FC.base.add(0x0DF3C0),
        CheckAchievements18 : Modules.ED6FC.base.add(0x0DF400),
        RunCallbacks        : Modules.ED6FC.base.add(0x0B8F15),
    },
};

export const Offsets = {
    ED6FC: {
    },
};
