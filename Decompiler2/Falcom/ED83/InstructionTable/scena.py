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
    'TextCtrlCode',
    'ScriptId',
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
                # log.debug(f'xref {repr(operand.value)} at 0x{pos:08X}')
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

def Handler_02(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            oprs = readAllOperands(ctx, 'sSB')
            inst.operands = oprs[:-1]
            count = oprs[-1].value
            if count != 0:
                inst.operands.extend(readAllOperands(ctx, 'V' * count))

            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            count = len(inst.operands[2:])
            fmts = 'sSB' + 'V' * count
            inst.operands.insert(2, Operand(value = count))
            applyDescriptors(ctx, fmts)
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, str)

def Handler_06(ctx: InstructionHandlerContext):
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
            cases = [readAllOperands(ctx, 'LO') for _ in range(count.value)]
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

            fmts = 'EB' + 'IO' * count + 'O'

            applyDescriptors(ctx, fmts)

            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor)

def Handler_0B(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
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

def Handler_0D(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BB' + {
            0x00: 'E',
            # 0x01: 'E',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_23(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WWWWB',
            0x01: 'WWBB',
            0x02: 'WW',
            0x05: 'WWWWB',
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

def Handler_29(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BB' + {
            0x00: 'WfL',
            0x01: 'SL',
            0x02: 'BWWB',
            0x03: '',
            0x04: 'B',
            # 0x05: 'WL',
            0x06: 'W',
            0x07: 'W',
            0x08: 'SLVV',
            # 0x09: 'SV',
            0x0A: '',
            0x0B: 'V',
            # 0x0C: 'W',
            # 0x0D: 'L',
            # 0x0E: 'L',
            0x0F: '',
            0x10: '',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_2B(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BLBB' + {
            0x00: 'LBLB',
            0x01: 'WWWW',
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
            return genVariadicFuncStub(ctx.descriptor, int, int, int, int)

def Handler_2E(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BWB' + {
            # 0x00: '',
            # 0x01: 'ffB',
            0x02: 'B',
            0x03: 'B',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))

            return inst

        case HandlerAction.Format:
            for opr in ctx.instruction.operands:
                if opr.descriptor.format.type == OperandType.MBCS:
                    ctx.instruction.flags |= Flags.FormatMultiLine
                    break

            return

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int, int)

def Handler_2F(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BN' + {
            0x00: 'SS',
            # 0x01: 'SS',       # remove_chr_animeclip
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
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction

            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))

            return inst

        case HandlerAction.Format:
            totalLen = 0
            for opr in ctx.instruction.operands:
                if opr.descriptor.format.type == OperandType.MBCS:
                    totalLen += len(opr.value)

            if totalLen > 64:
                ctx.instruction.flags |= Flags.FormatMultiLine

            return

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_32(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
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
            0x14: 'WBffffWB',
            0x15: 'WBffffWB',
            0x16: 'BS',
            0x17: 'WBf',
            # 0x18: 'WBW',
            # 0x19: 'WBff',
            0x1A: 'S',
            0x1B: 'W',
            0x1C: 'LS',
            0x1D: 'L',
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

def Handler_33(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WWC',        # bt_damage
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
            0x0B: 'WL',         # set_flags
            0x0C: 'WL',         # clear_flags
            0x0D: 'W',          # get_flags
            0x0E: 'WWL',
            0x0F: 'WW',
            0x10: 'W',
            # 0x11: 'WB',
            # 0x12: 'W' * 9,
            0x13: 'WWWLLL',
            0x14: 'W',
            0x15: 'Wfffff',
            0x16: '',
            0x17: 'WI',
            0x18: '',
            0x19: 'L',
            0x1A: 'L',
            0x1B: '',
            # 0x1C: 'W',
            # 0x1D: 'WLL',
            0x1E: 'WWSS',       # createTempChar(tempChrIndex, chrId, model, ani)
            0x1F: 'W',          # deleteTempChar(tempChrIndex)
            0x20: 'Wff',        # createFollowChar
            0x21: '',
            0x22: '',
            0x23: '',
            0x24: '',
            0x25: '',
            0x26: 'B',
            0x27: 'BWffff',
            # 0x28: '',
            0x29: '',
            # 0x2A: '',
            # 0x2B: '',
            0x2C: '',
            0x2D: 'W',
            0x2E: 'W',
            0x2F: 'WW',
            0x30: 'W',
            0x31: '',
            0x32: 'WSS',
            0x33: 'WWffffBB',
            0x39: 'WWffffBB',
            0x34: '',
            0x35: 'WI',
            0x36: 'Wffff',
            0x37: 'WWfW',
            0x38: 'WWfffffB',
            0x3A: 'W',
            0x3B: 'B',
            0x3C: 'WWff',
            0x3D: 'WBfffBB',
            0x46: 'fff',
            0x47: '',
            0x48: 'W',
            # 0x49: 'W',
            0x4A: 'f',
            0x4B: 'WB',
            # 0x50: 'WSffffW',
            # 0x51: 'SW',
            0x52: 'WB',         # load_effect
            0x53: 'S',
            0x5A: 'WL',
            0x5B: 'BL',
            0x5C: 'B',
            # 0x5D: 'W',
            # 0x5E: 'W',
            # 0x5F: 'W',
            # 0x60: 'W',
            0x61: 'WBLLLL',
            0x62: 'WB',
            0x63: 'W',
            # 0x64: 'S',
            # 0x65: 'W',
            # 0x66: 'W',
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
            # 0x72: 'LfWB',
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
            # 0x82: 'S',
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
            # 0x95: 'WL',
            # 0x96: 'WL',
            # 0x97: 'B',
            0x98: 'W',
            # 0x99: 'B',
            # 0x9A: '',
            # 0x9B: 'W',
            # 0x9C: 'WL',
            # 0x9D: 'WW',
            0x9E: 'WS',
            # 0x9F: '',
            # 0xA0: 'WL',
            # 0xA1: 'WL',
            # 0xA2: 'WL',
            # 0xA3: 'WL',
            # 0xA4: 'WL',
            # 0xA5: 'WL',
            0xA6: '',
            0xA7: '',
            0xA8: '',
            0xA9: '',
            0xAA: '',
            0xAB: '',
            # 0xAC: '',
            # 0xAD: '',
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
            0xB8: 'WB',
            # 0xB9: 'W',
            0xBA: 'VS',
            0xBB: 'VV',
            0xBC: 'BBBB',
            0xBD: '',
            0xBE: '',
            0xBF: 'W',
            0xC0: 'W',
            0xC1: 'L',
            0xC2: 'W',
            0xC3: '',
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

def Handler_36(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: '',
            0x02: 'BfffH',
            0x03: 'BWSfffW',
            0x04: 'BfffHB',
            0x05: 'BfH',
            0x06: 'BWB',
            0x07: 'W',
            0x08: 'BW',
            0x09: 'fff',
            0x0A: 'fffWWWWWB',
            0x0B: 'BfW',
            0x0C: 'BfffH',
            0x0D: 'BWSfffW',
            # 0x0E: 'BWWfW',
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
            # 0x1E: '',
            # 0x1F: 'BfiB',
            0x28: 'fff',
            0x29: 'fff',
            0x2A: 'f',
            0x2B: 'f',
            0x2C: 'W',
            # 0x2D: 'W',
            0x2E: 'B',
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

def Handler_3A(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WfWLB',
            0x01: 'WB',
            0x02: 'B',
            0x03: 'fWB',
            0x04: 'WfWLB',
            0x05: 'WW',
            0x06: 'W',
            0x07: '',
            0x08: 'WB',
            0x09: 'B',
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

def Handler_3B(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'VfVffWWffffSWWWWWWW' + 'W' * 3,
            0x32: 'VfVffWWffffSWWWWWWW' + 'W' * 3,

            0x01: 'VV',
            0x33: 'VV',

            0x02: 'V',
            0x34: 'V',

            0x03: 'VfW',
            # 0x35: 'VfW',

            0x04: 'VfWB',
            # 0x36: 'VfWB',

            # 0x05: 'L',
            0x37: 'L',

            0x39: 'W',
            0x3A: 'WVVVV',
            0x3B: 'L',
            0x3C: 'L',
            0x3D: '',
            # 0x3E: 'W',
            0x64: 'Iff',
            # 0x65: 'f' * 15,
            0x96: 'W',
            0xFA: 'B',
            0xFB: 'B',
            # 0xFD: 'B',
            0xFE: 'W',
            0xFF: 'fff',
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

def Handler_3C(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BN' + {
            0x01: 'SS',
            0x03: 'SSSSS',
            0x04: 'S',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_40(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WWfff' + {
            0xFE00: 'fBW',
            0xFE01: 'fBW',

            0xFE02: 'ffBW',
            0xFE03: 'ffBW',
            # 0xFE04: 'ffBW',

            # 0xFE05: 'fBWS',

            0xF011: 'fBW',
            # 0xFE00: 'fBW',
            0xFFFE: 'fBW',
            0xFFFF: 'fBW',
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
            return genVariadicFuncStub(ctx.descriptor, int, int, float, float, float)

def Handler_43(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BH' + {
            0x05: '',
            0x06: '',
            0x0A: '',
            0x0B: '',
            0x0C: '',
            0x69: '',
            0x6A: '',
            0xFE: '',
            0xFF: 'W',

            # n != 0xC
            0x00: 'fW',
            0x01: 'fW',
            0x03: 'fW',
            0x64: 'fW',
            0x65: 'fW',
            0x67: 'fW',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_46(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BNNW' + {
            0x00: '',
            0x01: 'fff',
            0x02: '',
            0x03: 'f',
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
            return genVariadicFuncStub(ctx.descriptor, int, int, int, int)

def Handler_49(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'N',                  # FormationAddMember
            0x01: 'W',
            0x04: 'N',                  # FormationSetLeader
            0x05: 'W',
            0x06: 'W',
            0x08: 'WffB',               # set_formation
            0x09: 'W',
            0x0A: 'W',
            0x0B: 'W',
            0x0C: 'WW',
            0x0D: 'W' * 0x18,
            0x0E: 'B',
            0x0F: 'B',
            0x11: 'W',
            0x17: 'WW',

            0x02: '',                   # FormationReset
            0x03: '',
            0x07: '',
            0x10: '',
            0x12: '',
            0x13: '',
            0x14: '',
            0x18: '',
            0x19: '',
            0x1A: '',
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

def Handler_4F(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: 'fWWff',
            0x01: '',
            # 0x02: 'WWW',
            0x03: 'ffffWB',
            # 0x04: 'W',
            # 0x05: 'W',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_54(ctx: InstructionHandlerContext):
    def getfmts(n1, n2):
        if n1 == 0x31:
            return 'BB' + {0x00: 'WWffBB', 0x01: 'W'}[n2]

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
            0x01: 'L' + 'f' * 7,
            0x03: 'L' * 8,
            0x07: '',
            0x08: 'L' * 8,
            0x0A: 'B',
            0x0B: 'W',          # resetAttach
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
            0x2D: '',
            0x2E: '',
            0x2F: '',
            0x30: 'V',
            0x34: 'L',
            0x35: 'WLSSS',
            0x36: '',
            0x37: 'WBBB',
            0x38: 'BL',
            0x39: 'W',
            0x3A: 'WWffffB',
            0x3B: 'WWff',
            0x3C: 'Wff',
            0x3E: 'BSL',
            0x3F: '',
            0x40: 'N',
            0x41: '',
            0x42: 'WW',
            0x43: '',
            0x44: 'fff',
            0x45: 'f',
            # 0x46: 'f',
            0x47: 'BW',
            0x48: 'Wf',
            0x49: 'WW',     # set_ovalgear
            0x4A: 'WW',     # battle_change_style
            0x4B: 'W',
            0x4C: 'WWB',
            # 0x4D: 'f',
            # 0x4E: '',
            0x50: 'f',
            0x51: 'WS',
            0x52: 'WWB',
            0x53: 'WW',     # set_chr_model_chrId
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

def Handler_5E(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WfWWWfWfff',
            0x01: 'W',
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

def Handler_65(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BS' + {
            0x00: 'W',
            0x01: 'W',
            # 0x02: 'f',
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
            return genVariadicFuncStub(ctx.descriptor, int, str)

def Handler_66(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BN' + {
            0x00: 'W',          # addCraft
            0x01: 'W',
            0x02: 'L',
            0x03: '',
            0x04: 'W',          # set_sbreak
            0x05: '',
            0x06: 'W',
            0x07: '',
            0x08: 'W',
        #     0x09: 'W',
            0x0A: 'W',
            0x0B: '',
            0x0C: 'W',
            0x0D: '',
            0x0E: 'W',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_67(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: 'W',
            0x01: 'W',
            0x02: '',
            0x03: '',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_68(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BS' + {
            0x00: 'W',
            0x01: 'W',
            0x02: 'fff',
            0x03: 'fff',
            0x04: 'fff',
            0x05: '',
            0x06: '',
            0x07: 'ffffWB',
            0x08: 'fffWB',
            # 0x09: '',
            # 0x0A: '',
            0x0B: 'W',
            # 0x18: 'L',
            # 0x19: '',
            0x1E: 'SSSfff',
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
            return genVariadicFuncStub(ctx.descriptor, int, str)

def Handler_69(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
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
            0x13: 'W',
            0x14: '',
            0x15: '',
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

def Handler_6A(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x00: 'fBW',
            0x03: 'fBW',

            0x01: '',
            0x02: 'fff',
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

def Handler_70(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WWB',
            0x01: 'WB',
            # 0x02: 'WW',
            0x03: 'WWBB',
            0x04: 'WBB',
            0x05: 'WWBB',
            0x06: 'WBBBB',
            0x07: 'WB',
            0x08: 'WWW',
            0x09: 'WBB',
            0x0A: 'WLL',
            0x0B: 'WB',
            0x0C: 'WBB',
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
    def getfmts(n1, n2):
        return {
            0x00: '',
            0x01: 'WB',
            0x02: 'WB',
            0x03: 'BB',
            0x04: 'BB',
            0x05: '',
            0x06: 'W' if n1 < 0x100 else '',
            0x07: '',
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

def Handler_74(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'WB' + {
            0x00: 'L',
            0x01: '',
            0x02: 'WfWWSf',
            0x03: 'SfWWSf',
            0x04: '',
            # 0x14: 'L',
            # 0x15: '',
            0x16: '',
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

def Handler_75(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BB' + {
            0x00: 'WLL',
            0x01: 'SL',
            0x02: 'BWWB',
            0x03: '',
            0x04: 'B',
            0x05: 'WL',
            0x06: 'W',
            0x07: 'W',
            # 0x08: '',

            0x0E: '',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_79(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: '',
            0x01: '',
            0x02: '',
            0x03: '',
            0x04: '',
            # 0x05: 'B' * 6,
            # 0x06: '',
            0x07: 'B',
            0x08: '',
            0x09: '',
            0x0A: '',
            # 0x0B: '',
            # 0x0C: '',
            0x0D: '',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_7A(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'S',
            0x01: 'WS',
            0x02: 'WS',
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

def Handler_7B(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x01: 'SBBB',

            # 0x00: '',
            0x02: '',
            0x09: '',
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

def Handler_7C(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'BWWWWWWW',
            0x01: '',
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

def Handler_7E(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: '',
            0x01: '',
            0x02: 'W',
            0x03: 'fff',
            0x04: 'W',
            0x05: 'f',
            0x06: 'W',
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

def Handler_84(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'ffff',
            0x01: 'ffff',
            0x02: 'ffff',
            0x03: 'WSB',
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

def Handler_8A(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WWSS',               # attachChr
            0x01: 'WWSS',
            0x02: 'W',
            0x03: 'Wfffffffff',
            0xFE: 'WSf',
            0xFF: 'WSf',

            # # <= 0x33
            0x32: 'WS',
            0x33: 'WS',
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

def Handler_8C(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'W',
            # 0x01: '',
            0x02: '',
            0x03: 'B',
            # 0x04: 'L',
            # 0x05: 'W',
            0x06: '',
            0x07: '',
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

def Handler_91(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WL',
            0x01: 'WL',
            0x02: 'SB',
            0x05: 'WL',
            0x0A: 'WL',
            0x0B: 'WL',
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

def Handler_93(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'B',
            0x01: '',
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

def Handler_94(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'L',
            0x01: '',
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

def Handler_95(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'SSBW',
            0x01: '',
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

def Handler_98(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'W' + {
            0x01: 'f',
            # 0x02: 'L',
            # 0x03: 'WB',
            # 0x04: '',
            # 0x05: '',
            0x3E8: 'fB',
            0x3E9: 'fB',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekWord(ctx)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_9B(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'W',
            0x01: '',
            0x02: '',
            0x03: '',
            0x04: '',
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
            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))
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
            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_AB(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WB' + 'W' * 15 + 'B' * 4 + 'W' * 4 + 'B' * 8,
            0x01: '',
            0x02: 'B' + 'W' * 50,
            0x03: 'fff',
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

def Handler_AC(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'B',
            0x01: 'L',
            0x02: 'L',
            0x03: 'V',
            0x04: 'V',
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
            inst.operands = readAllOperands(ctx, getfmts(peekByte(ctx)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_AD(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'B',
            0x01: 'B',
            0x02: 'f',
            0x03: 'B',
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

def Handler_B9(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BL' + {
            0x00: 'WSSL',
            0x01: 'fffffff',
            0x02: 'fff',
            0x03: '',
            0x04: '',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_BA(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            # 0x00: '',
            # 0x01: '',
            # 0x02: '',
            0x0A: '',
            0x0B: '',
            # 0x0C: '',
            0x14: 'BB',
            0x15: '',
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

def Handler_BC(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BWV' + {
            0x00: 'f' * 8 + 'L' * 8,
            0x01: 'L' + 'f' * 15,
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
            return genVariadicFuncStub(ctx.descriptor, int, int, tuple)

def Handler_C0(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'W' + {
            0x01 : 'L',
            0x02 : 'f',
            0x03 : 'Sffffff',
            0x04 : 'SB',
            0x3E8: 'WW',
            0x3E9: 'WW',
        }[n]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(peekWord(ctx)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_C3(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'BLL',
            0x01: 'B',
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

def Handler_C4(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: '',
            0x01: 'B',
            0x02: 'BW',
            0x03: 'W',
            0x04: 'BVffff',
            0x05: 'BB',
            0x06: '',
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

def Handler_C5(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'B',
            0x01: '',
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

def Handler_C6(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'B',
            0x01: '',
            0x02: 'WB',
            0x03: 'WB',
            0x04: 'WL',
            0x05: 'NL',
            0x06: 'W',
            0x07: 'W',
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

def Handler_C7(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: '',
            0x01: 'WL',
            0x02: '',
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

def Handler_C9(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'W',
            0x01: 'W',
            0x02: '',
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

def Handler_CA(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'L',
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

def Handler_CD(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'B',
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


def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
    if operandfmts == '':
        raise ValueError('use NoOperand instead')

    if handler:
        assert operandfmts is NoOperand

    if operandfmts is NoOperand:
        operands = NoOperand
        if not handler and parameters:
            raise

    else:
        operands = ED83OperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

ScenaOpTable = ED83InstructionTable([
    # inst(0x00,  'ExitThread',                   NoOperand,                  Flags.EndBlock),
    inst(0x01,  'Return',                       NoOperand,                  Flags.EndBlock),
    inst(0x02,  'Call',                         NoOperand,                  Flags.Empty,        Handler_02,         parameters = ('type', 'name')),
    inst(0x03,  'Jump',                         'O',                        Flags.Jump,                             parameters = ('label',)),
    inst(0x04,  'OP_04',                        'BS'),
    inst(0x05,  'If',                           'EO',                                                               parameters = ('ops', 'false_successor')),
    inst(0x06,  'Switch',                       NoOperand,                  Flags.EndBlock,     Handler_06),
    inst(0x07,  'DebugLog',                     'BV'),
    inst(0x08,  'OP_08',                        'BE'),
    inst(0x0A,  'ExecExpressionWithReg',        'BE',                                                               parameters = ('regIndex', 'expressions')),
    # inst(0x0B,  'OP_0B',                        'BE'),
    inst(0x0C,  'OP_0C',                        'BB'),
    inst(0x0D,  'OP_0D',                        NoOperand,                                      handler = Handler_0D),
    inst(0x0E,  'OP_0E',                        'BBB'),
    inst(0x10,  'SetScenaFlags',                'F',                                                                        parameters = ('flags',)),
    inst(0x11,  'ClearScenaFlags',              'F'),
    inst(0x12,  'OP_12',                        'W'),
    inst(0x13,  'OP_13',                        'L'),
    inst(0x14,  'OP_14',                        'L'),
    inst(0x15,  'OP_15',                        'L'),
    inst(0x16,  'Sleep',                        'H'),
    inst(0x17,  'OP_17',                        'WW'),
    inst(0x18,  'OP_18',                        'BE'),
    inst(0x1A,  'OP_1A',                        'BB'),
    inst(0x1D,  'CreateChr',                    'NSSSBLLfffffffSSLBffW',    Flags.Empty,                                    parameters = ('chrId', 'model', 'name', 'monsterId', 'type')),
    inst(0x1E,  'CreateThread',                 'NBsS',                                                                     parameters = ('chrId', 'threadId', 'scriptId', 'func')),
    inst(0x1F,  'OP_1F',                        'WB'),
    inst(0x20,  'OP_20',                        'BVVV'),
    inst(0x21,  'OP_21',                        'B'),
    inst(0x22,  'Talk',                         'WT',                       Flags.FormatMultiLine,                          parameters = ('chrId', 'text')),
    inst(0x23,  'OP_23',                        NoOperand,                                      handler = Handler_23),
    inst(0x24,  'ChrTalk',                      'NLT',                      Flags.FormatMultiLine,                          parameters = ('chrId', 'flags', 'text')),
    inst(0x25,  'OP_25',                        'B'),
    inst(0x26,  'WaitForMsg',                   NoOperand),
    inst(0x27,  'OP_27',                        'SW'),
    inst(0x28,  'OP_28',                        'VVB'),
    inst(0x29,  'MenuCmd',                      NoOperand,                                      handler = Handler_29),
    inst(0x2A,  'OP_2A',                        'BWSSB'),
    inst(0x2B,  'Battle',                       NoOperand,                                      handler = Handler_2B),
    inst(0x2C,  'PlayChrAnimeClip',             'NSBBBBBffffBB',                                                            parameters = ('chrId', 'animeClip', 'loop', 'arg4', 'reverse', 'arg6', 'arg7', 'delay', 'startTime', 'endTime', 'currentTime', 'slot', 'arg13')),
    inst(0x2D,  'WaitAnimeClip',                'WfB',                                                                      parameters = ('chrId', 'expiration', 'animeSlot')),
    inst(0x2E,  'OP_2E',                        NoOperand,                                      handler = Handler_2E),
    inst(0x2F,  'ChrAnimeClipCtrl',             NoOperand,                                      handler = Handler_2F,       parameters = ('type', 'chrId')),
    inst(0x30,  'EquipCtrl',                    'BWSSfffffffff'),
    inst(0x31,  'OP_31',                        'BS'),
    inst(0x32,  'EffectCtrl',                   NoOperand,                                      handler = Handler_32),
    inst(0x33,  'BattleCtrl',                   NoOperand,                                      handler = Handler_33),
    inst(0x34,  'OP_34',                        'Bffff'),
    inst(0x35,  'ChrPhysicsCtrl',               'BNL'),
    inst(0x36,  'CameraCtrl',                   NoOperand,                                      handler = Handler_36),
    inst(0x37,  'SetChrPos',                    'Nffff',                                                                    parameters = ('chrId', 'x', 'y', 'z', 'direction')),
    inst(0x38,  'OP_38',                        'NBBS'),
    inst(0x39,  'SetChrAniFunction',            'NBSffL'),
    inst(0x3A,  'OP_3A',                        NoOperand,                                      handler = Handler_3A),
    inst(0x3B,  'OP_3B',                        NoOperand,                                      handler = Handler_3B),
    inst(0x3C,  'SetChrFace',                   NoOperand,                                      handler = Handler_3C),
    inst(0x3D,  'OP_3D',                        'NffB'),
    inst(0x3E,  'OP_3E',                        'WWfB'),
    inst(0x3F,  'OP_3F',                        'N'),
    inst(0x40,  'MoveType',                     NoOperand,                                      handler = Handler_40),
    inst(0x41,  'OP_41',                        'WB'),
    inst(0x42,  'OP_42',                        'BWfffffBW'),
    inst(0x43,  'Fade',                         NoOperand,                                      handler = Handler_43),
    inst(0x44,  'OP_44',                        'WBfWf'),
    inst(0x45,  'OP_45',                        'NfffWW'),
    inst(0x46,  'OP_46',                        NoOperand,                                      handler = Handler_46),
    inst(0x47,  'OP_47',                        'BSW'),
    inst(0x48,  'OP_48',                        'BWWW'),
    inst(0x49,  'FormationCtrl',                NoOperand,                                      handler = Handler_49),
    inst(0x4A,  'OP_4A',                        'ffffWB'),
    inst(0x4B,  'ChrSetRGBA',                   'NffffHB', parameters = ('chrId', 'r', 'g', 'b', 'a', 'durationInMs')),
    inst(0x4C,  'OP_4C',                        'WfffWB'),
    inst(0x4D,  'WaitForThreadExit',            'NB',                                                                       parameters = ('chrId', 'threadId')),
    inst(0x4E,  'OP_4E',                        'ffB'),
    inst(0x4F,  'OP_4F',                        NoOperand,                                      handler = Handler_4F),
    inst(0x50,  'OP_50',                        'VS'),
    inst(0x51,  'OP_51',                        'fffffWffff'),
    inst(0x52,  'OP_52',                        'BW'),
    inst(0x53,  'OP_53',                        'BB'),
    inst(0x54,  'OP_54',                        NoOperand,                                      handler = Handler_54),
    inst(0x55,  'OP_55',                        'BWWWWWWWWWWffffBBSS'),
    inst(0x56,  'OP_56',                        'BBBfffff'),
    inst(0x57,  'OP_57',                        'BB'),
    inst(0x58,  'OP_58',                        'B'),
    inst(0x5A,  'OP_5A',                        'WWSBBB'),
    inst(0x5B,  'OP_5B',                        'WBE'),
    inst(0x5C,  'OP_5C',                        'WBS'),
    inst(0x5D,  'OP_5D',                        'WSfffffffffWBB'),
    inst(0x5E,  'OP_5E',                        NoOperand,                                      handler = Handler_5E),
    inst(0x60,  'OP_60',                        'WBS'),
    inst(0x61,  'OP_61',                        'BSBWfffffffW'),
    inst(0x62,  'OP_62',                        NoOperand),
    inst(0x63,  'OP_63',                        'WB'),
    inst(0x64,  'OP_64',                        'Bf'),
    inst(0x65,  'SetLookpointFlag',             NoOperand,                                      handler = Handler_65,       parameters = ('lookpoint', )),
    inst(0x66,  'CraftCtrl',                    NoOperand,                                      handler = Handler_66),
    inst(0x67,  'OP_67',                        NoOperand,                                      handler = Handler_67),
    inst(0x68,  'OP_68',                        NoOperand,                                      handler = Handler_68),
    inst(0x69,  'OP_69',                        NoOperand,                                      handler = Handler_69),
    inst(0x6A,  'OP_6A',                        NoOperand,                                      handler = Handler_6A),
    inst(0x6B,  'OP_6B',                        'BWWfLL'),
    inst(0x6C,  'OP_6C',                        'Nf'),
    inst(0x6E,  'OP_6E',                        'WffffB'),
    inst(0x6F,  'AddItem',                      'BWI'),
    inst(0x70,  'OP_70',                        NoOperand,                                      handler = Handler_70),
    inst(0x72,  'QuestCtrl',                    NoOperand,                                      handler = Handler_72),
    inst(0x73,  'OP_73',                        NoOperand,                                      handler = Handler_73),
    inst(0x74,  'OP_74',                        NoOperand,                                      handler = Handler_74),
    inst(0x75,  'OP_75',                        NoOperand,                                      handler = Handler_75),
    inst(0x76,  'OP_76',                        'NSSBBffff'),
    inst(0x77,  'ReleaseChr',                   'N'),
    inst(0x78,  'OP_78',                        'BS'),
    inst(0x79,  'OP_79',                        NoOperand,                                      handler = Handler_79),
    inst(0x7A,  'OP_7A',                        NoOperand,                                      handler = Handler_7A),
    inst(0x7B,  'OP_7B',                        NoOperand,                                      handler = Handler_7B),
    inst(0x7C,  'OP_7C',                        NoOperand,                                      handler = Handler_7C),
    inst(0x7D,  'OP_7D',                        'WL'),
    inst(0x7E,  'OP_7E',                        NoOperand,                                      handler = Handler_7E),
    inst(0x80,  'OP_80',                        'f'),
    inst(0x82,  'OP_82',                        'WffWffffW'),
    inst(0x83,  'OP_83',                        'WWWW'),
    inst(0x84,  'OP_84',                        NoOperand,                                      handler = Handler_84),
    inst(0x86,  'OP_86',                        'BWWWWWWfffS'),
    inst(0x87,  'OP_87',                        'BL'),
    inst(0x88,  'OP_88',                        'W'),
    inst(0x89,  'OP_89',                        'W'),
    inst(0x8A,  'OP_8A',                        NoOperand,                                      handler = Handler_8A),
    inst(0x8B,  'OP_8B',                        'fffffB'),
    inst(0x8C,  'OP_8C',                        NoOperand,                                      handler = Handler_8C),
    inst(0x8D,  'OP_8D',                        'Wffff'),
    inst(0x8E,  'OP_8E',                        'W' * 7),
    inst(0x8F,  'OP_8F',                        NoOperand),
    inst(0x90,  'OP_90',                        'SL'),
    inst(0x91,  'OP_91',                        NoOperand,                                      handler = Handler_91),
    inst(0x92,  'OP_92',                        'BW'),
    inst(0x93,  'OP_93',                        NoOperand,                                      handler = Handler_93),
    inst(0x94,  'OP_94',                        NoOperand,                                      handler = Handler_94),
    inst(0x95,  'OP_95',                        NoOperand,                                      handler = Handler_95),
    inst(0x97,  'OP_97',                        'BWL'),
    inst(0x98,  'OP_98',                        NoOperand,                                      handler = Handler_98),
    inst(0x99,  'OP_99',                        'W'),
    inst(0x9A,  'OP_9A',                        'Wfff'),
    inst(0x9B,  'OP_9B',                        NoOperand,                                      handler = Handler_9B),
    inst(0x9C,  'OP_9C',                        NoOperand,                                      handler = Handler_9C),
    inst(0x9D,  'OP_9D',                        'BB'),
    inst(0x9E,  'OP_9E',                        NoOperand,                                      handler = Handler_9E),
    inst(0xA0,  'OP_A0',                        NoOperand),
    inst(0xA1,  'OP_A1',                        'fffWW'),
    inst(0xA3,  'OP_A3',                        'WW'),
    inst(0xA4,  'OP_A4',                        'BB' + 'W' * 20),
    inst(0xA6,  'OP_A6',                        'Wfff'),
    inst(0xA8,  'OP_A8',                        'L'),
    inst(0xA9,  'OP_A9',                        'B'),
    inst(0xAA,  'OP_AA',                        'BB'),
    inst(0xAB,  'OP_AB',                        NoOperand,                                      handler = Handler_AB),
    inst(0xAC,  'OP_AC',                        NoOperand,                                      handler = Handler_AC),
    inst(0xAD,  'OP_AD',                        NoOperand,                                      handler = Handler_AD),
    inst(0xAE,  'SetEndhookFunction',           'SW'),
    inst(0xAF,  'OP_AF',                        'B'),
    inst(0xB1,  'MenuChrFlagCmd',               'BNL'),
    inst(0xB2,  'OP_B2',                        'BW'),
    inst(0xB3,  'OP_B3',                        'ffffWW'),
    inst(0xB4,  'OP_B4',                        NoOperand),
    inst(0xB5,  'OP_B5',                        'WBfff'),
    inst(0xB6,  'OP_B6',                        'WB'),
    inst(0xB7,  'OP_B7',                        'BW'),
    inst(0xB8,  'OP_B8',                        'BVV'),
    inst(0xB9,  'OP_B9',                        NoOperand,                                      handler = Handler_B9),
    inst(0xBA,  'OP_BA',                        NoOperand,                                      handler = Handler_BA),
    inst(0xBB,  'OP_BB',                        'W'),
    inst(0xBC,  'OP_BC',                        NoOperand,                                      handler = Handler_BC),
    inst(0xBE,  'OP_BE',                        'WBff'),
    inst(0xC0,  'OP_C0',                        NoOperand,                                      handler = Handler_C0),
    inst(0xC2,  'OP_C2',                        'B'),
    inst(0xC3,  'OP_C3',                        NoOperand,                                      handler = Handler_C3),
    inst(0xC4,  'OP_C4',                        NoOperand,                                      handler = Handler_C4),
    inst(0xC5,  'OP_C5',                        NoOperand,                                      handler = Handler_C5),
    inst(0xC6,  'OP_C6',                        NoOperand,                                      handler = Handler_C6),
    inst(0xC7,  'OP_C7',                        NoOperand,                                      handler = Handler_C7),
    inst(0xC8,  'OP_C8',                        'BWL'),
    inst(0xC9,  'OP_C9',                        NoOperand,                                      handler = Handler_C9),
    inst(0xCA,  'OP_CA',                        NoOperand,                                      handler = Handler_CA),
    inst(0xCB,  'OP_CB',                        'B'),
    inst(0xCC,  'OP_CC',                        'B'),
    inst(0xCD,  'OP_CD',                        NoOperand,                                      handler = Handler_CD),
])

del inst
