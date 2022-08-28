from Falcom.ED9.Parser.scena_writer import *
from Falcom.ED9.Parser.scena_writer_gen import *
from Falcom.ED9.Parser.consts import *
import struct

def PUSH_INT(v: sint32):
    return PUSH(v | (ScenaValue.Type.Integer << 30))

def PUSH_FLOAT(f: float32):
    b = struct.pack('f', f)
    v = int.from_bytes(b, 'little', signed = False)
    return PUSH(v | (ScenaValue.Type.Float << 30))

def PUSH_STR(s: str):
    PUSH(s)

def Call(module: str, func: str, *args):
    pass

def CallNoReturn(module: str, func: str, *args):
    pass

def GetReg(id: int):
    pass

def SetReg(id: int, value: int):
    pass

def JmpIfZero():
    pass

def JmpIfNotZero():
    pass

def Syscall():
    pass

def LogicalOr():
    pass

def LogicalAnd():
    pass

def Return():
    pass
