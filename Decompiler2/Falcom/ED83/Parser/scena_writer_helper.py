from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *
from Falcom.ED83.Parser.consts import *

ChrTable = GlobalConfig.ChrTable

def ForEachTarget(cb):
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)

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

    BattleTargetsIterNext(0xFFFE)

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

    BattleTargetsIterReset(0x01, 0xFFFE)

def RandIf(probability, true_succ, false_succ):
    assert 0 <= probability <= 100

    end    = genLabel()
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

    true_succ and true_succ()
    Jump(end)

    label(false)

    false_succ and false_succ()

    label(end)

def ReturnToTitle():
    Call(0x0A, 'FC_EventEndMapChange', (0xDD, 'title'), (0xDD, ''))

def SaveClearData():
    OP_90('current', 0x00000019)
    OP_93(0x00, 0x02)
    OP_93(0x01)


# formation 0x49

def FormationAddMember(chrId: int):
    FormationCtrl(0x00, chrId)

def FormationReset():
    FormationCtrl(0x02)

def FormationSetLeader(chrId: int):
    FormationCtrl(0x04, chrId)


# model ctrl 0x54

def ModelSetChrId(chrId: int, modelChrId: int):
    ModelCtrl(0x53, chrId, modelChrId)

def ModelSetBattleStyle(chrId: int, style: int):
    ModelCtrl(0x4A, chrId, style)

def ModelGetBattleStyle(chrId: int):
    ModelCtrl(0x4B, chrId)


'''
    event
'''

def EventJump(eventId: int):
    OP_AC(0x01, eventId)

'''
    debug
'''

def DebugString(s: str):
    OP_07(0x02, (0xDD, s))


# anime clip 0x2F

def AnimeClipLoadByCatalog(chrId: int, catalog: int):
    AnimeClipCtrl(0x06, chrId, catalog)

def AnimeClipReleaseByCatalog(chrId: int, catalog: int):
    AnimeClipCtrl(0x07, chrId, catalog)

def AnimeClipLoadMultiple(chrId: int, group: int, *animeClips: str):
    assert len(animeClips) <= 16
    if len(animeClips) < 16:
        animeClips: list = list(animeClips)
        animeClips.extend([''] * (16 - len(animeClips)))

    AnimeClipCtrl(0x08, chrId, group, *animeClips)

def AnimeClipRefreshSkin(chrId: int):
    return AnimeClipChangeSkin(chrId, '')

def AnimeClipChangeSkin(chrId: int, model: str):
    AnimeClipCtrl(0x0A, chrId, model, '')

# equip 0x30

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

# asset 0x31

def LoadAsset(asset: str):
    AssetCtrl(0x00, asset)

def ReleaseAsset(asset: str):
    AssetCtrl(0x01, asset)

def IsAssetLoaded(asset: str):
    AssetCtrl(0x02, asset)

def LoadAssetAsync(asset: str):
    AssetCtrl(0x03, asset)


# effect 0x32

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


# battle 0x33

def BattleDamage(targetChr: int, sourceChr: int, calc: int):
    BattleCtrl(0x00, targetChr, sourceChr, calc)

def BattleDamageAnime(targetChr: int, knockBack: tuple, arg3: tuple, arg4: int):
    BattleCtrl(0x01, targetChr, knockBack, arg3, arg4)

def BattleDamageAnime2(targetChr: int, knockBack: float, arg3: float, arg4: int = 1):
    BattleCtrl(0x01, targetChr, (0xEE, knockBack, 0x0), (0xEE, arg3, 0x0), arg4)

def BattleTargetsIterReset(regIndex: int, chrId: int):
    BattleCtrl(0x02, regIndex, chrId)

def BattleTargetsIterNext(chrId: int):
    BattleCtrl(0x03, chrId)

def BattleTargetsIterInit(unknown: int):
    BattleCtrl(0x04, unknown)

def BattleInitHit(chrId: int):
    BattleCtrl(0x09, chrId)

def BattleSetChrFlags(chrId: int, flags: int):
    BattleCtrl(0x0B, chrId, flags)

def BattleClearChrFlags(chrId: int, flags: int):
    BattleCtrl(0x0C, chrId, flags)

def BattleGetChrFlags(chrId: int):
    BattleCtrl(0x0D, chrId)

