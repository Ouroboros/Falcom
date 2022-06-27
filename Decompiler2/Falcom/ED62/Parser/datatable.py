from Falcom.Common import *
from Falcom.ED6.Parser.datatable import *

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
        ('status',          'D'),
        ('name',            'S'),
    )

    @classmethod
    def readIndexes(cls, fs: fileio.FileStream) -> list[int]:
        fs.Position = 2
        indexes = []
        while True:
            offset = fs.ReadUShort()
            indexes.append(offset)
            with fs.PositionSaver:
                fs.Position = offset
                if fs.ReadUShort() == 2999:
                    break

        return indexes

    @classmethod
    def writeIndexes(cls, fs: fileio.FileStream, indexes: list[int]):
        fs.Position = 0
        fs.WriteUShort(len(indexes) * 2 + 2)
        [fs.WriteUShort(offset) for offset in indexes]

class MagicTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('craftId',             'W'),
        ('target',              'B'),
        ('flags',               'B'),
        ('attr',                'B'),
        ('areaType',            'B'),
        ('effect1',             'B'),
        ('effect2',             'B'),
        ('rng',                 'W'),
        ('areaSize',            'W'),
        ('atAria',              'W'),
        ('at',                  'W'),
        ('ep_cp',               'W'),
        ('position',            'W'),
        ('effect1Param',        'W'),
        ('effect1Time',         'W'),
        ('effect2Param',        'W'),
        ('effect2Time',         'W'),
        ('name',                'S'),
        ('desc',                'S'),
    )

    @classmethod
    def readIndexes(cls, fs: fileio.FileStream) -> list[int]:
        fs.Position = 0
        entryCount = fs.ReadUShort() // 2
        fs.Position = 0
        return [fs.ReadUShort() for _ in range(entryCount)]

    @classmethod
    def writeIndexes(cls, fs: fileio.FileStream, indexes: list[int]):
        fs.Position = 0
        [fs.WriteUShort(offset) for offset in indexes]

DataTable.PythonHeader = [
    'from Falcom.ED62.Parser.datatable import *',
    '',
    'entries = [',
]

DataTable.DataTableDataTypes.update({
    't_name'    : NameTableData,
    't_magic'   : MagicTableData,
})
