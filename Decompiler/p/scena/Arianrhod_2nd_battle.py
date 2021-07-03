
from ScenarioHelper import *

def Arianrhod_LastBattle(caller_locals):

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00156.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00256.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00356.itc", 0x25)

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "not_load_noel_chip")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("not_load_noel_chip")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "not_load_lazy_chip")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("not_load_lazy_chip")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "not_load_rixia_chip")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("not_load_rixia_chip")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "not_load_noel_chip_2")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("not_load_noel_chip_2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "not_load_lazy_chip_2")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("not_load_lazy_chip_2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "not_load_rixia_chip_2")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("not_load_rixia_chip_2")

    LoadChrToIndex("chr/ch04250.itc", 0x2B)
    LoadChrToIndex("chr/ch04253.itc", 0x2E)
    LoadChrToIndex("chr/ch04254.itc", 0x2F)
    LoadChrToIndex("chr/ch00001.itc", 0x30)
    LoadChrToIndex("chr/ch00301.itc", 0x31)
    LoadChrToIndex("chr/ch02901.itc", 0x32)
    LoadChrToIndex("chr/ch03201.itc", 0x33)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    LoadEffect(0x2, "map/mpbell.eff")
    SoundLoad(832)
    SoundLoad(825)
    SoundLoad(132)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13700.itp")
    SoundLoad(3906)
    SoundLoad(3907)
    SoundLoad(3908)
    OP_A3(0x4, 0x80)
    OP_A5(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    OP_A5(0x5, 0x8000)
    SetChrPos(0x101, -14110, 0, 580, 90)
    SetChrPos(0x102, -14470, 0, -650, 90)
    SetChrPos(0x103, -14880, 0, 1630, 90)
    SetChrPos(0x104, -14680, 0, -2040, 90)
    SetChrPos(0xF4, -16079, 0, 1140, 90)
    SetChrPos(0xF5, -15780, 0, -1400, 90)


    #Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F92")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)


    OP_A3(0x8, 0x80)
    OP_A2(0x8, 0x8000)
    SetChrPos(0x8, -5900, 1140, 0, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-5900, 2140, 0, 0)
    OP_68(-12700, 2420, 0, 5000)
    OP_6D(0x5A, 0x9, 0x0, 0x0)
    OP_6E(0x226, 0x0)
    OP_6C(0x3F15, 0x0)
    OP_6C(0x46E6, 0x1388)
    BeginChrThread(0xD, 1, 0, 11)
    PlayBGM("ed7584.ogg", 0)

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "xxx_first_battle_lose")

    # win

    OP_2C(0xB0, 0x5)
    OP_29(0xB0, 0x1, 0x7)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        "#13703F#40W………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F#40W#6P#N呼……呼……\x01",
            "怎……怎么样……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#40W#12P#N这、这就是\x01",
            "我们的全部实力……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#13704F#30W……真令人吃惊。\x02\x03",
            "#13702F#30W虽然你们有六个人，\x01\x02",
            "#13702F但能跟我战斗到这个地步，\x01\x02",
            "已经很了不起了。\x02\x03",
            "#13700F那么，我就稍微认真一点好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()


    ChrTalk(
        0x101,
        "#00010F#6P#N……什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()


    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "team_has_not_lazy")

    ChrTalk(
        0x105,
        "#10410F#6P#N#40W还要打吗……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("check_lazy_end")


    label("team_has_not_lazy")

    ChrTalk(
        0x106,
        "#10707F#6P#N#40W她还想打吗……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("check_lazy_end")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "team_has_not_noel")

    ChrTalk(
        0x109,
        (
            "#10107F#6P#N#40W但、但是……\x01",
            "我已经……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("check_noel_end")

    label("team_has_not_noel")

    ChrTalk(
        0x106,
        (
            "#10707F#6P#N#40W但是……\x01",
            "我已经……！\x02",
        )
    )


    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("check_noel_end")


    #FadeToDark(0, -1, 0)
    #FadeToDark(650, 16777215, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xF4, 0x1)
    EndChrThread(0xF5, 0x1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x8, 0x0)

    OP_C5(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ShowSaveMenu()

    Battle("BattleInfo_Last", 0x0, 0x0, 0x100, 0x40, 0xFF)
    FadeToDark(0, 0, -1)

    IfScenaFlagOff(SCENA_FLAGS_OFFSET_1, SCENA_FLAGS_BIT_ARIANRHOD, 'arianrhod_already_beat')

    IfLastBattleLostGoto('last_battle_lost')
    SetScenarioFlags(SCENA_FLAGS_OFFSET_1, SCENA_FLAGS_BIT_ARIANRHOD)

    AnonymousTalk(
        999,
        (
            scpstr(7, 5),
            "现在可以使用真正的第七柱了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label('arianrhod_already_beat')
    label('last_battle_lost')

    OP_CC(0x1, 0xFF, 0x0)
    Call(0, GetFuntionId('Function_12_1D3D'))

    Return()


    ##########################################################

    label("xxx_first_battle_lose")
    Jump('first_battle_lose')


