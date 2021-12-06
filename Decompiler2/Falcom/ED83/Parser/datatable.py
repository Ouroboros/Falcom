from Falcom.Common import *
from . import utils

__all__ = (
    'DataTable',
    'TableNameEntry',
    'TableDataEntry',
    'NameTableData',
    'AttachTableData',
    'EventTableData',
)

class TableNameEntry:
    def __init__(self, fs: fileio.FileStream):
        self.name = fs.ReadMultiByte()
        self.entryCount = fs.ReadULong()

    def __str__(self):
        return f'{self.name} @ {self.entryCount}'

    __repr__ = __str__

class TableDataEntry:
    ENTRY_NAME = ''

    def __init__(self, fs: fileio.FileStream):
        if not fs:
            return

        self.entryName  = fs.ReadMultiByte()
        self.entrySize  = fs.ReadUShort()

    def toPython(self) -> List[str]:
        raise NotImplementedError

    def __str__(self):
        return '\n'.join(self.toPython())

    __repr__ = __str__

class DataTable:
    @staticmethod
    def create(*args, **kwargs):
        return createDataTable(*args, **kwargs)

    def __init__(self, *, fs: fileio.FileStream):
        self.fs = fs

        if fs:
            self.entryCount = fs.ReadUShort()
            self.tableCount = fs.ReadULong()
            self.tables = [TableNameEntry(fs) for _ in range(self.tableCount)]

            self.load(fs)

    def load(self, fs: fileio.FileStream):
        entryMap = {
            'NameTableData'     : NameTableData,
            'AttachTableData'   : AttachTableData,
            'EventTableData'    : EventTableData,
        }

        self.entries = []
        entryCount = sum([e.entryCount for e in self.tables])

        for _ in range(entryCount):
            with fs.PositionSaver:
                header = TableDataEntry(fs)

            cls = entryMap[header.entryName]
            entry = cls(fs = fs)
            self.entries.append(entry)

    def toPython(self, filename: str) -> List[str]:
        f = [
            'from Falcom.ED83.Parser.datatable import *',
            '',
            f"DataTable.create('{filename}',",
        ]

        for e in self.entries:
            f.extend([f'{GlobalConfig.DefaultIndent}{l}' for l in e.toPython()])
            f[-1] += ','

        f.append(')')

        return f

    def serialize(self) -> bytes:
        raise NotImplementedError

    def __str__(self):
        return f'{self.tables}'

    __repr__ = __str__

class NameTableData(TableDataEntry):
    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.chrId      = fs.ReadUShort()
            self.chrName    = fs.ReadMultiByte()
            self.model      = fs.ReadMultiByte()
            self.ani        = fs.ReadMultiByte()
            self.faceDefault= fs.ReadMultiByte()
            self.face       = fs.ReadMultiByte()
            self.name2      = fs.ReadMultiByte()
            self.dword1     = fs.ReadULong()
            self.dword2     = fs.ReadULong()
            self.dword3     = fs.ReadULong()
            self.dword4     = fs.ReadULong()
            self.word5      = fs.ReadUShort()
            self.byte6      = fs.ReadByte()

    def toPython(self) -> List[str]:
        return [
            'NameTableData(',
            f'    chrId         = 0x{self.chrId:04X},',
            f"    chrName       = '{self.chrName}',",
            f"    model         = '{self.model}',",
            f"    ani           = '{self.ani}',",
            f"    faceDefault   = '{self.faceDefault}',",
            f"    face          = '{self.face}',",
            f"    name2         = '{self.name2}',",
            f'    dword1        = 0x{self.dword1:08X},',
            f'    dword2        = 0x{self.dword2:08X},',
            f'    dword3        = 0x{self.dword3:08X},',
            f'    dword4        = 0x{self.dword4:08X},',
            f'    word5         = 0x{self.word5:04X},',
            f'    byte6         = 0x{self.byte6:02X},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.chrId, 2))
        body.extend(utils.str_to_bytes(self.chrName))
        body.extend(utils.str_to_bytes(self.model))
        body.extend(utils.str_to_bytes(self.ani))
        body.extend(utils.str_to_bytes(self.faceDefault))
        body.extend(utils.str_to_bytes(self.face))
        body.extend(utils.str_to_bytes(self.name2))
        body.extend(utils.int_to_bytes(self.dword1, 4))
        body.extend(utils.int_to_bytes(self.dword2, 4))
        body.extend(utils.int_to_bytes(self.dword3, 4))
        body.extend(utils.int_to_bytes(self.dword4, 4))
        body.extend(utils.int_to_bytes(self.word5, 2))
        body.extend(utils.int_to_bytes(self.byte6, 1))

        return bytes(body)

class AttachTableData(TableDataEntry):
    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.chrId      = fs.ReadUShort()
            self.dword02    = fs.ReadULong()
            self.itemId     = fs.ReadULong()
            self.scenaFlags = fs.ReadULong()
            self.dword0E    = fs.ReadULong()
            self.dword12    = fs.ReadULong()
            self.str16      = fs.ReadMultiByte()
            self.str17      = fs.ReadMultiByte()

    def toPython(self) -> List[str]:
        return [
            'AttachTableData(',
            f'    chrId      = 0x{self.chrId:04X},',
            f"    dword02    = {self.dword02},",
            f"    itemId     = 0x{self.itemId:08X},",
            f"    scenaFlags = 0x{self.scenaFlags:08X},",
            f"    dword0E    = {self.dword0E},",
            f"    dword12    = {self.dword12},",
            f"    str16      = '{self.str16}',",
            f"    str17      = '{self.str17}',",
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.chrId, 2))
        body.extend(utils.int_to_bytes(self.dword02, 4))
        body.extend(utils.int_to_bytes(self.itemId, 4))
        body.extend(utils.int_to_bytes(self.scenaFlags, 4))
        body.extend(utils.int_to_bytes(self.dword0E, 4))
        body.extend(utils.int_to_bytes(self.dword12, 4))
        body.extend(utils.str_to_bytes(self.str16))
        body.extend(utils.str_to_bytes(self.str17))

        return bytes(body)

