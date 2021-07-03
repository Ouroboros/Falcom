from Common import *
from . import instruction

if TYPE_CHECKING:
    from . import instruction_table
    from . import disassembler
    from . import function

__all__ = (
    'InstructionHandler',
    'InstructionHandlerInfo',
    'FormatOperandHandler',
    'FormatOperandHandlerInfo',
)

class BaseHandlerInfo:
    class Action(IntEnum2):
        Disassemble = 0
        Assemble    = 1
        Format      = 2

    def __init__(self, action: Action):
        self.action         = action    # type: Action
        self.disassembler   = None      # type: disassembler.Disassembler

class InstructionHandlerInfo(BaseHandlerInfo):
    def __init__(self, action: 'BaseHandlerInfo.Action', descriptor: 'instruction_table.InstructionDescriptor'):
        super().__init__(action)
        self.descriptor     = descriptor                                # type: instruction_table.InstructionDescriptor
        self.disasmInfo     = None                                      # type: disassembler.DisassembleInfo
        self.instruction    = None                                      # type: instruction.Instruction     format only
        self.offset         = instruction.Instruction.InvalidOffset     # type: int

    def createCodeBlock(self, offset: int) -> 'function.CodeBlock':
        return self.disassembler.createCodeBlock(offset)

    def addBranch(self, offset: int) -> 'function.CodeBlock':
        return self.disassembler.currentBlock.addBranch(self.createCodeBlock(offset))

InstructionHandler = Callable[[InstructionHandlerInfo], Any]


class FormatOperandHandlerInfo:
    def __init__(self, inst: 'instruction.Instruction', operand: 'instruction.Operand', labels: 'Dict[int, str]' = None):
        self.instruction    = inst              # type: instruction.Instruction
        self.operand        = operand           # type: instruction.Operand
        self.labels         = labels or {}      # type: Dict[int, str]

FormatOperandHandler = Callable[[FormatOperandHandlerInfo], Any]
