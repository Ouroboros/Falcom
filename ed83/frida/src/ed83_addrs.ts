import { Modules } from "./modules";

export const Addrs = {
    BlowFish_Decode                     : Modules.ED83.base.add(0x20CAA0),
    Logger_Output                       : Modules.ED83.base.add(0x11D160),

    // patch
    DLC_Check                           : Modules.ED83.base.add(0x3A8359),
    File_Open                           : Modules.ED83.base.add(0x0F5920),
    LoadTableData                       : Modules.ED83.base.add(0x2817F0),
    ScriptLoad                          : Modules.ED83.base.add(0x3C91B0),
    ScriptVMExecute                     : Modules.ED83.base.add(0x3C6DA0),
    ScriptGetFunctionByName             : Modules.ED83.base.add(0x3C7FF0),
    GetFileSize                         : Modules.ED83.base.add(0x134400),

    // api

    ED83: {
        sharedInstance                      : Modules.ED83.base.add(0xC4B3E0),
        findNameTableDataByModel            : Modules.ED83.base.add(0x27F560),
        findNameTableDataByChrId            : Modules.ED83.base.add(0x27F440),
        findPartyCharByChrId                : Modules.ED83.base.add(0x2C2F80),
    },

    // hook

    CharacterManager: {
        CreatePartyCharacters_stricmp   : Modules.ED83.base.add(0x2CAA52),
        // CallReleaseCharacter            : Modules.ED83.base.add(0x2CA925),
        // ReleaseCharacter                : Modules.ED83.base.add(0x2CA360),
    },

    Character: {
        ChangeSkinFinished              : Modules.ED83.base.add(0x255FBA),
        LoadCharaAniByFieldInit         : Modules.ED83.base.add(0x2CAB82),

        // constructor                     : Modules.ED83.base.add(0x24CE60),
        // GetAssetFromAttachTable         : Modules.ED83.base.add(0x25CA40),
        Initialize                      : Modules.ED83.base.add(0x258990),
        InitAnimeClipTable              : Modules.ED83.base.add(0x254380),
        GetModelFromAttach              : Modules.ED83.base.add(0x25CA40),
        LoadAni                         : Modules.ED83.base.add(0x25D590),
        SetFace                         : Modules.ED83.base.add(0x25D880),
    },

    BattleCharacter: {
        IsChrNPC                        : Modules.ED83.base.add(0x15A1C0),
        InitNpcCraftAI                  : Modules.ED83.base.add(0x15C2C0),
        InitEquipAndOrbs                : Modules.ED83.base.add(0x159D70),
        InitPartyCraft                  : Modules.ED83.base.add(0x15C290),
        InitMagic                       : Modules.ED83.base.add(0x15C260),
    },

    BattleAITable: {
        GetCraftByID                    : Modules.ED83.base.add(0x13E900),
    },

    Asset: {
        LoadAsset                       : Modules.ED83.base.add(0x0E0320),
        HashSymbol                      : Modules.ED83.base.add(0x52E1F0),
    },

    BattleProc: {
        SetupBattle_FormatAlgoScript    : Modules.ED83.base.add(0x1A8362),
        SetupBattle_FormatAlgoScript2   : Modules.ED83.base.add(0x2A6790),
        SetupBattle_InitPartyCraft      : Modules.ED83.base.add(0x1A8563),
        SetupBattle_InitCraft           : Modules.ED83.base.add(0x1A8535),
        SetupBattle_InitCraftEnd        : Modules.ED83.base.add(0x1A85B2),
    },
};

export const Offsets = {
    ED83: {
        t_name              : 0x20D9C0,
        CharacterManager    : 0x1CF0,
        CraftList           : 0x359AB8,
        MagicList           : 0x35A0B8,
        SBreakList          : 0x35AE98,
        BattleStyleList     : 0x35AE38,
    },

    ScriptLoader: {
        vtbl        : {
            init    : 0x08,
        },

        IsDisable   : 0x009,
        Name        : 0x014,
        NameSize    : 0x01F,
        Type        : 0x6B4,
        Buffer      : 0x6B8,
        BufferBase  : 0x6C0,
    },

    TableLoader: {
        vtbl        : {
            init    : 0x08,
        },

        Buffer      : 0x08,
    },

    Character: {
        vtbl        : {
            init    : 0x08,
        },

        Model               : 0xA8,
        Name                : 0x6F8,
        FaceModel           : 0x768,
        PresetFaceModel     : 0x780,
        ChrID               : 0x7D8,
        faceTexture         : 0x868,
        ModelChrId          : 0x1A34,
    },

    BattleCharacter: {
        vtbl        : {
            init    : 0x08,
        },

        BattleProc      : 0x08,
        Character       : 0x10,
        SBreakCraftID   : 0x1AA,
        battleChrId     : 0xE8E,
    },
};
