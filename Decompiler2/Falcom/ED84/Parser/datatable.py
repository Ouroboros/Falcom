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

class VoiceTableData(TableDataEntry):
    ENTRY_NAME = 'voice'

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.id     = fs.ReadUShort()
            self.symbol = fs.ReadMultiByte()
            self.file   = fs.ReadMultiByte()
            self.word4  = fs.ReadUShort()
            self.float5 = fs.ReadFloat()
            self.float6 = fs.ReadFloat()
            self.word7  = fs.ReadUShort()
            self.word8  = fs.ReadUShort()
            self.float9 = fs.ReadFloat()
            self.text   = fs.ReadMultiByte()

    def toPython(self) -> List[str]:
        return [
            f'{self.__class__.__name__}(',
            f'    id        = 0x{self.id:04X},',
            f"    symbol    = '{self.symbol}',",
            f"    file      = '{self.file}',",
            f'    word4     = {self.word4},',
            f'    float5    = {self.float5},',
            f'    float6    = {self.float6},',
            f'    word7     = {self.word7},',
            f'    word8     = {self.word8},',
            f'    float9    = {self.float9},',
            f"    text      = '{self.text}',",
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.id, 2))
        body.extend(utils.str_to_bytes(self.symbol))
        body.extend(utils.str_to_bytes(self.file))
        body.extend(utils.int_to_bytes(self.word4, 2))
        body.extend(utils.float_to_bytes(self.float5))
        body.extend(utils.float_to_bytes(self.float6))
        body.extend(utils.int_to_bytes(self.word7, 2))
        body.extend(utils.int_to_bytes(self.word8, 2))
        body.extend(utils.float_to_bytes(self.float9))
        body.extend(utils.str_to_bytes(self.text))

        return bytes(body)


DataTable.DataTableDataTypes.update({
    'bgm'   : BGMTableData,
    'voice' : VoiceTableData,
})

DataTable.PythonHeader = [
    'from Falcom.ED84.Parser.datatable import *',
    '',
    'entries = [',
]
