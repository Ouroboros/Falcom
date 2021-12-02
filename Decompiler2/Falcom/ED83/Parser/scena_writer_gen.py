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

def Call(type: int, name: str, *args):
    # 0x02
    assert isinstance(type, int)
    assert isinstance(name, str)
    return scena.handleOpCode(0x02, type, name, *args)

def OP_02(type: int, name: str, *args):
    # 0x02
    assert isinstance(type, int)
    assert isinstance(name, str)
    return scena.handleOpCode(0x02, type, name, *args)

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

def OP_07(arg1: int, arg2: tuple | list):
    # 0x07
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    scena.handleOpCode(0x07, arg1, arg2)

def OP_08(arg1: int, arg2: tuple | list):
    # 0x08
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    scena.handleOpCode(0x08, arg1, arg2)

def OP_0A(arg1: int, arg2: tuple | list):
    # 0x0A
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    scena.handleOpCode(0x0A, arg1, arg2)

def OP_0C(arg1: int, arg2: int):
    # 0x0C
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x0C, arg1, arg2)

def OP_0D(arg1: int, arg2: int, *args):
    # 0x0D
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x0D, arg1, arg2, *args)

def OP_0E(arg1: int, arg2: int, arg3: int):
    # 0x0E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x0E, arg1, arg2, arg3)

def SetScenaFlags(flags: int):
    # 0x10
    assert isinstance(flags, int)
    scena.handleOpCode(0x10, flags)

def OP_10(flags: int):
    # 0x10
    assert isinstance(flags, int)
    scena.handleOpCode(0x10, flags)

def OP_11(arg1: int):
    # 0x11
    assert isinstance(arg1, int)
    scena.handleOpCode(0x11, arg1)

def OP_12(arg1: int):
    # 0x12
    assert isinstance(arg1, int)
    scena.handleOpCode(0x12, arg1)

def OP_13(arg1: int):
    # 0x13
    assert isinstance(arg1, int)
    scena.handleOpCode(0x13, arg1)

def OP_14(arg1: int):
    # 0x14
    assert isinstance(arg1, int)
    scena.handleOpCode(0x14, arg1)

def OP_15(arg1: int):
    # 0x15
    assert isinstance(arg1, int)
    scena.handleOpCode(0x15, arg1)

def OP_16(arg1: int):
    # 0x16
    assert isinstance(arg1, int)
    scena.handleOpCode(0x16, arg1)

def OP_17(arg1: int, arg2: int):
    # 0x17
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x17, arg1, arg2)

def OP_18(arg1: int, arg2: tuple | list):
    # 0x18
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    scena.handleOpCode(0x18, arg1, arg2)

def OP_1A(arg1: int, arg2: int):
    # 0x1A
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x1A, arg1, arg2)

def CreateChr(chrId: int, model: str, name: str, monsterId: str, type: int, arg6: int, arg7: int, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: str, arg16: str, arg17: int, arg18: int, arg19: float, arg20: float, arg21: int):
    # 0x1D
    assert isinstance(chrId, int)
    assert isinstance(model, str)
    assert isinstance(name, str)
    assert isinstance(monsterId, str)
    assert isinstance(type, int)
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
    scena.handleOpCode(0x1D, chrId, model, name, monsterId, type, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21)

def OP_1D(chrId: int, model: str, name: str, monsterId: str, type: int, arg6: int, arg7: int, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: str, arg16: str, arg17: int, arg18: int, arg19: float, arg20: float, arg21: int):
    # 0x1D
    assert isinstance(chrId, int)
    assert isinstance(model, str)
    assert isinstance(name, str)
    assert isinstance(monsterId, str)
    assert isinstance(type, int)
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
    scena.handleOpCode(0x1D, chrId, model, name, monsterId, type, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21)

def OP_1E(arg1: int, arg2: int, arg3: int, arg4: str):
    # 0x1E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, str)
    scena.handleOpCode(0x1E, arg1, arg2, arg3, arg4)

def OP_1F(arg1: int, arg2: int):
    # 0x1F
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x1F, arg1, arg2)

