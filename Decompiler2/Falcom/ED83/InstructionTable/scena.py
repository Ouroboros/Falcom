from enum import Flag
from Falcom.Common  import *
from Assembler      import *
from .types         import *
from pprint import pprint

__all__ = (
    'ScenaOpTable',
    'ED83InstructionTable',
    'ED83OperandType',
    'ED83OperandFormat',
    'ED83OperandDescriptor'
)

NoOperand = InstructionDescriptor.NoOperand

class ED83InstructionTable(InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        return fs.ReadByte()

    def writeOpCode(self, fs: fileio.FileStream, opcode: int):
        fs.WriteByte(opcode)

    def readOperand(self, context: InstructionHandlerContext, desc: ED83OperandDescriptor) -> Operand:
        opr = super().readOperand(context, desc)
        if desc.format.type == ED83OperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, context: InstructionHandlerContext, operand: Operand):
        match operand.descriptor.type:
            case ED83OperandType.Offset:
                fs = context.disasmContext.fs
                pos = fs.Position
                log.debug(f'xref {repr(operand.value)} at 0x{pos:08X}')
                context.addXRef(operand.value, pos)

        super().writeOperand(context, operand)

    def writeAllOperands(self, context: InstructionHandlerContext, operands: List[Operand]):
        return super().writeAllOperands(context, operands)

def genVariadicParamStub(desc: InstructionDescriptor) -> List[str]:
    return [
        f'def {desc.mnemonic}(n: int, *args):',
        f'    # 0x{desc.opcode:02X}',
        f'    return scena.handleOpCode(0x{desc.opcode:02X}, n, *args)',
        '',
    ]

def genArgsStub(desc: InstructionDescriptor) -> List[str]:
    return [
        f'def {desc.mnemonic}(*args):',
        f'    # 0x{desc.opcode:02X}',
        f'    return scena.handleOpCode(0x{desc.opcode:02X}, *args)',
        '',
    ]

def peekByte(ctx: InstructionHandlerContext) -> int:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.ReadByte()

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    return ctx.instructionTable.readAllOperands(ctx, ED83OperandDescriptor.fromFormatString(fmts))

def ScriptThread_getFunctionStrWorkValue(ctx: InstructionHandlerContext) -> List[Operand]:
    n = peekByte(ctx)

    {
        0x11: '',
        0x22: '',
        0x33: '',
        0x44: '',
    }

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED83OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def Handler_Switch(ctx: InstructionHandlerContext):
    SWITCH_DEFAULT = -1
    '''
        Switch(
            (
                ('Exp23', 0xF7),
                'Return',
            ),
            (1, 'loc_28D4'),
            (2, 'loc_28E4'),
            (-1, 'loc_28F4'),
        )
    '''

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            expr = readAllOperands(ctx, 'E')[0]
            count = readAllOperands(ctx, 'B')[0]
            cases = [readAllOperands(ctx, 'IO') for _ in range(count.value)]
            default = readAllOperands(ctx, 'O')[0]

            inst.operands = [expr, cases, default]
            # ibp()

            return inst

        case HandlerAction.Format:
            inst = ctx.instruction
            desc = inst.descriptor
            expr, cases, default = inst.operands

            def formatOperand(opr: Operand):
                return ctx.instructionTable.formatOperand(handlers.FormatOperandHandlerContext(inst, opr))

            f = [
                f'{desc.mnemonic}(',
                f'{DefaultIndent}(',
                *[f'{DefaultIndent * 2}{opr},'.rstrip() for opr in formatOperand(expr)],
                f'{DefaultIndent}),',

                *[f'{DefaultIndent}({id.value}, {formatOperand(o)}),' for id, o in cases],
                f'{DefaultIndent}({SWITCH_DEFAULT}, {formatOperand(default)}),',
            ]

            f.append(')')

            return f

        case HandlerAction.Assemble:
            inst = ctx.instruction
            expr = inst.operands[0]
            cases = inst.operands[1:]
            count = len(cases) - 1

            operands = [
                expr,
                Operand(value = count),
            ]

            default = None
            for c in cases:
                index, offset = c.value
                if index == SWITCH_DEFAULT:
                    if default is not None:
                        raise ValueError('multiple default cases')

                    default = offset

                else:
                    operands.extend([
                        Operand(value = index),
                        Operand(value = offset),
                    ])

            operands.append(Operand(value = default))
            inst.operands = operands

            fmts = 'EB' + 'IO' * count + 'O'

            applyDescriptors(ctx, fmts)

            return

        case HandlerAction.CodeGen:
            return genArgsStub(ctx.descriptor)

