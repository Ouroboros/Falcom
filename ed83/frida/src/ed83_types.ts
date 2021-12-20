import { Addrs, Offsets } from "./ed83_addrs";
import { ED8BaseObject } from "./utils";
import * as utils from "./utils";

export const MaxPartyChrId = 0x30;
export const MinCustomChrId = 0x2000;
export const InvalidChrId = 0xFFFF;

export class ScriptLoader extends ED8BaseObject {
    get name(): string {
        return this.pointer.add(Offsets.ScriptLoader.Name).readUtf8String()!;
    }

    set name(n: string) {
        this.pointer.add(Offsets.ScriptLoader.Name).writeUtf8String(n.slice(0, Offsets.ScriptLoader.NameSize));
    }

    get type(): UInt64 {
        return uint64(this.readU32(Offsets.ScriptLoader.Type));
    }

    set type(t: UInt64) {
        this.pointer.add(Offsets.ScriptLoader.Type).writeU32(t);
    }

    get buffer(): NativePointer {
        return this.pointer.add(Offsets.ScriptLoader.Buffer).readPointer();
    }

    set buffer(ptr: NativePointer) {
        this.pointer.add(Offsets.ScriptLoader.Buffer).writePointer(ptr);
    }

    get bufferBase(): NativePointer {
        return this.pointer.add(Offsets.ScriptLoader.BufferBase).readPointer();
    }

    set bufferBase(ptr: NativePointer) {
        this.pointer.add(Offsets.ScriptLoader.BufferBase).writePointer(ptr);
    }

    get disabled(): boolean {
        return this.pointer.add(Offsets.ScriptLoader.IsDisable).readU8() != 0;
    }

    vtbl(): NativePointer {
        return this.pointer.readPointer();
    }

    reset() {
        const init = new NativeFunction(this.vtbl().add(Offsets.ScriptLoader.vtbl.init).readPointer(), 'void', ['pointer'], 'win64');
        init(this.pointer);
    }
}

export class TableLoader extends ED8BaseObject {
    get buffer(): NativePointer {
        return this.pointer.add(Offsets.TableLoader.Buffer).readPointer();
    }

    set buffer(ptr: NativePointer) {
        this.pointer.add(Offsets.TableLoader.Buffer).writePointer(ptr);
    }
}

export class CharacterManager extends ED8BaseObject {
    // private static _ReleaseCharacter = new NativeFunction(Addrs.CharacterManager.ReleaseCharacter, 'void', ['pointer', 'pointer'], 'win64');

    // releaseCharacter(char: NativePointer) {
    //     CharacterManager._ReleaseCharacter(this.pointer, char);
    // }
}

export class Character extends ED8BaseObject {
    isReplaced(nameData?: NameTableData | null): boolean {
        return ED83.getBattleStyle(this.chrId) >= MinCustomChrId;

        // const name = nameData ? nameData : ED83.findNameTableDataByModel(this.model);
        // if (!name)
        //     return false;

        // if (name.chrId == 0xFFFF)
        //     return false;

        // return name.chrId != this.chrId;
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

    get face(): string {
        return this.readUtf8String(Offsets.Character.FaceModel)!;
    }

    set face(asset: string) {
        this.pointer.add(Offsets.Character.FaceModel).writeUtf8String(asset);
    }

    get faceTexture(): string {
        return this.readUtf8String(Offsets.Character.faceTexture)!;
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
        return this.readPointer(Offsets.BattleCharacter.SBreakCraftID).readU16();
    }

    set sbreakCraftID(craftId: number) {
        this.pointer.add(Offsets.BattleCharacter.SBreakCraftID).writeU16(craftId);
    }

    get battleAITable(): BattleAITable {
        return new BattleAITable(this.readPointer(Offsets.BattleCharacter.BattleAITable));
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
        BattleCharacter._InitPartyCraft(this.pointer, ED83.getCraftList(chrId));
    }

    initMagic(chrId: number) {
        BattleCharacter._InitMagic(this.pointer, ED83.getMagicList(chrId));
    }
}

export class AnimeClipObject extends ED8BaseObject {
    get name(): string {
        return this.readPointer(0x40).readUtf8String()!;
    }
}

export class NameTableData extends ED8BaseObject {
    get chrId(): number {
        return this.readU16(0x00);
    }