class EventTableData(TableDataEntry):
    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.eventId    = fs.ReadUShort()
            self.eventEntry = fs.ReadMultiByte()
            self.scena      = fs.ReadMultiByte()
            self.word01     = fs.ReadUShort()
            self.word02     = fs.ReadUShort()
            self.word03     = fs.ReadUShort()
            self.str04      = fs.ReadMultiByte()
            self.word05     = fs.ReadUShort()
            self.word06     = fs.ReadUShort()
            self.word07     = fs.ReadUShort()
            self.word08     = fs.ReadUShort()
            self.word09     = fs.ReadUShort()
            self.word0A     = fs.ReadUShort()
            self.word0B     = fs.ReadUShort()
            self.word0C     = fs.ReadUShort()
            self.word0D     = fs.ReadUShort()

    def toPython(self) -> List[str]:
        return [
            'EventTableData(',
            f'    eventId       = 0x{self.eventId:X},',
            f"    eventEntry    = '{self.eventEntry}',",
            f"    scena         = '{self.scena}',",
            f'    word01        = 0x{self.word01:X},',
            f'    word02        = 0x{self.word02:X},',
            f'    word03        = 0x{self.word03:X},',
            f"    str04         = '{self.str04}',",
            f'    word05        = 0x{self.word05:X},',
            f'    word06        = 0x{self.word06:X},',
            f'    word07        = 0x{self.word07:X},',
            f'    word08        = 0x{self.word08:X},',
            f'    word09        = 0x{self.word09:X},',
            f'    word0A        = 0x{self.word0A:X},',
            f'    word0B        = 0x{self.word0B:X},',
            f'    word0C        = 0x{self.word0C:X},',
            f'    word0D        = 0x{self.word0D:X},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.eventId, 2))
        body.extend(utils.str_to_bytes(self.eventEntry))
        body.extend(utils.str_to_bytes(self.scena))
        body.extend(utils.int_to_bytes(self.word01, 2))
        body.extend(utils.int_to_bytes(self.word02, 2))
        body.extend(utils.int_to_bytes(self.word03, 2))
        body.extend(utils.str_to_bytes(self.str04))
        body.extend(utils.int_to_bytes(self.word05, 2))
        body.extend(utils.int_to_bytes(self.word06, 2))
        body.extend(utils.int_to_bytes(self.word07, 2))
        body.extend(utils.int_to_bytes(self.word08, 2))
        body.extend(utils.int_to_bytes(self.word09, 2))
        body.extend(utils.int_to_bytes(self.word0A, 2))
        body.extend(utils.int_to_bytes(self.word0B, 2))
        body.extend(utils.int_to_bytes(self.word0C, 2))
        body.extend(utils.int_to_bytes(self.word0D, 2))

        return bytes(body)

def createDataTable(filename: str, *entries):
    table = bytearray()
    data = bytearray()

    table.extend(utils.int_to_bytes(len(entries), 2))

    entryCounter = {}

    for e in entries:
        tableName = e.ENTRY_NAME
        if not tableName:
            tableName = e.__class__.__name__

        entryCounter[tableName] = entryCounter.get(tableName, 0) + 1

        body = e.serialize()

        data.extend(utils.str_to_bytes(tableName))
        data.extend(utils.int_to_bytes(len(body), 2))
        data.extend(body)

    table.extend(utils.int_to_bytes(len(entryCounter), 4))
    for name, count in entryCounter.items():
        table.extend(utils.str_to_bytes(name))
        table.extend(utils.int_to_bytes(count, 4))

    table.extend(data)

    padding = b'\x00' * (((len(table) + 0x10) & ~0x0F) - len(table))
    table.extend(padding)

    open(filename, 'wb').write(table)

    return entries
