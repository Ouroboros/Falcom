from Falcom.Common  import *
from Assembler      import *
from .types         import *

__all__ = (
    'ScenaOpTable',
    'ED6InstructionTable',
    'ED6OperandType',
    'ED6OperandFormat',
    'ED6OperandDescriptor',
    'ScenaExpression',
    'TextCtrlCode',
)

NoOperand = InstructionDescriptor.NoOperand

class ED6InstructionTable(InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        return fs.ReadByte()

    def writeOpCode(self, fs: fileio.FileStream, opcode: int):
        fs.WriteByte(opcode)

    def readOperand(self, context: InstructionHandlerContext, desc: ED6OperandDescriptor) -> Operand:
        opr = super().readOperand(context, desc)
        if desc.format.type == ED6OperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, context: InstructionHandlerContext, operand: Operand):
        match operand.descriptor.type:
            case ED6OperandType.Offset:
                fs = context.disasmContext.fs
                pos = fs.Position
                # log.debug(f'xref {repr(operand.value)} at 0x{pos:08X}')
                context.addXRef(operand.value, pos)

        super().writeOperand(context, operand)

    def writeAllOperands(self, context: InstructionHandlerContext, operands: List[Operand]):
        return super().writeAllOperands(context, operands)

def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED6OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)

def Handler_04(ctx: InstructionHandlerContext):
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
            count = readAllOperands(ctx, 'W')[0]
            cases = [readAllOperands(ctx, 'HO') for _ in range(count.value)]
            default = readAllOperands(ctx, 'O')[0]

            inst.operands = [expr, cases, default]

            return inst

        case HandlerAction.Format:
            inst = ctx.instruction
            desc = inst.descriptor
            expr, cases, default = inst.operands

            def formatOperand(opr: Operand):
                return ctx.instructionTable.formatOperand(handlers.FormatOperandHandlerContext(inst, opr, formatter = ctx.formatter))

            f = [
                f'{desc.mnemonic}(',
                f'{DefaultIndent}(',
                *[f'{DefaultIndent * 2}{opr},'.rstrip() for opr in formatOperand(expr)],
                f'{DefaultIndent}),',

                *[f'{DefaultIndent}(0x{id.value:08X}, {formatOperand(o)}),' for id, o in cases],
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

            fmts = 'EW' + 'HO' * count + 'O'

            applyDescriptors(ctx, fmts)

            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor)

