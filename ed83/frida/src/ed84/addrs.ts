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
                HandleActMenu                           : Modules.ED84.base.add(0x2CE060),

                Crc32CheckSum                           : Modules.ED84.base.add(0x09C000),

                SaveDataChecksum                        : Modules.ED84.base.add(0x3E4DD0),

                File: {
                    Open                                : Modules.ED84.base.add(0x0ED240),
                    GetSize                             : Modules.ED84.base.add(0x0ED190),
                },

                ED84: {
                    SharedInstance                      : Modules.ED84.base.add(0xD099B8),
                    FindNameTableDataByModel            : Modules.ED84.base.add(0x257840),
                    FindNameTableDataByChrId            : Modules.ED84.base.add(0x2576E0),
                    FindPartyCharByChrId                : Modules.ED84.base.add(0x29EA40),
                },

                Script: {
                    Load                                : Modules.ED84.base.add(0x3EB010),
                    Call                                : Modules.ED84.base.add(0x432D50),
                },

                ScriptManager: {
                    LoadLibraries                       : Modules.ED84.base.add(0x2A3410),
                    // CreatePartyCharacters_stricmp       : Modules.ED84.base.add(0),
                    GetScriptByID                       : Modules.ED84.base.add(0x3E7D40),
                },

                Character: {
                    // ChangeSkinFinished                  : Modules.ED84.base.add(0),
                    // LoadCharaAniByFieldInit             : Modules.ED84.base.add(0),
                    // LoadCharaAniByCreateBattleCharacter : Modules.ED84.base.add(0),

                    Initialize                          : Modules.ED84.base.add(0x22F290),
                    LoadFaceModel                       : Modules.ED84.base.add(0x22A530),
                    LoadAni                             : Modules.ED84.base.add(0x233DB0),
                },

                BattleCharacter: {
                    IsChrNPC                            : Modules.ED84.base.add(0x117090),
                    InitNpcCraftAI                      : Modules.ED84.base.add(0x1196B0),
                    InitEquipAndOrbs                    : Modules.ED84.base.add(0x116BB0),
                    InitPartyCraft                      : Modules.ED84.base.add(0x119680),
                    InitMagic                           : Modules.ED84.base.add(0x119650),
                    FormatBattleSymbol                  : Modules.ED84.base.add(0x10DC10),
                },

                BattleInfoTable: {
                    GetCraftByID                        : Modules.ED84.base.add(0x0F98F0),
                },

                BattleProc: {
                    SetupBattle_FormatAlgoScript        : Modules.ED84.base.add(0x15ABAB),
                    SetupBattle_InitCraft               : Modules.ED84.base.add(0x15AE7F),
                    SetupBattle_InitCraftEnd            : Modules.ED84.base.add(0x15AEF3),
                },

                Asset: {
                    LoadAsset                           : Modules.ED84.base.add(0x098470),
                    // HashSymbol                          : Modules.ED84.base.add(0x0973D0),
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
                    ScriptManager       : 0x1CB8,
                    CraftList           : 0x9AEB00,
                    MagicList           : 0x9AF300,
                    SBreakList          : 0x9B0580,
                    BattleStyleList     : 0x9B0500,
                },

                ScriptManager: {
                    ThreadContext       : 0x18928,
                    SizeOfThreadContext : 0x568,

                    Scripts: {
                        common          : 0x1D9A8,
                        system2         : 0x1E6E0,
                        system3         : 0x1F418,
                        system4         : 0x20150,
                        btlsys          : 0x20E88,
                        btlwin          : 0x22128,
                        debug           : 0x233C8,
                        btlcom          : 0x24100,
                        sound           : 0x253A0,
                        tk_common       : 0x260D8,
                    },
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
                    BattleProc      : 0x08,
                    Character       : 0x10,
                    SBreakCraftID   : 0x202,
                    BattleInfoTable : 0x480,
                    BattleChrId     : 0xF06,
                },

                BattleInfoTable: {
                    AlgoTable       : 0x08,
                    ActionTable     : 0x18,
                    BattleCharacter : 0x60,
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