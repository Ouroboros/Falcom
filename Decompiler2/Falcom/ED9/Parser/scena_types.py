from multiprocessing.sharedctypes import Value
from tokenize import String
from Falcom.Common import *
from . import utils
import struct, inspect

class ScenaFunctionParamFlags(IntEnum2):
    Pointer     = 0x04
    Nullable    = 0x08
    Mask        = 0x0C

class ScenaFunctionParamType(IntEnum2):
    Value   = 0x01
    Offset  = 0x02
    Mask    = 0x03

    Pointer         = Value | ScenaFunctionParamFlags.Pointer
    NullableValue   = Value | ScenaFunctionParamFlags.Nullable
    NullableOffset  = Offset | ScenaFunctionParamFlags.Nullable

class RawInt(int):
    def __repr__(self) -> str:
        return f'RawInt({super()})'

Value32     = int | float
Nullable32  = Value32 | None
NullableStr = str | None
Pointer     = object

class ScenaHeader:
    MAGIC = b'#scp'

    def __init__(self, *, fs: fileio.FileStream = None):
        self.magic                  = self.MAGIC        # type: int
        self.functionEntryOffset    = 0x18              # type: int
        self.functionCount          = 0                 # type: int
        self.globalVarOffset        = 0                 # type: int
        self.globalVarCount         = 0                 # type: int
        self.dword_14               = 0                 # type: int

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        assert fs.Read(4) == self.MAGIC

        self.functionEntryOffset    = fs.ReadULong()    # 0x04
        self.functionCount          = fs.ReadULong()    # 0x08
        self.globalVarOffset        = fs.ReadULong()    # 0x0C
        self.globalVarCount         = fs.ReadULong()    # 0x10
        self.dword_14               = fs.ReadULong()    # 0x14

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(self.MAGIC)
        fs.write(utils.int_to_bytes(self.functionEntryOffset, 4))
        fs.write(utils.int_to_bytes(self.functionCount, 4))
        fs.write(utils.int_to_bytes(self.globalVarOffset, 4))
        fs.write(utils.int_to_bytes(self.globalVarCount, 4))
        fs.write(utils.int_to_bytes(self.dword_14, 4))

        return fs.getvalue()

class ScenaFunctionEntry:
    def __init__(
            self,
            offset                  : int = 0,
            paramCount              : int = 0,
            byte05                  : int = 0,
            byte06                  : int = 0,
            defaultParamsCount      : int = 0,
            defaultParamsOffset     : int = 0,
            paramFlagsOffset        : int = 0,
            debugSymbolCount        : int = 0,
            debugSymbolOffset       : int = 0,
            nameCrc32               : int = 0,
            nameOffset              : int = 0,
            *,
            fs: fileio.FileStream = None
        ):
        self.offset                 = offset
        self.paramCount             = paramCount
        self.byte05                 = byte05
        self.byte06                 = byte06
        self.defaultParamsCount     = defaultParamsCount
        self.defaultParamsOffset    = defaultParamsOffset
        self.paramFlagsOffset       = paramFlagsOffset
        self.debugSymbolCount       = debugSymbolCount
        self.debugSymbolOffset      = debugSymbolOffset
        self.nameCrc32              = nameCrc32
        self.nameOffset             = nameOffset
        self.name                   = None

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.offset                 = fs.ReadULong()
        self.paramCount             = fs.ReadByte()
        self.byte05                 = fs.ReadByte()
        self.byte06                 = fs.ReadByte()
        self.defaultParamsCount     = fs.ReadByte()
        self.defaultParamsOffset    = fs.ReadULong()
        self.paramFlagsOffset       = fs.ReadULong()
        self.debugSymbolCount       = fs.ReadULong()
        self.debugSymbolOffset      = fs.ReadULong()
        self.nameCrc32              = fs.ReadULong()
        self.nameOffset             = fs.ReadULong()

    def serialize(self) -> bytes:
        fs = io.BytesIO()

        fs.write(utils.int_to_bytes(self.offset, 4))
        fs.write(utils.int_to_bytes(self.paramCount, 1))
        fs.write(utils.int_to_bytes(self.byte05, 1))
        fs.write(utils.int_to_bytes(self.byte06, 1))
        fs.write(utils.int_to_bytes(self.defaultParamsCount, 1))
        fs.write(utils.int_to_bytes(self.defaultParamsOffset, 4))
        fs.write(utils.int_to_bytes(self.paramFlagsOffset, 4))
        fs.write(utils.int_to_bytes(self.debugSymbolCount, 4))
        fs.write(utils.int_to_bytes(self.debugSymbolOffset, 4))
        fs.write(utils.int_to_bytes(self.nameCrc32, 4))
        fs.write(utils.int_to_bytes(self.nameOffset, 4))

        return fs.getvalue()

    def toPython(self) -> List[str]:
        f = [
            'ScenaFunctionEntry(',
            f'{defaultIndent()}offset                = 0x{self.offset:08X},',
            f'{defaultIndent()}paramCount            = 0x{self.paramCount:08X},',
            f'{defaultIndent()}byte05                = 0x{self.byte05:02X},',
            f'{defaultIndent()}byte06                = 0x{self.byte06:02X},',
            f'{defaultIndent()}defaultParamsCount    = 0x{self.defaultParamsCount :08X},',
            f'{defaultIndent()}defaultParamsOffset   = 0x{self.defaultParamsOffset :08X},',
            f'{defaultIndent()}paramFlagsOffset      = 0x{self.paramFlagsOffset:08X},',
            f'{defaultIndent()}debugSymbolCount      = 0x{self.debugSymbolCount:08X},',
            f'{defaultIndent()}debugSymbolOffset     = 0x{self.debugSymbolOffset:08X},',
            f'{defaultIndent()}nameCrc32             = 0x{self.nameCrc32:08X},',
            f'{defaultIndent()}name                  = \'{self.name}\',' if self.name else
            f'{defaultIndent()}nameOffset            = 0x{self.nameOffset:08X},',
            ')',
        ]

        return f

