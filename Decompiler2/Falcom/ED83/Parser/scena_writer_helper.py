from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *

ChrTable = GlobalConfig.ChrTable

L_ARM_POINT = 'L_arm_point'
R_ARM_POINT = 'R_arm_point'

DummyCharBaseId         = 0xB5E
TempCharBaseId          = 0xB68

TargetSaved             = 0xFFF4
TargetSelectedPos       = 0xFFF5
TargetSelectedTarget    = 0xFFFB
TargetSelf              = 0xFFFE

def RandIf(probability, true_succ, false_succ):
    assert 0 <= probability <= 100

    end     = genLabel()
    false  = genLabel()
    end    = genLabel()

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 100),
            Expr.Mod,
            (Expr.PushLong, probability),
            Expr.Lss,
            Expr.Return,
        ),
        false,
    )

    true_succ()
    Jump(end)

    label(false)

    false_succ()

    label(end)

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
    debug
'''

def DebugString(s: str):
    OP_07(0x02, (0xDD, s))

'''
    camera
'''

def CameraRotate(vertical: float, horizontal: float, tilt: float, durationInMs: int = 0, unknown: int = 1):
    '''
        上下
        左右
        翻转
    '''
    OP_36(0x04, 0x03, vertical, horizontal, tilt, durationInMs, unknown)
    return

def CameraSetPos(x: float, y: float, z: float, unknwon: int = 0):
    CameraCtrl(0x02, 0x03, x, y, z, unknwon)

def CameraRotateByTarget(chrId: int, node: str, byte3: int, vertical: float, horizontal: float, tilt: float, durationInMs: int, byte8: int):
    CameraCtrl(0x13, chrId, node, byte3, vertical, horizontal, tilt, durationInMs, byte8)

def CameraSetPosByTarget(chrId: int, node: str, horizontal: float, vertical: float, depth: float, durationInMs: int):
    CameraCtrl(0x14, 0x03, chrId, node, horizontal, vertical, depth, durationInMs)

def CameraSetDistance(distance: float, durationInMs: int = 0):
    CameraCtrl(0x05, 0x03, distance, durationInMs)

def CameraSetHeight(height: float, durationInMs: int = 0):
    CameraCtrl(0x16, 0x03, height, durationInMs)

def CameraShake():
    CameraCtrl(0x0A, 0.2, 0.125, 0.01, 0x001E, 0x012C, 0x003C, 0x0000, 0x0000, 0x00)


'''
    equip
'''

def AttachEquip(chrId: int, equip: str, node: str, *args):
    if not args:
        args = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    # EquipCtrl(0x00, 0xFFFE, 'C_EQU090', 'R_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCtrl(0x00, chrId, equip, node, *args)

def DeatchEquip(chrId: int, node: str, *args):
    if not args:
        args = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    # EquipCtrl(0x01, 0xFFFE, '', 'L_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCtrl(0x01, chrId, '', node, *args)


'''
    effect
'''

def LoadEffect(chrId: int, slot: int, eff: str):
    EffectCtrl(0x0A, chrId, slot, eff)

def ReleaseEffect(chrId: int, slot: int):
    EffectCtrl(0x0B, chrId, slot)

def PlayEffect(chrId: int, effectId: tuple, targetChrId: int, *args):
    EffectCtrl(0x0C, chrId, effectId, targetChrId, *args)

def PlayEffect2(
    chrId               : int,
    effectId            : int,
    targetChrId         : int,
    unknown             : int,
    node                : str,
    horizontal          : float,
    vertical            : float,
    depth               : float,
    rotate_vertical     : float,
    rotate_horizontal   : float,
    rotate_rotation     : float,
    scale_vertical      : float,
    scale_horizontal    : float,    # ?
    scale_depth         : float,
    slot                : int,
):
    EffectCtrl(
        0x0C,
        chrId,
        (0xFF, effectId, 0),
        targetChrId,
        unknown,
        (0xDD, node),
        (0xEE, horizontal, 0),
        (0xEE, vertical, 0),
        (0xEE, depth, 0),
        rotate_vertical,
        rotate_horizontal,
        rotate_rotation,
        (0xEE, scale_vertical, 0),
        (0xEE, scale_horizontal, 0),
        (0xEE, scale_depth, 0),
        slot,
    )

def StopEffect(chrId: int, slot: int, unknown: int):
    EffectCtrl(0x0D, chrId, slot, unknown)


'''
    asset
'''

def LoadAsset(asset: str):
    OP_31(0x00, asset)

def ReleaseAsset(asset: str):
    OP_31(0x01, asset)

def IsAssetLoaded(asset: str):
    OP_31(0x02, asset)

def LoadAssetAsync(asset: str):
    OP_31(0x03, asset)


'''
    battle chr
'''

def ChrSavePosition(targetChrId: int, unknown: int):
    BattleChrCtrl(0x35, targetChrId, unknown)

def ChrHide(chrId: int, flags: int):
    OP_35(0x00, chrId, flags)

def ChrShow(chrId: int, flags: int):
    OP_35(0x01, chrId, flags)

def ChrCreateDummy(chrId: int, count: int):
    assert count <= 5
    BattleChrCtrl(0x17, chrId, count)

def ChrCreateAfterImage(chrId: int):
    BattleChrCtrl(0x30, chrId)

def ChrSetAfterImageOn(chrId: int, unknown1: float, unknown2: float, unknown3: float, unknown4: float, unknown5: float):
    BattleChrCtrl(0x15, chrId, unknown1, unknown2, unknown3, unknown4, unknown5)

def ChrSetAfterImageOff():
    BattleChrCtrl(0x16)

def ChrCreateTempChar(tempChrIndex: int, srcChrId: int, model: str, ani: str = '') -> int:
    assert tempChrIndex < 4
    OP_33(0x1E, tempChrIndex, srcChrId, model, ani)
    return tempChrIndex + TempCharBaseId

def PlaySound(sound: int):
    OP_3B(0x00, (0xFF, sound, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def PlayVoice(voice1: int, voice2: int = 0, voice3: int = 0, voice4: int = 0):
    OP_3B(0x3A, 0xFFFE, (0xFF, voice1, 0x0), (0xFF, voice2, 0x0), (0xFF, voice3, 0x0), (0xFF, voice4, 0x0))

def IsBattleModelEqualTo(chrId: int, model: str):
    OP_7A(0x01, chrId, model)

def ChrMoveToTarget():
    OP_33(0x34)

def ChrTurnDirection(chrId: int, targetId: int, unknown: float, speed: float = -1.0):
    OP_33(0x3C, chrId, targetId, unknown, speed)

def ChrSetPosByTarget(chrId: int, targetId: int, horizontal: float, vertical: float, depth: float, speed: float, unknown2: int = 0, unknown3: int = 0):
    OP_33(0x33, chrId, targetId, horizontal, vertical, depth, speed, unknown2, unknown3)

def ChrSetPosByTargetAsync(chrId: int, targetId: int, horizontal: float, vertical: float, depth: float, speed: float, unknown2: int, unknown3: int):
    OP_33(0x39, chrId, targetId, horizontal, vertical, depth, speed, unknown2, unknown3)

def ChrSetBattleFlags(chrId: int, flags: int):
    OP_33(0x0B, chrId, flags)

def ChrClearBattleFlags(chrId: int, flags: int):
    OP_33(0x0C, chrId, flags)

def ChrGetBattleFlags(chrId: int):
    OP_33(0x0D, chrId)
