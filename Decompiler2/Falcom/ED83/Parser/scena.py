from Assembler.function import Function
from Assembler.instruction import Instruction
from .scena_types import *
from ..InstructionTable import ScenaOpTable as ED83ScenaOpTable
from ..InstructionTable.scena_optimizer import ED83Optimizer
import pathlib

__all__ = (
    'ScenaParser',
    'ScenaHeader',
    'ScenaFunctionType',
    'ScenaFunction',
    'ScenaBattleMonsterSet',
    'ScenaBattleSetting',
    'ScenaAnimeClips',
    'ScenaAnimeClipTableEntry',
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
            if func.type == ScenaFunctionType.BattleSetting:
                funcName = f'{func.type}{func.index:02X}'
            else:
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
        self.functionNameMap    = {}                # type: Dict[str, bool]
        self.instructionCb      = None              # type: Callable[[Instruction], None]

    def __str__(self) -> str:
        funcs = '\n'.join([str(f) for f in self.functions])
        return '\n'.join([
            f'headerSize            = 0x{self.header.headerSize:04X}',
            f'nameOffset            = 0x{self.header.nameOffset:04X}',
            f'functionEntryOffset   = 0x{self.header.functionEntryOffset:04X}',
            f'functionEntrySize     = 0x{self.header.functionEntrySize:04X}',
            f'functionNameOffset    = 0x{self.header.functionNameOffset:04X}',
            f'functionCount         = 0x{self.header.functionCount:04X}',
            f'fullHeaderSize        = 0x{self.header.fullHeaderSize:04X}',
            f'magic                 = 0x{self.header.magic:04X}',
            '',
            f'{funcs}',
        ])

    functionTypeMap = {
        'ActionTable'       : ScenaFunctionType.ActionTable,
        'WeaponAttTable'    : ScenaFunctionType.WeaponAttTable,
        'BreakTable'        : ScenaFunctionType.BreakTable,
        'AlgoTable'         : ScenaFunctionType.AlgoTable,
        'SummonTable'       : ScenaFunctionType.SummonTable,
        'AddCollision'      : ScenaFunctionType.AddCollision,
        'PartTable'         : ScenaFunctionType.PartTable,
        'ReactionTable'     : ScenaFunctionType.ReactionTable,
        'AnimeClipTable'    : ScenaFunctionType.AnimeClipTable,
        'FieldMonsterData'  : ScenaFunctionType.FieldMonsterData,
        'FieldFollowData'   : ScenaFunctionType.FieldFollowData,
        'ShinigPomBtlset'   : ScenaFunctionType.ShinigPomBtlset,
    }

    def getFunctionType(self, name: str) -> ScenaFunctionType:
        typ = self.functionTypeMap.get(name)
        if typ:
            return typ

        if any([
                name == '',
                name.startswith('BTLSET'),
            ]):
            return ScenaFunctionType.BattleSetting

        if name.startswith('FC_auto'):
            return ScenaFunctionType.FaceAuto

        if name.startswith('_'):
            if name[1:] not in self.functionNameMap:
                raise Exception(f'unsupported func name: {name}')

            return ScenaFunctionType.AnimeClips

        return ScenaFunctionType.Code

    def parse(self):
        self.readHeader()
        self.disasmFunctions()

    def readHeader(self):
        fs = self.fs
        fs.Position = 0

        self.header = ScenaHeader(fs = fs)

        hdr = self.header

        fs.Position = hdr.nameOffset
        self.name = fs.ReadMultiByte(DefaultEncoding)

        fs.Position = hdr.functionEntryOffset
        for i in range(hdr.functionCount):
            self.functions.append(ScenaFunction(index = i, offset = fs.ReadULong(), name = ''))

        fs.Position = hdr.functionNameOffset
        nameOffsets = [fs.ReadUShort() for _ in range(hdr.functionCount)]

        for i, offset in enumerate(nameOffsets):
            fs.Position = offset
            name = fs.ReadMultiByte(DefaultEncoding)
            self.functions[i].name = name
            self.functionNameMap[name] = True

        for i, f in enumerate(self.functions):
            if i == 0 and not f.name:
                f.type = ScenaFunctionType.Code

            else:
                f.type = self.getFunctionType(f.name)

    def setInstructionCallback(self, cb: Callable[[Instruction], None]):
        self.instructionCb = cb

    def disasmFunctions(self):
        def cb(inst: Instruction):
            if inst.opcode == 0x02:
                self.functionNameMap[inst.operands[1].value] = True

        fs = self.fs
        dis = Assembler.Disassembler(ED83ScenaOpTable)
        ctx = Assembler.DisasmContext(fs, instCallback = self.instructionCb, scriptName = self.name)

        for func in self.functions:
            fs.Position = func.offset

            log.debug(f'disasm func: {func}')

            match func.type:
                case ScenaFunctionType.Code:
                    # if func.index == 0x9E: break

                    try:
                        func.obj = dis.disasmFunction(ctx, name = func.name)
                    except KeyError as e:
                        e.args = (f'0x{e.args[0]:X} ({e.args[0]})',)
                        raise

                case ScenaFunctionType.BattleSetting:
                    func.obj = ScenaBattleSetting(fs = fs)

                case ScenaFunctionType.AnimeClips:
                    func.obj = ScenaAnimeClips(fs = fs)

                case ScenaFunctionType.ActionTable:
                    func.obj = ScenaActionTable(fs = fs)

                case ScenaFunctionType.WeaponAttTable:
                    func.obj = ScenaWeaponAttTable(fs = fs)

                case ScenaFunctionType.BreakTable:
                    func.obj = ScenaBreakTable(fs = fs)

                case ScenaFunctionType.AlgoTable:
                    func.obj = ScenaAlgoTable(fs = fs)

                case ScenaFunctionType.SummonTable:
                    func.obj = ScenaSummonTable(fs = fs)

                case ScenaFunctionType.AddCollision:
                    raise NotImplementedError

                case ScenaFunctionType.PartTable:
                    func.obj = ScenaPartTable(fs = fs)

                case ScenaFunctionType.ReactionTable:
                    func.obj = ScenaReactionTable(fs = fs)

                case ScenaFunctionType.AnimeClipTable:
                    func.obj = ScenaAnimeClipTable(fs = fs)

                case ScenaFunctionType.FieldMonsterData:
                    func.obj = ScenaFieldMonsterData(fs = fs)

                case ScenaFunctionType.FieldFollowData:
                    func.obj = ScenaFieldFollowData(fs = fs)

                case ScenaFunctionType.FaceAuto:
                    func.obj = ScenaFaceAuto(fs = fs)

                case ScenaFunctionType.ShinigPomBtlset:
                    raise NotImplementedError

                case _:
                    raise NotImplementedError(f'unknown func type: {func.type}')

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(ED83ScenaOpTable, name = self.name, optimizer = ED83Optimizer())

        lines = f'''\
import sys
sys.path.append(r'{pathlib.Path(__file__).parent.parent.parent.parent}')

from Falcom.ED83.Parser.scena_writer_helper import *
try:
    import {pathlib.Path(filename).stem}_hook
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
