from Falcom.ED6.Parser.scena_writer import _gScena

sint8 = int
uint8 = int
sint16 = int
uint16 = int
sint32 = int
uint32 = int
float32 = float | int

def ExitThread():
    # 0x00
    _gScena.handleOpCode(0x00)

def OP_00():
    # 0x00
    _gScena.handleOpCode(0x00)

def Return():
    # 0x01
    _gScena.handleOpCode(0x01)

def OP_01():
    # 0x01
    _gScena.handleOpCode(0x01)

def If(arg1: tuple | list, arg2: str):
    # 0x02
    assert isinstance(arg1, tuple | list)
    assert isinstance(arg2, str)
    _gScena.handleOpCode(0x02, arg1, arg2)

def OP_02(arg1: tuple | list, arg2: str):
    # 0x02
    assert isinstance(arg1, tuple | list)
    assert isinstance(arg2, str)
    _gScena.handleOpCode(0x02, arg1, arg2)

def Jump(arg1: str):
    # 0x03
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x03, arg1)

def OP_03(arg1: str):
    # 0x03
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x03, arg1)

def Switch(*args):
    # 0x04
    return _gScena.handleOpCode(0x04, *args)

def OP_04(*args):
    # 0x04
    return _gScena.handleOpCode(0x04, *args)

def Call(arg1: uint8, arg2: uint16):
    # 0x05
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x05, arg1, arg2)

def OP_05(arg1: uint8, arg2: uint16):
    # 0x05
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x05, arg1, arg2)

def NewScene(arg1: uint32, arg2: uint8, arg3: uint8, arg4: uint8):
    # 0x06
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint8)
    _gScena.handleOpCode(0x06, arg1, arg2, arg3, arg4)

def OP_06(arg1: uint32, arg2: uint8, arg3: uint8, arg4: uint8):
    # 0x06
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint8)
    _gScena.handleOpCode(0x06, arg1, arg2, arg3, arg4)

def Yield():
    # 0x07
    _gScena.handleOpCode(0x07)

def OP_07():
    # 0x07
    _gScena.handleOpCode(0x07)

def Sleep(arg1: uint32):
    # 0x08
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x08, arg1)

def OP_08(arg1: uint32):
    # 0x08
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x08, arg1)

def SetMapFlags(arg1: uint32):
    # 0x09
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x09, arg1)

def OP_09(arg1: uint32):
    # 0x09
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x09, arg1)

def ClearMapFlags(arg1: uint32):
    # 0x0A
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x0A, arg1)

def OP_0A(arg1: uint32):
    # 0x0A
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x0A, arg1)

def FadeToDark(arg1: sint32, arg2: sint32, arg3: sint8):
    # 0x0B
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint8)
    _gScena.handleOpCode(0x0B, arg1, arg2, arg3)

def OP_0B(arg1: sint32, arg2: sint32, arg3: sint8):
    # 0x0B
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint8)
    _gScena.handleOpCode(0x0B, arg1, arg2, arg3)

def FadeToLight(arg1: sint32, arg2: sint32):
    # 0x0C
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    _gScena.handleOpCode(0x0C, arg1, arg2)

def OP_0C(arg1: sint32, arg2: sint32):
    # 0x0C
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    _gScena.handleOpCode(0x0C, arg1, arg2)

def OP_0D():
    # 0x0D
    _gScena.handleOpCode(0x0D)

def Fade(arg1: uint32):
    # 0x0E
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x0E, arg1)

def OP_0E(arg1: uint32):
    # 0x0E
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x0E, arg1)

def Battle(arg1: uint32, arg2: uint32, arg3: uint8, arg4: uint16, arg5: uint8):
    # 0x0F
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint16)
    assert isinstance(arg5, uint8)
    _gScena.handleOpCode(0x0F, arg1, arg2, arg3, arg4, arg5)

def OP_0F(arg1: uint32, arg2: uint32, arg3: uint8, arg4: uint16, arg5: uint8):
    # 0x0F
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint16)
    assert isinstance(arg5, uint8)
    _gScena.handleOpCode(0x0F, arg1, arg2, arg3, arg4, arg5)

def OP_10(arg1: uint8, arg2: uint8):
    # 0x10
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x10, arg1, arg2)

def OP_11(arg1: uint8, arg2: uint8, arg3: uint8, arg4: uint32, arg5: uint32, arg6: uint32):
    # 0x11
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    _gScena.handleOpCode(0x11, arg1, arg2, arg3, arg4, arg5, arg6)

def StopSound(arg1: uint32, arg2: uint32, arg3: uint32):
    # 0x12
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    _gScena.handleOpCode(0x12, arg1, arg2, arg3)

