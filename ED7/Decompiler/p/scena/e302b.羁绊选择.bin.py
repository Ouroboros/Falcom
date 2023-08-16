from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e302b.bin",                # FileName
        "e302b",                    # MapName
        "e302b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e302b",                  # 0
        "正骑士阿巴斯",           # 1
        "约纳",                   # 2
        "瓦吉",                   # 3
        "缇欧",                   # 4
        "芙兰",                   # 5
        "莉夏",                   # 6
        "兰迪",                   # 7
        "诺艾尔",                 # 8
        "艾莉",                   # 9
        "麦克道尔议长",           # 10
        "格蕾丝",                 # 11
        "神狼蔡特",               # 12
        "随从骑士维恩图斯",       # 13
        "随从骑士朱诺",           # 14
    ))

    AddCharChip((
        "chr/ch06712.itc",                   # 00
        "chr/ch06102.itc",                   # 01
        "chr/ch03100.itc",                   # 02
        "chr/ch03102.itc",                   # 03
        "chr/ch00202.itc",                   # 04
        "chr/ch06900.itc",                   # 05
        "chr/ch03200.itc",                   # 06
        "chr/ch00302.itc",                   # 07
        "chr/ch06002.itc",                   # 08
        "chr/ch02902.itc",                   # 09
        "chr/ch00102.itc",                   # 0A
        "chr/ch05802.itc",                   # 0B
        "chr/ch02710.itc",                   # 0C
        "chr/ch48400.itc",                   # 0D
    ))

    DeclNpc(101790,  150,     -94010,  90,   261,  0x0, 0,   0,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(3000,    -1350,   6960,    45,   261,  0x0, 0,   1,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(101790,  150,     -95980,  90,   261,  0x0, 0,   3,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-3119,   -1350,   7039,    315,  261,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(100849,  0,       270,     270,  261,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-1500,   0,       -1500,   0,    389,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(97639,   170,     959,     90,   261,  0x0, 0,   7,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(100309,  170,     959,     270,  261,  0x0, 0,   9,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(100169,  100,     -102720, 270,  261,  0x0, 0,   10,  0,   255, 255, 0,   6,   255,  0)
    DeclNpc(98440,   100,     -101110, 180,  261,  0x0, 0,   11,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(100220,  100,     -104779, 270,  261,  0x0, 0,   8,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-3000,   0,       -2500,   0,    389,  0x0, 0,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(103569,  0,       -97089,  270,  257,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(103949,  0,       -209,    270,  257,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)

    DeclActor(102510,  0,       -97020,  1000,    103570,  1500,    -97090,  0x007E, 0,  18, 0x0000)
    DeclActor(102710,  0,       -200,    400,     103950,  1500,    -210,    0x007E, 0,  20, 0x0000)
    DeclActor(2350,    0,       -92230,  800,     2350,    1500,    -92230,  0x007C, 0,  28, 0x0000)
    DeclActor(103750,  0,       -105640, 2000,    103750,  1500,    -105640, 0x007C, 0,  3,  0x0000)

    ChipFrameInfo(864, 0)                                        # 0

    ScpFunction((
        "Function_0_360",          # 00, 0
        "Function_1_410",          # 01, 1
        "Function_2_509",          # 02, 2
        "Function_3_54E",          # 03, 3
        "Function_4_6F6",          # 04, 4
        "Function_5_831",          # 05, 5
        "Function_6_D2D",          # 06, 6
        "Function_7_102D",         # 07, 7
        "Function_8_1522",         # 08, 8
        "Function_9_1849",         # 09, 9
        "Function_10_1967",        # 0A, 10
        "Function_11_1DBE",        # 0B, 11
        "Function_12_1EFF",        # 0C, 12
        "Function_13_24BA",        # 0D, 13
        "Function_14_26EA",        # 0E, 14
        "Function_15_2810",        # 0F, 15
        "Function_16_2BBE",        # 10, 16
        "Function_17_2F67",        # 11, 17
        "Function_18_3243",        # 12, 18
        "Function_19_3247",        # 13, 19
        "Function_20_3519",        # 14, 20
        "Function_21_351D",        # 15, 21
        "Function_22_3700",        # 16, 22
        "Function_23_3D9F",        # 17, 23
        "Function_24_43E0",        # 18, 24
        "Function_25_4A48",        # 19, 25
        "Function_26_52F2",        # 1A, 26
        "Function_27_5B69",        # 1B, 27
        "Function_28_5F76",        # 1C, 28
        "Function_29_6871",        # 1D, 29
        "Function_30_6891",        # 1E, 30
    ))


    def Function_0_360(): pass

    label("Function_0_360")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_398"),
        (1, "loc_3A4"),
        (2, "loc_3B0"),
        (3, "loc_3BC"),
        (4, "loc_3C8"),
        (5, "loc_3D4"),
        (6, "loc_3E0"),
        (SWITCH_DEFAULT, "loc_3EC"),
    )


    label("loc_398")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3A4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3B0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3BC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3C8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3D4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_3F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3F8")

    label("loc_40F")

    Return()

    # Function_0_360 end

    def Function_1_410(): pass

    label("Function_1_410")

    SetMapFlags(0x10000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x12, 0x8)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xB)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD")
    SetChrFlags(0xB, 0x10)

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4D7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 30)
    Jump("loc_508")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_4EB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 29)
    Jump("loc_508")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x24, 3)
    SetChrPos(0x0, 102230, 0, -105070, 90)

    label("loc_508")

    Return()

    # Function_1_410 end

    def Function_2_509(): pass

    label("Function_2_509")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_527")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53B")
    OP_24(0x1F2)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_541")

    label("loc_53B")

    Sound(498, 1, 80, 0)

    label("loc_541")

    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x3, 0x10)
    Return()

    # Function_2_509 end

    def Function_3_54E(): pass

    label("Function_3_54E")

    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_573")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A9")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5AC"),
        (1, "loc_5DB"),
        (2, "loc_68D"),
        (3, "loc_695"),
        (SWITCH_DEFAULT, "loc_6A4"),
    )


    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CB")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_5D6")

    label("loc_5CB")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_5D6")

    Jump("loc_6A4")

    label("loc_5DB")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    SetChrName("自动语音")

    AnonymousTalk(
        0xFF,
        "这里是克洛斯贝尔警察局。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_665")

    AnonymousTalk(
        0xFF,
        "即将受理您的报告。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自动语音")

    AnonymousTalk(
        0xFF,
        (
            "报告处理完毕，\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67F")

    label("loc_665")


    AnonymousTalk(
        0xFF,
        "没有可以报告的委托。\x02",
    )

    CloseMessageWindow()

    label("loc_67F")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_6A4")

    label("loc_68D")

    Call(0, 4)
    Jump("loc_6A4")

    label("loc_695")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A4")

    label("loc_6A4")

    Jump("loc_573")

    label("loc_6A9")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E6")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(0, 5)
    Return()

    label("loc_6E6")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_3_54E end

    def Function_4_6F6(): pass

    label("Function_4_6F6")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_718")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718")
    ClearScenarioFlags(0x2A, 0)

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_735")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_735")
    ClearScenarioFlags(0x2A, 1)

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_752")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_752")
    ClearScenarioFlags(0x2A, 2)

    label("loc_752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_76F")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76F")
    ClearScenarioFlags(0x2A, 3)

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_78C")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78C")
    ClearScenarioFlags(0x2A, 4)

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_7A9")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A9")
    ClearScenarioFlags(0x2A, 5)

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_7B5")
    SetScenarioFlags(0x2A, 6)

    label("loc_7B5")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FA")
    Sound(498, 1, 50, 0)
    Jump("loc_800")

    label("loc_7FA")

    Sound(498, 1, 100, 0)

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_830")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_830")

    Return()

    # Function_4_6F6 end

    def Function_5_831(): pass

    label("Function_5_831")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_89A")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_89A")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00205F啊……\x02\x03",
            "#00204F看样子，罗伊德前辈已经\x01",
            "在『波波碰！』游戏中\x01",
            "战胜过所有对手了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905F哎哎，真的吗～！？\x02\x03",
            "#01909F不愧是罗伊德警官……\x01",
            "实在是太厉害了～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_9F4")

    ChrTalk(
        0x9,
        (
            "#02302F嘿，的确，\x01",
            "你也挺有一套的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F4")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢，\x01",
            "其实只是运气好而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F不，在这种脑力游戏中，\x01",
            "光靠运气是无法取得胜利的。\x02\x03",
            "#12102F班宁斯，你才是真正的\x01",
            "『波波碰大师』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F……这、这真是过奖了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(贤者, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C33")

    ChrTalk(
        0x8,
        (
            "#12100F哦，对了……\x02\x03",
            "不介意的话，就收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x1F, 0xF0),
            scpstr(0x7, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(贤者, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12100F这是教会与爱普斯泰恩财团\x01",
            "以古代秘术为基础，\x01",
            "共同开发的禁忌核心回路。\x02\x03",
            "由于性能过强，很难操控，\x01",
            "所以一直没有正式投入运用……\x02\x03",
            "#12102F不过，你应该有能力控制它。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F嗯，明白了，\x01",
            "我一定会让它发挥作用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFB")

    label("loc_C33")


    ChrTalk(
        0x8,
        (
            "#12100F嗯……对了。\x02\x03",
            "#12102F作为奖励，把这个给你吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x1F, 0x67),
            scpstr(0x7, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(水耀珠, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000F哈哈，谢谢，\x01",
            "我一定会让它派上用场的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CFB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_831 end

    def Function_6_D2D(): pass

    label("Function_6_D2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D50")
    Call(0, 22)
    Jump("loc_DA5")

    label("loc_D50")


    ChrTalk(
        0x10,
        (
            "#00102F（……待会见吧。）\x02\x03",
            "#00104F（迟些再来也没关系，\x01",
            "  请认真做好万全准备。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA5")

    Jump("loc_1029")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBE")

    ChrTalk(
        0x10,
        (
            "#00103F解放克洛斯贝尔市作战……\x01",
            "明天就要正式开始了。\x02\x03",
            "#00108F如果能见到贝尔和迪塔叔叔，我一定要问出\x01",
            "他们策动这一系列事件的真正目的……\x01",
            "而且还要尽力说服他们。\x02\x03",
            "#00101F可是，如果无法说服成功……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F艾莉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00106F……对不起，\x01",
            "忍不住说出了丧气话。\x02\x03",
            "#00100F为了报答那些不顾自身安危，\x01",
            "向我们伸出援手的人们……\x02\x03",
            "更为了夺回小琪雅，\x01",
            "我们是绝不能输的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F……明天一起加油吧，艾莉。\x01",
            "我和大家都会陪在你身边的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F……呵呵，嗯。\x02\x03",
            "#00102F谢谢，罗伊德。\x01",
            "多亏你的劝慰，\x01",
            "我感觉轻松了一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_1029")

    label("loc_FBE")


    ChrTalk(
        0x10,
        (
            "#00104F谢谢，罗伊德。\x01",
            "多亏你的劝慰，\x01",
            "我感觉轻松了一些。\x02\x03",
            "#00102F今天就早点休息……\x01",
            "为明天做好准备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1029")

    TalkEnd(0xFE)
    Return()

    # Function_6_D2D end

    def Function_7_102D(): pass

    label("Function_7_102D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1050")
    Call(0, 23)
    Jump("loc_10AE")

    label("loc_1050")


    ChrTalk(
        0xB,
        (
            "#00204F把手头的事情做完以后，\x01",
            "我就会去甲板的。\x02\x03",
            "#00202F要谈的事情……\x01",
            "就等到那时再说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AE")

    Jump("loc_151E")

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1498")

    ChrTalk(
        0xB,
        (
            "#00203F（快速敲击键盘……）\x02\x03",
            "#00200F嗯，这样就准备得差不多了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F缇欧……\x01",
            "你在做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11CD")
    Jump("loc_1217")

    label("loc_11CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11ED")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_11ED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_120D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1217")

    label("loc_120D")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1217")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00202F为了明天的突入行动，\x01",
            "我正在对梅尔卡瓦的系统\x01",
            "做最终检查。\x02\x03",
            "#00203F我到时也会离开梅尔卡瓦，\x01",
            "和大家一起作战……\x02\x03",
            "#00200F所以控制通讯终端之后的网络侵入\x01",
            "工作要交给约纳和芙兰来处理，\x01",
            "现在就要完成交接。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F这样啊……\x01",
            "真是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F没什么，马上就要\x01",
            "处理完了，不必担心。\x02\x03",
            "#00202F罗伊德前辈只要摆出一副\x01",
            "队长的架势，威严地站在边上\x01",
            "看着就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F那可不行啊，为了明天的作战，\x01",
            "还有好多事情需要准备呢。\x02\x03",
            "#00000F既然你这么有干劲，\x01",
            "这里就全部交给你了。\x02\x03",
            "缇欧，你们要\x01",
            "注意休息哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F嗯，知道了，\x01",
            "罗伊德前辈也要好好休息。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_151E")

    label("loc_1498")


    ChrTalk(
        0xB,
        (
            "#00204F为了明天的突入行动，\x01",
            "我正在对梅尔卡瓦的系统\x01",
            "做最终检查。\x02\x03",
            "#00202F检查完毕之后，\x01",
            "我就会去休息了。\x01",
            "罗伊德前辈也要好好休息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151E")

    TalkEnd(0xFE)
    Return()

    # Function_7_102D end

    def Function_8_1522(): pass

    label("Function_8_1522")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1545")
    Call(0, 24)
    Jump("loc_1592")

    label("loc_1545")


    ChrTalk(
        0xE,
        (
            "#00304F那我们稍后见吧。\x02\x03",
            "#00302F等我检修完这东西之后，\x01",
            "马上就会过去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1592")

    Jump("loc_1845")

    label("loc_1597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D5")

    ChrTalk(
        0xE,
        "#00300F哟，罗伊德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F兰迪，你们正在\x01",
            "检修武器吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302F嗯，毕竟明天的作战可以算是\x01",
            "我们至今为止要面对的最大难关。\x02\x03",
            "#00304F有可能会用到『狂战士』，\x01",
            "为了预防万一，现在必须要\x01",
            "认真做好准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F唔，至今为止总是很忙，\x01",
            "一直都没时间维护武器……\x02\x03",
            "#00003F我是不是也应该趁着今晚，\x01",
            "好好检查一下旋棍呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309F嗯，还是检查一下吧。\x02\x03",
            "#00303F虽说你的武器和来复枪不同，\x01",
            "不需要特别检修\x01",
            "精密部件……\x02\x03",
            "#00300F但就算只是擦拭一下，\x01",
            "手感也会有很大改善。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F原、原来如此……\x01",
            "也许正如你所说呢。\x02\x03",
            "#00002F多谢指点，我稍后\x01",
            "也去检查一下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_1845")

    label("loc_17D5")


    ChrTalk(
        0xE,
        (
            "#00304F你最好也在明天之前，\x01",
            "把武器认真检修一番。\x02\x03",
            "#00309F一定要像对待绝世美女那样，\x01",
            "小心翼翼地温柔处理哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1845")

    TalkEnd(0xFE)
    Return()

    # Function_8_1522 end

    def Function_9_1849(): pass

    label("Function_9_1849")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_18EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186C")
    Call(0, 25)
    Jump("loc_18EA")

    label("loc_186C")


    ChrTalk(
        0xF,
        (
            "#10106F那、那个……\x01",
            "我有件事必须要拜托\x01",
            "罗伊德警官。\x02\x03",
            "#10101F稍后请到甲板来找我吧。\x01",
            "我处理完手边的事情之后\x01",
            "就会过去的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EA")

    Jump("loc_1963")

    label("loc_18EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1901")
    Call(0, 10)
    Jump("loc_1963")

    label("loc_1901")


    ChrTalk(
        0xF,
        (
            "#10100F我今天晚上还要\x01",
            "再和司令联络一次。\x02\x03",
            "#10103F为了明天的作战，\x01",
            "还是再做一次最终确认为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1963")

    TalkEnd(0xFE)
    Return()

    # Function_9_1849 end

    def Function_10_1967(): pass

    label("Function_10_1967")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x101, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19F8")
    Jump("loc_1A42")

    label("loc_19F8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A18")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A42")

    label("loc_1A18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A38")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A42")

    label("loc_1A38")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A42")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x101,
        (
            "#00000F辛苦你们了，诺艾尔、芙兰。\x02\x03",
            "#00002F明天就要展开作战了，\x01",
            "但这里的气氛却很平和呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10102F真不好意思。\x02\x03",
            "#10106F我正在检修武器，\x01",
            "芙兰却突然跑了进来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909F呵呵，我是来给\x01",
            "姐姐打气的～\x02\x03",
            "#01904F因为我已经做好了\x01",
            "充足的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F哈哈，真是可靠啊。\x02\x03",
            "#00000F芙兰，你明天也要在\x01",
            "后援岗位上大显身手哦，\x01",
            "今天就尽量养精蓄锐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01902F嗯，当然～\x01",
            "……其实，我就是为了\x01",
            "这个才来的～！\x02\x03",
            "#01909F不管怎么说，\x01",
            "我只要待在姐姐身边，\x01",
            "就可以补充能量了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F哈哈，也许\x01",
            "正如你所说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#10106F唉，真是的……\x01",
            "只要别妨碍到我就好。\x02\x03",
            "#10100F那、那个，罗伊德警官，\x01",
            "我今天晚上还要\x01",
            "再和司令联络一次。\x02\x03",
            "#10103F为了明天的作战，\x01",
            "还是再做一次最终确认为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F嗯，那就拜托你了。\x02\x03",
            "#00000F诺艾尔，检修完武器之后，\x01",
            "要早点休息哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#10109F好的！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1DB, 0)
    Return()

    # Function_10_1967 end

    def Function_11_1DBE(): pass

    label("Function_11_1DBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE1")
    Call(0, 26)
    Jump("loc_1E4D")

    label("loc_1DE1")


    ChrTalk(
        0xA,
        (
            "#10404F还有一件事，\x01",
            "我觉得应该悄悄\x01",
            "告诉你。\x02\x03",
            "#10402F稍后到甲板上来吧。\x01",
            "我和阿巴斯喝完酒以后\x01",
            "就会过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4D")

    Jump("loc_1EFB")

    label("loc_1E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E64")
    Call(0, 12)
    Jump("loc_1EFB")

    label("loc_1E64")


    ChrTalk(
        0xA,
        (
            "#10404F总之，既然上面已经下达了许可，\x01",
            "我们就不必再顾虑其它事情，\x01",
            "只需专心完成使命即可。\x02\x03",
            "#10402F呵呵，看来明天会很忙碌呢，\x01",
            "要趁现在好好休息一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFB")

    TalkEnd(0xFE)
    Return()

    # Function_11_1DBE end

    def Function_12_1EFF(): pass

    label("Function_12_1EFF")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x101, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F90")
    Jump("loc_1FDA")

    label("loc_1F90")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FB0")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FDA")

    label("loc_1FB0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FD0")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FDA")

    label("loc_1FD0")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FDA")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x101, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2090")
    Jump("loc_20DA")

    label("loc_2090")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20B0")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20DA")

    label("loc_20B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20D0")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20DA")

    label("loc_20D0")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20DA")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x8, 0x10)

    ChrTalk(
        0x101,
        (
            "#00005F瓦吉、阿巴斯……\x01",
            "你们在喝酒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F嗯，因为我们已经\x01",
            "完成了必要的准备工作。\x02\x03",
            "#10402F呵呵，你要不要也来一杯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F喂喂……明天还要作战呢，\x01",
            "你们这样没问题吗？\x02\x03",
            "#00001F边上已经摆着很多\x01",
            "被你们喝空的杯子了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F不必担心，\x01",
            "这是让维恩图斯特地\x01",
            "调制的无酒精鸡尾酒。\x02\x03",
            "不会对明天的作战\x01",
            "造成任何影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F啊，是这样啊……\x02\x03",
            "#00000F算啦，既然阿巴斯这么说，\x01",
            "那我这次就相信了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409F呵呵，我一个人喝的时候，\x01",
            "你也应该相信啊。\x02\x03",
            "#10403F……对了，有件事情还是\x01",
            "通知你一声比较好。\x02\x03",
            "#10400F关于明天的作战，法王阁下\x01",
            "已经下达了正式的参战许可。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F啊……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F梅尔卡瓦的主要用途是执行\x01",
            "隐秘活动，本应尽量避免将其\x01",
            "使用于大规模的作战中……\x02\x03",
            "但考虑到整个大陆的混乱状况，\x01",
            "就算稍微有所暴露，也是没有办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F这样啊……\x01",
            "教会能做出这种判断，真是值得感谢。\x02\x03",
            "#00013F……总之，明天就要决战了，\x01",
            "还请二位助我一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10402F呵呵，明白了，队长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12102F我们自然会全力相助。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetScenarioFlags(0x1DB, 1)
    Return()

    # Function_12_1EFF end

    def Function_13_24BA(): pass

    label("Function_13_24BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x69), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E2")
    Call(0, 26)
    Jump("loc_25CF")

    label("loc_24E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CF")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2533"),
        (1, "loc_25A4"),
        (SWITCH_DEFAULT, "loc_25C0"),
    )


    label("loc_2533")


    ChrTalk(
        0x8,
        (
            "#12100F真是的……\x01",
            "那可是机密事项啊。\x02\x03",
            "#12102F……算了，这也没办法。\x01",
            "让你们知道，应该也不会有什么问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25CA")

    label("loc_25A4")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25CA")

    label("loc_25C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25CA")

    Jump("loc_24EC")

    label("loc_25CF")

    Jump("loc_26E6")

    label("loc_25D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E6")
    Call(0, 12)
    Jump("loc_26E6")

    label("loc_25E6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E6")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2637"),
        (1, "loc_26BB"),
        (SWITCH_DEFAULT, "loc_26D7"),
    )


    label("loc_2637")


    ChrTalk(
        0x8,
        (
            "#12100F在明天的作战中……\x01",
            "我们会在梅尔卡瓦上\x01",
            "专心为你们提供后援支持。\x02\x03",
            "而你们则要潜入市内，\x01",
            "所以最好趁现在\x01",
            "做好充分准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26E1")

    label("loc_26BB")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26E1")

    label("loc_26D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26E1")

    Jump("loc_25F0")

    label("loc_26E6")

    TalkEnd(0xFE)
    Return()

    # Function_13_24BA end

    def Function_14_26EA(): pass

    label("Function_14_26EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x68), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2799")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270D")
    Call(0, 25)
    Jump("loc_2794")

    label("loc_270D")


    ChrTalk(
        0xC,
        (
            "#01900F罗伊德警官，请你一定要认真\x01",
            "倾听姐姐的愿望哦。\x02\x03",
            "#01909F呵呵，真期待结果呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F（唔……芙兰为什么\x01",
            "  这么兴奋……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2794")

    Jump("loc_280C")

    label("loc_2799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AB")
    Call(0, 10)
    Jump("loc_280C")

    label("loc_27AB")


    ChrTalk(
        0xC,
        (
            "#01902F罗伊德警官，\x01",
            "明天一定要加油哦～\x02\x03",
            "#01909F我也会通过姐姐\x01",
            "来补充能量，\x01",
            "做好万全准备的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280C")

    TalkEnd(0xFE)
    Return()

    # Function_14_26EA end

    def Function_15_2810(): pass

    label("Function_15_2810")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B36")

    ChrTalk(
        0x9,
        (
            "#02300F在你们明天潜入克洛斯贝尔市的\x01",
            "同时，我们也会在梅尔卡瓦上\x01",
            "发动网络入侵。\x02\x03",
            "#02303F总之，你们就多加努力，\x01",
            "在市内闹个天翻地覆吧。\x02\x03",
            "#02302F只要在市内造成混乱，\x01",
            "应该就会出现能成功\x01",
            "侵入导力网络的机会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F嗯，我们一起加油，\x01",
            "努力完成各自的任务吧。\x02\x03",
            "#00001F……话说回来，约纳……\x01",
            "你今晚该不会是准备\x01",
            "熬一通宵吧？（盯视）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305F……呃！\x02\x03",
            "#02309F这、这个嘛……\x01",
            "虽然准备工作已经做得差不多了，\x01",
            "但我毕竟是夜行生物嘛。\x02\x03",
            "#02304F而且，与其明明睡不着\x01",
            "却硬要去睡，也许还是\x01",
            "通宵之后的精神状态更好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F我说你啊……\x01",
            "明天的作战可是一场持久战，\x01",
            "你要是通宵，说不定会撑不下来的。\x02\x03",
            "#00001F既然准备工作已经快完成了，\x01",
            "你就尽早去休息吧。\x01",
            "肯定还是休息之后的精神状态更好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02306F好啦好啦，我知道了。\x02\x03",
            "#02300F手头的事情告一段落之后，我就会收工\x01",
            "去休息的，你不要一直盯着我嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 3)
    Jump("loc_2BBA")

    label("loc_2B36")


    ChrTalk(
        0x9,
        (
            "#02300F明天的网络入侵行动的\x01",
            "准备工作就快完成了。\x02\x03",
            "#02306F手头事情告一段落之后，我就会收工\x01",
            "去休息的，你不要动不动就过来盯梢啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBA")

    TalkEnd(0xFE)
    Return()

    # Function_15_2810 end

    def Function_16_2BBE(): pass

    label("Function_16_2BBE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EE0")

    ChrTalk(
        0x12,
        (
            "#02103F对现有体制持有异议的人们\x01",
            "集结在一起，抱着拼死的觉悟而\x01",
            "发动『解放克洛斯贝尔市作战』……\x02\x03",
            "#02101F如果这次的作战以失败而告终，\x01",
            "世人恐怕就会得出『总统才是正确的』\x01",
            "这种结论。\x02\x03",
            "#02103F就像卡尔瓦德一样，在过去的\x01",
            "民主化过程中所策动的种种阴谋，\x01",
            "如今都已被解释为正当合法的行为了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……是啊。\x02\x03",
            "#00001F甚至可以说……\x01",
            "是非成败，全都取决于明天的结果。\x01",
            "我非常明白这一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109F哈哈哈，其实我并没打算\x01",
            "给你施加压力。\x02\x03",
            "#02103F……作为一名记者，我的义务\x01",
            "是亲眼见证克洛斯贝尔的命运，\x01",
            "并将其传达给大众。\x02\x03",
            "#02100F不过，抛开新闻工作者这层身份，\x01",
            "我更希望站在一名普通人的立场上\x01",
            "来支持你们。\x02\x03",
            "#02104F为你们这个继承了盖伊先生的意志\x01",
            "而诞生的特别任务支援科加油呐喊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02109F呵呵，为了小琪雅……\x01",
            "你们明天一定要拼尽全力哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F嗯，放心吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 4)
    Jump("loc_2F63")

    label("loc_2EE0")


    ChrTalk(
        0x12,
        (
            "#02100F抛开新闻工作者这层身份，\x01",
            "我更希望站在一名普通人的立场上\x01",
            "来支持你们。\x02\x03",
            "#02109F为了小琪雅……\x01",
            "你们明天一定要拼尽全力哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F63")

    TalkEnd(0xFE)
    Return()

    # Function_16_2BBE end

    def Function_17_2F67(): pass

    label("Function_17_2F67")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")

    ChrTalk(
        0x11,
        (
            "#02503F……明天恐怕将会是\x01",
            "十分艰辛的一天。\x02\x03",
            "#02500F竟然让你们这些年轻人\x01",
            "来背负『自治州的命运』\x01",
            "这个沉重负担。\x02\x03",
            "#02503F身为自治州的代表之一……\x01",
            "我要向你们表示歉意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……请您不要\x01",
            "这么说。\x02\x03",
            "#00000F麦克道尔议长，您已经\x01",
            "完成了发表『独立无效宣言』\x01",
            "这个重要的职责。\x02\x03",
            "#00004F至于接下来的事情，\x01",
            "就必须要由我们这些\x01",
            "战斗人员来亲手解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#02503F……真不好意思，\x01",
            "实在是辛苦你们了。\x02\x03",
            "#02500F既然如此，我就以你们一定能够\x01",
            "在『解放作战』中取得胜利为前提，\x01",
            "继续考虑今后的对策吧。\x02\x03",
            "#02503F这也是为了让陷入混乱的克洛斯贝尔\x01",
            "居民们尽早恢复到正常生活之中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F好……那就拜托您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 5)
    Jump("loc_323F")

    label("loc_31CB")


    ChrTalk(
        0x11,
        (
            "#02503F我就以你们一定能够\x01",
            "在『解放作战』中取得胜利为前提，\x01",
            "继续考虑今后的对策吧。\x02\x03",
            "#02500F……愿女神保佑你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323F")

    TalkEnd(0xFE)
    Return()

    # Function_17_2F67 end

    def Function_18_3243(): pass

    label("Function_18_3243")

    Call(0, 19)
    Return()

    # Function_18_3243 end

    def Function_19_3247(): pass

    label("Function_19_3247")

    TalkBegin(0x14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3515")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "购买装备\x01",        # 1
            "购买消耗品\x01",      # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_32B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3333")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_32D2")
    OP_AF(0xD8)
    Jump("loc_3324")

    label("loc_32D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_32E2")
    OP_AF(0xD7)
    Jump("loc_3324")

    label("loc_32E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_32F2")
    OP_AF(0xD6)
    Jump("loc_3324")

    label("loc_32F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3302")
    OP_AF(0xD5)
    Jump("loc_3324")

    label("loc_3302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_3312")
    OP_AF(0xD4)
    Jump("loc_3324")

    label("loc_3312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_3322")
    OP_AF(0xD3)
    Jump("loc_3324")

    label("loc_3322")

    OP_AF(0xD2)

    label("loc_3324")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3510")

    label("loc_3333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3353")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3510")

    label("loc_3353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3367")
    Jump("loc_3510")

    label("loc_3367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3510")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346C")

    ChrTalk(
        0x14,
        (
            "我也很清楚，\x01",
            "如今的状况实在\x01",
            "是不容乐观……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "不过，警察、教会、警备队、黑月……\x01",
            "甚至连『神狼』和『银』都\x01",
            "站在了我们这边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "集结了这么多的伙伴，\x01",
            "让我不禁开始觉得，无论面对什么\x01",
            "挑战，我们都可以顺利取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3510")

    label("loc_346C")


    ChrTalk(
        0x14,
        (
            "警察、教会、警备队、黑月……\x01",
            "甚至连『神狼』和『银』都\x01",
            "站在了我们这边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "集结了这么多的伙伴，\x01",
            "让我不禁开始觉得，无论面对什么\x01",
            "挑战，我们都可以顺利取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3510")

    Jump("loc_3254")

    label("loc_3515")

    TalkEnd(0x14)
    Return()

    # Function_19_3247 end

    def Function_20_3519(): pass

    label("Function_20_3519")

    Call(0, 21)
    Return()

    # Function_20_3519 end

    def Function_21_351D(): pass

    label("Function_21_351D")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_352A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36FC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3580")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3580")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A0")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36F7")

    label("loc_35A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35B4")
    Jump("loc_36F7")

    label("loc_35B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3687")

    ChrTalk(
        0x15,
        (
            "在明天的作战中，\x01",
            "最大的问题显然还是\x01",
            "那三架『神机』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "想办法击退那些『神机』，\x01",
            "正是潜入市内的关键。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我们到时会和各方势力联手作战，\x01",
            "无论如何都要取得成功。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36F7")

    label("loc_3687")


    ChrTalk(
        0x15,
        (
            "想办法击退那三架『神机』，\x01",
            "正是潜入市内的关键。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "我们到时会和各方势力联手作战，\x01",
            "无论如何都要取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F7")

    Jump("loc_352A")

    label("loc_36FC")

    TalkEnd(0x15)
    Return()

    # Function_21_351D end

    def Function_22_3700(): pass

    label("Function_22_3700")

    EventBegin(0x0)
    Fade(500)
    OP_68(100420, 1000, -101760, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15480, 0)
    SetChrPos(0x101, 100110, 0, -101660, 180)
    SetChrSubChip(0x10, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB1")

    ChrTalk(
        0x10,
        (
            "#12P#00106F解放克洛斯贝尔市作战……\x01",
            "明天就要正式开始了。\x02\x03",
            "#00108F如果能见到贝尔和迪塔叔叔，我一定要问出\x01",
            "他们策动这一系列事件的真正目的……\x01",
            "而且还要尽力说服他们。\x02\x03",
            "#00101F可是，如果无法说服成功……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P……对立恐怕就是不可避免的了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00103F嗯……我早已\x01",
            "有所觉悟了。\x02\x03",
            "#00108F为了报答那些不顾自身安危，\x01",
            "向我们伸出援手的人们……\x02\x03",
            "#00101F更为了夺回小琪雅，\x01",
            "我们是绝对\x01",
            "不能输的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFFFF)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#5P……艾莉。\x02\x03",
            "#00000F你不必将这一切都扛在自己肩上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00105F哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P不管是迪塔先生还是玛丽亚贝尔小姐，\x01",
            "对我们而言，也都是很亲近的熟人。\x02\x03",
            "#00001F所以说，这份重担并不是只属于你一个人的，\x01",
            "应该由我们大家一起来背负。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#00108F罗伊德……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F……明天一起加油吧，艾莉，\x01",
            "我和大家都会陪在你身边的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00104F……呵呵，嗯。\x02\x03",
            "#00102F谢谢，罗伊德。\x01",
            "多亏你的劝慰，我感觉轻松了一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#5P哈哈……不用客气。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10)
    Sleep(500)

    ChrTalk(
        0x10,
        (
            "#12P#00106F（……那、那个，罗伊德。）\x02\x03",
            "#00112F（做完准备工作之后，\x01",
            "  你可以来甲板一趟吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5P（哎……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00113F（如果方便……\x01",
            "  我有些话，想单独和你\x01",
            "  谈一谈……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 5)
    Jump("loc_3C2C")

    label("loc_3BB1")


    ChrTalk(
        0x10,
        (
            "#12P#00112F（做完准备工作之后，\x01",
            "  你可以来甲板一趟吗？）\x02\x03",
            "#00113F（如果方便……\x01",
            "  我有些话，想单独和你\x01",
            "  谈一谈……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2C")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受艾莉的邀请\x01",      # 0
            "拒绝\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CDE")

    ChrTalk(
        0x101,
        (
            "#00002F#5P（……知道了，\x01",
            "  我稍后就会过去的。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#00109F（……呵呵，谢谢，\x01",
            "  那我们就待会再见吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 3)
    Jump("loc_3D98")

    label("loc_3CDE")


    ChrTalk(
        0x10,
        (
            "#12P#00106F（……是吗。）\x02\x03",
            "#00102F（呵呵，不必在意，\x01",
            "  其实也不是什么大不了的事情。）\x02\x03",
            "#00104F（不过，如果你改变主意了，\x01",
            "  就再来和我说一声吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P（好的，我会的。）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3D98")

    SetChrSubChip(0x10, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_3700 end

    def Function_23_3D9F(): pass

    label("Function_23_3D9F")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3160, -500, 6480, 0)
    MoveCamera(52, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_END)), "loc_3DE1")
    SetChrSubChip(0xB, 0x1)

    label("loc_3DE1")

    SetChrPos(0x101, -3610, -1500, 5780, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4250")

    ChrTalk(
        0xB,
        (
            "#11P#00203F（快速敲击键盘……）\x02\x03",
            "#00200F嗯，这样就准备得差不多了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)

    ChrTalk(
        0xB,
        (
            "#11P#00208F（咔嚓）\x02\x03",
            "#00203F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F缇欧……\x01",
            "你在做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    ChrTalk(
        0xB,
        (
            "#5P#00202F为了明天的突入行动，\x01",
            "我正在对梅尔卡瓦的系统\x01",
            "做最终检查。\x02\x03",
            "#00203F我到时也会离开梅尔卡瓦，\x01",
            "和大家一起作战……\x02\x03",
            "#00200F所以控制通讯终端之后的网络侵入\x01",
            "工作要交给约纳和芙兰来处理，\x01",
            "现在就要完成交接。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F这样啊……\x01",
            "真是辛苦你了。\x02\x03",
            "#00000F我能帮上什么忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00203F……不，没什么。\x02\x03",
            "#00202F这些都是我擅长的工作，\x01",
            "而且还有约纳协助，人手足够了。\x02\x03",
            "#00204F罗伊德前辈只要摆出一副\x01",
            "队长的架势，威严地站在边上\x01",
            "看着就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00006F那可不行啊，为了明天的作战，\x01",
            "还有好多事情需要准备呢。\x02\x03",
            "#00000F既然你这么有干劲，\x01",
            "这里就全部交给你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#5P#00203F……对了，\x01",
            "我的确有件事想拜托罗伊德前辈。\x02\x03",
            "#00208F其实……我有点事\x01",
            "想和你商量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F和我商量……？\x01",
            "你有什么烦恼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00206F……那个，在这里说话有些不方便。\x02\x03",
            "#00201F你忙完了手上的事情之后，\x01",
            "可以来梅尔卡瓦的\x01",
            "甲板吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 6)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_42C0")

    label("loc_4250")


    ChrTalk(
        0xB,
        (
            "#5P#00206F其实……我有点事\x01",
            "想和罗伊德前辈商量。\x02\x03",
            "#00201F你忙完了手上的事情之后，\x01",
            "可以来梅尔卡瓦的\x01",
            "甲板吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C0")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受缇欧的邀请\x01",      # 0
            "拒绝\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4352")

    ChrTalk(
        0x101,
        (
            "#12P#00002F知道了，\x01",
            "我很愿意陪你商量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#00209F呵呵……\x01",
            "那就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 4)
    Jump("loc_43D9")

    label("loc_4352")


    ChrTalk(
        0xB,
        (
            "#5P#00204F……这样啊。\x01",
            "算了，这也没办法。\x02\x03",
            "#00202F如果愿意和我商量事情了，\x01",
            "就再来和我说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F好的，我知道了。\x02",
    )

    OP_5A()
    CloseMessageWindow()

    label("loc_43D9")

    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_3D9F end

    def Function_24_43E0(): pass

    label("Function_24_43E0")

    EventBegin(0x0)
    Fade(500)
    OP_68(98200, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16090, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488C")

    ChrTalk(
        0xE,
        "#5P#00300F哟，罗伊德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000F兰迪，你们正在\x01",
            "检修武器吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302F嗯，毕竟明天的作战可以算是\x01",
            "我们至今为止要面对的最大难关。\x02\x03",
            "#00304F有可能会用到『狂战士』，\x01",
            "为了预防万一，现在必须要\x01",
            "认真做好准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005F唔，至今为止总是很忙，\x01",
            "一直都没时间维护武器……\x02\x03",
            "#00003F我是不是也应该趁着今晚，\x01",
            "好好检查一下旋棍呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309F嗯，还是检查一下吧。\x02\x03",
            "#00303F虽说你的武器和来复枪不同，\x01",
            "不需要特别检修\x01",
            "精密部件……\x02\x03",
            "#00300F但就算只是擦拭一下，\x01",
            "手感也会有很大改善。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009F哈哈，说得也是。\x02\x03",
            "#00005F话说回来，兰迪……\x01",
            "没想到你的心思还挺慎密的。\x02\x03",
            "#00000F不光是那把来复枪，\x01",
            "你好像连斧枪都会\x01",
            "坚持每天检查吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00302F嗯，检查武器可是\x01",
            "基础中的基础啊。\x02\x03",
            "#00304F一定要像对待绝世美女那样，\x01",
            "小心翼翼地温柔处理。\x02\x03",
            "#00300F不然的话，\x01",
            "说不定会在战场上\x01",
            "突然出现故障……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    ChrTalk(
        0x101,
        (
            "#12P#00011F……抱歉，我是不是\x01",
            "让你回想起了不愉快的往事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309F……哈哈，这有什么好道歉的。\x02\x03",
            "#00306F……嗯，话说回来……\x02\x03",
            "#00308F我差不多……也该把那些\x01",
            "事情告诉你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00300F你待会要是有空，\x01",
            "能不能来梅尔卡瓦的甲板一趟？\x02\x03",
            "我想让你\x01",
            "陪我聊聊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 7)
    Jump("loc_48DE")

    label("loc_488C")


    ChrTalk(
        0xE,
        (
            "#5P#00300F你待会要是有空，\x01",
            "能不能来梅尔卡瓦的甲板一趟？\x02\x03",
            "我想让你\x01",
            "陪我聊聊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48DE")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受兰迪的邀请\x01",      # 0
            "拒绝\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A7")

    ChrTalk(
        0x101,
        (
            "#12P#00002F……我知道了，\x01",
            "稍后就会过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P#00309F哈哈，那我们就待会再见吧。\x02\x03",
            "#00302F等我检修完这东西之后，\x01",
            "马上就会过去的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 5)
    Jump("loc_4A41")

    label("loc_49A7")


    ChrTalk(
        0xE,
        (
            "#5P#00306F……这样啊。\x01",
            "算了，反正也不是什么\x01",
            "令人愉快的话题……\x02\x03",
            "#00300F不过，你要是改变主意了，\x01",
            "可以再来和我说一声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4A41")

    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_43E0 end

    def Function_25_4A48(): pass

    label("Function_25_4A48")

    EventBegin(0x0)
    Fade(500)
    OP_68(100500, 1000, -240, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16970, 0)
    SetChrPos(0x101, 100340, 0, -1010, 0)
    SetChrSubChip(0xF, 0x1)
    OP_93(0xC, 0xB4, 0x0)
    OP_4B(0xC, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AA")

    ChrTalk(
        0xF,
        "#5P#10100F罗伊德警官，辛苦你了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#01902F辛苦啦～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000F你们也辛苦了，诺艾尔、芙兰。\x02\x03",
            "#00009F明天就要展开作战了，\x01",
            "但这里的气氛却很平和呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10102F真不好意思。\x02\x03",
            "#10106F我正在检修武器，\x01",
            "芙兰却突然跑了进来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01909F呵呵，我是来给\x01",
            "姐姐打气的～\x02\x03",
            "#01904F因为我已经做好了\x01",
            "充足的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004F哈哈，真是可靠啊。\x02\x03",
            "#00000F芙兰，你明天也要在\x01",
            "后援岗位上大显身手哦，\x01",
            "今天就尽量养精蓄锐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01902F嗯，当然～\x01",
            "……其实，我就是为了\x01",
            "这个才来的～！\x02\x03",
            "#01909F不管怎么说，\x01",
            "我只要待在姐姐身边，\x01",
            "就可以补充能量了呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈，也许\x01",
            "正如你所说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10106F唉，真是的……\x01",
            "只要别妨碍到我就好。\x02\x03",
            "#10102F那、那个，罗伊德警官。\x01",
            "我今天晚上还要\x01",
            "再和司令联络一次。\x02\x03",
            "#10103F为了明天的作战，\x01",
            "还是再做一次最终确认为好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，那就拜托你了。\x02\x03",
            "#00003F诺艾尔，你明天也要\x01",
            "和我们一起潜入市内……\x02\x03",
            "#00000F今天一定要做好充分准备，\x01",
            "然后早点休息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5P#10109F是！\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#11P#01905F（姐姐，姐姐！\x01",
            "  再这么下去，你们今天的谈话\x01",
            "  可就要结束了哦！）\x02\x03",
            "#01909F（这可是个难得的好机会啊，\x01",
            "  你想就这样白白浪费掉吗～？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#5P#10111F（什、什么好机会……\x01",
            "  芙兰，你别再乱说……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005F……嗯？怎么了？\x01",
            "难道出了什么问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#5P#10114F没、没有啦，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F（加油呀，姐姐！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10103F……那个……等你有空的时候，\x01",
            "可以来一趟甲板吗？\x02\x03",
            "#10101F虽然并不是很重要的事，\x01",
            "但我有件事情想拜托\x01",
            "罗伊德警官帮忙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 0)
    Jump("loc_5117")

    label("loc_50AA")


    ChrTalk(
        0xF,
        (
            "#5P#10103F……稍后……可以来甲板吗？\x02\x03",
            "#10101F虽然并不是很重要的事，\x01",
            "但我有件事情想拜托\x01",
            "罗伊德警官帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5117")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受诺艾尔的邀请\x01",      # 0
            "拒绝\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_520C")

    ChrTalk(
        0x101,
        (
            "#12P#00002F好啊，我知道了。\x01",
            "诺艾尔竟然有事情要拜托我，\x01",
            "这可真是稀奇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11P#01909F（成功啦！姐姐！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P#10114F那、那么……\x01",
            "我处理完手边的事情之后\x01",
            "就会过去的……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 6)
    Jump("loc_52E0")

    label("loc_520C")


    ChrTalk(
        0xF,
        (
            "#5P#10106F……这、这样啊……\x02\x03",
            "#10112F不、不用放在心上！\x01",
            "真的不是很重要\x01",
            "的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#01906F唔～这也没办法～\x02\x03",
            "#01901F罗伊德警官，你要是\x01",
            "改变主意了，就再去\x01",
            "和姐姐说一声吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F嗯，我知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_52E0")

    SetChrSubChip(0xF, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_25_4A48 end

    def Function_26_52F2(): pass

    label("Function_26_52F2")

    EventBegin(0x0)
    Fade(500)
    OP_68(102260, 800, -94610, 0)
    MoveCamera(48, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100450, 0, -95200, 90)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0xA, 0x1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_595F")

    ChrTalk(
        0x101,
        (
            "#6P#00005F瓦吉、阿巴斯……\x01",
            "你们在喝酒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404F嗯，因为我们已经\x01",
            "完成了必要的准备工作。\x02\x03",
            "#10402F呵呵，你要不要也来一杯？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F喂喂……明天还要作战呢，\x01",
            "你们这样没问题吗？\x02\x03",
            "#00001F边上已经摆着很多\x01",
            "被你们喝空的杯子了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100F不必担心，\x01",
            "这是让维恩图斯特地\x01",
            "调制的无酒精鸡尾酒。\x02\x03",
            "不会对明天的作战\x01",
            "造成任何影响。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F啊，是这样啊……\x02\x03",
            "#00000F算啦，既然阿巴斯这么说，\x01",
            "那我这次就相信了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10409F呵呵，我一个人喝的时候，\x01",
            "你也应该相信啊。\x02\x03",
            "#10403F……对了，有件事情还是\x01",
            "通知你一声比较好。\x02\x03",
            "#10400F关于明天的作战，法王阁下\x01",
            "已经下达了正式的参战许可。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F啊……是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100F梅尔卡瓦的主要用途是执行\x01",
            "隐秘活动，本应尽量避免将其\x01",
            "使用于大规模的作战中……\x02\x03",
            "但考虑到整个大陆的混乱状况，\x01",
            "就算稍微有所暴露，也是没有办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F这样啊……\x01",
            "教会能做出这种判断，真是值得感谢。\x02\x03",
            "#00013F……总之，明天就要决战了，\x01",
            "还请二位助我一臂之力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10402F呵呵，明白了，队长。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#12102F我们自然会全力相助。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#11P#10403F对了……我刚想起来。\x01",
            "还有另外一件事，\x01",
            "也应该告诉你。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100F……瓦吉，\x01",
            "那件事情在目前\x01",
            "仍属于机密事项哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10405F哎，这样啊？\x02\x03",
            "#10409F呵呵，既然如此，\x01",
            "那我就只能偷偷地告诉你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5P#12100F……算了，既然瓦吉都\x01",
            "这么说了，那也没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00012F我、我完全听不懂\x01",
            "你们在说什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404F呵呵，这件事情\x01",
            "与你们有很大关系。\x02\x03",
            "#10402F如果你有兴趣，\x01",
            "待会就去甲板上等我吧，\x01",
            "这样我就可以偷偷告诉你了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 1)
    Jump("loc_59DE")

    label("loc_595F")


    ChrTalk(
        0xA,
        (
            "#11P#10404F还有另外一件事，\x01",
            "也应该告诉你。\x02\x03",
            "#10402F呵呵，如果你有兴趣，\x01",
            "待会就去甲板上等我吧，\x01",
            "这样我就可以偷偷告诉你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59DE")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受瓦吉的邀请\x01",      # 0
            "拒绝\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B01")

    ChrTalk(
        0x101,
        (
            "#6P#00006F……我知道了，\x01",
            "去甲板等你是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#10409F呵呵，就这么定了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#12100F瓦吉，谨慎起见，我话说在先，\x01",
            "你绝不能再泄露更多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#10404F呵呵，我知道啦。\x02\x03",
            "#10400F我喝完酒才会过去，\x01",
            "你不用着急哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 27)
    SetScenarioFlags(0x1AA, 7)
    Jump("loc_5B5E")

    label("loc_5B01")


    ChrTalk(
        0xA,
        (
            "#11P#10405F……这样吗？\x01",
            "那也无所谓……\x02\x03",
            "#10404F呵呵，如果你改变主意了，\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5B5E")

    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_26_52F2 end

    def Function_27_5B69(): pass

    label("Function_27_5B69")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_5C0E")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……必须去向艾莉道歉，\x01",
            "  告诉她我不能赴约了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德向艾莉道了歉，\x01",
            "取消了之前的约定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_5F75")

    label("loc_5C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_5CA8")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……必须去向缇欧道歉，\x01",
            "  告诉她我不能赴约了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德向缇欧道了歉，\x01",
            "取消了之前的约定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_5F75")

    label("loc_5CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_5D42")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……必须去向兰迪道歉，\x01",
            "  告诉他我不能赴约了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德向兰迪道了歉，\x01",
            "取消了之前的约定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_5F75")

    label("loc_5D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_5DE0")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……必须去向诺艾尔道歉，\x01",
            "  告诉她我不能赴约了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德向诺艾尔道了歉，\x01",
            "取消了之前的约定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_5F75")

    label("loc_5DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_5E7A")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……必须去向瓦吉道歉，\x01",
            "  告诉他我不能赴约了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德向瓦吉道了歉，\x01",
            "取消了之前的约定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_5F75")

    label("loc_5E7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_5F14")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F（……必须去向莉夏道歉，\x01",
            "  告诉她我不能赴约了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德向莉夏道了歉，\x01",
            "取消了之前的约定。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_5F75")

    label("loc_5F14")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F（……在休息室做好\x01",
            "  明天必要的准备工作之后，\x01",
            "  就去甲板吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5F75")

    Return()

    # Function_27_5B69 end

    def Function_28_5F76(): pass

    label("Function_28_5F76")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6571")
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 1420, 0, -92300, 90)
    OP_68(2300, 1000, -92050, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_6092")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（对了……之前和艾莉有约，\x01",
            "  得去甲板和她谈一些事情。）\x02\x03",
            "#00003F（…………………………………）\x02\x03",
            "#00000F（……如何？\x01",
            "  要先把明天的准备工作完成吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6405")

    label("loc_6092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_6142")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（对了……缇欧有事想和我商量，\x01",
            "  得去甲板和她碰面。）\x02\x03",
            "#00003F（…………………………………）\x02\x03",
            "#00000F（……如何？\x01",
            "  要先把明天的准备工作完成吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6405")

    label("loc_6142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_61F0")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（对了……兰迪有话想和我说，\x01",
            "  得去甲板和他碰面。）\x02\x03",
            "#00003F（…………………………………）\x02\x03",
            "#00000F（……如何？\x01",
            "  要先把明天的准备工作完成吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6405")

    label("loc_61F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_62A0")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（对了……诺艾尔有事想拜托我，\x01",
            "  得去甲板和她碰面。）\x02\x03",
            "#00003F（…………………………………）\x02\x03",
            "#00000F（……如何？\x01",
            "  要先把明天的准备工作完成吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6405")

    label("loc_62A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_635C")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（对了……瓦吉刚才说了一些很令人\x01",
            "  在意的话，得去甲板和他碰面。）\x02\x03",
            "#00003F（…………………………………）\x02\x03",
            "#00000F（……如何？\x01",
            "  要先把明天的准备工作完成吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6405")

    label("loc_635C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_6405")

    ChrTalk(
        0x101,
        (
            "#00005F#6P（对了……之前和莉夏有约，\x01",
            "  得去甲板上和她聊聊。）\x02\x03",
            "#00003F（…………………………………）\x02\x03",
            "#00000F（……如何？\x01",
            "  要先把明天的准备工作完成吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6405")

    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "一旦结束自由行动，本日就会结束，\x01",
            "剧情也会自动进展，敬请注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    '''

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情】\x01",                          # 0
            "【结束自由行动，去和约见的同伴会面】\x01",      # 1
        )
    )

    MenuEnd(0x0)

    '''

    optlist = \
    [
        '【还有其它事情】',
        '【结束自由行动，去和约见的同伴会面】',
        '【结束自由行动，依次和所有后宫会面】',
    ]

    CreateMenuAndShow(optlist)

    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_64D1"),
        (1, "loc_64D6"),
        (2, "fuck_all_member"),
        (SWITCH_DEFAULT, "loc_6558"),
    )

    label('fuck_all_member')

    StopSound(498, 1500, 70)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "之后，罗伊德为明日的解放作战做好了\x01",
            "必要的准备工作，来到了夜幕笼罩下的甲板。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)

    SetScenarioFlags(0x1AA, 3)
    SetScenarioFlags(0x1AA, 4)
    SetScenarioFlags(0x1AA, 5)
    SetScenarioFlags(0x1AA, 6)
    SetScenarioFlags(0x1AA, 7)
    SetScenarioFlags(0x1AB, 0)

    NewScene("e440c", 0, 0, 0)
    IdleLoop()
    Jump("loc_6558")



    label("loc_64D1")

    Jump("loc_6558")

    label("loc_64D6")

    StopSound(498, 1500, 70)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "之后，罗伊德为明日的解放作战做好了\x01",
            "必要的准备工作，来到了夜幕笼罩下的甲板。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("e440B", 0, 0, 0)
    IdleLoop()
    Jump("loc_6558")

    label("loc_6558")

    OP_5A()
    SetChrPos(0x0, 550, 0, -92390, 270)
    EventEnd(0x5)
    Jump("loc_686D")

    label("loc_6571")


    ChrTalk(
        0x101,
        (
            "#00005F（……今天是不是\x01",
            "  应该早点休息呢？）\x02\x03",
            "#00003F（但明天就要展开作战了，\x01",
            "  还是去确认一下大家的\x01",
            "  状态为好……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "如果选择在休息室休息，\x01",
            "本日就会结束，剧情也会\x01",
            "自动进展，敬请注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【还有其它事情】\x01",                # 0
            "【结束自由行动，入内休息】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BD")
    Jump("loc_686D")

    label("loc_66BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_686D")
    EventBegin(0x0)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#6P（……先在休息室做一番准备，\x01",
            "  然后就直接休息吧。）\x02\x03",
            "#00001F（解放克洛斯贝尔市的作战就在明天……\x01",
            "  无论如何也要取得成功！）\x02",
        )
    )

    CloseMessageWindow()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_67EB():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67EB)
    Sleep(1000)
    StopSound(498, 2000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    OP_21(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    EventEnd(0x3)

    label("loc_686D")

    TalkEnd(0xFF)
    Return()

    # Function_28_5F76 end

    def Function_29_6871(): pass

    label("Function_29_6871")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -150, 0, -88230, 180)
    EventEnd(0x5)
    Return()

    # Function_29_6871 end

    def Function_30_6891(): pass

    label("Function_30_6891")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50203.itc", 0x1E)
    LoadChrToIndex("chr/ch06902.itc", 0x1F)
    LoadChrToIndex("chr/ch06000.itc", 0x20)
    LoadChrToIndex("chr/ch05800.itc", 0x21)
    SoundLoad(943)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68CB")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_68CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68DE")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_68DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68F1")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_68F1")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 0x3)
    SetChrSubChip(0x105, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x4)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x13, 0x5)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x14)
    OP_70(0x1, 0x24)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "就这样，牢不可破、笼罩着整个\x01",
            "克洛斯贝尔市的『结界』消失了。\x02\x03",
            "罗伊德等人与『黑月』的曹，\x01",
            "以及反抗组织的米蕾优等人取得了联系……\x02\x03",
            "而索妮亚司令也作出了保证，\x01",
            "贝尔加德门和唐古拉姆门的\x01",
            "部队将会保持中立。\x02\x03",
            "入夜之后……\x02\x03",
            "众人在梅尔卡瓦的舰桥上\x01",
            "接到了凯文神父发来的联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x9, -3150, -1350, 7150, 315)
    SetChrPos(0x13, 2900, 0, -850, 0)
    SetChrPos(0x11, -3300, 0, 250, 45)
    SetChrPos(0x12, -3800, 0, -1000, 45)
    SetChrPos(0x8, 0, -1350, 6700, 0)
    SetChrPos(0xC, 3000, -1350, 6960, 45)
    SetChrPos(0x101, -750, 250, 200, 0)
    SetChrPos(0x102, 0, 0, -450, 0)
    SetChrPos(0x104, 650, 0, -1250, 0)
    SetChrPos(0x105, 0, 500, 2400, 0)
    SetChrPos(0x103, -1460, 0, -1190, 0)
    SetChrPos(0x109, -700, 0, -1770, 0)
    SetChrPos(0x106, 200, 0, -2200, 0)
    PlayBGM("ed7583", 0)
    Sound(498, 1, 80, 0)
    FadeToBright(1000, 0)
    OP_68(660, 800, 3830, 0)
    MoveCamera(44, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(22500, 2000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetMessageWindowPos(95, 70, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "也就是说，\x01",
            "我们就算进入克洛斯贝尔的领空，\x01",
            "也不会有遭到攻击的危险吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        (
            "#10403F#6P嗯，那些神机似乎\x01",
            "都在专心守卫都市。\x02\x03",
            "#10400F只要不接近克洛斯贝尔市，\x01",
            "应该就不会有问题。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "很好，这样一来，\x01",
            "总算是有点眉目了……\x02\x03",
            "天亮之后，我就会返回你们那边。\x02\x03",
            "至于具体的行动时机，\x01",
            "就等我们到了之后再商量吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10402F#6P呵呵，明白了。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(190, -1, -1, -1)
    SetChrName("莉丝的声音")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "#2S……凯文，换我说几句。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_70(0x1, 0x1F)
    Sound(73, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#00102F#12P莉丝小姐……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, -1, -1, -1)
    SetChrName("莉丝修女")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "……艾莉小姐，\x01",
            "你能平安无事，真是太好了。\x02\x03",
            "还有罗伊德警官和各位，\x01",
            "你们也一样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00002F#12P哈哈，托你们的福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12P哎呀～真没想到会以这种形式\x01",
            "和莉丝小姐交谈啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#12P#N你们会为我们的\x01",
            "突入作战提供协助吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(140, 70, -1, -1)
    SetChrName("莉丝修女")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "是的，我们准备用\x01",
            "这架梅尔卡瓦来吸引\x01",
            "那些保护都市的神机。\x02\x03",
            "不过，这样就不能同时对付\x01",
            "猎兵和国防军了……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#12P……这就足够了，\x01",
            "真是帮了我们的大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12P莉丝小姐、凯文神父，\x01",
            "真不知道该怎么感谢你们……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, -1, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "好啦，道谢的话，\x01",
            "还是留到作战成功之后再说吧。\x02\x03",
            "其实我们还打算\x01",
            "带来几个帮手……\x02\x03",
            "但即使如此，面对那些智能兵器，\x01",
            "恐怕还是没有什么胜算。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00208F#12P#N的确……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P总之，\x01",
            "你们千万不要太过逞强。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(105, -1, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "哈哈，多谢关心。\x02\x03",
            "瓦吉，\x01",
            "我们明天早上见。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10400F#6P嗯，我等你们。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(180, -1, -1, -1)
    SetChrName("莉丝修女")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "诸位再见。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_70(0x1, 0x1E)
    Sound(73, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Sound(943, 2, 60, 0)
    OP_71(0x1, 0x2F, 0x4C, 0x0, 0x8)
    OP_68(-340, 800, 2640, 2000)
    MoveCamera(40, 22, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(22440, 2000)
    Sleep(1000)
    SetChrFlags(0x13, 0x20)

    def lambda_721E():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_721E)
    Sleep(50)

    def lambda_722E():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_722E)
    Sleep(50)

    def lambda_723E():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_723E)
    Sleep(50)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x13, 0x20)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#02501F#5P唔，看来明天\x01",
            "将会是艰辛的一天啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02106F#6P#N是啊……\x01",
            "单看地面战力的差距，\x01",
            "也是总统一派占据上风。\x02\x03",
            "#02101F更麻烦的是，那些智能兵器\x01",
            "简直强得离谱。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x106,
        (
            "#10708F#12P据约鲁古大师说，\x01",
            "那架白色机体已经失去了\x01",
            "『消灭空间』的能力……\x02\x03",
            "#10701F不过，它的基础性能\x01",
            "却没有丝毫减弱吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#12100F#5P嗯，恐怕\x01",
            "正如你所说。\x02\x03",
            "看来有必要驾驶这艘九号机，\x01",
            "去探查一下白色机体的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P不管怎么说，都市周边一带\x01",
            "肯定会陷入胶着状态。\x02\x03",
            "#10401F而整个作战的关键，\x01",
            "就掌握在我们这些潜入队员的手中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12P嗯，我明白。\x02\x03",
            "#00013F……必须要想办法潜入市内，\x01",
            "与科长和达德利警官\x01",
            "他们会合。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11P话说回来，他们不要紧吧？\x02\x03",
            "#00301F听说和达德利警官的联络\x01",
            "在中途断开了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    ChrTalk(
        0x9,
        (
            "#02305F#5P多半是被通讯终端\x01",
            "强行切断了信号。\x02\x03",
            "#02303F终端拥有令特定的艾尼格玛号码\x01",
            "无法收发信号的机能。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#01901F#5P也就是说，总统一派的人\x01",
            "在市内可以随意联络，\x01",
            "而我们却不可以……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12P是的，所以我们要\x01",
            "控制住通讯终端。\x02\x03",
            "#00208F但通讯终端设置在兰花塔内，\x01",
            "恐怕无法轻易得手……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12P总而言之……\x01",
            "成败与否，全都要看明天早上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#12P嗯……\x01",
            "为了夺回琪雅……\x02\x03",
            "#00101F我们无论如何也要在\x01",
            "『解放克洛斯贝尔市作战』中取得成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P没错……大家今晚要\x01",
            "好好休息，养精蓄锐。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#5P船内有休息室，\x01",
            "如果累了，可以去里面休息。\x02\x03",
            "#00000F就让我们以最完美的状态……\x01",
            "共同迎接明天的早晨吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(290, 50, -1, -1)
    SetChrName("众人")

    AnonymousTalk(
        0xFF,
        "#4S好！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(22940, 2000)
    StopSound(498, 2000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearChrFlags(0x105, 0x4)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A5, 2)
    OP_29(0xB0, 0x4, 0x10)
    OP_29(0xB1, 0x4, 0x2)
    OP_29(0xB1, 0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_783B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_783B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7852")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7852")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7869")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7869")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7D), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7880")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7880")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7C), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7897")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7897")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7E), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_78AE")
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_78AE")

    OP_21(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7513", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(498, 1, 80, 0)
    OP_24(0x3AF)
    Sleep(500)
    SetScenarioFlags(0x22, 2)
    NewScene("e302B", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_6891 end

    SaveToFile()

Try(main)
