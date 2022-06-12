from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *
from Falcom.ED83.Parser.consts import *

ChrTable = GlobalConfig.ChrTable
ItemTable = GlobalConfig.ItemTable
CraftTable = GlobalConfig.CraftTable

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
    FormationCmd(0x00, chrId)

def FormationReset():
    FormationCmd(0x02)

def FormationSetLeader(chrId: int):
    FormationCmd(0x04, chrId)


# model ctrl 0x54

def ModelSetChrId(chrId: int, modelChrId: int):
    ModelCmd(0x53, chrId, modelChrId)

def ModelSetBattleStyle(chrId: int, style: int):
    ModelCmd(0x4A, chrId, style)

def ModelGetBattleStyle(chrId: int):
    ModelCmd(0x4B, chrId)


# event 0xAC

def EventJump(eventId: int):
    OP_AC(0x01, eventId)

# debug 0x07

def DebugString(s: str):
    OP_07(0x02, (0xDD, s))


# menu cmd 0x29

def MenuCreate(level: int, height: int, fontSize: float, color: int = 0):
    MenuCmd(0x00, level, height, fontSize, color)

def MenuAddItem(level: int, text: str, id: int):
    MenuCmd(0x01, level, text, id)

def MenuSetPos(level: int, arg2: int, x: int, y: int, arg5: int):
    MenuCmd(0x02, level, arg2, x & 0xFFFF, y & 0xFFFF, arg5)

def MenuShow(level: int, resultVar: int):
    MenuCmd(0x04, level, resultVar)


# anime clip 0x2F

def AnimeClipAddSymbol(chrId: int, asset: str, symbol: str):
    AnimeClipCmd(0x00, chrId, asset, symbol)

def AnimeClipRemoveSymbol(chrId: int, symbol: str):
    AnimeClipCmd(0x01, chrId, '', symbol)

def AnimeClipLoadAsset(chrId: int, asset: str):
    AnimeClipCmd(0x02, chrId, asset, '')

def AnimeClipAddAsset(chrId: int, asset: str):
    AnimeClipCmd(0x04, chrId, asset, '')

def AnimeClipRemoveAsset(chrId: int, asset: str):
    AnimeClipCmd(0x05, chrId, asset, '')

def AnimeClipLoadByCatalog(chrId: int, catalog: int):
    AnimeClipCmd(0x06, chrId, catalog)

def AnimeClipReleaseByCatalog(chrId: int, catalog: int):
    AnimeClipCmd(0x07, chrId, catalog)

def AnimeClipLoadMultiple(chrId: int, group: int, *animeClips: str):
    assert len(animeClips) <= 16
    if len(animeClips) < 16:
        animeClips: list = list(animeClips)
        animeClips.extend([''] * (16 - len(animeClips)))

    AnimeClipCmd(0x08, chrId, group, *animeClips)

def AnimeClipRefreshSkin(chrId: int):
    return AnimeClipChangeSkin(chrId, '')

def AnimeClipChangeSkin(chrId: int, model: str):
    AnimeClipCmd(0x0A, chrId, model, '')

def AnimeClipLoadFace(chrId: int, asset: str):
    AnimeClipCmd(0x0B, chrId, asset, '')

def AnimeClipSetChrPresetFaceModel(chrId: int, presetFaceModel: str):
    AnimeClipCmd(0x0C, chrId, presetFaceModel, '')



# equip 0x30

def AttachEquip(chrId: int, equip: str, node: str, *args):
    if not args:
        args = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    # EquipCmd(0x00, 0xFFFE, 'C_EQU090', 'R_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCmd(0x00, chrId, equip, node, *args)

def DeatchEquip(chrId: int, node: str, *args):
    if not args:
        args = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    # EquipCmd(0x01, 0xFFFE, '', 'L_arm_point', 0, 0, 0, 0, 0, 0, 1, 1, 1)
    EquipCmd(0x01, chrId, '', node, *args)

# asset 0x31

def LoadAsset(asset: str):
    AssetCmd(0x00, asset)

def ReleaseAsset(asset: str):
    AssetCmd(0x01, asset)

