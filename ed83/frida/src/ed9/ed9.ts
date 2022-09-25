import * as utils from "../utils";
import { API, Modules } from "../modules";
import { Addrs } from "./addrs";
import { Interceptor2 } from "../utils";

rpc.exports = function() {
    let lastFile = NULL;
    const arg1 = ptr(0x1407AD3B0);
    const load_file = new NativeFunction(ptr(0x1404126B0), 'pointer', ['pointer', 'pointer', 'uint32']);
    const release1 = new NativeFunction(ptr(0x140451760), 'pointer', ['pointer', 'pointer']);
    const release2 = new NativeFunction(ptr(0x140412AF0), 'pointer', ['pointer', 'pointer']);
    const free_memory = new NativeFunction(ptr(0x14060D3D0), 'pointer', ['pointer', 'uint32']);

    return {
        loadFile: function(filename: string) {
            if (!lastFile.isNull()) {
                release1(arg1.readPointer().add(0x68), lastFile.add(0x90).readPointer());
                release2(arg1.readPointer().add(0x08), lastFile.add(0x84));
                free_memory(lastFile, 0xA0);
                lastFile = NULL;
            }

            const ret = load_file(arg1.readPointer(), Memory.allocUtf8String(filename), 0);
            if (ret.isNull()) {
                // return undefined;
                throw new Error(`load failed: ${filename}`);
            }

            lastFile = ret;

            const size = ret.add(0x98).readU64();
            const pointer = ret.add(0x90).readPointer();
            const data = pointer.readByteArray(size.valueOf())!;

            return data;
        },
    };
}();

function hex(v: number): string {
    return `0x${v.toString(16).padStart(8, '0')}`
}

function hookSteamAndMisc() {
    // Interceptor.attach(ptr(0x1404126B0), {
    //     onEnter: function(args) {
    //         const filename = args[1].readUtf8String()!;

    //         console.log(`${filename}`);
    //     },
    // });
}

function hookIoRedirection() {
    const File_GetRecirectPath = Interceptor2.jmp(
        Addrs.File.GetRecirectPath,
        function(arg1: NativePointer, path: NativePointer) {
            const patch = utils.getPatchFile2(path.readAnsiString()!);

            if (!patch) {
                File_GetRecirectPath(arg1, path);
                return;
            }

            utils.log(`patch ${patch}`);

            path.writeUtf8String(patch);
        },
        'void', ['pointer', 'pointer'],
    );

}

export function main() {
    // (new NativeFunction(Process.getModuleByName('KERNEL32.dll').getExportByName('AllocConsole'), 'bool', []))();

    // console.log('sc dx9 patchModuleText');
    // utils.patchModuleText(Modules.ED6SC, ExeText);

    console.log('hookSteamAndMisc');
    hookSteamAndMisc();

    // console.log('hookEncodingCheck');
    // hookEncodingCheck();

    // console.log('hookWindow');
    // hookWindow();

    console.log('hookIoRedirection');
    hookIoRedirection();

    // console.log('hookTextRenderer');
    // hookTextRenderer();

    // console.log('hookTalk');
    // hookTalk();

    console.log('done');
}
