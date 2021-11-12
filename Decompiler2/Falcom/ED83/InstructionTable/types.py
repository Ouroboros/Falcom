from Falcom.Common  import *
from Assembler      import *

DefaultIndent = GlobalConfig.DefaultIndent
UserDefined = OperandType.UserDefined + 1

class ED83OperandType(IntEnum2):
    Offset,     \
    Item,       \
    BGM,        \
    Expression, \
    UserDefined = range(UserDefined, UserDefined + 5)

    __str__     = OperandType.__str__
    __repr__    = OperandType.__repr__

class ED83OperandFormat(OperandFormat):
    sizeTable = {
        **OperandFormat.sizeTable,

        ED83OperandType.Offset     : 4,
        ED83OperandType.Item       : 2,
        ED83OperandType.BGM        : 2,
        ED83OperandType.Expression : None,
    }

class ED83OperandDescriptor(OperandDescriptor):
    formatTable: Dict[str, 'ED83OperandDescriptor'] = {}

    def readValue(self, context: 'handlers.InstructionHandlerContext') -> Any:
        return {
            OperandType.MBCS           : self.readText,
            ED83OperandType.Expression : self.readExpression,
            ED83OperandType.Offset     : lambda context: context.disasmContext.fs.ReadULong(),
            ED83OperandType.Item       : lambda context: context.disasmContext.fs.ReadUShort(),
            ED83OperandType.BGM        : lambda context: context.disasmContext.fs.ReadShort(),

        }.get(self.format.type, super().readValue)(context)

    def readText(self, context: 'handlers.InstructionHandlerContext') -> 'List[TextObject]':
        fs = context.disasmContext.fs

        s = bytearray()
        objs: List[TextObject] = []
        containsCtrlCodes = False

        def flushText():
            if len(s) != 0:
                objs.append(TextObject(value = s.decode(self.format.encoding)))
                s.clear()

        while True:
            c = fs.read(1)
            if len(c) == 0:
                break

            c = c[0]

            if c == 0:
                flushText()
                break

            if c >= 0x20:
                s.append(c)
                if c >= 0x80:
                    s.append(fs.read(1)[0])

                continue

            flushText()

            containsCtrlCodes = True

            try:
                code = TextCtrlCode(c)
            except ValueError:
                code = c

            o = TextObject(code = code)

            if c in [
                    TextCtrlCode.NewLine,
                    TextCtrlCode.NewLine2,
                    TextCtrlCode.WaitForEnter,
                    TextCtrlCode.Clear,
                    TextCtrlCode.Clear2,
                    0x05,
                    TextCtrlCode.ShowAll,
                    0x18,
                ]:
                o.code = TextCtrlCode(o.code)
                pass

            elif c == TextCtrlCode.SetColor:
                o.value = fs.read(1)[0]

            elif c == TextCtrlCode.Item:
                o.value = fs.ReadUShort()

            objs.append(o)

        if containsCtrlCodes is False and len(objs) == 1:
            return objs[0].value

        return objs

    def readExpression(self, context: 'handlers.InstructionHandlerContext') -> 'List[ScenaExpression]':
        return ScenaExpression.readExpressions(context)

    def formatValue(self, context: 'FormatOperandHandlerContext') -> str:
        return {
            OperandType.MBCS            : self.formatTextObjects,
            ED83OperandType.Expression : self.formatExpression,
            ED83OperandType.Offset     : lambda context: "'%s'" % context.operand.value.name,    # CodeBlock
            # ED83OperandType.Item       : ,
            # ED83OperandType.BGM        : ,

        }.get(self.format.type, super().formatValue)(context)

    def formatTextObjects(self, context: 'FormatOperandHandlerContext', depth: int = 1) -> List[str]:
        if isinstance(context.operand.value, str):
            return super().formatValue(context)

        context.instruction.flags |= Flags.FormatArgNewLine

        text = []

        indent = DefaultIndent * (depth - 1)

        objs = context.operand.value       # type: List[TextObject]

        for o in objs:
            if o.code is None:
                text.append(repr(o.value))
                continue

            if o.value is None:
                text.append(str(o.code))
                continue

            text.append('(%s, %s)' % (o.code, o.value))

        for i, t in enumerate(text):
            text[i] = indent + t

        return text

    def formatExpression(self, context: FormatOperandHandlerContext) -> List[str]:
        context.instruction.flags |= Flags.FormatArgNewLine

        expr = context.operand.value           # type: List[ScenaExpression]
        text = []

        for e in expr:
            if isinstance(e.operator, IntEnum2):
                opr = str(e.operator)
            else:
                opr = '0x%02X' % e.operator

            if e.operator == ScenaExpression.Operator.TestScenaFlags:
                t = '(%s, ScenaFlags(0x%02X, %d))' % (opr, e.operand >> 3, e.operand & 7)

            elif e.operand:
                t = '(%s, %s)' % (opr, e.operand)

            else:
                t = opr

            text.append(t)

        return text

