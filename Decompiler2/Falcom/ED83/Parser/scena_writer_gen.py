from Falcom.ED83.Parser.scena_writer import _gScena as scena

def ExitThread():
    # 0x00
    scena.handleOpCode(0x00)

def OP_00():
    # 0x00
    scena.handleOpCode(0x00)

def Return():
    # 0x01
    scena.handleOpCode(0x01)

def OP_01():
    # 0x01
    scena.handleOpCode(0x01)

def Call(*args):
    # 0x02
    return scena.handleOpCode(0x02, *args)

def OP_02(*args):
    # 0x02
    return scena.handleOpCode(0x02, *args)

def Jump(label: str):
    # 0x03
    assert isinstance(label, str)
    scena.handleOpCode(0x03, label)

def OP_03(label: str):
    # 0x03
    assert isinstance(label, str)
    scena.handleOpCode(0x03, label)

def OP_04(arg1: int, arg2: str):
    # 0x04
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    scena.handleOpCode(0x04, arg1, arg2)

def If(ops: tuple | list, successor: str):
    # 0x05
    assert isinstance(ops, tuple | list)
    assert isinstance(successor, str)
    scena.handleOpCode(0x05, ops, successor)

def OP_05(ops: tuple | list, successor: str):
    # 0x05
    assert isinstance(ops, tuple | list)
    assert isinstance(successor, str)
    scena.handleOpCode(0x05, ops, successor)

def Switch(*args):
    # 0x06
    return scena.handleOpCode(0x06, *args)

def OP_06(*args):
    # 0x06
    return scena.handleOpCode(0x06, *args)

def SetScenaFlags(flags: int):
    # 0x10
    assert isinstance(flags, int)
    scena.handleOpCode(0x10, flags)

def OP_10(flags: int):
    # 0x10
    assert isinstance(flags, int)
    scena.handleOpCode(0x10, flags)

def OP_13(arg1: int):
    # 0x13
    assert isinstance(arg1, int)
    scena.handleOpCode(0x13, arg1)

def OP_14(arg1: int):
    # 0x14
    assert isinstance(arg1, int)
    scena.handleOpCode(0x14, arg1)

def OP_18(arg1: int, arg2: tuple | list):
    # 0x18
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    scena.handleOpCode(0x18, arg1, arg2)

def OP_1D(arg1: int, arg2: str, arg3: str, arg4: str, arg5: int, arg6: int, arg7: int, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: str, arg16: str, arg17: int, arg18: int, arg19: float, arg20: float, arg21: int):
    # 0x1D
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    assert isinstance(arg3, str)
    assert isinstance(arg4, str)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, float)
    assert isinstance(arg12, float)
    assert isinstance(arg13, float)
    assert isinstance(arg14, float)
    assert isinstance(arg15, str)
    assert isinstance(arg16, str)
    assert isinstance(arg17, int)
    assert isinstance(arg18, int)
    assert isinstance(arg19, float)
    assert isinstance(arg20, float)
    assert isinstance(arg21, int)
    scena.handleOpCode(0x1D, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21)

def OP_1E(arg1: int, arg2: int, arg3: int, arg4: str):
    # 0x1E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, str)
    scena.handleOpCode(0x1E, arg1, arg2, arg3, arg4)

def Talk(chrId: int, text: str):
    # 0x22
    assert isinstance(chrId, int)
    assert isinstance(text, str)
    scena.handleOpCode(0x22, chrId, text)

def OP_22(chrId: int, text: str):
    # 0x22
    assert isinstance(chrId, int)
    assert isinstance(text, str)
    scena.handleOpCode(0x22, chrId, text)

def OP_23(arg1: int, *args):
    # 0x23
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x23, arg1, *args)

def OP_25(arg1: int):
    # 0x25
    assert isinstance(arg1, int)
    scena.handleOpCode(0x25, arg1)

def OP_26():
    # 0x26
    scena.handleOpCode(0x26)

def MenuCmd(arg1: int, *args):
    # 0x29
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x29, arg1, *args)

def OP_29(arg1: int, *args):
    # 0x29
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x29, arg1, *args)

def OP_3A(arg1: int, *args):
    # 0x3A
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x3A, arg1, *args)

def OP_3B(arg1: int, *args):
    # 0x3B
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x3B, arg1, *args)

def OP_72(arg1: int, arg2: int, *args):
    # 0x72
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x72, arg1, arg2, *args)

def OP_7C(arg1: int, *args):
    # 0x7C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x7C, arg1, *args)

def OP_86(arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float, arg9: float, arg10: float, arg11: str):
    # 0x86
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, str)
    scena.handleOpCode(0x86, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11)

def OP_87(arg1: int, arg2: int):
    # 0x87
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x87, arg1, arg2)

def OP_9C(arg1: int, *args):
    # 0x9C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9C, arg1, *args)

def OP_9E(arg1: int, *args):
    # 0x9E
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9E, arg1, *args)

def OP_AC(arg1: int, *args):
    # 0xAC
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xAC, arg1, *args)

def MenuChrFlagCmd(arg1: int, arg2: int, arg3: int):
    # 0xB1
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0xB1, arg1, arg2, arg3)

def OP_B1(arg1: int, arg2: int, arg3: int):
    # 0xB1
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0xB1, arg1, arg2, arg3)