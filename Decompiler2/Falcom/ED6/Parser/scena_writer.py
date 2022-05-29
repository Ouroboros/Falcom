from Falcom.Common import *
from Falcom import ED6
from Falcom.ED6.Parser.scena_types import *
import uuid

Expr        = ED6.ScenaExpression.Operator
TxtCtl      = ED6.TextCtrlCode

class LambdaHelper:
    def __init__(self, name: str, f: Callable[[], Any]) -> None:
        self.name = name
        self.func = f

class _ScenaWriter:
    def __init__(self):
        self.labels             = {}                    # type: Dict[str, int]
        self.xrefs              = []                    # type: List[Assembler.XRef]
        self.functions          = []                    # type: List[ED6.ScenaFunction]
        self.instructionTable   = None                  # type: ED6.ED6InstructionTable
        self.scenaName          = ''
        self.fs                 = fileio.FileStream().OpenMemory()
        self.globals            = None                  # type: dict
        self.opcodeCallbacks    = []                    # type: List[Callable[[int, Tuple]]]
        self.funcCallbacks      = []                    # type: List[Callable[[str, Callable]]]
        self.runCallbacks       = []                    # type: List[Callable[[dict]]]

    def init(self, instructionTable: ED6.ED6InstructionTable, scenaName: str):
        self.instructionTable   = instructionTable
        self.scenaName          = scenaName

    def registerRunCallback(self, cb):
        self.runCallbacks.append(cb)

    def registerFuncCallback(self, cb):
        self.funcCallbacks.append(cb)

    def registerOpCodeCallback(self, cb):
        self.opcodeCallbacks.append(cb)

    def functionDecorator(self, name: str, type: ED6.ScenaFunctionType) -> Callable[[], None]:
        def wrapper(f: Callable[[], Any]):
            for cb in self.funcCallbacks:
                f2 = cb(name, f)
                if f2 is not None:
                    f = f2

            func = ED6.ScenaFunction(len(self.functions), 0xFFFFFFFF, name)
            func.type = type
            func.obj = f
            self.functions.append(func)

            return lambda: None

        return wrapper

    # decorators

    def Code(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.Code)

    def Header(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.Header)

    def StringTable(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.StringTable)

    def EntryPoint(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.EntryPoint)

    def ChipData(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.ChipData)

    def NpcData(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.NpcData)

    def MonsterData(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.MonsterData)

    def EventData(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.EventData)

    def ActorData(self, name: str):
        return self.functionDecorator(name, ED6.ScenaFunctionType.ActorData)

    def Lambda(self, name: str):
        def wrapper(f: Callable[[], Any]):
            def wrapper():
                self.addLabel(name)
                f()

            return LambdaHelper(name, wrapper)

        return wrapper

    def getDataFunc(self, type: ScenaFunctionType):
        return [f for f in self.functions if f.type == type][-1].obj()

    def getCodeFunc(self) -> list[ScenaFunction]:
        return [f for f in self.functions if f.type == ScenaFunctionType.Code]

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

        hdr = self.writeHeader()
        fs.Position = fs.END_OF_FILE

        funcOffsets = []

        for f in self.functions:
            if f.type != ScenaFunctionType.Code:
                continue

            f.offset = fs.Position
            funcOffsets.append(f.offset)
            hdr.functionTable.size += 2

            self.compileCode(fs, f)

        with fs.PositionSaver:
            for x in self.xrefs:
                offset = self.labels[x.name]
                fs.Position = x.offset
                fs.WriteUShort(offset)

            self.xrefs.clear()

        hdr.functionTable.offset = fs.Position
        [fs.WriteUShort(o) for o in funcOffsets]

        hdr.stringTableOffset = fs.Position
        strtbl = '\x00'.join(self.getDataFunc(ScenaFunctionType.StringTable)).encode(GlobalConfig.DefaultEncoding)
        if strtbl[-1] != 0:
            strtbl += b'\x00'

        fs.Write(strtbl)

        fs.Position = 0
        fs.Write(hdr.serialize())

        fs.Flush()

    def writeHeader(self) -> ScenaHeader:
        fs = self.fs

        hdr: ScenaHeader = self.getDataFunc(ScenaFunctionType.Header)
        hdr.entryPoint = self.getDataFunc(ScenaFunctionType.EntryPoint)

        for i in range(len(hdr.importTable)):
            v = hdr.importTable[i]
            if isinstance(v, int):
                hdr.importTable[i] = DATFileIndex(v)

        fs.Position = 0
        fs.Write(hdr.serialize())

        chips: tuple[int, int] = self.getDataFunc(ScenaFunctionType.ChipData)
        chipCH = [ScenaChipData(c[0]) for c in chips if c[0] is not None]
        chipCP = [ScenaChipData(c[1]) for c in chips if c[1] is not None]

        hdr.dataTable[ScenaDataTableType.ChipDataCH] = ScenaDataIndex(fs.Position, len(chipCH))
        if chipCH:
            [fs.Write(ch.serialize()) for ch in chipCH]
            fs.Write(b'\xFF')

        hdr.dataTable[ScenaDataTableType.ChipDataCP] = ScenaDataIndex(fs.Position, len(chipCP))
        if chipCP:
            [fs.Write(cp.serialize()) for cp in chipCP]
            fs.Write(b'\xFF')

        for index, type in (
                (ScenaDataTableType.NpcData,        ScenaFunctionType.NpcData),
                (ScenaDataTableType.MonsterData,    ScenaFunctionType.MonsterData),
                (ScenaDataTableType.EventData,      ScenaFunctionType.EventData),
                (ScenaDataTableType.ActorData,      ScenaFunctionType.ActorData),
            ):
            data = self.getDataFunc(type)
            hdr.dataTable[index] = ScenaDataIndex(fs.Position, len(data))
            [fs.Write(e.serialize()) for e in data]

        hdr.headerSize = fs.Position

        fs.Position = 0
        fs.Write(hdr.serialize())

        return hdr

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
        context.instructionTable = self.instructionTable
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
    _gScena.init(instructionTable = ED6.ScenaOpTable, scenaName = scriptName)
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

def TXT(index: int, s: str) -> str:
    return s