    get name(): string {
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

    get faceAnimeClip(): string {
        return this.readPointer(0x28).readUtf8String()!;
    }

    get name2(): string {
        return this.readPointer(0x30).readUtf8String()!;
    }
}

class vector extends ED8BaseObject {
    get size(): number {
        return this.readU32(0x00);
    }

    get ptr(): NativePointer {
        return this.readPointer(0x08);
    }
}

export class BattleAITable extends ED8BaseObject {
    get algoTable(): AlgoTable {
        return new AlgoTable(this.pointer.add(Offsets.BattleAITable.AlgoTable));
    }

    get actionTable(): ActionTable {
        return new ActionTable(this.pointer.add(Offsets.BattleAITable.ActionTable));
    }

    get battleCharacter(): BattleCharacter {
        return new BattleCharacter(this.readPointer(Offsets.BattleAITable.BattleCharacter));
    }
}

export class AlgoTable extends vector {
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
        return this.readU8(0x24);
    }

    get area(): number {
        return this.readU8(0x84);
    }

    get rng(): number {
        return this.readFloat(0x88);
    }
}

export class ActionTable extends vector {
    getCraft(index: number): ActionTableData {
        return new ActionTableData(this.ptr.add(index * 8).readPointer())
    }
}

export class ED83 extends ED8BaseObject {
    private static _sharedInstance: ED83;

    private static _findNameTableDataByModel = new NativeFunction(Addrs.ED83.findNameTableDataByModel, "pointer", ['pointer', 'pointer'], 'win64');
    private static _findNameTableDataByChrId = new NativeFunction(Addrs.ED83.findNameTableDataByChrId, "pointer", ['pointer', 'uint16'], 'win64');
    private static _findPartyCharByChrId     = new NativeFunction(Addrs.ED83.findPartyCharByChrId, "pointer", ['pointer', 'uint16', 'uint32'], 'win64');

    static get sharedInstance(): ED83 {
        if (this._sharedInstance)
            return this._sharedInstance;

        const p = Addrs.ED83.sharedInstance.readPointer();

        if (p.isNull()) {
            throw new Error('ED83 null');
        }

        this._sharedInstance = new ED83(p);
        return this._sharedInstance;
    }

    static enableLogger() {
        Interceptor.attach(Addrs.Logger_Output, {
            onEnter: function(args) {
                const buf = args[2].readUtf8String()!;
                if (buf.substring(buf.length - 1) == '\n') {
                    utils.log(buf.substring(0, buf.length - 1));
                } else {
                    utils.log(buf);
                }
            },
        });
    }

    static get nameTable(): NativePointer {
        return this.sharedInstance.readPointer(Offsets.ED83.t_name);
    }

    static get characterManager(): CharacterManager {
        return new CharacterManager(this.sharedInstance.readPointer(Offsets.ED83.CharacterManager));
    }

    static findNameTableDataByModel(model: string): NameTableData | null {
        const m = Memory.allocUtf8String(model);
        const p = this._findNameTableDataByModel(this.nameTable, m);
        if (p.isNull())
            return null;

        return new NameTableData(p);
    }

    static findNameTableDataByChrId(chrId: number): NameTableData | null {
        if (chrId == InvalidChrId)
            return null;

        const p = this._findNameTableDataByChrId(this.nameTable, chrId);
        if (p.isNull())
            return null;

        return new NameTableData(p);
    }

    static findCharByChrId(chrId: number): Character | null {
        const char = this._findPartyCharByChrId(this.characterManager.pointer, chrId, 0);
        return char ? new Character(char) : null;
    }

    static getCraftList(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED83.CraftList).add(chrId * 0x10);
    }

    static getMagicList(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED83.MagicList).add(chrId * 0x10);
    }

    static getSBreak(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED83.SBreakList).add(chrId * 2);
    }

    static getBattleStyle(chrId: number): number {
        return this.sharedInstance.pointer.add(Offsets.ED83.BattleStyleList).add(chrId * 2).readU16();
    }
}
