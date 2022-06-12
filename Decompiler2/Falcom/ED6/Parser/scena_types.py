from Falcom.Common import *
from . import utils

class ScenaTypeBase:
    DESCRIPTOR: Tuple[str, str] = None

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
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
            'i' : lambda v: f'{v}',
            'I' : lambda v: f'{v}',
            'L' : lambda v: f'0x{v:08X}',
            'f' : lambda v: f'{v:g}.0' if f'{v:g}'.count('.') == 0 else f'{v:g}',
            'S' : lambda v: f"{repr(v)}",
        }

        for name, type in self.DESCRIPTOR:
            type = type.split(':', maxsplit = 1)[0]
            value = getattr(self, name)
            lines.append(f'{GlobalConfig.DefaultIndent}{name.ljust(align)}= {formatter[type](value)},')

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
            'i' : lambda v: utils.int_to_bytes(v, 4),
            'I' : lambda v: utils.int_to_bytes(v, 4),
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
            'i' : lambda: fs.ReadLong(),
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

class DATFileIndex:
    INVALID_INDEX = 0xFFFFFFFF

    def __init__(self, value: int = INVALID_INDEX, *, fs: fileio.FileStream = None) -> None:
        if isinstance(value, str):
            value = GlobalConfig.DirTable[value]

        self.value = value             # type: int
        self.read(fs)

    @property
    def dat(self) -> int:
        return self.value >> 16

    @property
    def index(self) -> int:
        return self.value & 0xFFFF

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.value = fs.ReadULong()

    def serialize(self) -> bytes:
        buf = bytearray()
        buf.extend(utils.int_to_bytes(self.value, 4))
        return bytes(buf)

    @property
    def datName(self) -> str:
        return f'ED6_DT{self.dat:02d}'

    @property
    def fileName(self) -> str | None:
        if GlobalConfig.DirTable:
            name = GlobalConfig.DirTable.get(f'{self.value:08X}')
            if name is None:
                return None

            return f"'{name}'"

        return None

    @property
    def nameOrValue(self) -> str:
        name = self.fileName
        if name is not None:
            return name

        return "0x%08X" % self.value

    def __str__(self) -> str:
        return f'({self.datName}, 0x{self.index:X})' if self.value != self.INVALID_INDEX else '<None>'

    __repr__ = __str__

class ScenaDataIndex:
    def __init__(self, offset: int = 0, size: int = 0, *, fs: fileio.FileStream = None):
        self.offset = offset    # type: int
        self.size   = size      # type: int

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.offset = fs.ReadUShort()
        self.size   = fs.ReadUShort()

    def serialize(self) -> bytes:
        buf = bytearray()
        buf.extend(utils.int_to_bytes((self.size << 16) | self.offset, 4))
        return bytes(buf)

    def __str__(self) -> str:
        return f'(0x{self.offset:X}, 0x{self.size:X})'

    __repr__ = __str__

class ScenaEntryPoint(ScenaTypeBase):
    SIZE = 0x44
    DESCRIPTOR = (
        ('dword_00',        'L'),
        ('dword_04',        'L'),
        ('dword_08',        'L'),
        ('word_0C',         'W'),
        ('word_0E',         'W'),
        ('dword_10',        'i'),
        ('dword_14',        'i'),
        ('dword_18',        'i'),
        ('dword_1C',        'i'),
        ('dword_20',        'i'),
        ('dword_24',        'i'),
        ('dword_28',        'i'),
        ('dword_2C',        'i'),
        ('word_30',         'H'),
        ('word_32',         'H'),
        ('word_34',         'H'),
        ('word_36',         'H'),
        ('word_38',         'H'),
        ('word_3A',         'H'),
        ('preInitScena',    'W'),
        ('preInitFunction', 'W'),
        ('initScena',       'W'),
        ('initFunction',    'W'),
    )

