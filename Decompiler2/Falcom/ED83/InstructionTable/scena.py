from Falcom.Common  import *
from Assembler      import *
from .types         import *
from pprint import pprint

__all__ = (
    'ScenaOpTable',
    'ED83InstructionTable',
    'ED83OperandType',
    'ED83OperandFormat',
    'ED83OperandDescriptor',
    'ScenaExpression',
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

            case ED83OperandType.ThreadValue:
                threadId = operand.value[0]
                fmts = ScriptThread_getFunctionStrWorkValue(threadId)
                oprs = [Operand(value = v) for v in operand.value]
                applyDescriptorsToOperands(oprs, fmts)
                self.writeAllOperands(context, oprs)
                return

        super().writeOperand(context, operand)

    def writeAllOperands(self, context: InstructionHandlerContext, operands: List[Operand]):
        return super().writeAllOperands(context, operands)

def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED83OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)

def Handler_Call(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            oprs = readAllOperands(ctx, 'BSB')
            inst.operands = oprs
            if oprs[-1].value != 0:
                inst.operands.extend(readAllOperands(ctx, 'V'))

            return inst

        case HandlerAction.Assemble:
            fmts = 'BSB'
            if ctx.instruction.operands[2].value != 0:
                fmts += 'V'

            applyDescriptors(ctx, fmts)
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, str, int, parameters = ctx.descriptor.parameters)

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
            return genVariadicFuncStub(ctx.descriptor)

