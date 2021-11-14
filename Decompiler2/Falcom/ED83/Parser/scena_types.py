from Falcom.Common import *
from Falcom.ED83.Parser.datatable import TableNameEntry
from . import utils

DefaultEndian = GlobalConfig.DefaultEndian
DefaultIndent = GlobalConfig.DefaultIndent
DefaultEncoding = GlobalConfig.DefaultEncoding

class ScenaHeader:
    MAGIC = 0xABCDEF00
    def __init__(self, *, fs: fileio.FileStream = None):
        self.headerSize             = None      # type: int
        self.nameOffset             = None      # type: int
        self.functionEntryOffset    = None      # type: int
        self.functionEntrySize      = None      # type: int
        self.functionNameOffset     = None      # type: int
        self.functionCount          = None      # type: int
        self.fullHeaderSize         = None      # type: int
        self.magic                  = None      # type: int

        if fs:
            self.headerSize          = fs.ReadULong()
            self.nameOffset          = fs.ReadULong()
            self.functionEntryOffset = fs.ReadULong()
            self.functionEntrySize   = fs.ReadULong()
            self.functionNameOffset  = fs.ReadULong()
            self.functionCount       = fs.ReadULong()
            self.fullHeaderSize      = fs.ReadULong()
            self.magic               = fs.ReadULong()

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.headerSize, 4))
        fs.write(utils.int_to_bytes(self.nameOffset, 4))
        fs.write(utils.int_to_bytes(self.functionEntryOffset, 4))
        fs.write(utils.int_to_bytes(self.functionEntrySize, 4))
        fs.write(utils.int_to_bytes(self.functionNameOffset, 4))
        fs.write(utils.int_to_bytes(self.functionCount, 4))
        fs.write(utils.int_to_bytes(self.fullHeaderSize, 4))
        fs.write(utils.int_to_bytes(self.magic, 4))

        fs.seek(0)

        return fs.read()

class ScenaFunctionType(IntEnum2):
    Invalid             = 0
    Code                = 1
    BattleSetting       = 3
    AnimeClips          = 4     # gatherAnimeClipInAniFunc
    ActionTable         = 5
    WeaponAttTable      = 6
    BreakTable          = 7
    AlgoTable           = 8
    SummonTable         = 9
    AddCollision        = 10
    PartTable           = 11
    ReactionTable       = 12
    AnimeClipTable      = 13
    FieldMonsterData    = 14
    FieldFollowData     = 15
    ShinigPomBtlset     = 16
    FaceAuto            = 17

class ScenaFunction:
    def __init__(self, index: int, offset: int, name: str):
        self.index  = index
        self.offset = offset
        self.name   = name
        self.type   = ScenaFunctionType.Invalid
        self.obj    = None

    def __str__(self) -> str:
        return f'0x{self.index:04X} 0x{self.offset:08X} {repr(self.name)} {self.type}'

class ScenaBattleMonsterSet:
    # No corresponding battle. battleset(%d) monset(%d)

    TerminatorID   = 0xFFFFFFFF

    def __init__(
        self,
        id                  : int       = None,
        monsters            : List[str] = None,
        encounterProbability: List[int] = None,
        bytes8C             : bytes     = None,
        *,
        fs: fileio.FileStream = None,
    ):

        self.id                     = id
        self.monsters               = monsters
        self.encounterProbability   = encounterProbability
        self.bytes8C                = bytes8C

        if monsters: assert len(monsters) == 8
        if encounterProbability: assert len(encounterProbability) == 8

        if fs:
            self.id = fs.ReadULong()

            match self.id:
                case self.TerminatorID:
                    pass

                case 0xFFFFFFFE:
                    # fs.Position += 0x50 - 4
                    raise
                    self.id = fs.ReadULong()

                case _:
                    self.monsters               = [utils.read_fixed_string(fs, 0x10) for _ in range(8)]
                    self.encounterProbability   = [fs.ReadByte() for _ in range(8)]
                    self.bytes8C                = fs.Read(8)

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.id, 4))

        match self.id:
            case self.TerminatorID:
                fs.write(b'\x00' * 0x18)
                pass

            case 0xFFFFFFFE:
                raise

            case _:
                [fs.write(utils.pad_string(m, 0x10)) for m in self.monsters]
                [fs.write(utils.int_to_bytes(p, 1)) for p in self.encounterProbability]
                # fs.write(self.bytes8C)
                fs.write(b'\x00' * 8)

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        indent = DefaultIndent
        match self.id:
            case ScenaBattleMonsterSet.TerminatorID:
                body = [f'ScenaBattleMonsterSet(id = ScenaBattleMonsterSet.TerminatorID)']

            case _:
                body = [
                    f'ScenaBattleMonsterSet(',
                    f'{indent}id                      = 0x{self.id:08X},',
                    f'{indent}monsters                = {self.monsters},',
                    f'{indent}encounterProbability    = {self.encounterProbability},',
                    ')',
                ]

        return body


