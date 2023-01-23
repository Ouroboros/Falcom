from Falcom.ED9.Parser.scena_writer import *
from Falcom.ED9.Parser.scena_writer_gen import *
from Falcom.ED9.Parser.consts import *

_ORIG_PUSH = PUSH

def PUSH(v: int | RawInt):
    assert isinstance(v, int | RawInt)
    return _ORIG_PUSH(RawInt(v))

def PUSH_INT(v: sint32):
    assert isinstance(v, sint32)
    return _ORIG_PUSH(v)

def PUSH_FLOAT(f: float32):
    assert isinstance(f, float32)
    return _ORIG_PUSH(f)

def PUSH_STR(s: str):
    assert isinstance(s, str)
    return _ORIG_PUSH(s)

def PUSH_CURRENT_FUNC_ID():
    PUSH(getScena().currentFunctionId)

def Call(module: str, func: str, *args):
    raise NotImplementedError

def CallNoReturn(module: str, func: str, *args):
    raise NotImplementedError

def GetReg(id: int):
    raise NotImplementedError

def SetReg(id: int, value: int):
    raise NotImplementedError

def JmpIfZero():
    raise NotImplementedError

def JmpIfNotZero():
    raise NotImplementedError

def Syscall():
    raise NotImplementedError

def LogicalOr():
    raise NotImplementedError

def LogicalAnd():
    raise NotImplementedError

def Return():
    raise NotImplementedError

def handleAssignment(stack: ScenaStack, assign: Tracer.Assignment, varname: str, locals: dict[str, StackValue]):
    assert assign.src is not None

    if assign.dest is None:
        assign.dest = stack.Var()
        src = assign.src
        dest = assign.dest

        match src:
            case RawInt():
                PUSH(src)

            case int():
                PUSH_INT(src)

            case float():
                PUSH_FLOAT(src)

            case str():
                PUSH_STR(src)

            case StackValue():
                if src.isArg:
                    LOAD_STACK(src.offsetTo(dest))

    locals[varname] = assign.dest
