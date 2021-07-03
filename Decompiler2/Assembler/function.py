from Common import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import instruction

__all__ = (
    'CodeBlock',
    'Function',
)

class CodeBlock:
    def __init__(self, instructions: 'List[instruction.Instruction]'):
        self.name           = None          # type: str
        self.instructions   = instructions  # type: List[instruction.Instruction]
        self.branches       = []            # type: List[CodeBlock]
        self.labels         = None          # type: List[instruction.Label]
        self.offset         = None          # type: int
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
        return '\n'.join(['%s' % inst for inst in self.instructions])

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