def Handler_28(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x01: 'W',
            0x02: 'W',
            0x03: 'B',
            0x04: 'B',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekBytes(ctx, 3)[-1]))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_29(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x00: 'B',
            0x01: 'W',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekBytes(ctx, 3)[-1]))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_2A(ctx: InstructionHandlerContext):
    MAX_PARAM_COUNT = 0xC

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            fs = ctx.disasmContext.fs

            with fs.PositionSaver:
                count = len(fs.Read(MAX_PARAM_COUNT * 2).split(b'\xFF\xFF')[0]) // 2
                count += count != MAX_PARAM_COUNT

            inst.operands = readAllOperands(ctx, 'W' * min(count, MAX_PARAM_COUNT))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, 'W' * min(len(ctx.instruction.operands), MAX_PARAM_COUNT))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_41(ctx: InstructionHandlerContext):
    def getfmts(itemid):
        return 'B' if itemid in [0x258, 0x259, 0x25A, 0x25B, 0x25C, 0x25D, 0x25E, 0x25F, 0x260, 0x261, 0x262, 0x263, 0x264, 0x265, 0x266, 0x267, 0x268, 0x269, 0x26A, 0x26B, 0x26C, 0x26D, 0x26E, 0x26F, 0x270, 0x271, 0x272, 0x273, 0x274, 0x275, 0x276, 0x27D, 0x27E, 0x27F, 0x280, 0x281, 0x282, 0x283, 0x284, 0x285, 0x286, 0x287, 0x28A, 0x28B, 0x28E, 0x28F, 0x291, 0x2C1, 0x2C2, 0x2C3, 0x2C6, 0x2C7, 0x2C8, 0x2C9, 0x2CA, 0x2D0, 0x2D1, 0x2D2, 0x2D3, 0x2D4, 0x315, 0x316, 0x317, 0x318, 0x319, 0x31A, 0x31B, 0x31C, 0x31D, 0x31E, 0x31F] else ''

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            inst.operands = readAllOperands(ctx, 'BW')
            inst.operands.extend(readAllOperands(ctx, getfmts(inst.operands[1].value)))

            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, 'BW' + getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def lambdaHandler(ctx: InstructionHandlerContext, extraCodeSize: int):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            fs = ctx.disasmContext.fs

            chrId, threadId, codeSize = readAllOperands(ctx, 'WWB')

            pos = fs.Position + codeSize.value + extraCodeSize
            block = ctx.disassembler.disasmBlock(ctx.disasmContext)
            fs.Position = pos

            block.name = f'lambda_{block.offset:04X}'
            inst.operands = [chrId, threadId, block]

            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            chrId, threadId, block = inst.operands
            tbl = ctx.instructionTable
            fs = ctx.disasmContext.fs

            oprs = [chrId, threadId]

            applyDescriptorsToOperands(oprs, 'WW')

            tbl.writeOpCode(fs, inst.opcode)
            tbl.writeAllOperands(ctx, oprs)

            pos = fs.Position
            fs.WriteByte(0)

            block.value.func()

            with fs.PositionSaver:
                len = fs.Position - pos - extraCodeSize - 1
                fs.Position = pos
                fs.WriteByte(len)

            return True

        case HandlerAction.Format:
            inst = ctx.instruction
            desc = inst.descriptor
            operands = inst.operands
            code: CodeBlock = operands[2]

            def formatOperand(opr: Operand):
                return ctx.instructionTable.formatOperand(handlers.FormatOperandHandlerContext(inst, opr, formatter = ctx.formatter))

            blockName = code.name

            return [
                f"@scena.Lambda('{blockName}')",
                f'def {blockName}():',
                *[f'{DefaultIndent}{line}' for line in ctx.formatter.formatBlock(code)],
                '',
                f'{desc.mnemonic}({formatOperand(operands[0])}, {formatOperand(operands[1])}, {blockName})',
            ]

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_45(ctx: InstructionHandlerContext):
    '''
        @scena.Lambda('lambda_5029')
        def lambda_5029():
            OP_6D(54030, 0, 55920, 1000)

            ExitThread()            # <--           1 byte

        DispatchAsync(0x0101, 0x0001, lambda_5029)
    '''
    return lambdaHandler(ctx, 1)

def Handler_46(ctx: InstructionHandlerContext):
    '''
        @scena.Lambda('lambda_464E')
        def lambda_464E():
            TurnDirection(0x00FE, 0x0102, 0)
            Yield()                         # <--   1 byte

            Jump('lambda_464E')             # <--   3 bytes

        DispatchAsync2(0x0101, 0x0001, lambda_464E)
    '''
    return lambdaHandler(ctx, 4)

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

def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
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
        operands = ED6OperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)


desc_16 = 'B', {
    0x00: '',
    0x01: '',
    0x02: 'LLLL',
}

desc_29 = 'WB', {
    0x00: '',
    0x01: '',
    0x02: 'LLLL',
}

