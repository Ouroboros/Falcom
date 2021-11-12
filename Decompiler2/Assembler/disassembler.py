from Common             import *
from .instruction       import *
from .instruction_table import *
from .function          import *
from .handlers          import *

__all__ = (
    'Disassembler',
    'DisasmContext',
)

class DisasmContext:
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
            block = CodeBlock(instructions = [], offset = offset, name = f'loc_{offset:X}')
            self.allocatedBlocks[offset] = block

        return block

    def addBranch(self, offset: int) -> CodeBlock:
        return self.currentBlock.addBranch(self.createCodeBlock(offset))

    def disasmFunction(self, context: DisasmContext, *, name: str = None) -> Function:
        func = Function()

        func.offset = context.fs.Position
        if name:
            func.name = name

        log.debug(f'disasm func 0x{func.offset:08X} {func.name}')

        func.block = self.disasmBlock(context)

        if name:
            func.block.name = name

        return func

    def disasmBlock(self, context: DisasmContext) -> CodeBlock:
        offset = context.fs.Position
        block = self.disassembledBlocks.get(offset)

        if block is not None:
            return block

        block = self.createCodeBlock(offset)

        self.disassembledBlocks[offset] = block

        previousBlock = self.currentBlock
        self.currentBlock = block

        while True:
            inst = self.disasmInstruction(context)

            block.instructions.append(inst)

            if inst.flags.endBlock:
                break

            if inst.flags.startBlock:
                block.insertBranch(self.createCodeBlock(context.fs.Position))
                break

            if context.fs.Position in self.allocatedBlocks:
                break

        for index, branch in enumerate(block.branches):
            pos = context.fs.Position

            context.fs.Position = branch.offset
            block.branches[index] = self.disasmBlock(context)

            context.fs.Position = pos

        self.currentBlock = previousBlock

        return block

    def disasmInstruction(self, context: DisasmContext) -> Instruction:
        pos = context.fs.Position

        try:
            opcode = self.instructionTable.readOpCode(context.fs)
        except Exception as e:
            log.error('error occurred %s @ position %X' % (e, pos))
            raise e

        log.debug(f'disasm inst 0x{opcode:02X} @ 0x{pos:08X}')

        desc = self.instructionTable.getDescriptor(opcode)

        handlerContext = InstructionHandlerContext(InstructionHandlerContext.Action.Disassemble, desc)

        handlerContext.offset          = pos
        handlerContext.disasmContext   = context
        handlerContext.disassembler    = self

        inst: Instruction = None

        if desc.handler is not None:
            inst = desc.handler(handlerContext)

        if inst is None:
            inst = self.defaultInstructionParser(handlerContext)

        if inst is None:
            raise Exception('disasmInstruction %02X @ %08X failed' % (opcode, pos))

        inst.descriptor = inst.descriptor if inst.descriptor is None else desc
        inst.flags = inst.descriptor.flags if inst.flags is None else inst.flags

        return inst

    def defaultInstructionParser(self, context: InstructionHandlerContext) -> Instruction:
        fs      = context.disasmContext.fs
        desc    = context.descriptor

        inst = Instruction(desc.opcode)

        inst.offset     = context.offset
        inst.operands   = [self.instructionTable.readOperand(context, inst, oprdesc) for oprdesc in (desc.operands or [])]
        inst.size       = fs.Position - inst.offset
        inst.descriptor = desc
        inst.flags      = desc.flags

        return inst
