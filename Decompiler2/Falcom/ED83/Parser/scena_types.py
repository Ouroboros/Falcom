from Falcom.Common import *
from . import utils

DefaultEndian = GlobalConfig.DefaultEndian
DefaultIndent = GlobalConfig.DefaultIndent
DefaultEncoding = GlobalConfig.DefaultEncoding

class ScenaTypesBase:
    DESCRIPTOR: Tuple[str, str] = None

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        if not fs:
            self.deserialize(fs)

    def toPython(self) -> List[str]:
        if not self.DESCRIPTOR:
            raise NotImplementedError

        align = max([len(e[0]) for e in self.DESCRIPTOR])
        align = (align + 4) & ~3

        lines = [
            f'{self.__class__.__name__}(',
        ]

        formatter = {
            'C' : lambda v: f'{v}',
            'B' : lambda v: f'0x{v:02X}',
            'H' : lambda v: f'{v}',
            'W' : lambda v: f'0x{v:04X}',
            'I' : lambda v: f'{v}',
            'L' : lambda v: f'0x{v:08X}',
            'f' : lambda v: f'{v:g}.0' if f'{v:g}'.count('.') == 0 else f'{v:g}',
            'S' : lambda v: f"{repr(v)}",
        }

        for name, type in self.DESCRIPTOR:
            type = type.split(':', maxsplit = 1)[0]
            value = getattr(self, name)
            lines.append(f'{DefaultIndent}{name.ljust(align)}= {formatter[type](value)},')

        lines.append(')')

        return lines

    def serialize(self) -> bytes:
        if not self.DESCRIPTOR:
            raise NotImplementedError

        writer = {
            'B' : lambda v: utils.int_to_bytes(v, 1),
            'C' : lambda v: utils.int_to_bytes(v, 1),
            'H' : lambda v: utils.int_to_bytes(v, 2),
            'W' : lambda v: utils.int_to_bytes(v, 2),
            'I' : lambda v: utils.int_to_bytes(v, 4),
            'L' : lambda v: utils.int_to_bytes(v, 4),
            'f' : lambda v: utils.float_to_bytes(v),
            'S' : lambda v: utils.str_to_bytes(v),
        }

        body = bytearray()

        for name, type in self.DESCRIPTOR:
            body.extend(writer[type](getattr(self, name)))

        return body

    def deserialize(self, fs: fileio.FileStream):
        if not self.DESCRIPTOR:
            return

        reader = {
            'B' : lambda: fs.ReadByte(),
            'C' : lambda: fs.ReadByte(),
            'H' : lambda: fs.ReadUShort(),
            'W' : lambda: fs.ReadUShort(),
            'I' : lambda: fs.ReadULong(),
            'L' : lambda: fs.ReadULong(),
            'f' : lambda: fs.ReadFloat(),
            'S' : lambda: fs.ReadMultiByte(),
        }

        for name, type in self.DESCRIPTOR:
            setattr(self, name, reader[type]())

    def __str__(self):
        return '\n'.join(self.toPython())

    __repr__ = __str__


class ScenaHeader:
    MAGIC = 0xABCDEF00
    def __init__(self, *, fs: fileio.FileStream = None):
        self.headerSize             = 0x20              # type: int
        self.nameOffset             = self.headerSize   # type: int
        self.functionEntryOffset    = None              # type: int
        self.functionEntrySize      = None              # type: int
        self.functionNameOffset     = None              # type: int
        self.functionCount          = None              # type: int
        self.fullHeaderSize         = None              # type: int
        self.magic                  = self.MAGIC        # type: int

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
    BattleSetting       = 2
    AnimeClips          = 3     # gatherAnimeClipInAniFunc
    ActionTable         = 4
    WeaponAttTable      = 5
    BreakTable          = 6
    AlgoTable           = 7
    SummonTable         = 8
    AddCollision        = 9
    PartTable           = 10
    ReactionTable       = 11
    AnimeClipTable      = 12
    FieldMonsterData    = 13
    FieldFollowData     = 14
    FaceAuto            = 15    # FC_autoXX
    ShinigPomBtlset     = 16
    StyleName           = 17

ScenaDataFunctionTypes = set([
    ScenaFunctionType.BattleSetting,
    ScenaFunctionType.AnimeClips,
    ScenaFunctionType.ActionTable,
    ScenaFunctionType.WeaponAttTable,
    ScenaFunctionType.BreakTable,
    ScenaFunctionType.AlgoTable,
    ScenaFunctionType.SummonTable,
    ScenaFunctionType.AddCollision,
    ScenaFunctionType.PartTable,
    ScenaFunctionType.ReactionTable,
    ScenaFunctionType.AnimeClipTable,
    ScenaFunctionType.FieldMonsterData,
    ScenaFunctionType.FieldFollowData,
    ScenaFunctionType.FaceAuto,
    ScenaFunctionType.ShinigPomBtlset,
    ScenaFunctionType.StyleName,
])

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
        id                  : int       = InvalidID,
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
                    f'{indent}id                      = 0x{self.id:X},',
                    f'{indent}monsters                = {self.monsters},',
                    f'{indent}encounterProbability    = {self.encounterProbability},',
                    ')',
                ]

        return body