def Handler_29(ctx: InstructionHandlerContext):
    def getfmt(n):
        match n:
            case 0x00:
                fmt = 'WfL'

            case 0x01:
                fmt = 'Si'

            case 0x02:
                fmt = 'BWWB'

            case 0x03:
                fmt = ''

            case 0x04:
                fmt = 'B'

            case _:
                raise NotImplementedError(f'0x{n:X}')

        return 'BB' + fmt

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmt(n))

            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmt(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

def Handler_3A(ctx: InstructionHandlerContext):
    fmts = {
        0: 'WfWLB',
        1: 'WB',
        2: 'B',
        3: 'fWB',
        4: 'WfWLB',
        5: 'WW',
        6: 'W',
        7: '',
        8: 'WB',
        9: 'B',
    }

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, 'B' + fmts[n])

            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, 'B' + fmts[ctx.instruction.operands[0].value])
            return

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

def Handler_3B(ctx: InstructionHandlerContext):
    def getfmt(n):
        match n:
            case 0x64:
                fmt = 'Iff'

            case _:
                raise NotImplementedError(f'n: 0x{n:X}')

        return 'B' + fmt

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmt(n))

            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmt(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

def Handler_7C(ctx: InstructionHandlerContext):
    fmts = {
        0x00: 'BWWWWWWW',
        0x01: '',
    }

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, 'B' + fmts[n])
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, 'B' + fmts[ctx.instruction.operands[0].value])
            return

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

def Handler_9E(ctx: InstructionHandlerContext):
    fmts = {
        0x0F: 'B',
        0x10: '',
        0x11: 'HC',
        0x12: 'BB',
    }

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, 'B' + fmts[n])
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, 'B' + fmts[ctx.instruction.operands[0].value])
            return

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

def Handler_AC(ctx: InstructionHandlerContext):
    fmts = {
        0x00: '',
        0x01: 'L',
        0x02: 'L',
        0x05: 'W',
        0x06: '',
        0x07: 'W',
        0x08: '',
        0x09: 'W',
        0x0A: '',
    }

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, 'B' + fmts[n])
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, 'B' + fmts[ctx.instruction.operands[0].value])
            return

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)


def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
    if operandfmts is NoOperand:
        operands = NoOperand
        if parameters:
            raise

    else:
        operands = ED83OperandDescriptor.fromFormatString(operandfmts)
        if parameters and len(operands) != len(parameters):
            raise

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

ScenaOpTable = ED83InstructionTable([
    inst(0x00,  'ExitThread',                   NoOperand,                  Flags.EndBlock),
    inst(0x01,  'Return',                       NoOperand,                  Flags.EndBlock),
    # inst(0x02,  'Call',                         'BSB',                      Flags.StartBlock,                       parameters = ('type', 'name', 'type2')),
    inst(0x03,  'Jump',                         'O',                        Flags.Jump,                             parameters = ('label',)),
    inst(0x04,  'OP_04',                        'BS'),
    inst(0x05,  'If',                           'EO',                                                               parameters = ('ops', 'successor')),
    inst(0x06,  'Switch',                       NoOperand,                  Flags.EndBlock,     Handler_Switch),
    inst(0x10,  'SetScenaFlags',                'F',                                                                parameters = ('flags',)),
    inst(0x13,  'OP_13',                        'L'),
    inst(0x14,  'OP_14',                        'L'),
    inst(0x18,  'OP_18',                        'BE'),
    inst(0x1D,  'OP_1D',                        'HSSSBLLfffffffSSLBffW',    Flags.FormatMultiLine),
    inst(0x1E,  'OP_1E',                        'WBBS'),
    inst(0x29,  'MenuCmd',                      NoOperand,                                      handler = Handler_29),
    # inst(0x2B,  'Battle',                       ''),
    inst(0x3A,  'OP_3A',                        NoOperand,                                      handler = Handler_3A),
    inst(0x3B,  'OP_3B',                        NoOperand,                                      handler = Handler_3B),
    inst(0x7C,  'OP_7C',                        NoOperand,                                      handler = Handler_7C),
    inst(0x86,  'OP_86',                        'BWWWWWWfffS'),
    inst(0x9E,  'OP_9E',                        NoOperand,                                      handler = Handler_9E),
    inst(0xAC,  'OP_AC',                        NoOperand,                                      handler = Handler_AC),
    inst(0xB1,  'MenuChrFlagCmd',               'BWL'),
])

del inst
