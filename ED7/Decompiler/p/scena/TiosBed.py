from ScenarioHelper import *

class CharInfo:
    def __init__(self, id, name, SetChipHandler = None):
        self.Name = name
        self.Id = id
        self.SetChipHandler = SetChipHandler

StaticCharList = \
(
    CharInfo(0x00, '罗伊德'),
    CharInfo(0x01, '艾莉'),
    CharInfo(0x02, '缇欧'),
    CharInfo(0x03, '兰迪'),
    CharInfo(0x04, '瓦吉'),
    CharInfo(0x05, '银'),
    CharInfo(0x06, '神狼蔡特'),
    CharInfo(0x07, '亚里欧斯'),
    CharInfo(0x08, '诺艾尔上士'),
    CharInfo(0x09, '达德利搜查官'),
    CharInfo(0x0A, '加尔西亚'),
)


ORIGINAL_ARIANRHOD_ID   = 0xEF

def SetArianrhodChip(SourceChrId, TargetChrInfo):
    not_clear   = GenerateUniqueLable()
    set_end     = GenerateUniqueLable()

    IfScenaFlagOn(SCENA_FLAGS_OFFSET_1, SCENA_FLAGS_BIT_ARIANRHOD, not_clear)

    SetChrChipPat(SourceChrId, 1, TargetChrInfo.Id)
    Jump(set_end)

    label(not_clear)

    SetChrChipPat(SourceChrId, 1, ORIGINAL_ARIANRHOD_ID)

    label(set_end)


StaticGodList = \
(
    CharInfo(0xB0, '阿瑞安赫德',     SetArianrhodChip),
    CharInfo(0xB1, '小丑肯帕雷拉'),
    CharInfo(0xF0, '钢盔肾斗士'),

    CharInfo(0xC0, '血腥谢莉'),
    CharInfo(0xC1, '战鬼西格蒙德'),
    CharInfo(0xC2, '玛丽亚贝尔'),
    CharInfo(0xC3, '亚里欧斯长官'),
    CharInfo(0xC4, '风之剑圣亚里欧斯'),
    CharInfo(0xC5, '『神速』杜巴莉'),
    CharInfo(0xC6, '『刚毅』艾奈丝'),
    CharInfo(0xC7, '『魔弓』恩奈雅'),
    CharInfo(0xC8, '游击士艾欧莉娅'),
    CharInfo(0xC9, '游击士林'),

    CharInfo(0xD0, '碧之虚神'),
    CharInfo(0xD1, '神机TYPE-α'),

    CharInfo(None, '无'),
)

StaticCharMap = {}
StaticGodMap = {}

for char in StaticCharList:
    StaticCharMap[char.Id] = char.Name
    StaticCharMap[char.Name] = char.Id

for char in StaticGodList:
    StaticGodMap[char.Id] = char.Name
    StaticGodMap[char.Name] = char.Id


def ShowGodListMenuWorker(SourceChrId, GodList, IsSubMenu = False):

    menu_end_label = GenerateUniqueLable()
    menu_return_label = GenerateUniqueLable()

    if StaticCharMap[SourceChrId] == '银':

        yin_not_change_to_rixia = GenerateUniqueLable()
        yin_or_rixia_end        = GenerateUniqueLable()

        Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), yin_not_change_to_rixia)
        MenuCmd(0x1, 0x0, '莉夏')
        MenuTitle(10, 0, 0x0, "要把 莉夏 替换成")
        Jump(yin_or_rixia_end)

        label(yin_not_change_to_rixia)
        MenuTitle(10, 0, 0x0, "要把 %s 替换成" % StaticCharMap[SourceChrId])

        label(yin_or_rixia_end)

    else:
        MenuTitle(10, 0, 0x0, "要把 %s 替换成" % StaticCharMap[SourceChrId])

    if False:
        CharList = []
        for char in GodList:
            CharList.append(char.Name + '\x01')
        CharList.append('放弃\x01')

        Menu(1, 14, 80, 1, CharList)
        MenuCmd(0x4, 0x0, 0x0)
        MenuEnd(0x0)
        MenuCmd(0x4, 0x0, 0x0)
    else:
        CharList = []
        for char in GodList:
            CharList.append(char.Name)
        CharList.append('放弃')

        CreateMenuAndShow(CharList, 1, 15, 45)

    CaseList = []
    for i in range(len(GodList)):
        CaseList.append( (i, GenerateUniqueLable()) )

    CaseList.append((SWITCH_DEFAULT, GenerateUniqueLable()))

    Switch((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), *CaseList)

    for i in range(len(CaseList)):
        caseid, caselabel = CaseList[i]
        label(caselabel)

        if caseid == SWITCH_DEFAULT:
            if IsSubMenu:
                RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_END)))

            Jump(menu_return_label)
            continue

        if GodList[i].SetChipHandler == None:
            if GodList[i].Id is None:
                if StaticCharMap[SourceChrId] == '银':

                    yin_not_change_to_rixia = GenerateUniqueLable()
                    yin_or_rixia_end        = GenerateUniqueLable()

                    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), yin_not_change_to_rixia)
                    SetChrChipPat(SourceChrId, 1, 0x35C)

                    Jump(yin_or_rixia_end)

                    label(yin_not_change_to_rixia)
                    SetChrChipPat(SourceChrId, 1, SourceChrId + 0x350)

                    label(yin_or_rixia_end)

                elif StaticCharMap[SourceChrId] == '瓦吉':

                    lazy_not_change_to_knight = GenerateUniqueLable()
                    lazy_or_knight_end        = GenerateUniqueLable()

                    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), lazy_not_change_to_knight)
                    SetChrChipPat(SourceChrId, 1, 0x35B)

                    Jump(lazy_or_knight_end)

                    label(lazy_not_change_to_knight)
                    SetChrChipPat(SourceChrId, 1, SourceChrId + 0x350)

                    label(lazy_or_knight_end)

                else:
                    SetChrChipPat(SourceChrId, 1, SourceChrId + 0x350)
            else:
                SetChrChipPat(SourceChrId, 1, GodList[i].Id)
        else:
            GodList[i].SetChipHandler(SourceChrId, GodList[i])

        Jump(menu_end_label)

    label(menu_end_label)
    LoadChrChipPat()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_END)))


    label(menu_return_label)

    OP_60(1)


