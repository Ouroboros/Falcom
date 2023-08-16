from ScenarioHelper import *

def main():
    CreateScenaFile(
        "a0000_2.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0001,                     # 克洛斯贝尔市
        -1,
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        b',\x01\x00\x00\xc8\x02\x00\x006\x04\x00\x00\xb9\x05\x00\x00Q\n\x00\x00\x8d\x0e\x00\x00>\x13\x00\x00\xb2\x14\x00\x00\xeb\x18\x00\x00s\x1d\x00\x00*"\x00\x00l#\x00\x00\xce\'\x00\x00\x11*\x00\x00\x17.\x00\x00\xc42\x00\x00',
    )

    BuildStringList((
        "a0000_2",                # 0
    ))

    ScpFunction((
        "Function_0_12C",          # 00, 0
        "Function_1_2C8",          # 01, 1
        "Function_2_436",          # 02, 2
        "Function_3_5B9",          # 03, 3
        "Function_4_A51",          # 04, 4
        "Function_5_E8D",          # 05, 5
        "Function_6_133E",         # 06, 6
        "Function_7_14B2",         # 07, 7
        "Function_8_18EB",         # 08, 8
        "Function_9_1D73",         # 09, 9
        "Function_10_222A",        # 0A, 10
        "Function_11_236C",        # 0B, 11
        "Function_12_27CE",        # 0C, 12
        "Function_13_2A11",        # 0D, 13
        "Function_14_2E17",        # 0E, 14
        "Function_15_32C4",        # 0F, 15
        "Function_16_37EB",        # 10, 16
        "Function_17_3A56",        # 11, 17
        "Function_18_3ED4",        # 12, 18
        "Function_19_43BB",        # 13, 19
        "Function_20_47EE",        # 14, 20
        "Function_21_4BCE",        # 15, 21
        "Function_22_4C35",        # 16, 22
        "Function_23_50AB",        # 17, 23
        "Function_24_5520",        # 18, 24
        "Function_25_59C1",        # 19, 25
        "Function_26_60BF",        # 1A, 26
        "Function_27_6B86",        # 1B, 27
        "Function_28_739A",        # 1C, 28
        "Function_29_7B73",        # 1D, 29
        "Function_30_82F0",        # 1E, 30
        "Function_31_8551",        # 1F, 31
        "Function_32_85B5",        # 20, 32
        "Function_33_85DD",        # 21, 33
        "Function_34_8674",        # 22, 34
        "Function_35_874A",        # 23, 35
        "Function_36_8784",        # 24, 36
        "Function_37_883C",        # 25, 37
        "Function_38_8891",        # 26, 38
        "Function_39_88AD",        # 27, 39
        "Function_40_899E",        # 28, 40
        "Function_41_8A6E",        # 29, 41
        "Function_42_8AE1",        # 2A, 42
        "Function_43_8B48",        # 2B, 43
        "Function_44_8B82",        # 2C, 44
        "Function_45_8C3A",        # 2D, 45
        "Function_46_8C8F",        # 2E, 46
        "Function_47_8CAB",        # 2F, 47
        "Function_48_8D9F",        # 30, 48
        "Function_49_91C0",        # 31, 49
        "Function_50_A9F3",        # 32, 50
        "Function_51_CB53",        # 33, 51
        "Function_52_D333",        # 34, 52
        "Function_53_F4BC",        # 35, 53
    ))


    label("Function_0_12C")

    Call(2, 31)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_139")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼０章①\x01",        # 0
            "▼１章①\x01",        # 1
            "▼１章②\x01",        # 2
            "▼１章③\x01",        # 3
            "▼２章①\x01",        # 4
            "▼２章②\x01",        # 5
            "▼２章③\x01",        # 6
            "▼２章④\x01",        # 7
            "▼幕間①\x01",        # 8
            "▼幕間②\x01",        # 9
            "▼３章①\x01",        # 10
            "▼３章②\x01",        # 11
            "▼３章③\x01",        # 12
            "▼３章④\x01",        # 13
            "Cancel\x01",      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23B"),
        (1, "loc_243"),
        (2, "loc_24B"),
        (3, "loc_253"),
        (4, "loc_25B"),
        (5, "loc_263"),
        (6, "loc_26B"),
        (7, "loc_273"),
        (8, "loc_27B"),
        (9, "loc_283"),
        (10, "loc_28B"),
        (11, "loc_293"),
        (12, "loc_29B"),
        (13, "loc_2A3"),
        (SWITCH_DEFAULT, "loc_2AB"),
    )


    label("loc_23B")

    Call(2, 3)
    Jump("loc_2B5")

    label("loc_243")

    Call(2, 4)
    Jump("loc_2B5")

    label("loc_24B")

    Call(2, 5)
    Jump("loc_2B5")

    label("loc_253")

    Call(2, 6)
    Jump("loc_2B5")

    label("loc_25B")

    Call(2, 7)
    Jump("loc_2B5")

    label("loc_263")

    Call(2, 8)
    Jump("loc_2B5")

    label("loc_26B")

    Call(2, 9)
    Jump("loc_2B5")

    label("loc_273")

    Call(2, 10)
    Jump("loc_2B5")

    label("loc_27B")

    Call(2, 11)
    Jump("loc_2B5")

    label("loc_283")

    Call(2, 12)
    Jump("loc_2B5")

    label("loc_28B")

    Call(2, 13)
    Jump("loc_2B5")

    label("loc_293")

    Call(2, 14)
    Jump("loc_2B5")

    label("loc_29B")

    Call(2, 15)
    Jump("loc_2B5")

    label("loc_2A3")

    Call(2, 16)
    Jump("loc_2B5")

    label("loc_2AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B5")

    Jump("loc_139")

    label("loc_2BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_0_12C end


    label("Function_1_2C8")

    Call(2, 31)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_428")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼４章①\x01",        # 0
            "▼４章②\x01",        # 1
            "▼４章③\x01",        # 2
            "▼断章①\x01",        # 3
            "▼終章①\x01",        # 4
            "▼終章②\x01",        # 5
            "▼終章③\x01",        # 6
            "▼終章④\x01",        # 7
            "▼終章⑤\x01",        # 8
            "▼終章⑥\x01",        # 9
            "▼終章⑦\x01",        # 10
            "▼終章⑧\x01",        # 11
            "Cancel\x01",      # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B9"),
        (1, "loc_3C1"),
        (2, "loc_3C9"),
        (3, "loc_3D1"),
        (4, "loc_3D9"),
        (5, "loc_3E1"),
        (6, "loc_3E9"),
        (7, "loc_3F1"),
        (8, "loc_3F9"),
        (9, "loc_401"),
        (10, "loc_409"),
        (11, "loc_411"),
        (SWITCH_DEFAULT, "loc_419"),
    )


    label("loc_3B9")

    Call(2, 17)
    Jump("loc_423")

    label("loc_3C1")

    Call(2, 18)
    Jump("loc_423")

    label("loc_3C9")

    Call(2, 19)
    Jump("loc_423")

    label("loc_3D1")

    Call(2, 20)
    Jump("loc_423")

    label("loc_3D9")

    Call(2, 22)
    Jump("loc_423")

    label("loc_3E1")

    Call(2, 23)
    Jump("loc_423")

    label("loc_3E9")

    Call(2, 24)
    Jump("loc_423")

    label("loc_3F1")

    Call(2, 25)
    Jump("loc_423")

    label("loc_3F9")

    Call(2, 26)
    Jump("loc_423")

    label("loc_401")

    Call(2, 27)
    Jump("loc_423")

    label("loc_409")

    Call(2, 28)
    Jump("loc_423")

    label("loc_411")

    Call(2, 29)
    Jump("loc_423")

    label("loc_419")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_423")

    Jump("loc_2D5")

    label("loc_428")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_1_2C8 end


    label("Function_2_436")

    Call(2, 31)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AB")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼羁绊事件\x01",                        # 0
            "▼6107兰花塔屋上の回想\x01",      # 1
            "▼克洛斯贝尔时代周刊用scene１\x01",      # 2
            "▼克洛斯贝尔时代周刊用scene２\x01",      # 3
            "▼克洛斯贝尔时代周刊用scene３\x01",      # 4
            "▼克洛斯贝尔时代周刊用scene４\x01",      # 5
            "Cancel\x01",                          # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_53F"),
        (1, "loc_547"),
        (2, "loc_558"),
        (3, "loc_569"),
        (4, "loc_57A"),
        (5, "loc_58B"),
        (SWITCH_DEFAULT, "loc_59C"),
    )


    label("loc_53F")

    Call(2, 30)
    Jump("loc_5A6")

    label("loc_547")

    SetScenarioFlags(0x22, 6)
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_5A6")

    label("loc_558")

    SetScenarioFlags(0x23, 1)
    NewScene("c1500", 0, 0, 0)
    OP_07()
    Jump("loc_5A6")

    label("loc_569")

    SetScenarioFlags(0x22, 2)
    NewScene("c1560", 0, 0, 0)
    OP_07()
    Jump("loc_5A6")

    label("loc_57A")

    SetScenarioFlags(0x22, 2)
    NewScene("c1120", 0, 0, 0)
    OP_07()
    Jump("loc_5A6")

    label("loc_58B")

    SetScenarioFlags(0x23, 4)
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_5A6")

    label("loc_59C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A6")

    Jump("loc_443")

    label("loc_5AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_2_436 end


    label("Function_3_5B9")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A43")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼0001Ｄ∴Ｇ教団阿尔泰尔\x01",      # 0
            "②▼0003Ｄ∴Ｇ教団阿尔泰尔\x01",      # 1
            "③▼0008认识到亚里欧斯等人的强大\x01",      # 2
            "④▼0010阿奈斯特与哈尔特曼\x01",      # 3
            "⑤▼0011阿奈斯特与哈尔特曼\x01",      # 4
            "⑥▼0012诺埃尔＆特務支援課\x01",      # 5
            "⑦▼0014关于琪雅&芙兰\x01",      # 6
            "⑧▼0015关于Ｄ∴Ｇ教団的故事\x01",      # 7
            "⑨▼0017阿奈斯特の元に辿り着\x01",      # 8
            "⑩▼0018魔人阿奈斯特戦闘後\x01",        # 9
            "?▼0019真魔人阿奈斯特戦闘後\x01",       # 10
            "?▼002与达德利等人分别\x01",         # 11
            "?▼0021大陸横断鉄道（唐古拉姆\x01",       # 12
            "?▼0023大陸横断鉄道（东克洛斯\x01",       # 13
            "?▼0025克洛斯贝尔駅に到达\x01",           # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_822"),
        (13, "loc_822"),
        (12, "loc_825"),
        (11, "loc_825"),
        (10, "loc_825"),
        (9, "loc_825"),
        (8, "loc_825"),
        (7, "loc_828"),
        (6, "loc_82B"),
        (5, "loc_82E"),
        (4, "loc_831"),
        (3, "loc_831"),
        (2, "loc_834"),
        (1, "loc_843"),
        (0, "loc_843"),
        (SWITCH_DEFAULT, "loc_851"),
    )


    label("loc_822")

    SetScenarioFlags(0x25, 2)

    label("loc_825")

    SetScenarioFlags(0x121, 1)

    label("loc_828")

    SetScenarioFlags(0x121, 0)

    label("loc_82B")

    SetScenarioFlags(0x120, 7)

    label("loc_82E")

    SetScenarioFlags(0x120, 6)

    label("loc_831")

    SetScenarioFlags(0x120, 5)

    label("loc_834")

    SetScenarioFlags(0x120, 0)
    SetScenarioFlags(0x120, 1)
    SetScenarioFlags(0x120, 2)
    SetScenarioFlags(0x120, 3)
    SetScenarioFlags(0x120, 4)

    label("loc_843")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_856")

    label("loc_851")

    Jump("loc_856")

    label("loc_856")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87F")
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x7, 0xFF)

    label("loc_87F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8E3"),
        (1, "loc_941"),
        (2, "loc_952"),
        (3, "loc_960"),
        (4, "loc_96E"),
        (5, "loc_97F"),
        (6, "loc_98D"),
        (7, "loc_99B"),
        (8, "loc_9A9"),
        (9, "loc_9B7"),
        (10, "loc_9C8"),
        (11, "loc_9D9"),
        (12, "loc_9EA"),
        (13, "loc_A04"),
        (14, "loc_A1E"),
        (SWITCH_DEFAULT, "loc_A2F"),
    )


    label("loc_8E3")

    OP_40(0x270F, 0x63)
    OP_36(0x0, 0xFFFF)
    OP_36(0x1, 0xFFFF)
    OP_36(0x2, 0xFFFF)
    OP_36(0x3, 0xFFFF)
    OP_36(0x4, 0xFFFF)
    OP_36(0x8, 0xFFFF)
    OP_36(0x5, 0xFFFF)
    OP_36(0x9, 0xFFFF)
    OP_36(0x7, 0xFFFF)
    OP_38(0x0, 0x7F, 0x0)
    OP_38(0x1, 0x7F, 0x0)
    OP_38(0x2, 0x7F, 0x0)
    OP_38(0x3, 0x7F, 0x0)
    OP_38(0x4, 0x7F, 0x0)
    OP_38(0x8, 0x7F, 0x0)
    OP_38(0x5, 0x7F, 0x0)
    OP_38(0x9, 0x7F, 0x0)
    OP_38(0x7, 0x7F, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("m4000", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_941")

    SetScenarioFlags(0x22, 0)
    NewScene("m4010", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_952")

    NewScene("m4020", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_960")

    NewScene("m4040", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_96E")

    SetScenarioFlags(0x22, 0)
    NewScene("m4040", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_97F")

    NewScene("m4050", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_98D")

    NewScene("m4060", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_99B")

    NewScene("m4060", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_9A9")

    NewScene("m4090", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_9B7")

    SetScenarioFlags(0x22, 0)
    NewScene("m4090", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_9C8")

    SetScenarioFlags(0x22, 1)
    NewScene("m4090", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_9D9")

    SetScenarioFlags(0x22, 0)
    NewScene("t5000", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_9EA")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t2500", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_A04")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r0040", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_A1E")

    SetScenarioFlags(0x22, 0)
    NewScene("c0800", 0, 0, 0)
    OP_07()
    Jump("loc_A3E")

    label("loc_A2F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3E")

    label("loc_A3E")

    Jump("loc_5D4")

    label("loc_A43")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_3_5B9 end


    label("Function_4_A51")

    Call(2, 32)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E7F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼1001支援要請的注意\x01",      # 0
            "②▼1006在屋内与琪雅汇合\x01",      # 1
            "③▼1007确认后门的工程进展\x01",      # 2
            "④▼1008琪雅等人离开\x01",      # 3
            "⑤▼1009接受塞尔盖の連絡\x01",      # 4
            "⑥▼1011西克洛斯贝尔街道に出た\x01",      # 5
            "⑦▼1012独眼の中年男と遭遇する\x01",      # 6
            "⑧▼1015警察学校の入口を確認す\x01",      # 7
            "⑨▼1016诺克斯森林道に足を踏\x01",      # 8
            "⑩▼1018警察学校の玄関前に到着\x01",      # 9
            "?▼1020警察学校の中に入る\x01",           # 10
            "?▼1021新型導力車を受け取る\x01",         # 11
            "?▼1025新型導力車に乗り込む（\x01",       # 12
            "?▼1030夕暮れの克洛斯贝尔に到\x01",       # 13
            "?▼1032琪雅を迎えに行く（中\x01",       # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_CBF"),
        (13, "loc_CBF"),
        (12, "loc_CBF"),
        (11, "loc_CC2"),
        (10, "loc_CC5"),
        (9, "loc_CC8"),
        (8, "loc_CCE"),
        (7, "loc_CD1"),
        (6, "loc_CD4"),
        (5, "loc_CD7"),
        (4, "loc_CDA"),
        (3, "loc_CDD"),
        (2, "loc_CE0"),
        (1, "loc_CE3"),
        (0, "loc_CE9"),
        (SWITCH_DEFAULT, "loc_CF7"),
    )


    label("loc_CBF")

    SetScenarioFlags(0x127, 6)

    label("loc_CC2")

    SetScenarioFlags(0x127, 5)

    label("loc_CC5")

    SetScenarioFlags(0x127, 3)

    label("loc_CC8")

    SetScenarioFlags(0x127, 1)
    SetScenarioFlags(0x127, 2)

    label("loc_CCE")

    SetScenarioFlags(0x127, 0)

    label("loc_CD1")

    SetScenarioFlags(0x126, 7)

    label("loc_CD4")

    SetScenarioFlags(0x126, 6)

    label("loc_CD7")

    SetScenarioFlags(0x126, 5)

    label("loc_CDA")

    SetScenarioFlags(0x126, 4)

    label("loc_CDD")

    SetScenarioFlags(0x126, 3)

    label("loc_CE0")

    SetScenarioFlags(0x126, 2)

    label("loc_CE3")

    SetScenarioFlags(0x126, 0)
    SetScenarioFlags(0x126, 1)

    label("loc_CE9")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CFC")

    label("loc_CF7")

    Jump("loc_CFC")

    label("loc_CFC")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D60"),
        (1, "loc_D71"),
        (2, "loc_D7F"),
        (3, "loc_D91"),
        (4, "loc_DA3"),
        (5, "loc_DBB"),
        (6, "loc_DC9"),
        (7, "loc_DD7"),
        (8, "loc_DE5"),
        (9, "loc_DF3"),
        (10, "loc_E01"),
        (11, "loc_E0F"),
        (12, "loc_E1D"),
        (13, "loc_E37"),
        (14, "loc_E51"),
        (SWITCH_DEFAULT, "loc_E6B"),
    )


    label("loc_D60")

    SetScenarioFlags(0x22, 0)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_D71")

    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_D7F")

    AddParty(0xA4, 0xFF, 0xFF)
    NewScene("c0200", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_D91")

    AddParty(0xA4, 0xFF, 0xFF)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_DA3")

    OP_29(0x65, 0x4, 0x10)
    OP_29(0x66, 0x4, 0x10)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_DBB")

    NewScene("r1000", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_DC9")

    NewScene("r1020", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_DD7")

    NewScene("r1030", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_DE5")

    NewScene("r4000", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_DF3")

    NewScene("t6000", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_E01")

    NewScene("t6010", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_E0F")

    NewScene("t6000", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_E1D")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r4010", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_E37")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r1000", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_E51")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_E7A")

    label("loc_E6B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E7A")

    label("loc_E7A")

    Jump("loc_A6F")

    label("loc_E7F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_4_A51 end


    label("Function_5_E8D")

    Call(2, 32)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1330")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼1037年長班级の授業\x01",            # 0
            "②▼1038给琪雅看导力车\x01",      # 1
            "③▼1043缇欧の連絡\x01",            # 2
            "④▼1044雨の克洛斯贝尔\x01",              # 3
            "⑤▼1048交換屋奈因瓦利を訪\x01",      # 4
            "⑥▼1052瓦鲁德登場\x01",                # 5
            "⑦▼1053瓦鲁德登場（戦闘後）\x01",      # 6
            "⑧▼1055芙兰の連絡\x01",            # 7
            "⑨▽1071罗赞贝尔克工房を訪\x01",      # 8
            "⑩▼1075ビクセン町長からの依頼\x01",      # 9
            "?▼1076旧鉱山前に终于来了\x01",         # 10
            "?▼1081旧鉱山前の２map目に\x01",       # 11
            "?▼1082巨大な幻獣が出現\x01",             # 12
            "?▼1083巨大な幻獣が出現（戦闘\x01",       # 13
            "?▼1084码因兹を後にする\x01",           # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_10D1"),
        (13, "loc_10D1"),
        (12, "loc_10D1"),
        (11, "loc_10D4"),
        (10, "loc_10DA"),
        (9, "loc_10DD"),
        (8, "loc_10E3"),
        (7, "loc_1113"),
        (6, "loc_1116"),
        (5, "loc_1116"),
        (4, "loc_111F"),
        (3, "loc_1125"),
        (2, "loc_1125"),
        (1, "loc_1125"),
        (0, "loc_1128"),
        (SWITCH_DEFAULT, "loc_1163"),
    )


    label("loc_10D1")

    SetScenarioFlags(0x12A, 3)

    label("loc_10D4")

    SetScenarioFlags(0x12A, 1)
    SetScenarioFlags(0x12A, 2)

    label("loc_10DA")

    SetScenarioFlags(0x12A, 0)

    label("loc_10DD")

    SetScenarioFlags(0x129, 5)
    SetScenarioFlags(0x12A, 5)

    label("loc_10E3")

    SetScenarioFlags(0x128, 7)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x32, 0)
    SetScenarioFlags(0x32, 4)
    SetScenarioFlags(0x34, 1)
    SetScenarioFlags(0x34, 2)
    SetScenarioFlags(0x34, 3)
    SetScenarioFlags(0x35, 0)
    SetScenarioFlags(0x35, 4)
    SetScenarioFlags(0x37, 1)
    SetScenarioFlags(0x37, 2)
    SetScenarioFlags(0x37, 3)
    SetScenarioFlags(0x129, 0)
    SetScenarioFlags(0x129, 1)

    label("loc_1113")

    SetScenarioFlags(0x128, 6)

    label("loc_1116")

    SetScenarioFlags(0x128, 5)
    SetScenarioFlags(0x128, 4)
    SetScenarioFlags(0x128, 3)

    label("loc_111F")

    SetScenarioFlags(0x128, 2)
    SetScenarioFlags(0x128, 1)

    label("loc_1125")

    SetScenarioFlags(0x128, 0)

    label("loc_1128")

    SetScenarioFlags(0x127, 7)
    SetScenarioFlags(0x127, 6)
    SetScenarioFlags(0x127, 5)
    SetScenarioFlags(0x127, 3)
    SetScenarioFlags(0x127, 1)
    SetScenarioFlags(0x127, 2)
    SetScenarioFlags(0x127, 0)
    SetScenarioFlags(0x126, 7)
    SetScenarioFlags(0x126, 6)
    SetScenarioFlags(0x126, 5)
    SetScenarioFlags(0x126, 4)
    SetScenarioFlags(0x126, 3)
    SetScenarioFlags(0x126, 2)
    SetScenarioFlags(0x126, 0)
    SetScenarioFlags(0x126, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1168")

    label("loc_1163")

    Jump("loc_1168")

    label("loc_1168")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11CC"),
        (1, "loc_11DA"),
        (2, "loc_11EC"),
        (3, "loc_1201"),
        (4, "loc_1212"),
        (5, "loc_1234"),
        (6, "loc_1256"),
        (7, "loc_127B"),
        (8, "loc_12AC"),
        (9, "loc_12BA"),
        (10, "loc_12C8"),
        (11, "loc_12D6"),
        (12, "loc_12E4"),
        (13, "loc_12F2"),
        (14, "loc_1307"),
        (SWITCH_DEFAULT, "loc_131C"),
    )


    label("loc_11CC")

    NewScene("t4010", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_11DA")

    AddParty(0x52, 0xFF, 0xFF)
    NewScene("r2000", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_11EC")

    AddParty(0x52, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("c011B", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_1201")

    SetScenarioFlags(0x22, 1)
    NewScene("c0120", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_1212")

    OP_BA(0x96, 0x232)
    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    OP_BA(0x75, 0x232)
    NewScene("c1440", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_1234")

    OP_BA(0x96, 0x232)
    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    OP_BA(0x75, 0x232)
    NewScene("c1400", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_1256")

    SetScenarioFlags(0x22, 1)
    OP_BA(0x96, 0x232)
    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    OP_BA(0x75, 0x232)
    NewScene("c1400", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_127B")

    OP_BA(0x96, 0x232)
    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    OP_BA(0x75, 0x232)
    OP_29(0x6A, 0x4, 0x10)
    OP_29(0x6B, 0x4, 0x10)
    OP_29(0x6C, 0x4, 0x10)
    NewScene("c1000", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_12AC")

    NewScene("t3000", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_12BA")

    NewScene("t0510", 100, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_12C8")

    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_12D6")

    NewScene("m4120", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_12E4")

    NewScene("m4190", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_12F2")

    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("m4190", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_1307")

    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t0500", 0, 0, 0)
    OP_07()
    Jump("loc_132B")

    label("loc_131C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_132B")

    label("loc_132B")

    Jump("loc_EAB")

    label("loc_1330")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_5_E8D end


    label("Function_6_133E")

    Call(2, 32)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A4")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼1091幻焔計画開始\x01",                # 0
            "②▼1093兰迪与叔父再会\x01",      # 1
            "Cancel\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_13D0"),
        (0, "loc_13D3"),
        (SWITCH_DEFAULT, "loc_1441"),
    )


    label("loc_13D0")

    SetScenarioFlags(0x12A, 4)

    label("loc_13D3")

    SetScenarioFlags(0x12A, 3)
    SetScenarioFlags(0x12A, 1)
    SetScenarioFlags(0x12A, 2)
    SetScenarioFlags(0x12A, 0)
    SetScenarioFlags(0x129, 5)
    SetScenarioFlags(0x12A, 5)
    SetScenarioFlags(0x31, 1)
    SetScenarioFlags(0x128, 7)
    SetScenarioFlags(0x129, 0)
    SetScenarioFlags(0x129, 1)
    SetScenarioFlags(0x128, 6)
    SetScenarioFlags(0x128, 5)
    SetScenarioFlags(0x128, 4)
    SetScenarioFlags(0x128, 3)
    SetScenarioFlags(0x128, 2)
    SetScenarioFlags(0x128, 1)
    SetScenarioFlags(0x128, 0)
    SetScenarioFlags(0x127, 7)
    SetScenarioFlags(0x127, 6)
    SetScenarioFlags(0x127, 5)
    SetScenarioFlags(0x127, 3)
    SetScenarioFlags(0x127, 1)
    SetScenarioFlags(0x127, 2)
    SetScenarioFlags(0x127, 0)
    SetScenarioFlags(0x126, 7)
    SetScenarioFlags(0x126, 6)
    SetScenarioFlags(0x126, 5)
    SetScenarioFlags(0x126, 4)
    SetScenarioFlags(0x126, 3)
    SetScenarioFlags(0x126, 2)
    SetScenarioFlags(0x126, 0)
    SetScenarioFlags(0x126, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1446")

    label("loc_1441")

    Jump("loc_1446")

    label("loc_1446")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_145C"),
        (1, "loc_1476"),
        (SWITCH_DEFAULT, "loc_1490"),
    )


    label("loc_145C")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2030", 0, 0, 0)
    OP_07()
    Jump("loc_149F")

    label("loc_1476")

    RemoveParty(0x3, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0500", 0, 0, 0)
    OP_07()
    Jump("loc_149F")

    label("loc_1490")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_149F")

    label("loc_149F")

    Jump("loc_1360")

    label("loc_14A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_6_133E end


    label("Function_7_14B2")

    Call(2, 32)
    Call(2, 33)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18DD")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼2001兰花塔亮相\x01",      # 0
            "②▼2002警備対策会議に同席\x01",          # 1
            "③▼2003市内に配置される警官た\x01",      # 2
            "④▼2005与兰迪的对话（\x01",      # 3
            "⑤▼2007米歇尔の連絡（タ\x01",      # 4
            "⑥▼2008米歇尔の連絡（病\x01",      # 5
            "⑦▼2009游击士协会で米歇尔と話す\x01",      # 6
            "⑧▼2011支援課に帰る（東通り）\x01",      # 7
            "⑨▼2014ノイエ＝ブランへ向かう\x01",      # 8
            "⑩▼2017ノイエ＝ブランに到着\x01",        # 9
            "?▼2020首脳来訪前夜（執務室）\x01",       # 10
            "?▼2021首脳来訪前夜（アルセイ\x01",       # 11
            "?▼2022首脳来訪前夜（约那终端\x01",       # 12
            "?▼2023通商会議に沸く市民（中\x01",       # 13
            "?▼2025帝国首脳の来訪（駅前）\x01",       # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_1727"),
        (13, "loc_1727"),
        (12, "loc_1727"),
        (11, "loc_1727"),
        (10, "loc_1727"),
        (9, "loc_1727"),
        (8, "loc_1727"),
        (7, "loc_1727"),
        (6, "loc_1727"),
        (5, "loc_172A"),
        (4, "loc_172A"),
        (3, "loc_172D"),
        (2, "loc_1730"),
        (1, "loc_1730"),
        (0, "loc_1730"),
        (SWITCH_DEFAULT, "loc_173E"),
    )


    label("loc_1727")

    SetScenarioFlags(0x140, 2)

    label("loc_172A")

    SetScenarioFlags(0x140, 1)

    label("loc_172D")

    SetScenarioFlags(0x140, 0)

    label("loc_1730")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1743")

    label("loc_173E")

    Jump("loc_1743")

    label("loc_1743")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17A7"),
        (1, "loc_17B8"),
        (2, "loc_17C9"),
        (3, "loc_17DA"),
        (4, "loc_17E8"),
        (5, "loc_1800"),
        (6, "loc_1818"),
        (7, "loc_1826"),
        (8, "loc_1837"),
        (9, "loc_1851"),
        (10, "loc_1862"),
        (11, "loc_1873"),
        (12, "loc_188D"),
        (13, "loc_189E"),
        (14, "loc_18AF"),
        (SWITCH_DEFAULT, "loc_18C9"),
    )


    label("loc_17A7")

    SetScenarioFlags(0x22, 0)
    NewScene("c1500", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_17B8")

    SetScenarioFlags(0x22, 0)
    NewScene("c1150", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_17C9")

    SetScenarioFlags(0x22, 3)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_17DA")

    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_17E8")

    OP_29(0x6F, 0x4, 0x10)
    OP_29(0x70, 0x4, 0x10)
    NewScene("t2500", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1800")

    OP_29(0x6F, 0x4, 0x10)
    OP_29(0x70, 0x4, 0x10)
    NewScene("t1500", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1818")

    NewScene("c1010", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1826")

    SetScenarioFlags(0x22, 1)
    NewScene("c100B", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1837")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1851")

    SetScenarioFlags(0x22, 0)
    NewScene("c0490", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1862")

    SetScenarioFlags(0x22, 0)
    NewScene("e4010", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_1873")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e430B", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_188D")

    SetScenarioFlags(0x22, 0)
    NewScene("m0101", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_189E")

    SetScenarioFlags(0x22, 4)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_18AF")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0000", 0, 0, 0)
    OP_07()
    Jump("loc_18D8")

    label("loc_18C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18D8")

    label("loc_18D8")

    Jump("loc_14D7")

    label("loc_18DD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_7_14B2 end


    label("Function_8_18EB")

    Call(2, 32)
    Call(2, 33)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D65")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼2027共和国首脳の来訪（東通\x01",      # 0
            "②▼2030王国首脳の来訪（南街道\x01",      # 1
            "③▼2034轿车で移動（中央）\x01",      # 2
            "④▼2036兰花塔のお披露\x01",      # 3
            "⑤▼2041２日目午後?中央広場の\x01",       # 4
            "⑥▼2044关键任务終了\x01",            # 5
            "⑦▼2045支援課での休憩\x01",              # 6
            "⑧▼2048空港前選択肢\x01",                # 7
            "⑨▼2053夜の中央広場\x01",                # 8
            "⑩▼2055地下区域Ｂ区画の扉\x01",      # 9
            "?▼2057中boss戦\x01",                     # 10
            "?▼2058约那の部屋の前に到着す\x01",       # 11
            "?▼2062３日目開始\x01",                   # 12
            "?▼2064兰花塔前にやっ\x01",       # 13
            "?▼2067迪塔市長のタワー\x01",       # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_1B29"),
        (13, "loc_1B2F"),
        (12, "loc_1B32"),
        (11, "loc_1B35"),
        (10, "loc_1B38"),
        (9, "loc_1B3E"),
        (8, "loc_1B41"),
        (7, "loc_1B41"),
        (6, "loc_1B47"),
        (5, "loc_1B4A"),
        (4, "loc_1B50"),
        (3, "loc_1B50"),
        (2, "loc_1B50"),
        (1, "loc_1B50"),
        (0, "loc_1B50"),
        (SWITCH_DEFAULT, "loc_1B67"),
    )


    label("loc_1B29")

    SetScenarioFlags(0x141, 6)
    SetScenarioFlags(0x141, 7)

    label("loc_1B2F")

    SetScenarioFlags(0x141, 5)

    label("loc_1B32")

    SetScenarioFlags(0x141, 4)

    label("loc_1B35")

    SetScenarioFlags(0x141, 3)

    label("loc_1B38")

    SetScenarioFlags(0x141, 1)
    SetScenarioFlags(0x141, 2)

    label("loc_1B3E")

    SetScenarioFlags(0x141, 0)

    label("loc_1B41")

    SetScenarioFlags(0x140, 6)
    SetScenarioFlags(0x140, 7)

    label("loc_1B47")

    SetScenarioFlags(0x140, 5)

    label("loc_1B4A")

    SetScenarioFlags(0x140, 3)
    SetScenarioFlags(0x140, 4)

    label("loc_1B50")

    SetScenarioFlags(0x140, 2)
    SetScenarioFlags(0x140, 1)
    SetScenarioFlags(0x140, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B6C")

    label("loc_1B67")

    Jump("loc_1B6C")

    label("loc_1B6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B93")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_1B93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BBA")
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_1BBA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C1E"),
        (1, "loc_1C38"),
        (2, "loc_1C52"),
        (3, "loc_1C6C"),
        (4, "loc_1C86"),
        (5, "loc_1C97"),
        (6, "loc_1CAA"),
        (7, "loc_1CB8"),
        (8, "loc_1CC6"),
        (9, "loc_1CD7"),
        (10, "loc_1CE5"),
        (11, "loc_1CF3"),
        (12, "loc_1D07"),
        (13, "loc_1D22"),
        (14, "loc_1D3A"),
        (SWITCH_DEFAULT, "loc_1D51"),
    )


    label("loc_1C1E")

    SetScenarioFlags(0x22, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1000", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1C38")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r1500", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1C52")

    SetScenarioFlags(0x22, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1C6C")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1500", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1C86")

    SetScenarioFlags(0x22, 6)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1C97")

    OP_29(0x74, 0x4, 0x10)
    NewScene("c1000", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1CAA")

    NewScene("c0110", 100, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1CB8")

    NewScene("r1500", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1CC6")

    SetScenarioFlags(0x22, 2)
    NewScene("c010B", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1CD7")

    NewScene("c030B", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1CE5")

    NewScene("m0102", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1CF3")

    VolumeBGM(0x28, 0xC8)
    NewScene("m0101", 133, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1D07")

    SetScenarioFlags(0x22, 7)
    OP_BA(0x96, 0x7D)
    OP_BA(0x65, 0x7D)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1D22")

    OP_BA(0x96, 0x7D)
    OP_BA(0x65, 0x7D)
    NewScene("c1500", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1D3A")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1510", 0, 0, 0)
    OP_07()
    Jump("loc_1D60")

    label("loc_1D51")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D60")

    label("loc_1D60")

    Jump("loc_1910")

    label("loc_1D65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_8_18EB end


    label("Function_9_1D73")

    Call(2, 32)
    Call(2, 33)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼2075通商会議開催\x01",                # 0
            "②▼2083報道陣による各国首脳へ\x01",      # 1
            "③▼2086洛克史密斯大統領との\x01",      # 2
            "④▼2087奥兹本の部屋を確認\x01",      # 3
            "⑤▼2089通商会議後半開始\x01",            # 4
            "⑥▼2093飛行艇の襲撃\x01",                # 5
            "⑦▼2098非常階段の封鎖を確認\x01",        # 6
            "⑧▼2100塔の制御を解放\x01",          # 7
            "⑨▼2101降下的电梯\x01",      # 8
            "⑩▼2104与亚里欧斯等人分头\x01",      # 9
            "?▼2105地下駐車場に入る\x01",             # 10
            "?▼2107貨物路線場の手前で爆発\x01",       # 11
            "?▼2111恐怖分子に追いつ\x01",       # 12
            "?▼2112新型装甲車両との戦闘\x01",         # 13
            "?▼2114赤い星座による虐殺\x01",           # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_1FC6"),
        (13, "loc_1FC9"),
        (12, "loc_1FC9"),
        (11, "loc_1FD5"),
        (10, "loc_1FDB"),
        (9, "loc_1FDE"),
        (8, "loc_1FE4"),
        (7, "loc_1FE4"),
        (6, "loc_1FE4"),
        (5, "loc_1FE7"),
        (4, "loc_1FE7"),
        (3, "loc_1FED"),
        (2, "loc_1FF0"),
        (1, "loc_1FF6"),
        (0, "loc_1FFC"),
        (SWITCH_DEFAULT, "loc_203A"),
    )


    label("loc_1FC6")

    SetScenarioFlags(0x143, 7)

    label("loc_1FC9")

    SetScenarioFlags(0x143, 3)
    SetScenarioFlags(0x143, 4)
    SetScenarioFlags(0x143, 5)
    SetScenarioFlags(0x143, 6)

    label("loc_1FD5")

    SetScenarioFlags(0x143, 1)
    SetScenarioFlags(0x143, 2)

    label("loc_1FDB")

    SetScenarioFlags(0x143, 0)

    label("loc_1FDE")

    SetScenarioFlags(0x142, 6)
    SetScenarioFlags(0x142, 7)

    label("loc_1FE4")

    SetScenarioFlags(0x142, 5)

    label("loc_1FE7")

    SetScenarioFlags(0x142, 4)
    SetScenarioFlags(0x1C4, 4)

    label("loc_1FED")

    SetScenarioFlags(0x142, 3)

    label("loc_1FF0")

    SetScenarioFlags(0x142, 1)
    SetScenarioFlags(0x142, 2)

    label("loc_1FF6")

    SetScenarioFlags(0x142, 0)
    SetScenarioFlags(0x146, 3)

    label("loc_1FFC")

    SetScenarioFlags(0x141, 6)
    SetScenarioFlags(0x141, 7)
    SetScenarioFlags(0x141, 5)
    SetScenarioFlags(0x141, 4)
    SetScenarioFlags(0x141, 3)
    SetScenarioFlags(0x141, 1)
    SetScenarioFlags(0x141, 2)
    SetScenarioFlags(0x141, 0)
    SetScenarioFlags(0x140, 6)
    SetScenarioFlags(0x140, 7)
    SetScenarioFlags(0x140, 5)
    SetScenarioFlags(0x140, 3)
    SetScenarioFlags(0x140, 4)
    SetScenarioFlags(0x140, 2)
    SetScenarioFlags(0x140, 1)
    SetScenarioFlags(0x140, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_203F")

    label("loc_203A")

    Jump("loc_203F")

    label("loc_203F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20A3"),
        (1, "loc_20B4"),
        (2, "loc_20CE"),
        (3, "loc_20E5"),
        (4, "loc_20FC"),
        (5, "loc_210D"),
        (6, "loc_2127"),
        (7, "loc_213F"),
        (8, "loc_215A"),
        (9, "loc_2175"),
        (10, "loc_218D"),
        (11, "loc_21A5"),
        (12, "loc_21BD"),
        (13, "loc_21D5"),
        (14, "loc_21F0"),
        (SWITCH_DEFAULT, "loc_2208"),
    )


    label("loc_20A3")

    SetScenarioFlags(0x22, 1)
    NewScene("c1540", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_20B4")

    SetScenarioFlags(0x22, 2)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1540", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_20CE")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1550", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_20E5")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1550", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_20FC")

    SetScenarioFlags(0x22, 3)
    NewScene("c1540", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_210D")

    SetScenarioFlags(0x22, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1540", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_2127")

    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x231)
    NewScene("c1550", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_213F")

    SetScenarioFlags(0x23, 0)
    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x231)
    NewScene("c1540", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_215A")

    SetScenarioFlags(0x22, 1)
    OP_BA(0x97, 0x160)
    OP_BA(0x12C, 0x231)
    NewScene("c1520", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_2175")

    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x231)
    NewScene("m0401", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_218D")

    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x231)
    NewScene("m0303", 104, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_21A5")

    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x220)
    NewScene("m0301", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_21BD")

    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x220)
    NewScene("m0309", 101, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_21D5")

    SetScenarioFlags(0x22, 0)
    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x220)
    NewScene("m0309", 0, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_21F0")

    OP_BA(0x97, 0x220)
    OP_BA(0x12C, 0x231)
    NewScene("m0309", 104, 0, 0)
    OP_07()
    Jump("loc_2217")

    label("loc_2208")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2217")

    label("loc_2217")

    Jump("loc_1D9C")

    label("loc_221C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_9_1D73 end


    label("Function_10_222A")

    Call(2, 32)
    Call(2, 33)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_235E")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼2115黒月の动向\x01",                # 0
            "②▼2116国家独立の提言\x01",            # 1
            "③▼2117Ａｆｔｅｒｗａｒｄｓ\x01",      # 2
            "Cancel\x01",                        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (2, "loc_22DC"),
        (1, "loc_22DC"),
        (0, "loc_22DC"),
        (SWITCH_DEFAULT, "loc_22ED"),
    )


    label("loc_22DC")

    Call(2, 34)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22F2")

    label("loc_22ED")

    Jump("loc_22F2")

    label("loc_22F2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_230E"),
        (1, "loc_2328"),
        (2, "loc_2339"),
        (SWITCH_DEFAULT, "loc_234A"),
    )


    label("loc_230E")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0200", 0, 0, 0)
    OP_07()
    Jump("loc_2359")

    label("loc_2328")

    SetScenarioFlags(0x23, 1)
    NewScene("c1540", 0, 0, 0)
    OP_07()
    Jump("loc_2359")

    label("loc_2339")

    SetScenarioFlags(0x22, 0)
    NewScene("m0401", 0, 0, 0)
    OP_07()
    Jump("loc_2359")

    label("loc_234A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2359")

    label("loc_2359")

    Jump("loc_2253")

    label("loc_235E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_10_222A end


    label("Function_11_236C")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2398")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼I001エルム湖上?水上bus\x01",         # 0
            "②▼I005琪雅が甲板に現れる\x01",        # 1
            "③▼I007米修拉姆に到着\x01",            # 2
            "④▼I008宾馆の部屋を导游\x01",          # 3
            "⑤▼I011湖水浴場の受付前に来る\x01",      # 4
            "⑥▼I013女性陣登場\x01",                  # 5
            "⑦▼I014打西瓜\x01",                  # 6
            "⑧▼I016琪雅を寻找\x01",      # 7
            "⑨▼I017琪雅を発見\x01",                # 8
            "⑩▼I018主题公园前で合流\x01",        # 9
            "?▼I020主题公园を後にする\x01",       # 10
            "?▼I021夜の宾馆\x01",                   # 11
            "?▼I023琪雅に関しての確認\x01",         # 12
            "?▼I024迎賓館に到着\x01",                 # 13
            "?▼I026満月が出ている夜空\x01",           # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_259F"),
        (13, "loc_259F"),
        (12, "loc_25A2"),
        (11, "loc_25A5"),
        (10, "loc_25A5"),
        (9, "loc_25A8"),
        (8, "loc_25AB"),
        (7, "loc_25AB"),
        (6, "loc_25AE"),
        (5, "loc_25B1"),
        (4, "loc_25B7"),
        (3, "loc_25BA"),
        (2, "loc_25BA"),
        (1, "loc_25BD"),
        (0, "loc_25C9"),
        (SWITCH_DEFAULT, "loc_25D7"),
    )


    label("loc_259F")

    SetScenarioFlags(0x145, 6)

    label("loc_25A2")

    SetScenarioFlags(0x145, 5)

    label("loc_25A5")

    SetScenarioFlags(0x145, 4)

    label("loc_25A8")

    SetScenarioFlags(0x145, 2)

    label("loc_25AB")

    SetScenarioFlags(0x145, 1)

    label("loc_25AE")

    SetScenarioFlags(0x145, 0)

    label("loc_25B1")

    SetScenarioFlags(0x144, 6)
    SetScenarioFlags(0x144, 7)

    label("loc_25B7")

    SetScenarioFlags(0x144, 5)

    label("loc_25BA")

    SetScenarioFlags(0x144, 4)

    label("loc_25BD")

    SetScenarioFlags(0x144, 0)
    SetScenarioFlags(0x144, 1)
    SetScenarioFlags(0x144, 2)
    SetScenarioFlags(0x144, 3)

    label("loc_25C9")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25DC")

    label("loc_25D7")

    Jump("loc_25DC")

    label("loc_25DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_260E")
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)

    label("loc_260E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2672"),
        (1, "loc_2683"),
        (2, "loc_26A0"),
        (3, "loc_26B1"),
        (4, "loc_26C2"),
        (5, "loc_26D9"),
        (6, "loc_26F0"),
        (7, "loc_2710"),
        (8, "loc_272A"),
        (9, "loc_273D"),
        (10, "loc_274F"),
        (11, "loc_2760"),
        (12, "loc_2771"),
        (13, "loc_2786"),
        (14, "loc_279B"),
        (SWITCH_DEFAULT, "loc_27AC"),
    )


    label("loc_2672")

    SetScenarioFlags(0x22, 0)
    NewScene("e3000", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_2683")

    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    NewScene("e3000", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_26A0")

    SetScenarioFlags(0x22, 0)
    NewScene("t1000", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_26B1")

    SetScenarioFlags(0x22, 0)
    NewScene("t1020", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_26C2")

    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x8, 0xFF)
    NewScene("t1320", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_26D9")

    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x8, 0xFF)
    NewScene("t1310", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_26F0")

    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t1310", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_2710")

    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x8, 0xFF)
    SetScenarioFlags(0x22, 1)
    NewScene("t1080", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_272A")

    OP_BA(0x235, 0x6F)
    NewScene("t1100", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_273D")

    AddParty(0x52, 0xFF, 0xFF)
    NewScene("t1030", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_274F")

    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_2760")

    SetScenarioFlags(0x22, 0)
    NewScene("t100B", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_2771")

    SetScenarioFlags(0x147, 2)
    AddParty(0x1, 0xEF, 0xFF)
    NewScene("t108B", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_2786")

    SetScenarioFlags(0x147, 2)
    AddParty(0x1, 0xEF, 0xFF)
    NewScene("t110B", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_279B")

    SetScenarioFlags(0x22, 1)
    NewScene("e430B", 0, 0, 0)
    OP_07()
    Jump("loc_27BB")

    label("loc_27AC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27BB")

    label("loc_27BB")

    Jump("loc_2398")

    label("loc_27C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_11_236C end


    label("Function_12_27CE")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A03")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼I029罗伊德の悪夢\x01",                # 0
            "②▼I033装飾が変わった夜の公园\x01",      # 1
            "③▼I034装飾が変わった公园\x01",      # 2
            "④▼I035肯帕雷拉登場\x01",            # 3
            "⑤▼I036鏡の城の手前で琪雅を\x01",      # 4
            "⑥▼I037米修拉姆を後にする（\x01",      # 5
            "Cancel\x01",                          # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (5, "loc_28F8"),
        (4, "loc_28F8"),
        (3, "loc_28FB"),
        (2, "loc_28FB"),
        (1, "loc_28FE"),
        (0, "loc_2901"),
        (SWITCH_DEFAULT, "loc_293C"),
    )


    label("loc_28F8")

    SetScenarioFlags(0x146, 2)

    label("loc_28FB")

    SetScenarioFlags(0x146, 1)

    label("loc_28FE")

    SetScenarioFlags(0x146, 0)

    label("loc_2901")

    SetScenarioFlags(0x145, 7)
    SetScenarioFlags(0x145, 6)
    SetScenarioFlags(0x145, 5)
    SetScenarioFlags(0x145, 4)
    SetScenarioFlags(0x145, 2)
    SetScenarioFlags(0x145, 1)
    SetScenarioFlags(0x145, 0)
    SetScenarioFlags(0x144, 6)
    SetScenarioFlags(0x144, 7)
    SetScenarioFlags(0x144, 5)
    SetScenarioFlags(0x144, 4)
    SetScenarioFlags(0x144, 0)
    SetScenarioFlags(0x144, 1)
    SetScenarioFlags(0x144, 2)
    SetScenarioFlags(0x144, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2941")

    label("loc_293C")

    Jump("loc_2941")

    label("loc_2941")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_296F"),
        (1, "loc_298F"),
        (2, "loc_29A2"),
        (3, "loc_29B5"),
        (4, "loc_29CB"),
        (5, "loc_29DE"),
        (SWITCH_DEFAULT, "loc_29EF"),
    )


    label("loc_296F")

    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("m3099", 0, 0, 0)
    OP_07()
    Jump("loc_29FE")

    label("loc_298F")

    OP_BA(0x201, 0x234)
    NewScene("t103B", 0, 0, 0)
    OP_07()
    Jump("loc_29FE")

    label("loc_29A2")

    OP_BA(0x201, 0x234)
    NewScene("t130B", 0, 0, 0)
    OP_07()
    Jump("loc_29FE")

    label("loc_29B5")

    SetScenarioFlags(0x22, 0)
    OP_BA(0x201, 0x234)
    NewScene("t130B", 0, 0, 0)
    OP_07()
    Jump("loc_29FE")

    label("loc_29CB")

    OP_BA(0x201, 0x234)
    NewScene("t140B", 100, 0, 0)
    OP_07()
    Jump("loc_29FE")

    label("loc_29DE")

    SetScenarioFlags(0x22, 1)
    NewScene("e3000", 0, 0, 0)
    OP_07()
    Jump("loc_29FE")

    label("loc_29EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29FE")

    label("loc_29FE")

    Jump("loc_27FA")

    label("loc_2A03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_12_27CE end


    label("Function_13_2A11")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E09")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼3001星辰の間\x01",                    # 0
            "②▼3002兰花塔外観\x01",          # 1
            "③▼3005緊急要請を確認する\x01",          # 2
            "④▼3007中洲の小洞窟入口を発見\x01",      # 3
            "⑤▼3008乌尔丝拉間道?幻獣を発\x01",       # 4
            "⑥▼3009乌尔丝拉間道?幻獣を退\x01",       # 5
            "⑦▼3012東克洛斯贝尔街道?幻獣\x01",       # 6
            "⑧▼3013東克洛斯贝尔街道?幻獣\x01",       # 7
            "⑨▼3016伊安弁護士と遭遇\x01",          # 8
            "⑩▼3017被大司教叫住\x01",      # 9
            "?▼3019莉丝说出灵智之草\x01",       # 10
            "?▼3021闇の中での会話\x01",               # 11
            "?▼3022早晨の中央広場\x01",                 # 12
            "?▼3025人形工房前での交谈\x01",       # 13
            "?▼3028约鲁古老人からの情報\x01",         # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_2C64"),
        (13, "loc_2C6A"),
        (12, "loc_2C70"),
        (11, "loc_2C70"),
        (10, "loc_2C70"),
        (9, "loc_2C76"),
        (8, "loc_2C79"),
        (7, "loc_2C88"),
        (6, "loc_2C8B"),
        (5, "loc_2C8B"),
        (4, "loc_2C8E"),
        (3, "loc_2C91"),
        (2, "loc_2C97"),
        (1, "loc_2C97"),
        (0, "loc_2C97"),
        (SWITCH_DEFAULT, "loc_2CA5"),
    )


    label("loc_2C64")

    SetScenarioFlags(0x162, 2)
    SetScenarioFlags(0x162, 3)

    label("loc_2C6A")

    SetScenarioFlags(0x162, 0)
    SetScenarioFlags(0x162, 1)

    label("loc_2C70")

    SetScenarioFlags(0x161, 6)
    SetScenarioFlags(0x161, 7)

    label("loc_2C76")

    SetScenarioFlags(0x161, 5)

    label("loc_2C79")

    SetScenarioFlags(0x168, 1)
    SetScenarioFlags(0x160, 4)
    SetScenarioFlags(0x161, 1)
    SetScenarioFlags(0x161, 2)
    SetScenarioFlags(0x161, 3)

    label("loc_2C88")

    SetScenarioFlags(0x161, 0)

    label("loc_2C8B")

    SetScenarioFlags(0x160, 3)

    label("loc_2C8E")

    SetScenarioFlags(0x160, 2)

    label("loc_2C91")

    SetScenarioFlags(0x160, 0)
    SetScenarioFlags(0x160, 1)

    label("loc_2C97")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CAA")

    label("loc_2CA5")

    Jump("loc_2CAA")

    label("loc_2CAA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D0E"),
        (1, "loc_2D1F"),
        (2, "loc_2D30"),
        (3, "loc_2D41"),
        (4, "loc_2D4F"),
        (5, "loc_2D5D"),
        (6, "loc_2D6E"),
        (7, "loc_2D7C"),
        (8, "loc_2D8D"),
        (9, "loc_2D9B"),
        (10, "loc_2DA9"),
        (11, "loc_2DB7"),
        (12, "loc_2DC8"),
        (13, "loc_2DD9"),
        (14, "loc_2DE7"),
        (SWITCH_DEFAULT, "loc_2DF5"),
    )


    label("loc_2D0E")

    SetScenarioFlags(0x22, 0)
    NewScene("e4600", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D1F")

    SetScenarioFlags(0x22, 2)
    NewScene("c1500", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D30")

    SetScenarioFlags(0x22, 7)
    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D41")

    NewScene("r1530", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D4F")

    NewScene("r1610", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D5D")

    SetScenarioFlags(0x22, 0)
    NewScene("r1610", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D6E")

    NewScene("r0200", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D7C")

    SetScenarioFlags(0x22, 0)
    NewScene("r0200", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D8D")

    NewScene("t4000", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2D9B")

    NewScene("t4010", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2DA9")

    NewScene("t4000", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2DB7")

    SetScenarioFlags(0x22, 0)
    NewScene("m0001", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2DC8")

    SetScenarioFlags(0x23, 0)
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2DD9")

    NewScene("t3000", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2DE7")

    NewScene("t3010", 0, 0, 0)
    OP_07()
    Jump("loc_2E04")

    label("loc_2DF5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E04")

    label("loc_2E04")

    Jump("loc_2A40")

    label("loc_2E09")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_13_2A11 end


    label("Function_14_2E17")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼3030三叉路でenigmaの通信\x01",      # 0
            "②▼3039脱線事故の現場に到着\x01",        # 1
            "③▼3040現場検証を終える\x01",            # 2
            "④▼3042高台で鬼哭を聞く\x01",            # 3
            "⑤▼3043破壊音を聞く\x01",                # 4
            "⑥▼3045樹海に続く爪痕を発見す\x01",      # 5
            "⑦▼3048魔人瓦鲁德襲来\x01",            # 6
            "⑧▼3049魔人瓦鲁德襲来（戦闘\x01",      # 7
            "⑨▼3050雨の旧市街\x01",                  # 8
            "⑩▼3052米歇尔との会話\x01",            # 9
            "?▼3053ＩＢＣで主任を呼び出す\x01",       # 10
            "?▼3054兰花塔を訪れる\x01",       # 11
            "?▼3058兰花塔の屋上に\x01",       # 12
            "?▼3061波止場で船に乗り込\x01",       # 13
            "?▼3065エルム湖上での交谈\x01",       # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_306C"),
        (13, "loc_306F"),
        (12, "loc_3075"),
        (11, "loc_3081"),
        (10, "loc_3084"),
        (9, "loc_3087"),
        (8, "loc_308D"),
        (7, "loc_308D"),
        (6, "loc_308D"),
        (5, "loc_3093"),
        (4, "loc_3099"),
        (3, "loc_309C"),
        (2, "loc_309F"),
        (1, "loc_30A2"),
        (0, "loc_30AE"),
        (SWITCH_DEFAULT, "loc_30F2"),
    )


    label("loc_306C")

    SetScenarioFlags(0x165, 1)

    label("loc_306F")

    SetScenarioFlags(0x164, 7)
    SetScenarioFlags(0x165, 0)

    label("loc_3075")

    SetScenarioFlags(0x164, 3)
    SetScenarioFlags(0x164, 4)
    SetScenarioFlags(0x164, 5)
    SetScenarioFlags(0x164, 6)

    label("loc_3081")

    SetScenarioFlags(0x164, 2)

    label("loc_3084")

    SetScenarioFlags(0x164, 1)

    label("loc_3087")

    SetScenarioFlags(0x168, 2)
    SetScenarioFlags(0x164, 0)

    label("loc_308D")

    SetScenarioFlags(0x163, 6)
    SetScenarioFlags(0x163, 7)

    label("loc_3093")

    SetScenarioFlags(0x163, 4)
    SetScenarioFlags(0x163, 5)

    label("loc_3099")

    SetScenarioFlags(0x163, 3)

    label("loc_309C")

    SetScenarioFlags(0x163, 2)

    label("loc_309F")

    SetScenarioFlags(0x163, 1)

    label("loc_30A2")

    SetScenarioFlags(0x162, 5)
    SetScenarioFlags(0x162, 6)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x163, 0)

    label("loc_30AE")

    SetScenarioFlags(0x162, 4)
    SetScenarioFlags(0x162, 2)
    SetScenarioFlags(0x162, 3)
    SetScenarioFlags(0x162, 0)
    SetScenarioFlags(0x162, 1)
    SetScenarioFlags(0x161, 6)
    SetScenarioFlags(0x161, 7)
    SetScenarioFlags(0x161, 5)
    SetScenarioFlags(0x160, 4)
    SetScenarioFlags(0x161, 1)
    SetScenarioFlags(0x161, 2)
    SetScenarioFlags(0x161, 3)
    SetScenarioFlags(0x161, 0)
    SetScenarioFlags(0x168, 1)
    SetScenarioFlags(0x160, 3)
    SetScenarioFlags(0x160, 2)
    SetScenarioFlags(0x160, 0)
    SetScenarioFlags(0x160, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30F7")

    label("loc_30F2")

    Jump("loc_30F7")

    label("loc_30F7")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_315B"),
        (1, "loc_3169"),
        (2, "loc_317C"),
        (3, "loc_3192"),
        (4, "loc_31AF"),
        (5, "loc_31CC"),
        (6, "loc_31E9"),
        (7, "loc_31F7"),
        (8, "loc_3208"),
        (9, "loc_3219"),
        (10, "loc_3231"),
        (11, "loc_3249"),
        (12, "loc_3261"),
        (13, "loc_3279"),
        (14, "loc_3291"),
        (SWITCH_DEFAULT, "loc_32A2"),
    )


    label("loc_315B")

    NewScene("r2030", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3169")

    OP_BA(0x96, 0x97)
    NewScene("r1050", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_317C")

    SetScenarioFlags(0x22, 0)
    OP_BA(0xCD, 0x97)
    NewScene("r1050", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3192")

    OP_BA(0x96, 0x97)
    OP_BA(0xCD, 0xCB)
    OP_BA(0xFA, 0xCB)
    NewScene("r1020", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_31AF")

    OP_BA(0x96, 0x97)
    OP_BA(0xCD, 0xCB)
    OP_BA(0xFA, 0xCB)
    NewScene("r1030", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_31CC")

    OP_BA(0x96, 0x97)
    OP_BA(0xCD, 0xCB)
    OP_BA(0xFA, 0xCB)
    NewScene("r4000", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_31E9")

    NewScene("r4090", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_31F7")

    SetScenarioFlags(0x22, 0)
    NewScene("r4090", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3208")

    SetScenarioFlags(0x22, 2)
    NewScene("c1400", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3219")

    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    NewScene("c1010", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3231")

    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    NewScene("c1310", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3249")

    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    NewScene("c1510", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3261")

    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3279")

    OP_BA(0x65, 0x232)
    OP_BA(0x74, 0x232)
    NewScene("c1200", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_3291")

    SetScenarioFlags(0x22, 0)
    NewScene("e4500", 0, 0, 0)
    OP_07()
    Jump("loc_32B1")

    label("loc_32A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32B1")

    label("loc_32B1")

    Jump("loc_2E46")

    label("loc_32B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_14_2E17 end


    label("Function_15_32C4")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37DD")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼3066湿地帯に到着する\x01",            # 0
            "②▼3067艾欧里亚を発見\x01",              # 1
            "③▼3068林を発見\x01",                  # 2
            "④▼3069大型幻獣との戦い\x01",            # 3
            "⑤▼3070大型幻獣との戦い（戦闘\x01",      # 4
            "⑥▼3071湿地帯からの帰り\x01",            # 5
            "⑦▼3073后街の大楼に到着する\x01",      # 6
            "⑧▼3075码因兹山道での交戦\x01",        # 7
            "⑨▼3078码因兹山道での交戦（\x01",      # 8
            "⑩▼3081夜の兰花塔外観\x01",      # 9
            "?▼3083宵の口の中央広場\x01",             # 10
            "?▼3085深夜の中央広場\x01",               # 11
            "?▼3088兰迪の失踪\x01",               # 12
            "?▼3096百货屋上でのツァオ\x01",       # 13
            "?▼3101绳索を確認\x01",                 # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_3501"),
        (13, "loc_350A"),
        (12, "loc_3519"),
        (11, "loc_3519"),
        (10, "loc_3519"),
        (9, "loc_3519"),
        (8, "loc_3519"),
        (7, "loc_3519"),
        (6, "loc_3519"),
        (5, "loc_3519"),
        (4, "loc_3519"),
        (3, "loc_3519"),
        (2, "loc_351C"),
        (1, "loc_351F"),
        (0, "loc_3522"),
        (SWITCH_DEFAULT, "loc_35A8"),
    )


    label("loc_3501")

    SetScenarioFlags(0x166, 2)
    SetScenarioFlags(0x166, 3)
    SetScenarioFlags(0x166, 4)

    label("loc_350A")

    SetScenarioFlags(0x165, 5)
    SetScenarioFlags(0x165, 6)
    SetScenarioFlags(0x165, 7)
    SetScenarioFlags(0x166, 0)
    SetScenarioFlags(0x166, 1)

    label("loc_3519")

    SetScenarioFlags(0x165, 4)

    label("loc_351C")

    SetScenarioFlags(0x165, 3)

    label("loc_351F")

    SetScenarioFlags(0x165, 2)

    label("loc_3522")

    SetScenarioFlags(0x165, 1)
    SetScenarioFlags(0x164, 7)
    SetScenarioFlags(0x165, 0)
    SetScenarioFlags(0x164, 3)
    SetScenarioFlags(0x164, 4)
    SetScenarioFlags(0x164, 5)
    SetScenarioFlags(0x164, 6)
    SetScenarioFlags(0x164, 2)
    SetScenarioFlags(0x164, 1)
    SetScenarioFlags(0x168, 2)
    SetScenarioFlags(0x164, 0)
    SetScenarioFlags(0x163, 6)
    SetScenarioFlags(0x163, 7)
    SetScenarioFlags(0x163, 4)
    SetScenarioFlags(0x163, 5)
    SetScenarioFlags(0x163, 3)
    SetScenarioFlags(0x163, 2)
    SetScenarioFlags(0x163, 1)
    SetScenarioFlags(0x162, 5)
    SetScenarioFlags(0x162, 6)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x163, 0)
    SetScenarioFlags(0x162, 4)
    SetScenarioFlags(0x162, 2)
    SetScenarioFlags(0x162, 3)
    SetScenarioFlags(0x162, 0)
    SetScenarioFlags(0x162, 1)
    SetScenarioFlags(0x161, 6)
    SetScenarioFlags(0x161, 7)
    SetScenarioFlags(0x161, 5)
    SetScenarioFlags(0x160, 4)
    SetScenarioFlags(0x161, 1)
    SetScenarioFlags(0x161, 2)
    SetScenarioFlags(0x161, 3)
    SetScenarioFlags(0x161, 0)
    SetScenarioFlags(0x168, 1)
    SetScenarioFlags(0x160, 3)
    SetScenarioFlags(0x160, 2)
    SetScenarioFlags(0x160, 0)
    SetScenarioFlags(0x160, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35AD")

    label("loc_35A8")

    Jump("loc_35AD")

    label("loc_35AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3641")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "与诺埃尔一起\x01",      # 0
            "瓦吉一起\x01",        # 1
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_361F"),
        (1, "loc_362E"),
        (SWITCH_DEFAULT, "loc_363D"),
    )


    label("loc_361F")

    RemoveParty(0x4, 0xFF)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_363D")

    label("loc_362E")

    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    Jump("loc_363D")

    label("loc_363D")

    AddParty(0x5, 0xFF, 0xFF)

    label("loc_3641")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_36A5"),
        (1, "loc_36B6"),
        (2, "loc_36C4"),
        (3, "loc_36D2"),
        (4, "loc_36E0"),
        (5, "loc_36F1"),
        (6, "loc_3702"),
        (7, "loc_371C"),
        (8, "loc_372D"),
        (9, "loc_3747"),
        (10, "loc_3761"),
        (11, "loc_3772"),
        (12, "loc_3789"),
        (13, "loc_379D"),
        (14, "loc_37B3"),
        (SWITCH_DEFAULT, "loc_37C9"),
    )


    label("loc_36A5")

    SetScenarioFlags(0x22, 0)
    NewScene("m4200", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_36B6")

    NewScene("m4210", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_36C4")

    NewScene("m4220", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_36D2")

    NewScene("m4290", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_36E0")

    SetScenarioFlags(0x22, 0)
    NewScene("m4290", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_36F1")

    SetScenarioFlags(0x22, 1)
    NewScene("e4500", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_3702")

    SetScenarioFlags(0x22, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0500", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_371C")

    SetScenarioFlags(0x22, 4)
    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_372D")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2050", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_3747")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c150B", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_3761")

    SetScenarioFlags(0x22, 3)
    NewScene("c010B", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_3772")

    SetScenarioFlags(0x22, 4)
    VolumeBGM(0x3C, 0x64)
    NewScene("c010B", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_3789")

    RemoveParty(0x3, 0xFF)
    SetScenarioFlags(0x23, 2)
    NewScene("c0120", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_379D")

    RemoveParty(0x3, 0xFF)
    OP_BA(0x96, 0x97)
    NewScene("c0180", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_37B3")

    RemoveParty(0x3, 0xFF)
    OP_BA(0x96, 0x97)
    NewScene("r2030", 0, 0, 0)
    OP_07()
    Jump("loc_37D8")

    label("loc_37C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37D8")

    label("loc_37D8")

    Jump("loc_32F3")

    label("loc_37DD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_15_32C4 end


    label("Function_16_37EB")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_381A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A48")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼3103軍用魔獣の襲撃\x01",              # 0
            "②▼3104軍用魔獣の襲撃（戦闘後\x01",      # 1
            "③▼3106谢莉との戦闘\x01",          # 2
            "④▼3107谢莉との戦闘（戦\x01",      # 3
            "⑤▼3108晚上の鉱山町\x01",                # 4
            "Cancel\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (4, "loc_38ED"),
        (3, "loc_38ED"),
        (2, "loc_38ED"),
        (1, "loc_38F3"),
        (0, "loc_38F3"),
        (SWITCH_DEFAULT, "loc_399D"),
    )


    label("loc_38ED")

    SetScenarioFlags(0x166, 6)
    SetScenarioFlags(0x166, 7)

    label("loc_38F3")

    SetScenarioFlags(0x166, 5)
    SetScenarioFlags(0x166, 2)
    SetScenarioFlags(0x166, 3)
    SetScenarioFlags(0x166, 4)
    SetScenarioFlags(0x165, 5)
    SetScenarioFlags(0x165, 6)
    SetScenarioFlags(0x165, 7)
    SetScenarioFlags(0x166, 0)
    SetScenarioFlags(0x166, 1)
    SetScenarioFlags(0x165, 4)
    SetScenarioFlags(0x165, 3)
    SetScenarioFlags(0x165, 2)
    SetScenarioFlags(0x165, 1)
    SetScenarioFlags(0x164, 7)
    SetScenarioFlags(0x165, 0)
    SetScenarioFlags(0x164, 3)
    SetScenarioFlags(0x164, 4)
    SetScenarioFlags(0x164, 5)
    SetScenarioFlags(0x164, 6)
    SetScenarioFlags(0x164, 2)
    SetScenarioFlags(0x164, 1)
    SetScenarioFlags(0x168, 2)
    SetScenarioFlags(0x164, 0)
    SetScenarioFlags(0x163, 6)
    SetScenarioFlags(0x163, 7)
    SetScenarioFlags(0x163, 4)
    SetScenarioFlags(0x163, 5)
    SetScenarioFlags(0x163, 3)
    SetScenarioFlags(0x163, 2)
    SetScenarioFlags(0x163, 1)
    SetScenarioFlags(0x162, 5)
    SetScenarioFlags(0x162, 6)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x163, 0)
    SetScenarioFlags(0x162, 4)
    SetScenarioFlags(0x162, 2)
    SetScenarioFlags(0x162, 3)
    SetScenarioFlags(0x162, 0)
    SetScenarioFlags(0x162, 1)
    SetScenarioFlags(0x161, 6)
    SetScenarioFlags(0x161, 7)
    SetScenarioFlags(0x161, 5)
    SetScenarioFlags(0x160, 4)
    SetScenarioFlags(0x161, 1)
    SetScenarioFlags(0x161, 2)
    SetScenarioFlags(0x161, 3)
    SetScenarioFlags(0x161, 0)
    SetScenarioFlags(0x168, 1)
    SetScenarioFlags(0x160, 3)
    SetScenarioFlags(0x160, 2)
    SetScenarioFlags(0x160, 0)
    SetScenarioFlags(0x160, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39A2")

    label("loc_399D")

    Jump("loc_39A2")

    label("loc_39A2")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_39CA"),
        (1, "loc_39DB"),
        (2, "loc_39EF"),
        (3, "loc_3A09"),
        (4, "loc_3A23"),
        (SWITCH_DEFAULT, "loc_3A34"),
    )


    label("loc_39CA")

    RemoveParty(0x3, 0xFF)
    NewScene("m4160", 103, 0, 0)
    OP_07()
    Jump("loc_3A43")

    label("loc_39DB")

    RemoveParty(0x3, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("m4160", 0, 0, 0)
    OP_07()
    Jump("loc_3A43")

    label("loc_39EF")

    RemoveParty(0x3, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_3A43")

    label("loc_3A09")

    SetScenarioFlags(0x22, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_3A43")

    label("loc_3A23")

    SetScenarioFlags(0x22, 3)
    NewScene("t0500", 0, 0, 0)
    OP_07()
    Jump("loc_3A43")

    label("loc_3A34")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A43")

    label("loc_3A43")

    Jump("loc_381A")

    label("loc_3A48")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_16_37EB end


    label("Function_17_3A56")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EC6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼4001晚上の歓楽街\x01",                # 0
            "②▼4003火势熊熊的歓楽街\x01",      # 1
            "③▼4006兰花塔前の攻防\x01",      # 2
            "④▼4007旧市街の魔人瓦鲁德\x01",        # 3
            "⑤▼4008黒月襲撃\x01",                    # 4
            "⑥▼4010回来的罗伊德等人\x01",        # 5
            "⑦▼4013ＩＢＣ逃出来的人\x01",      # 6
            "⑧▼4016戦鬼西格蒙特との戦い\x01",      # 7
            "⑨▼4017戦鬼西格蒙特との戦い\x01",      # 8
            "⑩▼4020百货屋上での交谈\x01",      # 9
            "?▼4023１週間後の克洛斯贝尔（\x01",       # 10
            "?▼4027支援業務再開\x01",                 # 11
            "?▼4030乌尔丝拉病院に入る\x01",           # 12
            "?▼4032芙兰の看望\x01",             # 13
            "?▼4035约那の連絡\x01",               # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_3CA6"),
        (13, "loc_3CAF"),
        (12, "loc_3CB5"),
        (11, "loc_3CBB"),
        (10, "loc_3CBB"),
        (9, "loc_3CBB"),
        (8, "loc_3CBB"),
        (7, "loc_3CBB"),
        (6, "loc_3CBE"),
        (5, "loc_3CC1"),
        (4, "loc_3CC1"),
        (3, "loc_3CC1"),
        (2, "loc_3CC1"),
        (1, "loc_3CC1"),
        (0, "loc_3CC1"),
        (SWITCH_DEFAULT, "loc_3CCF"),
    )


    label("loc_3CA6")

    SetScenarioFlags(0x180, 7)
    SetScenarioFlags(0x181, 0)
    SetScenarioFlags(0x181, 1)

    label("loc_3CAF")

    SetScenarioFlags(0x180, 5)
    SetScenarioFlags(0x180, 6)

    label("loc_3CB5")

    SetScenarioFlags(0x180, 2)
    SetScenarioFlags(0x180, 3)

    label("loc_3CBB")

    SetScenarioFlags(0x180, 1)

    label("loc_3CBE")

    SetScenarioFlags(0x180, 0)

    label("loc_3CC1")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CD4")

    label("loc_3CCF")

    Jump("loc_3CD4")

    label("loc_3CD4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D38"),
        (1, "loc_3D49"),
        (2, "loc_3D63"),
        (3, "loc_3D7D"),
        (4, "loc_3D97"),
        (5, "loc_3DB1"),
        (6, "loc_3DCB"),
        (7, "loc_3DDE"),
        (8, "loc_3DF1"),
        (9, "loc_3E0B"),
        (10, "loc_3E25"),
        (11, "loc_3E36"),
        (12, "loc_3E5B"),
        (13, "loc_3E78"),
        (14, "loc_3E95"),
        (SWITCH_DEFAULT, "loc_3EB2"),
    )


    label("loc_3D38")

    SetScenarioFlags(0x22, 3)
    NewScene("c0400", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3D49")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c040B", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3D63")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c150B", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3D7D")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e3800", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3D97")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c120B", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3DB1")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c030B", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3DCB")

    OP_BA(0x96, 0x220)
    NewScene("c120B", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3DDE")

    OP_BA(0x96, 0x220)
    NewScene("c130B", 102, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3DF1")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c130B", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3E0B")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c018D", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3E25")

    SetScenarioFlags(0x22, 0)
    NewScene("c110D", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3E36")

    SetScenarioFlags(0x23, 3)
    OP_BA(0x96, 0x233)
    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3E5B")

    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("t1500", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3E78")

    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("t1550", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3E95")

    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("t1500", 0, 0, 0)
    OP_07()
    Jump("loc_3EC1")

    label("loc_3EB2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3EC1")

    label("loc_3EC1")

    Jump("loc_3A88")

    label("loc_3EC6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_17_3A56 end


    label("Function_18_3ED4")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43AD")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼4036港湾区の灯塔前の约那\x01",        # 0
            "②▼4037熱処理工厂の空間に\x01",      # 1
            "③▼4038中間地点到达\x01",      # 2
            "④▼4039トルゾーＺとの戦い\x01",          # 3
            "⑤▼4040トルゾーＺとの戦い（戦\x01",      # 4
            "⑥▼4042离开灯塔\x01",        # 5
            "⑦▼4044塞西尔の訪問\x01",                # 6
            "⑧▼4045大統領就任演説１\x01",            # 7
            "⑨▼4053大統領就任演説10\x01",            # 8
            "⑩▼4054游击士协会での会話\x01",              # 9
            "?▼4055旧鲁巴切商会前に来\x01",       # 10
            "?▼4057会長室に入る\x01",                 # 11
            "?▼4059被带走的琪雅\x01",           # 12
            "?▼4061米修拉姆に到着\x01",             # 13
            "?▼4062主题公园前の幻獣戦\x01",       # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_4122"),
        (13, "loc_4125"),
        (12, "loc_4125"),
        (11, "loc_4125"),
        (10, "loc_412B"),
        (9, "loc_412E"),
        (8, "loc_4131"),
        (7, "loc_4131"),
        (6, "loc_4131"),
        (5, "loc_4131"),
        (4, "loc_4137"),
        (3, "loc_4137"),
        (2, "loc_413A"),
        (1, "loc_413D"),
        (0, "loc_4143"),
        (SWITCH_DEFAULT, "loc_416F"),
    )


    label("loc_4122")

    SetScenarioFlags(0x182, 5)

    label("loc_4125")

    SetScenarioFlags(0x182, 3)
    SetScenarioFlags(0x182, 4)

    label("loc_412B")

    SetScenarioFlags(0x182, 2)

    label("loc_412E")

    SetScenarioFlags(0x182, 1)

    label("loc_4131")

    SetScenarioFlags(0x181, 7)
    SetScenarioFlags(0x182, 0)

    label("loc_4137")

    SetScenarioFlags(0x181, 6)

    label("loc_413A")

    SetScenarioFlags(0x181, 5)

    label("loc_413D")

    SetScenarioFlags(0x181, 3)
    SetScenarioFlags(0x181, 4)

    label("loc_4143")

    SetScenarioFlags(0x181, 2)
    SetScenarioFlags(0x180, 7)
    SetScenarioFlags(0x181, 0)
    SetScenarioFlags(0x181, 1)
    SetScenarioFlags(0x180, 5)
    SetScenarioFlags(0x180, 6)
    SetScenarioFlags(0x180, 2)
    SetScenarioFlags(0x180, 3)
    SetScenarioFlags(0x180, 1)
    SetScenarioFlags(0x180, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4174")

    label("loc_416F")

    Jump("loc_4174")

    label("loc_4174")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_419D")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)

    label("loc_419D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4201"),
        (1, "loc_421E"),
        (2, "loc_423F"),
        (3, "loc_4260"),
        (4, "loc_4281"),
        (5, "loc_42A5"),
        (6, "loc_42B3"),
        (7, "loc_42C4"),
        (8, "loc_42D5"),
        (9, "loc_42E6"),
        (10, "loc_4308"),
        (11, "loc_432A"),
        (12, "loc_434C"),
        (13, "loc_4366"),
        (14, "loc_4381"),
        (SWITCH_DEFAULT, "loc_4399"),
    )


    label("loc_4201")

    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("c120D", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_421E")

    AddParty(0x3D, 0xFF, 0xFF)
    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("m0200", 109, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_423F")

    AddParty(0x3D, 0xFF, 0xFF)
    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("m0200", 119, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_4260")

    AddParty(0x3D, 0xFF, 0xFF)
    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("m0209", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_4281")

    AddParty(0x3D, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 1)
    OP_BA(0x65, 0x233)
    OP_BA(0x74, 0x233)
    OP_BA(0x7B, 0x203)
    NewScene("m0209", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_42A5")

    NewScene("c120D", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_42B3")

    SetScenarioFlags(0x23, 4)
    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_42C4")

    SetScenarioFlags(0x22, 4)
    NewScene("c1500", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_42D5")

    SetScenarioFlags(0x23, 5)
    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_42E6")

    OP_BA(0x96, 0x97)
    OP_BA(0x65, 0x97)
    OP_BA(0x74, 0x97)
    OP_BA(0x75, 0x97)
    NewScene("c1010", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_4308")

    OP_BA(0x96, 0x97)
    OP_BA(0x65, 0x97)
    OP_BA(0x74, 0x97)
    OP_BA(0x75, 0x97)
    NewScene("c0500", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_432A")

    OP_BA(0x96, 0x97)
    OP_BA(0x65, 0x97)
    OP_BA(0x74, 0x97)
    OP_BA(0x75, 0x97)
    NewScene("c0597", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_434C")

    SetScenarioFlags(0x23, 6)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_4366")

    SetScenarioFlags(0x22, 1)
    OP_BA(0x235, 0x231)
    OP_BA(0xA0, 0x231)
    NewScene("t1000", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_4381")

    OP_BA(0x235, 0x231)
    OP_BA(0xA0, 0x231)
    NewScene("t1030", 0, 0, 0)
    OP_07()
    Jump("loc_43A8")

    label("loc_4399")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43A8")

    label("loc_43A8")

    Jump("loc_3F06")

    label("loc_43AD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_18_3ED4 end


    label("Function_19_43BB")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼4064玄関areaの幻獣戦\x01",          # 0
            "②▼4066城の前の幻獣戦\x01",              # 1
            "③▼4068鏡の城に入る\x01",                # 2
            "④▼4069大鏡の前に到着\x01",              # 3
            "⑤▼4071最奥の間\x01",                    # 4
            "⑥▼4072帝国軍侵攻\x01",                  # 5
            "⑦▼4074琪雅覚醒?前\x01",               # 6
            "⑧▼4084亚里欧斯国防長官との戦\x01",      # 7
            "⑨▼4085琪雅覚醒?後\x01",               # 8
            "⑩▼4086神機アイオーン降臨\x01",          # 9
            "?▼4095共和国軍壊滅?空\x01",              # 10
            "?▼4088帝国軍壊滅\x01",                   # 11
            "?▼4089卡雷利亚要塞\x01",                 # 12
            "?▼4091兰花塔屋上\x01",           # 13
            "?▼4092罗伊德被拘捕\x01",                   # 14
            "Cancel\x01",                          # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_45C0"),
        (13, "loc_45C0"),
        (12, "loc_45C0"),
        (11, "loc_45C0"),
        (10, "loc_45C0"),
        (9, "loc_45C0"),
        (8, "loc_45C0"),
        (7, "loc_45C0"),
        (6, "loc_45C0"),
        (5, "loc_45C0"),
        (4, "loc_45C0"),
        (3, "loc_45C6"),
        (2, "loc_45C9"),
        (1, "loc_45CC"),
        (0, "loc_45CF"),
        (SWITCH_DEFAULT, "loc_461F"),
    )


    label("loc_45C0")

    SetScenarioFlags(0x183, 2)
    SetScenarioFlags(0x183, 3)

    label("loc_45C6")

    SetScenarioFlags(0x183, 1)

    label("loc_45C9")

    SetScenarioFlags(0x183, 0)

    label("loc_45CC")

    SetScenarioFlags(0x182, 7)

    label("loc_45CF")

    SetScenarioFlags(0x182, 6)
    SetScenarioFlags(0x182, 5)
    SetScenarioFlags(0x182, 3)
    SetScenarioFlags(0x182, 4)
    SetScenarioFlags(0x182, 2)
    SetScenarioFlags(0x182, 1)
    SetScenarioFlags(0x181, 7)
    SetScenarioFlags(0x182, 0)
    SetScenarioFlags(0x181, 6)
    SetScenarioFlags(0x181, 5)
    SetScenarioFlags(0x181, 3)
    SetScenarioFlags(0x181, 4)
    SetScenarioFlags(0x181, 2)
    SetScenarioFlags(0x180, 7)
    SetScenarioFlags(0x181, 0)
    SetScenarioFlags(0x181, 1)
    SetScenarioFlags(0x180, 5)
    SetScenarioFlags(0x180, 6)
    SetScenarioFlags(0x180, 2)
    SetScenarioFlags(0x180, 3)
    SetScenarioFlags(0x180, 1)
    SetScenarioFlags(0x180, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4624")

    label("loc_461F")

    Jump("loc_4624")

    label("loc_4624")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4688"),
        (1, "loc_46A0"),
        (2, "loc_46B8"),
        (3, "loc_46D0"),
        (4, "loc_46DE"),
        (5, "loc_46EC"),
        (6, "loc_46FD"),
        (7, "loc_470E"),
        (8, "loc_4728"),
        (9, "loc_4739"),
        (10, "loc_4753"),
        (11, "loc_476D"),
        (12, "loc_4787"),
        (13, "loc_47A1"),
        (14, "loc_47BB"),
        (SWITCH_DEFAULT, "loc_47CC"),
    )


    label("loc_4688")

    OP_BA(0x235, 0x231)
    OP_BA(0xA0, 0x231)
    NewScene("t1300", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_46A0")

    OP_BA(0x235, 0x231)
    OP_BA(0xA0, 0x231)
    NewScene("t1400", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_46B8")

    OP_BA(0x235, 0x231)
    OP_BA(0xA0, 0x231)
    NewScene("t1401", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_46D0")

    NewScene("t1401", 108, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_46DE")

    NewScene("t1490", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_46EC")

    SetScenarioFlags(0x22, 0)
    NewScene("t2100", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_46FD")

    SetScenarioFlags(0x22, 0)
    NewScene("t1490", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_470E")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x249), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t1490", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_4728")

    SetScenarioFlags(0x22, 2)
    NewScene("t1490", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_4739")

    SetScenarioFlags(0x22, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x228), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_4753")

    SetScenarioFlags(0x24, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_476D")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4210", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_4787")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t2100", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_47A1")

    SetScenarioFlags(0x22, 4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x22A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_47BB")

    SetScenarioFlags(0x22, 3)
    NewScene("t1490", 0, 0, 0)
    OP_07()
    Jump("loc_47DB")

    label("loc_47CC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_47DB")

    label("loc_47DB")

    Jump("loc_43E5")

    label("loc_47E0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_19_43BB end


    label("Function_20_47EE")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_480F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BC0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼5001beiowarufu号甲板\x01",          # 0
            "②▼5002瓦鲁德が旧市街に現れ\x01",      # 1
            "③▼5003塔屋上?結社の会話\x01",       # 2
            "④▼5005脱走開始\x01",                    # 3
            "⑤▼5006国防軍兵士との戦闘①\x01",        # 4
            "⑥▼5008国防軍兵士との戦闘②\x01",        # 5
            "⑦▼5010国防軍兵士との戦闘③\x01",        # 6
            "⑧▼5012国防軍兵士との戦闘④\x01",        # 7
            "⑨▼5016加尔西亚と別れる\x01",            # 8
            "⑩▼5018樹海に逃げる\x01",                # 9
            "?▼5019樹海を走る罗伊德\x01",             # 10
            "?▼5021神獣蔡特登場\x01",             # 11
            "?▼5022神狼の話\x01",                     # 12
            "?▼5023与瓦吉再会\x01",             # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_49F6"),
        (12, "loc_49F6"),
        (11, "loc_49F6"),
        (10, "loc_49F6"),
        (9, "loc_49F6"),
        (8, "loc_49F9"),
        (7, "loc_4A05"),
        (6, "loc_4A08"),
        (5, "loc_4A0B"),
        (4, "loc_4A0E"),
        (3, "loc_4A11"),
        (2, "loc_4A11"),
        (1, "loc_4A11"),
        (0, "loc_4A11"),
        (SWITCH_DEFAULT, "loc_4A1F"),
    )


    label("loc_49F6")

    SetScenarioFlags(0x184, 4)

    label("loc_49F9")

    SetScenarioFlags(0x184, 0)
    SetScenarioFlags(0x184, 1)
    SetScenarioFlags(0x184, 2)
    SetScenarioFlags(0x184, 3)

    label("loc_4A05")

    SetScenarioFlags(0x183, 7)

    label("loc_4A08")

    SetScenarioFlags(0x183, 6)

    label("loc_4A0B")

    SetScenarioFlags(0x183, 5)

    label("loc_4A0E")

    SetScenarioFlags(0x183, 4)

    label("loc_4A11")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A24")

    label("loc_4A1F")

    Jump("loc_4A24")

    label("loc_4A24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A4B")
    AddParty(0xA, 0xFF, 0xFF)

    label("loc_4A4B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4AA9"),
        (1, "loc_4AC6"),
        (2, "loc_4AE0"),
        (3, "loc_4AFA"),
        (4, "loc_4B0B"),
        (5, "loc_4B19"),
        (6, "loc_4B27"),
        (7, "loc_4B35"),
        (8, "loc_4B43"),
        (9, "loc_4B51"),
        (10, "loc_4B5F"),
        (11, "loc_4B79"),
        (12, "loc_4B8A"),
        (13, "loc_4B9B"),
        (SWITCH_DEFAULT, "loc_4BAC"),
    )


    label("loc_4AA9")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 2)
    NewScene("t3520", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4AC6")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c140D", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4AE0")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x164), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4AFA")

    SetScenarioFlags(0x22, 0)
    NewScene("t6050", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B0B")

    NewScene("t6050", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B19")

    NewScene("t6051", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B27")

    NewScene("t6051", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B35")

    NewScene("t6051", 102, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B43")

    NewScene("t6000", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B51")

    NewScene("r4000", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B5F")

    SetScenarioFlags(0x22, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1C5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r4050", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B79")

    SetScenarioFlags(0x22, 1)
    NewScene("r4090", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B8A")

    SetScenarioFlags(0x22, 0)
    NewScene("e4200", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4B9B")

    SetScenarioFlags(0x22, 0)
    NewScene("e4100", 0, 0, 0)
    OP_07()
    Jump("loc_4BBB")

    label("loc_4BAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BBB")

    label("loc_4BBB")

    Jump("loc_480F")

    label("loc_4BC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_20_47EE end


    label("Function_21_4BCE")

    ClearScenarioFlags(0x26, 2)
    ClearScenarioFlags(0x26, 5)
    ClearScenarioFlags(0x26, 3)
    ClearScenarioFlags(0x27, 0)
    ClearScenarioFlags(0x26, 1)
    ClearScenarioFlags(0x27, 1)
    SetScenarioFlags(0x26, 0)
    SetScenarioFlags(0x26, 4)
    SetScenarioFlags(0x26, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_END)), "loc_4BF5")
    SetScenarioFlags(0x26, 2)

    label("loc_4BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_4C01")
    SetScenarioFlags(0x26, 5)

    label("loc_4C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_4C0D")
    SetScenarioFlags(0x26, 3)

    label("loc_4C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4C1C")
    SetScenarioFlags(0x27, 0)
    ClearScenarioFlags(0x26, 6)

    label("loc_4C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_4C28")
    SetScenarioFlags(0x26, 1)

    label("loc_4C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4C34")
    SetScenarioFlags(0x27, 1)

    label("loc_4C34")

    Return()

    # Function_21_4BCE end


    label("Function_22_4C35")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_509D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6001飛行する２機の梅尔卡瓦\x01",      # 0
            "②▼6003克洛斯贝尔領空潜入\x01",          # 1
            "③▼6004玖号機の客舱\x01",            # 2
            "④▼6008中州の外れに降り立つ\x01",        # 3
            "⑤▼6009乌尔丝拉間道途中の幻獣\x01",      # 4
            "⑥▼6011乌尔丝拉病院前の様子を\x01",      # 5
            "⑦▼6014突入前選択肢\x01",                # 6
            "⑧▼6016病院前での国防軍との戦\x01",      # 7
            "⑨▼6018伊利亚を看望event\x01",      # 8
            "⑩▼6020ドノバンを看望event\x01",      # 9
            "?▼6022乌尔丝拉病院を後にする\x01",       # 10
            "?▼6024飛行する梅尔卡瓦\x01",             # 11
            "?▼6027阿尔摩里卡村に到着する\x01",       # 12
            "?▼6029哈罗德家と会う\x01",           # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_4E7A"),
        (12, "loc_4E7D"),
        (11, "loc_4E80"),
        (10, "loc_4E80"),
        (9, "loc_4E8C"),
        (8, "loc_4E8C"),
        (7, "loc_4E8F"),
        (6, "loc_4E8F"),
        (5, "loc_4E92"),
        (4, "loc_4E95"),
        (3, "loc_4E98"),
        (2, "loc_4EA1"),
        (1, "loc_4EA1"),
        (0, "loc_4EA1"),
        (SWITCH_DEFAULT, "loc_4EAF"),
    )


    label("loc_4E7A")

    SetScenarioFlags(0x1A1, 3)

    label("loc_4E7D")

    SetScenarioFlags(0x1A1, 2)

    label("loc_4E80")

    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)

    label("loc_4E8C")

    SetScenarioFlags(0x1A0, 5)

    label("loc_4E8F")

    SetScenarioFlags(0x1A0, 4)

    label("loc_4E92")

    SetScenarioFlags(0x1A0, 3)

    label("loc_4E95")

    SetScenarioFlags(0x1A0, 2)

    label("loc_4E98")

    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)

    label("loc_4EA1")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4EB4")

    label("loc_4EAF")

    Jump("loc_4EB4")

    label("loc_4EB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EE4")
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    Jump("loc_4F43")

    label("loc_4EE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F14")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    Jump("loc_4F43")

    label("loc_4F14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F43")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_4F43")

    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4FA4"),
        (1, "loc_4FB5"),
        (2, "loc_4FCF"),
        (3, "loc_4FE0"),
        (4, "loc_4FF1"),
        (5, "loc_4FFF"),
        (6, "loc_500D"),
        (7, "loc_501B"),
        (8, "loc_502C"),
        (9, "loc_503A"),
        (10, "loc_5048"),
        (11, "loc_5059"),
        (12, "loc_506A"),
        (13, "loc_507B"),
        (SWITCH_DEFAULT, "loc_5089"),
    )


    label("loc_4FA4")

    SetScenarioFlags(0x22, 1)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_4FB5")

    SetScenarioFlags(0x22, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4310", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_4FCF")

    SetScenarioFlags(0x22, 2)
    NewScene("e3020", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_4FE0")

    SetScenarioFlags(0x22, 1)
    NewScene("r1610", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_4FF1")

    NewScene("r1540", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_4FFF")

    NewScene("r1540", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_500D")

    NewScene("r1540", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_501B")

    SetScenarioFlags(0x22, 2)
    NewScene("t1500", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_502C")

    NewScene("t1550", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_503A")

    NewScene("t1550", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_5048")

    SetScenarioFlags(0x22, 3)
    NewScene("t1500", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_5059")

    SetScenarioFlags(0x22, 3)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_506A")

    SetScenarioFlags(0x22, 0)
    NewScene("t0000", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_507B")

    NewScene("t0020", 0, 0, 0)
    OP_07()
    Jump("loc_5098")

    label("loc_5089")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5098")

    label("loc_5098")

    Jump("loc_4C68")

    label("loc_509D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_22_4C35 end


    label("Function_23_50AB")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5512")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6031古戦場に到着する\x01",            # 0
            "②▼6032《赤い星座》の伏击\x01",      # 1
            "③▼6033莉夏＆黒月登場\x01",          # 2
            "④▼6035飛行する梅尔卡瓦２\x01",          # 3
            "⑤▼6037码因兹山道に到着する\x01",      # 4
            "⑥▼6038工房前に到着する\x01",            # 5
            "⑦▼6041軍用魔獣の群れに襲撃さ\x01",      # 6
            "⑧▼6043導力地雷の設置を確認\x01",        # 7
            "⑨▼6044トンネル道から出て来た\x01",      # 8
            "⑩▼6046崖上からの狙撃\x01",              # 9
            "?▼6047崖上からの狙撃（戦闘後\x01",       # 10
            "?▼6048码因兹?宿酒場\x01",              # 11
            "?▼6050飛行する梅尔卡瓦３\x01",           # 12
            "?▼6052西克洛斯贝尔街道に到着\x01",       # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_52F3"),
        (12, "loc_52F6"),
        (11, "loc_52F6"),
        (10, "loc_52F6"),
        (9, "loc_52F6"),
        (8, "loc_52FC"),
        (7, "loc_52FF"),
        (6, "loc_5302"),
        (5, "loc_5308"),
        (4, "loc_530B"),
        (3, "loc_530E"),
        (2, "loc_530E"),
        (1, "loc_530E"),
        (0, "loc_5311"),
        (SWITCH_DEFAULT, "loc_534C"),
    )


    label("loc_52F3")

    SetScenarioFlags(0x1A2, 7)

    label("loc_52F6")

    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)

    label("loc_52FC")

    SetScenarioFlags(0x1A2, 4)

    label("loc_52FF")

    SetScenarioFlags(0x1A2, 3)

    label("loc_5302")

    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)

    label("loc_5308")

    SetScenarioFlags(0x1A2, 0)

    label("loc_530B")

    SetScenarioFlags(0x1A1, 7)

    label("loc_530E")

    SetScenarioFlags(0x1A1, 6)

    label("loc_5311")

    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5351")

    label("loc_534C")

    Jump("loc_5351")

    label("loc_5351")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_538E")
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    Jump("loc_53CA")

    label("loc_538E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53CA")
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_53CA")

    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_542B"),
        (1, "loc_5439"),
        (2, "loc_5447"),
        (3, "loc_5458"),
        (4, "loc_5469"),
        (5, "loc_5477"),
        (6, "loc_5485"),
        (7, "loc_5493"),
        (8, "loc_54A1"),
        (9, "loc_54AF"),
        (10, "loc_54BD"),
        (11, "loc_54CE"),
        (12, "loc_54DF"),
        (13, "loc_54F0"),
        (SWITCH_DEFAULT, "loc_54FE"),
    )


    label("loc_542B")

    NewScene("r3000", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5439")

    NewScene("r3070", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5447")

    SetScenarioFlags(0x22, 0)
    NewScene("r3070", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5458")

    SetScenarioFlags(0x22, 4)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5469")

    NewScene("r2030", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5477")

    NewScene("t3000", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5485")

    NewScene("r2030", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_5493")

    NewScene("r2050", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54A1")

    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54AF")

    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54BD")

    SetScenarioFlags(0x22, 6)
    NewScene("r2060", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54CE")

    SetScenarioFlags(0x22, 4)
    NewScene("t0500", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54DF")

    SetScenarioFlags(0x22, 5)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54F0")

    NewScene("r1030", 0, 0, 0)
    OP_07()
    Jump("loc_550D")

    label("loc_54FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_550D")

    label("loc_550D")

    Jump("loc_50EA")

    label("loc_5512")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_23_50AB end


    label("Function_24_5520")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5567")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59B3")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6053線路沿いに門まで行く事\x01",      # 0
            "②▼6058贝尔加德門に到着する\x01",      # 1
            "③▼6060拦路的诺埃尔\x01",            # 2
            "④▼6061索尼娅司令登場\x01",            # 3
            "⑤▼6064飛行する梅尔卡瓦４\x01",          # 4
            "⑥▼6067米修拉姆の攻略を開始\x01",      # 5
            "⑦▼6069ビーチmapから出る直\x01",      # 6
            "⑧▼6071蔡特の陽動\x01",              # 7
            "⑨▼6073拱廊での戦闘\x01",          # 8
            "⑩▼6074別荘区画での戦闘\x01",            # 9
            "?▼6075迎賓館前での戦闘\x01",             # 10
            "?▼6076迎賓館前での戦闘（戦闘\x01",       # 11
            "?▼6077漆黒の人形兵器との戦い\x01",       # 12
            "?▼6078艾莉たちと合流\x01",             # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_576B"),
        (12, "loc_576B"),
        (11, "loc_576E"),
        (10, "loc_576E"),
        (9, "loc_5771"),
        (8, "loc_5774"),
        (7, "loc_5777"),
        (6, "loc_5777"),
        (5, "loc_577A"),
        (4, "loc_577D"),
        (3, "loc_577D"),
        (2, "loc_577D"),
        (1, "loc_5780"),
        (0, "loc_5783"),
        (SWITCH_DEFAULT, "loc_57DF"),
    )


    label("loc_576B")

    SetScenarioFlags(0x1A4, 0)

    label("loc_576E")

    SetScenarioFlags(0x1A3, 7)

    label("loc_5771")

    SetScenarioFlags(0x1A3, 6)

    label("loc_5774")

    SetScenarioFlags(0x1A3, 5)

    label("loc_5777")

    SetScenarioFlags(0x1A3, 4)

    label("loc_577A")

    SetScenarioFlags(0x1A3, 3)

    label("loc_577D")

    SetScenarioFlags(0x1A3, 2)

    label("loc_5780")

    SetScenarioFlags(0x1A3, 1)

    label("loc_5783")

    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57E4")

    label("loc_57DF")

    Jump("loc_57E4")

    label("loc_57E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5820")
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_5820")

    OP_CE(0x1)
    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5883"),
        (1, "loc_5891"),
        (2, "loc_589F"),
        (3, "loc_58AD"),
        (4, "loc_58BE"),
        (5, "loc_58CF"),
        (6, "loc_58E0"),
        (7, "loc_58F8"),
        (8, "loc_5913"),
        (9, "loc_592B"),
        (10, "loc_5943"),
        (11, "loc_595B"),
        (12, "loc_5976"),
        (13, "loc_598E"),
        (SWITCH_DEFAULT, "loc_599F"),
    )


    label("loc_5883")

    NewScene("r1010", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_5891")

    NewScene("t2000", 104, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_589F")

    NewScene("t2030", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_58AD")

    SetScenarioFlags(0x22, 1)
    NewScene("t2030", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_58BE")

    SetScenarioFlags(0x22, 6)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_58CF")

    SetScenarioFlags(0x22, 1)
    NewScene("t1310", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_58E0")

    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1310", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_58F8")

    SetScenarioFlags(0x22, 0)
    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1030", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_5913")

    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1020", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_592B")

    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1010", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_5943")

    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1100", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_595B")

    SetScenarioFlags(0x22, 0)
    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1100", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_5976")

    OP_BA(0xFB, 0x21C)
    OP_BA(0x235, 0x21C)
    NewScene("t1110", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_598E")

    SetScenarioFlags(0x22, 0)
    NewScene("t1110", 0, 0, 0)
    OP_07()
    Jump("loc_59AE")

    label("loc_599F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59AE")

    label("loc_59AE")

    Jump("loc_5567")

    label("loc_59B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_24_5520 end


    label("Function_25_59C1")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60B1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6079飛行する梅尔卡瓦５\x01",          # 0
            "②▼6083無線增幅器地点上空\x01",      # 1
            "③▼6084克洛斯贝尔独立国の無効\x01",      # 2
            "④▼6092约鲁古からの連絡\x01",            # 3
            "⑤▼6093月の僧院前に到达\x01",      # 4
            "⑥▼6095被封印的门を確認する\x01",      # 5
            "⑦▼6096道化師肯帕雷拉との\x01",      # 6
            "⑧▼6097道化師肯帕雷拉との\x01",      # 7
            "⑨▼6098星見の塔前にやって来る\x01",      # 8
            "⑩▼6100剛毅のアイネスとの戦い\x01",      # 9
            "?▼6102魔弓のエンネアとの戦い\x01",       # 10
            "?▼6104神速のデュバリィとの戦\x01",       # 11
            "?▼6106鋼の聖女アリアンロード\x01",       # 12
            "?▼6108鋼の聖女アリアンロード\x01",       # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_5C30"),
        (12, "loc_5C30"),
        (11, "loc_5C33"),
        (10, "loc_5C36"),
        (9, "loc_5C39"),
        (8, "loc_5C3C"),
        (7, "loc_5C3F"),
        (6, "loc_5C3F"),
        (5, "loc_5C42"),
        (4, "loc_5C45"),
        (3, "loc_5C48"),
        (2, "loc_5C48"),
        (1, "loc_5C48"),
        (0, "loc_5C4B"),
        (SWITCH_DEFAULT, "loc_5CBF"),
    )


    label("loc_5C30")

    SetScenarioFlags(0x1A5, 1)

    label("loc_5C33")

    SetScenarioFlags(0x1A5, 0)

    label("loc_5C36")

    SetScenarioFlags(0x1A4, 7)

    label("loc_5C39")

    SetScenarioFlags(0x1A4, 6)

    label("loc_5C3C")

    SetScenarioFlags(0x1A4, 5)

    label("loc_5C3F")

    SetScenarioFlags(0x1A4, 4)

    label("loc_5C42")

    SetScenarioFlags(0x1A4, 3)

    label("loc_5C45")

    SetScenarioFlags(0x1A4, 2)

    label("loc_5C48")

    SetScenarioFlags(0x1A4, 1)

    label("loc_5C4B")

    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5CC4")

    label("loc_5CBF")

    Jump("loc_5CC4")

    label("loc_5CC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EF0")
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "诺埃尔と一起\x01",        # 0
            "瓦吉と一起\x01",          # 1
            "莉夏と一起\x01",      # 2
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_5D60"),
        (1, "loc_5D69"),
        (2, "loc_5D72"),
        (SWITCH_DEFAULT, "loc_5D7B"),
    )


    label("loc_5D60")

    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_5D7B")

    label("loc_5D69")

    AddParty(0x4, 0xF4, 0xFF)
    Jump("loc_5D7B")

    label("loc_5D72")

    AddParty(0x5, 0xF4, 0xFF)
    Jump("loc_5D7B")

    label("loc_5D7B")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DC0")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_5DC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5DFA")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_5DFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E30")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")

    label("loc_5E30")

    MenuCmd(0x2, 0x2, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x4)
    OP_60(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7B")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_5E64"),
        (1, "loc_5E6D"),
        (SWITCH_DEFAULT, "loc_5E76"),
    )


    label("loc_5E64")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_5E76")

    label("loc_5E6D")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_5E76")

    label("loc_5E76")

    Jump("loc_5EF0")

    label("loc_5E7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EB8")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_5EA1"),
        (1, "loc_5EAA"),
        (SWITCH_DEFAULT, "loc_5EB3"),
    )


    label("loc_5EA1")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_5EB3")

    label("loc_5EAA")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_5EB3")

    label("loc_5EB3")

    Jump("loc_5EF0")

    label("loc_5EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EF0")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_5EDE"),
        (1, "loc_5EE7"),
        (SWITCH_DEFAULT, "loc_5EF0"),
    )


    label("loc_5EDE")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_5EF0")

    label("loc_5EE7")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_5EF0")

    label("loc_5EF0")

    OP_CE(0x1)
    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F53"),
        (1, "loc_5F81"),
        (2, "loc_5FAF"),
        (3, "loc_5FDD"),
        (4, "loc_600B"),
        (5, "loc_6019"),
        (6, "loc_6027"),
        (7, "loc_6035"),
        (8, "loc_6046"),
        (9, "loc_6054"),
        (10, "loc_6062"),
        (11, "loc_6070"),
        (12, "loc_607E"),
        (13, "loc_608C"),
        (SWITCH_DEFAULT, "loc_609D"),
    )


    label("loc_5F53")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 7)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_5F81")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 0)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_5FAF")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 2)
    NewScene("e3020", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_5FDD")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 3)
    NewScene("e3020", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_600B")

    NewScene("r2070", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6019")

    NewScene("m2000", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6027")

    NewScene("m2060", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6035")

    SetScenarioFlags(0x22, 1)
    NewScene("m2060", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6046")

    NewScene("m1000", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6054")

    NewScene("m1140", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6062")

    NewScene("m1060", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_6070")

    NewScene("m1099", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_607E")

    NewScene("m1090", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_608C")

    SetScenarioFlags(0x22, 1)
    NewScene("m1090", 0, 0, 0)
    OP_07()
    Jump("loc_60AC")

    label("loc_609D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60AC")

    label("loc_60AC")

    Jump("loc_5A08")

    label("loc_60B1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_25_59C1 end


    label("Function_26_60BF")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B78")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6109克洛斯贝尔市の結界が解\x01",      # 0
            "②▼6117夜の梅尔卡瓦\x01",                # 1
            "③▼6118梅尔卡瓦合流\x01",                # 2
            "④▼6119克洛斯贝尔市解放作戦開\x01",      # 3
            "⑤▼6120克洛斯贝尔市解放作戦開\x01",      # 4
            "⑥▼6121梅尔卡瓦伍号機がアイオ\x01",      # 5
            "⑦▼6125克洛斯贝尔市解放作戦開\x01",      # 6
            "⑧▼6127克洛斯贝尔市解放作戦開\x01",      # 7
            "⑨▼6129襲い掛かる魔導兵\x01",            # 8
            "⑩▼6131与課長等人碰头\x01",        # 9
            "?▽6132支援課に戻ってくる\x01",           # 10
            "?▼6133導力車を检查\x01",             # 11
            "?▼6134克洛斯贝尔駅前選択肢\x01",         # 12
            "?▼6137３番ホーム、２番車輌の\x01",       # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_62E8"),
        (12, "loc_62EE"),
        (11, "loc_62F1"),
        (10, "loc_62F1"),
        (9, "loc_62F4"),
        (8, "loc_62F4"),
        (7, "loc_62F4"),
        (6, "loc_62F4"),
        (5, "loc_62F4"),
        (4, "loc_62F4"),
        (3, "loc_62F4"),
        (2, "loc_62F4"),
        (1, "loc_62F7"),
        (0, "loc_62F7"),
        (SWITCH_DEFAULT, "loc_6386"),
    )


    label("loc_62E8")

    SetScenarioFlags(0x1A5, 6)
    SetScenarioFlags(0x1A5, 7)

    label("loc_62EE")

    SetScenarioFlags(0x1A5, 5)

    label("loc_62F1")

    SetScenarioFlags(0x1A5, 3)

    label("loc_62F4")

    SetScenarioFlags(0x1A5, 2)

    label("loc_62F7")

    SetScenarioFlags(0x1A5, 1)
    SetScenarioFlags(0x1A5, 0)
    SetScenarioFlags(0x1A4, 7)
    SetScenarioFlags(0x1A4, 6)
    SetScenarioFlags(0x1A4, 5)
    SetScenarioFlags(0x1A4, 4)
    SetScenarioFlags(0x1A4, 3)
    SetScenarioFlags(0x1A4, 2)
    SetScenarioFlags(0x1A4, 1)
    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_638B")

    label("loc_6386")

    Jump("loc_638B")

    label("loc_638B")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C6")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "诺埃尔と一起\x01",        # 0
            "瓦吉と一起\x01",          # 1
            "莉夏と一起\x01",      # 2
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_6436"),
        (1, "loc_643F"),
        (2, "loc_6448"),
        (SWITCH_DEFAULT, "loc_6451"),
    )


    label("loc_6436")

    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_6451")

    label("loc_643F")

    AddParty(0x4, 0xF4, 0xFF)
    Jump("loc_6451")

    label("loc_6448")

    AddParty(0x5, 0xF4, 0xFF)
    Jump("loc_6451")

    label("loc_6451")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6496")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_6496")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64D0")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_64D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6506")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")

    label("loc_6506")

    MenuCmd(0x2, 0x2, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x4)
    OP_60(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6551")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_653A"),
        (1, "loc_6543"),
        (SWITCH_DEFAULT, "loc_654C"),
    )


    label("loc_653A")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_654C")

    label("loc_6543")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_654C")

    label("loc_654C")

    Jump("loc_65C6")

    label("loc_6551")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_658E")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_6577"),
        (1, "loc_6580"),
        (SWITCH_DEFAULT, "loc_6589"),
    )


    label("loc_6577")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_6589")

    label("loc_6580")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_6589")

    label("loc_6589")

    Jump("loc_65C6")

    label("loc_658E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65C6")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_65B4"),
        (1, "loc_65BD"),
        (SWITCH_DEFAULT, "loc_65C6"),
    )


    label("loc_65B4")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_65C6")

    label("loc_65BD")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_65C6")

    label("loc_65C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_690D")
    ClearScenarioFlags(0x20, 5)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "诺埃尔と一起\x01",        # 0
            "瓦吉と一起\x01",          # 1
            "莉夏と一起\x01",      # 2
            "达德利と一起\x01",      # 3
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_666D"),
        (1, "loc_6676"),
        (2, "loc_667F"),
        (3, "loc_6688"),
        (SWITCH_DEFAULT, "loc_6691"),
    )


    label("loc_666D")

    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_6691")

    label("loc_6676")

    AddParty(0x4, 0xF4, 0xFF)
    Jump("loc_6691")

    label("loc_667F")

    AddParty(0x5, 0xF4, 0xFF)
    Jump("loc_6691")

    label("loc_6688")

    AddParty(0x9, 0xF4, 0xFF)
    Jump("loc_6691")

    label("loc_6691")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66EC")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_66EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_673C")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_673C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6788")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_6788")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67D4")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_67D4")

    MenuCmd(0x2, 0x2, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x4)
    OP_60(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_682E")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_680E"),
        (1, "loc_6817"),
        (2, "loc_6820"),
        (SWITCH_DEFAULT, "loc_6829"),
    )


    label("loc_680E")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_6829")

    label("loc_6817")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_6829")

    label("loc_6820")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_6829")

    label("loc_6829")

    Jump("loc_690D")

    label("loc_682E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_687A")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_685A"),
        (1, "loc_6863"),
        (2, "loc_686C"),
        (SWITCH_DEFAULT, "loc_6875"),
    )


    label("loc_685A")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_6875")

    label("loc_6863")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_6875")

    label("loc_686C")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_6875")

    label("loc_6875")

    Jump("loc_690D")

    label("loc_687A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68C6")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_68A6"),
        (1, "loc_68AF"),
        (2, "loc_68B8"),
        (SWITCH_DEFAULT, "loc_68C1"),
    )


    label("loc_68A6")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_68C1")

    label("loc_68AF")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_68C1")

    label("loc_68B8")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_68C1")

    label("loc_68C1")

    Jump("loc_690D")

    label("loc_68C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_690D")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_68F2"),
        (1, "loc_68FB"),
        (2, "loc_6904"),
        (SWITCH_DEFAULT, "loc_690D"),
    )


    label("loc_68F2")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_690D")

    label("loc_68FB")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_690D")

    label("loc_6904")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_690D")

    label("loc_690D")

    OP_CE(0x1)
    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6970"),
        (1, "loc_698A"),
        (2, "loc_699B"),
        (3, "loc_69C9"),
        (4, "loc_69E3"),
        (5, "loc_69FD"),
        (6, "loc_6A17"),
        (7, "loc_6A31"),
        (8, "loc_6A4B"),
        (9, "loc_6A82"),
        (10, "loc_6AB4"),
        (11, "loc_6AE0"),
        (12, "loc_6B0C"),
        (13, "loc_6B38"),
        (SWITCH_DEFAULT, "loc_6B64"),
    )


    label("loc_6970")

    SetScenarioFlags(0x23, 7)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x23B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_698A")

    SetScenarioFlags(0x22, 0)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_699B")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_69C9")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2010", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_69E3")

    SetScenarioFlags(0x22, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r0000", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_69FD")

    SetScenarioFlags(0x23, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6A17")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4211", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6A31")

    SetScenarioFlags(0x22, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r1500", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6A4B")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x24, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x220), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6A82")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 1)
    NewScene("m0302", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6AB4")

    OP_BA(0x96, 0x23D)
    OP_BA(0x65, 0x23D)
    OP_BA(0x74, 0x23D)
    OP_BA(0x75, 0x23D)
    OP_BA(0x6F, 0x23D)
    OP_BA(0x71, 0x23D)
    NewScene("c0110", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6AE0")

    OP_BA(0x96, 0x23D)
    OP_BA(0x65, 0x23D)
    OP_BA(0x74, 0x23D)
    OP_BA(0x75, 0x23D)
    OP_BA(0x6F, 0x23D)
    OP_BA(0x71, 0x23D)
    NewScene("c0200", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6B0C")

    OP_BA(0x96, 0x23D)
    OP_BA(0x65, 0x23D)
    OP_BA(0x74, 0x23D)
    OP_BA(0x75, 0x23D)
    OP_BA(0x6F, 0x23D)
    OP_BA(0x71, 0x23D)
    NewScene("c0000", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6B38")

    OP_BA(0x96, 0x23D)
    OP_BA(0x65, 0x23D)
    OP_BA(0x74, 0x23D)
    OP_BA(0x75, 0x23D)
    OP_BA(0x6F, 0x23D)
    OP_BA(0x71, 0x23D)
    NewScene("c0800", 0, 0, 0)
    OP_07()
    Jump("loc_6B73")

    label("loc_6B64")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B73")

    label("loc_6B73")

    Jump("loc_60DE")

    label("loc_6B78")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_26_60BF end


    label("Function_27_6B86")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6BA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_738C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6139兰花塔突入作戦\x01",      # 0
            "②▼6141梅尔卡瓦伍号機ＶＳ高速\x01",      # 1
            "③▼6144帕蒂尔玛蒂尔ＶＳ重量\x01",      # 2
            "④▼6145攻略を開始する罗伊德た\x01",      # 3
            "⑤▼6147中枢区画に入る\x01",              # 4
            "⑥▼6150制御终端室に入る\x01",      # 5
            "⑦▼6151３６Ｆに到着する\x01",            # 6
            "⑧▼6152小滴との再会\x01",              # 7
            "⑨▼6153电梯で４０Ｆへ\x01",      # 8
            "⑩▼6157迪塔との対峙\x01",          # 9
            "?▼6158迪塔との対峙（戦\x01",       # 10
            "?▼6161《碧の大樹》が出現する\x01",       # 11
            "?▼6162飛行する梅尔卡瓦６\x01",           # 12
            "?▼6165梅尔卡瓦ＶＳベイオウル\x01",       # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_6DB9"),
        (12, "loc_6DBC"),
        (11, "loc_6DBC"),
        (10, "loc_6DBC"),
        (9, "loc_6DBC"),
        (8, "loc_6DBF"),
        (7, "loc_6DC2"),
        (6, "loc_6DC5"),
        (5, "loc_6DC8"),
        (4, "loc_6DD1"),
        (3, "loc_6DD7"),
        (2, "loc_6DD7"),
        (1, "loc_6DD7"),
        (0, "loc_6DD7"),
        (SWITCH_DEFAULT, "loc_6E75"),
    )


    label("loc_6DB9")

    SetScenarioFlags(0x1A7, 1)

    label("loc_6DBC")

    SetScenarioFlags(0x1A7, 0)

    label("loc_6DBF")

    SetScenarioFlags(0x1A6, 7)

    label("loc_6DC2")

    SetScenarioFlags(0x1A6, 6)

    label("loc_6DC5")

    SetScenarioFlags(0x1A6, 5)

    label("loc_6DC8")

    SetScenarioFlags(0x1A6, 2)
    SetScenarioFlags(0x1A6, 3)
    SetScenarioFlags(0x1A6, 4)

    label("loc_6DD1")

    SetScenarioFlags(0x1A6, 0)
    SetScenarioFlags(0x1A6, 1)

    label("loc_6DD7")

    SetScenarioFlags(0x1A5, 6)
    SetScenarioFlags(0x1A5, 7)
    SetScenarioFlags(0x1A5, 5)
    SetScenarioFlags(0x1A5, 3)
    SetScenarioFlags(0x1A5, 2)
    SetScenarioFlags(0x1A5, 1)
    SetScenarioFlags(0x1A5, 0)
    SetScenarioFlags(0x1A4, 7)
    SetScenarioFlags(0x1A4, 6)
    SetScenarioFlags(0x1A4, 5)
    SetScenarioFlags(0x1A4, 4)
    SetScenarioFlags(0x1A4, 3)
    SetScenarioFlags(0x1A4, 2)
    SetScenarioFlags(0x1A4, 1)
    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E7A")

    label("loc_6E75")

    Jump("loc_6E7A")

    label("loc_6E7A")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71DE")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "诺埃尔と一起\x01",        # 0
            "瓦吉と一起\x01",          # 1
            "莉夏と一起\x01",      # 2
            "达德利と一起\x01",      # 3
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_6F3E"),
        (1, "loc_6F47"),
        (2, "loc_6F50"),
        (3, "loc_6F59"),
        (SWITCH_DEFAULT, "loc_6F62"),
    )


    label("loc_6F3E")

    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_6F62")

    label("loc_6F47")

    AddParty(0x4, 0xF4, 0xFF)
    Jump("loc_6F62")

    label("loc_6F50")

    AddParty(0x5, 0xF4, 0xFF)
    Jump("loc_6F62")

    label("loc_6F59")

    AddParty(0x9, 0xF4, 0xFF)
    Jump("loc_6F62")

    label("loc_6F62")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FBD")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_6FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_700D")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_700D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7059")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_7059")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70A5")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_70A5")

    MenuCmd(0x2, 0x2, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x4)
    OP_60(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70FF")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_70DF"),
        (1, "loc_70E8"),
        (2, "loc_70F1"),
        (SWITCH_DEFAULT, "loc_70FA"),
    )


    label("loc_70DF")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_70FA")

    label("loc_70E8")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_70FA")

    label("loc_70F1")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_70FA")

    label("loc_70FA")

    Jump("loc_71DE")

    label("loc_70FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_714B")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_712B"),
        (1, "loc_7134"),
        (2, "loc_713D"),
        (SWITCH_DEFAULT, "loc_7146"),
    )


    label("loc_712B")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_7146")

    label("loc_7134")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_7146")

    label("loc_713D")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_7146")

    label("loc_7146")

    Jump("loc_71DE")

    label("loc_714B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7197")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_7177"),
        (1, "loc_7180"),
        (2, "loc_7189"),
        (SWITCH_DEFAULT, "loc_7192"),
    )


    label("loc_7177")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_7192")

    label("loc_7180")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_7192")

    label("loc_7189")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_7192")

    label("loc_7192")

    Jump("loc_71DE")

    label("loc_7197")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71DE")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_71C3"),
        (1, "loc_71CC"),
        (2, "loc_71D5"),
        (SWITCH_DEFAULT, "loc_71DE"),
    )


    label("loc_71C3")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_71DE")

    label("loc_71CC")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_71DE")

    label("loc_71D5")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_71DE")

    label("loc_71DE")

    OP_CE(0x1)
    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7241"),
        (1, "loc_7252"),
        (2, "loc_7280"),
        (3, "loc_729A"),
        (4, "loc_72AB"),
        (5, "loc_72C3"),
        (6, "loc_72D1"),
        (7, "loc_72E4"),
        (8, "loc_72F2"),
        (9, "loc_7305"),
        (10, "loc_7313"),
        (11, "loc_7324"),
        (12, "loc_7335"),
        (13, "loc_7367"),
        (SWITCH_DEFAULT, "loc_7378"),
    )


    label("loc_7241")

    SetScenarioFlags(0x22, 2)
    NewScene("c1100", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7252")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 4)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7280")

    SetScenarioFlags(0x22, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4212", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_729A")

    SetScenarioFlags(0x22, 1)
    NewScene("c1510", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_72AB")

    OP_BA(0x97, 0x0)
    OP_BA(0x160, 0x0)
    NewScene("c1580", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_72C3")

    NewScene("c1583", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_72D1")

    OP_BA(0x97, 0x160)
    NewScene("c1550", 107, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_72E4")

    NewScene("c1550", 118, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_72F2")

    OP_BA(0x97, 0x160)
    NewScene("c1520", 103, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7305")

    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7313")

    SetScenarioFlags(0x23, 2)
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7324")

    SetScenarioFlags(0x23, 3)
    NewScene("c1600", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7335")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 6)
    NewScene("e4300", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7367")

    SetScenarioFlags(0x23, 7)
    NewScene("e4320", 0, 0, 0)
    OP_07()
    Jump("loc_7387")

    label("loc_7378")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7387")

    label("loc_7387")

    Jump("loc_6BA5")

    label("loc_738C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_27_6B86 end


    label("Function_28_739A")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B65")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6172《神域》への到着\x01",            # 0
            "②▼6173中間地点に到達する\x01",          # 1
            "③▼6176象の領域に入る\x01",              # 2
            "④▼6177瓦鲁德との最終決戦\x01",        # 3
            "⑤▼6178瓦鲁德との最終決戦（\x01",      # 4
            "⑥▼6183色の領域に入る\x01",              # 5
            "⑦▼6186谢莉との最終決戦\x01",      # 6
            "⑧▼6187谢莉との最終決戦\x01",      # 7
            "⑨▼6191谢莉の独り言\x01",          # 8
            "⑩▼6193業の領域への入口を発見\x01",      # 9
            "?▼6194業の領域に入る\x01",               # 10
            "?▼6195西格蒙特との最終決戦\x01",       # 11
            "?▼6196西格蒙特との最終決戦\x01",       # 12
            "?▼6200戒の領域への入口を発見\x01",       # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_75C3"),
        (12, "loc_75C9"),
        (11, "loc_75C9"),
        (10, "loc_75CC"),
        (9, "loc_75CF"),
        (8, "loc_75D2"),
        (7, "loc_75D5"),
        (6, "loc_75D5"),
        (5, "loc_75DB"),
        (4, "loc_75E1"),
        (3, "loc_75E1"),
        (2, "loc_75E4"),
        (1, "loc_75F6"),
        (0, "loc_75F9"),
        (SWITCH_DEFAULT, "loc_76B5"),
    )


    label("loc_75C3")

    SetScenarioFlags(0x1A9, 1)
    SetScenarioFlags(0x1A9, 0)

    label("loc_75C9")

    SetScenarioFlags(0x1A8, 7)

    label("loc_75CC")

    SetScenarioFlags(0x1A8, 6)

    label("loc_75CF")

    SetScenarioFlags(0x1A8, 5)

    label("loc_75D2")

    SetScenarioFlags(0x1A8, 3)

    label("loc_75D5")

    SetScenarioFlags(0x1A8, 1)
    SetScenarioFlags(0x1A8, 2)

    label("loc_75DB")

    SetScenarioFlags(0x1A7, 7)
    SetScenarioFlags(0x1A8, 0)

    label("loc_75E1")

    SetScenarioFlags(0x1A7, 6)

    label("loc_75E4")

    SetScenarioFlags(0x1A7, 3)
    SetScenarioFlags(0x1A7, 4)
    SetScenarioFlags(0x1A7, 5)
    SetScenarioFlags(0x1AA, 0)
    SetScenarioFlags(0x1AA, 1)
    SetScenarioFlags(0x1AA, 2)

    label("loc_75F6")

    SetScenarioFlags(0x1A7, 2)

    label("loc_75F9")

    SetScenarioFlags(0x1A7, 1)
    SetScenarioFlags(0x1A7, 0)
    SetScenarioFlags(0x1A6, 7)
    SetScenarioFlags(0x1A6, 6)
    SetScenarioFlags(0x1A6, 5)
    SetScenarioFlags(0x1A6, 2)
    SetScenarioFlags(0x1A6, 3)
    SetScenarioFlags(0x1A6, 4)
    SetScenarioFlags(0x1A6, 0)
    SetScenarioFlags(0x1A6, 1)
    SetScenarioFlags(0x1A5, 6)
    SetScenarioFlags(0x1A5, 7)
    SetScenarioFlags(0x1A5, 5)
    SetScenarioFlags(0x1A5, 3)
    SetScenarioFlags(0x1A5, 2)
    SetScenarioFlags(0x1A5, 1)
    SetScenarioFlags(0x1A5, 0)
    SetScenarioFlags(0x1A4, 7)
    SetScenarioFlags(0x1A4, 6)
    SetScenarioFlags(0x1A4, 5)
    SetScenarioFlags(0x1A4, 4)
    SetScenarioFlags(0x1A4, 3)
    SetScenarioFlags(0x1A4, 2)
    SetScenarioFlags(0x1A4, 1)
    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_76BA")

    label("loc_76B5")

    Jump("loc_76BA")

    label("loc_76BA")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A1E")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "诺埃尔と一起\x01",        # 0
            "瓦吉と一起\x01",          # 1
            "莉夏と一起\x01",      # 2
            "达德利と一起\x01",      # 3
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_777E"),
        (1, "loc_7787"),
        (2, "loc_7790"),
        (3, "loc_7799"),
        (SWITCH_DEFAULT, "loc_77A2"),
    )


    label("loc_777E")

    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_77A2")

    label("loc_7787")

    AddParty(0x4, 0xF4, 0xFF)
    Jump("loc_77A2")

    label("loc_7790")

    AddParty(0x5, 0xF4, 0xFF)
    Jump("loc_77A2")

    label("loc_7799")

    AddParty(0x9, 0xF4, 0xFF)
    Jump("loc_77A2")

    label("loc_77A2")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77FD")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_77FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_784D")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_784D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7899")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_7899")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78E5")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_78E5")

    MenuCmd(0x2, 0x2, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x4)
    OP_60(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_793F")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_791F"),
        (1, "loc_7928"),
        (2, "loc_7931"),
        (SWITCH_DEFAULT, "loc_793A"),
    )


    label("loc_791F")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_793A")

    label("loc_7928")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_793A")

    label("loc_7931")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_793A")

    label("loc_793A")

    Jump("loc_7A1E")

    label("loc_793F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_798B")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_796B"),
        (1, "loc_7974"),
        (2, "loc_797D"),
        (SWITCH_DEFAULT, "loc_7986"),
    )


    label("loc_796B")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_7986")

    label("loc_7974")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_7986")

    label("loc_797D")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_7986")

    label("loc_7986")

    Jump("loc_7A1E")

    label("loc_798B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79D7")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_79B7"),
        (1, "loc_79C0"),
        (2, "loc_79C9"),
        (SWITCH_DEFAULT, "loc_79D2"),
    )


    label("loc_79B7")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_79D2")

    label("loc_79C0")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_79D2")

    label("loc_79C9")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_79D2")

    label("loc_79D2")

    Jump("loc_7A1E")

    label("loc_79D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A1E")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_7A03"),
        (1, "loc_7A0C"),
        (2, "loc_7A15"),
        (SWITCH_DEFAULT, "loc_7A1E"),
    )


    label("loc_7A03")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_7A1E")

    label("loc_7A0C")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_7A1E")

    label("loc_7A15")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_7A1E")

    label("loc_7A1E")

    OP_CE(0x1)
    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7A81"),
        (1, "loc_7A92"),
        (2, "loc_7AA0"),
        (3, "loc_7AAE"),
        (4, "loc_7ABC"),
        (5, "loc_7ACD"),
        (6, "loc_7ADB"),
        (7, "loc_7AE9"),
        (8, "loc_7AFA"),
        (9, "loc_7B08"),
        (10, "loc_7B16"),
        (11, "loc_7B24"),
        (12, "loc_7B32"),
        (13, "loc_7B43"),
        (SWITCH_DEFAULT, "loc_7B51"),
    )


    label("loc_7A81")

    SetScenarioFlags(0x22, 0)
    NewScene("m9000", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7A92")

    NewScene("m9002", 103, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7AA0")

    NewScene("m9060", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7AAE")

    NewScene("m9062", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7ABC")

    SetScenarioFlags(0x22, 0)
    NewScene("m9062", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7ACD")

    NewScene("m9050", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7ADB")

    NewScene("m9052", 100, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7AE9")

    SetScenarioFlags(0x22, 0)
    NewScene("m9052", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7AFA")

    NewScene("m9052", 100, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7B08")

    NewScene("m9005", 105, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7B16")

    NewScene("m9070", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7B24")

    NewScene("m9072", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7B32")

    SetScenarioFlags(0x22, 0)
    NewScene("m9072", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7B43")

    NewScene("m9008", 0, 0, 0)
    OP_07()
    Jump("loc_7B60")

    label("loc_7B51")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B60")

    label("loc_7B60")

    Jump("loc_73B9")

    label("loc_7B65")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_28_739A end


    label("Function_29_7B73")

    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82E2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼6201戒の領域に入る\x01",              # 0
            "②▼6202亚里欧斯との最終決戦\x01",        # 1
            "③▼6203亚里欧斯との最終決戦（\x01",      # 2
            "④▼6207昇降機前選択肢\x01",              # 3
            "⑤▼6210贝尔との戦い\x01",          # 4
            "⑥▼6211《碧のデミウルゴス》と\x01",      # 5
            "⑦▼6212《碧のデミウルゴス》と\x01",      # 6
            "⑧▼6213零の世界\x01",                    # 7
            "⑨▼6215罗伊德归来\x01",            # 8
            "⑩▼0000\x01",                            # 9
            "?▼0000\x01",                             # 10
            "?▼0000\x01",                             # 11
            "?▼0000\x01",                             # 12
            "?▼0000　　　　　　　　　　　\x01",       # 13
            "Cancel\x01",                          # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_7D42"),
        (12, "loc_7D42"),
        (11, "loc_7D42"),
        (10, "loc_7D42"),
        (9, "loc_7D42"),
        (8, "loc_7D42"),
        (7, "loc_7D42"),
        (6, "loc_7D42"),
        (5, "loc_7D42"),
        (4, "loc_7D42"),
        (3, "loc_7D45"),
        (2, "loc_7D4B"),
        (1, "loc_7D4B"),
        (0, "loc_7D4E"),
        (SWITCH_DEFAULT, "loc_7E43"),
    )


    label("loc_7D42")

    SetScenarioFlags(0x1A9, 6)

    label("loc_7D45")

    SetScenarioFlags(0x1A9, 4)
    SetScenarioFlags(0x1A9, 5)

    label("loc_7D4B")

    SetScenarioFlags(0x1A9, 3)

    label("loc_7D4E")

    SetScenarioFlags(0x1A9, 2)
    SetScenarioFlags(0x1A9, 0)
    SetScenarioFlags(0x1A9, 1)
    SetScenarioFlags(0x1A8, 7)
    SetScenarioFlags(0x1A8, 6)
    SetScenarioFlags(0x1A8, 5)
    SetScenarioFlags(0x1A8, 3)
    SetScenarioFlags(0x1A8, 1)
    SetScenarioFlags(0x1A8, 2)
    SetScenarioFlags(0x1A7, 7)
    SetScenarioFlags(0x1A8, 0)
    SetScenarioFlags(0x1A7, 6)
    SetScenarioFlags(0x1AA, 0)
    SetScenarioFlags(0x1AA, 1)
    SetScenarioFlags(0x1AA, 2)
    SetScenarioFlags(0x1A7, 3)
    SetScenarioFlags(0x1A7, 4)
    SetScenarioFlags(0x1A7, 5)
    SetScenarioFlags(0x1A7, 2)
    SetScenarioFlags(0x1A7, 1)
    SetScenarioFlags(0x1A7, 0)
    SetScenarioFlags(0x1A6, 7)
    SetScenarioFlags(0x1A6, 6)
    SetScenarioFlags(0x1A6, 5)
    SetScenarioFlags(0x1A6, 2)
    SetScenarioFlags(0x1A6, 3)
    SetScenarioFlags(0x1A6, 4)
    SetScenarioFlags(0x1A6, 0)
    SetScenarioFlags(0x1A6, 1)
    SetScenarioFlags(0x1A5, 6)
    SetScenarioFlags(0x1A5, 7)
    SetScenarioFlags(0x1A5, 5)
    SetScenarioFlags(0x1A5, 3)
    SetScenarioFlags(0x1A5, 2)
    SetScenarioFlags(0x1A5, 1)
    SetScenarioFlags(0x1A5, 0)
    SetScenarioFlags(0x1A4, 7)
    SetScenarioFlags(0x1A4, 6)
    SetScenarioFlags(0x1A4, 5)
    SetScenarioFlags(0x1A4, 4)
    SetScenarioFlags(0x1A4, 3)
    SetScenarioFlags(0x1A4, 2)
    SetScenarioFlags(0x1A4, 1)
    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E48")

    label("loc_7E43")

    Jump("loc_7E48")

    label("loc_7E48")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81BC")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "诺埃尔と一起\x01",        # 0
            "瓦吉と一起\x01",          # 1
            "莉夏と一起\x01",      # 2
            "达德利と一起\x01",      # 3
        )
    )

    MenuEnd(0x4)
    OP_60(0x2)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_7F0C"),
        (1, "loc_7F15"),
        (2, "loc_7F26"),
        (3, "loc_7F37"),
        (SWITCH_DEFAULT, "loc_7F40"),
    )


    label("loc_7F0C")

    AddParty(0x8, 0xF4, 0xFF)
    Jump("loc_7F40")

    label("loc_7F15")

    AddParty(0x4, 0xF4, 0xFF)
    SetChrChipPat(0x4, 0x1, 0x1F)
    LoadChrChipPat()
    Jump("loc_7F40")

    label("loc_7F26")

    AddParty(0x5, 0xF4, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    Jump("loc_7F40")

    label("loc_7F37")

    AddParty(0x9, 0xF4, 0xFF)
    Jump("loc_7F40")

    label("loc_7F40")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0x0, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F9B")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_7F9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FEB")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_7FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8037")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "达德利と一起")

    label("loc_8037")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8083")
    MenuCmd(0x1, 0x2, "诺埃尔と一起")
    MenuCmd(0x1, 0x2, "瓦吉と一起")
    MenuCmd(0x1, 0x2, "莉夏と一起")

    label("loc_8083")

    MenuCmd(0x2, 0x2, 0xFFFF, 0xFFFF, 0x0)
    MenuEnd(0x4)
    OP_60(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80DD")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_80BD"),
        (1, "loc_80C6"),
        (2, "loc_80CF"),
        (SWITCH_DEFAULT, "loc_80D8"),
    )


    label("loc_80BD")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_80D8")

    label("loc_80C6")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_80D8")

    label("loc_80CF")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_80D8")

    label("loc_80D8")

    Jump("loc_81BC")

    label("loc_80DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8129")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_8109"),
        (1, "loc_8112"),
        (2, "loc_811B"),
        (SWITCH_DEFAULT, "loc_8124"),
    )


    label("loc_8109")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_8124")

    label("loc_8112")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_8124")

    label("loc_811B")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_8124")

    label("loc_8124")

    Jump("loc_81BC")

    label("loc_8129")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8175")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_8155"),
        (1, "loc_815E"),
        (2, "loc_8167"),
        (SWITCH_DEFAULT, "loc_8170"),
    )


    label("loc_8155")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_8170")

    label("loc_815E")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_8170")

    label("loc_8167")

    AddParty(0x9, 0xF5, 0xFF)
    Jump("loc_8170")

    label("loc_8170")

    Jump("loc_81BC")

    label("loc_8175")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81BC")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_81A1"),
        (1, "loc_81AA"),
        (2, "loc_81B3"),
        (SWITCH_DEFAULT, "loc_81BC"),
    )


    label("loc_81A1")

    AddParty(0x8, 0xF5, 0xFF)
    Jump("loc_81BC")

    label("loc_81AA")

    AddParty(0x4, 0xF5, 0xFF)
    Jump("loc_81BC")

    label("loc_81B3")

    AddParty(0x5, 0xF5, 0xFF)
    Jump("loc_81BC")

    label("loc_81BC")

    OP_CE(0x1)
    Call(2, 21)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_821F"),
        (1, "loc_822D"),
        (2, "loc_823B"),
        (3, "loc_824C"),
        (4, "loc_825A"),
        (5, "loc_8268"),
        (6, "loc_8279"),
        (7, "loc_828A"),
        (8, "loc_829B"),
        (9, "loc_82B5"),
        (10, "loc_82BA"),
        (11, "loc_82BF"),
        (12, "loc_82C4"),
        (13, "loc_82C9"),
        (SWITCH_DEFAULT, "loc_82CE"),
    )


    label("loc_821F")

    NewScene("m9080", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_822D")

    NewScene("m9082", 100, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_823B")

    SetScenarioFlags(0x22, 0)
    NewScene("m9082", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_824C")

    NewScene("m9008", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_825A")

    NewScene("m9012", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_8268")

    SetScenarioFlags(0x22, 0)
    NewScene("m9012", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_8279")

    SetScenarioFlags(0x22, 1)
    NewScene("m9012", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_828A")

    SetScenarioFlags(0x22, 0)
    NewScene("m9013", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_829B")

    SetScenarioFlags(0x22, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x245), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m9012", 0, 0, 0)
    OP_07()
    Jump("loc_82DD")

    label("loc_82B5")

    Jump("loc_82DD")

    label("loc_82BA")

    Jump("loc_82DD")

    label("loc_82BF")

    Jump("loc_82DD")

    label("loc_82C4")

    Jump("loc_82DD")

    label("loc_82C9")

    Jump("loc_82DD")

    label("loc_82CE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_82DD")

    label("loc_82DD")

    Jump("loc_7B92")

    label("loc_82E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_29_7B73 end


    label("Function_30_82F0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_82FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8543")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼艾莉との最終絆event\x01",        # 0
            "②▼缇欧との最終絆event\x01",        # 1
            "③▼兰迪との最終絆event\x01",      # 2
            "④▼诺埃尔との最終絆event\x01",        # 3
            "⑤▼瓦吉との最終絆event\x01",          # 4
            "⑥▼莉夏との最終絆event\x01",      # 5
            "Cancel\x01",                          # 6
        )
    )

    MenuEnd(0x0)
    Call(2, 32)
    Call(2, 33)
    Call(2, 34)
    Call(2, 35)
    Call(2, 36)
    Call(2, 37)
    Call(2, 38)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x20, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1A5, 2)
    SetScenarioFlags(0x1A5, 1)
    SetScenarioFlags(0x1A5, 0)
    SetScenarioFlags(0x1A4, 7)
    SetScenarioFlags(0x1A4, 6)
    SetScenarioFlags(0x1A4, 5)
    SetScenarioFlags(0x1A4, 4)
    SetScenarioFlags(0x1A4, 3)
    SetScenarioFlags(0x1A4, 2)
    SetScenarioFlags(0x1A4, 1)
    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    ClearScenarioFlags(0x1AA, 3)
    ClearScenarioFlags(0x1AA, 4)
    ClearScenarioFlags(0x1AA, 5)
    ClearScenarioFlags(0x1AA, 6)
    ClearScenarioFlags(0x1AA, 7)
    ClearScenarioFlags(0x1AB, 0)
    ClearScenarioFlags(0x1AB, 1)
    ClearScenarioFlags(0x1AB, 2)
    ClearScenarioFlags(0x1AB, 3)
    ClearScenarioFlags(0x1AB, 4)
    ClearScenarioFlags(0x1AB, 5)
    ClearScenarioFlags(0x1AB, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_84C9"),
        (1, "loc_84DA"),
        (2, "loc_84EB"),
        (3, "loc_84FC"),
        (4, "loc_850D"),
        (5, "loc_851E"),
        (SWITCH_DEFAULT, "loc_852F"),
    )


    label("loc_84C9")

    SetScenarioFlags(0x1AA, 3)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_853E")

    label("loc_84DA")

    SetScenarioFlags(0x1AA, 4)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_853E")

    label("loc_84EB")

    SetScenarioFlags(0x1AA, 5)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_853E")

    label("loc_84FC")

    SetScenarioFlags(0x1AA, 6)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_853E")

    label("loc_850D")

    SetScenarioFlags(0x1AA, 7)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_853E")

    label("loc_851E")

    SetScenarioFlags(0x1AB, 0)
    NewScene("e302B", 0, 0, 0)
    OP_07()
    Jump("loc_853E")

    label("loc_852F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_853E")

    label("loc_853E")

    Jump("loc_82FA")

    label("loc_8543")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_30_82F0 end


    label("Function_31_8551")

    ClearScenarioFlags(0x22, 0)
    ClearScenarioFlags(0x22, 1)
    ClearScenarioFlags(0x22, 2)
    ClearScenarioFlags(0x22, 3)
    ClearScenarioFlags(0x22, 4)
    ClearScenarioFlags(0x22, 5)
    ClearScenarioFlags(0x22, 6)
    ClearScenarioFlags(0x22, 7)
    ClearScenarioFlags(0x23, 1)
    ClearScenarioFlags(0x23, 2)
    ClearScenarioFlags(0x23, 3)
    ClearScenarioFlags(0x23, 4)
    ClearScenarioFlags(0x23, 5)
    ClearScenarioFlags(0x23, 6)
    ClearScenarioFlags(0x23, 7)
    ClearScenarioFlags(0x24, 0)
    ClearScenarioFlags(0x24, 1)
    ClearScenarioFlags(0x24, 2)
    ClearScenarioFlags(0x24, 3)
    ClearScenarioFlags(0x24, 4)
    ClearScenarioFlags(0x24, 5)
    ClearScenarioFlags(0x24, 6)
    ClearScenarioFlags(0x24, 7)
    ClearScenarioFlags(0x25, 0)
    ClearScenarioFlags(0x25, 1)
    Call(2, 40)
    Call(2, 41)
    Call(2, 42)
    Call(2, 43)
    Call(2, 44)
    Call(2, 45)
    Call(2, 46)
    Call(2, 47)
    Return()

    # Function_31_8551 end


    label("Function_32_85B5")

    SetScenarioFlags(0x120, 0)
    SetScenarioFlags(0x120, 1)
    SetScenarioFlags(0x120, 2)
    SetScenarioFlags(0x120, 3)
    SetScenarioFlags(0x120, 4)
    SetScenarioFlags(0x120, 5)
    SetScenarioFlags(0x120, 6)
    SetScenarioFlags(0x120, 7)
    SetScenarioFlags(0x121, 0)
    SetScenarioFlags(0x121, 1)
    SetScenarioFlags(0x25, 2)
    OP_C9(0x1, 0x80)
    Return()

    # Function_32_85B5 end


    label("Function_33_85DD")

    SetScenarioFlags(0x126, 0)
    SetScenarioFlags(0x126, 1)
    SetScenarioFlags(0x126, 2)
    SetScenarioFlags(0x126, 3)
    SetScenarioFlags(0x126, 4)
    SetScenarioFlags(0x126, 5)
    SetScenarioFlags(0x126, 6)
    SetScenarioFlags(0x126, 7)
    SetScenarioFlags(0x127, 0)
    SetScenarioFlags(0x127, 1)
    SetScenarioFlags(0x127, 2)
    SetScenarioFlags(0x127, 3)
    SetScenarioFlags(0x127, 4)
    SetScenarioFlags(0x127, 5)
    SetScenarioFlags(0x127, 6)
    SetScenarioFlags(0x127, 7)
    SetScenarioFlags(0x128, 0)
    SetScenarioFlags(0x128, 1)
    SetScenarioFlags(0x128, 2)
    SetScenarioFlags(0x128, 3)
    SetScenarioFlags(0x128, 4)
    SetScenarioFlags(0x128, 5)
    SetScenarioFlags(0x128, 6)
    SetScenarioFlags(0x128, 7)
    SetScenarioFlags(0x31, 1)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x32, 0)
    SetScenarioFlags(0x32, 4)
    SetScenarioFlags(0x34, 1)
    SetScenarioFlags(0x34, 3)
    SetScenarioFlags(0x35, 0)
    SetScenarioFlags(0x35, 4)
    SetScenarioFlags(0x37, 1)
    SetScenarioFlags(0x37, 3)
    SetScenarioFlags(0x129, 0)
    SetScenarioFlags(0x129, 1)
    SetScenarioFlags(0x129, 2)
    SetScenarioFlags(0x129, 3)
    SetScenarioFlags(0x129, 4)
    SetScenarioFlags(0x129, 5)
    SetScenarioFlags(0x129, 6)
    SetScenarioFlags(0x129, 7)
    SetScenarioFlags(0x12A, 5)
    SetScenarioFlags(0x12A, 0)
    SetScenarioFlags(0x12A, 1)
    SetScenarioFlags(0x12A, 2)
    SetScenarioFlags(0x12A, 3)
    SetScenarioFlags(0x12A, 4)
    Return()

    # Function_33_85DD end


    label("Function_34_8674")

    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x32, 0)
    SetScenarioFlags(0x32, 1)
    SetScenarioFlags(0x32, 2)
    SetScenarioFlags(0x32, 3)
    SetScenarioFlags(0x32, 4)
    SetScenarioFlags(0x32, 5)
    SetScenarioFlags(0x32, 6)
    SetScenarioFlags(0x32, 7)
    SetScenarioFlags(0x33, 0)
    SetScenarioFlags(0x33, 1)
    SetScenarioFlags(0x33, 2)
    SetScenarioFlags(0x33, 3)
    SetScenarioFlags(0x33, 7)
    SetScenarioFlags(0x34, 1)
    SetScenarioFlags(0x34, 2)
    SetScenarioFlags(0x34, 3)
    SetScenarioFlags(0x2F, 6)
    SetScenarioFlags(0x35, 0)
    SetScenarioFlags(0x35, 1)
    SetScenarioFlags(0x35, 2)
    SetScenarioFlags(0x35, 3)
    SetScenarioFlags(0x35, 4)
    SetScenarioFlags(0x35, 5)
    SetScenarioFlags(0x35, 6)
    SetScenarioFlags(0x35, 7)
    SetScenarioFlags(0x36, 0)
    SetScenarioFlags(0x36, 1)
    SetScenarioFlags(0x36, 2)
    SetScenarioFlags(0x36, 3)
    SetScenarioFlags(0x36, 7)
    SetScenarioFlags(0x37, 1)
    SetScenarioFlags(0x37, 2)
    SetScenarioFlags(0x37, 3)
    SetScenarioFlags(0x2F, 7)
    SetScenarioFlags(0x140, 0)
    SetScenarioFlags(0x140, 1)
    SetScenarioFlags(0x140, 2)
    SetScenarioFlags(0x140, 3)
    SetScenarioFlags(0x140, 4)
    SetScenarioFlags(0x140, 5)
    SetScenarioFlags(0x140, 6)
    SetScenarioFlags(0x140, 7)
    SetScenarioFlags(0x141, 0)
    SetScenarioFlags(0x141, 1)
    SetScenarioFlags(0x141, 2)
    SetScenarioFlags(0x141, 3)
    SetScenarioFlags(0x141, 4)
    SetScenarioFlags(0x141, 5)
    SetScenarioFlags(0x141, 6)
    SetScenarioFlags(0x141, 7)
    SetScenarioFlags(0x142, 0)
    SetScenarioFlags(0x142, 1)
    SetScenarioFlags(0x142, 2)
    SetScenarioFlags(0x142, 3)
    SetScenarioFlags(0x142, 4)
    SetScenarioFlags(0x1C4, 4)
    SetScenarioFlags(0x142, 5)
    SetScenarioFlags(0x142, 6)
    SetScenarioFlags(0x142, 7)
    SetScenarioFlags(0x143, 0)
    SetScenarioFlags(0x143, 1)
    SetScenarioFlags(0x143, 2)
    SetScenarioFlags(0x143, 3)
    SetScenarioFlags(0x143, 4)
    SetScenarioFlags(0x143, 5)
    SetScenarioFlags(0x143, 6)
    SetScenarioFlags(0x143, 7)
    SetScenarioFlags(0x146, 3)
    Return()

    # Function_34_8674 end


    label("Function_35_874A")

    SetScenarioFlags(0x144, 0)
    SetScenarioFlags(0x144, 1)
    SetScenarioFlags(0x144, 2)
    SetScenarioFlags(0x144, 3)
    SetScenarioFlags(0x144, 4)
    SetScenarioFlags(0x144, 5)
    SetScenarioFlags(0x144, 6)
    SetScenarioFlags(0x144, 7)
    SetScenarioFlags(0x145, 0)
    SetScenarioFlags(0x145, 1)
    SetScenarioFlags(0x145, 2)
    SetScenarioFlags(0x145, 3)
    SetScenarioFlags(0x145, 4)
    SetScenarioFlags(0x145, 5)
    SetScenarioFlags(0x145, 6)
    SetScenarioFlags(0x145, 7)
    SetScenarioFlags(0x146, 0)
    SetScenarioFlags(0x146, 1)
    SetScenarioFlags(0x146, 2)
    Return()

    # Function_35_874A end


    label("Function_36_8784")

    SetScenarioFlags(0x160, 0)
    SetScenarioFlags(0x160, 1)
    SetScenarioFlags(0x160, 2)
    SetScenarioFlags(0x160, 3)
    SetScenarioFlags(0x160, 4)
    SetScenarioFlags(0x160, 5)
    SetScenarioFlags(0x160, 6)
    SetScenarioFlags(0x160, 7)
    SetScenarioFlags(0x161, 0)
    SetScenarioFlags(0x161, 1)
    SetScenarioFlags(0x161, 2)
    SetScenarioFlags(0x161, 3)
    SetScenarioFlags(0x161, 4)
    SetScenarioFlags(0x161, 5)
    SetScenarioFlags(0x161, 6)
    SetScenarioFlags(0x161, 7)
    SetScenarioFlags(0x162, 0)
    SetScenarioFlags(0x162, 1)
    SetScenarioFlags(0x162, 2)
    SetScenarioFlags(0x162, 3)
    SetScenarioFlags(0x162, 4)
    SetScenarioFlags(0x162, 5)
    SetScenarioFlags(0x162, 6)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x163, 0)
    SetScenarioFlags(0x163, 1)
    SetScenarioFlags(0x163, 2)
    SetScenarioFlags(0x163, 3)
    SetScenarioFlags(0x163, 4)
    SetScenarioFlags(0x163, 5)
    SetScenarioFlags(0x163, 6)
    SetScenarioFlags(0x163, 7)
    SetScenarioFlags(0x164, 0)
    SetScenarioFlags(0x168, 2)
    SetScenarioFlags(0x164, 1)
    SetScenarioFlags(0x164, 2)
    SetScenarioFlags(0x164, 3)
    SetScenarioFlags(0x164, 4)
    SetScenarioFlags(0x164, 5)
    SetScenarioFlags(0x164, 6)
    SetScenarioFlags(0x164, 7)
    SetScenarioFlags(0x165, 0)
    SetScenarioFlags(0x165, 1)
    SetScenarioFlags(0x165, 2)
    SetScenarioFlags(0x165, 3)
    SetScenarioFlags(0x165, 4)
    SetScenarioFlags(0x165, 5)
    SetScenarioFlags(0x165, 6)
    SetScenarioFlags(0x165, 7)
    SetScenarioFlags(0x166, 0)
    SetScenarioFlags(0x166, 1)
    SetScenarioFlags(0x166, 2)
    SetScenarioFlags(0x166, 3)
    SetScenarioFlags(0x166, 4)
    SetScenarioFlags(0x166, 5)
    SetScenarioFlags(0x166, 6)
    SetScenarioFlags(0x166, 7)
    SetScenarioFlags(0x168, 0)
    SetScenarioFlags(0x168, 1)
    SetScenarioFlags(0x168, 3)
    SetScenarioFlags(0x168, 4)
    Return()

    # Function_36_8784 end


    label("Function_37_883C")

    SetScenarioFlags(0x180, 0)
    SetScenarioFlags(0x180, 1)
    SetScenarioFlags(0x180, 2)
    SetScenarioFlags(0x180, 3)
    SetScenarioFlags(0x180, 4)
    SetScenarioFlags(0x180, 5)
    SetScenarioFlags(0x180, 6)
    SetScenarioFlags(0x180, 7)
    SetScenarioFlags(0x181, 0)
    SetScenarioFlags(0x181, 1)
    SetScenarioFlags(0x181, 2)
    SetScenarioFlags(0x181, 3)
    SetScenarioFlags(0x181, 4)
    SetScenarioFlags(0x181, 5)
    SetScenarioFlags(0x181, 6)
    SetScenarioFlags(0x181, 7)
    SetScenarioFlags(0x182, 0)
    SetScenarioFlags(0x182, 1)
    SetScenarioFlags(0x182, 2)
    SetScenarioFlags(0x182, 3)
    SetScenarioFlags(0x182, 4)
    SetScenarioFlags(0x182, 5)
    SetScenarioFlags(0x182, 6)
    SetScenarioFlags(0x182, 7)
    SetScenarioFlags(0x183, 0)
    SetScenarioFlags(0x183, 1)
    SetScenarioFlags(0x183, 2)
    SetScenarioFlags(0x183, 3)
    Return()

    # Function_37_883C end


    label("Function_38_8891")

    SetScenarioFlags(0x183, 4)
    SetScenarioFlags(0x183, 5)
    SetScenarioFlags(0x183, 6)
    SetScenarioFlags(0x183, 7)
    SetScenarioFlags(0x184, 0)
    SetScenarioFlags(0x184, 1)
    SetScenarioFlags(0x184, 2)
    SetScenarioFlags(0x184, 3)
    SetScenarioFlags(0x184, 4)
    Return()

    # Function_38_8891 end


    label("Function_39_88AD")

    SetScenarioFlags(0x20, 5)
    SetScenarioFlags(0x1A0, 0)
    SetScenarioFlags(0x1A0, 1)
    SetScenarioFlags(0x1A0, 2)
    SetScenarioFlags(0x1A0, 3)
    SetScenarioFlags(0x1A0, 4)
    SetScenarioFlags(0x1A0, 5)
    SetScenarioFlags(0x1A0, 6)
    SetScenarioFlags(0x1A0, 7)
    SetScenarioFlags(0x1A1, 0)
    SetScenarioFlags(0x1A1, 1)
    SetScenarioFlags(0x1A1, 2)
    SetScenarioFlags(0x1A1, 3)
    SetScenarioFlags(0x1A1, 4)
    SetScenarioFlags(0x1A1, 5)
    SetScenarioFlags(0x1A1, 6)
    SetScenarioFlags(0x1A1, 7)
    SetScenarioFlags(0x1A2, 0)
    SetScenarioFlags(0x1A2, 1)
    SetScenarioFlags(0x1A2, 2)
    SetScenarioFlags(0x1A2, 3)
    SetScenarioFlags(0x1A2, 4)
    SetScenarioFlags(0x1A2, 5)
    SetScenarioFlags(0x1A2, 6)
    SetScenarioFlags(0x1A2, 7)
    SetScenarioFlags(0x1A3, 0)
    SetScenarioFlags(0x1A3, 1)
    SetScenarioFlags(0x1A3, 2)
    SetScenarioFlags(0x1A3, 3)
    SetScenarioFlags(0x1A3, 4)
    SetScenarioFlags(0x1A3, 5)
    SetScenarioFlags(0x1A3, 6)
    SetScenarioFlags(0x1A3, 7)
    SetScenarioFlags(0x1A4, 0)
    SetScenarioFlags(0x1A4, 1)
    SetScenarioFlags(0x1A4, 2)
    SetScenarioFlags(0x1A4, 3)
    SetScenarioFlags(0x1A4, 4)
    SetScenarioFlags(0x1A4, 5)
    SetScenarioFlags(0x1A4, 6)
    SetScenarioFlags(0x1A4, 7)
    SetScenarioFlags(0x1A5, 0)
    SetScenarioFlags(0x1A5, 1)
    SetScenarioFlags(0x1A5, 2)
    SetScenarioFlags(0x1A5, 3)
    SetScenarioFlags(0x1A5, 5)
    SetScenarioFlags(0x1A5, 6)
    SetScenarioFlags(0x1A5, 7)
    SetScenarioFlags(0x1A6, 0)
    SetScenarioFlags(0x1A6, 1)
    SetScenarioFlags(0x1A6, 2)
    SetScenarioFlags(0x1A6, 3)
    SetScenarioFlags(0x1A6, 4)
    SetScenarioFlags(0x1A6, 5)
    SetScenarioFlags(0x1A6, 6)
    SetScenarioFlags(0x1A6, 7)
    SetScenarioFlags(0x1A7, 0)
    SetScenarioFlags(0x1A7, 1)
    SetScenarioFlags(0x1A7, 2)
    SetScenarioFlags(0x1A7, 3)
    SetScenarioFlags(0x1A7, 4)
    SetScenarioFlags(0x1A7, 5)
    SetScenarioFlags(0x1A7, 6)
    SetScenarioFlags(0x1A7, 7)
    SetScenarioFlags(0x1A8, 0)
    SetScenarioFlags(0x1A8, 1)
    SetScenarioFlags(0x1A8, 2)
    SetScenarioFlags(0x1A8, 3)
    SetScenarioFlags(0x1A8, 4)
    SetScenarioFlags(0x1A8, 5)
    SetScenarioFlags(0x1A8, 6)
    SetScenarioFlags(0x1A8, 7)
    SetScenarioFlags(0x1A9, 0)
    SetScenarioFlags(0x1A9, 1)
    SetScenarioFlags(0x1A9, 2)
    SetScenarioFlags(0x1A9, 3)
    SetScenarioFlags(0x1A9, 4)
    SetScenarioFlags(0x1A9, 5)
    SetScenarioFlags(0x1A9, 6)
    SetScenarioFlags(0x1AB, 7)
    Return()

    # Function_39_88AD end


    label("Function_40_899E")

    ClearScenarioFlags(0x120, 0)
    ClearScenarioFlags(0x120, 1)
    ClearScenarioFlags(0x120, 2)
    ClearScenarioFlags(0x120, 3)
    ClearScenarioFlags(0x120, 4)
    ClearScenarioFlags(0x120, 5)
    ClearScenarioFlags(0x120, 6)
    ClearScenarioFlags(0x120, 7)
    ClearScenarioFlags(0x121, 0)
    ClearScenarioFlags(0x121, 1)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x20, 5)
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
    ClearScenarioFlags(0x31, 1)
    Return()

    # Function_40_899E end


    label("Function_41_8A6E")

    ClearScenarioFlags(0x126, 0)
    ClearScenarioFlags(0x126, 1)
    ClearScenarioFlags(0x126, 2)
    ClearScenarioFlags(0x126, 3)
    ClearScenarioFlags(0x126, 4)
    ClearScenarioFlags(0x126, 5)
    ClearScenarioFlags(0x126, 6)
    ClearScenarioFlags(0x126, 7)
    ClearScenarioFlags(0x127, 0)
    ClearScenarioFlags(0x127, 1)
    ClearScenarioFlags(0x127, 2)
    ClearScenarioFlags(0x127, 3)
    ClearScenarioFlags(0x127, 4)
    ClearScenarioFlags(0x127, 5)
    ClearScenarioFlags(0x127, 6)
    ClearScenarioFlags(0x127, 7)
    ClearScenarioFlags(0x128, 0)
    ClearScenarioFlags(0x128, 1)
    ClearScenarioFlags(0x128, 2)
    ClearScenarioFlags(0x128, 3)
    ClearScenarioFlags(0x128, 4)
    ClearScenarioFlags(0x128, 5)
    ClearScenarioFlags(0x128, 6)
    ClearScenarioFlags(0x128, 7)
    ClearScenarioFlags(0x31, 1)
    ClearScenarioFlags(0x129, 0)
    ClearScenarioFlags(0x129, 1)
    ClearScenarioFlags(0x129, 2)
    ClearScenarioFlags(0x129, 3)
    ClearScenarioFlags(0x129, 4)
    ClearScenarioFlags(0x129, 5)
    ClearScenarioFlags(0x129, 6)
    ClearScenarioFlags(0x129, 7)
    ClearScenarioFlags(0x12A, 0)
    ClearScenarioFlags(0x12A, 1)
    ClearScenarioFlags(0x12A, 2)
    ClearScenarioFlags(0x12A, 3)
    ClearScenarioFlags(0x12A, 4)
    Return()

    # Function_41_8A6E end


    label("Function_42_8AE1")

    ClearScenarioFlags(0x140, 0)
    ClearScenarioFlags(0x140, 1)
    ClearScenarioFlags(0x140, 2)
    ClearScenarioFlags(0x140, 3)
    ClearScenarioFlags(0x140, 4)
    ClearScenarioFlags(0x140, 5)
    ClearScenarioFlags(0x140, 6)
    ClearScenarioFlags(0x140, 7)
    ClearScenarioFlags(0x141, 0)
    ClearScenarioFlags(0x141, 1)
    ClearScenarioFlags(0x141, 2)
    ClearScenarioFlags(0x141, 3)
    ClearScenarioFlags(0x141, 4)
    ClearScenarioFlags(0x141, 5)
    ClearScenarioFlags(0x141, 6)
    ClearScenarioFlags(0x141, 7)
    ClearScenarioFlags(0x142, 0)
    ClearScenarioFlags(0x142, 1)
    ClearScenarioFlags(0x142, 2)
    ClearScenarioFlags(0x142, 3)
    ClearScenarioFlags(0x142, 4)
    ClearScenarioFlags(0x1C4, 4)
    ClearScenarioFlags(0x142, 5)
    ClearScenarioFlags(0x142, 6)
    ClearScenarioFlags(0x142, 7)
    ClearScenarioFlags(0x143, 0)
    ClearScenarioFlags(0x143, 1)
    ClearScenarioFlags(0x143, 2)
    ClearScenarioFlags(0x143, 3)
    ClearScenarioFlags(0x143, 4)
    ClearScenarioFlags(0x143, 5)
    ClearScenarioFlags(0x143, 6)
    ClearScenarioFlags(0x143, 7)
    ClearScenarioFlags(0x146, 3)
    Return()

    # Function_42_8AE1 end


    label("Function_43_8B48")

    ClearScenarioFlags(0x144, 0)
    ClearScenarioFlags(0x144, 1)
    ClearScenarioFlags(0x144, 2)
    ClearScenarioFlags(0x144, 3)
    ClearScenarioFlags(0x144, 4)
    ClearScenarioFlags(0x144, 5)
    ClearScenarioFlags(0x144, 6)
    ClearScenarioFlags(0x144, 7)
    ClearScenarioFlags(0x145, 0)
    ClearScenarioFlags(0x145, 1)
    ClearScenarioFlags(0x145, 2)
    ClearScenarioFlags(0x145, 3)
    ClearScenarioFlags(0x145, 4)
    ClearScenarioFlags(0x145, 5)
    ClearScenarioFlags(0x145, 6)
    ClearScenarioFlags(0x145, 7)
    ClearScenarioFlags(0x146, 0)
    ClearScenarioFlags(0x146, 1)
    ClearScenarioFlags(0x146, 2)
    Return()

    # Function_43_8B48 end


    label("Function_44_8B82")

    ClearScenarioFlags(0x160, 0)
    ClearScenarioFlags(0x160, 1)
    ClearScenarioFlags(0x160, 2)
    ClearScenarioFlags(0x160, 3)
    ClearScenarioFlags(0x160, 4)
    ClearScenarioFlags(0x160, 5)
    ClearScenarioFlags(0x160, 6)
    ClearScenarioFlags(0x160, 7)
    ClearScenarioFlags(0x161, 0)
    ClearScenarioFlags(0x161, 1)
    ClearScenarioFlags(0x161, 2)
    ClearScenarioFlags(0x161, 3)
    ClearScenarioFlags(0x161, 4)
    ClearScenarioFlags(0x161, 5)
    ClearScenarioFlags(0x161, 6)
    ClearScenarioFlags(0x161, 7)
    ClearScenarioFlags(0x162, 0)
    ClearScenarioFlags(0x162, 1)
    ClearScenarioFlags(0x162, 2)
    ClearScenarioFlags(0x162, 3)
    ClearScenarioFlags(0x162, 4)
    ClearScenarioFlags(0x162, 5)
    ClearScenarioFlags(0x162, 6)
    ClearScenarioFlags(0x162, 7)
    ClearScenarioFlags(0x163, 0)
    ClearScenarioFlags(0x163, 1)
    ClearScenarioFlags(0x163, 2)
    ClearScenarioFlags(0x163, 3)
    ClearScenarioFlags(0x163, 4)
    ClearScenarioFlags(0x163, 5)
    ClearScenarioFlags(0x163, 6)
    ClearScenarioFlags(0x163, 7)
    ClearScenarioFlags(0x164, 0)
    ClearScenarioFlags(0x168, 2)
    ClearScenarioFlags(0x164, 1)
    ClearScenarioFlags(0x164, 2)
    ClearScenarioFlags(0x164, 3)
    ClearScenarioFlags(0x164, 4)
    ClearScenarioFlags(0x164, 5)
    ClearScenarioFlags(0x164, 6)
    ClearScenarioFlags(0x164, 7)
    ClearScenarioFlags(0x165, 0)
    ClearScenarioFlags(0x165, 1)
    ClearScenarioFlags(0x165, 2)
    ClearScenarioFlags(0x165, 3)
    ClearScenarioFlags(0x165, 4)
    ClearScenarioFlags(0x165, 5)
    ClearScenarioFlags(0x165, 6)
    ClearScenarioFlags(0x165, 7)
    ClearScenarioFlags(0x166, 0)
    ClearScenarioFlags(0x166, 1)
    ClearScenarioFlags(0x166, 2)
    ClearScenarioFlags(0x166, 3)
    ClearScenarioFlags(0x166, 4)
    ClearScenarioFlags(0x166, 5)
    ClearScenarioFlags(0x166, 6)
    ClearScenarioFlags(0x166, 7)
    ClearScenarioFlags(0x168, 0)
    ClearScenarioFlags(0x168, 1)
    ClearScenarioFlags(0x168, 3)
    ClearScenarioFlags(0x168, 4)
    Return()

    # Function_44_8B82 end


    label("Function_45_8C3A")

    ClearScenarioFlags(0x180, 0)
    ClearScenarioFlags(0x180, 1)
    ClearScenarioFlags(0x180, 2)
    ClearScenarioFlags(0x180, 3)
    ClearScenarioFlags(0x180, 4)
    ClearScenarioFlags(0x180, 5)
    ClearScenarioFlags(0x180, 6)
    ClearScenarioFlags(0x180, 7)
    ClearScenarioFlags(0x181, 0)
    ClearScenarioFlags(0x181, 1)
    ClearScenarioFlags(0x181, 2)
    ClearScenarioFlags(0x181, 3)
    ClearScenarioFlags(0x181, 4)
    ClearScenarioFlags(0x181, 5)
    ClearScenarioFlags(0x181, 6)
    ClearScenarioFlags(0x181, 7)
    ClearScenarioFlags(0x182, 0)
    ClearScenarioFlags(0x182, 1)
    ClearScenarioFlags(0x182, 2)
    ClearScenarioFlags(0x182, 3)
    ClearScenarioFlags(0x182, 4)
    ClearScenarioFlags(0x182, 5)
    ClearScenarioFlags(0x182, 6)
    ClearScenarioFlags(0x182, 7)
    ClearScenarioFlags(0x183, 0)
    ClearScenarioFlags(0x183, 1)
    ClearScenarioFlags(0x183, 2)
    ClearScenarioFlags(0x183, 3)
    Return()

    # Function_45_8C3A end


    label("Function_46_8C8F")

    ClearScenarioFlags(0x183, 4)
    ClearScenarioFlags(0x183, 5)
    ClearScenarioFlags(0x183, 6)
    ClearScenarioFlags(0x183, 7)
    ClearScenarioFlags(0x184, 0)
    ClearScenarioFlags(0x184, 1)
    ClearScenarioFlags(0x184, 2)
    ClearScenarioFlags(0x184, 3)
    ClearScenarioFlags(0x184, 4)
    Return()

    # Function_46_8C8F end


    label("Function_47_8CAB")

    ClearScenarioFlags(0x20, 5)
    ClearScenarioFlags(0x1A0, 0)
    ClearScenarioFlags(0x1A0, 1)
    ClearScenarioFlags(0x1A0, 2)
    ClearScenarioFlags(0x1A0, 3)
    ClearScenarioFlags(0x1A0, 4)
    ClearScenarioFlags(0x1A0, 5)
    ClearScenarioFlags(0x1A0, 6)
    ClearScenarioFlags(0x1A0, 7)
    ClearScenarioFlags(0x1A1, 0)
    ClearScenarioFlags(0x1A1, 1)
    ClearScenarioFlags(0x1A1, 2)
    ClearScenarioFlags(0x1A1, 3)
    ClearScenarioFlags(0x1A1, 4)
    ClearScenarioFlags(0x1A1, 5)
    ClearScenarioFlags(0x1A1, 6)
    ClearScenarioFlags(0x1A1, 7)
    ClearScenarioFlags(0x1A2, 0)
    ClearScenarioFlags(0x1A2, 1)
    ClearScenarioFlags(0x1A2, 2)
    ClearScenarioFlags(0x1A2, 3)
    ClearScenarioFlags(0x1A2, 4)
    ClearScenarioFlags(0x1A2, 5)
    ClearScenarioFlags(0x1A2, 6)
    ClearScenarioFlags(0x1A2, 7)
    ClearScenarioFlags(0x1A3, 0)
    ClearScenarioFlags(0x1A3, 1)
    ClearScenarioFlags(0x1A3, 2)
    ClearScenarioFlags(0x1A3, 3)
    ClearScenarioFlags(0x1A3, 4)
    ClearScenarioFlags(0x1A3, 5)
    ClearScenarioFlags(0x1A3, 6)
    ClearScenarioFlags(0x1A3, 7)
    ClearScenarioFlags(0x1A4, 0)
    ClearScenarioFlags(0x1A4, 1)
    ClearScenarioFlags(0x1A4, 2)
    ClearScenarioFlags(0x1A4, 3)
    ClearScenarioFlags(0x1A4, 4)
    ClearScenarioFlags(0x1A4, 5)
    ClearScenarioFlags(0x1A4, 6)
    ClearScenarioFlags(0x1A4, 7)
    ClearScenarioFlags(0x1A5, 0)
    ClearScenarioFlags(0x1A5, 1)
    ClearScenarioFlags(0x1A5, 2)
    ClearScenarioFlags(0x1A5, 3)
    ClearScenarioFlags(0x1A5, 4)
    ClearScenarioFlags(0x1A5, 5)
    ClearScenarioFlags(0x1A5, 6)
    ClearScenarioFlags(0x1A5, 7)
    ClearScenarioFlags(0x1A6, 0)
    ClearScenarioFlags(0x1A6, 1)
    ClearScenarioFlags(0x1A6, 2)
    ClearScenarioFlags(0x1A6, 3)
    ClearScenarioFlags(0x1A6, 4)
    ClearScenarioFlags(0x1A6, 5)
    ClearScenarioFlags(0x1A6, 6)
    ClearScenarioFlags(0x1A6, 7)
    ClearScenarioFlags(0x1A7, 0)
    ClearScenarioFlags(0x1A7, 1)
    ClearScenarioFlags(0x1A7, 2)
    ClearScenarioFlags(0x1A7, 3)
    ClearScenarioFlags(0x1A7, 4)
    ClearScenarioFlags(0x1A7, 5)
    ClearScenarioFlags(0x1A7, 6)
    ClearScenarioFlags(0x1A7, 7)
    ClearScenarioFlags(0x1A8, 0)
    ClearScenarioFlags(0x1A8, 1)
    ClearScenarioFlags(0x1A8, 2)
    ClearScenarioFlags(0x1A8, 3)
    ClearScenarioFlags(0x1A8, 4)
    ClearScenarioFlags(0x1A8, 5)
    ClearScenarioFlags(0x1A8, 6)
    ClearScenarioFlags(0x1A8, 7)
    ClearScenarioFlags(0x1A9, 0)
    ClearScenarioFlags(0x1A9, 1)
    ClearScenarioFlags(0x1A9, 2)
    ClearScenarioFlags(0x1A9, 3)
    ClearScenarioFlags(0x1A9, 4)
    ClearScenarioFlags(0x1A9, 5)
    ClearScenarioFlags(0x1A9, 6)
    ClearScenarioFlags(0x1AB, 7)
    Return()

    # Function_47_8CAB end


    label("Function_48_8D9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91B5")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "後編１章クエスト\x01",      # 0
            "後編２章クエスト\x01",      # 1
            "後編幕間クエスト\x01",      # 2
            "後編３章クエスト\x01",      # 3
            "後編４章クエスト\x01",      # 4
            "後編終章クエスト\x01",      # 5
            "前編序章クエスト\x01",      # 6
            "前編１章クエスト\x01",      # 7
            "前編２章クエスト\x01",      # 8
            "前編３章クエスト\x01",      # 9
            "前編幕間クエスト\x01",      # 10
            "前編４章クエスト\x01",      # 11
            "前編終章クエスト\x01",      # 12
            "前編全て達成済み\x01",      # 13
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F13"),
        (1, "loc_8F1B"),
        (2, "loc_8F23"),
        (3, "loc_8F2B"),
        (4, "loc_8F33"),
        (5, "loc_8F3B"),
        (6, "loc_8F40"),
        (7, "loc_8F48"),
        (8, "loc_8F50"),
        (9, "loc_8F58"),
        (10, "loc_8F60"),
        (11, "loc_8F68"),
        (12, "loc_8F70"),
        (13, "loc_8F78"),
        (SWITCH_DEFAULT, "loc_91A1"),
    )


    label("loc_8F13")

    Call(2, 49)
    Jump("loc_91B0")

    label("loc_8F1B")

    Call(2, 50)
    Jump("loc_91B0")

    label("loc_8F23")

    Call(2, 51)
    Jump("loc_91B0")

    label("loc_8F2B")

    Call(2, 52)
    Jump("loc_91B0")

    label("loc_8F33")

    Call(2, 53)
    Jump("loc_91B0")

    label("loc_8F3B")

    Jump("loc_91B0")

    label("loc_8F40")

    Call(1, 102)
    Jump("loc_91B0")

    label("loc_8F48")

    Call(1, 102)
    Jump("loc_91B0")

    label("loc_8F50")

    Call(1, 103)
    Jump("loc_91B0")

    label("loc_8F58")

    Call(1, 104)
    Jump("loc_91B0")

    label("loc_8F60")

    Call(1, 105)
    Jump("loc_91B0")

    label("loc_8F68")

    Call(1, 106)
    Jump("loc_91B0")

    label("loc_8F70")

    Call(1, 106)
    Jump("loc_91B0")

    label("loc_8F78")

    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)
    OP_29(0x2, 0x4, 0x10)
    OP_29(0x2, 0x4, 0x20)
    OP_29(0x3, 0x4, 0x10)
    OP_29(0x3, 0x4, 0x20)
    OP_29(0x4, 0x4, 0x10)
    OP_29(0x4, 0x4, 0x20)
    OP_29(0x35, 0x4, 0x10)
    OP_29(0x35, 0x4, 0x20)
    OP_29(0x5, 0x4, 0x10)
    OP_29(0x5, 0x4, 0x20)
    OP_29(0x6, 0x4, 0x10)
    OP_29(0x6, 0x4, 0x20)
    OP_29(0x7, 0x4, 0x10)
    OP_29(0x7, 0x4, 0x20)
    OP_29(0x8, 0x4, 0x10)
    OP_29(0x8, 0x4, 0x20)
    OP_29(0x9, 0x4, 0x10)
    OP_29(0x9, 0x4, 0x20)
    OP_29(0xA, 0x4, 0x10)
    OP_29(0xA, 0x4, 0x20)
    OP_29(0xB, 0x4, 0x10)
    OP_29(0xB, 0x4, 0x20)
    OP_29(0xC, 0x4, 0x10)
    OP_29(0xC, 0x4, 0x20)
    OP_29(0xD, 0x4, 0x10)
    OP_29(0xD, 0x4, 0x20)
    OP_29(0xE, 0x4, 0x10)
    OP_29(0xE, 0x4, 0x20)
    OP_29(0xF, 0x4, 0x10)
    OP_29(0xF, 0x4, 0x20)
    OP_29(0x10, 0x4, 0x10)
    OP_29(0x10, 0x4, 0x20)
    OP_29(0x11, 0x4, 0x10)
    OP_29(0x11, 0x4, 0x20)
    OP_29(0x12, 0x4, 0x10)
    OP_29(0x12, 0x4, 0x20)
    OP_29(0x13, 0x4, 0x10)
    OP_29(0x13, 0x4, 0x20)
    OP_29(0x14, 0x4, 0x10)
    OP_29(0x14, 0x4, 0x20)
    OP_29(0x15, 0x4, 0x10)
    OP_29(0x15, 0x4, 0x20)
    OP_29(0x16, 0x4, 0x10)
    OP_29(0x16, 0x4, 0x20)
    OP_29(0x17, 0x4, 0x10)
    OP_29(0x17, 0x4, 0x20)
    OP_29(0x18, 0x4, 0x10)
    OP_29(0x18, 0x4, 0x20)
    OP_29(0x19, 0x4, 0x10)
    OP_29(0x19, 0x4, 0x20)
    OP_29(0x1A, 0x4, 0x10)
    OP_29(0x1A, 0x4, 0x20)
    OP_29(0x1B, 0x4, 0x10)
    OP_29(0x1B, 0x4, 0x20)
    OP_29(0x1C, 0x4, 0x10)
    OP_29(0x1C, 0x4, 0x20)
    OP_29(0x1D, 0x4, 0x10)
    OP_29(0x1D, 0x4, 0x20)
    OP_29(0x1E, 0x4, 0x10)
    OP_29(0x1E, 0x4, 0x20)
    OP_29(0x1F, 0x4, 0x10)
    OP_29(0x1F, 0x4, 0x20)
    OP_29(0x20, 0x4, 0x10)
    OP_29(0x20, 0x4, 0x20)
    OP_29(0x21, 0x4, 0x10)
    OP_29(0x21, 0x4, 0x20)
    OP_29(0x22, 0x4, 0x10)
    OP_29(0x22, 0x4, 0x20)
    OP_29(0x23, 0x4, 0x10)
    OP_29(0x23, 0x4, 0x20)
    OP_29(0x24, 0x4, 0x10)
    OP_29(0x24, 0x4, 0x20)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x20)
    OP_29(0x26, 0x4, 0x10)
    OP_29(0x26, 0x4, 0x20)
    OP_29(0x27, 0x4, 0x10)
    OP_29(0x27, 0x4, 0x20)
    OP_29(0x28, 0x4, 0x10)
    OP_29(0x28, 0x4, 0x20)
    OP_29(0x29, 0x4, 0x10)
    OP_29(0x29, 0x4, 0x20)
    OP_29(0x2A, 0x4, 0x10)
    OP_29(0x2A, 0x4, 0x20)
    OP_29(0x2B, 0x4, 0x10)
    OP_29(0x2B, 0x4, 0x20)
    OP_29(0x2C, 0x4, 0x10)
    OP_29(0x2C, 0x4, 0x20)
    OP_29(0x2D, 0x4, 0x10)
    OP_29(0x2D, 0x4, 0x20)
    OP_29(0x2E, 0x4, 0x10)
    OP_29(0x2E, 0x4, 0x20)
    OP_29(0x2F, 0x4, 0x10)
    OP_29(0x2F, 0x4, 0x20)
    OP_29(0x30, 0x4, 0x10)
    OP_29(0x30, 0x4, 0x20)
    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x4, 0x20)
    OP_29(0x32, 0x4, 0x10)
    OP_29(0x32, 0x4, 0x20)
    OP_29(0x33, 0x4, 0x10)
    OP_29(0x33, 0x4, 0x20)
    OP_29(0x34, 0x4, 0x10)
    OP_29(0x34, 0x4, 0x20)
    SetScenarioFlags(0xAE, 1)
    SetScenarioFlags(0xEF, 7)
    OP_29(0x3, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x2)
    Jump("loc_91B0")

    label("loc_91A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B0")

    label("loc_91B0")

    Jump("loc_8DA9")

    label("loc_91B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_8D9F end


    label("Function_49_91C0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9DB")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "QS_1101 enigmaⅡの講習\x01",              # 0
            "QS_1102 帝国書記官の身元確認\x01",          # 1
            "QS_1103 メゾン?イメルダの手配魔\x01",       # 2
            "QS_1104 西克洛斯贝尔街道の手配魔\x01",      # 3
            "QS_1105 暴走車の取り締まり\x01",            # 4
            "QS_1106 不審住戸の調査依頼\x01",            # 5
            "QS_1107 消えた雨傘の捜索\x01",              # 6
            "QS_1108 βテストの参加依頼\x01",            # 7
            "QS_1109 码因兹山道の手配魔獣\x01",        # 8
            "QS_1110 Ｄ∴Ｇ教団に関する取材協\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9352"),
        (1, "loc_9352"),
        (2, "loc_9352"),
        (3, "loc_9352"),
        (4, "loc_9352"),
        (5, "loc_9352"),
        (6, "loc_9352"),
        (7, "loc_9352"),
        (8, "loc_9352"),
        (9, "loc_9352"),
        (10, "loc_9352"),
        (SWITCH_DEFAULT, "loc_93CB"),
    )


    label("loc_9352")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x4)
    Jump("loc_93DA")

    label("loc_93CB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93DA")

    label("loc_93DA")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9D6")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9432"),
        (1, "loc_965C"),
        (2, "loc_9886"),
        (3, "loc_9AB0"),
        (4, "loc_9CDA"),
        (5, "loc_9F04"),
        (6, "loc_A12E"),
        (7, "loc_A358"),
        (8, "loc_A582"),
        (9, "loc_A7AC"),
        (SWITCH_DEFAULT, "loc_A9D6"),
    )


    label("loc_9432")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951F")
    OP_29(0x65, 0x3, 0x0)
    OP_29(0x65, 0x3, 0x1)
    OP_29(0x65, 0x3, 0x2)
    OP_29(0x65, 0x3, 0x10)
    OP_29(0x65, 0x3, 0x20)
    OP_29(0x65, 0x3, 0x40)
    OP_29(0x65, 0x2, 0x0)
    OP_29(0x65, 0x2, 0x1)
    OP_29(0x65, 0x2, 0x2)
    OP_29(0x65, 0x2, 0x3)
    OP_29(0x65, 0x2, 0x4)
    OP_29(0x65, 0x2, 0x5)
    OP_29(0x65, 0x2, 0x6)
    OP_29(0x65, 0x2, 0x7)
    OP_29(0x65, 0x2, 0x8)
    OP_29(0x65, 0x2, 0x9)
    OP_29(0x65, 0x2, 0xA)
    OP_29(0x65, 0x2, 0xB)
    OP_29(0x65, 0x2, 0xC)
    OP_29(0x65, 0x2, 0xD)
    OP_29(0x65, 0x2, 0xE)
    OP_29(0x65, 0x2, 0xF)
    OP_29(0x65, 0x2, 0x10)
    OP_29(0x65, 0x2, 0x11)
    OP_29(0x65, 0x2, 0x12)
    OP_29(0x65, 0x2, 0x13)
    OP_29(0x65, 0x2, 0x14)
    OP_29(0x65, 0x2, 0x15)
    OP_29(0x65, 0x2, 0x16)
    OP_29(0x65, 0x2, 0x17)
    OP_29(0x65, 0x2, 0x18)
    OP_29(0x65, 0x2, 0x19)
    OP_29(0x65, 0x2, 0x1A)
    OP_29(0x65, 0x2, 0x1B)
    OP_29(0x65, 0x2, 0x1C)
    OP_29(0x65, 0x2, 0x1D)
    OP_29(0x65, 0x2, 0x1E)
    OP_29(0x65, 0x2, 0x1F)

    label("loc_951F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9533")
    OP_29(0x65, 0x4, 0x2)

    label("loc_9533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9548")
    OP_29(0x65, 0x1, 0x0)

    label("loc_9548")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_955D")
    OP_29(0x65, 0x1, 0x1)

    label("loc_955D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9572")
    OP_29(0x65, 0x1, 0x2)

    label("loc_9572")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9587")
    OP_29(0x65, 0x1, 0x3)

    label("loc_9587")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_959C")
    OP_29(0x65, 0x1, 0x4)

    label("loc_959C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_95B1")
    OP_29(0x65, 0x1, 0x5)

    label("loc_95B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_95C6")
    OP_29(0x65, 0x1, 0x6)

    label("loc_95C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_95DB")
    OP_29(0x65, 0x1, 0x7)

    label("loc_95DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_95F0")
    OP_29(0x65, 0x1, 0x8)

    label("loc_95F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9605")
    OP_29(0x65, 0x1, 0x9)

    label("loc_9605")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_961A")
    OP_29(0x65, 0x1, 0xA)

    label("loc_961A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_962F")
    OP_29(0x65, 0x1, 0xB)

    label("loc_962F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9643")
    OP_29(0x65, 0x4, 0x10)

    label("loc_9643")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9657")
    OP_29(0x65, 0x4, 0x20)

    label("loc_9657")

    Jump("loc_A9D6")

    label("loc_965C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9749")
    OP_29(0x66, 0x3, 0x0)
    OP_29(0x66, 0x3, 0x1)
    OP_29(0x66, 0x3, 0x2)
    OP_29(0x66, 0x3, 0x10)
    OP_29(0x66, 0x3, 0x20)
    OP_29(0x66, 0x3, 0x40)
    OP_29(0x66, 0x2, 0x0)
    OP_29(0x66, 0x2, 0x1)
    OP_29(0x66, 0x2, 0x2)
    OP_29(0x66, 0x2, 0x3)
    OP_29(0x66, 0x2, 0x4)
    OP_29(0x66, 0x2, 0x5)
    OP_29(0x66, 0x2, 0x6)
    OP_29(0x66, 0x2, 0x7)
    OP_29(0x66, 0x2, 0x8)
    OP_29(0x66, 0x2, 0x9)
    OP_29(0x66, 0x2, 0xA)
    OP_29(0x66, 0x2, 0xB)
    OP_29(0x66, 0x2, 0xC)
    OP_29(0x66, 0x2, 0xD)
    OP_29(0x66, 0x2, 0xE)
    OP_29(0x66, 0x2, 0xF)
    OP_29(0x66, 0x2, 0x10)
    OP_29(0x66, 0x2, 0x11)
    OP_29(0x66, 0x2, 0x12)
    OP_29(0x66, 0x2, 0x13)
    OP_29(0x66, 0x2, 0x14)
    OP_29(0x66, 0x2, 0x15)
    OP_29(0x66, 0x2, 0x16)
    OP_29(0x66, 0x2, 0x17)
    OP_29(0x66, 0x2, 0x18)
    OP_29(0x66, 0x2, 0x19)
    OP_29(0x66, 0x2, 0x1A)
    OP_29(0x66, 0x2, 0x1B)
    OP_29(0x66, 0x2, 0x1C)
    OP_29(0x66, 0x2, 0x1D)
    OP_29(0x66, 0x2, 0x1E)
    OP_29(0x66, 0x2, 0x1F)

    label("loc_9749")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_975D")
    OP_29(0x66, 0x4, 0x2)

    label("loc_975D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9772")
    OP_29(0x66, 0x1, 0x0)

    label("loc_9772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9787")
    OP_29(0x66, 0x1, 0x1)

    label("loc_9787")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_979C")
    OP_29(0x66, 0x1, 0x2)

    label("loc_979C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_97B1")
    OP_29(0x66, 0x1, 0x3)

    label("loc_97B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_97C6")
    OP_29(0x66, 0x1, 0x4)

    label("loc_97C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_97DB")
    OP_29(0x66, 0x1, 0x5)

    label("loc_97DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_97F0")
    OP_29(0x66, 0x1, 0x6)

    label("loc_97F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9805")
    OP_29(0x66, 0x1, 0x7)

    label("loc_9805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_981A")
    OP_29(0x66, 0x1, 0x8)

    label("loc_981A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_982F")
    OP_29(0x66, 0x1, 0x9)

    label("loc_982F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9844")
    OP_29(0x66, 0x1, 0xA)

    label("loc_9844")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9859")
    OP_29(0x66, 0x1, 0xB)

    label("loc_9859")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_986D")
    OP_29(0x66, 0x4, 0x10)

    label("loc_986D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9881")
    OP_29(0x66, 0x4, 0x20)

    label("loc_9881")

    Jump("loc_A9D6")

    label("loc_9886")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9973")
    OP_29(0x67, 0x3, 0x0)
    OP_29(0x67, 0x3, 0x1)
    OP_29(0x67, 0x3, 0x2)
    OP_29(0x67, 0x3, 0x10)
    OP_29(0x67, 0x3, 0x20)
    OP_29(0x67, 0x3, 0x40)
    OP_29(0x67, 0x2, 0x0)
    OP_29(0x67, 0x2, 0x1)
    OP_29(0x67, 0x2, 0x2)
    OP_29(0x67, 0x2, 0x3)
    OP_29(0x67, 0x2, 0x4)
    OP_29(0x67, 0x2, 0x5)
    OP_29(0x67, 0x2, 0x6)
    OP_29(0x67, 0x2, 0x7)
    OP_29(0x67, 0x2, 0x8)
    OP_29(0x67, 0x2, 0x9)
    OP_29(0x67, 0x2, 0xA)
    OP_29(0x67, 0x2, 0xB)
    OP_29(0x67, 0x2, 0xC)
    OP_29(0x67, 0x2, 0xD)
    OP_29(0x67, 0x2, 0xE)
    OP_29(0x67, 0x2, 0xF)
    OP_29(0x67, 0x2, 0x10)
    OP_29(0x67, 0x2, 0x11)
    OP_29(0x67, 0x2, 0x12)
    OP_29(0x67, 0x2, 0x13)
    OP_29(0x67, 0x2, 0x14)
    OP_29(0x67, 0x2, 0x15)
    OP_29(0x67, 0x2, 0x16)
    OP_29(0x67, 0x2, 0x17)
    OP_29(0x67, 0x2, 0x18)
    OP_29(0x67, 0x2, 0x19)
    OP_29(0x67, 0x2, 0x1A)
    OP_29(0x67, 0x2, 0x1B)
    OP_29(0x67, 0x2, 0x1C)
    OP_29(0x67, 0x2, 0x1D)
    OP_29(0x67, 0x2, 0x1E)
    OP_29(0x67, 0x2, 0x1F)

    label("loc_9973")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9987")
    OP_29(0x67, 0x4, 0x2)

    label("loc_9987")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_999C")
    OP_29(0x67, 0x1, 0x0)

    label("loc_999C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_99B1")
    OP_29(0x67, 0x1, 0x1)

    label("loc_99B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_99C6")
    OP_29(0x67, 0x1, 0x2)

    label("loc_99C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_99DB")
    OP_29(0x67, 0x1, 0x3)

    label("loc_99DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_99F0")
    OP_29(0x67, 0x1, 0x4)

    label("loc_99F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A05")
    OP_29(0x67, 0x1, 0x5)

    label("loc_9A05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A1A")
    OP_29(0x67, 0x1, 0x6)

    label("loc_9A1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A2F")
    OP_29(0x67, 0x1, 0x7)

    label("loc_9A2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A44")
    OP_29(0x67, 0x1, 0x8)

    label("loc_9A44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A59")
    OP_29(0x67, 0x1, 0x9)

    label("loc_9A59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A6E")
    OP_29(0x67, 0x1, 0xA)

    label("loc_9A6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A83")
    OP_29(0x67, 0x1, 0xB)

    label("loc_9A83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9A97")
    OP_29(0x67, 0x4, 0x10)

    label("loc_9A97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9AAB")
    OP_29(0x67, 0x4, 0x20)

    label("loc_9AAB")

    Jump("loc_A9D6")

    label("loc_9AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B9D")
    OP_29(0x68, 0x3, 0x0)
    OP_29(0x68, 0x3, 0x1)
    OP_29(0x68, 0x3, 0x2)
    OP_29(0x68, 0x3, 0x10)
    OP_29(0x68, 0x3, 0x20)
    OP_29(0x68, 0x3, 0x40)
    OP_29(0x68, 0x2, 0x0)
    OP_29(0x68, 0x2, 0x1)
    OP_29(0x68, 0x2, 0x2)
    OP_29(0x68, 0x2, 0x3)
    OP_29(0x68, 0x2, 0x4)
    OP_29(0x68, 0x2, 0x5)
    OP_29(0x68, 0x2, 0x6)
    OP_29(0x68, 0x2, 0x7)
    OP_29(0x68, 0x2, 0x8)
    OP_29(0x68, 0x2, 0x9)
    OP_29(0x68, 0x2, 0xA)
    OP_29(0x68, 0x2, 0xB)
    OP_29(0x68, 0x2, 0xC)
    OP_29(0x68, 0x2, 0xD)
    OP_29(0x68, 0x2, 0xE)
    OP_29(0x68, 0x2, 0xF)
    OP_29(0x68, 0x2, 0x10)
    OP_29(0x68, 0x2, 0x11)
    OP_29(0x68, 0x2, 0x12)
    OP_29(0x68, 0x2, 0x13)
    OP_29(0x68, 0x2, 0x14)
    OP_29(0x68, 0x2, 0x15)
    OP_29(0x68, 0x2, 0x16)
    OP_29(0x68, 0x2, 0x17)
    OP_29(0x68, 0x2, 0x18)
    OP_29(0x68, 0x2, 0x19)
    OP_29(0x68, 0x2, 0x1A)
    OP_29(0x68, 0x2, 0x1B)
    OP_29(0x68, 0x2, 0x1C)
    OP_29(0x68, 0x2, 0x1D)
    OP_29(0x68, 0x2, 0x1E)
    OP_29(0x68, 0x2, 0x1F)

    label("loc_9B9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9BB1")
    OP_29(0x68, 0x4, 0x2)

    label("loc_9BB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9BC6")
    OP_29(0x68, 0x1, 0x0)

    label("loc_9BC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9BDB")
    OP_29(0x68, 0x1, 0x1)

    label("loc_9BDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9BF0")
    OP_29(0x68, 0x1, 0x2)

    label("loc_9BF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C05")
    OP_29(0x68, 0x1, 0x3)

    label("loc_9C05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C1A")
    OP_29(0x68, 0x1, 0x4)

    label("loc_9C1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C2F")
    OP_29(0x68, 0x1, 0x5)

    label("loc_9C2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C44")
    OP_29(0x68, 0x1, 0x6)

    label("loc_9C44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C59")
    OP_29(0x68, 0x1, 0x7)

    label("loc_9C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C6E")
    OP_29(0x68, 0x1, 0x8)

    label("loc_9C6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C83")
    OP_29(0x68, 0x1, 0x9)

    label("loc_9C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9C98")
    OP_29(0x68, 0x1, 0xA)

    label("loc_9C98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CAD")
    OP_29(0x68, 0x1, 0xB)

    label("loc_9CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CC1")
    OP_29(0x68, 0x4, 0x10)

    label("loc_9CC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CD5")
    OP_29(0x68, 0x4, 0x20)

    label("loc_9CD5")

    Jump("loc_A9D6")

    label("loc_9CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DC7")
    OP_29(0x69, 0x3, 0x0)
    OP_29(0x69, 0x3, 0x1)
    OP_29(0x69, 0x3, 0x2)
    OP_29(0x69, 0x3, 0x10)
    OP_29(0x69, 0x3, 0x20)
    OP_29(0x69, 0x3, 0x40)
    OP_29(0x69, 0x2, 0x0)
    OP_29(0x69, 0x2, 0x1)
    OP_29(0x69, 0x2, 0x2)
    OP_29(0x69, 0x2, 0x3)
    OP_29(0x69, 0x2, 0x4)
    OP_29(0x69, 0x2, 0x5)
    OP_29(0x69, 0x2, 0x6)
    OP_29(0x69, 0x2, 0x7)
    OP_29(0x69, 0x2, 0x8)
    OP_29(0x69, 0x2, 0x9)
    OP_29(0x69, 0x2, 0xA)
    OP_29(0x69, 0x2, 0xB)
    OP_29(0x69, 0x2, 0xC)
    OP_29(0x69, 0x2, 0xD)
    OP_29(0x69, 0x2, 0xE)
    OP_29(0x69, 0x2, 0xF)
    OP_29(0x69, 0x2, 0x10)
    OP_29(0x69, 0x2, 0x11)
    OP_29(0x69, 0x2, 0x12)
    OP_29(0x69, 0x2, 0x13)
    OP_29(0x69, 0x2, 0x14)
    OP_29(0x69, 0x2, 0x15)
    OP_29(0x69, 0x2, 0x16)
    OP_29(0x69, 0x2, 0x17)
    OP_29(0x69, 0x2, 0x18)
    OP_29(0x69, 0x2, 0x19)
    OP_29(0x69, 0x2, 0x1A)
    OP_29(0x69, 0x2, 0x1B)
    OP_29(0x69, 0x2, 0x1C)
    OP_29(0x69, 0x2, 0x1D)
    OP_29(0x69, 0x2, 0x1E)
    OP_29(0x69, 0x2, 0x1F)

    label("loc_9DC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DDB")
    OP_29(0x69, 0x4, 0x2)

    label("loc_9DDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DF0")
    OP_29(0x69, 0x1, 0x0)

    label("loc_9DF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E05")
    OP_29(0x69, 0x1, 0x1)

    label("loc_9E05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E1A")
    OP_29(0x69, 0x1, 0x2)

    label("loc_9E1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E2F")
    OP_29(0x69, 0x1, 0x3)

    label("loc_9E2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E44")
    OP_29(0x69, 0x1, 0x4)

    label("loc_9E44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E59")
    OP_29(0x69, 0x1, 0x5)

    label("loc_9E59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E6E")
    OP_29(0x69, 0x1, 0x6)

    label("loc_9E6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E83")
    OP_29(0x69, 0x1, 0x7)

    label("loc_9E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9E98")
    OP_29(0x69, 0x1, 0x8)

    label("loc_9E98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9EAD")
    OP_29(0x69, 0x1, 0x9)

    label("loc_9EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9EC2")
    OP_29(0x69, 0x1, 0xA)

    label("loc_9EC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9ED7")
    OP_29(0x69, 0x1, 0xB)

    label("loc_9ED7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9EEB")
    OP_29(0x69, 0x4, 0x10)

    label("loc_9EEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9EFF")
    OP_29(0x69, 0x4, 0x20)

    label("loc_9EFF")

    Jump("loc_A9D6")

    label("loc_9F04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF1")
    OP_29(0x6A, 0x3, 0x0)
    OP_29(0x6A, 0x3, 0x1)
    OP_29(0x6A, 0x3, 0x2)
    OP_29(0x6A, 0x3, 0x10)
    OP_29(0x6A, 0x3, 0x20)
    OP_29(0x6A, 0x3, 0x40)
    OP_29(0x6A, 0x2, 0x0)
    OP_29(0x6A, 0x2, 0x1)
    OP_29(0x6A, 0x2, 0x2)
    OP_29(0x6A, 0x2, 0x3)
    OP_29(0x6A, 0x2, 0x4)
    OP_29(0x6A, 0x2, 0x5)
    OP_29(0x6A, 0x2, 0x6)
    OP_29(0x6A, 0x2, 0x7)
    OP_29(0x6A, 0x2, 0x8)
    OP_29(0x6A, 0x2, 0x9)
    OP_29(0x6A, 0x2, 0xA)
    OP_29(0x6A, 0x2, 0xB)
    OP_29(0x6A, 0x2, 0xC)
    OP_29(0x6A, 0x2, 0xD)
    OP_29(0x6A, 0x2, 0xE)
    OP_29(0x6A, 0x2, 0xF)
    OP_29(0x6A, 0x2, 0x10)
    OP_29(0x6A, 0x2, 0x11)
    OP_29(0x6A, 0x2, 0x12)
    OP_29(0x6A, 0x2, 0x13)
    OP_29(0x6A, 0x2, 0x14)
    OP_29(0x6A, 0x2, 0x15)
    OP_29(0x6A, 0x2, 0x16)
    OP_29(0x6A, 0x2, 0x17)
    OP_29(0x6A, 0x2, 0x18)
    OP_29(0x6A, 0x2, 0x19)
    OP_29(0x6A, 0x2, 0x1A)
    OP_29(0x6A, 0x2, 0x1B)
    OP_29(0x6A, 0x2, 0x1C)
    OP_29(0x6A, 0x2, 0x1D)
    OP_29(0x6A, 0x2, 0x1E)
    OP_29(0x6A, 0x2, 0x1F)

    label("loc_9FF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A005")
    OP_29(0x6A, 0x4, 0x2)

    label("loc_A005")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A01A")
    OP_29(0x6A, 0x1, 0x0)

    label("loc_A01A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A02F")
    OP_29(0x6A, 0x1, 0x1)

    label("loc_A02F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A044")
    OP_29(0x6A, 0x1, 0x2)

    label("loc_A044")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A059")
    OP_29(0x6A, 0x1, 0x3)

    label("loc_A059")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A06E")
    OP_29(0x6A, 0x1, 0x4)

    label("loc_A06E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A083")
    OP_29(0x6A, 0x1, 0x5)

    label("loc_A083")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A098")
    OP_29(0x6A, 0x1, 0x6)

    label("loc_A098")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0AD")
    OP_29(0x6A, 0x1, 0x7)

    label("loc_A0AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0C2")
    OP_29(0x6A, 0x1, 0x8)

    label("loc_A0C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0D7")
    OP_29(0x6A, 0x1, 0x9)

    label("loc_A0D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0EC")
    OP_29(0x6A, 0x1, 0xA)

    label("loc_A0EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A101")
    OP_29(0x6A, 0x1, 0xB)

    label("loc_A101")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A115")
    OP_29(0x6A, 0x4, 0x10)

    label("loc_A115")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A129")
    OP_29(0x6A, 0x4, 0x20)

    label("loc_A129")

    Jump("loc_A9D6")

    label("loc_A12E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A21B")
    OP_29(0x6B, 0x3, 0x0)
    OP_29(0x6B, 0x3, 0x1)
    OP_29(0x6B, 0x3, 0x2)
    OP_29(0x6B, 0x3, 0x10)
    OP_29(0x6B, 0x3, 0x20)
    OP_29(0x6B, 0x3, 0x40)
    OP_29(0x6B, 0x2, 0x0)
    OP_29(0x6B, 0x2, 0x1)
    OP_29(0x6B, 0x2, 0x2)
    OP_29(0x6B, 0x2, 0x3)
    OP_29(0x6B, 0x2, 0x4)
    OP_29(0x6B, 0x2, 0x5)
    OP_29(0x6B, 0x2, 0x6)
    OP_29(0x6B, 0x2, 0x7)
    OP_29(0x6B, 0x2, 0x8)
    OP_29(0x6B, 0x2, 0x9)
    OP_29(0x6B, 0x2, 0xA)
    OP_29(0x6B, 0x2, 0xB)
    OP_29(0x6B, 0x2, 0xC)
    OP_29(0x6B, 0x2, 0xD)
    OP_29(0x6B, 0x2, 0xE)
    OP_29(0x6B, 0x2, 0xF)
    OP_29(0x6B, 0x2, 0x10)
    OP_29(0x6B, 0x2, 0x11)
    OP_29(0x6B, 0x2, 0x12)
    OP_29(0x6B, 0x2, 0x13)
    OP_29(0x6B, 0x2, 0x14)
    OP_29(0x6B, 0x2, 0x15)
    OP_29(0x6B, 0x2, 0x16)
    OP_29(0x6B, 0x2, 0x17)
    OP_29(0x6B, 0x2, 0x18)
    OP_29(0x6B, 0x2, 0x19)
    OP_29(0x6B, 0x2, 0x1A)
    OP_29(0x6B, 0x2, 0x1B)
    OP_29(0x6B, 0x2, 0x1C)
    OP_29(0x6B, 0x2, 0x1D)
    OP_29(0x6B, 0x2, 0x1E)
    OP_29(0x6B, 0x2, 0x1F)

    label("loc_A21B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A22F")
    OP_29(0x6B, 0x4, 0x2)

    label("loc_A22F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A244")
    OP_29(0x6B, 0x1, 0x0)

    label("loc_A244")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A259")
    OP_29(0x6B, 0x1, 0x1)

    label("loc_A259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A26E")
    OP_29(0x6B, 0x1, 0x2)

    label("loc_A26E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A283")
    OP_29(0x6B, 0x1, 0x3)

    label("loc_A283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A298")
    OP_29(0x6B, 0x1, 0x4)

    label("loc_A298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A2AD")
    OP_29(0x6B, 0x1, 0x5)

    label("loc_A2AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A2C2")
    OP_29(0x6B, 0x1, 0x6)

    label("loc_A2C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A2D7")
    OP_29(0x6B, 0x1, 0x7)

    label("loc_A2D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A2EC")
    OP_29(0x6B, 0x1, 0x8)

    label("loc_A2EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A301")
    OP_29(0x6B, 0x1, 0x9)

    label("loc_A301")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A316")
    OP_29(0x6B, 0x1, 0xA)

    label("loc_A316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A32B")
    OP_29(0x6B, 0x1, 0xB)

    label("loc_A32B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A33F")
    OP_29(0x6B, 0x4, 0x10)

    label("loc_A33F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A353")
    OP_29(0x6B, 0x4, 0x20)

    label("loc_A353")

    Jump("loc_A9D6")

    label("loc_A358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A445")
    OP_29(0x6C, 0x3, 0x0)
    OP_29(0x6C, 0x3, 0x1)
    OP_29(0x6C, 0x3, 0x2)
    OP_29(0x6C, 0x3, 0x10)
    OP_29(0x6C, 0x3, 0x20)
    OP_29(0x6C, 0x3, 0x40)
    OP_29(0x6C, 0x2, 0x0)
    OP_29(0x6C, 0x2, 0x1)
    OP_29(0x6C, 0x2, 0x2)
    OP_29(0x6C, 0x2, 0x3)
    OP_29(0x6C, 0x2, 0x4)
    OP_29(0x6C, 0x2, 0x5)
    OP_29(0x6C, 0x2, 0x6)
    OP_29(0x6C, 0x2, 0x7)
    OP_29(0x6C, 0x2, 0x8)
    OP_29(0x6C, 0x2, 0x9)
    OP_29(0x6C, 0x2, 0xA)
    OP_29(0x6C, 0x2, 0xB)
    OP_29(0x6C, 0x2, 0xC)
    OP_29(0x6C, 0x2, 0xD)
    OP_29(0x6C, 0x2, 0xE)
    OP_29(0x6C, 0x2, 0xF)
    OP_29(0x6C, 0x2, 0x10)
    OP_29(0x6C, 0x2, 0x11)
    OP_29(0x6C, 0x2, 0x12)
    OP_29(0x6C, 0x2, 0x13)
    OP_29(0x6C, 0x2, 0x14)
    OP_29(0x6C, 0x2, 0x15)
    OP_29(0x6C, 0x2, 0x16)
    OP_29(0x6C, 0x2, 0x17)
    OP_29(0x6C, 0x2, 0x18)
    OP_29(0x6C, 0x2, 0x19)
    OP_29(0x6C, 0x2, 0x1A)
    OP_29(0x6C, 0x2, 0x1B)
    OP_29(0x6C, 0x2, 0x1C)
    OP_29(0x6C, 0x2, 0x1D)
    OP_29(0x6C, 0x2, 0x1E)
    OP_29(0x6C, 0x2, 0x1F)

    label("loc_A445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A459")
    OP_29(0x6C, 0x4, 0x2)

    label("loc_A459")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A46E")
    OP_29(0x6C, 0x1, 0x0)

    label("loc_A46E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A483")
    OP_29(0x6C, 0x1, 0x1)

    label("loc_A483")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A498")
    OP_29(0x6C, 0x1, 0x2)

    label("loc_A498")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A4AD")
    OP_29(0x6C, 0x1, 0x3)

    label("loc_A4AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A4C2")
    OP_29(0x6C, 0x1, 0x4)

    label("loc_A4C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A4D7")
    OP_29(0x6C, 0x1, 0x5)

    label("loc_A4D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A4EC")
    OP_29(0x6C, 0x1, 0x6)

    label("loc_A4EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A501")
    OP_29(0x6C, 0x1, 0x7)

    label("loc_A501")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A516")
    OP_29(0x6C, 0x1, 0x8)

    label("loc_A516")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A52B")
    OP_29(0x6C, 0x1, 0x9)

    label("loc_A52B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A540")
    OP_29(0x6C, 0x1, 0xA)

    label("loc_A540")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A555")
    OP_29(0x6C, 0x1, 0xB)

    label("loc_A555")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A569")
    OP_29(0x6C, 0x4, 0x10)

    label("loc_A569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A57D")
    OP_29(0x6C, 0x4, 0x20)

    label("loc_A57D")

    Jump("loc_A9D6")

    label("loc_A582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A66F")
    OP_29(0x6D, 0x3, 0x0)
    OP_29(0x6D, 0x3, 0x1)
    OP_29(0x6D, 0x3, 0x2)
    OP_29(0x6D, 0x3, 0x10)
    OP_29(0x6D, 0x3, 0x20)
    OP_29(0x6D, 0x3, 0x40)
    OP_29(0x6D, 0x2, 0x0)
    OP_29(0x6D, 0x2, 0x1)
    OP_29(0x6D, 0x2, 0x2)
    OP_29(0x6D, 0x2, 0x3)
    OP_29(0x6D, 0x2, 0x4)
    OP_29(0x6D, 0x2, 0x5)
    OP_29(0x6D, 0x2, 0x6)
    OP_29(0x6D, 0x2, 0x7)
    OP_29(0x6D, 0x2, 0x8)
    OP_29(0x6D, 0x2, 0x9)
    OP_29(0x6D, 0x2, 0xA)
    OP_29(0x6D, 0x2, 0xB)
    OP_29(0x6D, 0x2, 0xC)
    OP_29(0x6D, 0x2, 0xD)
    OP_29(0x6D, 0x2, 0xE)
    OP_29(0x6D, 0x2, 0xF)
    OP_29(0x6D, 0x2, 0x10)
    OP_29(0x6D, 0x2, 0x11)
    OP_29(0x6D, 0x2, 0x12)
    OP_29(0x6D, 0x2, 0x13)
    OP_29(0x6D, 0x2, 0x14)
    OP_29(0x6D, 0x2, 0x15)
    OP_29(0x6D, 0x2, 0x16)
    OP_29(0x6D, 0x2, 0x17)
    OP_29(0x6D, 0x2, 0x18)
    OP_29(0x6D, 0x2, 0x19)
    OP_29(0x6D, 0x2, 0x1A)
    OP_29(0x6D, 0x2, 0x1B)
    OP_29(0x6D, 0x2, 0x1C)
    OP_29(0x6D, 0x2, 0x1D)
    OP_29(0x6D, 0x2, 0x1E)
    OP_29(0x6D, 0x2, 0x1F)

    label("loc_A66F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A683")
    OP_29(0x6D, 0x4, 0x2)

    label("loc_A683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A698")
    OP_29(0x6D, 0x1, 0x0)

    label("loc_A698")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A6AD")
    OP_29(0x6D, 0x1, 0x1)

    label("loc_A6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A6C2")
    OP_29(0x6D, 0x1, 0x2)

    label("loc_A6C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A6D7")
    OP_29(0x6D, 0x1, 0x3)

    label("loc_A6D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A6EC")
    OP_29(0x6D, 0x1, 0x4)

    label("loc_A6EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A701")
    OP_29(0x6D, 0x1, 0x5)

    label("loc_A701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A716")
    OP_29(0x6D, 0x1, 0x6)

    label("loc_A716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A72B")
    OP_29(0x6D, 0x1, 0x7)

    label("loc_A72B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A740")
    OP_29(0x6D, 0x1, 0x8)

    label("loc_A740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A755")
    OP_29(0x6D, 0x1, 0x9)

    label("loc_A755")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A76A")
    OP_29(0x6D, 0x1, 0xA)

    label("loc_A76A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A77F")
    OP_29(0x6D, 0x1, 0xB)

    label("loc_A77F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A793")
    OP_29(0x6D, 0x4, 0x10)

    label("loc_A793")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A7A7")
    OP_29(0x6D, 0x4, 0x20)

    label("loc_A7A7")

    Jump("loc_A9D6")

    label("loc_A7AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A899")
    OP_29(0x6E, 0x3, 0x0)
    OP_29(0x6E, 0x3, 0x1)
    OP_29(0x6E, 0x3, 0x2)
    OP_29(0x6E, 0x3, 0x10)
    OP_29(0x6E, 0x3, 0x20)
    OP_29(0x6E, 0x3, 0x40)
    OP_29(0x6E, 0x2, 0x0)
    OP_29(0x6E, 0x2, 0x1)
    OP_29(0x6E, 0x2, 0x2)
    OP_29(0x6E, 0x2, 0x3)
    OP_29(0x6E, 0x2, 0x4)
    OP_29(0x6E, 0x2, 0x5)
    OP_29(0x6E, 0x2, 0x6)
    OP_29(0x6E, 0x2, 0x7)
    OP_29(0x6E, 0x2, 0x8)
    OP_29(0x6E, 0x2, 0x9)
    OP_29(0x6E, 0x2, 0xA)
    OP_29(0x6E, 0x2, 0xB)
    OP_29(0x6E, 0x2, 0xC)
    OP_29(0x6E, 0x2, 0xD)
    OP_29(0x6E, 0x2, 0xE)
    OP_29(0x6E, 0x2, 0xF)
    OP_29(0x6E, 0x2, 0x10)
    OP_29(0x6E, 0x2, 0x11)
    OP_29(0x6E, 0x2, 0x12)
    OP_29(0x6E, 0x2, 0x13)
    OP_29(0x6E, 0x2, 0x14)
    OP_29(0x6E, 0x2, 0x15)
    OP_29(0x6E, 0x2, 0x16)
    OP_29(0x6E, 0x2, 0x17)
    OP_29(0x6E, 0x2, 0x18)
    OP_29(0x6E, 0x2, 0x19)
    OP_29(0x6E, 0x2, 0x1A)
    OP_29(0x6E, 0x2, 0x1B)
    OP_29(0x6E, 0x2, 0x1C)
    OP_29(0x6E, 0x2, 0x1D)
    OP_29(0x6E, 0x2, 0x1E)
    OP_29(0x6E, 0x2, 0x1F)

    label("loc_A899")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A8AD")
    OP_29(0x6E, 0x4, 0x2)

    label("loc_A8AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A8C2")
    OP_29(0x6E, 0x1, 0x0)

    label("loc_A8C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A8D7")
    OP_29(0x6E, 0x1, 0x1)

    label("loc_A8D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A8EC")
    OP_29(0x6E, 0x1, 0x2)

    label("loc_A8EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A901")
    OP_29(0x6E, 0x1, 0x3)

    label("loc_A901")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A916")
    OP_29(0x6E, 0x1, 0x4)

    label("loc_A916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A92B")
    OP_29(0x6E, 0x1, 0x5)

    label("loc_A92B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A940")
    OP_29(0x6E, 0x1, 0x6)

    label("loc_A940")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A955")
    OP_29(0x6E, 0x1, 0x7)

    label("loc_A955")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A96A")
    OP_29(0x6E, 0x1, 0x8)

    label("loc_A96A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A97F")
    OP_29(0x6E, 0x1, 0x9)

    label("loc_A97F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A994")
    OP_29(0x6E, 0x1, 0xA)

    label("loc_A994")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A9A9")
    OP_29(0x6E, 0x1, 0xB)

    label("loc_A9A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A9BD")
    OP_29(0x6E, 0x4, 0x10)

    label("loc_A9BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A9D1")
    OP_29(0x6E, 0x4, 0x20)

    label("loc_A9D1")

    Jump("loc_A9D6")

    label("loc_A9D6")

    Jump("loc_91CA")

    label("loc_A9DB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_49_91C0 end


    label("Function_50_A9F3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB3B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "QS_1201 警備隊演習の参加要請\x01",          # 0
            "QS_1202 問診表の回収\x01",                  # 1
            "QS_1203 塔の古文書調査\x01",                # 2
            "QS_1204 阿尔摩里卡古道の手配魔獣\x01",      # 3
            "QS_1205 黒月からの依頼\x01",                # 4
            "QS_1206 仔猫の捜索依頼\x01",                # 5
            "QS_1207 遊撃士訓練への参加要請\x01",        # 6
            "QS_1208 演奏家の捜索\x01",                  # 7
            "QS_1209 東克洛斯贝尔街道の手配魔\x01",      # 8
            "QS_1210 解毒薬の材料調達\x01",              # 9
            "QS_1211 共和国臨検官の作業補助\x01",        # 10
            "QS_1212 消えたコレクションの捜索\x01",      # 11
            "QS_1213 乌尔丝拉間道の手配魔獣\x01",        # 12
            "QS_1214 月の僧院の調査\x01",                # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ABF2"),
        (1, "loc_ABF2"),
        (2, "loc_ABF2"),
        (3, "loc_ABF2"),
        (4, "loc_ABF2"),
        (5, "loc_ABF2"),
        (6, "loc_ABF2"),
        (7, "loc_ABF2"),
        (8, "loc_ABF2"),
        (9, "loc_ABF2"),
        (10, "loc_ABF2"),
        (11, "loc_ABF2"),
        (12, "loc_ABF2"),
        (13, "loc_ABF2"),
        (SWITCH_DEFAULT, "loc_AC6B"),
    )


    label("loc_ABF2")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x4)
    Jump("loc_AC7A")

    label("loc_AC6B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AC7A")

    label("loc_AC7A")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB36")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ACEA"),
        (1, "loc_AF14"),
        (2, "loc_B13E"),
        (3, "loc_B368"),
        (4, "loc_B592"),
        (5, "loc_B7BC"),
        (6, "loc_B9E6"),
        (7, "loc_BC10"),
        (8, "loc_BE3A"),
        (9, "loc_C064"),
        (10, "loc_C28E"),
        (11, "loc_C4B8"),
        (12, "loc_C6E2"),
        (13, "loc_C90C"),
        (SWITCH_DEFAULT, "loc_CB36"),
    )


    label("loc_ACEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADD7")
    OP_29(0x6F, 0x3, 0x0)
    OP_29(0x6F, 0x3, 0x1)
    OP_29(0x6F, 0x3, 0x2)
    OP_29(0x6F, 0x3, 0x10)
    OP_29(0x6F, 0x3, 0x20)
    OP_29(0x6F, 0x3, 0x40)
    OP_29(0x6F, 0x2, 0x0)
    OP_29(0x6F, 0x2, 0x1)
    OP_29(0x6F, 0x2, 0x2)
    OP_29(0x6F, 0x2, 0x3)
    OP_29(0x6F, 0x2, 0x4)
    OP_29(0x6F, 0x2, 0x5)
    OP_29(0x6F, 0x2, 0x6)
    OP_29(0x6F, 0x2, 0x7)
    OP_29(0x6F, 0x2, 0x8)
    OP_29(0x6F, 0x2, 0x9)
    OP_29(0x6F, 0x2, 0xA)
    OP_29(0x6F, 0x2, 0xB)
    OP_29(0x6F, 0x2, 0xC)
    OP_29(0x6F, 0x2, 0xD)
    OP_29(0x6F, 0x2, 0xE)
    OP_29(0x6F, 0x2, 0xF)
    OP_29(0x6F, 0x2, 0x10)
    OP_29(0x6F, 0x2, 0x11)
    OP_29(0x6F, 0x2, 0x12)
    OP_29(0x6F, 0x2, 0x13)
    OP_29(0x6F, 0x2, 0x14)
    OP_29(0x6F, 0x2, 0x15)
    OP_29(0x6F, 0x2, 0x16)
    OP_29(0x6F, 0x2, 0x17)
    OP_29(0x6F, 0x2, 0x18)
    OP_29(0x6F, 0x2, 0x19)
    OP_29(0x6F, 0x2, 0x1A)
    OP_29(0x6F, 0x2, 0x1B)
    OP_29(0x6F, 0x2, 0x1C)
    OP_29(0x6F, 0x2, 0x1D)
    OP_29(0x6F, 0x2, 0x1E)
    OP_29(0x6F, 0x2, 0x1F)

    label("loc_ADD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ADEB")
    OP_29(0x6F, 0x4, 0x2)

    label("loc_ADEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE00")
    OP_29(0x6F, 0x1, 0x0)

    label("loc_AE00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE15")
    OP_29(0x6F, 0x1, 0x1)

    label("loc_AE15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE2A")
    OP_29(0x6F, 0x1, 0x2)

    label("loc_AE2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE3F")
    OP_29(0x6F, 0x1, 0x3)

    label("loc_AE3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE54")
    OP_29(0x6F, 0x1, 0x4)

    label("loc_AE54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE69")
    OP_29(0x6F, 0x1, 0x5)

    label("loc_AE69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE7E")
    OP_29(0x6F, 0x1, 0x6)

    label("loc_AE7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AE93")
    OP_29(0x6F, 0x1, 0x7)

    label("loc_AE93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AEA8")
    OP_29(0x6F, 0x1, 0x8)

    label("loc_AEA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AEBD")
    OP_29(0x6F, 0x1, 0x9)

    label("loc_AEBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AED2")
    OP_29(0x6F, 0x1, 0xA)

    label("loc_AED2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AEE7")
    OP_29(0x6F, 0x1, 0xB)

    label("loc_AEE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AEFB")
    OP_29(0x6F, 0x4, 0x10)

    label("loc_AEFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AF0F")
    OP_29(0x6F, 0x4, 0x20)

    label("loc_AF0F")

    Jump("loc_CB36")

    label("loc_AF14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B001")
    OP_29(0x70, 0x3, 0x0)
    OP_29(0x70, 0x3, 0x1)
    OP_29(0x70, 0x3, 0x2)
    OP_29(0x70, 0x3, 0x10)
    OP_29(0x70, 0x3, 0x20)
    OP_29(0x70, 0x3, 0x40)
    OP_29(0x70, 0x2, 0x0)
    OP_29(0x70, 0x2, 0x1)
    OP_29(0x70, 0x2, 0x2)
    OP_29(0x70, 0x2, 0x3)
    OP_29(0x70, 0x2, 0x4)
    OP_29(0x70, 0x2, 0x5)
    OP_29(0x70, 0x2, 0x6)
    OP_29(0x70, 0x2, 0x7)
    OP_29(0x70, 0x2, 0x8)
    OP_29(0x70, 0x2, 0x9)
    OP_29(0x70, 0x2, 0xA)
    OP_29(0x70, 0x2, 0xB)
    OP_29(0x70, 0x2, 0xC)
    OP_29(0x70, 0x2, 0xD)
    OP_29(0x70, 0x2, 0xE)
    OP_29(0x70, 0x2, 0xF)
    OP_29(0x70, 0x2, 0x10)
    OP_29(0x70, 0x2, 0x11)
    OP_29(0x70, 0x2, 0x12)
    OP_29(0x70, 0x2, 0x13)
    OP_29(0x70, 0x2, 0x14)
    OP_29(0x70, 0x2, 0x15)
    OP_29(0x70, 0x2, 0x16)
    OP_29(0x70, 0x2, 0x17)
    OP_29(0x70, 0x2, 0x18)
    OP_29(0x70, 0x2, 0x19)
    OP_29(0x70, 0x2, 0x1A)
    OP_29(0x70, 0x2, 0x1B)
    OP_29(0x70, 0x2, 0x1C)
    OP_29(0x70, 0x2, 0x1D)
    OP_29(0x70, 0x2, 0x1E)
    OP_29(0x70, 0x2, 0x1F)

    label("loc_B001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B015")
    OP_29(0x70, 0x4, 0x2)

    label("loc_B015")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B02A")
    OP_29(0x70, 0x1, 0x0)

    label("loc_B02A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B03F")
    OP_29(0x70, 0x1, 0x1)

    label("loc_B03F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B054")
    OP_29(0x70, 0x1, 0x2)

    label("loc_B054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B069")
    OP_29(0x70, 0x1, 0x3)

    label("loc_B069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B07E")
    OP_29(0x70, 0x1, 0x4)

    label("loc_B07E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B093")
    OP_29(0x70, 0x1, 0x5)

    label("loc_B093")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B0A8")
    OP_29(0x70, 0x1, 0x6)

    label("loc_B0A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B0BD")
    OP_29(0x70, 0x1, 0x7)

    label("loc_B0BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B0D2")
    OP_29(0x70, 0x1, 0x8)

    label("loc_B0D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B0E7")
    OP_29(0x70, 0x1, 0x9)

    label("loc_B0E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B0FC")
    OP_29(0x70, 0x1, 0xA)

    label("loc_B0FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B111")
    OP_29(0x70, 0x1, 0xB)

    label("loc_B111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B125")
    OP_29(0x70, 0x4, 0x10)

    label("loc_B125")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B139")
    OP_29(0x70, 0x4, 0x20)

    label("loc_B139")

    Jump("loc_CB36")

    label("loc_B13E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B22B")
    OP_29(0x71, 0x3, 0x0)
    OP_29(0x71, 0x3, 0x1)
    OP_29(0x71, 0x3, 0x2)
    OP_29(0x71, 0x3, 0x10)
    OP_29(0x71, 0x3, 0x20)
    OP_29(0x71, 0x3, 0x40)
    OP_29(0x71, 0x2, 0x0)
    OP_29(0x71, 0x2, 0x1)
    OP_29(0x71, 0x2, 0x2)
    OP_29(0x71, 0x2, 0x3)
    OP_29(0x71, 0x2, 0x4)
    OP_29(0x71, 0x2, 0x5)
    OP_29(0x71, 0x2, 0x6)
    OP_29(0x71, 0x2, 0x7)
    OP_29(0x71, 0x2, 0x8)
    OP_29(0x71, 0x2, 0x9)
    OP_29(0x71, 0x2, 0xA)
    OP_29(0x71, 0x2, 0xB)
    OP_29(0x71, 0x2, 0xC)
    OP_29(0x71, 0x2, 0xD)
    OP_29(0x71, 0x2, 0xE)
    OP_29(0x71, 0x2, 0xF)
    OP_29(0x71, 0x2, 0x10)
    OP_29(0x71, 0x2, 0x11)
    OP_29(0x71, 0x2, 0x12)
    OP_29(0x71, 0x2, 0x13)
    OP_29(0x71, 0x2, 0x14)
    OP_29(0x71, 0x2, 0x15)
    OP_29(0x71, 0x2, 0x16)
    OP_29(0x71, 0x2, 0x17)
    OP_29(0x71, 0x2, 0x18)
    OP_29(0x71, 0x2, 0x19)
    OP_29(0x71, 0x2, 0x1A)
    OP_29(0x71, 0x2, 0x1B)
    OP_29(0x71, 0x2, 0x1C)
    OP_29(0x71, 0x2, 0x1D)
    OP_29(0x71, 0x2, 0x1E)
    OP_29(0x71, 0x2, 0x1F)

    label("loc_B22B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B23F")
    OP_29(0x71, 0x4, 0x2)

    label("loc_B23F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B254")
    OP_29(0x71, 0x1, 0x0)

    label("loc_B254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B269")
    OP_29(0x71, 0x1, 0x1)

    label("loc_B269")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B27E")
    OP_29(0x71, 0x1, 0x2)

    label("loc_B27E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B293")
    OP_29(0x71, 0x1, 0x3)

    label("loc_B293")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B2A8")
    OP_29(0x71, 0x1, 0x4)

    label("loc_B2A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B2BD")
    OP_29(0x71, 0x1, 0x5)

    label("loc_B2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B2D2")
    OP_29(0x71, 0x1, 0x6)

    label("loc_B2D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B2E7")
    OP_29(0x71, 0x1, 0x7)

    label("loc_B2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B2FC")
    OP_29(0x71, 0x1, 0x8)

    label("loc_B2FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B311")
    OP_29(0x71, 0x1, 0x9)

    label("loc_B311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B326")
    OP_29(0x71, 0x1, 0xA)

    label("loc_B326")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B33B")
    OP_29(0x71, 0x1, 0xB)

    label("loc_B33B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B34F")
    OP_29(0x71, 0x4, 0x10)

    label("loc_B34F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B363")
    OP_29(0x71, 0x4, 0x20)

    label("loc_B363")

    Jump("loc_CB36")

    label("loc_B368")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B455")
    OP_29(0x72, 0x3, 0x0)
    OP_29(0x72, 0x3, 0x1)
    OP_29(0x72, 0x3, 0x2)
    OP_29(0x72, 0x3, 0x10)
    OP_29(0x72, 0x3, 0x20)
    OP_29(0x72, 0x3, 0x40)
    OP_29(0x72, 0x2, 0x0)
    OP_29(0x72, 0x2, 0x1)
    OP_29(0x72, 0x2, 0x2)
    OP_29(0x72, 0x2, 0x3)
    OP_29(0x72, 0x2, 0x4)
    OP_29(0x72, 0x2, 0x5)
    OP_29(0x72, 0x2, 0x6)
    OP_29(0x72, 0x2, 0x7)
    OP_29(0x72, 0x2, 0x8)
    OP_29(0x72, 0x2, 0x9)
    OP_29(0x72, 0x2, 0xA)
    OP_29(0x72, 0x2, 0xB)
    OP_29(0x72, 0x2, 0xC)
    OP_29(0x72, 0x2, 0xD)
    OP_29(0x72, 0x2, 0xE)
    OP_29(0x72, 0x2, 0xF)
    OP_29(0x72, 0x2, 0x10)
    OP_29(0x72, 0x2, 0x11)
    OP_29(0x72, 0x2, 0x12)
    OP_29(0x72, 0x2, 0x13)
    OP_29(0x72, 0x2, 0x14)
    OP_29(0x72, 0x2, 0x15)
    OP_29(0x72, 0x2, 0x16)
    OP_29(0x72, 0x2, 0x17)
    OP_29(0x72, 0x2, 0x18)
    OP_29(0x72, 0x2, 0x19)
    OP_29(0x72, 0x2, 0x1A)
    OP_29(0x72, 0x2, 0x1B)
    OP_29(0x72, 0x2, 0x1C)
    OP_29(0x72, 0x2, 0x1D)
    OP_29(0x72, 0x2, 0x1E)
    OP_29(0x72, 0x2, 0x1F)

    label("loc_B455")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B469")
    OP_29(0x72, 0x4, 0x2)

    label("loc_B469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B47E")
    OP_29(0x72, 0x1, 0x0)

    label("loc_B47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B493")
    OP_29(0x72, 0x1, 0x1)

    label("loc_B493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B4A8")
    OP_29(0x72, 0x1, 0x2)

    label("loc_B4A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B4BD")
    OP_29(0x72, 0x1, 0x3)

    label("loc_B4BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B4D2")
    OP_29(0x72, 0x1, 0x4)

    label("loc_B4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B4E7")
    OP_29(0x72, 0x1, 0x5)

    label("loc_B4E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B4FC")
    OP_29(0x72, 0x1, 0x6)

    label("loc_B4FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B511")
    OP_29(0x72, 0x1, 0x7)

    label("loc_B511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B526")
    OP_29(0x72, 0x1, 0x8)

    label("loc_B526")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B53B")
    OP_29(0x72, 0x1, 0x9)

    label("loc_B53B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B550")
    OP_29(0x72, 0x1, 0xA)

    label("loc_B550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B565")
    OP_29(0x72, 0x1, 0xB)

    label("loc_B565")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B579")
    OP_29(0x72, 0x4, 0x10)

    label("loc_B579")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B58D")
    OP_29(0x72, 0x4, 0x20)

    label("loc_B58D")

    Jump("loc_CB36")

    label("loc_B592")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67F")
    OP_29(0x73, 0x3, 0x0)
    OP_29(0x73, 0x3, 0x1)
    OP_29(0x73, 0x3, 0x2)
    OP_29(0x73, 0x3, 0x10)
    OP_29(0x73, 0x3, 0x20)
    OP_29(0x73, 0x3, 0x40)
    OP_29(0x73, 0x2, 0x0)
    OP_29(0x73, 0x2, 0x1)
    OP_29(0x73, 0x2, 0x2)
    OP_29(0x73, 0x2, 0x3)
    OP_29(0x73, 0x2, 0x4)
    OP_29(0x73, 0x2, 0x5)
    OP_29(0x73, 0x2, 0x6)
    OP_29(0x73, 0x2, 0x7)
    OP_29(0x73, 0x2, 0x8)
    OP_29(0x73, 0x2, 0x9)
    OP_29(0x73, 0x2, 0xA)
    OP_29(0x73, 0x2, 0xB)
    OP_29(0x73, 0x2, 0xC)
    OP_29(0x73, 0x2, 0xD)
    OP_29(0x73, 0x2, 0xE)
    OP_29(0x73, 0x2, 0xF)
    OP_29(0x73, 0x2, 0x10)
    OP_29(0x73, 0x2, 0x11)
    OP_29(0x73, 0x2, 0x12)
    OP_29(0x73, 0x2, 0x13)
    OP_29(0x73, 0x2, 0x14)
    OP_29(0x73, 0x2, 0x15)
    OP_29(0x73, 0x2, 0x16)
    OP_29(0x73, 0x2, 0x17)
    OP_29(0x73, 0x2, 0x18)
    OP_29(0x73, 0x2, 0x19)
    OP_29(0x73, 0x2, 0x1A)
    OP_29(0x73, 0x2, 0x1B)
    OP_29(0x73, 0x2, 0x1C)
    OP_29(0x73, 0x2, 0x1D)
    OP_29(0x73, 0x2, 0x1E)
    OP_29(0x73, 0x2, 0x1F)

    label("loc_B67F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B693")
    OP_29(0x73, 0x4, 0x2)

    label("loc_B693")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B6A8")
    OP_29(0x73, 0x1, 0x0)

    label("loc_B6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B6BD")
    OP_29(0x73, 0x1, 0x1)

    label("loc_B6BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B6D2")
    OP_29(0x73, 0x1, 0x2)

    label("loc_B6D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B6E7")
    OP_29(0x73, 0x1, 0x3)

    label("loc_B6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B6FC")
    OP_29(0x73, 0x1, 0x4)

    label("loc_B6FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B711")
    OP_29(0x73, 0x1, 0x5)

    label("loc_B711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B726")
    OP_29(0x73, 0x1, 0x6)

    label("loc_B726")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B73B")
    OP_29(0x73, 0x1, 0x7)

    label("loc_B73B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B750")
    OP_29(0x73, 0x1, 0x8)

    label("loc_B750")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B765")
    OP_29(0x73, 0x1, 0x9)

    label("loc_B765")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B77A")
    OP_29(0x73, 0x1, 0xA)

    label("loc_B77A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B78F")
    OP_29(0x73, 0x1, 0xB)

    label("loc_B78F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B7A3")
    OP_29(0x73, 0x4, 0x10)

    label("loc_B7A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B7B7")
    OP_29(0x73, 0x4, 0x20)

    label("loc_B7B7")

    Jump("loc_CB36")

    label("loc_B7BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A9")
    OP_29(0x74, 0x3, 0x0)
    OP_29(0x74, 0x3, 0x1)
    OP_29(0x74, 0x3, 0x2)
    OP_29(0x74, 0x3, 0x10)
    OP_29(0x74, 0x3, 0x20)
    OP_29(0x74, 0x3, 0x40)
    OP_29(0x74, 0x2, 0x0)
    OP_29(0x74, 0x2, 0x1)
    OP_29(0x74, 0x2, 0x2)
    OP_29(0x74, 0x2, 0x3)
    OP_29(0x74, 0x2, 0x4)
    OP_29(0x74, 0x2, 0x5)
    OP_29(0x74, 0x2, 0x6)
    OP_29(0x74, 0x2, 0x7)
    OP_29(0x74, 0x2, 0x8)
    OP_29(0x74, 0x2, 0x9)
    OP_29(0x74, 0x2, 0xA)
    OP_29(0x74, 0x2, 0xB)
    OP_29(0x74, 0x2, 0xC)
    OP_29(0x74, 0x2, 0xD)
    OP_29(0x74, 0x2, 0xE)
    OP_29(0x74, 0x2, 0xF)
    OP_29(0x74, 0x2, 0x10)
    OP_29(0x74, 0x2, 0x11)
    OP_29(0x74, 0x2, 0x12)
    OP_29(0x74, 0x2, 0x13)
    OP_29(0x74, 0x2, 0x14)
    OP_29(0x74, 0x2, 0x15)
    OP_29(0x74, 0x2, 0x16)
    OP_29(0x74, 0x2, 0x17)
    OP_29(0x74, 0x2, 0x18)
    OP_29(0x74, 0x2, 0x19)
    OP_29(0x74, 0x2, 0x1A)
    OP_29(0x74, 0x2, 0x1B)
    OP_29(0x74, 0x2, 0x1C)
    OP_29(0x74, 0x2, 0x1D)
    OP_29(0x74, 0x2, 0x1E)
    OP_29(0x74, 0x2, 0x1F)

    label("loc_B8A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B8BD")
    OP_29(0x74, 0x4, 0x2)

    label("loc_B8BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B8D2")
    OP_29(0x74, 0x1, 0x0)

    label("loc_B8D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B8E7")
    OP_29(0x74, 0x1, 0x1)

    label("loc_B8E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B8FC")
    OP_29(0x74, 0x1, 0x2)

    label("loc_B8FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B911")
    OP_29(0x74, 0x1, 0x3)

    label("loc_B911")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B926")
    OP_29(0x74, 0x1, 0x4)

    label("loc_B926")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B93B")
    OP_29(0x74, 0x1, 0x5)

    label("loc_B93B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B950")
    OP_29(0x74, 0x1, 0x6)

    label("loc_B950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B965")
    OP_29(0x74, 0x1, 0x7)

    label("loc_B965")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B97A")
    OP_29(0x74, 0x1, 0x8)

    label("loc_B97A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B98F")
    OP_29(0x74, 0x1, 0x9)

    label("loc_B98F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B9A4")
    OP_29(0x74, 0x1, 0xA)

    label("loc_B9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B9B9")
    OP_29(0x74, 0x1, 0xB)

    label("loc_B9B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B9CD")
    OP_29(0x74, 0x4, 0x10)

    label("loc_B9CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B9E1")
    OP_29(0x74, 0x4, 0x20)

    label("loc_B9E1")

    Jump("loc_CB36")

    label("loc_B9E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAD3")
    OP_29(0x75, 0x3, 0x0)
    OP_29(0x75, 0x3, 0x1)
    OP_29(0x75, 0x3, 0x2)
    OP_29(0x75, 0x3, 0x10)
    OP_29(0x75, 0x3, 0x20)
    OP_29(0x75, 0x3, 0x40)
    OP_29(0x75, 0x2, 0x0)
    OP_29(0x75, 0x2, 0x1)
    OP_29(0x75, 0x2, 0x2)
    OP_29(0x75, 0x2, 0x3)
    OP_29(0x75, 0x2, 0x4)
    OP_29(0x75, 0x2, 0x5)
    OP_29(0x75, 0x2, 0x6)
    OP_29(0x75, 0x2, 0x7)
    OP_29(0x75, 0x2, 0x8)
    OP_29(0x75, 0x2, 0x9)
    OP_29(0x75, 0x2, 0xA)
    OP_29(0x75, 0x2, 0xB)
    OP_29(0x75, 0x2, 0xC)
    OP_29(0x75, 0x2, 0xD)
    OP_29(0x75, 0x2, 0xE)
    OP_29(0x75, 0x2, 0xF)
    OP_29(0x75, 0x2, 0x10)
    OP_29(0x75, 0x2, 0x11)
    OP_29(0x75, 0x2, 0x12)
    OP_29(0x75, 0x2, 0x13)
    OP_29(0x75, 0x2, 0x14)
    OP_29(0x75, 0x2, 0x15)
    OP_29(0x75, 0x2, 0x16)
    OP_29(0x75, 0x2, 0x17)
    OP_29(0x75, 0x2, 0x18)
    OP_29(0x75, 0x2, 0x19)
    OP_29(0x75, 0x2, 0x1A)
    OP_29(0x75, 0x2, 0x1B)
    OP_29(0x75, 0x2, 0x1C)
    OP_29(0x75, 0x2, 0x1D)
    OP_29(0x75, 0x2, 0x1E)
    OP_29(0x75, 0x2, 0x1F)

    label("loc_BAD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BAE7")
    OP_29(0x75, 0x4, 0x2)

    label("loc_BAE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BAFC")
    OP_29(0x75, 0x1, 0x0)

    label("loc_BAFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB11")
    OP_29(0x75, 0x1, 0x1)

    label("loc_BB11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB26")
    OP_29(0x75, 0x1, 0x2)

    label("loc_BB26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB3B")
    OP_29(0x75, 0x1, 0x3)

    label("loc_BB3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB50")
    OP_29(0x75, 0x1, 0x4)

    label("loc_BB50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB65")
    OP_29(0x75, 0x1, 0x5)

    label("loc_BB65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB7A")
    OP_29(0x75, 0x1, 0x6)

    label("loc_BB7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BB8F")
    OP_29(0x75, 0x1, 0x7)

    label("loc_BB8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBA4")
    OP_29(0x75, 0x1, 0x8)

    label("loc_BBA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBB9")
    OP_29(0x75, 0x1, 0x9)

    label("loc_BBB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBCE")
    OP_29(0x75, 0x1, 0xA)

    label("loc_BBCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBE3")
    OP_29(0x75, 0x1, 0xB)

    label("loc_BBE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBF7")
    OP_29(0x75, 0x4, 0x10)

    label("loc_BBF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BC0B")
    OP_29(0x75, 0x4, 0x20)

    label("loc_BC0B")

    Jump("loc_CB36")

    label("loc_BC10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCFD")
    OP_29(0x76, 0x3, 0x0)
    OP_29(0x76, 0x3, 0x1)
    OP_29(0x76, 0x3, 0x2)
    OP_29(0x76, 0x3, 0x10)
    OP_29(0x76, 0x3, 0x20)
    OP_29(0x76, 0x3, 0x40)
    OP_29(0x76, 0x2, 0x0)
    OP_29(0x76, 0x2, 0x1)
    OP_29(0x76, 0x2, 0x2)
    OP_29(0x76, 0x2, 0x3)
    OP_29(0x76, 0x2, 0x4)
    OP_29(0x76, 0x2, 0x5)
    OP_29(0x76, 0x2, 0x6)
    OP_29(0x76, 0x2, 0x7)
    OP_29(0x76, 0x2, 0x8)
    OP_29(0x76, 0x2, 0x9)
    OP_29(0x76, 0x2, 0xA)
    OP_29(0x76, 0x2, 0xB)
    OP_29(0x76, 0x2, 0xC)
    OP_29(0x76, 0x2, 0xD)
    OP_29(0x76, 0x2, 0xE)
    OP_29(0x76, 0x2, 0xF)
    OP_29(0x76, 0x2, 0x10)
    OP_29(0x76, 0x2, 0x11)
    OP_29(0x76, 0x2, 0x12)
    OP_29(0x76, 0x2, 0x13)
    OP_29(0x76, 0x2, 0x14)
    OP_29(0x76, 0x2, 0x15)
    OP_29(0x76, 0x2, 0x16)
    OP_29(0x76, 0x2, 0x17)
    OP_29(0x76, 0x2, 0x18)
    OP_29(0x76, 0x2, 0x19)
    OP_29(0x76, 0x2, 0x1A)
    OP_29(0x76, 0x2, 0x1B)
    OP_29(0x76, 0x2, 0x1C)
    OP_29(0x76, 0x2, 0x1D)
    OP_29(0x76, 0x2, 0x1E)
    OP_29(0x76, 0x2, 0x1F)

    label("loc_BCFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD11")
    OP_29(0x76, 0x4, 0x2)

    label("loc_BD11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD26")
    OP_29(0x76, 0x1, 0x0)

    label("loc_BD26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD3B")
    OP_29(0x76, 0x1, 0x1)

    label("loc_BD3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD50")
    OP_29(0x76, 0x1, 0x2)

    label("loc_BD50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD65")
    OP_29(0x76, 0x1, 0x3)

    label("loc_BD65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD7A")
    OP_29(0x76, 0x1, 0x4)

    label("loc_BD7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD8F")
    OP_29(0x76, 0x1, 0x5)

    label("loc_BD8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BDA4")
    OP_29(0x76, 0x1, 0x6)

    label("loc_BDA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BDB9")
    OP_29(0x76, 0x1, 0x7)

    label("loc_BDB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BDCE")
    OP_29(0x76, 0x1, 0x8)

    label("loc_BDCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BDE3")
    OP_29(0x76, 0x1, 0x9)

    label("loc_BDE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BDF8")
    OP_29(0x76, 0x1, 0xA)

    label("loc_BDF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE0D")
    OP_29(0x76, 0x1, 0xB)

    label("loc_BE0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE21")
    OP_29(0x76, 0x4, 0x10)

    label("loc_BE21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE35")
    OP_29(0x76, 0x4, 0x20)

    label("loc_BE35")

    Jump("loc_CB36")

    label("loc_BE3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF27")
    OP_29(0x77, 0x3, 0x0)
    OP_29(0x77, 0x3, 0x1)
    OP_29(0x77, 0x3, 0x2)
    OP_29(0x77, 0x3, 0x10)
    OP_29(0x77, 0x3, 0x20)
    OP_29(0x77, 0x3, 0x40)
    OP_29(0x77, 0x2, 0x0)
    OP_29(0x77, 0x2, 0x1)
    OP_29(0x77, 0x2, 0x2)
    OP_29(0x77, 0x2, 0x3)
    OP_29(0x77, 0x2, 0x4)
    OP_29(0x77, 0x2, 0x5)
    OP_29(0x77, 0x2, 0x6)
    OP_29(0x77, 0x2, 0x7)
    OP_29(0x77, 0x2, 0x8)
    OP_29(0x77, 0x2, 0x9)
    OP_29(0x77, 0x2, 0xA)
    OP_29(0x77, 0x2, 0xB)
    OP_29(0x77, 0x2, 0xC)
    OP_29(0x77, 0x2, 0xD)
    OP_29(0x77, 0x2, 0xE)
    OP_29(0x77, 0x2, 0xF)
    OP_29(0x77, 0x2, 0x10)
    OP_29(0x77, 0x2, 0x11)
    OP_29(0x77, 0x2, 0x12)
    OP_29(0x77, 0x2, 0x13)
    OP_29(0x77, 0x2, 0x14)
    OP_29(0x77, 0x2, 0x15)
    OP_29(0x77, 0x2, 0x16)
    OP_29(0x77, 0x2, 0x17)
    OP_29(0x77, 0x2, 0x18)
    OP_29(0x77, 0x2, 0x19)
    OP_29(0x77, 0x2, 0x1A)
    OP_29(0x77, 0x2, 0x1B)
    OP_29(0x77, 0x2, 0x1C)
    OP_29(0x77, 0x2, 0x1D)
    OP_29(0x77, 0x2, 0x1E)
    OP_29(0x77, 0x2, 0x1F)

    label("loc_BF27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF3B")
    OP_29(0x77, 0x4, 0x2)

    label("loc_BF3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF50")
    OP_29(0x77, 0x1, 0x0)

    label("loc_BF50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF65")
    OP_29(0x77, 0x1, 0x1)

    label("loc_BF65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF7A")
    OP_29(0x77, 0x1, 0x2)

    label("loc_BF7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF8F")
    OP_29(0x77, 0x1, 0x3)

    label("loc_BF8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFA4")
    OP_29(0x77, 0x1, 0x4)

    label("loc_BFA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFB9")
    OP_29(0x77, 0x1, 0x5)

    label("loc_BFB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFCE")
    OP_29(0x77, 0x1, 0x6)

    label("loc_BFCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFE3")
    OP_29(0x77, 0x1, 0x7)

    label("loc_BFE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BFF8")
    OP_29(0x77, 0x1, 0x8)

    label("loc_BFF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C00D")
    OP_29(0x77, 0x1, 0x9)

    label("loc_C00D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C022")
    OP_29(0x77, 0x1, 0xA)

    label("loc_C022")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C037")
    OP_29(0x77, 0x1, 0xB)

    label("loc_C037")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C04B")
    OP_29(0x77, 0x4, 0x10)

    label("loc_C04B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C05F")
    OP_29(0x77, 0x4, 0x20)

    label("loc_C05F")

    Jump("loc_CB36")

    label("loc_C064")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C151")
    OP_29(0x78, 0x3, 0x0)
    OP_29(0x78, 0x3, 0x1)
    OP_29(0x78, 0x3, 0x2)
    OP_29(0x78, 0x3, 0x10)
    OP_29(0x78, 0x3, 0x20)
    OP_29(0x78, 0x3, 0x40)
    OP_29(0x78, 0x2, 0x0)
    OP_29(0x78, 0x2, 0x1)
    OP_29(0x78, 0x2, 0x2)
    OP_29(0x78, 0x2, 0x3)
    OP_29(0x78, 0x2, 0x4)
    OP_29(0x78, 0x2, 0x5)
    OP_29(0x78, 0x2, 0x6)
    OP_29(0x78, 0x2, 0x7)
    OP_29(0x78, 0x2, 0x8)
    OP_29(0x78, 0x2, 0x9)
    OP_29(0x78, 0x2, 0xA)
    OP_29(0x78, 0x2, 0xB)
    OP_29(0x78, 0x2, 0xC)
    OP_29(0x78, 0x2, 0xD)
    OP_29(0x78, 0x2, 0xE)
    OP_29(0x78, 0x2, 0xF)
    OP_29(0x78, 0x2, 0x10)
    OP_29(0x78, 0x2, 0x11)
    OP_29(0x78, 0x2, 0x12)
    OP_29(0x78, 0x2, 0x13)
    OP_29(0x78, 0x2, 0x14)
    OP_29(0x78, 0x2, 0x15)
    OP_29(0x78, 0x2, 0x16)
    OP_29(0x78, 0x2, 0x17)
    OP_29(0x78, 0x2, 0x18)
    OP_29(0x78, 0x2, 0x19)
    OP_29(0x78, 0x2, 0x1A)
    OP_29(0x78, 0x2, 0x1B)
    OP_29(0x78, 0x2, 0x1C)
    OP_29(0x78, 0x2, 0x1D)
    OP_29(0x78, 0x2, 0x1E)
    OP_29(0x78, 0x2, 0x1F)

    label("loc_C151")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C165")
    OP_29(0x78, 0x4, 0x2)

    label("loc_C165")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C17A")
    OP_29(0x78, 0x1, 0x0)

    label("loc_C17A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C18F")
    OP_29(0x78, 0x1, 0x1)

    label("loc_C18F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1A4")
    OP_29(0x78, 0x1, 0x2)

    label("loc_C1A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1B9")
    OP_29(0x78, 0x1, 0x3)

    label("loc_C1B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1CE")
    OP_29(0x78, 0x1, 0x4)

    label("loc_C1CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1E3")
    OP_29(0x78, 0x1, 0x5)

    label("loc_C1E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1F8")
    OP_29(0x78, 0x1, 0x6)

    label("loc_C1F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C20D")
    OP_29(0x78, 0x1, 0x7)

    label("loc_C20D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C222")
    OP_29(0x78, 0x1, 0x8)

    label("loc_C222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C237")
    OP_29(0x78, 0x1, 0x9)

    label("loc_C237")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C24C")
    OP_29(0x78, 0x1, 0xA)

    label("loc_C24C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C261")
    OP_29(0x78, 0x1, 0xB)

    label("loc_C261")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C275")
    OP_29(0x78, 0x4, 0x10)

    label("loc_C275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C289")
    OP_29(0x78, 0x4, 0x20)

    label("loc_C289")

    Jump("loc_CB36")

    label("loc_C28E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C37B")
    OP_29(0x79, 0x3, 0x0)
    OP_29(0x79, 0x3, 0x1)
    OP_29(0x79, 0x3, 0x2)
    OP_29(0x79, 0x3, 0x10)
    OP_29(0x79, 0x3, 0x20)
    OP_29(0x79, 0x3, 0x40)
    OP_29(0x79, 0x2, 0x0)
    OP_29(0x79, 0x2, 0x1)
    OP_29(0x79, 0x2, 0x2)
    OP_29(0x79, 0x2, 0x3)
    OP_29(0x79, 0x2, 0x4)
    OP_29(0x79, 0x2, 0x5)
    OP_29(0x79, 0x2, 0x6)
    OP_29(0x79, 0x2, 0x7)
    OP_29(0x79, 0x2, 0x8)
    OP_29(0x79, 0x2, 0x9)
    OP_29(0x79, 0x2, 0xA)
    OP_29(0x79, 0x2, 0xB)
    OP_29(0x79, 0x2, 0xC)
    OP_29(0x79, 0x2, 0xD)
    OP_29(0x79, 0x2, 0xE)
    OP_29(0x79, 0x2, 0xF)
    OP_29(0x79, 0x2, 0x10)
    OP_29(0x79, 0x2, 0x11)
    OP_29(0x79, 0x2, 0x12)
    OP_29(0x79, 0x2, 0x13)
    OP_29(0x79, 0x2, 0x14)
    OP_29(0x79, 0x2, 0x15)
    OP_29(0x79, 0x2, 0x16)
    OP_29(0x79, 0x2, 0x17)
    OP_29(0x79, 0x2, 0x18)
    OP_29(0x79, 0x2, 0x19)
    OP_29(0x79, 0x2, 0x1A)
    OP_29(0x79, 0x2, 0x1B)
    OP_29(0x79, 0x2, 0x1C)
    OP_29(0x79, 0x2, 0x1D)
    OP_29(0x79, 0x2, 0x1E)
    OP_29(0x79, 0x2, 0x1F)

    label("loc_C37B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C38F")
    OP_29(0x79, 0x4, 0x2)

    label("loc_C38F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3A4")
    OP_29(0x79, 0x1, 0x0)

    label("loc_C3A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3B9")
    OP_29(0x79, 0x1, 0x1)

    label("loc_C3B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3CE")
    OP_29(0x79, 0x1, 0x2)

    label("loc_C3CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3E3")
    OP_29(0x79, 0x1, 0x3)

    label("loc_C3E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3F8")
    OP_29(0x79, 0x1, 0x4)

    label("loc_C3F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C40D")
    OP_29(0x79, 0x1, 0x5)

    label("loc_C40D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C422")
    OP_29(0x79, 0x1, 0x6)

    label("loc_C422")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C437")
    OP_29(0x79, 0x1, 0x7)

    label("loc_C437")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C44C")
    OP_29(0x79, 0x1, 0x8)

    label("loc_C44C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C461")
    OP_29(0x79, 0x1, 0x9)

    label("loc_C461")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C476")
    OP_29(0x79, 0x1, 0xA)

    label("loc_C476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C48B")
    OP_29(0x79, 0x1, 0xB)

    label("loc_C48B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C49F")
    OP_29(0x79, 0x4, 0x10)

    label("loc_C49F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4B3")
    OP_29(0x79, 0x4, 0x20)

    label("loc_C4B3")

    Jump("loc_CB36")

    label("loc_C4B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5A5")
    OP_29(0x7A, 0x3, 0x0)
    OP_29(0x7A, 0x3, 0x1)
    OP_29(0x7A, 0x3, 0x2)
    OP_29(0x7A, 0x3, 0x10)
    OP_29(0x7A, 0x3, 0x20)
    OP_29(0x7A, 0x3, 0x40)
    OP_29(0x7A, 0x2, 0x0)
    OP_29(0x7A, 0x2, 0x1)
    OP_29(0x7A, 0x2, 0x2)
    OP_29(0x7A, 0x2, 0x3)
    OP_29(0x7A, 0x2, 0x4)
    OP_29(0x7A, 0x2, 0x5)
    OP_29(0x7A, 0x2, 0x6)
    OP_29(0x7A, 0x2, 0x7)
    OP_29(0x7A, 0x2, 0x8)
    OP_29(0x7A, 0x2, 0x9)
    OP_29(0x7A, 0x2, 0xA)
    OP_29(0x7A, 0x2, 0xB)
    OP_29(0x7A, 0x2, 0xC)
    OP_29(0x7A, 0x2, 0xD)
    OP_29(0x7A, 0x2, 0xE)
    OP_29(0x7A, 0x2, 0xF)
    OP_29(0x7A, 0x2, 0x10)
    OP_29(0x7A, 0x2, 0x11)
    OP_29(0x7A, 0x2, 0x12)
    OP_29(0x7A, 0x2, 0x13)
    OP_29(0x7A, 0x2, 0x14)
    OP_29(0x7A, 0x2, 0x15)
    OP_29(0x7A, 0x2, 0x16)
    OP_29(0x7A, 0x2, 0x17)
    OP_29(0x7A, 0x2, 0x18)
    OP_29(0x7A, 0x2, 0x19)
    OP_29(0x7A, 0x2, 0x1A)
    OP_29(0x7A, 0x2, 0x1B)
    OP_29(0x7A, 0x2, 0x1C)
    OP_29(0x7A, 0x2, 0x1D)
    OP_29(0x7A, 0x2, 0x1E)
    OP_29(0x7A, 0x2, 0x1F)

    label("loc_C5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5B9")
    OP_29(0x7A, 0x4, 0x2)

    label("loc_C5B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5CE")
    OP_29(0x7A, 0x1, 0x0)

    label("loc_C5CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5E3")
    OP_29(0x7A, 0x1, 0x1)

    label("loc_C5E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5F8")
    OP_29(0x7A, 0x1, 0x2)

    label("loc_C5F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C60D")
    OP_29(0x7A, 0x1, 0x3)

    label("loc_C60D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C622")
    OP_29(0x7A, 0x1, 0x4)

    label("loc_C622")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C637")
    OP_29(0x7A, 0x1, 0x5)

    label("loc_C637")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C64C")
    OP_29(0x7A, 0x1, 0x6)

    label("loc_C64C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C661")
    OP_29(0x7A, 0x1, 0x7)

    label("loc_C661")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C676")
    OP_29(0x7A, 0x1, 0x8)

    label("loc_C676")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C68B")
    OP_29(0x7A, 0x1, 0x9)

    label("loc_C68B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6A0")
    OP_29(0x7A, 0x1, 0xA)

    label("loc_C6A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6B5")
    OP_29(0x7A, 0x1, 0xB)

    label("loc_C6B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6C9")
    OP_29(0x7A, 0x4, 0x10)

    label("loc_C6C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C6DD")
    OP_29(0x7A, 0x4, 0x20)

    label("loc_C6DD")

    Jump("loc_CB36")

    label("loc_C6E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7CF")
    OP_29(0x7B, 0x3, 0x0)
    OP_29(0x7B, 0x3, 0x1)
    OP_29(0x7B, 0x3, 0x2)
    OP_29(0x7B, 0x3, 0x10)
    OP_29(0x7B, 0x3, 0x20)
    OP_29(0x7B, 0x3, 0x40)
    OP_29(0x7B, 0x2, 0x0)
    OP_29(0x7B, 0x2, 0x1)
    OP_29(0x7B, 0x2, 0x2)
    OP_29(0x7B, 0x2, 0x3)
    OP_29(0x7B, 0x2, 0x4)
    OP_29(0x7B, 0x2, 0x5)
    OP_29(0x7B, 0x2, 0x6)
    OP_29(0x7B, 0x2, 0x7)
    OP_29(0x7B, 0x2, 0x8)
    OP_29(0x7B, 0x2, 0x9)
    OP_29(0x7B, 0x2, 0xA)
    OP_29(0x7B, 0x2, 0xB)
    OP_29(0x7B, 0x2, 0xC)
    OP_29(0x7B, 0x2, 0xD)
    OP_29(0x7B, 0x2, 0xE)
    OP_29(0x7B, 0x2, 0xF)
    OP_29(0x7B, 0x2, 0x10)
    OP_29(0x7B, 0x2, 0x11)
    OP_29(0x7B, 0x2, 0x12)
    OP_29(0x7B, 0x2, 0x13)
    OP_29(0x7B, 0x2, 0x14)
    OP_29(0x7B, 0x2, 0x15)
    OP_29(0x7B, 0x2, 0x16)
    OP_29(0x7B, 0x2, 0x17)
    OP_29(0x7B, 0x2, 0x18)
    OP_29(0x7B, 0x2, 0x19)
    OP_29(0x7B, 0x2, 0x1A)
    OP_29(0x7B, 0x2, 0x1B)
    OP_29(0x7B, 0x2, 0x1C)
    OP_29(0x7B, 0x2, 0x1D)
    OP_29(0x7B, 0x2, 0x1E)
    OP_29(0x7B, 0x2, 0x1F)

    label("loc_C7CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7E3")
    OP_29(0x7B, 0x4, 0x2)

    label("loc_C7E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7F8")
    OP_29(0x7B, 0x1, 0x0)

    label("loc_C7F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C80D")
    OP_29(0x7B, 0x1, 0x1)

    label("loc_C80D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C822")
    OP_29(0x7B, 0x1, 0x2)

    label("loc_C822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C837")
    OP_29(0x7B, 0x1, 0x3)

    label("loc_C837")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C84C")
    OP_29(0x7B, 0x1, 0x4)

    label("loc_C84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C861")
    OP_29(0x7B, 0x1, 0x5)

    label("loc_C861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C876")
    OP_29(0x7B, 0x1, 0x6)

    label("loc_C876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C88B")
    OP_29(0x7B, 0x1, 0x7)

    label("loc_C88B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8A0")
    OP_29(0x7B, 0x1, 0x8)

    label("loc_C8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8B5")
    OP_29(0x7B, 0x1, 0x9)

    label("loc_C8B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8CA")
    OP_29(0x7B, 0x1, 0xA)

    label("loc_C8CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8DF")
    OP_29(0x7B, 0x1, 0xB)

    label("loc_C8DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C8F3")
    OP_29(0x7B, 0x4, 0x10)

    label("loc_C8F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C907")
    OP_29(0x7B, 0x4, 0x20)

    label("loc_C907")

    Jump("loc_CB36")

    label("loc_C90C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9F9")
    OP_29(0x7C, 0x3, 0x0)
    OP_29(0x7C, 0x3, 0x1)
    OP_29(0x7C, 0x3, 0x2)
    OP_29(0x7C, 0x3, 0x10)
    OP_29(0x7C, 0x3, 0x20)
    OP_29(0x7C, 0x3, 0x40)
    OP_29(0x7C, 0x2, 0x0)
    OP_29(0x7C, 0x2, 0x1)
    OP_29(0x7C, 0x2, 0x2)
    OP_29(0x7C, 0x2, 0x3)
    OP_29(0x7C, 0x2, 0x4)
    OP_29(0x7C, 0x2, 0x5)
    OP_29(0x7C, 0x2, 0x6)
    OP_29(0x7C, 0x2, 0x7)
    OP_29(0x7C, 0x2, 0x8)
    OP_29(0x7C, 0x2, 0x9)
    OP_29(0x7C, 0x2, 0xA)
    OP_29(0x7C, 0x2, 0xB)
    OP_29(0x7C, 0x2, 0xC)
    OP_29(0x7C, 0x2, 0xD)
    OP_29(0x7C, 0x2, 0xE)
    OP_29(0x7C, 0x2, 0xF)
    OP_29(0x7C, 0x2, 0x10)
    OP_29(0x7C, 0x2, 0x11)
    OP_29(0x7C, 0x2, 0x12)
    OP_29(0x7C, 0x2, 0x13)
    OP_29(0x7C, 0x2, 0x14)
    OP_29(0x7C, 0x2, 0x15)
    OP_29(0x7C, 0x2, 0x16)
    OP_29(0x7C, 0x2, 0x17)
    OP_29(0x7C, 0x2, 0x18)
    OP_29(0x7C, 0x2, 0x19)
    OP_29(0x7C, 0x2, 0x1A)
    OP_29(0x7C, 0x2, 0x1B)
    OP_29(0x7C, 0x2, 0x1C)
    OP_29(0x7C, 0x2, 0x1D)
    OP_29(0x7C, 0x2, 0x1E)
    OP_29(0x7C, 0x2, 0x1F)

    label("loc_C9F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA0D")
    OP_29(0x7C, 0x4, 0x2)

    label("loc_CA0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA22")
    OP_29(0x7C, 0x1, 0x0)

    label("loc_CA22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA37")
    OP_29(0x7C, 0x1, 0x1)

    label("loc_CA37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA4C")
    OP_29(0x7C, 0x1, 0x2)

    label("loc_CA4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA61")
    OP_29(0x7C, 0x1, 0x3)

    label("loc_CA61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA76")
    OP_29(0x7C, 0x1, 0x4)

    label("loc_CA76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA8B")
    OP_29(0x7C, 0x1, 0x5)

    label("loc_CA8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CAA0")
    OP_29(0x7C, 0x1, 0x6)

    label("loc_CAA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CAB5")
    OP_29(0x7C, 0x1, 0x7)

    label("loc_CAB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CACA")
    OP_29(0x7C, 0x1, 0x8)

    label("loc_CACA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CADF")
    OP_29(0x7C, 0x1, 0x9)

    label("loc_CADF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CAF4")
    OP_29(0x7C, 0x1, 0xA)

    label("loc_CAF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB09")
    OP_29(0x7C, 0x1, 0xB)

    label("loc_CB09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB1D")
    OP_29(0x7C, 0x4, 0x10)

    label("loc_CB1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB31")
    OP_29(0x7C, 0x4, 0x20)

    label("loc_CB31")

    Jump("loc_CB36")

    label("loc_CB36")

    Jump("loc_A9FD")

    label("loc_CB3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_50_A9F3 end


    label("Function_51_CB53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D31B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "QS_1251  盗まれた宝飾品\x01",          # 0
            "QS_1252  切り裂き事件の捜査\x01",      # 1
            "QS_1254  隠れみっしぃ探し\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CBE2"),
        (1, "loc_CBE2"),
        (2, "loc_CBE2"),
        (SWITCH_DEFAULT, "loc_CC5B"),
    )


    label("loc_CBE2")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x4)
    Jump("loc_CC6A")

    label("loc_CC5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC6A")

    label("loc_CC6A")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D316")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CC98"),
        (1, "loc_CEC2"),
        (2, "loc_D0EC"),
        (SWITCH_DEFAULT, "loc_D316"),
    )


    label("loc_CC98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD85")
    OP_29(0x7D, 0x3, 0x0)
    OP_29(0x7D, 0x3, 0x1)
    OP_29(0x7D, 0x3, 0x2)
    OP_29(0x7D, 0x3, 0x10)
    OP_29(0x7D, 0x3, 0x20)
    OP_29(0x7D, 0x3, 0x40)
    OP_29(0x7D, 0x2, 0x0)
    OP_29(0x7D, 0x2, 0x1)
    OP_29(0x7D, 0x2, 0x2)
    OP_29(0x7D, 0x2, 0x3)
    OP_29(0x7D, 0x2, 0x4)
    OP_29(0x7D, 0x2, 0x5)
    OP_29(0x7D, 0x2, 0x6)
    OP_29(0x7D, 0x2, 0x7)
    OP_29(0x7D, 0x2, 0x8)
    OP_29(0x7D, 0x2, 0x9)
    OP_29(0x7D, 0x2, 0xA)
    OP_29(0x7D, 0x2, 0xB)
    OP_29(0x7D, 0x2, 0xC)
    OP_29(0x7D, 0x2, 0xD)
    OP_29(0x7D, 0x2, 0xE)
    OP_29(0x7D, 0x2, 0xF)
    OP_29(0x7D, 0x2, 0x10)
    OP_29(0x7D, 0x2, 0x11)
    OP_29(0x7D, 0x2, 0x12)
    OP_29(0x7D, 0x2, 0x13)
    OP_29(0x7D, 0x2, 0x14)
    OP_29(0x7D, 0x2, 0x15)
    OP_29(0x7D, 0x2, 0x16)
    OP_29(0x7D, 0x2, 0x17)
    OP_29(0x7D, 0x2, 0x18)
    OP_29(0x7D, 0x2, 0x19)
    OP_29(0x7D, 0x2, 0x1A)
    OP_29(0x7D, 0x2, 0x1B)
    OP_29(0x7D, 0x2, 0x1C)
    OP_29(0x7D, 0x2, 0x1D)
    OP_29(0x7D, 0x2, 0x1E)
    OP_29(0x7D, 0x2, 0x1F)

    label("loc_CD85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD99")
    OP_29(0x7D, 0x4, 0x2)

    label("loc_CD99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDAE")
    OP_29(0x7D, 0x1, 0x0)

    label("loc_CDAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDC3")
    OP_29(0x7D, 0x1, 0x1)

    label("loc_CDC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDD8")
    OP_29(0x7D, 0x1, 0x2)

    label("loc_CDD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDED")
    OP_29(0x7D, 0x1, 0x3)

    label("loc_CDED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE02")
    OP_29(0x7D, 0x1, 0x4)

    label("loc_CE02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE17")
    OP_29(0x7D, 0x1, 0x5)

    label("loc_CE17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE2C")
    OP_29(0x7D, 0x1, 0x6)

    label("loc_CE2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE41")
    OP_29(0x7D, 0x1, 0x7)

    label("loc_CE41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE56")
    OP_29(0x7D, 0x1, 0x8)

    label("loc_CE56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE6B")
    OP_29(0x7D, 0x1, 0x9)

    label("loc_CE6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE80")
    OP_29(0x7D, 0x1, 0xA)

    label("loc_CE80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE95")
    OP_29(0x7D, 0x1, 0xB)

    label("loc_CE95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEA9")
    OP_29(0x7D, 0x4, 0x10)

    label("loc_CEA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEBD")
    OP_29(0x7D, 0x4, 0x20)

    label("loc_CEBD")

    Jump("loc_D316")

    label("loc_CEC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFAF")
    OP_29(0x7E, 0x3, 0x0)
    OP_29(0x7E, 0x3, 0x1)
    OP_29(0x7E, 0x3, 0x2)
    OP_29(0x7E, 0x3, 0x10)
    OP_29(0x7E, 0x3, 0x20)
    OP_29(0x7E, 0x3, 0x40)
    OP_29(0x7E, 0x2, 0x0)
    OP_29(0x7E, 0x2, 0x1)
    OP_29(0x7E, 0x2, 0x2)
    OP_29(0x7E, 0x2, 0x3)
    OP_29(0x7E, 0x2, 0x4)
    OP_29(0x7E, 0x2, 0x5)
    OP_29(0x7E, 0x2, 0x6)
    OP_29(0x7E, 0x2, 0x7)
    OP_29(0x7E, 0x2, 0x8)
    OP_29(0x7E, 0x2, 0x9)
    OP_29(0x7E, 0x2, 0xA)
    OP_29(0x7E, 0x2, 0xB)
    OP_29(0x7E, 0x2, 0xC)
    OP_29(0x7E, 0x2, 0xD)
    OP_29(0x7E, 0x2, 0xE)
    OP_29(0x7E, 0x2, 0xF)
    OP_29(0x7E, 0x2, 0x10)
    OP_29(0x7E, 0x2, 0x11)
    OP_29(0x7E, 0x2, 0x12)
    OP_29(0x7E, 0x2, 0x13)
    OP_29(0x7E, 0x2, 0x14)
    OP_29(0x7E, 0x2, 0x15)
    OP_29(0x7E, 0x2, 0x16)
    OP_29(0x7E, 0x2, 0x17)
    OP_29(0x7E, 0x2, 0x18)
    OP_29(0x7E, 0x2, 0x19)
    OP_29(0x7E, 0x2, 0x1A)
    OP_29(0x7E, 0x2, 0x1B)
    OP_29(0x7E, 0x2, 0x1C)
    OP_29(0x7E, 0x2, 0x1D)
    OP_29(0x7E, 0x2, 0x1E)
    OP_29(0x7E, 0x2, 0x1F)

    label("loc_CFAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFC3")
    OP_29(0x7E, 0x4, 0x2)

    label("loc_CFC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFD8")
    OP_29(0x7E, 0x1, 0x0)

    label("loc_CFD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFED")
    OP_29(0x7E, 0x1, 0x1)

    label("loc_CFED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D002")
    OP_29(0x7E, 0x1, 0x2)

    label("loc_D002")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D017")
    OP_29(0x7E, 0x1, 0x3)

    label("loc_D017")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D02C")
    OP_29(0x7E, 0x1, 0x4)

    label("loc_D02C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D041")
    OP_29(0x7E, 0x1, 0x5)

    label("loc_D041")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D056")
    OP_29(0x7E, 0x1, 0x6)

    label("loc_D056")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D06B")
    OP_29(0x7E, 0x1, 0x7)

    label("loc_D06B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D080")
    OP_29(0x7E, 0x1, 0x8)

    label("loc_D080")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D095")
    OP_29(0x7E, 0x1, 0x9)

    label("loc_D095")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0AA")
    OP_29(0x7E, 0x1, 0xA)

    label("loc_D0AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0BF")
    OP_29(0x7E, 0x1, 0xB)

    label("loc_D0BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0D3")
    OP_29(0x7E, 0x4, 0x10)

    label("loc_D0D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0E7")
    OP_29(0x7E, 0x4, 0x20)

    label("loc_D0E7")

    Jump("loc_D316")

    label("loc_D0EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D9")
    OP_29(0x7F, 0x3, 0x0)
    OP_29(0x7F, 0x3, 0x1)
    OP_29(0x7F, 0x3, 0x2)
    OP_29(0x7F, 0x3, 0x10)
    OP_29(0x7F, 0x3, 0x20)
    OP_29(0x7F, 0x3, 0x40)
    OP_29(0x7F, 0x2, 0x0)
    OP_29(0x7F, 0x2, 0x1)
    OP_29(0x7F, 0x2, 0x2)
    OP_29(0x7F, 0x2, 0x3)
    OP_29(0x7F, 0x2, 0x4)
    OP_29(0x7F, 0x2, 0x5)
    OP_29(0x7F, 0x2, 0x6)
    OP_29(0x7F, 0x2, 0x7)
    OP_29(0x7F, 0x2, 0x8)
    OP_29(0x7F, 0x2, 0x9)
    OP_29(0x7F, 0x2, 0xA)
    OP_29(0x7F, 0x2, 0xB)
    OP_29(0x7F, 0x2, 0xC)
    OP_29(0x7F, 0x2, 0xD)
    OP_29(0x7F, 0x2, 0xE)
    OP_29(0x7F, 0x2, 0xF)
    OP_29(0x7F, 0x2, 0x10)
    OP_29(0x7F, 0x2, 0x11)
    OP_29(0x7F, 0x2, 0x12)
    OP_29(0x7F, 0x2, 0x13)
    OP_29(0x7F, 0x2, 0x14)
    OP_29(0x7F, 0x2, 0x15)
    OP_29(0x7F, 0x2, 0x16)
    OP_29(0x7F, 0x2, 0x17)
    OP_29(0x7F, 0x2, 0x18)
    OP_29(0x7F, 0x2, 0x19)
    OP_29(0x7F, 0x2, 0x1A)
    OP_29(0x7F, 0x2, 0x1B)
    OP_29(0x7F, 0x2, 0x1C)
    OP_29(0x7F, 0x2, 0x1D)
    OP_29(0x7F, 0x2, 0x1E)
    OP_29(0x7F, 0x2, 0x1F)

    label("loc_D1D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1ED")
    OP_29(0x7F, 0x4, 0x2)

    label("loc_D1ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D202")
    OP_29(0x7F, 0x1, 0x0)

    label("loc_D202")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D217")
    OP_29(0x7F, 0x1, 0x1)

    label("loc_D217")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D22C")
    OP_29(0x7F, 0x1, 0x2)

    label("loc_D22C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D241")
    OP_29(0x7F, 0x1, 0x3)

    label("loc_D241")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D256")
    OP_29(0x7F, 0x1, 0x4)

    label("loc_D256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D26B")
    OP_29(0x7F, 0x1, 0x5)

    label("loc_D26B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D280")
    OP_29(0x7F, 0x1, 0x6)

    label("loc_D280")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D295")
    OP_29(0x7F, 0x1, 0x7)

    label("loc_D295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2AA")
    OP_29(0x7F, 0x1, 0x8)

    label("loc_D2AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2BF")
    OP_29(0x7F, 0x1, 0x9)

    label("loc_D2BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2D4")
    OP_29(0x7F, 0x1, 0xA)

    label("loc_D2D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2E9")
    OP_29(0x7F, 0x1, 0xB)

    label("loc_D2E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2FD")
    OP_29(0x7F, 0x4, 0x10)

    label("loc_D2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D311")
    OP_29(0x7F, 0x4, 0x20)

    label("loc_D311")

    Jump("loc_D316")

    label("loc_D316")

    Jump("loc_CB5D")

    label("loc_D31B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_51_CB53 end


    label("Function_52_D333")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D33D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4A4")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "QS_1301 一押しグルメの取材協力\x01",        # 0
            "QS_1302 偽ブランド商の追跡\x01",            # 1
            "QS_1303 不審人物の調査\x01",                # 2
            "QS_1304 旧鉱山の手配魔獣\x01",              # 3
            "QS_1305 副局長の依頼\x01",                  # 4
            "QS_1306 誤配荷物の再配達\x01",              # 5
            "QS_1307 主题公园のアルバイト\x01",      # 6
            "QS_1308 不審商人の調査\x01",                # 7
            "QS_1309 西克洛斯贝尔街道の手配魔\x01",      # 8
            "QS_1310 克洛斯贝尔問題の取材協力\x01",      # 9
            "QS_1311 市民フォーラムへの参加要\x01",      # 10
            "QS_1312 暴走車の追跡\x01",                  # 11
            "QS_1313 地下区域Ｄ１区画の手\x01",      # 12
            "QS_1314 秘密の演技指導\x01",                # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D536"),
        (1, "loc_D536"),
        (2, "loc_D536"),
        (3, "loc_D536"),
        (4, "loc_D536"),
        (5, "loc_D536"),
        (6, "loc_D536"),
        (7, "loc_D536"),
        (8, "loc_D536"),
        (9, "loc_D536"),
        (10, "loc_D536"),
        (11, "loc_D536"),
        (12, "loc_D536"),
        (13, "loc_D536"),
        (SWITCH_DEFAULT, "loc_D5AF"),
    )


    label("loc_D536")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x4)
    Jump("loc_D5BE")

    label("loc_D5AF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D5BE")

    label("loc_D5BE")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F49F")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D62E"),
        (1, "loc_D858"),
        (2, "loc_DA82"),
        (3, "loc_DCAC"),
        (4, "loc_DED6"),
        (5, "loc_E100"),
        (6, "loc_E32A"),
        (7, "loc_E554"),
        (8, "loc_E77E"),
        (9, "loc_E9A8"),
        (10, "loc_EBD2"),
        (11, "loc_EDFC"),
        (12, "loc_F04B"),
        (13, "loc_F275"),
        (SWITCH_DEFAULT, "loc_F49F"),
    )


    label("loc_D62E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71B")
    OP_29(0x80, 0x3, 0x0)
    OP_29(0x80, 0x3, 0x1)
    OP_29(0x80, 0x3, 0x2)
    OP_29(0x80, 0x3, 0x10)
    OP_29(0x80, 0x3, 0x20)
    OP_29(0x80, 0x3, 0x40)
    OP_29(0x80, 0x2, 0x0)
    OP_29(0x80, 0x2, 0x1)
    OP_29(0x80, 0x2, 0x2)
    OP_29(0x80, 0x2, 0x3)
    OP_29(0x80, 0x2, 0x4)
    OP_29(0x80, 0x2, 0x5)
    OP_29(0x80, 0x2, 0x6)
    OP_29(0x80, 0x2, 0x7)
    OP_29(0x80, 0x2, 0x8)
    OP_29(0x80, 0x2, 0x9)
    OP_29(0x80, 0x2, 0xA)
    OP_29(0x80, 0x2, 0xB)
    OP_29(0x80, 0x2, 0xC)
    OP_29(0x80, 0x2, 0xD)
    OP_29(0x80, 0x2, 0xE)
    OP_29(0x80, 0x2, 0xF)
    OP_29(0x80, 0x2, 0x10)
    OP_29(0x80, 0x2, 0x11)
    OP_29(0x80, 0x2, 0x12)
    OP_29(0x80, 0x2, 0x13)
    OP_29(0x80, 0x2, 0x14)
    OP_29(0x80, 0x2, 0x15)
    OP_29(0x80, 0x2, 0x16)
    OP_29(0x80, 0x2, 0x17)
    OP_29(0x80, 0x2, 0x18)
    OP_29(0x80, 0x2, 0x19)
    OP_29(0x80, 0x2, 0x1A)
    OP_29(0x80, 0x2, 0x1B)
    OP_29(0x80, 0x2, 0x1C)
    OP_29(0x80, 0x2, 0x1D)
    OP_29(0x80, 0x2, 0x1E)
    OP_29(0x80, 0x2, 0x1F)

    label("loc_D71B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D72F")
    OP_29(0x80, 0x4, 0x2)

    label("loc_D72F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D744")
    OP_29(0x80, 0x1, 0x0)

    label("loc_D744")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D759")
    OP_29(0x80, 0x1, 0x1)

    label("loc_D759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D76E")
    OP_29(0x80, 0x1, 0x2)

    label("loc_D76E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D783")
    OP_29(0x80, 0x1, 0x3)

    label("loc_D783")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D798")
    OP_29(0x80, 0x1, 0x4)

    label("loc_D798")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D7AD")
    OP_29(0x80, 0x1, 0x5)

    label("loc_D7AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D7C2")
    OP_29(0x80, 0x1, 0x6)

    label("loc_D7C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D7D7")
    OP_29(0x80, 0x1, 0x7)

    label("loc_D7D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D7EC")
    OP_29(0x80, 0x1, 0x8)

    label("loc_D7EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D801")
    OP_29(0x80, 0x1, 0x9)

    label("loc_D801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D816")
    OP_29(0x80, 0x1, 0xA)

    label("loc_D816")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D82B")
    OP_29(0x80, 0x1, 0xB)

    label("loc_D82B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D83F")
    OP_29(0x80, 0x4, 0x10)

    label("loc_D83F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D853")
    OP_29(0x80, 0x4, 0x20)

    label("loc_D853")

    Jump("loc_F49F")

    label("loc_D858")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D945")
    OP_29(0x81, 0x3, 0x0)
    OP_29(0x81, 0x3, 0x1)
    OP_29(0x81, 0x3, 0x2)
    OP_29(0x81, 0x3, 0x10)
    OP_29(0x81, 0x3, 0x20)
    OP_29(0x81, 0x3, 0x40)
    OP_29(0x81, 0x2, 0x0)
    OP_29(0x81, 0x2, 0x1)
    OP_29(0x81, 0x2, 0x2)
    OP_29(0x81, 0x2, 0x3)
    OP_29(0x81, 0x2, 0x4)
    OP_29(0x81, 0x2, 0x5)
    OP_29(0x81, 0x2, 0x6)
    OP_29(0x81, 0x2, 0x7)
    OP_29(0x81, 0x2, 0x8)
    OP_29(0x81, 0x2, 0x9)
    OP_29(0x81, 0x2, 0xA)
    OP_29(0x81, 0x2, 0xB)
    OP_29(0x81, 0x2, 0xC)
    OP_29(0x81, 0x2, 0xD)
    OP_29(0x81, 0x2, 0xE)
    OP_29(0x81, 0x2, 0xF)
    OP_29(0x81, 0x2, 0x10)
    OP_29(0x81, 0x2, 0x11)
    OP_29(0x81, 0x2, 0x12)
    OP_29(0x81, 0x2, 0x13)
    OP_29(0x81, 0x2, 0x14)
    OP_29(0x81, 0x2, 0x15)
    OP_29(0x81, 0x2, 0x16)
    OP_29(0x81, 0x2, 0x17)
    OP_29(0x81, 0x2, 0x18)
    OP_29(0x81, 0x2, 0x19)
    OP_29(0x81, 0x2, 0x1A)
    OP_29(0x81, 0x2, 0x1B)
    OP_29(0x81, 0x2, 0x1C)
    OP_29(0x81, 0x2, 0x1D)
    OP_29(0x81, 0x2, 0x1E)
    OP_29(0x81, 0x2, 0x1F)

    label("loc_D945")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D959")
    OP_29(0x81, 0x4, 0x2)

    label("loc_D959")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D96E")
    OP_29(0x81, 0x1, 0x0)

    label("loc_D96E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D983")
    OP_29(0x81, 0x1, 0x1)

    label("loc_D983")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D998")
    OP_29(0x81, 0x1, 0x2)

    label("loc_D998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D9AD")
    OP_29(0x81, 0x1, 0x3)

    label("loc_D9AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D9C2")
    OP_29(0x81, 0x1, 0x4)

    label("loc_D9C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D9D7")
    OP_29(0x81, 0x1, 0x5)

    label("loc_D9D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D9EC")
    OP_29(0x81, 0x1, 0x6)

    label("loc_D9EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA01")
    OP_29(0x81, 0x1, 0x7)

    label("loc_DA01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA16")
    OP_29(0x81, 0x1, 0x8)

    label("loc_DA16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA2B")
    OP_29(0x81, 0x1, 0x9)

    label("loc_DA2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA40")
    OP_29(0x81, 0x1, 0xA)

    label("loc_DA40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA55")
    OP_29(0x81, 0x1, 0xB)

    label("loc_DA55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA69")
    OP_29(0x81, 0x4, 0x10)

    label("loc_DA69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DA7D")
    OP_29(0x81, 0x4, 0x20)

    label("loc_DA7D")

    Jump("loc_F49F")

    label("loc_DA82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB6F")
    OP_29(0x82, 0x3, 0x0)
    OP_29(0x82, 0x3, 0x1)
    OP_29(0x82, 0x3, 0x2)
    OP_29(0x82, 0x3, 0x10)
    OP_29(0x82, 0x3, 0x20)
    OP_29(0x82, 0x3, 0x40)
    OP_29(0x82, 0x2, 0x0)
    OP_29(0x82, 0x2, 0x1)
    OP_29(0x82, 0x2, 0x2)
    OP_29(0x82, 0x2, 0x3)
    OP_29(0x82, 0x2, 0x4)
    OP_29(0x82, 0x2, 0x5)
    OP_29(0x82, 0x2, 0x6)
    OP_29(0x82, 0x2, 0x7)
    OP_29(0x82, 0x2, 0x8)
    OP_29(0x82, 0x2, 0x9)
    OP_29(0x82, 0x2, 0xA)
    OP_29(0x82, 0x2, 0xB)
    OP_29(0x82, 0x2, 0xC)
    OP_29(0x82, 0x2, 0xD)
    OP_29(0x82, 0x2, 0xE)
    OP_29(0x82, 0x2, 0xF)
    OP_29(0x82, 0x2, 0x10)
    OP_29(0x82, 0x2, 0x11)
    OP_29(0x82, 0x2, 0x12)
    OP_29(0x82, 0x2, 0x13)
    OP_29(0x82, 0x2, 0x14)
    OP_29(0x82, 0x2, 0x15)
    OP_29(0x82, 0x2, 0x16)
    OP_29(0x82, 0x2, 0x17)
    OP_29(0x82, 0x2, 0x18)
    OP_29(0x82, 0x2, 0x19)
    OP_29(0x82, 0x2, 0x1A)
    OP_29(0x82, 0x2, 0x1B)
    OP_29(0x82, 0x2, 0x1C)
    OP_29(0x82, 0x2, 0x1D)
    OP_29(0x82, 0x2, 0x1E)
    OP_29(0x82, 0x2, 0x1F)

    label("loc_DB6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DB83")
    OP_29(0x82, 0x4, 0x2)

    label("loc_DB83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DB98")
    OP_29(0x82, 0x1, 0x0)

    label("loc_DB98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DBAD")
    OP_29(0x82, 0x1, 0x1)

    label("loc_DBAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DBC2")
    OP_29(0x82, 0x1, 0x2)

    label("loc_DBC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DBD7")
    OP_29(0x82, 0x1, 0x3)

    label("loc_DBD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DBEC")
    OP_29(0x82, 0x1, 0x4)

    label("loc_DBEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC01")
    OP_29(0x82, 0x1, 0x5)

    label("loc_DC01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC16")
    OP_29(0x82, 0x1, 0x6)

    label("loc_DC16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC2B")
    OP_29(0x82, 0x1, 0x7)

    label("loc_DC2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC40")
    OP_29(0x82, 0x1, 0x8)

    label("loc_DC40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC55")
    OP_29(0x82, 0x1, 0x9)

    label("loc_DC55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC6A")
    OP_29(0x82, 0x1, 0xA)

    label("loc_DC6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC7F")
    OP_29(0x82, 0x1, 0xB)

    label("loc_DC7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC93")
    OP_29(0x82, 0x4, 0x10)

    label("loc_DC93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DCA7")
    OP_29(0x82, 0x4, 0x20)

    label("loc_DCA7")

    Jump("loc_F49F")

    label("loc_DCAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD99")
    OP_29(0x83, 0x3, 0x0)
    OP_29(0x83, 0x3, 0x1)
    OP_29(0x83, 0x3, 0x2)
    OP_29(0x83, 0x3, 0x10)
    OP_29(0x83, 0x3, 0x20)
    OP_29(0x83, 0x3, 0x40)
    OP_29(0x83, 0x2, 0x0)
    OP_29(0x83, 0x2, 0x1)
    OP_29(0x83, 0x2, 0x2)
    OP_29(0x83, 0x2, 0x3)
    OP_29(0x83, 0x2, 0x4)
    OP_29(0x83, 0x2, 0x5)
    OP_29(0x83, 0x2, 0x6)
    OP_29(0x83, 0x2, 0x7)
    OP_29(0x83, 0x2, 0x8)
    OP_29(0x83, 0x2, 0x9)
    OP_29(0x83, 0x2, 0xA)
    OP_29(0x83, 0x2, 0xB)
    OP_29(0x83, 0x2, 0xC)
    OP_29(0x83, 0x2, 0xD)
    OP_29(0x83, 0x2, 0xE)
    OP_29(0x83, 0x2, 0xF)
    OP_29(0x83, 0x2, 0x10)
    OP_29(0x83, 0x2, 0x11)
    OP_29(0x83, 0x2, 0x12)
    OP_29(0x83, 0x2, 0x13)
    OP_29(0x83, 0x2, 0x14)
    OP_29(0x83, 0x2, 0x15)
    OP_29(0x83, 0x2, 0x16)
    OP_29(0x83, 0x2, 0x17)
    OP_29(0x83, 0x2, 0x18)
    OP_29(0x83, 0x2, 0x19)
    OP_29(0x83, 0x2, 0x1A)
    OP_29(0x83, 0x2, 0x1B)
    OP_29(0x83, 0x2, 0x1C)
    OP_29(0x83, 0x2, 0x1D)
    OP_29(0x83, 0x2, 0x1E)
    OP_29(0x83, 0x2, 0x1F)

    label("loc_DD99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DDAD")
    OP_29(0x83, 0x4, 0x2)

    label("loc_DDAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DDC2")
    OP_29(0x83, 0x1, 0x0)

    label("loc_DDC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DDD7")
    OP_29(0x83, 0x1, 0x1)

    label("loc_DDD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DDEC")
    OP_29(0x83, 0x1, 0x2)

    label("loc_DDEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE01")
    OP_29(0x83, 0x1, 0x3)

    label("loc_DE01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE16")
    OP_29(0x83, 0x1, 0x4)

    label("loc_DE16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE2B")
    OP_29(0x83, 0x1, 0x5)

    label("loc_DE2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE40")
    OP_29(0x83, 0x1, 0x6)

    label("loc_DE40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE55")
    OP_29(0x83, 0x1, 0x7)

    label("loc_DE55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE6A")
    OP_29(0x83, 0x1, 0x8)

    label("loc_DE6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE7F")
    OP_29(0x83, 0x1, 0x9)

    label("loc_DE7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE94")
    OP_29(0x83, 0x1, 0xA)

    label("loc_DE94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEA9")
    OP_29(0x83, 0x1, 0xB)

    label("loc_DEA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEBD")
    OP_29(0x83, 0x4, 0x10)

    label("loc_DEBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DED1")
    OP_29(0x83, 0x4, 0x20)

    label("loc_DED1")

    Jump("loc_F49F")

    label("loc_DED6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFC3")
    OP_29(0x84, 0x3, 0x0)
    OP_29(0x84, 0x3, 0x1)
    OP_29(0x84, 0x3, 0x2)
    OP_29(0x84, 0x3, 0x10)
    OP_29(0x84, 0x3, 0x20)
    OP_29(0x84, 0x3, 0x40)
    OP_29(0x84, 0x2, 0x0)
    OP_29(0x84, 0x2, 0x1)
    OP_29(0x84, 0x2, 0x2)
    OP_29(0x84, 0x2, 0x3)
    OP_29(0x84, 0x2, 0x4)
    OP_29(0x84, 0x2, 0x5)
    OP_29(0x84, 0x2, 0x6)
    OP_29(0x84, 0x2, 0x7)
    OP_29(0x84, 0x2, 0x8)
    OP_29(0x84, 0x2, 0x9)
    OP_29(0x84, 0x2, 0xA)
    OP_29(0x84, 0x2, 0xB)
    OP_29(0x84, 0x2, 0xC)
    OP_29(0x84, 0x2, 0xD)
    OP_29(0x84, 0x2, 0xE)
    OP_29(0x84, 0x2, 0xF)
    OP_29(0x84, 0x2, 0x10)
    OP_29(0x84, 0x2, 0x11)
    OP_29(0x84, 0x2, 0x12)
    OP_29(0x84, 0x2, 0x13)
    OP_29(0x84, 0x2, 0x14)
    OP_29(0x84, 0x2, 0x15)
    OP_29(0x84, 0x2, 0x16)
    OP_29(0x84, 0x2, 0x17)
    OP_29(0x84, 0x2, 0x18)
    OP_29(0x84, 0x2, 0x19)
    OP_29(0x84, 0x2, 0x1A)
    OP_29(0x84, 0x2, 0x1B)
    OP_29(0x84, 0x2, 0x1C)
    OP_29(0x84, 0x2, 0x1D)
    OP_29(0x84, 0x2, 0x1E)
    OP_29(0x84, 0x2, 0x1F)

    label("loc_DFC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DFD7")
    OP_29(0x84, 0x4, 0x2)

    label("loc_DFD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DFEC")
    OP_29(0x84, 0x1, 0x0)

    label("loc_DFEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E001")
    OP_29(0x84, 0x1, 0x1)

    label("loc_E001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E016")
    OP_29(0x84, 0x1, 0x2)

    label("loc_E016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E02B")
    OP_29(0x84, 0x1, 0x3)

    label("loc_E02B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E040")
    OP_29(0x84, 0x1, 0x4)

    label("loc_E040")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E055")
    OP_29(0x84, 0x1, 0x5)

    label("loc_E055")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E06A")
    OP_29(0x84, 0x1, 0x6)

    label("loc_E06A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E07F")
    OP_29(0x84, 0x1, 0x7)

    label("loc_E07F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E094")
    OP_29(0x84, 0x1, 0x8)

    label("loc_E094")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0A9")
    OP_29(0x84, 0x1, 0x9)

    label("loc_E0A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0BE")
    OP_29(0x84, 0x1, 0xA)

    label("loc_E0BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0D3")
    OP_29(0x84, 0x1, 0xB)

    label("loc_E0D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0E7")
    OP_29(0x84, 0x4, 0x10)

    label("loc_E0E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0FB")
    OP_29(0x84, 0x4, 0x20)

    label("loc_E0FB")

    Jump("loc_F49F")

    label("loc_E100")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1ED")
    OP_29(0x85, 0x3, 0x0)
    OP_29(0x85, 0x3, 0x1)
    OP_29(0x85, 0x3, 0x2)
    OP_29(0x85, 0x3, 0x10)
    OP_29(0x85, 0x3, 0x20)
    OP_29(0x85, 0x3, 0x40)
    OP_29(0x85, 0x2, 0x0)
    OP_29(0x85, 0x2, 0x1)
    OP_29(0x85, 0x2, 0x2)
    OP_29(0x85, 0x2, 0x3)
    OP_29(0x85, 0x2, 0x4)
    OP_29(0x85, 0x2, 0x5)
    OP_29(0x85, 0x2, 0x6)
    OP_29(0x85, 0x2, 0x7)
    OP_29(0x85, 0x2, 0x8)
    OP_29(0x85, 0x2, 0x9)
    OP_29(0x85, 0x2, 0xA)
    OP_29(0x85, 0x2, 0xB)
    OP_29(0x85, 0x2, 0xC)
    OP_29(0x85, 0x2, 0xD)
    OP_29(0x85, 0x2, 0xE)
    OP_29(0x85, 0x2, 0xF)
    OP_29(0x85, 0x2, 0x10)
    OP_29(0x85, 0x2, 0x11)
    OP_29(0x85, 0x2, 0x12)
    OP_29(0x85, 0x2, 0x13)
    OP_29(0x85, 0x2, 0x14)
    OP_29(0x85, 0x2, 0x15)
    OP_29(0x85, 0x2, 0x16)
    OP_29(0x85, 0x2, 0x17)
    OP_29(0x85, 0x2, 0x18)
    OP_29(0x85, 0x2, 0x19)
    OP_29(0x85, 0x2, 0x1A)
    OP_29(0x85, 0x2, 0x1B)
    OP_29(0x85, 0x2, 0x1C)
    OP_29(0x85, 0x2, 0x1D)
    OP_29(0x85, 0x2, 0x1E)
    OP_29(0x85, 0x2, 0x1F)

    label("loc_E1ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E201")
    OP_29(0x85, 0x4, 0x2)

    label("loc_E201")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E216")
    OP_29(0x85, 0x1, 0x0)

    label("loc_E216")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E22B")
    OP_29(0x85, 0x1, 0x1)

    label("loc_E22B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E240")
    OP_29(0x85, 0x1, 0x2)

    label("loc_E240")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E255")
    OP_29(0x85, 0x1, 0x3)

    label("loc_E255")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E26A")
    OP_29(0x85, 0x1, 0x4)

    label("loc_E26A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E27F")
    OP_29(0x85, 0x1, 0x5)

    label("loc_E27F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E294")
    OP_29(0x85, 0x1, 0x6)

    label("loc_E294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2A9")
    OP_29(0x85, 0x1, 0x7)

    label("loc_E2A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2BE")
    OP_29(0x85, 0x1, 0x8)

    label("loc_E2BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2D3")
    OP_29(0x85, 0x1, 0x9)

    label("loc_E2D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2E8")
    OP_29(0x85, 0x1, 0xA)

    label("loc_E2E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2FD")
    OP_29(0x85, 0x1, 0xB)

    label("loc_E2FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E311")
    OP_29(0x85, 0x4, 0x10)

    label("loc_E311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E325")
    OP_29(0x85, 0x4, 0x20)

    label("loc_E325")

    Jump("loc_F49F")

    label("loc_E32A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E417")
    OP_29(0x86, 0x3, 0x0)
    OP_29(0x86, 0x3, 0x1)
    OP_29(0x86, 0x3, 0x2)
    OP_29(0x86, 0x3, 0x10)
    OP_29(0x86, 0x3, 0x20)
    OP_29(0x86, 0x3, 0x40)
    OP_29(0x86, 0x2, 0x0)
    OP_29(0x86, 0x2, 0x1)
    OP_29(0x86, 0x2, 0x2)
    OP_29(0x86, 0x2, 0x3)
    OP_29(0x86, 0x2, 0x4)
    OP_29(0x86, 0x2, 0x5)
    OP_29(0x86, 0x2, 0x6)
    OP_29(0x86, 0x2, 0x7)
    OP_29(0x86, 0x2, 0x8)
    OP_29(0x86, 0x2, 0x9)
    OP_29(0x86, 0x2, 0xA)
    OP_29(0x86, 0x2, 0xB)
    OP_29(0x86, 0x2, 0xC)
    OP_29(0x86, 0x2, 0xD)
    OP_29(0x86, 0x2, 0xE)
    OP_29(0x86, 0x2, 0xF)
    OP_29(0x86, 0x2, 0x10)
    OP_29(0x86, 0x2, 0x11)
    OP_29(0x86, 0x2, 0x12)
    OP_29(0x86, 0x2, 0x13)
    OP_29(0x86, 0x2, 0x14)
    OP_29(0x86, 0x2, 0x15)
    OP_29(0x86, 0x2, 0x16)
    OP_29(0x86, 0x2, 0x17)
    OP_29(0x86, 0x2, 0x18)
    OP_29(0x86, 0x2, 0x19)
    OP_29(0x86, 0x2, 0x1A)
    OP_29(0x86, 0x2, 0x1B)
    OP_29(0x86, 0x2, 0x1C)
    OP_29(0x86, 0x2, 0x1D)
    OP_29(0x86, 0x2, 0x1E)
    OP_29(0x86, 0x2, 0x1F)

    label("loc_E417")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E42B")
    OP_29(0x86, 0x4, 0x2)

    label("loc_E42B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E440")
    OP_29(0x86, 0x1, 0x0)

    label("loc_E440")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E455")
    OP_29(0x86, 0x1, 0x1)

    label("loc_E455")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E46A")
    OP_29(0x86, 0x1, 0x2)

    label("loc_E46A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E47F")
    OP_29(0x86, 0x1, 0x3)

    label("loc_E47F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E494")
    OP_29(0x86, 0x1, 0x4)

    label("loc_E494")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4A9")
    OP_29(0x86, 0x1, 0x5)

    label("loc_E4A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4BE")
    OP_29(0x86, 0x1, 0x6)

    label("loc_E4BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4D3")
    OP_29(0x86, 0x1, 0x7)

    label("loc_E4D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4E8")
    OP_29(0x86, 0x1, 0x8)

    label("loc_E4E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4FD")
    OP_29(0x86, 0x1, 0x9)

    label("loc_E4FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E512")
    OP_29(0x86, 0x1, 0xA)

    label("loc_E512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E527")
    OP_29(0x86, 0x1, 0xB)

    label("loc_E527")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E53B")
    OP_29(0x86, 0x4, 0x10)

    label("loc_E53B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E54F")
    OP_29(0x86, 0x4, 0x20)

    label("loc_E54F")

    Jump("loc_F49F")

    label("loc_E554")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E641")
    OP_29(0x87, 0x3, 0x0)
    OP_29(0x87, 0x3, 0x1)
    OP_29(0x87, 0x3, 0x2)
    OP_29(0x87, 0x3, 0x10)
    OP_29(0x87, 0x3, 0x20)
    OP_29(0x87, 0x3, 0x40)
    OP_29(0x87, 0x2, 0x0)
    OP_29(0x87, 0x2, 0x1)
    OP_29(0x87, 0x2, 0x2)
    OP_29(0x87, 0x2, 0x3)
    OP_29(0x87, 0x2, 0x4)
    OP_29(0x87, 0x2, 0x5)
    OP_29(0x87, 0x2, 0x6)
    OP_29(0x87, 0x2, 0x7)
    OP_29(0x87, 0x2, 0x8)
    OP_29(0x87, 0x2, 0x9)
    OP_29(0x87, 0x2, 0xA)
    OP_29(0x87, 0x2, 0xB)
    OP_29(0x87, 0x2, 0xC)
    OP_29(0x87, 0x2, 0xD)
    OP_29(0x87, 0x2, 0xE)
    OP_29(0x87, 0x2, 0xF)
    OP_29(0x87, 0x2, 0x10)
    OP_29(0x87, 0x2, 0x11)
    OP_29(0x87, 0x2, 0x12)
    OP_29(0x87, 0x2, 0x13)
    OP_29(0x87, 0x2, 0x14)
    OP_29(0x87, 0x2, 0x15)
    OP_29(0x87, 0x2, 0x16)
    OP_29(0x87, 0x2, 0x17)
    OP_29(0x87, 0x2, 0x18)
    OP_29(0x87, 0x2, 0x19)
    OP_29(0x87, 0x2, 0x1A)
    OP_29(0x87, 0x2, 0x1B)
    OP_29(0x87, 0x2, 0x1C)
    OP_29(0x87, 0x2, 0x1D)
    OP_29(0x87, 0x2, 0x1E)
    OP_29(0x87, 0x2, 0x1F)

    label("loc_E641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E655")
    OP_29(0x87, 0x4, 0x2)

    label("loc_E655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E66A")
    OP_29(0x87, 0x1, 0x0)

    label("loc_E66A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E67F")
    OP_29(0x87, 0x1, 0x1)

    label("loc_E67F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E694")
    OP_29(0x87, 0x1, 0x2)

    label("loc_E694")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6A9")
    OP_29(0x87, 0x1, 0x3)

    label("loc_E6A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6BE")
    OP_29(0x87, 0x1, 0x4)

    label("loc_E6BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6D3")
    OP_29(0x87, 0x1, 0x5)

    label("loc_E6D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6E8")
    OP_29(0x87, 0x1, 0x6)

    label("loc_E6E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6FD")
    OP_29(0x87, 0x1, 0x7)

    label("loc_E6FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E712")
    OP_29(0x87, 0x1, 0x8)

    label("loc_E712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E727")
    OP_29(0x87, 0x1, 0x9)

    label("loc_E727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E73C")
    OP_29(0x87, 0x1, 0xA)

    label("loc_E73C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E751")
    OP_29(0x87, 0x1, 0xB)

    label("loc_E751")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E765")
    OP_29(0x87, 0x4, 0x10)

    label("loc_E765")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E779")
    OP_29(0x87, 0x4, 0x20)

    label("loc_E779")

    Jump("loc_F49F")

    label("loc_E77E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E86B")
    OP_29(0x88, 0x3, 0x0)
    OP_29(0x88, 0x3, 0x1)
    OP_29(0x88, 0x3, 0x2)
    OP_29(0x88, 0x3, 0x10)
    OP_29(0x88, 0x3, 0x20)
    OP_29(0x88, 0x3, 0x40)
    OP_29(0x88, 0x2, 0x0)
    OP_29(0x88, 0x2, 0x1)
    OP_29(0x88, 0x2, 0x2)
    OP_29(0x88, 0x2, 0x3)
    OP_29(0x88, 0x2, 0x4)
    OP_29(0x88, 0x2, 0x5)
    OP_29(0x88, 0x2, 0x6)
    OP_29(0x88, 0x2, 0x7)
    OP_29(0x88, 0x2, 0x8)
    OP_29(0x88, 0x2, 0x9)
    OP_29(0x88, 0x2, 0xA)
    OP_29(0x88, 0x2, 0xB)
    OP_29(0x88, 0x2, 0xC)
    OP_29(0x88, 0x2, 0xD)
    OP_29(0x88, 0x2, 0xE)
    OP_29(0x88, 0x2, 0xF)
    OP_29(0x88, 0x2, 0x10)
    OP_29(0x88, 0x2, 0x11)
    OP_29(0x88, 0x2, 0x12)
    OP_29(0x88, 0x2, 0x13)
    OP_29(0x88, 0x2, 0x14)
    OP_29(0x88, 0x2, 0x15)
    OP_29(0x88, 0x2, 0x16)
    OP_29(0x88, 0x2, 0x17)
    OP_29(0x88, 0x2, 0x18)
    OP_29(0x88, 0x2, 0x19)
    OP_29(0x88, 0x2, 0x1A)
    OP_29(0x88, 0x2, 0x1B)
    OP_29(0x88, 0x2, 0x1C)
    OP_29(0x88, 0x2, 0x1D)
    OP_29(0x88, 0x2, 0x1E)
    OP_29(0x88, 0x2, 0x1F)

    label("loc_E86B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E87F")
    OP_29(0x88, 0x4, 0x2)

    label("loc_E87F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E894")
    OP_29(0x88, 0x1, 0x0)

    label("loc_E894")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8A9")
    OP_29(0x88, 0x1, 0x1)

    label("loc_E8A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8BE")
    OP_29(0x88, 0x1, 0x2)

    label("loc_E8BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8D3")
    OP_29(0x88, 0x1, 0x3)

    label("loc_E8D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8E8")
    OP_29(0x88, 0x1, 0x4)

    label("loc_E8E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8FD")
    OP_29(0x88, 0x1, 0x5)

    label("loc_E8FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E912")
    OP_29(0x88, 0x1, 0x6)

    label("loc_E912")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E927")
    OP_29(0x88, 0x1, 0x7)

    label("loc_E927")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E93C")
    OP_29(0x88, 0x1, 0x8)

    label("loc_E93C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E951")
    OP_29(0x88, 0x1, 0x9)

    label("loc_E951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E966")
    OP_29(0x88, 0x1, 0xA)

    label("loc_E966")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E97B")
    OP_29(0x88, 0x1, 0xB)

    label("loc_E97B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E98F")
    OP_29(0x88, 0x4, 0x10)

    label("loc_E98F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E9A3")
    OP_29(0x88, 0x4, 0x20)

    label("loc_E9A3")

    Jump("loc_F49F")

    label("loc_E9A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA95")
    OP_29(0x89, 0x3, 0x0)
    OP_29(0x89, 0x3, 0x1)
    OP_29(0x89, 0x3, 0x2)
    OP_29(0x89, 0x3, 0x10)
    OP_29(0x89, 0x3, 0x20)
    OP_29(0x89, 0x3, 0x40)
    OP_29(0x89, 0x2, 0x0)
    OP_29(0x89, 0x2, 0x1)
    OP_29(0x89, 0x2, 0x2)
    OP_29(0x89, 0x2, 0x3)
    OP_29(0x89, 0x2, 0x4)
    OP_29(0x89, 0x2, 0x5)
    OP_29(0x89, 0x2, 0x6)
    OP_29(0x89, 0x2, 0x7)
    OP_29(0x89, 0x2, 0x8)
    OP_29(0x89, 0x2, 0x9)
    OP_29(0x89, 0x2, 0xA)
    OP_29(0x89, 0x2, 0xB)
    OP_29(0x89, 0x2, 0xC)
    OP_29(0x89, 0x2, 0xD)
    OP_29(0x89, 0x2, 0xE)
    OP_29(0x89, 0x2, 0xF)
    OP_29(0x89, 0x2, 0x10)
    OP_29(0x89, 0x2, 0x11)
    OP_29(0x89, 0x2, 0x12)
    OP_29(0x89, 0x2, 0x13)
    OP_29(0x89, 0x2, 0x14)
    OP_29(0x89, 0x2, 0x15)
    OP_29(0x89, 0x2, 0x16)
    OP_29(0x89, 0x2, 0x17)
    OP_29(0x89, 0x2, 0x18)
    OP_29(0x89, 0x2, 0x19)
    OP_29(0x89, 0x2, 0x1A)
    OP_29(0x89, 0x2, 0x1B)
    OP_29(0x89, 0x2, 0x1C)
    OP_29(0x89, 0x2, 0x1D)
    OP_29(0x89, 0x2, 0x1E)
    OP_29(0x89, 0x2, 0x1F)

    label("loc_EA95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAA9")
    OP_29(0x89, 0x4, 0x2)

    label("loc_EAA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EABE")
    OP_29(0x89, 0x1, 0x0)

    label("loc_EABE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAD3")
    OP_29(0x89, 0x1, 0x1)

    label("loc_EAD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAE8")
    OP_29(0x89, 0x1, 0x2)

    label("loc_EAE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAFD")
    OP_29(0x89, 0x1, 0x3)

    label("loc_EAFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB12")
    OP_29(0x89, 0x1, 0x4)

    label("loc_EB12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB27")
    OP_29(0x89, 0x1, 0x5)

    label("loc_EB27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB3C")
    OP_29(0x89, 0x1, 0x6)

    label("loc_EB3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB51")
    OP_29(0x89, 0x1, 0x7)

    label("loc_EB51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB66")
    OP_29(0x89, 0x1, 0x8)

    label("loc_EB66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB7B")
    OP_29(0x89, 0x1, 0x9)

    label("loc_EB7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB90")
    OP_29(0x89, 0x1, 0xA)

    label("loc_EB90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EBA5")
    OP_29(0x89, 0x1, 0xB)

    label("loc_EBA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EBB9")
    OP_29(0x89, 0x4, 0x10)

    label("loc_EBB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EBCD")
    OP_29(0x89, 0x4, 0x20)

    label("loc_EBCD")

    Jump("loc_F49F")

    label("loc_EBD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECBF")
    OP_29(0x8A, 0x3, 0x0)
    OP_29(0x8A, 0x3, 0x1)
    OP_29(0x8A, 0x3, 0x2)
    OP_29(0x8A, 0x3, 0x10)
    OP_29(0x8A, 0x3, 0x20)
    OP_29(0x8A, 0x3, 0x40)
    OP_29(0x8A, 0x2, 0x0)
    OP_29(0x8A, 0x2, 0x1)
    OP_29(0x8A, 0x2, 0x2)
    OP_29(0x8A, 0x2, 0x3)
    OP_29(0x8A, 0x2, 0x4)
    OP_29(0x8A, 0x2, 0x5)
    OP_29(0x8A, 0x2, 0x6)
    OP_29(0x8A, 0x2, 0x7)
    OP_29(0x8A, 0x2, 0x8)
    OP_29(0x8A, 0x2, 0x9)
    OP_29(0x8A, 0x2, 0xA)
    OP_29(0x8A, 0x2, 0xB)
    OP_29(0x8A, 0x2, 0xC)
    OP_29(0x8A, 0x2, 0xD)
    OP_29(0x8A, 0x2, 0xE)
    OP_29(0x8A, 0x2, 0xF)
    OP_29(0x8A, 0x2, 0x10)
    OP_29(0x8A, 0x2, 0x11)
    OP_29(0x8A, 0x2, 0x12)
    OP_29(0x8A, 0x2, 0x13)
    OP_29(0x8A, 0x2, 0x14)
    OP_29(0x8A, 0x2, 0x15)
    OP_29(0x8A, 0x2, 0x16)
    OP_29(0x8A, 0x2, 0x17)
    OP_29(0x8A, 0x2, 0x18)
    OP_29(0x8A, 0x2, 0x19)
    OP_29(0x8A, 0x2, 0x1A)
    OP_29(0x8A, 0x2, 0x1B)
    OP_29(0x8A, 0x2, 0x1C)
    OP_29(0x8A, 0x2, 0x1D)
    OP_29(0x8A, 0x2, 0x1E)
    OP_29(0x8A, 0x2, 0x1F)

    label("loc_ECBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECD3")
    OP_29(0x8A, 0x4, 0x2)

    label("loc_ECD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECE8")
    OP_29(0x8A, 0x1, 0x0)

    label("loc_ECE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECFD")
    OP_29(0x8A, 0x1, 0x1)

    label("loc_ECFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED12")
    OP_29(0x8A, 0x1, 0x2)

    label("loc_ED12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED27")
    OP_29(0x8A, 0x1, 0x3)

    label("loc_ED27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED3C")
    OP_29(0x8A, 0x1, 0x4)

    label("loc_ED3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED51")
    OP_29(0x8A, 0x1, 0x5)

    label("loc_ED51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED66")
    OP_29(0x8A, 0x1, 0x6)

    label("loc_ED66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED7B")
    OP_29(0x8A, 0x1, 0x7)

    label("loc_ED7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED90")
    OP_29(0x8A, 0x1, 0x8)

    label("loc_ED90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EDA5")
    OP_29(0x8A, 0x1, 0x9)

    label("loc_EDA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EDBA")
    OP_29(0x8A, 0x1, 0xA)

    label("loc_EDBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EDCF")
    OP_29(0x8A, 0x1, 0xB)

    label("loc_EDCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EDE3")
    OP_29(0x8A, 0x4, 0x10)

    label("loc_EDE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EDF7")
    OP_29(0x8A, 0x4, 0x20)

    label("loc_EDF7")

    Jump("loc_F49F")

    label("loc_EDFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEE9")
    OP_29(0x8B, 0x3, 0x0)
    OP_29(0x8B, 0x3, 0x1)
    OP_29(0x8B, 0x3, 0x2)
    OP_29(0x8B, 0x3, 0x10)
    OP_29(0x8B, 0x3, 0x20)
    OP_29(0x8B, 0x3, 0x40)
    OP_29(0x8B, 0x2, 0x0)
    OP_29(0x8B, 0x2, 0x1)
    OP_29(0x8B, 0x2, 0x2)
    OP_29(0x8B, 0x2, 0x3)
    OP_29(0x8B, 0x2, 0x4)
    OP_29(0x8B, 0x2, 0x5)
    OP_29(0x8B, 0x2, 0x6)
    OP_29(0x8B, 0x2, 0x7)
    OP_29(0x8B, 0x2, 0x8)
    OP_29(0x8B, 0x2, 0x9)
    OP_29(0x8B, 0x2, 0xA)
    OP_29(0x8B, 0x2, 0xB)
    OP_29(0x8B, 0x2, 0xC)
    OP_29(0x8B, 0x2, 0xD)
    OP_29(0x8B, 0x2, 0xE)
    OP_29(0x8B, 0x2, 0xF)
    OP_29(0x8B, 0x2, 0x10)
    OP_29(0x8B, 0x2, 0x11)
    OP_29(0x8B, 0x2, 0x12)
    OP_29(0x8B, 0x2, 0x13)
    OP_29(0x8B, 0x2, 0x14)
    OP_29(0x8B, 0x2, 0x15)
    OP_29(0x8B, 0x2, 0x16)
    OP_29(0x8B, 0x2, 0x17)
    OP_29(0x8B, 0x2, 0x18)
    OP_29(0x8B, 0x2, 0x19)
    OP_29(0x8B, 0x2, 0x1A)
    OP_29(0x8B, 0x2, 0x1B)
    OP_29(0x8B, 0x2, 0x1C)
    OP_29(0x8B, 0x2, 0x1D)
    OP_29(0x8B, 0x2, 0x1E)
    OP_29(0x8B, 0x2, 0x1F)

    label("loc_EEE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EEFD")
    OP_29(0x8B, 0x4, 0x2)

    label("loc_EEFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF37")
    OP_29(0x8B, 0x1, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x23, 1)
    NewScene("r1010", 0, 0, 0)
    OP_07()

    label("loc_EF37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF4C")
    OP_29(0x8B, 0x1, 0x1)

    label("loc_EF4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF61")
    OP_29(0x8B, 0x1, 0x2)

    label("loc_EF61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF76")
    OP_29(0x8B, 0x1, 0x3)

    label("loc_EF76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EF8B")
    OP_29(0x8B, 0x1, 0x4)

    label("loc_EF8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EFA0")
    OP_29(0x8B, 0x1, 0x5)

    label("loc_EFA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EFB5")
    OP_29(0x8B, 0x1, 0x6)

    label("loc_EFB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EFCA")
    OP_29(0x8B, 0x1, 0x7)

    label("loc_EFCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EFDF")
    OP_29(0x8B, 0x1, 0x8)

    label("loc_EFDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EFF4")
    OP_29(0x8B, 0x1, 0x9)

    label("loc_EFF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F009")
    OP_29(0x8B, 0x1, 0xA)

    label("loc_F009")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F01E")
    OP_29(0x8B, 0x1, 0xB)

    label("loc_F01E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F032")
    OP_29(0x8B, 0x4, 0x10)

    label("loc_F032")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F046")
    OP_29(0x8B, 0x4, 0x20)

    label("loc_F046")

    Jump("loc_F49F")

    label("loc_F04B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F138")
    OP_29(0x8C, 0x3, 0x0)
    OP_29(0x8C, 0x3, 0x1)
    OP_29(0x8C, 0x3, 0x2)
    OP_29(0x8C, 0x3, 0x10)
    OP_29(0x8C, 0x3, 0x20)
    OP_29(0x8C, 0x3, 0x40)
    OP_29(0x8C, 0x2, 0x0)
    OP_29(0x8C, 0x2, 0x1)
    OP_29(0x8C, 0x2, 0x2)
    OP_29(0x8C, 0x2, 0x3)
    OP_29(0x8C, 0x2, 0x4)
    OP_29(0x8C, 0x2, 0x5)
    OP_29(0x8C, 0x2, 0x6)
    OP_29(0x8C, 0x2, 0x7)
    OP_29(0x8C, 0x2, 0x8)
    OP_29(0x8C, 0x2, 0x9)
    OP_29(0x8C, 0x2, 0xA)
    OP_29(0x8C, 0x2, 0xB)
    OP_29(0x8C, 0x2, 0xC)
    OP_29(0x8C, 0x2, 0xD)
    OP_29(0x8C, 0x2, 0xE)
    OP_29(0x8C, 0x2, 0xF)
    OP_29(0x8C, 0x2, 0x10)
    OP_29(0x8C, 0x2, 0x11)
    OP_29(0x8C, 0x2, 0x12)
    OP_29(0x8C, 0x2, 0x13)
    OP_29(0x8C, 0x2, 0x14)
    OP_29(0x8C, 0x2, 0x15)
    OP_29(0x8C, 0x2, 0x16)
    OP_29(0x8C, 0x2, 0x17)
    OP_29(0x8C, 0x2, 0x18)
    OP_29(0x8C, 0x2, 0x19)
    OP_29(0x8C, 0x2, 0x1A)
    OP_29(0x8C, 0x2, 0x1B)
    OP_29(0x8C, 0x2, 0x1C)
    OP_29(0x8C, 0x2, 0x1D)
    OP_29(0x8C, 0x2, 0x1E)
    OP_29(0x8C, 0x2, 0x1F)

    label("loc_F138")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F14C")
    OP_29(0x8C, 0x4, 0x2)

    label("loc_F14C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F161")
    OP_29(0x8C, 0x1, 0x0)

    label("loc_F161")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F176")
    OP_29(0x8C, 0x1, 0x1)

    label("loc_F176")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F18B")
    OP_29(0x8C, 0x1, 0x2)

    label("loc_F18B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F1A0")
    OP_29(0x8C, 0x1, 0x3)

    label("loc_F1A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F1B5")
    OP_29(0x8C, 0x1, 0x4)

    label("loc_F1B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F1CA")
    OP_29(0x8C, 0x1, 0x5)

    label("loc_F1CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F1DF")
    OP_29(0x8C, 0x1, 0x6)

    label("loc_F1DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F1F4")
    OP_29(0x8C, 0x1, 0x7)

    label("loc_F1F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F209")
    OP_29(0x8C, 0x1, 0x8)

    label("loc_F209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F21E")
    OP_29(0x8C, 0x1, 0x9)

    label("loc_F21E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F233")
    OP_29(0x8C, 0x1, 0xA)

    label("loc_F233")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F248")
    OP_29(0x8C, 0x1, 0xB)

    label("loc_F248")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F25C")
    OP_29(0x8C, 0x4, 0x10)

    label("loc_F25C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F270")
    OP_29(0x8C, 0x4, 0x20)

    label("loc_F270")

    Jump("loc_F49F")

    label("loc_F275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F362")
    OP_29(0x8D, 0x3, 0x0)
    OP_29(0x8D, 0x3, 0x1)
    OP_29(0x8D, 0x3, 0x2)
    OP_29(0x8D, 0x3, 0x10)
    OP_29(0x8D, 0x3, 0x20)
    OP_29(0x8D, 0x3, 0x40)
    OP_29(0x8D, 0x2, 0x0)
    OP_29(0x8D, 0x2, 0x1)
    OP_29(0x8D, 0x2, 0x2)
    OP_29(0x8D, 0x2, 0x3)
    OP_29(0x8D, 0x2, 0x4)
    OP_29(0x8D, 0x2, 0x5)
    OP_29(0x8D, 0x2, 0x6)
    OP_29(0x8D, 0x2, 0x7)
    OP_29(0x8D, 0x2, 0x8)
    OP_29(0x8D, 0x2, 0x9)
    OP_29(0x8D, 0x2, 0xA)
    OP_29(0x8D, 0x2, 0xB)
    OP_29(0x8D, 0x2, 0xC)
    OP_29(0x8D, 0x2, 0xD)
    OP_29(0x8D, 0x2, 0xE)
    OP_29(0x8D, 0x2, 0xF)
    OP_29(0x8D, 0x2, 0x10)
    OP_29(0x8D, 0x2, 0x11)
    OP_29(0x8D, 0x2, 0x12)
    OP_29(0x8D, 0x2, 0x13)
    OP_29(0x8D, 0x2, 0x14)
    OP_29(0x8D, 0x2, 0x15)
    OP_29(0x8D, 0x2, 0x16)
    OP_29(0x8D, 0x2, 0x17)
    OP_29(0x8D, 0x2, 0x18)
    OP_29(0x8D, 0x2, 0x19)
    OP_29(0x8D, 0x2, 0x1A)
    OP_29(0x8D, 0x2, 0x1B)
    OP_29(0x8D, 0x2, 0x1C)
    OP_29(0x8D, 0x2, 0x1D)
    OP_29(0x8D, 0x2, 0x1E)
    OP_29(0x8D, 0x2, 0x1F)

    label("loc_F362")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F376")
    OP_29(0x8D, 0x4, 0x2)

    label("loc_F376")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F38B")
    OP_29(0x8D, 0x1, 0x0)

    label("loc_F38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F3A0")
    OP_29(0x8D, 0x1, 0x1)

    label("loc_F3A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F3B5")
    OP_29(0x8D, 0x1, 0x2)

    label("loc_F3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F3CA")
    OP_29(0x8D, 0x1, 0x3)

    label("loc_F3CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F3DF")
    OP_29(0x8D, 0x1, 0x4)

    label("loc_F3DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F3F4")
    OP_29(0x8D, 0x1, 0x5)

    label("loc_F3F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F409")
    OP_29(0x8D, 0x1, 0x6)

    label("loc_F409")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F41E")
    OP_29(0x8D, 0x1, 0x7)

    label("loc_F41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F433")
    OP_29(0x8D, 0x1, 0x8)

    label("loc_F433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F448")
    OP_29(0x8D, 0x1, 0x9)

    label("loc_F448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F45D")
    OP_29(0x8D, 0x1, 0xA)

    label("loc_F45D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F472")
    OP_29(0x8D, 0x1, 0xB)

    label("loc_F472")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F486")
    OP_29(0x8D, 0x4, 0x10)

    label("loc_F486")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F49A")
    OP_29(0x8D, 0x4, 0x20)

    label("loc_F49A")

    Jump("loc_F49F")

    label("loc_F49F")

    Jump("loc_D33D")

    label("loc_F4A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_52_D333 end


    label("Function_53_F4BC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F4C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10822")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "QS_1401 旧市街の復興支援\x01",              # 0
            "QS_1402 チャリティeventへの協\x01",      # 1
            "QS_1403 生き別れの父の捜索\x01",            # 2
            "QS_1404 古戦場の調査\x01",                  # 3
            "QS_1405 诺克斯森林道の手配魔獣\x01",      # 4
            "QS_1406 医療物資の捜索\x01",                # 5
            "QS_1407 地下区域Ｃ区画の手配\x01",      # 6
            "QS_1408 ニールセンの取材３\x01",            # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F5F9"),
        (1, "loc_F5F9"),
        (2, "loc_F5F9"),
        (3, "loc_F5F9"),
        (4, "loc_F5F9"),
        (5, "loc_F5F9"),
        (6, "loc_F5F9"),
        (7, "loc_F5F9"),
        (SWITCH_DEFAULT, "loc_F672"),
    )


    label("loc_F5F9")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x4)
    Jump("loc_F681")

    label("loc_F672")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F681")

    label("loc_F681")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1081D")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F6CD"),
        (1, "loc_F8F7"),
        (2, "loc_FB21"),
        (3, "loc_FD4B"),
        (4, "loc_FF75"),
        (5, "loc_1019F"),
        (6, "loc_103C9"),
        (7, "loc_105F3"),
        (SWITCH_DEFAULT, "loc_1081D"),
    )


    label("loc_F6CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7BA")
    OP_29(0x8E, 0x3, 0x0)
    OP_29(0x8E, 0x3, 0x1)
    OP_29(0x8E, 0x3, 0x2)
    OP_29(0x8E, 0x3, 0x10)
    OP_29(0x8E, 0x3, 0x20)
    OP_29(0x8E, 0x3, 0x40)
    OP_29(0x8E, 0x2, 0x0)
    OP_29(0x8E, 0x2, 0x1)
    OP_29(0x8E, 0x2, 0x2)
    OP_29(0x8E, 0x2, 0x3)
    OP_29(0x8E, 0x2, 0x4)
    OP_29(0x8E, 0x2, 0x5)
    OP_29(0x8E, 0x2, 0x6)
    OP_29(0x8E, 0x2, 0x7)
    OP_29(0x8E, 0x2, 0x8)
    OP_29(0x8E, 0x2, 0x9)
    OP_29(0x8E, 0x2, 0xA)
    OP_29(0x8E, 0x2, 0xB)
    OP_29(0x8E, 0x2, 0xC)
    OP_29(0x8E, 0x2, 0xD)
    OP_29(0x8E, 0x2, 0xE)
    OP_29(0x8E, 0x2, 0xF)
    OP_29(0x8E, 0x2, 0x10)
    OP_29(0x8E, 0x2, 0x11)
    OP_29(0x8E, 0x2, 0x12)
    OP_29(0x8E, 0x2, 0x13)
    OP_29(0x8E, 0x2, 0x14)
    OP_29(0x8E, 0x2, 0x15)
    OP_29(0x8E, 0x2, 0x16)
    OP_29(0x8E, 0x2, 0x17)
    OP_29(0x8E, 0x2, 0x18)
    OP_29(0x8E, 0x2, 0x19)
    OP_29(0x8E, 0x2, 0x1A)
    OP_29(0x8E, 0x2, 0x1B)
    OP_29(0x8E, 0x2, 0x1C)
    OP_29(0x8E, 0x2, 0x1D)
    OP_29(0x8E, 0x2, 0x1E)
    OP_29(0x8E, 0x2, 0x1F)

    label("loc_F7BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F7CE")
    OP_29(0x8E, 0x4, 0x2)

    label("loc_F7CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F7E3")
    OP_29(0x8E, 0x1, 0x0)

    label("loc_F7E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F7F8")
    OP_29(0x8E, 0x1, 0x1)

    label("loc_F7F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F80D")
    OP_29(0x8E, 0x1, 0x2)

    label("loc_F80D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F822")
    OP_29(0x8E, 0x1, 0x3)

    label("loc_F822")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F837")
    OP_29(0x8E, 0x1, 0x4)

    label("loc_F837")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F84C")
    OP_29(0x8E, 0x1, 0x5)

    label("loc_F84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F861")
    OP_29(0x8E, 0x1, 0x6)

    label("loc_F861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F876")
    OP_29(0x8E, 0x1, 0x7)

    label("loc_F876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F88B")
    OP_29(0x8E, 0x1, 0x8)

    label("loc_F88B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F8A0")
    OP_29(0x8E, 0x1, 0x9)

    label("loc_F8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F8B5")
    OP_29(0x8E, 0x1, 0xA)

    label("loc_F8B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F8CA")
    OP_29(0x8E, 0x1, 0xB)

    label("loc_F8CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F8DE")
    OP_29(0x8E, 0x4, 0x10)

    label("loc_F8DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F8F2")
    OP_29(0x8E, 0x4, 0x20)

    label("loc_F8F2")

    Jump("loc_1081D")

    label("loc_F8F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9E4")
    OP_29(0x8F, 0x3, 0x0)
    OP_29(0x8F, 0x3, 0x1)
    OP_29(0x8F, 0x3, 0x2)
    OP_29(0x8F, 0x3, 0x10)
    OP_29(0x8F, 0x3, 0x20)
    OP_29(0x8F, 0x3, 0x40)
    OP_29(0x8F, 0x2, 0x0)
    OP_29(0x8F, 0x2, 0x1)
    OP_29(0x8F, 0x2, 0x2)
    OP_29(0x8F, 0x2, 0x3)
    OP_29(0x8F, 0x2, 0x4)
    OP_29(0x8F, 0x2, 0x5)
    OP_29(0x8F, 0x2, 0x6)
    OP_29(0x8F, 0x2, 0x7)
    OP_29(0x8F, 0x2, 0x8)
    OP_29(0x8F, 0x2, 0x9)
    OP_29(0x8F, 0x2, 0xA)
    OP_29(0x8F, 0x2, 0xB)
    OP_29(0x8F, 0x2, 0xC)
    OP_29(0x8F, 0x2, 0xD)
    OP_29(0x8F, 0x2, 0xE)
    OP_29(0x8F, 0x2, 0xF)
    OP_29(0x8F, 0x2, 0x10)
    OP_29(0x8F, 0x2, 0x11)
    OP_29(0x8F, 0x2, 0x12)
    OP_29(0x8F, 0x2, 0x13)
    OP_29(0x8F, 0x2, 0x14)
    OP_29(0x8F, 0x2, 0x15)
    OP_29(0x8F, 0x2, 0x16)
    OP_29(0x8F, 0x2, 0x17)
    OP_29(0x8F, 0x2, 0x18)
    OP_29(0x8F, 0x2, 0x19)
    OP_29(0x8F, 0x2, 0x1A)
    OP_29(0x8F, 0x2, 0x1B)
    OP_29(0x8F, 0x2, 0x1C)
    OP_29(0x8F, 0x2, 0x1D)
    OP_29(0x8F, 0x2, 0x1E)
    OP_29(0x8F, 0x2, 0x1F)

    label("loc_F9E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F9F8")
    OP_29(0x8F, 0x4, 0x2)

    label("loc_F9F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA0D")
    OP_29(0x8F, 0x1, 0x0)

    label("loc_FA0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA22")
    OP_29(0x8F, 0x1, 0x1)

    label("loc_FA22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA37")
    OP_29(0x8F, 0x1, 0x2)

    label("loc_FA37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA4C")
    OP_29(0x8F, 0x1, 0x3)

    label("loc_FA4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA61")
    OP_29(0x8F, 0x1, 0x4)

    label("loc_FA61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA76")
    OP_29(0x8F, 0x1, 0x5)

    label("loc_FA76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FA8B")
    OP_29(0x8F, 0x1, 0x6)

    label("loc_FA8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FAA0")
    OP_29(0x8F, 0x1, 0x7)

    label("loc_FAA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FAB5")
    OP_29(0x8F, 0x1, 0x8)

    label("loc_FAB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FACA")
    OP_29(0x8F, 0x1, 0x9)

    label("loc_FACA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FADF")
    OP_29(0x8F, 0x1, 0xA)

    label("loc_FADF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FAF4")
    OP_29(0x8F, 0x1, 0xB)

    label("loc_FAF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FB08")
    OP_29(0x8F, 0x4, 0x10)

    label("loc_FB08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FB1C")
    OP_29(0x8F, 0x4, 0x20)

    label("loc_FB1C")

    Jump("loc_1081D")

    label("loc_FB21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC0E")
    OP_29(0x90, 0x3, 0x0)
    OP_29(0x90, 0x3, 0x1)
    OP_29(0x90, 0x3, 0x2)
    OP_29(0x90, 0x3, 0x10)
    OP_29(0x90, 0x3, 0x20)
    OP_29(0x90, 0x3, 0x40)
    OP_29(0x90, 0x2, 0x0)
    OP_29(0x90, 0x2, 0x1)
    OP_29(0x90, 0x2, 0x2)
    OP_29(0x90, 0x2, 0x3)
    OP_29(0x90, 0x2, 0x4)
    OP_29(0x90, 0x2, 0x5)
    OP_29(0x90, 0x2, 0x6)
    OP_29(0x90, 0x2, 0x7)
    OP_29(0x90, 0x2, 0x8)
    OP_29(0x90, 0x2, 0x9)
    OP_29(0x90, 0x2, 0xA)
    OP_29(0x90, 0x2, 0xB)
    OP_29(0x90, 0x2, 0xC)
    OP_29(0x90, 0x2, 0xD)
    OP_29(0x90, 0x2, 0xE)
    OP_29(0x90, 0x2, 0xF)
    OP_29(0x90, 0x2, 0x10)
    OP_29(0x90, 0x2, 0x11)
    OP_29(0x90, 0x2, 0x12)
    OP_29(0x90, 0x2, 0x13)
    OP_29(0x90, 0x2, 0x14)
    OP_29(0x90, 0x2, 0x15)
    OP_29(0x90, 0x2, 0x16)
    OP_29(0x90, 0x2, 0x17)
    OP_29(0x90, 0x2, 0x18)
    OP_29(0x90, 0x2, 0x19)
    OP_29(0x90, 0x2, 0x1A)
    OP_29(0x90, 0x2, 0x1B)
    OP_29(0x90, 0x2, 0x1C)
    OP_29(0x90, 0x2, 0x1D)
    OP_29(0x90, 0x2, 0x1E)
    OP_29(0x90, 0x2, 0x1F)

    label("loc_FC0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC22")
    OP_29(0x90, 0x4, 0x2)

    label("loc_FC22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC37")
    OP_29(0x90, 0x1, 0x0)

    label("loc_FC37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC4C")
    OP_29(0x90, 0x1, 0x1)

    label("loc_FC4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC61")
    OP_29(0x90, 0x1, 0x2)

    label("loc_FC61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC76")
    OP_29(0x90, 0x1, 0x3)

    label("loc_FC76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC8B")
    OP_29(0x90, 0x1, 0x4)

    label("loc_FC8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCA0")
    OP_29(0x90, 0x1, 0x5)

    label("loc_FCA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCB5")
    OP_29(0x90, 0x1, 0x6)

    label("loc_FCB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCCA")
    OP_29(0x90, 0x1, 0x7)

    label("loc_FCCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCDF")
    OP_29(0x90, 0x1, 0x8)

    label("loc_FCDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCF4")
    OP_29(0x90, 0x1, 0x9)

    label("loc_FCF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD09")
    OP_29(0x90, 0x1, 0xA)

    label("loc_FD09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD1E")
    OP_29(0x90, 0x1, 0xB)

    label("loc_FD1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD32")
    OP_29(0x90, 0x4, 0x10)

    label("loc_FD32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD46")
    OP_29(0x90, 0x4, 0x20)

    label("loc_FD46")

    Jump("loc_1081D")

    label("loc_FD4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE38")
    OP_29(0x91, 0x3, 0x0)
    OP_29(0x91, 0x3, 0x1)
    OP_29(0x91, 0x3, 0x2)
    OP_29(0x91, 0x3, 0x10)
    OP_29(0x91, 0x3, 0x20)
    OP_29(0x91, 0x3, 0x40)
    OP_29(0x91, 0x2, 0x0)
    OP_29(0x91, 0x2, 0x1)
    OP_29(0x91, 0x2, 0x2)
    OP_29(0x91, 0x2, 0x3)
    OP_29(0x91, 0x2, 0x4)
    OP_29(0x91, 0x2, 0x5)
    OP_29(0x91, 0x2, 0x6)
    OP_29(0x91, 0x2, 0x7)
    OP_29(0x91, 0x2, 0x8)
    OP_29(0x91, 0x2, 0x9)
    OP_29(0x91, 0x2, 0xA)
    OP_29(0x91, 0x2, 0xB)
    OP_29(0x91, 0x2, 0xC)
    OP_29(0x91, 0x2, 0xD)
    OP_29(0x91, 0x2, 0xE)
    OP_29(0x91, 0x2, 0xF)
    OP_29(0x91, 0x2, 0x10)
    OP_29(0x91, 0x2, 0x11)
    OP_29(0x91, 0x2, 0x12)
    OP_29(0x91, 0x2, 0x13)
    OP_29(0x91, 0x2, 0x14)
    OP_29(0x91, 0x2, 0x15)
    OP_29(0x91, 0x2, 0x16)
    OP_29(0x91, 0x2, 0x17)
    OP_29(0x91, 0x2, 0x18)
    OP_29(0x91, 0x2, 0x19)
    OP_29(0x91, 0x2, 0x1A)
    OP_29(0x91, 0x2, 0x1B)
    OP_29(0x91, 0x2, 0x1C)
    OP_29(0x91, 0x2, 0x1D)
    OP_29(0x91, 0x2, 0x1E)
    OP_29(0x91, 0x2, 0x1F)

    label("loc_FE38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE4C")
    OP_29(0x91, 0x4, 0x2)

    label("loc_FE4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE61")
    OP_29(0x91, 0x1, 0x0)

    label("loc_FE61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE76")
    OP_29(0x91, 0x1, 0x1)

    label("loc_FE76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE8B")
    OP_29(0x91, 0x1, 0x2)

    label("loc_FE8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEA0")
    OP_29(0x91, 0x1, 0x3)

    label("loc_FEA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEB5")
    OP_29(0x91, 0x1, 0x4)

    label("loc_FEB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FECA")
    OP_29(0x91, 0x1, 0x5)

    label("loc_FECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEDF")
    OP_29(0x91, 0x1, 0x6)

    label("loc_FEDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEF4")
    OP_29(0x91, 0x1, 0x7)

    label("loc_FEF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF09")
    OP_29(0x91, 0x1, 0x8)

    label("loc_FF09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF1E")
    OP_29(0x91, 0x1, 0x9)

    label("loc_FF1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF33")
    OP_29(0x91, 0x1, 0xA)

    label("loc_FF33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF48")
    OP_29(0x91, 0x1, 0xB)

    label("loc_FF48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF5C")
    OP_29(0x91, 0x4, 0x10)

    label("loc_FF5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF70")
    OP_29(0x91, 0x4, 0x20)

    label("loc_FF70")

    Jump("loc_1081D")

    label("loc_FF75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10062")
    OP_29(0x92, 0x3, 0x0)
    OP_29(0x92, 0x3, 0x1)
    OP_29(0x92, 0x3, 0x2)
    OP_29(0x92, 0x3, 0x10)
    OP_29(0x92, 0x3, 0x20)
    OP_29(0x92, 0x3, 0x40)
    OP_29(0x92, 0x2, 0x0)
    OP_29(0x92, 0x2, 0x1)
    OP_29(0x92, 0x2, 0x2)
    OP_29(0x92, 0x2, 0x3)
    OP_29(0x92, 0x2, 0x4)
    OP_29(0x92, 0x2, 0x5)
    OP_29(0x92, 0x2, 0x6)
    OP_29(0x92, 0x2, 0x7)
    OP_29(0x92, 0x2, 0x8)
    OP_29(0x92, 0x2, 0x9)
    OP_29(0x92, 0x2, 0xA)
    OP_29(0x92, 0x2, 0xB)
    OP_29(0x92, 0x2, 0xC)
    OP_29(0x92, 0x2, 0xD)
    OP_29(0x92, 0x2, 0xE)
    OP_29(0x92, 0x2, 0xF)
    OP_29(0x92, 0x2, 0x10)
    OP_29(0x92, 0x2, 0x11)
    OP_29(0x92, 0x2, 0x12)
    OP_29(0x92, 0x2, 0x13)
    OP_29(0x92, 0x2, 0x14)
    OP_29(0x92, 0x2, 0x15)
    OP_29(0x92, 0x2, 0x16)
    OP_29(0x92, 0x2, 0x17)
    OP_29(0x92, 0x2, 0x18)
    OP_29(0x92, 0x2, 0x19)
    OP_29(0x92, 0x2, 0x1A)
    OP_29(0x92, 0x2, 0x1B)
    OP_29(0x92, 0x2, 0x1C)
    OP_29(0x92, 0x2, 0x1D)
    OP_29(0x92, 0x2, 0x1E)
    OP_29(0x92, 0x2, 0x1F)

    label("loc_10062")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10076")
    OP_29(0x92, 0x4, 0x2)

    label("loc_10076")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1008B")
    OP_29(0x92, 0x1, 0x0)

    label("loc_1008B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100A0")
    OP_29(0x92, 0x1, 0x1)

    label("loc_100A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100B5")
    OP_29(0x92, 0x1, 0x2)

    label("loc_100B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100CA")
    OP_29(0x92, 0x1, 0x3)

    label("loc_100CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100DF")
    OP_29(0x92, 0x1, 0x4)

    label("loc_100DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100F4")
    OP_29(0x92, 0x1, 0x5)

    label("loc_100F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10109")
    OP_29(0x92, 0x1, 0x6)

    label("loc_10109")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1011E")
    OP_29(0x92, 0x1, 0x7)

    label("loc_1011E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10133")
    OP_29(0x92, 0x1, 0x8)

    label("loc_10133")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10148")
    OP_29(0x92, 0x1, 0x9)

    label("loc_10148")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1015D")
    OP_29(0x92, 0x1, 0xA)

    label("loc_1015D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10172")
    OP_29(0x92, 0x1, 0xB)

    label("loc_10172")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10186")
    OP_29(0x92, 0x4, 0x10)

    label("loc_10186")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1019A")
    OP_29(0x92, 0x4, 0x20)

    label("loc_1019A")

    Jump("loc_1081D")

    label("loc_1019F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028C")
    OP_29(0x93, 0x3, 0x0)
    OP_29(0x93, 0x3, 0x1)
    OP_29(0x93, 0x3, 0x2)
    OP_29(0x93, 0x3, 0x10)
    OP_29(0x93, 0x3, 0x20)
    OP_29(0x93, 0x3, 0x40)
    OP_29(0x93, 0x2, 0x0)
    OP_29(0x93, 0x2, 0x1)
    OP_29(0x93, 0x2, 0x2)
    OP_29(0x93, 0x2, 0x3)
    OP_29(0x93, 0x2, 0x4)
    OP_29(0x93, 0x2, 0x5)
    OP_29(0x93, 0x2, 0x6)
    OP_29(0x93, 0x2, 0x7)
    OP_29(0x93, 0x2, 0x8)
    OP_29(0x93, 0x2, 0x9)
    OP_29(0x93, 0x2, 0xA)
    OP_29(0x93, 0x2, 0xB)
    OP_29(0x93, 0x2, 0xC)
    OP_29(0x93, 0x2, 0xD)
    OP_29(0x93, 0x2, 0xE)
    OP_29(0x93, 0x2, 0xF)
    OP_29(0x93, 0x2, 0x10)
    OP_29(0x93, 0x2, 0x11)
    OP_29(0x93, 0x2, 0x12)
    OP_29(0x93, 0x2, 0x13)
    OP_29(0x93, 0x2, 0x14)
    OP_29(0x93, 0x2, 0x15)
    OP_29(0x93, 0x2, 0x16)
    OP_29(0x93, 0x2, 0x17)
    OP_29(0x93, 0x2, 0x18)
    OP_29(0x93, 0x2, 0x19)
    OP_29(0x93, 0x2, 0x1A)
    OP_29(0x93, 0x2, 0x1B)
    OP_29(0x93, 0x2, 0x1C)
    OP_29(0x93, 0x2, 0x1D)
    OP_29(0x93, 0x2, 0x1E)
    OP_29(0x93, 0x2, 0x1F)

    label("loc_1028C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_102A0")
    OP_29(0x93, 0x4, 0x2)

    label("loc_102A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_102B5")
    OP_29(0x93, 0x1, 0x0)

    label("loc_102B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_102CA")
    OP_29(0x93, 0x1, 0x1)

    label("loc_102CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_102DF")
    OP_29(0x93, 0x1, 0x2)

    label("loc_102DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_102F4")
    OP_29(0x93, 0x1, 0x3)

    label("loc_102F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10309")
    OP_29(0x93, 0x1, 0x4)

    label("loc_10309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1031E")
    OP_29(0x93, 0x1, 0x5)

    label("loc_1031E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10333")
    OP_29(0x93, 0x1, 0x6)

    label("loc_10333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10348")
    OP_29(0x93, 0x1, 0x7)

    label("loc_10348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1035D")
    OP_29(0x93, 0x1, 0x8)

    label("loc_1035D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10372")
    OP_29(0x93, 0x1, 0x9)

    label("loc_10372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10387")
    OP_29(0x93, 0x1, 0xA)

    label("loc_10387")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1039C")
    OP_29(0x93, 0x1, 0xB)

    label("loc_1039C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103B0")
    OP_29(0x93, 0x4, 0x10)

    label("loc_103B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103C4")
    OP_29(0x93, 0x4, 0x20)

    label("loc_103C4")

    Jump("loc_1081D")

    label("loc_103C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104B6")
    OP_29(0x94, 0x3, 0x0)
    OP_29(0x94, 0x3, 0x1)
    OP_29(0x94, 0x3, 0x2)
    OP_29(0x94, 0x3, 0x10)
    OP_29(0x94, 0x3, 0x20)
    OP_29(0x94, 0x3, 0x40)
    OP_29(0x94, 0x2, 0x0)
    OP_29(0x94, 0x2, 0x1)
    OP_29(0x94, 0x2, 0x2)
    OP_29(0x94, 0x2, 0x3)
    OP_29(0x94, 0x2, 0x4)
    OP_29(0x94, 0x2, 0x5)
    OP_29(0x94, 0x2, 0x6)
    OP_29(0x94, 0x2, 0x7)
    OP_29(0x94, 0x2, 0x8)
    OP_29(0x94, 0x2, 0x9)
    OP_29(0x94, 0x2, 0xA)
    OP_29(0x94, 0x2, 0xB)
    OP_29(0x94, 0x2, 0xC)
    OP_29(0x94, 0x2, 0xD)
    OP_29(0x94, 0x2, 0xE)
    OP_29(0x94, 0x2, 0xF)
    OP_29(0x94, 0x2, 0x10)
    OP_29(0x94, 0x2, 0x11)
    OP_29(0x94, 0x2, 0x12)
    OP_29(0x94, 0x2, 0x13)
    OP_29(0x94, 0x2, 0x14)
    OP_29(0x94, 0x2, 0x15)
    OP_29(0x94, 0x2, 0x16)
    OP_29(0x94, 0x2, 0x17)
    OP_29(0x94, 0x2, 0x18)
    OP_29(0x94, 0x2, 0x19)
    OP_29(0x94, 0x2, 0x1A)
    OP_29(0x94, 0x2, 0x1B)
    OP_29(0x94, 0x2, 0x1C)
    OP_29(0x94, 0x2, 0x1D)
    OP_29(0x94, 0x2, 0x1E)
    OP_29(0x94, 0x2, 0x1F)

    label("loc_104B6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104CA")
    OP_29(0x94, 0x4, 0x2)

    label("loc_104CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104DF")
    OP_29(0x94, 0x1, 0x0)

    label("loc_104DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104F4")
    OP_29(0x94, 0x1, 0x1)

    label("loc_104F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10509")
    OP_29(0x94, 0x1, 0x2)

    label("loc_10509")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1051E")
    OP_29(0x94, 0x1, 0x3)

    label("loc_1051E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10533")
    OP_29(0x94, 0x1, 0x4)

    label("loc_10533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10548")
    OP_29(0x94, 0x1, 0x5)

    label("loc_10548")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1055D")
    OP_29(0x94, 0x1, 0x6)

    label("loc_1055D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10572")
    OP_29(0x94, 0x1, 0x7)

    label("loc_10572")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10587")
    OP_29(0x94, 0x1, 0x8)

    label("loc_10587")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1059C")
    OP_29(0x94, 0x1, 0x9)

    label("loc_1059C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105B1")
    OP_29(0x94, 0x1, 0xA)

    label("loc_105B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105C6")
    OP_29(0x94, 0x1, 0xB)

    label("loc_105C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105DA")
    OP_29(0x94, 0x4, 0x10)

    label("loc_105DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105EE")
    OP_29(0x94, 0x4, 0x20)

    label("loc_105EE")

    Jump("loc_1081D")

    label("loc_105F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106E0")
    OP_29(0x95, 0x3, 0x0)
    OP_29(0x95, 0x3, 0x1)
    OP_29(0x95, 0x3, 0x2)
    OP_29(0x95, 0x3, 0x10)
    OP_29(0x95, 0x3, 0x20)
    OP_29(0x95, 0x3, 0x40)
    OP_29(0x95, 0x2, 0x0)
    OP_29(0x95, 0x2, 0x1)
    OP_29(0x95, 0x2, 0x2)
    OP_29(0x95, 0x2, 0x3)
    OP_29(0x95, 0x2, 0x4)
    OP_29(0x95, 0x2, 0x5)
    OP_29(0x95, 0x2, 0x6)
    OP_29(0x95, 0x2, 0x7)
    OP_29(0x95, 0x2, 0x8)
    OP_29(0x95, 0x2, 0x9)
    OP_29(0x95, 0x2, 0xA)
    OP_29(0x95, 0x2, 0xB)
    OP_29(0x95, 0x2, 0xC)
    OP_29(0x95, 0x2, 0xD)
    OP_29(0x95, 0x2, 0xE)
    OP_29(0x95, 0x2, 0xF)
    OP_29(0x95, 0x2, 0x10)
    OP_29(0x95, 0x2, 0x11)
    OP_29(0x95, 0x2, 0x12)
    OP_29(0x95, 0x2, 0x13)
    OP_29(0x95, 0x2, 0x14)
    OP_29(0x95, 0x2, 0x15)
    OP_29(0x95, 0x2, 0x16)
    OP_29(0x95, 0x2, 0x17)
    OP_29(0x95, 0x2, 0x18)
    OP_29(0x95, 0x2, 0x19)
    OP_29(0x95, 0x2, 0x1A)
    OP_29(0x95, 0x2, 0x1B)
    OP_29(0x95, 0x2, 0x1C)
    OP_29(0x95, 0x2, 0x1D)
    OP_29(0x95, 0x2, 0x1E)
    OP_29(0x95, 0x2, 0x1F)

    label("loc_106E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106F4")
    OP_29(0x95, 0x4, 0x2)

    label("loc_106F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10709")
    OP_29(0x95, 0x1, 0x0)

    label("loc_10709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1071E")
    OP_29(0x95, 0x1, 0x1)

    label("loc_1071E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10733")
    OP_29(0x95, 0x1, 0x2)

    label("loc_10733")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10748")
    OP_29(0x95, 0x1, 0x3)

    label("loc_10748")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1075D")
    OP_29(0x95, 0x1, 0x4)

    label("loc_1075D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10772")
    OP_29(0x95, 0x1, 0x5)

    label("loc_10772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10787")
    OP_29(0x95, 0x1, 0x6)

    label("loc_10787")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1079C")
    OP_29(0x95, 0x1, 0x7)

    label("loc_1079C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_107B1")
    OP_29(0x95, 0x1, 0x8)

    label("loc_107B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_107C6")
    OP_29(0x95, 0x1, 0x9)

    label("loc_107C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_107DB")
    OP_29(0x95, 0x1, 0xA)

    label("loc_107DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_107F0")
    OP_29(0x95, 0x1, 0xB)

    label("loc_107F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10804")
    OP_29(0x95, 0x4, 0x10)

    label("loc_10804")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10818")
    OP_29(0x95, 0x4, 0x20)

    label("loc_10818")

    Jump("loc_1081D")

    label("loc_1081D")

    Jump("loc_F4C6")

    label("loc_10822")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_53_F4BC end

    SaveToFile()

Try(main)
