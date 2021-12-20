from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *

ChrTable = GlobalConfig.ChrTable

L_ARM_POINT = 'L_arm_point'
R_ARM_POINT = 'R_arm_point'
NODE_R_ARM  = 'NODE_R_ARM'

DummyCharBaseId         = 0xB5E
TempCharBaseId          = 0xB68

class CraftTarget(IntEnum2):
    Saved           = 0xFFF4
    SelectedPos     = 0xFFF5
    Current         = 0xFFFB
    Self            = 0xFFFE

class AbnormalCondition(IntEnum2):
    Poison              = 0x00000001
    Seal                = 0x00000002
    Mute                = 0x00000004
    Blind               = 0x00000008
    Sleep               = 0x00000010
    Burn                = 0x00000020
    Freeze              = 0x00000040
    Petrify             = 0x00000080
    Faint               = 0x00000100
    Confuse             = 0x00000200
    Charm               = 0x00000400
    Deathblow           = 0x00000800
    Nightmare           = 0x00001000
    Delay               = 0x00002000
    Vanish              = 0x00004000
    STRDown             = 0x00008000
    DEFDown             = 0x00010000
    ATSDown             = 0x00020000
    ADFDown             = 0x00040000
    SPDDown             = 0x00080000
    MOVDown             = 0x00100000
    Insight             = 0x00200000
    SlowHPRecover       = 0x00400000
    SlowCPRecover       = 0x00800000
    CraftGuard          = 0x01000000
    MagicReflect        = 0x02000000
    PhysicalReflect     = 0x04000000
    SpiritUnification   = 0x08000000
    Possess             = 0x10000000
    Stealth             = 0x20000000
    BalanceDown         = 0x40000000
    Death               = 0x80000000

class AbnormalCondition2(IntEnum2):
    BurningHeart            = 0x00000001
    HPUpDownVitality        = 0x00000002
    AlmightyConflagration   = 0x00000004
    TemporaryHPboost        = 0x00000008
    GuardBreak              = 0x00000010
    LinkBreak               = 0x00000020
    Enhanced                = 0x00000040
    Brandish                = 0x00000100
    ProtectionAgainstAll    = 0x00000200
    AbsoluteReflect         = 0x00000400
    CantMove                = 0x00000800
    ElementWeakness         = 0x00001000
    Hide                    = 0x00004000

