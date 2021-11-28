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

def ChrTalk(chrId: int, flags: int, text: str):
    # 0x24
    assert isinstance(chrId, int)
    assert isinstance(flags, int)
    assert isinstance(text, str)
    scena.handleOpCode(0x24, chrId, flags, text)

def OP_24(chrId: int, flags: int, text: str):
    # 0x24
    assert isinstance(chrId, int)
    assert isinstance(flags, int)
    assert isinstance(text, str)
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

def OP_4F(arg1: int, arg2: int, *args):
    # 0x4F
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x4F, arg1, arg2, *args)

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

def OP_5E(arg1: int, *args):
    # 0x5E
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x5E, arg1, *args)

def OP_62():
    # 0x62
    scena.handleOpCode(0x62)

def OP_63(arg1: int, arg2: int):
    # 0x63
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x63, arg1, arg2)

def OP_66(arg1: int, arg2: int, *args):
    # 0x66
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x66, arg1, arg2, *args)

def OP_69(arg1: int, *args):
    # 0x69
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x69, arg1, *args)

def OP_6B(arg1: int, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int):
    # 0x6B
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, int)
    assert isinstance(arg4, float)
    assert isinstance(arg5, int)
    assert isinstance(arg6, int)
    scena.handleOpCode(0x6B, arg1, arg2, arg3, arg4, arg5, arg6)

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

def OP_77(arg1: int):
    # 0x77
    assert isinstance(arg1, int)
    scena.handleOpCode(0x77, arg1)

def OP_79(arg1: int, arg2: int, *args):
    # 0x79
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return scena.handleOpCode(0x79, arg1, arg2, *args)

def OP_7C(arg1: int, *args):
    # 0x7C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x7C, arg1, *args)

def OP_7D(arg1: int, arg2: int):
    # 0x7D
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    scena.handleOpCode(0x7D, arg1, arg2)

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

def OP_93(arg1: int, *args):
    # 0x93
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x93, arg1, *args)

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

def OP_99(arg1: int):
    # 0x99
    assert isinstance(arg1, int)
    scena.handleOpCode(0x99, arg1)

def OP_9C(arg1: int, *args):
    # 0x9C
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9C, arg1, *args)

def OP_9E(arg1: int, *args):
    # 0x9E
    assert isinstance(arg1, int)
    return scena.handleOpCode(0x9E, arg1, *args)

def OP_A0():
    # 0xA0
    scena.handleOpCode(0xA0)

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

def OP_A8(arg1: int):
    # 0xA8
    assert isinstance(arg1, int)
    scena.handleOpCode(0xA8, arg1)

def OP_A9(arg1: int):
    # 0xA9
    assert isinstance(arg1, int)
    scena.handleOpCode(0xA9, arg1)

def OP_AC(arg1: int, *args):
    # 0xAC
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xAC, arg1, *args)

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

def OP_BC(arg1: int, arg2: int, arg3: tuple, *args):
    # 0xBC
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    assert isinstance(arg3, tuple)
    return scena.handleOpCode(0xBC, arg1, arg2, arg3, *args)

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

def OP_C9(arg1: int, *args):
    # 0xC9
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xC9, arg1, *args)

def OP_CA(arg1: int, *args):
    # 0xCA
    assert isinstance(arg1, int)
    return scena.handleOpCode(0xCA, arg1, *args)
