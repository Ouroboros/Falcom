import { Addrs } from "./ed83_addrs";
import { Modules } from "./modules";
import * as utils from "./utils";

const _AllocObject      = new NativeFunction(Modules.ED83.base.add(0x4DAAC0), "pointer", ['size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _AllocMemory      = new NativeFunction(Modules.ED83.base.add(0x5DFE70), "pointer", ['size_t', 'size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _BlowfishInit     = new NativeFunction(Modules.ED83.base.add(0x20C730), "void", ['pointer', 'pointer', 'size_t'], 'win64');
const _BlowfishInit2    = new NativeFunction(Modules.ED83.base.add(0x20CAC0), "void", ['pointer', 'pointer'], 'win64');
const _BlowfishDecode   = new NativeFunction(Modules.ED83.base.add(0x20CAA0), "void", ['pointer', 'pointer', 'size_t', 'int'], 'win64');
const _FreeMemory       = new NativeFunction(Modules.ED83.base.add(0x4DAA50), "void", ['pointer'], 'win64');
const _findNameTableDataByModel = new NativeFunction(Addrs.findNameTableDataByModel, "pointer", ['pointer', 'pointer'], 'win64');

function BlowfishDecode(data: ArrayBuffer, key1: ArrayBuffer, key2: ArrayBuffer) {
    const bf = AllocObject(0x1444);

    _BlowfishInit(bf, key2.unwrap(), 8);
    _BlowfishInit2(bf, key1.unwrap());

    _BlowfishDecode(bf, data.unwrap(), data.byteLength, 0);

    FreeMemory(bf);
}

rpc.exports = function () {
    function blowfishDecryptInternal(data: ArrayBuffer, hash1: ArrayBuffer, hash2: ArrayBuffer): ArrayBuffer {
        BlowfishDecode(data, hash1, hash2);
        return data;
    }

    return {
        blowfishDecrypt(data: number[], hash1: number[], hash2: number[]): ArrayBuffer {
            return blowfishDecryptInternal(utils.arrayToBytes(data), utils.arrayToBytes(hash1), utils.arrayToBytes(hash2));
        },
    };
}()

export function AllocObject(size: number): NativePointer {
    return _AllocObject(size, 0, 0, 0) as NativePointer;
}

export function AllocMemory(size: number, tag: number): NativePointer {
    return _AllocMemory(size, tag, 0, 0, 0) as NativePointer;
}

export function FreeMemory(p: NativePointer) {
    _FreeMemory(p);
}

export function findNameTableDataByModel(p: NativePointer, model: string): NativePointer {
    const m = Memory.allocUtf8String(model);
    return _findNameTableDataByModel(p, m);
}
