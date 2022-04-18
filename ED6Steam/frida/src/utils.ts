import { sprintf, vsprintf } from "sprintf-js";
import { API } from "./modules";

const Logging = !false;

export class EDBaseObject {
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

    readByteArray(offset: number, length: number): ArrayBuffer | null {
        return this.impl.add(offset).readByteArray(length);
    }

    writeU16(offset: number, value: number) {
        this.impl.add(offset).writeU16(value);
    }

    writeU32(offset: number, value: number) {
        this.impl.add(offset).writeU32(value);
    }
}

export class ED8Vector extends EDBaseObject {
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
        abi: NativeABI,
    ) {
        Interceptor.replace(target, new NativeCallback(replacement, retType, argTypes, abi));
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
        abi: NativeABI,
    ) {
        const stub = new NativeFunction(target, retType, argTypes);
        Interceptor.replace(target, new NativeCallback(replacement, retType, argTypes, abi));
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

export function readMBCS(p: NativePointer, encoding: string, length?: number): string {
    const len = length ? length : API.crt.strlen(p);
    if (len == 0)
        return '';

    const codePage = ({
        gbk     : 936,
        sjis    : 932,
    })[encoding];

    if (!codePage)
        return `<unknown encoding: ${encoding}>`;

    const wchar = Memory.alloc((len + 1) * 2);
    const ret = API.WIN32.MultiByteToWideChar(codePage, 0, p, len, wchar, len);
    wchar.add(ret * 2).writeU16(0);

    return wchar.readUtf16String()!;
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

export function getNtHeaders(base?: NativePointer): NativePointer {
    base = base ? base : Process.enumerateModules()[0].base;
    return base.add(base.add(0x3C).readU32());
}

export function getSectionHeaders(base?: NativePointer): NativePointer[] {
    const header = getNtHeaders(base);
    const numberOfSections = header.add(6).readU16();
    const sizeOfOptionalHeader = header.add(0x14).readU16();
    const sectionHeader = header.add(0x18 + sizeOfOptionalHeader);

    return new Array<NativePointer>(numberOfSections).fill(NULL).map((_, index) => {return sectionHeader.add(index * 0x28)});
}

export function getGameVersion(): string {
    const header = getNtHeaders();
    const timestamp = header.add(8).readU32();

    switch (timestamp) {
        case 0x590BDEA4: return 'ed6fc';
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

interface IModuleText {
    rva : string;
    text: string;
    // ptr : NativePointer;
}

export function patchModuleText(module: Module, text: IModuleText[]) {
    const sections = getSectionHeaders(module.base);
    const textSection = sections[0];
    const dotData = Buffer.from([0x2E, 0x64, 0x61, 0x74, 0x61, 0x00]);

    const dataSection = sections.filter((s) => {
        return Buffer.from(s.readByteArray(6)!).equals(dotData);
    })[0];

    const textStart = module.base.add(textSection.add(0x0C).readU32());
    const textSize  = textSection.add(0x10).readU32();
    const dataStart = dataSection ? module.base.add(dataSection.add(0x0C).readU32()) : undefined;
    const dataSize  = dataSection ? dataSection.add(0x10).readU32() : undefined;

    for (let e of text) {
        const va = module.base.add(parseInt(e.rva, 16));
        const pattern = new Array<String>(Process.pointerSize).fill('').map((_, index) => {return va.shr(index * 8).and(0xFF).toString(16).padStart(2, '0')}).join(' ');

        let ptr: NativePointer;

        function getptr() {
            if (ptr !== undefined)
                return ptr;

            ptr = API.crt.malloc(e.text.length * 2 + 1);
            ptr.writeAnsiString(e.text);
            return ptr;
        }

        for (let addr of Memory.scanSync(textStart, textSize, pattern)) {
            const address = addr.address;

            if ((address.sub(1).readU8() & 0xF0) == 0xB0 ||
                 address.sub(1).readU8() == 0x68 ||
                 address.sub(4).readU16() == 0x44C7
            ) {
                // console.log(`patch text: ${address} ${e.text} @ ${va} @ ${pattern}`);

                Memory.patchCode(address, addr.size, (code) => {
                    code.writePointer(getptr());
                });
            }
        }

        if (!dataStart || !dataSize)
            continue;

        for (let addr of Memory.scanSync(dataStart, dataSize, pattern)) {
            const address = addr.address;

            // console.log(`patch data: ${address} ${e.text} @ ${va} @ ${pattern}`);

            address.writePointer(getptr());
        }
    }
}
