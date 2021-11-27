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

def Handler_Call(ctx: InstructionHandlerContext):
    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            oprs = readAllOperands(ctx, 'BSB')
            inst.operands = oprs[:-1]
            count = oprs[-1].value
            if count != 0:
                inst.operands.extend(readAllOperands(ctx, 'V' * count))

            return inst

        case HandlerAction.Assemble:
            inst = ctx.instruction
            count = len(inst.operands[2:])
            fmts = 'BSB' + 'V' * count
            inst.operands.insert(2, Operand(value = count))
            applyDescriptors(ctx, fmts)
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, str)

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
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_MenuCmd(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BB' + {
            0x00: 'WfL',
            0x01: 'SI',
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
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_2F(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            # 0x00: 'SS',
            # 0x01: 'SS',
            # 0x02: 'SS',
            # 0x03: '',
            # 0x04: 'SS',
            # 0x05: 'SS',
            # 0x06: 'L',
            # 0x07: 'L',
            # 0x08: 'B' + 'S' * 16,
            # 0x09: 'B',
            # 0x0A: 'SS',
            0x0B: 'SS',
            # 0x0C: 'SS',
            # 0x0D: '',
            # 0x0E: 'LSS',
            # 0x0F: 'B',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_36(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            # 0x00: '',
            # 0x02: 'BLLL',
            # 0x03: 'BWSfffW',
            0x04: 'BfffWB',
            # 0x05: 'BfW',
            # 0x06: 'BWB',
            0x07: 'W',
            0x08: 'BW',
            # 0x09: 'fff',
            0x0A: 'fffWWWWWB',
            # 0x0B: 'BfW',
            # 0x0C: 'BfffW',
            # 0x0D: 'BWSfffW',
            # 0x0E: 'BWWfW',
            # 0x0F: 'Wfff',
            # 0x10: '',
            # 0x11: 'BfffWB',
            0x12: 'W',
            # 0x13: 'WSBfffWB',
            # 0x14: 'BWSfffW',
            # 0x15: 'BfiB',
            # 0x16: 'BfW',
            # 0x17: 'W',
            # 0x18: 'BSfffW',
            # 0x19: 'BSfffW',
            # 0x1A: 'SBfffWB',
            # 0x1B: 'ff',
            # 0x1C: '',
            # 0x1D: '',
            # 0x1E: '',
            # 0x1F: 'BfiB',
            # 0x28: 'fff',
            # 0x29: 'fff',
            # 0x2A: 'f',
            # 0x2B: 'f',
            # 0x2C: 'W',
            # 0x2D: 'W',
            # 0x2E: 'B',
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

            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))

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

            # 0x01: 'VV',
            # 0x33: 'VV',

            # 0x02: 'V',
            # 0x34: 'V',

            # 0x03: 'VfW',
            # 0x35: 'VfW',

            # 0x04: 'VfWB',
            # 0x36: 'VfWB',

            # 0x05: 'L',
            # 0x37: 'L',

            # 0x39: 'W',
            # 0x3A: 'WVVVV',
            # 0x3B: 'L',
            # 0x3C: 'L',
            # 0x3D: '',
            # 0x3E: 'W',
            0x64: 'Iff',
            # 0x65: 'f' * 15,
            # 0x96: 'W',
            # 0xFA: 'B',
            # 0xFB: 'B',
            # 0xFD: 'B',
            # 0xFE: 'W',
            0xFF: 'fff',
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