def OP_20(arg1: int, arg2: tuple | list, arg3: tuple | list, arg4: tuple | list):
    # 0x20
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    assert isinstance(arg3, tuple | list)
    assert isinstance(arg4, tuple | list)
    scena.handleOpCode(0x20, arg1, arg2, arg3, arg4)

def OP_21(arg1: int):
    # 0x21
    assert isinstance(arg1, int)
    scena.handleOpCode(0x21, arg1)

def Talk(chrId: int, text: str | tuple):
    # 0x22
    assert isinstance(chrId, int)
    assert isinstance(text, str | tuple)
    scena.handleOpCode(0x22, chrId, text)

def OP_22(chrId: int, text: str | tuple):
    # 0x22
    assert isinstance(chrId, int)
    assert isinstance(text, str | tuple)
    scena.handleOpCode(0x22, chrId, text)

def OP_23(arg1: int, *args):
    # 0x23
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x23, arg1, *args)

def ChrTalk(chrId: int, flags: int, text: str | tuple):
    # 0x24
    assert isinstance(chrId, int)
    assert isinstance(flags, int)
    assert isinstance(text, str | tuple)
    scena.handleOpCode(0x24, chrId, flags, text)

def OP_24(chrId: int, flags: int, text: str | tuple):
    # 0x24
    assert isinstance(chrId, int)
    assert isinstance(flags, int)
    assert isinstance(text, str | tuple)
    scena.handleOpCode(0x24, chrId, flags, text)

def OP_25(arg1: int):
    # 0x25
    assert isinstance(arg1, int)
    scena.handleOpCode(0x25, arg1)

def OP_26():
    # 0x26
    scena.handleOpCode(0x26)

def OP_27(arg1: str, arg2: int):
    # 0x27
    assert isinstance(arg1, str)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x27, arg1, arg2)

def OP_28(arg1: tuple | list, arg2: tuple | list, arg3: int):
    # 0x28
    assert isinstance(arg1, tuple | list)
    assert isinstance(arg2, tuple | list)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x28, arg1, arg2, arg3)

def MenuCmd(arg1: int, arg2: int, *args):
    # 0x29
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x29, arg1, arg2, *args)

def OP_29(arg1: int, arg2: int, *args):
    # 0x29
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x29, arg1, arg2, *args)

def OP_2A(arg1: int, arg2: int, arg3: str, arg4: str, arg5: int):
    # 0x2A
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    assert isinstance(arg4, str)
    assert isinstance(arg5, int)
    scena.handleOpCode(0x2A, arg1, arg2, arg3, arg4, arg5)

def Battle(arg1: int, arg2: int, arg3: int, arg4: int, *args):
    # 0x2B
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    return scena.handleOpCode(0x2B, arg1, arg2, arg3, arg4, *args)

def OP_2B(arg1: int, arg2: int, arg3: int, arg4: int, *args):
    # 0x2B
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    return scena.handleOpCode(0x2B, arg1, arg2, arg3, arg4, *args)

def OP_2C(arg1: int, arg2: str, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float, arg9: float, arg10: float, arg11: float, arg12: int, arg13: int):
    # 0x2C
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, float)
    assert isinstance(arg12, int)
    assert isinstance(arg13, int)
    scena.handleOpCode(0x2C, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)

def OP_2D(arg1: int, arg2: float, arg3: int):
    # 0x2D
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x2D, arg1, arg2, arg3)

def OP_2E(arg1: int, arg2: int, arg3: int, *args):
    # 0x2E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    return scena.handleOpCode(0x2E, arg1, arg2, arg3, *args)

def AddChrAnimeClip(type: int, chrId: int, *args):
    # 0x2F
    assert isinstance(type, int)
    assert isinstance(chrId, int)
    return scena.handleOpCode(0x2F, type, chrId, *args)

def OP_2F(type: int, chrId: int, *args):
    # 0x2F
    assert isinstance(type, int)
    assert isinstance(chrId, int)
    return scena.handleOpCode(0x2F, type, chrId, *args)

