from .scena_types import *
from ..InstructionTable import ScenaOpTable as ED83ScenaOpTable

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
    def formatFuncion(self, func: ScenaFunction) -> List[str]:
        funcName = func.name
        if not funcName:
            funcName = f'func_{func.offset:X}'

        f = [
            f'# id: 0x{func.index:04X} offset: 0x{func.offset:X}',
            f'@scena.{func.type}(\'{func.name}\')',
            f'def {funcName}():',
        ]

        formatter = self._formatter.get(func.type)
        if formatter is None:
            raise NotImplementedError(f'unknown func type: {func.type}')

        try:
            body = formatter(self, func)

        except NotImplementedError:
            body = ['pass']

        f.extend([DefaultIndent + l for l in body])
        f.append('')

        return f

    def formatBattleSetting(self, f: ScenaFunction) -> List[str]:
        bs: ScenaBattleSetting = f.obj
        body = bs.toPython()
        body[0] = 'return ' + body[0]
        return body

    def formatCode(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError
        # blk = self.formatBlock(func.func.block)
        # for b in blk:
        #     if b:
        #         b = DefaultIndent + b

        #     f.append(b)

    def formatAnimeClips(self, f: ScenaFunction) -> List[str]:
        acs: ScenaAnimeClips = f.obj
        body = acs.toPython()
        body[0] = 'return ' + body[0]
        return body

    def formatActionTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatWeaponAttTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatBreakTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatAlgoTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatSummonTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatAddCollision(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatPartTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatReactionTable(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatAnimeClipTable(self, f: ScenaFunction) -> List[str]:
        acs: ScenaAnimeClipTable = f.obj
        body = acs.toPython()
        body[0] = 'return ' + body[0]
        return body

    def formatFieldMonsterData(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatFieldFollowData(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatShinigPomBtlset(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    def formatFaceAuto(self, f: ScenaFunction) -> List[str]:
        raise NotImplementedError

    _formatter = {
        ScenaFunctionType.Function          : formatCode,
        ScenaFunctionType.BattleSetting     : formatBattleSetting,
        ScenaFunctionType.AnimeClips        : formatAnimeClips,
        ScenaFunctionType.ActionTable       : formatActionTable,
        ScenaFunctionType.WeaponAttTable    : formatWeaponAttTable,
        ScenaFunctionType.BreakTable        : formatBreakTable,
        ScenaFunctionType.AlgoTable         : formatAlgoTable,
        ScenaFunctionType.SummonTable       : formatSummonTable,
        ScenaFunctionType.AddCollision      : formatAddCollision,
        ScenaFunctionType.PartTable         : formatPartTable,
        ScenaFunctionType.ReactionTable     : formatReactionTable,
        ScenaFunctionType.AnimeClipTable    : formatAnimeClipTable,
        ScenaFunctionType.FieldMonsterData  : formatFieldMonsterData,
        ScenaFunctionType.FieldFollowData   : formatFieldFollowData,
        ScenaFunctionType.ShinigPomBtlset   : formatShinigPomBtlset,
        ScenaFunctionType.FaceAuto          : formatFaceAuto,
    }

class ScenaParser:
    def __init__(self, fs: fileio.FileStream) -> None:
        self.fs                 = fs                # type: fileio.FileStream
        self.name               = ''                # type: str
        self.header             = None              # type: ScenaHeader
        self.functions          = []                # type: List[ScenaFunction]
        self.functionNameMap    = {}                # type: Dict[str, bool]

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

        if name == '' or name.startswith('BTLSET_'):
            return ScenaFunctionType.BattleSetting

        if name.startswith('FC_auto'):
            return ScenaFunctionType.FaceAuto

        if name.startswith('_'):
            if name[1:] not in self.functionNameMap:
                raise Exception(f'unsupported func name: {name}')

            return ScenaFunctionType.AnimeClips

        return ScenaFunctionType.Function

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
                f.type = ScenaFunctionType.Function

            else:
                f.type = self.getFunctionType(f.name)

    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED83ScenaOpTable)
        ctx = Assembler.DisasmContext(fs)

        for func in self.functions:
            fs.Position = func.offset

            log.debug(f'disasm func: {func}')

            match func.type:
                case ScenaFunctionType.Function:
                    # func.func = dis.disasmFunction(ctx, name = func.name)
                    pass

                case ScenaFunctionType.BattleSetting:
                    func.obj = ScenaBattleSetting(fs = fs)

                case ScenaFunctionType.AnimeClips:
                    func.obj = ScenaAnimeClips(fs = fs)

                case ScenaFunctionType.ActionTable:
                    pass

                case ScenaFunctionType.WeaponAttTable:
                    pass

                case ScenaFunctionType.BreakTable:
                    pass

                case ScenaFunctionType.AlgoTable:
                    pass

                case ScenaFunctionType.SummonTable:
                    pass

                case ScenaFunctionType.AddCollision:
                    pass

                case ScenaFunctionType.PartTable:
                    pass

                case ScenaFunctionType.ReactionTable:
                    pass

                case ScenaFunctionType.AnimeClipTable:
                    func.obj = ScenaAnimeClipTable(fs = fs)

                case ScenaFunctionType.FieldMonsterData:
                    pass

                case ScenaFunctionType.FieldFollowData:
                    pass

                case ScenaFunctionType.ShinigPomBtlset:
                    pass

                case ScenaFunctionType.FaceAuto:
                    pass

                case _:
                    raise NotImplementedError(f'unknown func type: {func.type}')

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(ED83ScenaOpTable)

        lines = f'''\
from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_op_gen import *

scena = createScenaWriter('{filename}')

'''.splitlines()

        for func in self.functions:
            lines.extend(formatter.formatFuncion(func))

        main = '''
def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

'''

        lines.extend(main.splitlines())

        # print('\n'.join(lines))

        return lines
