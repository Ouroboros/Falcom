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

class DATIndex:
    INVALID_INDEX = 0xFFFFFFFF

    def __init__(self, *, fs: fileio.FileStream) -> None:
        self.dat    = 0     # type: int
        self.index  = 0     # type: int
        self.value  = 0     # type: int

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        v = fs.ReadULong()

        self.dat    = v >> 16
        self.index  = v & 0xFFFF
        self.value  = v

    @property
    def datName(self) -> str:
        return f'ED6_DT{self.dat:02d}'

    @property
    def fileName(self) -> str:
        return '<None>'

    def __str__(self) -> str:
        return f'({self.datName}, 0x{self.index:X})' if self.value != self.INVALID_INDEX else '<None>'

    __repr__ = __str__

class ScenaDataIndex:
    def __init__(self, *, fs: fileio.FileStream = None):
        self.offset = 0     # type: int
        self.size   = 0     # type: int

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.offset = fs.ReadUShort()
        self.size   = fs.ReadUShort()

    def __str__(self) -> str:
        return f'(0x{self.offset:X}, 0x{self.size:X})'

    __repr__ = __str__

class ScenaEntryPoint:
    SIZE = 0x44

    def __init__(self, *, fs: fileio.FileStream = None):
        self.dword_00           = 0             # type: int
        self.dword_04           = 0             # type: int
        self.dword_08           = 0             # type: int
        self.word_0C            = 0             # type: int
        self.word_0E            = 0             # type: int
        self.dword_10           = 0             # type: int
        self.dword_14           = 0             # type: int
        self.dword_18           = 0             # type: int
        self.dword_1C           = 0             # type: int
        self.dword_20           = 0             # type: int
        self.dword_24           = 0             # type: int
        self.dword_28           = 0             # type: int
        self.dword_2C           = 0             # type: int
        self.word_30            = 0             # type: int
        self.word_32            = 0             # type: int
        self.word_34            = 0             # type: int
        self.word_36            = 0             # type: int
        self.word_38            = 0             # type: int
        self.word_3A            = 0             # type: int
        self.preInitScena       = 0             # type: int
        self.preInitFunction    = 0             # type: int
        self.initScena          = 0             # type: int
        self.initFunction       = 0             # type: int

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.dword_00           = fs.ReadULong()
        self.dword_04           = fs.ReadULong()
        self.dword_08           = fs.ReadULong()
        self.word_0C            = fs.ReadUShort()
        self.word_0E            = fs.ReadUShort()
        self.dword_10           = fs.ReadULong()
        self.dword_14           = fs.ReadULong()
        self.dword_18           = fs.ReadULong()
        self.dword_1C           = fs.ReadULong()
        self.dword_20           = fs.ReadULong()
        self.dword_24           = fs.ReadULong()
        self.dword_28           = fs.ReadULong()
        self.dword_2C           = fs.ReadULong()
        self.word_30            = fs.ReadUShort()
        self.word_32            = fs.ReadUShort()
        self.word_34            = fs.ReadUShort()
        self.word_36            = fs.ReadUShort()
        self.word_38            = fs.ReadUShort()
        self.word_3A            = fs.ReadUShort()
        self.preInitScena       = fs.ReadUShort()
        self.preInitFunction    = fs.ReadUShort()       # byte
        self.initScena          = fs.ReadUShort()
        self.initFunction       = fs.ReadUShort()       # byte

class ScenaHeader:
    IMPORT_SCENA_COUNT  = 8
    DATA_TABLE_COUNT    = 6

    def __init__(self, *, fs: fileio.FileStream = None):
        self.mapName                = ''                # type: str
        self.mapModel               = ''                # type: str
        self.bgm                    = 0                 # type: int
        self.flags                  = 0                 # type: int
        self.entryFunction          = 0                 # type: int
        self.importTable            = []                # type: List[int]
        self.reversed               = 0                 # type: int
        self.dataTable              = []                # type: List[ScenaDataIndex]
        self.stringTableOffset      = 0                 # type: int
        self.headerSize             = []                # type: int
        self.functionTable          = []                # type: ScenaDataIndex
        self.entryPoint             = []                # type: List[ScenaEntryPoint]

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.mapName            = utils.read_fixed_string(fs, 0x0A)                                             # 0x00
        self.mapModel           = utils.read_fixed_string(fs, 0x0E)                                             # 0x0A
        self.mapIndex           = fs.ReadUShort()                                                               # 0x18
        self.bgm                = fs.ReadUShort()                                                               # 0x1A
        self.flags              = fs.ReadUShort()                                                               # 0x1C
        self.entryFunction      = fs.ReadUShort()                                                               # 0x1E
        self.importTable        = [DATIndex(fs = fs) for _ in range(self.IMPORT_SCENA_COUNT)]                   # 0x20
        self.reversed           = fs.ReadUShort()                                                               # 0x40
        self.dataTable          = [ScenaDataIndex(fs = fs) for _ in range(self.DATA_TABLE_COUNT)]               # 0x42
        self.stringTableOffset  = fs.ReadUShort()                                                               # 0x5A
        self.headerSize         = fs.ReadULong()                                                                # 0x5C
        self.functionTable      = ScenaDataIndex(fs = fs)                                                       # 0x60

        entryPointCount = (self.dataTable[0].offset - fs.Position) // ScenaEntryPoint.SIZE
        for _ in range(entryPointCount):
            self.entryPoint.append(ScenaEntryPoint(fs = fs))

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
    def __init__(self, index: int, offset: int, name: str, *, type = ScenaFunctionType.Invalid):
        self.index  = index
        self.offset = offset
        self.name   = name
        self.type   = type
        self.obj    = None

    def __str__(self) -> str:
        return f'{self.name}(index = 0x{self.index:04X}, offset = 0x{self.offset:08X}, type = {self.type})'

    __repr__ = __str__
