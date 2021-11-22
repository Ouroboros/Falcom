from Common import *
from . import instruction_table

if TYPE_CHECKING:
    from . import function

__all__ = (
    'XRef',
    'Operand',
    'Flags',
    'Instruction',
)

OperandDescriptor = instruction_table.OperandDescriptor
NoOperand = instruction_table.InstructionDescriptor.NoOperand

class XRef:
    def __init__(self, name: str, offset: int):
        self.name   = name                          # type: str
        self.offset = offset                        # type: int

    def __str__(self):
        return f'<xref> from 0x{self.offset:X} to {self.name}'

    __repr__ = __str__

class Operand:
    def __init__(self, *, value: Any = None):
        self.value      = value                     # type: Any
        self.size       = None                      # type: int
        self.descriptor = None                      # type: OperandDescriptor

    def __str__(self):
        return f'<{self.descriptor}> {self.value}'

    __repr__ = __str__

class Flags(IntFlag2):
    Empty               = 0
    EndBlock            = 1 << 0
    StartBlock          = 1 << 1
    Call                = (1 << 2) | StartBlock
    Jump                = (1 << 3) | EndBlock

    FormatMultiLine     = 1 << 4

    @property
    def endBlock(self):
        return bool(self.value & self.EndBlock)

    @property
    def startBlock(self):
        return bool(self.value & self.StartBlock)

    @property
    def call(self):
        return bool(self.value & self.Call & ~self.StartBlock)

    @property
    def jump(self):
        return bool(self.value & self.Jump & ~self.EndBlock)

    @property
    def multiline(self):
        return bool(self.value & self.FormatMultiLine)

class Instruction:
    InvalidOffset   = None

    def __init__(self, opcode: int):
        self.opcode                 = opcode                    # type: int
        self.offset                 = self.InvalidOffset        # type: int
        self.size                   = 0                         # type: int
        self.operands               = []                        # type: List[Operand]
        self.branches               = []                        # type: List[function.CodeBlock]
        self.descriptor             = None                      # type: instruction_table.InstructionDescriptor
        self.label                  = None                      # type: XRef
        self.flags                  = None                      # type: Flags
        self.operandDescriptors     = NoOperand                 # type: List[OperandDescriptor]
                                                                # assemble only

    def __str__(self):
        return '%s(%s)' % (self.descriptor.mnemonic, ', '.join(['%s' % opr for opr in self.operands]))

    def __repr__(self):
        return self.__str__()
