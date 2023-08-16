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

export class ED6FC extends EDBaseObject {
    // private static _sharedInstance: ED6FC;
    private static _dirCacheTable: ED6DirEntry[];

    static get dirCacheTable(): ED6DirEntry[] {
        if (!this._dirCacheTable) {
            const p = Addrs.ED6FC.DirCacheTable;
            const table: ED6DirEntry[] = new Array(32).fill(null);

            table.forEach((_, index: number) => {
                table[index] = new ED6DirEntry(p.add(index * Process.pointerSize).readPointer());
            })

            this._dirCacheTable = table;
        }

        return this._dirCacheTable;
    }

    static get fontSizeIndex(): number {
        return Addrs.ED6FC.FontSizeIndex.readU32();
    }

    static get seVolume(): number {
        return Addrs.ED6FC.SEVolumeTable.add(Addrs.ED6FC.SEVolumeIndex.readU32() * 4).readU32();
    }
}
