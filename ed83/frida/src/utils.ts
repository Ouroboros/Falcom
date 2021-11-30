import { sprintf, vsprintf } from "sprintf-js";
import { API, Modules } from "./modules";

const Logging = !false;

export function log(format: string, ...args: any[]): void {
    if (!Logging)
        return;

    if (args.length != 0) {
        format = vsprintf(format, args);
    }

    const now = new Date;
    const time = sprintf('%02d:%02d:%02d.%03d', now.getHours(), now.getMinutes(), now.getSeconds(), now.getMilliseconds());
    console.log(`${time} ${format}`);
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