class ScenaBattleSetting:
    def __init__(
        self,
        mapName     : str = '',
        x           : int = 0,
        y           : int = 0,
        z           : int = 0,
        direction   : int = 0,
        length      : int = 0,
        width       : int = 0,
        battleId    : int = 0,
        flags       : int = 0,
        bgm         : int = 0,
        dangerBGM   : int = 0,
        word34      : int = 0,
        word36      : int = 0,
        atBonus     : int = 0,
        battleScript: str = '',
        monsterSet  : List[ScenaBattleMonsterSet] = None,
        *,
        fs: fileio.FileStream = None,
    ):

        self.mapName        = mapName       # type: str
        self.x              = x             # type: int
        self.y              = y             # type: int
        self.z              = z             # type: int
        self.direction      = direction     # type: int
        self.length         = length        # type: int
        self.width          = width         # type: int
        self.battleId       = battleId      # type: int
        self.flags          = flags         # type: int
        self.bgm            = bgm           # type: int
        self.dangerBGM      = dangerBGM     # type: int
        self.word34         = word34        # type: int
        self.word36         = word36        # type: int
        self.atBonus        = atBonus       # type: int
        self.battleScript   = battleScript  # type: str
        self.monsterSet     = monsterSet    # type: List[ScenaBattleMonsterSet]

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.mapName        = utils.read_fixed_string(fs, 0x10)     # 0x00
        self.x              = fs.ReadFloat()                        # 0x10
        self.y              = fs.ReadFloat()                        # 0x14
        self.z              = fs.ReadFloat()                        # 0x18
        self.direction      = fs.ReadFloat()                        # 0x1C
        self.length         = fs.ReadFloat()                        # 0x20
        self.width          = fs.ReadFloat()                        # 0x24
        self.battleId       = fs.ReadUShort()                       # 0x28

        fs.Position += 2    # padding                               # 0x2A

        self.flags          = fs.ReadULong()                        # 0x2C
        self.bgm            = fs.ReadUShort()                       # 0x30
        self.dangerBGM      = fs.ReadUShort()                       # 0x32
        self.word34         = fs.ReadUShort()                       # 0x34
        self.word36         = fs.ReadUShort()                       # 0x36
        self.atBonus        = fs.ReadULong()                        # 0x38
        self.battleScript   = utils.read_fixed_string(fs, 0x10)     # 0x3C

        self.monsterSet = []                                    # 0x4C

        for _ in range(255):
            monset = ScenaBattleMonsterSet(fs = fs)
            if monset.id == ScenaBattleMonsterSet.InvalidID:
                break

            self.monsterSet.append(monset)

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.pad_string(self.mapName, 0x10))
        fs.write(utils.float_to_bytes(self.x))
        fs.write(utils.float_to_bytes(self.y))
        fs.write(utils.float_to_bytes(self.z))
        fs.write(utils.float_to_bytes(self.direction))
        fs.write(utils.float_to_bytes(self.length))
        fs.write(utils.float_to_bytes(self.width))
        fs.write(utils.int_to_bytes(self.battleId, 2))

        fs.write(b'\x00' * 2) # padding

        fs.write(utils.int_to_bytes(self.flags, 4))
        fs.write(utils.int_to_bytes(self.bgm, 2))
        fs.write(utils.int_to_bytes(self.dangerBGM, 2))
        fs.write(utils.int_to_bytes(self.word34, 2))
        fs.write(utils.int_to_bytes(self.word36, 2))
        fs.write(utils.int_to_bytes(self.atBonus, 4))
        fs.write(utils.pad_string(self.battleScript, 0x10))

        for monset in self.monsterSet:
            fs.write(monset.serialize())

        if self.monsterSet[-1].id != ScenaBattleMonsterSet.InvalidID:
            fs.write(ScenaBattleMonsterSet(ScenaBattleMonsterSet.InvalidID).serialize())

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        body = [
            f'ScenaBattleSetting(',
            f'{DefaultIndent}mapName        = \'{self.mapName}\',',
            f'{DefaultIndent}x              = {self.x},',
            f'{DefaultIndent}y              = {self.y},',
            f'{DefaultIndent}z              = {self.z},',
            f'{DefaultIndent}direction      = {self.direction},',
            f'{DefaultIndent}length         = {self.length},',
            f'{DefaultIndent}width          = {self.width},',
            f'{DefaultIndent}battleId       = {self.battleId},',
            f'{DefaultIndent}flags          = 0x{self.flags:08X},',
            f'{DefaultIndent}bgm            = {self.bgm},',
            f'{DefaultIndent}dangerBGM      = {self.dangerBGM},',
            f'{DefaultIndent}word34         = {self.word34},',
            f'{DefaultIndent}word36         = {self.word36},',
            f'{DefaultIndent}atBonus        = {self.atBonus},',
            f'{DefaultIndent}battleScript   = \'{self.battleScript}\',',
            f'{DefaultIndent}monsterSet     = [',
        ]

        indent2 = DefaultIndent * 2
        for monset in self.monsterSet:
            body.extend([indent2 + l for l in monset.toPython()])
            body[-1] += ','

        body.append(f'{DefaultIndent}],')
        body.append(f')')

        return body

