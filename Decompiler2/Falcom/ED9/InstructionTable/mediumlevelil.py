from Falcom.Common  import *
from Assembler      import *
from .types         import *
from enum import auto

if TYPE_CHECKING:
    from ..Parser.scena_types import ScenaFunction, ScenaVariable

# from binary ninja MLIL

class MLIL(IntEnum2):
    UNDEF                   = auto()
    NOP                     = auto()
    SET_LINENO              = auto()
    SET_VAR                 = auto()
    DEL_VAR                 = auto()
    LOAD_GLOBAL_VAR         = auto()
    SET_GLOBAL_VAR          = auto()
    VAR                     = auto()
    ADDRESS_OF              = auto()
    CONST                   = auto()
    FLOAT_CONST             = auto()
    ADD                     = auto()
    SUB                     = auto()
    AND                     = auto()
    OR                      = auto()
    XOR                     = auto()
    MUL                     = auto()
    DIVS                    = auto()
    MODS                    = auto()
    NEG                     = auto()
    NOT                     = auto()
    LOGICAL_AND             = auto()
    LOGICAL_OR              = auto()
    JMP                     = auto()
    JMP_IF_ZERO             = auto()
    JMP_IF_NOT_ZERO         = auto()
    CALL                    = auto()
    CALL_MODULE             = auto()
    SET_REG                 = auto()
    GET_REG                 = auto()
    RET                     = auto()
    IF                      = auto()
    SYSCALL                 = auto()
    CMP_EZ                  = auto()
    CMP_EQ                  = auto()
    CMP_NE                  = auto()
    CMP_LT                  = auto()
    CMP_LE                  = auto()
    CMP_GE                  = auto()
    CMP_GT                  = auto()

class MediumLevelILInstruction:
    OpCode = MLIL.UNDEF
    def __init__(self):
        self.lineno = 0

class MediumLevelILNop(MediumLevelILInstruction):
    OpCode = MLIL.NOP

class MediumLevelILRet(MediumLevelILInstruction):
    OpCode = MLIL.RET

class MediumLevelILSetLineno(MediumLevelILInstruction):
    OpCode = MLIL.SET_LINENO

class MediumLevelILSetVar(MediumLevelILInstruction):
    OpCode = MLIL.SET_VAR
    def __init__(self, dest: 'ScenaVariable', src: 'ScenaVariable'):
        super().__init__()

        self.dest = dest
        self.src = src

class MediumLevelILDelVar(MediumLevelILInstruction):
    OpCode = MLIL.DEL_VAR
    def __init__(self, var: 'ScenaVariable'):
        super().__init__()
        self.var = var

class MediumLevelILLoadGlobalVar(MediumLevelILInstruction):
    OpCode = MLIL.LOAD_GLOBAL_VAR
    def __init__(self, dest: 'ScenaVariable', src: 'ScenaVariable'):
        super().__init__()
        self.dest = dest
        self.src = src

class MediumLevelILSetGlobalVar(MediumLevelILInstruction):
    OpCode = MLIL.SET_GLOBAL_VAR
    def __init__(self, dest: 'ScenaVariable', src: 'ScenaVariable'):
        super().__init__()
        self.dest = dest
        self.src = src

class MediumLevelILAddressOf(MediumLevelILInstruction):
    OpCode = MLIL.ADDRESS_OF
    def __init__(self, dest: 'ScenaVariable', src: 'ScenaVariable'):
        super().__init__()

        self.dest = dest
        self.src = src

class MediumLevelILSetReg(MediumLevelILInstruction):
    OpCode = MLIL.SET_REG
    def __init__(self, regid: int, value: 'ScenaVariable'):
        super().__init__()
        self.regid  = regid
        self.value  = value

class MediumLevelILGetReg(MediumLevelILInstruction):
    OpCode = MLIL.GET_REG
    def __init__(self, regid: int, value: 'ScenaVariable'):
        super().__init__()
        self.regid  = regid
        self.value  = value

class MediumLevelILAdd(MediumLevelILInstruction):
    OpCode = MLIL.ADD
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILSub(MediumLevelILInstruction):
    OpCode = MLIL.SUB
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILMul(MediumLevelILInstruction):
    OpCode = MLIL.MUL
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILDiv(MediumLevelILInstruction):
    OpCode = MLIL.DIVS
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILMod(MediumLevelILInstruction):
    OpCode = MLIL.MODS
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILNeg(MediumLevelILInstruction):
    OpCode = MLIL.NEG
    def __init__(self, var: 'ScenaVariable'):
        super().__init__()
        self.var = var

class MediumLevelILNot(MediumLevelILInstruction):
    OpCode = MLIL.NOT
    def __init__(self, var: 'ScenaVariable'):
        super().__init__()
        self.var = var

class MediumLevelILOr(MediumLevelILInstruction):
    OpCode = MLIL.OR
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILAnd(MediumLevelILInstruction):
    OpCode = MLIL.AND
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILLogicalOr(MediumLevelILInstruction):
    OpCode = MLIL.LOGICAL_OR
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILLogicalAnd(MediumLevelILInstruction):
    OpCode = MLIL.LOGICAL_AND
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILCmpEZ(MediumLevelILInstruction):
    OpCode = MLIL.CMP_EZ
    def __init__(self, var: 'ScenaVariable'):
        super().__init__()
        self.var = var

class MediumLevelILCmpEQ(MediumLevelILInstruction):
    OpCode = MLIL.CMP_EQ
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILCmpNE(MediumLevelILInstruction):
    OpCode = MLIL.CMP_NE
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILCmpLT(MediumLevelILInstruction):
    OpCode = MLIL.CMP_LT
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILCmpLE(MediumLevelILInstruction):
    OpCode = MLIL.CMP_LE
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILCmpGT(MediumLevelILInstruction):
    OpCode = MLIL.CMP_GT
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILCmpGE(MediumLevelILInstruction):
    OpCode = MLIL.CMP_GE
    def __init__(self, left: 'ScenaVariable', right: 'ScenaVariable'):
        super().__init__()
        self.left = left
        self.right = right

class MediumLevelILJmpIfZero(MediumLevelILInstruction):
    OpCode = MLIL.JMP_IF_ZERO
    def __init__(self, var: 'ScenaVariable', target: CodeBlock):
        super().__init__()
        self.var = var
        self.target = target

class MediumLevelILJmpIfNotZero(MediumLevelILInstruction):
    OpCode = MLIL.JMP_IF_NOT_ZERO
    def __init__(self, var: 'ScenaVariable', target: CodeBlock):
        super().__init__()
        self.var = var
        self.target = target

class MediumLevelILCall(MediumLevelILInstruction):
    OpCode = MLIL.CALL
    def __init__(self, target: 'ScenaFunction', params: 'list[ScenaVariable]', returnValue: 'ScenaVariable' = None):
        super().__init__()

        self.target         = target
        self.params         = params
        self.returnValue    = returnValue

class MediumLevelILCallModule(MediumLevelILInstruction):
    OpCode = MLIL.CALL_MODULE
    def __init__(self, module: str, func: str, params: 'list[ScenaVariable]', returnValue: 'ScenaVariable' = None, *, noReturn = False):
        super().__init__()

        self.module         = module
        self.func           = func
        self.params         = params
        self.returnValue    = returnValue
        self.noReturn       = noReturn

class MediumLevelILSyscall(MediumLevelILInstruction):
    OpCode = MLIL.SYSCALL
    def __init__(self, catalog: 'ScenaVariable', cmd: 'ScenaVariable', params: 'list[ScenaVariable]'):
        super().__init__()

        self.catalog = catalog
        self.cmd = cmd
        self.params = params
