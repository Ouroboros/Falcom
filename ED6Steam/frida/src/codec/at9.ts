import * as utils from "../utils";
import { ArrayBuffer2 } from "../utils";

const at9API = (function() {
    const dll = Module.load('libatrac9.dll');
    return {
        Atrac9DecodeBuffer: new NativeFunction(dll.getExportByName('Atrac9DecodeBuffer'), 'int32', ['pointer', 'int32', 'pointer', 'pointer', 'pointer', 'pointer'], 'stdcall'),
        Atrac9FreeBuffer: new NativeFunction(dll.getExportByName('Atrac9FreeBuffer'), 'void', ['pointer'], 'stdcall'),
    };
})()

export interface AT9DecodeResult {
    pcm         : NativePointer;
    wfxFormat   : NativePointer;
    data        : NativePointer;
    dataSize    : number;
}

export class AT9Decoder {
    static decode(at9: ArrayBuffer2): AT9DecodeResult | undefined {
        // const buffer    = Memory.alloc(Process.pointerSize);
        // const size      = Memory.alloc(4);
        // const wfxFormat = Memory.alloc(4);
        // const data      = Memory.alloc(4);

        const buf       = Memory.alloc(Process.pointerSize + 4 * 3);
        const buffer    = buf;
        const size      = buffer.add(Process.pointerSize)
        const wfxFormat = size.add(4);
        const data      = wfxFormat.add(4);

        const ret = at9API.Atrac9DecodeBuffer(at9.ptr, at9.byteLength, buffer, size, wfxFormat, data);
        if (ret != 0) {
            console.log(`decode at9 return ${ret}`);
            return undefined;
        }

        const p = buffer.readPointer();
        const pcm = Memory.alloc(size.readU32());

        pcm.writeByteArray(p.readByteArray(size.readU32())!);

        const result = {
            pcm         : pcm,
            wfxFormat   : pcm.add(wfxFormat.readU32()),
            data        : pcm.add(data.readU32()),
            dataSize    : 0,
        };

        result.dataSize = result.data.sub(4).readU32();

        at9API.Atrac9FreeBuffer(p);

        return result;
    }
}
