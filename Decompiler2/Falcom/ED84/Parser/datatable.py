from Falcom.Common import *
from Falcom.ED83.Parser.datatable import *
from Falcom.ED83.Parser.datatable import createDataTable
from . import utils

class BGMTableData(TableDataEntry):
    ENTRY_NAME = 'bgm'

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.id     = fs.ReadUShort()
            self.file   = fs.ReadMultiByte()
            self.word3  = fs.ReadUShort()
            self.float4 = fs.ReadFloat()

    def toPython(self) -> List[str]:
        return [
            f'{self.__class__.__name__}(',
            f'    id     = {self.id},',
            f"    file   = '{self.file}',",
            f'    word3  = {self.word3},',
            f'    float4 = {self.float4:g},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.id, 2))
        body.extend(utils.str_to_bytes(self.file))
        body.extend(utils.int_to_bytes(self.word3, 2))
        body.extend(utils.float_to_bytes(self.float4))

        return bytes(body)


DataTable.DataTableDataTypes.update({
    'bgm'               : BGMTableData,
})

DataTable.PythonHeader = [
    'from Falcom.ED84.Parser.datatable import *',
    '',
    'entries = [',
]
