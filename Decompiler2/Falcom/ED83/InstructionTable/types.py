from Falcom.Common  import *
from Assembler      import *
from .utils         import *

DefaultIndent = GlobalConfig.DefaultIndent
UserDefined = OperandType.UserDefined + 1

class ED83OperandType(IntEnum2):
    Offset,         \
    Item,           \
    BGM,            \
    Expression,     \
    Text,           \
    ScenaFlags,     \
    ThreadValue,    \
    UserDefined = range(UserDefined, UserDefined + 8)

    __str__     = OperandType.__str__
    __repr__    = OperandType.__repr__

class ED83OperandFormat(OperandFormat):
    sizeTable = {
        **OperandFormat.sizeTable,

        ED83OperandType.Offset      : 4,
        ED83OperandType.Item        : 2,
        ED83OperandType.BGM         : 2,
        ED83OperandType.ScenaFlags  : 2,
        ED83OperandType.Expression  : None,
        ED83OperandType.Text        : None,
    }

class ED83OperandDescriptor(OperandDescriptor):
    formatTable: Dict[str, 'ED83OperandDescriptor'] = {}

    def readValue(self, context: InstructionHandlerContext) -> Any:
        return {
            ED83OperandType.Text            : self.readText,
            ED83OperandType.Expression      : self.readExpression,
            ED83OperandType.ThreadValue     : self.readThreadValue,
            ED83OperandType.ScenaFlags      : lambda context: context.disasmContext.fs.ReadUShort(),
            ED83OperandType.Offset          : lambda context: context.disasmContext.fs.ReadULong(),
            # ED83OperandType.Item       : lambda context: context.disasmContext.fs.ReadUShort(),
            # ED83OperandType.BGM        : lambda context: context.disasmContext.fs.ReadShort(),

        }.get(self.format.type, super().readValue)(context)

    def writeValue(self, context: InstructionHandlerContext, value: Any):
        return {
            ED83OperandType.Text        : self.writeText,
            ED83OperandType.ScenaFlags  : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED83OperandType.Offset      : lambda context, value: context.disasmContext.fs.WriteULong(0xFFFFABCD),
            ED83OperandType.Expression  : self.writeExpression,
            # ED83OperandType.ThreadValue : self.writeThreadValue,
        }.get(self.format.type, super().writeValue)(context, value)

    def formatValue(self, context: FormatOperandHandlerContext) -> str:
        return {
            ED83OperandType.Text        : self.formatText,
            OperandType.MBCS            : self.formatText,
            ED83OperandType.Expression  : self.formatExpression,
            ED83OperandType.ThreadValue : self.formatThreadValue,
            ED83OperandType.ScenaFlags  : lambda context: self.formatScenaFlags(context.operand.value),
            ED83OperandType.Offset      : lambda context: "'%s'" % context.operand.value.name,    # CodeBlock
            # ED83OperandType.Item        : ,
            # ED83OperandType.BGM         : ,

        }.get(self.format.type, super().formatValue)(context)

    def readText(self, context: InstructionHandlerContext) -> 'List[TextObject]':
        fs = context.disasmContext.fs
        text = bytearray()
        while True:
            ch = fs.ReadByte()
            if ch == 0:
                break

            text.append(ch)
            if ch >= 0x20:
                continue

            if ch == 0x10:
                text.extend(fs.Read(2))
                continue

            if 0x10 < ch <= 0x12:
                text.extend(fs.Read(4))

        return text.decode(GlobalConfig.DefaultEncoding)

    def readExpression(self, context: InstructionHandlerContext) -> 'List[ScenaExpression]':
        return ScenaExpression.readExpressions(context)

    def readThreadValue(self, context: InstructionHandlerContext) -> List[Operand]:
        fmts = ScriptThread_getFunctionStrWorkValue(peekByte(context))
        return readAllOperands(context, fmts)

    def writeExpression(self, context: InstructionHandlerContext, value: 'List[ScenaExpression]'):
        ScenaExpression.writeExpressions(context, [ScenaExpression(v[0], *v[1:]) if isinstance(v, tuple | list) else ScenaExpression(v) for v in value])

    def writeText(self, context: InstructionHandlerContext, text: str) -> 'List[TextObject]':
        fs = context.disasmContext.fs
        return fs.Write(text.encode(self.format.encoding) + b'\x00')

    def formatThreadValue(self, context: FormatOperandHandlerContext) -> List[str]:
        return f'({", ".join([f"0x{o.value:X}" if isinstance(o.value, int) else f"{round(o.value, 5)}" if isinstance(o.value, float) else formatText(o.value) for o in context.operand.value])})'

    def formatText(self, context: FormatOperandHandlerContext) -> str:
        return formatText(context.operand.value)

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

            if e.operator == ScenaExpression.Operator.TestScenaFlags:
                t = f"({opr}, {self.formatScenaFlags(e.operand)})"

            elif e.operator == ScenaExpression.Operator.Eval:
                s = context.formatter.formatInstruction(e.operand)
                t = f"({opr}, '{'; '.join(s)}')"

            elif e.operand is not None:
                t = f"({opr}, {e.formatOperand()})"

            else:
                t = opr

            text.append(t)

        return text

    def formatScenaFlags(self, flags: int) -> str:
        return '0x%X' % flags
        flags &= 0XFFFF
        return f'ScenaFlag(0x{flags >> 3:04X}, {flags & 7})'

