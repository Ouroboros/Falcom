from Common import *
from . import instruction

if TYPE_CHECKING:
    from . import instruction_table
    from . import disassembler
    from . import function

__all__ = (
    'HandlerAction',
    'InstructionHandler',
    'InstructionHandlerContext',
    'FormatOperandHandler',
    'FormatOperandHandlerContext',
)

class HandlerAction(IntEnum2):
    Disassemble = 0
    Assemble    = 1
    Format      = 2
    CodeGen     = 3

class BaseHandlerInfo:
    def __init__(self, action: HandlerAction):
        self.action         = action    # type: HandlerAction
        self.disassembler   = None      # type: disassembler.Disassembler

class InstructionHandlerContext(BaseHandlerInfo):
    def __init__(self, action: HandlerAction, descriptor: 'instruction_table.InstructionDescriptor'):
        super().__init__(action)
        self.instructionTable   = None                                      # type: instruction_table.InstructionTable
        self.descriptor         = descriptor                                # type: instruction_table.InstructionDescriptor
        self.disasmContext      = None                                      # type: disassembler.DisasmContext
        self.instruction        = None                                      # type: instruction.Instruction
                                                                            # format only
        self.offset             = instruction.Instruction.InvalidOffset     # type: int

    def createCodeBlock(self, offset: int) -> 'function.CodeBlock':
        return self.disassembler.createCodeBlock(offset)

    def addBranch(self, offset: int) -> 'function.CodeBlock':
        return self.disassembler.addBranch(offset)

InstructionHandler = Callable[[InstructionHandlerContext], 'instruction.Instruction']


class FormatOperandHandlerContext:
    def __init__(self, inst: 'instruction.Instruction', operand: 'instruction.Operand', labels: 'Dict[int, str]' = None):
        self.instruction    = inst              # type: instruction.Instruction
        self.operand        = operand           # type: instruction.Operand
        self.labels         = labels or {}      # type: Dict[int, str]

FormatOperandHandler = Callable[[FormatOperandHandlerContext], Any]
