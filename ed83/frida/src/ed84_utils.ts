import { Addrs } from "./ed84_addrs";

const _AllocObject      = new NativeFunction(Addrs.AllocObject, "pointer", ['size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _AllocMemory      = new NativeFunction(Addrs.AllocMemory, "pointer", ['size_t', 'size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _FreeMemory       = new NativeFunction(Addrs.FreeMemory, "void", ['pointer'], 'win64');

export function AllocObject(size: number): NativePointer {
    return _AllocObject(size, 0, 0, 0) as NativePointer;
}

export function AllocMemory(size: number, tag: number): NativePointer {
    return _AllocMemory(size, tag, 0, 0, 0) as NativePointer;
}

export function FreeMemory(p: NativePointer) {
    _FreeMemory(p);
}