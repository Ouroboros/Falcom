import { sprintf, vsprintf } from "sprintf-js";
import { API } from "./modules";

const Logging = !false;

export class ED8BaseObject {
    private impl: NativePointer;

    constructor(impl: NativePointer) {
        this.impl = impl;
    }

    get pointer(): NativePointer {
        return this.impl;
    }

    readPointer(offset: number): NativePointer {
        return this.impl.add(offset).readPointer();
    }

    readU8(offset: number): number {
        return this.impl.add(offset).readU8();
    }

    readU16(offset: number): number {
        return this.impl.add(offset).readU16();
    }

    readU32(offset: number): number {
        return this.impl.add(offset).readU32();
    }

    readFloat(offset: number): number {
        return this.impl.add(offset).readFloat();
    }

    readUtf8String(offset: number): string | null {
        return this.impl.add(offset).readUtf8String();
    }

    writeU16(offset: number, value: number) {
        this.impl.add(offset).writeU16(value);
    }

    writeU32(offset: number, value: number) {
        this.impl.add(offset).writeU32(value);
    }
}

export class ED8Vector extends ED8BaseObject {
    get size(): number {
        return this.readU32(0x00);
    }

    get ptr(): NativePointer {
        return this.readPointer(0x08);
    }
}

export class Interceptor2 {
    static call<RetType extends NativeCallbackReturnType, ArgTypes extends NativeCallbackArgumentType[] | []> (
        target: NativePointerValue,
        replacement: NativeCallbackImplementation<
                GetNativeCallbackReturnValue<RetType>,
                Extract<GetNativeCallbackArgumentValue<ArgTypes>, unknown[]>
            >,
        retType: RetType,
        argTypes: ArgTypes,
    ) {
        Interceptor.replace(target, new NativeCallback(replacement, retType, argTypes, 'win64'));
        Interceptor.flush();
        Memory.patchCode(target, 1, (code: NativePointer) => {
            code.writeU8(0xE8);
        });
    }

    static jmp<RetType extends NativeCallbackReturnType, ArgTypes extends NativeCallbackArgumentType[] | []> (
        target: NativePointerValue,
        replacement: NativeCallbackImplementation<
                GetNativeCallbackReturnValue<RetType>,
                Extract<GetNativeCallbackArgumentValue<ArgTypes>, unknown[]>
            >,
        retType: RetType,
        argTypes: ArgTypes,
    ) {
        const stub = new NativeFunction(target, retType, argTypes);
        Interceptor.replace(target, new NativeCallback(replacement, retType, argTypes, 'win64'));
        return stub;
    }
}

export function log(format: string, ...args: any[]): void {
    if (!Logging)
        return;

    if (args.length != 0) {
        format = vsprintf(format, args);
    }

    const now = new Date;
    const offset = (8 * 3600 - now.getTimezoneOffset()) / 3600;
    const time = sprintf('%02d:%02d:%02d.%03d', now.getHours() + offset, now.getMinutes(), now.getSeconds(), now.getMilliseconds());
    const msg = `${time} ${format}`;
    console.log(msg);
    send({msg: 'log', data: msg});
}

export function arrayToBytes(data: number[]): ArrayBuffer {
    const p = Memory.alloc(data.length);
    p.writeByteArray(data);

    const buf = ArrayBuffer.wrap(p, data.length);
    (buf as any).ptr = p;

    return buf;
}

export function ptrToBytes(addr: NativePointer, size: number): ArrayBuffer {
    const buf = ArrayBuffer.wrap(addr, size);
    (buf as any).ptr = addr;
    return buf;
}

export function UTF16(s: string): NativePointer {
    return s ? Memory.allocUtf16String(s) : NULL;
}

export function UTF8(s: string): NativePointer {
    return s ? Memory.allocUtf8String(s) : NULL;
}

export function readFileContent(path: string): ArrayBuffer | null {
    const fp = API.crt.fopen(UTF8(path), UTF8('rb')) as NativePointer;
    if (fp.isNull()) {
        return null;
    }

    const fileSize = API.crt._filelengthi64(API.crt._fileno(fp)) as UInt64;

    const p = Memory.alloc(fileSize);

    const bytesRead = API.crt.fread(p, fileSize, 1, fp);

    API.crt.fclose(fp);

    return ptrToBytes(p, fileSize.toNumber());
}

export function isPathExists(path: string): boolean {
    const INVALID_FILE_ATTRIBUTES = 0xFFFFFFFF;
    return API.WIN32.GetFileAttributesA(Memory.allocAnsiString(path)) != INVALID_FILE_ATTRIBUTES;
}

class TLS {
    disableDecrypt  : boolean = false;
    patchFileName   : string = '';
}

const tls: {[key: number]: TLS} = {};

export function getTLS(): TLS {
    const tid = Process.getCurrentThreadId();

    if (!tls[tid])
        tls[tid] = new TLS;

    return tls[tid];
}

export function getGameVersion(): string {
    const exe = Process.enumerateModules()[0].base;

    const header = exe.add(exe.add(0x3C).readU32());
    const timestamp = header.add(8).readU32();

    switch (timestamp) {
        case 0x6079B2A5: return 'ed84_jp';
        case 0x6079B1DF: return 'ed84_us';
        case 0x60767137: return 'ed83_cn';
        case 0x62DA17AE: return 'ed9';
    }

    throw new Error('unknown game version');
}

let patchDirs = [
    'patch/',
    'ouroboros/',
    'data_cn/',
];

export function setPatchDirs(dirs: string[]) {
    if (dirs?.length) {
        patchDirs = dirs;
        log(`new patch dirs: ${patchDirs}`);
    }
}

export function getPatchFile(path: string): string | null {
    if (path.slice(0, 5) != 'data/') {
        return null;
    }

    for (let dir of patchDirs) {
        const patchPath = dir + path.slice(5);
        if (isPathExists(patchPath)) {
            // log(`patch: ${patchPath}`);
            return patchPath;
        }
    }

    return null;
}

export function loadPatchFile(path: string): ArrayBuffer | null {
    const patchPath = getPatchFile(path);

    if (!patchPath)
        return null;

    let data = readFileContent(patchPath);

    return data;
}