def AttachEquip(arg1: int, arg2: int, arg3: str, arg4: str, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
    # 0x30
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    assert isinstance(arg4, str)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, float)
    assert isinstance(arg12, float)
    assert isinstance(arg13, float)
    scena.handleOpCode(0x30, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)

def OP_30(arg1: int, arg2: int, arg3: str, arg4: str, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
    # 0x30
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    assert isinstance(arg4, str)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, float)
    assert isinstance(arg12, float)
    assert isinstance(arg13, float)
    scena.handleOpCode(0x30, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13)

def OP_31(arg1: int, arg2: str):
    # 0x31
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    scena.handleOpCode(0x31, arg1, arg2)

def PlayEffect(arg1: int, *args):
    # 0x32
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x32, arg1, *args)

def OP_32(arg1: int, *args):
    # 0x32
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x32, arg1, *args)

def OP_33(arg1: int, *args):
    # 0x33
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x33, arg1, *args)

def OP_34(arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
    # 0x34
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    scena.handleOpCode(0x34, arg1, arg2, arg3, arg4, arg5)

def OP_35(arg1: int, arg2: int, arg3: int):
    # 0x35
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x35, arg1, arg2, arg3)

def CameraRotateChr(arg1: int, *args):
    # 0x36
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x36, arg1, *args)

def OP_36(arg1: int, *args):
    # 0x36
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x36, arg1, *args)

def OP_37(arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
    # 0x37
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    scena.handleOpCode(0x37, arg1, arg2, arg3, arg4, arg5)

def OP_38(arg1: int, arg2: int, arg3: int, arg4: str):
    # 0x38
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, str)
    scena.handleOpCode(0x38, arg1, arg2, arg3, arg4)

def OP_39(arg1: int, arg2: int, arg3: str, arg4: float, arg5: float, arg6: int):
    # 0x39
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x39, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_3A(arg1: int, *args):
    # 0x3A
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x3A, arg1, *args)

def OP_3B(arg1: int, *args):
    # 0x3B
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x3B, arg1, *args)

def OP_3C(arg1: int, arg2: int, *args):
    # 0x3C
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x3C, arg1, arg2, *args)

def OP_3D(arg1: int, arg2: float, arg3: float, arg4: int):
    # 0x3D
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, int)
    scena.handleOpCode(0x3D, arg1, arg2, arg3, arg4)

def OP_3E(arg1: int, arg2: int, arg3: float, arg4: int):
    # 0x3E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, int)
    scena.handleOpCode(0x3E, arg1, arg2, arg3, arg4)

def OP_3F(arg1: int):
    # 0x3F
    assert isinstance(arg1, int)
    scena.handleOpCode(0x3F, arg1)

def MoveType(arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, *args):
    # 0x40
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    return scena.handleOpCode(0x40, arg1, arg2, arg3, arg4, arg5, *args)

def OP_40(arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, *args):
    # 0x40
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    return scena.handleOpCode(0x40, arg1, arg2, arg3, arg4, arg5, *args)

def OP_41(arg1: int, arg2: int):
    # 0x41
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x41, arg1, arg2)

def OP_42(arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int):
    # 0x42
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, int)
    assert isinstance(arg9, int)
    scena.handleOpCode(0x42, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

def OP_43(arg1: int, arg2: int, *args):
    # 0x43
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x43, arg1, arg2, *args)

def OP_44(arg1: int, arg2: int, arg3: float, arg4: int, arg5: float):
    # 0x44
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, int)
    assert isinstance(arg5, float)
    scena.handleOpCode(0x44, arg1, arg2, arg3, arg4, arg5)

def OP_45(arg1: int, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int):
    # 0x45
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x45, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_46(arg1: int, arg2: int, arg3: int, arg4: int, *args):
    # 0x46
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    return scena.handleOpCode(0x46, arg1, arg2, arg3, arg4, *args)

def OP_47(arg1: int, arg2: str, arg3: int):
    # 0x47
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x47, arg1, arg2, arg3)

def OP_48(arg1: int, arg2: int, arg3: int, arg4: int):
    # 0x48
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    scena.handleOpCode(0x48, arg1, arg2, arg3, arg4)

