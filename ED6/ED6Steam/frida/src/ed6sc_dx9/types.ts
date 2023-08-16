import { Addrs } from "./addrs";
import { EDBaseObject } from "../utils";

export class ED6DirEntry extends EDBaseObject {
    get fileName(): string {
        return Buffer.from(this.readByteArray(0, 0x0C)!).toString('utf8');
    }

    get size(): number {
        return this.readU32(0x10);
    }

    get offset(): number {
        return this.readU32(0x20);
    }

    get next(): ED6DirEntry {
        return new ED6DirEntry(this.pointer.add(0x24));
    }
}

export class ED6SC extends EDBaseObject {
    // private static _sharedInstance: ED6SC;
    private static _dirCacheTable: ED6DirEntry[];

    static get dirCacheTable(): ED6DirEntry[] {
        if (!this._dirCacheTable) {
            const p = Addrs.ED6SC.DirCacheTable;
            const table: ED6DirEntry[] = new Array(0x3F).fill(null);

            table.forEach((_, index: number) => {
                table[index] = new ED6DirEntry(p.add(index * Process.pointerSize).readPointer());
            })

            this._dirCacheTable = table;
        }

        return this._dirCacheTable;
    }

    static get fontSizeIndex(): number {
        return Addrs.ED6SC.FontSizeIndex.readU32();
    }

    static get seVolume(): number {
        return Addrs.ED6SC.SEVolumeTable.add(Addrs.ED6SC.SEVolumeIndex.readU32() * 4).readU32();
    }
}
