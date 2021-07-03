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

    let filePath = path.readUtf8String()!.replace('data/', 'data_cn/');

    if (filePath.slice(0, 5) == 'data/') {
        filePath = 'data_cn/' + filePath.slice(5);
    }

    utils.log(`Script::load: ${filePath}`);

    const data = utils.readFileContent(filePath)!;

    buffer = ED83.AllocMemory(data.byteLength, 1);
    buffer.writeByteArray(data);

    loader.buffer = buffer;
    loader.bufferBase = buffer;
    loader.type = type;
    loader.name = buffer.add(buffer.add(4).readU32()).readUtf8String()!;

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

    Interceptor.replace(
        Addrs.ScriptLoad,
        new NativeCallback((self: NativePointer, path: NativePointer, type: UInt64, log: boolean): NativePointer => {
                return ED83ScriptLoad(self, path, type, log);
            },
            'pointer',
            ['pointer', 'pointer', 'uint64', 'bool'],
            'win64',
        ),
    );
}

console.log();
test_ed83();
