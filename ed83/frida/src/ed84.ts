import * as utils from "./utils";
import { Interceptor2 } from "./utils";
import { Addrs } from "./ed84_addrs";
import {
    ED84,
} from "./ed84_types";

function hookIoRedirection() {
    const File_Open = Interceptor2.jmp(
        Addrs.File.Open,
        function(self: NativePointer, path: NativePointer, mode: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readAnsiString()!);
            if (patch) {
                path = Memory.allocAnsiString(patch);
            }

            return File_Open(self, path, mode);
        },
        'pointer', ['pointer', 'pointer', 'pointer'],
    );

    const File_GetSize = Interceptor2.jmp(
        Addrs.File.GetSize,
        function(self: NativePointer, path: NativePointer, arg3: NativePointer, fileSize: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readAnsiString()!);
            if (patch) {
                path = Memory.allocAnsiString(patch);
            }

            return File_GetSize(self, path, arg3, fileSize);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer'],
    );
}

function hookCharacterModelInit() {

}

export function main() {
    ED84.enableLogger();

    hookIoRedirection();
    hookCharacterModelInit();

    Memory.patchCode(Addrs.SaveDataChecksum, 1, (code) => {
        code.writeU8(0xEB);
    });
}
