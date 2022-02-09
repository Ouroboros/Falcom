from Falcom.ED85.Parser.scena_writer import *
from Falcom.ED85.Parser.scena_writer_gen import *
from Falcom.ED83.Parser.consts import *

ChrTable = GlobalConfig.ChrTable
MAX_PARTY_CHR_ID = 0x3F

# utils

def ReturnToTitle():
    Call(ScriptId.System, 'FC_EventEndMapChange', (0xDD, 'title'), (0xDD, ''))

def SaveClearData():
    OP_90('current', 0x00000019)
    OP_93(0xD2, 0x0005)
    OP_93(0xD3)
    OP_93(0xDC)
    OP_93(0xDD)
    OP_93(0x00, 0x00)
    OP_93(0x01)

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

def ShowMenu(
        resultVar: int,
        level: int,
        *items: Tuple[str, Callable],
        height      = 0,
        fontSize    = 40.0,
        pos         = (0xFFFF, 0xFFFF),
        autoExit    = False,
        style       = 99,
    ):

    assert resultVar <= 0x100
    assert len(items)

    ExecExpressionWithVar(
        resultVar,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    menuLoop        = genLabel()
    menuCanceled    = genLabel()
    menuSwitchEnd   = genLabel()
    menuEnd         = genLabel()

    itemCases = []

    label(menuLoop)

    If(
        (
            (Expr.PushVar, resultVar),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        menuEnd,
    )

    MenuCreate(level, height, fontSize, style)

    for id, item in enumerate(items):
        id += 1
        MenuAddItem(level, item[0], id)
        itemCases.append((id, genLabel()))

    itemCases.append((-1, menuCanceled))

    MenuSetPos(level, 0x01, pos[0] & 0xFFFF, pos[1] & 0xFFFF, 0x01)
    MenuShow(level, resultVar)

    Switch(
        (
            (Expr.PushVar, resultVar),
            Expr.Return,
        ),
        *itemCases,
    )

    for i, item in enumerate(items):
        label(itemCases[i][1])
        item[1]()
        Jump(menuSwitchEnd)

    label(menuCanceled)

    ExecExpressionWithVar(
        resultVar,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump(menuLoop)

    label(menuSwitchEnd)

    if autoExit:
        ExecExpressionWithVar(
            resultVar,
            (
                (Expr.PushLong, 0xFFFFFFFF),
                Expr.Nop,
                Expr.Return,
            ),
        )

    Jump(menuLoop)

    label(menuEnd)

    MenuCmd(0x03, level)

def Switch2(expr: tuple, handlers: Dict[int, Callable]):
    handlers.setdefault(-1, lambda: None)

    cases: List[Tuple[int, str]] = []

    for id in sorted(handlers.keys()):
        if id == -1:
            continue

        cases.append((id, genLabel()))

    cases.append((-1, genLabel()))

    label_end = genLabel()

    Switch(expr, *cases)
    for i, case in enumerate(cases):
        label(case[1])
        handlers[case[0]]()
        Jump(label_end)

    label(label_end)

def ForEachTarget(cb, reg = 0):
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(reg, 0xFFFE)

    start = genLabel()
    end = genLabel()
    label(start)

    If(
        (
            (Expr.PushReg, reg),
            Expr.Return,
        ),
        end,
    )

    cb()

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        reg,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump(start)

    label(end)

    BattleTargetsIterReset(0x01, 0xFFFE)

# debug 0x07

def DebugString(s: str):
    DebugLog(0x02, ParamStr(s))


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
    AnimeClipCtrl(0x00, chrId, asset, symbol)

def AnimeClipRemoveSymbol(chrId: int, symbol: str):
    AnimeClipCtrl(0x01, chrId, '', symbol)

def AnimeClipLoadAsset(chrId: int, asset: str):
    AnimeClipCtrl(0x02, chrId, asset, '')

def AnimeClipAddAsset(chrId: int, asset: str):
    AnimeClipCtrl(0x04, chrId, asset, '')

def AnimeClipRemoveAsset(chrId: int, asset: str):
    AnimeClipCtrl(0x05, chrId, asset, '')

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

def AnimeClipLoadFace(chrId: int, asset: str):
    AnimeClipCtrl(0x0B, chrId, asset, '')

def AnimeClipSetChrPresetFaceModel(chrId: int, presetFaceModel: str):
    AnimeClipCtrl(0x0C, chrId, presetFaceModel, '')


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

def LoadEffect(chrId: int, slot: int, eff: str, flags: int = 0):
    EffectCtrl(0x0A, chrId, slot, eff, flags)

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

def WaitEffect(chrId: int, effid: int, arg3: int):
    EffectCtrl(0x10, chrId, effid, arg3)

def EffectSetRGBA(chrId: int, arg2: int, r: float, g: float, b: float, a: float, arg7: int, slot: int):
    EffectCtrl(0x14, chrId, arg2, r, g, b, a, arg7, slot)

# BattleCtrl 0x33

def BattleDamage(target: int, source: int, calc: int, arg4: int):
    BattleCtrl(0x00, target, source, calc, arg4)

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

def BattleKillTarget(chrId: int):
    BattleCtrl(0x14, chrId)

def BattleSetChrAfterImageOn(chrId: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
    BattleCtrl(0x15, chrId, arg1, arg2, arg3, arg4, arg5)

def BattleSetChrAfterImageOff(hideOnly: int):
    BattleCtrl(0x16, hideOnly)

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
    BattleCtrl(0x31, chrId)

def BattleSetChrPos(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int = 0, unknown3: int = 0):
    BattleCtrl(0x37, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def BattleMoveToTarget():
    BattleCtrl(0x38)

def BattleSaveChrPosition(targetChrId: int, unknown: int):
    BattleCtrl(0x3A, targetChrId, unknown)

def BattleSetChrPosAsync(chrId: int, targetId: int, x: float, y: float, z: float, speed: float, unknown2: int, unknown3: int):
    BattleCtrl(0x3E, chrId, targetId, x, y, z, speed, unknown2, unknown3)

def BattleTurnChrDirection(chrId: int, targetId: int, unknown: float, speed: float = -1.0):
    BattleCtrl(0x41, chrId, targetId, unknown, speed)

def BattleShowText(s: str):
    BattleCtrl(0x64, s)

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

def ReplaceBGMReset():
    BGMCtrl(0x05, 1, 1)

def SetMapBGM(bgm: int):
    BGMCtrl(0x06, bgm)

def PlaySE(sound: int):
    OP_3B(0x00, (0xFF, sound, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def PlayVoice(voice1: int, *, speed: float = 0.0):
    # OP_3B(0x3A, 0xFFFE, (0xFF, voice1, 0x0), (0xFF, voice2, 0x0), (0xFF, voice3, 0x0), (0xFF, voice4, 0x0))
    OP_3B(0x32, (0xFF, voice1, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, speed, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

def StopVoice(voice: int):
    OP_3B(0x34, (0xFF, voice, 0x0))


# formation 0x49

def FormationAddMember(chrId: int):
    FormationCtrl(0x00, chrId)

def FormationDelMember(chrId: int):
    FormationCtrl(0x01, chrId)

def FormationReset(releaseChar: int):
    FormationCtrl(0x02, releaseChar)

def FormationSetLeader(chrId: int):
    FormationCtrl(0x04, chrId)

def FormationHasMember(chrId: int):
    FormationCtrl(0x05, chrId)

# def FormationSetMembers(*chrId: int):
#     chrId = list(chrId)
#     if len(chrId) < 0x18:
#         chrId.extend([0xFFFF] * (len(chrId) - 0x18))

#     FormationCtrl(0x0D, *chrId)

# def FormationGetMemberCount():
#     FormationCtrl(0x10)


# model ctrl 0x54

def ModelSetChrId(chrId: int, modelChrId: int):
    ModelCtrl(0x53, chrId, modelChrId)

def ModelSetBattleStyle(chrId: int, style: int):
    ModelCtrl(0x4A, chrId, style)

def ModelGetBattleStyle(chrId: int):
    ModelCtrl(0x4B, chrId)

# check names 0x7A

def IsMapEqualTo(name: str):
    OP_7A(0x00, name)

def IsBattleModelEqualTo(chrId: int, name: str):
    OP_7A(0x01, chrId, name)

def IsAnimeClipEqualTo(chrId: int, name: str):
    OP_7A(0x02, chrId, name)