ScenaOpTable = ED6InstructionTable([
    inst(0x00,  'ExitThread',                   NoOperand,          Flags.EndBlock),
    inst(0x01,  'Return',                       NoOperand,          Flags.EndBlock),
    inst(0x02,  'If',                           'EO'),
    inst(0x03,  'Jump',                         'O',                Flags.Jump),
    inst(0x04,  'Switch',                       NoOperand,          Flags.EndBlock,     Handler_04),
    inst(0x05,  'Call',                         'CW'),                                                      # Call(scp index, func index)
    inst(0x06,  'NewScene',                     'LCCC'),
    inst(0x07,  'IdleLoop'),
    inst(0x08,  'Sleep',                        'I',                Flags.FormatNewLine),
    inst(0x09,  'SetMapFlags',                  'L'),
    inst(0x0A,  'ClearMapFlags',                'L'),
    inst(0x0B,  'FadeOut',                      'iic'),
    inst(0x0C,  'FadeIn',                       'ii'),
    inst(0x0D,  'OP_0D'),
    inst(0x0E,  'Fade',                         'I'),
    inst(0x0F,  'Battle',                       'LLBWB'),
    inst(0x10,  'OP_10',                        'BB'),
    inst(0x11,  'OP_11',                        'BBBLLL'),
    inst(0x12,  'OP_12',                        'LLL'),
    inst(0x13,  'SetPlaceName',                 'W'),
    inst(0x14,  'OP_14'),
    inst(0x15,  'OP_15'),
    inst(0x16,  'OP_16',                        desc_16),
    inst(0x17,  'ShowSaveMenu'),
    inst(0x18,  'OP_18'),
    inst(0x19,  'EventBegin',                   'B'),
    inst(0x1A,  'EventEnd',                     'B'),
    inst(0x1B,  'OP_1B',                        'BBW'),
    inst(0x1C,  'OP_1C',                        'BBW'),
    inst(0x1D,  'OP_1D',                        'B'),
    inst(0x1E,  'OP_1E'),
    inst(0x1F,  'OP_1F',                        'BL'),
    inst(0x20,  'OP_20',                        'L'),
    inst(0x21,  'OP_21'),
    inst(0x22,  'OP_22',                        'WBB'),
    inst(0x23,  'OP_23',                        'W'),
    inst(0x24,  'OP_24',                        'WB'),
    inst(0x25,  'OP_25',                        'WLLLLLBL'),
    inst(0x26,  'OP_26',                        'H'),
    inst(0x27,  'OP_27'),
    inst(0x28,  'OP_28',                        NoOperand,                              handler = Handler_28),
    inst(0x29,  'OP_29',                        NoOperand,                              handler = Handler_29),
    inst(0x2A,  'OP_2A',                        NoOperand,                              handler = Handler_2A),
    inst(0x2B,  'OP_2B',                        'WW'),
    inst(0x2C,  'OP_2C',                        'WW'),
    inst(0x2D,  'FormationAddMember',           'BB'),
    inst(0x2E,  'FormationDelMember',           'BB'),
    inst(0x2F,  'FormationReset'),
    inst(0x30,  'OP_30',                        'B'),
    inst(0x31,  'OP_31',                        'BBW'),
    inst(0x32,  'OP_32',                        'BW'),
    inst(0x33,  'OP_33',                        'BW'),
    inst(0x34,  'OP_34',                        'BW'),
    inst(0x35,  'OP_35',                        'BW'),
    inst(0x36,  'OP_36',                        'BW'),
    inst(0x37,  'OP_37',                        'BW'),
    inst(0x38,  'AddSepith',                    'BW'),  # AddSepith(0~6, number)
    inst(0x39,  'SubSepith',                    'BW'),
    inst(0x3A,  'AddMira',                      'H'),
    inst(0x3B,  'SubMira',                      'H'),
    inst(0x3C,  'OP_3C',                        'H'),
    inst(0x3D,  'OP_3D',                        'H'),
    inst(0x3E,  'OP_3E',                        'Wh'),
    inst(0x3F,  'OP_3F',                        'Wh'),
    inst(0x40,  'OP_40',                        'W'),
    inst(0x41,  'OP_41',                        NoOperand,          Flags.Empty,        Handler_41),
    inst(0x42,  'OP_42',                        'B'),
    inst(0x43,  'CreateThread',                 'WBBW'),
    inst(0x44,  'TerminateThread',              'WB'),
    inst(0x45,  'DispatchAsync',                NoOperand,          Flags.FormatMultiLine,  Handler_45),
    inst(0x46,  'DispatchAsync2',               NoOperand,          Flags.FormatMultiLine,  Handler_46),
    inst(0x47,  'WaitForThreadExit',            'WW'),
    inst(0x48,  'Yield'),
    inst(0x49,  'Event',                        'CH'),
    inst(0x4A,  'OP_4A',                        'WC'),
    inst(0x4B,  'OP_4B',                        'WC'),
    inst(0x4C,  'OP_4C'),
    inst(0x4D,  'ExecExpressionWithReg',        'WE'),
    inst(0x4E,  'OP_4E'),
    inst(0x4F,  'ExecExpressionWithVar',        'BE'),
    inst(0x50,  'OP_50'),
    inst(0x51,  'ExecExpressionWithValue',      'WBE'),
    inst(0x52,  'TalkBegin',                    'W'),
    inst(0x53,  'TalkEnd',                      'W'),
    inst(0x54,  'Talk',                         'T'),
    inst(0x55,  'Yeild2'),
    inst(0x56,  'OP_56',                        'B'),
    inst(0x57,  'OP_57'),
    inst(0x58,  'CloseMessageWindow'),
    inst(0x59,  'OP_59'),
    inst(0x5A,  'SetMessageWindowPos',          'hhhh'),  # SetMessageWindowPos(x, y, -1, -1)
    inst(0x5B,  'ChrTalk',                      'WT'),
    inst(0x5C,  'NpcTalk',                      'WST'),
    inst(0x5D,  'Menu',                         'hhhcT',            Flags.FormatTextIndex),
    inst(0x5E,  'MenuEnd',                      'W'),
    inst(0x5F,  'OP_5F',                        'W'),
    inst(0x60,  'SetChrName',                   'S'),
    inst(0x61,  'OP_61',                        'W'),
    inst(0x62,  'OP_62',                        'WLIBBLB'),
    inst(0x63,  'OP_63',                        'W'),
    inst(0x64,  'OP_64',                        'BW'),
    inst(0x65,  'OP_65',                        'BW'),
    inst(0x66,  'OP_66',                        'W'),
    inst(0x67,  'OP_67',                        'iiii'),
    inst(0x68,  'OP_68',                        'W'),
    inst(0x69,  'OP_69',                        'WL'),
    inst(0x6A,  'OP_6A',                        'W'),
    inst(0x6B,  'OP_6B',                        'ii'),  # SetCameraDistance(distance, duration)
    inst(0x6C,  'OP_6C',                        'ii'),
    inst(0x6D,  'OP_6D',                        'iiii'),
    inst(0x6E,  'OP_6E',                        'ii'),
    inst(0x6F,  'OP_6F',                        'Wi'),
    inst(0x70,  'OP_70',                        'WL'),
    inst(0x71,  'OP_71',                        'WW'),
    inst(0x72,  'OP_72',                        'WW'),
    inst(0x73,  'OP_73',                        'W'),
    inst(0x74,  'OP_74',                        'WLW'),
    inst(0x75,  'OP_75',                        'BLB'),
    inst(0x76,  'OP_76',                        'WLWLLLBB'),
    inst(0x77,  'OP_77',                        'BBBLB'),
    inst(0x78,  'OP_78',                        'BBB'),
    inst(0x79,  'OP_79',                        'BW'),
    inst(0x7A,  'OP_7A',                        'BW'),
    inst(0x7B,  'OP_7B'),
    inst(0x7C,  'OP_7C',                        'LLLL'),
    inst(0x7D,  'OP_7D',                        'B'),
    inst(0x7E,  'OP_7E',                        'WWWBL'),
    inst(0x7F,  'LoadEffect',                   'BS'),
    inst(0x80,  'PlayEffect',                   'BBWiiihhhiiiwiiii'),
    inst(0x81,  'Play3DEffect',                 'BBBSLLLWWWLLLL'),
    inst(0x82,  'OP_82',                        'BB'),
    inst(0x83,  'OP_83',                        'BB'),
    inst(0x84,  'OP_84',                        'B'),
    inst(0x85,  'OP_85',                        'W'),
    inst(0x86,  'SetChrChipByIndex',            'WH'),
    inst(0x87,  'SetChrSubChip',                'WH'),
    inst(0x88,  'SetChrPos',                    'Wiiih'),
    inst(0x89,  'OP_89',                        'Wiiih'),
    inst(0x8A,  'ChrTurnDirection',             'WWH'),
    inst(0x8B,  'OP_8B',                        'WLLW'),
    inst(0x8C,  'OP_8C',                        'Whh'),
    inst(0x8D,  'OP_8D',                        'Wiiiii'),
    inst(0x8E,  'OP_8E',                        'WLLLLB'),
    inst(0x8F,  'OP_8F',                        'WLLLLB'),
    inst(0x90,  'OP_90',                        'WLLLLB'),
    inst(0x91,  'OP_91',                        'WLLLLB'),
    inst(0x92,  'OP_92',                        'WWLLB'),
    inst(0x93,  'OP_93',                        'WWLLB'),
    inst(0x94,  'OP_94',                        'BWWLLB'),
    inst(0x95,  'OP_95',                        'WLLLLL'),
    inst(0x96,  'OP_96',                        'WLLLLL'),
    inst(0x97,  'OP_97',                        'WLLLLW'),
    inst(0x98,  'OP_98',                        'WLLLL'),
    inst(0x99,  'OP_99',                        'WBBL'),
    inst(0x9A,  'SetChrFlags',                  'WW'),
    inst(0x9B,  'ClearChrFlags',                'WW'),
    inst(0x9C,  'SetChrBattleFlags',            'WW'),
    inst(0x9D,  'ClearChrBattleFlags',          'WW'),
    inst(0x9E,  'OP_9E',                        'WLLLL'),
    inst(0x9F,  'OP_9F',                        'WBBBBL'),
    inst(0xA0,  'OP_A0',                        'WBBBL'),
    inst(0xA1,  'OP_A1',                        'WW'),
    inst(0xA2,  'OP_A2',                        'W'),
    inst(0xA3,  'OP_A3',                        'W'),
    inst(0xA4,  'OP_A4',                        'W'),
    inst(0xA5,  'OP_A5',                        'W'),
    inst(0xA6,  'OP_A6',                        'W'),
    inst(0xA7,  'OP_A7',                        'WW'),
    inst(0xA8,  'OP_A8',                        'BBBBB'),
    inst(0xA9,  'OP_A9',                        'B'),
    inst(0xAA,  'OP_AA'),
    inst(0xAB,  'OP_AB'),
    inst(0xAC,  'OP_AC',                        'W'),
    inst(0xAD,  'OP_AD',                        'LWWL'),
    inst(0xAE,  'OP_AE',                        'L'),
    inst(0xAF,  'OP_AF',                        'BW'),
    inst(0xB0,  'OP_B0',                        'WB'),
    inst(0xB1,  'OP_B1',                        'S'),
    inst(0xB2,  'OP_B2',                        'BBW'),
    inst(0xB3,  'PlayMovie',                    'BS'),
    inst(0xB4,  'OP_B4',                        'B'),
    inst(0xB5,  'OP_B5',                        'WB'),
    inst(0xB6,  'OP_B6',                        'B'),
    inst(0xB7,  'OP_B7',                        'WB'),
    inst(0xB8,  'OP_B8',                        'B'),
    inst(0xB9,  'OP_B9',                        'WW'),
    inst(0xBA,  'OP_BA',                        'BW'),
    inst(0xBB,  'OP_BB',                        'BB'),
    inst(0xDE,  'SaveClearData'),
])

del inst
