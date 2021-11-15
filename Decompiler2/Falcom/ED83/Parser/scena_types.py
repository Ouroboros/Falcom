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

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.headerSize          = fs.ReadULong()       # 0x00
        self.nameOffset          = fs.ReadULong()       # 0x04
        self.functionEntryOffset = fs.ReadULong()       # 0x08
        self.functionEntrySize   = fs.ReadULong()       # 0x0C
        self.functionNameOffset  = fs.ReadULong()       # 0x10
        self.functionCount       = fs.ReadULong()       # 0x14
        self.fullHeaderSize      = fs.ReadULong()       # 0x18
        self.magic               = fs.ReadULong()       # 0x1C

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

    InvalidID = 0xFFFFFFFF

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

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.id = fs.ReadULong() # 0x00

        match self.id:
            case self.InvalidID:
                pass

            case 0xFFFFFFFE:
                # fs.Position += 0x50 - 4
                raise NotImplementedError
                self.id = fs.ReadULong()

            case _:
                self.monsters               = [utils.read_fixed_string(fs, 0x10) for _ in range(8)]     # 0x04
                self.encounterProbability   = [fs.ReadByte() for _ in range(8)]                         # 0x84
                self.bytes8C                = fs.Read(8)                                                # 0x8C

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.id, 4))

        match self.id:
            case self.InvalidID:
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
            case ScenaBattleMonsterSet.InvalidID:
                body = [f'ScenaBattleMonsterSet(id = ScenaBattleMonsterSet.InvalidID)']

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

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.mapName    = utils.read_fixed_string(fs, 0x10)     # 0x00
        self.x          = fs.ReadFloat()                        # 0x10
        self.y          = fs.ReadFloat()                        # 0x14
        self.z          = fs.ReadFloat()                        # 0x18
        self.direction  = fs.ReadFloat()                        # 0x1C
        self.float20    = fs.ReadFloat()                        # 0x20
        self.float24    = fs.ReadFloat()                        # 0x24
        self.word28     = fs.ReadUShort()                       # 0x28

        fs.Position += 2    # padding                           # 0x2A

        self.dword2C    = fs.ReadULong()                        # 0x2C
        self.word30     = fs.ReadUShort()                       # 0x30
        self.word32     = fs.ReadUShort()                       # 0x32
        self.word34     = fs.ReadUShort()                       # 0x34
        self.word36     = fs.ReadUShort()                       # 0x36
        self.dword38    = fs.ReadULong()                        # 0x38
        self.battleName = utils.read_fixed_string(fs, 0x10)     # 0x3C

        self.monsterSet = []                                    # 0x4C

        monsetid = 0

        while monsetid != ScenaBattleMonsterSet.InvalidID:
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
    def __init__(self, type: int = None, word04: int = None, word06: int = None, floats: List[float] = None, *, fs: fileio.FileStream = None):
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

class ScenaFieldFollowData:
    def __init__(self, floats: List[float] = None, *, fs: fileio.FileStream = None):
        self.floats = floats

        if floats: assert len(floats) == 5

        if fs:
            self.floats = [fs.ReadFloat() for _ in range(5)]

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        for f in self.floats:
            fs.write(utils.float_to_bytes(f))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        body = [
            'ScenaFieldFollowData(',
            f'{DefaultIndent}floats = {self.floats},',
            ')',
        ]

        return body

