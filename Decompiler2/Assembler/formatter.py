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
    def __init__(self, instructionTable: InstructionTable) -> None:
        self.instructionTable   = instructionTable        # type: InstructionTable
        self.formatted          = set()

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

                    # text.insert(0, "Jump('loc_115FF')")

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

    def formatInstruction(self, inst: Instruction) -> List[str]:
        handler = inst.descriptor.handler
        if handler is not None:
            handlerContext = InstructionHandlerContext(HandlerAction.Format, inst.descriptor)

            handlerContext.instructionTable = self.instructionTable
            handlerContext.disassembler = self
            handlerContext.instruction = inst

            ret = handler(handlerContext)
            if ret is not None:
                return ret

        mnemonic = inst.descriptor.mnemonic
        context = FormatOperandHandlerContext(inst, None, formatter = self)
        operands = self.instructionTable.formatAllOperands(context, inst.operands)

        if inst.flags.multiline:
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
