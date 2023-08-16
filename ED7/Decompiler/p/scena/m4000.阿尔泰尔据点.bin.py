from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4000.bin",                # FileName
        "m4000",                    # MapName
        "m4000",                    # Location
        0x007A,                     # 阿尔泰尔据点
        "ed70151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x18\xfc\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0]\x00\x00\xf4\x01\x00\x00\x1e\x00-\x00\x00\x00h\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00z\x00\x00\x02\x00\x03',
    )

    BuildStringList((
        "m4000",                  # 0
        "共和国军士官",           # 1
        "剧情用魔兽",             # 2
        "剧情用魔兽",             # 3
        "bm4000",                 # 4
    ))

    ATBonus("ATBonus_13C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_15C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_1FC", 0x0002, 3, 6, 45, 3, 3, 30, 0, "bm4000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72200.dat", "ms72200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_15C", "MonsterBattlePostion_1DC", "ed70452", "ed70453", "ATBonus_13C"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-6660,   0,       27520,   1200,    -6660,   2000,    27520,   0x007C, 0,  4,  0x0000)

    ChipFrameInfo(620, 0)                                        # 0

    ScpFunction((
        "Function_0_26C",          # 00, 0
        "Function_1_28B",          # 01, 1
        "Function_2_2AA",          # 02, 2
        "Function_3_306",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_66B",          # 05, 5
        "Function_6_1841",         # 06, 6
        "Function_7_189C",         # 07, 7
        "Function_8_1934",         # 08, 8
        "Function_9_19CC",         # 09, 9
        "Function_10_1A60",        # 0A, 10
    ))


    def Function_0_26C(): pass

    label("Function_0_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_26C")

    label("loc_28A")

    Return()

    # Function_0_26C end

    def Function_1_28B(): pass

    label("Function_1_28B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A9")
    OP_A1(0xFE, 0x4B0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_28B")

    label("loc_2A9")

    Return()

    # Function_1_28B end

    def Function_2_2AA(): pass

    label("Function_2_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2BC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 5)
    SetScenarioFlags(0x0, 0)

    label("loc_2BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_305")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305")
    SetChrPos(0x0, -6660, 0, 27520, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_305")

    Return()

    # Function_2_2AA end

    def Function_3_306(): pass

    label("Function_3_306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_31B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_31B")

    MiniGame(0x2F, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_3_306 end

    def Function_4_33E(): pass

    label("Function_4_33E")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_370")
    SetScenarioFlags(0x31, 2)

    label("loc_370")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3B0")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A5")
    Sound(2499, 255, 100, 0)
    Jump("loc_3AB")

    label("loc_3A5")

    Sound(3537, 255, 100, 0)

    label("loc_3AB")

    Jump("loc_3B6")

    label("loc_3B0")

    Sound(3344, 255, 100, 0)

    label("loc_3B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_427")
    MenuCmd(0x0, 0x0)
    MenuCmd(0x1, 0x0, "登上梅尔卡瓦")
    MenuCmd(0x1, 0x0, "放弃")
    MenuCmd(0x2, 0x0, 0xFFFF, 0xFFFF, 0x1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_407"),
        (SWITCH_DEFAULT, "loc_418"),
    )


    label("loc_407")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_422")

    label("loc_418")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_422")

    Jump("loc_658")

    label("loc_427")

    MenuCmd(0x0, 0x0)
    MenuCmd(0x1, 0x0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_457")
    MenuCmd(0x1, 0x0, "在导力车中休息")

    label("loc_457")

    MenuCmd(0x2, 0x0, 0xFFFF, 0xFFFF, 0x1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_481"),
        (1, "loc_585"),
        (2, "loc_616"),
        (SWITCH_DEFAULT, "loc_64E"),
    )


    label("loc_481")

    OP_76(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B2")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4C2")

    label("loc_4B2")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4C2")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_518")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_518")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B")
    Sound(461, 0, 100, 0)

    label("loc_53B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55B")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_56B")

    label("loc_55B")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_56B")

    Sleep(1000)
    OP_0D()
    OP_76(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_3B6")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_5F7")
    OP_57(0x0)
    OP_21(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_5BA")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_5D2")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_5CD")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_5D2")

    label("loc_5CD")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_5D2")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_611")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_607")
    OP_AF(0xFB)
    Jump("loc_611")

    label("loc_607")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_611")

    Jump("loc_658")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_649")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_63F")
    OP_AF(0xFB)
    Jump("loc_649")

    label("loc_63F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_649")

    Jump("loc_658")

    label("loc_64E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_658")

    Jump("loc_3B6")

    label("loc_65D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_33E end

    def Function_5_66B(): pass

    label("Function_5_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_676")
    OutputDebugInt(0xC8)

    label("loc_676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_END)), "loc_681")
    OutputDebugInt(0x6F)

    label("loc_681")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetScenarioFlags(0x20, 0)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x20, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_6AB")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_6BD")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6CF")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6DB")
    SetScenarioFlags(0x2C, 0)

    label("loc_6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_6F0")
    SetScenarioFlags(0x2C, 2)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_705")
    SetScenarioFlags(0x2C, 4)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_71A")
    SetScenarioFlags(0x2C, 6)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730")
    OP_3B(0x4E20)
    Jump("loc_75F")

    label("loc_730")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746")
    OP_3B(0x2710)
    Jump("loc_75F")

    label("loc_746")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x21), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C")
    OP_3B(0x1388)
    Jump("loc_75F")

    label("loc_75C")

    OP_3B(0x7D0)

    label("loc_75F")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    LoadChrToIndex("chr/ch00950.itc", 0x20)
    LoadChrToIndex("chr/ch02450.itc", 0x21)
    LoadChrToIndex("chr/ch41200.itc", 0x22)
    LoadChrToIndex("monster/ch72250.itc", 0x23)
    LoadChrToIndex("monster/ch72250.itc", 0x24)
    LoadChrToIndex("monster/ch72252.itc", 0x25)
    CreatePortrait(0, 16, 20, 528, 84, 0, 10, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis500.itp")
    SoundLoad(3306)
    SoundLoad(3307)
    SoundLoad(3308)
    SoundLoad(3309)
    SoundLoad(3310)
    SoundLoad(3508)
    SoundLoad(3509)
    SoundLoad(3510)
    SoundLoad(3443)
    SoundLoad(3444)
    SoundLoad(3445)
    SoundLoad(3446)
    SoundLoad(3447)
    SoundLoad(4042)
    SoundLoad(4043)
    SoundLoad(4044)
    SoundLoad(4045)
    SoundLoad(4046)
    SetChrPos(0x101, 31000, 0, -56000, 330)
    SetChrPos(0x109, 31000, 0, -56000, 330)
    SetChrPos(0x108, 31000, 0, -56000, 330)
    SetChrPos(0x10A, 31000, 0, -56000, 330)
    SetChrPos(0x8, 31000, 0, -56000, 330)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    OP_A3(0x8, 0x80)
    OP_A2(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    OP_A2(0x9, 0x8000)
    OP_A7(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x9, 1300, 0, 55000, 180)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    OP_A2(0xA, 0x8000)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0xA, 2000, 0, 55000, 180)
    Sleep(1000)
    OP_C9(0x0, 0x800)
    OP_5B(0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "#30W#40A七耀历１２０４年的某月……",
            scpstr(0x6),
            scpstr(0x2),
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    AnonymousTalk(
        0xFF,
        (
            "#30W#50A卡尔瓦德共和国西端，\x01",
            "阿尔泰尔市的郊外……",
            scpstr(0x6),
            scpstr(0x2),
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_5B(0xE, 0x118, 0x3C, 0x3)
    OP_C9(0x1, 0x800)
    OP_68(23000, 2000, -43500, 0)
    OP_6D(0x154, 0x17, 0x0, 0x0)
    OP_6E(0x2BC, 0x0)
    OP_6C(0x8CA0, 0x0)
    PlayBGM("ed70151", 0)
    OP_6D(0x145, 0x17, 0x0, 0x36B0)
    OP_6C(0x7530, 0x36B0)
    FadeToBright(2000, 0)
    BeginChrThread(0x8, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x109, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x108, 3, 0, 6)
    Sleep(800)
    BeginChrThread(0x10A, 3, 0, 6)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(8000, 2000, -26600, 0)
    OP_6D(0x14F, 0x17, 0x0, 0x0)
    OP_6E(0x2BC, 0x0)
    OP_6C(0x3E80, 0x0)
    OP_68(8000, 2000, -20600, 5500)
    OP_6D(0x14F, 0x7, 0x0, 0x157C)
    OP_6C(0x4650, 0x157C)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x108, 0xFF)
    EndChrThread(0x10A, 0xFF)
    SetChrPos(0x8, 8000, 0, -31600, 0)
    SetChrPos(0x101, 8000, 0, -34400, 0)
    SetChrPos(0x109, 8400, 0, -36100, 0)
    SetChrPos(0x108, 6600, 0, -35100, 0)
    SetChrPos(0x10A, 7000, 0, -36500, 0)

    def lambda_A87():
        OP_97(0x8, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A87)
    Sleep(50)

    def lambda_AA4():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA4)
    Sleep(50)

    def lambda_AC1():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC1)
    Sleep(50)

    def lambda_ADE():
        OP_97(0x108, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_ADE)
    Sleep(50)

    def lambda_AFB():
        OP_97(0x10A, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_AFB)
    Sleep(50)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x108, 0x0)
    WaitChrThread(0x10A, 0x0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x8,
        "到了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x101,
        "#00005F#3306V#5P#30W啊……！\x02",
    )

    CloseMessageWindow()
    OP_24(0xCEA)
    OP_68(2000, 5000, 46000, 5000)
    OP_6D(0x15, 0x11, 0x0, 0x1388)
    OP_6C(0xA410, 0x1388)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(2110, 23000, 50810, 0)
    OP_6D(0x165, 0xFFF9, 0x0, 0x0)
    OP_6E(0x2BC, 0x0)
    OP_6C(0xD6D8, 0x0)
    OP_68(2110, 13000, 51000, 8000)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Sleep(300)
    OP_5B(0xE, 0x118, 0xFFFF, 0x3)

    ChrTalk(
        0x108,
        "#01400F#4042V#3P#N#30W……完全没变呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00001F#3307V#4P#N#30W这里就是阿尔泰尔据点……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10101F#3508V#4P#N#30W六年前救出\x01",
            "缇欧的地方吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#00601F#3443V#3P#N#30W哼……\x01",
            "真是个低级趣味的入口啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD73)
    Fade(500)
    OP_68(2000, 1100, 33600, 0)
    OP_6D(0x14A, 0xD, 0x0, 0x0)
    OP_6E(0x226, 0x0)
    OP_6C(0x5014, 0x0)
    OP_6C(0x445C, 0xBB8)
    SetChrPos(0x101, 2000, 0, 27600, 0)
    SetChrPos(0x109, 2400, 0, 25900, 0)
    SetChrPos(0x108, 600, 0, 26900, 0)
    SetChrPos(0x10A, 1000, 0, 25500, 0)
    SetChrPos(0x8, 2000, 0, 30400, 0)

    def lambda_D93():
        OP_97(0x8, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_D93)
    Sleep(50)

    def lambda_DB0():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DB0)
    Sleep(50)

    def lambda_DCD():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DCD)
    Sleep(50)

    def lambda_DEA():
        OP_97(0x108, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_DEA)
    Sleep(50)

    def lambda_E07():
        OP_97(0x10A, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_E07)
    Sleep(50)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x108, 0x0)
    WaitChrThread(0x10A, 0x0)
    OP_6F(0x79)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        "#11P我就带路到这里了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P顺便提醒一下，你们的行动期限\x01",
            "截止至本日１７：００……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P如果超越时限，我军部队\x01",
            "将会采取强制镇压措施。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x10A,
        "#3P#00603F#3444V……明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x108,
        "#01400F#4043V多谢你耐心带路。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xFCB)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#11P总之，你们几个就多加小心吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P既然有大名鼎鼎的『风之剑圣』随行，\x01",
            "应该也不必担心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_F9B():

        label("loc_F9B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_F9B")

    QueueWorkItem2(0x101, 2, lambda_F9B)

    def lambda_FAD():

        label("loc_FAD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FAD")

    QueueWorkItem2(0x109, 2, lambda_FAD)

    def lambda_FBF():

        label("loc_FBF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FBF")

    QueueWorkItem2(0x108, 2, lambda_FBF)

    def lambda_FD1():

        label("loc_FD1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_FD1")

    QueueWorkItem2(0x10A, 2, lambda_FD1)

    def lambda_FE3():
        OP_95(0xFE, 0xED8, 0x0, 0x7B70, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FE3)
    WaitChrThread(0x8, 0x1)
    OP_68(2000, 1100, 31600, 3000)

    def lambda_1012():
        OP_95(0xFE, 0x3E8, 0x0, 0x5208, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1012)
    WaitChrThread(0x8, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x108, 0x2)
    EndChrThread(0x10A, 0x2)
    OP_A2(0x8, 0x80)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x109,
        (
            "#12P#10106F#3509V#30W唔……似乎并不是\x01",
            "很欢迎我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00006F#3308V#11P#30W算啦，站在他的角度上想一想，\x01",
            "就如同自己的领地中闯进了罪犯，\x01",
            "却只得交给外人去处理一样。\x02\x03",
            "#00001F#3309V怎么办？\x01",
            "我们这就进去吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1121():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1121)
    Sleep(50)

    def lambda_1131():
        TurnDirection(0x108, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1131)
    Sleep(50)

    def lambda_1141():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1141)
    Sleep(50)
    WaitChrThread(0x108, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(
        0x10A,
        "#6P#00603F#3445V#30W嗯，已经没时间犹豫了。\x02",
    )

    CloseMessageWindow()
    OP_24(0xD75)
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#6P#00601F#3446V#30W……马克莱因，\x01",
            "里面会不会有机关或陷阱？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11D7():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11D7)
    Sleep(100)

    def lambda_11E7():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11E7)
    Sleep(200)

    ChrTalk(
        0x108,
        (
            "#01403F#4044V#5P#30W在六年前的镇压作战中，\x01",
            "那些东西基本都被我们破坏掉了。\x02\x03",
            "#01401F#4045V但是，徘徊在其中的魔兽却……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFCD)
    OP_21(0xFA0)
    OP_93(0x108, 0x0, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x108, 0x21)
    SetChrSubChip(0x108, 0x0)
    Sound(932, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 30, 0)
    Sound(540, 0, 30, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(2000, 1500, 47500, 2000)
    OP_6D(0x14A, 0xF, 0x0, 0x7D0)
    OP_6E(0x28A, 0x7D0)
    OP_6C(0x38A4, 0x7D0)

    def lambda_1322():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1322)
    Sleep(50)

    def lambda_1332():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1332)
    Sleep(50)

    def lambda_1342():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1342)
    Sleep(50)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed70452", 0)
    Sound(831, 0, 100, 0)
    OP_82(0x0, 0x32, 0xBB8, 0x1B58)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(900)
    BeginChrThread(0xA, 3, 0, 8)
    Sleep(1000)
    OP_68(2000, 1500, 45500, 3500)
    OP_6C(0x445C, 0xDAC)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(1700, 1300, 34600, 0)
    OP_6D(0x145, 0xD, 0x0, 0x0)
    OP_6E(0x28A, 0x0)
    OP_6C(0x3E80, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x9, 0x3)
    WaitChrThread(0xA, 0x3)

    ChrTalk(
        0x10A,
        "#3P#00610F#3447V#30W什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107F#3510V#30W魔、魔物……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00010F#3310V#30W曾在『太阳堡垒』中出现过的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#01407F#4046V#30W它们要来了！\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xFCE)
    Sound(830, 0, 100, 0)
    OP_82(0x96, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x9, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 9)
    Sleep(1050)

    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_6C(0x32C8, 0x1F4)
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_1525")
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1645")

    label("loc_1525")

    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x800), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x8000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x8000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x10000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x20000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1645")

    OP_C9(0x1, 0x80)
    OP_32(0x0, 0x0, 0x2D)
    OP_32(0x0, 0x5, 0x5A)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x0, 0x640, 0xFF)
    RemoveCraft(0x0, 0xFFFF)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x82, 0x1)
    OP_38(0x0, 0x85, 0x1)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0x97)
    AddCraft(0x0, 0x98)
    AddCraft(0x0, 0x99)
    AddCraft(0x0, 0x9A)
    AddCraft(0x0, 0x118)
    AddCraft(0x0, 0x119)
    SetChrChipPat(0x0, 0x6, 0x119)
    SetChrChipPat(0x0, 0x6, 0x11B)
    SetChrChipPat(0x0, 0x6, 0x11C)
    SetChrChipPat(0x0, 0x6, 0x11A)
    OP_32(0x8, 0x0, 0x2D)
    OP_32(0x8, 0x5, 0x5A)
    OP_42(0x8, 0x44C, 0xFF)
    OP_42(0x8, 0x5DC, 0xFF)
    OP_42(0x8, 0x640, 0xFF)
    RemoveCraft(0x8, 0xFFFF)
    OP_38(0x8, 0x80, 0x2)
    OP_38(0x8, 0x81, 0x1)
    OP_38(0x8, 0x84, 0x1)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0xE9)
    AddCraft(0x8, 0x140)
    SetChrChipPat(0x8, 0x6, 0x140)
    SetChrChipPat(0x8, 0x6, 0x143)
    OP_32(0x9, 0x0, 0x3C)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x465, 0xFF)
    OP_42(0x9, 0x5DC, 0xFF)
    OP_42(0x9, 0x640, 0xFF)
    OP_42(0x9, 0x4C, 0x3)
    OP_42(0x9, 0x49, 0x4)
    RemoveCraft(0x9, 0xFFFF)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x82, 0x1)
    OP_38(0x9, 0x83, 0x1)
    OP_38(0x9, 0x84, 0x1)
    OP_42(0x9, 0xE8, 0x0)
    OP_42(0x9, 0x6C, 0x2)
    OP_42(0x9, 0xBA, 0x3)
    OP_42(0x9, 0x88, 0x4)
    AddCraft(0x9, 0xF5)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF7)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0xF4)
    AddCraft(0x9, 0x145)
    SetChrChipPat(0x9, 0x6, 0x145)
    SetChrChipPat(0x9, 0x6, 0x148)
    SetChrChipPat(0x9, 0x6, 0x146)
    OP_32(0x7, 0x0, 0x3C)
    OP_32(0x7, 0x5, 0xC8)
    OP_42(0x7, 0x46A, 0xFF)
    OP_42(0x7, 0x5DC, 0xFF)
    OP_42(0x7, 0x640, 0xFF)
    OP_42(0x7, 0x33, 0x3)
    OP_42(0x7, 0x51, 0x4)
    RemoveCraft(0x7, 0xFFFF)
    OP_38(0x7, 0x80, 0x2)
    OP_38(0x7, 0x81, 0x1)
    OP_38(0x7, 0x82, 0x1)
    OP_38(0x7, 0x85, 0x1)
    OP_38(0x7, 0x86, 0x1)
    OP_84(0x15, 0x4)
    OP_42(0x7, 0xF1, 0x0)
    OP_42(0x7, 0x6C, 0x1)
    OP_42(0x7, 0x7C, 0x2)
    OP_42(0x7, 0x80, 0x5)
    OP_42(0x7, 0x88, 0x6)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0x13B)
    SetChrChipPat(0x7, 0x6, 0x13B)
    AddItemNumber(0x1F4, 20)
    AddItemNumber(0x1F8, 3)
    AddItemNumber(0x1FB, 3)
    AddItemNumber(0x20B, 3)
    AddItemNumber(0x20E, 10)
    AddItemNumber(0x1, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x320, 1)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x21, 4)

    CancelBlur(0)

    import TiosBed
    TiosBed.ShowMenu()

    Battle("BattleInfo_1FC", 0x0, 0x0, 0x0, 0x8, 0xFF)
    FadeToDark(0, 0, -1)
    OP_A2(0x9, 0x80)
    OP_A2(0xA, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 10)
    Return()

    # Function_5_66B end

    def Function_6_1841(): pass

    label("Function_6_1841")


    def lambda_1846():
        OP_95(0xFE, 0x5BCC, 0x0, 0xFFFF5808, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1846)
    WaitChrThread(0xFE, 0x1)

    def lambda_1864():
        OP_95(0xFE, 0x2EE0, 0x0, 0xFFFF7360, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1864)
    WaitChrThread(0xFE, 0x1)

    def lambda_1882():
        OP_95(0xFE, 0x1F40, 0x0, 0xFFFF9A70, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1882)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_6_1841 end

    def Function_7_189C(): pass

    label("Function_7_189C")

    OP_A3(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x9, 0x20)

    def lambda_18D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_18D4)
    BeginChrThread(0x9, 0, 0, 1)

    def lambda_18EB():
        OP_96(0xFE, 0x12C, 0x0, 0x9858, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18EB)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 0)
    Return()

    # Function_7_189C end

    def Function_8_1934(): pass

    label("Function_8_1934")

    OP_A3(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0xA, 0x20)

    def lambda_196C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_196C)
    BeginChrThread(0xA, 0, 0, 1)

    def lambda_1983():
        OP_96(0xFE, 0xBB8, 0x0, 0x98BC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1983)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 0)
    Return()

    # Function_8_1934 end

    def Function_9_19CC(): pass

    label("Function_9_19CC")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_19FE():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_19FE)
    WaitChrThread(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 1)

    def lambda_1A4A():
        OP_96(0xFE, 0x6A4, 0x0, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A4A)
    Return()

    # Function_9_19CC end

    def Function_10_1A60(): pass

    label("Function_10_1A60")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis400.itp")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    LoadChrToIndex("chr/ch00950.itc", 0x20)
    LoadChrToIndex("chr/ch02450.itc", 0x21)
    SoundLoad(3311)
    SoundLoad(3312)
    SoundLoad(3313)
    SoundLoad(3511)
    SoundLoad(3512)
    SoundLoad(3448)
    SoundLoad(3449)
    SoundLoad(3450)
    SoundLoad(4047)
    SoundLoad(4048)
    OP_68(1700, 1300, 34600, 0)
    OP_6D(0x145, 0xD, 0x0, 0x0)
    OP_6E(0x28A, 0x0)
    OP_6C(0x3E80, 0x0)
    SetChrPos(0x101, 2000, 0, 32600, 0)
    SetChrPos(0x109, 2400, 0, 30900, 0)
    SetChrPos(0x108, 600, 0, 31900, 0)
    SetChrPos(0x10A, 1000, 0, 30500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0x21)
    SetChrSubChip(0x108, 0x0)
    OP_68(1700, 1300, 33600, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(531, 0, 50, 0)
    Sound(540, 0, 50, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x10A,
        (
            "#3P#00607F#3448V#30W唔……\x01",
            "刚才那些怪物难道是……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#6P#10101F#3511V#30W感觉与『塔』和『僧院』\x01",
            "中的魔物很相似……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#5P#00003F#3311V#30W……和徘徊在『太阳堡垒』地下的\x01",
            "某种魔物是同一类别。\x02\x03",
            "#00013F#3312V看来『他们』确实\x01",
            "逃进了这个地方呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x10A,
        (
            "#3P#00610F#3449V#30W啧……\x01",
            "真是死不悔改的家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD79)
    TurnDirection(0x108, 0x109, 500)
    Sleep(300)

    ChrTalk(
        0x108,
        (
            "#01403F#4047V#5P#30W时间不多了，\x01",
            "我们赶快进去吧。\x02\x03",
            "#01401F#4048V如果尽快行动，现在应该还来得及。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xFD0)

    def lambda_1D8B():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D8B)
    Sleep(100)
    TurnDirection(0x109, 0x108, 500)
    Sleep(200)

    ChrTalk(
        0x101,
        "#2P#00007F#3313V#30W嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#4P#10107F#3512V#30W明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#3P#00607F#3450V#30W哼……\x01",
            "绝对不会让他们逃掉的！\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xD7A)

    def lambda_1E29():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E29)
    Sleep(50)

    def lambda_1E39():
        OP_93(0x108, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1E39)
    Sleep(50)

    def lambda_1E49():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E49)
    Sleep(50)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x108, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_68(1700, 1300, 38600, 4000)
    OP_6C(0x4650, 0xFA0)

    def lambda_1E7F():
        OP_97(0x101, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E7F)
    Sleep(50)

    def lambda_1E9C():
        OP_97(0x109, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E9C)
    Sleep(50)

    def lambda_1EB9():
        OP_97(0x108, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1EB9)
    Sleep(50)

    def lambda_1ED6():
        OP_97(0x10A, 0x0, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1ED6)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21(0xFA0)
    WaitBGM()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x108, 0xFF)
    OP_E5(0xA)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("m4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1A60 end

    SaveToFile()

Try(main)
