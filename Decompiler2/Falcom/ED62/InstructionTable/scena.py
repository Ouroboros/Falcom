from Falcom.Common  import *
from Assembler      import *
from .types         import *
from Falcom.ED6.InstructionTable import ED6InstructionTable, ScenaOpTable as ED6ScenaOpTable

__all__ = (
    'ScenaOpTable',
    'ED62InstructionTable',
    'ED62OperandType',
    'ED62OperandFormat',
    'ED62OperandDescriptor',
    'ScenaExpression',
    'TextCtrlCode',
)

NoOperand = InstructionDescriptor.NoOperand

class ED62InstructionTable(ED6InstructionTable):
    pass

    # def update(self, descriptors: List[InstructionDescriptor]) -> 'ED62InstructionTable':
    #     ret = super().update(descriptors)
    #     for instdesc in ret.descTable.values():
    #         if not instdesc.operands:
    #             continue

    #         instdesc.operands = list(instdesc.operands)
    #         for i, opr in enumerate(instdesc.operands):
    #             if opr.format.type == ED62OperandType.Offset:
    #                 instdesc.operands[i] = ED62OperandDescriptor(ED62OperandFormat(ED62OperandType.Offset))

    #         instdesc.operands = tuple(instdesc.operands)

    #     return ret

    # def readOperand(self, context: InstructionHandlerContext, desc: ED62OperandDescriptor) -> Operand:
    #     opr = super().readOperand(context, desc)
    #     if desc.format.type == ED62OperandType.Offset:
    #         print(desc.readValue)
    #         ibp()

    #     return opr


def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED62OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)

def Handler_37(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BB' + {
            0x7F: 'B',
            0x80: 'B',
            0x81: 'B',
            0x82: 'B',
            0x83: 'B',
            0x84: 'B',
            0x85: 'B',
            0x86: 'B',
            0x87: 'B',
        }.get(n, '')

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekBytes(ctx, 2)[-1]))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_C9(ctx: InstructionHandlerContext):
    MAX_PARAM_COUNT = 0x20

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            fs = ctx.disasmContext.fs

            inst.operands = readAllOperands(ctx, 'BB')
            inst.operands.extend(readAllOperands(ctx, 'W' * inst.operands[1].value))

            with fs.PositionSaver:
                count = len(fs.Read(MAX_PARAM_COUNT * 2).split(b'\xFF\xFF')[0]) // 2
                count += count != MAX_PARAM_COUNT

            inst.operands.extend(readAllOperands(ctx, 'W' * min(count, MAX_PARAM_COUNT)))
            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            desc = inst.descriptor

            ctrlcode, params1, params2 = inst.operands

            inst.operands = [
                ctrlcode,
                Operand(value = len(params1.value)),
                *[Operand(value = v) for v in params1.value],
                *[Operand(value = v) for v in params2.value],
            ]

            applyDescriptors(ctx, 'BB' + len(params1.value) * 'W' + min(len(params2.value), MAX_PARAM_COUNT) * 'W')
            return

        case HandlerAction.Format:
            inst = ctx.instruction
            desc = inst.descriptor
            operands = inst.operands

            def formatOperand(opr: Operand):
                return ctx.instructionTable.formatOperand(handlers.FormatOperandHandlerContext(inst, opr, formatter = ctx.formatter))

            count = operands[1].value

            f = [
                f'{desc.mnemonic}(',
                f'{DefaultIndent}{formatOperand(operands[0])},',
                f'{DefaultIndent}(',
                *[f'{DefaultIndent * 2}{formatOperand(opr)},'.rstrip() for opr in operands[2:2 + count]],
                f'{DefaultIndent}),',

                f'{DefaultIndent}(',
                *[f'{DefaultIndent * 2}{formatOperand(opr)},'.rstrip() for opr in operands[2 + count:]],
                f'{DefaultIndent}),',
                ')',
            ]

            inst.flags |= Flags.FormatMultiLine

            return f

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
    from Falcom.ED6.InstructionTable.scena import genHandler

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
        operands = ED62OperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)


desc_98 = 'B', {
    0x00: 'W',
    0x01: 'LLL',
    0x02: 'WLB',
}

desc_CC = 'BB', {
    0x00: 'WWB',
    0x01: 'S',
    0x02: '',
}

desc_D9 = 'B', {
    0x00: 'S',
    0x01: '',
}

