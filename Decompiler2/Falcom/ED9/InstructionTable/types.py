from Falcom.Common import *
from Assembler     import *
from .utils        import *

class ED9OperandValueType(IntEnum2):
    Undefined       = 0
    Integer         = 1
    Float           = 2
    String          = 3

class ED9OperandType(IntEnum2):
    Offset,         \
    Item,           \
    CraftId,        \
    BGM,            \
    Text,           \
    ScenaFlags,     \
    FunctionID,     \
    ChrId,          \
    Value,          \
    UserDefined = range(OperandType.UserDefined, OperandType.UserDefined + 10)

    __str__     = OperandType.__str__
    __repr__    = OperandType.__repr__

class ED9OperandFormat(OperandFormat):
    sizeTable = {
        **OperandFormat.sizeTable,

        ED9OperandType.Value        : 4,
        ED9OperandType.Offset       : 4,
        ED9OperandType.Item         : 2,
        ED9OperandType.CraftId      : 2,
        ED9OperandType.BGM          : 2,
        ED9OperandType.ScenaFlags   : 2,
        ED9OperandType.ChrId        : 2,
        ED9OperandType.FunctionID   : 2,
        ED9OperandType.Text         : None,
    }

class ED9OperandDescriptor(OperandDescriptor):
    formatTable: Dict[str, 'ED9OperandDescriptor'] = {}

    def readValue(self, context: InstructionHandlerContext) -> Any:
        return {
            ED9OperandType.ScenaFlags   : lambda context: context.disasmContext.fs.ReadUShort(),
            ED9OperandType.Offset       : lambda context: context.disasmContext.fs.ReadULong(),
            ED9OperandType.ChrId        : lambda context: context.disasmContext.fs.ReadUShort(),
            ED9OperandType.Item         : lambda context: context.disasmContext.fs.ReadUShort(),
            ED9OperandType.CraftId      : lambda context: context.disasmContext.fs.ReadUShort(),
            ED9OperandType.FunctionID   : lambda context: context.disasmContext.fs.ReadUShort(),
            ED9OperandType.Value        : self.readScenaValue,

        }.get(self.format.type, super().readValue)(context)

    def writeValue(self, context: InstructionHandlerContext, value: Any):
        return {
            ED9OperandType.ScenaFlags   : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED9OperandType.Offset       : lambda context, value: context.disasmContext.fs.WriteULong(0xFFFFABCD),
            ED9OperandType.ChrId        : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED9OperandType.FunctionID   : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED9OperandType.Item         : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED9OperandType.CraftId      : lambda context, value: context.disasmContext.fs.WriteUShort(value),
        }.get(self.format.type, super().writeValue)(context, value)

    def formatValue(self, context: FormatOperandHandlerContext) -> str:
        return {
            ED9OperandType.ScenaFlags   : lambda context: self.formatScenaFlags(context.operand.value),
            ED9OperandType.Offset       : lambda context: "'%s'" % context.operand.value.name,    # CodeBlock
            ED9OperandType.ChrId        : lambda context: self.formatChrId(context.operand.value),
            ED9OperandType.FunctionID   : lambda context: context.formatter.parser.getCodeFuncName(context.operand.value),
            ED9OperandType.Item         : lambda context: self.formatItemId(context.operand.value),
            ED9OperandType.CraftId      : lambda context: self.formatCraftId(context.operand.value),
            ED9OperandType.Value        : self.formatScenaValue,

        }.get(self.format.type, super().formatValue)(context)

    def readScenaValue(self, context: InstructionHandlerContext):
        from ..Parser.scena_types import ScenaValue
        fs = context.disasmContext.fs
        return ScenaValue(fs = fs)

    def formatScenaValue(self, context: FormatOperandHandlerContext):
        from ..Parser.scena_types import ScenaValue

        v: ScenaValue = context.operand.value
        match v.type:
            case ScenaValue.Type.Undefined:
                fmt = 'L'

            case ScenaValue.Type.Integer:
                if v.value in [0xFFFE, 0xFFE6, 0xFFFD]:
                    fmt = 'W'
                else:
                    fmt = 'i'

            case ScenaValue.Type.Float:
                fmt = 'f'

            case ScenaValue.Type.String:
                fmt = 'S'

        context.operand.value = v.value
        applyDescriptorsToOperands([context.operand], fmt)

        return super().formatValue(context)

    def formatScenaFlags(self, flags: int) -> str:
        # return '0x%X' % flags
        flags &= 0XFFFF
        return f'ScenaFlag(0x{flags >> 3:04X}, {flags & 7}, 0x{flags:X})'

    def formatChrId(self, chrId: int) -> str:
        try:
            name = GlobalConfig.ChrTable[chrId]
            return f"ChrTable['{name}']"
        except KeyError:
            from ..Parser.consts import PseudoChrId
            if chrId in PseudoChrId._value2member_map_:
                return f'PseudoChrId.{PseudoChrId(chrId)}'

            return f'0x{chrId:04X}'

    def formatItemId(self, itemId: int) -> str:
        try:
            name = GlobalConfig.ItemTable[itemId]
            return f"ItemTable['{name}']"
        except KeyError:
            return f'0x{itemId:04X}'

    def formatCraftId(self, craftId: int) -> str:
        try:
            name = GlobalConfig.CraftTable[craftId]
            return f"CraftTable['{name}']"
        except KeyError:
            return f'0x{craftId:04X}'

def oprdesc(*args, **kwargs) -> ED9OperandDescriptor:
    return ED9OperandDescriptor(ED9OperandFormat(*args, **kwargs))

ED9OperandDescriptor.formatTable.update({
    **OperandDescriptor.formatTable,

    'O' : oprdesc(ED9OperandType.Offset),
    'F' : oprdesc(ED9OperandType.FunctionID),
    'V' : oprdesc(ED9OperandType.Value),
    # 't' : oprdesc(ED9OperandType.Item),
    # 'R' : oprdesc(ED9OperandType.CraftId),
    # 'N' : oprdesc(ED9OperandType.ChrId),
})

def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED9OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)