class ScenaAnimeClipItem:
    def __init__(self, type: int = 0, type2: int = 0, dword4: int = 0, name: str = '', *, fs: fileio.FileStream = None):
        '''
            type:
                2 = asset
                3 = eff
                4 = se
                5 = voice
                9 = anime clip
        '''
        self.type   = type
        self.type2  = type2
        self.dword4 = dword4
        self.name   = name

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

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
    def __init__(self, *clips: ScenaAnimeClipItem, fs: fileio.FileStream = None):
        self.clips = clips
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.clips = []
        while True:
            c = ScenaAnimeClipItem(fs = fs)
            if c.type == 0:
                break
            self.clips.append(c)

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
    def __init__(self, catalog: int = 0, asset: str = '', symbol: str = '', *, fs: fileio.FileStream = None):
        self.catalog    = catalog
        self.asset      = asset
        self.symbol     = symbol

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.catalog = fs.ReadULong()
        if self.catalog != 0:
            self.asset  = utils.read_fixed_string(fs, 0x20)
            self.symbol = utils.read_fixed_string(fs, 0x20)

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.catalog, 4))
        if self.catalog != 0:
            fs.write(utils.pad_string(self.asset, 0x20))
            fs.write(utils.pad_string(self.symbol, 0x20))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        f = [
            'ScenaAnimeClipTableEntry(',
            f'{DefaultIndent}catalog    = 0x{self.catalog:08X},',
        ]

        if self.catalog != 0:
            f.extend([
                f"{DefaultIndent}asset      = '{self.asset}',",
                f"{DefaultIndent}symbol     = '{self.symbol}',",
            ])

        f.append(')')

        return f

class ScenaAnimeClipTable:
    def __init__(self, *entries: ScenaAnimeClipTableEntry, fs: fileio.FileStream = None):
        self.entries = entries
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.entries = []
        while True:
            e = ScenaAnimeClipTableEntry(fs = fs)
            if e.catalog == 0:
                break
            self.entries.append(e)

    def serialize(self) -> bytes:
        b = bytearray()

        for e in self.entries:
            b.extend(e.serialize())

        if not self.entries or self.entries[-1].catalog != 0:
            b.extend(ScenaAnimeClipTableEntry(catalog = 0).serialize())

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
    def __init__(self, type: int = 0, word04: int = 0, word06: int = 0, floats08: List[float] = None, *, fs: fileio.FileStream = None):
        self.type       = type
        self.word04     = word04
        self.word06     = word06
        self.floats08   = floats08

        if floats08: assert len(floats08) == 5

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.type       = fs.ReadULong()                                  # 0x00
        self.word04     = fs.ReadUShort()                               # 0x04
        self.word06     = fs.ReadUShort()                               # 0x06
        self.floats08   = [fs.ReadFloat() for _ in range(5)]            # 0x08

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.type, 4))
        fs.write(utils.int_to_bytes(self.word04, 2))
        fs.write(utils.int_to_bytes(self.word06, 2))

        for f in self.floats08:
            fs.write(utils.float_to_bytes(f))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        body = [
            'ScenaFieldMonsterData(',
            f'{DefaultIndent}type       = 0x{self.type:08X},',
            f'{DefaultIndent}word04     = 0x{self.word04:04X},',
            f'{DefaultIndent}word06     = 0x{self.word06:04X},',
            f'{DefaultIndent}floats08   = {self.floats08},',
            ')',
        ]

        return body

class ScenaFieldFollowData:
    def __init__(self, *floats: float, fs: fileio.FileStream = None):
        self.floats = floats
        if floats: assert len(floats) == 5
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.floats = [fs.ReadFloat() for _ in range(5)]

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        for f in self.floats:
            fs.write(utils.float_to_bytes(f))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        params = ['%s' % f for f in self.floats]
        body = [
            'ScenaFieldFollowData(',
            f'{DefaultIndent}{", ".join(params)},',
            ')',
        ]

        return body

