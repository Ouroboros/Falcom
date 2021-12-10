import { sprintf } from "sprintf-js";
import * as utils from "./utils";
import { Interceptor2 } from "./utils";
import { Addrs } from "./ed83_addrs";
import { AllocMemory, FreeMemory } from "./ed83_utils";
import { ED83, ScriptLoader, Character, BattleCharacter, MaxPartyChrId } from "./ed83_types";

function ED83ScriptLoad(self: NativePointer, path: NativePointer): NativePointer {
    let filePath = path.readAnsiString()!;

    if (filePath.slice(0, 5) != 'data/') {
        return NULL;
    }

    let data = utils.loadPatchFile(filePath);

    if (data == null) {
        filePath = 'data_cn/' + filePath.slice(5);
        data = utils.readFileContent(filePath);
    }

    if (data == null) {
        utils.log(`Script::load failed: ${filePath}`);
        return NULL;
    }

    // utils.log(`Script::load: ${filePath}`);

    const loader = new ScriptLoader(self);
    let buffer = loader.buffer;

    if (buffer.isNull() == false) {
        FreeMemory(buffer);
        loader.buffer = NULL;
    }

    buffer = AllocMemory(data!.byteLength, 1);
    buffer.writeByteArray(data!);

    loader.buffer = buffer;
    loader.bufferBase = buffer;

    return buffer;
}

function hookCharacterModelInit() {
    const InitAnimeClipTable = Interceptor2.jmp(
        Addrs.Character.InitAnimeClipTable,
        function(chr: NativePointer, animeclip: NativePointer) {
            const char = new Character(chr);
            const nameData = ED83.findNameTableDataByModel(char.model);

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
            const nameData = ED83.findNameTableDataByModel(char.model);

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
            const nameData = ED83.findNameTableDataByModel(char.model);
            char.loadAni(nameData ? nameData.ani : ani.readUtf8String()!);
        },
        'void', ['pointer', 'pointer', 'uint32'],
    );

    const AssetSymbolMap: any = {
        'C_CHR500'  : 'C_CHR033',
        'I_BTLSC500': 'I_BTLSC033',
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

            utils.log('SetupBattle_FormatAlgoScript');

            let path = (function() {
                utils.log('findCharByChrId');
                const char = ED83.findCharByChrId(chrId);

                if (!char)
                return '';

                utils.log('findNameTableDataByModel');
                const nameData = ED83.findNameTableDataByModel(char.model);

                if (!nameData)
                return '';

                utils.log('isReplaced');
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
            utils.log(`path = ${path}`);
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
                replaced ? battleChar.initNpcCraftAI(false) : battleChar.initPartyCraft(chrId);
                battleChar.initMagic(chrId);
                battleChar.sbreakCraftID = replaced ? 0x3EF : ED83.getSBreak(chrId).readU16();
            }
        },
        'void', [],
    );

    Memory.patchCode(Addrs.BattleProc.SetupBattle_InitCraft.add(5), 2, (code) => {
        code.writeU8(0xEB);
        code.add(1).writeU8(Addrs.BattleProc.SetupBattle_InitCraftEnd.sub(Addrs.BattleProc.SetupBattle_InitCraft).sub(5 + 2).toUInt32());
    });
}

function hookFileRedirection() {
    // Interceptor.attach(Addrs.ScriptLoad, {
    //     onEnter: function(args) {
    //         this.self = args[0];
    //         this.path = args[1];
    //     },
    //     onLeave: function(retval) {
    //         const ret = ED83ScriptLoad(this.self, this.path);
    //         if (ret.isNull() == false)
    //             retval.replace(ret);
    //     },
    // });

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

            // utils.log(`LoadTableData: ${p}`);

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

export function main() {
    // ED83.enableLogger();

    hookFileRedirection();
    hookCharacterModelInit();
    hookBattle();

    Memory.patchCode(Addrs.DLC_Check, 1, (code) => {
        code.writeU8(0xEB);
    });

    // Interceptor.attach(Addrs.ScriptVMExecute, {
    //     onEnter: function(args) {
    //         const p = args[1];
    //         const scriptName = p.add(0x14).readUtf8String()!;
    //         const currentFunction = p.add(0x34).readUtf8String()!;
    //         const offset = p.add(0x78).readU32();

    //         if (offset == 0) return;

    //         // utils.log('%s %s 0x%08X', scriptName, currentFunction, offset);
    //     },
    // });

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