def OP_12(arg1: uint32, arg2: uint32, arg3: uint32):
    # 0x12
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    _gScena.handleOpCode(0x12, arg1, arg2, arg3)

def SetPlaceName(arg1: uint16):
    # 0x13
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x13, arg1)

def OP_13(arg1: uint16):
    # 0x13
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x13, arg1)

def BlurSwitch():
    # 0x14
    _gScena.handleOpCode(0x14)

def OP_14():
    # 0x14
    _gScena.handleOpCode(0x14)

def OP_15():
    # 0x15
    _gScena.handleOpCode(0x15)

def OP_16(arg1: int, *args):
    # 0x16
    assert isinstance(arg1, int)
    return _gScena.handleOpCode(0x16, arg1, *args)

def ShowSaveMenu():
    # 0x17
    _gScena.handleOpCode(0x17)

def OP_17():
    # 0x17
    _gScena.handleOpCode(0x17)

def OP_18():
    # 0x18
    _gScena.handleOpCode(0x18)

def EventBegin(arg1: uint8):
    # 0x19
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x19, arg1)

def OP_19(arg1: uint8):
    # 0x19
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x19, arg1)

def EventEnd(arg1: uint8):
    # 0x1A
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x1A, arg1)

def OP_1A(arg1: uint8):
    # 0x1A
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x1A, arg1)

def OP_1B(arg1: uint8, arg2: uint8, arg3: uint16):
    # 0x1B
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0x1B, arg1, arg2, arg3)

def OP_1C(arg1: uint8, arg2: uint8, arg3: uint16):
    # 0x1C
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0x1C, arg1, arg2, arg3)

def OP_1D(arg1: uint8):
    # 0x1D
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x1D, arg1)

def OP_1E():
    # 0x1E
    _gScena.handleOpCode(0x1E)

def OP_1F(arg1: uint8, arg2: uint32):
    # 0x1F
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint32)
    _gScena.handleOpCode(0x1F, arg1, arg2)

def OP_20(arg1: uint32):
    # 0x20
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0x20, arg1)

def OP_21():
    # 0x21
    _gScena.handleOpCode(0x21)

def OP_22(arg1: uint16, arg2: uint8, arg3: uint8):
    # 0x22
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x22, arg1, arg2, arg3)

def OP_23(arg1: uint16):
    # 0x23
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x23, arg1)

def OP_24(arg1: uint16, arg2: uint8):
    # 0x24
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x24, arg1, arg2)

def SoundDistance(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint32, arg7: uint8, arg8: uint32):
    # 0x25
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint8)
    assert isinstance(arg8, uint32)
    _gScena.handleOpCode(0x25, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

def OP_25(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint32, arg7: uint8, arg8: uint32):
    # 0x25
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint8)
    assert isinstance(arg8, uint32)
    _gScena.handleOpCode(0x25, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

def SoundLoad(arg1: uint16):
    # 0x26
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x26, arg1)

def OP_26(arg1: uint16):
    # 0x26
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x26, arg1)

def Yield():
    # 0x27
    _gScena.handleOpCode(0x27)

def OP_27():
    # 0x27
    _gScena.handleOpCode(0x27)

def OP_28(arg1: int, *args):
    # 0x28
    assert isinstance(arg1, int)
    return _gScena.handleOpCode(0x28, arg1, *args)

def OP_29(arg1: int, arg2: int, *args):
    # 0x29
    assert isinstance(arg1, int)
    assert isinstance(arg2, int)
    return _gScena.handleOpCode(0x29, arg1, arg2, *args)

def OP_2A(arg1: int, *args):
    # 0x2A
    assert isinstance(arg1, int)
    return _gScena.handleOpCode(0x2A, arg1, *args)

def OP_2B(arg1: uint16, arg2: uint16):
    # 0x2B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x2B, arg1, arg2)

def OP_2C(arg1: uint16, arg2: uint16):
    # 0x2C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x2C, arg1, arg2)

def FormationAddMember(arg1: uint8, arg2: uint8):
    # 0x2D
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x2D, arg1, arg2)

def OP_2D(arg1: uint8, arg2: uint8):
    # 0x2D
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x2D, arg1, arg2)

def FormationDelMember(arg1: uint8, arg2: uint8):
    # 0x2E
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x2E, arg1, arg2)

def OP_2E(arg1: uint8, arg2: uint8):
    # 0x2E
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x2E, arg1, arg2)

def FormationReset():
    # 0x2F
    _gScena.handleOpCode(0x2F)

def OP_2F():
    # 0x2F
    _gScena.handleOpCode(0x2F)

def OP_30(arg1: uint8):
    # 0x30
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x30, arg1)

def OP_31(arg1: uint8, arg2: uint8, arg3: uint16):
    # 0x31
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0x31, arg1, arg2, arg3)

