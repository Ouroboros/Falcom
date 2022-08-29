from Assembler.function import CodeBlock, Function
from Assembler.instruction import Flags, Instruction
from Assembler.instruction_table import InstructionDescriptor
from ..InstructionTable import ScenaOpTable as ED9ScenaOpTable
from .scena_types import *
from pprint import pprint
import pathlib

if TYPE_CHECKING:
    from Assembler.instruction_table import InstructionTable

__all__ = (
    'ScenaParser',
    'ScenaHeader',
    'ScenaFunctionType',
    'ScenaFunction',
    'ScenaFunctionEntry',
)

class ScenaFormatter(Assembler.Formatter):
    def __init__(self, parser: 'ScenaParser', instructionTable: 'InstructionTable', *args, **kwargs):
        super().__init__(instructionTable, *args, **kwargs)
        self.parser = parser

    def formatLabel(self, name: str) -> List[str]:
        return [
            f'def _{name}(): pass',
            '',
            f"label('{name}')",
        ]

    def formatFuncion(self, func: ScenaFunction) -> List[str]:
        if self.optimizer is not None:
            self.optimizer.optimizeFunction(func)

        log.debug(f'format {func.name}')

        funcName = func.name
        if not funcName:
            if func.type == ScenaFunctionType.BattleSetting:
                funcName = f'{func.type}{func.index:02X}'
            else:
                funcName = f'func_{func.offset:X}'

        if func.entry.defaultParamsCount != 0:
            args = []
            for index, p in enumerate(func.params):
                p: ScenaParamFlags
                # assert p.defaultValue is not None
                s = f'arg{index + 1}'
                if p.defaultValue is not None:
                    s += f' = {repr(p.defaultValue)}'

                args.append(s)

            args = ', '.join(args)

        else:
            args = ', '.join([f'arg{index + 1}: {p.getPythonType()}' for index, p in enumerate(func.params)])

        f = [
            f'# id: 0x{func.index:04X} offset: 0x{func.offset:X}',
            f'@scena.{func.type}(\'{func.name}\')',
            f'def {funcName}({args}):',
        ]

        if func.type in ScenaDataFunctionTypes:
            body = self.formatDataFunction(func)

        elif func.type == ScenaFunctionType.Code:
            body = self.formatCode(func)

        else:
            raise NotImplementedError(f'unknown func type: {func.type}')

        if not body:
            body = ['pass']

        f.extend([f'{GlobalConfig.DefaultIndent}{l}'.rstrip() for l in body])
        if f[-1] != '':
            f.append('')

        return f

    def formatCode(self, f: ScenaFunction) -> List[str]:
        func: Function = f.obj

        if func is None:
            return

        body = []
        blk = self.formatBlock(func.block, genLabel = False)
        for b in blk:
            body.append(b)

        return body

    def formatDataFunction(self, f: ScenaFunction) -> List[str]:
        if f.obj is None:
            return

        body = f.obj.toPython()
        body[0] = 'return ' + body[0]
        return body