def Handler_3C(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x01: 'SS',
            0x03: 'SSSSS',
            0x04: 'S',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_43(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: 'fW',
            0x05: '',
            # 0x06: '',
            0x0A: '',
            0x0B: '',
            0x0C: '',
            0x69: '',
            # 0x6A: '',
            # 0xFE: '',
            0xFF: 'W',

            # n != 0xC
            0x64: 'fW',
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
        return 'BWWW' + {
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
        return 'B' + {
            # 0x00: 'L' * 8,
            # 0x01: 'f' * 8,
            # 0x03: 'L' * 8,
            0x08: 'L' * 8,
            # 0x0A: 'B',
            # 0x0B: 'W',
            # 0x0D: 'SSWW',
            # 0x0E: 'B',
            # 0x0F: '',
            # 0x10: '',
            # 0x11: '',
            # 0x12: '',
            # 0x13: '',
            # 0x14: 'SSWWWWWW',
            # 0x15: 'S',
            # 0x16: '',
            # 0x17: 'L',
            # 0x18: 'WB',
            # 0x19: 'SS',
            # 0x1A: '',
            # 0x1B: '',
            # 0x1C: 'SWW',
            # 0x1D: '',
            # 0x1E: '',
            # 0x1F: '',
            # 0x20: '',
            # 0x21: 'Wf',
            # 0x22: 'W',
            # 0x23: 'WWWL',
            # 0x24: 'W',
            # 0x25: '',
            # 0x26: 'BLLS',
            # 0x27: '',
            # 0x28: 'W',
            # 0x29: 'BW',
            # 0x2A: '',
            # 0x2B: 'BSW',
            # 0x2C: 'Bff',
            # 0x2D: '',
            # 0x2E: '',
            # 0x2F: '',
            # 0x30: 'V',
            # 0x31: 'B' + {0x00: 'WWffBB', 0x01: 'W'}[n2],
            # 0x34: 'L',
            # 0x35: 'WLSSS',
            # 0x36: '',
            # 0x37: 'WBBB',
            # 0x38: 'BL',
            # 0x39: 'W',
            # 0x3A: 'WWffffB',
            # 0x3B: 'WWff',
            # 0x3C: 'B' * 0xA,
            # 0x3E: 'BSL',
            # 0x3F: '',
            # 0x40: 'W',
            # 0x41: '',
            # 0x42: 'WW',
            # 0x43: '',
            # 0x44: 'fff',
            # 0x45: 'f',
            # 0x46: 'f',
            # 0x47: 'BW',
            # 0x48: 'Wf',
            # 0x49: 'WW',     # set_ovalgear
            # 0x4A: 'WW',
            # 0x4B: 'W',
            # 0x4C: 'WWB',
            # 0x4D: 'f',
            # 0x4E: '',
            # 0x4F: 'B' + {0x00: 'BW', 0x01: 'B', 0x02: 'WWB', 0x03: 'W', 0x04: 'WWBB', 0x0A: 'WBfW'}[n2],
            # 0x50: 'f',
            # 0x51: 'WS',
            # 0x52: 'WWB',
            # 0x53: 'WW',
        }[n1]

    match ctx.action:
        case HandlerAction.Disassemble:
            inst = ctx.instruction
            inst.operands = readAllOperands(ctx, getfmts(*peekBytes(ctx, 2)))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[0].value, ctx.instruction.operands[1].value))
            return

        case HandlerAction.CodeGen:
            return genVariadicFuncStub(ctx.descriptor, int)

def Handler_5E(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WfWWWfWfff',
            # 0x01: 'W',
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

def Handler_66(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: 'W',
        #     0x01: 'W',
        #     0x02: 'L',
            0x03: '',
            0x04: 'W',
        #     0x05: '',
        #     0x06: 'W',
        #     0x07: '',
        #     0x08: 'W',
        #     0x09: 'W',
        #     0x0A: 'W',
        #     0x0B: '',
        #     0x0C: 'W',
        #     0x0D: '',
        #     0x0E: 'W',
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

def Handler_69(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            # 0x00: 'WWBBB',
            # 0x01: 'W',
            # 0x02: 'WWW',
            # 0x03: 'WWW',
            0x04: 'W',
            0x05: 'WWW',
            0x06: 'WWWL',
            0x07: 'W',
            0x08: 'W',
            0x09: 'W',
            # 0x0A: 'WWB',
            # 0x0B: 'W',
            # 0x0C: 'WW',
            # 0x0D: 'WW',
            # 0x12: 'WW',
            # 0x13: 'W',
            # 0x14: '',
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

def Handler_70(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'WWB',
            0x01: 'WB',
            # 0x02: 'WW',
            # 0x03: 'WWBB',
            # 0x04: 'WBB',
            # 0x05: 'WWBB',
            # 0x06: 'WBBBB',
            # 0x07: 'WB',
            # 0x08: 'WWW',
            # 0x09: 'WBB',
            # 0x0A: 'WLL',
            # 0x0B: 'WB',
            # 0x0C: 'WBB',
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

def Handler_74(ctx: InstructionHandlerContext):
    def getfmts(n):
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
            inst.operands = readAllOperands(ctx, getfmts(n))
            return inst

        case HandlerAction.Assemble:
            applyDescriptors(ctx, getfmts(ctx.instruction.operands[2].value))
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

def Handler_79(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BW' + {
            0x00: '',
            0x01: '',
            # 0x02: '',
            0x03: '',
            0x04: '',
            # 0x05: 'B' * 6,
            # 0x06: '',
            0x07: 'B',
            # 0x08: '',
            # 0x09: '',
            0x0A: '',
            # 0x0B: '',
            # 0x0C: '',
            # 0x0D: '',
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
            return genVariadicFuncStub(ctx.descriptor, int, int)

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

def Handler_84(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'ffff',
            0x03: 'WSB',
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
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
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

def Handler_BC(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'BWV' + {
            # 0x00: 'f' * 16,
            # 0x01: 'f' * 16,
            # 0x02: 'B',
            0x03: '',
            # 0x04: 'WW',
            # 0x05: 'WW',
            0x06: '',
            # 0x07: 'ffhW',
            0x08: 'L',
            # 0x09: 'ffffffWh',
            # 0x0A: 'ff',
            # 0x0B: 'L',
            # 0x0C: 'Sff',
            # 0x0D: 'L',
            # 0x0E: 'VWW',
            # 0x0F: 'WLS',
            # 0x10: 'LLh',
            # 0x11: 'Sff',
            # 0x12: 'Sff',
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
            return genVariadicFuncStub(ctx.descriptor, int, int, tuple)

def Handler_C3(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            0x00: 'BLL',
            0x01: 'B',
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

def Handler_C4(ctx: InstructionHandlerContext):
    def getfmts(n):
        return 'B' + {
            # 0x00: '',
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
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
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
            n = peekByte(ctx)
            inst.operands = readAllOperands(ctx, getfmts(n))
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
            0x05: 'WL',
            0x06: 'W',
            0x07: 'W',
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
        if parameters and len(operands) != len(parameters):
            raise

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

ScenaOpTable = ED83InstructionTable([
    inst(0x00,  'ExitThread',                   NoOperand,                  Flags.EndBlock),
    inst(0x01,  'Return',                       NoOperand,                  Flags.EndBlock),
    inst(0x02,  'Call',                         NoOperand,                  Flags.Empty,        Handler_Call,       parameters = ('type', 'name')),
    inst(0x03,  'Jump',                         'O',                        Flags.Jump,                             parameters = ('label',)),
    inst(0x04,  'OP_04',                        'BS'),
    inst(0x05,  'If',                           'EO',                                                               parameters = ('ops', 'successor')),
    inst(0x06,  'Switch',                       NoOperand,                  Flags.EndBlock,     Handler_Switch),
    inst(0x07,  'OP_07',                        'BV'),
    inst(0x08,  'OP_08',                        'BE'),
    inst(0x0A,  'OP_0A',                        'BE'),
    inst(0x0C,  'OP_0C',                        'BB'),
    inst(0x0E,  'OP_0E',                        'BBB'),
    inst(0x10,  'SetScenaFlags',                'F',                                                                parameters = ('flags',)),
    inst(0x11,  'OP_11',                        'W'),
    inst(0x12,  'OP_12',                        'W'),
    inst(0x13,  'OP_13',                        'L'),
    inst(0x14,  'OP_14',                        'L'),
    inst(0x15,  'OP_15',                        'L'),
    inst(0x16,  'OP_16',                        'W'),
    inst(0x18,  'OP_18',                        'BE'),
    inst(0x1D,  'OP_1D',                        'HSSSBLLfffffffSSLBffW',    Flags.FormatMultiLine),
    inst(0x1E,  'OP_1E',                        'WBBS'),
    inst(0x20,  'OP_20',                        'BVVV'),
    inst(0x21,  'OP_21',                        'B'),
    inst(0x22,  'Talk',                         'WT',                       Flags.FormatMultiLine,                  parameters = ('chrId', 'text')),
    inst(0x23,  'OP_23',                        NoOperand,                                      handler = Handler_23),
    inst(0x24,  'ChrTalk',                      'WLT',                      Flags.FormatMultiLine,                  parameters = ('chrId', 'flags', 'text')),
    inst(0x25,  'OP_25',                        'B'),
    inst(0x26,  'OP_26',                        NoOperand),
    inst(0x27,  'OP_27',                        'SW'),
    inst(0x28,  'OP_28',                        'VVB'),
    inst(0x29,  'MenuCmd',                      NoOperand,                                      handler = Handler_MenuCmd),
    # inst(0x2B,  'Battle',                       ''),
    inst(0x2F,  'AddChrAnimeClip',              NoOperand,                                      handler = Handler_2F,   parameters = ('type', 'chrId')),
    inst(0x35,  'OP_35',                        'BWL'),
    inst(0x36,  'CameraRotateChr',              NoOperand,                                      handler = Handler_36),
    inst(0x38,  'OP_38',                        'WBBS'),
    inst(0x3A,  'OP_3A',                        NoOperand,                                      handler = Handler_3A),
    inst(0x3B,  'OP_3B',                        NoOperand,                                      handler = Handler_3B),
    inst(0x3C,  'OP_3C',                        NoOperand,                                      handler = Handler_3C),
    inst(0x3D,  'OP_3D',                        'WffB'),
    inst(0x43,  'OP_43',                        NoOperand,                                      handler = Handler_43),
    inst(0x44,  'OP_44',                        'WBfWf'),
    inst(0x45,  'OP_45',                        'WfffWW'),
    inst(0x46,  'OP_46',                        NoOperand,                                      handler = Handler_46),
    inst(0x48,  'OP_48',                        'BWWW'),
    inst(0x49,  'OP_49',                        NoOperand,                                      handler = Handler_49),
    inst(0x4B,  'OP_4B',                        'WffffWB'),
    inst(0x4C,  'OP_4C',                        'WfffWB'),
    inst(0x4F,  'OP_4F',                        NoOperand,                                      handler = Handler_4F),
    inst(0x54,  'OP_54',                        NoOperand,                                      handler = Handler_54),
    inst(0x55,  'OP_55',                        'BWWWWWWWWWWffffBBSS'),
    inst(0x56,  'OP_56',                        'BBBfffff'),
    inst(0x57,  'OP_57',                        'BB'),
    inst(0x58,  'OP_58',                        'B'),
    inst(0x5A,  'OP_5A',                        'WWSBBB'),
    inst(0x5E,  'OP_5E',                        NoOperand,                                      handler = Handler_5E),
    inst(0x62,  'OP_62',                        NoOperand),
    inst(0x63,  'OP_63',                        'WB'),
    inst(0x66,  'OP_66',                        NoOperand,                                      handler = Handler_66),
    inst(0x69,  'OP_69',                        NoOperand,                                      handler = Handler_69),
    inst(0x6B,  'OP_6B',                        'BWWfLL'),
    inst(0x6F,  'OP_6F',                        'BWL'),
    inst(0x70,  'OP_70',                        NoOperand,                                      handler = Handler_70),
    inst(0x72,  'QuestInfo',                    NoOperand,                                      handler = Handler_72),
    inst(0x74,  'OP_74',                        NoOperand,                                      handler = Handler_74),
    inst(0x75,  'OP_75',                        NoOperand,                                      handler = Handler_75),
    inst(0x77,  'OP_77',                        'W'),
    inst(0x79,  'OP_79',                        NoOperand,                                      handler = Handler_79),
    inst(0x7C,  'OP_7C',                        NoOperand,                                      handler = Handler_7C),
    inst(0x84,  'OP_84',                        NoOperand,                                      handler = Handler_84),
    inst(0x86,  'OP_86',                        'BWWWWWWfffS'),
    inst(0x87,  'OP_87',                        'BL'),
    inst(0x88,  'OP_88',                        'W'),
    inst(0x89,  'OP_89',                        'W'),
    inst(0x8E,  'OP_8E',                        'W' * 7),
    inst(0x8F,  'OP_8F',                        NoOperand),
    inst(0x90,  'OP_90',                        'SL'),
    inst(0x91,  'OP_91',                        NoOperand,                                      handler = Handler_91),
    inst(0x93,  'OP_93',                        NoOperand,                                      handler = Handler_93),
    inst(0x9C,  'OP_9C',                        NoOperand,                                      handler = Handler_9C),
    inst(0x9E,  'OP_9E',                        NoOperand,                                      handler = Handler_9E),
    inst(0xA0,  'OP_A0',                        NoOperand),
    inst(0xA4,  'OP_A4',                        'BB' + 'W' * 20),
    inst(0xA8,  'OP_A8',                        'L'),
    inst(0xAC,  'OP_AC',                        NoOperand,                                      handler = Handler_AC),
    inst(0xAF,  'OP_AF',                        'B'),
    inst(0xB1,  'MenuChrFlagCmd',               'BWL'),
    inst(0xBC,  'OP_BC',                        NoOperand,                                      handler = Handler_BC),
    inst(0xC2,  'OP_C2',                        'B'),
    inst(0xC3,  'OP_C3',                        NoOperand,                                      handler = Handler_C3),
    inst(0xC4,  'OP_C4',                        NoOperand,                                      handler = Handler_C4),
    inst(0xC5,  'OP_C5',                        NoOperand,                                      handler = Handler_C5),
    inst(0xC6,  'OP_C6',                        NoOperand,                                      handler = Handler_C6),
])

del inst
