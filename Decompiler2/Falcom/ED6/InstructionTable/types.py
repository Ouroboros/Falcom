from Falcom.Common import *
from Assembler     import *
from .utils        import *

DefaultIndent = GlobalConfig.DefaultIndent
UserDefined = OperandType.UserDefined + 1

class ED6OperandType(IntEnum2):
    Offset,         \
    Expression,     \
    Text,           \
    Item,           \
    ChrId,          \
    ChrId1,         \
    BGM,            \
    ScenaFlags,     \
    CraftId,        \
    DATFile,        \
    Function,       \
    UserDefined = range(UserDefined, UserDefined + 12)

    __str__     = OperandType.__str__
    __repr__    = OperandType.__repr__

class ED6OperandFormat(OperandFormat):
    sizeTable = {
        **OperandFormat.sizeTable,

        ED6OperandType.Offset      : 2,
        ED6OperandType.Item        : 2,
        ED6OperandType.CraftId     : 2,
        ED6OperandType.BGM         : 2,
        ED6OperandType.ScenaFlags  : 2,
        ED6OperandType.ChrId1      : 1,
        ED6OperandType.ChrId       : 2,
        ED6OperandType.DATFile     : 4,
        ED6OperandType.Function    : 2,
        ED6OperandType.Expression  : None,
        ED6OperandType.Text        : None,
    }

class ED6OperandDescriptor(OperandDescriptor):
    formatTable: Dict[str, 'ED6OperandDescriptor'] = {}

    def readValue(self, context: InstructionHandlerContext) -> Any:
        from ..Parser.scena_types import DATFileIndex

        return {
            ED6OperandType.Text            : self.readText,
            ED6OperandType.Expression      : self.readExpression,
            ED6OperandType.ScenaFlags      : lambda context: context.disasmContext.fs.ReadUShort(),
            ED6OperandType.Offset          : lambda context: context.disasmContext.fs.ReadUShort(),
            ED6OperandType.ChrId1          : lambda context: context.disasmContext.fs.ReadByte(),
            ED6OperandType.ChrId           : lambda context: context.disasmContext.fs.ReadUShort(),
            ED6OperandType.Item            : lambda context: context.disasmContext.fs.ReadUShort(),
            ED6OperandType.CraftId         : lambda context: context.disasmContext.fs.ReadUShort(),
            ED6OperandType.DATFile         : lambda context: DATFileIndex(context.disasmContext.fs.ReadULong()),
            ED6OperandType.Function        : lambda context: context.disasmContext.fs.ReadUShort(),
            # ED6OperandType.BGM        : lambda context: context.disasmContext.fs.ReadShort(),

        }.get(self.format.type, super().readValue)(context)

    def writeValue(self, context: InstructionHandlerContext, value: Any):
        from ..Parser.scena_types import DATFileIndex

        return {
            ED6OperandType.Text        : self.writeText,
            ED6OperandType.Expression  : self.writeExpression,
            ED6OperandType.ScenaFlags  : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED6OperandType.Offset      : lambda context, value: context.disasmContext.fs.WriteUShort(0xF00D),
            ED6OperandType.ChrId1      : lambda context, value: context.disasmContext.fs.WriteByte(value),
            ED6OperandType.ChrId       : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED6OperandType.Item        : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED6OperandType.CraftId     : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED6OperandType.DATFile     : lambda context, value: context.disasmContext.fs.WriteULong(DATFileIndex(value).value),
            ED6OperandType.Function    : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            # ED6OperandType.ThreadValue : self.writeThreadValue,
        }.get(self.format.type, super().writeValue)(context, value)

    def formatValue(self, context: FormatOperandHandlerContext) -> str:
        return {
            ED6OperandType.Text        : self.formatText,
            ED6OperandType.Expression  : self.formatExpression,
            ED6OperandType.ScenaFlags  : lambda context: self.formatScenaFlags(context.operand.value),
            ED6OperandType.Offset      : lambda context: "'%s'" % context.operand.value.name,    # CodeBlock
            ED6OperandType.ChrId1      : lambda context: self.formatChrId(context.operand.value),
            ED6OperandType.ChrId       : lambda context: self.formatChrId(context.operand.value),
            ED6OperandType.Item        : lambda context: self.formatItemId(context.operand.value),
            ED6OperandType.CraftId     : lambda context: self.formatCraftId(context.operand.value),
            ED6OperandType.DATFile     : lambda context: context.operand.value.nameOrValue,
            ED6OperandType.Function    : lambda context: context.formatter.parser.getCodeFuncName(context.instruction),
            # ED6OperandType.BGM         : ,

        }.get(self.format.type, super().formatValue)(context)

    def readText(self, context: InstructionHandlerContext) -> 'List[TextObject]':
        return readTextObjects(context.disasmContext.fs, self.format.encoding)

    def readExpression(self, context: InstructionHandlerContext) -> 'List[ScenaExpression]':
        return ScenaExpression.readExpressions(context)

    def writeExpression(self, context: InstructionHandlerContext, value: 'List[ScenaExpression]'):
        ScenaExpression.writeExpressions(context, [ScenaExpression(v[0], *v[1:]) if isinstance(v, tuple | list) else ScenaExpression(v) for v in value])

    def writeText(self, context: InstructionHandlerContext, text: str):
        fs = context.disasmContext.fs

        if isinstance(text, str):
            return fs.Write(text.encode(self.format.encoding) + b'\x00')

        for v in text:
            if isinstance(v, int):
                fs.WriteByte(v)

            elif isinstance(v, str):
                fs.Write(v.replace('\n', '\x01').encode(self.format.encoding))

            else:
                code, value = v

                fs.WriteByte(code)
                match code:
                    case TextCtrlCode.SetColor:
                        fs.WriteByte(value)

                    case TextCtrlCode.Item:
                        fs.WriteUShort(value)

                    case _:
                        ibp()
                        raise NotImplementedError

        fs.WriteByte(0)

    def formatText(self, context: FormatOperandHandlerContext) -> str:
        context.instruction.flags |= Flags.FormatMultiLine

        value = context.operand.value
        if isinstance(value, str):
            return formatText(context.operand.value)

        value: List['TextObject']
        t: list[str] = []
        textIndexes = []
        for v in value:
            if v.code is None:
                textIndexes.append(len(t))
                t.append(formatText(v.value))
                continue

            code = v.code
            if code in TextCtrlCode._value2member_map_:
                code = f'TxtCtl.{TextCtrlCode(code)}'
            else:
                code = f'0x{code:X}'

            match v.code:
                case TextCtrlCode.Item:
                    itemId = v.value
                    try:
                        itemName = GlobalConfig.ItemTable[itemId]
                        t.append(f"({code}, ItemTable['{itemName}'])")
                        continue

                    except KeyError:
                        pass

            if v.value is not None:
                t.append(f'({code}, 0x{v.value:X})')
            elif v.code != TextCtrlCode.NewLine:
                t.append(f'{code}')

        if context.instruction.flags.textIndex:
            for index in textIndexes:
                t[index] = f'TXT(0x{index:02X}, {t[index]})'

        return t

    def formatExpression(self, context: FormatOperandHandlerContext) -> List[str]:
        context.instruction.flags |= Flags.FormatMultiLine

        expr: List[ScenaExpression] = context.operand.value
        text = []

        for e in expr:
            if isinstance(e.operator, IntEnum2):
                opr = f"Expr.{e.operator}"
            else:
                raise NotImplementedError
                # opr = '0x%02X' % e.operator

            match e.operator:
                case ScenaExpression.Operator.TestScenaFlags:
                    t = f"({opr}, {self.formatScenaFlags(e.operand)})"

                case ScenaExpression.Operator.Eval:
                    s = context.formatter.formatInstruction(e.operand, flags = e.operand.flags)
                    t = f"({opr}, \"{'; '.join(s)}\")"

                case _:
                    if e.operand is not None:
                        t = f"({opr}, {e.formatOperand()})"

                    else:
                        t = opr

            text.append(t)

        return text

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

