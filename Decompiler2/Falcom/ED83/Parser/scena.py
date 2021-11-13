from Falcom.Common import *
from ..InstructionTable import ScenaOpTable as ED83ScenaOpTable

__all__ = (
    'ScenaHeader',
    'ScenaFunctionType',
    'ScenaFunction',
    'SceneParser',
    'ScenaFormatter',
)

DefaultEndian = GlobalConfig.DefaultEndian
DefaultIndent = GlobalConfig.DefaultIndent
DefaultEncoding = GlobalConfig.DefaultEncoding

class ScenaHeader:
    MAGIC = 0xABCDEF00
    def __init__(self, fs: fileio.FileStream = None) -> None:
        self.headerSize             = None      # type: int
        self.nameOffset             = None      # type: int
        self.functionEntryOffset    = None      # type: int
        self.functionEntrySize      = None      # type: int
        self.functionNameOffset     = None      # type: int
        self.functionCount          = None      # type: int
        self.fullHeaderSize         = None      # type: int
        self.magic                  = None      # type: int

        if fs:
            self.headerSize          = fs.ReadULong()
            self.nameOffset          = fs.ReadULong()
            self.functionEntryOffset = fs.ReadULong()
            self.functionEntrySize   = fs.ReadULong()
            self.functionNameOffset  = fs.ReadULong()
            self.functionCount       = fs.ReadULong()
            self.fullHeaderSize      = fs.ReadULong()
            self.magic               = fs.ReadULong()

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(int.to_bytes(self.headerSize,          4, DefaultEndian))
        fs.write(int.to_bytes(self.nameOffset,          4, DefaultEndian))
        fs.write(int.to_bytes(self.functionEntryOffset, 4, DefaultEndian))
        fs.write(int.to_bytes(self.functionEntrySize,   4, DefaultEndian))
        fs.write(int.to_bytes(self.functionNameOffset,  4, DefaultEndian))
        fs.write(int.to_bytes(self.functionCount,       4, DefaultEndian))
        fs.write(int.to_bytes(self.fullHeaderSize,      4, DefaultEndian))
        fs.write(int.to_bytes(self.magic,               4, DefaultEndian))

        fs.seek(0)

        return fs.read()

class ScenaFunctionType(IntEnum2):
    Invalid             = 0
    Function            = 1
    BattleSetting       = 3
    Effect              = 4

    ActionTable         = 5
    WeaponAttTable      = 6
    BreakTable          = 7
    AlgoTable           = 8
    SummonTable         = 9
    AddCollision        = 10
    PartTable           = 11
    ReactionTable       = 12
    AnimeClipTable      = 13
    FieldMonsterData    = 14
    FieldFollowData     = 15
    ShinigPomBtlset     = 16
    FaceAuto            = 17

class ScenaFunction:
    def __init__(self, index: int, offset: int, name: str) -> None:
        self.index  = index
        self.offset = offset
        self.name   = name
        self.func   = None                  # type: Assembler.Function
        self.type   = ScenaFunctionType.Invalid

    def __str__(self) -> str:
        return f'0x{self.index:04X} 0x{self.offset:08X} {repr(self.name)} {self.type}'

class SceneParser:
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
        'AnimeClipTable'    : ScenaFunctionType.AnimeClipTable,
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

            return ScenaFunctionType.Effect

        return ScenaFunctionType.Function

    def parse(self):
        self.readHeader()
        self.disasmFunctions()

    def readHeader(self):
        fs = self.fs
        fs.Position = 0

        self.header = ScenaHeader(fs)

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

        for f in self.functions:
            f.type = self.getFunctionType(f.name)
            print(f)

    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED83ScenaOpTable)
        ctx = Assembler.DisasmContext(fs)

        for func in self.functions:
            fs.Position = func.offset
            # func.func = dis.disasmFunction(ctx, name = func.name)
            # print()

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(ED83ScenaOpTable)

        lines = f'''
from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_op_gen import *

scena = createScenaWriter('{filename}')

'''.splitlines()[1:]

        for func in self.functions:
            # if not func.func:
            #     continue

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

class ScenaFormatter(Assembler.Formatter):
    def formatFuncion(self, func: ScenaFunction) -> List[str]:
        funcName = func.name
        if not funcName:
            funcName = f'func_{func.offset:X}'

        f = [
            f'@scena.{func.type}(\'{func.name}\')',
            f'def {funcName}():',
            '    pass',
            '',
        ]

        return f

        blk = self.formatBlock(func.func.block)
        for b in blk:
            if b:
                b = DefaultIndent + b

            f.append(b)

        return f
