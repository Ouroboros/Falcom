from Assembler.function import Function
from Falcom.ED6.InstructionTable.utils import formatText
from .scena_types import *
from ..InstructionTable import ScenaOpTable as ED6ScenaOpTable
import pathlib

__all__ = (
    'ScenaParser',
    'ScenaHeader',
    'ScenaFunctionType',
    'ScenaFunction',
)

class ScenaFormatter(Assembler.Formatter):
    def formatLabel(self, name: str) -> List[str]:
        return [
            f'def _{name}(): pass',
            '',
            f"label('{name}')",
        ]

    def formatFuncion(self, func: ScenaFunction) -> List[str]:
        funcName = func.name
        if not funcName:
            funcName = f'func_{func.index:02X}_{func.offset:X}'

        f = [
            f'# id: 0x{func.index:04X} offset: 0x{func.offset:X}',
            f'@scena.{func.type}(\'{func.name}\')',
            f'def {funcName}():',
        ]

        if func.type in ScenaDataFunctionTypes:
            body = self.formatDataFunction(func)

        elif func.type == ScenaFunctionType.Code:
            body = self.formatCode(func)

        else:
            raise NotImplementedError(f'unknown func type: {func.type}')

        if not body:
            body = ['pass']

        f.extend([f'{GlobalConfig.DefaultIndent}{l}'.rstrip() for l in body])
        if f[-1] != '':
            f.append('')

        return f

    def formatCode(self, f: ScenaFunction) -> List[str]:
        func: Function = f.obj

        if func is None:
            return

        body = []
        blk = self.formatBlock(func.block, genLabel = False)
        for b in blk:
            body.append(b)

        return body

    def formatDataFunction(self, f: ScenaFunction) -> List[str]:
        if f.obj is None:
            return

        match f.type:
            case ScenaFunctionType.Header:
                hdr: ScenaHeader = f.obj
                comma = ', '
                return [
                    f'header = ScenaHeader()',
                    f"header.mapName        = '{hdr.mapName}'",
                    f"header.mapModel       = '{hdr.mapModel}'",
                    f'header.mapIndex       = {hdr.mapIndex}',
                    f'header.bgm            = {hdr.bgm}',
                    f'header.flags          = 0x{hdr.flags:04X}',
                    f'header.entryFunction  = 0x{hdr.entryFunction:04X}',
                    f'header.importTable    = [{comma.join([t.nameOrValue for t in hdr.importTable])}]',
                    f'header.reserved       = {hdr.reserved}',
                    'return header'
                ]

            case ScenaFunctionType.StringTable:
                return ['return stringTable']

            case ScenaFunctionType.ChipData:
                ch, cp = f.obj
                ch: list[ScenaChipData]
                cp: list[ScenaChipData]

                n = max(len(ch), len(cp))
                ch.extend([None] * (n - len(ch)))
                cp.extend([None] * (n - len(cp)))

                return [
                    'return [',
                    f'{GlobalConfig.DefaultIndent}# (ch, cp)',
                    *[f'{GlobalConfig.DefaultIndent}({ch[i] and ch[i].nameOrValue}, {cp[i] and cp[i].nameOrValue}),' for i in range(n)],
                    ']',
                ]

            case _:
                body = [
                    'return (',
                ]

                for o in f.obj:
                    for l in o.toPython():
                        body.append(f'{GlobalConfig.DefaultIndent}{l}')

                    body[-1] += ','

                body.append(')')

                return body

