from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e3020.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x00D0,                     # 梅尔卡瓦
        "ed70570",
        0x00002000,                 # Flags
        ("e3020", "e3020_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e3020",                  # 0
        "正骑士阿巴斯",           # 1
        "约纳",                   # 2
        "瓦吉",                   # 3
        "缇欧",                   # 4
        "芙兰",                   # 5
        "莉夏",                   # 6
        "兰迪",                   # 7
        "格蕾丝",                 # 8
        "诺艾尔",                 # 9
        "艾莉",                   # 10
        "麦克道尔议长",           # 11
        "神狼蔡特",               # 12
        "达德利搜查官",           # 13
        "随从骑士维恩图斯",       # 14
        "随从骑士朱诺",           # 15
        "随从骑士塞萨尔",         # 16
        "随从骑士玛卡斯",         # 17
        "莉丝修女",               # 18
        "凯文神父",               # 19
        "诺艾尔",                 # 20
        "芙兰",                   # 21
        "格蕾丝",                 # 22
        " ",                      # 23
        "SE控制",                 # 24
    ))

    AddCharChip((
        "chr/ch06712.itc",                   # 00
        "chr/ch06100.itc",                   # 01
        "chr/ch03100.itc",                   # 02
        "chr/ch03102.itc",                   # 03
        "chr/ch00202.itc",                   # 04
        "chr/ch06902.itc",                   # 05
        "chr/ch03200.itc",                   # 06
        "chr/ch00300.itc",                   # 07
        "chr/ch06000.itc",                   # 08
        "chr/ch02900.itc",                   # 09
        "chr/ch00102.itc",                   # 0A
        "chr/ch05800.itc",                   # 0B
        "chr/ch02710.itc",                   # 0C
        "chr/ch00900.itc",                   # 0D
        "chr/ch48400.itc",                   # 0E
        "chr/ch48402.itc",                   # 0F
        "chr/ch02702.itc",                   # 10
        "chr/ch02708.itc",                   # 11
        "chr/ch00200.itc",                   # 12
        "chr/ch00302.itc",                   # 13
        "chr/ch02902.itc",                   # 14
        "chr/ch03202.itc",                   # 15
        "chr/ch00902.itc",                   # 16
        "chr/ch06102.itc",                   # 17
        "chr/ch06002.itc",                   # 18
        "chr/ch05802.itc",                   # 19
        "chr/ch06710.itc",                   # 1A
        "chr/ch06900.itc",                   # 1B
    ))

    DeclNpc(-39,     490,     2500,    0,    261,  0x0, 0,   0,   0,   255, 255, 1,   26,  255,  0)
    DeclNpc(-3119,   -1350,   7039,    315,  389,  0x0, 0,   1,   0,   255, 255, 1,   34,  255,  0)
    DeclNpc(101790,  150,     -93959,  90,   389,  0x0, 0,   2,   0,   0,   0,   1,   15,  255,  0)
    DeclNpc(-3119,   -1350,   7039,    315,  389,  0x0, 0,   18,  0,   0,   0,   1,   2,   255,  0)
    DeclNpc(3000,    -1350,   6960,    45,   389,  0x0, 0,   5,   0,   255, 255, 1,   31,  255,  0)
    DeclNpc(-1500,   0,       -1500,   0,    389,  0x0, 0,   6,   0,   0,   0,   1,   19,  255,  0)
    DeclNpc(98970,   170,     -970,    0,    389,  0x0, 0,   7,   0,   0,   0,   1,   6,   255,  0)
    DeclNpc(-3000,   -1490,   6000,    0,    389,  0x0, 0,   8,   0,   255, 255, 1,   37,  255,  0)
    DeclNpc(100309,  170,     959,     270,  389,  0x0, 0,   9,   0,   0,   0,   1,   12,  255,  0)
    DeclNpc(100169,  100,     -102720, 270,  389,  0x0, 0,   10,  0,   0,   0,   1,   0,   255,  0)
    DeclNpc(98440,   100,     -101110, 180,  389,  0x0, 0,   11,  0,   255, 255, 1,   39,  255,  0)
    DeclNpc(97610,   0,       -97069,  180,  405,  0x0, 0,   12,  0,   255, 255, 1,   22,  255,  0)
    DeclNpc(97639,   170,     959,     90,   389,  0x0, 0,   13,  0,   255, 255, 1,   24,  255,  0)
    DeclNpc(103569,  0,       -97089,  270,  257,  0x0, 0,   14,  0,   0,   0,   1,   43,  255,  0)
    DeclNpc(103949,  0,       -209,    270,  257,  0x0, 0,   14,  0,   0,   0,   1,   46,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   9,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(102510,  0,       -97020,  1000,    103570,  1500,    -97090,  0x007E, 1,  42, 0x0000)
    DeclActor(102710,  0,       -200,    400,     103950,  1500,    -210,    0x007E, 1,  45, 0x0000)
    DeclActor(2350,    0,       -92230,  800,     2350,    1500,    -92230,  0x007C, 0,  46, 0x0000)
    DeclActor(103750,  0,       -105640, 2000,    103750,  1500,    -105640, 0x007C, 1,  49, 0x0000)

    ChipFrameInfo(1260, 0)                                       # 0

    ScpFunction((
        "Function_0_4EC",          # 00, 0
        "Function_1_59C",          # 01, 1
        "Function_2_116A",         # 02, 2
        "Function_3_12CA",         # 03, 3
        "Function_4_12EA",         # 04, 4
        "Function_5_13FF",         # 05, 5
        "Function_6_14BC",         # 06, 6
        "Function_7_1573",         # 07, 7
        "Function_8_1A5F",         # 08, 8
        "Function_9_22D4",         # 09, 9
        "Function_10_3440",        # 0A, 10
        "Function_11_3482",        # 0B, 11
        "Function_12_395B",        # 0C, 12
        "Function_13_3A18",        # 0D, 13
        "Function_14_4040",        # 0E, 14
        "Function_15_405B",        # 0F, 15
        "Function_16_4C2D",        # 10, 16
        "Function_17_564F",        # 11, 17
        "Function_18_5B1D",        # 12, 18
        "Function_19_5B42",        # 13, 19
        "Function_20_5C42",        # 14, 20
        "Function_21_69A9",        # 15, 21
        "Function_22_6BF8",        # 16, 22
        "Function_23_7D9E",        # 17, 23
        "Function_24_80C3",        # 18, 24
        "Function_25_8487",        # 19, 25
        "Function_26_849D",        # 1A, 26
        "Function_27_84B6",        # 1B, 27
        "Function_28_8AD9",        # 1C, 28
        "Function_29_8AF9",        # 1D, 29
        "Function_30_9A8E",        # 1E, 30
        "Function_31_9EF7",        # 1F, 31
        "Function_32_A763",        # 20, 32
        "Function_33_A792",        # 21, 33
        "Function_34_A7B5",        # 22, 34
        "Function_35_A7DA",        # 23, 35
        "Function_36_A7F2",        # 24, 36
        "Function_37_A815",        # 25, 37
        "Function_38_A82F",        # 26, 38
        "Function_39_B304",        # 27, 39
        "Function_40_B53A",        # 28, 40
        "Function_41_BA02",        # 29, 41
        "Function_42_BA27",        # 2A, 42
        "Function_43_BF60",        # 2B, 43
        "Function_44_BF80",        # 2C, 44
        "Function_45_C3CF",        # 2D, 45
        "door_show_cg_menu",        # 2D, 45
    ))

    label('door_show_cg_menu')

    import TiosBed

    PartySelect(2)
    TiosBed.ShowMenu()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)

    Return()


    def Function_0_4EC(): pass

    label("Function_0_4EC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_524"),
        (1, "loc_530"),
        (2, "loc_53C"),
        (3, "loc_548"),
        (4, "loc_554"),
        (5, "loc_560"),
        (6, "loc_56C"),
        (SWITCH_DEFAULT, "loc_578"),
    )


    label("loc_524")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_530")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_53C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_548")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_554")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_560")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_56C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_578")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_584")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_584")

    label("loc_59B")

    Return()

    # Function_0_4EC end

    def Function_1_59C(): pass

    label("Function_1_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_6F5")
    OP_A3(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5")
    OP_A3(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 104200, 100, 5070, 90)
    Jump("loc_61E")

    label("loc_5F5")

    OP_A3(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_61E")

    OP_A3(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    OP_A3(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0x10, 100250, 100, -104800, 270)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_A3(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    OP_A3(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_6F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_84E")
    OP_A3(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    OP_A3(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 104200, 100, 5070, 90)
    Jump("loc_777")

    label("loc_74E")

    OP_A3(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)

    label("loc_777")

    OP_A3(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    OP_A3(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrPos(0x10, 100250, 100, -104800, 270)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_A3(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    OP_A3(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_84E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_963")
    OP_A3(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    OP_A3(0xB, 0x80)
    SetChrPos(0xB, -2110, -1490, 6190, 315)
    OP_A3(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    OP_A3(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_A3(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    OP_A3(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x16)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jump("loc_F57")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A8D")
    OP_A3(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xA)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    OP_A3(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 97620, 170, 970, 90)
    OP_A3(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    OP_A3(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    OP_A3(0xF, 0x80)
    SetChrPos(0xF, -3050, 0, -2960, 0)
    BeginChrThread(0xF, 0, 0, 0)
    OP_A3(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A88")
    OP_A2(0x12, 0x10)

    label("loc_A88")

    Jump("loc_F57")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_BCF")
    OP_A3(0xB, 0x80)
    SetChrPos(0xB, 97740, 0, -98460, 0)
    OP_A3(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    OP_A3(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x14)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    OP_A3(0xA, 0x80)
    SetChrPos(0xA, 1340, 0, -1280, 270)
    OP_A3(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 97640, 170, 960, 90)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrPos(0x8, 140, 0, -1320, 89)
    BeginChrThread(0x8, 0, 0, 0)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    OP_A2(0xC, 0x10)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    OP_A3(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, 100170, 100, -102720, 270)
    OP_A3(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC5")
    OP_A2(0xB, 0x10)

    label("loc_BC5")

    OP_A2(0x13, 0x10)
    Jump("loc_F57")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_CD8")
    OP_A3(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    OP_A3(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x13)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xE, 100170, 100, -102720, 270)
    OP_A2(0xE, 0x10)
    OP_A3(0x10, 0x80)
    SetChrPos(0x10, 3750, 0, -2770, 270)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_A3(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    OP_A2(0xD, 0x10)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 2620, 0, -2780, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD3")
    OP_A2(0x10, 0x10)
    OP_A2(0xC, 0x10)

    label("loc_CD3")

    Jump("loc_F57")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_DC1")
    OP_A3(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    OP_A3(0xE, 0x80)
    SetChrPos(0xE, 100560, 0, 2190, 270)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 100170, 100, -102720, 270)
    OP_A3(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x15)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 96830, 100, -102670, 90)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    OP_A3(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xF, 98440, 100, -101110, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_END)), "loc_DBC")
    OP_A2(0xF, 0x10)

    label("loc_DBC")

    Jump("loc_F57")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E4E")
    OP_A3(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDE")
    OP_A2(0xB, 0x10)

    label("loc_DDE")

    SetChrPos(0xB, 97740, 0, -98460, 0)
    OP_A3(0xA, 0x80)
    SetChrPos(0xA, 1410, 0, -100570, 270)
    OP_A3(0x13, 0x80)
    OP_A2(0x13, 0x10)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jump("loc_F57")

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_EEC")
    OP_A3(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    BeginChrThread(0x13, 0, 0, 0)
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrPos(0x8, -2110, -1490, 6190, 315)
    BeginChrThread(0x8, 0, 0, 0)
    OP_A3(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE7")
    OP_A2(0x8, 0x10)
    OP_A2(0xB, 0x10)

    label("loc_EE7")

    Jump("loc_F57")

    label("loc_EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F57")
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F41")
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    Jump("loc_F57")

    label("loc_F41")

    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F93")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAA")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_FD8")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 4)
    Jump("loc_1169")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_FEC")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)
    Jump("loc_1169")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1003")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 9)
    Jump("loc_1169")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1017")
    ClearScenarioFlags(0x22, 3)
    Event(0, 13)
    Jump("loc_1169")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_102B")
    ClearScenarioFlags(0x22, 4)
    Event(0, 15)
    Jump("loc_1169")

    label("loc_102B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_103F")
    ClearScenarioFlags(0x22, 5)
    Event(0, 16)
    Jump("loc_1169")

    label("loc_103F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1059")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 17)
    Jump("loc_1169")

    label("loc_1059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_106D")
    ClearScenarioFlags(0x22, 7)
    Event(0, 20)
    Jump("loc_1169")

    label("loc_106D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_1081")
    ClearScenarioFlags(0x23, 0)
    Event(0, 22)
    Jump("loc_1169")

    label("loc_1081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_1095")
    ClearScenarioFlags(0x23, 1)
    Event(0, 24)
    Jump("loc_1169")

    label("loc_1095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_10A9")
    ClearScenarioFlags(0x23, 2)
    Event(0, 27)
    Jump("loc_1169")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_10C0")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 29)
    Jump("loc_1169")

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_10D4")
    ClearScenarioFlags(0x23, 4)
    Event(0, 30)
    Jump("loc_1169")

    label("loc_10D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_10E8")
    ClearScenarioFlags(0x23, 5)
    Event(0, 31)
    Jump("loc_1169")

    label("loc_10E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_10FC")
    ClearScenarioFlags(0x23, 6)
    Event(0, 38)
    Jump("loc_1169")

    label("loc_10FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_1110")
    ClearScenarioFlags(0x23, 7)
    Event(0, 40)
    Jump("loc_1169")

    label("loc_1110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_1124")
    ClearScenarioFlags(0x24, 0)
    Event(0, 42)
    Jump("loc_1169")

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_1138")
    ClearScenarioFlags(0x24, 1)
    Event(0, 44)
    Jump("loc_1169")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_114C")
    ClearScenarioFlags(0x24, 2)
    Event(0, 3)
    Jump("loc_1169")

    label("loc_114C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_1169")
    ClearScenarioFlags(0x24, 3)
    SetChrPos(0x0, 102230, 0, -105070, 90)

    label("loc_1169")

    Return()

    # Function_1_59C end

    def Function_2_116A(): pass

    label("Function_2_116A")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1187")
    OP_24(0x1F2)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_11A6")

    label("loc_1187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    Sound(498, 1, 50, 0)
    Jump("loc_11A6")

    label("loc_11A0")

    Sound(498, 1, 100, 0)

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_11D7")

    label("loc_11C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11D7")

    OP_72(0x1, 0x4)
    OP_73(0x6, 0x4)
    OP_72(0x7, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1203")
    OP_72(0x6, 0x4)
    OP_73(0x7, 0x4)

    label("loc_1203")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1214")
    OP_66(0x3, 0x1)

    label("loc_1214")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF4080FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1236")
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x1)
    Jump("loc_123C")

    label("loc_1236")

    OP_10(0x7, 0x0)
    OP_10(0x0, 0x1)

    label("loc_123C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_126A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1261")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_126A")

    label("loc_1261")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_126A")

    OP_73(0x3, 0x10)
    SetMapFlags(0x10000)
    SetScenarioFlags(0x26, 0)
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_END)), "loc_128A")
    SetScenarioFlags(0x26, 2)

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1296")
    SetScenarioFlags(0x26, 1)

    label("loc_1296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_12A2")
    SetScenarioFlags(0x26, 3)

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12B1")
    SetScenarioFlags(0x27, 0)
    ClearScenarioFlags(0x26, 6)

    label("loc_12B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_12BD")
    SetScenarioFlags(0x26, 5)

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12C9")
    SetScenarioFlags(0x27, 1)

    label("loc_12C9")

    Return()

    # Function_2_116A end

    def Function_3_12CA(): pass

    label("Function_3_12CA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_3_12CA end

    def Function_4_12EA(): pass

    label("Function_4_12EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SoundLoad(132)
    SoundLoad(497)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1311")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_1311")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0x1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetEventSkip(0x0, "loc_13C4")
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, -30000, 990000, 0)

    def lambda_1352():
        OP_96(0x1E, 0xFFF0BDC0, 0xFFFEA070, 0xF4A10, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1352)
    OP_F0(0x1, 0x7D0)
    OP_68(-1005000, -50000, 1005000, 0)
    OP_6D(0x91, 0xFFDD, 0x0, 0x0)
    OP_6D(0x8C, 0xFFE2, 0x0, 0x9C4)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x88B8, 0x0)
    Sleep(2000)
    StopSound(132, 1000, 80)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_13C4")

    EndChrThread(0x1E, 0x1)
    SetChrPos(0x0, 0, 0, -2940, 0)
    OP_31(0x1)
    Sleep(0)
    OP_6F(0xFF)
    OP_69(0xFF, 0x0)
    Sound(498, 1, 100, 0)
    Sleep(1500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x6)
    OP_A2(0x8, 0x8000)
    Return()

    # Function_4_12EA end

    def Function_5_13FF(): pass

    label("Function_5_13FF")

    SoundLoad(132)
    SoundLoad(497)
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_14BB")
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1050000, 120000, 920000, 0)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)

    def lambda_144E():
        OP_96(0x1E, 0xFFEFFA70, 0xEA60, 0xE7EF0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_144E)
    OP_F0(0x1, 0x7D0)
    OP_68(-976190, -500, 1037099, 0)
    OP_6D(0x23, 0x27, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x3836A, 0x0)
    Sleep(2000)
    StopSound(132, 1000, 80)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21(0x7D0)
    WaitBGM()
    SetEventSkip(0x1, 0x0)

    label("loc_14BB")

    Return()

    # Function_5_13FF end

    def Function_6_14BC(): pass

    label("Function_6_14BC")

    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_1572")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_14F9():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14F9)
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 0, 800000, 0)
    OP_6D(0x1E, 0xFFF9, 0x0, 0x0)
    OP_6D(0x14, 0xFFF9, 0x0, 0xBB8)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x1B198, 0x0)
    Sleep(300)
    Sound(499, 0, 100, 0)
    Sleep(1700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    OP_21(0x7D0)
    WaitBGM()
    SetEventSkip(0x1, 0x0)

    label("loc_1572")

    Return()

    # Function_6_14BC end

    def Function_7_1573(): pass

    label("Function_7_1573")

    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B3")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_16A3")

    label("loc_15B3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D6")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_16A3")

    label("loc_15D6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F9")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_16A3")

    label("loc_15F9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_16A3")

    label("loc_161C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163F")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_16A3")

    label("loc_163F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1662")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_16A3")

    label("loc_1662")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1685")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_16A3")

    label("loc_1685")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A3")
    SetScenarioFlags(0x3C, 7)

    label("loc_16A3")

    PartySelect(0x2)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_END)),
        (0, "loc_175C"),
        (1, "loc_1775"),
        (3, "loc_178E"),
        (5, "loc_17A7"),
        (7, "loc_17C0"),
        (9, "loc_17D9"),
        (51, "loc_17F2"),
        (17, "loc_180B"),
        (19, "loc_1824"),
        (21, "loc_183D"),
        (23, "loc_1856"),
        (24, "loc_186F"),
        (25, "loc_1888"),
        (26, "loc_18A1"),
        (27, "loc_18BA"),
        (28, "loc_18D3"),
        (29, "loc_18EC"),
        (33, "loc_1905"),
        (35, "loc_191E"),
        (37, "loc_1937"),
        (41, "loc_1950"),
        (43, "loc_1969"),
        (46, "loc_1982"),
        (52, "loc_199B"),
        (47, "loc_19B4"),
        (48, "loc_19D6"),
        (50, "loc_19F8"),
        (49, "loc_1A1A"),
        (42, "loc_1A3C"),
        (SWITCH_DEFAULT, "loc_1A5E"),
    )


    label("loc_175C")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1775")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_178E")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17A7")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17C0")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17D9")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_17F2")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1610", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_180B")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1824")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2030", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_183D")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2050", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1856")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r3000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_186F")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1888")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18A1")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1310", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18BA")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t2500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18D3")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t2000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_18EC")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1905")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m1000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_191E")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r2070", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1937")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t6000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1950")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1969")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1982")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m4250", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_199B")

    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19B4")

    OP_21(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19D6")

    OP_21(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t0000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_19F8")

    OP_21(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("r1610", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A1A")

    OP_21(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("t1500", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A3C")

    OP_21(0x7D0)
    WaitBGM()
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1D4, 6)
    EventEnd(0x6)
    NewScene("m9000", 99, 0, 0)
    IdleLoop()
    Jump("loc_1A5E")

    label("loc_1A5E")

    Return()

    # Function_7_1573 end

    def Function_8_1A5F(): pass

    label("Function_8_1A5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17002.eff")
    SoundLoad(493)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    OP_73(0x1, 0x4)
    OP_32(0x4, 0x0, 0x52)
    OP_32(0x4, 0x5, 0x64)
    OP_42(0x4, 0x441, 0xFF)
    OP_42(0x4, 0x5ED, 0xFF)
    OP_42(0x4, 0x651, 0xFF)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x2)
    OP_38(0x4, 0x83, 0x2)
    OP_38(0x4, 0x84, 0x2)
    OP_38(0x4, 0x85, 0x2)
    OP_38(0x4, 0x86, 0x1)
    OP_42(0x4, 0xA1, 0x2)
    OP_42(0x4, 0x94, 0x3)
    OP_42(0x4, 0xB8, 0x4)
    OP_42(0x4, 0x89, 0x5)
    AddCraft(0x4, 0xC1)
    AddCraft(0x4, 0xC3)
    OP_32(0x6, 0x0, 0x55)
    OP_32(0x6, 0x5, 0x64)
    OP_38(0x6, 0x81, 0x2)
    OP_38(0x6, 0x82, 0x2)
    OP_38(0x6, 0x83, 0x2)
    OP_38(0x6, 0x84, 0x2)
    OP_38(0x6, 0x85, 0x2)
    OP_38(0x6, 0x86, 0x2)
    OP_42(0x6, 0x474, 0xFF)
    OP_42(0x6, 0x477, 0xFF)
    OP_42(0x6, 0x478, 0xFF)
    OP_42(0x6, 0x3A, 0x3)
    OP_42(0x6, 0x27, 0x4)
    SetChrChipPat(0x4, 0x1, 0x1F)
    LoadChrChipPat()
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    RemoveCraft(0x6, 0x53)
    RemoveCraft(0x6, 0x61)
    RemoveCraft(0x6, 0x69)
    RemoveCraft(0x6, 0x72)
    RemoveCraft(0x6, 0x79)
    RemoveCraft(0x6, 0x7C)
    RemoveCraft(0x6, 0x85)
    RemoveCraft(0x6, 0x87)
    RemoveCraft(0x6, 0x34)
    RemoveCraft(0x6, 0x3E)
    RemoveCraft(0x6, 0x48)
    OP_A2(0x8, 0x8000)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrChipByIndex(0x15, 0xF)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    OP_A3(0x15, 0x80)
    OP_A2(0x15, 0x8000)
    OP_72(0x1, 0x1000)
    OP_74(0x1, 0x14)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    SetChrPos(0x15, -3100, -1350, 7100, 315)
    OP_68(-280, 1800, -1040, 0)
    OP_6D(0x2C, 0x1A, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5DC0, 0x0)
    FadeToBright(1000, 0)
    OP_68(1170, 1800, 3900, 3000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-1360, 3800, 2000, 0)
    OP_68(-1360, 1800, 2720, 4000)
    OP_6D(0x2C, 0x12, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x459C, 0x0)
    Sleep(1000)
    Sound(943, 2, 70, 0)
    OP_71(0x1, 0x1, 0x1E, 0x0, 0x8)
    OP_79(0x1)
    Sound(143, 0, 50, 0)
    OP_24(0x3AF)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    OP_70(0x1, 0x1F)
    Sound(72, 0, 100, 0)
    Sleep(300)
    OP_5B(0x55, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "好，按照原定计划行事，\x01",
            "『智能兵器』就由我们来对付。\x02\x03",
            "至于你们，可千万要小心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x105,
        (
            "#10404F#6P呵呵，你才更要小心呢，\x01",
            "『异端制裁者』……不对，是『千之护手』。\x02\x03",
            "#10402F刚刚换了新诨名，\x01",
            "可别就此丢了性命啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x8C, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "哈哈，说的也是。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x8,
        (
            "#12102F#6P说起来，那个诨名是来自\x01",
            "『千之腕』露菲娜大人吧……\x02\x03",
            "格拉汉姆大人，你得到了一个很不错的诨名啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x91, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "……多谢夸奖。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xBE, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("莉丝修女")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x101,
        "#00008F#12P（似乎有不少隐情呢……）\x02",
    )

    CloseMessageWindow()
    OP_5B(0x55, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德，前路艰辛，\x01",
            "希望你多加努力。\x02\x03",
            "在如今这种状况下，克洛斯贝尔\x01",
            "已经不能指望来自外界的援助了。\x02\x03",
            "现在唯一的希望，就是你至今为止\x01",
            "在克洛斯贝尔所积累的羁绊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x101,
        (
            "#00005F#12P积累的羁绊……\x02\x03",
            "#00004F明白了，\x01",
            "我会谨记于心的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_70(0x1, 0x20)
    OP_0D()
    Sleep(500)
    OP_5B(0xBE, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("莉丝修女")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德警官，愿女神保佑你们。\x02\x03",
            "艾莉小姐就\x01",
            "拜托你了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x101,
        "#00000F#12P嗯，放心！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_70(0x1, 0x1E)
    Sound(73, 0, 100, 0)
    Sleep(300)
    OP_6C(0x4CC2, 0xBB8)
    OP_21(0xBB8)
    Sleep(1000)
    Sound(943, 2, 60, 0)
    OP_71(0x1, 0x2F, 0x4C, 0x0, 0x8)
    Sleep(500)
    SetChrSubChip(0x105, 0x0)
    OP_6F(0x79)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70542", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_79(0x1)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(1002, 0, 40, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 2000, 0, 12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00011F#12P怎么回事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11P已启动光学迷彩机能。\x02\x03",
            "当然，并不能完美隐匿机体，\x01",
            "而且还有启动之后\x01",
            "会使速度降低等缺点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11P如果就这样直接潜入，\x01",
            "那些高机动性能的智能兵器\x01",
            "肯定会立刻出来迎击。\x02\x03",
            "#10401F即使认真迎战，\x01",
            "我们恐怕也没有什么胜算，\x01",
            "所以就由五号机来引开它们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12P原来如此……\x01",
            "然后我们就趁机潜入吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#3C#12P唔，就让我好好见识一下\x01",
            "星杯守护者的实力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x50AA, 0x7D0)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x105, 0x4)
    OP_6F(0x79)
    OP_24(0x3AF)
    SetScenarioFlags(0x22, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1A5F end

    def Function_9_22D4(): pass

    label("Function_9_22D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SoundLoad(497)
    SoundLoad(498)
    SoundLoad(132)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis335.itp")
    CreatePortrait(1, 198, 150, 214, 166, 0, 0, 512, 256, 488, 0, 504, 16, 0xFFFFFF, 0x0, "c_vis335.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_A2(0x101, 0x4)
    SetChrPos(0x101, 100230, 50, -102650, 270)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    OP_A2(0x105, 0x4)
    SetChrPos(0x105, 98470, 50, -101100, 180)
    SetChrChipByIndex(0x107, 0x10)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x107, 100400, 0, -101700, 270)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    OP_A2(0x8, 0x8000)
    SetChrPos(0x8, 750, 0, -2500, 270)
    SetChrChipByIndex(0x15, 0xE)
    SetChrSubChip(0x15, 0x0)
    OP_A2(0x15, 0x8000)
    OP_4B(0x15, 0xFF)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    OP_A2(0x16, 0x8000)
    OP_4B(0x16, 0xFF)
    SetChrPos(0x15, -750, 0, -2000, 90)
    SetChrPos(0x16, -750, 0, -3000, 90)
    OP_72(0x0, 0x1000)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 1500, 1000000, 0)
    OP_6D(0x78, 0x0, 0x0, 0x0)
    OP_6E(0x320, 0x0)
    OP_6C(0xC350, 0x0)
    OP_6D(0x87, 0xA, 0x0, 0x1770)
    OP_6C(0x9C40, 0x1770)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0xFFFF)
    Sleep(500)
    Sound(498, 2, 100, 0)
    OP_68(1500, 1000, 500, 0)
    OP_6D(0x2D, 0x19, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5208, 0x0)
    OP_68(1500, 1000, -2500, 6000)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(100110, 3000, -101660, 0)
    OP_6D(0x32, 0x14, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x4542, 0x0)
    OP_68(100110, 1000, -101660, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10406F#5P我们总算成功潜入了，\x01",
            "但克洛斯贝尔如今已经\x01",
            "完全与『至宝』融为了一体。\x02\x03",
            "#10401F在接下来的行动中，如果不多加注意，\x01",
            "智能兵器肯定会飞袭而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11P也就是说，不能一直\x01",
            "依靠这艘飞艇吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3C确实如此，以这艘飞艇的大小来说，如果\x01",
            "直接降落到地面，马上就会被由灵智之草\x01",
            "而构建的『网络』所捕捉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P是的，这样下去，\x01",
            "我们连着陆都无法做到……\x02\x03",
            "#10400F所以，我接下来准备探查\x01",
            "七耀脉力场的『狭间』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11P力场的『狭间』……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C嗯，七耀脉力场\x01",
            "覆盖着整个大地。\x02\x03",
            "#01200F不过，在一股股强大的波流之间，\x01",
            "也会存在一些『狭间』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P原来如此……\x02\x03",
            "#00000F也就是说，我们只要在这些『狭间』\x01",
            "中着陆，就不会被发现了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5P呵呵，正是如此。\x02\x03",
            "#10402F另外，我们现在所处的位置\x01",
            "正好就是那样的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(1300)
    OP_5B(0x1E, 0xA, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            "#00001F乌尔斯拉间道的河滩……\x01",
            "离当时出现幻兽的那个地方很近呢。\x02\x03",
            "#00005F你们竟能这么快就发现『狭间』啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0x5A, 0xC8, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x105,
        (
            "#10404F呵呵，在异变发生前，\x01",
            "我就和阿巴斯一起调查过了。\x02\x03",
            "#10402F耍了点小伎俩之后，\x01",
            "就逃离了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0x1E, 0xA, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        "#00011F原、原来如此。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xFA, 0x14, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x107,
        "#01203F#3C唔，还真是准备周全。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0x5A, 0xC8, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x105,
        (
            "#10404F#0C不过现在只找到了这一个地方。\x01",
            "为了增加着陆地点，今后必须\x01",
            "要继续寻找其它『狭间』呢。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10403F#5P那么，接下来要怎么办？\x02\x03",
            "#10400F既然有『结界』阻挡，\x01",
            "我们肯定无法进入克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P……是啊，\x01",
            "不过还是先降落吧。\x02\x03",
            "#00008F哪怕只是一点点也好，\x01",
            "我很想了解克洛斯贝尔现在的状况……\x02\x03",
            "#00001F而且还想确认一下\x01",
            "乌尔斯拉医院的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#5P呵呵，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01203F#11P#3C那就降落吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x105)
    Sleep(500)

    ChrTalk(
        0x107,
        "#01200F#5P#3C嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P那个……事到如今，似乎不该再问这种问题了……\x02\x03",
            "#00001F但是蔡特……你为何要\x01",
            "帮助我们呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P从你对利贝尔那条龙的介绍来看……\x02\x03",
            "#10401F你们圣兽对于围绕『至宝』而产生的\x01",
            "种种因缘，应该只能旁观见证，\x01",
            "并不能直接介入其中吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3C不错，因为我们要遵守古老的『盟约』。\x02\x03",
            "#01200F然而，如今『幻之至宝』已经消失，\x01",
            "我原有的使命便随之结束了。\x02\x03",
            "束缚吾身的『禁忌』也因此而减轻，\x01",
            "所以我可以在一定程度上自由行动。\x02\x03",
            "至少可以给人类之子\x01",
            "提供少量的帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11P所以你当时才会在黑手党的军犬\x01",
            "事件中向我们伸出援手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C嗯，正是。\x02\x03",
            "#01200F虽然我不能无限制地帮助你们……\x01",
            "但在短时间内，就继续\x01",
            "给你们提供协助吧。\x02\x03",
            "毕竟我也算是登录在案的\x01",
            "『警犬』啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P哈哈，明白了，\x01",
            "那就请你多帮忙啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x105, 0x0)
    Sleep(150)

    ChrTalk(
        0x105,
        (
            "#10404F#5P看来我们暂时就要以\x01",
            "这种阵容来行动了。\x02\x03",
            "#10400F如果想降落到地面，\x01",
            "就去找阿巴斯吧。\x02\x03",
            "另外，这艘『梅尔卡瓦』内部\x01",
            "备有数种设施。\x02\x03",
            "#10404F其中包括装备店、道具店以及工房，\x01",
            "如果有什么需要，就去和舰员们说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00000F#11P好的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_6C(0x463C, 0x3E8)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "瓦吉与蔡特加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x4, 0x12D)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "瓦吉习得Ｓ战技\x01\x07\x02",
            "『虚空手臂』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xFFFF, 0x34, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "『虚空手臂』\x07\x05",
            "设置为Ｓ爆发技吗？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(0x2),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312C")
    SetChrChipPat(0x4, 0x6, 0x12D)

    label("loc_312C")

    OP_5A()
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "蔡特暂时会以战斗成员\x01",
            "的身份参加战斗。\x02\x03",
            "由于蔡特并未持有艾尼格玛Ⅱ，\x01",
            "因此无法对其回路进行调整，\x01",
            "但它可以使用威力强大的高级魔法。\x02\x03",
            "同时还请注意，\x01",
            "蔡特并没有Ｓ战技。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "另外，身处梅尔卡瓦舰内时，\x01",
            "罗伊德就会单独行动，\x01",
            "其他成员则在舰内待命。\x02\x03",
            "不过在主菜单中仍然可以\x01",
            "对全员的装备、回路进行操作，\x01",
            "在商店和工房也可参考各项数值。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_A3(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_A3(0x15, 0x8000)
    SetChrPos(0x15, 103570, 0, -97090, 270)
    OP_4C(0x15, 0xFF)
    OP_A3(0x16, 0x8000)
    SetChrPos(0x16, 103950, 0, -210, 270)
    OP_4C(0x16, 0xFF)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    OP_73(0x0, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_A3(0x101, 0x4)
    OP_A3(0x105, 0x4)
    OP_49()
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(0x1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x6, 0xFF)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 100150, 0, -100950, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x20, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    SetScenarioFlags(0x1A0, 0)
    OP_29(0xAF, 0x4, 0x2)
    OP_29(0xAF, 0x1, 0x0)
    Sound(498, 2, 100, 0)
    ClearScenarioFlags(0x32, 0)
    ClearScenarioFlags(0x32, 1)
    ClearScenarioFlags(0x32, 2)
    ClearScenarioFlags(0x32, 3)
    ClearScenarioFlags(0x32, 4)
    ClearScenarioFlags(0x32, 5)
    ClearScenarioFlags(0x32, 6)
    ClearScenarioFlags(0x32, 7)
    ClearScenarioFlags(0x33, 0)
    ClearScenarioFlags(0x33, 1)
    ClearScenarioFlags(0x33, 2)
    ClearScenarioFlags(0x33, 3)
    ClearScenarioFlags(0x33, 4)
    ClearScenarioFlags(0x33, 5)
    ClearScenarioFlags(0x33, 6)
    ClearScenarioFlags(0x33, 7)
    ClearScenarioFlags(0x34, 0)
    ClearScenarioFlags(0x34, 1)
    ClearScenarioFlags(0x34, 2)
    ClearScenarioFlags(0x34, 3)
    ClearScenarioFlags(0x34, 4)
    ClearScenarioFlags(0x34, 5)
    ClearScenarioFlags(0x34, 6)
    ClearScenarioFlags(0x34, 7)
    ClearScenarioFlags(0x31, 6)
    ClearScenarioFlags(0x31, 4)
    ClearScenarioFlags(0x2F, 6)
    ClearScenarioFlags(0x31, 3)
    ClearScenarioFlags(0x2D, 6)
    ClearScenarioFlags(0x2D, 4)
    ClearScenarioFlags(0x2D, 2)
    ClearScenarioFlags(0x2B, 6)
    ClearScenarioFlags(0x35, 0)
    ClearScenarioFlags(0x35, 1)
    ClearScenarioFlags(0x35, 2)
    ClearScenarioFlags(0x35, 3)
    ClearScenarioFlags(0x35, 4)
    ClearScenarioFlags(0x35, 5)
    ClearScenarioFlags(0x35, 6)
    ClearScenarioFlags(0x35, 7)
    ClearScenarioFlags(0x36, 0)
    ClearScenarioFlags(0x36, 1)
    ClearScenarioFlags(0x36, 2)
    ClearScenarioFlags(0x36, 3)
    ClearScenarioFlags(0x36, 4)
    ClearScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x36, 6)
    ClearScenarioFlags(0x36, 7)
    ClearScenarioFlags(0x37, 0)
    ClearScenarioFlags(0x37, 1)
    ClearScenarioFlags(0x37, 2)
    ClearScenarioFlags(0x37, 3)
    ClearScenarioFlags(0x37, 4)
    ClearScenarioFlags(0x37, 5)
    ClearScenarioFlags(0x37, 6)
    ClearScenarioFlags(0x37, 7)
    ClearScenarioFlags(0x31, 7)
    ClearScenarioFlags(0x31, 5)
    ClearScenarioFlags(0x2F, 7)
    ClearScenarioFlags(0x2F, 5)
    ClearScenarioFlags(0x2D, 7)
    ClearScenarioFlags(0x2D, 5)
    ClearScenarioFlags(0x2D, 3)
    ClearScenarioFlags(0x2B, 7)
    EventEnd(0x5)
    Return()

    # Function_9_22D4 end

    def Function_10_3440(): pass

    label("Function_10_3440")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3481")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_10_3440")

    label("loc_3481")

    Return()

    # Function_10_3440 end

    def Function_11_3482(): pass

    label("Function_11_3482")

    EventBegin(0x0)
    Fade(500)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-220, -500, 6740, 0)
    OP_6D(0x2D, 0x14, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x4650, 0x0)
    SetChrSubChip(0x8, 0x1)
    SetChrPos(0x101, -1500, -1500, 6000, 45)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A7")

    ChrTalk(
        0x8,
        "#12100F#11P想好了吗，接下来要做些什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P这个嘛，总之就先\x01",
            "降落到这个地方看看吧。\x02\x03",
            "#00000F话说回来，没想到你们\x01",
            "竟然有这样的背景。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11P这一切都是为了瞒过\x01",
            "教会内部的对立者——对骑士团\x01",
            "持批判态度的艾拉尔达大主教。\x02\x03",
            "谁都不会想到，\x01",
            "最高级别的骑士之一\x01",
            "就是不良团伙的头目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P这个嘛，确实如此。\x02\x03",
            "#00005F啊，但你们不是经常\x01",
            "胡乱使用圣典、圣战这些\x01",
            "很有宗教特色的词语吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12105F#11P哦，你说那个啊。\x02\x03",
            "#12100F我认为那种不严肃的态度\x01",
            "反而更能混淆他人的视线……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P说、说的也是，\x01",
            "营造出了一种很独特的组织氛围，\x01",
            "成功蒙混了过去。\x02\x03",
            "#00000F对了，\x01",
            "现在随时可以降落吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11P是的，我们已经精确\x01",
            "掌握了『狭间』的位置。\x02\x03",
            "做好准备之后，和我说一声就可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1A0, 1)
    Jump("loc_381E")

    label("loc_37A7")


    ChrTalk(
        0x8,
        (
            "#12100F#11P我们已经精确掌握了\x01",
            "『狭间』的位置。\x02\x03",
            "做好准备之后，只要和我说一声，\x01",
            "就可以降落到乌尔斯拉间道的河滩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_381E")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "降落\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3862"),
        (1, "loc_3902"),
        (SWITCH_DEFAULT, "loc_395A"),
    )


    label("loc_3862")


    ChrTalk(
        0x8,
        (
            "#12102F#11P明白了，下去之后\x01",
            "不要忘记飞艇的所在位置。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_38E2")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x0)
    Call(0, 12)
    Call(0, 5)
    Call(0, 7)
    Jump("loc_38FD")

    label("loc_38E2")

    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_38FD")

    Jump("loc_395A")

    label("loc_3902")


    ChrTalk(
        0x8,
        (
            "#12100F#11P既然如此，做好准备之后，\x01",
            "就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x0, -1500, -1500, 6000, 45)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_395A")

    label("loc_395A")

    Return()

    # Function_11_3482 end

    def Function_12_395B(): pass

    label("Function_12_395B")

    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    OP_A2(0x8, 0x8000)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    OP_68(0, 500, 3500, 0)
    OP_6D(0x2D, 0x19, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5208, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_68(0, 5000, 3500, 3000)
    Sleep(2000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x105, 0x4)
    SetScenarioFlags(0x22, 1)
    Return()

    # Function_12_395B end

    def Function_13_3A18(): pass

    label("Function_13_3A18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(938)
    SoundLoad(132)
    SoundLoad(497)
    OP_A2(0xB, 0x80)
    OP_A2(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    OP_A2(0x8, 0x8000)
    OP_A3(0xC, 0x80)
    OP_A2(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    OP_6D(0x2D, 0x12, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x49AC, 0x0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -750, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    Sound(938, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00203F#12P#N……感知到了新的\x01",
            "七耀脉力场的『狭间』。\x02\x03",
            "#00202F我马上把数据传送过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#01909F#5P好的，明白了。\x02\x03",
            "#01901F（敲击键盘……）\x01",
            "成功确定了坐标！\x02\x03",
            "就在克洛斯贝尔东北区域，\x01",
            "『阿尔摩利卡村』附近！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00002F#12P真厉害……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102F#11P唔，真是帮大忙了。\x02\x03",
            "普拉托的感应能力自不必说，\x01",
            "如今还有了熟悉终端操作的专业通讯员，\x01",
            "船舰的运用效率真是大幅提升了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5P嘿嘿……\x01",
            "我的水平还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11P呵呵，看来我们今后能够\x01",
            "高效率地寻找可降落地点了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x105, 0x1)
    Sleep(200)

    ChrTalk(
        0x105,
        (
            "#10400F#5P那么，接下来有什么计划？\x02\x03",
            "直接去那个新地点\x01",
            "看看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P嗯，这样就可以确认一下\x01",
            "阿尔摩利卡村的状况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#11P启动最大机能，目的地是\x01",
            "『阿尔摩利卡村』的上空。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F#12P#N在保持警戒的状态下，\x01",
            "前往目的地。\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x4AA6, 0x3E8)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_24(0x3AA)
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_F3(0x186A0)
    OP_A3(0x1E, 0x80)
    OP_78(0x0, 0x1E)
    OP_49()
    OP_73(0x0, 0x4)
    OP_72(0x0, 0x1000)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)
    PlayEffect(0x0, 0x0, 0x1E, 0x5, -4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1E, 0x5, 4250, 1750, -10250, 0, 0, 0, 1500, 1500, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-1000000, 0, 800000, 0)
    OP_6D(0x14A, 0xFFF9, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x1B198, 0x0)
    OP_6D(0x154, 0xFFF9, 0x0, 0xBB8)

    def lambda_3F33():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3F33)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sound(499, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    StopSound(497, 3000, 100)
    Sleep(2000)
    StopSound(132, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0xFFFF)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    Sleep(500)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(0x1)
    OP_A3(0x103, 0x4)
    OP_A3(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    OP_A3(0x8, 0x8000)
    OP_A3(0xC, 0x8000)
    SetScenarioFlags(0x26, 2)
    SetScenarioFlags(0x1A1, 2)
    OP_29(0xAF, 0x1, 0x3)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_4036")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x31), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_402B")
    Call(0, 6)
    Jump("loc_402E")

    label("loc_402B")

    Call(0, 5)

    label("loc_402E")

    Call(0, 7)
    Jump("loc_403F")

    label("loc_4036")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_403F")

    Return()

    # Function_13_3A18 end

    def Function_14_4040(): pass

    label("Function_14_4040")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_405A")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_14_4040")

    label("loc_405A")

    Return()

    # Function_14_4040 end

    def Function_15_405B(): pass

    label("Function_15_405B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    SoundLoad(938)
    OP_A2(0xB, 0x80)
    OP_A2(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    OP_A2(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0xC, 0x80)
    OP_A2(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    OP_6D(0x2D, 0x12, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x49AC, 0x0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 500, 0, -950, 0)
    SetChrPos(0x106, -1400, 0, -1150, 0)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    Sound(938, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00204F#12P#N感知到了新的『狭间』。\x02\x03",
            "#00202F芙兰小姐，\x01",
            "我把数据传送过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F#5P收到～\x01",
            "（敲击键盘……）\x02\x03",
            "#01905F分析完毕！\x01",
            "就在克洛斯贝尔西北区域……\x02\x03",
            "#01901F玛因兹山道的中间地点！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        (
            "#00002F#12P玛因兹地区吗……\x01",
            "我们的行动范围又扩大了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11P不过，对方差不多也该\x01",
            "察觉到我们的动向了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#N……说起来，除了黑月之外，\x01",
            "在玛因兹地区也有一股势力\x01",
            "正在发起反抗活动。\x02\x03",
            "#10701F听说他们的首领是\x01",
            "对国防军的现状抱持\x01",
            "反对意见的原警备队成员。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-1230, 1100, 3390, 1000)
    OP_6C(0x4D58, 0x3E8)

    def lambda_442A():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_442A)
    OP_A2(0x107, 0x20)

    def lambda_443C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_443C)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x1)
    OP_6F(0x79)
    OP_A3(0x107, 0x20)

    ChrTalk(
        0x101,
        "#00011F#5P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5P我本以为所有警备队员都已\x01",
            "加入国防军了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5P唔，这也不难理解。\x02\x03",
            "『赤色星座』曾沉痛打击过\x01",
            "警备队，如今却可以\x01",
            "大摇大摆地四处行动。\x02\x03",
            "有人无法忍受这种欺骗行径\x01",
            "也不足为奇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01901F#5P既、既然如此，\x01",
            "说不定姐姐她也……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00006F#11P……不，\x01",
            "很遗憾，她恐怕不会那样做。\x02\x03",
            "#00008F诺艾尔是在坚定决心，忍下了一切之后，\x01",
            "才选择了继续守护如今这个克洛斯贝尔\x01",
            "的道路。\x02\x03",
            "#00013F她那份决心是\x01",
            "不会轻易动摇的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01912F#5P#30W……啊哈哈，说的也是。\x02\x03",
            "#01908F#30W姐姐她真的很坚强……\x01",
            "但也很笨拙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#5P……芙兰小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P好啦，不管怎么说，\x01",
            "我们还是去和那股反抗势力\x01",
            "接触一下为好。\x02\x03",
            "#10400F说不定他们还会和\x01",
            "『黑月』一样协助我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11P嗯，立刻降落吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#5P……对了，莉夏。\x02\x03",
            "#00000F在此之前，你要不要去\x01",
            "乌尔斯拉医院看看？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10712F#12P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P伊莉娅小姐\x01",
            "非常想见你。\x02\x03",
            "#00002F我也知道你大概有很多自己的想法……\x01",
            "不过，还是让她看看你精神十足的样子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)

    ChrTalk(
        0x106,
        (
            "#10706F#12P……不，还是不要了。\x02\x03",
            "#10708F我现在还无法坦然地\x01",
            "站在伊莉娅小姐的面前……\x02\x03",
            "#10710F如果要见面，至少也要等到\x01",
            "解放克洛斯贝尔市，\x01",
            "并夺回彩虹剧团之后。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P……这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5P虽然很让人焦急……\x01",
            "但我能明白你的心情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12P啊哈哈……抱歉。\x02\x03",
            "#10702F啊，当然了，\x01",
            "如果各位有要事的话，\x01",
            "去乌尔斯拉医院也无妨……！\x02\x03",
            "#10704F至于我……会在医院门前\x01",
            "等着各位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5P好吧，我明白了。\x02\x03",
            "#00000F（话说回来……\x01",
            "  这才是莉夏的本性啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x4E52, 0x3E8)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "莉夏加入了队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ACE")
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)
    Jump("loc_4AD6")

    label("loc_4ACE")

    AddCraft(0x5, 0x195)
    AddCraft(0x0, 0x195)

    label("loc_4AD6")

    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和莉夏习得组合战技\x01\x07\x02",
            "『比翼双龙击』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(0x1)
    OP_A3(0x103, 0x4)
    OP_A3(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    OP_A3(0x8, 0x8000)
    OP_A3(0xC, 0x8000)
    ClearChrBattleFlags(0xA, 0x4)
    OP_A3(0xA, 0x80)
    SetChrPos(0xA, -1520, 0, -100980, 180)
    SetChrChipByIndex(0xA, 0x2)
    BeginChrThread(0xA, 0, 0, 0)
    SetScenarioFlags(0x26, 5)
    SetScenarioFlags(0x1A1, 7)
    OP_29(0xAF, 0x1, 0x7)
    Sleep(300)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    OP_24(0x3AA)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_4C23")
    FadeToDark(0, 0, -1)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C18")
    Call(0, 6)
    Jump("loc_4C1B")

    label("loc_4C18")

    Call(0, 5)

    label("loc_4C1B")

    Call(0, 7)
    Jump("loc_4C2C")

    label("loc_4C23")

    NewScene("e3020", 102, 0, 0)
    IdleLoop()

    label("loc_4C2C")

    Return()

    # Function_15_405B end

    def Function_16_4C2D(): pass

    label("Function_16_4C2D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    SoundLoad(938)
    OP_A2(0xB, 0x80)
    OP_A2(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    OP_A2(0x8, 0x8000)
    OP_A3(0xC, 0x80)
    OP_A2(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    OP_A3(0xF, 0x80)
    OP_A2(0xF, 0x8000)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-560, 2900, 4130, 0)
    OP_6D(0x27, 0x12, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x4D58, 0x0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 1300, 0, -1500, 0)
    SetChrPos(0x106, -1400, 0, -1150, 0)
    SetChrPos(0x104, 200, 0, -750, 0)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xF, -750, 500, 3300, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-560, 1100, 4130, 3500)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_63(0xF, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#02109F#11P哇……\x01",
            "这艘飞艇真是好棒！\x02\x03",
            "#02110F没想到七耀教会\x01",
            "竟然拥有这样的飞艇！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5P……我重申一次，\x01",
            "绝不要把这里的事情外泄。\x02\x03",
            "如果你擅自写到报道之中，\x01",
            "就要做好今后失去教会\x01",
            "一切庇护的心理准备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#11P哈哈，就算真的写进报道，\x01",
            "读者们应该也只会把它当作\x01",
            "荒唐无稽的奇谈怪论吧？\x02\x03",
            "#10402F就像当时对『结社』的报道一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12107F#5P瓦吉……！\x02",
    )

    CloseMessageWindow()
    OP_68(-230, 1100, 2950, 1000)
    OP_6C(0x4D58, 0x3E8)
    OP_93(0xF, 0xB4, 0x1F4)
    Sleep(300)
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#02104F#5P不用担心，我会严格遵守约定的。\x02\x03",
            "#02100F当然也不会泄露莉夏·毛的真正身份\x01",
            "就是神秘魔人『银』这件事！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10706F#12P#N……拜托您了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P（我说，罗伊德……）\x02\x03",
            "#00301F（带她一起上来，\x01",
            "  真的没问题吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P（应、应该没问题吧，\x01",
            "  我相信她会遵守约定。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-790, 1100, 4000, 1000)
    OP_6F(0x79)
    Sound(938, 2, 100, 0)

    ChrTalk(
        0x103,
        (
            "#00201F#11P在克洛斯贝尔西部\x01",
            "感知到了新的『狭间』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xF, 0x13B, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#01908F#5P（敲击键盘……）\x01",
            "已确定具体坐标。\x02\x03",
            "#01903F位于西克洛斯贝尔街道的中部……\x02\x03",
            "#01901F就在通往警察学校与拘留所的\x01",
            "那条路的岔路口附近。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(938, 300, 100)

    ChrTalk(
        0x101,
        "#00001F#11P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12P对了，在你逃离拘留所的\x01",
            "时候，加尔西亚大叔帮了\x01",
            "很大的忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P嗯……虽然他一直冷嘲热讽，\x01",
            "但确实为我提供了很大帮助。\x02\x03",
            "#00008F不知他之后到底怎么样了，\x01",
            "真是有些在意呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10406F#5P不过，现在去警察学校那边\x01",
            "可不是什么好主意。\x02\x03",
            "#10401F由于你从那里逃脱，\x01",
            "目前警备力度肯定大幅加强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P#N至于其它的可去之处，\x01",
            "也只有国防军驻守的贝尔加德门……\x02\x03",
            "#10701F真让人为难呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        (
            "#02106F#11P嗯，如果毫无防备地跑到那里，\x01",
            "一定会被抓住的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01908F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P……不管怎么说，\x01",
            "还是先降落吧。\x02\x03",
            "#00001F我想确认一下国防军\x01",
            "的警备力度有多强，\x01",
            "而且也很在意幻兽的游荡状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#11P明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5P在矿山镇前也已\x01",
            "设置了『法阵』。\x02\x03",
            "今后随时都可以降落。\x01",
            "如果有需要，和我说一声就行。\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x4E52, 0x3E8)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    EndChrThread(0x103, 0x0)
    EndChrThread(0xC, 0x0)
    Sound(814, 0, 100, 0)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "兰迪加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x3, 0x129)
    AddCraft(0x3, 0x168)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "兰迪习得Ｓ战技\x01\x07\x02",
            "『狂战士』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xFFFF, 0x34, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "『狂战士』\x07\x05",
            "设置为Ｓ爆发技吗？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(0x2),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F6")
    SetChrChipPat(0x3, 0x6, 0x129)

    label("loc_55F6")

    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(0x1)
    OP_A3(0x103, 0x4)
    OP_A3(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    OP_A2(0xA, 0x80)
    SetChrPos(0x0, -150, 0, -88230, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x26, 3)
    SetScenarioFlags(0x1A2, 7)
    OP_29(0xAF, 0x1, 0xD)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_16_4C2D end

    def Function_17_564F(): pass

    label("Function_17_564F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06900.itc", 0x1E)
    LoadChrToIndex("apl/ch51027.itc", 0x1F)
    LoadChrToIndex("apl/ch51712.itc", 0x20)
    SoundLoad(498)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x1B, 0x80)
    OP_A2(0x1B, 0x8000)
    OP_A3(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    OP_A2(0x1C, 0x8000)
    SetChrPos(0x101, 500, 0, -104000, 0)
    SetChrPos(0x1B, -500, 0, -104000, 0)
    SetChrPos(0x106, 500, 0, -104000, 0)
    SetChrPos(0x103, -500, 0, -104000, 0)
    SetChrPos(0x104, 500, 0, -104000, 0)
    SetChrPos(0x105, -500, 0, -104000, 0)
    SetChrPos(0x107, 0, 0, -104000, 0)
    SetChrPos(0x1C, 0, 0, -85000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_73(0x2, 0x10)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "之后，诺艾尔收拾好行李，\x01",
            "与罗伊德等人一同乘上了梅尔卡瓦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed70514", 0)
    Sound(498, 2, 100, 0)
    OP_68(0, 1250, -102500, 0)
    OP_68(0, 1250, -93000, 6000)
    OP_6D(0x2D, 0x19, 0x0, 0x0)
    OP_6D(0x2D, 0x14, 0x0, 0x1770)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x4268, 0x0)
    FadeToBright(1000, 0)

    def lambda_5830():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5830)

    def lambda_5845():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5845)
    Sleep(100)

    def lambda_5859():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5859)

    def lambda_586E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_586E)
    Sleep(500)

    def lambda_5882():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5882)

    def lambda_5897():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_5897)
    Sleep(100)

    def lambda_58AB():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_58AB)

    def lambda_58C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_58C0)
    Sleep(500)

    def lambda_58D4():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_58D4)

    def lambda_58E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_58E9)
    Sleep(100)

    def lambda_58FD():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58FD)

    def lambda_5912():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5912)
    Sleep(800)

    def lambda_5926():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5926)

    def lambda_593B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_593B)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_5964():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5964)

    def lambda_5979():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5979)
    WaitChrThread(0x1C, 0x1)
    WaitChrThread(0x1C, 0x2)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x1B, 0x1)
    WaitChrThread(0x1B, 0x2)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x103, 0x2)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x104, 0x2)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x105, 0x2)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x107, 0x2)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    OP_63(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_59EA():

        label("loc_59EA")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_59EA")

    QueueWorkItem2(0x101, 2, lambda_59EA)

    def lambda_59FC():

        label("loc_59FC")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_59FC")

    QueueWorkItem2(0x103, 2, lambda_59FC)

    def lambda_5A0E():

        label("loc_5A0E")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5A0E")

    QueueWorkItem2(0x104, 2, lambda_5A0E)

    def lambda_5A20():

        label("loc_5A20")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5A20")

    QueueWorkItem2(0x105, 2, lambda_5A20)

    def lambda_5A32():

        label("loc_5A32")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_5A32")

    QueueWorkItem2(0x106, 2, lambda_5A32)
    OP_68(0, 1250, -95000, 2500)
    OP_6C(0x4074, 0x4268)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x1C, 3, 0, 19)
    Sleep(3000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "出来迎接的芙兰\x01",
            "冲上去抱住了诺艾尔，\x01",
            "低声抽泣不止……\x02\x03",
            "而诺艾尔在安抚妹妹的同时，\x01",
            "双目也已湿润，泛出了泪水。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_6C(0x4074, 0x3E8)
    OP_6F(0x79)
    OP_0D()
    OP_21(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_564F end

    def Function_18_5B1D(): pass

    label("Function_18_5B1D")


    def lambda_5B22():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B22)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_18_5B1D end

    def Function_19_5B42(): pass

    label("Function_19_5B42")

    OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFE8E78, 0x1770, 0x0)
    Fade(250)
    OP_A2(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_A2(0x1B, 0x2)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    Sound(812, 0, 100, 0)
    Sound(811, 0, 30, 0)
    OP_A6(0x1B, 0x0, 0xA, 0x1F4, 0xBB8)
    OP_0D()
    OP_63(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x1B)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x106, 0x2)
    Sleep(500)

    def lambda_5BC9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5BC9)
    WaitChrThread(0x1C, 0x2)
    Sleep(500)

    def lambda_5BE9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5BE9)
    WaitChrThread(0x1C, 0x2)
    Sleep(1500)

    def lambda_5C09():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5C09)
    WaitChrThread(0x1C, 0x2)
    Sleep(500)

    def lambda_5C29():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_5C29)
    WaitChrThread(0x1C, 0x2)
    Return()

    # Function_19_5B42 end

    def Function_20_5C42(): pass

    label("Function_20_5C42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x8, 0xFF, 0xFF)
    OP_32(0x8, 0x0, 0x56)
    OP_32(0x8, 0x5, 0x64)
    OP_42(0x8, 0x455, 0xFF)
    OP_42(0x8, 0x5ED, 0xFF)
    OP_42(0x8, 0x651, 0xFF)
    OP_38(0x8, 0x81, 0x2)
    OP_38(0x8, 0x84, 0x2)
    OP_38(0x8, 0x85, 0x2)
    OP_38(0x8, 0x86, 0x2)
    OP_42(0x8, 0xB4, 0x1)
    OP_42(0x8, 0x72, 0x4)
    OP_42(0x8, 0xB9, 0x5)
    OP_42(0x8, 0xA0, 0x6)
    AddCraft(0x8, 0xEC)
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("apl/ch51773.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis284.itp")
    OP_A2(0xB, 0x80)
    OP_A2(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x107, 0x5)
    OP_A2(0x8, 0x8000)
    OP_A3(0xC, 0x80)
    OP_A2(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    OP_A3(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    OP_A2(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0x103, 0, 0, 14)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 14)
    OP_68(-850, 2900, 3210, 0)
    OP_6D(0x27, 0x13, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x50D2, 0x0)
    SetChrPos(0x101, -750, 250, 300, 0)
    SetChrPos(0x103, -3100, -1350, 7100, 315)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x107, 1500, 0, -1500, 0)
    SetChrPos(0x106, -1500, 0, -1250, 0)
    SetChrPos(0x104, 500, 0, -750, 0)
    SetChrPos(0x109, -500, 0, -1750, 0)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrPos(0xF, -3480, -1500, 4650, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    OP_68(-850, 1100, 3210, 3500)
    OP_6D(0x27, 0x13, 0x0, 0xDAC)
    OP_6E(0x1F4, 0xDAC)
    OP_6C(0x50D2, 0xDAC)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(836, 0, 100, 0)

    ChrTalk(
        0x103,
        (
            "#00204F#11P……感知到了位于\x01",
            "米修拉姆一带的『狭间』。\x02\x03",
            "#00202F芙兰小姐，我这就把坐标传送给你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01908F#5P嗯，呜呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12P真是的……\x01",
            "你要哭到什么时候啊？\x02\x03",
            "#10101F会被大家取笑的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#11P哈哈，不会啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#12P#N呵呵……\x01",
            "总觉得很羡慕二位呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0xC,
        (
            "#01909F#5P嘿嘿……不好意思。\x02\x03",
            "#01900F（敲击键盘……）\x01",
            "已经确定了位置！\x02\x03",
            "#01903F在米修拉姆疗养地的\x01",
            "翠雀酒店附近……\x02\x03",
            "#01901F就在那个湖水浴场呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12P哇，这还真是巧啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11P呵呵，但这次可不是\x01",
            "去悠闲度假了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x101, 500)

    ChrTalk(
        0xF,
        (
            "#02105F#5P啊，难道说……\x02\x03",
            "你们曾去那里的\x01",
            "湖水浴场玩过吗？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_60B7():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_60B7)
    Sleep(50)

    def lambda_60C7():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_60C7)
    Sleep(50)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x104, 0x0)
    SetChrSubChip(0x103, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(100)

    ChrTalk(
        0x101,
        "#00002F#11P嗯，是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5P就在通商会议结束之后。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106F#5P真是的，你们好无情啊。\x02\x03",
            "#02101F那么有趣的活动，\x01",
            "为什么不叫上我啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P这个……其实我们也\x01",
            "只是被招待的客人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10408F#5P如今回想起来，她当时邀请我们，\x01",
            "似乎也怀有某种目的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#12P#N……确实如此。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x101,
        (
            "#00003F#11P……总之，\x01",
            "下一个目的地已经确定了。\x02\x03",
            "#00008F不过，那里似乎有『赤色星座』\x01",
            "的部队在把守……\x02\x03",
            "#00001F诺艾尔，你知道他们驻守在那里\x01",
            "的部队大概是什么规模吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#12P这个嘛……\x01",
            "大概有一个中队吧。\x02\x03",
            "#10113F如果以我们这个人数去正面交锋，\x01",
            "老实说，恐怕没有任何胜算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308F#11P不过，如果先发起佯攻，\x01",
            "将对方的战力分散……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10701F#12P#N既然如此，就由我……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A2(0x107, 0x20)
    TurnDirection(0x107, 0x109, 500)
    Sleep(150)
    OP_A3(0x107, 0x20)

    ChrTalk(
        0x107,
        (
            "#01203F#11P#3C不，还是交给我吧。\x02\x03",
            "#01201F只要我变回原本的形态，\x01",
            "足以吸引住相当数量的敌人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    EndChrThread(0xC, 0x0)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    OP_68(-50, 1100, 2370, 1000)

    def lambda_654E():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_654E)
    Sleep(50)

    def lambda_655E():
        TurnDirection(0x104, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_655E)
    Sleep(50)

    def lambda_656E():
        TurnDirection(0x109, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_656E)
    Sleep(50)

    def lambda_657E():
        TurnDirection(0x106, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_657E)
    Sleep(50)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x104, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x106, 0x0)
    SetChrSubChip(0xC, 0x2)
    Sleep(50)
    SetChrSubChip(0x8, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x103,
        "#00205F#5P蔡特……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5P这……真的可以吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#11P#3C我原本就打算\x01",
            "尽量多帮助你们。\x02\x03",
            "如今，你们的同伴陆续汇集，\x01",
            "已经积累了相当的战斗力，\x01",
            "差不多不再需要我的协助了。\x02\x03",
            "#01203F所以就把这当作是\x01",
            "我送给你们的最后赠礼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5P谢谢你了，蔡特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#5P是啊，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P不过，就算有蔡特助阵，\x01",
            "这场战斗也仍会相当严峻。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5P但不仅是议长，\x01",
            "连艾莉也在米修拉姆。\x02\x03",
            "#00007F做好万全的准备……\x01",
            "无论如何也要顺利解救他们！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67A8():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_67A8)
    Sleep(50)

    def lambda_67B8():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_67B8)
    Sleep(50)

    def lambda_67C8():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_67C8)
    Sleep(50)
    WaitChrThread(0x104, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x106, 0x0)

    ChrTalk(
        0x103,
        "#00201F#5P……好的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#11P没问题！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#12P明白！\x02",
    )

    CloseMessageWindow()
    OP_6C(0x51CC, 0x3E8)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "蔡特离开队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "诺艾尔加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x8, 0x141)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "诺艾尔习得Ｓ战技\x01\x07\x02",
            "『武装军势』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0xFFFF, 0x34, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "『武装军势』\x07\x05",
            "设置为Ｓ爆发技吗？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(0x2),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6947")
    SetChrChipPat(0x8, 0x6, 0x141)

    label("loc_6947")

    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x6, 0xFF)
    PartySelect(0x1)
    OP_A3(0x103, 0x4)
    OP_A3(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x36, 5)
    ClearScenarioFlags(0x26, 6)
    SetScenarioFlags(0x27, 0)
    SetScenarioFlags(0x1A3, 3)
    OP_29(0xAF, 0x1, 0x11)
    SetScenarioFlags(0x33, 5)
    SetScenarioFlags(0x36, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sound(498, 2, 100, 0)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5C42 end

    def Function_21_69A9(): pass

    label("Function_21_69A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F（……一旦在这里着陆，\x01",
            "  恐怕立刻就会与『赤色星座』\x01",
            "  展开战斗。）\x02\x03",
            "#00013F（降落之后，就无法进行补给了……\x01",
            "  已经做好万全准备了吗？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它的事情】\x01",      # 0
            "【降落在米修拉姆】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6A9D"),
        (1, "loc_6AAB"),
        (SWITCH_DEFAULT, "loc_6BF7"),
    )


    label("loc_6A9D")

    FadeToBright(0, 0)
    Jump("loc_6BF7")

    label("loc_6AAB")

    Call(0, 6)
    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AEE")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_6BDE")

    label("loc_6AEE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B11")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_6BDE")

    label("loc_6B11")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B34")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_6BDE")

    label("loc_6B34")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B57")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_6BDE")

    label("loc_6B57")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B7A")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_6BDE")

    label("loc_6B7A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9D")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_6BDE")

    label("loc_6B9D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BC0")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_6BDE")

    label("loc_6BC0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BDE")
    SetScenarioFlags(0x3C, 7)

    label("loc_6BDE")

    PartySelect(0x2)
    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_6BF7")

    label("loc_6BF7")

    Return()

    # Function_21_69A9 end

    def Function_22_6BF8(): pass

    label("Function_22_6BF8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis285.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    AddParty(0x1, 0xFF, 0xFF)
    OP_32(0x1, 0x0, 0x58)
    OP_32(0x1, 0x5, 0x64)
    OP_42(0x1, 0x405, 0xFF)
    OP_42(0x1, 0x5ED, 0xFF)
    OP_42(0x1, 0x651, 0xFF)
    OP_38(0x1, 0x83, 0x2)
    OP_38(0x1, 0x84, 0x2)
    OP_38(0x1, 0x85, 0x2)
    OP_38(0x1, 0x86, 0x2)
    OP_42(0x1, 0xA4, 0x3)
    OP_42(0x1, 0x7E, 0x4)
    OP_42(0x1, 0x82, 0x5)
    OP_42(0x1, 0xB3, 0x6)
    SetScenarioFlags(0x20, 3)
    SetScenarioFlags(0x20, 6)
    AddCraft(0x2, 0xB1)
    OP_32(0x6, 0x0, 0x5A)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A2(0x15, 0x80)
    OP_A2(0xA, 0x80)
    OP_A2(0xE, 0x80)
    OP_A2(0xD, 0x80)
    OP_A3(0x13, 0x80)
    OP_A3(0xF, 0x80)
    OP_A3(0x9, 0x80)
    OP_A3(0x12, 0x80)
    OP_A3(0xC, 0x80)
    OP_A2(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    OP_A2(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xA)
    SetChrSubChip(0x102, 0x2)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x1)
    OP_A2(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x19)
    SetChrSubChip(0x12, 0x0)
    OP_A2(0xF, 0x4)
    SetChrChipByIndex(0xF, 0x18)
    SetChrSubChip(0xF, 0x1)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0x13, 0x11)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 0)
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x12, 98470, 70, -101100, 180)
    SetChrPos(0x101, 100150, 70, -102850, 270)
    SetChrPos(0x102, 100100, 70, -104800, 270)
    SetChrPos(0xF, 96800, 70, -102650, 90)
    SetChrPos(0x105, 96800, 70, -104800, 90)
    SetChrPos(0x103, 102350, 0, -104050, 270)
    SetChrPos(0x104, 102060, 0, -102890, 270)
    SetChrPos(0x9, 101700, 0, -105600, 315)
    SetChrPos(0x109, 96950, 0, -100550, 135)
    SetChrPos(0xC, 96050, 0, -100600, 135)
    SetChrPos(0x106, 101350, 0, -100350, 225)
    SetChrPos(0x13, 99400, 0, -98000, 180)
    SetChrPos(0x8, 97150, 0, -106150, 0)
    OP_68(98500, 1250, -103350, 0)
    OP_6D(0x2C, 0xE, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x3B92, 0x0)
    OP_6C(0x3F7A, 0xBB8)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xF,
        (
            "#02101F#6P那么，议长，\x01",
            "您已经下定决心了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x12,
        (
            "嗯……在场众人之中，\x01",
            "恐怕也有持反对意见者。\x02\x03",
            "但是如果不迈出这一步，\x01",
            "我们就无法继续前进。\x02\x03",
            "就算要失去这短暂的秩序\x01",
            "与霸权，也必须这么做。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x102,
        "#00108F#11P是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6P『克洛斯贝尔独立无效宣言』吗……\x02\x03",
            "#10400F这确实是只有前政府代表之一的\x01",
            "议长阁下才能祭出的王牌呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10701F#5P不过，具体该用\x01",
            "什么方式来发表宣言呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#6P如果无法传达给市民与国防军，\x01",
            "是不会有什么效果的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11P关于这个问题，\x01",
            "约纳好像有个主意。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99360, 1250, -104040, 1000)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0xF, 0x2)
    SetChrSubChip(0x12, 0x1)
    SetChrSubChip(0x105, 0x0)

    def lambda_7184():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7184)
    Sleep(50)

    def lambda_7194():
        TurnDirection(0x106, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_7194)
    Sleep(50)

    def lambda_71A4():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_71A4)
    Sleep(50)

    def lambda_71B4():
        TurnDirection(0xC, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_71B4)
    Sleep(50)

    def lambda_71C4():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_71C4)
    Sleep(50)

    def lambda_71D4():
        TurnDirection(0x13, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_71D4)
    WaitChrThread(0x104, 0x0)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "嗯，在唐古拉姆丘陵上，\x01",
            "有一台用于连接列曼自治州和克洛斯贝尔\x01",
            "导力网络的实验用无线信号增幅器。\x02\x03",
            "如果从那里趁虚而入，应该可以\x01",
            "顺利入侵克洛斯贝尔的导力网络。\x02\x03",
            "只要想想办法，大概能\x01",
            "维持十分钟左右吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x104,
        (
            "#00305F#5P虽然不是很明白……\x01",
            "但关键就是能控制\x01",
            "那些街头的显示屏吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#11P是的，而且还能连接上\x01",
            "国防军方面的所有终端。\x02\x03",
            "#00202F如此一来，应该就可以达成\x01",
            "索妮亚司令提出的条件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#6P只要能让大家对总统一派的正当性\x01",
            "产生质疑，国防军就会暂时按兵不动……\x02\x03",
            "#12102F那样的话，接下来的行动就会方便多了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(98990, 1250, -103480, 1000)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(50)
    SetChrSubChip(0xF, 0x0)
    Sleep(50)
    SetChrSubChip(0x12, 0x0)

    def lambda_74D3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_74D3)
    Sleep(50)

    def lambda_74E3():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_74E3)
    Sleep(50)

    def lambda_74F3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_74F3)
    Sleep(50)

    def lambda_7503():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7503)
    Sleep(50)

    def lambda_7513():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_7513)
    Sleep(50)

    def lambda_7523():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7523)
    WaitChrThread(0x104, 0x0)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00108F#11P罗伊德……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5P唔……罗伊德。\x02\x03",
            "#02500F这个『独立无效宣言』\x01",
            "只是我个人的想法而已。\x02\x03",
            "如果身为队长的你持反对意见，\x01",
            "我会改变计划的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        (
            "#00000F#11P不，拜托您了。\x02\x03",
            "#00003F在过去……\x01",
            "迪塔先生还是ＩＢＣ总裁的时候，\x01",
            "他曾对我们说过关于『正义』的观点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#11P啊……\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    OP_5B(0x50, 0x1E, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "归根结底，人类终究还是一种\x01",
            "会去追逐正义的生物。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "因为所谓的『正义』，\x01",
            "就是使人信赖社会的『基础』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    Sleep(300)
    OP_5B(0xA, 0x64, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "腐败的政治，以及黑手党问题……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "虽然警察不会对其进行整治，\x01",
            "但由于经济十分繁荣发达，\x01",
            "所以多数市民并不会为生计发愁。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "然而，即使是在这种环境下，\x01",
            "人们还是会以各种方式\x01",
            "来追寻所谓的『正义』。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "因为不管是以何种形式，人们始终\x01",
            "需要可以对社会产生信赖的『安全感』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    Sleep(300)
    OP_5B(0xFA, 0x32, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "正因如此，\x01",
            "我才对你们的表现十分期待。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "你们要用自己的方式，\x01",
            "去追求自己心中的『正义』……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "然后以清晰可见的形式，将你们追寻正义的\x01",
            "身姿展现给市民们。我认为，这是非常重要的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_C9(0x1, 0x800)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    VolumeBGM(0x64, 0x3E8)

    ChrTalk(
        0x12,
        "#02505F#5P迪塔曾说过那种话啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11P是啊，他确实说过。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#11P离那个时候还不足一年，\x01",
            "但却觉得十分怀念呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P总裁当时所说的那番话……\x02\x03",
            "#00008F究竟是发自真心，\x01",
            "还是单纯地装装样子？\x01",
            "老实说，我无法断言……\x02\x03",
            "#00001F但不管怎么说，他那番话\x01",
            "都深深触动了我们的心灵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11P是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02103F#6P嗯，确实是很有深意的一番话呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，所以……\x01",
            "我想用他当时说的那一番话\x01",
            "来反问他自己。\x02\x03",
            "#00003F这是为了我们，也是为了他。\x02\x03",
            "#00001F更重要的是，要让市民与国防军\x01",
            "的士兵们得到一个重新思考的契机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F#5P我明白了。\x02\x03",
            "#02500F我会以自己的形式，将刚刚那些话\x01",
            "简单易懂地融入到宣言稿之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#11P好的，拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10402F#6P那就这么决定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02104F#6P接下来，就认真商讨\x01",
            "一下具体步骤吧！\x02\x03",
            "#02110F约纳、芙兰！技术方面的\x01",
            "支援工作就交给你们啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909F#5P是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#02302F#11P嘿，包在我身上。\x02",
    )

    CloseMessageWindow()
    OP_6C(0x416E, 0x5DC)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "就这样，众人开始商讨麦克道尔议长\x01",
            "的『克洛斯贝尔独立无效宣言』的\x01",
            "具体发表步骤。\x02\x03",
            "而约纳与芙兰则专注于\x01",
            "入侵导力网络的\x01",
            "专业技术问题……\x02\x03",
            "接下来，就只剩下决定发表时机了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e4400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_6BF8 end

    def Function_23_7D9E(): pass

    label("Function_23_7D9E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F（通过实验用的无线信号增幅器\x01",
            "  入侵克洛斯贝尔的导力网络，\x01",
            "  并发表『克洛斯贝尔独立无效宣言』。）\x02\x03",
            "#00001F（一旦开始，就不能再回头了……\x01",
            "  做好心理准备了吗？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情】\x01",                # 0
            "【前往无线信号增幅器地点】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7EB0"),
        (1, "loc_7EBE"),
        (SWITCH_DEFAULT, "loc_80C2"),
    )


    label("loc_7EB0")

    FadeToBright(0, 0)
    Jump("loc_80C2")

    label("loc_7EBE")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(498, 500, 80)
    Sleep(500)
    SetEventSkip(0x0, "loc_7F7F")
    FadeToBright(1000, 0)
    ClearMapFlags(0x1)
    OP_C9(0x0, 0x20)
    OP_78(0x0, 0x1E)
    SetChrPos(0x1E, -1000000, 0, 700000, 0)

    def lambda_7F0C():
        OP_96(0x1E, 0xFFF0BDC0, 0x0, 0x16E360, 0x1D4C0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7F0C)
    OP_F0(0x1, 0x7D0)
    OP_68(-1000000, 0, 800000, 0)
    OP_6D(0x1E, 0xFFF9, 0x0, 0x0)
    OP_6D(0x14, 0xFFF9, 0x0, 0xBB8)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x1B198, 0x0)
    Sleep(300)
    Sound(499, 0, 100, 0)
    Sleep(1700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    SetEventSkip(0x1, 0x0)

    label("loc_7F7F")

    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FBF")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_80AF")

    label("loc_7FBF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FE2")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_80AF")

    label("loc_7FE2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8005")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_80AF")

    label("loc_8005")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8028")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_80AF")

    label("loc_8028")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804B")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_80AF")

    label("loc_804B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_806E")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_80AF")

    label("loc_806E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8091")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_80AF")

    label("loc_8091")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80AF")
    SetScenarioFlags(0x3C, 7)

    label("loc_80AF")

    PartySelect(0x2)
    SetScenarioFlags(0x23, 0)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Jump("loc_80C2")

    label("loc_80C2")

    Return()

    # Function_23_7D9E end

    def Function_24_80C3(): pass

    label("Function_24_80C3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    SoundLoad(952)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80F1")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_80F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8104")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_8104")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8117")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_8117")

    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A2(0xA, 0x80)
    OP_A3(0xC, 0x80)
    OP_A3(0xF, 0x80)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_A3(0x9, 0x80)
    OP_A2(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    OP_A3(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    OP_A3(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    OP_A2(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    OP_73(0x1, 0x4)
    OP_71(0x1, 0x1E, 0x1E, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x12, 0, 500, 2400, 0)
    SetChrPos(0xF, 900, 500, 1750, 0)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, 2150, -1500, 7300, 90)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 750, 250, 400, 0)
    SetChrPos(0x106, -950, 0, -1650, 0)
    OP_68(0, 3300, 2000, 0)
    OP_68(0, 1500, 2000, 3500)
    OP_6D(0x2D, 0x14, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5208, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#01901F#5P摄影机已经准备好了！\x01",
            "声音测试也已完成！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5P飞艇已经抵达无线信号增幅器的正上方……\x02\x03",
            "随时都可以开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109F#11P很好，很好。\x02\x03",
            "#02100F议长，准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#02501F#5P嗯，开始吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0xBB8)
    OP_68(-2830, -750, 6760, 2000)
    OP_6D(0x2D, 0x1E, 0x0, 0x7D0)
    OP_6E(0x1F4, 0x7D0)
    OP_6C(0x4268, 0x7D0)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#02304F#11P嘿嘿，那就开始了哦。\x02\x03",
            "#02301F现在就要通过无线信号增幅器\x01",
            "来入侵导力网络。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70352", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(952, 2, 80, 0)
    BeginChrThread(0x1F, 1, 0, 25)
    OP_6C(0x3E80, 0xBB8)
    BeginChrThread(0x9, 0, 0, 26)
    Sleep(1000)
    StopSound(498, 1000, 100)
    StopSound(952, 1000, 70)
    EndChrThread(0x1F, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x0)
    OP_24(0x3B8)
    SetScenarioFlags(0x22, 1)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_80C3 end

    def Function_25_8487(): pass

    label("Function_25_8487")

    Sound(938, 0, 60, 0)
    Sound(836, 0, 60, 0)
    Sleep(800)
    Sound(836, 0, 60, 0)
    Return()

    # Function_25_8487 end

    def Function_26_849D(): pass

    label("Function_26_849D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_84B5")
    OP_A1(0xFE, 0x7D0, 0x2, 0x0, 0x1)
    Jump("Function_26_849D")

    label("loc_84B5")

    Return()

    # Function_26_849D end

    def Function_27_84B6(): pass

    label("Function_27_84B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    LoadChrToIndex("chr/ch05802.itc", 0x1E)
    LoadChrToIndex("apl/ch51770.itc", 0x1F)
    LoadChrToIndex("apl/ch51714.itc", 0x20)
    SoundLoad(952)
    SoundLoad(938)
    OP_A3(0xC, 0x80)
    OP_A3(0xF, 0x80)
    OP_A3(0x13, 0x80)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A2(0xA, 0x80)
    OP_A3(0xC, 0x80)
    OP_A3(0xF, 0x80)
    OP_A3(0x13, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_A3(0x9, 0x80)
    OP_A2(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x1)
    OP_A3(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    OP_A3(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x4)
    OP_A2(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x8)
    SetChrSubChip(0xF, 0x0)
    OP_73(0x1, 0x4)
    OP_71(0x1, 0x1E, 0x1E, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x12, 0, 500, 2400, 0)
    SetChrPos(0xF, 900, 500, 1750, 0)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, 2150, -1500, 7300, 90)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 750, 250, 400, 0)
    SetChrPos(0x106, -950, 0, -1650, 0)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_68(-3150, -750, 7150, 0)
    OP_6D(0x2D, 0x1E, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x36B0, 0x0)
    OP_6C(0x4268, 0x1388)
    BeginChrThread(0x9, 0, 0, 26)
    Sound(952, 2, 70, 0)
    BeginChrThread(0x1F, 1, 0, 28)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x9, 0x0)
    SetChrSubChip(0x9, 0x1)
    EndChrThread(0x1F, 0x1)
    StopSound(938, 1000, 100)
    StopSound(952, 1000, 70)
    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)

    ChrTalk(
        0x9,
        (
            "#02302F#11P成功了！\x01",
            "已经掌控了通讯机能！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1500, 2000, 2000)
    OP_6D(0x2D, 0x19, 0x0, 0x7D0)
    OP_6E(0x1F4, 0x7D0)
    OP_6C(0x4A38, 0x7D0)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#01901F#5P马上切换镜头！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02110F#11P嗯，好的！\x02",
    )

    CloseMessageWindow()
    OP_21(0x1770)
    OP_68(0, 1800, 2000, 2000)
    OP_6D(0x2D, 0x14, 0x0, 0x7D0)
    OP_6F(0x79)
    Fade(250)
    OP_A2(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x20)
    OP_A0(0xF, 1500, 0x0, 0x2)
    OP_0D()
    OP_70(0x1, 0x21)
    Sound(72, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "大家好。\x02\x03",
            "我是隶属于克洛斯贝尔通讯社的\x01",
            "新闻记者——格蕾丝·琳。\x02\x03",
            "慎重起见，我事先说明一点，\x01",
            "克洛斯贝尔通讯社对本次事件\x01",
            "毫不知情。\x02\x03",
            "此报道只是我的个人行为，\x01",
            "还请各位理解。\x02\x03",
            "……那么，接下来，\x01",
            "我要向各位介绍一位人物。\x02\x03",
            "他就是『克洛斯贝尔自治州』代表，\x01",
            "亨利·麦克道尔议长阁下！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_70(0x1, 0x22)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70566", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x12,
        (
            "克洛斯贝尔的各位市民，\x01",
            "以及此时正在观看本影像\x01",
            "的所有人，大家好。\x02\x03",
            "我是『克洛斯贝尔自治州议会』的议长，\x01",
            "亨利·麦克道尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_6C(0x5208, 0xBB8)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3B8)
    OP_24(0x3AA)
    SetScenarioFlags(0x23, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_84B6 end

    def Function_28_8AD9(): pass

    label("Function_28_8AD9")

    Sound(938, 2, 70, 0)

    label("loc_8ADF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AF8")
    Sound(836, 0, 60, 0)
    Sleep(700)
    Jump("loc_8ADF")

    label("loc_8AF8")

    Return()

    # Function_28_8AD9 end

    def Function_29_8AF9(): pass

    label("Function_29_8AF9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A2(0xA, 0x80)
    OP_A3(0xC, 0x80)
    OP_A3(0x8, 0x80)
    OP_A3(0x13, 0x80)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_73(0x1, 0x4)
    OP_70(0x1, 0x23)
    Sleep(1500)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            "#00005F您已经知道消除\x01",
            "『结界』的方法了！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    PlayBGM("ed70580", 0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    OP_68(660, 700, 3830, 0)
    OP_6D(0x2C, 0x12, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5172, 0x0)
    OP_6C(0x555A, 0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    OP_5B(0x64, 0x46, 0xFFFF, 0xFFFF)
    SetChrName("约鲁古老人")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "嗯，还有如何抑制\x01",
            "那三台『神机』的方法。\x02\x03",
            "总之，关键就是那些『大钟』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N『大钟』……\x01",
            "是塔和僧院中的大钟吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10401F#6P就是它强化了\x01",
            "结界和那些智能兵器吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x50, 0x46, 0xFFFF, 0xFFFF)
    SetChrName("约鲁古老人")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "不，强化它们的终究\x01",
            "还是『至宝』的力量。\x02\x03",
            "但目前来看，『至宝』的力量\x01",
            "恐怕还不完全。\x02\x03",
            "为了在大范围内显现那些\x01",
            "超乎想象的『奇迹』，\x01",
            "似乎还是要依靠特殊的『力场』。\x02\x03",
            "也就是通过大钟的共鸣\x01",
            "而产生的『力场』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#10708F#12P那些大钟居然还有这种作用……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#12P那、那么，只要让大钟\x01",
            "停止共鸣，就可以……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x69, 0x46, 0xFFFF, 0xFFFF)
    SetChrName("约鲁古老人")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "是的，说不定就能消除那个\x01",
            "巨大的结界……\x02\x03",
            "而且应该还能使那台毁灭了\x01",
            "卡雷利亚要塞的白色『神机』\x01",
            "力量减弱。\x02\x03",
            "不过，我也不敢断言。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x104,
        (
            "#00305F#12P即使如此，也很有\x01",
            "尝试的价值啊……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5P唔……那个结界与白色智能\x01",
            "兵器确实是最大的障碍。\x02\x03",
            "只要那二者还在，\x01",
            "我们就永远不可能\x01",
            "解放克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12P既然如此……\x01",
            "我们的目标就是『塔』与『僧院』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P嗯，之前被运到古战场的大钟，\x01",
            "如今似乎已经被运回到市内的中央广场了。\x02\x03",
            "#00000F虽然我们动不了市内的大钟，\x01",
            "但却可以阻止『塔』与『僧院』的\x01",
            "大钟继续共鸣……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x78, 0x46, 0xFFFF, 0xFFFF)
    SetChrName("约鲁古老人")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "嗯，但那两个地方都有\x01",
            "『结社』的人在把守。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#12P说起来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F#12P#N……确实如此呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0x6E, 0x46, 0xFFFF, 0xFFFF)
    SetChrName("约鲁古老人")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "看守『月之僧院』的人\x01",
            "似乎是肯帕雷拉。\x02\x03",
            "而守卫着『星见之塔』的……\x01",
            "则是阿瑞安赫德。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    ChrTalk(
        0x106,
        "#10701F#12P……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#12P那个超乎想象的女骑士吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P……老实说，这可真是难办啊。\x02\x03",
            "#10408F『小丑』那边，\x01",
            "说不定还能想办法攻破……\x02\x03",
            "#10401F但『钢之圣女』那样的对手……\x01",
            "就只能用坚不可摧来形容了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P……真的有那么强吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P嗯，虽然『结社』中\x01",
            "高手如云……\x02\x03",
            "但其他达人完全\x01",
            "无法同她相提并论。\x02\x03",
            "#10401F甚至可以这样说──\x01",
            "以人类之身，绝不可能战胜她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#12P居、居然有那么强吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P瓦吉，你在教会中\x01",
            "也是被称作『守护骑士』\x01",
            "的特别人物……\x02\x03",
            "#00101F连你也无法与她对抗吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P嗯，就算动用『圣痕』的力量，\x01",
            "在她那铠甲面前，大概也会徒劳无功。\x02\x03",
            "#10408F能与她抗衡的人，\x01",
            "恐怕也只有我们的总长了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F#5P但整个大陆都已陷入如此状况……\x02\x03",
            "再怎么说，也不可能让\x01",
            "瑟尔纳特总长来这里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5P呼，是啊。\x02\x03",
            "#10408F……在这种时候，如果有凯文在，\x01",
            "说不定还能想点办法。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P没时间继续烦恼了。\x02\x03",
            "#00001F如今终于看到了一丝\x01",
            "打破现状的希望。\x02\x03",
            "我们自然应该勇敢地\x01",
            "踏出这一步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#12P没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#12P#N我也这么想。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10701F#12P无论多强的高手……\x01",
            "也不可能完全没有\x01",
            "任何弱点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#5P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#12P说的对……\x01",
            "如果在这种地方踌躇不前，\x01",
            "我们永远都无法见到贝尔他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#12P出发吧！\x01",
            "目标是『塔』和『僧院』！\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x69, 0x46, 0xFFFF, 0xFFFF)
    SetChrName("约鲁古老人")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "总之，祝你们幸运吧。\x02\x03",
            "不妨把阿瑞安赫德所在\x01",
            "的『塔』留在后面。\x02\x03",
            "别说她本人了，光是她手下那些\x01",
            "女战士就能让你们吃尽苦头。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_6C(0x5942, 0x7D0)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "如果要前往『月之僧院』，可以从\x01",
            "玛因兹山道途中的隧道岔路口过去。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    PartySelect(0x1)
    OP_A3(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 2)
    OP_29(0xAF, 0x1, 0x15)
    OP_29(0xAF, 0x4, 0x10)
    OP_29(0xB0, 0x4, 0x2)
    OP_29(0xB0, 0x1, 0x0)
    PlayBGM("ed70570", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 2, 100, 0)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_29_8AF9 end

    def Function_30_9A8E(): pass

    label("Function_30_9A8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    PartySelect(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AB5")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_9AB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AC8")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_9AC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9ADB")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_9ADB")

    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A3(0xC, 0x80)
    OP_A3(0x8, 0x80)
    OP_A3(0x12, 0x80)
    OP_A3(0xF, 0x80)
    OP_A3(0x9, 0x80)
    OP_A3(0x13, 0x80)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_4B(0xF, 0xFF)
    OP_A3(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x4)
    OP_A2(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0xB)
    SetChrSubChip(0x12, 0x0)
    OP_73(0x1, 0x4)
    OP_70(0x1, 0x26)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x12, -3300, 0, 250, 45)
    SetChrPos(0xF, -3800, 0, -1000, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    OP_68(410, 800, 4070, 0)
    OP_6D(0x2C, 0x10, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x57E4, 0x0)
    OP_6C(0x53FC, 0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00105F#12P好、好厉害……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12P那个葱头神父\x01",
            "所说的帮手，\x01",
            "原来就是艾丝蒂尔他们啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5P嗯，似乎是遵从了他们本人的意愿，\x01",
            "特地把他们从利贝尔带了过来。\x02\x03",
            "#10402F话说回来，这可是个好机会啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12107F#5P嗯，我立刻解除光学迷彩，\x01",
            "降落在南出口处……！\x02\x03",
            "你们就从船底的升降口出去吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12P明白了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12P#N那就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_9DF0():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_9DF0)
    Sleep(50)

    def lambda_9E00():
        TurnDirection(0xF, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_9E00)
    Sleep(50)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0xF, 0x0)
    Sleep(150)

    ChrTalk(
        0x12,
        "#02507F#6P#N愿女神保佑各位。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xC, 0x2)
    Sleep(50)

    ChrTalk(
        0xC,
        "#01901F#5P大家要多加小心！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6P#N我会在上空\x01",
            "用心记录取材的！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x9, 0x1)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#02302F#5P我也会通过导力网络\x01",
            "来支援你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x55F0, 0x5DC)
    StopSound(498, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A3(0x105, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_9A8E end

    def Function_31_9EF7(): pass

    label("Function_31_9EF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11402.itc", 0x1E)
    LoadChrToIndex("apl/ch51025.itc", 0x1F)
    LoadChrToIndex("chr/ch11502.itc", 0x20)
    LoadEffect(0x0, "event/ev10037.eff")
    LoadEffect(0x1, "event/ev17103.eff")
    LoadEffect(0x2, "event/ev17104.eff")
    LoadEffect(0x3, "event/ev17105.eff")
    SoundLoad(825)
    OP_A2(0x8, 0x80)
    OP_A2(0xC, 0x80)
    OP_A2(0x9, 0x80)
    OP_A2(0xF, 0x80)
    OP_A2(0x0, 0x80)
    OP_A2(0x1, 0x80)
    OP_A2(0x2, 0x80)
    OP_A2(0x3, 0x80)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    OP_A3(0x1A, 0x80)
    OP_A2(0x1A, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    OP_A3(0x19, 0x80)
    OP_A2(0x19, 0x8000)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    OP_A3(0x17, 0x80)
    OP_A2(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0xF)
    SetChrSubChip(0x18, 0x0)
    OP_A3(0x18, 0x80)
    OP_A2(0x18, 0x8000)
    OP_76(0x6, "base02", 0x2, "sky_ani2")
    OP_76(0x6, "base03", 0x2, "sky_ani2")
    SetChrPos(0x1A, 0, 500, 2400, 0)
    SetChrPos(0x19, -3100, -1350, 7100, 315)
    SetChrPos(0x17, 3100, -1350, 7100, 45)
    SetChrPos(0x18, 0, -1350, 6700, 0)
    OP_68(-1590, 1500, 4910, 0)
    OP_6D(0x27, 0x15, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5172, 0x0)
    OP_6C(0x4D8A, 0x9C4)
    BeginChrThread(0x17, 0, 0, 32)
    BeginChrThread(0x17, 1, 0, 34)
    BeginChrThread(0x1F, 2, 0, 33)
    Sound(825, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x17,
        "#5P镜面装甲受损７０％！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P已、已经撑不住了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13801F#11P敌机进一步加速了！\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        (
            "#04303F#11P啧……不妙了啊。\x02\x03",
            "#04308F事到如今……\x01",
            "也只能使出那个了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x19, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x19, 0x1)
    Sleep(50)
    SetChrSubChip(0x18, 0x1)
    Sleep(50)
    SetChrSubChip(0x17, 0x2)

    ChrTalk(
        0x17,
        "#5P格拉汉姆大人……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#11P难道要……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#13807F#5P等一下……！\x01",
            "这也太突然了！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        (
            "#04304F#11P如果不在这种时候加把劲，\x01",
            "我就没脸使用来自姐姐的诨名了。\x02\x03",
            "#04300F各位，请支援我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#5P……明白了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x18, 0x0)
    Sleep(50)
    SetChrSubChip(0x17, 0x0)
    Sleep(300)
    Sound(1002, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1800, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1300, -200, 4500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x18,
        "#11P『圣痕模式』启动……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        "#13808F#5P凯文……\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        (
            "#04304F#11P莉丝，别担心。\x02\x03",
            "#04302F做好支援我的工作……\x01",
            "捕捉敌机位置的任务就交给你了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#13801F#5P……我知道了！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x19, 0x0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrPos(0x1A, 0, 500, 3300, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    BeginChrThread(0x1A, 0, 0, 35)
    OP_68(-1560, 1500, 5150, 800)
    OP_6F(0x79)
    OP_6C(0x4588, 0x61A8)
    Sleep(500)

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        "#04303F#11P#3C#40W#19A『于深渊中闪耀光芒的苍之刻印啊……』\x02",
    )

    CloseMessageWindow()
    Sound(895, 0, 100, 0)
    BeginChrThread(0x1F, 0, 0, 36)
    PlayEffect(0x0, 0xFF, 0x1A, 0x3, 0, 400, -100, 0, 0, 0, 650, 650, 650, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        "#04303F#11P#3C#40W#21A『化为照耀炼狱的光柱，冲天而起吧……』\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    BeginChrThread(0x1F, 1, 0, 37)
    PlayEffect(0x3, 0xFF, 0x1A, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0x17,
        "#5P收束『梅尔卡瓦』的所有导力！\x05\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x18,
        (
            "#11P已识别『圣痕』模式！\x01",
            "开始向外部展开！\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x19,
        (
            "#13807F#11P敌机已变形！\x01",
            "它展开主炮，向我们冲来了！\x05\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        (
            "#04301F#11P#40W#18A守护骑士第五位，\x01",
            "『千之护手』在此下令……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Fade(500)
    EndChrThread(0x1A, 0x0)
    SetChrSubChip(0x1A, 0x5)
    OP_6C(0x41A0, 0x320)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0x1A,
        "守护骑士凯文",
        "#04307F#11P#4S#15A『圣痕炮』星球之源灭——发射！\x02",
    )

    CloseMessageWindow()
    OP_6C(0x4D58, 0xBB8)
    Sound(829, 0, 100, 0)
    FadeToDark(3000, 16777215, -1)
    Sleep(1500)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1F, 0x2)
    OP_0D()
    StopSound(825, 1000, 70)
    StopSound(498, 1000, 100)
    Sleep(1000)
    SetScenarioFlags(0x23, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_9EF7 end

    def Function_32_A763(): pass

    label("Function_32_A763")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A791")
    OP_7D(0xFF, 0x50, 0x50, 0x0, 0x1F4)
    Sleep(100)
    Sleep(700)
    OP_7D(0xFF, 0xC8, 0xC8, 0x0, 0x1F4)
    Sleep(600)
    Sleep(100)
    Jump("Function_32_A763")

    label("loc_A791")

    Return()

    # Function_32_A763 end

    def Function_33_A792(): pass

    label("Function_33_A792")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7B4")
    Sleep(100)
    Sound(840, 0, 70, 0)
    Sleep(700)
    Sleep(600)
    Sleep(100)
    Jump("Function_33_A792")

    label("loc_A7B4")

    Return()

    # Function_33_A792 end

    def Function_34_A7B5(): pass

    label("Function_34_A7B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7D9")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_34_A7B5")

    label("loc_A7D9")

    Return()

    # Function_34_A7B5 end

    def Function_35_A7DA(): pass

    label("Function_35_A7DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A7F1")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("Function_35_A7DA")

    label("loc_A7F1")

    Return()

    # Function_35_A7DA end

    def Function_36_A7F2(): pass

    label("Function_36_A7F2")

    Sound(934, 0, 50, 0)
    Sleep(1500)

    label("loc_A7FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A814")
    Sound(934, 0, 30, 0)
    Sleep(1500)
    Jump("loc_A7FB")

    label("loc_A814")

    Return()

    # Function_36_A7F2 end

    def Function_37_A815(): pass

    label("Function_37_A815")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A82E")
    Sound(929, 0, 50, 0)
    Sleep(2200)
    Jump("Function_37_A815")

    label("loc_A82E")

    Return()

    # Function_37_A815 end

    def Function_38_A82F(): pass

    label("Function_38_A82F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A854")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_A854")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A867")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_A867")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A87A")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_A87A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A88D")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_A88D")

    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A3(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    OP_A3(0xC, 0x80)
    OP_A3(0x8, 0x80)
    OP_A3(0x13, 0x80)
    OP_A3(0xF, 0x80)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_4B(0xF, 0xFF)
    OP_73(0x1, 0x4)
    OP_72(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x27)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(0, 700, 3000, 0)
    OP_6D(0x32, 0x14, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x4A38, 0x0)
    OP_6C(0x4E20, 0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#02310F#5P话说回来，\x01",
            "真是出现了惊人的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01908F#5P那真的是因小琪雅\x01",
            "的力量而出现的吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P嗯……\x01",
            "应该没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C『碧之大树』……\x01",
            "那就是人工至宝的完成形态啊。\x02\x03",
            "#01201F真没想到，凭着人类之子的执念，\x01",
            "竟能做到这种地步……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#5P连你也不知道\x01",
            "那棵大树究竟拥有\x01",
            "怎样的力量吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C……嗯。\x01",
            "但可以从那幽蓝色的光芒中\x01",
            "感觉到它绝非寻常之物。\x02\x03",
            "#01200F可以说那棵大树汇集了全部七耀之力……\x01",
            "特别是『幻』、『时』、『空』\x01",
            "三种上级属性的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6P『零之至宝』本是\x01",
            "库罗伊斯家族为了重现\x01",
            "『幻之至宝』而创造的……\x02\x03",
            "#00108F难道在创造的过程中，令至宝\x01",
            "同时具备了『时』与『空』的力量……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#11P#3C唔，老实说，\x01",
            "连我都无法估量这东西\x01",
            "究竟拥有多么强大的力量。\x02\x03",
            "#01201F或者也可以这样说，\x01",
            "『没有它无法\x01",
            "　实现的事情』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#12P这真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5P可以媲美女神的力量吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#11P无论怎样也好……\x01",
            "我们该做的事情都不会有任何改变。\x02\x03",
            "#00008F亚里欧斯先生、玛丽亚贝尔小姐，\x01",
            "还有伊安律师等人……\x02\x03",
            "#00013F我们一定要确定他们的真正目的，\x01",
            "并亲手夺回琪雅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#12P……是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02110F#6P哎呀呀～该怎么说才好呢，\x01",
            "真是让我激动得浑身发抖啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)

    def lambda_AEC2():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_AEC2)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xC, 0x2)

    def lambda_AED7():
        TurnDirection(0x101, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AED7)
    Sleep(50)

    def lambda_AEE7():
        TurnDirection(0x102, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEE7)
    Sleep(50)

    def lambda_AEF7():
        TurnDirection(0x103, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AEF7)
    Sleep(50)

    def lambda_AF07():
        TurnDirection(0x104, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF07)
    Sleep(50)

    def lambda_AF17():
        TurnDirection(0x109, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AF17)
    Sleep(50)

    def lambda_AF27():
        TurnDirection(0x106, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_AF27)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x103, 0x0)
    WaitChrThread(0x104, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x106, 0x0)
    OP_A2(0x13, 0x20)

    def lambda_AF51():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_AF51)
    OP_A3(0x13, 0x20)

    ChrTalk(
        0x10A,
        (
            "#00606F#11P……格蕾丝，\x01",
            "你为何会在这里？\x02\x03",
            "#00601F你不是应该和麦克道尔议长\x01",
            "一起离开这艘船了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10A, 500)

    ChrTalk(
        0xF,
        (
            "#02103F#5P真啰嗦～\x01",
            "我的去留由我自己决定！\x02\x03",
            "#02100F而且，克洛斯贝尔的市民们\x01",
            "一定也很想知道此次事件的详细情况。\x02\x03",
            "#02109F相关的跟踪报道工作\x01",
            "就交给我好啦⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#11P这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#11P让人越来越不安了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11P总之，在潜入大树之前，\x01",
            "我们还是做足准备为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#12P是啊……\x01",
            "毕竟我们完全不知道接下来\x01",
            "将要面对什么样的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P各地的战斗都已平息，\x01",
            "如今已经可以让梅尔卡瓦降落在\x01",
            "克洛斯贝尔的任意地点了。\x02\x03",
            "#10400F如果有需要，就直接下指示吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        "#00000F#11P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_6C(0x4F1A, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(0x1)
    OP_A3(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A7, 1)
    OP_29(0xB2, 0x4, 0x2)
    OP_29(0xB2, 0x1, 0x0)
    SetScenarioFlags(0x34, 6)
    SetScenarioFlags(0x37, 6)
    SetScenarioFlags(0x20, 5)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed70150", "ed70563")
    ReplaceBGM("ed70101", "ed70563")
    ReplaceBGM("ed70116", "ed70563")
    ReplaceBGM("ed70117", "ed70563")
    ReplaceBGM("ed70111", "ed70563")
    ReplaceBGM("ed70113", "ed70563")
    Sleep(500)
    NewScene("e3020", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_38_A82F end

    def Function_39_B304(): pass

    label("Function_39_B304")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()

    AnonymousTalk(
        0x101,
        (
            "#00003F（『碧之大树』……\x01",
            "  琪雅，还有一切事情的\x01",
            "  真相都在那里等着我们……）\x02\x03",
            "#00013F（做好准备了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "【还有其它事情】\x01",          # 0
            "【前往『碧之大树』】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B3D1"),
        (1, "loc_B3DF"),
        (SWITCH_DEFAULT, "loc_B539"),
    )


    label("loc_B3D1")

    FadeToBright(0, 0)
    Jump("loc_B539")

    label("loc_B3DF")

    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000)
    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B430")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_B520")

    label("loc_B430")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B453")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_B520")

    label("loc_B453")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B476")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_B520")

    label("loc_B476")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B499")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_B520")

    label("loc_B499")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4BC")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_B520")

    label("loc_B4BC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4DF")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_B520")

    label("loc_B4DF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B502")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_B520")

    label("loc_B502")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B520")
    SetScenarioFlags(0x3C, 7)

    label("loc_B520")

    PartySelect(0x2)
    OP_21(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x23, 7)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Jump("loc_B539")

    label("loc_B539")

    Return()

    # Function_39_B304 end

    def Function_40_B53A(): pass

    label("Function_40_B53A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    SoundLoad(498)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B562")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_B562")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B575")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_B575")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B588")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_B588")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B59B")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_B59B")

    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A3(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    OP_A2(0xB, 0x80)
    OP_A3(0xC, 0x80)
    OP_A3(0x8, 0x80)
    OP_A3(0x13, 0x80)
    OP_A3(0xF, 0x80)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_73(0x1, 0x4)
    OP_72(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x28)
    OP_73(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_76(0x6, "base02", 0x2, "sky_ani2")
    OP_76(0x6, "base03", 0x2, "sky_ani2")
    BeginChrThread(0x101, 3, 0, 41)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(370, 700, 3790, 0)
    OP_6D(0x28, 0x13, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x510E, 0x0)
    OP_6C(0x4E20, 0x5DC)
    Sound(498, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#01901F#5P……在五点钟方向发现敌舰！\x02\x03",
            "那是赤色星座的\x01",
            "『贝奥武夫号』！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12P出现了吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#12P#N那就是『赤色星座』正在\x01",
            "使用的强袭型战舰吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#12P嗯，我还在团里的时候，\x01",
            "他们就计划要正式运用\x01",
            "强袭型战舰……\x02\x03",
            "#00311F没想到现在已经能\x01",
            "操控得如此纯熟了……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P也许是库罗伊斯家族为了此次计划，\x01",
            "给他们提供了资金……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#11P看上去，似乎还融入了\x01",
            "『结社』的技术……\x02\x03",
            "#10408F阿巴斯，能甩开它吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100F#5P我尽力而为。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02302F#5P嘿，那东西看起来又大又笨重，\x01",
            "要比速度的话，我们应该不会输吧？\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(499, 0, 80, 0)
    OP_76(0x6, "base02", 0x2, "sky_ani3")
    OP_76(0x6, "base03", 0x2, "sky_ani3")
    OP_68(370, 700, 790, 1000)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x24, 0)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_B53A end

    def Function_41_BA02(): pass

    label("Function_41_BA02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA26")
    OP_82(0x2, 0x2, 0xBB8, 0x1388)
    Sleep(5000)
    Jump("Function_41_BA02")

    label("loc_BA26")

    Return()

    # Function_41_BA02 end

    def Function_42_BA27(): pass

    label("Function_42_BA27")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    LoadChrToIndex("apl/ch51217.itc", 0x20)
    LoadChrToIndex("apl/ch51218.itc", 0x21)
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    LoadChrToIndex("apl/ch51220.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51224.itc", 0x25)
    LoadChrToIndex("apl/ch51774.itc", 0x26)
    LoadEffect(0x0, "event/ev17053.eff")
    LoadEffect(0x1, "event/ev17021.eff")
    LoadEffect(0x2, "event/ev17057.eff")
    SoundLoad(498)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A3(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    OP_A2(0xB, 0x80)
    OP_A3(0xC, 0x80)
    OP_A3(0x8, 0x80)
    OP_A3(0x13, 0x80)
    OP_A3(0xF, 0x80)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    OP_A3(0x1E, 0x80)
    OP_A2(0x1E, 0x8)
    OP_73(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_F3(0x186A0)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    SetChrPos(0x1E, 17000, -750, 13000, 0)
    OP_68(370, 700, 3790, 0)
    OP_6D(0x28, 0x13, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5014, 0x0)
    OP_6C(0x4E20, 0x3E8)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x101, 1, 0, 34)
    BeginChrThread(0x1F, 2, 0, 33)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(498, 2, 100, 0)
    BeginChrThread(0x1F, 1, 0, 43)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#02311F#5P呜哇哇哇哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12P#N这、这是……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10110F#12P#N难道……\x01",
            "是布置在空中的电磁机雷！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00207F#12P#N……没错！\x01",
            "财团也已经正式应用这种东西了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x1, 0x1, 0x1E, 0x1, 0, 0, 0, 0, 0, 0, 80, 80, 80, 0xFF, 0, 0, 0, 0)

    def lambda_BD97():
        OP_96(0xFE, 0x2710, 0xFFFFFD12, 0x4E20, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_BD97)

    ChrTalk(
        0x10A,
        "#00610F#12P#N他们果然很善于战斗……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopEffect(0x0, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1F, 0x2)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10410F#12P啧……让对方得逞了呢。\x02\x03",
            "#10407F敌舰已经绕到了右舷前方！\x01",
            "阿巴斯，展开抗冲击力场！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x8,
        (
            "#12107F#11P明白了！\x02\x03",
            "大家都蹲下，\x01",
            "准备好接下来的冲击！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x24)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x106, 0x25)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    OP_0D()
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, 5000, 0, 18000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopSound(498, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 1)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_BA27 end

    def Function_43_BF60(): pass

    label("Function_43_BF60")

    Sound(204, 0, 100, 0)

    label("loc_BF66")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF7F")
    Sound(203, 0, 100, 0)
    Sleep(900)
    Jump("loc_BF66")

    label("loc_BF7F")

    Return()

    # Function_43_BF60 end

    def Function_44_BF80(): pass

    label("Function_44_BF80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    LoadChrToIndex("apl/ch51217.itc", 0x20)
    LoadChrToIndex("apl/ch51218.itc", 0x21)
    LoadChrToIndex("apl/ch51219.itc", 0x22)
    LoadChrToIndex("apl/ch51220.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51224.itc", 0x25)
    LoadChrToIndex("apl/ch51774.itc", 0x26)
    LoadEffect(0x0, "event/ev17057.eff")
    SoundLoad(498)
    SoundLoad(825)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A3(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    OP_A3(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    OP_A2(0xB, 0x80)
    OP_A3(0xC, 0x80)
    OP_A3(0x8, 0x80)
    OP_A3(0x13, 0x80)
    OP_A3(0xF, 0x80)
    OP_A2(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x0)
    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x13, 0xFF)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x5)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x24)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x106, 0x25)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    OP_73(0x6, 0x4)
    OP_72(0x7, 0x4)
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0xF, -3000, 0, 250, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x103, -950, 0, -1650, 0)
    SetChrPos(0x104, 550, 0, -1350, 0)
    SetChrPos(0x109, 1550, 0, -1950, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x106, 0, 0, -2200, 0)
    SetChrPos(0x10A, -2250, 0, -1250, 0)
    OP_68(370, 700, 3790, 0)
    OP_6D(0x28, 0x13, 0x0, 0x0)
    OP_6E(0x1F4, 0x0)
    OP_6C(0x5014, 0x0)
    OP_6C(0x4E20, 0x3E8)
    BeginChrThread(0x101, 0, 0, 32)
    BeginChrThread(0x1F, 2, 0, 33)
    Sound(498, 2, 100, 0)
    Sound(825, 2, 100, 0)
    FadeToBright(1000, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 50, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x3E8)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010F#12P唔……！\x02",
    )

    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(500)
    OP_82(0x14, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 34)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xF,
        "#02106F#6P#N哇啊啊啊啊！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xC,
        (
            "#01911F#5P没、没问题！\x01",
            "舰身只受到轻微损伤！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10407F#11P很好，接下来将抗冲击力场\x01",
            "集中到舰首前方！\x02\x03",
            "强行突破雷群，\x01",
            "直接冲向『大树』！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#12107F#11P#4S明白！\x02",
    )

    CloseMessageWindow()
    Sound(920, 0, 100, 0)
    Sound(921, 0, 100, 0)
    Sound(922, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 0, 13000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    Sound(499, 0, 100, 0)
    OP_76(0x6, "base02", 0x2, "sky_ani3")
    OP_76(0x6, "base03", 0x2, "sky_ani3")
    OP_68(370, 700, 790, 1000)
    StopSound(498, 1000, 100)
    StopSound(825, 1000, 100)
    EndChrThread(0x1F, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x24, 2)
    NewScene("e4320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_BF80 end

    def Function_45_C3CF(): pass

    label("Function_45_C3CF")

    OP_F4(0x5)
    Return()

    # Function_45_C3CF end

    SaveToFile()

Try(main)