class ScenaParser:
    def __init__(self, fs: fileio.FileStream, name: str = ''):
        self.fs                 = fs                # type: fileio.FileStream
        self.name               = name              # type: str
        self.header             = None              # type: ScenaHeader
        self.globalVars         = []                # type: list[ScenaGlobalVar]
        self.functions          = []                # type: List[ScenaFunction]
        self.functionNameMap    = {}                # type: Dict[str, bool]
        self.instructionCb      = None              # type: Callable[[Instruction], None]

    def __str__(self) -> str:
        funcs = '\n'.join([str(f) for f in self.functions])
        return '\n'.join([
            f'magic                 = {self.header.magic}',
            f'functionEntryOffset   = 0x{self.header.functionEntryOffset:08X}',
            f'functionCount         = 0x{self.header.functionCount:08X}',
            f'globalVarOffset       = 0x{self.header.globalVarOffset:08X}',
            '',
            f'{funcs}',
        ])

    def parse(self):
        self.readHeader()
        self.disasmFunctions()

    def readHeader(self):
        fs = self.fs
        fs.Position = 0

        self.header = ScenaHeader(fs = fs)

        hdr = self.header

        funcEntries = [ScenaFunctionEntry(fs = fs) for _ in range(hdr.functionCount)]

        for index, f in enumerate(funcEntries):
            assert f.nameOffset >> 30 == 3
            fs.Position = f.nameOffset & 0x3FFFFFFF
            func = ScenaFunction(index = index, offset = f.addr, name = fs.ReadMultiByte(), type = ScenaFunctionType.Code, entry = f)

            fs.Position = f.paramFlagsOffset
            func.params = [ScenaParamFlags(fs = fs) for _ in range(f.paramCount)]

            fs.Position = func.entry.defaultParamsOffset
            for i in range(func.entry.defaultParamsCount):
                func.params[len(func.params) - i - 1].defaultValue = ScenaValue(fs = fs).value

            self.functions.append(func)

            f.name = self.functions[-1].name

            # print('\n'.join(f.toPython()))

        if hdr.globalVarCount == 0:
            return

        fs.Position = hdr.globalVarOffset
        self.globalVars = [ScenaGlobalVar(i, fs = fs) for i in range(hdr.globalVarCount)]

    def getCodeFuncName(self, funcID: int) -> str:
        return self.functions[funcID].name

    def getGlobalVarName(self, index: int) -> str:
        return f'g_{self.globalVars[index].name}'

    def setInstructionCallback(self, cb: Callable[[Instruction], None]):
        self.instructionCb = cb

    def disasmFunctions(self):
        fs = self.fs
        dis = Assembler.Disassembler(ED9ScenaOpTable)
        ctx = Assembler.DisasmContext(fs, instCallback = self.instructionCb, scriptName = self.name)
        optimizer = ED9Optimizer(self)

        for func in self.functions:
            log.debug(f'disasm func: {func}')

            match func.type:
                case ScenaFunctionType.Code:
                    fs.Position = func.offset
                    try:
                        func.obj = dis.disasmFunction(ctx, name = func.name)
                    except KeyError as e:
                        e.args = (f'0x{e.args[0]:X} ({e.args[0]})',)
                        raise

                    optimizer.optimizeFunction(func, dis)

                case _:
                    if func.type not in ScenaDataFunctionTypes:
                        raise NotImplementedError(f'unknown func type: {func.type}')

    def generatePython(self, filename: str) -> List[str]:
        formatter = ScenaFormatter(self, ED9ScenaOpTable, name = self.name)

        lines = f'''\
import sys
sys.path.append(r'{pathlib.Path(__file__).parent.parent.parent.parent}')

from Falcom.ED9.Parser.scena_writer_helper import *
try:
    import {pathlib.Path(filename).stem.strip()}_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('{filename}')

'''.splitlines()

        if self.globalVars:
            align = max([len(g.name) for g in self.globalVars])
            align = (align + 4) & ~3
            lines.extend([
                *[f"{self.getGlobalVarName(g.index).ljust(align)}= {g.type == ScenaGlobalVar.Type.Integer and 'IntGlobalVar' or 'StrGlobalVar'}({g.index}, '{g.name}')" for g in self.globalVars],
                '',
                'scena.setGlobalVars(',
                *[f'{defaultIndent()}g_{g.name},' for g in self.globalVars],
                ')',
                '',
            ])

        for func in self.functions:
            lines.extend(formatter.formatFuncion(func))

        main = '''\
def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

'''

        lines.extend(main.splitlines())

        # print('\n'.join(lines))

        return lines

from ..InstructionTable.mediumlevelil import *

