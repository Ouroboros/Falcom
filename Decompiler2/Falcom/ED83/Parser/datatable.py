from Falcom.Common import *
from . import utils

__all__ = (
    'DataTable',
    'TableNameEntry',
    'TableDataEntry',
    'NameTableData',
    'AttachTableData',
    'EventTableData',
    'StatusTableData',
    'VoiceTableData',
    'SETableData',
    'BGMTableData',
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
    DESCRIPTOR: Tuple[str, str] = None

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        if not fs:
            return

        self.entryName  = fs.ReadMultiByte()
        self.entrySize  = fs.ReadUShort()

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

class NameTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('chrId',           'W'),
        ('chrName',         'S'),
        ('model',           'S'),
        ('ani',             'S'),
        ('faceModel',       'S'),
        ('faceTexture',     'S'),
        ('name2',           'S'),
        ('dword1',          'L'),
        ('dword2',          'L'),
        ('dword3',          'L'),
        ('dword4',          'L'),
        ('word5',           'W'),
        ('byte6',           'B'),
    )

class AttachTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('chrId',       'W'),
        ('type',        'I'),
        ('itemId',      'L'),
        ('scenaFlags',  'L'),
        ('dword0E',     'I'),
        ('dword12',     'I'),
        ('model',       'S'),
        ('str17',       'S'),
    )

class EventTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('eventId',         'W'),
        ('eventEntry',      'S'),
        ('scena',           'S'),
        ('word01',          'W'),
        ('nextEventId',     'W'),
        ('word03',          'W'),
        ('str04',           'S'),
        ('word05',          'W'),
        ('word06',          'W'),
        ('word07',          'W'),
        ('word08',          'W'),
        ('word09',          'W'),
        ('word0A',          'W'),
        ('word0B',          'W'),
        ('word0C',          'W'),
        ('word0D',          'W'),
    )

class StatusTableData(TableDataEntry):
    ENTRY_NAME = 'status'
    DESCRIPTOR  = (
        ('algoFile',             'S'),
        ('model',                'S'),
        ('ani',                  'S'),
        ('float1',               'f'),
        ('float2',               'f'),
        ('float3',               'f'),
        ('float4',               'f'),
        ('float5',               'f'),
        ('float6',               'f'),
        ('float7',               'f'),
        ('short8',               'W'),
        ('short9',               'W'),
        ('byte10',               'B'),
        ('level',                'C'),
        ('hpBase',               'I'),
        ('hpFactor',             'f'),
        ('epMax',                'H'),
        ('epInit',               'H'),
        ('cpMax',                'H'),
        ('cpInit',               'H'),
        ('str',                  'H'),
        ('strFactor',            'f'),
        ('def_',                 'H'),
        ('defFactor',            'f'),
        ('ats',                  'H'),
        ('atsFactor',            'f'),
        ('adf',                  'H'),
        ('adfFactor',            'f'),
        ('dex',                  'H'),
        ('dexFactor',            'f'),
        ('agl',                  'H'),
        ('aglFactor',            'f'),
        ('evade',                'H'),
        ('spd',                  'H'),
        ('spdFactor',            'f'),
        ('mov',                  'H'),
        ('movFactor',            'f'),
        ('exp',                  'H'),
        ('expFactor',            'f'),
        ('brk',                  'H'),
        ('brkFactor',            'f'),
        ('efficacyEarth',        'C'),
        ('efficacyWater',        'C'),
        ('efficacyFire',         'C'),
        ('efficacyWind',         'C'),
        ('efficacyTime',         'C'),
        ('efficacySpace',        'C'),
        ('efficacyMirage',       'C'),
        ('efficacyPoison',       'C'),
        ('efficacySeal',         'C'),
        ('efficacyMute',         'C'),
        ('efficacyBlind',        'C'),
        ('efficacySleep',        'C'),
        ('efficacyBurn',         'C'),
        ('efficacyFreeze',       'C'),
        ('efficacyPetrify',      'C'),
        ('efficacyFaint',        'C'),
        ('efficacyConfuse',      'C'),
        ('efficacyCharm',        'C'),
        ('efficacyDeathblow',    'C'),
        ('efficacyNightmare',    'C'),
        ('efficacyATDelay',      'C'),
        ('efficacyVanish',       'C'),
        ('efficacySPDDown',      'C'),
        ('efficacySlash',        'H'),
        ('efficacyThurst',       'H'),
        ('efficacyPierce',       'H'),
        ('efficacyStrike',       'H'),
        ('sepithEarth',          'C'),
        ('sepithWater',          'C'),
        ('sepithFire',           'C'),
        ('sepithWind',           'C'),
        ('sepithTime',           'C'),
        ('sepithSpace',          'C'),
        ('sepithMirage',         'C'),
        ('sepithMass',           'C'),
        ('sepithEarthFactor',    'f'),
        ('sepithWaterFactor',    'f'),
        ('sepithFireFactor',     'f'),
        ('sepithWindFactor',     'f'),
        ('sepithTimeFactor',     'f'),
        ('sepithSpaceFactor',    'f'),
        ('sepithMirageFactor',   'f'),
        ('sepithMassFactor',     'f'),
        ('dropItemId1',          'W'),
        ('dropRate1',            'C'),
        ('dropItemId2',          'W'),
        ('dropRate2',            'C'),
        ('float11',              'f'),
        ('float12',              'f'),
        ('flags',                'S'),
        ('name',                 'S'),
        ('description',          'S'),
    )