class ScenaParser:
    def __init__(self, fs: fileio.FileStream):
        self.fs                 = fs                # type: fileio.FileStream
        self.name               = ''                # type: str
        self.header             = None              # type: ScenaHeader
        self.functions          = []                # type: List[ScenaFunction]
        self.stringTable        = []                # type: List[str]

    def __str__(self) -> str:
        funcs = "\n".join([str(f) for f in self.functions])
        return '\n'.join([
            f'mapName               = {self.header.mapName}',
            f'mapModel              = {self.header.mapModel}',
            f'bgm                   = 0x{self.header.bgm:04X}',
            f'flags                 = 0x{self.header.flags:04X}',
            f'entryFunction         = 0x{self.header.entryFunction:X}',
            f'importTable           = {self.header.importTable}',
            f'reversed              = {self.header.reserved}',
            f'dataTable             = {self.header.dataTable}',
            f'stringTableOffset     = 0x{self.header.stringTableOffset:04X}',
            f'headerSize            = 0x{self.header.headerSize:04X}',
            f'functionTable         = {self.header.functionTable}',
            '',
            f'functions: \n{funcs}',
            '',
        ])

    def parse(self):
        self.readHeader()
        self.disasmFunctions()

    def readHeader(self):
        fs = self.fs
        fs.Position = 0

        self.header = ScenaHeader(fs = fs)
        hdr = self.header

        self.functions.append(ScenaFunction(index = 0xFFFF, offset = 0, name = 'Header', type = ScenaFunctionType.Header, obj = hdr))

        self.parseDataTable()

        fs.Position = hdr.functionTable.offset

        funcNames = {
            0: 'PreInit',
            1: 'Init',
            2: 'ReInit',
        }
        for i in range(hdr.functionTable.size // 2):
            offset = fs.ReadUShort()
            self.functions.append(ScenaFunction(index = i, offset = offset, name = funcNames.get(i, f'func_{i:02X}_{offset:X}'), type = ScenaFunctionType.Code))

    def parseDataTable(self):
        fs = self.fs
        dataTable = self.header.dataTable
        funcIndex = 0xFFFF

        def readTable(constructor, entry: ScenaDataIndex) -> list:
            fs.Position = entry.offset
            return [constructor(fs = fs) for _ in range(entry.size)]

        def createFunc(offset: int, type: ScenaFunctionType, obj: Any):
            nonlocal funcIndex
            self.functions.append(ScenaFunction(index = funcIndex, offset = offset, name = str(type), type = type, obj = obj))
            funcIndex += 1

        fs.Position = self.header.stringTableOffset
        data = fs.Read()
        self.stringTable = [s.decode(GlobalConfig.DefaultEncoding) for s in data.split(b'\x00')]

        createFunc(self.header.stringTableOffset, ScenaFunctionType.StringTable, self.stringTable)
        createFunc(self.header.entryPointOffset, ScenaFunctionType.EntryPoint, self.header.entryPoint)
        createFunc(dataTable[ScenaDataTableType.ChipDataCH].offset, ScenaFunctionType.ChipData, (readTable(ScenaChipData, dataTable[0]), readTable(ScenaChipData, dataTable[1])))

        for constructor, index, type in (
                (ScenaNpcData,      ScenaDataTableType.NpcData,        ScenaFunctionType.NpcData),
                (ScenaMonsterData,  ScenaDataTableType.MonsterData,    ScenaFunctionType.MonsterData),
                (ScenaEventData,    ScenaDataTableType.EventData,      ScenaFunctionType.EventData),
                (ScenaActorData,    ScenaDataTableType.ActorData,      ScenaFunctionType.ActorData),
            ):
            createFunc(dataTable[index].offset, type, readTable(constructor, dataTable[index]))

    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED6ScenaOpTable)
        ctx = Assembler.DisasmContext(fs)

        for func in self.functions:
            log.debug(f'disasm func: {func}')

            match func.type:
                case ScenaFunctionType.Code:
                    fs.Position = func.offset
                    try:
                        func.obj = dis.disasmFunction(ctx, name = func.name)
                    except KeyError as e:
                        e.args = (f'0x{e.args[0]:X} ({e.args[0]})',)
                        raise

                case _:
                    if func.type not in ScenaDataFunctionTypes:
                        raise NotImplementedError(f'unknown func type: {func.type}')

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(ED6ScenaOpTable, name = self.name)

        linefeed = '\n'

        lines = f'''\
import sys
sys.path.append(r'{pathlib.Path(__file__).parent.parent.parent.parent}')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import {pathlib.Path(filename).stem.strip()}_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('{filename}')

stringTable = [
{linefeed.join([f'{GlobalConfig.DefaultIndent}TXT(0x{i:02X}, {formatText(s)}),' for i, s in enumerate(self.stringTable)])}
]

'''.splitlines()

        for func in self.functions:
            lines.extend(formatter.formatFuncion(func))

        main = '''\
def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

'''

        lines.extend(main.splitlines())

        # print('\n'.join(lines))

        return lines
