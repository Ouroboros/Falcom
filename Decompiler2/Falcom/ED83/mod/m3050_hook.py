from Falcom.ED83.Parser.scena_writer_helper import *

def funcCallBack(name: str, f: Callable):
    match name:
        case 'EV_03_81_01': return EV_03_81_01
        case _: pass

    pass

def EV_03_81_01():
    Call(0x0A, 'FC_EventBegin', (0xFF, 0x3123, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_BE15',
    )

    Call(0x0A, 'FC_TSMenu_Reset')
    OP_49(0x02)
    OP_49(0x00, 0x0000)
    OP_49(0x04, 0x0000)

    def _loc_BE15(): pass

    label('loc_BE15')

    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.000000, 1.000000, 1.000000, 0.000000, 0x00, 0x00, 'I_SVIS0318', '')
    OP_55(0x01, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.000000, 1.000000, 1.000000, 0.000000, 0x00, 0x00, 'I_SVIS0318_01', '')
    EffectCtrl(0x0A, 0xFFFF, 0xC8, 'event/evmm30_00.eff')
    EffectCtrl(0x0A, 0xFFFF, 0xC9, 'event/evbom010.eff')
    EffectCtrl(0x0A, 0xFFFF, 0xCA, 'event/evret_01.eff')
    EffectCtrl(0x0A, 0xFFFF, 0xCB, 'event/evr22_00.eff')
    EffectCtrl(0x0A, 0xFFFF, 0xCC, 'event/evr22_01.eff')

    CreateChr(
        ChrTable['尤西斯'],
        'C_CHR006',
        '尤西斯',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['米莉亞姆'],
        'C_CHR009',
        '米莉亞姆',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['蓋烏斯'],
        'C_CHR008',
        '蓋烏斯',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['莎拉'],
        'C_CHR017',
        '莎拉',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['奧蕾莉亞分校長'],
        'C_CHR021',
        '奧蕾莉亞',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['安潔莉卡'],
        'C_CHR019',
        '安潔莉卡',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['悠娜'],
        'C_CHR011',
        '悠娜',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['庫爾特'],
        'C_CHR010',
        '庫爾特',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['亞爾緹娜'],
        'C_CHR015',
        '亞爾緹娜',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['亞修'],
        'C_CHR012',
        '亞修',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['妙婕'],
        'C_CHR013',
        '妙婕',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['鋼之雅里安洛德'],
        'C_CHR033',
        '鋼之雅里安洛德',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['神速杜巴莉'],
        'C_CHR035',
        '神速杜巴莉',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['剛毅艾奈絲'],
        'C_CHR037',
        '剛毅艾奈絲',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['魔弓恩奈雅'],
        'C_CHR039',
        '魔弓恩奈雅',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    CreateChr(
        ChrTable['永世α'],
        'C_ROB022',
        '神機永世αⅡ',
        '',
        0x00,
        0x00000001,
        0x00000000,
        0.000000,
        0.000000,
        0.000000,
        0.000000,
        1.000000,
        1.600000,
        0.090000,
        '',
        '',
        0xFFFFFFFF,
        0x00,
        0.000000,
        0.000000,
        0x0000,
    )

    OP_1E(0x0000, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x0006, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x0009, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x0008, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x000F, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x0010, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x0012, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x000A, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x000B, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x000C, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x000E, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x000D, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x006C, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x006D, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x006E, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x006F, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    OP_1E(0x0339, 0x03, 0x0A, 'FC_chr_entry')
    OP_16(0x0000)
    ChrAnimeClipCtrl(0x08, ChrTable['黎恩'], 0x00, 'AniEvDead1', 'AniEv00025', 'AniEvSquat', 'AniEv00024', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['尤西斯'], 0x00, 'AniEvDead1', 'AniEvSquat', 'AniEvGyu', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['米莉亞姆'], 0x00, 'AniEvDead1', 'AniEvSquat', 'AniEvRyoteGyu', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['蓋烏斯'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['莎拉'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvDead1', 'AniEvWeak', 'AniEvBtlWait', 'AniEvFieldAttackEnd', 'AniEv34085', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['悠娜'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', 'AniEvPhoneLook', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvDead1', 'AniEv32030', 'AniEvPhoneHold', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['神速杜巴莉'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['魔弓恩奈雅'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['剛毅艾奈絲'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrAnimeClipCtrl(0x08, ChrTable['永世α'], 0x00, 'AniEvk1023', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_11(0x05D1)
    OP_3B(0x37, 0x00002B60)
    OP_3B(0x37, 0x00002BC6)
    OP_3B(0x37, 0x00002C28)
    OP_3B(0x37, 0x00002CF1)
    OP_3B(0x37, 0x00002C8D)
    OP_3B(0x37, 0x00002F45)
    OP_3B(0x37, 0x0000300D)
    OP_3B(0x37, 0x00003071)
    OP_3B(0x37, 0x000030D5)
    SetChrPos(ChrTable['黎恩'], -35.959999, 114.000000, -2.890000, 283.000000)
    SetChrPos(ChrTable['尤西斯'], -34.950001, 114.000000, -1.530000, 267.000000)
    SetChrPos(ChrTable['米莉亞姆'], -33.560001, 114.000000, 0.160000, 250.699997)
    SetChrPos(ChrTable['蓋烏斯'], -34.119999, 114.000000, -4.590000, 274.500000)
    SetChrPos(ChrTable['莎拉'], -35.320000, 114.000000, 0.350000, 265.299988)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -38.020000, 114.000000, -0.830000, 270.600006)
    OP_35(0x00, ChrTable['黎恩'], 0x00000010)
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['尤西斯'], 0x00000010)
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['米莉亞姆'], 0x00000010)
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['蓋烏斯'], 0x00000010)
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['莎拉'], 0x00000010)
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['奧蕾莉亞分校長'], 0x00000010)
    OP_38(ChrTable['奧蕾莉亞分校長'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['奧蕾莉亞分校長'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrFace(0x03, ChrTable['黎恩'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['莎拉'], 0.000000, 35.000000, 0.000000, 0x0000, 0x0000)
    SetChrPos(ChrTable['安潔莉卡'], -35.790001, 114.000000, -16.170000, 354.299988)
    SetChrPos(ChrTable['悠娜'], -34.680000, 114.000000, -14.700000, 340.799988)
    SetChrPos(ChrTable['庫爾特'], -35.080002, 114.000000, -15.600000, 341.399994)
    SetChrPos(ChrTable['亞爾緹娜'], -33.740002, 114.000000, -14.700000, 333.299988)
    SetChrPos(ChrTable['亞修'], -33.849998, 114.000000, -15.600000, 333.500000)
    SetChrPos(ChrTable['妙婕'], -33.000000, 114.000000, -15.100000, 325.200012)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvOdoroki', -1.000000, 1.000000, 0x00000001)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', -1.000000, 1.000000, 0x00000001)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', -1.000000, 1.000000, 0x00000001)
    SetChrFace(0x03, ChrTable['悠娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.250000, 114.000000, -0.970000, 84.699997)
    SetChrPos(ChrTable['神速杜巴莉'], -48.349998, 114.000000, -2.690000, 72.000000)
    SetChrPos(ChrTable['剛毅艾奈絲'], -49.230000, 114.000000, -5.260000, 62.799999)
    SetChrPos(ChrTable['魔弓恩奈雅'], -47.689999, 114.000000, -0.000000, 98.000000)
    OP_35(0x00, ChrTable['鋼之雅里安洛德'], 0x00000010)
    OP_38(ChrTable['鋼之雅里安洛德'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['鋼之雅里安洛德'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['神速杜巴莉'], 0x00000010)
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['剛毅艾奈絲'], 0x00000010)
    OP_38(ChrTable['剛毅艾奈絲'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['剛毅艾奈絲'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x00, ChrTable['魔弓恩奈雅'], 0x00000010)
    OP_38(ChrTable['魔弓恩奈雅'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['魔弓恩奈雅'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)

    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvGourei', -1.000000, 1.000000, 0x00000000)

    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvDead1', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniAttachMainWeapon', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniAttachMainWeapon', -1.000000, 1.000000, 0x00000000)

    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '0', 'A', '0[autoB0]', '#b', '0')
    # SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1111111110]#M_0#B_0')

    SetChrFace(0x03, ChrTable['神速杜巴莉'], 'C', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['鋼之雅里安洛德'], 0x0000)
    SetChrPos(ChrTable['永世α'], -60.450001, 114.000000, -0.300000, 90.000000)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1023', -1.000000, 1.000000, 0x00000000)
    EffectCtrl(0x0C, 0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.000000, 0.000000, 0.000000, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    CameraCtrl(0x02, 0x03, -38.450001, 116.820000, -2.220000, 0)
    CameraCtrl(0x04, 0x03, 351.000000, 99.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 4.300000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.000000)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    OP_3A(0x00, 0x0137, 1.000000, 0x0000, 0x00000000, 0x00)
    Call(0x15, 'Init_ENVSE')
    CameraCtrl(0x02, 0x03, -34.220001, 114.919998, -2.240000, 6000)
    CameraCtrl(0x04, 0x03, 357.000000, 104.000000, 354.000000, 6000, 0x01)
    CameraCtrl(0x05, 0x03, 4.300000, 6000)
    Fade(0x64, 1000, 1.000000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    OP_16(0x01F4)
    Fade(0x65, 800, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x02, 0x03, -38.709999, 115.269997, -1.960000, 0)
    CameraCtrl(0x04, 0x03, 17.000000, 232.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.100000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.000000)
    OP_7E(0x06, 0x0001)
    CameraCtrl(0x02, 0x03, -36.750000, 114.870003, -1.500000, 12000)
    CameraCtrl(0x04, 0x03, 10.000000, 232.000000, 0.000000, 12000, 0x01)
    CameraCtrl(0x05, 0x03, 1.600000, 12000)
    Fade(0xFF, 0, 0x0000)
    OP_16(0x05DC)
    OP_45(ChrTable['尤西斯'], 0.000000, 30.000000, 0.000000, 0x05DC, 0x0000)
    SetChrFace(0x03, ChrTable['尤西斯'], '9998[autoE8]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3A(0x03, 0.700000, 0x01F4, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_8#M_E#B_0')

    ChrTalk(
        0x0006,
        0x00000000,
        (
            (TxtCtl.Voice, 0x905E),
            '這就是……極致嗎。',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['莎拉'], 0.000000, 0.000000, 0.000000, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['莎拉'], '#E[9]#M_E#B_0')

    ChrTalk(
        0x000F,
        0x00000000,
        (
            (TxtCtl.Voice, 0x905F),
            '唔，修行還不夠呢……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)

    # CameraCtrl(0x02, 0x03, -45.279999, 104.739998, -2.270000, 0)
    CameraCtrl(0x02, 0x03, -45.110001, 114.790001, -0.600000, 0)

    CameraCtrl(0x04, 0x03, 8.000000, 52.000000, 352.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 2.500000, 0)
    CameraCtrl(0x0B, 0x03, 32.900002, 0x0000)

    # CameraCtrl(0x02, 0x03, -45.990002, 104.639999, -2.060000, 15000)
    CameraCtrl(0x02, 0x03, -45.080002, 115.139999, -0.580000, 3000)

    CameraCtrl(0x04, 0x03, 6.000000, 43.000000, 1.000000, 15000, 0x01)
    CameraCtrl(0x05, 0x03, 2.100000, 15000)
    OP_45(ChrTable['尤西斯'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0001)
    OP_45(ChrTable['尤西斯'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], 0xFFFF, 0x0000)
    OP_45(ChrTable['莎拉'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0001)
    OP_45(ChrTable['莎拉'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['莎拉'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E_8#M_8#B_0')

    ChrTalk(
        0x006F,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9060),
            '我居然會……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E_8#M_2#B_0')

    ChrTalk(
        0x006E,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9061),
            '被這瘋女人打敗……？',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['神速杜巴莉'], 20.000000, -30.000000, 0.000000, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[B]#M_8#B_0')

    ChrTalk(
        0x006D,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9062),
            '不、不可能……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -34.660000, 115.169998, -14.320000, 0)
    CameraCtrl(0x04, 0x03, 358.000000, 351.000000, 355.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 2.300000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -34.669998, 115.250000, -14.430000, 20000)
    CameraCtrl(0x04, 0x03, 356.000000, 2.000000, 355.000000, 20000, 0x01)
    CameraCtrl(0x05, 0x03, 1.600000, 20000)
    OP_45(ChrTable['神速杜巴莉'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0001)
    OP_45(ChrTable['神速杜巴莉'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], 0xFFFF, 0x0000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvWait1', 1.000000, 0.800000, 0x00000000)
    SetChrFace(0x04, ChrTable['亞修'], '#E[C]#M[H]#B_0')

    ChrTalk(
        0x000E,
        0x00000000,
        (
            (TxtCtl.Voice, 0x2CF3),
            '………………………',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['庫爾特'], '#E[C]#M_8#B_0')

    ChrTalk(
        0x000B,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9064),
            '武的化境……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['安潔莉卡'], 0.000000, -15.000000, 0.000000, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['安潔莉卡'], '#E[3]#M_2#B_0')

    ChrTalk(
        0x0012,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9065),
            '這已經可以\n',
            '紀錄在帝國史上了……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)


    CameraCtrl(0x02, 0x03, -45.110001, 114.790001, -0.800000, 0)

    CameraCtrl(0x04, 0x03, 13.000000, 126.000000, 3.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 2.1, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)

    CameraCtrl(0x02, 0x03, -45.080002, 115.139999, -0.90000, 3000)

    CameraCtrl(0x04, 0x03, 6.000000, 119.000000, 4.000000, 15000, 0x01)
    OP_45(ChrTable['安潔莉卡'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0001)
    OP_45(ChrTable['安潔莉卡'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['安潔莉卡'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_16(0x07D0)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[3]#M_2#B_0')

    ChrTalk(
        0x006C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9066),
            '……老實說，我很驚訝。',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)

    # CameraCtrl(0x02, 0x03, -45.110001, 114.790001, -0.600000, 0)
    CameraCtrl(0x02, 0x03, -45.080002, 115.139999, -0.580000, 0)

    CameraCtrl(0x04, 0x03, 3.000000, 281.000000, 358.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 2.400000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -45.080002, 115.139999, -0.580000, 3000)
    CameraCtrl(0x04, 0x03, 4.000000, 288.000000, 358.000000, 15000, 0x01)
    CameraCtrl(0x05, 0x03, 2.100000, 15000)
    SetChrPos(ChrTable['尤西斯'], -34.419998, 114.000000, -2.130000, 272.899994)
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
    SetChrPos(ChrTable['神速杜巴莉'], -48.580002, 114.000000, -2.760000, 72.000000)
    SetChrPos(ChrTable['魔弓恩奈雅'], -48.119999, 114.000000, 0.760000, 98.000000)
    Fade(0xFF, 0, 0x0000)
    # SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv32030', -1.000000, 0.700000, 0x00000000)
    CameraCtrl(0x07, 0x0002)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_0#B_0')

    ChrTalk(
        0x006C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9067),
            '現在的妳\n',
            '已經比曾經的我更強了……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -44.869999, 115.459999, -0.970000, 0)
    CameraCtrl(0x04, 0x03, 8.000000, 61.000000, 3.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 0.900000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 5.000000)
    OP_7E(0x06, 0x0001)
    CameraCtrl(0x02, 0x03, -44.869999, 115.459999, -0.970000, 10000)
    CameraCtrl(0x04, 0x03, 2.000000, 66.000000, 3.000000, 10000, 0x01)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.250000, 114.000000, -0.970000, 90.400002)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], 'E', 'A[autoMA]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['鋼之雅里安洛德'], -20.000000, -8.000000, 0.000000, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[EEEEEEEEEEEE0]#M_A#B_0')

    ChrTalk(
        0x006C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9068),
            '呵呵，雖然很不甘心，\n',
            '但我不得不承認。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不過看樣子也達到極限了。\n',
            TxtCtl.Enter,
        ),
    )

    OP_16(0x0320)
    OP_45(ChrTable['鋼之雅里安洛德'], -5.000000, 0.000000, 0.000000, 0x05DC, 0x0000)
    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -37.070000, 114.790001, -2.790000, 0)
    CameraCtrl(0x04, 0x03, 8.000000, 308.000000, 3.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 0.900000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.000000)
    OP_7E(0x06, 0x0001)
    CameraCtrl(0x02, 0x03, -36.980000, 114.790001, -2.830000, 20000)
    CameraCtrl(0x04, 0x03, 3.000000, 300.000000, 1.000000, 20000, 0x01)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M[H]#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9069),
            '啊……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

    ChrTalk(
        0x0008,
        0x00000000,
        (
            (TxtCtl.Voice, 0x906A),
            '……所以還是……沒能超越聖女嗎？',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_A#B_0')

    ChrTalk(
        0x0010,
        0x00000000,
        (
            (TxtCtl.Voice, 0x906B),
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)

    CameraCtrl(0x02, 0x03, -40, 114.5, -0.5, 0)
    CameraCtrl(0x04, 0x03, 11.000000, 281.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 0.9, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -39.2, 114.5, -0.7, 20000)
    CameraCtrl(0x04, 0x03, 0.000000, 281.000000, 0.000000, 20000, 0x01)

    # SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvBtlWait', 1.000000, 0.800000, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    # SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_0#M_A#B_0')

    ChrTalk(
        0x0010,
        0x00000000,
        (
            (TxtCtl.Voice, 0x906C),
            '因為我的年紀\n',
            '比活著時的妳還要多一倍……',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.000000, -15.000000, 0.000000, 0x03E8, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '1', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_16(0x01F4)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_2#B_0')

    ChrTalk(
        0x0010,
        0x00000000,
        (
            (TxtCtl.Voice, 0x906D),
            '然而……我能到達的境界\n',
            '就到此為止了嗎。',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    # SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvFieldAttackEnd', -1.000000, 0.800000, 0x00000000)
    OP_16(0x05DC)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -43.689999, 115.199997, -0.720000, 0)
    CameraCtrl(0x04, 0x03, 354.000000, 67.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.000000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -44.369999, 115.300003, -0.820000, 15000)
    CameraCtrl(0x04, 0x03, 352.000000, 72.000000, 0.000000, 15000, 0x01)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0000)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.000000, -5.000000, 0.000000, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1111111110]#M_0#B_0')

    ChrTalk(
        0x006C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x906E),
            '是的──再往上，\n',
            '就是與《巨碩之存在》有關之人的領域了。',
            TxtCtl.Enter,
        ),
    )

    OP_16(0x0320)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.000000, 0.000000, 0.000000, 0x03E8, 0x0000)
    OP_26()

    ReturnToTitle()

    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -35.849998, 115.129997, -2.410000, 0)
    CameraCtrl(0x04, 0x03, 358.000000, 101.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 5.200000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x04, 0x03, 359.000000, 102.000000, 6.000000, 20000, 0x01)
    CameraCtrl(0x05, 0x03, 5.700000, 1500)
    SetChrPos(ChrTable['米莉亞姆'], -33.779999, 114.000000, -0.590000, 250.699997)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_44(0x0000, 0x15, 0.150000, 0x0000, 0.000000)
    OP_44(0x0006, 0x15, 0.150000, 0x0000, 0.000000)
    OP_44(0x0009, 0x15, 0.150000, 0x0000, 0.000000)
    OP_44(0x0008, 0x15, 0.150000, 0x0000, 0.000000)
    OP_44(0x000F, 0x15, 0.150000, 0x0000, 0.000000)
    OP_44(0x0010, 0x15, 0.150000, 0x0000, 0.000000)
    OP_16(0x03E8)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M_8#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x906F),
            '什麼……！？',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['莎拉'], '#E_2#M_2#B_0')

    ChrTalk(
        0x000F,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9070),
            '那個詞……！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_2#M_2#B_0')

    ChrTalk(
        0x0006,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9071),
            '在那個《夢幻迴廊》的盡頭\n',
            '所聽到的……！？',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    Fade(0x6A, 300)
    OP_11(0x0324)
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Call(0x15, 'Stop_ENVSE_VAR', (0xFF, 0x1F4, 0x0))
    OP_3A(0x03, 0.400000, 0x01F4, 0x00)
    OP_56(0x00, 0x03, 0x00, 1.000000, 1.000000, 1.000000, 1.000000, 300.000000)
    OP_57(0x00, 0x03)
    OP_16(0x05DC)
    OP_56(0x01, 0x03, 0x00, 1.000000, 1.000000, 1.000000, 1.000000, 300.000000)
    OP_57(0x01, 0x03)
    CameraCtrl(0x00)
    OP_16(0x05DC)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0001)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.000000, 0.000000, 0.000000, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], 0xFFFF, 0x0000)
    SetChrPos(ChrTable['黎恩'], -35.959999, 114.000000, -2.890000, 271.299988)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.250000, 114.000000, -0.970000, 104.500000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniDetachMainWeapon', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['黎恩'], 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    CameraCtrl(0x02, 0x03, -44.689999, 115.440002, -1.250000, 0)
    CameraCtrl(0x04, 0x03, 2.000000, 122.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.000000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -44.750000, 115.440002, -1.370000, 15000)
    CameraCtrl(0x04, 0x03, 351.000000, 106.000000, 0.000000, 15000, 0x01)
    Call(0x15, 'Init_ENVSE_VAR', (0xFF, 0x3E8, 0x0))
    OP_3A(0x03, 0.700000, 0x03E8, 0x00)
    OP_56(0x00, 0x03, 0x00, 1.000000, 1.000000, 1.000000, 0.000000, 0.000000)
    OP_56(0x01, 0x03, 0x00, 1.000000, 1.000000, 1.000000, 0.000000, 750.000000)
    OP_57(0x01, 0x03)
    OP_16(0x02EE)
    OP_3A(0x01, 0x0FA0, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        0x006C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9072),
            '《灰》之啟動者，\n',
            '黎恩・舒華澤。',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['鋼之雅里安洛德'], 30.000000, 0.000000, 0.000000, 0x05DC, 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '33332[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_16(0x01F4)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        0x006C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9073),
            '以及準啟動者們。\n',
            '──你們都做好覺悟了吧？',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -36.430000, 115.489998, -2.930000, 0)
    CameraCtrl(0x04, 0x03, 3.000000, 240.000000, 0.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.100000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -36.430000, 115.489998, -2.930000, 6000)
    CameraCtrl(0x04, 0x03, 0.000000, 243.000000, 0.000000, 6000, 0x01)
    CameraCtrl(0x05, 0x03, 1.000000, 6000)
    SetChrPos(ChrTable['永世α'], -60.450001, 114.000000, -1.940000, 90.000000)
    SetChrPos(ChrTable['安潔莉卡'], -37.230000, 114.000000, -13.000000, 356.399994)
    SetChrPos(ChrTable['悠娜'], -35.889999, 114.000000, -10.700000, 355.200012)
    SetChrPos(ChrTable['庫爾特'], -36.630001, 114.000000, -11.460000, 356.200012)
    SetChrPos(ChrTable['亞爾緹娜'], -35.209999, 114.000000, -11.190000, 354.799988)
    SetChrPos(ChrTable['亞修'], -34.509998, 114.000000, -12.480000, 346.399994)
    SetChrPos(ChrTable['妙婕'], -34.020000, 114.000000, -11.490000, 347.799988)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
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
    OP_35(0x01, ChrTable['黎恩'], 0x00000010)
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvSquat', -1.000000, 0.800000, 0x00000002)
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    OP_16(0x0320)
    CameraCtrl(0x0A, 0.020000, 0.020000, 0.000000, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_2#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9074),
            '#4S正合我意──！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    OP_3A(0x02, 0x00)
    OP_3A(0x00, 0x01CC, 0.700000, 0x0000, 0x00000000, 0x00)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -36.380001, 115.540001, -2.640000, 0)
    CameraCtrl(0x04, 0x03, 9.000000, 320.000000, 4.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.000000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -36.380001, 115.559998, -2.640000, 20000)
    CameraCtrl(0x04, 0x03, 8.000000, 349.000000, 4.000000, 20000, 0x01)
    SetChrFace(0x03, ChrTable['黎恩'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv00024', 1.000000, 1.000000, 0x00000000)
    SetChrPos(ChrTable['尤西斯'], -33.480000, 114.000000, -1.660000, 272.899994)
    SetChrPos(ChrTable['米莉亞姆'], -33.799999, 114.000000, -0.530000, 250.699997)
    SetChrPos(ChrTable['莎拉'], -35.320000, 114.000000, 0.350000, 265.299988)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -36.330002, 114.000000, -0.660000, 270.600006)
    OP_35(0x01, ChrTable['莎拉'], 0x00000010)
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x01, ChrTable['尤西斯'], 0x00000010)
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    OP_35(0x01, ChrTable['米莉亞姆'], 0x00000010)
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['黎恩'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[3]#M_2#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9075),
            '接下來才是重頭戲……！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['黎恩'], -50.000000, 0.000000, 0.000000, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '336[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_16(0x012C)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_2#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9076),
            '悠娜、庫爾特、亞爾緹娜、\n',
            '亞修和妙婕！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_45(ChrTable['黎恩'], 0.000000, -10.000000, 0.000000, 0x04B0, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '6667', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_16(0x01F4)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[7]#M_2#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9077),
            '以及尤西斯、米莉亞姆、\n',
            '蓋烏斯和莎拉教官！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -35.689999, 116.489998, -2.090000, 0)
    CameraCtrl(0x04, 0x03, 355.000000, 90.000000, 6.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 5.700000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.000000)
    OP_7E(0x06, 0x0001)
    CameraCtrl(0x02, 0x03, -34.330002, 115.599998, -2.130000, 8000)
    CameraCtrl(0x04, 0x03, 355.000000, 91.000000, 6.000000, 8000, 0x01)
    CameraCtrl(0x05, 0x03, 4.800000, 8000)
    SetChrPos(ChrTable['黎恩'], -35.950001, 114.000000, -2.560000, 271.299988)
    SetChrPos(ChrTable['蓋烏斯'], -33.869999, 114.000000, -3.950000, 274.500000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['黎恩'], 0x0000)
    OP_35(0x01, ChrTable['蓋烏斯'], 0x00000010)
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniWait', 0.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvWait', 0.000000, 1.000000, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['黎恩'], 0.000000, 0.000000, 0.000000, 0x0320, 0x0000)
    OP_16(0x01F4)
    SetChrFace(0x04, ChrTable['黎恩'], '#E_6#M_2#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x9078),
            '#4S請你們──助我一臂之力！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvRyoteGyu', -1.000000, 1.000000, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvGyu', -1.000000, 1.000000, 0x00000000)
    OP_1E(0x000F, 0x02, 0x0A, 'FC_look_dir_Yes')
    OP_1E(0x0008, 0x02, 0x0A, 'FC_look_dir_Yes')
    OP_16(0x01F4)
    CameraCtrl(0x0A, 0.020000, 0.020000, 0.000000, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0004, 0.500000, 0x012C, 0x0320, 0x01F4, 0.500000, 0xFFFF, -9000.000000, -9000.000000, -9000.000000)
    OP_1E(0xFFFF, 0x02, 0x15, 'VOICE_YES_03_81_01')
    OP_27('新舊Ⅶ班', 0xFFFF)
    SetChrFace(0x04, ChrTable['悠娜'], '#E_0#M_0#B_0')

    ChrTalk(
        0x000A,
        0x00000000,
        (
            (TxtCtl.Voice, 0x2B60),
            '#6S喔！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    OP_11(0x0324)
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 800, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -55.470001, 119.190002, -3.170000, 0)
    CameraCtrl(0x04, 0x03, 6.000000, 128.000000, 3.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 9.400000, 0)
    CameraCtrl(0x0B, 0x03, 34.599998, 0x0000)
    CameraCtrl(0x02, 0x03, -51.950001, 117.169998, 1.360000, 6000)
    CameraCtrl(0x04, 0x03, 348.000000, 56.000000, 352.000000, 6000, 0x01)
    CameraCtrl(0x05, 0x03, 11.200000, 6000)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x763C, 0x0), 1.000000, (0xFF, 0x0, 0x0), 0.000000, 0.000000, 0x0000, 0xFFFF, 0.000000, 0.000000, 0.000000, 0.000000, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0C, 0xFFFF, (0xFF, 0xCC, 0x0), 0x0339, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.000000, 0.000000, 0.000000, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_16(0x0320)
    OP_3B(0x00, (0xFF, 0x7737, 0x0), 0.700000, (0xFF, 0x3E8, 0x0), 0.000000, 0.000000, 0x0000, 0xFFFF, 0.000000, 0.000000, 0.000000, 0.000000, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7593, 0x0), 0.500000, (0xFF, 0x3E8, 0x0), 0.000000, 0.000000, 0x0000, 0xFFFF, 0.000000, 0.000000, 0.000000, 0.000000, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0C, 0x0339, (0xFF, 0xCB, 0x0), 0x0339, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.000000, 0.000000, 0.000000, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    CameraCtrl(0x07, 0x00BF)
    OP_16(0x01F4)
    OP_3B(0x01, (0xFF, 0x7737, 0x0), (0xFF, 0xFA0, 0x0))
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -35.750000, 115.389999, -2.780000, 0)
    CameraCtrl(0x04, 0x03, 3.000000, 312.000000, 13.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.700000, 0)
    CameraCtrl(0x0B, 0x03, 34.000000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[7777777777776]#M_2#B_0')

    ChrTalk(
        0x0000,
        0x00000000,
        (
            (TxtCtl.Voice, 0x2B0A),
            '#5S來吧─#20W─\n',
            '#1000W《灰之騎神》瓦利瑪！！',
            TxtCtl.Enter,
        ),
    )

    OP_16(0x05DC)
    CameraCtrl(0x09, 0.050000, 0.050000, 0.200000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv00025', 1.000000, 1.000000, 0x00000000)
    CameraCtrl(0x02, 0x03, -35.980000, 115.650002, -2.700000, 1200)
    CameraCtrl(0x04, 0x03, 28.000000, 270.000000, 350.000000, 1200, 0x01)
    CameraCtrl(0x05, 0x03, 1.500000, 1200)
    CameraCtrl(0x0B, 0x03, 34.000000, 0x04B0)
    OP_26()
    OP_63(0xFFFF, 0x01)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -35.810001, 115.339996, -10.210000, 0)
    CameraCtrl(0x04, 0x03, 9.000000, 19.000000, 6.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.600000, 0)
    CameraCtrl(0x0B, 0x03, 34.000000, 0x0000)
    CameraCtrl(0x02, 0x03, -35.799999, 115.279999, -10.430000, 15000)
    CameraCtrl(0x04, 0x03, 359.000000, 28.000000, 6.000000, 15000, 0x01)
    SetChrPos(ChrTable['悠娜'], -35.889999, 114.000000, -10.700000, 355.200012)
    SetChrPos(ChrTable['庫爾特'], -36.660000, 114.000000, -11.300000, 26.799999)
    SetChrPos(ChrTable['亞爾緹娜'], -35.389999, 114.000000, -11.210000, 354.799988)
    SetChrPos(ChrTable['亞修'], -34.820000, 114.000000, -12.280000, 30.299999)
    SetChrPos(ChrTable['妙婕'], -33.669998, 114.000000, -11.630000, 295.700012)
    SetChrFace(0x03, ChrTable['悠娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['悠娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞修'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['黎恩'], 0x0000)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvPhoneTalk', -1.000000, 1.000000, 0x00000001)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvPhoneLook', -1.000000, 1.000000, 0x00000001)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvPhoneTalk', -1.000000, 1.200000, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_16(0x0708)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[3322222222222222222332]#M_2#B[777777777777777777770]')

    ChrTalk(
        0x000A,
        0x00000000,
        (
            (TxtCtl.Voice, 0x907B),
            '緹妲，拜託妳！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['庫爾特'], '#E_6#M_2#B_0')

    ChrTalk(
        0x000B,
        0x00000000,
        (
            (TxtCtl.Voice, 0x907C),
            '勇士和鷹隼就拜託了！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E_6#M_2#B_0')

    ChrTalk(
        0x000C,
        0x00000000,
        (
            (TxtCtl.Voice, 0x907D),
            '現在地點，以信標修正！',
            TxtCtl.Enter,
        ),
    )

    OP_26()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    OP_11(0x0324)
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.000000, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraCtrl(0x02, 0x03, -34.560001, 115.330002, -11.900000, 0)
    CameraCtrl(0x04, 0x03, 7.000000, 247.000000, 5.000000, 0, 0x01)
    CameraCtrl(0x05, 0x03, 1.700000, 0)
    CameraCtrl(0x0B, 0x03, 34.000000, 0x0000)
    CameraCtrl(0x02, 0x03, -34.560001, 115.400002, -11.900000, 6000)
    CameraCtrl(0x04, 0x03, 10.000000, 253.000000, 5.000000, 6000, 0x01)
    Fade(0xFF, 0, 0x0000)
    OP_16(0x01F4)
    OP_46(0x00, ChrTable['亞修'], ChrTable['妙婕'], 0x03E8)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['亞修'], 0x03E8)
    OP_16(0x05DC)
    OP_45(ChrTable['亞修'], 0.000000, -20.000000, 0.000000, 0x01F4, 0x0000)
    OP_45(ChrTable['妙婕'], 0.000000, -20.000000, 0.000000, 0x01F4, 0x0000)
    SetChrFace(0x03, ChrTable['亞修'], '33333332', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '33333332', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_16(0x01F4)
    OP_45(ChrTable['亞修'], 0.000000, 0.000000, 0.000000, 0x01F4, 0x0000)
    OP_45(ChrTable['妙婕'], 0.000000, 0.000000, 0.000000, 0x01F4, 0x0000)
    OP_16(0x03E8)
    Call(0x15, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.000000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_AC(0x06)

    Return()