def ForEachTarget(cb):
    ChrTargetsIterInit(0x00)
    ChrTargetsIterReset(0x01, 0xFFFE)

    start = genLabel()
    end = genLabel()
    label(start)

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        end,
    )

    cb()

    ChrTargetsIterNext(0xFFFE)

    OP_0A(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump(start)

    label(end)

    ChrTargetsIterReset(0x01, 0xFFFE)

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

def CameraSetPos(x: float, y: float, z: float, durationInMs: int = 0):
    CameraCtrl(0x02, 0x03, x, y, z, durationInMs)

def CameraRotateByTarget(chrId: int, node: str, byte3: int, vertical: float, horizontal: float, tilt: float, durationInMs: int, byte8: int):
    CameraCtrl(0x13, chrId, node, byte3, vertical, horizontal, tilt, durationInMs, byte8)

def CameraSetPosByTarget(chrId: int, node: str, x: float, y: float, z: float, durationInMs: int):
    CameraCtrl(0x14, 0x03, chrId, node, x, y, z, durationInMs)

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
    x                   : float,
    y                   : float,
    z                   : float,
    rotate_vertical     : float,
    rotate_horizontal   : float,
    rotate_tilt         : float,
    scale_y             : float,
    scale_x             : float,    # ?
    scale_z             : float,
    slot                : int,
):
    EffectCtrl(
        0x0C,
        chrId,
        (0xFF, effectId, 0),
        targetChrId,
        unknown,
        (0xDD, node),
        (0xEE, x, 0),
        (0xEE, y, 0),
        (0xEE, z, 0),
        rotate_vertical,
        rotate_horizontal,
        rotate_tilt,
        (0xEE, scale_y, 0),
        (0xEE, scale_x, 0),
        (0xEE, scale_z, 0),
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

def ChrLoadAnimeClipByCatalog(chrId: int, catalog: int):
    ChrAnimeClipCtrl(0x06, chrId, catalog)

def ChrReleaseAnimeClipByCatalog(chrId: int, catalog: int):
    ChrAnimeClipCtrl(0x07, chrId, catalog)


'''
    battle chr
'''

def ChrSetAbnormalCondition(chrId: int, condition: AbnormalCondition, param1: int, param2: int, unused: int):
    BattleChrCtrl(0xB7, 0x00, chrId, condition, param1, param2, unused)

def ChrClearAbnormalCondition(chrId: int, condition: AbnormalCondition):
    BattleChrCtrl(0xB7, 0x01, chrId, condition, 0, 0, 0)

def ChrSetAbnormalCondition2(chrId: int, condition: AbnormalCondition2, param1: int, param2: int, se: int):
    BattleChrCtrl(0xB7, 0x02, chrId, condition, param1, param2, se)

def ChrClearAbnormalCondition2(chrId: int, condition: AbnormalCondition2):
    BattleChrCtrl(0xB7, 0x03, chrId, condition, 0, 0, 0)

def ChrPlayAnimeClipSeq(chrId: int, group: int, *animeClips: str):
    assert len(animeClips) <= 16
    if len(animeClips) < 16:
        animeClips: list = list(animeClips)
        animeClips.extend([''] * (16 - len(animeClips)))

    ChrAnimeClipCtrl(0x08, chrId, group, *animeClips)

def ChrTargetsIterInit(unknown: int):
    BattleChrCtrl(0x04, unknown)

def ChrTargetsIterReset(regIndex: int, chrId: int):
    BattleChrCtrl(0x02, regIndex, chrId)

def ChrTargetsIterNext(chrId: int):
    BattleChrCtrl(0x03, chrId)

def ChrSavePosition(targetChrId: int, unknown: int):
    BattleChrCtrl(0x35, targetChrId, unknown)

def ChrSetPhysicsFlags(chrId: int, flags: int):
    OP_35(0x00, chrId, flags)

def ChrClearPhysicsFlags(chrId: int, flags: int):
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
    assert tempChrIndex <= 4
    OP_33(0x1E, tempChrIndex, srcChrId, model, ani)
    return tempChrIndex + TempCharBaseId

def ChrDeleteTempChar(tempChrIndex: int = 0xFFFF):
    assert tempChrIndex <= 4 or tempChrIndex == 0xFFFF
    OP_33(0x1F, tempChrIndex)

def PlaySE(sound: int):
    OP_3B(0x00, (0xFF, sound, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def PlayVoice(voice1: int):
    # OP_3B(0x3A, 0xFFFE, (0xFF, voice1, 0x0), (0xFF, voice2, 0x0), (0xFF, voice3, 0x0), (0xFF, voice4, 0x0))
    OP_3B(0x32, (0xFF, voice1, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def IsBattleModelEqualTo(chrId: int, model: str):
    OP_7A(0x01, chrId, model)

def ChrMoveToTarget():
    OP_33(0x34)

def ChrTurnDirection(chrId: int, targetId: int, unknown: float, speed: float = -1.0):
    OP_33(0x3C, chrId, targetId, unknown, speed)

def ChrSetPosByTarget(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int = 0, unknown3: int = 0):
    OP_33(0x33, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def ChrSetPosByTargetAsync(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int, unknown3: int):
    OP_33(0x39, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def ChrSetBattleFlags(chrId: int, flags: int):
    OP_33(0x0B, chrId, flags)

def ChrClearBattleFlags(chrId: int, flags: int):
    OP_33(0x0C, chrId, flags)

def ChrGetBattleFlags(chrId: int):
    OP_33(0x0D, chrId)