class ScenaActionTableEntry:
    InvalidCraftID = 0xFFFF

    def __init__(self, *, fs: fileio.FileStream = None):
        self.craftId        = None                  # type: int
        self.byte02         = None                  # type: int
        self.byte03         = None                  # type: int
        self.byte04         = None                  # type: int
        self.byte05         = None                  # type: int
        self.byte06         = None                  # type: int
        self.pad07          = None                  # type: int
        self.float08        = None                  # type: int
        self.float0C        = None                  # type: int
        self.float10        = None                  # type: int
        self.byte14         = None                  # type: int
        self.pad15          = None                  # type: int
        self.byte16         = None                  # type: int
        self.pad17          = None                  # type: int
        self.word18         = None                  # type: int
        self.word1A         = None                  # type: int
        self.word1C         = None                  # type: int
        self.word1E         = None                  # type: int
        self.word20         = None                  # type: int
        self.pad22          = None                  # type: int
        self.dword24        = None                  # type: int
        self.dword28        = None                  # type: int
        self.dword2C        = None                  # type: int
        self.dword30        = None                  # type: int
        self.dword34        = None                  # type: int
        self.dword38        = None                  # type: int
        self.dword3C        = None                  # type: int
        self.dword40        = None                  # type: int
        self.dword44        = None                  # type: int
        self.dword48        = None                  # type: int
        self.dword4C        = None                  # type: int
        self.dword50        = None                  # type: int
        self.dword54        = None                  # type: int
        self.dword58        = None                  # type: int
        self.dword5C        = None                  # type: int
        self.CP             = None                  # type: int
        self.pad62          = None                  # type: int
        self.flags          = None                  # type: str
        self.action         = None                  # type: str
        self.name           = None                  # type: str

        if not fs:
            return

        self.craftId        = fs.ReadUShort()                   # 0x00

        if self.craftId == self.InvalidCraftID:
            return

        self.byte02         = fs.ReadByte()                     # 0x02
        self.byte03         = fs.ReadByte()                     # 0x03
        self.byte04         = fs.ReadByte()                     # 0x04
        self.byte05         = fs.ReadByte()                     # 0x05
        self.byte06         = fs.ReadByte()                     # 0x06
        self.pad07          = fs.ReadByte()                     # 0x07
        self.float08        = fs.ReadFloat()                    # 0x08
        self.float0C        = fs.ReadFloat()                    # 0x0C
        self.float10        = fs.ReadFloat()                    # 0x10
        self.byte14         = fs.ReadByte()                     # 0x14
        self.pad15          = fs.ReadByte()                     # 0x15
        self.byte16         = fs.ReadByte()                     # 0x16
        self.pad17          = fs.ReadByte()                     # 0x17
        self.word18         = fs.ReadUShort()                   # 0x18
        self.word1A         = fs.ReadUShort()                   # 0x1A
        self.word1C         = fs.ReadUShort()                   # 0x1C
        self.word1E         = fs.ReadUShort()                   # 0x1E
        self.word20         = fs.ReadUShort()                   # 0x20
        self.pad22          = fs.ReadUShort()                   # 0x22
        self.dword24        = fs.ReadULong()                    # 0x24
        self.dword28        = fs.ReadULong()                    # 0x28
        self.dword2C        = fs.ReadULong()                    # 0x2C
        self.dword30        = fs.ReadULong()                    # 0x30
        self.dword34        = fs.ReadULong()                    # 0x34
        self.dword38        = fs.ReadULong()                    # 0x38
        self.dword3C        = fs.ReadULong()                    # 0x3C
        self.dword40        = fs.ReadULong()                    # 0x40
        self.dword44        = fs.ReadULong()                    # 0x44
        self.dword48        = fs.ReadULong()                    # 0x48
        self.dword4C        = fs.ReadULong()                    # 0x4C
        self.dword50        = fs.ReadULong()                    # 0x50
        self.dword54        = fs.ReadULong()                    # 0x54
        self.dword58        = fs.ReadULong()                    # 0x58
        self.dword5C        = fs.ReadULong()                    # 0x5C
        self.CP             = fs.ReadUShort()                   # 0x60
        self.pad62          = fs.ReadUShort()                   # 0x62
        self.flags          = utils.read_fixed_string(fs, 0x10) # 0x64
        self.action  = utils.read_fixed_string(fs, 0x20) # 0x74
        self.name           = utils.read_fixed_string(fs, 0x40) # 0x94

    def toPython(self) -> List[str]:
        return [
            'ScenaActionTableEntry(',
            f'{DefaultIndent}craftId       = 0x{self.craftId:X},',
            f'{DefaultIndent}byte02        = 0x{self.byte02:02X},',
            f'{DefaultIndent}byte03        = 0x{self.byte03:02X},',
            f'{DefaultIndent}byte04        = 0x{self.byte04:02X},',
            f'{DefaultIndent}byte05        = 0x{self.byte05:02X},',
            f'{DefaultIndent}byte06        = 0x{self.byte06:02X},',
            f'{DefaultIndent}pad07         = 0x{self.pad07:02X},',
            f'{DefaultIndent}float08       = {self.float08},',
            f'{DefaultIndent}float0C       = {self.float0C},',
            f'{DefaultIndent}float10       = {self.float10},',
            f'{DefaultIndent}byte14        = 0x{self.byte14:02X},',
            f'{DefaultIndent}pad15         = 0x{self.pad15:02X},',
            f'{DefaultIndent}byte16        = 0x{self.byte16:02X},',
            f'{DefaultIndent}pad17         = 0x{self.pad17:02X},',
            f'{DefaultIndent}word18        = 0x{self.word18:04X},',
            f'{DefaultIndent}word1A        = 0x{self.word1A:04X},',
            f'{DefaultIndent}word1C        = 0x{self.word1C:04X},',
            f'{DefaultIndent}word1E        = 0x{self.word1E:04X},',
            f'{DefaultIndent}word20        = 0x{self.word20:04X},',
            f'{DefaultIndent}pad22         = 0x{self.pad22:02X},',
            f'{DefaultIndent}dword24       = {self.dword24},',
            f'{DefaultIndent}dword28       = {self.dword28},',
            f'{DefaultIndent}dword2C       = {self.dword2C},',
            f'{DefaultIndent}dword30       = {self.dword30},',
            f'{DefaultIndent}dword34       = {self.dword34},',
            f'{DefaultIndent}dword38       = {self.dword38},',
            f'{DefaultIndent}dword3C       = {self.dword3C},',
            f'{DefaultIndent}dword40       = {self.dword40},',
            f'{DefaultIndent}dword44       = {self.dword44},',
            f'{DefaultIndent}dword48       = {self.dword48},',
            f'{DefaultIndent}dword4C       = {self.dword4C},',
            f'{DefaultIndent}dword50       = {self.dword50},',
            f'{DefaultIndent}dword54       = {self.dword54},',
            f'{DefaultIndent}dword58       = {self.dword58},',
            f'{DefaultIndent}dword5C       = {self.dword5C},',
            f'{DefaultIndent}CP            = {self.CP},',
            f'{DefaultIndent}pad62         = 0x{self.pad62:02X},',
            f"{DefaultIndent}flags         = '{self.flags}',",
            f"{DefaultIndent}action        = '{self.action}',",
            f"{DefaultIndent}name          = '{self.name}',",
            ')',
        ]