class ScenaBattleSetting:
    def __init__(
        self,
        mapName     : str = None,
        x           : int = None,
        y           : int = None,
        z           : int = None,
        direction   : int = None,
        float20     : int = None,
        float24     : int = None,
        word28      : int = None,
        dword2C     : int = None,
        word30      : int = None,
        word32      : int = None,
        word34      : int = None,
        word36      : int = None,
        dword38     : int = None,
        battleName  : str = None,
        monsterSet  : List[ScenaBattleMonsterSet] = None,
        *,
        fs: fileio.FileStream = None,
    ):

        self.mapName        = mapName       # type: str
        self.x              = x             # type: int
        self.y              = y             # type: int
        self.z              = z             # type: int
        self.direction      = direction     # type: int
        self.float20        = float20       # type: int
        self.float24        = float24       # type: int
        self.word28         = word28        # type: int
        self.dword2C        = dword2C       # type: int
        self.word30         = word30        # type: int
        self.word32         = word32        # type: int
        self.word34         = word34        # type: int
        self.word36         = word36        # type: int
        self.dword38        = dword38       # type: int
        self.battleName     = battleName    # type: str
        self.monsterSet     = monsterSet    # type: List[ScenaBattleMonsterSet]

        if fs:
            self.mapName    = utils.read_fixed_string(fs, 0x10)
            self.x          = fs.ReadFloat()
            self.y          = fs.ReadFloat()
            self.z          = fs.ReadFloat()
            self.direction  = fs.ReadFloat()
            self.float20    = fs.ReadFloat()
            self.float24    = fs.ReadFloat()
            self.word28     = fs.ReadUShort()

            fs.Position += 2    # padding

            self.dword2C    = fs.ReadULong()
            self.word30     = fs.ReadUShort()
            self.word32     = fs.ReadUShort()
            self.word34     = fs.ReadUShort()
            self.word36     = fs.ReadUShort()
            self.dword38    = fs.ReadULong()
            self.battleName = utils.read_fixed_string(fs, 0x10)

            self.monsterSet = []

            monsetid = 0

            while monsetid != ScenaBattleMonsterSet.TerminatorID:
                self.monsterSet.append(ScenaBattleMonsterSet(fs = fs))
                monsetid = self.monsterSet[-1].id

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.pad_string(self.mapName, 0x10))
        fs.write(utils.float_to_bytes(self.x))
        fs.write(utils.float_to_bytes(self.y))
        fs.write(utils.float_to_bytes(self.z))
        fs.write(utils.float_to_bytes(self.direction))
        fs.write(utils.float_to_bytes(self.float20))
        fs.write(utils.float_to_bytes(self.float24))
        fs.write(utils.int_to_bytes(self.word28, 2))

        fs.write(b'\x00' * 2) # padding

        fs.write(utils.int_to_bytes(self.dword2C, 4))
        fs.write(utils.int_to_bytes(self.word30, 2))
        fs.write(utils.int_to_bytes(self.word32, 2))
        fs.write(utils.int_to_bytes(self.word34, 2))
        fs.write(utils.int_to_bytes(self.word36, 2))
        fs.write(utils.int_to_bytes(self.dword38, 4))
        fs.write(utils.pad_string(self.battleName, 0x10))

        for monset in self.monsterSet:
            fs.write(monset.serialize())

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        body = [
            f'ScenaBattleSetting(',
            f'{DefaultIndent}mapName     = \'{self.mapName}\',',
            f'{DefaultIndent}x           = {self.x},',
            f'{DefaultIndent}y           = {self.y},',
            f'{DefaultIndent}z           = {self.z},',
            f'{DefaultIndent}direction   = {self.direction},',
            f'{DefaultIndent}float20     = {self.float20},',
            f'{DefaultIndent}float24     = {self.float24},',
            f'{DefaultIndent}word28      = {self.word28},',
            f'{DefaultIndent}dword2C     = {self.dword2C},',
            f'{DefaultIndent}word30      = {self.word30},',
            f'{DefaultIndent}word32      = {self.word32},',
            f'{DefaultIndent}word34      = {self.word34},',
            f'{DefaultIndent}word36      = {self.word36},',
            f'{DefaultIndent}dword38     = {self.dword38},',
            f'{DefaultIndent}battleName  = \'{self.battleName}\',',
            f'{DefaultIndent}monsterSet  = [',
        ]

        indent2 = DefaultIndent * 2
        for monset in self.monsterSet:
            body.extend([indent2 + l for l in monset.toPython()])
            body[-1] += ','

        body.append(f'{DefaultIndent}],')
        body.append(f')')

        return body

