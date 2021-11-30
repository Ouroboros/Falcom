from Falcom.Common import *
from . import utils

__all__ = (
    'DataTable',
    'TableNameEntry',
    'TableDataEntry',
    'NameTableData',
)

class TableNameEntry:
    def __init__(self, fs: fileio.FileStream):
        self.name = fs.ReadMultiByte()
        self.entryCount = fs.ReadULong()

    def __str__(self):
        return f'{self.name} @ {self.entryCount}'

    __repr__ = __str__

class TableDataEntry:
    def __init__(self, fs: fileio.FileStream):
        if not fs:
            return

        self.entryName  = fs.ReadMultiByte()
        self.entrySize  = fs.ReadUShort()

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
            'NameTableData' : NameTableData,
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

    def __str__(self):
        return '\n'.join(self.toPython())

    __repr__ = __str__

def createDataTable(filename: str, *entries):
    table = bytearray()
    data = bytearray()

    table.extend(utils.int_to_bytes(len(entries), 2))

    entryCounter = {}

    for e in entries:
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
