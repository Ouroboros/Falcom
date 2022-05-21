from ntpath import join
from Assembler.function import Function
from Assembler.instruction import Instruction
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
            funcName = f'func_{func.offset:X}'

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

        f.extend([f'{DefaultIndent}{l}'.rstrip() for l in body])
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

        body = f.obj.toPython()
        body[0] = 'return ' + body[0]
        return body


class ScenaParser:
    def __init__(self, fs: fileio.FileStream):
        self.fs                 = fs                # type: fileio.FileStream
        self.name               = ''                # type: str
        self.header             = None              # type: ScenaHeader
        self.functions          = []                # type: List[ScenaFunction]
        self.strings            = []                # type: List[str]

    def __str__(self) -> str:
        funcs = "\n".join([str(f) for f in self.functions])
        return '\n'.join([
            f'mapName               = {self.header.mapName}',
            f'mapModel              = {self.header.mapModel}',
            f'bgm                   = 0x{self.header.bgm:04X}',
            f'flags                 = 0x{self.header.flags:04X}',
            f'entryFunction         = 0x{self.header.entryFunction:X}',
            f'importTable           = {self.header.importTable}',
            f'reversed              = {self.header.reversed}',
            f'dataTable             = {self.header.dataTable}',
            f'stringTableOffset     = 0x{self.header.stringTableOffset:04X}',
            f'headerSize            = 0x{self.header.headerSize:04X}',
            f'functionTable         = {self.header.functionTable}',
            '',
            f'functions: \n{funcs}',
            '',
            f'{self.strings}'
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

        fs.Position = hdr.stringTableOffset
        data = fs.Read()
        if data[-1] == 0 and data[-2] != 0:
            data = data[:-1]

        self.strings = [s.decode(GlobalConfig.DefaultEncoding) for s in data.split(b'\x00\x00', maxsplit = 1)[0].split(b'\x00')]

        fs.Position = hdr.functionTable.offset

        for i in range(hdr.functionTable.size // 2):
            offset = fs.ReadUShort()
            self.functions.append(ScenaFunction(index = i, offset = offset, name = f'func_{offset:X}', type = ScenaFunctionType.Code))

    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED6ScenaOpTable)
        ctx = Assembler.DisasmContext(fs)

        for func in self.functions:
            fs.Position = func.offset

            if func.index == 0x13: break

            log.debug(f'disasm func: {func}')

            match func.type:
                case ScenaFunctionType.Code:
                    # if func.index == 0x9E: break

                    try:
                        func.obj = dis.disasmFunction(ctx, name = func.name)
                    except KeyError as e:
                        e.args = (f'0x{e.args[0]:X} ({e.args[0]})',)
                        raise

                case _:
                    raise NotImplementedError(f'unknown func type: {func.type}')

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(ED6ScenaOpTable, name = self.name)

        lines = f'''\
import sys
sys.path.append(r'{pathlib.Path(__file__).parent.parent.parent.parent}')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import {pathlib.Path(filename).stem.strip()}_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('{filename}')

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
