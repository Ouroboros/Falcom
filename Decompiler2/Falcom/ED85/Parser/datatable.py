from Falcom.Common import *
from Falcom.ED84.Parser.datatable import *
from Falcom.ED84.Parser.datatable import createDataTable

class MapBgmTableData(TableDataEntry):
    DESCRIPTOR  = (
        ('map',     'M'),
        ('bgmId',   'H'),
        ('word03',  'W'),
        ('word04',  'W'),
    )

class EventTableData(TableDataEntry):
    DESCRIPTOR = (
        ('eventId',         'W'),
        ('eventEntry',      'S'),
        ('word01',          'W'),
        ('word02',          'W'),
        ('desc',            'S'),
        ('jumpEntry',       'S'),
        ('word03',          'W'),
        ('word04',          'W'),
        ('scena',           'S'),
        ('word05',          'W'),
        ('nextEventId',     'W'),
        ('word06',          'W'),
        ('str04',           'S'),
        ('word07',          'W'),
        ('word08',          'W'),
        ('word09',          'W'),
        ('word0A',          'W'),
        ('word0B',          'W'),
        ('word0C',          'W'),
        ('word0D',          'W'),
        ('word0E',          'W'),
    )

class EventGroupData(TableDataEntry):
    DESCRIPTOR  = (
        ('id',      'W'),
        ('name',    'S'),
    )

DataTable.DataTableDataTypes.update({
    'MapBgmTableData'       : MapBgmTableData,
    'EventTableData'        : EventTableData,
    'EventGroupData'        : EventGroupData,
})

DataTable.PythonHeader = [
    'from Falcom.ED85.Parser.datatable import *',
    '',
    'entries = [',
]
