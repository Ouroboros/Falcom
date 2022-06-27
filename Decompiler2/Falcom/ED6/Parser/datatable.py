from Falcom.Common import *
from . import utils
from .scena_types import DATFileIndex
import pathlib

__all__ = (
    'DataTable',
    'TableDataEntry',
    'NameTableData',
    'TownTableData',
)

class TableDataEntry:
    # ENTRY_NAME = ''
    DESCRIPTOR: Tuple[str, str] = None

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        if not fs:
            return

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
            's' : lambda v: f"'{v}'",
            'S' : lambda v: f"'{v}'",
            'D' : lambda v: v.nameOrValue,
        }

        for name, type in self.DESCRIPTOR:
            value = getattr(self, name)
            lines.append(f'    {name.ljust(align)}= {formatter[type](value)},')

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
            's' : lambda v: utils.str_to_bytes(v),
            'S' : lambda v: utils.str_to_bytes(v),
            'D' : lambda v: DATFileIndex(v).value,
        }

        body = bytearray()

        for name, type in self.DESCRIPTOR:
            if name.startswith('__'):
                continue

            body.extend(writer[type](getattr(self, name)))

        return body

    def deserialize(self, fs: fileio.FileStream):
        if not self.DESCRIPTOR:
            return

        def readStr() -> str:
            offset = fs.ReadUShort()
            with fs.PositionSaver:
                fs.Position = offset
                return fs.ReadMultiByte(cp = GlobalConfig.DefaultEncoding)

        def readDATEntry() -> DATFileIndex:
            return DATFileIndex(fs = fs)

        reader = {
            'B' : lambda: fs.ReadByte(),
            'C' : lambda: fs.ReadByte(),
            'H' : lambda: fs.ReadUShort(),
            'W' : lambda: fs.ReadUShort(),
            'I' : lambda: fs.ReadULong(),
            'L' : lambda: fs.ReadULong(),
            'M' : lambda: fs.ReadULong(),
            'f' : lambda: fs.ReadFloat(),
            'S' : readStr,
            's' : lambda: fs.ReadMultiByte(),
            'D' : readDATEntry,
        }

        for name, type in self.DESCRIPTOR:
            if name == '__index':
                value = 0
            else:
                value = reader[type]()
            setattr(self, name, value)

    @classmethod
    def readIndexes(cls, fs: fileio.FileStream) -> list[int]:
        fs.Position = 0
        entryCount = fs.ReadUShort()
        return [fs.ReadUShort() for _ in range(entryCount)]

    def __str__(self):
        return '\n'.join(self.toPython())

    __repr__ = __str__


class TownTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('__index',         'I'),
        ('name',            's'),
    )

class NameTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('chrId',           'W'),
        ('word_02',         'W'),
        ('walkCH',          'D'),
        ('runCH',           'D'),
        ('walkCP',          'D'),
        ('runCP',           'D'),
        ('ms1',             'D'),
        ('ms2',             'D'),
        ('name',            'S'),
    )

    @classmethod
    def readIndexes(cls, fs: fileio.FileStream) -> list[int]:
        fs.Position = 0
        entryCount = fs.ReadUShort() // 2
        fs.Position = 0
        return [fs.ReadUShort() for _ in range(entryCount)]

class DataTable:
    DataTableDataTypes = {
        't_name'            : NameTableData,
        't_town'            : TownTableData,
    }

    PythonHeader = [
        'from Falcom.ED6.Parser.datatable import *',
        '',
        'entries = [',
    ]

    @staticmethod
    def create(*args, **kwargs):
        # return createDataTable(*args, **kwargs)
        pass

    def __init__(self, *, filename: str):
        fs = fileio.FileStream(filename, encoding = GlobalConfig.DefaultEncoding, endian = GlobalConfig.StructEndian)
        fs.Open(filename, 'rb')

        self.fs = fs
        self.tableName = pathlib.Path(filename).stem.strip().lower()

        if fs:
            try:
                self.load(fs)
            except:
                print(f'pos = 0x{fs.Position:X}')
                raise

    def load(self, fs: fileio.FileStream):
        cls: TableDataEntry = self.DataTableDataTypes[self.tableName]
        indexes = cls.readIndexes(fs)
        self.entries = []

        for index, offset in enumerate(indexes):
            fs.Position = offset
            entry = cls(fs = fs)
            if hasattr(entry, '__index'):
                setattr(entry, '__index', index)
            self.entries.append(entry)

    def toPython(self, filename: str) -> List[str]:
        f = self.PythonHeader.copy()

        for e in self.entries:
            f.extend([f'{GlobalConfig.DefaultIndent}{l}' for l in e.toPython()])
            f[-1] += ','

        f.extend([
            ']',
            '',
            "if __name__ == '__main__':",
            f"{GlobalConfig.DefaultIndent}DataTable.create('{filename}', *entries)",
            '',
        ])

        return f

    def serialize(self) -> bytes:
        raise NotImplementedError

    def __str__(self):
        return f'{self.entries}'

    __repr__ = __str__