class OPCode:
    PUSH                    = ED9ScenaOpTable.getDescriptorByName('PUSH')
    POP                     = ED9ScenaOpTable.getDescriptorByName('POP')
    LOAD_STACK              = ED9ScenaOpTable.getDescriptorByName('LOAD_STACK')
    LOAD_STACK_DEREF        = ED9ScenaOpTable.getDescriptorByName('LOAD_STACK_DEREF')
    PUSH_STACK_OFFSET       = ED9ScenaOpTable.getDescriptorByName('PUSH_STACK_OFFSET')
    POP_TO                  = ED9ScenaOpTable.getDescriptorByName('POP_TO')
    POP_TO_DEREF            = ED9ScenaOpTable.getDescriptorByName('POP_TO_DEREF')
    LOAD_GLOBAL             = ED9ScenaOpTable.getDescriptorByName('LOAD_GLOBAL')
    SET_GLOBAL              = ED9ScenaOpTable.getDescriptorByName('SET_GLOBAL')
    GET_REG                 = ED9ScenaOpTable.getDescriptorByName('GET_REG')
    SET_REG                 = ED9ScenaOpTable.getDescriptorByName('SET_REG')
    JMP                     = ED9ScenaOpTable.getDescriptorByName('JMP')
    CALL                    = ED9ScenaOpTable.getDescriptorByName('CALL')
    RETURN                  = ED9ScenaOpTable.getDescriptorByName('RETURN')
    POP_JMP_NOT_ZERO        = ED9ScenaOpTable.getDescriptorByName('POP_JMP_NOT_ZERO')
    POP_JMP_ZERO            = ED9ScenaOpTable.getDescriptorByName('POP_JMP_ZERO')
    ADD                     = ED9ScenaOpTable.getDescriptorByName('ADD')
    SUB                     = ED9ScenaOpTable.getDescriptorByName('SUB')
    MUL                     = ED9ScenaOpTable.getDescriptorByName('MUL')
    DIV                     = ED9ScenaOpTable.getDescriptorByName('DIV')
    MOD                     = ED9ScenaOpTable.getDescriptorByName('MOD')
    EQ                      = ED9ScenaOpTable.getDescriptorByName('EQ')
    NE                      = ED9ScenaOpTable.getDescriptorByName('NE')
    GT                      = ED9ScenaOpTable.getDescriptorByName('GT')
    GE                      = ED9ScenaOpTable.getDescriptorByName('GE')
    LT                      = ED9ScenaOpTable.getDescriptorByName('LT')
    LE                      = ED9ScenaOpTable.getDescriptorByName('LE')
    BITWISE_AND             = ED9ScenaOpTable.getDescriptorByName('BITWISE_AND')
    BITWISE_OR              = ED9ScenaOpTable.getDescriptorByName('BITWISE_OR')
    LOGICAL_AND             = ED9ScenaOpTable.getDescriptorByName('LOGICAL_AND')
    LOGICAL_OR              = ED9ScenaOpTable.getDescriptorByName('LOGICAL_OR')
    NEG                     = ED9ScenaOpTable.getDescriptorByName('NEG')
    EZ                      = ED9ScenaOpTable.getDescriptorByName('EZ')
    NOT                     = ED9ScenaOpTable.getDescriptorByName('NOT')
    CALL_MODULE             = ED9ScenaOpTable.getDescriptorByName('CALL_MODULE')
    CALL_MODULE_NO_RETURN   = ED9ScenaOpTable.getDescriptorByName('CALL_MODULE_NO_RETURN')
    SYSCALL                 = ED9ScenaOpTable.getDescriptorByName('SYSCALL')
    PUSH_CALLER_CONTEXT     = ED9ScenaOpTable.getDescriptorByName('PUSH_CALLER_CONTEXT')
    DEBUG_SET_LINENO        = ED9ScenaOpTable.getDescriptorByName('DEBUG_SET_LINENO')
    POPN                    = ED9ScenaOpTable.getDescriptorByName('POPN')
    DEBUG_LOG               = ED9ScenaOpTable.getDescriptorByName('DEBUG_LOG')

    PUSH_INT                = ED9ScenaOpTable.getDescriptorByName('PUSH_INT')
    PUSH_FLOAT              = ED9ScenaOpTable.getDescriptorByName('PUSH_FLOAT')
    PUSH_STR                = ED9ScenaOpTable.getDescriptorByName('PUSH_STR')
    PUSH_FUNC_ID            = ED9ScenaOpTable.getDescriptorByName('PUSH_FUNC_ID')
    PUSH_RET_ADDR           = ED9ScenaOpTable.getDescriptorByName('PUSH_RET_ADDR')

    MLIL_STUB               = ED9ScenaOpTable.getDescriptorByName('MLIL_STUB')

class InstructionList:
    def __init__(self) -> None:
        self.instructions = []
        self.currentInstruction = None  # type: Instruction

    def addMLIL(self, mlil: MediumLevelILInstruction):
        inst = Instruction(OPCode.MLIL_STUB.opcode, descriptor = OPCode.MLIL_STUB)
        inst.operands = mlil
        inst.currinst = self.currentInstruction
        self.instructions.append(inst)
        return inst

    def add(self, inst: Instruction):
        self.instructions.append(inst)
        return inst