def oprdesc(*args, **kwargs) -> ED6OperandDescriptor:
    return ED6OperandDescriptor(ED6OperandFormat(*args, **kwargs))

ED6OperandDescriptor.formatTable.update({
    **OperandDescriptor.formatTable,

    'O' : oprdesc(ED6OperandType.Offset),
    'F' : oprdesc(ED6OperandType.ScenaFlags),
    'E' : oprdesc(ED6OperandType.Expression),
    'T' : oprdesc(ED6OperandType.Text),
    't' : oprdesc(ED6OperandType.Item),
    'R' : oprdesc(ED6OperandType.CraftId),
    'n' : oprdesc(ED6OperandType.ChrId1),
    'N' : oprdesc(ED6OperandType.ChrId),
    'D' : oprdesc(ED6OperandType.DATFile),
    'm' : oprdesc(ED6OperandType.Function),
})

class TextCtrlCode(IntEnum2):
    Null            = 0x00
    NewLine         = 0x01
    Enter           = 0x02
    Clear           = 0x03
    # Clear2          = 0x04
    ShowAll         = 0x06
    SetColor        = 0x07
    NewLine2        = 0x0A
    Craft           = 0x19
    Item            = 0x1F

class TextObject:
    def __init__(self, code: int = None, value: Any = None):
        self.code   = code              # type: int
        self.value  = value             # type: Any

    def __eq__(self, o: 'TextObject') -> bool:
        return o.code == self.code and o.value == self.value

    def __str__(self):
        if self.code is None:
            return "'%s'" % self.value

        if self.value is not None:
            return 'code = %s, value = %s' % (self.code, self.value)

        return 'code = %s' % self.code

    def __repr__(self):
        return self.__str__()

