import { Modules } from "../modules";

export const Addrs = {
    // api

    ED6FC: {
        SharedInstance  : NULL,

        DirCacheTable   : Modules.ED6FC.base.add(0x1D5D50),         // ED6_DT%02x.dir
        FontSizeIndex   : Modules.ED6FC.base.add(0x145e384),
        JPFontSizeLimit : Modules.ED6FC.base.add(0x0D6FA4),         // font192._da

        LoadFileFromDAT : Modules.ED6FC.base.add(0x062090),         // ED6_DT%02x.DAT
        DecompressData  : Modules.ED6FC.base.add(0x064FC0),
        GetGlyphsBitmap : Modules.ED6FC.base.add(0x0B1D90),         // 8B 55 14 83 EC 34 83 FA 13
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
        CheckAchievements   : Modules.ED6FC.base.add(0x0DD160),
        CheckAchievements2  : Modules.ED6FC.base.add(0x0DE4C0),
        RunCallbacks        : Modules.ED6FC.base.add(0x0B8F15),
    },
};

export const Offsets = {
    ED6FC: {
        t_name              : 0x20D9C0,
        CharacterManager    : 0x1CF0,
        CraftList           : 0x359AB8,
        MagicList           : 0x35A0B8,
        SBreakList          : 0x35AE98,
        BattleStyleList     : 0x35AE38,
    },
};
