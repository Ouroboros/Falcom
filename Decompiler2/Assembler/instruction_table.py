from Common import *
from . import instruction
from . import handlers

if TYPE_CHECKING:
    from . import disassembler

__all__ = (
    'OperandType',
    'OperandFormat',
    'OperandDescriptor',
    'InstructionDescriptor',
    'InstructionTable',
)

class OperandType(IntEnum2):
    Empty,      \
    SInt8,      \
    SInt16,     \
    SInt32,     \
    SInt64,     \
    UInt8,      \
    UInt16,     \
    UInt32,     \
    UInt64,     \
    SHex8,      \
    SHex16,     \
    SHex32,     \
    SHex64,     \
    UHex8,      \
    UHex16,     \
    UHex32,     \
    UHex64,     \
    Float32,    \
    Float64,    \
    MBCS,       \
    UserDefined = range(21)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class OperandFormat:
    sizeTable = {
        OperandType.SInt8   : 1,
        OperandType.SInt16  : 2,
        OperandType.SInt32  : 4,
        OperandType.SInt64  : 8,

        OperandType.UInt8   : 1,
        OperandType.UInt16  : 2,
        OperandType.UInt32  : 4,
        OperandType.UInt64  : 8,

        OperandType.SHex8   : 1,
        OperandType.SHex16  : 2,
        OperandType.SHex32  : 4,
        OperandType.SHex64  : 8,

        OperandType.UHex8   : 1,
        OperandType.UHex16  : 2,
        OperandType.UHex32  : 4,
        OperandType.UHex64  : 8,

        OperandType.Float32 : 4,
        OperandType.Float64 : 8,

        OperandType.MBCS    : None,
    }

    def __init__(self, oprType: OperandType, hex: bool = False, encoding: str = 'GBK'):
        self.type       = oprType                   # type: OperandType
        self.hex        = hex                       # type: bool
        self.encoding   = encoding                  # type: str

    def __str__(self):
        return repr(self.type)

    def __repr__(self):
        return self.__str__()

    @property
    def size(self):
        return self.sizeTable.get(self.type)

class OperandDescriptor:
    @classmethod
    def fromFormatString(cls, fmtstr: str, formatTable = None) -> 'Tuple[OperandDescriptor]':
        formatTable = formatTable if formatTable else cls.formatTable
        return tuple(formatTable[f] for f in fmtstr)

    def __init__(self, format: OperandFormat, formatHandler: 'handlers.FormatOperandHandler' = None):
        self.format     = format                    # type: OperandFormat
        self.handler    = formatHandler             # type: handlers.FormatOperandHandler

    def readValue(self, info: 'handlers.InstructionHandlerInfo') -> Any:
        fs = info.disasmInfo.fs

        return {
            OperandType.SInt8   : lambda : fs.ReadChar(),
            OperandType.UInt8   : lambda : fs.ReadByte(),

            OperandType.SInt16  : lambda : fs.ReadShort(),
            OperandType.UInt16  : lambda : fs.ReadUShort(),

            OperandType.SInt32  : lambda : fs.ReadLong(),
            OperandType.UInt32  : lambda : fs.ReadULong(),

            OperandType.SInt64  : lambda : fs.ReadLong64(),
            OperandType.UInt64  : lambda : fs.ReadULong64(),

            OperandType.Float32 : lambda : fs.ReadFloat(),
            OperandType.Float64 : lambda : fs.ReadDouble(),

            OperandType.MBCS    : lambda : fs.ReadMultiByte(self.format.encoding),
        }[self.format.type]()

    def formatValue(self, info: 'handlers.FormatOperandHandlerInfo') -> str:
        operand = info.operand
        desc    = operand.descriptor
        fmt     = desc.format

        def formatInteger():
            return (fmt.hex and '0x%X' or '%d') % operand.value

        def formatFloat():
            return '%f' % operand.value

        return {
            OperandType.SInt8   : formatInteger,
            OperandType.UInt8   : formatInteger,

            OperandType.SInt16  : formatInteger,
            OperandType.UInt16  : formatInteger,

            OperandType.SInt32  : formatInteger,
            OperandType.UInt32  : formatInteger,

            OperandType.SInt64  : formatInteger,
            OperandType.UInt64  : formatInteger,

            OperandType.Float32 : formatFloat,
            OperandType.Float64 : formatFloat,

            OperandType.MBCS    : lambda : repr(operand.value),
        }[desc.format.type]()

    def __str__(self):
        return str(self.format)

    def __repr__(self):
        return self.__str__()

