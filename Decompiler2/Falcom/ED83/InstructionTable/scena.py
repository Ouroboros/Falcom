from enum import Flag
from Falcom.Common  import *
from Assembler      import *
from .types         import *

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

    def writeOpCode(self, fs: fileio.FileStream, inst: Instruction):
        fs.WriteByte(inst.opcode)

    def readOperand(self, context: InstructionHandlerContext, desc: ED83OperandDescriptor) -> ED83OperandType:
        opr = super().readOperand(context, desc)
        if desc.format.type == ED83OperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, fs: fileio.FileStream, operand: ED83OperandType):
        raise NotImplementedError

def genVariadicParamStub(desc: InstructionDescriptor) -> List[str]:
    return [
        f'def {desc.mnemonic}(n: int, *args):',
        f'    # 0x{desc.opcode:02X}',
        f'    return scena.handleOpCode(0x{desc.opcode:02X}, n, *args)',
    ]

def peekByte(ctx: InstructionHandlerContext) -> int:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.ReadByte()

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    return ctx.instructionTable.readAllOperands(ctx, ED83OperandDescriptor.fromFormatString(fmts))

def Handler_Switch(ctx: InstructionHandlerContext):
    raise NotImplementedError

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

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

    return None

def Handler_3B(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            n = peekByte(ctx)
            match n:
                case 0x64:
                    fmts = 'Iff'

                case _:
                    raise NotImplementedError(f'n: 0x{n:X}')

            inst.operands = readAllOperands(ctx, 'B' + fmts)

            return inst

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

    return None

def Handler_9E(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            n = peekByte(ctx)
            fmts = {
                0x0F: 'B',
                0x10: '',
                0x11: 'HC',
                0x12: 'BB',
            }

            inst.operands = readAllOperands(ctx, 'B' + fmts[n])

            return inst

        case HandlerAction.CodeGen:
            return genVariadicParamStub(ctx.descriptor)

    return None


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
    inst(0x02,  'Call',                         'BSB',                      Flags.StartBlock,                       parameters = ('type', 'name', 'type2')),
    inst(0x03,  'Jump',                         'o',                        Flags.Jump,                             parameters = ('label',)),
    inst(0x04,  'OP_04',                        'BS'),
    inst(0x05,  'If',                           'Eo',                                                               parameters = ('ops', 'successor')),
    inst(0x06,  'Switch',                       NoOperand,                  Flags.EndBlock,     Handler_Switch),
    inst(0x10,  'SetScenaFlags',                'F',                                                                parameters = ('flags',)),
    inst(0x13,  'OP_13',                        'L'),
    inst(0x14,  'OP_14',                        'L'),
    inst(0x1D,  'OP_1D',                        'HSSSBLLfffffffSSLBffW',    Flags.FormatMultiLine),
    inst(0x1E,  'OP_1E',                        'WBBS'),
    inst(0x2B,  'Battle',                       ''),
    inst(0x3A,  'OP_3A',                        NoOperand,                                      handler = Handler_3A),
    inst(0x3B,  'OP_3B',                        NoOperand,                                      handler = Handler_3B),
    inst(0x86,  'OP_86',                        'BWWWWWWfffS'),
    inst(0x9E,  'OP_9E',                        NoOperand,                                      handler = Handler_9E),
    inst(0xB1,  'MenuChrFlagCmd',               'BWL'),
])

del inst