def OP_49(arg1: int, *args):
    # 0x49
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x49, arg1, *args)

def OP_4A(arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int):
    # 0x4A
    assert isinstance(arg1, float)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x4A, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_4B(arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int):
    # 0x4B
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    scena.handleOpCode(0x4B, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

def OP_4C(arg1: int, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int):
    # 0x4C
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x4C, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_4D(arg1: int, arg2: int):
    # 0x4D
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x4D, arg1, arg2)

def OP_4E(arg1: float, arg2: float, arg3: int):
    # 0x4E
    assert isinstance(arg1, float)
    assert isinstance(arg2, float)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x4E, arg1, arg2, arg3)

def OP_4F(arg1: int, arg2: int, *args):
    # 0x4F
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x4F, arg1, arg2, *args)

def OP_50(arg1: tuple | list, arg2: str):
    # 0x50
    assert isinstance(arg1, tuple | list)
    assert isinstance(arg2, str)
    scena.handleOpCode(0x50, arg1, arg2)

def OP_51(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: float, arg8: float, arg9: float, arg10: float):
    # 0x51
    assert isinstance(arg1, float)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, int)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    scena.handleOpCode(0x51, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10)

def OP_52(arg1: int, arg2: int):
    # 0x52
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x52, arg1, arg2)

def OP_53(arg1: int, arg2: int):
    # 0x53
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x53, arg1, arg2)

def OP_54(arg1: int, *args):
    # 0x54
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x54, arg1, *args)

def OP_55(arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: float, arg13: float, arg14: float, arg15: float, arg16: int, arg17: int, arg18: str, arg19: str):
    # 0x55
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    assert isinstance(arg8, int)
    assert isinstance(arg9, int)
    assert isinstance(arg10, int)
    assert isinstance(arg11, int)
    assert isinstance(arg12, float)
    assert isinstance(arg13, float)
    assert isinstance(arg14, float)
    assert isinstance(arg15, float)
    assert isinstance(arg16, int)
    assert isinstance(arg17, int)
    assert isinstance(arg18, str)
    assert isinstance(arg19, str)
    scena.handleOpCode(0x55, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19)

def OP_56(arg1: int, arg2: int, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
    # 0x56
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    scena.handleOpCode(0x56, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

def OP_57(arg1: int, arg2: int):
    # 0x57
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x57, arg1, arg2)

def OP_58(arg1: int):
    # 0x58
    assert isinstance(arg1, int)
    scena.handleOpCode(0x58, arg1)

def OP_5A(arg1: int, arg2: int, arg3: str, arg4: int, arg5: int, arg6: int):
    # 0x5A
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x5A, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_5B(arg1: int, arg2: int, arg3: tuple | list):
    # 0x5B
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, tuple | list)
    scena.handleOpCode(0x5B, arg1, arg2, arg3)

def OP_5C(arg1: int, arg2: int, arg3: str):
    # 0x5C
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    scena.handleOpCode(0x5C, arg1, arg2, arg3)

def OP_5D(arg1: int, arg2: str, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: int, arg13: int, arg14: int):
    # 0x5D
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, float)
    assert isinstance(arg12, int)
    assert isinstance(arg13, int)
    assert isinstance(arg14, int)
    scena.handleOpCode(0x5D, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)

def OP_5E(arg1: int, *args):
    # 0x5E
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x5E, arg1, *args)

def OP_60(arg1: int, arg2: int, arg3: str):
    # 0x60
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, str)
    scena.handleOpCode(0x60, arg1, arg2, arg3)

def OP_61(arg1: int, arg2: str, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: int):
    # 0x61
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    assert isinstance(arg10, float)
    assert isinstance(arg11, float)
    assert isinstance(arg12, int)
    scena.handleOpCode(0x61, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12)

def OP_62():
    # 0x62
    scena.handleOpCode(0x62)

def OP_63(arg1: int, arg2: int):
    # 0x63
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x63, arg1, arg2)

