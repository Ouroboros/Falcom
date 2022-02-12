from Falcom.Common  import *
from Assembler      import *
from .types         import *
from Falcom.ED84.InstructionTable import ED84InstructionTable, ScenaOpTable as ED84ScenaOpTable
from pprint import pprint

__all__ = (
    'ScenaOpTable',
    'ED85InstructionTable',
    'ED85OperandType',
    'ED85OperandFormat',
    'ED85OperandDescriptor',
    'ScenaExpression',
    'TextCtrlCode',
    'ScriptId',
)

NoOperand = InstructionDescriptor.NoOperand

class ED85InstructionTable(ED84InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        op = fs.ReadByte()
        return op

    def preDisasmInstruction(self, context: InstructionHandlerContext):
        inst = context.instruction
        if inst.opcode not in [
            0x00,   # abort
            0x01,   # return
            0x04,
        ]:
            dbginfo = context.disasmContext.fs.ReadULong()
            lineno, size = dbginfo & 0x00FFFFFF, dbginfo >> 0x18
            context.dbgInfo = (lineno, size)
        else:
            context.dbgInfo = None

    def postDisasmInstruction(self, context: InstructionHandlerContext):
        if context.dbgInfo is None:
            return

        _, size = context.dbgInfo
        if size == 0xFF:
            return

        inst = context.instruction

        if inst.opcode in [
            0x03,   # Jump
            0x05,   # If
            0x08,
            0x0A,   # ExecExpressionWithReg
            0x0D,
            0x18,   # ExecExpressionWithVar
            0x5B,
        ]:
            return

        if size != inst.size:
            # HACK
            if (inst.opcode, context.offset) in [
                (0x3E, 0x0000741B),       # a1001
                (0x3E, 0x0003F278),       # e3100
                (0x3E, 0x00002C08),       # mg14_00
                (0x3E, 0x0000090F),       # mg14_99
                (0xCF, 0x00017498),       # a0000
            ]:
                context.disasmContext.fs.Position = context.offset + size
                return

            raise Exception('disasmInstruction %02X @ %08X failed' % (inst.opcode, context.offset))

        # print(f'0x{size:X} 0x{inst.size:X}')

    def writeOpCode(self, fs: fileio.FileStream, opcode: int):
        fs.WriteByte(opcode)
        fs.WriteULong(0)
        # fs.WriteULong(0xFFFFFFFF)

def applyDescriptorsToOperands(operands: List[Operand], fmts: str):
    assert len(operands) == len(fmts)
    for i, desc in enumerate(ED85OperandDescriptor.fromFormatString(fmts)):
        operands[i].descriptor = desc

def applyDescriptors(ctx: InstructionHandlerContext, fmts: str):
    operands = ctx.instruction.operands
    applyDescriptorsToOperands(operands, fmts)

def Handler_1E(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            oprs = readAllOperands(ctx, 'NBSsB')
            inst.operands = oprs[:-1]
            count = oprs[-1].value
            if count != 0:
                inst.operands.extend(readAllOperands(ctx, 'V' * count))

            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            count = len(inst.operands[4:])
            fmts = 'NBSsB' + 'V' * count
            inst.operands.insert(4, Operand(value = count))
            applyDescriptors(ctx, fmts)
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int, str, int)

def Handler_33(ctx: InstructionHandlerContext):
    def getfmts(n, n2):
        match n:
            case 0x12:
                return 'BB' + {
                    0x00: 'SWff',
                    0x01: '',
                    0x02: '',
                }[n2]

            case 0xD4:
                return 'BB' + {
                    0x00: '',
                    0x01: '',
                    0x02: 'B',
                    0x03: 'B',
                    0x04: 'W',
                    0x05: 'WB',
                    0x32: '',
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
            0x16: 'B',
            0x17: 'WL',
            0x18: '',
            0x19: 'L',
            0x1A: 'L',
            0x1B: '',
            # 0x1D: 'WLL',
            0x1E: 'WWSS',
            0x1F: 'W',
            0x20: 'Wff',
            0x21: '',
            0x22: '',
            0x23: '',
            0x24: '',
            0x25: '',
            0x26: 'B',
            0x27: 'ff',
            # 0x28: 'BWLLLL',
            0x29: '',
            0x2A: 'W',
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
            0x35: 'BWfffS',
            0x36: 'Wffff',
            0x37: 'WWffffBB',
            0x3E: 'WWffffBB',
            0x38: '',
            0x39: '',
            0x3A: 'WL',
            0x3B: 'Wffff',
            0x3C: 'WWfW',
            0x3D: 'WWfffffB',
            0x3F: 'W',
            0x40: 'WB',
            0x41: 'WWff',
            0x42: 'WBLLLBB',
            0x46: 'fff',
            0x47: '',
            0x48: 'WW',
            0x49: 'W',
            0x4A: 'f',
            0x4B: 'WB',
            0x4C: '',
            # 0x51: 'SW',
            0x52: 'WB',         # load_effect
            0x53: 'S',
            0x54: 'WBfff',
            0x55: 'W',
            0x56: 'B',
            0x5A: 'WL',
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
            0xD3: 'LB',
            0xD5: 'BWW',
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

def Handler_3E(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'NNfB' + {
            0xFE12: 'B',
            0xFE13: 'f',
        }.get(n, '')

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekWords(ctx, 2)[1]))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int, float, int)

