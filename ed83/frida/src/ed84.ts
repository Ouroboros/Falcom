import * as utils from "./utils";
import { Modules } from "./modules";
import { Addrs } from "./ed84_addrs";

const _AllocObject      = new NativeFunction(Addrs.AllocObject, "pointer", ['size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _AllocMemory      = new NativeFunction(Addrs.AllocMemory, "pointer", ['size_t', 'size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _FreeMemory       = new NativeFunction(Addrs.FreeMemory, "void", ['pointer'], 'win64');

function AllocObject(size: number): NativePointer {
    return _AllocObject(size, 0, 0, 0) as NativePointer;
}

function AllocMemory(size: number, tag: number): NativePointer {
    return _AllocMemory(size, tag, 0, 0, 0) as NativePointer;
}

function FreeMemory(p: NativePointer) {
    _FreeMemory(p);
}

export function main() {
    Interceptor.attach(Addrs.File_Open, {
        onEnter: function(args) {
            const patch = utils.getPatchFile(args[1].readAnsiString()!);
            if (patch) {
                this.patch = Memory.allocAnsiString(patch);
                args[1] = this.patch;
            }
        },
    });

    Memory.patchCode(Addrs.SaveDataChecksum, 1, (code) => {
        code.writeU8(0xEB);
    });
}