class ScenaActionTable:
    def __init__(self, *actions: List[ScenaActionTableEntry], fs: fileio.FileStream = None):
        self.actions = actions

        if not fs:
            return

        self.actions: List[ScenaActionTableEntry] = []

        while True:
            entry = ScenaActionTableEntry(fs = fs)
            if entry.craftId == ScenaActionTableEntry.InvalidCraftID:
                break

            self.actions.append(entry)

    def toPython(self) -> List[str]:
        b = [
            'ScenaActionTable(',
        ]

        for i, a in enumerate(self.actions):
            b.extend([DefaultIndent + l for l in a.toPython()])
            b[-1] += ','

        b.append(')')
        return b

class ScenaAlgoTableEntry:
    # enemy battle ai

    def __init__(
            self,
            craftId         : int       = None,
            condition       : int       = None,
            probability     : int       = None,
            target          : int       = None,
            targetCondition : int       = None,
            parameters1     : List[int] = None,
            parameters2     : List[int] = None,
            *,
            fs: fileio.FileStream       = None,
        ):

        self.craftId            = craftId
        self.condition          = condition
        self.probability        = probability
        self.target             = target
        self.targetCondition    = targetCondition
        self.parameters1        = parameters1
        self.parameters2        = parameters2

        if parameters1: assert len(parameters1) == 3
        if parameters2: assert len(parameters2) == 3

        self.read(fs)

    def read(self, fs):
        if not fs:
            return

        self.craftId            = fs.ReadUShort()                       # 0x00
        self.condition          = fs.ReadByte()                         # 0x02
        self.probability        = fs.ReadByte()                         # 0x03
        self.target             = fs.ReadByte()                         # 0x04
        self.targetCondition    = fs.ReadByte()                         # 0x05

        pad06 = fs.ReadUShort()                       # 0x06      always 0

        self.parameters1        = [fs.ReadULong() for _ in range(3)]    # 0x08      params for condition
        self.parameters2        = [fs.ReadULong() for _ in range(3)]    # 0x14      params for targetCondition

        assert pad06 == 0

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.craftId, 2))
        fs.write(utils.int_to_bytes(self.condition, 1))
        fs.write(utils.int_to_bytes(self.probability, 1))
        fs.write(utils.int_to_bytes(self.target, 1))
        fs.write(utils.int_to_bytes(self.targetCondition, 1))
        fs.write(b'\x00' * 2)

        for p in self.parameters1 + self.parameters2:
            fs.write(utils.int_to_bytes(p, 4))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        return [
            'ScenaAlgoTableEntry(',
            f'{DefaultIndent}craftId            = 0x{self.craftId:X},',
            f'{DefaultIndent}condition          = 0x{self.condition:02X},',
            f'{DefaultIndent}probability        = {self.probability},',
            f'{DefaultIndent}target             = 0x{self.target:02X},',
            f'{DefaultIndent}targetCondition    = 0x{self.targetCondition:02X},',
            f'{DefaultIndent}parameters1        = {self.parameters1},',
            f'{DefaultIndent}parameters2        = {self.parameters2},',
            ')',
        ]

class ScenaAlgoTable:
    def __init__(self, *entries: List[ScenaAlgoTableEntry], fs: fileio.FileStream = None):
        self.entries = entries

        if not fs:
            return

        self.entries: List[ScenaAlgoTableEntry] = []

        while True:
            e = ScenaAlgoTableEntry(fs = fs)
            if e.craftId == 0:
                break

            self.entries.append(e)

    def serialize(self) -> bytes:
        b = bytearray()
        for e in self.entries:
            b.extend(e.serialize())

        b.extend(ScenaAlgoTableEntry(0, 0, 0, 0, 0, [0] * 3, [0] * 3).serialize())

        return bytes(b)

    def toPython(self) -> List[str]:
        b = [
            'ScenaAlgoTable(',
        ]

        for i, a in enumerate(self.entries):
            b.extend([DefaultIndent + l for l in a.toPython()])
            b[-1] += ','

        b.append(')')
        return b