class ScenaActionTableEntry:
    InvalidCraftID = 0xFFFF

    def __init__(
        self,
        craftId         : int = 0,
        type            : int = 0,
        attribute       : int = 0,
        rangeType       : int = 0,
        rng             : int = 0,
        area            : int = 0,
        float08         : int = 0,
        float0C         : int = 0,
        float10         : int = 0,
        ariaATDelay     : int = 0,
        atDelay         : int = 0,

        effect1         : int = 0,
        effect2         : int = 0,
        effect3         : int = 0,
        effect4         : int = 0,
        effect5         : int = 0,

        effect1Param1   : int = 0,
        effect1Param2   : int = 0,
        effect1Param3   : int = 0,

        effect2Param1   : int = 0,
        effect2Param2   : int = 0,
        effect2Param3   : int = 0,

        effect3Param1   : int = 0,
        effect3Param2   : int = 0,
        effect3Param3   : int = 0,

        effect4Param1   : int = 0,
        effect4Param2   : int = 0,
        effect4Param3   : int = 0,

        effect5Param1   : int = 0,
        effect5Param2   : int = 0,
        effect5Param3   : int = 0,

        cp              : int = 0,
        flags           : str = '',
        action          : str = '',
        name            : str = '',
        *,
        fs: fileio.FileStream = None,
    ):
        self.craftId        = craftId       # type: int
        self.type           = type          # type: int
        self.attribute      = attribute     # type: int
        self.rangeType      = rangeType     # type: int
        self.rng            = rng           # type: int
        self.area           = area          # type: int
        self.float08        = float08       # type: int
        self.float0C        = float0C       # type: int
        self.float10        = float10       # type: int
        self.ariaATDelay    = ariaATDelay   # type: int
        self.atDelay        = atDelay       # type: int
        self.effect1        = effect1       # type: int
        self.effect2        = effect2       # type: int
        self.effect3        = effect3       # type: int
        self.effect4        = effect4       # type: int
        self.effect5        = effect5       # type: int
        self.effect1Param1  = effect1Param1 # type: int
        self.effect1Param2  = effect1Param2 # type: int
        self.effect1Param3  = effect1Param3 # type: int
        self.effect2Param1  = effect2Param1 # type: int
        self.effect2Param2  = effect2Param2 # type: int
        self.effect2Param3  = effect2Param3 # type: int
        self.effect3Param1  = effect3Param1 # type: int
        self.effect3Param2  = effect3Param2 # type: int
        self.effect3Param3  = effect3Param3 # type: int
        self.effect4Param1  = effect4Param1 # type: int
        self.effect4Param2  = effect4Param2 # type: int
        self.effect4Param3  = effect4Param3 # type: int
        self.effect5Param1  = effect5Param1 # type: int
        self.effect5Param2  = effect5Param2 # type: int
        self.effect5Param3  = effect5Param3 # type: int
        self.cp             = cp            # type: int
        self.flags          = flags         # type: str
        self.action         = action        # type: str
        self.name           = name          # type: str

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.craftId = fs.ReadUShort()                          # 0x00

        if self.craftId == self.InvalidCraftID:
            return

        self.type           = fs.ReadByte()                     # 0x02
        self.attribute      = fs.ReadByte()                     # 0x03
        self.rangeType      = fs.ReadByte()                     # 0x04
        self.rng            = fs.ReadByte()                     # 0x05
        self.area           = fs.ReadByte()                     # 0x06
        pad07               = fs.ReadByte()                     # 0x07
        self.float08        = fs.ReadFloat()                    # 0x08
        self.float0C        = fs.ReadFloat()                    # 0x0C
        self.float10        = fs.ReadFloat()                    # 0x10
        self.ariaATDelay    = fs.ReadUShort()                   # 0x14
        self.atDelay        = fs.ReadByte()                     # 0x16
        pad17               = fs.ReadByte()                     # 0x17
        self.effect1        = fs.ReadUShort()                   # 0x18
        self.effect2        = fs.ReadUShort()                   # 0x1A
        self.effect3        = fs.ReadUShort()                   # 0x1C
        self.effect4        = fs.ReadUShort()                   # 0x1E
        self.effect5        = fs.ReadUShort()                   # 0x20
        pad22               = fs.ReadUShort()                   # 0x22
        self.effect1Param1  = fs.ReadULong()                    # 0x24
        self.effect1Param2  = fs.ReadULong()                    # 0x28
        self.effect1Param3  = fs.ReadULong()                    # 0x2C
        self.effect2Param1  = fs.ReadULong()                    # 0x30
        self.effect2Param2  = fs.ReadULong()                    # 0x34
        self.effect2Param3  = fs.ReadULong()                    # 0x38
        self.effect3Param1  = fs.ReadULong()                    # 0x3C
        self.effect3Param2  = fs.ReadULong()                    # 0x40
        self.effect3Param3  = fs.ReadULong()                    # 0x44
        self.effect4Param1  = fs.ReadULong()                    # 0x48
        self.effect4Param2  = fs.ReadULong()                    # 0x4C
        self.effect4Param3  = fs.ReadULong()                    # 0x50
        self.effect5Param1  = fs.ReadULong()                    # 0x54
        self.effect5Param2  = fs.ReadULong()                    # 0x58
        self.effect5Param3  = fs.ReadULong()                    # 0x5C
        self.cp             = fs.ReadUShort()                   # 0x60
        pad62               = fs.ReadUShort()                   # 0x62
        self.flags          = utils.read_fixed_string(fs, 0x10) # 0x64
        self.action         = utils.read_fixed_string(fs, 0x20) # 0x74
        self.name           = utils.read_fixed_string(fs, 0x40) # 0x94

        assert pad07 == 0
        assert pad17 == 0
        assert pad22 == 0
        assert pad62 == 0

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.craftId, 2))

        if self.craftId != self.InvalidCraftID:
            fs.write(utils.int_to_bytes(self.type, 1))
            fs.write(utils.int_to_bytes(self.attribute, 1))
            fs.write(utils.int_to_bytes(self.rangeType, 1))
            fs.write(utils.int_to_bytes(self.rng, 1))
            fs.write(utils.int_to_bytes(self.area, 1))

            fs.write(b'\x00')

            fs.write(utils.float_to_bytes(self.float08))
            fs.write(utils.float_to_bytes(self.float0C))
            fs.write(utils.float_to_bytes(self.float10))
            fs.write(utils.int_to_bytes(self.ariaATDelay, 2))
            fs.write(utils.int_to_bytes(self.atDelay, 2))
            fs.write(utils.int_to_bytes(self.effect1, 2))
            fs.write(utils.int_to_bytes(self.effect2, 2))
            fs.write(utils.int_to_bytes(self.effect3, 2))
            fs.write(utils.int_to_bytes(self.effect4, 2))
            fs.write(utils.int_to_bytes(self.effect5, 2))

            fs.write(b'\x00' * 2)

            fs.write(utils.int_to_bytes(self.effect1Param1, 4))
            fs.write(utils.int_to_bytes(self.effect1Param2, 4))
            fs.write(utils.int_to_bytes(self.effect1Param3, 4))
            fs.write(utils.int_to_bytes(self.effect2Param1, 4))
            fs.write(utils.int_to_bytes(self.effect2Param2, 4))
            fs.write(utils.int_to_bytes(self.effect2Param3, 4))
            fs.write(utils.int_to_bytes(self.effect3Param1, 4))
            fs.write(utils.int_to_bytes(self.effect3Param2, 4))
            fs.write(utils.int_to_bytes(self.effect3Param3, 4))
            fs.write(utils.int_to_bytes(self.effect4Param1, 4))
            fs.write(utils.int_to_bytes(self.effect4Param2, 4))
            fs.write(utils.int_to_bytes(self.effect4Param3, 4))
            fs.write(utils.int_to_bytes(self.effect5Param1, 4))
            fs.write(utils.int_to_bytes(self.effect5Param2, 4))
            fs.write(utils.int_to_bytes(self.effect5Param3, 4))
            fs.write(utils.int_to_bytes(self.cp, 2))

            fs.write(b'\x00' * 2)

            fs.write(utils.pad_string(self.flags, 0x10))
            fs.write(utils.pad_string(self.action, 0x20))
            fs.write(utils.pad_string(self.name, 0x40))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        return [
            'ScenaActionTableEntry(',
            f'{DefaultIndent}craftId       = 0x{self.craftId:X},',
            f'{DefaultIndent}type          = 0x{self.type:02X},',
            f'{DefaultIndent}attribute     = 0x{self.attribute:02X},',
            f'{DefaultIndent}rangeType     = 0x{self.rangeType:02X},',
            f'{DefaultIndent}rng           = 0x{self.rng:02X},',
            f'{DefaultIndent}area          = 0x{self.area:02X},',
            f'{DefaultIndent}float08       = {self.float08},',
            f'{DefaultIndent}float0C       = {self.float0C},',
            f'{DefaultIndent}float10       = {self.float10},',
            f'{DefaultIndent}ariaATDelay   = {self.ariaATDelay},',
            f'{DefaultIndent}atDelay       = {self.atDelay},',
            f'{DefaultIndent}effect1       = 0x{self.effect1:04X},',
            f'{DefaultIndent}effect2       = 0x{self.effect2:04X},',
            f'{DefaultIndent}effect3       = 0x{self.effect3:04X},',
            f'{DefaultIndent}effect4       = 0x{self.effect4:04X},',
            f'{DefaultIndent}effect5       = 0x{self.effect5:04X},',
            f'{DefaultIndent}effect1Param1 = {self.effect1Param1},',
            f'{DefaultIndent}effect1Param2 = {self.effect1Param2},',
            f'{DefaultIndent}effect1Param3 = {self.effect1Param3},',
            f'{DefaultIndent}effect2Param1 = {self.effect2Param1},',
            f'{DefaultIndent}effect2Param2 = {self.effect2Param2},',
            f'{DefaultIndent}effect2Param3 = {self.effect2Param3},',
            f'{DefaultIndent}effect3Param1 = {self.effect3Param1},',
            f'{DefaultIndent}effect3Param2 = {self.effect3Param2},',
            f'{DefaultIndent}effect3Param3 = {self.effect3Param3},',
            f'{DefaultIndent}effect4Param1 = {self.effect4Param1},',
            f'{DefaultIndent}effect4Param2 = {self.effect4Param2},',
            f'{DefaultIndent}effect4Param3 = {self.effect4Param3},',
            f'{DefaultIndent}effect5Param1 = {self.effect5Param1},',
            f'{DefaultIndent}effect5Param2 = {self.effect5Param2},',
            f'{DefaultIndent}effect5Param3 = {self.effect5Param3},',
            f'{DefaultIndent}cp            = {self.cp},',
            f"{DefaultIndent}flags         = '{self.flags}',",
            f"{DefaultIndent}action        = '{self.action}',",
            f"{DefaultIndent}name          = '{self.name}',",
            ')',
        ]

