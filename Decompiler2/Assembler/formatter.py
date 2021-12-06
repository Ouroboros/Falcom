from Common             import *
from .instruction       import *
from .instruction_table import *
from .function          import *
from .handlers          import *

__all__ = (
    'Formatter',
)

DefaultIndent = GlobalConfig.DefaultIndent

class Formatter:
    def __init__(self, instructionTable: InstructionTable, *, name = ''):
        self.instructionTable   = instructionTable        # type: InstructionTable
        self.formatted          = set()
        self.scriptName         = name

    def formatLabel(self, name: str) -> str:
        return f"label('{name}')"

    def formatFuncion(self, func: Function) -> List[str]:
        funcName = func.name
        if not funcName:
            funcName = f'func_{func.offset:X}'

        f = [
            f'def {funcName}(): pass',
            '',
        ]

        blk = self.formatBlock(func.block)

        f.extend(blk)

        return f

    def formatBlock(self, block: CodeBlock, *, genLabel = True) -> List[str]:
        todo = [block]
        blocks = []

        while todo:
            b = todo.pop()
            if b.offset in self.formatted:
                continue

            self.formatted.add(b.offset)

            blocks.append(b)
            todo.extend(b.branches)

        blocks = sorted(blocks, key = lambda b: b.offset)

        f = []
        for i, b in enumerate(blocks):
            f.extend(self.formatBlockWorker(b, genLabel = i != 0))
            if f and f[-1] != '':
                f.append('')

        return f[:-1]

    def formatBlockWorker(self, block: CodeBlock, *, genLabel = True) -> List[str]:
        # if block.offset in self.formatted:
        #     return []

        # self.formatted.add(block.offset)

        # log.debug(f'format block: 0x{block.offset:X}')

        text = []

        if not block.instructions:
            return text

        if genLabel and block.name:
            text = [
                self.formatLabel(block.name),
                '',
            ]

            text = _hackDeadCode(text, self.scriptName, block)

        def addEmptyLine():
            if text and text[-1] != '':
                text.append('')

        for inst in block.instructions:
            for x in inst.xrefs:
                text.extend([
                    self.formatLabel(x.name),
                    '',
                ])

            t = self.formatInstruction(inst)
            if not inst.flags.multiline:
                if inst.flags.startBlock or inst.flags.endBlock:
                    addEmptyLine()

                text.append(''.join(t))
                continue

            addEmptyLine()
            text.extend(t)
            addEmptyLine()

        # for blk in block.branches:
        #     addEmptyLine()
        #     text.extend(self.formatBlock(blk))

        return text

    def formatInstruction(self, inst: Instruction, *, flags: Flags = None) -> List[str]:
        # log.debug(f'format inst 0x{inst.opcode:02X}<{inst.opcode}> @ 0x{inst.offset:08X}')

        handler = inst.descriptor.handler
        if handler is not None:
            handlerContext = InstructionHandlerContext(HandlerAction.Format, inst.descriptor, formatter = self)

            handlerContext.instructionTable = self.instructionTable
            handlerContext.disassembler = self
            handlerContext.instruction = inst

            ret = handler(handlerContext)
            if ret is not None:
                return ret

        mnemonic = inst.descriptor.mnemonic
        context = FormatOperandHandlerContext(inst, None, formatter = self)
        operands = self.instructionTable.formatAllOperands(context, inst.operands)

        if flags is None:
            flags = inst.flags

        if flags.multiline:
            f = [f'{mnemonic}(']

            for opr in operands:
                if not isinstance(opr, tuple | list):
                    f.append(f'{DefaultIndent}{opr},')
                    continue

                f.extend([
                    f'{DefaultIndent}(',
                    *[f'{DefaultIndent * 2}{p},'.rstrip() for p in opr],
                    f'{DefaultIndent}),',
                ])

            f.append(')')

            return f

        else:
            return [f'{mnemonic}({", ".join(operands)})']

