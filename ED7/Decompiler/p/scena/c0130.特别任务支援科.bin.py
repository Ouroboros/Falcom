from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0130.bin",                # FileName
        "c0130",                    # MapName
        "c0130",                    # Location
        0x0009,                     # 特别任务支援科
        "ed70150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0]\x00\x00\xf4\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\t\x00\x00\x01\x00\x02',
    )

    BuildStringList((
        "c0130",                  # 0
        "琪雅",                   # 1
        "琪雅",                   # 2
        "蔡特",                   # 3
        "SE控制",                 # 4
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08202.itc",                   # 01
        "chr/ch02707.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  8,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(158830,  0,       125480,  1200,    158830,  2000,    125480,  0x007C, 0,  27, 0x0000)
    DeclActor(155320,  30,      123780,  1200,    155320,  1500,    123780,  0x007C, 0,  28, 0x0000)
    DeclActor(205730,  0,       130250,  1200,    205730,  1500,    130250,  0x007C, 0,  30, 0x0000)
    DeclActor(208820,  0,       123770,  1200,    208820,  2500,    123770,  0x007C, 0,  31, 0x0000)
    DeclActor(259740,  0,       121980,  1200,    259740,  3000,    121980,  0x007C, 0,  32, 0x0000)
    DeclActor(259339,  0,       126100,  1200,    259339,  1500,    126100,  0x007C, 0,  33, 0x0000)
    DeclActor(255780,  30,      65319,   1200,    255780,  1500,    65319,   0x007C, 0,  34, 0x0000)
    DeclActor(257120,  30,      68930,   1200,    257120,  1030,    68930,   0x007C, 0,  35, 0x0000)
    DeclActor(259010,  0,       66930,   1200,    259010,  1000,    66930,   0x007C, 0,  36, 0x0000)
    DeclActor(255680,  30,      73720,   1200,    255680,  1500,    73720,   0x007C, 0,  37, 0x0000)
    DeclActor(258000,  0,       63980,   1200,    258000,  2000,    63980,   0x007C, 0,  38, 0x0000)
    DeclActor(153580,  30,      127880,  1200,    153370,  1530,    128389,  0x007C, 0,  24, 0x0000)
    DeclActor(207040,  30,      128539,  1200,    207640,  1500,    129090,  0x007C, 0,  25, 0x0000)
    DeclActor(258360,  0,       128430,  1200,    258360,  1500,    128430,  0x007C, 0,  26, 0x0000)
    DeclActor(253320,  30,      71340,   1200,    253320,  1500,    71340,   0x007C, 0,  12, 0x0000)

    ChipFrameInfo(1472, 0)                                       # 0

    ScpFunction((
        "Function_0_5C0",          # 00, 0
        "Function_1_670",          # 01, 1
        "Function_2_950",          # 02, 2
        "Function_3_CDC",          # 03, 3
        "Function_4_F3C",          # 04, 4
        "Function_5_FE8",          # 05, 5
        "Function_6_13A4",         # 06, 6
        "Function_7_19AB",         # 07, 7
        "Function_8_19F6",         # 08, 8
        "Function_9_1A41",         # 09, 9
        "Function_10_1AE2",        # 0A, 10
        "Function_11_1B83",        # 0B, 11
        "Function_12_1BD2",        # 0C, 12
        "Function_13_25BC",        # 0D, 13
        "Function_14_2814",        # 0E, 14
        "Function_15_2A90",        # 0F, 15
        "Function_16_2C8B",        # 10, 16
        "Function_17_2E98",        # 11, 17
        "Function_18_3093",        # 12, 18
        "Function_19_328E",        # 13, 19
        "Function_20_3490",        # 14, 20
        "Function_21_3692",        # 15, 21
        "Function_22_3A3A",        # 16, 22
        "Function_23_3B50",        # 17, 23
        "Function_24_3BA3",        # 18, 24
        "Function_24_3BA3",        # 19, 25
        "Function_24_3BA3",        # 1A, 26
        "Function_27_3D80",        # 1B, 27
        "Function_28_3E31",        # 1C, 28
        "Function_29_3F0A",        # 1D, 29
        "Function_30_3F13",        # 1E, 30
        "Function_31_3FC6",        # 1F, 31
        "Function_32_4077",        # 20, 32
        "Function_33_4126",        # 21, 33
        "Function_34_41D9",        # 22, 34
        "Function_35_428A",        # 23, 35
        "Function_36_433B",        # 24, 36
        "Function_37_43EC",        # 25, 37
        "Function_38_44A1",        # 26, 38
        "Function_39_4558",        # 27, 39
        "Function_40_45CD",        # 28, 40
        "Function_41_45FC",        # 29, 41
        "Function_42_462B",        # 2A, 42
        "Function_43_465A",        # 2B, 43
        "Function_44_4689",        # 2C, 44
        "Function_45_518D",        # 2D, 45
        "Function_46_5195",        # 2E, 46
        "Function_47_610D",        # 2F, 47
        "Function_48_6167",        # 30, 48
        "Function_49_6183",        # 31, 49
        "Function_50_6B96",        # 32, 50
        "Function_51_6BB2",        # 33, 51
        "Function_52_844B",        # 34, 52
        "Function_53_849A",        # 35, 53
        "Function_54_84C3",        # 36, 54
        "Function_55_8562",        # 37, 55
        "Function_56_8579",        # 38, 56
        "Function_57_8590",        # 39, 57
        "Function_58_85A7",        # 3A, 58
        "Function_59_85BE",        # 3B, 59
        "Function_60_85DA",        # 3C, 60
        "Function_61_85F6",        # 3D, 61
        "Function_62_8612",        # 3E, 62
        "Function_63_8651",        # 3F, 63
        "Function_64_8697",        # 40, 64
        "Function_65_86C4",        # 41, 65
        "Function_66_86E0",        # 42, 66
        "Function_67_8710",        # 43, 67
        "Function_68_872C",        # 44, 68
        "Function_69_8FBC",        # 45, 69
        "Function_70_9011",        # 46, 70
        "Function_71_9069",        # 47, 71
        "Function_72_90C1",        # 48, 72
        "Function_73_9119",        # 49, 73
        "Function_74_9B3D",        # 4A, 74
    ))




    label("Function_24_3BA3")

    import TiosBed
    TiosBed.ShowMenu()
    Return()



    def Function_0_5C0(): pass

    label("Function_0_5C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5F8"),
        (1, "loc_604"),
        (2, "loc_610"),
        (3, "loc_61C"),
        (4, "loc_628"),
        (5, "loc_634"),
        (6, "loc_640"),
        (SWITCH_DEFAULT, "loc_64C"),
    )


    label("loc_5F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_604")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_610")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_61C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_628")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_634")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_640")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_64C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_658")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_66F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_658")

    label("loc_66F")

    Return()

    # Function_0_5C0 end

    def Function_1_670(): pass

    label("Function_1_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Event(0, 16)

    label("loc_6A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34A, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CC")
    Event(0, 15)

    label("loc_6CC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F3")
    Event(0, 18)

    label("loc_6F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71A")
    Event(0, 17)

    label("loc_71A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x351, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_741")
    Event(0, 20)

    label("loc_741")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x350, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_768")
    Event(0, 19)

    label("loc_768")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_783")
    Event(0, 5)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x358, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB")
    Event(0, 21)

    label("loc_7BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    Event(0, 21)

    label("loc_7D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F3")
    Event(0, 21)

    label("loc_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80F")
    Event(0, 21)

    label("loc_80F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82B")
    Event(0, 21)

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_839")
    Jump("loc_935")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_889")
    OP_A3(0x8, 0x80)
    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    OP_A3(0x8, 0x1)
    SetChrPos(0x8, 257500, 500, 68000, 270)
    SetChrPos(0xA, 258550, 0, 66740, 180)
    Jump("loc_935")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_897")
    Jump("loc_935")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D6")
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 257500, 500, 68000, 270)
    OP_A3(0x8, 0x1)

    label("loc_8D6")

    Jump("loc_935")

    label("loc_8DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E9")
    Jump("loc_935")

    label("loc_8E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8F7")
    Jump("loc_935")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_92C")
    OP_A3(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x8, 254100, 200, 71300, 270)
    Jump("loc_935")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_935")

    label("loc_935")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94F")
    Event(0, 68)

    label("loc_94F")

    Return()

    # Function_1_670 end

    def Function_2_950(): pass

    label("Function_2_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_963")
    OP_1B(0x2, 0x0, 0x49)

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AD")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    OP_76(0xFF, "wlight_add", 0x0, 0x1)
    OP_76(0xFF, "ylight_add", 0x0, 0x1)
    OP_76(0xFF, "out_add", 0x0, 0x1)

    label("loc_9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A01")
    OP_76(0xFF, "wlight_add", 0x0, 0x1)
    OP_76(0xFF, "ylight_add", 0x0, 0x1)
    OP_76(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A86")
    OP_76(0xFF, "danbo", 0x1, 0x1)
    OP_76(0xFF, "n01", 0x0, 0x1)
    OP_76(0xFF, "n02", 0x0, 0x1)
    OP_76(0xFF, "n03", 0x0, 0x1)
    OP_76(0xFF, "asihuki", 0x0, 0x1)
    OP_1D(0x0, 0x0, 0x1, 0x0, 0x3E670, 0xFFFFFC18, 0x1F784, 0x1F40, 0x1388, 0x0)
    OP_1D(0x0, 0x1, 0x1, 0x0, 0x3F353, 0xFFFFFC18, 0x1EC30, 0x1388, 0x1388, 0x15F90)
    Jump("loc_AC3")

    label("loc_A86")

    OP_76(0xFF, "danbo", 0x0, 0x1)
    OP_76(0xFF, "n01", 0x1, 0x1)
    OP_76(0xFF, "n02", 0x1, 0x1)
    OP_76(0xFF, "n03", 0x1, 0x1)
    OP_76(0xFF, "asihuki", 0x1, 0x1)

    label("loc_AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADD")
    OP_72(0x8, 0x4)
    OP_73(0x8, 0x2)
    OP_65(0x2, 0x1)

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B08")
    OP_72(0x9, 0x4)
    OP_73(0x9, 0x2)
    OP_65(0x3, 0x1)
    OP_72(0x14, 0x4)
    OP_73(0x14, 0x2)
    Jump("loc_B0E")

    label("loc_B08")

    OP_72(0x13, 0x4)

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B28")
    OP_72(0xA, 0x4)
    OP_73(0xA, 0x2)
    OP_65(0x4, 0x1)

    label("loc_B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B42")
    OP_72(0xB, 0x4)
    OP_73(0xB, 0x2)
    OP_65(0x5, 0x1)

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B60")
    OP_72(0xC, 0x4)
    OP_73(0xC, 0x2)
    OP_65(0x6, 0x1)

    label("loc_B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B7E")
    OP_72(0xD, 0x4)
    OP_73(0xD, 0x2)
    OP_65(0x7, 0x1)

    label("loc_B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B98")
    OP_72(0xE, 0x4)
    OP_73(0xE, 0x2)
    OP_65(0x8, 0x1)

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB2")
    OP_72(0xF, 0x4)
    OP_73(0xF, 0x2)
    OP_65(0x9, 0x1)

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC")
    OP_72(0x10, 0x4)
    OP_73(0x10, 0x2)
    OP_65(0xA, 0x1)

    label("loc_BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE6")
    OP_72(0x11, 0x4)
    OP_73(0x11, 0x2)
    OP_65(0xB, 0x1)

    label("loc_BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C00")
    OP_72(0x12, 0x4)
    OP_73(0x12, 0x2)
    OP_65(0xC, 0x1)

    label("loc_C00")

    OP_65(0x10, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x64), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6F")
    LoadEffect(0x10, "event\\eva00_00.eff")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 253320, 1200, 71340, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x10, 0x1)

    label("loc_C6F")

    OP_73(0x1, 0x10)
    OP_73(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C8E")
    OP_72(0x1, 0x10)
    OP_65(0x0, 0x1)

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CA1")
    OP_72(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_CA1")

    OP_B7(0x0, 0x0, 0x80)
    OP_B7(0x0, 0x1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC3")
    OP_B7(0x1, 0x0, 0x80)
    OP_B7(0x1, 0x1, 0x80)

    label("loc_CC3")

    OP_B7(0x0, 0x2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CDB")
    OP_B7(0x1, 0x2, 0x80)

    label("loc_CDB")

    Return()

    # Function_2_950 end

    def Function_3_CDC(): pass

    label("Function_3_CDC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CED")
    Jump("loc_F38")

    label("loc_CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D08")
    Call(0, 74)
    Jump("loc_D8B")

    label("loc_D08")


    ChrTalk(
        0x8,
        (
            "#01108F诺艾尔离开这里，\x01",
            "琪雅也会寂寞的……\x01",
            "不过，要打起精神哦，诺艾尔。\x02\x03",
            "#01102F我还等着芙兰康复之后，\x01",
            "你们两个一起过来玩呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8B")

    Jump("loc_F38")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D9E")
    Jump("loc_F38")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB8")
    TalkEnd(0xFE)
    Call(0, 6)
    Return()

    label("loc_DB8")

    Jump("loc_F38")

    label("loc_DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEC")

    ChrTalk(
        0x8,
        "#01105F啊，罗伊德，你们要出去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F嗯，琪雅要做主日学校的作业吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01100F嗯，今天没办法出去玩，\x01",
            "所以想先做完作业。\x02\x03",
            "#01106F其实我还想\x01",
            "坐那辆车呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F唔，真可惜啊。\x02\x03",
            "#10109F下次找个晴天的休息日，\x01",
            "大家开车去兜风吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01109F嗯！我很期待哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 1)
    Jump("loc_F38")

    label("loc_EEC")


    ChrTalk(
        0x8,
        (
            "#01109F嘿嘿，\x01",
            "晴天快点来吧。\x02\x03",
            "#01110F好，今天要干脆利落地\x01",
            "把作业写完！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F38")

    TalkEnd(0xFE)
    Return()

    # Function_3_CDC end

    def Function_4_F3C(): pass

    label("Function_4_F3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")

    ChrTalk(
        0xA,
        "#01203F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F蔡特对诺艾尔小姐说\x01",
            "『多保重啊』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F哈哈……\x01",
            "谢谢，蔡特。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FE4")

    label("loc_FC7")


    ChrTalk(
        0xA,
        "#01203F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_FE4")

    TalkEnd(0xFE)
    Return()

    # Function_4_F3C end

    def Function_5_FE8(): pass

    label("Function_5_FE8")

    EventBegin(0x0)
    Fade(500)
    OP_68(256649, 800, 124480, 0)
    OP_6D(0x1A, 0x16, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x5FB4, 0x0)
    SetChrPos(0x102, 257410, 0, 124690, 45)
    SetChrPos(0x101, 255000, 0, 124690, 315)
    SetChrPos(0x109, 256829, 0, 121730, 0)
    SetChrPos(0x105, 255220, 0, 122530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1082")
    SetChrPos(0x1A5, 256209, 0, 125400, 0)

    label("loc_1082")

    OP_0D()

    ChrTalk(
        0x109,
        (
            "#12P#10100F那个……这里是我的房间。\x02\x03",
            "#10106F我的房间里没什么陈设，\x01",
            "有些不好意思……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，只要收拾整洁\x01",
            "不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102F嗯，很有诺艾尔小姐的风格，\x01",
            "我觉得很不错。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1232")
    OP_93(0x1A5, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A5,
        (
            "#5P#01105F啊，那个小熊\x01",
            "是哪里来的？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_118D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_118D)

    def lambda_119A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_119A)
    Sleep(50)

    def lambda_11AA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11AA)
    Sleep(50)

    def lambda_11BA():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11BA)
    WaitChrThread(0x109, 0x1)

    ChrTalk(
        0x109,
        (
            "#12P#10109F哈哈……\x01",
            "那是和芙兰一起买的\x01",
            "成对玩偶。\x02\x03",
            "#10100F原本放在警备队的值班室，\x01",
            "被我带过来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12FE")

    label("loc_1232")

    OP_93(0x101, 0x87, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#5P#00000F啊，放在那里的\x01",
            "那个玩偶是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_126B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_126B)
    Sleep(50)

    def lambda_127B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_127B)
    Sleep(50)

    def lambda_128B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128B)
    WaitChrThread(0x109, 0x1)

    ChrTalk(
        0x109,
        (
            "#12P#10109F哈哈……\x01",
            "那是和芙兰一起买的\x01",
            "成对玩偶。\x02\x03",
            "#10100F原本放在警备队的值班室，\x01",
            "被我带过来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FE")


    ChrTalk(
        0x101,
        (
            "#5P#00000F哈哈，原来如此，\x01",
            "摆在这里当装饰，看起来很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100F呵呵，谢谢。\x02\x03",
            "#10104F那个……我礼数不周，\x01",
            "请大家多多包涵了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 256010, 0, 121130, 0)
    SetScenarioFlags(0x13B, 6)
    EventEnd(0x5)
    Return()

    # Function_5_FE8 end

    def Function_6_13A4(): pass

    label("Function_6_13A4")

    EventBegin(0x0)
    Fade(500)
    OP_68(256920, 1000, 67670, 0)
    OP_6D(0x32, 0x15, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    SetChrPos(0x101, 255850, 0, 68670, 135)
    SetChrPos(0x102, 256720, 30, 66620, 45)
    SetChrPos(0x103, 254820, 30, 69190, 135)
    SetChrPos(0x104, 254420, 0, 67580, 90)
    SetChrPos(0x109, 255300, 30, 66540, 56)
    SetChrPos(0x105, 258360, 0, 66040, 0)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_1458():

        label("loc_1458")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1458")

    QueueWorkItem2(0x101, 2, lambda_1458)

    def lambda_146A():

        label("loc_146A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_146A")

    QueueWorkItem2(0x102, 2, lambda_146A)

    def lambda_147C():

        label("loc_147C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_147C")

    QueueWorkItem2(0x103, 2, lambda_147C)

    def lambda_148E():

        label("loc_148E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_148E")

    QueueWorkItem2(0x104, 2, lambda_148E)

    def lambda_14A0():

        label("loc_14A0")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_14A0")

    QueueWorkItem2(0x109, 2, lambda_14A0)

    def lambda_14B2():

        label("loc_14B2")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_14B2")

    QueueWorkItem2(0x105, 2, lambda_14B2)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P#01110F啊，大家……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00200F琪雅……没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108F从昨天开始，\x01",
            "你就一直没什么精神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01102F嘿嘿，嗯，\x01",
            "琪雅没事，不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#11P#01103F罗伊德……\x02\x03",
            "#01108F滴的眼睛\x01",
            "真的很难治好吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_END)), "loc_1647")

    ChrTalk(
        0x101,
        (
            "#6P#00003F……嗯，\x01",
            "我想应该很难。\x02\x03",
            "#00000F不过，小滴\x01",
            "仍然非常乐观哦。\x02\x03",
            "不但没有消沉，\x01",
            "还因为治疗可以算是\x01",
            "有进展的而很开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169F")

    label("loc_1647")


    ChrTalk(
        0x101,
        (
            "#6P#00003F……嗯，\x01",
            "我想应该很难。\x02\x03",
            "#00008F不过，\x01",
            "这次的手术也不能\x01",
            "算是完全失败……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169F")


    ChrTalk(
        0x8,
        "#11P#01106F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F阿琪，\x01",
            "我知道你很沮丧……\x01",
            "但还是努力打起精神吧。\x02\x03",
            "#00300F小滴肯定也\x01",
            "不希望阿琪这样\x01",
            "消沉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103F是、是啊，小琪雅。\x02\x03",
            "#10102F你露出笑容，\x01",
            "才能让小滴\x01",
            "更加开心！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01108F……嗯，说的也是。\x02\x03",
            "#01102F琪雅是滴的好朋友……\x01",
            "为了她，下次见面时一定要打起精神。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_A3(0x8, 0x4)
    OP_A3(0x8, 0x20)
    OP_A3(0x8, 0x2)
    OP_A2(0x8, 0x1)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 256600, 0, 67990, 270)
    OP_A2(0x8, 0x40)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11P#01109F嘿嘿，谢谢大家，\x01",
            "心情已经好一点啦。\x02\x03",
            "#01100F对了，我和朋友们有约，\x01",
            "这就要出去玩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F哦……路上小心。\x02",
    )

    CloseMessageWindow()
    OP_95(0x8, 0x3D9A0, 0x0, 0x100FE, 0x7D0, 0x1)

    def lambda_18B2():
        OP_95(0xFE, 0x3D590, 0x0, 0x100EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18B2)

    def lambda_18CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_18CC)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    OP_A2(0x8, 0x80)
    EndChrThread(0x0, 0x2)
    EndChrThread(0x1, 0x2)
    EndChrThread(0x2, 0x2)
    EndChrThread(0x3, 0x2)
    EndChrThread(0x4, 0x2)
    EndChrThread(0x5, 0x2)
    Sleep(200)
    Sound(104, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#11P#10308F……不要紧吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F不知道……\x01",
            "不过，琪雅一定\x01",
            "能振作精神的。\x02\x03",
            "#00000F好了，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_A2(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_A2(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 255390, 0, 67800, 225)
    SetScenarioFlags(0x170, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_6_13A4 end

    def Function_7_19AB(): pass

    label("Function_7_19AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BD")
    Call(0, 13)
    Jump("loc_19F5")

    label("loc_19BD")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000F这是缇欧的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_19F5")

    Return()

    # Function_7_19AB end

    def Function_8_19F6(): pass

    label("Function_8_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A08")
    Call(0, 14)
    Jump("loc_1A40")

    label("loc_1A08")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000F这是兰迪的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1A40")

    Return()

    # Function_8_19F6 end

    def Function_9_1A41(): pass

    label("Function_9_1A41")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",
            "科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F说的也是，我们去叫她吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1A41 end

    def Function_10_1AE2(): pass

    label("Function_10_1AE2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",
            "科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F说的也是，我们去叫她吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_1AE2 end

    def Function_11_1B83(): pass

    label("Function_11_1B83")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000F琪雅要去主日学校上课，\x01",
            "从后门出去比较近。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1B83 end

    def Function_12_1BD2(): pass

    label("Function_12_1BD2")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    StopEffect(0x9, 0x0)
    OP_65(0x10, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis382.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis383.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis384.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis385.itp")
    OP_68(253680, 1430, 71690, 0)
    OP_6D(0x2C, 0x15, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x5208, 0x0)
    SetChrPos(0x101, 254540, 30, 72300, 225)
    SetChrPos(0x102, 253960, 30, 69890, 315)
    SetChrPos(0x103, 255030, 30, 71510, 270)
    SetChrPos(0x104, 255370, 30, 70080, 315)
    SetChrPos(0xF4, 256240, 30, 72240, 270)
    SetChrPos(0xF5, 256019, 30, 71220, 270)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F这是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#12P#00302F咦，白色的石头，\x01",
            "还挺漂亮的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00205F这好像是……\x02\x03",
            "#00200F罗伊德前辈在米修拉姆\x01",
            "送给琪雅的吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F嗯，是我在米修拉姆的沙滩上\x01",
            "送给琪雅的『纯白之石』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108F琪雅离开的时候，\x01",
            "把它忘在这里了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德拿起了纯白之石。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0xBB8)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(824, 0, 100, 0)
    Sleep(1000)
    Sound(2955, 255, 50, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#30W…………哎………………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70534", 0)
    Sound(824, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(2956, 255, 50, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2600)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    Sound(2957, 255, 60, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sound(2958, 255, 75, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sound(2959, 255, 90, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    Sleep(2000)
    Sound(2960, 255, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(2500)
    FadeToDark(2000, 16777215, -1)
    Sound(829, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    OP_0D()
    OP_6C(0x4A38, 0x0)
    OP_6C(0x5208, 0x7D0)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#40W……………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2110")

    ChrTalk(
        0x106,
        (
            "#11P#10708F#30W刚、刚才那是……\x01",
            "小琪雅……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2192")

    label("loc_2110")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2157")

    ChrTalk(
        0x109,
        (
            "#11P#10113F#30W刚、刚才那是……\x01",
            "小琪雅……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2192")

    label("loc_2157")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2192")

    ChrTalk(
        0x105,
        "#11P#10408F#30W刚才那是……琪雅……？\x02",
    )

    CloseMessageWindow()

    label("loc_2192")


    ChrTalk(
        0x104,
        (
            "#12P#00301F#30W应该没错。\x01",
            "……不过，是从哪里……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#00206F#30W可以从罗伊德前辈\x01",
            "手中的石头里感觉到\x01",
            "残留于其中的感情。\x02\x03",
            "#00208F……似乎是把\x01",
            "悲哀和迷茫硬塞进去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106F#30W小琪雅……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22C9")

    ChrTalk(
        0x10A,
        (
            "#11P#00608F#30W……真是的……\x01",
            "那个不通世事、天真无邪的孩子竟然……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236A")

    label("loc_22C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_231C")

    ChrTalk(
        0x105,
        (
            "#11P#10408F#30W……哎呀呀，\x01",
            "那么天真无邪的小孩子竟然……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236A")

    label("loc_231C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_236A")

    ChrTalk(
        0x109,
        (
            "#11P#10106F#30W……竟然让小琪雅\x01",
            "背负着如此沉重的感情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236A")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#30W……现在……\x01",
            "连最后的一丝踌躇也完全消失了。\x02\x03",
            "#00015F琪雅竟然……\x01",
            "一直在拼命压抑\x01",
            "自己的真实感情……\x02\x03",
            "#00010F这种状况，一定有哪里不对！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F是啊……这种局面\x01",
            "肯定是不正确的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00307F……既然如此，\x01",
            "我们无论如何也要\x01",
            "到阿琪的身边！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00201F嗯，为了让琪雅\x01",
            "恢复笑容，我们一定要……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00007F是啊……走吧，各位。\x02\x03",
            "#00003F（琪雅……等着我，\x01",
            "  我一定会去接你……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xBB8)
    OP_6C(0x537F, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x1F, 0x3A1),
            scpstr(0x7, 0x2),
            scpstr(0x7, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_5A()
    AddItemNumber(0x3A1, 1)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(10)
    OP_1F()
    OP_A2(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_A2(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 254410, 30, 69820, 225)
    SetScenarioFlags(0x1BC, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B9")
    OP_E0(0x34, 0x0)

    label("loc_25B9")

    EventEnd(0x5)
    Return()

    # Function_12_1BD2 end

    def Function_13_25BC(): pass

    label("Function_13_25BC")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    OP_6D(0x2B, 0x19, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x5D34, 0x0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2656")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_2656")

    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00100F这是缇欧的房间呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300F她现在正在\x01",
            "列曼自治州出差吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F嗯，她和约纳\x01",
            "一起去了爱普斯泰恩\x01",
            "财团的研究所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F由于自治州法的修正，\x01",
            "导力网络在今后将会进一步普及，\x01",
            "他们好像正在准备那方面的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103F听起来真是复杂……\x01",
            "看来他们那边的工作也很辛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27D4")

    ChrTalk(
        0x1A5,
        "#12P#01100F真希望缇欧早点回来～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27FC")

    label("loc_27D4")


    ChrTalk(
        0x101,
        (
            "#00000F嗯，真希望她能\x01",
            "早日回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FC")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_13_25BC end

    def Function_14_2814(): pass

    label("Function_14_2814")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    OP_6D(0x29, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x5CF8, 0x0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28AE")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_28AE")

    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000F这是兰迪的房间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F兰迪现在正带领着\x01",
            "贝尔加德门的部队\x01",
            "进行复健训练吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F哦，据说是因为士兵们\x01",
            "在教团事件中被骗服了那种药物？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103F嗯……\x01",
            "虽然还没有严重到\x01",
            "会留下后遗症的程度……\x02\x03",
            "#10108F但想恢复原有的体力与手感，\x01",
            "似乎还要花上一段时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F是吗……\x01",
            "希望警备队能尽快重振雄风啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A50")

    ChrTalk(
        0x1A5,
        "#12P#01100F也希望兰迪早点回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A78")

    label("loc_2A50")


    ChrTalk(
        0x102,
        (
            "#00100F是啊，也希望兰迪\x01",
            "早日回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A78")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_14_2814 end

    def Function_15_2A90(): pass

    label("Function_15_2A90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_73(0x8, 0x4)
    OP_72(0x8, 0x2)
    OP_68(157620, 1330, 125080, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AEA")
    OP_A2(0x0, 0x8)

    label("loc_2AEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AFD")
    OP_A2(0x1, 0x8)

    label("loc_2AFD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B10")
    OP_A2(0x2, 0x8)

    label("loc_2B10")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B23")
    OP_A2(0x3, 0x8)

    label("loc_2B23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B36")
    OP_A2(0x4, 0x8)

    label("loc_2B36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B49")
    OP_A2(0x5, 0x8)

    label("loc_2B49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B62")
    OP_A3(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_2B62")

    OP_A3(0x102, 0x8)
    SetChrPos(0x102, 157620, 30, 125080, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100F放在这里如何？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "艾莉的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34A, 1)
    SetScenarioFlags(0x13C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x2, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BFF")
    OP_A3(0x0, 0x8)

    label("loc_2BFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C12")
    OP_A3(0x1, 0x8)

    label("loc_2C12")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C25")
    OP_A3(0x2, 0x8)

    label("loc_2C25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C38")
    OP_A3(0x3, 0x8)

    label("loc_2C38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4B")
    OP_A3(0x4, 0x8)

    label("loc_2C4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C5E")
    OP_A3(0x5, 0x8)

    label("loc_2C5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C77")
    OP_A2(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_2C77")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_15_2A90 end

    def Function_16_2C8B(): pass

    label("Function_16_2C8B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_73(0x9, 0x4)
    OP_72(0x9, 0x2)
    OP_72(0x13, 0x4)
    OP_73(0x14, 0x4)
    OP_72(0x14, 0x2)
    OP_68(154920, 1330, 122580, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CF7")
    OP_A2(0x0, 0x8)

    label("loc_2CF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D0A")
    OP_A2(0x1, 0x8)

    label("loc_2D0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D1D")
    OP_A2(0x2, 0x8)

    label("loc_2D1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D30")
    OP_A2(0x3, 0x8)

    label("loc_2D30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D43")
    OP_A2(0x4, 0x8)

    label("loc_2D43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D56")
    OP_A2(0x5, 0x8)

    label("loc_2D56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2D6F")
    OP_A3(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_2D6F")

    OP_A3(0x102, 0x8)
    SetChrPos(0x102, 154920, 30, 122580, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#0100F放在这里如何？\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "艾莉的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34B, 1)
    SetScenarioFlags(0x13C, 7)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x3, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 44)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E0C")
    OP_A3(0x0, 0x8)

    label("loc_2E0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E1F")
    OP_A3(0x1, 0x8)

    label("loc_2E1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E32")
    OP_A3(0x2, 0x8)

    label("loc_2E32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E45")
    OP_A3(0x3, 0x8)

    label("loc_2E45")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E58")
    OP_A3(0x4, 0x8)

    label("loc_2E58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E6B")
    OP_A3(0x5, 0x8)

    label("loc_2E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E84")
    OP_A2(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_2E84")

    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_16_2C8B end

    def Function_17_2E98(): pass

    label("Function_17_2E98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_73(0xA, 0x4)
    OP_72(0xA, 0x2)
    OP_68(206000, 1300, 129509, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EF2")
    OP_A2(0x0, 0x8)

    label("loc_2EF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F05")
    OP_A2(0x1, 0x8)

    label("loc_2F05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F18")
    OP_A2(0x2, 0x8)

    label("loc_2F18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F2B")
    OP_A2(0x3, 0x8)

    label("loc_2F2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F3E")
    OP_A2(0x4, 0x8)

    label("loc_2F3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F51")
    OP_A2(0x5, 0x8)

    label("loc_2F51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F6A")
    OP_A3(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_2F6A")

    OP_A3(0x103, 0x8)
    SetChrPos(0x103, 206000, 0, 129509, 0)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "缇欧的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34C, 1)
    SetScenarioFlags(0x13D, 0)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3007")
    OP_A3(0x0, 0x8)

    label("loc_3007")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_301A")
    OP_A3(0x1, 0x8)

    label("loc_301A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_302D")
    OP_A3(0x2, 0x8)

    label("loc_302D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3040")
    OP_A3(0x3, 0x8)

    label("loc_3040")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3053")
    OP_A3(0x4, 0x8)

    label("loc_3053")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3066")
    OP_A3(0x5, 0x8)

    label("loc_3066")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_307F")
    OP_A2(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_307F")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_17_2E98 end

    def Function_18_3093(): pass

    label("Function_18_3093")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_73(0xB, 0x4)
    OP_72(0xB, 0x2)
    OP_68(208220, 1300, 123970, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30ED")
    OP_A2(0x0, 0x8)

    label("loc_30ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3100")
    OP_A2(0x1, 0x8)

    label("loc_3100")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3113")
    OP_A2(0x2, 0x8)

    label("loc_3113")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3126")
    OP_A2(0x3, 0x8)

    label("loc_3126")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3139")
    OP_A2(0x4, 0x8)

    label("loc_3139")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_314C")
    OP_A2(0x5, 0x8)

    label("loc_314C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3165")
    OP_A3(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_3165")

    OP_A3(0x103, 0x8)
    SetChrPos(0x103, 208220, 0, 123970, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "缇欧的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34D, 1)
    SetScenarioFlags(0x13D, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 46)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3202")
    OP_A3(0x0, 0x8)

    label("loc_3202")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3215")
    OP_A3(0x1, 0x8)

    label("loc_3215")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3228")
    OP_A3(0x2, 0x8)

    label("loc_3228")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_323B")
    OP_A3(0x3, 0x8)

    label("loc_323B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_324E")
    OP_A3(0x4, 0x8)

    label("loc_324E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3261")
    OP_A3(0x5, 0x8)

    label("loc_3261")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_327A")
    OP_A2(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_327A")

    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_18_3093 end

    def Function_19_328E(): pass

    label("Function_19_328E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_73(0xC, 0x4)
    OP_72(0xC, 0x2)
    OP_68(258329, 1300, 122180, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E8")
    OP_A2(0x0, 0x8)

    label("loc_32E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32FB")
    OP_A2(0x1, 0x8)

    label("loc_32FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330E")
    OP_A2(0x2, 0x8)

    label("loc_330E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3321")
    OP_A2(0x3, 0x8)

    label("loc_3321")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3334")
    OP_A2(0x4, 0x8)

    label("loc_3334")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3347")
    OP_A2(0x5, 0x8)

    label("loc_3347")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3360")
    OP_A3(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3360")

    OP_A3(0x109, 0x8)
    SetChrPos(0x109, 258329, 0, 122180, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100F放在这里应该不错。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "诺艾尔的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x13D, 2)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3404")
    OP_A3(0x0, 0x8)

    label("loc_3404")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3417")
    OP_A3(0x1, 0x8)

    label("loc_3417")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_342A")
    OP_A3(0x2, 0x8)

    label("loc_342A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343D")
    OP_A3(0x3, 0x8)

    label("loc_343D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3450")
    OP_A3(0x4, 0x8)

    label("loc_3450")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3463")
    OP_A3(0x5, 0x8)

    label("loc_3463")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_347C")
    OP_A2(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_347C")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_19_328E end

    def Function_20_3490(): pass

    label("Function_20_3490")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_73(0xD, 0x4)
    OP_72(0xD, 0x2)
    OP_68(258149, 1300, 125700, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x61A8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34EA")
    OP_A2(0x0, 0x8)

    label("loc_34EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34FD")
    OP_A2(0x1, 0x8)

    label("loc_34FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3510")
    OP_A2(0x2, 0x8)

    label("loc_3510")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3523")
    OP_A2(0x3, 0x8)

    label("loc_3523")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3536")
    OP_A2(0x4, 0x8)

    label("loc_3536")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3549")
    OP_A2(0x5, 0x8)

    label("loc_3549")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3562")
    OP_A3(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_3562")

    OP_A3(0x109, 0x8)
    SetChrPos(0x109, 258149, 0, 125700, 90)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x109,
        "#10100F放在这里应该不错。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "诺艾尔的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x13D, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 23)
    Call(0, 39)
    Call(0, 49)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3606")
    OP_A3(0x0, 0x8)

    label("loc_3606")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3619")
    OP_A3(0x1, 0x8)

    label("loc_3619")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_362C")
    OP_A3(0x2, 0x8)

    label("loc_362C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_363F")
    OP_A3(0x3, 0x8)

    label("loc_363F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3652")
    OP_A3(0x4, 0x8)

    label("loc_3652")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3665")
    OP_A3(0x5, 0x8)

    label("loc_3665")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_367E")
    OP_A2(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_367E")

    SetChrPos(0x0, 256010, 0, 121130, 0)
    EventEnd(0x5)
    Return()

    # Function_20_3490 end

    def Function_21_3692(): pass

    label("Function_21_3692")

    EventBegin(0x0)
    SoundLoad(3668)
    SoundLoad(3669)
    SoundLoad(3670)
    SoundLoad(3671)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BE")
    OP_A2(0x0, 0x8)

    label("loc_36BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D1")
    OP_A2(0x1, 0x8)

    label("loc_36D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E4")
    OP_A2(0x2, 0x8)

    label("loc_36E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36F7")
    OP_A2(0x3, 0x8)

    label("loc_36F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370A")
    OP_A2(0x4, 0x8)

    label("loc_370A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_371D")
    OP_A2(0x5, 0x8)

    label("loc_371D")

    OP_A2(0x8, 0x80)
    OP_A2(0xA, 0x80)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00000F（说起来……\x01",
            "  之前得到了琪雅\x01",
            "  可能会喜欢的玩偶。）\x02\x03",
            "（赶快送给她吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德找到了琪雅，\x01",
            "把玩偶送给了她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x0, 0x80000000)
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x8,
        (
            scpstr(0x7, 0x0),
            "#01100F#3668V哇，要送给我吗！？\x02\x03",
            "#3669V嘿嘿……\x01",
            "罗伊德，谢谢¤\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE55)
    OP_C9(0x1, 0x80000000)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00000F哈哈，不客气。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x354, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38AC")
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x13D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_73(0xF, 0x4)
    OP_72(0xF, 0x2)
    OP_66(0x9, 0x1)
    SetChrPos(0x9, 255500, 0, 68590, 89)
    OP_68(256000, 1300, 68810, 0)
    Call(0, 22)

    label("loc_38AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x355, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3902")
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x13D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_73(0xE, 0x4)
    OP_72(0xE, 0x2)
    OP_66(0x8, 0x1)
    SetChrPos(0x9, 255940, 30, 66720, 180)
    OP_68(256220, 1330, 66750, 0)
    Call(0, 22)

    label("loc_3902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x356, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3958")
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x13D, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_73(0x10, 0x4)
    OP_72(0x10, 0x2)
    OP_66(0xA, 0x1)
    SetChrPos(0x9, 258089, 0, 67110, 89)
    OP_68(258310, 1300, 67080, 0)
    Call(0, 22)

    label("loc_3958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x357, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39AE")
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x13D, 7)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_73(0x11, 0x4)
    OP_72(0x11, 0x2)
    OP_66(0xB, 0x1)
    SetChrPos(0x9, 255560, 30, 72720, 0)
    OP_68(255320, 1330, 72710, 0)
    Call(0, 22)

    label("loc_39AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x358, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A04")
    SubItemNumber(0x358, 1)
    SetScenarioFlags(0x13E, 0)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_73(0x12, 0x4)
    OP_72(0x12, 0x2)
    OP_66(0xC, 0x1)
    SetChrPos(0x9, 256500, 30, 63940, 89)
    OP_68(256850, 1330, 63910, 0)
    Call(0, 22)

    label("loc_3A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A25")
    Call(0, 51)

    label("loc_3A25")

    OP_5B(0xE, 0x118, 0x3C, 0x3)
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3692 end

    def Function_22_3A3A(): pass

    label("Function_22_3A3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A51")
    Sleep(1000)
    Jump("loc_3A54")

    label("loc_3A51")

    Sleep(500)

    label("loc_3A54")

    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x9, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ABE")

    ChrTalk(
        0x9,
        "#01100F#3670V嗯，放在这里应该不错。\x02",
    )

    Jump("loc_3AEC")

    label("loc_3ABE")


    ChrTalk(
        0x9,
        "#01100F#3671V嗯……把这孩子放在这里如何？\x02",
    )


    label("loc_3AEC")

    CloseMessageWindow()
    OP_24(0xE56)
    OP_24(0xE57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "琪雅的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Call(0, 23)
    Call(0, 39)
    FadeToDark(500, 0, -1)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_22_3A3A end

    def Function_23_3B50(): pass

    label("Function_23_3B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA2")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "如果得到了家具类道具，\x01",
            "可以放置在支援科各成员的房间中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_3BA2")

    Return()

    # Function_23_3B50 end


    def Function_27_3D80(): pass

    label("Function_27_3D80")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis362.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着优雅衣镜。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_3D80 end

    def Function_28_3E31(): pass

    label("Function_28_3E31")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis363.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着八音盒。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0x1F4)
    WaitBGM()
    Sleep(10)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    BeginChrThread(0xB, 1, 0, 29)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_3E31 end

    def Function_29_3F0A(): pass

    label("Function_29_3F0A")

    PlayBGM("ed70591", 0)
    Sleep(19000)
    OP_1F()
    Return()

    # Function_29_3F0A end

    def Function_30_3F13(): pass

    label("Function_30_3F13")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis364.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着影丸储蓄罐。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_30_3F13 end

    def Function_31_3FC6(): pass

    label("Function_31_3FC6")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis365.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着咪雪玩偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_31_3FC6 end

    def Function_32_4077(): pass

    label("Function_32_4077")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis370.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着竞赛旗。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_4077 end

    def Function_33_4126(): pass

    label("Function_33_4126")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis371.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着小径自行车。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_33_4126 end

    def Function_34_41D9(): pass

    label("Function_34_41D9")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis373.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着波波靠垫。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_34_41D9 end

    def Function_35_428A(): pass

    label("Function_35_428A")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis372.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着古怪靠垫。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_35_428A end

    def Function_36_433B(): pass

    label("Function_36_433B")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis374.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着黑泰迪熊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_36_433B end

    def Function_37_43EC(): pass

    label("Function_37_43EC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis375.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着苦番茄人玩偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_37_43EC end

    def Function_38_44A1(): pass

    label("Function_38_44A1")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis376.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "摆放着ＺＷＥＩ２企鹅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_38_44A1 end

    def Function_39_4558(): pass

    label("Function_39_4558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45CC")
    OP_E0(0x16, 0x0)

    label("loc_45CC")

    Return()

    # Function_39_4558 end

    def Function_40_45CD(): pass

    label("Function_40_45CD")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_40_45CD end

    def Function_41_45FC(): pass

    label("Function_41_45FC")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_41_45FC end

    def Function_42_462B(): pass

    label("Function_42_462B")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_42_462B end

    def Function_43_465A(): pass

    label("Function_43_465A")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_43_465A end

    def Function_44_4689(): pass

    label("Function_44_4689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_518C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis362.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis363.itp")
    LoadChrToIndex("chr/ch00102.itc", 0x1E)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_A2(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_473B")
    OP_A3(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_473B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4754")
    OP_A3(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_4754")

    OP_21(0xBB8)
    SetChrName("")
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "某日，罗伊德一行人趁着\x01",
            "支援工作的余暇回到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "与总部进行过定时联络后，\x01",
            "众人各自休息片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(154920, 1880, 123500, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57E4, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70102", 0)
    FadeToBright(1000, 0)
    OP_68(154920, 1330, 123500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00104F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 155790, 0, 118500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0x101, 0x8)

    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#1P艾莉，我可以进去吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x102, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00100F罗伊德？\x01",
            "嗯，进来吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    OP_A2(0x102, 0x40)
    SetChrPos(0x102, 155440, 30, 122630, 180)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_A3(0x102, 0x4)
    OP_68(155280, 1330, 121810, 2000)
    OP_6C(0x52E4, 0x7D0)
    Sleep(500)
    OP_9B(0x0, 0x102, 0x0, 0x1F4, 0x3E8, 0x0)

    def lambda_4944():

        label("loc_4944")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4944")

    QueueWorkItem2(0x102, 2, lambda_4944)
    OP_0D()
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_4960():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4960)

    def lambda_4975():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4975)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x101, 0x102, 500)
    EndChrThread(0x102, 0x2)
    OP_6F(0x79)
    Sleep(200)

    ChrTalk(
        0x102,
        "#00100F该出发了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F是啊，今天总部\x01",
            "也没什么特别的工作联络。\x02\x03",
            "#00000F不过大家还没集合呢，\x01",
            "所以不用太着急。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x14A, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x1E, 0x1F4)
    Sleep(750)

    ChrTalk(
        0x101,
        (
            "#00005F啊……\x01",
            "好像添置了不少东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(157760, 1330, 124430, 3000)
    OP_6C(0x56D6, 0xBB8)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 40)
    Sleep(1000)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x102,
        (
            scpstr(0x7, 0x0),
            "#00102F呵呵，一直住在这里，\x01",
            "不知不觉就增多了。\x02\x03",
            "#00104F偶尔回家的时候，\x01",
            "也会带走一些没用的书和小物件，\x01",
            "但还是这么乱……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00009F哪里，比我的房间\x01",
            "整洁多了。\x02\x03",
            "#00000F虽然添置了不少东西，\x01",
            "但都很适合这房间……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 41)
    OP_68(155770, 1330, 122300, 2000)
    OP_6C(0x5AB4, 0x7D0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4BC1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BC1)
    Sleep(200)

    def lambda_4BD1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BD1)
    Sleep(500)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(
        0x101,
        (
            "#00005F那个……\x01",
            "是八音盒吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F呵呵，是的。\x02",
    )

    CloseMessageWindow()
    OP_68(155140, 1330, 123720, 2000)
    OP_6C(0x56D6, 0x7D0)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 42)
    Sleep(1000)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x102,
        (
            scpstr(0x7, 0x0),
            "#00104F这个利威尔特公司\x01",
            "出品的古董八音盒是在\x01",
            "伊梅尔达夫人的店里购买的……\x02\x03",
            "#00100F这是一首我很怀念的曲子，\x01",
            "所以就忍不住买下了。\x02\x03",
            "#00109F……要听一听吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00000F好啊，我很有兴趣。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 43)
    Sleep(750)
    OP_21(0x1388)
    OP_6D(0x2D, 0x16, 0x0, 0xFA0)
    OP_6C(0x4E20, 0xFA0)
    OP_95(0x102, 0x25F30, 0x1E, 0x1DF06, 0x3E8, 0x0)
    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_A2(0x102, 0x4)
    SetChrPos(0x102, 155910, 200, 123440, 290)
    OP_0D()
    Sleep(250)
    OP_95(0x101, 0x25B3E, 0x1E, 0x1DE52, 0x7D0, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(949, 0, 100, 0)
    Sleep(900)
    Sound(853, 0, 50, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sleep(1500)
    OP_6C(0x4650, 0x4A38)
    OP_71(0x9, 0xF, 0x5F, 0x0, 0x20)
    BeginChrThread(0xB, 1, 0, 45)
    WaitChrThread(0xB, 0x1)
    OP_74(0x9, 0x0)
    Sleep(1000)
    PlayBGM("ed70102", 0)

    ChrTalk(
        0x101,
        (
            "#00009F#1P呼……\x01",
            "真是令人赞叹的音色啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#00109F呵呵，是吧？\x02\x03",
            "#00104F帝国的利威尔特公司\x01",
            "是一家著名的乐器制造厂商，\x01",
            "他们生产的八音盒也很受欢迎。\x02\x03",
            "#00100F我以前有过一个曲目\x01",
            "和它一样，但发音数\x01",
            "比较少的八音盒……\x02\x03",
            "#00106F但在留学的地方\x01",
            "不慎丢失了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#1P是吗……\x02\x03",
            "#00006F（莫非包含着\x01",
            "  和父母有关的回忆……？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F因为已经停产，\x01",
            "我也只能放弃了……\x02\x03",
            "#00100F没想到伊梅尔达夫人进到了货，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#1P是吗……\x02\x03",
            "#00002F哈哈，她的店\x01",
            "偶尔也能发挥作用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(812, 0, 100, 0)
    OP_A2(0x102, 0x40)
    SetChrPos(0x102, 155640, 30, 122530, 180)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_A3(0x102, 0x4)
    OP_68(154430, 1330, 122240, 1500)
    OP_6D(0x2D, 0x19, 0x0, 0x5DC)
    OP_6E(0x15E, 0x5DC)
    OP_6C(0x4D26, 0x5DC)
    OP_0D()

    def lambda_5066():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5066)
    Sleep(200)

    def lambda_5076():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5076)
    OP_6F(0x79)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#00100F好了，\x01",
            "我们走吧，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F……嗯！\x02",
    )

    CloseMessageWindow()
    OP_6C(0x510E, 0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "艾莉的家具已经收集全了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_21(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x102, 0xFF)
    OP_A3(0x101, 0x4)
    OP_A3(0x102, 0x4)
    OP_A3(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_514D")
    OP_A2(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_514D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5166")
    OP_A2(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_5166")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetScenarioFlags(0x12C, 6)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 108, 0, 0)
    IdleLoop()

    label("loc_518C")

    Return()

    # Function_44_4689 end

    def Function_45_518D(): pass

    label("Function_45_518D")

    PlayBGM("ed70591", 1)
    Sleep(19000)
    Return()

    # Function_45_518D end

    def Function_46_5195(): pass

    label("Function_46_5195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis365.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis364.itp")
    LoadChrToIndex("apl/ch50218.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    SoundLoad(938)
    SoundLoad(939)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_A2(0x103, 0x4)
    SetChrPos(0x103, 205890, 80, 126750, 180)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x103, 3, 0, 47)
    OP_73(0x15, 0x4)
    OP_70(0x15, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_526D")
    OP_A3(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_526D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5286")
    OP_A3(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_5286")

    OP_21(0xBB8)
    SetChrName("")
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "某日，罗伊德一行人趁着\x01",
            "支援工作的余暇回到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "与总部进行过定时联络后，\x01",
            "众人各自休息片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(205970, 1830, 125860, 0)
    OP_6D(0x2D, 0x19, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57EE, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70102", 0)
    Sound(938, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_68(205970, 1330, 125860, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 205780, 0, 119210, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0x101, 0x8)

    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#1P缇欧，我可以进去吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)
    StopSound(938, 300, 40)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00200F嗯，请进，\x01",
            "罗伊德前辈。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(205300, 1330, 124060, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(205440, 1330, 124910, 2000)

    def lambda_5435():
        OP_9B(0x0, 0xFE, 0x0, 0x125C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5435)

    def lambda_544A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_544A)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x101, 0x103, 500)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x103,
        "#00200F该出发了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F是啊，今天总部\x01",
            "也没什么特别的工作联络。\x02\x03",
            "#00000F不过大家还没集合呢，\x01",
            "所以不用太着急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F没关系，我马上就可以出发。\x02",
    )

    CloseMessageWindow()
    Sound(938, 2, 50, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x50, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(750)

    ChrTalk(
        0x101,
        (
            "#00005F啊……\x01",
            "好像添置了不少东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(209790, 1330, 124450, 2500)
    OP_6D(0x3C, 0x19, 0x0, 0x9C4)
    OP_6E(0x15E, 0x9C4)
    OP_6C(0x4E20, 0x9C4)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(205740, 1330, 129949, 5000)
    OP_6D(0x1E, 0x19, 0x0, 0x1388)
    OP_6F(0x79)
    Sleep(2000)
    BeginChrThread(0xB, 1, 0, 48)
    Fade(500)
    OP_68(205720, 1330, 125260, 0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57EE, 0x0)
    OP_6D(0x2D, 0x16, 0x0, 0x0)
    OP_0D()
    Sleep(1000)
    StopSound(938, 300, 40)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x103, 0x3)
    Sleep(800)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)
    Sound(71, 0, 60, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0xA, 0x0, 0x8)
    OP_79(0x15)
    Sleep(500)
    Fade(500)
    OP_A2(0x103, 0x40)
    SetChrPos(0x103, 205890, 0, 126850, 180)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_A3(0x103, 0x4)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00204F……嗯，收集到了\x01",
            "很多好东西。\x02\x03",
            "#00202F相比周边诸国，\x01",
            "克洛斯贝尔的虚拟角色\x01",
            "相关产品要丰富得多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F哈哈，再怎么说，\x01",
            "这里也是咪西的家乡嘛。\x02\x03",
            "#00004F借助米修拉姆主题公园的影响力，\x01",
            "咪西的人气也渐渐扩展到了周边各国……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(209440, 1330, 124760, 2500)
    OP_6D(0x3C, 0x19, 0x0, 0x9C4)
    OP_6E(0x15E, 0x9C4)
    OP_6C(0x5014, 0x9C4)

    def lambda_57A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57A1)
    Sleep(200)

    def lambda_57B1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57B1)
    OP_6F(0x79)
    Sleep(500)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    Call(0, 40)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5957")
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00005F说起来……\x02\x03",
            "#00000F那边那个粉红色的玩偶\x01",
            "是叫『咪雪』吧？\x02\x03",
            "#00004F记得它是咪西的妹妹。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x103,
        (
            scpstr(0x7, 0x0),
            "#00202F是的，虽然对蠢笨的哥哥抱怨不休，\x01",
            "但却一直在细心照顾着哥哥，\x01",
            "是很典型的妹系角色。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00012F是，是这样啊……\x01",
            "（妹系角色是什么意思？）\x02\x03",
            "#00005F嗯……那边那只\x01",
            "黑猫又是什么？\x02\x03",
            "#00000F坐垫也是以它为形象的，\x01",
            "跟咪西有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_5AF8")

    label("loc_5957")

    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00005F说起来……\x02\x03",
            "#00000F那只粉红色的咪西\x01",
            "是什么版本？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x103, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x103,
        (
            scpstr(0x7, 0x0),
            "#00206F……罗伊德前辈太不爱学习了。\x02\x03",
            "#00200F那不是咪西，\x01",
            "是它的妹妹咪雪。\x02\x03",
            "#00211F身为克洛斯贝尔的搜查官，\x01",
            "怎能连这种事都不知道。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00006F真、真是颜面无光……\x01",
            "（但这好像和搜查官没什么关系吧？）\x02\x03",
            "#00005F嗯……那边那只\x01",
            "黑猫又是什么？\x02\x03",
            "#00000F坐垫也是以它为形象的，\x01",
            "跟咪西有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5AF8")

    Call(0, 41)

    def lambda_5B00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B00)
    Sleep(200)

    def lambda_5B10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B10)
    OP_68(205550, 1330, 128690, 3000)
    OP_6D(0x22, 0x19, 0x0, 0xBB8)
    OP_6F(0x79)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    Call(0, 42)
    Sleep(1000)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x103,
        (
            scpstr(0x7, 0x0),
            "#00202F那是『影丸』。\x02\x03",
            "#00204F是一部最近很受欢迎的\x01",
            "连载小说中主人公饲养的猫……\x02\x03",
            "#00200F目中无人的可爱性格\x01",
            "和独特的叫声\x01",
            "令它大受欢迎。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00005F嘿，原来如此。\x02\x03",
            "#00003F说起来，『巴鲁卡』的奖品中\x01",
            "好像也有它的周边。\x02\x03",
            "#00009F话说回来，咪西也好，这家伙也好，\x01",
            "都很难用可爱来形容呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x103,
        (
            scpstr(0x7, 0x0),
            "#00211F（瞪）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00006F不不，我什么都没说。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x103,
        (
            scpstr(0x7, 0x0),
            "#00206F……算了，其实我明白你的意思。\x02\x03",
            "#00200F咪西的卖点是\x01",
            "难以形容的独特不安定感，\x01",
            "也就是所谓的『懒散型角色』……\x02\x03",
            "#00203F而影丸则凭借冷淡的性格\x01",
            "得到了大家的喜爱，\x01",
            "从而成为经典的虚拟角色。\x02\x03",
            "#00200F严格来说，它们确实不是\x01",
            "传统意义上的可爱类型。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_5B(0x118, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00005F原来如此……\x01",
            "好像很有说服力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 43)
    Sleep(250)
    OP_68(205720, 1330, 125260, 2500)
    OP_6E(0x15E, 0x9C4)
    OP_6C(0x57EE, 0x9C4)
    OP_6D(0x2D, 0x16, 0x0, 0x9C4)
    TurnDirection(0x103, 0x101, 500)
    OP_6F(0x79)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F对了，缇欧，\x01",
            "你更喜欢咪西\x01",
            "还是影丸？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00203F……………………………………\x02\x03",
            "#00211F……你竟然问了这个问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F我因为无法作答\x01",
            "而一直在逃避的问题……\x02\x03",
            "#00201F终于被问到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F哎，那个……缇欧……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F关于这个问题，\x01",
            "我们晚饭之后再慢慢交流吧。\x02\x03",
            "#00204F……罗伊德前辈，\x01",
            "今晚一定会是激情四射的一夜……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F（……虽然有本书很想看，\x01",
            "  但今天似乎也只能放弃了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x5BD6, 0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "缇欧的家具已经收集全了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_21(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x103, 0xFF)
    OP_A3(0x101, 0x4)
    OP_A3(0x103, 0x4)
    OP_A3(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_60C7")
    OP_A2(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_60C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_60E0")
    OP_A2(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_60E0")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    OP_72(0x15, 0x4)
    SetScenarioFlags(0x12C, 7)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_24(0x3AA)
    OP_24(0x3AB)
    EventEnd(0x6)
    NewScene("c0130", 110, 0, 0)
    IdleLoop()

    label("loc_610C")

    Return()

    # Function_46_5195 end

    def Function_47_610D(): pass

    label("Function_47_610D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6166")
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6138")
    Jump("Function_47_610D")

    label("loc_6138")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_614C")
    Jump("loc_6166")

    label("loc_614C")

    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)
    Sleep(100)
    SetChrSubChip(0x103, 0x1)
    Sleep(100)
    Jump("Function_47_610D")

    label("loc_6166")

    Return()

    # Function_47_610D end

    def Function_48_6167(): pass

    label("Function_48_6167")

    Sound(804, 0, 100, 0)
    Sleep(500)
    Sound(939, 2, 70, 0)
    Sleep(1000)
    Sound(73, 0, 100, 0)
    OP_24(0x3AB)
    Return()

    # Function_48_6167 end

    def Function_49_6183(): pass

    label("Function_49_6183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B95")
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02902.itc", 0x1E)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    OP_A2(0x109, 0x4)
    SetChrPos(0x109, 254080, 150, 127100, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_61DD")
    OP_A3(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_61DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_61F6")
    OP_A3(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_61F6")

    OP_21(0xBB8)
    SetChrName("")
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "某日，罗伊德一行人趁着\x01",
            "支援工作的余暇回到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "与总部进行过定时联络后，\x01",
            "众人各自休息片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(254580, 1800, 125790, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57E4, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70102", 0)
    FadeToBright(1000, 0)
    OP_68(254580, 1300, 125790, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10100F嗯……\x01",
            "这样就行了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 255880, 0, 119170, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0x101, 0x8)

    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#1P诺艾尔，我可以进去吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x109, 0x1)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10100F罗伊德警官？\x01",
            "嗯，请进吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    OP_A2(0x109, 0x40)
    SetChrPos(0x109, 254580, 0, 126410, 180)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_A3(0x109, 0x4)
    OP_0D()
    OP_68(255330, 1300, 123600, 2500)
    OP_6C(0x5208, 0x9C4)
    BeginChrThread(0x109, 1, 0, 50)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_63E9():
        OP_9B(0x0, 0xFE, 0x0, 0x1068, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63E9)

    def lambda_63FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_63FE)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x109, 0x1)
    OP_6F(0x79)
    Sleep(200)

    ChrTalk(
        0x109,
        "#10100F该出发了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F是啊，今天总部\x01",
            "也没什么特别的工作联络。\x02\x03",
            "#00000F不过大家还没集合呢，\x01",
            "所以不用太着急。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x14A, 0x1F4)
    Sleep(200)
    OP_68(254560, 1300, 125250, 1500)
    OP_6C(0x4E20, 0x5DC)
    OP_93(0x109, 0x14A, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F哎？你在写报告书吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F哈哈……\x01",
            "我毕竟是以外派的形式过来工作的。\x02\x03",
            "#10100F所以每周都要向索妮亚司令\x01",
            "提交一次报告书。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F是吗，辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(255830, 1300, 124180, 3000)
    OP_6D(0x3B, 0xE, 0x0, 0xBB8)
    OP_6E(0x1C2, 0xBB8)
    OP_6C(0x4074, 0xBB8)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(200)
    OP_93(0x109, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(750)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#4P哎……！\x01",
            "添置了不少有趣的东西啊。\x02\x03",
            "#00000F自行车，还有……\x01",
            "这是导力车赛车比赛时用的旗子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10102F啊……你连这些都知道吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    ChrTalk(
        0x101,
        (
            "#00000F#4P嗯，因为我在共和国\x01",
            "住过两年左右。\x02\x03",
            "#00004F那边和克洛斯贝尔不同，\x01",
            "经常能看到自行车呢……\x02\x03",
            "#00000F偶尔还会举办\x01",
            "导力车的赛车比赛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F是啊是啊，没错！\x02\x03",
            "#10104F……其实我去世的父亲\x01",
            "非常喜欢那些。\x02\x03",
            "#10100F在我小时候，\x01",
            "他还带我乘列车\x01",
            "去共和国看过比赛呢。\x02\x03",
            "#10102F但警备队的工作非常忙，\x01",
            "所以也只去过一次而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#4P是吗……\x02\x03",
            "#00000F也就是说，你从那时\x01",
            "就开始喜欢上导力车了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F哈哈……真是明察秋毫。\x02\x03",
            "#10100F等到休假的时候，\x01",
            "我想再去看看\x01",
            "赛车比赛……\x02\x03",
            "#10106F但最近一直没什么时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#4P哈哈，是啊。\x02\x03",
            "#00004F（诺艾尔大概不仅想看，\x01",
            "  还想参加比赛吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F#4P先不说赛车了……\x02\x03",
            "#00002F要是有什么推荐的\x01",
            "自行车型号，\x01",
            "等下次有机会时给我介绍一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105F咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#4P哦，在共和国的时候\x01",
            "经常看朋友骑车，\x01",
            "我也产生了一点兴趣。\x02\x03",
            "#00000F以后休息时，我们可以\x01",
            "一起骑车兜兜风，你看如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10100F好、好啊！\x02\x03",
            "#10104F既方便，又能锻炼身体，\x01",
            "而且十分有趣！\x02\x03",
            "#10109F我下次把放在家里的\x01",
            "自行车图鉴拿过来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#4P哈哈，拜托你了。\x02",
    )

    CloseMessageWindow()
    OP_6C(0x42CC, 0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "诺艾尔的家具已经收集全了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_21(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x109, 0xFF)
    OP_A3(0x101, 0x4)
    OP_A3(0x109, 0x4)
    OP_A3(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B5E")
    OP_A2(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_6B5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B77")
    OP_A2(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_6B77")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 1)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 115, 0, 0)
    IdleLoop()

    label("loc_6B95")

    Return()

    # Function_49_6183 end

    def Function_50_6B96(): pass

    label("Function_50_6B96")

    OP_95(0xFE, 0x3E77E, 0x0, 0x1E758, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_50_6B96 end

    def Function_51_6BB2(): pass

    label("Function_51_6BB2")

    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis342.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis343.itp")
    LoadChrToIndex("apl/ch51542.itc", 0x1E)
    LoadChrToIndex("apl/ch51216.itc", 0x1F)
    SoundLoad(3672)
    SoundLoad(3673)
    SoundLoad(3031)
    SoundLoad(3318)
    SoundLoad(3319)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_A2(0x9, 0x4)
    OP_A2(0x9, 0x40)
    OP_A3(0x9, 0x1)
    SetChrPos(0x9, 254100, 150, 71270, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6C66")
    OP_A3(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_6C66")

    Sleep(1000)
    OP_68(254920, 1830, 70340, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57E4, 0x0)
    OP_21(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70102", 0)
    FadeToBright(1000, 0)
    OP_68(254920, 1330, 70340, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 251210, 0, 65690, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0x101, 0x8)

    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#2P琪雅，我可以进去吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#01100F啊，罗伊德！\x01",
            "可以啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 66480, 2000)
    OP_6D(0x2D, 0x17, 0x0, 0x7D0)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_6D80():
        OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D80)

    def lambda_6D95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6D95)
    BeginChrThread(0x9, 1, 0, 52)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    TurnDirection(0x101, 0x9, 500)
    WaitChrThread(0x9, 0x1)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F哦……\x01",
            "不知不觉间，已经装饰得这么漂亮了。\x02\x03",
            "#00009F嗯，这样一看，\x01",
            "真是相当壮观呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01109F嘿嘿……\x01",
            "它们都很可爱吧？\x02\x03",
            "#01111F啊，不过……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E5D():

        label("loc_6E5D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6E5D")

    QueueWorkItem2(0x101, 1, lambda_6E5D)
    OP_68(256450, 1300, 64640, 3000)
    OP_6D(0x3C, 0x16, 0x0, 0xBB8)
    OP_6C(0x4E20, 0xBB8)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_95(0x9, 0x3EB2A, 0x1E, 0x103B0, 0x7D0, 0x1)
    OP_95(0x9, 0x3F034, 0x0, 0xFF0A, 0x7D0, 0x0)
    OP_93(0x9, 0xB4, 0x1F4)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)

    ChrTalk(
        0x9,
        (
            "#01110F#5P这孩子好像\x01",
            "并不是玩偶。\x02\x03",
            "#01100F说明书上说，这是『玩偶装』，\x01",
            "可以把它穿在身上哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6F50():

        label("loc_6F50")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6F50")

    QueueWorkItem2(0x9, 1, lambda_6F50)
    BeginChrThread(0x101, 1, 0, 53)
    OP_68(257690, 1300, 64489, 2000)
    OP_6D(0x3C, 0x18, 0x0, 0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6FFD")

    ChrTalk(
        0x101,
        (
            "#00005F#2P玩偶装……\x01",
            "就像咪西扮演装那样吗？\x02\x03",
            "#00003F原来如此，像琪雅这种身材的小孩子，\x01",
            "应该能穿得进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7070")

    label("loc_6FFD")


    ChrTalk(
        0x101,
        (
            "#00005F#2P玩偶装……\x01",
            "哦，也就是扮演玩偶的套装啊。\x02\x03",
            "#00003F原来如此，像琪雅这种身材的小孩子，\x01",
            "应该能穿得进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7070")

    WaitChrThread(0x101, 0x1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#01105F啊，既然如此……\x02\x03",
            "#01109F我想穿穿看，\x01",
            "帮帮我好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7136")

    ChrTalk(
        0x101,
        (
            "#00005F#2P可以是可以……\x01",
            "但穿上之后应该会很热哦。\x02\x03",
            "#00012F上次扮演咪西的时候，\x01",
            "热得我满身大汗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A3")

    label("loc_7136")


    ChrTalk(
        0x101,
        (
            "#00005F#2P可以是可以……\x01",
            "但穿上之后应该会很热哦。\x02\x03",
            "#00003F书上说过，穿上这种东西之后，\x01",
            "感觉会非常闷热。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A3")


    ChrTalk(
        0x9,
        (
            "#01100F嗯，没关系。\x02\x03",
            "#01109F而且我就是想穿上\x01",
            "让罗伊德看看嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#2P嗯……我知道了。\x02\x03",
            "#00004F（……该说是后生可畏吗，\x01",
            "  这孩子将来肯定会很了不得。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21(0xBB8)
    OP_72(0x12, 0x4)
    Sleep(2000)
    OP_68(254670, 1330, 68760, 0)
    OP_6D(0x2D, 0x1A, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57E4, 0x0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 255210, 30, 69560, 0)
    SetChrPos(0x101, 255340, 0, 68850, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(1000, 0, 100, 0)
    Sleep(1000)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F好……这样就行了。\x02\x03",
            "#00000F琪雅，不难受吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "嗯，没事。\x02\x03",
            "感觉很凉爽，\x01",
            "并没有你说的那么热哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F哦……大概是充分\x01",
            "考虑到透气性了吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70105", 0)
    Sleep(500)
    OP_6C(0x4E20, 0x1F4)
    TurnDirection(0x9, 0x101, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    Sound(3031, 255, 100, 0)

    NpcTalk(
        0x9,
        "琪雅企鹅",
        "锵锵锵！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00011F#5S哦哦哦！？\x02\x03",
            "#00009F#3S该、该怎么说呢……\x01",
            "真是超可爱啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0xB, 255000, 0, 71000, 315)
    OP_A3(0xB, 0x80)
    OP_A2(0xB, 0x8)

    NpcTalk(
        0xB,
        "琪雅企鹅",
        "#1P嘿嘿，是吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 1, 0, 54)
    Fade(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Fade(150)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0xB,
        "琪雅企鹅",
        (
            "#1P#3672V你好。\x02\x03",
            "#3673V请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE59)
    OP_C9(0x1, 0x80000000)
    OP_5B(0x10, 0x96, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0x101,
        (
            scpstr(0x7, 0x0),
            "#00011F哦哦……！\x01",
            "（杀伤力实在太强大了……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x103, 250000, 0, 64000, 90)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0x103, 0x8)
    OP_A2(0x103, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7646")
    OP_A3(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)

    label("loc_7646")

    SetChrPos(0x102, 250000, 0, 64000, 90)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A3(0x102, 0x8)
    OP_A2(0x102, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7685")
    OP_A3(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)

    label("loc_7685")


    NpcTalk(
        0x102,
        "艾莉的声音",
        "#2P罗伊德，在吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(253400, 1330, 66290, 1500)
    OP_6C(0x57E4, 0x5DC)
    OP_93(0x101, 0xE1, 0x1F4)
    OP_6F(0x79)

    NpcTalk(
        0x103,
        "缇欧的声音",
        (
            "#2P你一直不回来，\x01",
            "我们就来叫你了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F哦，我在，让你们久等了，抱歉。\x02\x03",
            "#00004F那个……请做好心理准备\x01",
            "之后再进来吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "艾莉的声音",
        "#2P？？？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x103,
        "缇欧的声音",
        "#2P心理准备……？\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x102, 251210, 0, 65690, 90)

    def lambda_77C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_77C8)
    BeginChrThread(0x102, 1, 0, 55)
    Sleep(500)
    SetChrPos(0x103, 251210, 0, 65690, 90)

    def lambda_77F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_77F3)
    BeginChrThread(0x103, 1, 0, 56)

    ChrTalk(
        0x102,
        "#00100F#2P到底发生什么事了……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x103, 0x2)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#2P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#3P#N………………………（目瞪口呆）\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    NpcTalk(
        0x9,
        "琪雅企鹅",
        (
            "啊，是艾莉和缇欧。\x02\x03",
            "你们好吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_78EE():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78EE)
    Sleep(20)

    def lambda_790A():
        OP_A6(0xFE, 0x0, 0x14, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_790A)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F这#500W、#40W这#500W、#40W这……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x103,
        "#00201F#3P#N#5S这属于重大事件……！\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(254700, 1300, 68970, 1000)
    OP_6C(0x4E20, 0x3E8)
    BeginChrThread(0x102, 1, 0, 59)
    Sleep(50)
    BeginChrThread(0x103, 1, 0, 60)
    Sleep(260)
    BeginChrThread(0x101, 1, 0, 62)
    OP_82(0x0, 0x64, 0xBB8, 0x64)
    Sound(811, 0, 100, 0)
    Sound(3318, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#4P#10A呜哇！\x02",
    )

    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_7A18():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A18)
    Sleep(20)

    def lambda_7A34():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A34)
    Sleep(20)

    def lambda_7A50():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7A50)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#00114F好、好可爱！\x01",
            "琪雅好可爱啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F难、难以相信……\x02\x03",
            "#00201F在现实世界中，\x01",
            "竟然存在这么可爱的……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(898, 0, 100, 0)

    def lambda_7AFD():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AFD)
    Sleep(20)

    def lambda_7B19():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7B19)
    Sleep(20)

    def lambda_7B35():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7B35)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x9, 0x1)

    NpcTalk(
        0x9,
        "琪雅企鹅",
        (
            "透、透不过气了……\x02\x03",
            "请不要\x01",
            "抱得这么紧……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x13B, 0x0)
    OP_0D()
    Sleep(250)
    OP_95(0x101, 0x3E3DC, 0x0, 0x10A2C, 0x7D0, 0x0)
    TurnDirection(0x101, 0x9, 0)
    OP_68(253400, 1330, 66290, 2500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F2B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7BFB")
    OP_A3(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_7BFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7C14")
    OP_A3(0x109, 0x80)
    ClearChrBattleFlags(0x109, 0x8000)

    label("loc_7C14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7C2D")
    OP_A3(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_7C2D")

    OP_A3(0x109, 0x8)
    OP_A2(0x109, 0x40)
    SetChrPos(0x109, 251210, 0, 65690, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7C58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7C58)
    BeginChrThread(0x109, 1, 0, 57)
    Sleep(500)
    OP_A3(0x104, 0x8)
    OP_A2(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7C98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7C98)
    BeginChrThread(0x104, 1, 0, 58)
    Sleep(500)
    OP_A3(0x105, 0x8)
    OP_A2(0x105, 0x40)
    SetChrPos(0x105, 251210, 0, 65690, 90)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7CD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7CD8)
    BeginChrThread(0x105, 1, 0, 56)

    ChrTalk(
        0x104,
        "#00305F吵什么呢……嗯？这是什么情况！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x105, 0x2)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x104, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10105F#12P小、小琪雅！？\x02\x03",
            "#10109F哇啊啊啊啊啊～！\x01",
            "让我也抱抱吧！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 1, 0, 61)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 63)
    OP_82(0x0, 0x64, 0xBB8, 0x64)
    Sound(811, 0, 100, 0)
    Sound(3319, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00011F#4P#10A哇啊！\x02",
    )

    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Sound(898, 0, 100, 0)

    def lambda_7DD6():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7DD6)
    Sleep(20)

    def lambda_7DF2():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7DF2)
    Sleep(20)

    def lambda_7E0E():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7E0E)
    Sleep(20)

    def lambda_7E2A():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E2A)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    OP_68(255000, 1330, 66890, 2000)
    BeginChrThread(0x104, 1, 0, 66)
    Sleep(200)
    BeginChrThread(0x105, 1, 0, 65)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x104, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10304F#6P呵呵，真是场灾难啊。\x02\x03",
            "#10309F虽然确实可爱到了\x01",
            "夸张的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#6P哎呀～！\x01",
            "如果出现在战场上，说不定会\x01",
            "引起另一种意义上的混乱呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x104, 0x9, 500)
    TurnDirection(0x105, 0x9, 500)
    Jump("loc_80B0")

    label("loc_7F2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7F44")
    OP_A3(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_7F44")

    OP_A3(0x104, 0x8)
    OP_A2(0x104, 0x40)
    SetChrPos(0x104, 251210, 0, 65690, 90)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_7F6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7F6F)
    BeginChrThread(0x104, 1, 0, 56)
    Sleep(500)

    ChrTalk(
        0x104,
        "#00305F吵什么呢……嗯？这是什么情况！？\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(898, 0, 100, 0)

    def lambda_7FBE():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FBE)
    Sleep(20)

    def lambda_7FDA():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7FDA)
    Sleep(20)

    def lambda_7FF6():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7FF6)
    OP_68(253160, 1330, 67480, 2000)
    OP_95(0x104, 0x3DDD8, 0x0, 0x109A0, 0x7D0, 0x0)
    TurnDirection(0x104, 0x9, 500)
    Sleep(500)
    WaitChrThread(0x104, 0x1)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00303F#6P喂喂，这未免也\x01",
            "太过可爱了吧……！？\x02\x03",
            "#00309F如果出现在战场上，说不定会\x01",
            "引起另一种意义上的混乱呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80DE")
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(750)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    OP_0D()
    TurnDirection(0x101, 0x9, 500)
    Sleep(500)

    label("loc_80DE")


    ChrTalk(
        0x101,
        (
            "#00012F哈、哈哈……\x01",
            "（也许真会如他所说……）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(254320, 1330, 68620, 2000)
    Sound(898, 0, 100, 0)

    def lambda_812C():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_812C)
    Sleep(20)

    def lambda_8148():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8148)
    Sleep(20)

    def lambda_8164():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8164)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_819E")
    Sleep(20)

    def lambda_818A():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_818A)

    label("loc_819E")

    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x9, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81B8")
    WaitChrThread(0x109, 0x1)

    label("loc_81B8")

    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6F(0x79)
    Sleep(200)

    NpcTalk(
        0x9,
        "琪雅企鹅",
        (
            "呜呜～\x01",
            "投降投降……\x02\x03",
            "快放开我吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_6C(0x55F0, 0x9C4)
    FadeToDark(2000, 0, -1)
    Sound(898, 0, 100, 0)

    def lambda_8222():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8222)
    Sleep(20)

    def lambda_823E():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_823E)
    Sleep(20)

    def lambda_825A():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_825A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8294")
    Sleep(20)

    def lambda_8280():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8280)

    label("loc_8294")

    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x9, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82AE")
    WaitChrThread(0x109, 0x1)

    label("loc_82AE")

    OP_0D()
    OP_64(0x9)
    SetChrName("")
    OP_5B(0xE, 0x118, 0x3C, 0x3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "之后，女孩子们又过了很久\x01",
            "才渐渐恢复理智……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "由于过于危险，大家定下了规则，\x01",
            "以后严禁琪雅再穿企鹅装出现了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(9, 0, 100, 0)
    SetChrName("")
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "把所有玩偶赠送给琪雅了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_21(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    OP_A2(0x9, 0x80)
    OP_A3(0x101, 0x4)
    OP_A3(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83A7")
    OP_A2(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_83A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83C0")
    OP_A2(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)

    label("loc_83C0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83D9")
    OP_A2(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)

    label("loc_83D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_83F2")
    OP_A2(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)

    label("loc_83F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_840B")
    OP_A2(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_840B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8424")
    OP_A2(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_8424")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    OP_73(0x12, 0x4)
    SetScenarioFlags(0x12D, 4)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0130", 112, 0, 0)
    IdleLoop()
    Return()

    # Function_51_6BB2 end

    def Function_52_844B(): pass

    label("Function_52_844B")

    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    Sound(812, 0, 100, 0)
    OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x1F4, 0xBB8)
    OP_A3(0xFE, 0x4)
    OP_A2(0x9, 0x1)
    OP_95(0xFE, 0x3DF7C, 0x1E, 0x10540, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_844B end

    def Function_53_849A(): pass

    label("Function_53_849A")

    OP_95(0xFE, 0x3E418, 0x1E, 0xFB7B, 0x7D0, 0x1)
    OP_95(0xFE, 0x3EA80, 0x1E, 0xFA00, 0x7D0, 0x0)
    Return()

    # Function_53_849A end

    def Function_54_84C3(): pass

    label("Function_54_84C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8561")
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_84EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8501")
    Sleep(150)
    Jump("loc_84EA")

    label("loc_8501")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8515")
    Jump("loc_8561")

    label("loc_8515")

    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)

    label("loc_8531")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8548")
    Sleep(150)
    Jump("loc_8531")

    label("loc_8548")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_855C")
    Jump("loc_8561")

    label("loc_855C")

    Jump("Function_54_84C3")

    label("loc_8561")

    Return()

    # Function_54_84C3 end

    def Function_55_8562(): pass

    label("Function_55_8562")

    OP_9B(0x0, 0xFE, 0x0, 0xA28, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_55_8562 end

    def Function_56_8579(): pass

    label("Function_56_8579")

    OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_56_8579 end

    def Function_57_8590(): pass

    label("Function_57_8590")

    OP_9B(0x0, 0xFE, 0xFFF6, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_57_8590 end

    def Function_58_85A7(): pass

    label("Function_58_85A7")

    OP_9B(0x0, 0xFE, 0xA, 0xBB8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_58_85A7 end

    def Function_59_85BE(): pass

    label("Function_59_85BE")

    OP_95(0xFE, 0x3E59E, 0x1E, 0x10DEC, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_59_85BE end

    def Function_60_85DA(): pass

    label("Function_60_85DA")

    OP_95(0xFE, 0x3E30A, 0x1E, 0x10FEA, 0x1388, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Return()

    # Function_60_85DA end

    def Function_61_85F6(): pass

    label("Function_61_85F6")

    OP_95(0xFE, 0x3E29C, 0x1E, 0x10D4C, 0x1388, 0x0)
    OP_93(0xFE, 0x2D, 0x0)
    Return()

    # Function_61_85F6 end

    def Function_62_8612(): pass

    label("Function_62_8612")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_861B():
        OP_9D(0xFE, 0x3E800, 0x0, 0x1084C, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_861B)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 0x2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_62_8612 end

    def Function_63_8651(): pass

    label("Function_63_8651")

    SetChrChipByIndex(0xFE, 0xFF)

    def lambda_865A():
        OP_9D(0xFE, 0x3E8C8, 0x0, 0x109DC, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_865A)
    BeginChrThread(0xFE, 3, 0, 64)
    WaitChrThread(0xFE, 0x2)
    EndChrThread(0xFE, 0x3)
    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_63_8651 end

    def Function_64_8697(): pass

    label("Function_64_8697")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86C3")
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Jump("Function_64_8697")

    label("loc_86C3")

    Return()

    # Function_64_8697 end

    def Function_65_86C4(): pass

    label("Function_65_86C4")

    OP_95(0xFE, 0x3E31E, 0x1E, 0x10734, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_65_86C4 end

    def Function_66_86E0(): pass

    label("Function_66_86E0")

    OP_95(0xFE, 0x3E332, 0x1E, 0x1034C, 0x7D0, 0x1)
    OP_95(0xFE, 0x3E724, 0x1E, 0x10522, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_66_86E0 end

    def Function_67_8710(): pass

    label("Function_67_8710")

    OP_95(0xFE, 0x3E256, 0x1E, 0x10798, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_67_8710 end

    def Function_68_872C(): pass

    label("Function_68_872C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3657)
    SoundLoad(3039)
    SoundLoad(3660)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51100.itc", 0x1E)
    OP_68(253500, 1100, 71300, 0)
    OP_6D(0x2D, 0x1B, 0x0, 0x0)
    OP_6E(0x190, 0x0)
    OP_6C(0x5208, 0x0)
    SetChrPos(0x101, 251000, 0, 66000, 90)
    SetChrPos(0x102, 251000, 0, 66000, 90)
    SetChrPos(0x109, 251000, 0, 66000, 90)
    SetChrPos(0x105, 251000, 0, 66000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A2(0x153, 0x4)
    SetChrPos(0x153, 254100, 200, 71300, 270)
    SetChrChipByIndex(0x153, 0x1)
    SetChrSubChip(0x153, 0x0)
    OP_6C(0x55F0, 0x5DC)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        (
            "#01111F#3657V#11P#40W唔……只要把这个值\x01",
            "代入这个等式……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE49)
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)
    OP_63(0x153, 0x0, 1700, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x153,
        "#01109F#3039V#11P#30W#4S嗯！做完了！\x02",
    )

    CloseMessageWindow()
    OP_24(0xBDF)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    Sound(808, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x101,
        "罗伊德的声音",
        "琪雅？\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x153, 0x1)
    Sound(103, 0, 100, 0)
    OP_68(254000, 1100, 69900, 3000)
    OP_6D(0x2D, 0x17, 0x0, 0xBB8)
    OP_6C(0x59D8, 0xBB8)
    BeginChrThread(0x101, 3, 0, 69)
    BeginChrThread(0x102, 3, 0, 70)
    BeginChrThread(0x109, 3, 0, 71)
    BeginChrThread(0x105, 3, 0, 72)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x153,
        "#01110F#3660V#5P#15A#30W啊，罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0x3)

    ChrTalk(
        0x101,
        (
            "#00005F#11P琪雅，你今天要去\x01",
            "主日学校上课吧？\x02\x03",
            "#00000F还不赶快出发吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105F#5P啊……嗯，\x01",
            "确实快到我和朋友约定的时间了。\x02\x03",
            "#01100F大家要去工作吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x3)
    WaitChrThread(0x109, 0x3)
    WaitChrThread(0x105, 0x3)

    ChrTalk(
        0x102,
        (
            "#12P#00109F嗯，你要是愿意，\x01",
            "我们就一起出门吧。\x02\x03",
            "#00105F啊……\x01",
            "在预习主日学校的功课吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01109F#5P嘿嘿，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#12P小琪雅真了不起。\x02\x03",
            "#10106F我当年在主日学校上课的时候，\x01",
            "好像很少预习呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，我更是连课都\x01",
            "几乎没去听过。\x02\x03",
            "#10302F比起听那些半桶水的神父讲课，\x01",
            "还是自学的效率比较高。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B8D():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B8D)
    Sleep(150)

    def lambda_8B9D():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8B9D)
    Sleep(150)

    def lambda_8BAD():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8BAD)
    Sleep(150)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x109, 0x0)

    def lambda_8BC9():

        label("loc_8BC9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_8BC9")

    QueueWorkItem2(0x101, 2, lambda_8BC9)

    def lambda_8BDB():

        label("loc_8BDB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_8BDB")

    QueueWorkItem2(0x102, 2, lambda_8BDB)

    def lambda_8BED():

        label("loc_8BED")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_8BED")

    QueueWorkItem2(0x109, 2, lambda_8BED)

    ChrTalk(
        0x101,
        "#5P#00001F瓦吉，你可真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00111F#11P别给小琪雅造成\x01",
            "不良影响啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01100F#5P嗯～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F哟，爸爸妈妈都生气了。\x02\x03",
            "#10305F……哎？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C9C():
        OP_95(0xFE, 0x3DC48, 0x1E, 0x10EB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8C9C)
    WaitChrThread(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10301F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11P瓦吉？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01105F#5P嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F没什么，我只是在想，克洛斯贝尔\x01",
            "在各种方面都走在其它地方的前面啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10300F话说回来，我们不是要出门吗？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)

    ChrTalk(
        0x101,
        "#00000F#11P是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    def lambda_8DC9():

        label("loc_8DC9")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_8DC9")

    QueueWorkItem2(0x101, 2, lambda_8DC9)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00000F#11P琪雅，一起走吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#5P嗯！\x01",
            "稍等一下哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_8E23():

        label("loc_8E23")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_8E23")

    QueueWorkItem2(0x105, 2, lambda_8E23)

    def lambda_8E35():

        label("loc_8E35")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_8E35")

    QueueWorkItem2(0x102, 2, lambda_8E35)

    def lambda_8E47():

        label("loc_8E47")

        TurnDirection(0xFE, 0x153, 500)
        Yield()
        Jump("loc_8E47")

    QueueWorkItem2(0x109, 2, lambda_8E47)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    Sound(802, 0, 100, 0)
    OP_68(255000, 1100, 69700, 3000)
    OP_9D(0x153, 0x3E0F8, 0x0, 0x11940, 0x12C, 0xBB8)
    OP_A3(0x153, 0x4)
    OP_93(0x153, 0x2D, 0x1F4)

    def lambda_8E9B():
        OP_95(0xFE, 0x3E6D4, 0x0, 0x11C60, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8E9B)
    WaitChrThread(0x153, 0x1)
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x153, 0x1E)
    SetChrSubChip(0x153, 0x0)
    OP_0D()
    OP_93(0x153, 0xB4, 0x1F4)
    OP_A2(0x153, 0x1000)

    def lambda_8EDD():
        OP_95(0xFE, 0x3E6D4, 0x1E, 0x11300, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8EDD)
    WaitChrThread(0x153, 0x1)
    OP_A3(0x153, 0x1000)
    OP_93(0x153, 0xE1, 0x1F4)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x153,
        "#5P#01110F嗯，久等了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002F好，那我们走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102F既然和琪雅一起走，\x01",
            "我们就从后门出去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    OP_D7(0x1E)
    RemoveParty(0x52, 0xFF)
    AddParty(0xA4, 0xFF, 0xFF)
    SetChrPos(0x0, 254700, 30, 69400, 225)
    SetScenarioFlags(0x126, 2)
    EventEnd(0x5)
    Return()

    # Function_68_872C end

    def Function_69_8FBC(): pass

    label("Function_69_8FBC")


    def lambda_8FC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8FC1)

    def lambda_8FD2():
        OP_95(0xFE, 0x3DC48, 0x0, 0x101D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FD2)
    WaitChrThread(0xFE, 0x1)

    def lambda_8FF0():
        OP_95(0xFE, 0x3E030, 0x0, 0x10EB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FF0)
    WaitChrThread(0xFE, 0x1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_69_8FBC end

    def Function_70_9011(): pass

    label("Function_70_9011")

    Sleep(700)

    def lambda_9019():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9019)

    def lambda_902A():
        OP_95(0xFE, 0x3DC48, 0x0, 0x101D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_902A)
    WaitChrThread(0xFE, 0x1)

    def lambda_9048():
        OP_95(0xFE, 0x3E15C, 0x0, 0x10ACC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9048)
    WaitChrThread(0xFE, 0x1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_70_9011 end

    def Function_71_9069(): pass

    label("Function_71_9069")

    Sleep(1400)

    def lambda_9071():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9071)

    def lambda_9082():
        OP_95(0xFE, 0x3DC48, 0x0, 0x101D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9082)
    WaitChrThread(0xFE, 0x1)

    def lambda_90A0():
        OP_95(0xFE, 0x3E47C, 0x0, 0x1093C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90A0)
    WaitChrThread(0xFE, 0x1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_71_9069 end

    def Function_72_90C1(): pass

    label("Function_72_90C1")

    Sleep(2100)

    def lambda_90C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_90C9)

    def lambda_90DA():
        OP_95(0xFE, 0x3DC48, 0x0, 0x101D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90DA)
    WaitChrThread(0xFE, 0x1)

    def lambda_90F8():
        OP_95(0xFE, 0x3DCAC, 0x0, 0x1093C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90F8)
    WaitChrThread(0xFE, 0x1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_72_90C1 end

    def Function_73_9119(): pass

    label("Function_73_9119")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    OP_6D(0x2D, 0x17, 0x0, 0x0)
    OP_6E(0x190, 0x0)
    OP_6C(0x5BCC, 0x0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_91FC():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_91FC)
    Sleep(200)

    def lambda_9219():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9219)
    Sleep(200)

    def lambda_9236():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9236)
    OP_6C(0x57E4, 0x7D0)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_9271():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9271)
    Sleep(400)

    def lambda_9285():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9285)
    Sleep(400)

    def lambda_9299():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9299)

    def lambda_92AA():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92AA)
    Sleep(300)

    def lambda_92C7():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92C7)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        "#00003F#11P那个……兰迪。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_5B(0xE, 0x118, 0x23, 0x3)
    Sleep(300)

    AnonymousTalk(
        0x104,
        "怎么了，罗伊德？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00008F#11P该怎么说呢……\x01",
            "关于你的父亲……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00306F哦，那件事啊……\x02\x03",
            "#00300F其实我并不是很在意啦。\x01",
            "在那个世界里，这并不算什么稀罕事。\x02\x03",
            "而且，在离开猎兵团的时候，\x01",
            "我和父亲之间就已经没什么关系了。\x02\x03",
            "#00304F当然，肯定不会毫无感觉……\x01",
            "但却也觉得好像松了口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P……是吗。\x02\x03",
            "#00001F等你有心情的时候，\x01",
            "给我讲讲过去的事吧？\x02\x03",
            "说不定我能\x01",
            "以队长的角度\x01",
            "提出一些想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#11P啊，抱歉，\x01",
            "我是不是有些自以为是了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F哈哈，没有没有。\x02\x03",
            "#00302F我只是在想，\x01",
            "你也成长了不少呢。\x02\x03",
            "#00309F嗯～哥哥我感慨颇深啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_97E1")

    ChrTalk(
        0x101,
        "#00006F#11P你可真是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00008F#11P……总之，在这种时候，\x01",
            "我很想为你做点什么。\x02\x03",
            "#00000F也许我现在还不够可靠，\x01",
            "但所谓的『搭档』，就是要互相依赖吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    OP_6C(0x55F0, 0x3E8)

    def lambda_970A():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_970A)
    WaitChrThread(0x104, 0x1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    OP_A2(0x104, 0x10)
    OP_A2(0x104, 0x2)
    OP_A2(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    OP_A2(0x101, 0x10)
    OP_A2(0x101, 0x2)
    OP_A2(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00302F……明白了，我以后\x01",
            "或许会和你好好聊聊。\x02\x03",
            "#00309F到时就要麻烦你了哦──搭档。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9875")

    label("loc_97E1")


    ChrTalk(
        0x101,
        "#00006F#11P你可真是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F……好啦，如果我以后有心情，\x01",
            "说不定会和你聊一聊。\x02\x03",
            "#00300F到时就要麻烦你了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_9875")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    NpcTalk(
        0x105,
        "瓦吉的声音",
        "#2P#2S哎？你们在干什么？\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x102,
        "艾莉的声音",
        "#2P#2S你们两个忘带东西了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_9972")
    OP_6C(0x57E4, 0x2BC)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_A3(0x104, 0x10)
    OP_A3(0x104, 0x2)
    OP_A3(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_A3(0x101, 0x10)
    OP_A3(0x101, 0x2)
    OP_A3(0x101, 0x20)

    def lambda_9959():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9959)
    WaitChrThread(0x104, 0x1)

    label("loc_9972")


    def lambda_9977():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9977)

    ChrTalk(
        0x101,
        "#00011F#11P抱歉，马上就出发！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00304F好，不要着急，\x01",
            "慢慢处理工作吧。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_99DD():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_99DD)
    Sleep(100)

    def lambda_99FA():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_99FA)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_9A21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9A21)
    Sleep(400)

    def lambda_9A35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A35)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "从现在开始，可以驾驶导力车，快速驶往\x01",
            "克洛斯贝尔自治州内的各个地区了。\x02\x03",
            "导力车停在位于西街的特别任务支援科后门，\x01",
            "请多加利用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_73_9119 end

    def Function_74_9B3D(): pass

    label("Function_74_9B3D")

    EventBegin(0x0)
    Fade(500)
    OP_68(256290, 1300, 67750, 0)
    OP_6D(0x32, 0x12, 0x0, 0x0)
    OP_6E(0x15E, 0x0)
    OP_6C(0x57B2, 0x0)
    SetChrPos(0x101, 255980, 0, 68000, 90)
    SetChrPos(0x102, 255700, 30, 68900, 90)
    SetChrPos(0x103, 255360, 0, 67250, 90)
    SetChrPos(0x104, 254500, 0, 68200, 90)
    SetChrPos(0x109, 253700, 30, 68850, 90)
    SetChrPos(0x105, 253800, 0, 67250, 90)
    OP_A3(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A3(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P#01100F大家路上小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109F呵呵，我们走了，小琪雅。\x02\x03",
            "#10106F……短时间内，\x01",
            "再也不能像现在这样听到\x01",
            "小琪雅说『路上小心』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002F哈哈……确实让人很失落呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F和小琪雅分开这种事，\x01",
            "光是想想都受不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#01100F诺艾尔离开这里，\x01",
            "琪雅也会寂寞的……\x01",
            "不过，要打起精神哦，诺艾尔。\x02\x03",
            "#01109F我还等着芙兰康复之后，\x01",
            "你们两个一起过来玩呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10102F嗯，谢谢你，小琪雅。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F哈哈，既然如此，\x01",
            "诺艾尔，你可要尽快完成\x01",
            "警备队的整顿任务啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202F也希望芙兰小姐\x01",
            "能早日康复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10109F呵呵，是啊。\x02\x03",
            "#10100F为了早日重见小琪雅的笑脸，\x01",
            "我一定会加油的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10302F哎呀呀，好像斗志高昂了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P#01102F嘿嘿……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x19D, 5)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    OP_A2(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_A2(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 255700, 0, 68570, 90)
    EventEnd(0x5)
    Return()

    # Function_74_9B3D end

    SaveToFile()

Try(main)
