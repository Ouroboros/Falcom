import { EDBaseObject } from "../utils";

class IUnknown extends EDBaseObject {
    private _Release: NativeFunction<number, [NativePointer]>;

    constructor(impl: NativePointer) {
        super(impl);
        const vtbl = impl.readPointer();
        this._Release = new NativeFunction(vtbl.add(2 * Process.pointerSize).readPointer(), 'uint32', ['pointer'], 'stdcall');
    }

    release() {
        this._Release(this.pointer);
    }
}

interface IDirectSoundBufferDescriptor {
    flags       : number;
    bufferBytes : number;
    wfxFormat   : NativePointer;
}

export class DirectSound extends IUnknown {
    private _CreateSoundBuffer: NativeFunction<number, [NativePointer, NativePointer, NativePointer, NativePointer]>;

    constructor(impl: NativePointer) {
        super(impl);

        const vtbl = impl.readPointer();

        this._CreateSoundBuffer = new NativeFunction(vtbl.add(3 * Process.pointerSize).readPointer(), 'int32', ['pointer', 'pointer', 'pointer', 'pointer'], 'stdcall');

        console.log(`CreateSoundBuffer: ${this._CreateSoundBuffer}`);
    }

    CreateSoundBuffer(desc: IDirectSoundBufferDescriptor): DirectSoundBuffer | undefined {
        const size = 0x20 + Process.pointerSize;
        const descBuffer = Memory.alloc(size);
        const dsb = Memory.alloc(Process.pointerSize);

        /*
            0019F7BC  24 00 00 00 82 00 00 00 00 51 00 00 00 00 00 00  $...?...Q......
            0019F7CC  34 B0 0E 0A 00 00 00 00 00 00 00 00 00 00 00 00  4?.............
            0019F7DC  00 00 00 00                                      ....
        */
        descBuffer.writeU32(size);
        descBuffer.add(0x04).writeU32(desc.flags);
        descBuffer.add(0x08).writeU32(desc.bufferBytes);
        descBuffer.add(0x0C).writeU32(0);
        descBuffer.add(0x10).writePointer(desc.wfxFormat);

        const result = this._CreateSoundBuffer(this.pointer, descBuffer, dsb, NULL);
        if (result < 0)
            return undefined;

        return new DirectSoundBuffer(dsb.readPointer());
    }
}

interface IDirectSoundBuffer {
    audioPtr1   : NativePointer;
    audioBytes1 : NativePointer;
    audioPtr2   : NativePointer;
    audioBytes2 : NativePointer;
}

export class DirectSoundBuffer extends IUnknown {
    private _Lock: NativeFunction<number, [NativePointer, NativePointer, NativePointer, NativePointer, NativePointer, NativePointer, NativePointer, number]>;
    private _Play: NativeFunction<number, [NativePointer, number, number, number]>;
    private _SetVolume: NativeFunction<number, [NativePointer, number]>;
    private _Stop: NativeFunction<number, [NativePointer]>;
    private _Unlock: NativeFunction<number, [NativePointer, NativePointer, NativePointer, NativePointer, NativePointer]>;

    constructor(impl: NativePointer) {
        super(impl);

        const vtbl = impl.readPointer();

        this._Lock      = new NativeFunction(vtbl.add(11 * Process.pointerSize).readPointer(), 'int32', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'pointer', 'uint32'], 'stdcall');
        this._Play      = new NativeFunction(vtbl.add(12 * Process.pointerSize).readPointer(), 'int32', ['pointer', 'uint32', 'uint32', 'uint32'], 'stdcall');
        this._SetVolume = new NativeFunction(vtbl.add(15 * Process.pointerSize).readPointer(), 'int32', ['pointer', 'uint32'], 'stdcall');
        this._Stop      = new NativeFunction(vtbl.add(18 * Process.pointerSize).readPointer(), 'int32', ['pointer'], 'stdcall');
        this._Unlock    = new NativeFunction(vtbl.add(19 * Process.pointerSize).readPointer(), 'int32', ['pointer', 'pointer', 'pointer', 'pointer', 'pointer'], 'stdcall');
    }

    lock(offset: NativePointer, sizeInBytes: NativePointer, flags: number): IDirectSoundBuffer | undefined {
        const dsbBuffer     = Memory.alloc(4 * Process.pointerSize);
        const audioPtr1     = dsbBuffer.add(0);
        const audioBytes1   = dsbBuffer.add(Process.pointerSize);
        const audioPtr2     = dsbBuffer.add(Process.pointerSize * 2);
        const audioBytes2   = dsbBuffer.add(Process.pointerSize * 3);

        const result = this._Lock(this.pointer, offset, sizeInBytes, audioPtr1, audioBytes1, audioPtr2, audioBytes2, flags);

        if (result < 0)
            return undefined;

        return {
            audioPtr1   : audioPtr1.readPointer(),
            audioBytes1 : audioBytes1.readPointer(),
            audioPtr2   : audioPtr2.readPointer(),
            audioBytes2 : audioBytes2.readPointer(),
        };
    }

    play(flags: number) {
        this._Play(this.pointer, 0, 0, flags);
    }

    setVolume(volume: number) {
        this._SetVolume(this.pointer, volume);
    }

    stop() {
        this._Stop(this.pointer);
    }

    unlock(dsb: IDirectSoundBuffer) {
        this._Unlock(this.pointer, dsb.audioPtr1, dsb.audioBytes1, dsb.audioPtr2, dsb.audioBytes2);
    }
}
