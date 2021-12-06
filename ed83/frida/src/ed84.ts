import * as utils from "./utils";
import { Modules } from "./modules";

const Addrs = (function() {
    switch (utils.getGameVersion()) {
        case 'ed84_jp':
            return {
                File_Open   : Modules.ED84.base.add(0x0ED240),
                AllocObject : Modules.ED84.base.add(0x4DAAC0),
                AllocMemory : Modules.ED84.base.add(0x52E940),
                FreeMemory  : Modules.ED84.base.add(0x52E920),
            };

        case 'ed84_us':
        default:
            return {
                File_Open : Modules.ED84.base.add(0x0ED240),
                AllocObject : Modules.ED84.base.add(0x4DAAC0),
                AllocMemory : Modules.ED84.base.add(0x52E940),
                FreeMemory  : Modules.ED84.base.add(0x52E920),
            };
    }
})();

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
}
