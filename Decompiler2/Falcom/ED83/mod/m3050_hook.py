from Falcom.ED83.Parser.scena_writer_helper import *

def funcCallBack(name: str, f: Callable):
    match name:
        case 'EV_03_81_01': return EV_03_81_01
        case 'EV_03_81_00_END': return EV_03_81_00_END
        case _: pass

def runCallBack(g):
    from Falcom.ED83.Parser.scena_writer import _gScena as scena
    for f in [
        EV_03_99_00,
        EV_03_99_00_END,
    ]:
        scena.Code(f.__name__)(f)

def _init():
    from Falcom.ED83.Parser.scena_writer import _gScena as scena
    scena.registerFuncCallback(funcCallBack)
    scena.registerRunCallback(runCallBack)

_init()

def EV_03_81_00_END():
    OP_58(0xFF)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_4E(1.0, 0.0, 0x03)
    OP_6C(ChrTable['剛毅艾奈絲'], 1.0)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['銀臂2'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['安潔莉卡'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['悠娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['庫爾特'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞爾緹娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    SetScenaFlags(ScenaFlag(0x00BA, 5, 0x5D5))

    FormationReset()
    FormationAddMember(0x00)
    FormationAddMember(0x05)
    FormationAddMember(0x0C)
    FormationAddMember(0x10)
    FormationSetLeader(0)

    Battle(0x00, 0x00000001, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

def EV_03_99_00():
    EV_Template(True)

def EV_03_99_00_END():
    OP_58(0xFF)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_4E(1.0, 0.0, 0x03)
    OP_6C(ChrTable['剛毅艾奈絲'], 1.0)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['銀臂2'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['安潔莉卡'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['悠娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['庫爾特'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞爾緹娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    SetScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))
    Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

def EV_03_81_01():
    return EV_Template(False)

def EV_Template(before_second_battle):
    if before_second_battle:
        Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3140, 0x0))
        ClearScenaFlags(ScenaFlag(0x00BA, 5, 0x5D5))
    else:
        Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3123, 0x0))
        ClearScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))

    loc_BE15 = genLabel()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        loc_BE15,
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_BE15(): pass

    label(loc_BE15)

    PlayBGM(311, 1.0, 0x0000, 0x00000000, 0x00)

    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_SVIS0318', '')
    OP_55(0x01, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_SVIS0318_01', '')
    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evret_01.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evr22_00.eff')
    LoadEffect(0xFFFF, 0xCC, 'event/evr22_01.eff')
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEvDead1', 'AniEv00025', 'AniEvSquat', 'AniEv00024', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['尤西斯'], 0x00, 'AniEvDead1', 'AniEvSquat', 'AniEvGyu', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['米莉亞姆'], 0x00, 'AniEvDead1', 'AniEvSquat', 'AniEvRyoteGyu', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['蓋烏斯'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['莎拉'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvDead1', 'AniEvWeak', 'AniEvBtlWait', 'AniEvFieldAttackEnd', 'AniEv34085', 'AniEvDead2', '', '', '', '', '', '', '', '', '', '')

    if before_second_battle:
        AnimeClipLoadMultiple(ChrTable['悠娜'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', 'AniEvPhoneLook', 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '')

    else:
        AnimeClipLoadMultiple(ChrTable['悠娜'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', 'AniEvPhoneLook', 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['安潔莉卡'], 0x00, 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['亞修'], 0x00, 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
        AnimeClipLoadMultiple(ChrTable['妙婕'], 0x00, 'AniEvDead1', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')

    AnimeClipLoadMultiple(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvDead1', 'AniEv32030', 'AniEvPhoneHold', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['神速杜巴莉'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvk1023', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')

    # ClearScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))

    OP_3B(0x37, 0x00002B60)
    OP_3B(0x37, 0x00002BC6)
    OP_3B(0x37, 0x00002C28)
    OP_3B(0x37, 0x00002CF1)
    OP_3B(0x37, 0x00002C8D)
    OP_3B(0x37, 0x00002F45)
    OP_3B(0x37, 0x0000300D)
    OP_3B(0x37, 0x00003071)
    OP_3B(0x37, 0x000030D5)
    SetChrPos(ChrTable['黎恩'], -35.96, 114.0, -2.89, 283.0)
    SetChrPos(ChrTable['尤西斯'], -34.95, 114.0, -1.53, 267.0)
    SetChrPos(ChrTable['米莉亞姆'], -33.56, 114.0, 0.16, 250.7)
    SetChrPos(ChrTable['蓋烏斯'], -34.12, 114.0, -4.59, 274.5)
    SetChrPos(ChrTable['莎拉'], -35.32, 114.0, 0.35, 265.3)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -38.02, 114.0, -0.83, 270.6)
    ChrSetPhysicsFlags(ChrTable['黎恩'], 0x00000010)
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['尤西斯'], 0x00000010)
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['米莉亞姆'], 0x00000010)
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['蓋烏斯'], 0x00000010)
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['莎拉'], 0x00000010)
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['奧蕾莉亞分校長'], 0x00000010)
    OP_38(ChrTable['奧蕾莉亞分校長'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['奧蕾莉亞分校長'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)

    if before_second_battle:
        SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    else:
        SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvDead2', -1.0, 1.0, 0x00000000)

    SetChrFace(0x03, ChrTable['黎恩'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['莎拉'], 0.0, 35.0, 0.0, 0x0000, 0x0000)
    SetChrPos(ChrTable['安潔莉卡'], -35.79, 114.0, -16.17, 354.3)
    SetChrPos(ChrTable['悠娜'], -34.68, 114.0, -14.7, 340.8)
    SetChrPos(ChrTable['庫爾特'], -35.08, 114.0, -15.6, 341.4)
    SetChrPos(ChrTable['亞爾緹娜'], -33.74, 114.0, -14.7, 333.3)
    SetChrPos(ChrTable['亞修'], -33.85, 114.0, -15.6, 333.5)
    SetChrPos(ChrTable['妙婕'], -33.0, 114.0, -15.1, 325.2)

    if before_second_battle:
        SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvOdoroki', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000001)

    else:
        pass
        SetChrAniFunction(ChrTable['安潔莉卡'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000001)
        SetChrAniFunction(ChrTable['妙婕'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000001)

    SetChrFace(0x03, ChrTable['悠娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.25, 114.0, -0.97, 84.7)
    SetChrPos(ChrTable['神速杜巴莉'], -48.35, 114.0, -2.69, 72.0)
    SetChrPos(ChrTable['剛毅艾奈絲'], -49.23, 114.0, -5.26, 62.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -47.69, 114.0, -0.0, 98.0)
    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000010)
    OP_38(ChrTable['鋼之雅里安洛德'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['鋼之雅里安洛德'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000010)
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000010)
    OP_38(ChrTable['剛毅艾奈絲'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['剛毅艾奈絲'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000010)
    OP_38(ChrTable['魔弓恩奈雅'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['魔弓恩奈雅'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)

    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvGourei', -1.0, 1.0, 0x00000000)

    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniAttachMainWeapon', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniAttachMainWeapon', -1.0, 1.0, 0x00000000)

    # SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '1', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '0', 'A', '0[autoB0]', '#b', '0')

    SetChrFace(0x03, ChrTable['神速杜巴莉'], 'C', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['鋼之雅里安洛德'], 0x0000)
    SetChrPos(ChrTable['永世α'], -60.45, 114.0, -0.3, 90.0)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1023', -1.0, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    CameraSetPos(-38.45, 116.82, -2.22, 0)
    CameraRotate(351.0, 99.0, 0.0, 0, 0x01)
    CameraSetDistance(4.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    # PlayBGM(311, 1.0, 0x0000, 0x00000000, 0x00)
    Call(ScriptId.Sound, 'Init_ENVSE')
    CameraSetPos(-34.22, 114.92, -2.24, 6000)
    CameraRotate(357.0, 104.0, 354.0, 6000, 0x01)
    CameraSetDistance(4.3, 6000)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(-38.71, 115.27, -1.96, 0)
    CameraRotate(17.0, 232.0, 0.0, 0, 0x01)
    CameraSetDistance(1.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(-36.75, 114.87, -1.5, 12000)
    CameraRotate(10.0, 232.0, 0.0, 12000, 0x01)
    CameraSetDistance(1.6, 12000)
    Fade(0xFF, 0, 0x0000)
    Sleep(1500)
    OP_45(ChrTable['尤西斯'], 0.0, 30.0, 0.0, 0x05DC, 0x0000)
    SetChrFace(0x03, ChrTable['尤西斯'], '9998[autoE8]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_8#M_E#B_0')

    if before_second_battle:
        ChrTalk(
            ChrTable['尤西斯'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x905E),
                '這就是……極致嗎。',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
        SetChrFace(0x04, ChrTable['莎拉'], '#E[9]#M_E#B_0')

        ChrTalk(
            ChrTable['莎拉'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x905F),
                '唔，修行還不夠呢……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

    else:
        ChrTalk(
            ChrTable['尤西斯'],
            0x00000000,
            (
                '這……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
        SetChrFace(0x04, ChrTable['莎拉'], '#E[9]#M_E#B_0')

        ChrTalk(
            ChrTable['莎拉'],
            0x00000000,
            (
                '剛才居然……不是全力嗎……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()


    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)

    CameraCtrl(0x00)

    # CameraSetPos(-45.28, 114.74, -0.27, 0)
    CameraSetPos(-45.11, 114.78, -0.6, 0)

    CameraRotate(8.0, 52.0, 352.0, 0, 0x01)
    CameraSetDistance(2.5, 0)
    CameraCtrl(0x0B, 0x03, 32.9, 0x0000)

    # CameraSetPos(-45.99, 114.64, -1.06, 15000)
    CameraSetPos(-45.08, 115.14, -0.58, 3000)

    CameraRotate(6.0, 43.0, 1.0, 15000, 0x01)
    CameraSetDistance(2.1, 15000)

    OP_45(ChrTable['尤西斯'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['尤西斯'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], 0xFFFF, 0x0000)
    OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['莎拉'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)

    if before_second_battle:
        SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E_8#M_8#B_0')
        ChrTalk(
            ChrTable['魔弓恩奈雅'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9060),
                '主人居然會……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

        SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E_8#M_2#B_0')
        ChrTalk(
            ChrTable['剛毅艾奈絲'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9061),
                '被打敗……？',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

        OP_45(ChrTable['神速杜巴莉'], 20.0, -30.0, 0.0, 0x03E8, 0x0000)
        SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[B]#M_8#B_0')

        ChrTalk(
            ChrTable['神速杜巴莉'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9062),
                '不、不可能……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

    else:
        SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[11C]#M_8#B_0')
        ChrTalk(
            ChrTable['神速杜巴莉'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x90B1),
                '主、主人……？',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

        SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E[C]#M_8#B_0')
        ChrTalk(
            ChrTable['剛毅艾奈絲'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x90B2),
                '那、那個難道是……',
                TxtCtl.Enter,
            ),
        )
        WaitForMsg()

        SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E_8#M_8#B_0')
        ChrTalk(
            ChrTable['魔弓恩奈雅'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x8CFF),
                '呵呵，何等驚人的實力……',
                TxtCtl.Enter,
            ),
        )
        WaitForMsg()

    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)

    CameraCtrl(0x00)

    if before_second_battle:
        CameraSetPos(-34.66, 115.17, -14.32, 0)
        CameraRotate(358.0, 351.0, 355.0, 0, 0x01)
        CameraSetDistance(2.3, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        CameraSetPos(-34.67, 115.25, -14.43, 20000)
        CameraRotate(356.0, 2.0, 355.0, 20000, 0x01)
        CameraSetDistance(1.6, 20000)

    else:
        CameraSetPos(-34.66, 115.17 - 0.5, -14.32, 0)
        CameraRotate(358.0, 351.0, 355.0, 0, 0x01)
        CameraSetDistance(3.2, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        CameraSetPos(-34.67, 115.25 - 0.5, -14.43, 20000)
        CameraRotate(356.0, 2.0, 355.0, 20000, 0x01)
        CameraSetDistance(2.6, 20000)

    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], 0xFFFF, 0x0000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)

    if before_second_battle:
        SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvWait1', 1.0, 0.8, 0x00000000)
        SetChrFace(0x04, ChrTable['亞修'], '#E[C]#M[H]#B_0')
        ChrTalk(
            ChrTable['亞修'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x2CF3),
                '………………………',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

    else:
        SetChrFace(0x04, ChrTable['亞修'], '#E[C]#M[H]#B_0')
        ChrTalk(
            ChrTable['亞修'],
            0x00000000,
            (
                '好驚人的鬥氣……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

        SetChrFace(0x04, ChrTable['庫爾特'], '#E[C]#M_8#B_0')
        ChrTalk(
            ChrTable['庫爾特'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9064),
                '武的化境……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        OP_45(ChrTable['安潔莉卡'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
        SetChrFace(0x04, ChrTable['安潔莉卡'], '#E[3]#M_2#B_0')

        ChrTalk(
            ChrTable['安潔莉卡'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9065),
                '這已經可以\n',
                '紀錄在帝國史上了……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)

    CameraCtrl(0x00)
    # CameraSetPos(-43.86, 114.41, -1.24, 0)
    CameraSetPos( -45.11, 114.79, -0.8, 0)

    CameraRotate(13.0, 126.0, 3.0, 0, 0x01)

    # CameraSetDistance(0.9, 0)
    CameraSetDistance(2.1, 0)

    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)

    # CameraSetPos(-44.29, 114.55, -1.17, 15000)
    CameraSetPos(-45.08, 115.14, -0.9, 3000)

    CameraRotate(6.0, 119.0, 4.0, 15000, 0x01)

    OP_45(ChrTable['安潔莉卡'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['安潔莉卡'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['安潔莉卡'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(2000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[3]#M_2#B_0')

    if before_second_battle:
        ChrTalk(
            ChrTable['鋼之雅里安洛德'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9066),
                '……老實說，我很驚訝。',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        OP_63(0xFFFF, 0x01)
        Fade(0x65, 800, 1.0, 0x0000)
        Fade(0xFE, 0)

        CameraCtrl(0x00)

        # CameraSetPos(-45.11, 114.79, -0.6, 0)
        CameraSetPos(-45.08, 115.14, -0.58, 0)

        CameraRotate(3.0, 281.0, 358.0, 0, 0x01)
        CameraSetDistance(2.4, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        CameraSetPos(-45.08, 115.14, -0.58, 3000)
        CameraRotate(4.0, 288.0, 358.0, 25000, 0x01)
        CameraSetDistance(2.1, 25000)

        SetChrPos(ChrTable['尤西斯'], -34.42, 114.0, -2.13, 272.9)
        SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
        SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
        SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
        SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
        SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
        SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
        OP_46(0x00, ChrTable['黎恩'], ChrTable['鋼之雅里安洛德'], 0x0000)
        OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
        OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
        OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
        OP_46(0x00, ChrTable['莎拉'], ChrTable['鋼之雅里安洛德'], 0x0000)
        OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x0000)
        SetChrPos(ChrTable['神速杜巴莉'], -48.58, 114.0, -2.76, 72.0)
        SetChrPos(ChrTable['魔弓恩奈雅'], -48.12, 114.0, 0.76, 98.0)
        Fade(0xFF, 0, 0x0000)

        # 起身
        # SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv32030', -1.0, 0.7, 0x00000000)

        # CameraCtrl(0x07, 0x0002)

        SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_0#B_0')

        ChrTalk(
            ChrTable['鋼之雅里安洛德'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9067),
                '現在的妳\n',
                '已經比曾經的我更強了……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        OP_63(0xFFFF, 0x01)
        Fade(0x65, 500, 1.0, 0x0000)
        Fade(0xFE, 0)
        CameraCtrl(0x00)
        CameraSetPos(-44.87, 115.46, -0.97, 0)
        CameraRotate(8.0, 61.0, 3.0, 0, 0x01)
        CameraSetDistance(0.9, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        OP_7E(0x00)
        OP_7E(0x02, 0x0001)
        OP_7E(0x05, 5.0)
        OP_7E(0x06, 0x0001)
        CameraSetPos(-44.87, 115.46, -0.97, 10000)
        CameraRotate(2.0, 66.0, 3.0, 10000, 0x01)
        SetChrPos(ChrTable['鋼之雅里安洛德'], -45.25, 114.0, -0.97, 90.4)
        SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], 'E', 'A[autoMA]', '0[autoB0]', '#b', '0')
        OP_45(ChrTable['鋼之雅里安洛德'], -20.0, -8.0, 0.0, 0x0000, 0x0000)
        Fade(0xFF, 0, 0x0000)
        SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[EEEEEEEEEEEE0]#M_A#B_0')

        ChrTalk(
            ChrTable['鋼之雅里安洛德'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9068),
                '呵呵，雖然很不甘心，\n',
                '但我不得不承認。',
                TxtCtl.Enter,
            ),
        )

        Sleep(800)
        OP_45(ChrTable['鋼之雅里安洛德'], -5.0, 0.0, 0.0, 0x05DC, 0x0000)
        WaitForMsg()

        OP_63(0xFFFF, 0x01)
        Fade(0x65, 500, 1.0, 0x0000)
        Fade(0xFE, 0)
        CameraCtrl(0x00)
        CameraSetPos(-37.07, 114.79, -2.79, 0)
        CameraRotate(8.0, 308.0, 3.0, 0, 0x01)
        CameraSetDistance(0.9, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        OP_7E(0x00)
        OP_7E(0x02, 0x0001)
        OP_7E(0x05, 20.0)
        OP_7E(0x06, 0x0001)
        CameraSetPos(-36.98, 114.79, -2.83, 20000)
        CameraRotate(3.0, 300.0, 1.0, 20000, 0x01)
        Fade(0xFF, 0, 0x0000)
        SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M[H]#B_0')

        ChrTalk(
            ChrTable['黎恩'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x9069),
                '啊……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

        ChrTalk(
            ChrTable['蓋烏斯'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x906A),
                '……所以是，超越了聖女嗎。',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

        SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_A#B_0')

        ChrTalk(
            ChrTable['奧蕾莉亞分校長'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x906B),
                '呵呵……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

    else:
        OP_63(0xFFFF, 0x01)
        Fade(0x65, 500, 1.0, 0x0000)
        Fade(0xFE, 0)
        CameraCtrl(0x00)
        CameraSetPos(-37.07, 114.79, -2.79, 0)
        CameraRotate(8.0, 308.0, 3.0, 0, 0x01)
        CameraSetDistance(0.9, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        OP_7E(0x00)
        OP_7E(0x02, 0x0001)
        OP_7E(0x05, 20.0)
        OP_7E(0x06, 0x0001)
        CameraSetPos(-36.98, 114.79, -2.83, 20000)
        CameraRotate(3.0, 300.0, 1.0, 20000, 0x01)
        Fade(0xFF, 0, 0x0000)

        SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

        ChrTalk(
            ChrTable['蓋烏斯'],
            0x00000000,
            (
                '還是沒能超越聖女……嗎。',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()

    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)

    CameraCtrl(0x00)

    if before_second_battle:
        # CameraSetPos(-38.46, 115.46, -0.85, 0)
        CameraSetPos(-40, 114.5, -0.5, 0)

        CameraRotate(11.0, 281.0, 0.0, 0, 0x01)
        # CameraSetDistance(1.0, 0)
        CameraSetDistance(0.9, 0)

        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        # CameraSetPos(-38.38, 115.45, -0.85, 20000)
        CameraSetPos(-39.2, 114.5, -0.7, 20000)

        # CameraRotate(0.0, 294.0, 0.0, 20000, 0x01)
        CameraRotate(0.0, 281.0, 0.0, 20000, 0x01)

        # 起身
        # SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvBtlWait', 1.0, 0.8, 0x00000000)
        Fade(0xFF, 0, 0x0000)
        # SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_0#M_A#B_0')

        ChrTalk(
            ChrTable['奧蕾莉亞分校長'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x906C),
                '因為我的年紀\n',
                '比活著時的妳還要多一倍……',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
        SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '1', '2[autoM2]', '0[autoB0]', '#b', '0')
        Sleep(500)

    else:
        SetChrPos(ChrTable['奧蕾莉亞分校長'], -38.02, 114.0 + 0.13, -0.83, 270.6)

        CameraSetPos(-39.5, 114.5 + 1.0, -0.5, 0)
        CameraRotate(31.0, 281.0, 0.0, 0, 0x01)
        CameraSetDistance(1.3, 0)
        CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
        CameraSetPos(-38.7, 114.5 + 1.0, -0.7, 10000)
        CameraRotate(60.0, 281.0, 0.0, 10000, 0x01)
        CameraSetDistance(1.8, 10000)

        Fade(0xFF, 0, 0x0000)

        SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_2#B_0')

        ChrTalk(
            ChrTable['奧蕾莉亞分校長'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x906D),
                '……我能到達的境界\n',
                '就到此為止了嗎。',
                TxtCtl.Enter,
            ),
        )

        WaitForMsg()
        Sleep(500)

        # ReturnToTitle()

        # SetChrPos(ChrTable['奧蕾莉亞分校長'], -38.02, 114.0, -0.83, 270.6)

    # 收剑
    # SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvFieldAttackEnd', -1.0, 0.8, 0x00000000)
    # Sleep(1500)

    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-43.69, 115.2, -0.72, 0)
    CameraRotate(354.0, 67.0, 0.0, 0, 0x01)
    CameraSetDistance(1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(-44.37, 115.3, -0.82, 15000)
    CameraRotate(352.0, 72.0, 0.0, 15000, 0x01)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -5.0, 0.0, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1111111110]#M_0#B_0')

    if before_second_battle:
        PlayBGM(466, 1.0, 0x0000, 0x00000000, 0x00)
        ChrTalk(
            ChrTable['鋼之雅里安洛德'],
            0x00000000,
            (
                # (TxtCtl.Voice, 0x913D),
                # '#3K呵呵……這樣啊。',
                # TxtCtl.Enter,
                # TxtCtl.Clear,
                (TxtCtl.Voice, 0x8CC2),
                '呵呵，這也是個好機會。',
                TxtCtl.Enter,
                TxtCtl.Clear,
                (TxtCtl.Voice, 0x1B5D),
                '那我就稍微认真一下吧。',
                TxtCtl.Enter,
            ),
        )
        Sleep(800)
        WaitForMsg()

        OP_63(0xFFFF, 0x00)
        OP_56(0x17, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 300.0)
        OP_4E(0.1, 0.0, 0x03)
        Sleep(45)
        OP_27('', 0xFFFF)
        OP_3B(0x01, (0xFF, 0x7714, 0x0), (0xFF, 0x1F4, 0x0))
        OP_AC(0x06)

        Return()

        return

    else:
        ChrTalk(
            ChrTable['鋼之雅里安洛德'],
            0x00000000,
            (
                (TxtCtl.Voice, 0x906E),
                '是的──再往上，\n',
                '就是與《巨碩之存在》有關之人的領域了。',
                TxtCtl.Enter,
            ),
        )
        Sleep(800)
        OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
        WaitForMsg()

    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-35.85, 115.13, -2.41, 0)
    CameraRotate(358.0, 101.0, 0.0, 0, 0x01)
    CameraSetDistance(5.2, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraRotate(359.0, 102.0, 6.0, 20000, 0x01)
    CameraSetDistance(5.7, 1500)
    SetChrPos(ChrTable['米莉亞姆'], -33.78, 114.0, -0.59, 250.7)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_44(0x0000, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0006, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0009, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0008, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000F, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0010, 0x15, 0.15, 0x0000, 0.0)
    Sleep(1000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906F),
            '什麼……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['莎拉'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9070),
            '那個詞……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9071),
            '在那個《夢幻迴廊》的盡頭\n',
            '所聽到的……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Call(ScriptId.Sound, 'Stop_ENVSE_VAR', (0xFF, 0x1F4, 0x0))
    OP_3A(0x03, 0.4, 0x01F4, 0x00)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    OP_57(0x00, 0x03)
    Sleep(1500)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    OP_57(0x01, 0x03)
    CameraCtrl(0x00)
    Sleep(1500)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], 0xFFFF, 0x0000)
    SetChrPos(ChrTable['黎恩'], -35.96, 114.0, -2.89, 271.3)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.25, 114.0, -0.97, 104.5)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniDetachMainWeapon', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['黎恩'], 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    CameraSetPos(-44.69, 115.44, -1.25, 0)
    CameraRotate(2.0, 122.0, 0.0, 0, 0x01)
    CameraSetDistance(1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(-44.75, 115.44, -1.37, 15000)
    CameraRotate(351.0, 106.0, 0.0, 15000, 0x01)
    Call(ScriptId.Sound, 'Init_ENVSE_VAR', (0xFF, 0x3E8, 0x0))
    OP_3A(0x03, 0.7, 0x03E8, 0x00)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 0.0)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 750.0)
    OP_57(0x01, 0x03)
    Sleep(750)
    OP_3A(0x01, 0x0FA0, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9072),
            '《灰》之啟動者，\n',
            '黎恩・舒華澤。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['鋼之雅里安洛德'], 30.0, 0.0, 0.0, 0x05DC, 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '33332[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9073),
            '以及準啟動者們。\n',
            '──你們都做好覺悟了吧？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-36.43, 115.49, -2.93, 0)
    CameraRotate(3.0, 240.0, 0.0, 0, 0x01)
    CameraSetDistance(1.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(-36.43, 115.49, -2.93, 6000)
    CameraRotate(0.0, 243.0, 0.0, 6000, 0x01)
    CameraSetDistance(1.0, 6000)
    SetChrPos(ChrTable['永世α'], -60.45, 114.0, -1.94, 90.0)
    SetChrPos(ChrTable['安潔莉卡'], -37.23, 114.0, -13.0, 356.4)
    SetChrPos(ChrTable['悠娜'], -35.89, 114.0, -10.7, 355.2)
    SetChrPos(ChrTable['庫爾特'], -36.63, 114.0, -11.46, 356.2)
    SetChrPos(ChrTable['亞爾緹娜'], -35.21, 114.0, -11.19, 354.8)
    SetChrPos(ChrTable['亞修'], -34.51, 114.0, -12.48, 346.4)
    SetChrPos(ChrTable['妙婕'], -34.02, 114.0, -11.49, 347.8)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['悠娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞修'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['黎恩'], 0x0000)
    ChrClearPhysicsFlags(ChrTable['黎恩'], 0x00000010)
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvSquat', -1.0, 0.8, 0x00000002)
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    Sleep(800)
    CameraCtrl(0x0A, 0.02, 0.02, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9074),
            '#4S正合我意──！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_3A(0x02, 0x00)
    PlayBGM(460, 0.7, 0x0000, 0x00000000, 0x00)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-36.38, 115.54, -2.64, 0)
    CameraRotate(9.0, 320.0, 4.0, 0, 0x01)
    CameraSetDistance(1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(-36.38, 115.56, -2.64, 20000)
    CameraRotate(8.0, 349.0, 4.0, 20000, 0x01)
    SetChrFace(0x03, ChrTable['黎恩'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv00024', 1.0, 1.0, 0x00000000)
    SetChrPos(ChrTable['尤西斯'], -33.48, 114.0, -1.66, 272.9)
    SetChrPos(ChrTable['米莉亞姆'], -33.8, 114.0, -0.53, 250.7)
    SetChrPos(ChrTable['莎拉'], -35.32, 114.0, 0.35, 265.3)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -36.33, 114.0, -0.66, 270.6)
    ChrClearPhysicsFlags(ChrTable['莎拉'], 0x00000010)
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrClearPhysicsFlags(ChrTable['尤西斯'], 0x00000010)
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrClearPhysicsFlags(ChrTable['米莉亞姆'], 0x00000010)
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['黎恩'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9075),
            '接下來才是重頭戲……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['黎恩'], -50.0, 0.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '336[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(300)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9076),
            '悠娜、庫爾特、亞爾緹娜、\n',
            '亞修和妙婕！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['黎恩'], 0.0, -10.0, 0.0, 0x04B0, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '6667', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[7]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9077),
            '以及尤西斯、米莉亞姆、\n',
            '蓋烏斯和莎拉教官！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-35.69, 116.49, -2.09, 0)
    CameraRotate(355.0, 90.0, 6.0, 0, 0x01)
    CameraSetDistance(5.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(-34.33, 115.6, -2.13, 8000)
    CameraRotate(355.0, 91.0, 6.0, 8000, 0x01)
    CameraSetDistance(4.8, 8000)
    SetChrPos(ChrTable['黎恩'], -35.95, 114.0, -2.56, 271.3)
    SetChrPos(ChrTable['蓋烏斯'], -33.87, 114.0, -3.95, 274.5)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['黎恩'], 0x0000)
    ChrClearPhysicsFlags(ChrTable['蓋烏斯'], 0x00000010)
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['黎恩'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9078),
            '#4S請你們──助我一臂之力！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvRyoteGyu', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvGyu', -1.0, 1.0, 0x00000000)
    CreateThread(ChrTable['莎拉'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    CreateThread(ChrTable['蓋烏斯'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    Sleep(500)
    CameraCtrl(0x0A, 0.02, 0.02, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0004, 0.5, 0x012C, 0x0320, 0x01F4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CreateThread(0xFFFF, 0x02, ScriptId.Sound, 'VOICE_YES_03_81_01')
    OP_27('新舊Ⅶ班', 0xFFFF)
    SetChrFace(0x04, ChrTable['悠娜'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x2B60),
            '#6S喔！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-55.47, 119.19, -3.17, 0)
    CameraRotate(6.0, 128.0, 3.0, 0, 0x01)
    CameraSetDistance(9.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(-51.95, 117.17, 1.36, 6000)
    CameraRotate(348.0, 56.0, 352.0, 6000, 0x01)
    CameraSetDistance(11.2, 6000)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x763C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(800)
    OP_3B(0x00, (0xFF, 0x7737, 0x0), 0.7, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7593, 0x0), 0.5, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCB, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    OP_3B(0x01, (0xFF, 0x7737, 0x0), (0xFF, 0xFA0, 0x0))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-35.75, 115.39, -2.78, 0)
    CameraRotate(3.0, 312.0, 13.0, 0, 0x01)
    CameraSetDistance(1.7, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[7777777777776]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x2B0A),
            '#5S來吧─#20W─\n',
            '#1000W《灰之騎神》瓦利瑪！！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)
    CameraCtrl(0x09, 0.05, 0.05, 0.2)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv00025', 1.0, 1.0, 0x00000000)
    CameraSetPos(-35.98, 115.65, -2.7, 1200)
    CameraRotate(28.0, 270.0, 350.0, 1200, 0x01)
    CameraSetDistance(1.5, 1200)
    CameraCtrl(0x0B, 0x03, 34.0, 0x04B0)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-35.81, 115.34, -10.21, 0)
    CameraRotate(9.0, 19.0, 6.0, 0, 0x01)
    CameraSetDistance(1.6, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    CameraSetPos(-35.8, 115.28, -10.43, 15000)
    CameraRotate(359.0, 28.0, 6.0, 15000, 0x01)
    SetChrPos(ChrTable['悠娜'], -35.89, 114.0, -10.7, 355.2)
    SetChrPos(ChrTable['庫爾特'], -36.66, 114.0, -11.3, 26.8)
    SetChrPos(ChrTable['亞爾緹娜'], -35.39, 114.0, -11.21, 354.8)
    SetChrPos(ChrTable['亞修'], -34.82, 114.0, -12.28, 30.3)
    SetChrPos(ChrTable['妙婕'], -33.67, 114.0, -11.63, 295.7)
    SetChrFace(0x03, ChrTable['悠娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['悠娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞修'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['黎恩'], 0x0000)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvPhoneTalk', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvPhoneLook', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvPhoneTalk', -1.0, 1.2, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    Sleep(1800)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[3322222222222222222332]#M_2#B[777777777777777777770]')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x907B),
            '緹妲，拜託妳！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['庫爾特'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['庫爾特'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x907C),
            '勇士和鷹隼就拜託了！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x907D),
            '現在地點，以信標修正！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(-34.56, 115.33, -11.9, 0)
    CameraRotate(7.0, 247.0, 5.0, 0, 0x01)
    CameraSetDistance(1.7, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    CameraSetPos(-34.56, 115.4, -11.9, 6000)
    CameraRotate(10.0, 253.0, 5.0, 6000, 0x01)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_46(0x00, ChrTable['亞修'], ChrTable['妙婕'], 0x03E8)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['亞修'], 0x03E8)
    Sleep(1500)
    OP_45(ChrTable['亞修'], 0.0, -20.0, 0.0, 0x01F4, 0x0000)
    OP_45(ChrTable['妙婕'], 0.0, -20.0, 0.0, 0x01F4, 0x0000)
    SetChrFace(0x03, ChrTable['亞修'], '33333332', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '33333332', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    OP_45(ChrTable['亞修'], 0.0, 0.0, 0.0, 0x01F4, 0x0000)
    OP_45(ChrTable['妙婕'], 0.0, 0.0, 0.0, 0x01F4, 0x0000)
    Sleep(1000)
    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_AC(0x06)

    Return()

