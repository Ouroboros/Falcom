from Falcom.Common import *
from . import utils

class ScenaFunctionParamType(IntEnum2):
    Value   = 0x01
    Offset  = 0x02
    Mask    = 0x03

class ScenaFunctionParamFlags(IntEnum2):
    Output      = 0x04
    Nullable    = 0x08
    Mask        = 0x0C

class ScenaHeader:
    MAGIC = b'#scp'

    def __init__(self, *, fs: fileio.FileStream = None):
        self.magic                  = self.MAGIC        # type: int
        self.functionEntryOffset    = 0                 # type: int
        self.functionCount          = 0                 # type: int
        self.globalVarOffset        = 0                 # type: int
        self.globalVarCount         = 0                 # type: int

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        assert fs.Read(4) == self.MAGIC

        self.functionEntryOffset    = fs.ReadULong()    # 0x04
        self.functionCount          = fs.ReadULong()    # 0x08
        self.globalVarOffset        = fs.ReadULong()    # 0x0C
        self.globalVarCount         = fs.ReadULong()    # 0x10
        self.dword_14               = fs.ReadULong()    # 0x14

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(self.MAGIC)
        fs.write(utils.int_to_bytes(self.functionEntryOffset, 4))
        fs.write(utils.int_to_bytes(self.functionCount, 4))
        fs.write(utils.int_to_bytes(self.globalVarOffset, 4))
        fs.write(utils.int_to_bytes(self.globalVarCount, 4))
        fs.write(utils.int_to_bytes(self.dword_14, 4))

        return fs.getvalue()

class ScenaFunctionEntry:
    def __init__(
            self,
            addr                : int = 0,
            paramCount          : int = 0,
            byte05              : int = 0,
            byte06              : int = 0,
            constCount          : int = 0,
            constOffset         : int = 0,
            paramFlagsOffset    : int = 0,
            debugSymbolCount    : int = 0,
            debugSymbolOffset   : int = 0,
            nameCrc32           : int = 0,
            nameOffset          : int = 0,
            *,
            fs: fileio.FileStream = None
        ):
        self.addr               = addr
        self.paramCount         = paramCount
        self.byte05             = byte05
        self.byte06             = byte06
        self.constCount         = constCount
        self.constOffset        = constOffset
        self.paramFlagsOffset   = paramFlagsOffset
        self.debugSymbolCount   = debugSymbolCount
        self.debugSymbolOffset  = debugSymbolOffset
        self.nameCrc32          = nameCrc32
        self.nameOffset         = nameOffset
        self.name               = None

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.addr               = fs.ReadULong()
        self.paramCount         = fs.ReadByte()
        self.byte05             = fs.ReadByte()
        self.byte06             = fs.ReadByte()
        self.constCount         = fs.ReadByte()
        self.constOffset        = fs.ReadULong()
        self.paramFlagsOffset   = fs.ReadULong()
        self.debugSymbolCount   = fs.ReadULong()
        self.debugSymbolOffset  = fs.ReadULong()
        self.nameCrc32          = fs.ReadULong()
        self.nameOffset         = fs.ReadULong()

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.addr, 4))

        return fs.getvalue()

    def toPython(self) -> List[str]:
        f = [
            'ScenaFunctionEntry(',
            f'{defaultIndent()}addr              = 0x{self.addr:08X},',
            f'{defaultIndent()}paramCount        = 0x{self.paramCount:08X},',
            f'{defaultIndent()}byte05            = 0x{self.byte05:02X},',
            f'{defaultIndent()}byte06            = 0x{self.byte06:02X},',
            f'{defaultIndent()}constCount        = 0x{self.constCount :08X},',
            f'{defaultIndent()}constOffset       = 0x{self.constOffset :08X},',
            f'{defaultIndent()}paramFlagsOffset  = 0x{self.paramFlagsOffset:08X},',
            f'{defaultIndent()}debugSymbolCount  = 0x{self.debugSymbolCount:08X},',
            f'{defaultIndent()}debugSymbolOffset = 0x{self.debugSymbolOffset:08X},',
            f'{defaultIndent()}nameCrc32         = 0x{self.nameCrc32:08X},',
            f'{defaultIndent()}name              = \'{self.name}\',' if self.name else
            f'{defaultIndent()}nameOffset        = 0x{self.nameOffset:08X},',
            ')',
        ]

        return f

class ScenaVariable:
    def __init__(self, value: int = 0, flags: int = 0, *, fs: fileio.FileStream = None):
        self.value  = value
        self.flags  = flags

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.value = fs.ReadULong()
        self.flags = fs.ReadULong()

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.flags, 4))

        return fs.getvalue()

    def toPython(self) -> List[str]:
        f = [
            'ScenaVariable(',
            f'{defaultIndent()}flags = 0x{self.flags:08X},',
            ')',
        ]

        return f

class ScenaFunctionType(IntEnum2):
    Invalid             = 0
    Code                = 1

ScenaDataFunctionTypes = set([
])

class ScenaFunction:
    def __init__(self, index: int, offset: int, name: str, *, type: ScenaFunctionType = ScenaFunctionType.Invalid, entry: ScenaFunctionEntry = None):
        self.index  = index
        self.offset = offset
        self.name   = name
        self.type   = type
        self.obj    = None
        self.entry  = entry

    def __str__(self) -> str:
        return f'0x{self.index:04X} 0x{self.offset:08X} {repr(self.name)} {self.type}'