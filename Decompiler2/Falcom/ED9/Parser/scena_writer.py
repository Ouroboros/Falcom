from Falcom.Common import *
from Falcom import ED9
from Falcom.ED9.Parser.scena_types import *
import pathlib
import uuid

class ScenaGlobalVar(ScenaGlobalVar):
    def load(self):
        pass

    def set(self):
        pass

class IntGlobalVar(ScenaGlobalVar):
    def __init__(self, index: int, name: str):
        super().__init__(index, name, ScenaGlobalVar.Type.Integer)

class StrGlobalVar(ScenaGlobalVar):
    def __init__(self, index: int, name: str):
        super().__init__(index, name, ScenaGlobalVar.Type.String)

class _StringPool:
    def __init__(self):
        self.pool = {}                                  # type: Dict[str, int]
        self.xref = []                                  # type: List[Tuple[str, int]]

    def addString(self, s: str, offset: int):
        self.pool.setdefault(s, 0)
        self.xref.append((s, offset))

class _ScenaWriter:
    def __init__(self):
        self.labels             = {}                    # type: Dict[str, int]
        self.xrefs              = []                    # type: List[Assembler.XRef]
        self.functions          = []                    # type: List[ED9.ScenaFunction]
        self.instructionTable   = None                  # type: ED9.ED9InstructionTable
        self.scenaName          = ''
        self.fs                 = fileio.FileStream().OpenMemory()
        self.globals            = None                  # type: dict
        self.opcodeCallbacks    = []                    # type: List[Callable[[int, Tuple]]]
        self.funcCallbacks      = []                    # type: List[Callable[[str, Callable]]]
        self.runCallbacks       = []                    # type: List[Callable[[dict]]]
        self.stringPool         = _StringPool()         # type: _StringPool

    def init(self, instructionTable: ED9.ED9InstructionTable, scenaName: str):
        self.instructionTable   = instructionTable
        self.scenaName          = scenaName

    def registerRunCallback(self, cb):
        self.runCallbacks.append(cb)

    def registerFuncCallback(self, cb):
        self.funcCallbacks.append(cb)

    def registerOpCodeCallback(self, cb):
        self.opcodeCallbacks.append(cb)

    def setGlobalVars(self, *vars):
        pass

    def functionDecorator(self, name: str, type: ED9.ScenaFunctionType) -> Callable[[], None]:
        def wrapper(f: Callable[[], Any]):
            for cb in self.funcCallbacks:
                f2 = cb(name, f)
                if f2 is not None:
                    f = f2

            func = ED9.ScenaFunction(len(self.functions), -1, name)
            func.type = type
            func.obj = f
            self.functions.append(func)

            return lambda: None

        return wrapper

    # decorators

    def Code(self, name: str):
        return self.functionDecorator(name, ED9.ScenaFunctionType.Code)

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
        raise NotImplementedError

    def addLabel(self, name):
        addr = self.labels.get(name)
        if addr is not None:
            raise Exception(f'label exists: {name} -> 0x{addr:08X}')

        self.labels[name] = self.fs.Position

    def addString(self, s: str):
        self.stringPool.addString(s, self.fs.Position)

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
    _gScena.init(instructionTable = ED9.ScenaOpTable, scenaName = scriptName)
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
