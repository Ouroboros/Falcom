from Falcom.Common import *

__all__ = (
    'DataTable',
    'TableNameEntry',
)

class TableNameEntry:
    def __init__(self, fs):
        self.name = fs.ReadMultiByte()
        self.entryCount = fs.ReadULong()

    def __str__(self):
        return f'{self.name} @ {self.entryCount}'

    __repr__ = __str__

class DataTable:
    def __init__(self, fs):
        self.entryCount = fs.ReadUShort()
        self.tableCount = fs.ReadULong()
        self.tableName = [TableNameEntry(fs) for _ in range(self.tableCount)]
        self.data = fileio.MemoryStream(data = fs.Read(), encoding = fs.Encoding)

    def __str__(self):
        return f'{self.tableName}'

    __repr__ = __str__
