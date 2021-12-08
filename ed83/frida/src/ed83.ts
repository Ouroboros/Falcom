import * as utils from "./utils";
import { Addrs } from "./ed83_addrs";
import { AllocMemory, FreeMemory } from "./ed83_utils";
import { ScriptLoader, Character, ED83 } from "./ed83_types";

function ED83ScriptLoad(self: NativePointer, path: NativePointer): NativePointer {
    let filePath = path.readAnsiString()!;

    if (filePath.slice(0, 5) != 'data/') {
        return NULL;
    }

    let data = utils.loadPatchFile(filePath);

    if (data == null) {
        filePath = 'data_cn/' + filePath.slice(5);
        data = utils.readFileContent(filePath);
    }

    if (data == null) {
        utils.log(`Script::load failed: ${filePath}`);
        return NULL;
    }

    // utils.log(`Script::load: ${filePath}`);

    const loader = new ScriptLoader(self);
    let buffer = loader.buffer;

    if (buffer.isNull() == false) {
        FreeMemory(buffer);
        loader.buffer = NULL;
    }

    buffer = AllocMemory(data!.byteLength, 1);
    buffer.writeByteArray(data!);

    loader.buffer = buffer;
    loader.bufferBase = buffer;

    return buffer;
}

export function main() {
    // Interceptor.attach(Addrs.Logger_Output, {
    //     onEnter: function(args) {
    //         const buf = args[2].readUtf8String()!;
    //         if (buf.substring(buf.length - 1) == '\n') {
    //             utils.log(buf.substring(0, buf.length - 1));
    //         } else {
    //             utils.log(buf);
    //         }
    //     },
    // });

    Interceptor.attach(Addrs.Character.ChangeSkinFinished, function() {
        const ctx = this.context as X64CpuContext;
        const char = new Character(ctx.rcx);
        const nameData = ED83.findNameTableDataByModel(char.model);

        if (!nameData)
            return;

        char.loadAni(nameData.ani);
    });

    Interceptor.attach(Addrs.ScriptLoad, {
        onEnter: function(args) {
            this.self = args[0];
            this.path = args[1];
        },
        onLeave: function(retval) {
            const ret = ED83ScriptLoad(this.self, this.path);
            if (ret.isNull() == false)
                retval.replace(ret);
        },
    });

    Interceptor.attach(Addrs.LoadTableData, {
        onEnter: function(args) {
            const self      = args[0];
            const path      = args[1].readAnsiString()!;
            const nodat     = args[2].toInt32() != 0;
            const fullpath  = args[3].toInt32() != 0;

            let p = path;

            if (fullpath == false) {
                if (nodat) {
                    p = `data/text/${path}.tbl`;
                } else {
                    p = `data/text/dat/${path}.tbl`;
                }
            }

            // utils.log(`LoadTableData: ${p}`);

            const patch = utils.getPatchFile(p)
            if (!patch)
                return;

            this.path = Memory.allocUtf8String(patch);

            const tls = utils.getTLS();

            tls.disableDecrypt = true;
            tls.patchFileName = patch;
        },
        onLeave: function(retval) {
            const tls = utils.getTLS();
            tls.disableDecrypt = false;
            tls.patchFileName = '';
        }
    });

    Interceptor.attach(Addrs.BlowFish_Decode, {
        onEnter: function(args) {
            if (utils.getTLS().disableDecrypt) {
                args[2] = NULL;     // size
            }
        },
    });

    Interceptor.attach(Addrs.File_Open, {
        onEnter: function(args) {
            const patch = utils.getTLS().patchFileName;
            if (patch) {
                this.path = Memory.allocAnsiString(patch);
                args[1] = this.path;
            } else {
                const patch = utils.getPatchFile(args[1].readAnsiString()!);
                if (patch) {
                    this.patch = Memory.allocAnsiString(patch);
                    args[1] = this.patch;
                }
            }
        },
    });

    Memory.patchCode(Addrs.DLC_Check, 1, (code) => {
        code.writeU8(0xEB);
    });

    // Interceptor.attach(Addrs.ScriptVMExecute, {
    //     onEnter: function(args) {
    //         const p = args[1];
    //         const scriptName = p.add(0x14).readUtf8String()!;
    //         const currentFunction = p.add(0x34).readUtf8String()!;
    //         const offset = p.add(0x78).readU32();

    //         if (offset == 0) return;

    //         // utils.log('%s %s 0x%08X', scriptName, currentFunction, offset);
    //     },
    // });

    const recorded: any = {};

    // Interceptor.attach(Addrs.ScriptGetFunctionByName, {
    //     onEnter: function(args) {
    //         const p = args[1];
    //         const scriptHeader = args[0].add(0x6B8).readPointer();
    //         const scriptName = scriptHeader.add(0x20).readUtf8String()!;
    //         const funcName = p.readUtf8String()!;

    //         const name = `${scriptName}.${funcName}`;

    //         if (funcName != 'FieldMonsterData') return;

    //         if (recorded[name])
    //             return;

    //         recorded[name] = true;

    //         this.name = name;
    //     },
    //     onLeave: function(retval) {
    //         if (!this.name)
    //             return;

    //         utils.log(`ScriptGetFunctionByName: ${this.name} = ${retval}`);
    //     },
    // });
}
