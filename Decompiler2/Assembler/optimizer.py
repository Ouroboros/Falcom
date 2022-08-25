from Common         import *
from .instruction   import *
from .function      import *

__all__ = (
    'Optimizer',
    'OptimizeResult',
)

class OptimizeResult:
    def __init__(self, mnemonic: str, operands: List[Any], flags: Flags):
        self.mnemonic   = mnemonic
        self.operands   = operands
        self.flags      = flags

class Optimizer:
    def optimizeFunction(self, func: Function):
        return None

    def optimizeInstruction(self, inst: Instruction, operands: List[Any], flags: Flags) -> OptimizeResult:
        return None