def OP_32(arg1: uint8, arg2: uint16):
    # 0x32
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x32, arg1, arg2)

def OP_33(arg1: uint8, arg2: uint16):
    # 0x33
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x33, arg1, arg2)

def OP_34(arg1: uint8, arg2: uint16):
    # 0x34
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x34, arg1, arg2)

def OP_35(arg1: uint8, arg2: uint16):
    # 0x35
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x35, arg1, arg2)

def OP_36(arg1: uint8, arg2: uint16):
    # 0x36
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x36, arg1, arg2)

def OP_37(arg1: uint8, arg2: uint16):
    # 0x37
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x37, arg1, arg2)

def AddSepith(arg1: uint8, arg2: uint16):
    # 0x38
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x38, arg1, arg2)

def OP_38(arg1: uint8, arg2: uint16):
    # 0x38
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x38, arg1, arg2)

def SubSepith(arg1: uint8, arg2: uint16):
    # 0x39
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x39, arg1, arg2)

def OP_39(arg1: uint8, arg2: uint16):
    # 0x39
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x39, arg1, arg2)

def AddMira(arg1: uint16):
    # 0x3A
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x3A, arg1)

def OP_3A(arg1: uint16):
    # 0x3A
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x3A, arg1)

def SubMira(arg1: uint16):
    # 0x3B
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x3B, arg1)

def OP_3B(arg1: uint16):
    # 0x3B
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x3B, arg1)

def OP_3C(arg1: uint16):
    # 0x3C
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x3C, arg1)

def OP_3D(arg1: uint16):
    # 0x3D
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x3D, arg1)

def OP_3E(arg1: uint16, arg2: sint8):
    # 0x3E
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint8)
    _gScena.handleOpCode(0x3E, arg1, arg2)

def OP_3F(arg1: uint16, arg2: sint8):
    # 0x3F
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint8)
    _gScena.handleOpCode(0x3F, arg1, arg2)

def OP_40(arg1: uint16):
    # 0x40
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x40, arg1)

def OP_41(arg1: int, *args):
    # 0x41
    assert isinstance(arg1, int)
    return _gScena.handleOpCode(0x41, arg1, *args)

def OP_42(arg1: uint8):
    # 0x42
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x42, arg1)

def BeginChrThread(arg1: uint16, arg2: uint8, arg3: uint8, arg4: uint16):
    # 0x43
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint16)
    _gScena.handleOpCode(0x43, arg1, arg2, arg3, arg4)

def OP_43(arg1: uint16, arg2: uint8, arg3: uint8, arg4: uint16):
    # 0x43
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint16)
    _gScena.handleOpCode(0x43, arg1, arg2, arg3, arg4)

def EndChrThread(arg1: uint16, arg2: uint8):
    # 0x44
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x44, arg1, arg2)

def OP_44(arg1: uint16, arg2: uint8):
    # 0x44
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x44, arg1, arg2)

def QueueWorkItem():
    raise NotImplementedError

def OP_45():
    raise NotImplementedError

def QueueWorkItem2():
    raise NotImplementedError

def OP_46():
    raise NotImplementedError

def WaitChrThread(arg1: uint16, arg2: uint16):
    # 0x47
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x47, arg1, arg2)

def OP_47(arg1: uint16, arg2: uint16):
    # 0x47
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x47, arg1, arg2)

def OP_48():
    # 0x48
    _gScena.handleOpCode(0x48)

def Event(arg1: uint8, arg2: uint16):
    # 0x49
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x49, arg1, arg2)

def OP_49(arg1: uint8, arg2: uint16):
    # 0x49
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x49, arg1, arg2)

def OP_4A(arg1: uint16, arg2: uint8):
    # 0x4A
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x4A, arg1, arg2)

def OP_4B(arg1: uint16, arg2: uint8):
    # 0x4B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x4B, arg1, arg2)

def OP_4C():
    # 0x4C
    _gScena.handleOpCode(0x4C)

def RunExpression(arg1: uint16, arg2: tuple | list):
    # 0x4D
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, tuple | list)
    _gScena.handleOpCode(0x4D, arg1, arg2)

def OP_4D(arg1: uint16, arg2: tuple | list):
    # 0x4D
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, tuple | list)
    _gScena.handleOpCode(0x4D, arg1, arg2)

def OP_4E():
    # 0x4E
    _gScena.handleOpCode(0x4E)

def OP_4F(arg1: uint8, arg2: tuple | list):
    # 0x4F
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, tuple | list)
    _gScena.handleOpCode(0x4F, arg1, arg2)

def OP_50():
    # 0x50
    _gScena.handleOpCode(0x50)

