from Falcom.ED83.Parser.scena_types import *

class ScenaReactionTable:
    def __init__(self, *reactions: ScenaReactionTableEntry, fs: fileio.FileStream = None):
        self.reactions = reactions
        if reactions: assert len(reactions) <= 8
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.reactions = []
        for _ in range(8):
            e = ScenaReactionTableEntry(fs = fs)
            if e.craftId == ScenaReactionTableEntry.InvalidID:
                break

            self.reactions.append(e)

    def serialize(self) -> bytes:
        b = bytearray()

        for s in self.reactions:
            b.extend(s.serialize())

        if not self.reactions or (len(self.reactions) < 8 and self.reactions[-1].craftId != ScenaReactionTableEntry.InvalidID):
            b.extend(ScenaReactionTableEntry(ScenaReactionTableEntry.InvalidID, 0, 0, 0, [0.0] * 12).serialize())

        return bytes(b)

    def toPython(self) -> List[str]:
        f = [
            f'ScenaReactionTable(',
        ]

        for p in self.reactions:
            f.extend([DefaultIndent + l for l in p.toPython()])
            f[-1] += ','

        f.append(')')

        return f

class ScenaStyleName:
    def __init__(self, style: str = '', styleEn: str = '', *, fs: fileio.FileStream = None):
        self.style = style
        self.styleEn = styleEn
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.style = utils.read_fixed_string(fs, 0x40)
        self.styleEn = utils.read_fixed_string(fs, 0x40)

    def serialize(self) -> bytes:
        return utils.pad_string(self.style, 0x40) + utils.pad_string(self.styleEn, 0x40)

    def toPython(self) -> List[str]:
        return [f"ScenaStyleName('{self.style}', '{self.styleEn}')"]
