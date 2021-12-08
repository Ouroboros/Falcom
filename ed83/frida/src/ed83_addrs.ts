import { Modules } from "./modules";

export const Addrs = {
    BlowFish_Decode         : Modules.ED83.base.add(0x20CAA0),
    Logger_Output           : Modules.ED83.base.add(0x11D160),

    // patch
    DLC_Check               : Modules.ED83.base.add(0x3A8359),
    File_Open               : Modules.ED83.base.add(0xF5920),
    LoadTableData           : Modules.ED83.base.add(0x2817F0),
    ScriptLoad              : Modules.ED83.base.add(0x3C91B0),
    ScriptVMExecute         : Modules.ED83.base.add(0x3C6DA0),
    ScriptGetFunctionByName : Modules.ED83.base.add(0x3C7FF0),

    // api
    gED83                   : Modules.ED83.base.add(0xC4B3E0),
    findNameTableDataByModel: Modules.ED83.base.add(0x27F560),

    // hook

    Character: {
        ChangeSkinFinished  : Modules.ED83.base.add(0x255F8F),
        loadAni             : Modules.ED83.base.add(0x25D590),
    },
};

export const Offsets = {
    ED83: {
        t_name      : 0x20D9C0,
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

        Model       : 0xA8,
        Name        : 0x6F8,
        ChrID       : 0x7D8,
    },
};