def OP_64(arg1: int, arg2: float):
    # 0x64
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    scena.handleOpCode(0x64, arg1, arg2)

def SetLookpointFlag(lookpoint: int, arg2: str, *args):
    # 0x65
    assert isinstance(lookpoint, int)
    assert isinstance(arg2, str)
    return scena.handleOpCode(0x65, lookpoint, arg2, *args)

def OP_65(lookpoint: int, arg2: str, *args):
    # 0x65
    assert isinstance(lookpoint, int)
    assert isinstance(arg2, str)
    return scena.handleOpCode(0x65, lookpoint, arg2, *args)

def OP_66(arg1: int, arg2: int, *args):
    # 0x66
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x66, arg1, arg2, *args)

def OP_67(arg1: int, arg2: int, *args):
    # 0x67
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x67, arg1, arg2, *args)

def OP_68(arg1: int, arg2: str, *args):
    # 0x68
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    return scena.handleOpCode(0x68, arg1, arg2, *args)

def OP_69(arg1: int, *args):
    # 0x69
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x69, arg1, *args)

def OP_6A(arg1: int, arg2: int, *args):
    # 0x6A
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x6A, arg1, arg2, *args)

def OP_6B(arg1: int, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int):
    # 0x6B
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, float)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x6B, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_6C(arg1: int, arg2: float):
    # 0x6C
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    scena.handleOpCode(0x6C, arg1, arg2)

def OP_6E(arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
    # 0x6E
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x6E, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_6F(arg1: int, arg2: int, arg3: int):
    # 0x6F
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x6F, arg1, arg2, arg3)

def OP_70(arg1: int, *args):
    # 0x70
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x70, arg1, *args)

def QuestInfo(arg1: int, arg2: int, *args):
    # 0x72
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x72, arg1, arg2, *args)

def OP_72(arg1: int, arg2: int, *args):
    # 0x72
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x72, arg1, arg2, *args)

def OP_73(arg1: int, arg2: int, *args):
    # 0x73
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x73, arg1, arg2, *args)

def OP_74(arg1: int, arg2: int, *args):
    # 0x74
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x74, arg1, arg2, *args)

def OP_75(arg1: int, arg2: int, *args):
    # 0x75
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x75, arg1, arg2, *args)

def OP_76(arg1: int, arg2: str, arg3: str, arg4: int, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float):
    # 0x76
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    assert isinstance(arg3, str)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, float)
    scena.handleOpCode(0x76, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

def OP_77(arg1: int):
    # 0x77
    assert isinstance(arg1, int)
    scena.handleOpCode(0x77, arg1)

def OP_78(arg1: int, arg2: str):
    # 0x78
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    scena.handleOpCode(0x78, arg1, arg2)

def OP_79(arg1: int, arg2: int, *args):
    # 0x79
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x79, arg1, arg2, *args)

def OP_7A(arg1: int, *args):
    # 0x7A
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x7A, arg1, *args)

def OP_7B(arg1: int, *args):
    # 0x7B
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x7B, arg1, *args)

def OP_7C(arg1: int, *args):
    # 0x7C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x7C, arg1, *args)

def OP_7D(arg1: int, arg2: int):
    # 0x7D
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x7D, arg1, arg2)

def OP_7E(arg1: int, *args):
    # 0x7E
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x7E, arg1, *args)

def OP_80(arg1: float):
    # 0x80
    assert isinstance(arg1, float)
    scena.handleOpCode(0x80, arg1)

def OP_82(arg1: int, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
    # 0x82
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, int)
    assert isinstance(arg5, float)
    assert isinstance(arg6, float)
    assert isinstance(arg7, float)
    assert isinstance(arg8, float)
    assert isinstance(arg9, int)
    scena.handleOpCode(0x82, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9)

def OP_83(arg1: int, arg2: int, arg3: int, arg4: int):
    # 0x83
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    scena.handleOpCode(0x83, arg1, arg2, arg3, arg4)

def OP_84(arg1: int, *args):
    # 0x84
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x84, arg1, *args)

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

