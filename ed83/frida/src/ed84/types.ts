import * as json5 from "json5"
import * as path from "path"
import { Modules } from "../modules";
import { Addrs, Offsets } from "./addrs";
import { ED8BaseObject, Interceptor2 } from "../utils";
import * as utils from "../utils";

export const MaxPartyChrId = 0x40;
export const MinCustomChrId = 0x2000;
export const InvalidChrId = 0xFFFF;

export interface INameTableData {
    chrId       : number;
    chrName     : string;
    model       : string;
    ani         : string;
    faceModel   : string;
    faceTexture : string;
    name2       : string;
}

export interface IConfig {
    nameTable: INameTableData[];
    assetMap: {[key: string]: string};
}

export class NameTableData extends ED8BaseObject implements INameTableData {
    get chrId(): number {
        return this.readU16(0x00);
    }

    get chrName(): string {
        return this.readPointer(0x08).readUtf8String()!;
    }

    get model(): string {
        return this.readPointer(0x10).readUtf8String()!;
    }

    get faceModel(): string {
        return this.readPointer(0x18).readUtf8String()!;
    }

    get ani(): string {
        return this.aniptr.readUtf8String()!;
    }

    get aniptr(): NativePointer {
        return this.readPointer(0x20);
    }

    get faceTexture(): string {
        return this.readPointer(0x28).readUtf8String()!;
    }

    get name2(): string {
        return this.readPointer(0x30).readUtf8String()!;
    }
}

export class CharacterManager extends ED8BaseObject {

}

export class Character extends ED8BaseObject {
    static isReplaced(chrId: number): boolean {
        return ED84.getBattleStyle(chrId) >= MinCustomChrId
    }

    isReplaced(): boolean {
        return Character.isReplaced(this.chrId);
    }

    get chrId(): number {
        return this.readU16(Offsets.Character.ChrID);
    }

    get modelChrId(): number {
        return this.readU16(Offsets.Character.ModelChrId);
    }

    set modelChrId(chrId: number) {
        this.writeU16(Offsets.Character.ModelChrId, chrId);
    }

    get model(): string {
        return this.readUtf8String(Offsets.Character.Model)!;
    }

    get faceModel(): string {
        return this.readUtf8String(Offsets.Character.FaceModel)!;
    }

    set faceModel(asset: string) {
        this.pointer.add(Offsets.Character.FaceModel).writeUtf8String(asset);
    }

    get presetFaceModel(): string {
        return this.readUtf8String(Offsets.Character.PresetFaceModel)!;
    }

    set presetFaceModel(model: string) {
        this.pointer.add(Offsets.Character.PresetFaceModel).writeUtf8String(model);
    }

    loadAni(ani: string) {
        const Character_LoadAni = new NativeFunction(Addrs.Character.LoadAni, "void", ['pointer', 'pointer', 'uint32'], 'win64');
        const p = Memory.allocUtf8String(ani);
        const auto_compile = 0;
        Character_LoadAni(this.pointer, p, auto_compile);
    }
}

export class ED84 extends ED8BaseObject {
    private static _sharedInstance: ED84;
    private static _config: IConfig;

    private static _findNameTableDataByModel = new NativeFunction(Addrs.ED84.findNameTableDataByModel, "pointer", ['pointer', 'pointer'], 'win64');
    private static _findNameTableDataByChrId = new NativeFunction(Addrs.ED84.findNameTableDataByChrId, "pointer", ['pointer', 'uint16'], 'win64');
    private static _findPartyCharByChrId     = new NativeFunction(Addrs.ED84.findPartyCharByChrId, "pointer", ['pointer', 'uint16', 'uint32'], 'win64');

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

    static get sharedInstance(): ED84 {
        if (this._sharedInstance)
            return this._sharedInstance;

        const p = Addrs.ED84.sharedInstance.readPointer();

        if (p.isNull()) {
            throw new Error('ED84 null');
        }

        this._sharedInstance = new ED84(p);
        return this._sharedInstance;
    }

    static get nameTable(): NativePointer {
        return this.sharedInstance.readPointer(Offsets.ED84.t_name);
    }

    static get characterManager(): CharacterManager {
        return new CharacterManager(this.sharedInstance.readPointer(Offsets.ED84.CharacterManager));
    }

    static getConfig(): IConfig {
        if (this._config)
            return this._config;

        this._config = function() {
            const exePath = path.join(path.dirname(path.dirname(path.dirname(Modules.ED84.path.split('\\').join('/')))), 'ouroboros', 'config.json5');
            const config = utils.readFileContent(exePath);
            if (!config)
                return null;

            const s = Buffer.from(config).toString('utf8');

            try {
                const cfg: IConfig = json5.parse(s);
                return cfg;
            } catch (e) {
                utils.log('load config: %s', e);
            }

            return null;
        }()!;

        return this._config;
    }

    static findNameTableDataByModel(model: string): INameTableData | undefined {
        const m = Memory.allocUtf8String(model);
        const p = this._findNameTableDataByModel(this.nameTable, m);
        if (!p.isNull())
            return new NameTableData(p);

        return ED84.getConfig().nameTable.find(data => data.model == model);
    }

    static findNameTableDataByChrId(chrId: number): INameTableData | undefined {
        if (chrId == InvalidChrId)
            return undefined;

        const p = this._findNameTableDataByChrId(this.nameTable, chrId);
        if (!p.isNull())
            return new NameTableData(p);

        return ED84.getConfig().nameTable.find(data => data.chrId == chrId);
    }

    static getCraftList(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED84.CraftList).add(chrId * 0x10);
    }

    static getMagicList(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED84.MagicList).add(chrId * 0x10);
    }

    static getSBreak(chrId: number): NativePointer {
        return this.sharedInstance.pointer.add(Offsets.ED84.SBreakList).add(chrId * 2);
    }

    static getBattleStyle(chrId: number): number {
        return this.sharedInstance.pointer.add(Offsets.ED84.BattleStyleList).add(chrId * 2).readU16();
    }
}
