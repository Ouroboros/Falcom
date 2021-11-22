from Common import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import instruction

__all__ = (
    'CodeBlock',
    'Function',
)

class CodeBlock:
    def __init__(self, instructions: 'List[instruction.Instruction]', offset: int = None, name: str = None):
        self.name           = name          # type: str
        self.instructions   = instructions  # type: List[instruction.Instruction]
        self.branches       = []            # type: List[CodeBlock]
        self.xrefs          = None          # type: List[instruction.XRef]
        self.offset         = offset        # type: int
        self.parent         = None          # type: CodeBlock

    def addBranch(self, block: 'CodeBlock'):
        block.parent = self
        self.branches.append(block)
        return block

    def insertBranch(self, block: 'CodeBlock'):
        block.parent = self
        self.branches.insert(-1, block)
        return block

    def __str__(self):
        return repr(self)
        return '\n'.join(['%s' % inst for inst in self.instructions])

    def __repr__(self):
        return f'CodeBlock: 0x{self.offset:X}'

class Function:
    def __init__(self, name: str = '', offset: int = 0):
        self.name   = name                  # type: str
        self.offset = offset                # type: int
        self.block  = None                  # type: CodeBlock

    def __str__(self):
        return '\n'.join([
            '%s @ 0x%X' % (self.name, self.offset),
            '%s' % self.block,
        ])
