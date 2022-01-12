import * as utils from "../utils";
import { sprintf } from "sprintf-js";
import { Interceptor2 } from "../utils";
import { API } from "../modules";
import { Addrs } from "./addrs";
import {
    ED84,
    ScriptId,
    Character,
    BattleCharacter,
    BattleInfoTable,
    INameTableData,
    InvalidChrId,
    MaxPartyChrId,
    MinCustomChrId,
    ScriptManager,
} from "./types";

function findReplacedNameData(chrId: number): INameTableData | undefined {
    const replacedChrId = ED84.getBattleStyle(chrId)
    if (replacedChrId == InvalidChrId) {
        return undefined;
    }

    return ED84.findNameTableDataByChrId(replacedChrId >= MaxPartyChrId ? replacedChrId : chrId);
}

function hookIoRedirection() {
    const File_Open = Interceptor2.jmp(
        Addrs.File.Open,
        function(self: NativePointer, path: NativePointer, mode: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readAnsiString()!);
            if (patch) {
                path = Memory.allocAnsiString(patch);
            }

            return File_Open(self, path, mode);
        },
        'pointer', ['pointer', 'pointer', 'pointer'],
    );

    const wfopen = Interceptor2.jmp(
        API.crt.wfopen,
        function(path: NativePointer, mode: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readUtf16String()!);
            if (patch) {
                path = Memory.allocUtf16String(patch);
            }

            return wfopen(path, mode);
        },
        'pointer', ['pointer', 'pointer'],
    );

    const File_GetSize = Interceptor2.jmp(
        Addrs.File.GetSize,
        function(self: NativePointer, path: NativePointer, arg3: NativePointer, fileSize: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readAnsiString()!);
            if (patch) {
                path = Memory.allocAnsiString(patch);
            }

            return File_GetSize(self, path, arg3, fileSize);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer'],
    );
}

