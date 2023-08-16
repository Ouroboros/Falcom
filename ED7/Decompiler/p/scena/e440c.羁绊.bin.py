from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e440c.bin",                # FileName
        "e440b",                    # MapName
        "e440b",                    # Location
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
        "e440b",                  # 0
        "莉夏",                   # 1
        "神狼蔡特",               # 2
        "艾莉",                   # 3
        "缇欧",                   # 4
        "兰迪",                   # 5
        "诺艾尔",                 # 6
        "瓦吉",                   # 7
        "SE控制",                 # 8
    ))

    AddCharChip((
        "chr/ch03200.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(2589,    0,       -29,     90,   453,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-1549,   0,       -959,    180,  405,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_311",          # 02, 2
        "Function_3_385",          # 03, 3
        "Function_4_8EB",          # 04, 4
        "Function_5_C44",          # 05, 5
        "Function_6_143A",         # 06, 6
        "Function_7_1849",         # 07, 7
        "Function_8_304D",         # 08, 8
        "Function_9_308C",         # 09, 9
        "Function_10_4D9E",        # 0A, 10
        "Function_11_4DBB",        # 0B, 11
        "Function_12_4E1C",        # 0C, 12
        "Function_13_4E39",        # 0D, 13
        "Function_14_6F17",        # 0E, 14
        "Function_15_6F33",        # 0F, 15
        "Function_16_8923",        # 10, 16
        "Function_17_A8FA",        # 11, 17
        "Function_18_C663",        # 12, 18
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C8 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x40)

    label("loc_29B")

    ClearChrFlags(0x9, 0x80)

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_2C0")
    Event(0, 7)
    Jump("loc_310")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_2D1")
    Event(0, 9)
    Jump("loc_310")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_2E2")
    Event(0, 13)
    Jump("loc_310")

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_2F3")
    Event(0, 15)
    Jump("loc_310")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_304")
    Event(0, 16)
    Jump("loc_310")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_310")
    Event(0, 17)

    label("loc_310")

    Return()

    # Function_1_278 end

    def Function_2_311(): pass

    label("Function_2_311")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF0A070D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Sound(132, 1, 70, 0)
    Sound(497, 1, 40, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_384")

    Return()

    # Function_2_311 end

    def Function_3_385(): pass

    label("Function_3_385")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6A), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8")
    Call(0, 5)
    Jump("loc_400")

    label("loc_3A8")


    ChrTalk(
        0x8,
        (
            "#10704F……我准备在这里\x01",
            "吹一阵风。\x02\x03",
            "#10702F不必急着过来，\x01",
            "做好准备之后再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400")

    Jump("loc_8E7")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_854")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10708F……明天……\x01",
            "终于就要潜入克洛斯贝尔市了。\x02\x03",
            "#10702F离开那里的时间\x01",
            "明明不算太久，\x01",
            "但却有种相当怀念的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F是吗……\x02\x03",
            "#00006F据说，由于结界已经消失，\x01",
            "『神机』开始集中全力防卫城市了……\x02\x03",
            "#00008F彩虹剧团的各位现在\x01",
            "正在做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F我想……即使在这种时候，\x01",
            "大家肯定也在不断练习吧。\x02\x03",
            "不管在什么时候，不管发生了什么事，\x01",
            "大家为了提升作品的完成度，\x01",
            "也都会毫不动摇地一心向前……\x02\x03",
            "#10710F这是伊莉娅小姐的意愿……\x01",
            "也是彩虹剧团的立身之道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F哈哈，或许正如你所说呢。\x02\x03",
            "#00000F……等到克洛斯贝尔市成功解放，\x01",
            "这次的事件也大致解决之后……\x01",
            "你有什么打算？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F……我想见伊莉娅小姐，\x01",
            "然后和以前一样，继续以\x01",
            "演员的身份在彩虹剧团起舞……\x02\x03",
            "不过，我虽然有这样的意愿，\x01",
            "如今却不知今后该怎么做。\x02\x03",
            "#10708F连与伊莉娅小姐和修利\x01",
            "重逢时该说些什么……\x01",
            "都毫无头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F是吗……\x02\x03",
            "#00000F不过，伊莉娅小姐和\x01",
            "彩虹剧团的各位一定都会\x01",
            "接受你的。\x02\x03",
            "现在还是不要想那些难题，\x01",
            "把精力集中在眼前的事情上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10704F……呵呵，说的也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F总之，如果无法解放克洛斯贝尔市，\x01",
            "一切都无法开始。\x02\x03",
            "#00000F我们明天一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10702F好的……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_8E7")

    label("loc_854")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10704F今晚我想在这里安心眺望月亮，\x01",
            "让自己的心情平复下来。\x02\x03",
            "#10710F为了解放克洛斯贝尔市和\x01",
            "彩虹剧团……明天一定要\x01",
            "竭尽全力才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_8E7")

    TalkEnd(0xFE)
    Return()

    # Function_3_385 end

    def Function_4_8EB(): pass

    label("Function_4_8EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDE")

    ChrTalk(
        0x9,
        (
            "#01200F#3C在明天的解放克洛斯贝尔市作战中……\x01",
            "我也会潜入城市，\x01",
            "负责侦查工作。\x02\x03",
            "#01203F虽然要和你们分头行动，\x01",
            "但如果有什么事，我会立刻赶到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F好的，到时就麻烦你了。\x02\x03",
            "#00004F说起来，\x01",
            "听说山岳地带的神狼们\x01",
            "也会协助我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3C是的，我已经吩咐\x01",
            "它们去援助警备队的\x01",
            "反抗组织了。\x02\x03",
            "只要取得了地形优势，\x01",
            "即使对手是『赤色星座』的那些猎兵，\x01",
            "它们应该也能势均力敌地抗衡。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F这样啊……\x01",
            "看来米蕾优三尉那边\x01",
            "有它们协助就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3C总之，我的部下们\x01",
            "也只能帮上这些忙了。\x02\x03",
            "夺回琪雅终究还是\x01",
            "你们的任务。\x02\x03",
            "#01203F要想达成这个目标，\x01",
            "必定要面对各种\x01",
            "难以想象的困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F是啊……但无论发生什么事，\x01",
            "我们都一定要夺回琪雅。\x02\x03",
            "#00000F蔡特，请你继续守护我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3C嗯……\x01",
            "就让我亲眼见证到最后吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 6)
    Jump("loc_C40")

    label("loc_BDE")


    ChrTalk(
        0x9,
        (
            "#01200F#3C夺回琪雅终究还是\x01",
            "你们的任务。\x02\x03",
            "你们是否能完成这项使命……\x01",
            "就让我亲眼见证到最后吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C40")

    TalkEnd(0xFE)
    Return()

    # Function_4_8EB end

    def Function_5_C44(): pass

    label("Function_5_C44")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 200, 1330, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11810, 0)
    SetChrPos(0x101, 1070, 0, 280, 90)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_END)), "loc_C9E")
    OP_93(0x8, 0x10E, 0x0)

    label("loc_C9E")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1265")

    ChrTalk(
        0x101,
        (
            "#6P#00005F莉夏……\x01",
            "你在这里做什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10712F啊……罗伊德警官。\x02\x03",
            "#10710F……我已经做好了明天的准备，\x01",
            "正在思考一些事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11P#10708F#5P……明天……\x01",
            "终于就要潜入克洛斯贝尔市了。\x02\x03",
            "#10702F离开那里的时间\x01",
            "明明不算太久，\x01",
            "但却有种相当怀念的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000F是吗……\x02\x03",
            "#00006F据说，由于结界已经消失，\x01",
            "『神机』开始集中全力防卫城市了……\x02\x03",
            "#00008F彩虹剧团的各位现在\x01",
            "正在做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704F#5P我想……即使在这种时候，\x01",
            "大家肯定也在不断练习吧。\x02\x03",
            "不管在什么时候，不管发生了什么事，\x01",
            "大家为了提升作品的完成度，\x01",
            "也都会毫不动摇地一心向前……\x02\x03",
            "#10710F这是伊莉娅小姐的做法……\x01",
            "也是彩虹剧团的作风。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F哈哈，或许正如你所说呢。\x02\x03",
            "#00000F……等到克洛斯贝尔市成功解放，\x01",
            "这次的事件也大致解决之后……\x01",
            "你有什么打算？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#10704F……我想见伊莉娅小姐，\x01",
            "然后和以前一样，继续以\x01",
            "演员的身份在彩虹剧团起舞……\x02\x03",
            "不过，我虽然有这样的意愿，\x01",
            "如今却不知今后该怎么做。\x02\x03",
            "#10708F连与伊莉娅小姐和修利\x01",
            "重逢时该说些什么……\x01",
            "都毫无头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F……是吗。\x02\x03",
            "#00000F不过，伊莉娅小姐和\x01",
            "彩虹剧团的各位一定都会\x01",
            "接受你的。\x02\x03",
            "不用想那些难题，\x01",
            "只要做真实的自己\x01",
            "就好了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#10712F……真实的自己……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10703F……那个，罗伊德警官。\x02\x03",
            "#10701F稍后可以占用你\x01",
            "一些时间吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F嗯……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704F呵呵，最近我也觉得\x01",
            "自己有点太逞强了呢……\x02\x03",
            "#10710F在明天的作战之前，\x01",
            "想和你稍微\x01",
            "聊聊。\x02\x03",
            "等你做好准备后，\x01",
            "可以再次到甲板来……\x01",
            "一起说说话吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_12D7")

    label("loc_1265")


    ChrTalk(
        0x8,
        (
            "#11P#10704F在明天的作战之前，\x01",
            "想和你稍微\x01",
            "聊聊。\x02\x03",
            "#10710F等你做好准备后，\x01",
            "可以再次到甲板来……\x01",
            "一起说说话吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D7")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受莉夏的邀请\x01",      # 0
            "拒绝\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AD")

    ChrTalk(
        0x101,
        "#6P#00002F没问题，我会过来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10709F呵呵，谢谢。\x02\x03",
            "#10704F……我准备在这里\x01",
            "吹一阵风。\x02\x03",
            "#10702F不必急着过来，\x01",
            "做好准备之后再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 6)
    SetScenarioFlags(0x1AB, 0)
    Jump("loc_1427")

    label("loc_13AD")


    ChrTalk(
        0x8,
        (
            "#11P#10704F……是吗……\x02\x03",
            "#10702F呵呵，如果稍后改变想法了，\x01",
            "也可以再来和我说一声哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F好的，我明白了。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_1427")

    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_C44 end

    def Function_6_143A(): pass

    label("Function_6_143A")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_14DF")
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
    Jump("loc_1848")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_1579")
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
    Jump("loc_1848")

    label("loc_1579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_1613")
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
    Jump("loc_1848")

    label("loc_1613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_16B1")
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
    Jump("loc_1848")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_174B")
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
    Jump("loc_1848")

    label("loc_174B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_17E5")
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
    Jump("loc_1848")

    label("loc_17E5")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F（……先在休息室\x01",
            "  做好明天的准备工作，\x01",
            "  然后再到甲板上来吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1848")

    Return()

    # Function_6_143A end

    def Function_7_1849(): pass

    label("Function_7_1849")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch51800.itc", 0x1F)
    LoadChrToIndex("apl/ch5180A.itc", 0x20)
    LoadChrToIndex("apl/ch5180B.itc", 0x21)
    SoundLoad(3411)
    SoundLoad(3412)
    SoundLoad(3413)
    SoundLoad(3414)
    SoundLoad(3415)
    SoundLoad(3416)
    SoundLoad(3417)
    SoundLoad(3418)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_63(0xA, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(2000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    OP_64(0xA)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00108F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0xA, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_1A2C():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A2C)

    def lambda_1A41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A41)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#5P啊……\x01",
            "艾莉，你先来了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A86():

        label("loc_1A86")

        TurnDirection(0xA, 0x101, 500)
        Yield()
        Jump("loc_1A86")

    QueueWorkItem2(0xA, 2, lambda_1A86)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xA,
        (
            "#3411V#30W嗯……\x01",
            "罗伊德，辛苦你了。\x02\x03",
            "#3412V已经做好明天的准备了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD54)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xF, 1, 0, 8)

    def lambda_1B9B():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B9B)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_68(350, 1000, -3890, 50000)
    MoveCamera(44, 14, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16880, 50000)

    ChrTalk(
        0x101,
        (
            "#00000F#5P嗯，大致完成了。\x02\x03",
            "#00006F不过……\x01",
            "实在算不上是万全的准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2179, 255, 100, 0)

    ChrTalk(
        0xA,
        "#00109F#11P#30W呵呵……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#5P#30W……真不可思议啊……\x01",
            "现在的状况如此危急……\x02\x03",
            "但我的心情却平静得\x01",
            "不可思议。\x02\x03",
            "#00108F贝尔的事，迪塔叔叔的事，\x01",
            "还有小琪雅的事……\x02\x03",
            "#00102F让人不安或担心的事情\x01",
            "明明有这么多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5P是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00004F#5P我也……和你一样啊。\x02\x03",
            "#00008F这大概是因为已经坚定了决心，\x01",
            "或者说，是因为已经明白了自己该做的事情吧……\x02\x03",
            "#00002F总之，多亏有你\x01",
            "和大家的支持。\x02\x03",
            "#00009F我真的非常感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#5P呵呵……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#11P该道谢的是我才对哦。\x02\x03",
            "#00108F老实说，在这种情况下，就算被\x01",
            "不安和焦躁彻底压垮也毫不奇怪……\x02\x03",
            "#00102F正是因为有你在，\x01",
            "我才能像现在这样\x01",
            "站在这里……\x02\x03",
            "#00104F……谢谢。\x01",
            "有你在我身边，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6P艾莉……\x02\x03",
            "#00012F哈哈……\x01",
            "能让你有此感觉，是我的荣幸。\x02\x03",
            "#00004F这大概也可以说明，\x01",
            "我已经渐渐成长为\x01",
            "能让大家依靠的队长了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#11P呵呵，你早就是\x01",
            "我们可靠的队长了啊。\x02\x03",
            "否则的话，大家根本不可能\x01",
            "一路前行到这里。\x02\x03",
            "#00108F不过……我想说的\x01",
            "并不是这个意思。\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6P咦……？\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00106F#5P……这次的事件。\x02\x03",
            "无论结局如何，克洛斯贝尔今后\x01",
            "都将面临十分艰辛的局势。\x02\x03",
            "#00108F我们支援科多半也\x01",
            "无法维持下去了……\x02\x03",
            "到时候，我们每个人都必须要\x01",
            "前往可以最大限度地发挥自己\x01",
            "力量的岗位上努力……\x02\x03",
            "#00101F这也是为了重建克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P……说的没错。\x02\x03",
            "#00008F我会继续当警察……\x02\x03",
            "至于兰迪……\x01",
            "等到国防军恢复成警备队之后，\x01",
            "应该会请求他回去协助吧。\x02\x03",
            "#00003F缇欧大概会回到财团，\x01",
            "负责导力网络方面的工作……\x02\x03",
            "#00001F……至于你……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5P……为了应对突发事件，我会去处理\x01",
            "行政、外交方面的危机管理工作。\x02\x03",
            "需要我做的事，大概就是贡献\x01",
            "那方面的知识与能力。\x02\x03",
            "#00108F在至今为止的留学生活中，\x01",
            "我也积累了不少相关的知识。\x02\x03",
            "#00102F如今想来，简直就像是专门为了\x01",
            "应对如今这种事态呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P#30W……是吗……\x02\x03",
            "#00006F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#5P呵呵……太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P……咦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00102F#5P看样子，你好像也\x01",
            "感到有些失落呢。\x02\x03",
            "#00106F『放心吧，艾莉，你一定没问题的』，\x01",
            "如果你这样鼓励我，我可就不知该如何是好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12P哈哈……\x02\x03",
            "#00006F……其实我也知道，\x01",
            "应该那样说才对……\x02\x03",
            "#00008F但无论如何也无法那样简单干脆地说出口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5P那是……为什么呢……？\x02\x03",
            "#00100F和想到即将与缇欧和兰迪\x01",
            "分别的心情是一样的吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12P这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00113F#5P回答我，罗伊德。\x02\x03",
            "如果说，我现在还有什么不安，\x01",
            "恐怕也只有你会怎么回答我这一点了……\x02\x03",
            "#00108F你应该……也明白吧？\x02\x03",
            "#00116F我为什么会说……\x01",
            "想和你好好聊聊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P…………艾莉………………\x02",
    )

    CloseMessageWindow()
    OP_21(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_93(0x101, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4250, 180)
    SetChrPos(0xA, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#5P其实我……\x01",
            "从相识之初就隐隐有些憧憬你。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x514, 0x5, 0x0, 0x1, 0x2, 0x1, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00105F#11P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5P眼前的女孩楚楚动人，\x01",
            "气质凛然，同时又极具包容感……\x02\x03",
            "#00000F从第一次见面的时候开始，\x01",
            "我就觉得你是一位各方面都十分出色的女性。\x02\x03",
            "#00002F那时候，我很努力地装出一副\x01",
            "平静从容的态度与你交谈……\x02\x03",
            "#00012F但说实话……\x01",
            "其实我一直都非常紧张。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x4, 0x5, 0x6)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00112F#11P#30W罗、罗伊德……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5P过了一个月之后，\x01",
            "我就不再觉得你是处在\x01",
            "不同世界的大小姐了……\x02\x03",
            "但我还是一直在偷偷暗想……\x01",
            "能和那么出色的女孩成为同事，\x01",
            "实在是一件值得骄傲的事。\x02\x03",
            "#00002F哪怕只是陪她聊聊天，\x01",
            "帮上她一点小忙，\x01",
            "对我来说，就是最大的快乐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x6, 0x7, 0x8)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#6P在接近一年的时间里，\x01",
            "无论是快乐还是痛苦，\x01",
            "我们都一同经历过来……\x02\x03",
            "虽然分离过一段时间，\x01",
            "但最终还是如愿重逢……\x02\x03",
            "#00008F到了现在，我的感觉仍然和相识之初时一样……\x02\x03",
            "#00002F不，要比那时更加心动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00116F#11P………罗伊德……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P我喜欢你，艾莉。\x02\x03",
            "不是作为一名同伴……\x01",
            "也不是把你当作家人。\x02\x03",
            "#00000F而是把你视为一个女孩。\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 70, 0)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0xB, 0xC, 0xD)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#00106F#3413V#11P罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_A1(0xA, 0x640, 0x4, 0xD, 0xE, 0xF, 0x10)

    def lambda_2B8F():

        label("loc_2B8F")

        OP_A0(0xFE, 1000, 0x10, 0x12)
        Yield()
        Jump("loc_2B8F")

    QueueWorkItem2(0xA, 3, lambda_2B8F)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00116F#3414V#11P我也……喜欢你。\x02",
    )

    CloseMessageWindow()
    OP_24(0xD56)
    Sleep(300)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    OP_68(400, 1000, -4250, 1200)

    def lambda_2BF3():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BF3)
    Sleep(50)

    def lambda_2C0B():
        OP_A0(0xFE, 1000, 0x1, 0x5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2C0B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)

    def lambda_2C41():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C41)

    def lambda_2C4E():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2C4E)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Fade(800)
    SetCameraDistance(15000, 1000)

    def lambda_2C71():
        OP_A0(0xFE, 1000, 0x9, 0xC)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C71)
    OP_A0(0xA, 1000, 0x9, 0xC)
    Sleep(300)
    OP_A0(0xA, 1000, 0x19, 0x1E)
    Sleep(300)

    ChrTalk(
        0xA,
        "#3415V#11P#40W#2S……………唔…………………\x02",
    )

    CloseMessageWindow()
    OP_24(0xD57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(812, 0, 100, 0)

    def lambda_2CD5():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2CD5)

    def lambda_2CE2():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2CE2)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DDA")

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W哈哈……\x02\x03",
            "#00002F……那个时候的后续，\x01",
            "总算是完成了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#00104F#3416V#11P#40W…………嗯……………\x02\x03",
            "#00116F#3417V我一直、一直在等……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD59)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00012F#6P#40W抱歉，让你久等了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E34")

    label("loc_2DDA")


    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W我一直……\x01",
            "很想这么做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#11P#40W…………我也是………………\x02",
    )

    CloseMessageWindow()

    label("loc_2E34")

    Sleep(300)

    def lambda_2E3C():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2E3C)
    Sleep(50)

    def lambda_2E4C():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2E4C)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W即使我们今后无法继续\x01",
            "走在同一条工作道路……\x02\x03",
            "#00004F我也希望我们能永远珍视彼此，\x01",
            "互相支持，一同前进……\x02\x03",
            "#00002F你愿意和我……成为那样的关系吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xA, 1300, 0x12, 0x17)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00109F#3418V#11P#40W………当然…………！\x02",
    )

    CloseMessageWindow()
    OP_24(0xD5A)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    OP_21(0x157C)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_2F82")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_2F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F94")
    Jump("loc_302A")

    label("loc_2F94")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "罗伊德和艾莉习得\x01",
            "星辰爆击Ⅲ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和艾莉的组合战技\x01",
            "『星辰爆击』得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)

    label("loc_302A")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x28, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 1)
    OP_29(0xB1, 0x1, 0x1)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)

    ClearScenarioFlags(0x1AA, 3)
    SetScenarioFlags(0x22, 0)
    NewScene("e440c", 0, 0, 0)
    IdleLoop()

    Return()

    # Function_7_1849 end

    def Function_8_304D(): pass

    label("Function_8_304D")

    OP_25(0x84, 0x41)
    OP_25(0x1F1, 0x23)
    Sleep(300)
    OP_25(0x84, 0x3C)
    OP_25(0x1F1, 0x1E)
    Sleep(300)
    OP_25(0x84, 0x37)
    OP_25(0x1F1, 0x19)
    Sleep(300)
    OP_25(0x84, 0x32)
    OP_25(0x1F1, 0x14)
    Sleep(300)
    OP_25(0x84, 0x2D)
    Sleep(300)
    OP_25(0x84, 0x28)
    Sleep(300)
    OP_25(0x84, 0x23)
    Return()

    # Function_8_304D end

    def Function_9_308C(): pass

    label("Function_9_308C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("apl/ch51801.itc", 0x1F)
    LoadChrToIndex("apl/ch51802.itc", 0x20)
    SoundLoad(2698)
    SoundLoad(2699)
    SoundLoad(2700)
    SoundLoad(2701)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00202.itp")
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xB, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_31BA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31BA)

    def lambda_31CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31CF)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P（嗯？缇欧……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 250, 0, 1250, 180)
    SetChrPos(0xB, 500, 0, -3750, 180)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7500, 0)
    OP_68(500, 2300, -3750, 3000)
    MoveCamera(125, -5, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(8500, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xB,
        "#00208F#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F#6P#N缇欧？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_68(320, 1000, -2950, 5000)
    MoveCamera(115, 15, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9000, 5000)

    def lambda_335F():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF92A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_335F)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()

    def lambda_33A7():

        label("loc_33A7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_33A7")

    QueueWorkItem2(0xB, 2, lambda_33A7)
    Sleep(1500)
    OP_64(0xB)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xB, 500)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        "#2698V#40W罗伊德……前辈……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA8A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，真罕见啊。\x02\x03",
            "#00002F居然一直等到我出声，\x01",
            "你才察觉到。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#00204F#2699V#11P#40W呵呵……是啊。\x02",
    )

    CloseMessageWindow()
    OP_24(0xA8B)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -3750, 3000)
    MoveCamera(135, 20, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(9000, 3000)
    OP_95(0x101, -500, 0, -3750, 1200, 0x0)
    TurnDirection(0x101, 0xB, 500)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#12P我已经做好明天的准备了。\x02\x03",
            "#00000F虽然算不上万全的准备，\x01",
            "但想到其他人的艰难状况，\x01",
            "这已经十分难得了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5P嗯……\x02\x03",
            "为了和琪雅、科长他们重逢，\x01",
            "我们必须要多加努力。\x02\x03",
            "#00202F而且我也很担心柯贝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P是啊……\x02\x03",
            "#00005F说起来，既然约纳被\x01",
            "送到了米修拉姆……\x02\x03",
            "那财团的罗伯兹主任\x01",
            "现在怎样了？\x02\x03",
            "#00008F毕竟现在的状况如此糟糕……\x01",
            "他是不是已经回列曼自治州了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#5P不，主任并没有\x01",
            "听从财团下达的\x01",
            "撤离指示。\x02\x03",
            "#00208F为了监视已被玛丽亚贝尔小姐\x01",
            "夺走控制权的导力网络状况，\x01",
            "他仍然留在市内……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x1, 0x3)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#00206F#5P不要紧，凭主任的手腕，\x01",
            "肯定能找理由\x01",
            "蒙混过去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P是吗……但还是有点担心呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1200, 0x3, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00202F#5P嗯……\x01",
            "一点点而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0xFA0)
    Fade(1000)
    SetChrSubChip(0xB, 0x4)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xB, 500, 0, -4250, 270)
    OP_68(0, 1100, -4250, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 25, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16000, 50000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00206F#11P罗伊德前辈。\x02\x03",
            "#00208F你愿意陪我聊聊吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P哦，当然没问题。\x02\x03",
            "#00001F莫非是关于\x01",
            "你刚才在看的那封信吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00206F#11P原来你已经发现了……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x4, 0x6)
    Sleep(500)
    Sound(802, 0, 100, 0)
    OP_A0(0xB, 1000, 0x7, 0x8)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00203F#11P经由阿巴斯先生的渠道，\x01",
            "这封信昨天送到了我的手上……\x02\x03",
            "#00201F写信人是我那已经抵达共和国\x01",
            "阿尔泰尔市的父母。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#6P什么……！？\x02\x03",
            "#00002F也就是说，他们为了见你，\x01",
            "特地从雷米菲利亚赶来了吗……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#11P是的，克洛斯贝尔独立之后，\x01",
            "他们通过信件和导力通讯都联络不到我……\x02\x03",
            "所以就借助财团的情报，\x01",
            "来到了那个边境附近的城市。\x02\x03",
            "#00208F不过，由于货运以外的出入境\x01",
            "正在受到完全管制，\x01",
            "所以他们也只能止步于那里了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P这样啊……\x02\x03",
            "#00000F……你怎么不早说啊！\x01",
            "既然如此，赶快开这艘飞艇把你送到阿尔泰尔市……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1300, 0x8, 0xA)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#00204F#11P没有这个必要。\x02\x03",
            "我已经请阿巴斯先生通过那条渠道，\x01",
            "告诉他们我现在平安无事了。\x02\x03",
            "#00208F而且……如果现在和他们见面，\x01",
            "我也许会无法平静心情，影响明天的作战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P………可、可是…………\x02\x03",
            "#00006F#30W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 800, 0xA, 0x8)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00209F#11P呵呵……\x01",
            "请不要露出那种表情。\x02\x03",
            "#00202F等解决了这次的事件之后，\x01",
            "我一定会去见父母的。\x02\x03",
            "#00204F受罗伊德前辈的影响，\x01",
            "我也有点犯思乡病了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P咦……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0xB, 1000, 0xD, 0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30W……和大家分散以后……\x02\x03",
            "我十分不安、寂寞。\x01",
            "听说罗伊德前辈被通缉时，\x01",
            "更是担心得坐立不安。\x02\x03",
            "#00206F能和你重逢……\x02\x03",
            "我真的很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30W就在那个时候，我突然意识到──\x02\x03",
            "啊，原来我是活着的。\x02\x03",
            "#00208F珍视他人的心情，\x01",
            "让我切实感觉到自己活在人世间。\x02\x03",
            "#00202F……为何要活下去，\x01",
            "该如何活下去……\x02\x03",
            "#00209F三年前，想向盖伊先生提出的这个问题，\x01",
            "终于在那个时候得到了答案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P#30W……缇欧………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 1300, 0xB, 0xD)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00206F#11P#30W之后又与艾莉前辈和\x01",
            "兰迪前辈他们重逢……\x02\x03",
            "#00208F大家一起为了琪雅而拼命努力，\x01",
            "一直走到今天这一步……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 60, 0)
    OP_A0(0xB, 1200, 0xD, 0x10)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00212F#11P#30W……然后，在看了这封信之后，\x01",
            "我的心简直就像被溶解的冰块一样，\x01",
            "一下子变得坦率了起来。\x02\x03",
            "#00213F我已经好久没有过……\x01",
            "这种想见爸爸和妈妈的感觉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(400, 1000, -4250, 1200)
    OP_9A(0x101, 0xB, 0x258, 0x1F4, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)

    def lambda_40EA():
        OP_A0(0xFE, 1000, 0x10, 0x13)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_40EA)

    def lambda_40F7():
        OP_A0(0xFE, 1000, 0x20, 0x23)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_40F7)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sound(898, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0x101, 3, 0, 12)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0xB,
        "#00216F#11P#40W#2S…………啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……太好了，\x01",
            "真是太好了……\x02\x03",
            "虽说那个使你转变的契机\x01",
            "让我有点不好意思……\x02\x03",
            "#00002F但你能产生\x01",
            "现在这样的想法，\x01",
            "我实在是太高兴了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x5, 0x13, 0x18, 0x19, 0x18, 0x13)
    Sleep(300)

    ChrTalk(
        0xB,
        "#00215F#11P#30W………罗伊德前辈…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0xBB8)
    Fade(1000)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 0, 0, -3750, 90)
    SetChrPos(0xB, 500, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(140, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 20, 0, 50000)
    SetCameraDistance(9000, 50000)

    def lambda_42A7():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42A7)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_A1(0xB, 0x320, 0x3, 0x1, 0x2, 0x3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30W……我有两个请求。\x02\x03",
            "你愿意答应我吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#12P没问题，无论什么事情都可以。\x02\x03",
            "#00009F不要客气，说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30W首先，第一件事是……\x02\x03",
            "#00208F虽然我也很喜欢被你\x01",
            "摸摸头……\x02\x03",
            "#00201F但在如此美丽的夜晚，\x01",
            "你这种举动未免也太像哄小孩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12P这、这样吗？\x02\x03",
            "#00012F啊，说来也是。\x01",
            "如果大哥或兰迪摸我的头，\x01",
            "我也会觉得他们把我当小孩子呢。\x02\x03",
            "#00000F唔……那就……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(1500)
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1950, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#12P缇、缇欧……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_A1(0xB, 0x3E8, 0x5, 0x1E, 0x2B, 0x2C, 0x2B, 0x1E)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            "#40W那、那个……\x02\x03",
            "重逢的时候，我冲过去抱住你，\x01",
            "好像让你有点痛……\x02\x03",
            "……现在这样，应该就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#12P#30W啊……嗯……\x02\x03",
            "#00004F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(250, 1000, -3750, 1000)
    OP_96(0x101, 0xFFFFFF9C, 0x0, 0xFFFFF15A, 0x1F4, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_465D():
        OP_A0(0xFE, 1000, 0x1E, 0x22)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_465D)

    def lambda_466A():
        OP_A0(0xFE, 1000, 0x36, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_466A)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        (
            "#05524F#2700V#5P#40W呵呵……好温暖……\x02\x03",
            "#05526F#2701V不过，我可没有艾莉前辈\x01",
            "抱起来那么舒服，\x01",
            "真是抱歉了……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA8D)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#12P#30W不、不会啊……\x02\x03",
            "#00008F（话说回来，有点难以控制啊……\x01",
            "  ……缇欧身上那种甘甜的气味……）\x02\x03",
            "#00011F（……不对！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 60, 0)

    def lambda_478F():
        OP_A0(0xFE, 1000, 0x22, 0x25)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_478F)

    def lambda_479C():
        OP_A0(0xFE, 1000, 0x39, 0x3C)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_479C)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#12P咳咳……\x01",
            "那另一个请求是什么？\x02\x03",
            "#00000F既然已经把话说到这里了，\x01",
            "我一定会奉陪到底。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x5, 0x25, 0x2E, 0x2F, 0x2E, 0x25)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05524F#5P嗯，另一个请求是……\x02\x03",
            "#05522F等事件告一段落，\x01",
            "我的父母来到克洛斯贝尔以后，\x01",
            "我希望你能陪我一起去见他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009F#12P哦，这当然没问题，\x01",
            "我早就想拜会他们了。\x02\x03",
            "#00002F不过，这种事情根本就不必\x01",
            "特地出言请求吧……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05526F#5P不是的，并不只是单纯的拜会……\x02\x03",
            "#05528F我想向他们简单说明一下\x01",
            "自己留在克洛斯贝尔的原因。\x02\x03",
            "#05521F如果不这样做，\x01",
            "他们一定不会轻易答应的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05524F#5P我喜欢这个有大家，\x01",
            "有咪西，还有导力网络的\x01",
            "克洛斯贝尔……\x02\x03",
            "#05528F但是……\x01",
            "比起这些……\x02\x03",
            "#05522F我更想留在让我明白『为何要活下去，\x01",
            "该如何活下去』这个问题的重要之人的身边……\x02\x03",
            "#05529F我打算这样告诉他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#12P#4S咦咦咦！？#3S\x02\x03",
            "#00011F等、等一下！\x01",
            "这简直就像是……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x2E)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05531F#5P你不是刚刚才说过吗？\x01",
            "『无论什么事情都可以』……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#00012F#12P啊啊！真是的，我明白了！\x02\x03",
            "#00002F等这次的事件告一段落之后，\x01",
            "我一定会和你一起去问候你的双亲的！\x02\x03",
            "#00006F唉，现在就得开始努力思考\x01",
            "到时候该如何解释了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x3E)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#05529F#5P呵呵……\x01",
            "请好好加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(812, 0, 60, 0)
    SetChrSubChip(0xB, 0x2E)
    Sleep(50)
    SetChrSubChip(0xB, 0x25)
    Sleep(200)
    SetCameraDistance(10500, 3500)

    def lambda_4C86():
        OP_A0(0xFE, 1000, 0x26, 0x29)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4C86)

    def lambda_4C93():
        OP_A0(0xFE, 1000, 0x3C, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4C93)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    OP_21(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_4CD7")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_4CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CE9")
    Jump("loc_4D7B")

    label("loc_4CE9")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "罗伊德和缇欧习得\x01",
            "Ω强袭Ⅲ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和缇欧的组合战技\x01",
            "『Ω强袭』得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)

    label("loc_4D7B")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x29, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 2)
    OP_29(0xB1, 0x1, 0x2)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)

    ClearScenarioFlags(0x1AA, 4)
    SetScenarioFlags(0x22, 0)
    NewScene("e440c", 0, 0, 0)
    IdleLoop()

    Return()

    # Function_9_308C end

    def Function_10_4D9E(): pass

    label("Function_10_4D9E")

    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_10_4D9E end

    def Function_11_4DBB(): pass

    label("Function_11_4DBB")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A0(0xFE, 900, 0x0, 0x3)
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 900, 0x4, 0xC)
    Sleep(300)
    OP_A0(0xFE, 1000, 0xC, 0xF)
    Sound(318, 0, 100, 0)
    Sleep(200)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x10, 0x14)
    Sleep(500)
    Sound(812, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x14, 0x1B)
    Sleep(300)
    OP_A0(0xFE, 1000, 0x1B, 0x1E)
    Return()

    # Function_11_4DBB end

    def Function_12_4E1C(): pass

    label("Function_12_4E1C")

    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrSubChip(0xFE, 0x23)
    Return()

    # Function_12_4E1C end

    def Function_13_4E39(): pass

    label("Function_13_4E39")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("apl/ch51804.itc", 0x1F)
    LoadChrToIndex("apl/ch51805.itc", 0x20)
    SoundLoad(2778)
    SoundLoad(2779)
    SoundLoad(2780)
    SoundLoad(2781)
    SoundLoad(2782)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(4, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis316.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_4FEA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FEA)

    def lambda_4FFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4FFF)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00300F#2778V#12P#N#30W哟，你来啦。\x02",
    )

    CloseMessageWindow()
    OP_24(0xADA)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#5P兰迪。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 500, 0, 1250, 180)
    SetChrPos(0xC, 500, 0, -3750, 0)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    OP_68(500, 1600, -3750, 5000)
    MoveCamera(125, 1, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9500, 5000)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xC,
        (
            "#2779V#40W真是的，虽说是我主动相约，\x01",
            "但在这样的夜晚，你怎么能把\x01",
            "时间留给一个大男人呢。\x02\x03",
            "#2780V难道你就没有一个可以聊聊\x01",
            "情感话题的对象吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xADC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(630, 1000, -3200, 3000)
    MoveCamera(120, 10, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10000, 3000)
    Sound(100, 0, 100, 0)

    def lambda_5257():

        label("loc_5257")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5257")

    QueueWorkItem2(0xC, 2, lambda_5257)
    OP_95(0x101, 250, 0, -1750, 1200, 0x0)
    TurnDirection(0x101, 0xC, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6P……多管闲事。\x02\x03",
            "#00001F这可是作战前夜……\x01",
            "根本没有心情去考虑那种事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#11P笨蛋！这种时候才是攻陷\x01",
            "对方的大好时机呢。\x02\x03",
            "#00308F①『罗伊德，我好不安……』\x02\x03",
            "#00301F②『别害怕，有我在呢。』\x02\x03",
            "#00309F③『紧紧拥入怀中！』\x01",
            "——正好可以使用这样的黄金连续技啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P最后一步也太跳跃了吧……\x02\x03",
            "#00012F我现在真是不得不怀疑了，\x01",
            "兰迪，你真的很受女孩子欢迎吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00310F#11P这叫什么话嘛～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0xFA0)
    OP_68(110, 1000, -4070, 4000)
    MoveCamera(135, 15, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(10000, 30000)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    EndChrThread(0xC, 0x2)
    OP_93(0xC, 0xB4, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xC,
        "#00300F#5P……已经做好明天的准备了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，老实说，\x01",
            "实在算不上是万全的准备……\x02\x03",
            "#00001F但想到米蕾优三尉他们的艰辛状况，\x01",
            "我们根本没有发牢骚的资格啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P是啊……\x02\x03",
            "#00303F总统大概会派出那些猎兵，\x01",
            "去镇压反抗组织和黑月。\x02\x03",
            "#00308F叔叔和谢莉\x01",
            "应该不会轻易出动……\x02\x03",
            "#00301F但只要有加雷斯那种实力的人出阵，\x01",
            "战斗就一定会相当艰险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P是吗……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    EndChrThread(0xC, 0x2)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P『赤色星座』……\x01",
            "战斗力比传闻中还要强悍啊。\x02\x03",
            "#00000F难怪会被称为\x01",
            "大陆西部最强的猎兵团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P说到这方面的历史，\x01",
            "可以追溯到中世纪的黑暗时代呢。\x02\x03",
            "#00301F狂战士奥兰多……\x02\x03",
            "据说在当时就已经是\x01",
            "相当有名的战士家族了。\x02\x03",
            "#00308F不断吸纳最新的战斗技术，\x01",
            "并以特殊的锻炼方式强化肉体，\x01",
            "以此维持『最强』之名的战士团……\x02\x03",
            "#00303F到了近代，则转型为猎兵团，\x01",
            "并以家族的徽章——赤色蝎子为名，\x01",
            "继续战斗着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P原来是这样……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#12P难道说……\x02\x03",
            "#00001F当时在旧城区的那次竞技，\x01",
            "就是以那种锻炼方式为原型的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#00309F#5P哈哈，真亏你能发现呢。\x02\x03",
            "#00300F那正是以『赤色星座』的战斗训练\x01",
            "为基础的，只是做了一些改动。\x02\x03",
            "#00306F原有的规则更接近于实战，\x01",
            "是随时都有丧命危险的残酷训练。\x02\x03",
            "我从小就要每天接受那样的训练，\x01",
            "甚至都到了吐血的程度。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P原来如此……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00000F#12P……让你参加那种训练的人，\x01",
            "就是你那被称作『斗神』的父亲吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P嗯，\x01",
            "巴德尔·奥兰多。\x02\x03",
            "#00308F简直就像钢铁狮子一样\x01",
            "严厉而毫不留情的老爸。\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0x1770)
    OP_93(0xC, 0xB4, 0x190)
    Fade(1000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W三年前……\x02\x03",
            "『斗神』交给我\x01",
            "一项任务。\x02\x03",
            "#00308F目标是我们的宿敌──\x01",
            "『西风旅团』猎兵团的两个中队……\x02\x03",
            "#00311F任务内容是率领我的部队\x01",
            "歼灭全部敌人。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(15000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30W敌方兵力是我们的两倍……\x02\x03",
            "老实说，如果凭实力正面抗衡，\x01",
            "战斗力的差距实在太大了。\x02\x03",
            "不过，我们有可以\x01",
            "奇袭和利用地形的优势。\x02\x03",
            "于是我……\x02\x03",
            "……利用了一个在平日里\x01",
            "用于补给的小村子。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30W我以奇袭为佯攻，\x01",
            "把其中一个中队引向村子……\x02\x03",
            "然后引起山泥塌陷，将他们隔开，\x01",
            "一口气击溃了另一个中队。\x02\x03",
            "之后，又炸毁了村外的仓库，\x01",
            "使敌人陷入混乱……\x02\x03",
            "我预判了他们撤离村子时的路线，\x01",
            "在路途中聚集全部火力，歼灭了剩下的中队。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30W……按照我设想的计划，\x01",
            "本应不会有任何一个村民为此牺牲。\x02\x03",
            "但战场上的偶然性极强，\x01",
            "计划落空了。\x02\x03",
            "最后，歼灭敌人的位置就在距离\x01",
            "村子仅有五十亚距的地方……\x02\x03",
            "有一家杂货店被卷了进来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#40W……那家杂货店的店员，是我除了猎兵同伴以外，\x01",
            "结识的第一个可以称作朋友的人。\x02\x03",
            "在没有任务的时候，我偶尔会和他一起\x01",
            "在酒馆喝酒、胡闹、搭讪……\x02\x03",
            "他曾经说过，自己的梦想是有朝一日\x01",
            "到大城市开一家属于自己的店。\x02\x03",
            "而那个梦想，那条生命，却被我夺去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(858, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(1300)
    SetMessageWindowPos(280, 170, -1, -1)
    SetChrName("谢莉")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W哇啊啊！\x01",
            "兰迪哥，你可真能干啊¤\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("战鬼西格蒙德")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x14),
            "#30W呵呵，你合格了，兰道夫。\x02\x03",
            "经过这次的『试炼』，\x01",
            "你已被确定为下一任『斗神』。\x02\x03",
            "为了继承大哥的威名，\x01",
            "今后也要继续努力。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P#30W……很压抑的一段往事吧？\x02\x03",
            "#00308F其实我并不是因为他的死而受到打击，\x01",
            "从而决定离开战场。\x02\x03",
            "也不是厌倦了猎兵\x01",
            "这种生存方式。\x02\x03",
            "#00303F我只是……\x01",
            "想不明白。\x02\x03",
            "那家伙希望有朝一日拥有一家\x01",
            "属于自己的店铺……\x02\x03",
            "这个小小的梦想，与我迟早\x01",
            "成为『斗神』，并至死战斗的人生……\x02\x03",
            "#00311F到底哪个更有意义？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P#30W……兰迪………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W这大概就是……\x01",
            "我所背负的『业障』吧。\x02\x03",
            "我生于奥兰多一族，\x01",
            "却未能化身为修罗，\x01",
            "只能浑浑噩噩地游荡在战场上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P兰迪，你是想彻底斩断\x01",
            "自己的『业障』吧……？\x02\x03",
            "#00001F以超越叔叔这种方式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P……算是吧。\x02\x03",
            "#00308F在老爸已经死去的如今，\x01",
            "已经没有其它方法可以斩断『业障』了。\x02\x03",
            "如果我能凭借自己现在的力量和立足之地，\x01",
            "成功超越那个怪物的话……\x02\x03",
            "#00300F也就算是把三年前\x01",
            "就该做的了断完成了。\x02\x03",
            "#00304F那样一来……从此以后也就不会\x01",
            "继续随波逐流地混日子了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64AE")

    ChrTalk(
        0x101,
        (
            "#00004F#6P……是吗……\x02\x03",
            "#00000F你肯定不介意让我以搭档的身份\x01",
            "助你一臂之力吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_650C")

    label("loc_64AE")


    ChrTalk(
        0x101,
        (
            "#00004F#6P……是吗……\x02\x03",
            "#00000F既然你愿意告诉我这些，\x01",
            "那就肯定不介意让我助你一臂之力吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_650C")

    TurnDirection(0xC, 0x101, 400)
    Sleep(250)

    ChrTalk(
        0xC,
        (
            "#00302F#11P当然，拜托你了。\x02\x03",
            "#00306F如果可以，我自然想独自解决，\x01",
            "但对手实在太过强大了。\x02\x03",
            "#00300F不好意思，就让我依赖你一次吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_660C")

    ChrTalk(
        0x101,
        (
            "#00004F#6P嗯，当然没问题。\x02\x03",
            "#00002F能成为你的搭档真是太好了……\x01",
            "你愿意依赖我，我非常高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6668")

    label("loc_660C")


    ChrTalk(
        0x101,
        (
            "#00004F#6P当然没问题。\x02\x03",
            "#00002F能成为你的同伴真是太好了……\x01",
            "你愿意依赖我，我非常高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6668")


    ChrTalk(
        0xC,
        (
            "#00315F#11P呵呵……不是和你说过吗，\x01",
            "不要总说这种会害我感动的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6P哎……？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(1000)
    SetChrPos(0x101, -600, 0, -3750, 90)
    SetChrPos(0xC, 600, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(135, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 15, 0, 70000)
    SetCameraDistance(9000, 70000)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x1, 0x2, 0x2, 0x2)
    Sound(854, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x2, 0x3, 0x3, 0x3)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0xC, 0x4)
    OP_0D()
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#00005F那是……酒吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xC,
        (
            "#00304F#5P朗姆酒，而且相当高级。\x02\x03",
            "#00300F这是我当年和那家伙一起\x01",
            "寄存在村中酒馆的酒。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00000F#12P……是吗………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 100, 0)
    Sound(857, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x5, 0x4, 0x5, 0x6, 0x6, 0x6)

    ChrTalk(
        0xC,
        (
            "#00300F#5P我虽然把这瓶酒带到了克洛斯贝尔，\x01",
            "和来复枪一起寄存了起来，但却始终无法把它喝掉。\x02\x03",
            "#00304F不过，我现在终于觉得\x01",
            "自己可以把剩下的酒喝掉了。\x02\x03",
            "#00302F就当是在决战前夜给我打打气，\x01",
            "可以陪我喝一杯吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00002F#12P当然没问题……那就不客气了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6993():
        OP_A0(0xFE, 1000, 0x7, 0x8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_6993)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_69A9():
        OP_A0(0xFE, 1000, 0x1, 0x2)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69A9)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0x9)
    OP_0D()
    Sleep(1000)
    Sleep(1000)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0xA)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(1000)
    Sleep(300)

    def lambda_69EE():
        OP_A0(0xFE, 800, 0xA, 0xC)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_69EE)
    Sleep(100)

    def lambda_69FE():
        OP_A0(0xFE, 1000, 0x4, 0x6)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69FE)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#00304F#5P……刚好空了。\x02\x03",
            "#00300F别太勉强哦。\x01",
            "虽然量不多，但这种酒相当烈。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xC, 0x8)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#12P我已经是成年人了，\x01",
            "喝这么一点没问题的。\x02\x03",
            "#00000F我们干杯吧，兰迪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00302F#5P好。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_6AE4():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6AE4)

    def lambda_6AFD():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_6AFD)
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0xC, 0xD)
    Sleep(50)
    Sound(856, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xC, 3)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xC, 0xE)
    SetChrSubChip(0x101, 0x8)
    OP_0D()
    Sleep(1000)

    def lambda_6B49():
        OP_A0(0xFE, 1000, 0xE, 0x10)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_6B49)
    Sound(2030, 255, 60, 0)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    WaitChrThread(0xC, 3)
    OP_A1(0xC, 0x3E8, 0x8, 0x10, 0x11, 0x12, 0x12, 0x13, 0x14, 0x13, 0x12)
    OP_A0(0x101, 1000, 0x9, 0xB)

    ChrTalk(
        0x101,
        (
            "#00015F#12P#40W哇……\x02\x01",
            "#00008F#30W……咳咳，果然很烈啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00309F#5P哈哈，我不是提醒过你嘛。\x02\x03",
            "#00302F这就是只属于\x01",
            "大人的味道哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_6C19():
        OP_A0(0xFE, 1000, 0x15, 0x16)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_6C19)

    def lambda_6C26():
        OP_A0(0xFE, 1000, 0xC, 0xD)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C26)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00013F#12P唔……说得就像\x01",
            "只有你才是大人一样。\x02\x03",
            "#00004F我说啊，兰迪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00305F#5P嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 80, 0)
    OP_A0(0x101, 1000, 0xD, 0xE)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00002F#12P等这次事件告一段落之后，\x01",
            "我想和你一起去一趟后巷的爵士酒吧。\x02\x03",
            "一起在那里寄存一瓶\x01",
            "新酒如何？\x02\x03",
            "#00012F如果可以，最好挑瓶\x01",
            "味道没这么烈的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1950, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x8, 0x16, 0x17, 0x18, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00302F#2781V#5P#40W哈哈……说的也是啊。\x02",
    )

    CloseMessageWindow()
    OP_24(0xADD)
    OP_57(0x0)
    OP_5A()
    OP_A1(0xC, 0x3E8, 0x3, 0x18, 0x19, 0x1A)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#00315F#2782V#5P#40W好啊……到时我们一起去吧！\x02",
    )

    CloseMessageWindow()
    OP_24(0xADE)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10500, 3000)
    FadeToDark(2000, 0, -1)
    OP_A1(0xC, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    OP_21(0x1194)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_6E50")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_6E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E62")
    Jump("loc_6EF4")

    label("loc_6E62")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "罗伊德和兰迪习得\x01",
            "燃烧之怒Ⅲ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和兰迪的组合战技\x01",
            "燃烧之怒得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)

    label("loc_6EF4")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x2A, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 3)
    OP_29(0xB1, 0x1, 0x3)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)

    ClearScenarioFlags(0x1AA, 5)
    SetScenarioFlags(0x22, 0)
    NewScene("e440c", 0, 0, 0)
    IdleLoop()

    Return()

    # Function_13_4E39 end

    def Function_14_6F17(): pass

    label("Function_14_6F17")

    OP_95(0x101, -500, 0, -3750, 1000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_14_6F17 end

    def Function_15_6F33(): pass

    label("Function_15_6F33")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    LoadChrToIndex("apl/ch51806.itc", 0x20)
    LoadChrToIndex("apl/ch51807.itc", 0x21)
    SoundLoad(3532)
    SoundLoad(3533)
    SoundLoad(3534)
    SoundLoad(3535)
    SoundLoad(4110)
    SoundLoad(3536)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis337.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis338.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xD, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10106F#3532V#40W……唉………\x01",
            "…………怎么办啊………\x02\x03",
            "#10108F#3533V怎么能在这种时候…#800W…\x01",
            "#10101F#40W不过，如果错过这个机会……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCD)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0xD, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_71C1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71C1)

    def lambda_71D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_71D6)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        "#00002F#5P诺艾尔，你已经来了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7245():

        label("loc_7245")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_7245")

    QueueWorkItem2(0xD, 2, lambda_7245)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10112F#3534V#12P#40W罗、罗伊德警官！\x01",
            "你辛苦了！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCE)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_72CD():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72CD)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xD, 500)
    EndChrThread(0xD, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，你也辛苦了。\x02\x03",
            "#00000F已经和索妮亚司令\x01",
            "联络过了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xD,
        (
            "#30W啊，是的。\x02\x03",
            "司令说，在明天的作战中，\x01",
            "她会让贝尔加德门和唐古拉姆门的\x01",
            "部队在原地待命到正午时分。\x02\x03",
            "但一旦超过这个时限，\x01",
            "她就不得不派兵介入了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P是吗……不过，能让部队\x01",
            "暂时待命，就已经帮了大忙了。\x02\x03",
            "#00013F这样一来，我们的任务就\x01",
            "更加重要了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10103F#11P是的……\x02\x03",
            "#10108F#30W…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P……市内的国防军应该\x01",
            "都已经被调到外围进行都市防御了。\x02\x03",
            "#00001F我想还是可以避免和他们在\x01",
            "市内开战的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11P不用担心，关于这一点，\x01",
            "我已经做好觉悟了。\x02\x03",
            "#10108F只是觉得自己实在是\x01",
            "有点丢人……\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xFA0)
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6P什么……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xD, 500, 0, -3750, 270)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#5P#30W其实我一直都觉得独立国\x01",
            "和国防军是错误的。\x02\x03",
            "#10106F可我却……没有米蕾优前辈那种\x01",
            "毅然投身于反抗组织的气概，\x01",
            "而是选择了随波逐流……\x02\x03",
            "这让我明白到，\x01",
            "自己一直都活在名为警备队的\x01",
            "狭小世界中。\x02\x03",
            "#10113F难得司令给了我外调至支援科\x01",
            "工作的机会，而我却……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P其实……大家都是一样的。\x02\x03",
            "#00008F如果没有琪雅和大家，\x01",
            "我大概也会选择顺应大势。\x02\x03",
            "#00012F毕竟我本来也不是\x01",
            "能做出什么大事的性格。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10112F#5P这个……\x01",
            "我可不这么想。\x02\x03",
            "#10114F如果不是那样的性格，\x01",
            "怎么会说出『你就是我的人了』这种……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P什么？\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10112F#5P啊！没什么！\x01",
            "真的没什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P？？？\x02\x03",
            "#00004F总之，最重要的还是有没有\x01",
            "一个让人下定决心的契机。\x02\x03",
            "而你抓住了那个契机，\x01",
            "最终选择跟我们一起前行。\x02\x03",
            "#00008F至于这个决定是否正确，\x01",
            "不能由我来断言……\x02\x03",
            "#00002F但是你帮了我们很多，\x01",
            "我真的很高兴。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10114F#5P罗、罗伊德警官……\x02\x03",
            "#10106F……啊～～～\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#11P#30W（冷、冷静下来！\x01",
            "  诺艾尔·希卡……！）\x02\x03",
            "#10103F（要像演习时一样，\x01",
            "  迅速且准确地判断状况，\x01",
            "  并控制好士气……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12P对了，你不是说有事\x01",
            "要拜托我吗……\x02\x03",
            "#00002F那是什么事？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#10105F#5P啊，是的！\x01",
            "其实是这样的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            "#10106F#5P……其实……那个……\x02\x03",
            "#10108F我想问个有点奇怪的\x01",
            "问题……\x02\x03",
            "#10101F你、你现在有正在交往的\x01",
            "对象吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12P咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5P不、不是的！\x01",
            "我没有什么特别的意思！\x02\x03",
            "#10102F只是……对了，只是和芙兰随便\x01",
            "聊过一下，讨论你有没有女朋友～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12P哦、哦……原来如此。\x02\x03",
            "#00012F哈哈，女孩子好像\x01",
            "很喜欢聊这类话题呢。\x02\x03",
            "#00006F唔……很遗憾，我现在没有女朋友哦。\x02\x03",
            "#00000F身边明明有那么多好女孩……\x01",
            "仔细想想，我还真是有点没用啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5P#30W啊、啊哈哈……哪有的事。\x01",
            "（应该不是故意这么说的吧……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xBB8)
    Sleep(1200)

    ChrTalk(
        0xD,
        "#10103F#5P#30W咳咳……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xD, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 2000)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    OP_68(0, 1000, -4250, 70000)
    MoveCamera(35, 20, 0, 70000)
    OP_6E(500, 70000)
    SetCameraDistance(14500, 70000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10103F#3535V#11P#40W那个，既然如此……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#10101F#4110V#11P#40W你可以暂时\x01",
            "收下这东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100E)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00005F这是……？\x02\x03",
            "#00001F克洛斯贝尔警备队的身份铭牌？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xD,
        (
            "#10104F#11P是的，重组为国防军的时候，\x01",
            "这东西就已经没有用处了……\x02\x03",
            "#10100F可我却无法把它丢弃，\x01",
            "一直都带在身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#6P是吗……\x02\x03",
            "#00005F不过，为什么要给我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11P……老实说，我认为明天的作战\x01",
            "一定会十分严峻。\x02\x03",
            "#10101F万一我出了什么意……\x02\x03",
            "#10112F不……只是想把它送给你当作护身符，\x01",
            "保佑明天的作战顺利成功。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P诺艾尔……\x02\x03",
            "#00004F……明白了，\x01",
            "能收下它，我很高兴。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(800)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10109F#11P啊……\x01",
            "谢谢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈，这不是什么\x01",
            "值得道谢的事啊。\x02\x03",
            "#00008F而且你也会和我们\x01",
            "一起行动……\x02\x03",
            "#00000F一定要记住，\x01",
            "在危急时刻千万不要\x01",
            "产生牺牲自己的念头哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10111F#11P#30W你、你为何会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P这点心事，我还是看得出来的。\x02\x03",
            "#00001F刚才也说过了，\x01",
            "关于抓捕我们的那件事，\x01",
            "你完全不必自责。\x02\x03",
            "#00002F我只希望你能以支援科成员\x01",
            "这个身份和我们一起前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10114F#11P#30W……罗伊德警官……\x02\x03",
            "#10116F（抽泣）……\x01",
            "……好的，我明白了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6P哈哈……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#6P话说回来，把自己的铭牌\x01",
            "交给他人保管吗……\x02\x03",
            "#00012F哈哈，总觉得这就像是\x01",
            "恋人间的习惯呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10114F#11P……！\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(300)

    def lambda_8429():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_8429)
    WaitChrThread(0xD, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W……唔～～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P诺艾尔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(250)
    Sound(812, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    OP_A1(0x101, 0x320, 0x7, 0x0, 0x1, 0x2, 0x1, 0x2, 0x1, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00011F#6P那个……请问……\x02\x03",
            "#00012F难道说……\x01",
            "你真的是那个意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W……………………（点头）\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W是、是吗……\x02\x03",
            "#00000F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯……我也不知道\x01",
            "这能否算是回应……\x02\x03",
            "#00000F你可以收下这个吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10114F#5P#30W咦……\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(150)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    AnonymousTalk(
        0xD,
        (
            "#10105F#11P这是……\x01",
            "……克洛斯贝尔警察局的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002F#6P我现在还是现役警察，\x01",
            "这个东西本不该离身……\x02\x03",
            "#00004F但在这次的事件彻底解决之前，\x01",
            "我希望暂时由你替我保管。\x02\x03",
            "#00000F等情况平息下来之后……\x01",
            "再由我主动对你说出那些话吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    ChrTalk(
        0xD,
        "#10116F#11P#30W#2S……………啊…………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10117F#3536V#11P#30W好的……我很乐意！\x02",
    )

    CloseMessageWindow()
    OP_24(0xDD0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(16000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    OP_21(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_8854")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_8854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8866")
    Jump("loc_8900")

    label("loc_8866")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "罗伊德和诺艾尔习得\x01",
            "勇猛之心Ⅱ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和诺艾尔的组合战技\x01",
            "『勇猛之心』得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)

    label("loc_8900")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x25, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 4)
    OP_29(0xB1, 0x1, 0x4)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)

    ClearScenarioFlags(0x1AA, 6)
    SetScenarioFlags(0x22, 0)
    NewScene("e440c", 0, 0, 0)
    IdleLoop()

    Return()

    # Function_15_6F33 end

    def Function_16_8923(): pass

    label("Function_16_8923")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("apl/ch51808.itc", 0x1F)
    LoadChrToIndex("apl/ch51813.itc", 0x20)
    SoundLoad(2926)
    SoundLoad(2927)
    SoundLoad(2928)
    SoundLoad(2929)
    SoundLoad(2930)
    SoundLoad(2430)
    SoundLoad(2431)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis325.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis349.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis326.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis327.itp")
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xE, 500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(18500, 2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_8AF0():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8AF0)

    def lambda_8B05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8B05)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10402F#2926V#11P#30W哟，你来啦。\x02",
    )

    CloseMessageWindow()
    OP_24(0xB6E)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00000F#5P嗯……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_8BA1():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8BA1)

    def lambda_8BBB():

        label("loc_8BBB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8BBB")

    QueueWorkItem2(0xE, 2, lambda_8BBB)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xE, 500)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6P听你说了那些故弄玄虚的话，\x01",
            "怎么可能不来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xE,
        (
            "#2927V#30W呵呵，我就喜欢嘴上不情愿，\x01",
            "却总是乖乖应约的你。\x02\x03",
            "#2928V就算说我爱你\x01",
            "也不为过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00006F#6P这种玩笑话就免了。\x02\x03",
            "#00001F……是关于琪雅的事吧？\x01",
            "快告诉我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#11P呵呵，好的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 50000)

    ChrTalk(
        0xE,
        (
            "#10408F#5P其实这些话原本是\x01",
            "不能说给外人听的……\x02\x03",
            "#10400F对于『零之至宝』，\x01",
            "教会已经不准备\x01",
            "继续介入了。\x02\x03",
            "#10403F……无论这次的事件如何收场，\x01",
            "教会也不会进一步干预。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#11P真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5P嗯，『蛇』的人已经撤退，\x01",
            "原版至宝也已经消失，\x01",
            "教会再没有积极介入此事的理由。\x02\x03",
            "#10400F在这种情况下，由我们带走琪雅\x01",
            "这个选项也就可以去除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P是吗……\x01",
            "谢谢你特地告诉我。\x02\x03",
            "#00005F不过，你继续协助我们，\x01",
            "不会有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10403F#5P虽然『小丑』和第七柱都已离去，\x01",
            "但现在还无法确认第六柱是否已经撤退。\x02\x03",
            "#10408F另外，包括那些智能兵器在内，\x01",
            "结社提供给库罗伊斯家族的技术支持\x01",
            "仍然有着很大的影响……\x02\x03",
            "#10400F在这些影响完全消失之前，\x01",
            "我们还会继续保持最低限度的介入行为。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P原来如此……\x02\x03",
            "#00001F……越听越觉得，\x01",
            "似乎有一场超出我们常识范围的\x01",
            "斗争正在不断扩大战火吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5P呵呵，那和你们所处的世界\x01",
            "完全没有交集呢。\x02\x03",
            "#10402F另外……对于我来说，\x01",
            "结束这件长达两年的\x01",
            "潜入克洛斯贝尔任务才是最重要。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#11P说起来……\x01",
            "你今年十七岁。\x02\x03",
            "#00003F也就是说，在两年前接下任务时，\x01",
            "只有十五岁而已……\x02\x03",
            "#00001F但『守护骑士』不是\x01",
            "相当重要的职位吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5P哦，『守护骑士』并不是\x01",
            "根据功绩而任命的。\x02\x03",
            "#10400F只有显现出『刻印』的人才能当上，\x01",
            "一切都是命运注定……\x02\x03",
            "#10409F总之，这方面的事情太过超乎常理，\x01",
            "一般人肯定很难相信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P哪有自己这样说的……\x02\x03",
            "#00001F……话说回来，所谓的『刻印』，\x01",
            "难道就是你在战斗中\x01",
            "偶尔显现出来的那个……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5P没错……\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x190)
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xE, 500, 0, -4250, 180)
    OP_68(430, 1000, -4460, 0)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(40, 20, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15000, 30000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#10403F#5P#30W『圣痕』──\x01",
            "这就是那个『刻印』的名字。\x02\x03",
            "#10408F镌刻于灵魂的刻印……\x01",
            "既是力量的源泉，也是禁忌之物。\x02\x03",
            "#10400F这东西在我身上显现，\x01",
            "大约是在七年前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P七年前……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5P虽然和Ｄ∴Ｇ教团\x01",
            "完全无关……\x02\x03",
            "#10402F不过，就算是消磨时间吧，要不要听一听呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯……\x01",
            "如果不介意，请一定讲给我听听。\x02\x03",
            "#00000F仔细想想，我几乎完全\x01",
            "不了解你的过去……\x02\x03",
            "#00012F虽然已经基本熟悉你的\x01",
            "性格和行动方式了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5P呵呵……好吧。\x02",
    )

    CloseMessageWindow()
    OP_21(0xFA0)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    SetCameraDistance(15000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C……我出生的故乡，\x01",
            "位于塞姆里亚大陆的某个边境地区。\x02\x03",
            "那是一个严禁与外界接触的地方，\x01",
            "也就是所谓的『隐者之村』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, 155, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C在那个村子里，供奉着不同于女神的\x01",
            "『太古之神』……\x02\x03",
            "我从小就担当着倾听\x01",
            "『神之音』的『巫子』。\x02\x03",
            "当然了，那并不是我自愿的，\x01",
            "只是在刚刚懂事的时候，被他们擅自选中的。\x02\x03",
            "我知道『神』的真正身份只是个\x01",
            "出处不明的太古咒具，所以觉得\x01",
            "这一切实在是太愚蠢了。\x02\x03",
            "我一直很希望自己能从这无聊的\x01",
            "职责中解放，获得自由。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C……后来，村子里\x01",
            "开始发生奇怪的事。\x02\x03",
            "村民们一个接一个地\x01",
            "陷入昏睡，原因不明。\x02\x03",
            "经过调查之后，我发现其中的\x01",
            "原因是『神』的力量开始失控，\x01",
            "通过地脉吸取人类的精气……\x02\x03",
            "我主张把『神』封印起来，\x01",
            "可村子里的长老们却不认可这种做法，\x01",
            "甚至还提出要给『神』献上活祭品。\x02\x03",
            "话说回来，那是一件拥有恐怖力量的咒具，\x01",
            "我们原本也不可能将它成功封印……\x02\x03",
            "就在那时，教会的骑士们\x01",
            "从外界抵达了村子。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    SetMessageWindowPos(180, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C与他们接触之后，我得知\x01",
            "所谓的『神』其实是一种古代遗物……\x02\x03",
            "在确信它并不是绝对的存在之后，\x01",
            "我做出了一个大胆的行动。\x02\x03",
            "我想把那个蓝色石板状的『神』\x01",
            "推下悬崖，将它摧毁。\x02\x03",
            "我当时只是希望从太古的\x01",
            "诅咒中解放，从此获得自由。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    SetMessageWindowPos(10, 150, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C但『神』的抵抗十分激烈，\x01",
            "并开始吸取我全部的力量。\x02\x03",
            "骑士们已经来不及救我了，\x01",
            "就在我的生命即将结束的瞬间……\x02\x03",
            "那个『刻印』出现在我的胸前。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(2500, 16777215, -1)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_0D()
    OP_68(-360, 2100, -3950, 0)
    MoveCamera(150, -49, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5667730, 0)
    Sleep(1500)
    FadeToBright(1500, 16777215)
    OP_0D()
    Sleep(800)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C我的『圣痕』反过来\x01",
            "夺去了『神』的所有力量……\x02\x03",
            "『神』变成一块普通的古老石板，\x01",
            "摔得粉碎。\x02\x03",
            "就这样，我获得了自由——\x01",
            "可喜可贺地被村民们赶出了故乡。\x02\x03",
            "作为『杀死』村民们尊崇的\x01",
            "『神』的大罪人。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x1)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 3000)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(150)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_6F(0x79)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W………居然有那种事…………\x02\x03",
            "#00006F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10409F#5P#30W呵呵……\x01",
            "是个相当荒诞无稽的故事吧？\x02\x03",
            "#10400F身为成长在大都市的现代人，\x01",
            "肯定很难相信吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P不，只要目睹过你的力量，\x01",
            "就会明白那是真实存在的往事。\x02\x03",
            "#00000F而且，我毕竟还亲眼看到了蔡特\x01",
            "那种活生生的神话呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10402F#5P哈哈，说的也是。\x02\x03",
            "#10404F就这样，我接受了骑士们的邀请，\x01",
            "前往亚尔特利亚法典国……\x02\x03",
            "成为整个大陆仅有十二名，拥有着『圣痕』的\x01",
            "『守护骑士』之一。\x02\x03",
            "#10400F我和阿巴斯也是\x01",
            "在那个时候认识的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6P是吗……\x02\x03",
            "#00006F……不过，这样一来，\x01",
            "你就再也没有回过故乡了吧？\x02\x03",
            "#00001F也再没和家人见过面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5P#30W嗯……这不是理所当然的吗？\x02\x03",
            "#10403F我粉碎了村民们的\x01",
            "精神信仰。\x02\x03",
            "只是为了能够获得自由……\x01",
            "完全没有考虑到后果。\x02\x03",
            "#10400F所以，这些都是我应得的惩罚。\x02\x03",
            "#10404F包括被家人憎恨在内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5P#30W据我所知，\x01",
            "教会在那之后进驻了村子，\x01",
            "并对村民们多加照顾。\x02\x03",
            "#10404F『神』的诅咒总有一天\x01",
            "也会变成历史。\x02\x03",
            "等到这段往事被遗忘之后，\x01",
            "我会回去看看的。\x02\x03",
            "#10402F所以你不用那么担心我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30W瓦吉……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00008F#6P解决了这次的事件之后……\x01",
            "你就会离开克洛斯贝尔了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10400F#5P嗯，这是我\x01",
            "身为骑士的使命。\x02\x03",
            "#10409F呵呵，怎么了？\x01",
            "你现在就开始感到寂寞了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0xFA0)

    ChrTalk(
        0x101,
        "#00001F#6P嗯，这是理所当然的啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 400)
    Sleep(150)

    ChrTalk(
        0xE,
        "#10405F#11P哎……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    Sleep(500)
    OP_6F(0x79)
    SetCameraDistance(9000, 30000)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30W虽然瓦鲁多变成那种样子，\x01",
            "但一定会恢复原状的。\x02\x03",
            "圣书会的各位也都会\x01",
            "继续生活在克洛斯贝尔。\x02\x03",
            "#00008F虽说你从一开始就另有所图，\x01",
            "但毕竟是我们的同伴……\x02\x03",
            "#00000F所以……\x01",
            "以后随时都可以来玩哦。\x02\x03",
            "#00009F对你来说，克洛斯贝尔\x01",
            "也算是第二故乡了吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(300)

    ChrTalk(
        0xE,
        "#10405F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    def lambda_A547():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A547)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10404F#2430V#5P#40W#12A……呵呵…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetChrSubChip(0xE, 0x3)

    def lambda_A5A5():
        OP_A6(0xFE, 0x0, 0x1E, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A5A5)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#10409F#2431V#50W#5P#4S#15A啊哈哈哈哈哈哈哈哈！\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W我也知道这番话显得很傻。\x02\x03",
            "#00000F但我可是百分之百发自内心的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10411F#5P#40W……呵呵，我明白。\x01",
            "在你面前，总会让我变得有点不对劲呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    OP_A0(0xE, 1000, 0x7, 0x5)
    OP_0D()
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10402F#2929V#5P#40W……我以后要是犯了思乡病，\x01",
            "一定会毫不客气地回来找你们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB71)
    Sleep(150)
    OP_A0(0xE, 1000, 0x5, 0x7)
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10404F#2930V#5P#40W这并不是为了替代无法返回的故乡，\x01",
            "而是为了确认和你们结下的这份孽缘哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB72)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x1770, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-360, 2100, -3950, 8000)
    MoveCamera(128, 27, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(40590, 8000)
    Sleep(500)
    OP_A0(0xE, 1000, 0x7, 0x5)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    OP_21(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_A82B")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_A82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A841")
    Jump("loc_A8D7")

    label("loc_A841")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "罗伊德和瓦吉习得\x01",
            "袭空天堂Ⅱ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和瓦吉的组合战技\x01",
            "『袭空天堂』得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)

    label("loc_A8D7")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x26, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 5)
    OP_29(0xB1, 0x1, 0x5)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)

    CancelBlur(0)
    ClearScenarioFlags(0x1AA, 7)
    SetScenarioFlags(0x22, 0)
    NewScene("e440c", 0, 0, 0)
    IdleLoop()

    Return()

    # Function_16_8923 end

    def Function_17_A8FA(): pass

    label("Function_17_A8FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x40)
    LoadChrToIndex("chr/ch03200.itc", 0x1E)
    LoadChrToIndex("apl/ch51809.itc", 0x1F)
    LoadChrToIndex("apl/ch51810.itc", 0x20)
    SoundLoad(3265)
    SoundLoad(3266)
    SoundLoad(3267)
    SoundLoad(3268)
    SoundLoad(3269)
    SoundLoad(3270)
    SoundLoad(2634)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10701.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis321.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis322.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis323.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis324.itp")
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -250, 120, 2750, 180)
    SetChrPos(0x8, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(125, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8000, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(115, 15, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00002F#6P#30W#N……好漂亮的满月。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()

    def lambda_AB30():

        label("loc_AB30")

        TurnDirection(0xFE, 0x101, 400)
        Yield()
        Jump("loc_AB30")

    QueueWorkItem2(0x8, 2, lambda_AB30)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#3265V#11P#40W罗伊德警官……\x02",
    )

    CloseMessageWindow()
    OP_24(0xCC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4200, 4500)
    MoveCamera(130, 20, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(10000, 4500)
    Sound(100, 0, 100, 0)

    def lambda_AC24():
        OP_95(0xFE, -500, 0, -3750, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AC24)
    WaitChrThread(0x101, 1)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    SetCameraDistance(9500, 30000)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W每次和你聊天的时候，\x01",
            "月色好像都特别美呢。\x02\x03",
            "#00002F不愧是『月之舞姬』的\x01",
            "饰演者啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10709F#2634V#5P#30W呵呵……\x02",
    )

    CloseMessageWindow()
    OP_24(0xA4A)
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10704F#3266V#40W#5P如果把太阳比喻为光，月亮便是影……\x02\x03",
            "#3267V我和月亮的确\x01",
            "有些相似之处。\x02\x03",
            "#10708F#3268V我们都是原本不会出现在\x01",
            "阳光之下的……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCC4)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W但你却在克洛斯贝尔\x01",
            "抓住了光芒……\x02\x03",
            "#00001F这是无可置疑的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A1(0x8, 0x3E8, 0x5, 0x2, 0x25, 0x26, 0x25, 0x2)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W是的，我已经不想再\x01",
            "否定这一事实了。\x02\x03",
            "#10708F可是……\x01",
            "……我毕竟走在一条\x01",
            "无比深暗的道路上。\x02\x03",
            "#10711F那就是名为『银』的一子相传式道路……\x02\x03",
            "#10703F也是继承自父亲的隐秘之路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P#30W你之前也说过这些呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W……如果方便，\x01",
            "可以给我讲一讲吗？\x02\x03",
            "#00008F讲讲来到克洛斯贝尔之前的你。\x02\x03",
            "#00001F我所不知道的莉夏·毛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W……好的。\x02\x03",
            "#10710F我早就隐隐觉得，\x01",
            "总有一天会把这些事情\x01",
            "讲给你听了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_21(0x1770)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    OP_93(0x8, 0xB4, 0x12C)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    OP_63(0x8, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10708F#5P#30W从刚懂事的时候开始，\x01",
            "我就一直和父亲生活在一起。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(9000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C……关于母亲的记忆，则完全没有。\x02\x03",
            "大概是为了让我\x01",
            "继承『银』的道路，\x01",
            "父亲刻意疏远了她。\x02\x03",
            "但对我来说，那就是正常的生活……\x02\x03",
            "严酷的锻炼，以及暗器和符术的修炼，\x01",
            "我都淡然承受了下来。\x02\x03",
            "辗转于各地的同时，我也会去主日学校上课，\x01",
            "学习与人相处的方法。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C父亲既不严厉也不温柔，\x01",
            "只是不断地教导我。\x02\x03",
            "因为『银』需要继承的东西\x01",
            "实在太多。\x02\x03",
            "代代传承的『银』的记忆……\x02\x03",
            "在什么样的情况下做什么样的工作……\x01",
            "面对各种目标时应该选用的处理方式……\x02\x03",
            "为了能够在任何时代始终如一，\x01",
            "继承者必须把这一切\x01",
            "都基本继承下来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C当把这一切都继承下来之后……\x01",
            "我就会成为『银』。\x02\x03",
            "话虽如此，但只要父亲还活着，\x01",
            "我就不会成为『银』。\x02\x03",
            "因为『银』只有一个，\x01",
            "这一点是不会变的。\x02\x03",
            "在那段时间里，我在等待父亲\x01",
            "归来的同时，过着安稳的生活。\x02\x03",
            "为了让我随时都能继承『银』这个身份，\x01",
            "父亲每次回来之后，\x01",
            "都会将工作的概要告知给我……\x02\x03",
            "虽然我当时已经有了用于对外示人的另一重身份，\x01",
            "但对我来说，那就是整个世界的全部了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(20, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C……那个世界之所以会崩溃，\x01",
            "是由于父亲因不治之症而病倒。\x02\x03",
            "我的父亲在历代『银』之中，\x01",
            "也是拥有卓越能力的一位……\x01",
            "但他也同样无法逃过病魔的侵袭。\x02\x03",
            "他很干脆地放弃了抗争，\x01",
            "也没有接受可以延续生命的手术……\x02\x03",
            "某一天，他把我叫去，并下达了命令——\x02\x03",
            "让我杀死他，继承『银』这个身份。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C……我没能做到。\x02\x03",
            "不知为何，\x01",
            "从来没有忤逆过父亲的我，\x01",
            "唯独做不到这件事。\x02\x03",
            "……我第一次感到恐惧。\x02\x03",
            "父亲费尽心力培养出来的『银』，\x01",
            "会不会只是个不中用的废物？\x02\x03",
            "濒临死亡的父亲是不是感到很失望？\x02\x03",
            "……父亲苦笑着，对当时\x01",
            "懊恼不已的我如此说道——\x02\x03",
            "『……那也是你啊。』\x02\x03",
            "『你的银就由你自己来决定吧！』\x02\x03",
            "……一个月后，父亲去世了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C而我也正式成为『银』。\x02\x03",
            "继承了父亲的关系网，\x01",
            "并利用黑衣和内功改变自己的体型……\x02\x03",
            "虽然能力远远比不上父亲，\x01",
            "但还是可以立刻继承工作。\x02\x03",
            "『你的银就由你自己来决定吧！』\x02\x03",
            "我并未理解父亲当时的话，\x01",
            "只是淡漠地随波逐流……\x02\x03",
            "……两年后，\x01",
            "我和黑月签署了长期契约。\x02\x03",
            "契约内容是协助黑月夺取位于\x01",
            "卡尔瓦德共和国西侧的贸易都市——\x01",
            "克洛斯贝尔的掌控权。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(1000)
    SetMessageWindowPos(250, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C抵达克洛斯贝尔之后，\x01",
            "我为了备战而调查城市环境的时候，\x01",
            "走进了位于欢乐街的某个剧场。\x02\x03",
            "那里正好在进行一场\x01",
            "公开练习……\x02\x03",
            "……之后的事情，\x01",
            "你就都知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 40000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W……原来如此……\x02\x03",
            "#00000F你就是在那个时候\x01",
            "被伊莉娅小姐看中的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10702F#5P#30W呵呵，我当时找了很多理由来推脱，\x01",
            "拒绝加入剧团。\x02\x03",
            "#10704F但伊莉娅小姐实在是太强势了……\x02\x03",
            "最终只能放弃挣扎，\x01",
            "乖乖加入。\x02\x03",
            "我对自己的体力和伪装很有自信，\x01",
            "所以觉得那里会是个不错的藏身之处。\x02\x03",
            "#10710F……不过，练习比想象中艰辛很多，\x01",
            "同时兼顾『银』这个身份，真是十分辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P#30W哈哈……\x02\x03",
            "#00004F谢谢你，莉夏。\x02\x03",
            "#00000F你愿意把这些往事告诉我，我真的很开心。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W呵呵，虽然不算是什么\x01",
            "有趣的故事……\x02\x03",
            "#10703F但这就是……\x01",
            "我继承自父亲与祖先的『道路』。\x02\x03",
            "#10708F即使抓住了那道名为\x01",
            "彩虹剧团的光芒……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A0(0x8, 1000, 0x2, 0x5)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W我恐怕也无法完全舍弃\x01",
            "这条『道路』……\x02",
        )
    )

    CloseMessageWindow()
    OP_21(0x1388)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30W是吗……\x02\x03",
            "#00008F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(1000)
    SetChrSubChip(0x8, 0x6)
    SetChrPos(0x101, -1000, 0, -4250, 90)
    SetChrPos(0x8, 0, 0, -4250, 270)
    OP_68(-300, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(-300, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003F#6P#30W『你的银就由你自己来决定吧！』\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x3E8, 0x5, 0x6, 0x29, 0x2A, 0x29, 0x6)

    ChrTalk(
        0x8,
        "#10712F#11P#30W…………哎……………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……『银』会继承一切。\x02\x03",
            "既然你已经抓住了\x01",
            "名为彩虹剧团的光芒……\x02\x03",
            "#00002F『银』也就只能接受\x01",
            "这光芒的一面了，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#30W这、这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W任何事物都会随着\x01",
            "时代潮流的发展而做出改变……\x02\x03",
            "#00003F不，是必须要做出改变。\x02\x03",
            "#00008F正因如此，人类的历史才能不断传承，\x01",
            "并向前迈进……\x02\x03",
            "#00001F你父亲的话语里，\x01",
            "恐怕也包含了这一层意思吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10708F#11P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W作为一名警察，我当然不能\x01",
            "鼓励你从事犯罪行为……\x02\x03",
            "但既使如此，我还是觉得，你只要将\x01",
            "『自己的银』作为目标就可以了。\x02\x03",
            "#00000F就算在此与『银』的过去一刀两断，\x01",
            "也同样是一条可行之路。\x02\x03",
            "#00002F我觉得……就算你那样做，\x01",
            "你的父亲肯定也不会介意的。\x02\x03",
            "#00009F他一定会苦笑着说『……那也是你啊』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#40W#2S…………啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……你有一个好父亲呢。\x02\x03",
            "#00008F虽然和普通家庭的父亲有些不同，\x01",
            "但他同样深爱着自己的女儿……\x02\x03",
            "#00002F至少我是这样觉得的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10718F#11P#50W………爸……爸…………\x02",
    )

    CloseMessageWindow()
    OP_68(-100, 1000, -4250, 1200)
    SetChrFlags(0x8, 0x20)

    def lambda_C235():
        OP_A0(0xFE, 1000, 0x6, 0x9)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_C235)
    OP_96(0x8, 0x96, 0x0, 0xFFFFEF66, 0x1F4, 0x0)
    Sound(812, 0, 60, 0)
    ClearChrFlags(0x8, 0x20)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A1(0x8, 0x3E8, 0x6, 0x1A, 0x1E, 0x1F, 0x20, 0x21, 0x22)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_63(0x8, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(812, 0, 60, 0)
    OP_A0(0x8, 1000, 0xA, 0xC)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10719F#11P#50W为……什么……\x02\x03",
            "……即使是在爸爸去世的时候……\x01",
            "我也……\x02\x03",
            "#10720F………完全没有……\x01",
            "流过泪啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W大概是和伊莉娅小姐他们\x01",
            "共同度过的这段日子改变了你……\x02\x03",
            "#00008F虽然我不知道你今后会\x01",
            "走上什么样的道路……\x02\x03",
            "#00000F但如果可以，\x01",
            "我想代替你的父亲守望你。\x02\x03",
            "#00002F看看这个已经抓住光芒的你，\x01",
            "究竟会有怎样的改变。\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x8, 1000, 0xC, 0xF)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10718F#11P#50W……罗伊德警官……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    OP_68(100, 1000, -4250, 1200)
    SetCameraDistance(15000, 1200)
    OP_9A(0x101, 0x8, 0x1F4, 0x258, 0x0)
    Sleep(300)
    Fade(250)
    Sound(898, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_C48D():
        OP_A0(0xFE, 1000, 0x14, 0x16)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_C48D)

    def lambda_C49A():
        OP_A0(0xFE, 1000, 0x5, 0x7)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C49A)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    OP_0D()
    MoveCamera(44, 23, 0, 15000)
    SetCameraDistance(70000, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10720F#11P#3269V#70W#20A……呜呜……啊啊………\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#10713F#11P#3270V#90W#30A#4S…………啊啊啊啊啊…………！\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    OP_21(0x1770)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_C592")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_C592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5A4")
    Jump("loc_C640")

    label("loc_C5A4")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x2),
            "罗伊德和莉夏习得\x01",
            "真·比翼双龙击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x7, 0x5),
            "罗伊德和莉夏的组合战技\x01",
            "『比翼双龙击』得到了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)

    label("loc_C640")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x27, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 6)
    OP_29(0xB1, 0x1, 0x6)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)

    SetScenarioFlags(0x1AA, 3)
    SetScenarioFlags(0x1AA, 4)
    SetScenarioFlags(0x1AA, 5)
    SetScenarioFlags(0x1AA, 6)
    SetScenarioFlags(0x1AA, 7)
    SetScenarioFlags(0x1AB, 0)

    CancelBlur(0)

    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_A8FA end

    def Function_18_C663(): pass

    label("Function_18_C663")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C67D")
    OP_A0(0xFE, 1000, 0x10, 0x12)
    Sleep(300)
    Jump("Function_18_C663")

    label("loc_C67D")

    Return()

    # Function_18_C663 end

    SaveToFile()

Try(main)
