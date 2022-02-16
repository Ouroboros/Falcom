from Falcom.Common  import *
from Assembler      import *
from .utils         import *

DefaultIndent = GlobalConfig.DefaultIndent
UserDefined = OperandType.UserDefined + 1

class ED83OperandType(IntEnum2):
    Offset,         \
    Item,           \
    CraftId,        \
    BGM,            \
    Expression,     \
    Text,           \
    ScenaFlags,     \
    ThreadValue,    \
    ChrId,          \
    ScriptId,       \
    UserDefined = range(UserDefined, UserDefined + 11)

    __str__     = OperandType.__str__
    __repr__    = OperandType.__repr__

class ED83OperandFormat(OperandFormat):
    sizeTable = {
        **OperandFormat.sizeTable,

        ED83OperandType.Offset      : 4,
        ED83OperandType.Item        : 2,
        ED83OperandType.CraftId     : 2,
        ED83OperandType.BGM         : 2,
        ED83OperandType.ScenaFlags  : 2,
        ED83OperandType.ChrId       : 2,
        ED83OperandType.ScriptId    : 1,
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
            ED83OperandType.ChrId           : lambda context: context.disasmContext.fs.ReadUShort(),
            ED83OperandType.Item            : lambda context: context.disasmContext.fs.ReadUShort(),
            ED83OperandType.CraftId         : lambda context: context.disasmContext.fs.ReadUShort(),
            ED83OperandType.ScriptId        : lambda context: context.disasmContext.fs.ReadByte(),
            # ED83OperandType.BGM        : lambda context: context.disasmContext.fs.ReadShort(),

        }.get(self.format.type, super().readValue)(context)

    def writeValue(self, context: InstructionHandlerContext, value: Any):
        return {
            ED83OperandType.Text        : self.writeText,
            ED83OperandType.ScenaFlags  : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED83OperandType.Offset      : lambda context, value: context.disasmContext.fs.WriteULong(0xFFFFABCD),
            ED83OperandType.ChrId       : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED83OperandType.Item        : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED83OperandType.CraftId     : lambda context, value: context.disasmContext.fs.WriteUShort(value),
            ED83OperandType.ScriptId    : lambda context, value: context.disasmContext.fs.WriteByte(value),
            ED83OperandType.Expression  : self.writeExpression,
            # ED83OperandType.ThreadValue : self.writeThreadValue,
        }.get(self.format.type, super().writeValue)(context, value)

    def formatValue(self, context: FormatOperandHandlerContext) -> str:
        return {
            ED83OperandType.Text        : self.formatText,
            ED83OperandType.Expression  : self.formatExpression,
            ED83OperandType.ThreadValue : self.formatThreadValue,
            ED83OperandType.ScriptId    : lambda context: f'ScriptId.{ScriptId(context.operand.value)}',
            ED83OperandType.ScenaFlags  : lambda context: self.formatScenaFlags(context.operand.value),
            ED83OperandType.Offset      : lambda context: "'%s'" % context.operand.value.name,    # CodeBlock
            ED83OperandType.ChrId       : lambda context: self.formatChrId(context.operand.value),
            ED83OperandType.Item        : lambda context: self.formatItemId(context.operand.value),
            ED83OperandType.CraftId     : lambda context: self.formatCraftId(context.operand.value),
            # ED83OperandType.BGM         : ,

        }.get(self.format.type, super().formatValue)(context)

    def readText(self, context: InstructionHandlerContext) -> 'List[TextObject]':
        fs = context.disasmContext.fs
        buf = bytearray()
        objs = []

        while True:
            ch = fs.ReadByte()
            if ch == 0:
                break

            if ch >= 0x20:
                buf.append(ch)
                continue

            if ch == TextCtrlCode.NewLine:
                buf.extend(b'\n')

            if buf:
                objs.append(TextObject(value = buf.decode(self.format.encoding)))
                buf.clear()

            match ch:
                case 0x10 | 0x17 | 0x19:
                    objs.append(TextObject(code = ch, value = fs.ReadUShort()))

                case 0x11 | 0x12:
                    objs.append(TextObject(code = ch, value = fs.ReadULong()))

                case _:
                    objs.append(TextObject(code = ch))

        if buf:
            objs.append(TextObject(value = buf.decode(self.format.encoding)))

        return objs

    def readExpression(self, context: InstructionHandlerContext) -> 'List[ScenaExpression]':
        return ScenaExpression.readExpressions(context)

    def readThreadValue(self, context: InstructionHandlerContext) -> List[Operand]:
        fmts = ScriptThread_getFunctionStrWorkValue(peekByte(context))
        return readAllOperands(context, fmts)

    def writeExpression(self, context: InstructionHandlerContext, value: 'List[ScenaExpression]'):
        ScenaExpression.writeExpressions(context, [ScenaExpression(v[0], *v[1:]) if isinstance(v, tuple | list) else ScenaExpression(v) for v in value])

    def writeText(self, context: InstructionHandlerContext, text: str) -> 'List[TextObject]':
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
                    case 0x10 | 0x17 | 0x19:
                        fs.WriteUShort(value)

                    case 0x11 | 0x12:
                        fs.WriteULong(value)

                    case _:
                        ibp()
                        raise NotImplementedError

        fs.WriteByte(0)

    def formatThreadValue(self, context: FormatOperandHandlerContext) -> List[str]:
        match len(context.operand.value):
            case 2:
                typ, value = context.operand.value
                typ, value = typ.value, value.value

            case 3:
                typ, value, byte3 = context.operand.value
                typ, value, byte3 = typ.value, value.value, byte3.value
                assert byte3 == 0

            case _:
                raise NotImplementedError(str(context.operand.value))

        match typ:
            case 0x11: return f'ArgReg(0x{value:02X})'
            case 0x33: return f'ArgInt({value})'
            case 0x44: return f'ArgStr({value})'
            case 0xDD: return f'ParamStr({formatText(value)})'
            case 0xEE: return f'ParamFloat({value:g})'
            case 0xFF: return f'ParamInt(0x{value:04X})' if value == 100 or value % 100 != 0 else f'ParamInt({value})'
            case _: return f'({", ".join([f"0x{o.value:X}" if isinstance(o.value, int) else ("%s" % o.value) if isinstance(o.value, float) else formatText(o.value) for o in context.operand.value])})'

    def formatText(self, context: FormatOperandHandlerContext) -> str:
        value = context.operand.value
        if isinstance(value, str):
            return formatText(context.operand.value)

        value: List['TextObject']
        t = []
        for v in value:
            if v.code is None:
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