class ScenaActionTable:
    def __init__(self, *actions: ScenaActionTableEntry, fs: fileio.FileStream = None):
        self.actions = actions
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.actions = []
        while True:
            entry = ScenaActionTableEntry(fs = fs)
            if entry.craftId == ScenaActionTableEntry.InvalidCraftID:
                break

            self.actions.append(entry)

    def serialize(self) -> bytes:
        b = bytearray()
        for e in self.actions:
            b.extend(e.serialize())

        if not self.actions or self.actions[-1].craftId != ScenaActionTableEntry.InvalidCraftID:
            b.extend(ScenaActionTableEntry(craftId = ScenaActionTableEntry.InvalidCraftID).serialize())

        return bytes(b)

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

    InvalidID = 0

    def __init__(
            self,
            craftId         : int       = 0,
            aiType          : int       = 0,
            probability     : int       = 0,
            maxNumOfUses    : int       = 0,
            targetType      : int       = 0,
            parameters1     : List[int] = None,
            parameters2     : List[int] = None,
            *,
            fs: fileio.FileStream       = None,
        ):

        self.craftId            = craftId
        self.aiType             = aiType                # 0x0F: SBreak
        self.probability        = probability
        self.maxNumOfUses       = maxNumOfUses
        self.targetType         = targetType
        self.parameters1        = parameters1
        self.parameters2        = parameters2

        if parameters1: assert len(parameters1) == 3
        if parameters2: assert len(parameters2) == 3

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        if fs.Remaining < 2:
            return

        self.craftId            = fs.ReadUShort()                       # 0x00
        if self.craftId == self.InvalidID:
            return

        self.aiType             = fs.ReadByte()                         # 0x02
        self.probability        = fs.ReadByte()                         # 0x03
        self.maxNumOfUses       = fs.ReadByte()                         # 0x04
        self.targetType         = fs.ReadByte()                         # 0x05

        pad06 = fs.ReadUShort()                       # 0x06      always 0

        self.parameters1        = [fs.ReadULong() for _ in range(3)]    # 0x08      params for aiType
        self.parameters2        = [fs.ReadULong() for _ in range(3)]    # 0x14      params for targetType

        assert pad06 == 0

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.craftId, 2))
        fs.write(utils.int_to_bytes(self.aiType, 1))
        fs.write(utils.int_to_bytes(self.probability, 1))
        fs.write(utils.int_to_bytes(self.maxNumOfUses, 1))
        fs.write(utils.int_to_bytes(self.targetType, 1))
        fs.write(b'\x00' * 2)

        for p in self.parameters1 + self.parameters2:
            fs.write(utils.int_to_bytes(p, 4))

        fs.seek(0)

        return fs.read()

    def toPython(self) -> List[str]:
        return [
            'ScenaAlgoTableEntry(',
            f'{DefaultIndent}craftId            = 0x{self.craftId:X},',
            f'{DefaultIndent}aiType             = 0x{self.aiType:02X},',
            f'{DefaultIndent}probability        = {self.probability},',
            f'{DefaultIndent}maxNumOfUses       = 0x{self.maxNumOfUses:02X},',
            f'{DefaultIndent}targetType         = 0x{self.targetType:02X},',
            f'{DefaultIndent}parameters1        = {self.parameters1},',
            f'{DefaultIndent}parameters2        = {self.parameters2},',
            ')',
        ]

