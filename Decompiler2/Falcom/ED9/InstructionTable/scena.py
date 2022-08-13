from Falcom.Common  import *
from Assembler      import *
from .types         import *
import struct

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

def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED9OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)

def Handler_00(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            fs = ctx.disasmContext.fs
            inst = ctx.instruction

            size = peekByte(ctx)
            assert size == 4

            inst.operands = readAllOperands(ctx, 'BL')[1:]
            value = inst.operands[0].value
            type = value >> 30

            match type:
                case ED9OperandValueType.Undefined:
                    applyDescriptorsToOperands(inst.operands, 'L')

                case ED9OperandValueType.Integer:
                    value = (value << 2) & 0xFFFFFFFF
                    sign = 0xC0000000 if value & 0x80000000 != 0 else 0
                    value = int.from_bytes((sign | (value >> 2)).to_bytes(4, 'little'), 'little', signed = True)
                    inst.operands[0].value = value
                    fmt = 'i'
                    if value in [65534, 65510]:
                        fmt = 'W'

                    applyDescriptorsToOperands(inst.operands, fmt)

                case ED9OperandValueType.Float:
                    inst.operands[0].value = struct.unpack('f', ((value << 2) & 0xFFFFFFFF).to_bytes(4, 'little'))[0]
                    applyDescriptorsToOperands(inst.operands, 'f')

                case ED9OperandValueType.String:
                    with fs.PositionSaver:
                        fs.Position = value & 0x3FFFFFFF
                        inst.operands[0].value = fs.ReadMultiByte()

                    applyDescriptorsToOperands(inst.operands, 'S')

            return inst

        case HandlerAction.Assemble:
            raise

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)


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
    inst(0x09,  'LOAD_RETURN_VALUE',                'C'),
    inst(0x0A,  'SET_RETURN_VALUE',                 'C'),                                               # return pop TOS
    inst(0x0B,  'JMP',                              'O',                    Flags.EndBlock),
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
    inst(0x17,  'GTR'),                                                                                 # TOS = TOS1 > TOS
    inst(0x18,  'GTE'),                                                                                 # TOS = TOS1 >= TOS
    inst(0x19,  'LE'),                                                                                  # TOS = TOS1 < TOS
    inst(0x1A,  'LEQ'),                                                                                 # TOS = TOS1 <= TOS
    inst(0x1B,  'BITWISE_AND'),                                                                         # TOS = TOS1 & TOS
    inst(0x1C,  'BITWISE_OR'),                                                                          # TOS = TOS1 | TOS
    inst(0x1D,  'LOGICAL_AND'),                                                                         # TOS = TOS1 && TOS
    inst(0x1E,  'LOGICAL_OR'),                                                                          # TOS = TOS1 || TOS
    inst(0x1F,  'NEG'),                                                                                 # TOS = -TOS
    inst(0x20,  'EZ'),                                                                                  # TOS = TOS == 0
    inst(0x21,  'NOT'),                                                                                 # TOS = -TOS
    inst(0x22,  'CALL_MODULE_FUNC',                 'LLC'),                                             # CALL_MODULE_FUNC('module', 'func', argCount)
    inst(0x23,  'CALL_MODULE_FUNC_DEFER',           'LLC'),                                             # CALL_MODULE_FUNC_WITH_STACK('module', 'func', argCount)
    inst(0x24,  'SYSCALL',                          'CBB'),                                             # SYSCALL(cmd1, cmd2, cmd3)
    inst(0x25,  'PUSH_CALLER_CONTEXT',              'O'),                                               # PUSH(funcIndex, retAddr, currScript, 0xF0000000)
    inst(0x26,  'DEBUG_SET_LINENO',                 'H',                    Flags.FormatIgnore),
    inst(0x27,  'POPN',                             'C'),                                               # POP N values
    inst(0x28,  'DEBUG_LOG',                        'L'),                                               # DEBUG_LOG('msg')

    # pseudo-instruction
])

del inst
