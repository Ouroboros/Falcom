from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *

ChrTable = GlobalConfig.ChrTable

def ReturnToTitle():
    Call(0x0A, 'FC_EventEndMapChange', (0xDD, 'title'), (0xDD, ''))

def SaveClearData():
    OP_90('current', 0x00000019)
    OP_93(0x00, 0x02)
    OP_93(0x01)

def RefreshSkin(chrId: int):
    return ChangeSkin(chrId, '')

def ChangeSkin(chrId: int, model: str):
    ChrAnimeClipCtrl(0x0A, chrId, model, '')

def SetChrModelChrId(chrId: int, modelChrId: int):
    OP_54(0x53, chrId, modelChrId)

def SetBattleStyle(chrId: int, style: int):
    OP_54(0x4A, chrId, style)

def GetBattleStyle(chrId: int):
    OP_54(0x4B, chrId)

def CameraRotate(vertical: float, horizontal: float, rotation: float, durationInMs: int = 0):
    '''
        上下
        左右
        翻转
    '''
    OP_36(0x04, 0x03, vertical, horizontal, rotation, durationInMs, 0x01)
    return

def CameraPos(x: float, y: float, z: float):
    CameraCtrl(0x02, 0x03, x, y, z, 0)

def CameraHeight(height: float, durationInMs: int = 0):
    CameraCtrl(0x05, 0x03, height, durationInMs)

def SetBattleChrFlags(chrId: int, flags: int):
    OP_33(0x0B, chrId, flags)

def ClearBattleChrFlags(chrId: int, flags: int):
    OP_33(0x0C, chrId, flags)

def GetBattleChrFlags(chrId: int):
    OP_33(0x0D, chrId)

L_ARM_POINT = 'L_arm_point'
R_ARM_POINT = 'R_arm_point'

def AttachEquip(chrId: int, equip: str, part: str):
    # EquipCtrl(0x00, 0xFFFE, 'C_EQU090', 'R_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCtrl(0x00, chrId, equip, part, 0, 0, 0, 0, 0, 0, 1, 1, 1)

def DeatchEquip(chrId: int, part: str):
    # EquipCtrl(0x01, 0xFFFE, '', 'L_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCtrl(0x01, chrId, '', part, 0, 0, 0, 0, 0, 0, 1, 1, 1)

def PlayVoice(voice1: int, voice2: int = 0, voice3: int = 0, voice4: int = 0):
    OP_3B(0x3A, 0xFFFE, (0xFF, voice1, 0x0), (0xFF, voice2, 0x0), (0xFF, voice3, 0x0), (0xFF, voice4, 0x0))