def OP_88(arg1: int):
    # 0x88
    assert isinstance(arg1, int)
    scena.handleOpCode(0x88, arg1)

def OP_89(arg1: int):
    # 0x89
    assert isinstance(arg1, int)
    scena.handleOpCode(0x89, arg1)

def OP_8A(arg1: int, *args):
    # 0x8A
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x8A, arg1, *args)

def OP_8B(arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
    # 0x8B
    assert isinstance(arg1, float)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x8B, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_8C(arg1: int, *args):
    # 0x8C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x8C, arg1, *args)

def OP_8D(arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
    # 0x8D
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    scena.handleOpCode(0x8D, arg1, arg2, arg3, arg4, arg5)

def OP_8E(arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
    # 0x8E
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    scena.handleOpCode(0x8E, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

def OP_8F():
    # 0x8F
    scena.handleOpCode(0x8F)

def OP_90(arg1: str, arg2: int):
    # 0x90
    assert isinstance(arg1, str)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x90, arg1, arg2)

def OP_91(arg1: int, *args):
    # 0x91
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x91, arg1, *args)

def OP_92(arg1: int, arg2: int):
    # 0x92
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x92, arg1, arg2)

def OP_93(arg1: int, *args):
    # 0x93
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x93, arg1, *args)

def OP_94(arg1: int, *args):
    # 0x94
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x94, arg1, *args)

def OP_95(arg1: int, *args):
    # 0x95
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x95, arg1, *args)

def OP_97(arg1: int, arg2: int, arg3: int):
    # 0x97
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0x97, arg1, arg2, arg3)

def OP_98(arg1: int, *args):
    # 0x98
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x98, arg1, *args)

def OP_99(arg1: int):
    # 0x99
    assert isinstance(arg1, int)
    scena.handleOpCode(0x99, arg1)

def OP_9A(arg1: int, arg2: float, arg3: float, arg4: float):
    # 0x9A
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    scena.handleOpCode(0x9A, arg1, arg2, arg3, arg4)

def OP_9B(arg1: int, *args):
    # 0x9B
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9B, arg1, *args)

def OP_9C(arg1: int, *args):
    # 0x9C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9C, arg1, *args)

def OP_9D(arg1: int, arg2: int):
    # 0x9D
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x9D, arg1, arg2)

def OP_9E(arg1: int, *args):
    # 0x9E
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9E, arg1, *args)

def OP_A0():
    # 0xA0
    scena.handleOpCode(0xA0)

def OP_A1(arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
    # 0xA1
    assert isinstance(arg1, float)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    scena.handleOpCode(0xA1, arg1, arg2, arg3, arg4, arg5)

def OP_A3(arg1: int, arg2: int):
    # 0xA3
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0xA3, arg1, arg2)

def OP_A4(arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: int, arg22: int):
    # 0xA4
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, int)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    assert isinstance(arg7, int)
    assert isinstance(arg8, int)
    assert isinstance(arg9, int)
    assert isinstance(arg10, int)
    assert isinstance(arg11, int)
    assert isinstance(arg12, int)
    assert isinstance(arg13, int)
    assert isinstance(arg14, int)
    assert isinstance(arg15, int)
    assert isinstance(arg16, int)
    assert isinstance(arg17, int)
    assert isinstance(arg18, int)
    assert isinstance(arg19, int)
    assert isinstance(arg20, int)
    assert isinstance(arg21, int)
    assert isinstance(arg22, int)
    scena.handleOpCode(0xA4, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17, arg18, arg19, arg20, arg21, arg22)

def OP_A6(arg1: int, arg2: float, arg3: float, arg4: float):
    # 0xA6
    assert isinstance(arg1, int)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    scena.handleOpCode(0xA6, arg1, arg2, arg3, arg4)

def OP_A8(arg1: int):
    # 0xA8
    assert isinstance(arg1, int)
    scena.handleOpCode(0xA8, arg1)

def OP_A9(arg1: int):
    # 0xA9
    assert isinstance(arg1, int)
    scena.handleOpCode(0xA9, arg1)

