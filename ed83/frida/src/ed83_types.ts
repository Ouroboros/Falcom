import { Addrs, Offsets } from "./ed83_addrs";
import * as ed83_utils from "./ed83_utils";

export class ScriptLoader {
    impl: NativePointer;

    constructor(impl: NativePointer) {
        this.impl = impl;
    }

    public get name(): string {
        return this.impl.add(Offsets.ScriptLoader.Name).readUtf8String()!;
    }

    public set name(n: string) {
        this.impl.add(Offsets.ScriptLoader.Name).writeUtf8String(n.slice(0, Offsets.ScriptLoader.NameSize));
    }

    public get type(): UInt64 {
        return uint64(this.impl.add(Offsets.ScriptLoader.Type).readU32());
    }

    public set type(t: UInt64) {
        this.impl.add(Offsets.ScriptLoader.Type).writeU32(t);
    }

    public get buffer(): NativePointer {
        return this.impl.add(Offsets.ScriptLoader.Buffer).readPointer();
    }

    public set buffer(ptr: NativePointer) {
        this.impl.add(Offsets.ScriptLoader.Buffer).writePointer(ptr);
    }

    public get bufferBase(): NativePointer {
        return this.impl.add(Offsets.ScriptLoader.BufferBase).readPointer();
    }

    public set bufferBase(ptr: NativePointer) {
        this.impl.add(Offsets.ScriptLoader.BufferBase).writePointer(ptr);
    }

    public get disabled(): boolean {
        return this.impl.add(Offsets.ScriptLoader.IsDisable).readU8() != 0;
    }

    vtbl(): NativePointer {
        return this.impl.readPointer();
    }

    reset() {
        const init = new NativeFunction(this.vtbl().add(Offsets.ScriptLoader.vtbl.init).readPointer(), 'void', ['pointer']);
        init(this.impl);
    }
}

export class TableLoader {
    impl: NativePointer;

    constructor(impl: NativePointer) {
        this.impl = impl;
    }

    public get buffer(): NativePointer {
        return this.impl.add(Offsets.TableLoader.Buffer).readPointer();
    }

    public set buffer(ptr: NativePointer) {
        this.impl.add(Offsets.TableLoader.Buffer).writePointer(ptr);
    }
}

export class Character {
    impl: NativePointer;

    constructor(impl: NativePointer) {
        this.impl = impl;
    }

    public get model(): string {
        return this.impl.add(Offsets.Character.Model).readUtf8String()!;
    }

    public loadAni(ani: string) {
        const Character_LoadAni = new NativeFunction(Addrs.Character.loadAni, "void", ['pointer', 'pointer', 'uint32'], 'win64');
        const p = Memory.allocUtf8String(ani);
        const auto_compile = 0;
        Character_LoadAni(this.impl, p, auto_compile);
    }
}

export class NameTableData {
    impl: NativePointer;

    constructor(impl: NativePointer) {
        this.impl = impl;
    }

    readPointer(offset: number): NativePointer {
        return this.impl.add(offset).readPointer();
    }

    public get chrId(): number {
        return this.impl.readU16();
    }

    public get name(): string {
        return this.readPointer(0x08).readUtf8String()!;
    }

    public get model(): string {
        return this.readPointer(0x10).readUtf8String()!;
    }

    public get defaultFace(): string {
        return this.readPointer(0x18).readUtf8String()!;
    }

    public get ani(): string {
        return this.readPointer(0x20).readUtf8String()!;
    }

    public get face(): string {
        return this.readPointer(0x28).readUtf8String()!;
    }

    public get name2(): string {
        return this.readPointer(0x30).readUtf8String()!;
    }
}

export class ED83 {
    public static instance(): NativePointer {
        return Addrs.gED83.readPointer();
    }

    public static get nameTable(): NativePointer {
        return this.instance().add(Offsets.ED83.t_name).readPointer();
    }

    public static findNameTableDataByModel(model: string): NameTableData | null {
        const p = ed83_utils.findNameTableDataByModel(this.nameTable, model);
        if (p.isNull())
            return null;

        return new NameTableData(p);
    }
}
