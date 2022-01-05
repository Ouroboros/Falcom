import * as json5 from "json5"
import * as path from "path"
import { Modules } from "../modules";
import { Addrs, Offsets } from "./addrs";
import { ED8BaseObject, ED8Vector, Interceptor2 } from "../utils";
import * as utils from "../utils";

export const MaxPartyChrId = 0x40;
export const MinCustomChrId = 0x2000;
export const InvalidChrId = 0xFFFF;

export interface INameTableData {
    chrId       : number;
    chrName     : string;
    model       : string;
    ani         : string;
    algo        : string;
    faceModel   : string;
    faceTexture : string;
    name2       : string;
}

export interface IConfig {
    nameTable: INameTableData[];
    assetMap: {[key: string]: string};
}

export class NameTableData extends ED8BaseObject implements INameTableData {
    get chrId(): number {
        return this.readU16(0x00);
    }

    get chrName(): string {
        return this.readPointer(0x08).readUtf8String()!;
    }

    get model(): string {
        return this.readPointer(0x10).readUtf8String()!;
    }

    get faceModel(): string {
        return this.readPointer(0x18).readUtf8String()!;
    }

    get ani(): string {
        return this.aniptr.readUtf8String()!;
    }

    get aniptr(): NativePointer {
        return this.readPointer(0x20);
    }

    get algo(): string {
        return '';
    }

    get faceTexture(): string {
        return this.readPointer(0x28).readUtf8String()!;
    }

    get name2(): string {
        return this.readPointer(0x30).readUtf8String()!;
    }
}

export class CharacterManager extends ED8BaseObject {

}

export class Character extends ED8BaseObject {
    static isReplaced(chrId: number): boolean {
        const id = ED84.getBattleStyle(chrId);
        if (id == InvalidChrId) {
            return false;
        }

        return id >= MaxPartyChrId;
    }

    isReplaced(): boolean {
        return Character.isReplaced(this.chrId);
    }

    get chrId(): number {
        return this.readU16(Offsets.Character.ChrID);
    }

    get modelChrId(): number {
        return this.readU16(Offsets.Character.ModelChrId);
    }

    set modelChrId(chrId: number) {
        this.writeU16(Offsets.Character.ModelChrId, chrId);
    }

    get model(): string {
        return this.readUtf8String(Offsets.Character.Model)!;
    }

    get faceModel(): string {
        return this.readUtf8String(Offsets.Character.FaceModel)!;
    }

    set faceModel(asset: string) {
        this.pointer.add(Offsets.Character.FaceModel).writeUtf8String(asset);
    }

    get presetFaceModel(): string {
        return this.readUtf8String(Offsets.Character.PresetFaceModel)!;
    }

    set presetFaceModel(model: string) {
        this.pointer.add(Offsets.Character.PresetFaceModel).writeUtf8String(model);
    }

    loadAni(ani: string) {
        const Character_LoadAni = new NativeFunction(Addrs.Character.LoadAni, "void", ['pointer', 'pointer', 'uint32'], 'win64');
        const p = Memory.allocUtf8String(ani);
        const auto_compile = 0;
        Character_LoadAni(this.pointer, p, auto_compile);
    }
}

export class BattleCharacter extends ED8BaseObject {
    private static _IsChrNPC            = new NativeFunction(Addrs.BattleCharacter.IsChrNPC, 'bool', ['pointer'], 'win64');
    private static _InitNpcCraftAI      = new NativeFunction(Addrs.BattleCharacter.InitNpcCraftAI, 'void', ['pointer', 'uint32'], 'win64');
    private static _InitEquipAndOrbs    = new NativeFunction(Addrs.BattleCharacter.InitEquipAndOrbs, 'void', ['pointer', 'uint32'], 'win64');
    private static _InitPartyCraft      = new NativeFunction(Addrs.BattleCharacter.InitPartyCraft, 'void', ['pointer', 'pointer'], 'win64');
    private static _InitMagic           = new NativeFunction(Addrs.BattleCharacter.InitMagic, 'void', ['pointer', 'pointer'], 'win64');

    get battleProc(): NativePointer {
        return this.readPointer(Offsets.BattleCharacter.BattleProc);
    }

    get character(): Character {
        return new Character(this.readPointer(Offsets.BattleCharacter.Character));
    }

    get sbreakCraftID(): number {
        return this.readU16(Offsets.BattleCharacter.SBreakCraftID);
    }

    set sbreakCraftID(craftId: number) {
        this.writeU16(Offsets.BattleCharacter.SBreakCraftID, craftId);
    }

    get battleInfoTable(): BattleInfoTable {
        return new BattleInfoTable(this.readPointer(Offsets.BattleCharacter.BattleInfoTable));
    }

    isChrNPC(): boolean {
        return (BattleCharacter._IsChrNPC(this.pointer) & 0xFF) != 0;
    }

    initNpcCraftAI(reset: boolean) {
        BattleCharacter._InitNpcCraftAI(this.pointer, Number(reset));
    }

    initEquipAndOrbs(chrId: number) {
        BattleCharacter._InitEquipAndOrbs(this.pointer, chrId);
    }

    initPartyCraft(chrId: number) {
        BattleCharacter._InitPartyCraft(this.pointer, ED84.getCraftList(chrId));
    }