function hookCharacterModel() {
    const Character_LoadFaceModel = Interceptor2.jmp(
        Addrs.Character.LoadFaceModel,
        function(chr: NativePointer, faceModel: NativePointer) {
            const char = new Character(chr);
            const nameData = ED84.findNameTableDataByModel(char.model);

            // utils.log(`model: ${char.model}`);
            // utils.log(`face: ${nameData?.faceModel}`);

            if (nameData) {
                const faceModel = nameData.faceModel;
                if (faceModel != 'null') {
                    char.presetFaceModel = faceModel;
                }
            }

            Character_LoadFaceModel(chr, faceModel);
        },
        'void', ['pointer', 'pointer'],
    );

    const Character_LoadAni = Interceptor2.jmp(
        Addrs.Character.LoadAni,
        function(chr: NativePointer, ani: NativePointer, autoCompile: number) {
            const char = new Character(chr);
            const nameData = ED84.findNameTableDataByModel(char.model);
            ani = nameData ? Memory.allocUtf8String(nameData.ani) : ani;

            // utils.log(`Character::LoadAni(${nameData?.ani})`);

            Character_LoadAni(chr, ani, 0);
        },
        'void', ['pointer', 'pointer', 'uint32'],
    );

    const Character_Initialize = Interceptor2.jmp(
        Addrs.Character.Initialize,
        function(
            chr     : NativePointer,
            model   : NativePointer,
            name    : NativePointer,
            a4      : NativePointer,
            a5      : NativePointer,
            a6      : NativePointer,
            a7      : NativePointer,
            a8      : NativePointer,
            a9      : NativePointer,
            a10     : NativePointer,
            a11     : NativePointer,
            a12     : NativePointer,
            a13     : NativePointer,
            a14     : NativePointer,
        ): NativePointer {

            const char = new Character(chr);
            const chrId = ED84.getBattleStyle(char.chrId);

            if (chrId >= MaxPartyChrId && char.modelChrId == InvalidChrId) {
                char.modelChrId = chrId;
                const nameData = findReplacedNameData(char.chrId);
                if (nameData) {
                    // utils.log(`new model: ${nameData.model}`);
                    model = Memory.allocUtf8String(nameData.model);
                }
            }

            return Character_Initialize(chr, model, name, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer'],
    );

    const Asset_LoadAsset = Interceptor2.jmp(
        Addrs.Asset.LoadAsset,
        function(a1: NativePointer, symbol: NativePointer, size: NativePointer, a4: NativePointer, a5: NativePointer): NativePointer {
            const s = symbol.readUtf8String()!;

            const s2 = ED84.getConfig()?.assetMap[s];
            if (s2) {
                symbol = Memory.allocUtf8String(s2);
            }

            return Asset_LoadAsset(a1, symbol, size, a4, a5);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer'],
    );

    const Crc32CheckSum = Interceptor2.jmp(
        Addrs.Crc32CheckSum,
        function(data: NativePointer, size: UInt64): number {
            do
            {
                if (size.valueOf() > 0x20 || size.valueOf() == 0)
                    break;

                const bytes = Buffer.from(data.readByteArray(size.valueOf())!);
                if (bytes.length == 0) {
                    // utils.log(`*** Crc32CheckSum ***(${data}, ${size.valueOf()})`);
                    break;
                }

                const nonAscii = bytes.reduce((prev, value) => (value >= 0x20 && value <= 0x7A) ? 0 : 1);
                if (nonAscii != 0)
                    break;

                const s2 = ED84.getConfig()?.assetMap[bytes.toString('utf8')];
                if (s2) {
                    data = Memory.allocUtf8String(s2);
                    size = new UInt64(s2.length);

                    // utils.log(`new symbol: ${s2} @ ${s2.length}`)
                }

            } while (false);

            return Crc32CheckSum(data, size);
        },
        'uint32', ['pointer', 'size_t'],
    );

    const BattleCharacter_FormatBattleSymbol = Interceptor2.jmp(
        Addrs.BattleCharacter.FormatBattleSymbol,
        function(btlChr: NativePointer, chr: NativePointer, buffer: NativePointer, bufferSize: number, arg5: number, arg6: number) {

            do
            {
                const battleChar = new BattleCharacter(btlChr);
                const char = battleChar.character;

                if (!char.isReplaced())
                    break;

                const prefixmap: any = {
                    'C_CHR' : 'C',
                    'C_MON' : 'M',
                    'O_E'   : 'OE',
                    'C_NPC' : 'N',
                    'C_ROB' : 'R',
                };

                const model = char.model;
                let prefix = '';
                let num = '';

                for (let p in prefixmap) {
                    if (!model.startsWith(p)) {
                        continue;
                    }

                    prefix = prefixmap[p];
                    num = model.slice(p.length, p.length + 3);
                    break;
                }

                const symbol = sprintf('I_BTLS%s', prefix + num);
                buffer.writeUtf8String(symbol.slice(0, bufferSize));

                return;

            } while (0);

            BattleCharacter_FormatBattleSymbol(btlChr, chr, buffer, bufferSize, arg5, arg6);
        },
        'void', ['pointer', 'pointer', 'pointer', 'uint32', 'uint8', 'uint8'],
    );
}

function hookBattle() {
    Interceptor2.call(
        Addrs.BattleProc.SetupBattle_FormatAlgoScript,
        function(buffer: NativePointer, size: number, fmt: NativePointer, battleAni: NativePointer) {
            const ctx = (this.context as X64CpuContext);
            const chrId = ctx.rdi.toUInt32() & 0xFFFF;

            let path = (function() {
                if (Character.isReplaced(chrId) == false)
                    return '';

                const nameData = findReplacedNameData(chrId);

                if (!nameData)
                    return '';

                const algo = sprintf(fmt.readAnsiString()!, nameData.algo ? nameData.algo.slice(2) : nameData.ani);
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

    Interceptor2.call(
        Addrs.BattleProc.SetupBattle_InitCraft,
        function() {
            const ctx = (this.context as X64CpuContext);
            const chrId = ctx.rdi.toUInt32() & 0xFFFF;
            const battleChar = new BattleCharacter(ctx.rcx);

            if (chrId >= MaxPartyChrId) {
                if (battleChar.isChrNPC()) {
                    battleChar.initNpcCraftAI(false);
                }
            } else {
                const replaced = Character.isReplaced(chrId);

                battleChar.initEquipAndOrbs(chrId);
                battleChar.initMagic(chrId);
                replaced ? battleChar.initNpcCraftAI(false) : battleChar.initPartyCraft(chrId);

                if (replaced) {
                    const actionTable = battleChar.battleInfoTable.actionTable;
                    if (actionTable.pointer.isNull())
                        return;

                    for (let i = 0, n = actionTable.size; i != n; i++) {
                        const craft = actionTable.getCraft(i);
                        if (craft.type != 0x1F)
                            continue;

                        battleChar.sbreakCraftID = craft.craftId;
                    }
                } else {
                    battleChar.sbreakCraftID = ED84.getSBreak(chrId).readU16();
                }

            }
        },
        'void', [],
    );

    Memory.patchCode(Addrs.BattleProc.SetupBattle_InitCraft.add(5), 2, (code) => {
        code.writeU8(0xEB);
        code.add(1).writeU8(Addrs.BattleProc.SetupBattle_InitCraftEnd.sub(Addrs.BattleProc.SetupBattle_InitCraft).sub(5 + 2).toUInt32());
    });

    const BattleInfoTable_GetCraftByID = Interceptor2.jmp(
        Addrs.BattleInfoTable.GetCraftByID,
        function(tables: NativePointer, craftId: number): NativePointer {
            const tbl = new BattleInfoTable(tables);
            const char = tbl.battleCharacter;

            if (char.character.isReplaced() == false) {
                return BattleInfoTable_GetCraftByID(tables, craftId);
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

            return BattleInfoTable_GetCraftByID(tables, craftId);

        }, 'pointer', ['pointer', 'uint16'],
    );
}

function hookScript() {
    const ScriptManager_LoadLibrary = Interceptor2.jmp(
        Addrs.ScriptManager.LoadLibraries,
        function(self: NativePointer): number {
            const ret = ScriptManager_LoadLibrary(self);

            if (ret == 0) {
                const mgr = new ScriptManager(self);
                mgr.debug.loadDebug();
            }

            return ret;
        },
        'uint32', ['pointer'],
    );

    const ScriptManager_GetScriptById = Interceptor2.jmp(
        Addrs.ScriptManager.GetScriptByID,
        function(context: NativePointer, id: number): NativePointer {
            switch (id) {
                case ScriptId.Debug:
                    return ED84.scriptManager.debug.pointer;
            }

            return ScriptManager_GetScriptById(context, id);
        },
        'pointer', ['pointer', 'uint16'],
    );

    const handleActMenu = Interceptor2.jmp(
        Addrs.HandleActMenu,
        function(arg1: NativePointer, arg2: number): number {
            const VK_SHIFT = 0x10;
            const ctx = (this.context as X64CpuContext);

            if (API.USER32.GetAsyncKeyState(VK_SHIFT) >= 0) {
                return handleActMenu(arg1, arg2);
            }

            const system = ScriptManager.getScriptByID(ScriptId.System);

            system?.call(ED84.scriptManager.getThreadContext(), 'FC_ActMenu_Ouroboros', 0, 0, 1, 1);

            return 0;
        },
        'uint8', ['pointer', 'double'],
    );
}

export function main() {
    ED84.enableLogger();

    hookIoRedirection();
    hookCharacterModel();
    hookBattle();
    hookScript();

    Memory.patchCode(Addrs.SaveDataChecksum, 1, (code) => {
        code.writeU8(0xEB);
    });
}