def BattleSetChrAfterImageOn(chrId: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
    BattleCtrl(0x15, chrId, arg1, arg2, arg3, arg4, arg5)

def BattleSetChrAfterImageOff():
    BattleCtrl(0x16)

def BattleCreateChrDummy(chrId: int, count: int):
    assert count <= 5
    BattleCtrl(0x17, chrId, count)

def BattleDeleteChrDummy():
    BattleCtrl(0x18)

def BattleSetFlags(flags: int):
    BattleCtrl(0x19, flags)

def BattleClearFlags(flags: int):
    BattleCtrl(0x1A, flags)

def BattleCreateTempChar(tempChrIndex: int, srcChrId: int, model: str, ani: str = '') -> int:
    assert tempChrIndex <= 4
    BattleCtrl(0x1E, tempChrIndex, srcChrId, model, ani)
    return tempChrIndex + TempCharBaseId

def BattleDeleteTempChar(tempChrIndex: int = 0xFFFF):
    assert tempChrIndex <= 4 or tempChrIndex == 0xFFFF
    BattleCtrl(0x1F, tempChrIndex)

def BattleCreateChrAfterImage(chrId: int):
    BattleCtrl(0x30, chrId)

def BattleSetChrPos(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int = 0, unknown3: int = 0):
    BattleCtrl(0x33, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def BattleMoveToTarget():
    BattleCtrl(0x34)

def BattleSaveChrPosition(targetChrId: int, unknown: int):
    BattleCtrl(0x35, targetChrId, unknown)

def BattleSetChrPosAsync(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int, unknown3: int):
    BattleCtrl(0x39, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def BattleTurnChrDirection(chrId: int, targetId: int, unknown: float, speed: float = -1.0):
    BattleCtrl(0x3C, chrId, targetId, unknown, speed)

def BattleSetChrAbnormalCondition(chrId: int, condition: AbnormalCondition, param1: int, param2: int, unused: int = 0):
    BattleCtrl(0xB7, 0x00, chrId, condition, param1, param2, unused)

def BattleClearChrAbnormalCondition(chrId: int, condition: AbnormalCondition):
    BattleCtrl(0xB7, 0x01, chrId, condition, 0, 0, 0)

def BattleSetChrAbnormalCondition2(chrId: int, condition: AbnormalCondition2, param1: int, param2: int, se: int):
    BattleCtrl(0xB7, 0x02, chrId, condition, param1, param2, se)

def BattleClearChrAbnormalCondition2(chrId: int, condition: AbnormalCondition2):
    BattleCtrl(0xB7, 0x03, chrId, condition, 0, 0, 0)

def BattleGetChrAbnormalCondition(chrId: int):
    BattleCtrl(0xB7, 0x04, chrId, 0, 0, 0, 0)

def BattleGetChrAbnormalCondition2(chrId: int):
    BattleCtrl(0xB7, 0x05, chrId, 0, 0, 0, 0)

# Physics 0x35

def ChrSetPhysicsFlags(chrId: int, flags: int):
    OP_35(0x00, chrId, flags)

def ChrClearPhysicsFlags(chrId: int, flags: int):
    OP_35(0x01, chrId, flags)


# camera 0x36

def CameraSetPos(n: int, x: float, y: float, z: float, durationInMs: int = 0):
    CameraCtrl(0x02, n, x, y, z, durationInMs)

def CameraRotate(n: int, vertical: float, horizontal: float, tilt: float, durationInMs: int = 0, unknown: int = 1):
    '''
        上下
        左右
        翻转
    '''
    CameraCtrl(0x04, n, vertical, horizontal, tilt, durationInMs, unknown)

def CameraSetDistance(n: int, distance: float, durationInMs: int = 0):
    CameraCtrl(0x05, n, distance, durationInMs)

def CameraRotateByTarget(chrId: int, node: str, byte3: int, vertical: float, horizontal: float, tilt: float, durationInMs: int, byte8: int):
    CameraCtrl(0x13, chrId, node, byte3, vertical, horizontal, tilt, durationInMs, byte8)

def CameraSetPosByTarget(n: int, chrId: int, node: str, x: float, y: float, z: float, durationInMs: int):
    CameraCtrl(0x14, n, chrId, node, x, y, z, durationInMs)

def CameraSetHeight(n: int, height: float, durationInMs: int = 0):
    CameraCtrl(0x16, n, height, durationInMs)

def CameraShake():
    CameraCtrl(0x0A, 0.2, 0.125, 0.01, 0x001E, 0x012C, 0x003C, 0x0000, 0x0000, 0x00)


# sound 0x3A 0x3B

def PlayBGM(bgm: int, arg2: float, arg3: int, arg4: int, arg5: int):
    BGMCtrl(0x00, bgm, arg2, arg3, arg4, arg5)

def StopBGM(bgm: int, arg2: int):
    BGMCtrl(0x01, bgm, arg2)

def PlayBGM2(bgm: int):
    BGMCtrl(0x00, bgm, 1.0, 0x0000, 0x00000000, 0x00)

def ReplaceBGM(old: int, new: int):
    BGMCtrl(0x05, old, new)

def SetMapBGM(bgm: int):
    BGMCtrl(0x06, bgm)

def PlaySE(sound: int):
    OP_3B(0x00, (0xFF, sound, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def PlayVoice(voice1: int, *, speed: float = 0.0):
    # OP_3B(0x3A, 0xFFFE, (0xFF, voice1, 0x0), (0xFF, voice2, 0x0), (0xFF, voice3, 0x0), (0xFF, voice4, 0x0))
    OP_3B(0x32, (0xFF, voice1, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, speed, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def StopVoice(voice: int):
    OP_3B(0x34, (0xFF, voice, 0x0))


# check names 0x7A

def IsMapEqualTo(name: str):
    OP_7A(0x00, name)

def IsBattleModelEqualTo(chrId: int, name: str):
    OP_7A(0x01, chrId, name)

def IsAnimeClipEqualTo(chrId: int, name: str):
    OP_7A(0x02, chrId, name)