def OP_51(arg1: uint16, arg2: uint8, arg3: tuple | list):
    # 0x51
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, tuple | list)
    _gScena.handleOpCode(0x51, arg1, arg2, arg3)

def TalkBegin(arg1: uint16):
    # 0x52
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x52, arg1)

def OP_52(arg1: uint16):
    # 0x52
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x52, arg1)

def TalkEnd(arg1: uint16):
    # 0x53
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x53, arg1)

def OP_53(arg1: uint16):
    # 0x53
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x53, arg1)

def Talk(arg1: str | tuple):
    # 0x54
    assert isinstance(arg1, str | tuple)
    _gScena.handleOpCode(0x54, arg1)

def OP_54(arg1: str | tuple):
    # 0x54
    assert isinstance(arg1, str | tuple)
    _gScena.handleOpCode(0x54, arg1)

def OP_55():
    # 0x55
    _gScena.handleOpCode(0x55)

def OP_56(arg1: uint8):
    # 0x56
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x56, arg1)

def OP_57():
    # 0x57
    _gScena.handleOpCode(0x57)

def WaitAndCloseMessageWindow():
    # 0x58
    _gScena.handleOpCode(0x58)

def OP_58():
    # 0x58
    _gScena.handleOpCode(0x58)

def OP_59():
    # 0x59
    _gScena.handleOpCode(0x59)

def SetMessageWindowPos(arg1: sint8, arg2: sint8, arg3: sint8, arg4: sint8):
    # 0x5A
    assert isinstance(arg1, sint8)
    assert isinstance(arg2, sint8)
    assert isinstance(arg3, sint8)
    assert isinstance(arg4, sint8)
    _gScena.handleOpCode(0x5A, arg1, arg2, arg3, arg4)

def OP_5A(arg1: sint8, arg2: sint8, arg3: sint8, arg4: sint8):
    # 0x5A
    assert isinstance(arg1, sint8)
    assert isinstance(arg2, sint8)
    assert isinstance(arg3, sint8)
    assert isinstance(arg4, sint8)
    _gScena.handleOpCode(0x5A, arg1, arg2, arg3, arg4)

def ChrTalk(arg1: uint16, arg2: str | tuple):
    # 0x5B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, str | tuple)
    _gScena.handleOpCode(0x5B, arg1, arg2)

def OP_5B(arg1: uint16, arg2: str | tuple):
    # 0x5B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, str | tuple)
    _gScena.handleOpCode(0x5B, arg1, arg2)

def NpcTalk(arg1: uint16, arg2: str, arg3: str | tuple):
    # 0x5C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, str)
    assert isinstance(arg3, str | tuple)
    _gScena.handleOpCode(0x5C, arg1, arg2, arg3)

def OP_5C(arg1: uint16, arg2: str, arg3: str | tuple):
    # 0x5C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, str)
    assert isinstance(arg3, str | tuple)
    _gScena.handleOpCode(0x5C, arg1, arg2, arg3)

def Menu(arg1: sint8, arg2: sint8, arg3: sint8, arg4: sint8, arg5: str):
    # 0x5D
    assert isinstance(arg1, sint8)
    assert isinstance(arg2, sint8)
    assert isinstance(arg3, sint8)
    assert isinstance(arg4, sint8)
    assert isinstance(arg5, str)
    _gScena.handleOpCode(0x5D, arg1, arg2, arg3, arg4, arg5)

def OP_5D(arg1: sint8, arg2: sint8, arg3: sint8, arg4: sint8, arg5: str):
    # 0x5D
    assert isinstance(arg1, sint8)
    assert isinstance(arg2, sint8)
    assert isinstance(arg3, sint8)
    assert isinstance(arg4, sint8)
    assert isinstance(arg5, str)
    _gScena.handleOpCode(0x5D, arg1, arg2, arg3, arg4, arg5)

def MenuEnd(arg1: uint16):
    # 0x5E
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x5E, arg1)

def OP_5E(arg1: uint16):
    # 0x5E
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x5E, arg1)

def OP_5F(arg1: uint16):
    # 0x5F
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x5F, arg1)

def SetChrName(arg1: str):
    # 0x60
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x60, arg1)

def OP_60(arg1: str):
    # 0x60
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0x60, arg1)

def OP_61(arg1: uint16):
    # 0x61
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x61, arg1)

def OP_62(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint8, arg5: uint8, arg6: uint32, arg7: uint8):
    # 0x62
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint8)
    assert isinstance(arg5, uint8)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint8)
    _gScena.handleOpCode(0x62, arg1, arg2, arg3, arg4, arg5, arg6, arg7)

def OP_63(arg1: uint16):
    # 0x63
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x63, arg1)

def OP_64(arg1: uint8, arg2: uint16):
    # 0x64
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x64, arg1, arg2)

