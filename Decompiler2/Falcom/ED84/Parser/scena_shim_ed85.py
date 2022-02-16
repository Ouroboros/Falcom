from Falcom.ED84.Parser.scena_writer_helper import *
from Falcom.ED84.Parser.scena_writer import _gScena

def _AlwaysFalse():
    return FormationCtrl(0x05, 0xEEEE)

# effect 0x32

def LoadEffect(chrId: int, slot: int, eff: str, _):
    EffectCtrl(0x0A, chrId, slot, eff)

# BattleCtrl 0x33

def BattleSetChrAfterImageOff(_):
    BattleCtrl(0x16)

def CreateThread(chrId: int, threadId: int, func: str, scriptId: int, *args):
    # 0x1E
    assert isinstance(chrId, int)
    assert isinstance(threadId, int)
    assert isinstance(func, str)
    assert isinstance(scriptId, int)
    return _gScena.handleOpCode(0x1E, chrId, threadId, scriptId, func)

def OP_2E(arg1: int, arg2: int, arg3: int, *args):
    # 0x2E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    match arg1:
        case 4 | 5:
            return Sleep(int(args[0] * 100000 / 30 / 100))

    return _gScena.handleOpCode(0x2E, arg1, arg2, arg3, *args)

def OP_3B(arg1: int, *args):
    # 0x3B
    assert isinstance(arg1, int)
    match arg1:
        case 0x01 | 0x33:
            args = args[:-1]

    return _gScena.handleOpCode(0x3B, arg1, *args)

def OP_4A(arg1: uint8, arg2: float32, arg3: float32, arg4: float32, arg5: float32, arg6: uint32, arg7: uint8):
    # 0x4A
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, float32)
    assert isinstance(arg3, float32)
    assert isinstance(arg4, float32)
    assert isinstance(arg5, float32)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint8)
    return _gScena.handleOpCode(0x4A, arg2, arg3, arg4, arg5, arg6, arg7)

def OP_4E(arg1: float32, arg2: float32, arg3: uint8, _):
    # 0x4E
    assert isinstance(arg1, float32)
    assert isinstance(arg2, float32)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x4E, arg1, arg2, arg3)

def OP_6C(arg1: uint16, arg2: float32, *args):
    # 0x6C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, float32)
    return _gScena.handleOpCode(0x6C, arg1, arg2)

def OP_8A(arg1: int, *args):
    # 0x8A
    assert isinstance(arg1, int)
    match arg1:
        case 0x00 | 0x0A | 0x0C:
            args = args[:-1]

    return _gScena.handleOpCode(0x8A, arg1, *args)

def OP_D9(*args):
    # 0xD9
    return _AlwaysFalse()