def oprdesc(*args, **kwargs) -> ED83OperandDescriptor:
    return ED83OperandDescriptor(ED83OperandFormat(*args, **kwargs))

ED83OperandDescriptor.formatTable.update({
    **OperandDescriptor.formatTable,

    'o' : oprdesc(ED83OperandType.Offset),
    'S' : oprdesc(OperandType.MBCS),
    'E' : oprdesc(ED83OperandType.Expression),
})

class TextCtrlCode(IntEnum2):
    NewLine         = 0x01
    NewLine2        = 0x0A
    WaitForEnter    = 0x02
    Clear           = 0x03
    Clear2          = 0x04
    ShowAll         = 0x06
    SetColor        = 0x07
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
        Push                = 0x00
        End                 = 0x01
        Equ                 = 0x02
        Neq                 = 0x03
        Lss                 = 0x04
        Gtr                 = 0x05
        Leq                 = 0x06
        Ge                  = 0x07
        Ez                  = 0x08
        Nez64               = 0x09
        And                 = 0x0A
        Or                  = 0x0B
        Add                 = 0x0C
        Sub                 = 0x0D
        Neg                 = 0x0E
        Xor                 = 0x0F
        IMul                = 0x10
        IDiv                = 0x11
        IMod                = 0x12
        Stub                = 0x13
        IMul2               = 0x14
        IDiv2               = 0x15
        IMod2               = 0x16
        Add2                = 0x17
        Sub2                = 0x18
        And2                = 0x19
        Xor2                = 0x1A
        Or2                 = 0x1B
        Exec                = 0x1C
        Not                 = 0x1D
        TestScenaFlags      = 0x1E
        GetResult           = 0x1F
        PushValueIndex      = 0x20
        GetChrWork          = 0x21
        Rand                = 0x22

    @classmethod
    def readExpressions(cls, context: 'handlers.InstructionHandlerContext') -> 'List[ScenaExpression]':
        Operator = cls.Operator

        fs = context.disasmContext.fs
        exps = []

        while True:
            e = cls(operator = fs.ReadByte())
            e.readOperand(context)

            exps.append(e)

            if e.operator == Operator.End:
                break

        return exps

    def __init__(self, operator: Operator, *operand: Tuple[int]):
        self.operator   = operator
        self.operand    = operand or None

        if not isinstance(operator, self.Operator):
            try:
                self.operator = self.Operator(operator)
            except ValueError:
                pass

    def readOperand(self, context: 'handlers.InstructionHandlerContext') -> Tuple[int]:
        Operator = self.Operator

        fs = context.disasmContext.fs

        if self.operator == Operator.Exec:
            pass

        reader = {
            Operator.Push           : lambda: fs.ReadULong(),
            Operator.TestScenaFlags : lambda: fs.ReadUShort(),
            Operator.GetResult      : lambda: fs.ReadUShort(),
            Operator.PushValueIndex : lambda: fs.ReadByte(),
            Operator.GetChrWork     : lambda: (fs.ReadUShort(), fs.ReadByte()),
        }.get(self.operator)

        if reader is not None:
            self.operand = reader()

        return self.operand

    def __str__(self):
        if self.operand:
            return '%s %s' % (self.operator, self.operand)

        return str(self.operator)

    def __repr__(self):
        return self.__str__()