class ScenaHeader:
    IMPORT_SCENA_COUNT  = 8
    DATA_TABLE_COUNT    = 6

    def __init__(self, *, fs: fileio.FileStream = None):
        self.mapName                = ''                                            # type: str
        self.mapModel               = ''                                            # type: str
        self.bgm                    = 0                                             # type: int
        self.flags                  = 0                                             # type: int
        self.entryFunction          = 0                                             # type: int
        self.importTable            = [DATFileIndex()] * self.IMPORT_SCENA_COUNT    # type: List[DATFileIndex]
        self.reserved               = 0                                             # type: int
        self.dataTable              = [ScenaDataIndex()] * self.DATA_TABLE_COUNT    # type: List[ScenaDataIndex]
        self.stringTableOffset      = 0                                             # type: int
        self.headerSize             = 0                                             # type: int
        self.functionTable          = ScenaDataIndex()                              # type: ScenaDataIndex
        self.entryPoint             = []                                            # type: List[ScenaEntryPoint]
        self.entryPointOffset       = 0                                             # type: int

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
        self.importTable        = [DATFileIndex(fs = fs) for _ in range(self.IMPORT_SCENA_COUNT)]               # 0x20
        self.reserved           = fs.ReadUShort()                                                               # 0x40
        self.dataTable          = [ScenaDataIndex(fs = fs) for _ in range(self.DATA_TABLE_COUNT)]               # 0x42
        self.stringTableOffset  = fs.ReadUShort()                                                               # 0x5A
        self.headerSize         = fs.ReadULong()                                                                # 0x5C
        self.functionTable      = ScenaDataIndex(fs = fs)                                                       # 0x60
        self.entryPointOffset   = fs.Position

        entryPointCount = (self.dataTable[0].offset - self.entryPointOffset) // ScenaEntryPoint.SIZE
        for _ in range(entryPointCount):
            self.entryPoint.append(ScenaEntryPoint(fs = fs))

    def serialize(self) -> bytes:
        assert len(self.importTable) == self.IMPORT_SCENA_COUNT
        assert len(self.dataTable) == self.DATA_TABLE_COUNT

        buf = bytearray()

        buf.extend(utils.pad_string(self.mapName, 0x0A))
        buf.extend(utils.pad_string(self.mapModel, 0x0E))
        buf.extend(utils.int_to_bytes(self.mapIndex, 2))
        buf.extend(utils.int_to_bytes(self.bgm, 2))
        buf.extend(utils.int_to_bytes(self.flags, 2))
        buf.extend(utils.int_to_bytes(self.entryFunction, 2))

        for idx in self.importTable:
            buf.extend(idx.serialize())

        buf.extend(utils.int_to_bytes(self.reserved, 2))

        for idx in self.dataTable:
            buf.extend(idx.serialize())

        buf.extend(utils.int_to_bytes(self.stringTableOffset, 2))
        buf.extend(utils.int_to_bytes(self.headerSize, 4))
        buf.extend(self.functionTable.serialize())

        for e in self.entryPoint:
            buf.extend(e.serialize())

        return bytes(buf)

class ScenaChipData(DATFileIndex):
    pass

class ScenaNpcData(ScenaTypeBase):
    DESCRIPTOR = (
        ('x',                   'i'),
        ('z',                   'i'),
        ('y',                   'i'),
        ('direction',           'H'),
        ('word_0E',             'H'),
        ('dword_10',            'I'),
        ('chipIndex',           'H'),
        ('npcIndex',            'H'),
        ('initFunctionIndex',   'W'),
        ('initScenaIndex',      'W'),
        ('talkFunctionIndex',   'W'),
        ('talkScenaIndex',      'W'),
    )

class ScenaMonsterData(ScenaTypeBase):
    DESCRIPTOR = (
        ('x',           'i'),
        ('z',           'i'),
        ('y',           'i'),
        ('word_0C',     'W'),
        ('word_0E',     'W'),
        ('byte_10',     'B'),
        ('byte_11',     'B'),
        ('dword_12',    'L'),
        ('battleIndex', 'W'),
        ('word_18',     'W'),
        ('word_1A',     'W'),
    )

class ScenaEventData(ScenaTypeBase):
    DESCRIPTOR = (
        ('x',           'i'),
        ('y',           'i'),
        ('z',           'i'),
        ('range',       'i'),
        ('dword_10',    'L'),
        ('dword_14',    'L'),
        ('dword_18',    'L'),
        ('dword_1C',    'L'),
    )

class ScenaActorData(ScenaTypeBase):
    DESCRIPTOR = (
        ('triggerX',            'i'),
        ('triggerZ',            'i'),
        ('triggerY',            'i'),
        ('triggerRange',        'i'),
        ('actorX',              'i'),
        ('actorZ',              'i'),
        ('actorY',              'i'),
        ('flags',               'W'),
        ('talkScenaIndex',      'W'),
        ('talkFunctionIndex',   'W'),
        ('word_22',             'W'),
    )

class ScenaFunctionType(IntEnum2):
    Invalid             = 0
    Code                = 1
    ChipData            = 2
    NpcData             = 3
    MonsterData         = 4
    EventData           = 5
    ActorData           = 6
    StringTable         = 7
    Header              = 8
    EntryPoint          = 9

class ScenaDataTableType(IntEnum2):
    ChipDataCH  = 0
    ChipDataCP  = 1
    NpcData     = 2
    MonsterData = 3
    EventData   = 4
    ActorData   = 5

ScenaDataFunctionTypes = set([
    ScenaFunctionType.Header,
    ScenaFunctionType.StringTable,
    ScenaFunctionType.EntryPoint,
    ScenaFunctionType.ChipData,
    ScenaFunctionType.NpcData,
    ScenaFunctionType.MonsterData,
    ScenaFunctionType.EventData,
    ScenaFunctionType.ActorData,
])

class ScenaFunction:
    def __init__(self, index: int, offset: int, name: str, *, type = ScenaFunctionType.Invalid, obj = None):
        self.index  = index
        self.offset = offset
        self.name   = name
        self.type   = type
        self.obj    = obj

    def __str__(self) -> str:
        return f'{self.name}(index = 0x{self.index:04X}, offset = 0x{self.offset:08X}, type = {self.type})'

    __repr__ = __str__
