import * as utils from "../utils";
import { API } from "../modules";

const dwriteRendererAPI = (function() {
    const dll = Module.load('DWriteRenderer.dll');

    const CreateDWriteRenderer    = new NativeFunction(dll.getExportByName('CreateDWriteRenderer'), 'pointer', ['pointer', 'pointer', 'uint32'], 'mscdecl');
    const DWriteRendererDrawRune  = new NativeFunction(dll.getExportByName('DWriteRendererDrawRune'), 'int32', ['pointer', 'uint16', 'uint32', 'pointer', 'uint32', 'pointer'], 'mscdecl');

    return {
        CreateDWriteRenderer: function(fontPath: string | undefined, faceName: string | undefined, fontSize: number): NativePointer {
            return CreateDWriteRenderer(fontPath ? utils.UTF16(fontPath) : NULL, faceName ? utils.UTF16(faceName) : NULL, fontSize);
        },

        DWriteRendererDrawRune: function(renderer: NativePointer, char: number, color: number, output: NativePointer, stride: number): number {
            return DWriteRendererDrawRune(renderer, char, color, output, stride, NULL);
        },
    };
})()

export class DWriteRenderer {
    private impl: NativePointer;

    constructor(fontSize: number, fontPath?: string, faceName?: string) {
        this.impl = dwriteRendererAPI.CreateDWriteRenderer(fontPath, faceName, fontSize);
    }

    get pointer(): NativePointer {
        return this.impl;
    }

    drawRune(char: number, color: number, buffer: NativePointer, stride: number) {
        dwriteRendererAPI.DWriteRendererDrawRune(this.impl, char, color, buffer, stride);
    }
}