class ScenaAlgoTable:
    def __init__(self, *entries: ScenaAlgoTableEntry, fs: fileio.FileStream = None):
        self.entries = entries
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.entries = []
        for _ in range(0x40):
            e = ScenaAlgoTableEntry(fs = fs)
            if e.craftId == ScenaAlgoTableEntry.InvalidID:
                break

            self.entries.append(e)

    def serialize(self) -> bytes:
        b = bytearray()
        for e in self.entries:
            b.extend(e.serialize())

        if not self.entries or self.entries[-1].craftId != ScenaAlgoTableEntry.InvalidID:
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

class ScenaWeaponAttTable:
    def __init__(self, *attrs: int, fs: fileio.FileStream = None):
        self.weaponAttributeData = attrs
        if attrs: assert len(attrs) == 4
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.weaponAttributeData = [fs.ReadByte() for _ in range(4)]

    def serialize(self) -> bytes:
        return bytes(self.weaponAttributeData)

    def toPython(self) -> List[str]:
        params = ['%d' % a for a in self.weaponAttributeData]
        return [
            f'ScenaWeaponAttTable({", ".join(params)})',
        ]

class ScenaBreakTable:
    InvalidID = 0

    def __init__(self, *breakData: Tuple[int, int], fs: fileio.FileStream = None):
        self.breakData = breakData
        if breakData:
            assert isinstance(breakData, tuple)
            for d in breakData:
                assert isinstance(d, (tuple, list))
                assert len(d) == 2

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.breakData = []

        for _ in range(0x40):
            d = fs.ReadULong()
            if d == self.InvalidID:
                break

            self.breakData.append((d & 0xFFFF, (d >> 16) & 0xFFFF))

    def serialize(self) -> bytes:
        fs = io.BytesIO()
        for d in self.breakData:
            fs.write(utils.int_to_bytes(d[0] | (d[1] << 16), 4))

        fs.write(utils.int_to_bytes(self.InvalidID, 4))
        fs.seek(0)
        return fs.read()

    def toPython(self) -> List[str]:
        f = [
            f'ScenaBreakTable(',
            f'{DefaultIndent}# ActionID, probability',
        ]

        for d in self.breakData:
            f.append(f'{DefaultIndent}({"0x%X, %d" % d}),',)

        f.append(')')
        return f

