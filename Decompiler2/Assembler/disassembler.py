from Common             import *
from .instruction       import *
from .instruction_table import *
from .function          import *
from .handlers          import *

__all__ = (
    'Disassembler',
    'DisassembleInfo',
)

class DisassembleInfo:
    def __init__(self, fs: fileio.FileStream):
        self.fs     = fs    # type: fileio.FileStream

class Disassembler:
    def __init__(self, instructionTable: InstructionTable):
        self.instructionTable   = instructionTable      # type: InstructionTable
        self.disassembledBlocks = {}                    # type: Dict[int, CodeBlock]
        self.allocatedBlocks    = {}                    # type: Dict[int, CodeBlock]
        self.currentBlock       = None                  # type: CodeBlock

    def createCodeBlock(self, offset: int):
        block = self.allocatedBlocks.get(offset)
        if block is None:
            block = CodeBlock(instructions = [])
            block.offset = offset
            block.name = 'loc_%X' % offset
            self.allocatedBlocks[offset] = block

        return block

    def disasmFunction(self, info: DisassembleInfo) -> Function:
        fun = Function()

        fun.offset = info.fs.Position
        fun.block = self.disasmBlock(info)
        fun.block.name = None

        return fun

    def disasmBlock(self, info: DisassembleInfo) -> CodeBlock:
        offset = info.fs.Position
        block = self.disassembledBlocks.get(offset)

        if block is not None:
            return block

        block = self.createCodeBlock(offset)

        self.disassembledBlocks[offset] = block

        previousBlock = self.currentBlock
        self.currentBlock = block

        while True:
            inst = self.disasmInstruction(info)

            block.instructions.append(inst)

            if inst.flags.endBlock:
                break

            if inst.flags.startBlock:
                block.insertBranch(self.createCodeBlock(info.fs.Position))
                break

            if info.fs.Position in self.allocatedBlocks:
                break

        for index, branch in enumerate(block.branches):
            pos = info.fs.Position

            info.fs.Position = branch.offset
            block.branches[index] = self.disasmBlock(info)

            info.fs.Position = pos

        self.currentBlock = previousBlock

        return block

    def disasmInstruction(self, info: DisassembleInfo) -> Instruction:
        pos = info.fs.Position

        try:
            opcode = self.instructionTable.readOpCode(info.fs)
        except Exception as e:
            print('error occurred %s @ position %X' % (e, pos))
            raise e

        desc = self.instructionTable.getDescriptor(opcode)

        handlerInfo = InstructionHandlerInfo(InstructionHandlerInfo.Action.Disassemble, desc)

        handlerInfo.offset          = pos
        handlerInfo.disasmInfo      = info
        handlerInfo.disassembler    = self

        inst = None

        if desc.handler is not None:
            inst = desc.handler(handlerInfo)

        if inst is None:
            inst = self.defaultInstructionParser(handlerInfo)

        if inst is None:
            raise Exception('disasmInstruction %02X @ %08X failed' % (opcode, pos))

        inst.descriptor = inst.descriptor if inst.descriptor is None else desc
        inst.flags = inst.descriptor.flags if inst.flags is None else inst.flags

        return inst

    def defaultInstructionParser(self, info: InstructionHandlerInfo) -> Instruction:
        fs      = info.disasmInfo.fs
        desc    = info.descriptor

        inst = Instruction(desc.opcode)

        inst.offset     = info.offset
        inst.operands   = [self.instructionTable.readOperand(info, inst, oprdesc) for oprdesc in (desc.operands or [])]
        inst.size       = fs.Position - inst.offset
        inst.descriptor = desc
        inst.flags      = desc.flags

        return inst

    def formatFuncion(self, fun: Function) -> List[str]:
        return self.formatBlock(fun.block)

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
            handlerInfo = InstructionHandlerInfo(InstructionHandlerInfo.Action.Format, inst.descriptor)

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