def Handler_54(ctx: InstructionHandlerContext):
    def getfmts(n1, n2):
        if n1 == 0x31:
            return 'BB' + {
                0x00: 'WWffBBW',
                0x01: 'W',
                0x02: 'W',
                0x03: '',
            }[n2]

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
            0x0A: 'B',
            0x0B: 'W',
            0x0D: 'SSWW',
            0x0E: 'B',
            0x0F: '',
            0x10: '',
            0x11: '',
            0x12: '',
            0x13: '',
            0x14: 'SS' + 'W' * 6,
            0x15: 'S',
            0x16: '',
            0x17: 'BL',
            0x18: 'WB',
            0x19: 'SS',
            0x1A: 'W',
            0x1B: '',
            0x1F: '',
            0x20: '',
            0x21: 'Wf',
            # 0x22: 'W',
            0x23: 'WWWf',
            0x24: 'W',
            0x25: '',
            0x26: 'BLLS',
            0x27: '',
            0x29: 'BW',
            0x2A: '',
            0x2B: 'BSW',
            0x2C: 'Bff',
            0x2D: '',               # FC_chr_exit
            0x2E: '',               # FC_chr_exit_tk
            0x2F: '',
            0x30: 'V',
            0x34: 'L',
            0x35: 'BWSLSSS',
            0x36: 'B',
            0x37: 'WBBB',
            0x38: 'BL',
            0x39: 'W',
            0x3A: 'WWffffB',
            0x3B: 'BWWWBff',
            0x3E: 'BSL',
            0x3F: '',
            0x40: 'W',
            0x41: '',
            0x42: 'WW',
            0x43: '',
            0x44: 'fff',
            0x45: 'f',
            0x46: 'f',
            0x47: 'BW',
            0x48: 'Wf',
            0x49: 'WW',     # set_ovalgear
            0x4A: 'WW',
            0x4B: 'W',
            0x4C: 'WWB',
            0x4D: 'f',
            0x4E: 'B',
            0x50: 'f',
            0x51: 'WS',
            0x52: 'WWB',
            0x53: 'WW',
            0x54: 'WL',
            0x55: '',
            0x56: 'W',
            0x57: 'B',
            0x58: 'WSffffB',
            0x59: '',
            0x5A: 'VVB',
            0x5B: 'L',
            0x5C: 'L',
            0x5D: 'WW',
            0x5F: 'Wfff',
            0x60: 'Wf',
            0x61: 'WWW',
            0x62: 'S',
            0x63: 'SLLL',
            0x64: 'L' * 8,
            0x65: 'L' + 'f' * 7,
            0x67: 'L' * 8,
            0x6B: 'L' * 8,
            0x6C: 'L' * 8,
            0x6D: 'L' * 8,
            0x6E: 'L' * 8,
            0x6F: 'L' * 8,
            0x70: 'L' * 8,
            0x71: 'L' * 8,
            0x72: 'L' * 8,
            0x73: 'L' * 8,
            0x74: 'L' * 8,
            0x79: 'L' * 8,
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
            0x06: 'V' * 6 + 'f',
            0x07: 'VBW',
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

