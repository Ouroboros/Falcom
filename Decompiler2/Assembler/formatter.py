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
        self.instructionTable = instructionTable        # type: InstructionTable

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

    def formatBlock(self, block: CodeBlock) -> List[str]:
        text = []

        if block.name:
            text = [
                "label('%s')" % block.name,
                '',
            ]

        for inst in block.instructions:
            t = self.formatInstruction(inst)
            if not inst.flags.argNewLine:
                text.append(''.join(t))
                continue

            text.append('')

            params = ['%s%s,' % (DefaultIndent, p) for p in t[1:-1]]

            text.append('\n'.join([t[0], *params, t[-1]]))

            text.append('')

        for blk in block.branches:
            text.append('')
            text.extend(self.formatBlock(blk))

        return text

    def formatInstruction(self, inst: Instruction) -> List[str]:
        handler = inst.descriptor.handler
        if handler is not None:
            handlerInfo = InstructionHandlerContext(InstructionHandlerContext.Action.Format, inst.descriptor)

            handlerInfo.disassembler = self
            handlerInfo.instruction = inst

            ret = handler(handlerInfo)
            if ret is not None:
                return ret

        mnemonic = inst.descriptor.mnemonic
        operands = self.instructionTable.formatAllOperand(inst)

        if inst.flags.argNewLine:
            return ['%s(' % mnemonic, *operands, ')']

        else:
            return ['%s(%s)' % (mnemonic, ', '.join(operands))]