class ScenaParamFlags:
    def __init__(self, typ: object = None, *, fs: fileio.FileStream = None):
        self.flags = 0

        if typ is not None:
            if typ == Value32:
                self.flags = ScenaFunctionParamType.Value

            elif typ == Nullable32:
                self.flags = ScenaFunctionParamType.NullableValue

            elif typ == str:
                self.flags = ScenaFunctionParamType.Offset

            elif typ == NullableStr:
                self.flags = ScenaFunctionParamType.NullableOffset

            elif typ == Pointer:
                self.flags = ScenaFunctionParamType.Pointer

            else:
                raise NotImplementedError(f'unsupported type: {typ}')

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.flags = fs.ReadULong()

    def serialize(self) -> bytes:
        return utils.int_to_bytes(self.flags, 4)

    def toPython(self) -> List[str]:
        f = [
            'ScenaParamFlags(',
            f'{defaultIndent()}flags = 0x{self.flags:08X},',
            ')',
        ]

        return f

    def getPythonType(self) -> str:
        # type = self.flags & ScenaFunctionParamType.Mask

        match self.flags:
            case ScenaFunctionParamType.Value:
                return 'Value32'

            case ScenaFunctionParamType.Offset:
                return 'str'

            case ScenaFunctionParamType.NullableValue:
                return 'Nullable32'

            case ScenaFunctionParamType.NullableOffset:
                return 'NullableStr'

            case ScenaFunctionParamType.Pointer:
                return 'Pointer'

        raise NotImplementedError(str(self))

    def __str__(self) -> str:
        return f'flags = 0x{self.flags:08X}'

    __repr__ =  __str__

class ScenaValue:
    class Type(IntEnum2):
        Raw             = 0
        Integer         = 1
        Float           = 2
        String          = 3

    ClassMap = {
        RawInt  : Type.Raw,
        int     : Type.Integer,
        float   : Type.Float,
        str     : Type.String,
    }

    def __init__(self, value: int | float | str = None, *, fs: fileio.FileStream = None):
        self.value  = value
        if value is not None:
            self.type = self.ClassMap[type(value)]
        else:
            self.type = None

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        value = fs.ReadULong()
        typ = value >> 30

        match typ:
            case ScenaValue.Type.Raw:
                value = RawInt(value)

            case ScenaValue.Type.Integer:
                value = (value << 2) & 0xFFFFFFFF
                sign = 0xC0000000 if value & 0x80000000 != 0 else 0
                value = int.from_bytes((sign | (value >> 2)).to_bytes(4, 'little'), 'little', signed = True)

            case ScenaValue.Type.Float:
                value = struct.unpack('f', ((value << 2) & 0xFFFFFFFF).to_bytes(4, 'little'))[0]

            case ScenaValue.Type.String:
                with fs.PositionSaver:
                    fs.Position = value & 0x3FFFFFFF
                    value = fs.ReadMultiByte()

        self.value = value
        self.type = ScenaValue.Type(typ)

    def serialize(self) -> bytes:
        match self.type:
            case ScenaValue.Type.Raw:
                v = self.value.to_bytes(4, defaultEndian())

            case ScenaValue.Type.Integer:
                assert self.value <= 0x3FFFFFFFF if self.value >= 0 else self.value >= -(0x1FFFFFFF + 1)

                v = (self.value & 0x3FFFFFFF) | (ScenaValue.Type.Integer << 30)
                v = int(v).to_bytes(4, defaultEndian(), signed = False)

            case ScenaValue.Type.Float:
                v = int.from_bytes(struct.pack('f', self.value), defaultEndian())
                v = (v >> 2) | (ScenaValue.Type.Float << 30)
                v = v.to_bytes(4, defaultEndian())

            case _:
                raise NotImplementedError(f'unsupported type: {self.value}')

        return v

    def __str__(self) -> str:
        return f'ScenaValue<{self.value}>'

    __repr__ = __str__