def OP_65(arg1: uint8, arg2: uint16):
    # 0x65
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x65, arg1, arg2)

def OP_66(arg1: uint16):
    # 0x66
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x66, arg1)

def OP_67(arg1: sint32, arg2: sint32, arg3: sint32, arg4: sint32):
    # 0x67
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint32)
    assert isinstance(arg4, sint32)
    _gScena.handleOpCode(0x67, arg1, arg2, arg3, arg4)

def OP_68(arg1: uint16):
    # 0x68
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x68, arg1)

def OP_69(arg1: uint16, arg2: uint32):
    # 0x69
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    _gScena.handleOpCode(0x69, arg1, arg2)

def OP_6A(arg1: uint16):
    # 0x6A
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x6A, arg1)

def OP_6B(arg1: sint32, arg2: sint32):
    # 0x6B
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    _gScena.handleOpCode(0x6B, arg1, arg2)

def OP_6C(arg1: sint32, arg2: sint32):
    # 0x6C
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    _gScena.handleOpCode(0x6C, arg1, arg2)

def OP_6D(arg1: sint32, arg2: sint32, arg3: sint32, arg4: sint32):
    # 0x6D
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint32)
    assert isinstance(arg4, sint32)
    _gScena.handleOpCode(0x6D, arg1, arg2, arg3, arg4)

def OP_6E(arg1: sint32, arg2: sint32):
    # 0x6E
    assert isinstance(arg1, sint32)
    assert isinstance(arg2, sint32)
    _gScena.handleOpCode(0x6E, arg1, arg2)

def OP_6F(arg1: uint16, arg2: sint32):
    # 0x6F
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint32)
    _gScena.handleOpCode(0x6F, arg1, arg2)

def OP_70(arg1: uint16, arg2: uint32):
    # 0x70
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    _gScena.handleOpCode(0x70, arg1, arg2)

def OP_71(arg1: uint16, arg2: uint16):
    # 0x71
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x71, arg1, arg2)

def OP_72(arg1: uint16, arg2: uint16):
    # 0x72
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x72, arg1, arg2)

def OP_73(arg1: uint16):
    # 0x73
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x73, arg1)

def OP_74(arg1: uint16, arg2: uint32, arg3: uint16):
    # 0x74
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0x74, arg1, arg2, arg3)

def OP_75(arg1: uint8, arg2: uint32, arg3: uint8):
    # 0x75
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x75, arg1, arg2, arg3)

def OP_76(arg1: uint16, arg2: uint32, arg3: uint16, arg4: uint32, arg5: uint32, arg6: uint32, arg7: uint8, arg8: uint8):
    # 0x76
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint16)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint8)
    assert isinstance(arg8, uint8)
    _gScena.handleOpCode(0x76, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

def OP_77(arg1: uint8, arg2: uint8, arg3: uint8, arg4: uint32, arg5: uint8):
    # 0x77
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint8)
    _gScena.handleOpCode(0x77, arg1, arg2, arg3, arg4, arg5)

def OP_78(arg1: uint8, arg2: uint8, arg3: uint8):
    # 0x78
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    _gScena.handleOpCode(0x78, arg1, arg2, arg3)

def OP_79(arg1: uint8, arg2: uint16):
    # 0x79
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x79, arg1, arg2)

def OP_7A(arg1: uint8, arg2: uint16):
    # 0x7A
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x7A, arg1, arg2)

def OP_7B():
    # 0x7B
    _gScena.handleOpCode(0x7B)

def OP_7C(arg1: uint32, arg2: uint32, arg3: uint32, arg4: uint32):
    # 0x7C
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    _gScena.handleOpCode(0x7C, arg1, arg2, arg3, arg4)

def OP_7D(arg1: uint8):
    # 0x7D
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x7D, arg1)

def OP_7E(arg1: uint16, arg2: uint16, arg3: uint16, arg4: uint8, arg5: uint32):
    # 0x7E
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint16)
    assert isinstance(arg4, uint8)
    assert isinstance(arg5, uint32)
    _gScena.handleOpCode(0x7E, arg1, arg2, arg3, arg4, arg5)

def LoadEffect(arg1: uint8, arg2: str):
    # 0x7F
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, str)
    _gScena.handleOpCode(0x7F, arg1, arg2)

def OP_7F(arg1: uint8, arg2: str):
    # 0x7F
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, str)
    _gScena.handleOpCode(0x7F, arg1, arg2)

