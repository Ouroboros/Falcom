import { sprintf } from "sprintf-js";
import * as utils from "./utils";
import { Interceptor2 } from "./utils";
import { Addrs } from "./ed83_addrs";
import {
    ED83,
    MinCustomChrId,
    InvalidChrId,
    Character,
    BattleCharacter,
    AnimeClipObject,
    MaxPartyChrId,
    NameTableData,
    BattleAITable,
} from "./ed83_types";

function findReplacedNameData(char: Character): NameTableData | null {
    return ED83.findNameTableDataByChrId(char.modelChrId);
}

function hookCharacterModelInit() {
    const InitAnimeClipTable = Interceptor2.jmp(
        Addrs.Character.InitAnimeClipTable,
        function(chr: NativePointer, animeclip: NativePointer) {
            const char = new Character(chr);
            const nameData = findReplacedNameData(char);

            if (nameData) {
                const faceModel = nameData.faceModel;
                if (faceModel != 'null') {
                    char.presetFaceModel = faceModel;
                }
            }

            InitAnimeClipTable(chr, animeclip);
        },
        'void', ['pointer', 'pointer'],
    );

    Interceptor2.call(
        Addrs.Character.ChangeSkinFinished,
        function(chr: NativePointer, animeclip: NativePointer) {
            const char = new Character(chr);
            const nameData = findReplacedNameData(char);

            if (!nameData) {
                InitAnimeClipTable(chr, animeclip);
                return;
            }

            char.loadAni(nameData.ani);
        },
        'void', ['pointer', 'pointer'],
    );

    Interceptor2.call(
        Addrs.Character.LoadCharaAniByFieldInit,
        function(chr: NativePointer, ani: NativePointer, autoCompile: number) {
            const char = new Character(chr);
            const nameData = findReplacedNameData(char);
            char.loadAni(nameData ? nameData.ani : ani.readUtf8String()!);
        },
        'void', ['pointer', 'pointer', 'uint32'],
    );

    const Character_Initialize = Interceptor2.jmp(
        Addrs.Character.Initialize,
        function(
            chr:    NativePointer,
            model:  NativePointer,
            name:   NativePointer,
            a4:     NativePointer,
            a5:     NativePointer,
            a6:     NativePointer,
            a7:     NativePointer,
            a8:     NativePointer,
            a9:     NativePointer,
            a10:     NativePointer,
            a11:     NativePointer,
            a12:     NativePointer,
            a13:     NativePointer,
            a14:     NativePointer,
        ): NativePointer {

            const char = new Character(chr);
            const chrId = ED83.getBattleStyle(char.chrId);

            // utils.log(`createChara a7 : 0x${a7.toUInt32().toString(16)}`);
            // utils.log(`createChara a8 : 0x${a8.toUInt32().toString(16)}`);
            // utils.log(`createChara a9 : 0x${a9.and(0xFF).toUInt32().toString(16)}`);
            // utils.log(`createChara a10: 0x${a10.and(0xFF).toUInt32().toString(16)}`);
            // utils.log(`createChara a11: 0x${a11.toUInt32().toString(16)}`);
            // utils.log(`createChara a12: 0x${a12.toUInt32().toString(16)}`);
            // utils.log(`createChara a13: 0x${a13.and(0xFF).toUInt32().toString(16)}`);

            const modifyModel = (function() {
                const args = [
                    a7.toUInt32(),
                    a8.toUInt32(),
                    a9.toUInt32() & 0xFF,
                    a10.toUInt32() & 0xFF,
                    a11.toUInt32(),
                    a12.toUInt32(),
                    a13.toUInt32() & 0xFF,
                ];

                const patterns = [
                    [
                        // field init
                        0x3fcccccd,
                        0x3ef5c28f,
                        0x1,
                        0x1,
                        0x3,
                        0x8,
                        0x0,
                    ],
                    [
                        // after image, dummy
                        0x0,
                        0x0,
                        0x0,
                        0x1,
                        0x3,
                        0x8,
                        0x0,
                    ],
                ];

                function arrayEquals(a1: any, a2: any): boolean {
                    if (a1.length != a2.length)
                        return false;

                    for (let i = 0; i != a1.length; i++) {
                        if (a1[i] != a2[i])
                            return false;
                    }

                    return true;
                }

                for (let p of patterns) {
                    if (arrayEquals(p, args))
                        return true;
                }

                return false;
            })();

            if (chrId >= MinCustomChrId && char.modelChrId == InvalidChrId && modifyModel) {
                char.modelChrId = chrId;
                const nameData = findReplacedNameData(char);
                if (nameData)
                    model = Memory.allocUtf8String(nameData.model);
            }

            return Character_Initialize(chr, model, name, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer'],
    );

    Interceptor2.call(
        Addrs.CharacterManager.CreatePartyCharacters_stricmp,
        function(scriptName: NativePointer, aniName: NativePointer): number {
            const ctx = (this.context as X64CpuContext);
            const char = new Character(ctx.r15);

            if (char.isReplaced()) {
                return 0;
            }

            return scriptName.readUtf8String()!.toLowerCase() == aniName.readUtf8String()!.toLowerCase() ? 0 : 1;
        },
        'uint32', ['pointer', 'pointer'],
    );

    // asset redirect

    const AssetSymbolMap: any = {
        'C_CHR500'  : 'C_CHR033',
        'I_BTLSC500': 'I_BTLSC033',
        'C_CHR501'  : 'C_CHR032',
        'I_BTLSC501': 'I_BTLSC032',
    };

    const AssetLoadMap = AssetSymbolMap;

    const LoadAsset = Interceptor2.jmp(
        Addrs.Asset.LoadAsset,
        function(a1: NativePointer, symbol: NativePointer, size: NativePointer, a4: NativePointer, a5: NativePointer): NativePointer {
            const s = symbol.readUtf8String()!;

            const s2 = AssetLoadMap[s];
            if (s2) {
                symbol = Memory.allocUtf8String(s2);
            }

            return LoadAsset(a1, symbol, size, a4, a5);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer'],
    );

    const AssetHashSymbol = Interceptor2.jmp(
        Addrs.Asset.HashSymbol,
        function(symbol: NativePointer): NativePointer {
            const s = symbol.readUtf8String()!;

            const s2 = AssetSymbolMap[s];
            if (s2) {
                symbol = Memory.allocUtf8String(s2);
            }

            return AssetHashSymbol(symbol);
        },
        'pointer', ['pointer'],
    );
}

function hookBattle() {
    Interceptor2.call(
        Addrs.BattleProc.SetupBattle_FormatAlgoScript,
        function(buffer: NativePointer, size: number, fmt: NativePointer, battleAni: NativePointer) {
            const ctx = (this.context as X64CpuContext);
            const chrId = ctx.r14.toUInt32() & 0xFFFF;

            let path = (function() {
                const char = ED83.findCharByChrId(chrId);

                if (!char)
                    return '';

                const nameData = findReplacedNameData(char);

                if (!nameData)
                    return '';

                if (char.isReplaced(nameData) == false)
                    return '';

                const algo = sprintf(fmt.readAnsiString()!, nameData.ani);
                if (!utils.getPatchFile(algo))
                    return '';

                return algo;
            })()

            if (!path)
                path = sprintf(fmt.readAnsiString()!, battleAni.readUtf8String()!);

            buffer.writeAnsiString(path.slice(0, size));
        },
        'void', ['pointer', 'uint32', 'pointer', 'pointer'],
    );

    const GetEncryptScriptPath = Interceptor2.jmp(
        Addrs.BattleProc.SetupBattle_FormatAlgoScript2,
        function(output: NativePointer, input: NativePointer) {
            const infile = input.readAnsiString()!;

            if (utils.getPatchFile(infile)) {
                output.writeAnsiString(infile);
            } else {
                GetEncryptScriptPath(output, input);
            }
        },
        'void', ['pointer', 'pointer'],
    );

    Interceptor2.call(
        Addrs.BattleProc.SetupBattle_InitCraft,
        function() {
            const ctx = (this.context as X64CpuContext);
            const chrId = ctx.r14.toUInt32() & 0xFFFF;
            const battleChar = new BattleCharacter(ctx.rcx);

            if (chrId >= MaxPartyChrId) {
                if (battleChar.isChrNPC()) {
                    battleChar.initNpcCraftAI(false);
                }
            } else {
                const replaced = battleChar.character.isReplaced();

                battleChar.initEquipAndOrbs(chrId);
                battleChar.initMagic(chrId);
                replaced ? battleChar.initNpcCraftAI(false) : battleChar.initPartyCraft(chrId);

                if (replaced) {
                    const actionTable = battleChar.battleAITable.actionTable;
                    if (actionTable.pointer.isNull())
                        return;

                    for (let i = 0, n = actionTable.size; i != n; i++) {
                        const craft = actionTable.getCraft(i);
                        if (craft.type != 0x1F)
                            continue;

                        battleChar.sbreakCraftID = craft.craftId;
                    }
                } else {
                    battleChar.sbreakCraftID = ED83.getSBreak(chrId).readU16();
                }

            }
        },
        'void', [],
    );

    Memory.patchCode(Addrs.BattleProc.SetupBattle_InitCraft.add(5), 2, (code) => {
        code.writeU8(0xEB);
        code.add(1).writeU8(Addrs.BattleProc.SetupBattle_InitCraftEnd.sub(Addrs.BattleProc.SetupBattle_InitCraft).sub(5 + 2).toUInt32());
    });

    const BattleAITable_GetCraftByID = Interceptor2.jmp(
        Addrs.BattleAITable.GetCraftByID,
        function(tables: NativePointer, craftId: number): NativePointer {
            const tbl = new BattleAITable(tables);
            const char = tbl.battleCharacter;

            if (char.character.isReplaced() == false) {
                return BattleAITable_GetCraftByID(tables, craftId);
            }

            switch (craftId) {
                case 0:     // regular attack
                {
                    const actionTable = tbl.actionTable;
                    for (let i = 0, n = actionTable.size; i != n; i++) {
                        const craft = actionTable.getCraft(i);
                        if (craft.type != 1)
                            continue;

                        return craft.pointer;
                    }
                    break;
                }

                case 1:     // move
                {
                    const actionTable = tbl.actionTable;
                    for (let i = 0, n = actionTable.size; i != n; i++) {
                        const craft = actionTable.getCraft(i);
                        if (craft.type != 3)
                            continue;

                        return craft.pointer;
                    }

                    break;
                }
            }

            return BattleAITable_GetCraftByID(tables, craftId);

        }, 'pointer', ['pointer', 'uint16'],
    );

    return;

    const recorded: any = {};

    const AnimeClipObject_GetStartTimeEndTime = Interceptor2.jmp(
        Addrs.AnimeClipObject.GetStartTimeEndTime,
        function(obj: NativePointer, startTime: NativePointer, endTime: NativePointer): number {
            const ret = AnimeClipObject_GetStartTimeEndTime(obj, startTime, endTime);

            if (ret == 0) {
                const clip = new AnimeClipObject(obj);
                const name = clip.name;

                if (!recorded[name]) {
                    recorded[name] = true;
                    utils.log(`anime clip ${clip.name} ${startTime.readFloat()} ~ ${endTime.readFloat()}`);
                }
            }

            return ret;
        },
        'uint32', ['pointer', 'pointer', 'pointer'],
    );
}

function hookFileRedirection() {
    const ScriptLoad = Interceptor2.jmp(
        Addrs.ScriptLoad,
        function(script: NativePointer, path: NativePointer, scriptType: NativePointer, stopIfNotExists: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readAnsiString()!);
            if (patch) {
                const tls = utils.getTLS();
                tls.patchFileName = patch;
                tls.disableDecrypt = true;

                const ret = ScriptLoad(script, path, scriptType, stopIfNotExists);

                tls.disableDecrypt = false;
                tls.patchFileName = '';

                return ret;
            }

            return ScriptLoad(script, path, scriptType, stopIfNotExists);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer'],
    )

    Interceptor.attach(Addrs.LoadTableData, {
        onEnter: function(args) {
            const self      = args[0];
            const path      = args[1].readAnsiString()!;
            const nodat     = args[2].toInt32() != 0;
            const fullpath  = args[3].toInt32() != 0;

            let p = path;

            if (fullpath == false) {
                if (nodat) {
                    p = `data/text/${path}.tbl`;
                } else {
                    p = `data/text/dat/${path}.tbl`;
                }
            }

            const patch = utils.getPatchFile(p)
            if (!patch)
                return;

            this.path = Memory.allocUtf8String(patch);

            const tls = utils.getTLS();

            tls.disableDecrypt = true;
            tls.patchFileName = patch;
        },
        onLeave: function(retval) {
            const tls = utils.getTLS();
            tls.disableDecrypt = false;
            tls.patchFileName = '';
        }
    });

    Interceptor.attach(Addrs.BlowFish_Decode, {
        onEnter: function(args) {
            if (utils.getTLS().disableDecrypt) {
                args[2] = NULL;     // size
            }
        },
    });

    Interceptor.attach(Addrs.File_Open, {
        onEnter: function(args) {
            const patch = utils.getTLS().patchFileName;
            if (patch) {
                this.path = Memory.allocAnsiString(patch);
                args[1] = this.path;
            } else {
                const patch = utils.getPatchFile(args[1].readAnsiString()!);
                if (patch) {
                    this.patch = Memory.allocAnsiString(patch);
                    args[1] = this.patch;
                }
            }
        },
    });

    Interceptor.attach(Addrs.GetFileSize, {
        onEnter: function(args) {
            const patch = utils.getPatchFile(args[1].readAnsiString()!);
            if (patch) {
                this.patch = Memory.allocAnsiString(patch);
                args[1] = this.patch;
            }
        },
    });
}

function traceScriptVM() {
    let tracing = false;

    Interceptor.attach(Addrs.ScriptVMExecute, {
        onEnter: function(args) {
            const p = args[1];
            const scriptName = p.add(0x14).readUtf8String()!;
            const currentFunction = p.add(0x34).readUtf8String()!;
            const offset = p.add(0x78).readU32();

            if (offset == 0) return;

            if (scriptName.indexOf('chr033') != -1) {
                tracing = true;
                utils.log('***** ScriptVMExecute: %s.%s 0x%08X *****', scriptName, currentFunction, offset);
            }
        },

        onLeave: function(retval) {
            if (tracing) {
                tracing = false;
                utils.log('****************** ScriptVMExecute END ******************');
            }
        }
    });

    Interceptor.attach(ptr(0x1403C6DDD), function() {
        if (!tracing)
            return;

        const ctx = (this.context as X64CpuContext);
        const offset = ctx.rdx.toUInt32();
        const script = ctx.rbx;
        const scriptName = script.add(0x14).readUtf8String()!;
        const currentFunction = script.add(0x34).readUtf8String()!;
        const opcode = ctx.r8.and(0xFF).toUInt32();

        // utils.log(`    OP_${ctx.r8.and(0xFF).toUInt32().toString(16).toUpperCase()} @ ${scriptName}.${currentFunction}.${ptr(offset)}`);
        utils.log(`    OP_%02X @ ${scriptName}.${currentFunction}.${ptr(offset)}`, opcode);
    });
}

export function main() {
    ED83.enableLogger();
    // traceScriptVM();

    hookFileRedirection();
    hookCharacterModelInit();
    hookBattle();

    Memory.patchCode(Addrs.DLC_Check, 1, (code) => {
        code.writeU8(0xEB);
    });

    const recorded: any = {};

    // Interceptor.attach(Addrs.ScriptGetFunctionByName, {
    //     onEnter: function(args) {
    //         const p = args[1];
    //         const scriptHeader = args[0].add(0x6B8).readPointer();
    //         const scriptName = scriptHeader.add(0x20).readUtf8String()!;
    //         const funcName = p.readUtf8String()!;

    //         const name = `${scriptName}.${funcName}`;

    //         if (funcName != 'FieldMonsterData') return;

    //         if (recorded[name])
    //             return;

    //         recorded[name] = true;

    //         this.name = name;
    //     },
    //     onLeave: function(retval) {
    //         if (!this.name)
    //             return;

    //         utils.log(`ScriptGetFunctionByName: ${this.name} = ${retval}`);
    //     },
    // });
}
