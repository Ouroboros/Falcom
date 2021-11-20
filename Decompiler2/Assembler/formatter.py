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
        if block.offset in self.formatted:
            return []

        self.formatted.add(block.offset)

        text = []

        if genLabel and block.name:
            text = [
                self.formatLabel(block.name),
                '',
            ]

        def addEmptyLine():
            # return
            if text and text[-1] != '':
                text.append('')

        for inst in block.instructions:
            t = self.formatInstruction(inst)
            if not inst.flags.multiline:
                if inst.flags.startBlock or inst.flags.endBlock:
                    addEmptyLine()

                text.append(''.join(t))
                continue

            addEmptyLine()
            text.extend(t)
            addEmptyLine()

        for blk in block.branches:
            addEmptyLine()
            text.extend(self.formatBlock(blk))

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
        operands = self.instructionTable.formatAllOperands(inst, inst.operands)

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