def PlayEffect(arg1: uint8, arg2: uint8, arg3: uint16, arg4: sint32, arg5: sint32, arg6: sint32, arg7: sint8, arg8: sint8, arg9: sint8, arg10: sint32, arg11: sint32, arg12: sint32, arg13: sint8, arg14: sint32, arg15: sint32, arg16: sint32, arg17: sint32):
    # 0x80
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint16)
    assert isinstance(arg4, sint32)
    assert isinstance(arg5, sint32)
    assert isinstance(arg6, sint32)
    assert isinstance(arg7, sint8)
    assert isinstance(arg8, sint8)
    assert isinstance(arg9, sint8)
    assert isinstance(arg10, sint32)
    assert isinstance(arg11, sint32)
    assert isinstance(arg12, sint32)
    assert isinstance(arg13, sint8)
    assert isinstance(arg14, sint32)
    assert isinstance(arg15, sint32)
    assert isinstance(arg16, sint32)
    assert isinstance(arg17, sint32)
    _gScena.handleOpCode(0x80, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17)

def OP_80(arg1: uint8, arg2: uint8, arg3: uint16, arg4: sint32, arg5: sint32, arg6: sint32, arg7: sint8, arg8: sint8, arg9: sint8, arg10: sint32, arg11: sint32, arg12: sint32, arg13: sint8, arg14: sint32, arg15: sint32, arg16: sint32, arg17: sint32):
    # 0x80
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint16)
    assert isinstance(arg4, sint32)
    assert isinstance(arg5, sint32)
    assert isinstance(arg6, sint32)
    assert isinstance(arg7, sint8)
    assert isinstance(arg8, sint8)
    assert isinstance(arg9, sint8)
    assert isinstance(arg10, sint32)
    assert isinstance(arg11, sint32)
    assert isinstance(arg12, sint32)
    assert isinstance(arg13, sint8)
    assert isinstance(arg14, sint32)
    assert isinstance(arg15, sint32)
    assert isinstance(arg16, sint32)
    assert isinstance(arg17, sint32)
    _gScena.handleOpCode(0x80, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, arg15, arg16, arg17)

def Play3DEffect(arg1: uint8, arg2: uint8, arg3: uint8, arg4: str, arg5: uint32, arg6: uint32, arg7: uint32, arg8: uint16, arg9: uint16, arg10: uint16, arg11: uint32, arg12: uint32, arg13: uint32, arg14: uint32):
    # 0x81
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, str)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint32)
    assert isinstance(arg8, uint16)
    assert isinstance(arg9, uint16)
    assert isinstance(arg10, uint16)
    assert isinstance(arg11, uint32)
    assert isinstance(arg12, uint32)
    assert isinstance(arg13, uint32)
    assert isinstance(arg14, uint32)
    _gScena.handleOpCode(0x81, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)

def OP_81(arg1: uint8, arg2: uint8, arg3: uint8, arg4: str, arg5: uint32, arg6: uint32, arg7: uint32, arg8: uint16, arg9: uint16, arg10: uint16, arg11: uint32, arg12: uint32, arg13: uint32, arg14: uint32):
    # 0x81
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, str)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    assert isinstance(arg7, uint32)
    assert isinstance(arg8, uint16)
    assert isinstance(arg9, uint16)
    assert isinstance(arg10, uint16)
    assert isinstance(arg11, uint32)
    assert isinstance(arg12, uint32)
    assert isinstance(arg13, uint32)
    assert isinstance(arg14, uint32)
    _gScena.handleOpCode(0x81, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14)

def OP_82(arg1: uint8, arg2: uint8):
    # 0x82
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x82, arg1, arg2)

def OP_83(arg1: uint8, arg2: uint8):
    # 0x83
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0x83, arg1, arg2)

def OP_84(arg1: uint8):
    # 0x84
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0x84, arg1)

def OP_85(arg1: uint16):
    # 0x85
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0x85, arg1)

def SetChrChipByIndex(arg1: uint16, arg2: uint16):
    # 0x86
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x86, arg1, arg2)

def OP_86(arg1: uint16, arg2: uint16):
    # 0x86
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x86, arg1, arg2)

def SetChrSubChip(arg1: uint16, arg2: uint16):
    # 0x87
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x87, arg1, arg2)

def OP_87(arg1: uint16, arg2: uint16):
    # 0x87
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x87, arg1, arg2)

def SetChrPos(arg1: uint16, arg2: sint32, arg3: sint32, arg4: sint32, arg5: sint8):
    # 0x88
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint32)
    assert isinstance(arg4, sint32)
    assert isinstance(arg5, sint8)
    _gScena.handleOpCode(0x88, arg1, arg2, arg3, arg4, arg5)

def OP_88(arg1: uint16, arg2: sint32, arg3: sint32, arg4: sint32, arg5: sint8):
    # 0x88
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint32)
    assert isinstance(arg4, sint32)
    assert isinstance(arg5, sint8)
    _gScena.handleOpCode(0x88, arg1, arg2, arg3, arg4, arg5)