def oprdesc(*args, **kwargs):
    return OperandDescriptor(OperandFormat(*args, **kwargs))

OperandDescriptor.formatTable = {
    'c' : oprdesc(OperandType.SInt8, hex = False),
    'C' : oprdesc(OperandType.UInt8, hex = False),
    'b' : oprdesc(OperandType.SInt8, hex = True),
    'B' : oprdesc(OperandType.UInt8, hex = True),

    'h' : oprdesc(OperandType.SInt16, hex = False),
    'H' : oprdesc(OperandType.UInt16, hex = False),
    'w' : oprdesc(OperandType.SInt16, hex = True),
    'W' : oprdesc(OperandType.UInt16, hex = True),

    'i' : oprdesc(OperandType.SInt32, hex = False),
    'I' : oprdesc(OperandType.UInt32, hex = False),
    'l' : oprdesc(OperandType.SInt32, hex = True),
    'L' : oprdesc(OperandType.UInt32, hex = True),

    'q' : oprdesc(OperandType.SInt64, hex = True),
    'Q' : oprdesc(OperandType.UInt64, hex = True),

    'f' : oprdesc(OperandType.Float32),
    'd' : oprdesc(OperandType.Float64),

    'S' : oprdesc(OperandType.MBCS, encoding = DefaultEncoding)
}

class InstructionDescriptor:
    NoOperand = None

    def __init__(
            self,
            opcode:     int,
            mnemonic:   str,
            operands:   List[OperandDescriptor] = NoOperand,
            flags:      'instruction.Flags' = 0,
            handler:    'handlers.InstructionHandler' = None
        ):
        self.opcode     = opcode                    # type: int
        self.mnemonic   = mnemonic                  # type: str
        self.operands   = operands                  # type: List[OperandDescriptor]
        self.flags      = flags                     # type: instruction.Flags
        self.handler    = handler                   # type: handlers.InstructionHandler

    def __str__(self):
        return ' '.join([
            f'{self.opcode:02X} {self.mnemonic}',
            '(%s)' % (', '.join([str(o) for o in self.operands]) if self.operands else ''),
            f'{self.flags}' if self.flags != instruction.Flags.Empty else '',
        ])

class InstructionTable:
    def __init__(self, descriptors: List[InstructionDescriptor]):
        self.descriptors    = descriptors           # type: List[InstructionDescriptor]
        self.descTable      = {}                    # type: Dict[int, InstructionDescriptor]

        for desc in self.descriptors:
            self.descTable[desc.opcode] = desc

    def getDescriptor(self, opcode: int) -> InstructionDescriptor:
        return self.descTable[opcode]

    def readOpCode(self, fs: fileio.FileStream) -> int:
        raise NotImplementedError

    def writeOpCode(self, fs: fileio.FileStream, inst: 'instruction.Instruction'):
        raise NotImplementedError

    def readInstruction(self, fs: fileio.FileStream) -> 'instruction.Instruction':
        raise NotImplementedError

    def writeInstruction(self, fs: fileio.FileStream, inst: 'instruction.Instruction'):
        raise NotImplementedError

    def readOperand(self, info: 'handlers.InstructionHandlerInfo', inst: 'instruction.Instruction', desc: OperandDescriptor) -> 'instruction.Operand':
        operand = instruction.Operand()

        fs = info.disasmInfo.fs

        pos = fs.Position

        operand.size = desc.format.size
        operand.descriptor = desc
        operand.value = desc.readValue(info)

        if operand.size is None:
            operand.size = fs.Position - pos

        return operand

    def writeOperand(self, fs: fileio.FileStream, operand: 'instruction.Operand'):
        raise NotImplementedError

    def formatOperand(self, info: 'handlers.FormatOperandHandlerInfo') -> str:
        result  = None
        operand = info.operand
        desc    = operand.descriptor

        handler = info.operand.descriptor.handler
        if handler is not None:
            result = handler(info)

        if result is None:
            result = desc.formatValue(info)

        return result

    def formatAllOperand(self, inst: 'instruction.Instruction') -> List[str]:
        text = []
        for opr in inst.operands:
            info = handlers.FormatOperandHandlerInfo(inst, opr)
            ret = self.formatOperand(info)

            if isinstance(ret, list):
                text.extend(ret)
            else:
                text.append(ret)

        return text

    def __str__(self):
        return '\n'.join(['%s' % x for x in self.descriptors])