class ScenaGlobalVar:
    class Type(IntEnum2):
        Integer = 0
        String  = 1

    def __init__(self, index: int = None, name: str = None, type: Type = None, *, fs: fileio.FileStream = None):
        self.index  = index
        self.name   = name
        self.type   = type

        self.read(fs)

    def read(self, fs: fileio.FileStream):
        if not fs:
            return

        self.name = ScenaValue(fs = fs).value
        self.type = ScenaGlobalVar.Type(fs.ReadULong())

class ScenaVariable:
    def __init__(
            self,value          = None,
            stackIndex: int     = 0,
            *,
            const               = False,
            stackRef            = False,
            name                = '',
            returnValue         = False,
            isReg               = False,
            isArg               = False,
            isGlobalVar         = False,
            isSetVar            = False,
            loadStack           = False,
            stack: 'ScenaStack' = None,
        ):
        self.value          = value
        self.stackIndex     = stackIndex
        self.const          = const
        self.stackRef       = stackRef
        self._name          = name
        self.returnValue    = returnValue
        self.isReg          = isReg
        self.isArg          = isArg
        self.isGlobalVar    = isGlobalVar
        self.isSetVar       = isSetVar
        self.loadStack      = loadStack

        self.isTos          = False
        self.inst           = None      # type: Assembler.Instruction
        self.stack          = stack

    @property
    def address(self) -> int:
        return self.stackIndex - self.stack.stackTop

    @property
    def name(self) -> str:
        if not self._name:
            if self.isGlobalVar:
                self._name = f'GlobalVar_{self.value:02d}'

            elif self.stackIndex is None:
                self._name = f'<value>'

            else:
                self._name = f'var_{self.stackIndex * 4:02X}'

        return self._name

    @name.setter
    def name(self, v: str):
        self._name = v

    def __str__(self) -> str:
        return f'{self.name} = {self.value}'

    __repr__ = __str__

class ScenaStack:
    def __init__(self):
        self.stack  = []        # type: list[ScenaVariable]
        self.savedContext = {}

    @property
    def stackTop(self) -> int:
        return len(self.stack)

    @property
    def isEmpty(self) -> int:
        return len(self.stack) == 0

    def saveContext(self, key):
        self.savedContext[key] = self.stack.copy()

    def restoreContext(self, key):
        self.stack = self.savedContext.pop(key)

    def clone(self) -> 'ScenaStack':
        stack = ScenaStack()
        stack.stack = self.stack.copy()
        return stack

    def push(self, v: ScenaVariable) -> ScenaVariable:
        v.isTos = True
        if self.stack:
            self.stack[-1].isTos = False

        self.stack.append(v)

        return v

    def Const(self, value) -> ScenaVariable:
        v = ScenaVariable(value, None, const = True, stack = self)
        return v

    def SetVar(self, value = None) -> ScenaVariable:
        v = ScenaVariable(value, self.stackTop, isSetVar = True, stack = self)
        return self.push(v)

    def LoadStack(self, value = None) -> ScenaVariable:
        v = ScenaVariable(value, self.stackTop, loadStack = True, stack = self)
        return self.push(v)

    def Arg(self) -> ScenaVariable:
        v = ScenaVariable(None, self.stackTop, isArg = True, stack = self)
        return self.push(v)

    def Reg(self) -> ScenaVariable:
        v = ScenaVariable(None, self.stackTop, isReg = True, stack = self)
        v.value = v
        return self.push(v)

    def Global(self, index: int) -> ScenaVariable:
        return ScenaVariable(index, self.stackTop, isGlobalVar = True, stack = self)

    def ReturnValue(self) -> ScenaVariable:
        v = ScenaVariable(None, self.stackTop, returnValue = True, stack = self)
        return self.push(v)

    def topOfStack(self) -> ScenaVariable:
        tos = self.stack[-1]
        tos.isTos = True
        return tos

    def pop(self) -> ScenaVariable:
        tos = self.stack.pop()
        tos.isTos = True
        return tos

    def getAt(self, index: int) -> ScenaVariable:
        return self.stack[index]

    def fromOffset(self, offset: int) -> ScenaVariable:
        index = offset // 4
        assert index < 0

        absIndex = self.stackTop + index

        if absIndex < 0:
            return ScenaVariable(None, 0, name = f'arg{-absIndex}', stack = self)

        else:
            return self.stack[index]

class ScenaFunctionType(IntEnum2):
    Invalid             = 0
    Code                = 1

ScenaDataFunctionTypes = set([
])

class ScenaFunction:
    def __init__(
            self,
            index   : int,
            offset  : int,
            name    : str,
            *,
            type    : ScenaFunctionType = ScenaFunctionType.Invalid,
            entry   : ScenaFunctionEntry = None,
            sig     : inspect.Signature = None,
        ):
        self.index      = index
        self.offset     = offset
        self.name       = name
        self.type       = type
        self.obj        = None
        self.entry      = entry
        self.sig        = sig
        self.params     = []        # list[ScenaParamFlags]

    def __str__(self) -> str:
        return f'0x{self.index:04X} 0x{self.offset:08X} {repr(self.name)} {self.type}'

    __repr__ = __str__