class ScenaSummonTableEntry:
    InvalidID = 0xFFFF

    def __init__(self, id: int = 0, byte2: int = 0, byte3: int = 0, name: str = '', *, fs: fileio.FileStream = None):
        self.id     = id
        self.byte2  = byte2
        self.byte3  = byte3
        self.name   = name

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.id     = fs.ReadUShort()                   # 0x00
        if self.id == self.InvalidID:
            return

        self.byte2  = fs.ReadByte()                     # 0x02
        self.byte3  = fs.ReadByte()                     # 0x03
        self.name   = utils.read_fixed_string(fs, 0x20) # 0x04

    def serialize(self) -> bytes:
        fs = io.BytesIO()
        fs.write(utils.int_to_bytes(self.id, 2))
        fs.write(utils.int_to_bytes(self.byte2, 1))
        fs.write(utils.int_to_bytes(self.byte3, 1))
        fs.write(utils.pad_string(self.name, 0x20))
        fs.seek(0)
        return fs.read()

    def toPython(self) -> List[str]:
        return [
            f'ScenaSummonTableEntry(0x{self.id:04X}, 0x{self.byte2:02X}, 0x{self.byte3:02X}, \'{self.name}\')',
        ]

class ScenaSummonTable:
    def __init__(self, *summons: ScenaSummonTableEntry, fs: fileio.FileStream = None):
        self.summons = summons
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.summons = []
        while True:
            s = ScenaSummonTableEntry(fs = fs)
            if s.id == ScenaSummonTableEntry.InvalidID:
                break

            self.summons.append(s)

    def serialize(self) -> bytes:
        b = bytearray()

        for s in self.summons:
            b.extend(s.serialize())

        if not self.summons or self.summons[-1].id != ScenaSummonTableEntry.InvalidID:
            b.extend(ScenaSummonTableEntry(ScenaSummonTableEntry.InvalidID).serialize())

        return bytes(b)

    def toPython(self) -> List[str]:
        f = [
            f'ScenaSummonTable(',
        ]

        for a in self.summons:
            f.extend([DefaultIndent + l for l in a.toPython()])
            f[-1] += ','

        f.append(')')

        return f

class ScenaAddCollision:
    InvalidID = 0

    def __init__(self, *entries: List[float], fs: fileio.FileStream = None):
        assert isinstance(entries, tuple | list)
        for e in entries:
            assert isinstance(e, tuple | list)
            assert len(e) == 6

        self.entries = entries
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        count = fs.ReadByte()
        self.entries = []
        for _ in range(count):
            id = fs.ReadUShort()
            if id == self.InvalidID:
                break

            fs.Position += 2
            self.entries.append((id, *[fs.ReadFloat() for _ in range(5)]))

    def serialize(self) -> bytes:
        b = bytearray()
        b.extend(utils.int_to_bytes(len(self.entries), 1))

        for e in self.entries:
            b.extend(utils.int_to_bytes(e[0], 4))
            for f in e[1:]:
                b.extend(utils.float_to_bytes(f))

        return bytes(b)

    def toPython(self) -> List[str]:
        return [
            f'ScenaAddCollision(',
            *[f'{DefaultIndent}({e[0]}, {", ".join(["%f" % f for f in e[1:]])}),' for e in self.entries],
            ')',
        ]