ScenaOpTable = ED62InstructionTable(ED6ScenaOpTable).update([
    inst(0x14,  'OP_14',                        'LLLBL'),
    inst(0x15,  'OP_15',                        'L'),
    inst(0x18,  'OP_18',                        'BBB'),
    inst(0x2D,  'FormationAddMember',           'BBB'),
    inst(0x37,  'OP_37',                        NoOperand,              handler = Handler_37),
    inst(0x40,  'OP_40',                        'WB'),
    inst(0x41,  'OP_41',                        'BWB'),
    inst(0x57,  'OP_57',                        'WWWS'),
    inst(0x7D,  'OP_7D',                        'BWWW'),
    inst(0x98,  'OP_98',                        desc_98),
    inst(0xB3,  'PlayMovie',                    'BSWW'),
    inst(0xB5,  'OP_B5',                        'B'),
    inst(0xB6,  'OP_B6',                        'WB'),
    inst(0xB7,  'OP_B7',                        'B'),
    inst(0xB8,  'OP_B8',                        'WW'),
    inst(0xB9,  'OP_B9',                        'BW'),
    inst(0xBA,  'OP_BA',                        'BB'),
    inst(0xBB,  'OP_BB',                        'BBL'),
    inst(0xBC,  'OP_BC',                        'BBW'),
    inst(0xBD,  'OP_BD'),
    inst(0xBE,  'OP_BE',                        'BBWWWBiiiiii'),
    inst(0xBF,  'OP_BF',                        'BBHH'),
    inst(0xC0,  'OP_C0',                        'BLLLLLLLL'),
    inst(0xC1,  'OP_C1',                        'BBL'),
    inst(0xC2,  'OP_C2'),
    inst(0xC3,  'OP_C3',                        'W'),
    inst(0xC4,  'OP_C4',                        'BL'),
    inst(0xC5,  'OP_C5',                        'BWWWWWWWWWWWWLBS'),
    inst(0xC6,  'OP_C6',                        'BBiii'),
    inst(0xC7,  'OP_C7',                        'BBB'),
    inst(0xC8,  'OP_C8',                        'WWSBW'),
    inst(0xC9,  'OP_C9',                        NoOperand,              handler = Handler_C9, parameters = ('mandatory', 'members')),      # character selection
    inst(0xCA,  'OP_CA',                        'BBL'),
    inst(0xCB,  'OP_CB',                        'B'),
    inst(0xCC,  'OP_CC',                        desc_CC),
    inst(0xCD,  'OP_CD',                        'W'),
    inst(0xCE,  'OP_CE',                        'BE'),
    inst(0xCF,  'OP_CF',                        'WBS'),
    inst(0xD0,  'OP_D0',                        'ii'),
    inst(0xD1,  'OP_D1',                        'hiiii'),
    inst(0xD2,  'OP_D2',                        'LLB'),
    inst(0xD3,  'OP_D3',                        'B'),
    inst(0xD4,  'OP_D4',                        'BB'),
    inst(0xD5,  'OP_D5',                        'BB'),
    inst(0xD6,  'OP_D6',                        'B'),
    inst(0xD7,  'OP_D7',                        'Bih'),
    inst(0xD8,  'OP_D8',                        'BW'),
    inst(0xD9,  'OP_D9',                        desc_D9),
    inst(0xDA,  'OP_DA'),
    inst(0xDB,  'OP_DB'),
    inst(0xDC,  'OP_DC'),
    inst(0xDD,  'OP_DD'),
    inst(0xDE,  'OP_DE',                        'S'),
    inst(0xDF,  'OP_DF',                        'S'),
    inst(0xE0,  'OP_E0',                        'B' * 13),
    inst(0xE1,  'OP_E1',                        'B' * 2),
    inst(0xE2,  'OP_E2',                        'B' * 3),
    inst(0xE3,  'OP_E3',                        'B' * 4),
    inst(0xE4,  'OP_E4',                        'B' * 3),
    inst(0xE5,  'OP_E5',                        'B' * 3),
    inst(0xE6,  'OP_E6',                        'B' * 1),
    inst(0xE7,  'OP_E7',                        'BSBL'),
    inst(0xE8,  'OP_E8',                        'B' * 4),
    inst(0xE9,  'OP_E9',                        'B' * 1),
    inst(0xEA,  'OP_EA',                        'B' * 4),
    inst(0xEB,  'OP_EB',                        'B' * 2),
])

del inst
