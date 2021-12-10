import { Addrs, Offsets } from "./ed83_addrs";
import { ED8BaseObject } from "./utils";
import * as utils from "./utils";

export const MaxPartyChrId = 0x30;

export class ScriptLoader extends ED8BaseObject {
    get name(): string {
        return this.impl.add(Offsets.ScriptLoader.Name).readUtf8String()!;
    }

    set name(n: string) {
        this.impl.add(Offsets.ScriptLoader.Name).writeUtf8String(n.slice(0, Offsets.ScriptLoader.NameSize));
    }

    get type(): UInt64 {
        return uint64(this.readU32(Offsets.ScriptLoader.Type));
    }

    set type(t: UInt64) {
        this.impl.add(Offsets.ScriptLoader.Type).writeU32(t);
    }

    get buffer(): NativePointer {
        return this.impl.add(Offsets.ScriptLoader.Buffer).readPointer();
    }

    set buffer(ptr: NativePointer) {
        this.impl.add(Offsets.ScriptLoader.Buffer).writePointer(ptr);
    }

    get bufferBase(): NativePointer {
        return this.impl.add(Offsets.ScriptLoader.BufferBase).readPointer();
    }

    set bufferBase(ptr: NativePointer) {
        this.impl.add(Offsets.ScriptLoader.BufferBase).writePointer(ptr);
    }

    get disabled(): boolean {
        return this.impl.add(Offsets.ScriptLoader.IsDisable).readU8() != 0;
    }

    vtbl(): NativePointer {
        return this.impl.readPointer();
    }

    reset() {
        const init = new NativeFunction(this.vtbl().add(Offsets.ScriptLoader.vtbl.init).readPointer(), 'void', ['pointer'], 'win64');
        init(this.impl);
    }
}

export class TableLoader extends ED8BaseObject {
    get buffer(): NativePointer {
        return this.impl.add(Offsets.TableLoader.Buffer).readPointer();
    }

    set buffer(ptr: NativePointer) {
        this.impl.add(Offsets.TableLoader.Buffer).writePointer(ptr);
    }
}

export class Character extends ED8BaseObject {
    isReplaced(nameData?: NameTableData | null): boolean {
        const name = nameData ? nameData : ED83.findNameTableDataByModel(this.model);
        if (!name)
            return false;

        if (name.chrId == 0xFFFF)
            return false;

        return name.chrId != this.chrId;
    }

    get chrId(): number {
        return this.readU16(Offsets.Character.ChrID);
    }

    get model(): string {
        return this.readUtf8String(Offsets.Character.Model)!;
    }

    get face(): string {
        return this.readUtf8String(Offsets.Character.FaceModel)!;
    }

    set face(asset: string) {
        this.impl.add(Offsets.Character.FaceModel).writeUtf8String(asset);
    }

    get faceTexture(): string {
        return this.readUtf8String(Offsets.Character.faceTexture)!;
    }

    get presetFaceModel(): string {
        return this.readUtf8String(Offsets.Character.PresetFaceModel)!;
    }

    set presetFaceModel(model: string) {
        this.impl.add(Offsets.Character.PresetFaceModel).writeUtf8String(model);
    }

    loadAni(ani: string) {
        const Character_LoadAni = new NativeFunction(Addrs.Character.LoadAni, "void", ['pointer', 'pointer', 'uint32'], 'win64');
        const p = Memory.allocUtf8String(ani);
        const auto_compile = 0;
        Character_LoadAni(this.impl, p, auto_compile);
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
        this.impl.add(Offsets.BattleCharacter.SBreakCraftID).writeU16(craftId);
    }

    isChrNPC(): boolean {
        return (BattleCharacter._IsChrNPC(this.impl) & 0xFF) != 0;
    }

    initNpcCraftAI(reset: boolean) {
        BattleCharacter._InitNpcCraftAI(this.impl, Number(reset));
    }

    initEquipAndOrbs(chrId: number) {
        BattleCharacter._InitEquipAndOrbs(this.impl, chrId);
    }

    initPartyCraft(chrId: number) {
        BattleCharacter._InitPartyCraft(this.impl, ED83.getCraftList(chrId));
    }

    initMagic(chrId: number) {
        BattleCharacter._InitMagic(this.impl, ED83.getMagicList(chrId));
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

export class ED83 extends ED8BaseObject {
    private static _sharedInstance: ED83;

    private static _findNameTableDataByModel = new NativeFunction(Addrs.ED83.findNameTableDataByModel, "pointer", ['pointer', 'pointer'], 'win64');
    private static _findNameTableDataByChrId = new NativeFunction(Addrs.ED83.findNameTableDataByChrId, "pointer", ['pointer', 'uint16'], 'win64');
    private static _findPartyCharByChrId     = new NativeFunction(Addrs.ED83.findPartyCharByChrId, "pointer", ['pointer', 'uint16', 'uint32'], 'win64');

    static get sharedInstance(): ED83 {
        if (this._sharedInstance)
            return this._sharedInstance;

        const p = Addrs.ED83.sharedInstance.readPointer();
        const i = new ED83(p);

        if (p.isNull() == false)
            this._sharedInstance = i;

        return i;
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

    static get characterManager(): NativePointer {
        return this.sharedInstance.readPointer(Offsets.ED83.CharacterManager);
    }

    static findNameTableDataByModel(model: string): NameTableData | null {
        const m = Memory.allocUtf8String(model);
        const p = this._findNameTableDataByModel(this.nameTable, m);
        if (p.isNull())
            return null;

        return new NameTableData(p);
    }

    static findNameTableDataByChrId(chrId: number): NameTableData | null {
        const p = this._findNameTableDataByChrId(this.nameTable, chrId);
        if (p.isNull())
            return null;

        return new NameTableData(p);
    }

    static findCharByChrId(chrId: number): Character | null {
        const char = this._findPartyCharByChrId(this.characterManager, chrId, 0);
        return char ? new Character(char) : null;
    }

    static getCraftList(chrId: number): NativePointer {
        return this.sharedInstance.impl.add(Offsets.ED83.CraftList).add(chrId * 0x10);
    }

    static getMagicList(chrId: number): NativePointer {
        return this.sharedInstance.impl.add(Offsets.ED83.MagicList).add(chrId * 0x10);
    }

    static getSBreak(chrId: number): NativePointer {
        return this.sharedInstance.impl.add(Offsets.ED83.SBreakList).add(chrId * 2);
    }
}
