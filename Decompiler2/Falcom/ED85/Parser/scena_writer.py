from Falcom.Common import *
from Falcom import ED85
from Falcom.ED85.Parser.scena_types import *
import pathlib
import uuid

Expr        = ED85.ScenaExpression.Operator
TxtCtl      = ED85.TextCtrlCode
ScriptId    = ED85.ScriptId

class _ScenaWriter:
    def __init__(self):
        self.labels             = {}                    # type: Dict[str, int]
        self.xrefs              = []                    # type: List[Assembler.XRef]
        self.functions          = []                    # type: List[ED85.ScenaFunction]
        self.instructionTable   = None                  # type: ED85.ED85InstructionTable
        self.scenaName          = ''
        self.fs                 = fileio.FileStream().OpenMemory()
        self.globals            = None                  # type: dict
        self.opcodeCallbacks    = []                    # type: List[Callable[[int, Tuple]]]
        self.funcCallbacks      = []                    # type: List[Callable[[str, Callable]]]
        self.runCallbacks       = []                    # type: List[Callable[[dict]]]

    def init(self, instructionTable: ED85.ED85InstructionTable, scenaName: str):
        self.instructionTable   = instructionTable
        self.scenaName          = scenaName

    def registerRunCallback(self, cb):
        self.runCallbacks.append(cb)

    def registerFuncCallback(self, cb):
        self.funcCallbacks.append(cb)

    def registerOpCodeCallback(self, cb):
        self.opcodeCallbacks.append(cb)

    def functionDecorator(self, name: str, type: ED85.ScenaFunctionType) -> Callable[[], None]:
        def wrapper(f: Callable[[], Any]):
            for cb in self.funcCallbacks:
                f2 = cb(name, f)
                if f2 is not None:
                    f = f2

            func = ED85.ScenaFunction(len(self.functions), -1, name)
            func.type = type
            func.obj = f
            self.functions.append(func)

            return lambda: None

        return wrapper

    # decorators

    def Code(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.Code)

    def BattleSetting(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.BattleSetting)

    def AnimeClips(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.AnimeClips)

    def ActionTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.ActionTable)

    def WeaponAttTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.WeaponAttTable)

    def BreakTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.BreakTable)

    def AlgoTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.AlgoTable)

    def SummonTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.SummonTable)

    def AddCollision(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.AddCollision)

    def PartTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.PartTable)

    def ReactionTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.ReactionTable)

    def AnimeClipTable(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.AnimeClipTable)

    def FieldMonsterData(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.FieldMonsterData)

    def FieldFollowData(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.FieldFollowData)

    def FaceAuto(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.FaceAuto)

    def ShinigPomBtlset(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.ShinigPomBtlset)

    def StyleName(self, name: str):
        return self.functionDecorator(name, ED85.ScenaFunctionType.StyleName)

    def run(self, g: dict):
        for cb in self.runCallbacks:
            cb(g)

        try:
            self.run2(g)
        except KeyError as e:
            if isinstance(e.args[0], int):
                e.args = (f'0x{e.args[0]:X} ({e.args[0]})',)
            raise

    def run2(self, g: dict):
        self.globals = g

        hdr = ScenaHeader()
        fs = fileio.FileStream(encoding = DefaultEncoding).OpenFile(self.scenaName, 'wb+')

        self.fs = fs
        name = (pathlib.Path(self.scenaName).stem).encode(DefaultEncoding) + b'\x00'

        if len(name) % 4 != 0:
            name += b'\x00' * (4 - len(name) % 4)

        hdr.functionEntryOffset = hdr.headerSize + len(name)
        hdr.functionEntrySize   = len(self.functions) * 4
        hdr.functionNameOffset  = hdr.functionEntryOffset + hdr.functionEntrySize
        hdr.functionCount       = len(self.functions)
        hdr.fullHeaderSize      = 0

        fs.Write(hdr.serialize())
        fs.Write(name)

        fs.Seek(fs.Position + hdr.functionEntrySize)

        funcNames = bytearray()
        pos = fs.Position + hdr.functionCount * 2

        for f in self.functions:
            n = f.name.encode(DefaultEncoding) + b'\x00'
            funcNames.extend(n)
            fs.WriteUShort(pos)
            pos += len(n)

        fs.Write(funcNames)
        hdr.fullHeaderSize = fs.Position

        fs.AlignTo(4)

        for f in self.functions:
            if f.type in ScenaDataFunctionTypes:
                o = f.obj()
                if o:
                    match f.type:
                        case ScenaFunctionType.FaceAuto:
                            fs.AlignTo(16)

                        case ScenaFunctionType.AnimeClips:
                            fs.AlignTo(16)

                        case _:
                            fs.AlignTo(4)

                    f.offset = fs.Position
                    fs.Write(o.serialize())

                    match f.type:
                        case ScenaFunctionType.FaceAuto:
                            pass

                        case _:
                            fs.WriteByte(1)
                    # fs.Position = (fs.Position + 4) & ~3

            else:
                fs.AlignTo(4)
                f.offset = fs.Position
                self.compileCode(fs, f)

        with fs.PositionSaver:
            for x in self.xrefs:
                offset = self.labels[x.name]
                fs.Position = x.offset
                fs.WriteULong(offset)

            self.xrefs.clear()

        fs.Position = 0
        fs.Write(hdr.serialize())

        fs.Position = hdr.functionEntryOffset
        [fs.WriteULong(f.offset) for f in self.functions]

    def addLabel(self, name):
        addr = self.labels.get(name)
        if addr is not None:
            raise Exception(f'label exists: {name} -> 0x{addr:08X}')

        self.labels[name] = self.fs.Position

    def compileCode(self, fs: fileio.FileStream, f: ScenaFunction):
        if f.name:
            self.addLabel(f.name)

        f.obj()

    def onEval(self, code: str):
        eval(code, self.globals)

    def handleOpCode(self, opcode: int, *args, **kwargs):
        # log.debug(f'handle opcode 0x{opcode:X} @ 0x{self.fs.Position:X}')

        for cb in self.opcodeCallbacks:
            if cb(opcode, *args) is True:
                return

        fs = self.fs
        tbl = self.instructionTable
        desc = tbl.getDescriptor(opcode)

        inst = Assembler.Instruction(opcode)
        inst.descriptor = desc

        for i, a in enumerate(args):
            opr = Assembler.Operand()
            opr.value = a
            opr.descriptor = desc.operands and desc.operands[i] or None
            inst.operands.append(opr)

        context = Assembler.InstructionHandlerContext(Assembler.HandlerAction.Assemble, desc)
        context.disasmContext = Assembler.DisasmContext(fs)
        context.instruction = inst
        context.xrefs = self.xrefs
        context.eval = self.onEval

        if desc.handler:
            if desc.handler(context):
                return

        else:
            assert len(desc.operands or []) == len(args)

        tbl.writeOpCode(fs, opcode)
        tbl.writeAllOperands(context, inst.operands)

_gScena: _ScenaWriter = _ScenaWriter()

def createScenaWriter(scriptName: str) -> _ScenaWriter:
    _gScena.init(instructionTable = ED85.ScenaOpTable, scenaName = scriptName)
    return _gScena

def label(name: str):
    _gScena.addLabel(name)

def genLabel() -> str:
    return str(uuid.uuid4())

def emit(*b: int):
    for v in b:
        _gScena.fs.WriteByte(v)

def ScenaFlag(offset: int, flag: int, *args) -> int:
    return ((offset & 0xFFFF) << 3) | (flag & 7)

def ArgReg(index: int, b: int = 0) -> Tuple[int, int, int]:
    return (0x11, index, b)

def ArgInt(index: int, b: int = 0) -> Tuple[int, int, int]:
    return (0x33, index, b)

def ArgStr(index: int, b: int = 0) -> Tuple[int, int, int]:
    return (0x44, index, b)

def ParamStr(s: str) -> Tuple[int, str]:
    return (0xDD, s)

def ParamFloat(v: float, b: int = 0) -> Tuple[int, float, int]:
    return (0xEE, v, b)

def ParamInt(v: int, b: int = 0) -> Tuple[int, int, int]:
    return (0xFF, v, b)