class VoiceTableData(TableDataEntry):
    ENTRY_NAME = 'voice'
    DESCRIPTOR  = (
        ('id',      'W'),
        ('symbol',  'S'),
        ('file',    'S'),
        ('word4',   'H'),
        ('float5',  'f'),
        ('float6',  'f'),
        ('word7',   'H'),
        ('word8',   'H'),
        ('float9',  'f'),
    )

class SETableData(VoiceTableData):
    ENTRY_NAME = 'se'

class BGMTableData(TableDataEntry):
    ENTRY_NAME = 'bgm'
    DESCRIPTOR  = (
        ('id',      'H'),
        ('file',    'S'),
        ('word3',   'H'),
    )

class ItemHelpData(TableDataEntry):
    DESCRIPTOR  = (
        ('id',      'W'),
        ('desc',    'S'),
        ('word3',   'W'),
        ('word4',   'W'),
        ('word5',   'W'),
        ('word6',   'W'),
        ('byte7',   'B'),
    )

class CompHelpData(TableDataEntry):
    DESCRIPTOR  = (
        ('id',      'W'),
        ('desc',    'S'),
        ('value',   'I'),
    )

class MapBgmTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('mapId',   'L'),
        ('bgmId',   'H'),
    )

class DataTable:
    DataTableDataTypes = {
        'NameTableData'     : NameTableData,
        'AttachTableData'   : AttachTableData,
        'EventTableData'    : EventTableData,
        'ItemHelpData'      : ItemHelpData,
        'CompHelpData'      : CompHelpData,
        'MapBgmTableData'   : MapBgmTableData,
        'status'            : StatusTableData,
        'voice'             : VoiceTableData,
        'se'                : SETableData,
        'bgm'               : BGMTableData,
    }

    PythonHeader = [
        'from Falcom.ED83.Parser.datatable import *',
        '',
        'entries = [',
    ]

    @staticmethod
    def create(*args, **kwargs):
        return createDataTable(*args, **kwargs)

    def __init__(self, *, fs: fileio.FileStream):
        self.fs = fs

        if fs:
            self.entryCount = fs.ReadUShort()
            self.tableCount = fs.ReadULong()
            self.tables = [TableNameEntry(fs) for _ in range(self.tableCount)]

            try:
                self.load(fs)
            except:
                print(f'pos = 0x{fs.Position:X}')
                raise

    def load(self, fs: fileio.FileStream):
        self.entries = []
        entryCount = sum([e.entryCount for e in self.tables])

        for _ in range(entryCount):
            with fs.PositionSaver:
                header = TableDataEntry(fs = fs)

            cls = self.DataTableDataTypes[header.entryName]
            entry = cls(fs = fs)
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
        return f'{self.tables}'

    __repr__ = __str__


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
