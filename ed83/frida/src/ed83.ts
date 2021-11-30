import * as utils from "./utils";
import { Modules } from "./modules";
import { Offsets } from "./consts";

const _AllocObject      = new NativeFunction(Modules.ED83.base.add(0x4DAAC0), "pointer", ['size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _AllocMemory      = new NativeFunction(Modules.ED83.base.add(0x5DFE70), "pointer", ['size_t', 'size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _BlowfishInit     = new NativeFunction(Modules.ED83.base.add(0x20C730), "void", ['pointer', 'pointer', 'size_t'], 'win64');
const _BlowfishInit2    = new NativeFunction(Modules.ED83.base.add(0x20CAC0), "void", ['pointer', 'pointer'], 'win64');
const _BlowfishDecode   = new NativeFunction(Modules.ED83.base.add(0x20CAA0), "void", ['pointer', 'pointer', 'size_t', 'int'], 'win64');
const _FreeMemory       = new NativeFunction(Modules.ED83.base.add(0x4DAA50), "void", ['pointer'], 'win64');

export function AllocObject(size: number): NativePointer {
    return _AllocObject(size, 0, 0, 0) as NativePointer;
}

export function AllocMemory(size: number, tag: number): NativePointer {
    return _AllocMemory(size, tag, 0, 0, 0) as NativePointer;
}

export function FreeMemory(p: NativePointer) {
    _FreeMemory(p);
}

export function BlowfishDecode(data: ArrayBuffer, key1: ArrayBuffer, key2: ArrayBuffer) {
    const bf = AllocObject(0x1444);

    _BlowfishInit(bf, key2.unwrap(), 8);
    _BlowfishInit2(bf, key1.unwrap());

    _BlowfishDecode(bf, data.unwrap(), data.byteLength, 0);

    FreeMemory(bf);
}

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
