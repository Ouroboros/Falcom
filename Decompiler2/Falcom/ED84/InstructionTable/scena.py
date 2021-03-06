from Falcom.Common  import *
from Assembler      import *
from .types         import *
from Falcom.ED83.InstructionTable import ED83InstructionTable, ScenaOpTable as ED83ScenaOpTable

__all__ = (
    'ScenaOpTable',
    'ED84InstructionTable',
    'ED84OperandType',
    'ED84OperandFormat',
    'ED84OperandDescriptor',
    'ScenaExpression',
    'TextCtrlCode',
    'ScriptId',
)

NoOperand = InstructionDescriptor.NoOperand

class ED84InstructionTable(ED83InstructionTable):
    pass

def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED84OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)

def Handler_33(ctx: InstructionHandlerContext):
    def getfmts(n, n2):
        match n:
            case 0x12:
                return 'BB' + {
                    0x00: 'SW',
                    0x01: '',
                    0x02: '',
                }[n2]

        return 'B' + {
            0x00: 'WWBB',       # bt_damage
            0x01: 'WVVB',       # bt_damage_anime
            0x02: 'BW',
            0x03: 'W',
            0x04: 'B',
            0x05: 'BS',
            0x06: 'B',
            0x07: 'BS',         # AniBtlItem
            0x08: 'B',
            0x09: 'W',          # bt_init_hit
            0x0A: 'WW',
            0x0B: 'WL',
            0x0C: 'WL',
            0x0D: 'W',
            0x0E: 'WWL',
            0x0F: 'WW',
            0x10: 'W',
            0x11: 'WB',
            0x13: 'WWWLLL',
            0x14: 'W',
            0x15: 'Wfffff',
            0x16: '',
            0x17: 'WL',
            0x18: '',
            0x19: 'L',
            0x1A: 'L',
            0x1B: '',
            # 0x1D: 'WLL',
            0x1E: 'WWSS',
            0x1F: 'W',
            0x20: 'Nff',        # createFollowChar
            0x21: '',
            0x22: '',
            0x23: '',
            0x24: '',
            0x25: '',
            0x26: 'B',
            0x27: 'ff',
            # 0x28: 'BWLLLL',
            0x29: '',
            0x2A: '',
            0x2B: '',
            0x2C: '',
            0x2D: '',
            0x2E: 'W',
            0x2F: 'W',
            0x30: 'WW',
            0x31: 'W',
            0x32: '',
            0x33: 'WSS',
            0x34: 'B',
            0x37: 'WWffffBB',
            0x3E: 'WWffffBB',
            0x38: '',
            0x39: '',
            0x3A: 'WL',
            0x3B: 'Wffff',
            0x3C: 'WWfW',
            0x3D: 'WWfffffB',
            0x3F: 'W',
            # 0x40: 'B',
            0x41: 'WWff',
            0x42: 'WBLLLBB',
            0x46: 'fff',
            0x47: '',
            0x48: 'WW',
            # 0x49: 'W',
            0x4A: 'f',
            0x4B: 'WB',
            0x4C: '',
            # 0x51: 'SW',
            0x52: 'WB',         # load_effect
            0x53: 'S',
            0x5A: 'NI',
            0x5B: 'BL',
            0x5C: 'B',
            # 0x5D: 'W',
            # 0x5E: 'W',
            # 0x5F: 'W',
            # 0x60: 'W',
            0x61: 'WBV',
            0x62: 'WB',
            0x63: 'W',
            0x64: 'S',
            0x65: 'W',
            0x66: 'W',
            0x67: '',
            0x68: '',
            # 0x69: '',
            # 0x6A: '',
            0x6B: 'W',
            0x6C: 'W',
            # 0x6D: 'W',
            0x6E: 'WWffff',         # bt_set_safetypoint
            0x6F: '',
            0x70: '',
            # 0x71: 'LWB',
            # 0x72: 'LWB',
            0x73: 'W',
            0x74: 'W',
            0x76: '',
            0x77: 'W',
            0x78: 'WW',
            # 0x79: 'W',
            # 0x7A: 'WB',
            0x7B: 'WW',
            0x7D: 'B',
            0x7E: 'fWB',
            0x7F: '',
            0x81: 'W',
            0x82: 'BWL',
            0x83: 'WW',
            0x85: '',
            0x86: '',
            0x87: '',
            0x88: '',
            0x89: 'W',
            0x8A: '',
            0x8E: 'WW',
            0x8F: 'W',
            0x90: 'B',
            0x91: 'WW',
            0x92: 'ff',
            # 0x93: 'W',
            0x94: 'WWW',
            0x97: 'BW',
            0x98: 'W',
            # 0x99: 'B',
            # 0x9A: '',
            # 0x9B: 'W',
            # 0x9C: 'WL',
            0x9E: 'WS',
            # 0x9F: '',
            0xA6: '',
            0xA7: 'B',
            0xA8: 'L',
            0xA9: 'BL',
            0xAA: '',
            0xAB: '',
            # 0xAC: 'B',
            0xAD: '',
            0xAE: 'W',
            0xAF: 'W',
            0xB0: '',
            0xB1: '',
            0xB2: '',
            # 0xB3: '',
            0xB4: 'WVVVV',
            0xB5: 'B',
            0xB6: 'ff',
            0xB7: 'BWLLLB',
            0xB8: 'WBB',
            # 0xB9: 'W',
            0xBA: 'VS',
            0xBB: 'VV',
            0xBC: 'BBBSS',
            0xBD: '',
            0xBE: '',
            0xBF: 'W',
            0xC0: 'WBB',
            0xC1: 'L',
            0xC2: 'WW',
            0xC3: '',
            0xC4: 'SS',
            0xC5: 'WLLLLL',
            0xC6: 'W',
            0xC7: 'L',
            0xC8: 'L',
            0xC9: 'WVVV',
            0xCA: 'W',
            0xCB: 'B',
            0xCC: 'WW',
            0xCD: 'L',
            0xCE: '',
            # 0xCF: '',
            # 0xD0: '',
            # 0xD1: 'BWW',
            0xD2: 'BWW',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(*peekBytes(ctx, 2)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value, ctx.instruction.operands[1].value if len(ctx.instruction.operands) > 1 else None))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_40(ctx: InstructionHandlerContext):
    def getfmts(n):
        match n:
            case 0xFE15:
                return 'NNVVVVBWffB'

        return 'NNfff' + {
            0xFE00: 'fBWffB',
            0xFE01: 'fBWffB',

            0xFE02: 'f' + 'fBWffB',
            0xFE03: 'f' + 'fBWffB',
            0xFE04: 'f' + 'fBWffB',

            0xFE05: 'fBWffB' + 'S',

            # 0xF011: 'fBWffB',
            # 0xFE00: 'fBWffB',
            # 0xFE16: 'fBWffB',
            0xFFFE: 'fBWffB',
            0xFFFF: 'fBWffB',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekWords(ctx, 2)[1]))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_41(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x00: '',
            0x01: '',
            0x02: '',
            0x03: '',
            0x04: 'ffffB',
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

def Handler_54(ctx: InstructionHandlerContext):
    def getfmts(n1, n2):
        if n1 == 0x31:
            return 'BB' + {0x00: 'WWffBBW', 0x01: 'W'}[n2]

        elif n1 == 0x4F:
            return 'BB' + {
                0x00: 'BW',
                0x01: 'B',
                0x02: 'WWB',
                0x03: 'W',
                0x04: 'WWBB',
                0x0A: 'WBfW',
            }[n2]

        return 'B' + {
            # 0x00: 'L' * 8,
            # 0x01: 'L' + 'f' * 7,
            # 0x03: 'L' * 8,
            # 0x07: '',
            # 0x08: 'L' * 8,
            0x0A: 'B',
            0x0B: 'W',
            0x0D: 'SSWW',
            0x0E: 'B',
            0x0F: '',
            0x10: '',
            0x11: '',
            0x12: '',
            # 0x13: '',
            0x14: 'SSWWWWWW',
            0x15: 'S',
            # 0x16: '',
            0x17: 'BL',
            0x18: 'WB',
            0x19: 'SS',
            0x1A: '',
            0x1B: '',
            # 0x1C: 'SWW',
            # 0x1D: '',
            # 0x1E: '',
            0x1F: '',
            0x20: '',
            0x21: 'Wf',
            # 0x22: 'W',
            0x23: 'WWWf',
            0x24: 'W',
            0x25: '',
            0x26: 'BLLS',
            0x27: '',
            # 0x28: 'W',
            # 0x29: 'BW',
            0x2A: '',
            0x2B: 'BSW',
            # 0x2C: 'Bff',
            0x2D: '',               # FC_chr_exit
            0x2E: '',               # FC_chr_exit_tk
            0x2F: '',
            0x30: 'V',
            0x34: 'L',
            0x35: 'BWSLSSS',
            0x36: '',
            0x37: 'WBBB',
            0x38: 'BL',
            0x39: 'W',
            0x3A: 'WWffffB',
            0x3B: 'WWff',
            0x3C: 'Wff',
            0x3E: 'BSL',
            0x3F: '',
            # 0x40: 'W',
            0x41: '',
            0x42: 'WW',
            0x43: '',
            0x44: 'fff',
            0x45: 'f',
            # 0x46: 'f',
            0x47: 'BW',
            0x48: 'Wf',
            0x49: 'WW',     # set_ovalgear
            0x4A: 'WW',
            0x4B: 'W',
            0x4C: 'WWB',
            # 0x4D: 'f',
            0x4E: 'B',
            0x50: 'f',
            0x51: 'WS',
            0x52: 'WWB',
            0x53: 'WW',

            0x54: 'WL',
            0x55: '',
            # 0x64: 'L' * 8,
            0x65: 'L' + 'f' * 7,
            # 0x67: 'L' * 8,
            0x6B: 'L' * 8,
            0x6C: 'L' * 8,
            0x6D: 'L' * 8,
            0x6E: 'L' * 8,
            0x6F: 'L' * 8,
        }[n1]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(*peekBytes(ctx, 2)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value, ctx.instruction.operands[1].value if len(ctx.instruction.operands) > 1 else None))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_6A(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x00: 'fBW',
            0x03: 'fBW',

            0x01: '',
            0x02: 'fffLLLL',
            0x04: 'fffffBW',
            0x05: 'f' * 7,          # curve_type
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
        operands = ED84OperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

desc_29 = 'BC', {
    0x00: 'HfI',
    0x01: 'SL',
    0x02: 'BHHB',
    0x03: '',
    0x04: 'B',
    # 0x05: 'WL',
    0x06: 'W',
    0x07: 'W',
    0x08: 'SLVV',
    0x09: 'SV',
    0x0A: '',
    0x0B: 'V',
    # 0x0C: 'W',
    0x0D: 'L',
    0x0E: 'L',
    0x0F: '',
    0x10: '',
    # 0x11: 'SWBBL',
    0x12: 'SWL',
}

desc_2B = 'BLBB', {
    0x00: 'LB' * 4,
    0x01: 'N' * 4,
}

desc_2F = 'BN', {
    0x00: 'SS',
    0x01: 'SS',
    # 0x02: 'SS',
    # 0x03: '',
    0x04: 'SS',
    0x05: 'SS',
    0x06: 'L',
    0x07: 'L',
    0x08: 'B' + 'S' * 16,
    0x09: 'B',
    0x0A: 'SS',
    0x0B: 'SS',
    0x0C: 'SS',
    0x0D: '',
    0x0E: 'LSS',
    0x0F: 'B',
    0x10: 'S',
}

desc_32 = 'B', {
    0x0A: 'WBS',
    0x0B: 'WB',
    0x0C: 'NVNLVVVVfffVVVB',
    0x0D: 'WBB',
    0x0E: 'WBB',
    0x0F: 'WWB',
    0x10: 'WWB',
    0x11: 'WB',
    0x12: 'WW',
    0x13: 'WBW',
    0x14: 'WBffffHB',
    0x15: 'WBffffHB',
    0x16: 'SS',
    0x17: 'WBf',
    0x18: 'WBW',
    # 0x19: 'WBff',
    0x1A: 'S',
    0x1B: 'W',
    0x1C: 'LSL',
    0x1D: 'L',
    0x1E: 'WBf',
    0x1F: 'WW',
    0x21: 'WWB',
    0x22: 'LS',
}

desc_36 = 'B', {
    0x00: '',
    0x02: 'BfffH',
    0x03: 'BWSfffW',
    0x04: 'BfffHB',
    0x05: 'BfH',
    0x06: 'BWB',
    0x07: 'W',
    0x08: 'BW',
    0x09: 'fff',
    0x0A: 'fffHHHHHB',
    0x0B: 'BfW',
    0x0C: 'BfffH',
    0x0D: 'BWSfffW',
    0x0E: 'BfffH',
    0x0F: 'Wfff',
    0x10: '',
    0x11: 'BfffWB',
    0x12: 'W',
    0x13: 'WSBfffHB',
    0x14: 'BWSfffH',
    0x15: 'BfiB',
    0x16: 'BfH',
    0x17: 'W',
    # 0x18: 'BSfffW',
    # 0x19: 'BSfffW',
    # 0x1A: 'SBfffWB',
    0x1B: 'ff',
    0x1C: '',
    0x1D: '',
    # 0x1F: 'BfiB',
    0x20: '',
    0x21: 'WS',
    0x28: 'fff',
    0x29: 'fff',
    0x2A: 'f',
    0x2B: 'f',
    0x2C: 'W',
    # 0x2D: 'W',
    0x2E: 'B',
}

desc_3B = 'B', {
    0x00: 'VVVfVWWfffVSVVWWWWWWf',
    0x32: 'VVVfVWWfffVSVVWWWWWWf',

    0x01: 'VV',
    0x33: 'VV',

    0x02: 'V',
    0x34: 'V',

    0x03: 'VfW',
    # 0x35: 'VfW',

    0x04: 'VfWB',
    # 0x36: 'VfWB',

    0x05: 'L',
    0x37: 'L',

    0x39: 'W',
    0x3A: 'WVVVV',
    0x3B: 'L',
    0x3C: 'L',
    0x3D: '',
    # 0x3E: 'W',
    0x3F: 'W',
    0x64: 'Iff',
    # 0x65: 'f' * 15,
    0x96: 'W',
    0xFA: 'B',
    0xFB: 'B',
    # 0xFD: 'B',
    0xFE: 'W',
    0xFF: 'fff',
}

desc_3C = 'BN', {
    0x01: 'SS',
    0x03: 'SSSSS',
    0x04: 'S',
    0x05: 'SSS',
}

desc_43 = 'BH', {
    0x05: '',
    0x06: '',
    0x0A: '',
    0x0B: '',
    0x0C: '',
    0x69: '',
    0x6A: '',
    0x6B: '',
    0xFE: '',
    0xFF: 'W',

    # n != 0xC
    0x00: 'fH',
    0x01: 'fH',
    0x02: 'fH',
    0x03: 'fH',
    0x64: 'fH',
    0x65: 'fH',
    0x67: 'fH',
    0x68: 'fH',
}

desc_46 = 'BNWW', {
    0x00: '',
    0x01: 'fff',
    0x02: '',
    0x03: 'fB',
    0x04: '',
    0x05: '',
    0x06: '',
    0x07: '',
}

desc_48 = 'BWW', {
    0x00: 'W',
    0x01: '',
}

desc_49 = 'B', {
    0x00: 'N',
    0x01: 'N',
    0x02: 'B',
    0x03: '',
    0x04: 'N',
    0x05: 'N',
    0x06: 'N',
    0x07: '',
    0x08: 'NffB',               # set_formation
    0x09: 'N',
    0x0A: 'N',
    0x0B: 'N',
    0x0C: 'NN',
    0x0D: 'N' * 0x18,
    0x0E: 'B',
    0x0F: 'B',
    0x10: '',
    0x11: 'N',
    0x12: 'B',
    0x14: 'N' * 20,
    0x15: 'N',
    0x16: 'NH',
    0x17: 'W',
    0x18: '',
    0x19: '',
    0x1A: '',
    0x1B: 'B',
    0x1C: 'B',
    0x1D: 'B',
    0x1E: 'N',
}

desc_5A = 'B', {
    0x00: 'WWSW',
    0x01: '',
}

desc_5E = 'B', {
    0x00: 'WfHHHfWSfff',
    0x01: 'W',
}

desc_61 = 'B', {
    0x00: 'SBWfffffffW',
    0x01: 'W',
    0x02: '',
}

desc_65 = 'BS', {
    0x00: 'W',
    0x01: 'W',
    # 0x02: 'f',
    0x03: 'f',
}

desc_66 = 'BN', {
    0x00: 'R',
    0x01: 'R',
    0x02: 'L',              # full_craft
    0x03: '',
    0x04: 'R',
    0x05: '',
    0x06: 'R',
    0x07: '',
    0x08: 'R',
#     0x09: 'W',
    0x0A: 'R',
    0x0B: 'L',
    0x0C: '',
    0x0D: 'RL',
    0x0E: '',
    0x0F: 'R',
    0x10: 'R',
    0x11: 'R',
}

desc_69 = 'B', {
    0x00: 'WWBBB',
    0x01: 'W',
    0x02: 'WWW',
    # 0x03: 'WWW',
    0x04: 'W',
    0x05: 'WWW',
    0x06: 'WWWL',
    0x07: 'W',
    0x08: 'W',
    0x09: 'W',
    # 0x0A: 'WWB',
    0x0B: 'W',
    # 0x0C: 'WW',
    # 0x0D: 'WW',
    # 0x12: 'WW',
    0x14: 'BB',
    0x15: 'W',
    0x16: '',
    0x18: 'WWWBBB',
}

desc_70 = 'B', {
    0x00: 'NtBB',
    0x01: 'NB',
    # 0x02: 'WW',
    0x03: 'NtBBB',
    0x04: 'NBB',
    0x05: 'NtBB',
    0x06: 'NBBBB',
    0x07: 'NB',
    0x08: 'tWW',
    0x09: 'NBB',
    0x0A: 'tLL',
    0x0B: 'NB',
    0x0C: 'NBB',
    0x0D: 'N',
    0x0E: 'Ntt',
}

desc_75 = 'BB', {
    0x00: 'WLL',
    0x01: 'SL',
    0x02: 'BWWB',
    0x03: '',
    0x04: 'B',
    0x05: 'WL',
    0x06: 'W',
    0x07: 'W',
    0x08: '',

    0x0E: '',
}

desc_78 = 'BS', {
    0x00: '',
    0x01: 'B',
}

desc_79 = 'BW', {
    0x00: '',
    0x01: '',
    0x02: '',
    0x03: '',
    0x04: '',
    0x05: '',
    0x06: '',
    0x07: 'B',
    0x08: '',
    0x09: '',
    0x0A: '',
    0x0B: '',
    0x0C: '',
    0x0D: '',
    0x0E: '',
    0x0F: '',
    0x10: '',
    0x11: '',
    0x12: '',
    0x13: '',
    0x14: '',
    0x15: '',
    0x16: '',
    0x17: '',
    0x18: '',
    0x1E: '',
    0x1F: '',
}

desc_7E = 'B', {
    0x00: '',
    0x01: '',
    0x02: 'W',
    0x03: 'fff',
    0x04: 'W',
    0x05: 'f',
    0x06: 'W',
    0x07: 'fB',
    0x08: '',
    0x09: '',
}

desc_8A = 'B', {
    0x00: 'WWSS',
    0x01: 'WWSS',
    0x02: 'WW',
    0x03: 'W' + 'f' * 9,
    0x0A: 'WSSS',
    0x0B: 'W',
    0x0C: 'WSSS',
    0x0D: 'S',
    0x32: 'WS',
    0x33: 'WS',
    0xFE: 'WSf',
    0xFF: 'WSf',
}

desc_93 = 'B', {
    0x00: 'B',
    0x01: '',
    0xC8: '',
    0xC9: '',
    0xD2: 'W',
    0xD3: '',
    0xDC: '',
    0xDD: '',
}

desc_94 = 'B', {
    0x00: 'L',
    0x01: '',
    0x03: '',
}

desc_98 = 'H', {
    0x01    : 'f',
    # 0x02    : 'L',
    # 0x03    : 'WB',
    # 0x04    : '',
    # 0x05    : '',
    0x06    : 'f',
    0x07    : 'f',
    1000    : 'fB',
    1001    : 'fB',
    2000    : 'BfB',
    2001    : '',
    3000    : 'ffWf',
    4000    : 'WfWB',
    4001    : 'SfWB',                  # set_obj_stealth
    # 5000    : 'L',
    5001    : 'f',
    # 5002    : 'L',
    6000    : 'L',
    # 6001    : 'L',
    6500    : 'f',
    7000    : 'B',
    7001    : '',
    8000    : 'SB',
    9000    : 'L',
}

desc_9C = 'B', {
    0x00: 'BWWL',
    0x01: '',
    0x02: 'W',
    0x03: '',
    0x04: '',
}

desc_AC = 'B', {
    0x00: 'B',
    0x01: 'V',
    0x02: 'L',
    0x03: 'V',
    0x04: 'V',
    0x05: 'V',
    0x07: 'W',
    0x08: '',
    0x09: 'W',
    # 0x0A: '',
    0x0B: 'W',
    # 0x0C: '',
    0x0D: 'V',
    0x0E: '',
    0x0F: 'W',
    0x10: '',
    0x11: '',
    0x12: 'V',
    0x13: 'W',
}

desc_BC = 'BWV', {
    0x00: 'LfffffffLLLLLLLWW',
    0x01: 'LfffffffLLLLLLLWW',
    0x02: 'B',
    0x03: '',
    0x04: 'WW',
    0x05: 'WW',
    0x06: '',
    0x07: 'ffhW',
    0x08: 'L',
    0x09: 'ffffffWh',
    0x0A: 'ff',
    0x0B: 'L',
    0x0C: 'Sff',
    0x0D: 'L',
    0x0E: 'VWW',
    0x0F: 'WLS',
    0x10: 'LLh',
    0x11: 'Sff',
    0x12: 'Sff',
    0x13: 'Sff',
    0x14: 'L',
    0x15: 'L',
    # 0x16: 'L',
}

desc_BD = 'B', {
    # 0x03: 'L',
    0x04: 'W',
    0x05: 'WWW',
}

desc_C4 = 'B', {
    0x00: 'B',
    0x01: 'B',
    0x02: 'BN',
    0x03: 'N',
    0x04: 'BVffff',
    0x05: 'BB',
    0x06: '',
}

desc_C5 = 'B', {
    0x00: 'BB',
    0x01: '',
}

desc_C6 = 'B', {
    0x00: 'B',
    0x01: '',
    0x02: 'WB',
    0x03: 'WB',
    0x04: 'WL',
    0x05: 'WL',
    0x06: 'W',
    0x07: 'W',
    0x08: 'WBBB',
    0x09: 'W',
}

desc_C9 = 'B', {
    0x00: 'W',
    0x01: 'W',
    0x02: '',
    0x03: 'WW',
    0x0A: 'WS',
}

desc_CE = 'W', {
    0x00: 'SSB',
    0x01: 'LB',
    0x02: 'SLLLLB',
    0x03: 'B',
    0x04: 'WLLLLB',
    0x05: 'WSB',
    0x06: 'B',
    # 0x07: 'B',
    # 0x08: 'B',
    0x09: 'LLBB',
    0x0A: 'SB',
    0x0B: 'LB',
    0x14: 'WSB',
    0x15: 'WLB',
    # 0x1E: 'SSB',
    # 0x1F: 'SLB',
    0x28: 'SB',
    0x32: 'SLB',
    # 0x33: 'SLB',
}

desc_CD = 'B', {
    0x00: '',
    0x01: 'WWWW',
    0x02: 'WW',
    0x05: '',
    0x06: 'WWWW',
}

desc_D0 = 'B', {
    0x00: 'WSSSSfff',
    # 0x1E: 'SSSSLLL',
}

desc_D1 = 'B', {
    0x00: 'SWff',
    0x01: 'SW',
}

desc_D2 = 'W', {
    0x00    : 'B',
    0x01    : '',
    0x02    : '',
    0xFFFD  : 'BBL',
    0xFFFE  : 'V',
    0xFFFF  : 'V',
}

desc_D3 = 'B', {
    0x00: 'ffffWBBB',
    0x01: '',
}

desc_D4 = 'B', {
    0x00: 'B',
}

desc_D5 = 'B', {
    0x00: '',
    0x01: 'W',
    0x02: '',
}


ScenaOpTable = ED84InstructionTable(ED83ScenaOpTable).update([
    inst(0x19,  'OP_19',                        'BW'),
    inst(0x20,  'OP_20',                        'BVVVV'),
    inst(0x29,  'MenuCmd',                      desc_29),
    inst(0x2B,  'Battle',                       desc_2B),
    inst(0x2F,  'AnimeClipCmd',                 desc_2F,                parameters = ('type', 'chrId')),
    inst(0x32,  'EffectCmd',                    desc_32),
    inst(0x33,  'BattleCmd',                    NoOperand,                                      handler = Handler_33),
    inst(0x34,  'OP_34',                        'BffffW'),
    inst(0x36,  'CameraCmd',                    desc_36),
    inst(0x3B,  'OP_3B',                        desc_3B),
    inst(0x3C,  'SetChrFace',                   desc_3C),
    inst(0x40,  'MoveChr',                      NoOperand,                                      handler = Handler_40),
    inst(0x41,  'OP_41',                        NoOperand,                                      handler = Handler_41),
    inst(0x43,  'OP_43',                        desc_43),
    inst(0x46,  'OP_46',                        desc_46),
    inst(0x48,  'OP_48',                        desc_48),
    inst(0x49,  'FormationCmd',                 desc_49),
    inst(0x50,  'OP_50',                        'VSL'),
    inst(0x54,  'ModelCmd',                     NoOperand,                                      handler = Handler_54),
    inst(0x5A,  'OP_5A',                        desc_5A),
    inst(0x5E,  'OP_5E',                        desc_5E),
    inst(0x61,  'OP_61',                        desc_61),
    inst(0x62,  'OP_62',                        'WW'),
    inst(0x65,  'SetLookpointFlag',             desc_65,                parameters = ('lookpoint', )),
    inst(0x66,  'CraftCmd',                     desc_66),
    inst(0x69,  'OP_69',                        desc_69),
    inst(0x6A,  'OP_6A',                        NoOperand,                                      handler = Handler_6A),
    inst(0x70,  'OP_70',                        desc_70),
    inst(0x71,  'OP_71',                        'BWW'),
    inst(0x75,  'OP_75',                        desc_75),
    inst(0x78,  'OP_78',                        desc_78),
    inst(0x79,  'OP_79',                        desc_79),
    inst(0x7E,  'OP_7E',                        desc_7E),
    inst(0x8A,  'OP_8A',                        desc_8A),
    inst(0x8E,  'OP_8E',                        'W' * 8),
    inst(0x93,  'OP_93',                        desc_93),
    inst(0x94,  'OP_94',                        desc_94),
    inst(0x98,  'WeatherCmd',                   desc_98),
    inst(0x9A,  'OP_9A',                        'WfffW'),
    inst(0x9C,  'OP_9C',                        desc_9C),
    inst(0xAC,  'OP_AC',                        desc_AC),
    inst(0xB5,  'OP_B5',                        'WBfffWW'),
    inst(0xBC,  'OP_BC',                        desc_BC),
    inst(0xBD,  'OP_BD',                        desc_BD),
    inst(0xC1,  'OP_C1',                        NoOperand),
    inst(0xC4,  'OP_C4',                        desc_C4),
    inst(0xC5,  'OP_C5',                        desc_C5),
    inst(0xC6,  'OP_C6',                        desc_C6),
    inst(0xC9,  'OP_C9',                        desc_C9),
    inst(0xCE,  'OP_CE',                        desc_CE),
    inst(0xCD,  'OP_CD',                        desc_CD),
    inst(0xCF,  'OP_CF',                        'B'),
    inst(0xD0,  'OP_D0',                        desc_D0),
    inst(0xD1,  'OP_D1',                        desc_D1),
    inst(0xD2,  'OP_D2',                        desc_D2),
    inst(0xD3,  'OP_D3',                        desc_D3),
    inst(0xD4,  'OP_D4',                        desc_D4),
    inst(0xD5,  'OP_D5',                        desc_D5),
    inst(0xD6,  'OP_D6',                        'WVVVV'),
    inst(0xD7,  'AddBattleCount',               'BL'),
])

del inst
