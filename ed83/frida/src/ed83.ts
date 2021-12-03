import * as utils from "./utils";
import { Modules } from "./modules";
import { Offsets } from "./consts";

const Addrs = {
    LoadTableData           : Modules.ED83.base.add(0x2817F0),
    ScriptLoad              : Modules.ED83.base.add(0x3C91B0),
    ScriptVMExecute         : Modules.ED83.base.add(0x3C6DA0),
    ScriptGetFunctionByName : Modules.ED83.base.add(0x3C7FF0),
    Logger_Output           : Modules.ED83.base.add(0x11D160),

    BlowFish_Decode         : Modules.ED83.base.add(0x20CAA0),

    File_Open               : Modules.ED83.base.add(0xF5920),

    DLC_Check               : Modules.ED83.base.add(0x3A8359),
};

const _AllocObject      = new NativeFunction(Modules.ED83.base.add(0x4DAAC0), "pointer", ['size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _AllocMemory      = new NativeFunction(Modules.ED83.base.add(0x5DFE70), "pointer", ['size_t', 'size_t', 'size_t', 'size_t', 'size_t'], 'win64');
const _BlowfishInit     = new NativeFunction(Modules.ED83.base.add(0x20C730), "void", ['pointer', 'pointer', 'size_t'], 'win64');
const _BlowfishInit2    = new NativeFunction(Modules.ED83.base.add(0x20CAC0), "void", ['pointer', 'pointer'], 'win64');
const _BlowfishDecode   = new NativeFunction(Modules.ED83.base.add(0x20CAA0), "void", ['pointer', 'pointer', 'size_t', 'int'], 'win64');
const _FreeMemory       = new NativeFunction(Modules.ED83.base.add(0x4DAA50), "void", ['pointer'], 'win64');

function AllocObject(size: number): NativePointer {
    return _AllocObject(size, 0, 0, 0) as NativePointer;
}

function AllocMemory(size: number, tag: number): NativePointer {
    return _AllocMemory(size, tag, 0, 0, 0) as NativePointer;
}

function FreeMemory(p: NativePointer) {
    _FreeMemory(p);
}

function BlowfishDecode(data: ArrayBuffer, key1: ArrayBuffer, key2: ArrayBuffer) {
    const bf = AllocObject(0x1444);

    _BlowfishInit(bf, key2.unwrap(), 8);
    _BlowfishInit2(bf, key1.unwrap());

    _BlowfishDecode(bf, data.unwrap(), data.byteLength, 0);

    FreeMemory(bf);
}

class ScriptLoader {
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

class TableLoader {
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


function ED83ScriptLoad(self: NativePointer, path: NativePointer): NativePointer {
    let filePath = path.readAnsiString()!;

    if (filePath.slice(0, 5) != 'data/') {
        return NULL;
    }

    let data = utils.loadPatchFile(filePath);

    if (data == null) {
        filePath = 'data_cn/' + filePath.slice(5);
        data = utils.readFileContent(filePath);
    }

    if (data == null) {
        utils.log(`Script::load failed: ${filePath}`);
        return NULL;
    }

    // utils.log(`Script::load: ${filePath}`);

    const loader = new ScriptLoader(self);
    let buffer = loader.buffer;

    if (buffer.isNull() == false) {
        FreeMemory(buffer);
        loader.buffer = NULL;
    }

    buffer = AllocMemory(data!.byteLength, 1);
    buffer.writeByteArray(data!);

    loader.buffer = buffer;
    loader.bufferBase = buffer;

    return buffer;
}

export function main() {
    // Interceptor.attach(Addrs.Logger_Output, {
    //     onEnter: function(args) {
    //         const buf = args[2].readUtf8String()!;
    //         if (buf.substring(buf.length - 1) == '\n') {
    //             utils.log(buf.substring(0, buf.length - 1));
    //         } else {
    //             utils.log(buf);
    //         }
    //     },
    // });

    Interceptor.attach(Addrs.ScriptLoad, {
        onEnter: function(args) {
            this.self = args[0];
            this.path = args[1];
        },
        onLeave: function(retval) {
            const ret = ED83ScriptLoad(this.self, this.path);
            if (ret.isNull() == false)
                retval.replace(ret);
        },
    });

    Interceptor.attach(Addrs.LoadTableData, {
        onEnter: function(args) {
            const self      = args[0];
            const path      = args[1].readAnsiString()!;
            const nodat     = args[2].toInt32() != 0;
            const fullpath  = args[3].toInt32() != 0;

            let p = path;

            if (fullpath == false) {
                if (nodat) {
                    p = `data/text/${path}.tbl`;
                } else {
                    p = `data/text/dat/${path}.tbl`;
                }
            }

            // utils.log(`LoadTableData: ${p}`);

            const patch = utils.getPatchFile(p)
            if (!patch)
                return;

            this.path = Memory.allocUtf8String(patch);

            const tls = utils.getTLS();

            tls.disableDecrypt = true;
            tls.patchFileName = patch;
        },
        onLeave: function(retval) {
            const tls = utils.getTLS();
            tls.disableDecrypt = false;
            tls.patchFileName = '';
        }
    });

    Interceptor.attach(Addrs.BlowFish_Decode, {
        onEnter: function(args) {
            if (utils.getTLS().disableDecrypt) {
                args[2] = NULL;     // size
            }
        },
    });

    Interceptor.attach(Addrs.File_Open, {
        onEnter: function(args) {
            const patch = utils.getTLS().patchFileName;
            if (patch) {
                this.path = Memory.allocUtf8String(patch);
                args[1] = this.path;
            }
        },
    });

    Memory.patchCode(Addrs.DLC_Check, 1, (code) => {
        code.writeU8(0xEB);
    });

    // Interceptor.attach(Addrs.ScriptVMExecute, {
    //     onEnter: function(args) {
    //         const p = args[1];
    //         const scriptName = p.add(0x14).readUtf8String()!;
    //         const currentFunction = p.add(0x34).readUtf8String()!;
    //         const offset = p.add(0x78).readU32();

    //         if (offset == 0) return;

    //         // utils.log('%s %s 0x%08X', scriptName, currentFunction, offset);
    //     },
    // });

    const recorded: any = {};

    // Interceptor.attach(Addrs.ScriptGetFunctionByName, {
    //     onEnter: function(args) {
    //         const p = args[1];
    //         const scriptHeader = args[0].add(0x6B8).readPointer();
    //         const scriptName = scriptHeader.add(0x20).readUtf8String()!;
    //         const funcName = p.readUtf8String()!;

    //         const name = `${scriptName}.${funcName}`;

    //         if (funcName != 'FieldMonsterData') return;

    //         if (recorded[name])
    //             return;

    //         recorded[name] = true;

    //         this.name = name;
    //     },
    //     onLeave: function(retval) {
    //         if (!this.name)
    //             return;

    //         utils.log(`ScriptGetFunctionByName: ${this.name} = ${retval}`);
    //     },
    // });
}
