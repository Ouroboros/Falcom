import * as utils from "./utils";
import { Modules, Addrs } from "./modules";
import * as ED83 from "./ed83";

rpc.exports = function () {
    function blowfishDecryptInternal(data: ArrayBuffer, hash1: ArrayBuffer, hash2: ArrayBuffer): ArrayBuffer {
        ED83.BlowfishDecode(data, hash1, hash2);
        return data;
    }

    return {
        blowfishDecrypt(data: number[], hash1: number[], hash2: number[]): ArrayBuffer {
            return blowfishDecryptInternal(utils.arrayToBytes(data), utils.arrayToBytes(hash1), utils.arrayToBytes(hash2));
        },
    };
}()

function ED83ScriptLoad(self: NativePointer, path: NativePointer, type: UInt64, log: boolean): NativePointer {
    const loader = new ED83.ScriptLoader(self);
    let buffer = loader.buffer;

    if (buffer.isNull() == false) {
        ED83.FreeMemory(buffer);
        loader.buffer = NULL;
    }

    loader.reset();

    if (loader.disabled) {
        return NULL;
    }

    let filePath = path.readUtf8String()!;

    if (filePath.slice(0, 5) == 'data/') {
        filePath = 'data_cn/' + filePath.slice(5);
    }

    utils.log(`Script::load: ${filePath}`);

    const data = utils.readFileContent(filePath);

    if (data == null) {
        utils.log(`Script::load failed: ${filePath}`);
    }

    buffer = ED83.AllocMemory(data!.byteLength, 1);
    buffer.writeByteArray(data!);

    loader.buffer = buffer;
    loader.bufferBase = buffer;
    loader.type = type;
    loader.name = buffer.add(buffer.add(4).readU32()).readUtf8String()!;

    return buffer;
}

function ED83ScriptLoad2(self: NativePointer, path: NativePointer): NativePointer {
    let filePath = path.readUtf8String()!;

    if (filePath.slice(0, 5) != 'data/') {
        return NULL;
    }

    filePath = 'data_cn/' + filePath.slice(5);

    const data = utils.readFileContent(filePath);

    if (data == null) {
        utils.log(`Script::load failed: ${filePath}`);
        return NULL;
    }

    utils.log(`Script::load: ${filePath}`);

    const loader = new ED83.ScriptLoader(self);
    let buffer = loader.buffer;

    if (buffer.isNull() == false) {
        ED83.FreeMemory(buffer);
        loader.buffer = NULL;
    }

    buffer = ED83.AllocMemory(data!.byteLength, 1);
    buffer.writeByteArray(data!);

    loader.buffer = buffer;
    loader.bufferBase = buffer;

    return buffer;
}

function test_ed83() {
    // Interceptor.attach(Modules.KERNEL32.getExportByName("CreateFileW"), {
    //     onEnter: function (args) {
    //         const fileName = args[0].readUtf16String();
    //     },
    //     onLeave: function (retval) {
    //     },
    // });

    // Interceptor.attach(Addrs.ScriptLoad, {
    //     onEnter: function (args) {
    //         ED83ScriptLoad(args[0] as NativePointer, args[1] as NativePointer, uint64(args[2]), Boolean(args[3]));
    //     },
    //     onLeave: function (retval) {
    //     },
    // });

    // return;

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

    // Interceptor.replace(
    //     Addrs.ScriptLoad,
    //     new NativeCallback((self: NativePointer, path: NativePointer, type: UInt64, log: boolean): NativePointer => {
    //             return ED83ScriptLoad(self, path, type, log);
    //         },
    //         'pointer',
    //         ['pointer', 'pointer', 'uint64', 'bool'],
    //         'win64',
    //     ),
    // );

    Interceptor.attach(Addrs.ScriptLoad, {
        onEnter: function(args) {
            this.self = args[0];
            this.path = args[1];
        },
        onLeave: function(retval) {
            const ret = ED83ScriptLoad2(this.self, this.path);
            if (ret.isNull() == false)
                retval.replace(ret);
        },
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

console.log();
test_ed83();
