from Falcom.Common  import *
from Assembler      import *
from .types         import *

__all__ = (
    'ScenaOpTable',
    'ED9InstructionTable',
    'ED9OperandType',
    'ED9OperandFormat',
    'ED9OperandDescriptor',
)

NoOperand = InstructionDescriptor.NoOperand

class ED9InstructionTable(InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        return fs.ReadByte()

    def writeOpCode(self, fs: fileio.FileStream, opcode: int):
        fs.WriteByte(opcode)

    def readOperand(self, context: InstructionHandlerContext, desc: ED9OperandDescriptor) -> Operand:
        opr = super().readOperand(context, desc)
        if desc.format.type == ED9OperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, context: InstructionHandlerContext, operand: Operand):
        match operand.descriptor.type:
            case ED9OperandType.Offset:
                fs = context.disasmContext.fs
                pos = fs.Position
                # log.debug(f'xref {repr(operand.value)} at 0x{pos:08X}')
                context.addXRef(operand.value, pos)

        super().writeOperand(context, operand)

    def writeAllOperands(self, context: InstructionHandlerContext, operands: List[Operand]):
        return super().writeAllOperands(context, operands)

def setOpCodeByName(inst: Instruction, name: str):
    inst.descriptor = ScenaOpTable.getDescriptorByName(name)
    inst.opcode = inst.descriptor.opcode

def genHandler(b: str, fmts: Dict[int, str]) -> Callable:
    def handler(ctx: InstructionHandlerContext):
        peeker = {
            'B': peekByte,
            'H': peekWord,
            'W': peekWord,
            'N': peekWord,
        }[b[0]]

        def getfmts(n):
            return b + fmts[n]

        match ctx.action:
            case HandlerAction.Disassemble:
                inst = ctx.instruction
                inst.operands = readAllOperands(ctx, getfmts(peeker(ctx)))
                return inst

            case HandlerAction.Assemble:
                applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
                return

            case HandlerAction.CodeGen:
                types = [{
                    'B': int,
                    'C': int,
                    'W': int,
                    'H': int,
                    'N': int,
                    'L': int,
                    'S': str,
                    'V': tuple,
                }[t] for t in b]
                return genVariadicFuncStub(ctx.descriptor, *types)

    return handler