def OP_AA(arg1: int, arg2: int):
    # 0xAA
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0xAA, arg1, arg2)

def OP_AB(arg1: int, *args):
    # 0xAB
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xAB, arg1, *args)

def OP_AC(arg1: int, *args):
    # 0xAC
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xAC, arg1, *args)

def OP_AD(arg1: int, *args):
    # 0xAD
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xAD, arg1, *args)

def OP_AE(arg1: str, arg2: int):
    # 0xAE
    assert isinstance(arg1, str)
    assert isinstance(arg2, int)
    scena.handleOpCode(0xAE, arg1, arg2)

def OP_AF(arg1: int):
    # 0xAF
    assert isinstance(arg1, int)
    scena.handleOpCode(0xAF, arg1)

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

def OP_B2(arg1: int, arg2: int):
    # 0xB2
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0xB2, arg1, arg2)

def OP_B3(arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int):
    # 0xB3
    assert isinstance(arg1, float)
    assert isinstance(arg2, float)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0xB3, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_B4():
    # 0xB4
    scena.handleOpCode(0xB4)

def OP_B5(arg1: int, arg2: int, arg3: float, arg4: float, arg5: float):
    # 0xB5
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    assert isinstance(arg5, float)
    scena.handleOpCode(0xB5, arg1, arg2, arg3, arg4, arg5)

def OP_B6(arg1: int, arg2: int):
    # 0xB6
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0xB6, arg1, arg2)

def OP_B7(arg1: int, arg2: int):
    # 0xB7
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0xB7, arg1, arg2)

def OP_B8(arg1: int, arg2: tuple | list, arg3: tuple | list):
    # 0xB8
    assert isinstance(arg1, int)
    assert isinstance(arg2, tuple | list)
    assert isinstance(arg3, tuple | list)
    scena.handleOpCode(0xB8, arg1, arg2, arg3)

def OP_B9(arg1: int, arg2: int, *args):
    # 0xB9
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0xB9, arg1, arg2, *args)

def OP_BA(arg1: int, *args):
    # 0xBA
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xBA, arg1, *args)

def OP_BB(arg1: int):
    # 0xBB
    assert isinstance(arg1, int)
    scena.handleOpCode(0xBB, arg1)

def OP_BC(arg1: int, arg2: int, arg3: tuple, *args):
    # 0xBC
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, tuple)
    return scena.handleOpCode(0xBC, arg1, arg2, arg3, *args)

def OP_BE(arg1: int, arg2: int, arg3: float, arg4: float):
    # 0xBE
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, float)
    assert isinstance(arg4, float)
    scena.handleOpCode(0xBE, arg1, arg2, arg3, arg4)

def OP_C0(arg1: int, *args):
    # 0xC0
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC0, arg1, *args)

def OP_C2(arg1: int):
    # 0xC2
    assert isinstance(arg1, int)
    scena.handleOpCode(0xC2, arg1)

def OP_C3(arg1: int, *args):
    # 0xC3
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC3, arg1, *args)

def OP_C4(arg1: int, *args):
    # 0xC4
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC4, arg1, *args)

def OP_C5(arg1: int, *args):
    # 0xC5
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC5, arg1, *args)

def OP_C6(arg1: int, *args):
    # 0xC6
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC6, arg1, *args)

def OP_C7(arg1: int, *args):
    # 0xC7
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC7, arg1, *args)

def OP_C8(arg1: int, arg2: int, arg3: int):
    # 0xC8
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    scena.handleOpCode(0xC8, arg1, arg2, arg3)

def OP_C9(arg1: int, *args):
    # 0xC9
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC9, arg1, *args)

def OP_CA(arg1: int, *args):
    # 0xCA
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xCA, arg1, *args)

def OP_CB(arg1: int):
    # 0xCB
    assert isinstance(arg1, int)
    scena.handleOpCode(0xCB, arg1)

def OP_CC(arg1: int):
    # 0xCC
    assert isinstance(arg1, int)
    scena.handleOpCode(0xCC, arg1)

def OP_CD(arg1: int, *args):
    # 0xCD
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xCD, arg1, *args)
