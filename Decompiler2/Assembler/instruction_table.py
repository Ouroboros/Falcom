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
    sizeTable: Dict[OperandType, int] = {
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

    def __init__(self, oprType: OperandType, hex: bool = False, encoding: str = None):
        encoding = encoding or GlobalConfig.DefaultEncoding

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
    formatTable: Dict[str, 'OperandDescriptor'] = {}

    @classmethod
    def fromFormatString(cls, fmtstr: str, formatTable = None) -> 'Tuple[OperandDescriptor]':
        formatTable = formatTable if formatTable else cls.formatTable
        return tuple(formatTable[f] for f in fmtstr)

    def __init__(self, format: OperandFormat, formatHandler: 'handlers.FormatOperandHandler' = None):
        self.format         = format                    # type: OperandFormat
        self.formatHandler  = formatHandler             # type: handlers.FormatOperandHandler

    @property
    def type(self) -> OperandType:
        return self.format.type

    def readValue(self, context: 'handlers.InstructionHandlerContext') -> Any:
        fs = context.disasmContext.fs

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

    def writeValue(self, context: 'handlers.InstructionHandlerContext', value: Any):
        fs = context.disasmContext.fs

        return {
            OperandType.SInt8   : lambda : fs.WriteChar(value),
            OperandType.UInt8   : lambda : fs.WriteByte(value),

            OperandType.SInt16  : lambda : fs.WriteShort(value),
            OperandType.UInt16  : lambda : fs.WriteUShort(value),

            OperandType.SInt32  : lambda : fs.WriteLong(value),
            OperandType.UInt32  : lambda : fs.WriteULong(value),

            OperandType.SInt64  : lambda : fs.WriteLong64(value),
            OperandType.UInt64  : lambda : fs.WriteULong64(value),

            OperandType.Float32 : lambda : fs.WriteFloat(value),
            OperandType.Float64 : lambda : fs.WriteDouble(value),

            OperandType.MBCS    : lambda : fs.Write(value.encode(self.format.encoding) + b'\x00'),
        }[self.format.type]()

    def formatValue(self, context: 'handlers.FormatOperandHandlerContext') -> str:
        operand = context.operand
        desc    = operand.descriptor
        fmt     = desc.format

        def formatInteger():
            if fmt.hex:
                f = f'0x%0{fmt.size * 2}X'
                return f % operand.value

            return '%d' % operand.value
            # return (fmt.hex and '0x%X' or '%d') % operand.value

        def formatFloat():
            return '%f' % round(operand.value, 7)

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

            OperandType.MBCS    : lambda : f"'{operand.value}'",
        }[desc.format.type]()

    def __str__(self):
        return str(self.format)

    def __repr__(self):
        return self.__str__()

def oprdesc(*args, **kwargs) -> OperandDescriptor:
    return OperandDescriptor(OperandFormat(*args, **kwargs))

OperandDescriptor.formatTable.update({
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

    'S' : oprdesc(OperandType.MBCS)
})

class InstructionDescriptor:
    NoOperand = None

    def __init__(
            self,
            opcode:     int,
            mnemonic:   str,
            operands:   List[OperandDescriptor] = NoOperand,
            flags:      'instruction.Flags' = 0,
            handler:    'handlers.InstructionHandler' = None,
            parameters: List[str] = None,
        ):
        self.opcode     = opcode                    # type: int
        self.mnemonic   = mnemonic                  # type: str
        self.operands   = operands                  # type: List[OperandDescriptor]
        self.flags      = flags                     # type: instruction.Flags
        self.handler    = handler                   # type: handlers.InstructionHandler
        self.parameters = parameters                # type: List[str]

    def __str__(self):
        return ' '.join([
            f'{self.opcode:02X} {self.mnemonic}',
            '(%s)' % (', '.join([(str(o) + (f' {self.parameters[i]}' if self.parameters else '')) for i, o in enumerate(self.operands)]) if self.operands else ''),
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

    def writeOpCode(self, fs: fileio.FileStream, opcode: int):
        raise NotImplementedError

    def readInstruction(self, fs: fileio.FileStream) -> 'instruction.Instruction':
        raise NotImplementedError

    def writeInstruction(self, fs: fileio.FileStream, inst: 'instruction.Instruction'):
        raise NotImplementedError

    def readAllOperands(self, context: 'handlers.InstructionHandlerContext', descriptors: List[OperandDescriptor]) -> 'List[instruction.Operand]':
        return [self.readOperand(context, desc) for desc in descriptors]

    def readOperand(self, context: 'handlers.InstructionHandlerContext', desc: OperandDescriptor) -> 'instruction.Operand':
        operand = instruction.Operand()

        fs = context.disasmContext.fs

        pos = fs.Position

        operand.size = desc.format.size
        operand.descriptor = desc
        operand.value = desc.readValue(context)

        if operand.size is None:
            operand.size = fs.Position - pos

        return operand

    def writeOperand(self, context: 'handlers.InstructionHandlerContext', operand: 'instruction.Operand'):
        desc = operand.descriptor
        desc.writeValue(context, operand.value)

    def writeAllOperands(self, context: 'handlers.InstructionHandlerContext', operands: 'List[instruction.Operand]'):
        for opr in operands:
            self.writeOperand(context, opr)

    def formatOperand(self, context: 'handlers.FormatOperandHandlerContext') -> str | List[str]:
        result  = None
        operand = context.operand
        desc    = operand.descriptor

        handler = context.operand.descriptor.formatHandler
        if handler is not None:
            result = handler(context)

        if result is None:
            result = desc.formatValue(context)

        return result

    def formatAllOperands(self, context: 'handlers.FormatOperandHandlerContext', operands: 'List[instruction.Operand]') -> List[str]:
        text = []
        for opr in operands:
            context = handlers.FormatOperandHandlerContext(context.instruction, opr, formatter = context.formatter)
            ret = self.formatOperand(context)

            if isinstance(ret, list | tuple):
                # text.extend(ret)
                text.append(ret)
            else:
                text.append(ret)

        return text

    def __str__(self):
        return '\n'.join(['%s' % x for x in self.descriptors])
