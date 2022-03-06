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

DataTable.DataTableDataTypes.update({
    'MapBgmTableData'       : MapBgmTableData,
})

DataTable.PythonHeader = [
    'from Falcom.ED85.Parser.datatable import *',
    '',
    'entries = [',
]
