from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *

ChrTable = GlobalConfig.ChrTable

def ReturnToTitle():
    Call(0x0A, 'FC_EventEndMapChange', (0xDD, 'title'), (0xDD, ''))

def SaveClearData():
    OP_90('current', 0x00000019)
    OP_93(0x00, 0x02)
    OP_93(0x01)

def FormationAddMember(chrId: int):
    OP_49(0x00, chrId)

def FormationReset():
    OP_49(0x02)

def FormationSetLeader(chrId: int):
    OP_49(0x04, chrId)

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


'''
    camera
'''

def CameraRotate(vertical: float, horizontal: float, rotation: float, durationInMs: int = 0, unknown: int = 1):
    '''
        上下
        左右
        翻转
    '''
    OP_36(0x04, 0x03, vertical, horizontal, rotation, durationInMs, unknown)
    return

def CameraPos(x: float, y: float, z: float, unknwon: int = 0):
    CameraCtrl(0x02, 0x03, x, y, z, unknwon)

def CameraHeight(height: float, durationInMs: int = 0):
    CameraCtrl(0x05, 0x03, height, durationInMs)

def SetBattleChrFlags(chrId: int, flags: int):
    OP_33(0x0B, chrId, flags)

def ClearBattleChrFlags(chrId: int, flags: int):
    OP_33(0x0C, chrId, flags)

def GetBattleChrFlags(chrId: int):
    OP_33(0x0D, chrId)


'''
    equip
'''

L_ARM_POINT = 'L_arm_point'
R_ARM_POINT = 'R_arm_point'

def AttachEquip(chrId: int, equip: str, part: str, *args):
    if not args:
        args = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    # EquipCtrl(0x00, 0xFFFE, 'C_EQU090', 'R_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCtrl(0x00, chrId, equip, part, *args)

def DeatchEquip(chrId: int, part: str, *args):
    if not args:
        args = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    # EquipCtrl(0x01, 0xFFFE, '', 'L_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCtrl(0x01, chrId, '', part, *args)


'''
    effect
'''

def LoadEffect(chrId: int, slot: int, eff: str):
    EffectCtrl(0x0A, chrId, slot, eff)

def PlayEffect(chrId: int, effectId: tuple, targetChrId: int, *args):
    EffectCtrl(0x0C, chrId, effectId, targetChrId, *args)

def StopEffect(chrId: int, slot: int, unknown: int):
    EffectCtrl(0x0D, chrId, slot, unknown)


'''
    asset
'''

def LoadAsset(asset: str):
    OP_31(0x00, asset)

def ReleaseAsset(asset: str):
    OP_31(0x01, asset)

def LoadAsset(asset: str):
    OP_31(0x02, asset)

def LoadAssetAsync(asset: str):
    OP_31(0x03, asset)


'''
    battle
'''

def PlaySound(sound: int):
    OP_3B(0x00, (0xFF, sound, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def PlayVoice(voice1: int, voice2: int = 0, voice3: int = 0, voice4: int = 0):
    OP_3B(0x3A, 0xFFFE, (0xFF, voice1, 0x0), (0xFF, voice2, 0x0), (0xFF, voice3, 0x0), (0xFF, voice4, 0x0))

TargetSelf = 0xFFFE
TargetSelectedPos = 0xFFF5

def IsBattleModelEqualTo(chrId: int, model: str):
    OP_7A(0x01, chrId, model)

def ChrMoveToTarget():
    OP_33(0x34)

def ChrTurnDirection(chrId: int, targetId: int, unknown: float, speed: float = -1.0):
    OP_33(0x3C, chrId, targetId, unknown, speed)

def ChrSetPosByTargetAsync(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int, unknown3: int):
    OP_33(0x39, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def ChrSetPosByTargetSync(chrId: int, targetId: int, x: float, y: float, forward: float, speed: float, unknown2: int, unknown3: int):
    OP_33(0x33, chrId, targetId, x, y, forward, speed, unknown2, unknown3)