class ScenaPartTableEntry:
    InvalidID = 0xFF

    def __init__(self, id: int = 0, name1: str = '', name2: str = '', *, fs: fileio.FileStream = None):
        self.id = id
        self.name1 = name1
        self.name2 = name2

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.id     = fs.ReadULong()
        self.name1  = utils.read_fixed_string(fs, 0x20)
        self.name2  = utils.read_fixed_string(fs, 0x20)

    def serialize(self) -> bytes:
        fs = io.BytesIO()
        fs.write(utils.int_to_bytes(self.id, 4))
        fs.write(utils.pad_string(self.name1, 0x20))
        fs.write(utils.pad_string(self.name2, 0x20))
        fs.seek(0)
        return fs.read()

    def toPython(self) -> List[str]:
        return [
            f'ScenaPartTableEntry({self.id}, \'{self.name1}\', \'{self.name2}\')',
        ]

class ScenaPartTable:
    def __init__(self, *parts: ScenaPartTableEntry, fs: fileio.FileStream = None):
        self.parts = parts
        if parts: assert len(parts) <= 4
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.parts = []
        for _ in range(4):
            e = ScenaPartTableEntry(fs = fs)
            if e.id == ScenaPartTableEntry.InvalidID:
                break

            self.parts.append(e)

    def serialize(self) -> bytes:
        b = bytearray()

        for s in self.parts:
            b.extend(s.serialize())

        if not self.parts or (len(self.parts) < 4 and self.parts[-1].id != ScenaPartTableEntry.InvalidID):
            b.extend(ScenaPartTableEntry(ScenaPartTableEntry.InvalidID).serialize())

        return bytes(b)

    def toPython(self) -> List[str]:
        f = [
            f'ScenaPartTable(',
        ]

        for p in self.parts:
            f.extend([DefaultIndent + l for l in p.toPython()])
            f[-1] += ','

        f.append(')')

        return f

class ScenaReactionTableEntry:
    InvalidID = 0

    def __init__(self, craftId: int = 0, word02: int = 0, word04: int = 0, word06: int = 0, floats08: List[float] = None, type: int = 0, *, fs: fileio.FileStream = None):
        self.craftId    = craftId
        self.word02     = word02
        self.word04     = word04
        self.word06     = word06
        self.floats08   = floats08
        self.type       = type

        if floats08: assert len(floats08) == 12

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.craftId    = fs.ReadUShort()
        self.word02     = fs.ReadUShort()
        self.word04     = fs.ReadUShort()
        self.word06     = fs.ReadUShort()
        self.floats08   = [fs.ReadFloat() for _ in range(12)]
        self.type       = fs.ReadULong()

    def serialize(self) -> bytes:
        fs = io.BytesIO()
        fs.write(utils.int_to_bytes(self.craftId, 2))
        fs.write(utils.int_to_bytes(self.word02, 2))
        fs.write(utils.int_to_bytes(self.word04, 2))
        fs.write(utils.int_to_bytes(self.word06, 2))
        [fs.write(utils.float_to_bytes(f)) for f in self.floats08]
        fs.write(utils.int_to_bytes(self.type, 4))
        fs.seek(0)
        return fs.read()

    def toPython(self) -> List[str]:
        return [
            f'ScenaReactionTableEntry(',
            f'{DefaultIndent}craftId    = 0x{self.craftId:04X},',
            f'{DefaultIndent}word02     = 0x{self.word02:04X},',
            f'{DefaultIndent}word04     = 0x{self.word04:04X},',
            f'{DefaultIndent}word06     = 0x{self.word06:04X},',
            f'{DefaultIndent}floats08   = {self.floats08},',
            f'{DefaultIndent}type       = {self.type},',
            f')',
        ]

class ScenaReactionTable:
    def __init__(self, *reactions: ScenaReactionTableEntry, fs: fileio.FileStream = None):
        self.reactions = reactions
        if reactions: assert len(reactions) <= 8
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.reactions = []
        for _ in range(4):
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

class ScenaFaceAuto:
    def __init__(self, s: str = '', *, fs: fileio.FileStream = None):
        self.s = s
        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.s = utils.read_fixed_string(fs, 0x10)

    def serialize(self) -> bytes:
        return utils.pad_string(self.s, 0x10)

    def toPython(self) -> List[str]:
        return [f"ScenaFaceAuto('{self.s}')"]