MAXIMUM_MENU_ITEM = 33 - 1

def ShowGodListMenuWithSubMenu(SourceChrId, GodList):

    ChrIdRange = []
    for i in range(0, len(GodList), MAXIMUM_MENU_ITEM):
        sublist = GodList[i:i + MAXIMUM_MENU_ITEM]
        ChrIdRange.append('%02X - %02X\x01' % (sublist[0].Id, sublist[-1].Id))
    ChrIdRange.append('放弃\x01')

    SubMenuCaseList = []
    for i in range(len(ChrIdRange) - 1):
        SubMenuCaseList.append((i, GenerateUniqueLable()))

    SubMenuCaseList.append((SWITCH_DEFAULT, GenerateUniqueLable()))


    menu_end_label      = GenerateUniqueLable()
    menu_return_label   = GenerateUniqueLable()
    continue_show_menu  = GenerateUniqueLable()
    show_menu           = GenerateUniqueLable()

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))


    label(show_menu)

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), menu_return_label)


    MenuTitle(10, 0, 0x0, "人物 ID 范围")
    Menu(1, 14, 70, 1, ChrIdRange)
    MenuCmd(0x4, 0x0, 0x0)
    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    Switch((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), *SubMenuCaseList)

    for i in range(len(SubMenuCaseList)):
        caseid, caselabel = SubMenuCaseList[i]
        label(caselabel)

        if caseid == SWITCH_DEFAULT:
            Jump(menu_return_label)
            continue

        StartId = i * MAXIMUM_MENU_ITEM
        ShowGodListMenuWorker(SourceChrId, GodList[StartId : StartId + MAXIMUM_MENU_ITEM], True)

        Jump(show_menu)
        #Jump(menu_end_label)

    label(menu_end_label)


    label(menu_return_label)

    OP_60(1)


def ShowGodListMenu(SourceChrId):

    if len(StaticGodList) > MAXIMUM_MENU_ITEM:
        ShowGodListMenuWithSubMenu(SourceChrId, list(StaticGodList))
        RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))
        return

    return ShowGodListMenuWorker(SourceChrId, list(StaticGodList))

def ShowChangeMemberMenu():

    menu_end_label = GenerateUniqueLable()
    show_menu_label = GenerateUniqueLable()

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))

    label(show_menu_label)

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), menu_end_label)


    MenuTitle(25, 0, 0x0, "要替换谁")

    if False:
        CharList = []
        for char in StaticCharList:
            CharList.append(char.Name + '\x01')
        CharList.append('放弃\x01')

        Menu(1, 15, 70, 1, CharList)
        MenuCmd(0x4, 0x0, 0x0)

    else:
        MenuCmd(0, 1)
        for chr in StaticCharList:
            chr = chr.Name
            if chr == '银':

                yin_not_change_to_rixia = GenerateUniqueLable()
                yin_or_rixia_end        = GenerateUniqueLable()

                Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), yin_not_change_to_rixia)
                MenuCmd(1, 1, '莉夏')
                Jump(yin_or_rixia_end)

                label(yin_not_change_to_rixia)
                MenuCmd(1, 1, chr)

                label(yin_or_rixia_end)

            else:
                MenuCmd(1, 1, chr)

        MenuCmd(0x2, 1, 15, 45, 0x1)

    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    CaseList = []
    for i in range(len(StaticCharList)):
        CaseList.append( (i, GenerateUniqueLable()) )

    CaseList.append((SWITCH_DEFAULT, GenerateUniqueLable()))

    Switch((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), *CaseList)

    for i in range(len(CaseList)):
        caseid, caselabel = CaseList[i]
        label(caselabel)

        if caseid == SWITCH_DEFAULT:
            RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_END)))
            Jump(show_menu_label)
            continue

        RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_END)))
        ShowGodListMenu(StaticCharList[i].Id)

        Jump(show_menu_label)

    label(menu_end_label)

    OP_60(1)