def OP_89(arg1: uint16, arg2: sint32, arg3: sint32, arg4: sint32, arg5: sint8):
    # 0x89
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint32)
    assert isinstance(arg4, sint32)
    assert isinstance(arg5, sint8)
    _gScena.handleOpCode(0x89, arg1, arg2, arg3, arg4, arg5)

def TurnDirection(arg1: uint16, arg2: uint16, arg3: uint16):
    # 0x8A
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0x8A, arg1, arg2, arg3)

def OP_8A(arg1: uint16, arg2: uint16, arg3: uint16):
    # 0x8A
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0x8A, arg1, arg2, arg3)

def OP_8B(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint16):
    # 0x8B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint16)
    _gScena.handleOpCode(0x8B, arg1, arg2, arg3, arg4)

def OP_8C(arg1: uint16, arg2: sint8, arg3: sint8):
    # 0x8C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint8)
    assert isinstance(arg3, sint8)
    _gScena.handleOpCode(0x8C, arg1, arg2, arg3)

def OP_8D(arg1: uint16, arg2: sint32, arg3: sint32, arg4: sint32, arg5: sint32, arg6: sint32):
    # 0x8D
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, sint32)
    assert isinstance(arg3, sint32)
    assert isinstance(arg4, sint32)
    assert isinstance(arg5, sint32)
    assert isinstance(arg6, sint32)
    _gScena.handleOpCode(0x8D, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_8E(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint8):
    # 0x8E
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint8)
    _gScena.handleOpCode(0x8E, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_8F(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint8):
    # 0x8F
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint8)
    _gScena.handleOpCode(0x8F, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_90(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint8):
    # 0x90
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint8)
    _gScena.handleOpCode(0x90, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_91(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint8):
    # 0x91
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint8)
    _gScena.handleOpCode(0x91, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_92(arg1: uint16, arg2: uint16, arg3: uint32, arg4: uint32, arg5: uint8):
    # 0x92
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint8)
    _gScena.handleOpCode(0x92, arg1, arg2, arg3, arg4, arg5)

def OP_93(arg1: uint16, arg2: uint16, arg3: uint32, arg4: uint32, arg5: uint8):
    # 0x93
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint8)
    _gScena.handleOpCode(0x93, arg1, arg2, arg3, arg4, arg5)

def OP_94(arg1: uint8, arg2: uint16, arg3: uint16, arg4: uint32, arg5: uint32, arg6: uint8):
    # 0x94
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint16)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint8)
    _gScena.handleOpCode(0x94, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_95(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint32):
    # 0x95
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    _gScena.handleOpCode(0x95, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_96(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint32):
    # 0x96
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint32)
    _gScena.handleOpCode(0x96, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_97(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32, arg6: uint16):
    # 0x97
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    assert isinstance(arg6, uint16)
    _gScena.handleOpCode(0x97, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_98(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32):
    # 0x98
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    _gScena.handleOpCode(0x98, arg1, arg2, arg3, arg4, arg5)

def OP_99(arg1: uint16, arg2: uint8, arg3: uint8, arg4: uint32):
    # 0x99
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint32)
    _gScena.handleOpCode(0x99, arg1, arg2, arg3, arg4)

def SetChrFlags(arg1: uint16, arg2: uint16):
    # 0x9A
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9A, arg1, arg2)

def OP_9A(arg1: uint16, arg2: uint16):
    # 0x9A
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9A, arg1, arg2)

def ClearChrFlags(arg1: uint16, arg2: uint16):
    # 0x9B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9B, arg1, arg2)

def OP_9B(arg1: uint16, arg2: uint16):
    # 0x9B
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9B, arg1, arg2)

def SetChrBattleFlags(arg1: uint16, arg2: uint16):
    # 0x9C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9C, arg1, arg2)

def OP_9C(arg1: uint16, arg2: uint16):
    # 0x9C
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9C, arg1, arg2)

def ClearChrBattleFlags(arg1: uint16, arg2: uint16):
    # 0x9D
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9D, arg1, arg2)

def OP_9D(arg1: uint16, arg2: uint16):
    # 0x9D
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0x9D, arg1, arg2)

def OP_9E(arg1: uint16, arg2: uint32, arg3: uint32, arg4: uint32, arg5: uint32):
    # 0x9E
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint32)
    assert isinstance(arg3, uint32)
    assert isinstance(arg4, uint32)
    assert isinstance(arg5, uint32)
    _gScena.handleOpCode(0x9E, arg1, arg2, arg3, arg4, arg5)

