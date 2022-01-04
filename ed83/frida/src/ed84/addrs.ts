import * as utils from "../utils";
import { Modules } from "../modules";

export const Addrs = (function() {
    // switch (utils.getGameVersion()) {
    //     case 'ed84_jp':
            return {
                AllocObject                             : Modules.ED84.base.add(0x4DAAC0),
                AllocMemory                             : Modules.ED84.base.add(0x52E940),
                FreeMemory                              : Modules.ED84.base.add(0x52E920),
                Logger_Output                           : Modules.ED84.base.add(0x0D6520),
                Logger_Ansi2UTF8                        : Modules.ED84.base.add(0x0D4FF0),

                Crc32CheckSum                           : Modules.ED84.base.add(0x09C000),

                SaveDataChecksum                        : Modules.ED84.base.add(0x3E4DD0),

                File: {
                    Open                                : Modules.ED84.base.add(0x0ED240),
                    GetSize                             : Modules.ED84.base.add(0x0ED190),
                },

                ED84: {
                    sharedInstance                      : Modules.ED84.base.add(0xD099B8),
                    findNameTableDataByModel            : Modules.ED84.base.add(0x257840),
                    findNameTableDataByChrId            : Modules.ED84.base.add(0x2576E0),
                    findPartyCharByChrId                : Modules.ED84.base.add(0x29EA40),
                },

                Character: {
                    ChangeSkinFinished                  : Modules.ED84.base.add(0),
                    LoadCharaAniByFieldInit             : Modules.ED84.base.add(0),
                    LoadCharaAniByCreateBattleCharacter : Modules.ED84.base.add(0),

                    Initialize                          : Modules.ED84.base.add(0x22F290),
                    LoadFaceModel                       : Modules.ED84.base.add(0x22A530),
                    LoadAni                             : Modules.ED84.base.add(0x233DB0),
                },

                Asset: {
                    LoadAsset                           : Modules.ED83.base.add(0x098470),
                    HashSymbol                          : Modules.ED83.base.add(0x0973D0),
                },
            };

        // case 'ed84_us':
        // default:
        //     return {
        //         File_Open   : Modules.ED84.base.add(0),
        //         AllocObject : Modules.ED84.base.add(0),
        //         AllocMemory : Modules.ED84.base.add(0),
        //         FreeMemory  : Modules.ED84.base.add(0),

        //         SaveDataChecksum: Modules.ED84.base.add(0x3E7080),
        //     };
    // }
})();


export const Offsets = (function() {
    // switch (utils.getGameVersion()) {
    //     case 'ed84_jp':
            return {
                ED84: {
                    t_name              : 0x83B248,
                    CharacterManager    : 0x1CB8,
                    CraftList           : 0x9AEB00,
                    MagicList           : 0x9AF300,
                    SBreakList          : 0x9B0580,
                    BattleStyleList     : 0x9B0500,
                },

                ScriptLoader: {
                },

                TableLoader: {
                },

                Character: {
                    Model               : 0xB0,
                    Name                : 0x7A0,
                    FaceModel           : 0x860,
                    PresetFaceModel     : 0x878,
                    ChrID               : 0x900,
                    // faceTexture         : 0x0,
                    ModelChrId          : 0x2174,
                },

                BattleCharacter: {
                },

                BattleInfoTable: {
                },
            };

        // case 'ed84_us':
        // default:
        //     return {
        //         File_Open   : Modules.ED84.base.add(0),
        //         AllocObject : Modules.ED84.base.add(0),
        //         AllocMemory : Modules.ED84.base.add(0),
        //         FreeMemory  : Modules.ED84.base.add(0),

        //         SaveDataChecksum: Modules.ED84.base.add(0x3E7080),
        //     };
    // }
})();