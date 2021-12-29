import { Addrs } from "./ed84_addrs";
import { ED8BaseObject, Interceptor2 } from "./utils";
import * as utils from "./utils";

export const MaxPartyChrId = 0x30;
export const MinCustomChrId = 0x2000;
export const InvalidChrId = 0xFFFF;

export class ED84 extends ED8BaseObject {
    private static _sharedInstance: ED84;

    static get sharedInstance(): ED84 {
        if (this._sharedInstance)
            return this._sharedInstance;

        const p = NULL;

        if (p.isNull()) {
            throw new Error('ED84 null');
        }

        this._sharedInstance = new ED84(p);
        return this._sharedInstance;
    }

    static enableLogger() {
        Interceptor2.jmp(
            Addrs.Logger_Ansi2UTF8,
            function(output: NativePointer, outputSize: NativePointer, input: NativePointer) {
                const s = input.readUtf8String()!
                output.writeUtf8String(s.slice(0, outputSize.toUInt32()));
            },
            'void', ['pointer', 'pointer', 'pointer'],
        );

        const Logger_Output = Interceptor2.jmp(
            Addrs.Logger_Output,
            function(self: NativePointer, level: NativePointer, buffer: NativePointer) {
                const buf = buffer.readUtf8String()!;
                if (buf.substring(buf.length - 1) == '\n') {
                    utils.log(buf.substring(0, buf.length - 1));
                } else {
                    utils.log(buf);
                }

                Logger_Output(self, level, buffer);
            },
            'void', ['pointer', 'pointer', 'pointer'],
        );
    }
}