class ED9Optimizer():
    def __init__(self, parser: ScenaParser):
        self.parser = parser

    def getOpCode(self, name: str) -> InstructionDescriptor:
        return ED9ScenaOpTable.getDescriptorByName(name)

    def setMLIL(self, inst: Instruction, mlil: MediumLevelILInstruction):
        inst.opcode = OPCode.MLIL_STUB.opcode
        inst.descriptor = OPCode.MLIL_STUB
        inst.operands = mlil

    def optimizeFunction(self, func: ScenaFunction, dis: Disassembler):
        console.setTitle(f'optimize {func.name}')
        self.pass0(func, dis)
        self.pass1(func, dis)

    def pass0(self, func: ScenaFunction, dis: Disassembler):
        self.translateToMLIL(func, dis, optimizeReturnAddr = True)

    def pass1(self, func: ScenaFunction, dis: Disassembler):
        self.translateToMLIL(func, dis, overwriteInstructions = True)

    def translateToMLIL(self, func: ScenaFunction, dis: Disassembler, *, optimizeReturnAddr = False, overwriteInstructions = False) -> list[Instruction]:
        # if not func.name == 'OnEventBegin': return

        stack = ScenaStack()

        def pushArgs():
            for i in range(len(func.params), 0, -1):
                stack.Arg().name = f'arg{i}'

        pushArgs()

        blocks: list[CodeBlock] = func.obj.block.getAllBlocks()
        for bb in blocks:
            try:
                stack.restoreContext(bb.name)
            except KeyError:
                pass

            instructions = InstructionList()
            ignoredInsts = set()
            pushVarMap = {}
            currentLineno = 0

            for index, inst in enumerate(bb.instructions):
                if index in ignoredInsts:
                    continue

                instructions.currentInstruction = inst

                # print(inst)

                def getNextInst() -> Instruction | None:
                    if index + 1 < len(bb.instructions):
                        return bb.instructions[index + 1]

                    return None

                match inst.opcode:
                    case OPCode.DEBUG_SET_LINENO.opcode:
                        currentLineno = inst.operands[0].value
                        continue

                    case OPCode.PUSH_INT.opcode | \
                         OPCode.PUSH.opcode | \
                         OPCode.PUSH_FLOAT.opcode | \
                         OPCode.PUSH_STR.opcode:
                        src = stack.Const(inst.operands[0])
                        dst = stack.SetVar(src)
                        dst.inst = instructions.addMLIL(MediumLevelILSetVar(dst, src))

                        if optimizeReturnAddr:
                            pushVarMap[dst] = inst

                    case OPCode.PUSH_STACK_OFFSET.opcode:
                        src = stack.fromOffset(inst.operands[0].value)
                        dst = stack.SetVar(src)
                        dst.inst = instructions.addMLIL(MediumLevelILAddressOf(dst, src))

                    case OPCode.LOAD_STACK.opcode:
                        src = stack.fromOffset(inst.operands[0].value)
                        dst = stack.LoadStack(src)
                        dst.inst = instructions.addMLIL(MediumLevelILSetVar(dst, src))

                    case OPCode.GET_REG.opcode:
                        instructions.addMLIL(MediumLevelILGetReg(inst.operands[0].value, stack.Reg()))

                    case OPCode.SET_REG.opcode:
                        instructions.addMLIL(MediumLevelILSetReg(inst.operands[0].value, stack.pop()))

                    case OPCode.NEG.opcode | \
                         OPCode.EZ.opcode | \
                         OPCode.NOT.opcode:

                        instructions.addMLIL(
                            {
                                OPCode.NEG.opcode           : MediumLevelILNeg,
                                OPCode.EZ.opcode            : MediumLevelILCmpEZ,
                                OPCode.NOT.opcode           : MediumLevelILNot,
                            }[inst.opcode](stack.topOfStack())
                        )

                    case OPCode.ADD.opcode | \
                         OPCode.SUB.opcode | \
                         OPCode.MUL.opcode | \
                         OPCode.DIV.opcode | \
                         OPCode.MOD.opcode | \
                         OPCode.EQ.opcode | \
                         OPCode.NE.opcode | \
                         OPCode.GT.opcode | \
                         OPCode.GE.opcode | \
                         OPCode.LT.opcode | \
                         OPCode.LE.opcode | \
                         OPCode.LOGICAL_OR.opcode | \
                         OPCode.LOGICAL_AND.opcode | \
                         OPCode.BITWISE_OR.opcode | \
                         OPCode.BITWISE_AND.opcode:
                        tos, tos1 = stack.pop(), stack.topOfStack()

                        instructions.addMLIL(
                            {
                                OPCode.ADD.opcode           : MediumLevelILAdd,
                                OPCode.SUB.opcode           : MediumLevelILSub,
                                OPCode.MUL.opcode           : MediumLevelILMul,
                                OPCode.DIV.opcode           : MediumLevelILDiv,
                                OPCode.MOD.opcode           : MediumLevelILMod,
                                OPCode.EQ.opcode            : MediumLevelILCmpEQ,
                                OPCode.NE.opcode            : MediumLevelILCmpNE,
                                OPCode.GT.opcode            : MediumLevelILCmpGT,
                                OPCode.GE.opcode            : MediumLevelILCmpGE,
                                OPCode.LT.opcode            : MediumLevelILCmpLT,
                                OPCode.LE.opcode            : MediumLevelILCmpLE,
                                OPCode.LOGICAL_OR.opcode    : MediumLevelILLogicalOr,
                                OPCode.LOGICAL_AND.opcode   : MediumLevelILLogicalAnd,
                                OPCode.BITWISE_OR.opcode    : MediumLevelILOr,
                                OPCode.BITWISE_AND.opcode   : MediumLevelILAnd,
                            }[inst.opcode](tos1, tos)
                        )

                    case OPCode.POP_TO.opcode:
                        tos = stack.pop()
                        dst = stack.fromOffset(inst.operands[0].value)
                        dst.inst = inst

                        instructions.addMLIL(MediumLevelILSetVar(dst, tos))

                    case OPCode.POP.opcode | OPCode.POPN.opcode:
                        n = inst.operands[0].value
                        if inst.opcode == OPCode.POP.opcode:
                            n //= 4

                        for _ in range(n):
                            instructions.addMLIL(MediumLevelILDelVar(stack.pop()))

                    case OPCode.RETURN.opcode:
                        instructions.addMLIL(MediumLevelILRet()).flags |= Flags.EndBlock

                    case OPCode.POP_JMP_ZERO.opcode | OPCode.POP_JMP_NOT_ZERO.opcode:
                        cond = stack.pop()
                        block = inst.operands[0]
                        stack.saveContext(block.value.name)
                        instructions.addMLIL((MediumLevelILJmpIfZero if inst.opcode == OPCode.POP_JMP_ZERO.opcode else MediumLevelILJmpIfNotZero)(cond, block))

                    case OPCode.JMP.opcode:
                        block = inst.operands[0]
                        stack.saveContext(block.value.name)
                        instructions.add(inst)

                    case OPCode.PUSH_CALLER_CONTEXT.opcode:
                        src = stack.Const(inst.operands[0])
                        funcId = stack.SetVar(func.index)
                        retAddr = stack.SetVar(src)
                        currScriptLowPart = stack.SetVar(self.parser.name)
                        currScriptHighPart = stack.SetVar(self.parser.name)
                        returnMagic = stack.SetVar(0xF0000000)

                        # funcId.inst             = instructions.addMLIL(MediumLevelILSetVar(funcId, None))
                        # retAddr.inst            = instructions.addMLIL(MediumLevelILSetVar(retAddr, src))
                        # currScriptLowPart.inst  = instructions.addMLIL(MediumLevelILSetVar(currScriptLowPart, None))
                        # currScriptHighPart.inst = instructions.addMLIL(MediumLevelILSetVar(currScriptHighPart, None))
                        # returnMagic.inst        = instructions.addMLIL(MediumLevelILSetVar(returnMagic, None))

                    case OPCode.CALL.opcode:
                        hasReturnValue = False

                        nextInst = getNextInst()
                        if nextInst and nextInst.opcode == OPCode.GET_REG.opcode and nextInst.operands[0].value == 0:
                            # next inst is get_reg(0)
                            hasReturnValue = True
                            ignoredInsts.add(index + 1)

                        target_func = self.parser.functions[inst.operands[0].value]
                        paramCount = len(target_func.params)
                        params = [stack.pop() for _ in range(paramCount + 2)]   # retaddr and caller func index

                        if optimizeReturnAddr:
                            # ibp()
                            try:
                                push_retaddr: Instruction = pushVarMap[params[-2]]
                                target = bb.addBranch(dis.createCodeBlock(push_retaddr.operands[0].value.value))
                                dis.disassembledOffset[target.offset].xrefs.append(XRef(target.name, -1))
                                push_retaddr.operands[0].value = target
                                applyDescriptorsToOperands(push_retaddr.operands, 'O')
                            except KeyError:
                                pass

                        for p in params:
                            if p.inst is not None:
                                p.inst.flags |= Flags.FormatIgnore

                        instructions.addMLIL(MediumLevelILCall(target_func, params, returnValue = stack.Reg() if hasReturnValue else None))

                    case OPCode.CALL_MODULE.opcode:
                        hasReturnValue = False

                        nextInst = getNextInst()
                        if nextInst and nextInst.opcode == OPCode.GET_REG.opcode and nextInst.operands[0].value == 0:
                            # next inst is get_reg(0)
                            hasReturnValue = True
                            ignoredInsts.add(index + 1)

                        module, funcName = inst.operands[0], inst.operands[1]
                        paramCount = inst.operands[2].value
                        params = [stack.pop() for _ in range(paramCount + 5)]   # funcid, retaddr, current_script * 2, 0xF0000000
                        for p in params:
                            if p.inst is not None:
                                p.inst.flags |= Flags.FormatIgnore

                        instructions.addMLIL(MediumLevelILCallModule(module, funcName, params))

                    case OPCode.CALL_MODULE_NO_RETURN.opcode:
                        module, funcName = inst.operands[0], inst.operands[1]
                        paramCount = inst.operands[2].value
                        params = [stack.pop() for _ in range(paramCount)]
                        for p in params:
                            if p.inst is not None:
                                p.inst.flags |= Flags.FormatIgnore

                        instructions.addMLIL(MediumLevelILCallModule(module, funcName, params, noReturn = True))

                        # pprint(stack.stack)
                        assert stack.isEmpty
                        pushArgs()

                    case OPCode.SYSCALL.opcode:
                        catalog     = stack.Const(inst.operands[0])
                        cmd         = stack.Const(inst.operands[1])
                        paramCount  = inst.operands[2].value
                        params      = []
                        for i in range(1, paramCount + 1):
                            p = stack.getAt(-i)
                            if p.inst is not None:
                                p.inst.flags |= Flags.FormatIgnore
                            params.append(p)

                        nextInst = getNextInst()
                        if paramCount != 0 and nextInst:
                            if nextInst.opcode == OPCode.POP.opcode:
                                popCount = nextInst.operands[0].value // 4
                                if popCount > paramCount:
                                    popCount -= paramCount
                                    popCount *= 4

                                else:
                                    popCount = 0

                            elif nextInst.opcode == OPCode.POPN.opcode:
                                popCount = nextInst.operands[0].value
                                if popCount > paramCount:
                                    popCount -= paramCount

                                else:
                                    popCount = 0

                            else:
                                raise NotImplementedError

                            if popCount != 0:
                                nextInst.operands[0].value = popCount
                            else:
                                ignoredInsts.add(index + 1)

                            [stack.pop() for _ in range(paramCount)]

                        instructions.addMLIL(MediumLevelILSyscall(catalog, cmd, params))

                    case OPCode.LOAD_GLOBAL.opcode:
                        g = stack.Global(inst.operands[0].value)
                        g.name = self.parser.getGlobalVarName(g.value)
                        v = stack.SetVar(g)
                        v.inst = inst
                        instructions.addMLIL(MediumLevelILLoadGlobalVar(v, g))

                    case OPCode.SET_GLOBAL.opcode:
                        v = stack.pop()
                        g = stack.Global(inst.operands[0].value)
                        g.name = self.parser.getGlobalVarName(g.value)
                        instructions.addMLIL(MediumLevelILSetGlobalVar(g, v))

                    case _:
                        raise NotImplementedError(f'{bb.name}:{index}@{currentLineno} {inst.descriptor} {inst.operands}')

            if overwriteInstructions:
                bb.instructions = instructions.instructions

