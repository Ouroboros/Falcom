from Common             import *
from .instruction       import *
from .instruction_table import *
from .function          import *
from .handlers          import *
from .optimizer         import *

__all__ = (
    'Formatter',
)

DefaultIndent = GlobalConfig.DefaultIndent

class Formatter:
    def __init__(self, instructionTable: InstructionTable, *, name = '', optimizer: Optimizer = None):
        self.instructionTable   = instructionTable        # type: InstructionTable
        self.formatted          = set()
        self.scriptName         = name
        self.optimizer          = optimizer

    def formatLabel(self, name: str) -> List[str]:
        return [f"label('{name}')"]

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
                *self.formatLabel(block.name),
                '',
            ]

            # text = _hackDeadCode(text, self.scriptName, block)

        def addEmptyLine():
            if text and text[-1] != '':
                text.append('')

        for inst in block.instructions:
            for x in inst.xrefs:
                text.extend([
                    *self.formatLabel(x.name),
                    '',
                ])

            if inst.opcode is Instruction.InvalidOpCode:
                continue

            t = self.formatInstruction(inst)
            if not inst.flags.multiline:
                if inst.flags.startBlock or inst.flags.endBlock:
                    addEmptyLine()

                text.append(''.join(t))

                if inst.flags.newline:
                    addEmptyLine()

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

        if self.optimizer is not None:
            result = self.optimizer.optimize(inst, operands, flags)
            if result is not None:
                mnemonic    = result.mnemonic
                operands    = result.operands
                flags       = result.flags

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
