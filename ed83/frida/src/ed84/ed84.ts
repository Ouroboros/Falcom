import * as utils from "../utils";
import { Interceptor2 } from "../utils";
import { Addrs } from "./addrs";
import {
    ED84,
    Character,
    INameTableData,
    InvalidChrId,
    MaxPartyChrId,
    MinCustomChrId,
} from "./types";

function findReplacedNameData(chrId: number): INameTableData | undefined {
    const replacedChrId = ED84.getBattleStyle(chrId)
    return ED84.findNameTableDataByChrId(replacedChrId >= MaxPartyChrId ? replacedChrId : chrId);
}

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
    const Character_LoadFaceModel = Interceptor2.jmp(
        Addrs.Character.LoadFaceModel,
        function(chr: NativePointer, faceModel: NativePointer) {
            const char = new Character(chr);
            const nameData = ED84.findNameTableDataByModel(char.model);

            // utils.log(`model: ${char.model}`);
            // utils.log(`face: ${nameData?.faceModel}`);

            if (nameData) {
                const faceModel = nameData.faceModel;
                if (faceModel != 'null') {
                    char.presetFaceModel = faceModel;
                }
            }

            Character_LoadFaceModel(chr, faceModel);
        },
        'void', ['pointer', 'pointer'],
    );

    const Character_LoadAni = Interceptor2.jmp(
        Addrs.Character.LoadAni,
        function(chr: NativePointer, ani: NativePointer, autoCompile: number) {
            const char = new Character(chr);
            const nameData = ED84.findNameTableDataByModel(char.model);
            ani = nameData ? Memory.allocUtf8String(nameData.ani) : ani;

            // utils.log(`Character::LoadAni(${nameData?.ani})`);

            Character_LoadAni(chr, ani, 0);
        },
        'void', ['pointer', 'pointer', 'uint32'],
    );

    const Character_Initialize = Interceptor2.jmp(
        Addrs.Character.Initialize,
        function(
            chr     : NativePointer,
            model   : NativePointer,
            name    : NativePointer,
            a4      : NativePointer,
            a5      : NativePointer,
            a6      : NativePointer,
            a7      : NativePointer,
            a8      : NativePointer,
            a9      : NativePointer,
            a10     : NativePointer,
            a11     : NativePointer,
            a12     : NativePointer,
            a13     : NativePointer,
            a14     : NativePointer,
        ): NativePointer {

            const char = new Character(chr);
            const chrId = ED84.getBattleStyle(char.chrId);

            if (chrId >= MaxPartyChrId && char.modelChrId == InvalidChrId) {
                char.modelChrId = chrId;
                const nameData = findReplacedNameData(char.chrId);
                if (nameData) {
                    // utils.log(`new model: ${nameData.model}`);
                    model = Memory.allocUtf8String(nameData.model);
                }
            }

            return Character_Initialize(chr, model, name, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer'],
    );

    const Asset_LoadAsset = Interceptor2.jmp(
        Addrs.Asset.LoadAsset,
        function(a1: NativePointer, symbol: NativePointer, size: NativePointer, a4: NativePointer, a5: NativePointer): NativePointer {
            const s = symbol.readUtf8String()!;

            const s2 = ED84.getConfig().assetMap[s];
            if (s2) {
                symbol = Memory.allocUtf8String(s2);
            }

            return Asset_LoadAsset(a1, symbol, size, a4, a5);
        },
        'pointer', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer'],
    );

    const Crc32CheckSum = Interceptor2.jmp(
        Addrs.Crc32CheckSum,
        function(data: NativePointer, size: UInt64): number {
            do
            {
                if (size.valueOf() > 0x20 || size.valueOf() == 0)
                    break;

                const bytes = Buffer.from(data.readByteArray(size.valueOf())!);
                if (bytes.length == 0) {
                    // utils.log(`*** Crc32CheckSum ***(${data}, ${size.valueOf()})`);
                    break;
                }

                const nonAscii = bytes.reduce((prev, value) => (value >= 0x20 && value <= 0x7A) ? 0 : 1);
                if (nonAscii != 0)
                    break;

                const s2 = ED84.getConfig().assetMap[bytes.toString('utf8')];
                if (s2) {
                    data = Memory.allocUtf8String(s2);
                    size = new UInt64(s2.length);

                    // utils.log(`new symbol: ${s2} @ ${s2.length}`)
                }

            } while (false);

            return Crc32CheckSum(data, size);
        },
        'uint32', ['pointer', 'size_t'],
    );
}

export function main() {
    ED84.enableLogger();

    hookIoRedirection();
    hookCharacterModelInit();

    Memory.patchCode(Addrs.SaveDataChecksum, 1, (code) => {
        code.writeU8(0xEB);
    });
}