def oprdesc(*args, **kwargs) -> ED83OperandDescriptor:
    return ED83OperandDescriptor(ED83OperandFormat(*args, **kwargs))

ED83OperandDescriptor.formatTable.update({
    **OperandDescriptor.formatTable,

    'O' : oprdesc(ED83OperandType.Offset),
    'F' : oprdesc(ED83OperandType.ScenaFlags),
    'E' : oprdesc(ED83OperandType.Expression),
    'T' : oprdesc(ED83OperandType.Text),
    't' : oprdesc(ED83OperandType.Item),
    'R' : oprdesc(ED83OperandType.CraftId),
    'V' : oprdesc(ED83OperandType.ThreadValue),
    'N' : oprdesc(ED83OperandType.ChrId),
    's' : oprdesc(ED83OperandType.ScriptId),
})

class ScriptId(IntEnum2):
    Map                 = 0x00
    System              = 0x0A
    Current             = 0x0B
    BtlSys              = 0x0C
    Common              = 0x0F
    CurrentCharacter    = 0x10
    BtlMagic            = 0x11
    BtlWin              = 0x12
    BtlCom              = 0x13
    Debug               = 0x14
    Sound               = 0x15
    TalkCommon          = 0x16
    System3             = 0x17

class TextCtrlCode(IntEnum2):
    Null            = 0x00
    NewLine         = 0x01
    Enter           = 0x02
    Clear           = 0x03
    # Clear2          = 0x04
    ShowAll         = 0x06
    SetColor        = 0x07
    NewLine2        = 0x0A
    Item            = 0x10
    Voice           = 0x11
    Craft           = 0x19

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
        PushVar             = 0x23      # push vars[index]
        Expr24              = 0x24      # *(_DWORD *)stack = (*(_DWORD *)ptr & *((_DWORD *)gED84 + 0xDA5)) != 0
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
            Operator.PushVar            : lambda: fs.ReadByte(),
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
            Operator.PushVar            : lambda: fs.WriteByte(self.operand[0]),
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
        if self.operand is not None:
            return f"{self.operator}<{self.operand}>"

        return str(self.operator)

    def __repr__(self):
        return self.__str__()