def Handler_72(ctx: InstructionHandlerContext):
    def getfmts(n1, n2):
        return {
            0x00: '',
            0x01: 'WB',
            0x02: 'WB',
            0x03: 'BB',
            0x04: 'BB',
            0x05: '',
            0x06: 'W',
            0x07: '',
            0x08: 'V',
            0x09: '',
            0x0A: 'V',
            0x0B: 'VBB',
        }[n2]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            oprs = readAllOperands(ctx, 'WB')
            fmts = getfmts(oprs[0].value, oprs[1].value)
            inst.operands = [*oprs, *readAllOperands(ctx, fmts)]
            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            oprs = inst.operands
            applyDescriptors(ctx, 'WB' + getfmts(oprs[0].value, oprs[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_73(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x00: 'BB',
            0x01: 'WB',
            0x02: 'VBB',
            0x04: 'V',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            n = peekBytes(ctx, 3)[-1]
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_9E(ctx: InstructionHandlerContext):
    def getfmts(n, n2):
        fmt1 = {
            0x00: '',
            0x01: '',
            0x02: '',
            0x0F: 'B',
            0x10: '',
            0x11: 'HC',
            0x12: 'BB',
            0x13: '',
            0x32: 'WS',
            0x33: 'WS',
            0x34: 'BL' + ('S' if n2 == 5 else ''),
            0x35: 'BW',
            0x36: 'BL',
            0x37: 'B',
            0x38: 'WBS',
            0x39: '',
            0x3A: 'WW' + 'f' * 8,
            0x3B: 'WB',
            0x3C: 'LW',
            0x3D: 'LW',
            0x3E: 'W',
            0x3F: 'W',
            0x40: '',
            0x41: 'WWLW',
            0x42: 'WL',
            0x43: 'WL',
            0x44: 'WW',
            0x45: 'WW',
            0x46: 'WLW',
            0x47: '',
            0x48: 'B',
            0x49: 'B',
            0x4A: 'Wfff',
            0x4B: 'W',
            0x4C: 'WB',
            0x4D: '',
            0x4E: '',
            0x4F: '',
            0x50: 'W',
            0x51: 'WLB',
            0x53: 'ff',
            0x54: 'B',
            0x55: '',
            0x56: 'B',
            0x59: 'L',
            0x5A: '',
        }

        fmt2 = {
            0x00: '',
            0x01: 'WS',
            0x02: 'W',
            0x03: 'B',
            0x04: 'L',
            0x05: 'Wffff',
            0x06: 'WWfff',
            0x07: 'W',
            0x09: 'BW',
            0x0A: 'WWfff',
            0x0B: 'WW',
            0x0D: 'BL',
            0x0E: 'BW',
            0x0F: 'B',
            0x10: 'W',
            0x11: 'WB',
            0x12: 'BL',
            0x13: 'BL',
            0x14: 'B',
            0x15: 'WBS',
            0x16: 'WL',
            0x17: '',
            0x18: 'W',
            0x19: 'WSV',
            0x1A: 'W',
            0x1B: 'W',
        }

        try:
            return 'B' + fmt1[n]
        except KeyError:
            return 'BB' + fmt2[n2]

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

        if isinstance(handler, tuple):
            handler = genHandler(*handler)

    if operandfmts is NoOperand:
        operands = NoOperand
        if not handler and parameters:
            raise NotImplementedError

    else:
        operands = ED85OperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

desc_23 = 'B', {
    0x00: 'HHHHB',
    0x01: 'HHBB',
    0x02: 'HH',
    0x05: 'HHHHB',
    0x06: 'fff',
    0x07: 'fff',
    0x08: 'fff',
    # 0x09: 'Wfff',
    0x0A: 'Wfff',
    0x0B: 'Wfff',
    0x0C: 'Wfff',
    0x0D: 'ffffB',
    0x13: 'ffffb',
}

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
    0x11: 'SWBBL',
    0x12: 'SWL',
    0x13: 'fff',
    0x14: 'fff',
    0x15: 'fff',
    0x16: 'ffffB',
}

desc_2A = 'BW', {
    0x00: 'SSB',
    0x01: 'SSB',
    0x02: 'SSB',
    0x03: 'SSB',
    0x04: 'SSS',
    0x05: 'SS',
}

desc_2E = 'BWB', {
    0x00: '',
    0x01: 'ffB',
    0x02: 'B',
    0x03: 'B',
    0x04: 'f',
    0x05: 'f',
}

desc_32 = 'B', {
    0x0A: 'WBSL',
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
    0x22: 'WLS',
    0x23: '',
    0x24: 'NVNLVVVVfffVVVBL',
}

desc_36 = 'B', {
    0x00: '',
    0x01: '',
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
    0x19: 'BSfffW',
    0x1A: 'SBfffWB',
    0x1B: 'ff',
    0x1C: 'B',
    0x1D: 'B',
    0x1F: 'BfiB',
    0x20: '',
    0x21: 'WS',
    0x28: 'fff',
    0x29: 'fff',
    0x2A: 'f',
    0x2B: 'f',
    0x2C: 'W',
    # 0x2D: 'W',
    0x2E: 'B',
    0x2F: 'B',
}

desc_3B = 'B', {
    0x00: 'VVVfVWWfffVSVVWWWWWWf',
    0x32: 'VVVfVWWfffVSVVWWWWWWf',

    0x01: 'VVW',
    0x33: 'VVW',

    0x02: 'V',
    0x34: 'V',

    0x03: 'VfW',
    0x35: 'VfW',

    0x04: 'VfWB',
    0x36: 'VfWB',

    0x05: 'L',
    0x37: 'L',

    0x39: 'W',
    0x3A: 'WVVVV',
    0x3B: 'L',
    0x3C: 'L',
    0x3D: '',
    0x3E: 'W',
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
    0x03: 'S' * 5,
    0x04: 'S',
    0x05: 'S' * 5,
}

desc_43 = 'BH', {
    0x05: '',
    0x06: '',
    0x0A: '',
    0x0B: '',
    0x0C: '',
    0x0D: 'W',
    0x0E: 'W',
    0x0F: 'WB',
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
    0x14: 'N' * 30,
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
    0x1F: 'L',
}

desc_64 = 'B', {
    0x00: 'f',
    0x01: 'f',
    0x02: '',
    0x03: '',
}

desc_66 = 'BN', {
    0x00: 'W',
    0x01: 'W',
    0x02: 'L',              # full_craft
    0x03: '',
    0x04: 'W',
    0x05: '',
    0x06: 'W',
    0x07: '',
    0x08: 'WB',
    0x09: 'W',
    0x0A: 'W',
    0x0B: 'L',
    0x0C: '',
    0x0D: 'WL',
    0x0E: '',
    0x0F: 'W',
    0x10: 'W',
    0x11: 'W',
    0x12: 'WL',
}


desc_68 = 'BS', {
    0x00: 'L',              # set_obj_flag
    0x01: 'L',              # reset_obj_flag
    0x02: 'fff',
    0x03: 'fff',            # obj_rot
    0x0D: 'fff',            # obj_rot
    0x04: 'fff',            # obj_size
    0x0E: 'fff',            # obj_size
    0x05: '',               # load_obj_asset
    0x06: '',               # release_obj_asset
    0x07: 'ffffWB',         # obj_color
    0x08: 'fffWB',          # obj_specular
    0x09: '',
    0x0A: '',
    0x0B: 'W',              # obj_chr_pos
    0x0F: 'W',
    0x10: 'WBS' + 'f' * 6,
    0x18: 'L',            # check_obj_flag
    0x19: '',             # get_obj_animetime
    0x1E: 'SSSfff',
}

desc_69 = 'B', {
    0x00: 'WWBBB',
    0x01: 'W',
    0x02: 'WWW',
    0x03: 'WWW',
    0x04: 'W',
    0x05: 'WWW',
    0x06: 'WWWL',
    0x07: 'W',
    0x08: 'W',
    0x09: 'W',
    0x0A: 'WWB',
    0x0B: 'W',
    0x0C: 'WW',
    0x0D: 'WW',
    0x12: 'WW',
    0x14: 'BB',
    0x15: 'W',
    0x16: '',
    0x17: 'W',
    0x18: 'WWWBBB',
    0x19: 'B',
    0x1A: 'VW',
    0x1B: 'W',
    0x1C: 'L',
    0x1D: 'W',
}

desc_6F = 'B', {
    0x00: 'WL',
    0x01: 'WL',
    0x02: 'WL',
    0x03: 'WL',
    0x04: 'WL',
    0x05: 'WL',
    0x06: 'WL',
    0x07: 'WL',
    0x08: 'WL',
    0x09: 'WL',
    0x0A: 'WL',
    0x0B: 'WL',
    0x0C: 'WL',
    0x0D: 'WL',
    0x0E: 'WL',
    0x0F: 'WL',
    0x10: 'WL',
    0x11: 'WL',
    0x12: 'WL',
    0x13: 'WL',
    0x14: 'WL',
    0x15: 'WL',
    0x16: 'WL',
    0x17: 'WL',
    0x18: 'WL',
    0x19: 'WL',
    0x1A: 'WL',
    0x1B: 'W',
    0x1C: 'LLBB',
    0x1D: 'V',
    0x1E: 'VVBB',
    0x1F: 'WL',
    0x20: 'WB',
    0x21: 'WL',
}

desc_70 = 'B', {
    0x00: 'WWBB',
    0x01: 'WB',
    # 0x02: 'WW',
    0x03: 'WWBBB',
    0x04: 'WBB',
    0x05: 'WWBB',
    0x06: 'WBBBB',
    0x07: 'WB',
    0x08: 'WWW',
    0x09: 'WBB',
    0x0A: 'WLL',
    0x0B: 'WB',
    0x0C: 'WBB',
    0x0D: 'W',
    0x0E: 'WWW',
    0x0F: 'WWW',
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
    0x09: 'fff',
    0x0A: 'fff',
    0x0B: 'fff',
    0x0C: 'V' * 5 + 'B',
    0x0D: 'V' * 4,
    0x0E: 'B',
    0x0F: 'B',
    0x10: 'L',
}

desc_79 = 'BW', {
    0x00: '',
    0x01: '',
    0x02: '',
    0x03: '',
    0x04: '',
    0x05: '',
    0x06: '',
    0x07: 'BB',
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
    0x20: '',
    0x21: '',
    0x22: '',
    0x23: '',
}

desc_7A = 'B', {
    0x00: 'S',
    0x01: 'NS',
    0x02: 'NS',
    0x03: 'S',
}

desc_7C = 'B', {
    0x00: 'BWWWWWWW',
    0x01: '',
    0x02: '',
}

desc_8A = 'B', {
    0x00: 'WWSSB',
    0x01: 'WWSS',
    0x02: 'WW',
    0x03: 'W' + 'f' * 9,
    0x0A: 'WSSSB',
    0x0B: 'W',
    0x0C: 'WSSSB',
    0x0D: 'S',
    0x32: 'WS',
    0x33: 'WS',
    0xFE: 'WSf',
    0xFF: 'WSf',
}

desc_8C = 'B', {
    0x00: 'W',
    0x01: '',
    0x02: '',
    0x03: 'B',
    # 0x04: 'L',
    # 0x05: 'W',
    0x06: '',
    0x07: '',
    0x08: 'L',
    0x09: '',
    0x0A: 'SS',
    0x0B: '',
    0x0C: 'SL',
    0x0D: 'LL',
    0x0F: 'L',
    0x10: 'LB',
    0x11: 'S',
    0x12: '',
    0x13: '',
    0x14: 'B',
}

desc_91 = 'B', {
    0x00: 'WL',
    0x01: 'WL',
    0x02: 'SB',
    0x05: 'WL',
    0x06: 'W',
    0x0A: 'WL',
    0x0B: 'WL',
}

desc_96 = 'B', {
    0x00: 'L',
    0x01: '',
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
    4002    : 'W',
    5000    : 'f',
    5001    : 'f',
    5002    : 'L',
    6000    : 'L',
    6001    : 'L',
    7000    : 'B',
    7001    : 'B',
    8000    : 'SB',
    9000    : 'f',
    10000   : 'f' * 8,
}

desc_A5 = 'BW', {
    0x00: 'WfB',
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
    0x0A: '',
    0x0B: 'W',
    0x0C: '',
    0x0D: 'V',
    0x0E: '',
    0x0F: 'W',
    0x10: '',
    0x11: '',
    0x12: 'V',
    0x13: 'W',
    0x14: 'V',
    0x15: 'W',
    0x16: 'V',
    0x17: 'W',
}

desc_B0 = 'B', {
    0x00: '',
    0x01: '',
    0x02: '',
    0x03: '',
    0x04: 'B',
    0x07: '',
    0x08: '',
    0x09: '',
    0x0A: 'B',
    0x0B: 'BB',
    0x0C: 'B',
    0x0D: '',
    0x0E: '',
    0x0F: '',
    0x10: 'V',
    0x11: '',
    0x12: 'B',
    0x17: '',
    0x18: '',
    0x19: 'B',
    0x1A: '',
    0x1B: '',
    0x1C: '',
    0x1D: 'B',
    0x1E: 'B',
    0x1F: '',
    0x20: '',
    0x21: 'B',
    0x22: '',
    0x23: '',
    0x24: '',
    0x25: 'B',
    0x26: '',
    0x27: '',
    0x28: 'B',
    0x29: '',
    0x2A: '',
    0x2B: '',
    0x2C: '',
    0x2D: '',
    0x2E: 'B',
    0x2F: 'B',
    0x30: '',
    0x31: 'L',
    0x32: '',
    0x33: '',
    0x34: '',
    0x35: '',
    0x36: 'LB',
    0x37: '',
    0x38: '',
    0x39: '',
    0x3A: '',
    0x3B: '',
    0x3C: 'BWB',
    0x3D: 'L',
    0x3E: 'L',
    0x3F: '',
    0x40: '',
}

desc_B2 = 'B', {
    0x00: 'BW',
    0x01: 'BBBW',
}

desc_BC = 'BWV', {
    0x00: 'LfffffffLLLLLLLWW',
    0x01: 'LfffffffLLLLLLLWW',
    0x02: 'B',
    0x03: '',
    0x04: 'WW',
    0x05: 'HW',
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
    0x16: 'L',
    0x17: 'ff',
    0x18: 'f',
    0x19: 'S',
}

desc_C0 = 'W', {
    0x01 : 'L',
    0x02 : 'f',
    0x03 : 'Sffffff',
    0x04 : 'SB',
    0x3E8: 'WW',
    0x3E9: 'WW',
    0x3EA: '',
    0x3EB: 'WW',
}

desc_C3 = 'B', {
    0x00: 'BLLL',
    0x01: 'B',
}

desc_C4 = 'B', {
    0x00: 'B',
    0x01: 'B',
    0x02: 'VN',
    0x03: 'N',
    0x04: 'BVffff',
    0x05: 'BB',
    0x06: 'VB',
    0x07: '',
    0x08: 'B',
    0x09: 'V',
    0x0A: 'B',
    0x0B: 'BB',
    0x0C: 'BW',
    0x0D: 'BW',
    0x0E: 'B' * 10,
    0x0F: 'B' * 9,
    0x10: 'VW',
}

desc_C5 = 'B', {
    0x00: 'BB',
    0x01: '',
    0x02: '',
    0x03: '',
    0x04: 'B',
    0x05: '',
    0x06: 'B',
    0x07: 'L',
    0x08: '',
    0x09: 'B' * 8,
    0x0A: 'B' * 8,
    0x0B: '',
    0x0C: 'B' * 5,
}

desc_C8 = 'BWL', {
    0x00: '',
    0x01: '',
    0x02: 'W',
    0x03: 'fff',
}

desc_D9 = 'B', {
    0x00: 'B',
    0x02: '',
    0x03: 'L',
    0x04: 'Wffffff',
    0x05: '',
    0x06: 'fff',
}

desc_DA = 'B', {
    0x00: 'B',
    0x01: '',
}

desc_DC = 'B', {
    0x00: 'WWB',
}

desc_DE = 'B', {
    0x00: '',
    0x01: 'BL',
    0x02: '',
    0x03: 'BBB',
    0x04: '',
    0x05: '',
}

desc_E0 = 'B', {
    0x00: '',
    0x01: '',
    0x02: 'BWfLLBB',
    0x03: 'Wfff',
    0x04: '',
    0x05: 'B',
    0x06: 'S',
    0x07: '',
    0x08: '',
}

desc_E1 = 'B', {
    0x00: 'Wff',
    0x01: '',
}

desc_E2 = 'B', {
    0x00: 'BB',
    0x01: 'B',
    0x02: 'BW',
    0x03: 'BW',
    0x04: 'B',
    0x05: 'BB',
    0x06: '',
}

desc_E3 = 'B', {
    0x00: '',
    0x01: '',
    0x02: 'WBWW',
    0x03: 'WBW',
    0x04: '',
    0x05: '',
}

desc_E5 = 'B', {
    0x00: 'B',
    0x01: 'BB',
}

ScenaOpTable = ED85InstructionTable(ED84ScenaOpTable).update([
    # inst(0x00,  'Abort',                        NoOperand),
    inst(0x1E,  'CreateThread',                 NoOperand,                                      handler = Handler_1E,       parameters = ('chrId', 'threadId', 'func', 'scriptId')),
    inst(0x20,  'OP_20',                        'BVVVVB'),
    inst(0x21,  'OP_21',                        'BB'),
    inst(0x23,  'OP_23',                        desc_23),
    inst(0x29,  'MenuCmd',                      desc_29),
    inst(0x2A,  'OP_2A',                        desc_2A),
    inst(0x2E,  'OP_2E',                        desc_2E),
    inst(0x32,  'EffectCtrl',                   desc_32),
    inst(0x33,  'BattleCtrl',                   NoOperand,                                      handler = Handler_33),
    inst(0x36,  'CameraCtrl',                   desc_36),
    inst(0x3B,  'OP_3B',                        desc_3B),
    inst(0x3C,  'SetChrFace',                   desc_3C),
    inst(0x3E,  'OP_3E',                        NoOperand,                                      handler = Handler_3E),
    inst(0x3F,  'OP_3F',                        'NL'),
    inst(0x43,  'OP_43',                        desc_43),
    inst(0x49,  'FormationCtrl',                desc_49),
    inst(0x4A,  'OP_4A',                        'BffffIB'),
    inst(0x4E,  'OP_4E',                        'ffBB'),
    inst(0x50,  'OP_50',                        'VSLB'),
    inst(0x54,  'ModelCtrl',                    NoOperand,                                      handler = Handler_54),
    inst(0x64,  'OP_64',                        desc_64),
    inst(0x66,  'CraftCtrl',                    desc_66),
    inst(0x68,  'OP_68',                        desc_68),
    inst(0x69,  'OP_69',                        desc_69),
    inst(0x6A,  'OP_6A',                        NoOperand,                                      handler = Handler_6A),
    inst(0x6C,  'OP_6C',                        'NfL'),
    inst(0x6F,  'AddItem',                      desc_6F),
    inst(0x70,  'OP_70',                        desc_70),
    inst(0x72,  'QuestCtrl',                    NoOperand,                                      handler = Handler_72),
    inst(0x73,  'OP_73',                        NoOperand,                                      handler = Handler_73),
    inst(0x75,  'OP_75',                        desc_75),
    inst(0x79,  'OP_79',                        desc_79),
    inst(0x7A,  'OP_7A',                        desc_7A),
    inst(0x7C,  'OP_7C',                        desc_7C),
    inst(0x7D,  'OP_7D',                        'WLf'),
    inst(0x8A,  'OP_8A',                        desc_8A),
    inst(0x8C,  'OP_8C',                        desc_8C),
    inst(0x91,  'OP_91',                        desc_91),
    inst(0x96,  'OP_96',                        desc_96),
    inst(0x98,  'WeatherCtrl',                  desc_98),
    inst(0x99,  'OP_99',                        'WW'),
    inst(0x9E,  'OP_9E',                        NoOperand,                                      handler = Handler_9E),
    inst(0xA2,  'OP_A2',                        'WSff'),
    inst(0xA5,  'OP_A5',                        desc_A5),
    inst(0xAC,  'OP_AC',                        desc_AC),
    inst(0xB0,  'OP_B0',                        desc_B0),
    inst(0xB2,  'OP_B2',                        desc_B2),
    inst(0xBC,  'OP_BC',                        desc_BC),
    inst(0xC0,  'OP_C0',                        desc_C0),
    inst(0xC3,  'OP_C3',                        desc_C3),
    inst(0xC4,  'OP_C4',                        desc_C4),
    inst(0xC5,  'OP_C5',                        desc_C5),
    inst(0xC8,  'OP_C8',                        desc_C8),
    inst(0xD9,  'OP_D9',                        desc_D9),
    inst(0xDA,  'OP_DA',                        desc_DA),
    inst(0xDB,  'OP_DB',                        'B'),
    inst(0xDC,  'OP_DC',                        desc_DC),
    inst(0xDE,  'OP_DE',                        desc_DE),
    inst(0xDF,  'OP_DF',                        'LB'),
    inst(0xE0,  'OP_E0',                        desc_E0),
    inst(0xE1,  'OP_E1',                        desc_E1),
    inst(0xE2,  'OP_E2',                        desc_E2),
    inst(0xE3,  'OP_E3',                        desc_E3),
    inst(0xE5,  'OP_E5',                        desc_E5),
    inst(0xE6,  'OP_E6',                        'W'),
])

del inst