def oprdesc(*args, **kwargs) -> ED83OperandDescriptor:
    return ED83OperandDescriptor(ED83OperandFormat(*args, **kwargs))

ED83OperandDescriptor.formatTable.update({
    **OperandDescriptor.formatTable,

    'O' : oprdesc(ED83OperandType.Offset),
    'F' : oprdesc(ED83OperandType.ScenaFlags),
    'E' : oprdesc(ED83OperandType.Expression),
    'T' : oprdesc(ED83OperandType.Text),
    'V' : oprdesc(ED83OperandType.ThreadValue),
})

class TextCtrlCode(IntEnum2):
    NewLine         = 0x01
    WaitForEnter    = 0x02
    Clear           = 0x03
    Clear2          = 0x04
    ShowAll         = 0x06
    SetColor        = 0x07
    NewLine2        = 0x0A
    Item            = 0x1F

class TextObject:
    def __init__(self, code: int = None, value: Any = None):
        self.code   = code              # type: int
        self.value  = value             # type: Any

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
        Expr23              = 0x23      # *(_DWORD *)stack = sub_14030FE70((__int64)gCurrentSaveData, *(unsigned __int8 *)ptr)
        Expr24              = 0x24      # *(_DWORD *)stack = (*(_DWORD *)ptr & *((_DWORD *)gCurrentSaveData + 0xDA5)) != 0
        Expr25              = 0x25      # *(_DWORD *)stack = *(_DWORD *)(*(_QWORD *)(qword98 + 0x60) + 4 * *(unsigned __int8 *)ptr)

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
            Operator.PushReg            : lambda: fs.ReadByte(),
            Operator.PushValueByIndex   : lambda: fs.ReadByte(),
            Operator.GetChrWork         : lambda: (fs.ReadUShort(), fs.ReadByte()),
            Operator.Expr23             : lambda: fs.ReadByte(),
            Operator.Expr24             : lambda: fs.ReadULong(),
            Operator.Expr25             : lambda: fs.ReadUShort(),
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
            Operator.PushReg            : lambda: fs.WriteByte(self.operand[0]),
            Operator.PushValueByIndex   : lambda: fs.WriteByte(self.operand[0]),
            Operator.GetChrWork         : lambda: (fs.WriteUShort(self.operand[0]), fs.WriteByte(self.operand[1])),
            Operator.Expr23             : lambda: fs.WriteByte(self.operand[0]),
            Operator.Expr24             : lambda: fs.WriteULong(self.operand[0]),
            Operator.Expr25             : lambda: fs.WriteUShort(self.operand[0]),
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
        if self.operand:
            return f"{self.operator}<{self.operand}>"

        return str(self.operator)

    def __repr__(self):
        return self.__str__()