def ReleaseAllGod():
    for i in range(len(StaticCharList)):
        SetChrChipPat(StaticCharList[i].Id, 1, StaticCharList[i].Id)

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "no_yin_to_rixia")
    SetChrChipPat(StaticCharMap['银'], 1, 0x20)
    label("no_yin_to_rixia")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "no_Lazy_Knight")
    SetChrChipPat(StaticCharMap['瓦吉'], 1, 0x1F)
    label("no_Lazy_Knight")

def ShowMenu():
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)))

    label('bed_show_cg_menu')

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "menu_return")

    if 0:
        SetScenarioFlags(SCENA_FLAGS_OFFSET_1, SCENA_FLAGS_BIT_ARIANRHOD)
        SetScenarioFlags(0x20, 2)

    IfScenaFlagOff(SCENA_FLAGS_OFFSET_1, SCENA_FLAGS_BIT_ARIANRHOD, 'hagane_already_clear')

    AnonymousTalk(
        999,
        (
            scpstr(7, 5),
            "\x01你还没有领悟宇宙的真理。\x07\x00\x02",
        )
    )

    label('hagane_already_clear')


    MenuTitle(-1, 5, 0x0, "星辰之间")

    Menu(
        0,
        0xFFFF,
        0xFFFF,
        0x1,
        (
            "原地复活\x01",                  # 0
            "换人\x01",                      # 1
            "全部还原\x01",                  # 2
            "挑战钢之圣女\x01",              # 3
            "进入Debug地图\x01",             # 4
            #"进入星辰之间\x01",              # 5
            "放弃\x01",                      # 6
        )
    )

    MenuCmd(0x4, 0x0, 0x0)
    MenuEnd(0x0)
    MenuCmd(0x4, 0x0, 0x0)

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "rest_here"),
        (1, "change_member"),
        (2, "restore_all"),
        (3, "challenge_hagane"),
        (4, "enter_debug_map"),
        #(5, "enter_celestial_globe"),
        (-1, "close_menu"),
    )

    label("rest_here")
    OP_32(0xFF, 0xFF, 0)

    #ShowSaveClearMenu()
    #OP_C5(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    #ShowSaveMenu()

    Jump('continue_show_menu')


    label('restore_all')
    ReleaseAllGod()
    Jump('continue_show_menu')


    label('define_hagane_battle_info')

    ATBonus("Hagane_ATBonus", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    MonsterBattlePostion("Hagane_MonsterBattlePostion", 8, 12, 180)

    BattleInfo(
        "Hagane_BattleInfo", 0x0052, 255, 6, 45, 3, 3, 30, 0, "bm1070", 0, 100, 0, 0, 0,
        (
            ("ms90011.dat", 0, 0, 0, 0, 0, 0, 0, "Hagane_MonsterBattlePostion", "Hagane_MonsterBattlePostion", "ed7544.ogg", "ed7544.ogg", "Hagane_ATBonus"),
            (),
            (),
            (),
        )
    )

    label('challenge_hagane')

    Battle("Hagane_BattleInfo", 0x0, 0x0, 0x100, 0x40, 0xFF)


    IfScenaFlagOff(SCENA_FLAGS_OFFSET_1, SCENA_FLAGS_BIT_ARIANRHOD, 'hagane_already_beat')

    IfLastBattleLostGoto('challenge_hagane_failed')
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

    label('hagane_already_beat')
    label('challenge_hagane_failed')

    Jump('continue_show_menu')


    label('enter_debug_map')
    NewScene('a0000', 0, 0, 0)
    OP_07()
    Jump('close_menu')


    label('change_member')

    ShowChangeMemberMenu()
    Jump('continue_show_menu')


    label('enter_celestial_globe')
    NewScene('e9990', 0, 0, 0)


    label('close_menu')
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_END)))
    Jump('bed_show_cg_menu')


    label('continue_show_menu')
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0), scpexpr(EXPR_END)))
    Jump('bed_show_cg_menu')


    label('menu_return')

    OP_60(0x0)
    OP_57(0x0)
    OP_DD()
    #ClearMapFlags(0x80)
    OP_54(0xFF)