def OP_9F(arg1: uint16, arg2: uint8, arg3: uint8, arg4: uint8, arg5: uint8, arg6: uint32):
    # 0x9F
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint8)
    assert isinstance(arg5, uint8)
    assert isinstance(arg6, uint32)
    _gScena.handleOpCode(0x9F, arg1, arg2, arg3, arg4, arg5, arg6)

def OP_A0(arg1: uint16, arg2: uint8, arg3: uint8, arg4: uint8, arg5: uint32):
    # 0xA0
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint8)
    assert isinstance(arg5, uint32)
    _gScena.handleOpCode(0xA0, arg1, arg2, arg3, arg4, arg5)

def OP_A1(arg1: uint16, arg2: uint16):
    # 0xA1
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0xA1, arg1, arg2)

def OP_A2(arg1: uint16):
    # 0xA2
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0xA2, arg1)

def OP_A3(arg1: uint16):
    # 0xA3
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0xA3, arg1)

def OP_A4(arg1: uint16):
    # 0xA4
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0xA4, arg1)

def OP_A5(arg1: uint16):
    # 0xA5
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0xA5, arg1)

def OP_A6(arg1: uint16):
    # 0xA6
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0xA6, arg1)

def OP_A7(arg1: uint16, arg2: uint16):
    # 0xA7
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0xA7, arg1, arg2)

def OP_A8(arg1: uint8, arg2: uint8, arg3: uint8, arg4: uint8, arg5: uint8):
    # 0xA8
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint8)
    assert isinstance(arg4, uint8)
    assert isinstance(arg5, uint8)
    _gScena.handleOpCode(0xA8, arg1, arg2, arg3, arg4, arg5)

def OP_A9(arg1: uint8):
    # 0xA9
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0xA9, arg1)

def OP_AA():
    # 0xAA
    _gScena.handleOpCode(0xAA)

def OP_AB():
    # 0xAB
    _gScena.handleOpCode(0xAB)

def OP_AC(arg1: uint16):
    # 0xAC
    assert isinstance(arg1, uint16)
    _gScena.handleOpCode(0xAC, arg1)

def OP_AD(arg1: uint32, arg2: uint16, arg3: uint16, arg4: uint32):
    # 0xAD
    assert isinstance(arg1, uint32)
    assert isinstance(arg2, uint16)
    assert isinstance(arg3, uint16)
    assert isinstance(arg4, uint32)
    _gScena.handleOpCode(0xAD, arg1, arg2, arg3, arg4)

def OP_AE(arg1: uint32):
    # 0xAE
    assert isinstance(arg1, uint32)
    _gScena.handleOpCode(0xAE, arg1)

def OP_AF(arg1: uint8, arg2: uint16):
    # 0xAF
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0xAF, arg1, arg2)

def OP_B0(arg1: uint16, arg2: uint8):
    # 0xB0
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0xB0, arg1, arg2)

def OP_B1(arg1: str):
    # 0xB1
    assert isinstance(arg1, str)
    _gScena.handleOpCode(0xB1, arg1)

def OP_B2(arg1: uint8, arg2: uint8, arg3: uint16):
    # 0xB2
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    assert isinstance(arg3, uint16)
    _gScena.handleOpCode(0xB2, arg1, arg2, arg3)

def PlayMovie(arg1: uint8, arg2: str):
    # 0xB3
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, str)
    _gScena.handleOpCode(0xB3, arg1, arg2)

def OP_B3(arg1: uint8, arg2: str):
    # 0xB3
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, str)
    _gScena.handleOpCode(0xB3, arg1, arg2)

def OP_B4(arg1: uint8):
    # 0xB4
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0xB4, arg1)

def OP_B5(arg1: uint16, arg2: uint8):
    # 0xB5
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0xB5, arg1, arg2)

def OP_B6(arg1: uint8):
    # 0xB6
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0xB6, arg1)

def OP_B7(arg1: uint16, arg2: uint8):
    # 0xB7
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0xB7, arg1, arg2)

def OP_B8(arg1: uint8):
    # 0xB8
    assert isinstance(arg1, uint8)
    _gScena.handleOpCode(0xB8, arg1)

def OP_B9(arg1: uint16, arg2: uint16):
    # 0xB9
    assert isinstance(arg1, uint16)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0xB9, arg1, arg2)

def OP_BA(arg1: uint8, arg2: uint16):
    # 0xBA
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint16)
    _gScena.handleOpCode(0xBA, arg1, arg2)

def OP_BB(arg1: uint8, arg2: uint8):
    # 0xBB
    assert isinstance(arg1, uint8)
    assert isinstance(arg2, uint8)
    _gScena.handleOpCode(0xBB, arg1, arg2)

def SaveClearData():
    # 0xBC
    _gScena.handleOpCode(0xBC)

def OP_BC():
    # 0xBC
    _gScena.handleOpCode(0xBC)