class ScenaExpression:
    class Operator(IntEnum2):
        # stack = DWORD[0x67]
        PushLong            = 0x00      # push LONG
        Return              = 0x01      # return [0]
        Equ                 = 0x02      # a = pop 0; b = pop 1; push a == b
        Neq                 = 0x03      # a = pop 0; b = pop 1; push a != b
        Lss                 = 0x04      # a = pop 0; b = pop 1; push a < b
        Gtr                 = 0x05      # a = pop 0; b = pop 1; push a > b
        Leq                 = 0x06      # a = pop 0; b = pop 1; push a <= b
        Geq                 = 0x07      # a = pop 0; b = pop 1; push a >= b
        Ez                  = 0x08      # a = pop 0; push a == 0
        Nez64               = 0x09      # a = pop 0; b = pop 1; push a != 0 && b != 0
        And                 = 0x0A      # a = pop 0; b = pop 1; push a & b
        Or                  = 0x0B      # a = pop 0; b = pop 1; push a | b
        Add                 = 0x0C      # a = pop 0; b = pop 1; push a + b
        Sub                 = 0x0D      # a = pop 0; b = pop 1; push a - b
        Neg                 = 0x0E      # a = pop 0; push -a
        Xor                 = 0x0F      # a = pop 0; b = pop 1; push a ^ b
        Mul                 = 0x10      # a = pop 0; b = pop 1; push a * b
        Div                 = 0x11      # a = pop 0; b = pop 1; push a / b
        Mod                 = 0x12      # a = pop 0; b = pop 1; push a % b
        Nop                 = 0x13      # nop
        Mul2                = 0x14
        Div2                = 0x15
        Mod2                = 0x16
        Add2                = 0x17
        Sub2                = 0x18
        And2                = 0x19
        Xor2                = 0x1A
        Or2                 = 0x1B
        Eval                = 0x1C      # push eval(op)
        Not                 = 0x1D      # a = pop 0; push ~a
        TestScenaFlags      = 0x1E      # (WORD)a = pop 0
        PushReg             = 0x1F      # push regs[(byte)index]
        PushValueByIndex    = 0x20      # push getValueByIndex((byte)index)
        GetChrWork          = 0x21      # push getChrWork((word)a1, (byte)a2)
        Rand                = 0x22      # push rand32()
        PushVar             = 0x23      # push vars[index]

    @classmethod
    def readExpressions(cls, context: InstructionHandlerContext) -> 'List[ScenaExpression]':
        Operator = cls.Operator
        fs = context.disasmContext.fs
        exps = []

        while True:
            e: ScenaExpression = cls(operator = fs.ReadByte())
            e.readOperand(context)
            exps.append(e)
            if e.operator == Operator.Return:
                break

        return exps

    @classmethod
    def writeExpressions(cls, context: InstructionHandlerContext, exprs: List['ScenaExpression']) -> 'List[ScenaExpression]':
        fs = context.disasmContext.fs
        for exp in exprs:
            fs.WriteByte(exp.operator)
            exp.writeOperand(context)

    def __init__(self, operator: Operator, *operand: Tuple[int]):
        if isinstance(operator, str):
            operator = ScenaExpression.Operator[operator]

        elif isinstance(operator, int):
            operator = ScenaExpression.Operator(operator)

        self.operator   = operator
        self.operand    = operand or None

    def readOperand(self, context: InstructionHandlerContext) -> Tuple[int]:
        Operator = self.Operator
        fs = context.disasmContext.fs

        reader = {
            Operator.PushLong           : lambda: fs.ReadULong(),
            Operator.Eval               : lambda: context.disassembler.disasmInstruction(context.disasmContext),
            Operator.TestScenaFlags     : lambda: fs.ReadUShort(),
            Operator.PushReg            : lambda: fs.ReadUShort(),
            Operator.PushValueByIndex   : lambda: fs.ReadByte(),
            Operator.GetChrWork         : lambda: (fs.ReadUShort(), fs.ReadByte()),
            Operator.PushVar            : lambda: fs.ReadByte(),
        }.get(self.operator)

        if reader is not None:
            self.operand = reader()

        return self.operand

    def writeOperand(self, context: InstructionHandlerContext):
        Operator = self.Operator
        fs = context.disasmContext.fs

        writer = {
            Operator.PushLong           : lambda: fs.WriteULong(self.operand[0]),
            Operator.Eval               : lambda: context.eval(self.operand[0]),
            Operator.TestScenaFlags     : lambda: fs.WriteUShort(self.operand[0]),
            Operator.PushReg            : lambda: fs.WriteUShort(self.operand[0]),
            Operator.PushValueByIndex   : lambda: fs.WriteByte(self.operand[0]),
            Operator.GetChrWork         : lambda: (fs.WriteUShort(self.operand[0]), fs.WriteByte(self.operand[1])),
            Operator.PushVar            : lambda: fs.WriteByte(self.operand[0]),
        }.get(self.operator)

        if writer:
            writer()

    def formatOperand(self) -> str:
        match self.operator:
            case self.Operator.GetChrWork:
                return f'0x{self.operand[0]:X}, 0x{self.operand[1]:X}'

            case _:
                return '0x%X' % self.operand

    def __str__(self):
        if self.operand is not None:
            return f"{self.operator}<{self.operand}>"

        return str(self.operator)

    def __repr__(self):
        return self.__str__()