def _hackDeadCode(text: List[str], scriptName: str, block: CodeBlock) -> List[str]:
    match scriptName:
        case 'a0000':
            match block.name:
                # XXX
                case 'loc_115FA':
                    text.insert(0, "Jump('loc_115FF')")

                case 'loc_20883':
                    text = [
                        'SetScenaFlags(0xF02)',
                        'SetScenaFlags(0xF01)',
                        'SetScenaFlags(0xF00)',
                        'SetScenaFlags(0xD65)',
                        'SetScenaFlags(0xD64)',
                        'SetScenaFlags(0xD63)',
                        'SetScenaFlags(0xD62)',
                        'SetScenaFlags(0xD61)',
                        'SetScenaFlags(0xD60)',
                        'SetScenaFlags(0xD5F)',
                        'SetScenaFlags(0xD5E)',
                        '',
                    ] + text

                case 'loc_41B36':
                    text = [
                        'OP_11(0x0B53)',
                        'OP_11(0x0B52)',
                        'OP_11(0x0B51)',
                        'SetScenaFlags(0xC94)',
                        'SetScenaFlags(0xC9D)',
                        'Jump("loc_41B5F")',
                        '',
                    ] + text

        case 'system':
            match block.name:
                case 'loc_9611':
                    text = [
                        'emit(0x00, 0x00, 0x00, 0xF8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x56, 0x17, 0x03, 0x00, 0x00, 0x00, 0x80, 0x3F, 0x00, 0x00, 0x80, 0x3F, 0x00, 0x00, 0x80, 0x3F, 0x00, 0x00, 0x80, 0x3F, 0xCD, 0xCC, 0x4C, 0x3E, 0x57, 0x17, 0x03, 0x03, 0xE4, 0x98, 0x00, 0x00)',
                        '',
                    ] + text

        case 'a1001':
            match block.name:
                case 'loc_16E9':
                    text = [
                        'emit(0x36, 0x02, 0x03, 0xEC, 0x51, 0x38, 0x3E, 0x00, 0x00, 0xC0, 0x3F, 0x9A, 0x99, 0xA1, 0x40, 0x00, 0x00, 0x36, 0x04, 0x03, 0xC3, 0xF5, 0xA8, 0x3E, 0xF6, 0x68, 0x4D, 0x43, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x36, 0x05, 0x03, 0x66, 0x66, 0xA6, 0x3F, 0x00, 0x00, 0x36, 0x0B, 0x03, 0x33, 0x33, 0xEB, 0x41, 0x00, 0x00, 0x16, 0x64, 0x00, 0x3C, 0x04, 0xFE, 0xFF, 0x23, 0x45, 0x5B, 0x43, 0x5D, 0x23, 0x4D, 0x5F, 0x30, 0x00, 0x24, 0xFE, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x23, 0x33, 0x4B, 0xE3, 0x81, 0x8A, 0xE9, 0xA1, 0x98, 0xE3, 0x81, 0x84, 0xE2, 0x80, 0xA6, 0xE2, 0x80, 0xA6, 0xE4, 0xBF, 0xBA, 0xE3, 0x81, 0x9F, 0xE3, 0x81, 0xA1, 0xE3, 0x81, 0xAB, 0xEF, 0xBC, 0x9F, 0x02, 0x00, 0x26, 0x3C, 0x04, 0xFE, 0xFF, 0x23, 0x45, 0x5B, 0x31, 0x5D, 0x23, 0x4D, 0x5F, 0x41, 0x00, 0x24, 0xFE, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x23, 0x32, 0x4B, 0x23, 0x46, 0xE2, 0x80, 0xA6, 0xE2, 0x80, 0xA6, 0xE7, 0xA7, 0x81, 0xE3, 0x81, 0x9F, 0xE3, 0x81, 0xA1, 0xE3, 0x81, 0xAF, 0xE3, 0x80, 0x81, 0xE8, 0xA8, 0x98, 0xE5, 0xBF, 0xB5, 0xE3, 0x83, 0xA9, 0xE3, 0x82, 0xA4, 0xE3, 0x83, 0x96, 0xE3, 0x81, 0xAE, 0x01, 0xE6, 0x9C, 0x80, 0xE5, 0xBE, 0x8C, 0xE3, 0x81, 0xAE, 0xE6, 0xBA, 0x96, 0xE5, 0x82, 0x99, 0xE3, 0x82, 0x92, 0xE5, 0xA7, 0x8B, 0xE3, 0x82, 0x81, 0xE3, 0x81, 0xAA, 0xE3, 0x81, 0x84, 0xE3, 0x81, 0xA8, 0xE3, 0x81, 0x84, 0xE3, 0x81, 0x91, 0xE3, 0x81, 0xAA, 0xE3, 0x81, 0x84, 0xE3, 0x80, 0x82, 0x02, 0x03, 0x23, 0x45, 0x5B, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x32, 0x5D, 0x23, 0x4D, 0x5F, 0x41, 0xE3, 0x81, 0xA0, 0xE3, 0x81, 0x8B, 0xE3, 0x82, 0x89, 0xE3, 0x80, 0x81, 0xE4, 0xBB, 0xA3, 0xE3, 0x82, 0x8F, 0xE3, 0x82, 0x8A, 0xE3, 0x81, 0xAB, 0xE2, 0x80, 0x9C, 0xE4, 0xBC, 0x9D, 0xE8, 0xA8, 0x80, 0xE2, 0x80, 0x9D, 0xE3, 0x82, 0x92, 0x01, 0xE5, 0xB1, 0x8A, 0xE3, 0x81, 0x91, 0xE3, 0x81, 0xA6, 0xE6, 0xAC, 0xB2, 0xE3, 0x81, 0x97, 0xE3, 0x81, 0x84, 0xE3, 0x81, 0xAE, 0xE2, 0x94, 0x80, 0xE2, 0x94, 0x80, 0xE3, 0x83, 0xAA, 0xE3, 0x82, 0xAA, 0xE3, 0x83, 0xB3, 0xE3, 0x81, 0xAB, 0xE3, 0x80, 0x82, 0x02, 0x00, 0x26, 0x3C, 0x04, 0xFE, 0xFF, 0x23, 0x45, 0x5F, 0x38, 0x23, 0x4D, 0x5F, 0x41, 0x23, 0x42, 0x5B, 0x31, 0x5D, 0x00, 0x24, 0xFE, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x23, 0x32, 0x50, 0xE2, 0x80, 0xA6, 0xE2, 0x80, 0xA6, 0xE5, 0x8B, 0x9D, 0xE6, 0x89, 0x8B, 0xE3, 0x81, 0xAB, 0xE4, 0xB8, 0x80, 0xE4, 0xBA, 0xBA, 0xE3, 0x81, 0xA7, 0xE6, 0x8A, 0xB1, 0xE3, 0x81, 0x88, 0xE8, 0xBE, 0xBC, 0xE3, 0x82, 0x93, 0xE3, 0x81, 0xA7, 0xE3, 0x80, 0x81, 0x01, 0xE6, 0x8C, 0x99, 0xE5, 0x8F, 0xA5, 0xE3, 0x81, 0xAB, 0xE5, 0x80, 0x92, 0xE3, 0x82, 0x8C, 0xE3, 0x81, 0x9F, 0xE3, 0x82, 0x8A, 0xE3, 0x81, 0xAA, 0xE3, 0x82, 0x93, 0xE3, 0x81, 0x8B, 0xE3, 0x81, 0x97, 0xE3, 0x81, 0xA6, 0xE3, 0x80, 0x82, 0x02, 0x03, 0x23, 0x45, 0x5B, 0x33, 0x5D, 0x23, 0x4D, 0x5F, 0x41, 0xE6, 0x96, 0x87, 0xE5, 0x8F, 0xA5, 0xE3, 0x81, 0xAE, 0xE4, 0xB8, 0x80, 0xE3, 0x81, 0xA4, 0xE3, 0x82, 0x82, 0xE8, 0xA8, 0x80, 0xE3, 0x81, 0xA3, 0xE3, 0x81, 0xA6, 0xE3, 0x81, 0x8A, 0xE3, 0x81, 0x8B, 0xE3, 0x81, 0xAA, 0xE3, 0x81, 0x84, 0xE3, 0x81, 0xA8, 0x01, 0xE6, 0xB0, 0x97, 0xE3, 0x81, 0x8C, 0xE3, 0x81, 0x99, 0xE3, 0x81, 0xBE, 0xE3, 0x81, 0xAA, 0xE3, 0x81, 0x84, 0xE3, 0x81, 0xAE, 0xE3, 0x82, 0x88, 0xE3, 0x81, 0xAD, 0xE3, 0x80, 0x82, 0x02, 0x00, 0x26, 0x3C, 0x04, 0xFE, 0xFF, 0x23, 0x45, 0x5F, 0x45, 0x23, 0x4D, 0x5F, 0x34, 0x00, 0x24, 0xFE, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x23, 0x34, 0x4B, 0x23, 0x46, 0xE3, 0x81, 0xB5, 0xE3, 0x81, 0xB5, 0xE3, 0x80, 0x81, 0xE7, 0xB4, 0xA0, 0xE7, 0x9B, 0xB4, 0xE3, 0x81, 0x98, 0xE3, 0x82, 0x83, 0xE3, 0x81, 0xAA, 0xE3, 0x81, 0x84, 0xE3, 0x82, 0x93, 0xE3, 0x81, 0xA0, 0xE3, 0x81, 0x8B, 0xE3, 0x82, 0x89, 0xE3, 0x80, 0x82, 0x02, 0x00, 0x26, 0x03, 0x03, 0x20, 0x00, 0x00)',
                        '',
                    ] + text

        case 'a2005':
            match block.name:
                case 'loc_19A7': text = ['Jump("loc_19A7")', ''] + text
                case 'loc_1B10': text = ['Jump("loc_1B10")', ''] + text
                case 'loc_1D5C': text = ['Jump("loc_1D5C")', ''] + text

        case 'c0230':
            match block.name:
                case 'loc_610': text = ['Jump("loc_856")', ''] + text

        case 'c0410':
            match block.name:
                case 'loc_F49': text = ['Jump("loc_F49")', ''] + text

        case 'c0800':
            match block.name:
                case 'loc_2A9C': text = ['Jump("loc_2A9C")', ''] + text

        case 'c1000':
            match block.name:
                case 'loc_1C53': text = [
                    "AddChrAnimeClip(0x08, 0xFFFE, 0x00, 'AniEvYasume', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')",
                    "OP_39(0xFFFE, 0x00, 'AniEvYasume', -1.0, 1.0, 0x00000001)",
                    "OP_35(0x00, 0xFFFE, 0x00000004)",
                    ''
                ] + text

        case 'c1010':
            match block.name:
                case 'loc_DC5': text = ['Jump("loc_DC5")', ''] + text

        case 'c2200':
            match block.name:
                case 'loc_8178': text = ['Jump("loc_8178")', ''] + text
                case 'loc_82DC': text = ['Jump("loc_82DC")', ''] + text

        case 'c2210':
            match block.name:
                case 'loc_78A0': text = ['Jump("loc_78F3")', ''] + text

        case 'c2400':
            match block.name:
                case 'loc_7B44': text = ['Jump("loc_7B44")', ''] + text

        case 'c2820':
            match block.name:
                case 'loc_C6F': text = ['Jump("loc_E0A")', ''] + text

        case 'c2830':
            match block.name:
                case 'loc_A01': text = ['Jump("loc_103C")', ''] + text
                case 'loc_D32': text = ['Jump("loc_103C")', ''] + text

        case 'c3410':
            match block.name:
                case 'loc_2118': text = ['Jump("loc_2118")', ''] + text

        case 'c3600':
            match block.name:
                case 'loc_1503': text = ['Jump("loc_1503")', ''] + text

        case 'r0090':
            match block.name:
                case 'loc_8CB2': text = ['Jump("loc_8CBA")', ''] + text

        case 't0040':
            match block.name:
                case 'loc_3417': text = ['Jump("loc_3DE8")', ''] + text
                case 'loc_3462': text = ['Jump("loc_3DE8")', ''] + text
                case 'loc_37B7': text = ['Jump("loc_3DE8")', ''] + text

        case 't0050':
            match block.name:
                case 'loc_FDD': text = ['Jump("loc_19A1")', ''] + text
                case 'loc_1369': text = ['Jump("loc_19A1")', ''] + text
                case 'loc_179B': text = ['Jump("loc_19A1")', ''] + text
                case 'loc_17E4': text = ['Jump("loc_19A1")', ''] + text

        case 't0060':
            match block.name:
                case 'loc_1675': text = ['Jump("loc_1959")', ''] + text

        case 't0070':
            match block.name:
                case 'loc_1ECE': text = ['Jump("loc_2B37")', ''] + text
                case 'loc_1F1D': text = ['Jump("loc_2B37")', ''] + text
                case 'loc_23DA': text = ['Jump("loc_2B37")', ''] + text
                case 'loc_25E3': text = ['Jump("loc_2B37")', ''] + text
                case 'loc_6BFB': text = ['Jump("loc_6C64")', ''] + text

        case 't0090':
            match block.name:
                case 'loc_14C6': text = ['Jump("loc_253D")', ''] + text
                case 'loc_1AEF': text = ['Jump("loc_253D")', ''] + text
                case 'loc_1FA4': text = ['Jump("loc_253D")', ''] + text
                case 'loc_2059': text = ['Jump("loc_253D")', ''] + text
                case 'loc_2534': text = ['Jump("loc_253D")', ''] + text

        case 't0100':
            match block.name:
                case 'loc_32F9': text = ['Jump("loc_3624")', ''] + text
                case 'loc_3346': text = ['Jump("loc_3624")', ''] + text
                case 'loc_34DD': text = ['Jump("loc_3624")', ''] + text

        case 't0200':
            match block.name:
                case 'loc_5EE4': text = ['Jump("loc_5EE4")', ''] + text

        case 't0210':
            match block.name:
                case 'loc_C626': text = ['Jump("loc_C688")', ''] + text

        case 't0230':
            match block.name:
                case 'loc_3955': text = ['Jump("loc_4212")', ''] + text
                case 'loc_3C77': text = ['Jump("loc_4212")', ''] + text
                case 'loc_3FD1': text = ['Jump("loc_4212")', ''] + text

        case 't0250':
            match block.name:
                case 'loc_144B6': text = ['Jump("loc_14532")', ''] + text

        case 't1000':
            match block.name:
                case 'loc_1962': text = ["emit(*bytes.fromhex('05 21 FE FF 09 00 09 00 00 00 02 01 5D 19 00 00 02 0B 4E 50 43 5F 45 4D 4F 5F 52 55 4E 52 55 4E 00 00 03 62 19 00 00'))", ''] + text

        case 't1040':
            match block.name:
                case 'loc_2150': text = ["Jump('loc_23ED')", ''] + text

        case 't1210':
            match block.name:
                case 'loc_1C92': text = ["Jump('loc_2631')", ''] + text
                case 'loc_200C': text = ["Jump('loc_2631')", ''] + text
                case 'loc_2365': text = ["Jump('loc_2631')", ''] + text
                case 'loc_23C2': text = ["Jump('loc_2631')", ''] + text

        case 't3200':
            match block.name:
                case 'loc_6CB2': text = ["Jump('loc_6E17')", ''] + text

        case 't3220':
            match block.name:
                case 'loc_191F': text = ["Jump('loc_1D3A')", ''] + text

        case 't3610':
            match block.name:
                case 'loc_25A5': text = ["Jump('loc_263D')", ''] + text
                case 'loc_25F4': text = ["Jump('loc_263D')", ''] + text

        case 't4020':
            match block.name:
                case 'loc_1948': text = ["Jump('loc_1F28')", ''] + text
                case 'loc_1B80': text = ["Jump('loc_1F28')", ''] + text

        case 't4060':
            match block.name:
                case 'loc_2A5E': text = ["Jump('loc_2A5E')", ''] + text

        case 'v0020':
            match block.name:
                case 'loc_2BFB': text = ["Jump('loc_2BFB')", ''] + text
                case 'loc_2DF2': text = ["Jump('loc_2DF2')", ''] + text
                case 'loc_3058': text = ["Jump('loc_3058')", ''] + text

        case 'tk_egret':
            match block.name:
                case 'loc_167': text = ["Jump('loc_226')", ''] + text

        case 'tk_fred':
            match block.name:
                case 'loc_580': text = ["Jump('loc_B9F')", ''] + text
                case 'loc_710': text = ["Jump('loc_B9F')", ''] + text

        case 'tk_freds':
            match block.name:
                case 'loc_37BD': text = ["Jump('loc_37BD')", ''] + text

    return text
