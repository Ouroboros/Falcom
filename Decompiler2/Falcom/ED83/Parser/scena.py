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
    def __init__(self) -> None:
        self.headerSize             = None      # type: int
        self.nameOffset             = None      # type: int
        self.functionEntryOffset    = None      # type: int
        self.functionEntrySize      = None      # type: int
        self.functionNameOffset     = None      # type: int
        self.functionCount          = None      # type: int
        self.fullHeaderSize         = None      # type: int
        self.magic                  = None      # type: int

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
    Invalid         = 1
    Function        = 1
    AnimeClipTable  = 2

class ScenaFunction:
    def __init__(self, offset: int, name: str) -> None:
        self.offset = offset
        self.name   = name
        self.func   = None                  # type: Assembler.Function
        self.type   = ScenaFunctionType.Invalid

    def __str__(self) -> str:
        return f'0x{self.offset:08X} {repr(self.name)}'

class SceneParser:
    def __init__(self, fs: fileio.FileStream) -> None:
        self.fs         = fs                # type: fileio.FileStream
        self.name       = ''                # type: str
        self.header     = ScenaHeader()     # type: ScenaHeader
        self.functions  = []                # type: List[ScenaFunction]

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

    def getFunctionTypeByName(self, name) -> ScenaFunctionType:
        match name:
            case 'AnimeClipTable':
                return ScenaFunctionType.AnimeClipTable

            case _:
                return ScenaFunctionType.Function

    def readHeader(self):
        fs = self.fs
        hdr = self.header

        fs.Position = 0

        hdr.headerSize          = fs.ReadULong()
        hdr.nameOffset          = fs.ReadULong()
        hdr.functionEntryOffset = fs.ReadULong()
        hdr.functionEntrySize   = fs.ReadULong()
        hdr.functionNameOffset  = fs.ReadULong()
        hdr.functionCount       = fs.ReadULong()
        hdr.fullHeaderSize      = fs.ReadULong()
        hdr.magic               = fs.ReadULong()

        fs.Position = hdr.nameOffset
        self.name = fs.ReadMultiByte(DefaultEncoding)

        fs.Position = hdr.functionEntryOffset
        for _ in range(hdr.functionCount):
            self.functions.append(ScenaFunction(offset = fs.ReadULong(), name = ''))

        fs.Position = hdr.functionNameOffset
        nameOffsets = [fs.ReadUShort() for _ in range(hdr.functionCount)]

        for i, offset in enumerate(nameOffsets):
            fs.Position = offset
            self.functions[i].name = fs.ReadMultiByte(DefaultEncoding)
            self.functions[i].type = self.getFunctionTypeByName(self.functions[i].name)

    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED83ScenaOpTable)
        ctx = Assembler.DisasmContext(fs)

        for func in self.functions:
            fs.Position = func.offset
            func.func = dis.disasmFunction(ctx, name = func.name)
            print()

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(ED83ScenaOpTable)

        lines = f'''
from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_op_gen import *

scena = createScenaWriter('{filename}')

'''.splitlines()[1:]

        for func in self.functions:
            if not func.func:
                continue

            lines.extend(formatter.formatFuncion(func))

        main = '''
def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

'''

        lines.extend(main.splitlines())

        print('\n'.join(lines))

        return lines

class ScenaFormatter(Assembler.Formatter):
    def formatFuncion(self, func: ScenaFunction) -> List[str]:
        funcName = func.name
        if not funcName:
            funcName = f'func_{func.offset:X}'

        f = [
            f'@scena.{func.type}(\'{func.name}\')',
            f'def {funcName}():',
        ]

        blk = self.formatBlock(func.func.block)
        for b in blk:
            if b:
                b = DefaultIndent + b

            f.append(b)

        return f