class ScenaAnimeClipItem:
    def __init__(self, type: int = None, type2: int = None, dword4: int = None, name: str = None, *, fs: fileio.FileStream = None):
        self.type   = type
        self.type2  = type2
        self.dword4 = dword4
        self.name   = name

        if fs:
            self.type   = fs.ReadUShort()
            self.type2  = fs.ReadUShort()
            self.dword4 = fs.ReadULong()
            self.name   = utils.read_fixed_string(fs, 0x20)

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.type, 2))
        fs.write(utils.int_to_bytes(self.type2, 2))
        fs.write(utils.int_to_bytes(self.dword4, 4))
        fs.write(utils.pad_string(self.name, 0x20))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        body = [
            f'ScenaAnimeClipItem(',
            f'{DefaultIndent}type   = 0x{self.type:04X},',
            f'{DefaultIndent}type2  = 0x{self.type2:04X},',
            f'{DefaultIndent}dword4 = 0x{self.dword4:08X},',
            f'{DefaultIndent}name   = \'{self.name}\',',
            ')',
        ]

        return body

class ScenaAnimeClips:
    def __init__(self, *clips: List[ScenaAnimeClipItem], fs: fileio.FileStream = None):
        self.clips = clips

        if not fs:
            return

        self.clips: List[ScenaAnimeClipItem] = []
        while True:
            c = ScenaAnimeClipItem(fs = fs)
            self.clips.append(c)
            if c.type == 0:
                break

    def serialize(self) -> bytes:
        b = bytearray()
        for clip in self.clips:
            b.extend(clip.serialize())

        if not self.clips or self.clips[-1].type != 0:
            b.extend(ScenaAnimeClipItem(0x0000, 0xFFFF, 0x00000000, '').serialize())

        return bytes(b)

    def toPython(self) -> List[str]:
        body = [
            f'ScenaAnimeClips(',
        ]

        for i, clip in enumerate(self.clips):
            # if clip.type == 0:
            #     assert i + 1 == len(self.clips)
            #     break

            body.extend([DefaultIndent + l for l in clip.toPython()])
            body[-1] += ','

        body.append(')')

        return body

class ScenaAnimeClipTableEntry:
    def __init__(self, flags: int = None, name1: str = None, name2: str = None, *, fs: fileio.FileStream = None):
        self.flags  = flags
        self.name1  = name1
        self.name2  = name2

        if fs:
            self.flags = fs.ReadULong()
            if self.flags != 0:
                self.name1 = utils.read_fixed_string(fs, 0x20)
                self.name2 = utils.read_fixed_string(fs, 0x20)

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.flags, 4))
        if self.flags != 0:
            fs.write(utils.pad_string(self.name1, 0x20))
            fs.write(utils.pad_string(self.name2, 0x20))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        f = [
            'ScenaAnimeClipTableEntry(',
            f'{DefaultIndent}flags = 0x{self.flags:08X},',
        ]

        if self.flags != 0:
            f.extend([
                f"{DefaultIndent}name1 = '{self.name1}',",
                f"{DefaultIndent}name2 = '{self.name2}',",
            ])

        f.append(')')

        return f

class ScenaAnimeClipTable:
    def __init__(self, *entries: List[ScenaAnimeClipTableEntry], fs: fileio.FileStream = None):
        self.entries = entries

        if not fs:
            return

        self.entries: List[ScenaAnimeClipTableEntry] = []

        while True:
            self.entries.append(ScenaAnimeClipTableEntry(fs = fs))
            if self.entries[-1].flags == 0:
                break

    def serialize(self) -> bytes:
        b = bytearray()

        for e in self.entries:
            b.extend(e.serialize())

        if not self.entries or self.entries[-1].flags != 0:
            b.extend(ScenaAnimeClipTableEntry(flags = 0).serialize())

        return b

    def toPython(self) -> List[str]:
        body = [
            'ScenaAnimeClipTable(',
        ]

        for i, e in enumerate(self.entries):
            # if e.flags == 0:
            #     assert i + 1 == len(self.entries)
            #     break

            body.extend([DefaultIndent + l for l in e.toPython()])
            body[-1] += ','

        body.append(')')

        return body

class ScenaFieldMonsterData:
    def __init__(self, type: int = None, word04: int = None, word06: int = None, floats: List[float] = None, fs: fileio.FileStream = None):
        self.type   = type
        self.word04 = word04
        self.word06 = word06
        self.floats = floats

        if floats: assert len(floats) == 5

        if fs:
            self.type = fs.ReadULong()
            self.word04 = fs.ReadUShort()
            self.word06 = fs.ReadUShort()
            self.floats = [fs.ReadFloat() for _ in range(5)]

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.type, 4))
        fs.write(utils.int_to_bytes(self.word04, 2))
        fs.write(utils.int_to_bytes(self.word06, 2))

        for f in self.floats:
            fs.write(utils.float_to_bytes(f))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        body = [
            'ScenaFieldMonsterData(',
            f'{DefaultIndent}type   = 0x{self.type:08X},',
            f'{DefaultIndent}word04 = 0x{self.word04:04X},',
            f'{DefaultIndent}word06 = 0x{self.word06:04X},',
            f'{DefaultIndent}floats = {self.floats},',
            ')',
        ]

        return body