def IsAssetLoaded(asset: str):
    AssetCmd(0x02, asset)

def LoadAssetAsync(asset: str):
    AssetCmd(0x03, asset)


# effect 0x32

def LoadEffect(chrId: int, slot: int, eff: str):
    EffectCmd(0x0A, chrId, slot, eff)

def ReleaseEffect(chrId: int, slot: int):
    EffectCmd(0x0B, chrId, slot)

def PlayEffect(chrId: int, effectId: tuple, targetChrId: int, *args):
    EffectCmd(0x0C, chrId, effectId, targetChrId, *args)

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
    EffectCmd(
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
    EffectCmd(0x0D, chrId, slot, unknown)

def WaitEffect(chrId: int, effid: int, arg3: int):
    EffectCmd(0x10, chrId, effid, arg3)

def EffectSetRGBA(chrId: int, arg2: int, r: float, g: float, b: float, a: float, arg7: int, slot: int):
    EffectCmd(0x14, chrId, arg2, r, g, b, a, arg7, slot)

# battle 0x33

def BattleDamage(targetChr: int, sourceChr: int, calc: int):
    BattleCmd(0x00, targetChr, sourceChr, calc)

def BattleDamageAnime(targetChr: int, knockBack: tuple, arg3: tuple, arg4: int):
    BattleCmd(0x01, targetChr, knockBack, arg3, arg4)

def BattleDamageAnime2(targetChr: int, knockBack: float, arg3: float, arg4: int = 1):
    BattleCmd(0x01, targetChr, ParamFloat(knockBack), ParamFloat(arg3), arg4)

def BattleTargetsIterReset(regIndex: int, chrId: int):
    BattleCmd(0x02, regIndex, chrId)

def BattleTargetsIterNext(chrId: int):
    BattleCmd(0x03, chrId)

def BattleTargetsIterInit(unknown: int):
    BattleCmd(0x04, unknown)

def BattleInitHit(chrId: int):
    BattleCmd(0x09, chrId)

def BattleSetChrFlags(chrId: int, flags: int):
    BattleCmd(0x0B, chrId, flags)

def BattleClearChrFlags(chrId: int, flags: int):
    BattleCmd(0x0C, chrId, flags)

def BattleGetChrFlags(chrId: int):
    BattleCmd(0x0D, chrId)

def BattleKillTarget(chrId: int):
    BattleCmd(0x14, chrId)

def BattleSetChrAfterImageOn(chrId: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
    BattleCmd(0x15, chrId, arg1, arg2, arg3, arg4, arg5)

def BattleSetChrAfterImageOff():
    BattleCmd(0x16)

def BattleCreateChrDummy(chrId: int, count: int):
    assert count <= 5
    BattleCmd(0x17, chrId, count)

def BattleDeleteChrDummy():
    BattleCmd(0x18)

def BattleSetFlags(flags: int):
    BattleCmd(0x19, flags)

def BattleClearFlags(flags: int):
    BattleCmd(0x1A, flags)

def BattleCreateTempChar(tempChrIndex: int, srcChrId: int, model: str, ani: str = '') -> int:
    assert tempChrIndex <= 4
    BattleCmd(0x1E, tempChrIndex, srcChrId, model, ani)
    return tempChrIndex + TempCharBaseId

def BattleDeleteTempChar(tempChrIndex: int = 0xFFFF):
    assert tempChrIndex <= 4 or tempChrIndex == 0xFFFF
    BattleCmd(0x1F, tempChrIndex)

def BattleCreateFollowChar(chrId: int, arg2: float, arg3: float):
    BattleCmd(0x20, chrId, arg2, arg3)

def BattleCreateChrAfterImage(chrId: int):
    BattleCmd(0x30, chrId)

def BattleSetChrPos(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int = 0, unknown3: int = 0):
    BattleCmd(0x33, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def BattleMoveToTarget():
    BattleCmd(0x34)

def BattleSaveChrPosition(targetChrId: int, unknown: int):
    BattleCmd(0x35, targetChrId, unknown)

def BattleSetChrPosAsync(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int, unknown3: int):
    BattleCmd(0x39, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def BattleTurnChrDirection(chrId: int, targetId: int, unknown: float, speed: float = -1.0):
    BattleCmd(0x3C, chrId, targetId, unknown, speed)

def BattleSetChrATDelay(chrId: int, atdelay: int):
    BattleCmd(0x5A, chrId, atdelay)

def BattleSetChrStatus(chrId: int, status: BattleStatus, param1: object, param2: object, param3: object, param4: object):
    BattleCmd(0x61, chrId, status, param1, param2, param3, param4)

def BattleGetChrStatus(chrId: int, status: BattleStatus):
    BattleCmd(0x62, chrId, status)

def BattleShowText(s: str):
    BattleCmd(0x64, s)

def BattleSetChrAbnormalStatus(chrId: int, status: AbnormalStatus, param1: int, param2: int, unused: int = 0):
    BattleCmd(0xB7, 0x00, chrId, status, param1, param2, unused)

def BattleClearChrAbnormalStatus(chrId: int, status: AbnormalStatus):
    BattleCmd(0xB7, 0x01, chrId, status, 0, 0, 0)

def BattleSetChrAbnormalStatus2(chrId: int, status: AbnormalStatus2, param1: int, param2: int, se: int):
    BattleCmd(0xB7, 0x02, chrId, status, param1, param2, se)

def BattleClearChrAbnormalStatus2(chrId: int, status: AbnormalStatus2):
    BattleCmd(0xB7, 0x03, chrId, status, 0, 0, 0)

def BattleGetChrAbnormalStatus(chrId: int):
    BattleCmd(0xB7, 0x04, chrId, 0, 0, 0, 0)

def BattleGetChrAbnormalStatus2(chrId: int):
    BattleCmd(0xB7, 0x05, chrId, 0, 0, 0, 0)

# Physics 0x35

def ChrSetPhysicsFlags(chrId: int, flags: int):
    OP_35(0x00, chrId, flags)

def ChrClearPhysicsFlags(chrId: int, flags: int):
    OP_35(0x01, chrId, flags)


# camera 0x36

def CameraSetPos(n: int, x: float, y: float, z: float, durationInMs: int = 0):
    CameraCmd(0x02, n, x, y, z, durationInMs)

def CameraRotate(n: int, vertical: float, horizontal: float, tilt: float, durationInMs: int = 0, unknown: int = 1):
    '''
        上下
        左右
        翻转
    '''
    CameraCmd(0x04, n, vertical, horizontal, tilt, durationInMs, unknown)

def CameraSetDistance(n: int, distance: float, durationInMs: int = 0):
    CameraCmd(0x05, n, distance, durationInMs)

def CameraRotateByTarget(chrId: int, node: str, byte3: int, vertical: float, horizontal: float, tilt: float, durationInMs: int, byte8: int):
    CameraCmd(0x13, chrId, node, byte3, vertical, horizontal, tilt, durationInMs, byte8)

def CameraSetPosByTarget(n: int, chrId: int, node: str, x: float, y: float, z: float, durationInMs: int):
    CameraCmd(0x14, n, chrId, node, x, y, z, durationInMs)

def CameraSetHeight(n: int, height: float, durationInMs: int = 0):
    CameraCmd(0x16, n, height, durationInMs)

def CameraShake():
    CameraCmd(0x0A, 0.2, 0.125, 0.01, 0x001E, 0x012C, 0x003C, 0x0000, 0x0000, 0x00)


# sound 0x3A 0x3B

def PlayBGM(bgm: int, volume: float, duration: int, arg4: int, slot: int):
    BGMCmd(0x00, bgm, volume, duration, arg4, slot)

def StopBGM(duration: int, slot: int):
    BGMCmd(0x01, duration, slot)

def PlayBGM2(bgm: int, volume: float = 1.0):
    BGMCmd(0x00, bgm, volume, 0x0000, 0x00000000, 0x00)

def SetBGMVolume(volume: float, duration: int, slot: int):
    BGMCmd(0x03, volume, duration, slot)

def ReplaceBGM(old: int, new: int):
    BGMCmd(0x05, old, new)

def SetMapBGM(bgm: int):
    BGMCmd(0x06, bgm)

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