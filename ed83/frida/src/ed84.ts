import * as utils from "./utils";
import { Interceptor2 } from "./utils";
import { Addrs } from "./ed84_addrs";
import {
    ED84,
} from "./ed84_types";

function hookFileRedirection() {
    const File_Open = Interceptor2.jmp(
        Addrs.File_Open,
        function(self: NativePointer, path: NativePointer, mode: NativePointer): NativePointer {
            const patch = utils.getPatchFile(path.readAnsiString()!);
            if (patch) {
                path = Memory.allocAnsiString(patch);
            }

            return File_Open(self, path, mode);
        },
        'pointer', ['pointer', 'pointer', 'pointer'],
    );
}

export function main() {
    ED84.enableLogger();

    hookFileRedirection();

    Memory.patchCode(Addrs.SaveDataChecksum, 1, (code) => {
        code.writeU8(0xEB);
    });
}
