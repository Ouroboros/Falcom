from Falcom.ED6.Parser.scena import ScenaParser as ED6ScenaParser, ScenaFormatter
from ..InstructionTable.utils import formatText
from ..InstructionTable import ScenaOpTable as ED62ScenaOpTable
from .scena_types import *
import pathlib

class ScenaParser(ED6ScenaParser):
    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED62ScenaOpTable)
        ctx = Assembler.DisasmContext(fs, instCallback = self.instructionCb, scriptName = self.name)

        for func in self.functions:
            # log.debug(f'disasm func: {func}')

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
        formatter = ScenaFormatter(self, ED62ScenaOpTable, name = self.name)

        lines = f'''\
import sys
sys.path.append(r'{pathlib.Path(__file__).parent.parent.parent.parent}')

from Falcom.ED62.Parser.scena_writer_helper import *
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