def Handler_23(ctx: InstructionHandlerContext):
    def getfmt(n):
        return 'B' + {
            0x00: 'WWWWB',
            0x01: 'WWBB',
            0x02: 'WW',
            0x05: 'WWWWB',
        }[n]

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
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_MenuCmd(ctx: InstructionHandlerContext):
    def getfmt(n):
        return 'BB' + {
            0x00: 'WfL',
            0x01: 'SL',
            0x02: 'BWWB',
            0x03: '',
            0x04: 'B',
            # 0x05: 'WL',
            # 0x06: 'W',
            # 0x07: 'W',
            0x08: 'SLVV',
            # 0x09: 'SV',
            # 0x0A: '',
            # 0x0B: 'V',
            # 0x0C: 'W',
            # 0x0D: 'L',
            # 0x0E: 'L',
            # 0x0F: '',
            0x10: '',
        }[n]

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
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_3A(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
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
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))

            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_3B(ctx: InstructionHandlerContext):
    def getfmt(n):
        return 'B' + {
            0x64: 'Iff',
        }[n]

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
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_43(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: 'fW',
            # 0x05: '',
            # 0x06: '',
            # 0x0A: '',
            # 0x0B: '',
            # 0x0C: '',
            # 0x69: '',
            # 0x6A: '',
            # 0xFE: '',
            0xFF: 'W',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_49(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'W',
            0x01: 'W',
            0x04: 'W',
            0x05: 'W',
            0x06: 'W',
            0x08: 'WffB',
            0x09: 'W',
            0x0A: 'W',
            0x0B: 'W',
            0x0C: 'WW',
            0x0D: 'W' * 0x18,
            0x0E: 'B',
            0x0F: 'B',
            0x11: 'W',
            0x17: 'WW',

            0x02: '',
            0x03: '',
            0x07: '',
            0x10: '',
            0x12: '',
            0x13: '',
            0x14: '',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_72(ctx: InstructionHandlerContext):
    def getfmt(n1, n2):
        return {
            0x00: '',
            0x01: 'WB',
            0x02: 'WB',
            0x03: 'BB',
            0x04: 'BB',
            0x06: 'W' if n1 < 0x100 else '',
            0x07: '',
        }[n2]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            oprs = readAllOperands(ctx, 'WB')
            fmts = getfmt(oprs[0].value, oprs[1].value)
            inst.operands = [*oprs, *readAllOperands(ctx, fmts)]
            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            oprs = inst.operands
            applyDescriptors(ctx, 'WB' + getfmt(oprs[0].value, oprs[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_74(ctx: InstructionHandlerContext):
    def getfmt(n):
        return 'WB' + {
            0x00: 'L',
            # 0x01: '',
            # 0x02: 'WfWWSf',
            # 0x03: 'SfWWSf',
            # 0x04: '',
            # 0x14: 'L',
            # 0x15: '',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekBytes(ctx, 3)[-1]
            inst.operands = readAllOperands(ctx, getfmt(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmt(ctx.instruction.operands[2].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_75(ctx: InstructionHandlerContext):
    def getfmt(n):
        return 'BB' + {
            0x00: 'WLL',
            0x01: 'SL',
            0x02: 'BWWB',
            0x03: '',
            0x04: 'B',
            0x05: 'WL',
            0x06: 'W',
            0x07: 'W',
        }[n]

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
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_7C(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'BWWWWWWW',
            0x01: '',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_9C(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'BWWL',
            0x01: '',
            0x02: 'W',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_9E(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x0F: 'B',
            0x10: '',
            0x11: 'HC',
            0x12: 'BB',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_AC(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: '',
            0x01: 'L',
            0x02: 'L',
            0x05: 'W',
            0x06: '',
            0x07: 'W',
            0x08: '',
            0x09: 'W',
            0x0A: '',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)


def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
    if handler:
        assert operandfmts is NoOperand

    if operandfmts is NoOperand:
        operands = NoOperand
        if not handler and parameters:
            raise

    else:
        operands = ED83OperandDescriptor.fromFormatString(operandfmts)
        if parameters and len(operands) != len(parameters):
            raise

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

ScenaOpTable = ED83InstructionTable([
    inst(0x00,  'ExitThread',                   NoOperand,                  Flags.EndBlock),
    inst(0x01,  'Return',                       NoOperand,                  Flags.EndBlock),
    inst(0x02,  'Call',                         NoOperand,                  Flags.Empty,        Handler_Call,       parameters = ('type', 'name', 'type2')),
    inst(0x03,  'Jump',                         'O',                        Flags.Jump,                             parameters = ('label',)),
    inst(0x04,  'OP_04',                        'BS'),
    inst(0x05,  'If',                           'EO',                                                               parameters = ('ops', 'successor')),
    inst(0x06,  'Switch',                       NoOperand,                  Flags.EndBlock,     Handler_Switch),
    inst(0x0A,  'OP_0A',                        'BE'),
    inst(0x0C,  'OP_0C',                        'BB'),
    inst(0x0E,  'OP_0E',                        'BBB'),
    inst(0x10,  'SetScenaFlags',                'F',                                                                parameters = ('flags',)),
    inst(0x11,  'OP_11',                        'W'),
    inst(0x12,  'OP_12',                        'W'),
    inst(0x13,  'OP_13',                        'L'),
    inst(0x14,  'OP_14',                        'L'),
    inst(0x16,  'OP_16',                        'W'),
    inst(0x18,  'OP_18',                        'BE'),
    inst(0x1D,  'OP_1D',                        'HSSSBLLfffffffSSLBffW',    Flags.FormatMultiLine),
    inst(0x1E,  'OP_1E',                        'WBBS'),
    inst(0x20,  'OP_20',                        'BVVV'),
    inst(0x22,  'Talk',                         'WT',                                                               parameters = ('chrId', 'text')),
    inst(0x23,  'OP_23',                        NoOperand,                                      handler = Handler_23),
    inst(0x24,  'OP_24',                        'WLT'),
    inst(0x25,  'OP_25',                        'B'),
    inst(0x26,  'OP_26',                        NoOperand),
    inst(0x28,  'OP_28',                        'VVB'),
    inst(0x29,  'MenuCmd',                      NoOperand,                                      handler = Handler_MenuCmd),
    # inst(0x2B,  'Battle',                       ''),
    inst(0x38,  'OP_38',                        'WBBS'),
    inst(0x3A,  'OP_3A',                        NoOperand,                                      handler = Handler_3A),
    inst(0x3B,  'OP_3B',                        NoOperand,                                      handler = Handler_3B),
    inst(0x43,  'OP_43',                        NoOperand,                                      handler = Handler_43),
    inst(0x49,  'OP_49',                        NoOperand,                                      handler = Handler_49),
    inst(0x55,  'OP_55',                        'BWWWWWWWWWWffffBBSS'),
    inst(0x56,  'OP_56',                        'BBBfffff'),
    inst(0x57,  'OP_57',                        'BB'),
    inst(0x58,  'OP_58',                        'B'),
    inst(0x5A,  'OP_5A',                        'WWSBBB'),
    inst(0x62,  'OP_62',                        ''),
    inst(0x6B,  'OP_6B',                        'BWWfLL'),
    inst(0x6F,  'OP_6F',                        'BWL'),
    inst(0x72,  'QuestInfo',                    NoOperand,                                      handler = Handler_72),
    inst(0x74,  'OP_74',                        NoOperand,                                      handler = Handler_74),
    inst(0x75,  'OP_75',                        NoOperand,                                      handler = Handler_75),
    inst(0x7C,  'OP_7C',                        NoOperand,                                      handler = Handler_7C),
    inst(0x86,  'OP_86',                        'BWWWWWWfffS'),
    inst(0x87,  'OP_87',                        'BL'),
    inst(0x88,  'OP_88',                        'W'),
    inst(0x9C,  'OP_9C',                        NoOperand,                                      handler = Handler_9C),
    inst(0x9E,  'OP_9E',                        NoOperand,                                      handler = Handler_9E),
    inst(0xAC,  'OP_AC',                        NoOperand,                                      handler = Handler_AC),
    inst(0xB1,  'MenuChrFlagCmd',               'BWL'),
    inst(0xC2,  'OP_C2',                        'B'),
])

del inst