def inst(opcode: int, mnemonic: str, operandfmts: str = NoOperand, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
    if operandfmts == '':
        raise ValueError('use NoOperand instead')

    elif isinstance(operandfmts, tuple):
        handler = genHandler(*operandfmts)
        operandfmts = NoOperand

    if handler:
        assert operandfmts is NoOperand

    if operandfmts is NoOperand:
        operands = NoOperand
        if not handler and parameters:
            raise

    else:
        operands = ED9OperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

def Handler_00(ctx: InstructionHandlerContext):
    from ..Parser.scena_types import ScenaValue

    match ctx.action:
        case HandlerAction.Disassemble:
            fs = ctx.disasmContext.fs
            inst = ctx.instruction

            size = peekByte(ctx)
            assert size == 4

            inst.operands = readAllOperands(ctx, 'BV')[1:]
            # value = inst.operands[0].value
            # type = value >> 30

            match inst.operands[0].value.type:
                case ScenaValue.Type.Undefined:
                    pass

                case ScenaValue.Type.Integer:
                    setOpCodeByName(inst, 'PUSH_INT')

                case ScenaValue.Type.Float:
                    setOpCodeByName(inst, 'PUSH_FLOAT')

                case ScenaValue.Type.String:
                    setOpCodeByName(inst, 'PUSH_STR')

            return inst

        case HandlerAction.Assemble:
            raise

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

from .mediumlevelil import *

def IL_Handler(ctx: InstructionHandlerContext):
    if ctx.action != HandlerAction.Format:
        return

    from ..Parser.scena_types import ScenaVariable, ScenaValue

    def formatScenaValue(v: ScenaValue):
        match v.type:
            case ScenaValue.Type.Undefined:
                fmt = 'L'
                f = ED9OperandDescriptor.formatInteger

            case ScenaValue.Type.Integer:
                f = ED9OperandDescriptor.formatInteger

                if v.value in [0xFFFE, 0xFFE6, 0xFFFD]:
                    fmt = 'W'
                else:
                    fmt = 'i'

            case ScenaValue.Type.Float:
                f = ED9OperandDescriptor.formatFloat
                fmt = 'f'

            case ScenaValue.Type.String:
                f = ED9OperandDescriptor.formatText
                fmt = 'S'

        opr = Operand(value = v.value)
        applyDescriptorsToOperands([opr], fmt)

        return f(opr)

    def formatValue(v: ScenaVariable, *, ignoreConst = False, ignoreSetVar = False):
        if isinstance(v, ScenaVariable):
            if not ignoreConst and v.const:
                return formatValue(v.value)

            if not ignoreSetVar and v.setVar:
                return formatValue(v.value)

            if v.isReg or v.isArg:
                return v.name

            if v.loadStack:
                return v.value.name

            # if v.value is None:
            #     return v.name

            # if isinstance(v.value, ScenaVariable):
            #     if v.value.const:
            #         return formatValue(v.value)

            #     return v.value.name

            return v.name

        if isinstance(v, ScenaValue):
            return formatScenaValue(v)

        if isinstance(v, Operand):
            if not isinstance(v.value, int | float | str):
                return formatValue(v.value)

            return ED9OperandDescriptor.formatOperand(v)

        ibp()
        # raise NotImplementedError

    inst: MediumLevelILInstruction = ctx.instruction.operands

    # print(ctx.instruction.currinst)

    match inst.OpCode:
        case MLIL.NOP:
            return []

        case MLIL.SET_VAR:
            setvar: MediumLevelILSetVar = inst
            return [
                f'{setvar.dest.name} = {formatValue(setvar.src)}'
            ]

        case MLIL.DEL_VAR:
            delvar: MediumLevelILDelVar = inst
            return [
                f'del {delvar.var.name}'
            ]

        case MLIL.ADDRESS_OF:
            addrof: MediumLevelILAddressOf = inst
            return [
                f'{addrof.dest.name} = {addrof.src.address}'
            ]

        case MLIL.CALL:
            call: MediumLevelILCall = inst

            params = ', '.join([formatValue(p) for p in call.params[:-2]])    # strip caller funcid and ret addr
            retval = call.returnValue

            if retval is None:
                return [
                    f'{call.target.name}({params})',
                    '',
                ]

            else:
                return [
                    f'{retval.name} = {call.target.name}({params})',
                    '',
                ]

        case MLIL.CALL_MODULE:
            callm: MediumLevelILCallModule = inst

            retval = callm.returnValue
            params = ', '.join([formatValue(p) for p in callm.params[:-5]])    # strip funcid, retaddr, current_script * 2, 0xF0000000
            if params:
                params = ', ' + params

            if retval is None:
                return [
                    f"Call({formatValue(callm.module)}, {formatValue(callm.func)}{params})",
                    '',
                ]

            else:
                return [
                    f"{retval.name} Call('{formatValue(callm.module)}', '{formatValue(callm.func)}'{params})",
                    '',
                ]

        case MLIL.SYSCALL:
            syscall: MediumLevelILSyscall = inst
            params = ', '.join([formatValue(p.value) for p in syscall.params])    # strip caller funcid and ret addr
            if params:
                params = ', ' + params

            return [
                f'Syscall({formatValue(syscall.catalog)}, {formatValue(syscall.cmd)}{params})',
                '',
            ]

        case MLIL.GET_REG:
            getreg: MediumLevelILGetReg = inst
            return [
                f'{getreg.value.name} = GetReg({getreg.regid})',
            ]

        case MLIL.SET_REG:
            setreg: MediumLevelILSetReg = inst
            return [
                f'SetReg({setreg.regid}, {setreg.value.name})',
            ]

        case MLIL.RET:
            # ret: MediumLevelILRet = inst
            return ['Return()']

        case MLIL.JMP_IF_ZERO:
            jz: MediumLevelILJmpIfZero = inst

            ctx.instruction.flags |= Flags.FormatNewLine
            return [
                f"JmpIfZero({jz.var.name}, '{jz.target.value.name}')"
            ]

        case MLIL.JMP_IF_NOT_ZERO:
            jnz: MediumLevelILJmpIfNotZero = inst

            ctx.instruction.flags |= Flags.FormatNewLine
            return [
                f"JmpIfNotZero({jnz.var.name}, '{jnz.target.value.name}')"
            ]

        case MLIL.ADD:
            inst_add: MediumLevelILAdd = inst
            return [f'{inst_add.left.name} = {inst_add.left.name} + {inst_add.right.name}']

        case MLIL.SUB:
            inst_sub: MediumLevelILSub = inst
            return [f'{inst_sub.left.name} = {inst_sub.left.name} - {inst_sub.right.name}']

        case MLIL.MUL:
            inst_mul: MediumLevelILMul = inst
            return [f'{inst_mul.left.name} = {inst_mul.left.name} * {inst_mul.right.name}']

        case MLIL.DIVS:
            inst_divs: MediumLevelILDiv = inst
            return [f'{inst_divs.left.name} = {inst_divs.left.name} // {inst_divs.right.name}']

        case MLIL.MODS:
            inst_mods: MediumLevelILMod = inst
            return [f'{inst_mods.left.name} = {inst_mods.left.name} % {inst_mods.right.name}']

        case MLIL.NEG:
            neg: MediumLevelILNeg = inst
            return [
                f'{neg.var.name} = {neg.var.name} == 0',
            ]

        case MLIL.NOT:
            inst_not: MediumLevelILNot = inst
            return [
                f'{inst_not.var.name} = {inst_not.var.name} == 0',
            ]

        case MLIL.CMP_EZ:
            ez: MediumLevelILCmpEZ = inst
            return [
                f'{ez.var.name} = {ez.var.name} == 0',
            ]

        case MLIL.CMP_EQ:
            eq: MediumLevelILCmpEQ = inst
            return [
                f'{eq.left.name} = {eq.left.name} == {eq.right.name}',
            ]

        case MLIL.CMP_NE:
            ne: MediumLevelILCmpNE = inst
            return [
                f'{ne.left.name} = {ne.left.name} != {ne.right.name}',
            ]

        case MLIL.CMP_LT:
            lt: MediumLevelILCmpLT = inst
            return [
                f'{lt.left.name} = {lt.left.name} < {lt.right.name}',
            ]

        case MLIL.CMP_LE:
            le: MediumLevelILCmpLE = inst
            return [
                f'{le.left.name} = {le.left.name} <= {le.right.name}',
            ]

        case MLIL.CMP_GT:
            gt: MediumLevelILCmpGT = inst
            return [
                f'{gt.left.name} = {gt.left.name} > {gt.right.name}',
            ]

        case MLIL.CMP_GE:
            ge: MediumLevelILCmpGE = inst
            return [
                f'{ge.left.name} = {ge.left.name} >= {ge.right.name}',
            ]

        case MLIL.OR:
            inst_or: MediumLevelILOr = inst
            return [
                f'{inst_or.left.name} = {inst_or.left.name} | {inst_or.right.name}',
            ]

        case MLIL.AND:
            inst_and: MediumLevelILAnd = inst
            return [
                f'{inst_and.left.name} = {inst_and.left.name} & {inst_and.right.name}',
            ]

        case MLIL.LOGICAL_OR:
            inst: MediumLevelILLogicalOr

            tos1, tos = inst.left, inst.right

            return [
                f'{tos1.name} = LogicalOr({tos1.name}, {tos.name})',
            ]

        case MLIL.LOGICAL_AND:
            inst: MediumLevelILLogicalAnd

            tos1, tos = inst.left, inst.right

            return [
                f'{tos1.name} = LogicalAnd({tos1.name}, {tos.name})',
            ]

    raise NotImplementedError(f'{inst}')

ScenaOpTable = ED9InstructionTable([
    inst(0x00,  'PUSH',                             handler = Handler_00),
    inst(0x01,  'POP',                              'C'),
    inst(0x02,  'LOAD_STACK',                       'i'),
    inst(0x03,  'LOAD_STACK_DEREF',                 'i'),
    inst(0x04,  'PUSH_STACK_OFFSET',                'i'),
    inst(0x05,  'POP_TO',                           'i'),
    inst(0x06,  'POP_TO_DEREF',                     'i'),
    inst(0x07,  'LOAD_GLOBAL',                      'i'),
    inst(0x08,  'SET_GLOBAL',                       'i'),
    inst(0x09,  'GET_REG',                          'C'),                                               # push regs[regid]
    inst(0x0A,  'SET_REG',                          'C'),                                               # regs[regid] = TOS
    inst(0x0B,  'JMP',                              'O',                    Flags.Jump),
    inst(0x0C,  'CALL',                             'F',                    Flags.FormatNewLine),
    inst(0x0D,  'RETURN',                           NoOperand,              Flags.EndBlock),
    inst(0x0E,  'POP_JMP_NOT_ZERO',                 'O',                    Flags.FormatNewLine),
    inst(0x0F,  'POP_JMP_ZERO',                     'O',                    Flags.FormatNewLine),
    inst(0x10,  'ADD'),                                                                                 # TOS = TOS1 + TOS
    inst(0x11,  'SUB'),                                                                                 # TOS = TOS1 - TOS
    inst(0x12,  'MUL'),                                                                                 # TOS = TOS1 * TOS
    inst(0x13,  'DIV'),                                                                                 # TOS = TOS1 / TOS
    inst(0x14,  'MOD'),                                                                                 # TOS = TOS1 % TOS
    inst(0x15,  'EQ'),                                                                                  # TOS = TOS1 == TOS
    inst(0x16,  'NE'),                                                                                  # TOS = TOS1 != TOS
    inst(0x17,  'GT'),                                                                                  # TOS = TOS1 > TOS
    inst(0x18,  'GE'),                                                                                  # TOS = TOS1 >= TOS
    inst(0x19,  'LT'),                                                                                  # TOS = TOS1 < TOS
    inst(0x1A,  'LE'),                                                                                  # TOS = TOS1 <= TOS
    inst(0x1B,  'BITWISE_AND'),                                                                         # TOS = TOS1 & TOS
    inst(0x1C,  'BITWISE_OR'),                                                                          # TOS = TOS1 | TOS
    inst(0x1D,  'LOGICAL_AND'),                                                                         # TOS = TOS1 && TOS
    inst(0x1E,  'LOGICAL_OR'),                                                                          # TOS = TOS1 || TOS
    inst(0x1F,  'NEG'),                                                                                 # TOS = -TOS
    inst(0x20,  'EZ'),                                                                                  # TOS = TOS == 0
    inst(0x21,  'NOT'),                                                                                 # TOS = ~TOS
    inst(0x22,  'CALL_MODULE_FUNC',                 'VVC'),                                             # CALL_MODULE_FUNC('module', 'func', argCount)
    inst(0x23,  'CALL_MODULE_FUNC_DEFER',           'VVC'),                                             # CALL_MODULE_FUNC_WITH_STACK('module', 'func', argCount)
    inst(0x24,  'SYSCALL',                          'CBB'),                                             # SYSCALL(catalog, cmd, argCount)
    inst(0x25,  'PUSH_CALLER_CONTEXT',              'O'),                                               # PUSH(funcIndex, retAddr, currScript, 0xF0000000)
    inst(0x26,  'DEBUG_SET_LINENO',                 'H',                    Flags.FormatIgnore),
    inst(0x27,  'POPN',                             'C'),                                               # POP N values
    inst(0x28,  'DEBUG_LOG',                        'L'),                                               # DEBUG_LOG('msg')

    # pseudo-instruction
    inst(0x1000,  'PUSH_INT',                       'i'),
    inst(0x1001,  'PUSH_FLOAT',                     'f'),
    inst(0x1002,  'PUSH_STR',                       'S'),
    inst(0x1003,  'PUSH_FUNC_ID',                   'F'),
    inst(0x1004,  'PUSH_RET_ADDR',                  'O'),

    # binary ninja style MLIL

    inst(0x5000,  'MLIL_STUB',                      handler = IL_Handler),
])

del inst