    initMagic(chrId: number) {
        BattleCharacter._InitMagic(this.pointer, ED84.getMagicList(chrId));
    }
}

export class BattleInfoTable extends ED8BaseObject {
    get algoTable(): AlgoTable {
        return new AlgoTable(this.pointer.add(Offsets.BattleInfoTable.AlgoTable));
    }

    get actionTable(): ActionTable {
        return new ActionTable(this.pointer.add(Offsets.BattleInfoTable.ActionTable));
    }

    get battleCharacter(): BattleCharacter {
        return new BattleCharacter(this.readPointer(Offsets.BattleInfoTable.BattleCharacter));
    }
}

export class AlgoTable extends ED8Vector {
}

class ActionTableData extends ED8BaseObject {
    get craftId(): number {
        return this.readU16(0x00);
    }

    get name(): string {
        return this.readPointer(0x10).readUtf8String()!;
    }

    get description(): string {
        return this.readPointer(0x18).readUtf8String()!;
    }

    get type(): number {
        return this.readU8(0x26);
    }

    get area(): number {
        return this.readU8(0x84);
    }

    get rng(): number {
        return this.readFloat(0x88);
    }
}

export class ActionTable extends ED8Vector {
    getCraft(index: number): ActionTableData {
        return new ActionTableData(this.ptr.add(index * 8).readPointer())
    }
}

export class ED84 extends ED8BaseObject {
    private static _sharedInstance: ED84;
    private static _config: IConfig | undefined;

    private static _findNameTableDataByModel = new NativeFunction(Addrs.ED84.findNameTableDataByModel, "pointer", ['pointer', 'pointer'], 'win64');
    private static _findNameTableDataByChrId = new NativeFunction(Addrs.ED84.findNameTableDataByChrId, "pointer", ['pointer', 'uint16'], 'win64');
    private static _findPartyCharByChrId     = new NativeFunction(Addrs.ED84.findPartyCharByChrId, "pointer", ['pointer', 'uint16', 'uint32'], 'win64');

    static enableLogger() {
        Interceptor2.jmp(
            Addrs.Logger_Ansi2UTF8,
            function(output: NativePointer, outputSize: NativePointer, input: NativePointer) {
                const s = input.readUtf8String()!
                output.writeUtf8String(s.slice(0, outputSize.toUInt32()));
            },
            'void', ['pointer', 'pointer', 'pointer'],
        );

        const Logger_Output = Interceptor2.jmp(
            Addrs.Logger_Output,
            function(self: NativePointer, level: NativePointer, buffer: NativePointer) {
                const buf = buffer.readUtf8String()!;
                if (buf.substring(buf.length - 1) == '\n') {
                    utils.log(buf.substring(0, buf.length - 1));
                } else {
                    utils.log(buf);
                }

                Logger_Output(self, level, buffer);
            },
            'void', ['pointer', 'pointer', 'pointer'],
        );
    }

    static get sharedInstance(): ED84 {
        if (this._sharedInstance)
            return this._sharedInstance;

        const p = Addrs.ED84.sharedInstance.readPointer();

        if (p.isNull()) {
            throw new Error('ED84 null');
        }

        this._sharedInstance = new ED84(p);
        return this._sharedInstance;
    }

    static get nameTable(): NativePointer {
        return this.sharedInstance.readPointer(Offsets.ED84.t_name);
    }

    static get characterManager(): CharacterManager {
        return new CharacterManager(this.sharedInstance.readPointer(Offsets.ED84.CharacterManager));
    }

    static getConfig(): IConfig | undefined {
        if (this._config)
            return this._config;

        this._config = function() {
            const exePath = path.join(path.dirname(path.dirname(path.dirname(Modules.ED84.path.split('\\').join('/')))), 'ouroboros', 'config.json5');
            const config = utils.readFileContent(exePath);
            if (!config)
                return undefined;

            const s = Buffer.from(config).toString('utf8');

            try {
                const cfg: IConfig = json5.parse(s);
                return cfg;
            } catch (e) {
                utils.log('load config: %s', e);
            }

            return undefined;
        }();

        return this._config;
    }

    static findNameTableDataByModel(model: string): INameTableData | undefined {
        const m = Memory.allocUtf8String(model);
        const p = this._findNameTableDataByModel(this.nameTable, m);
        if (!p.isNull())
            return new NameTableData(p);

        return ED84.getConfig()?.nameTable.find(data => data.model == model);
    }

    static findNameTableDataByChrId(chrId: number): INameTableData | undefined {
        if (chrId == InvalidChrId)
            return undefined;

        const p = this._findNameTableDataByChrId(this.nameTable, chrId);
        if (!p.isNull())
            return new NameTableData(p);

        return ED84.getConfig()?.nameTable.find(data => data.chrId == chrId);
    }

    static getCraftList(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED84.CraftList).add(chrId * 0x10);
    }

    static getMagicList(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED84.MagicList).add(chrId * 0x10);
    }

    static getSBreak(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED84.SBreakList).add(chrId * 2);
    }

    static getBattleStyle(chrId: number): number {
        if (chrId >= MaxPartyChrId) {
            return InvalidChrId;
        }

        return this.sharedInstance.pointer.add(Offsets.ED84.BattleStyleList).add(chrId * 2).readU16();
    }
}
