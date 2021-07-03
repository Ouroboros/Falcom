from ActionHelper import *

def main():
    CreateArtsAction("as90000.dat")

    CraftAction((
        "移动",                             # 00 0
        "移动",                             # 01 1
        "移动",                             # 02 2
        "移动",                             # 03 3
        "移动",                             # 04 4
        "移动",                             # 05 5
        "移动",                             # 06 6
        "移动",                             # 07 7
        "移动",                             # 08 8
        "移动",                             # 09 9
        "石之芒",                           # 0A 10
        "地震波",                           # 0B 11
        "石化之息",                         # 0C 12
        "大地之矛",                         # 0D 13
        "世界之树",                         # 0E 14
        "巨神狂怒震",                       # 0F 15
        "Craft_10_16_BE5",                  # 10 16
        "Craft_11_17_D69",                  # 11 17
        "防壁之符文",                       # 12 18
        "防壁之符文",                       # 13 19
        "冰之刃",                           # 14 20
        "冰蓝之泪",                         # 15 21
        "冰之锤",                           # 16 22
        "水流轰击",                         # 17 23
        "钻石星尘",                         # 18 24
        "大海啸",                           # 19 25
        "灭世冥寒灾",                       # 1A 26
        "Craft_1B_27_1832",                 # 1B 27
        "慈爱之符文",                       # 1C 28
        "慈爱之符文",                       # 1D 29
        "火之矢",                           # 1E 30
        "灼热之波",                         # 1F 31
        "熔岩之息",                         # 20 32
        "炎蝶之舞",                         # 21 33
        "赤红射线",                         # 22 34
        "龙皇炼狱火",                       # 23 35
        "Craft_24_36_2131",                 # 24 36
        "Craft_25_37_2132",                 # 25 37
        "胜利之符文",                       # 26 38
        "胜利之符文",                       # 27 39
        "雷电击",                           # 28 40
        "风之镰",                           # 29 41
        "风之领域",                         # 2A 42
        "闪电之力",                         # 2B 43
        "雷光龙卷",                         # 2C 44
        "终焉三重奏",                       # 2D 45
        "Craft_2E_46_29DE",                 # 2E 46
        "Craft_2F_47_29DF",                 # 2F 47
        "暴风之符文",                       # 30 48
        "暴风之符文",                       # 31 49
        "心灵之霞",                         # 32 50
        "死亡螺旋",                         # 33 51
        "暗影裁决",                         # 34 52
        "灾厄镰刃",                         # 35 53
        "堕天使暗翼",                       # 36 54
        "Craft_37_55_3063",                 # 37 55
        "Craft_38_56_3064",                 # 38 56
        "Craft_39_57_3065",                 # 39 57
        "刹那之符文",                       # 3A 58
        "刹那之符文",                       # 3B 59
        "暗物质",                           # 3C 60
        "光子飞射",                         # 3D 61
        "大灾变",                           # 3E 62
        "金耀辉环",                         # 3F 63
        "天劫轮回光",                       # 40 64
        "Craft_41_65_3AF5",                 # 41 65
        "Craft_42_66_3AF6",                 # 42 66
        "Craft_43_67_3AF7",                 # 43 67
        "震天之符文",                       # 44 68
        "震天之符文",                       # 45 69
        "混沌烙印",                         # 46 70
        "幻影之塔",                         # 47 71
        "天国之门",                         # 48 72
        "银色荆刺",                         # 49 73
        "幻银方舟炮",                       # 4A 74
        "Craft_4B_75_4774",                 # 4B 75
        "Craft_4C_76_4775",                 # 4C 76
        "Craft_4D_77_4776",                 # 4D 77
        "幻影之符文",                       # 4E 78
        "幻影之符文",                       # 4F 79
        "大地治愈",                         # 50 80
        "结晶防护",                         # 51 81
        "结晶防护·复",                     # 52 82
        "坚韧守护",                         # 53 83
        "Craft_54_84_499B",                 # 54 84
        "Craft_55_85_499C",                 # 55 85
        "Craft_56_86_499D",                 # 56 86
        "Craft_57_87_499E",                 # 57 87
        "强音之力",                         # 58 88
        "强音之力·复",                     # 59 89
        "振奋之激",                         # 5A 90
        "Craft_5B_91_4B0C",                 # 5B 91
        "Craft_5C_92_4B0D",                 # 5C 92
        "Craft_5D_93_4B0E",                 # 5D 93
        "Craft_5E_94_4B0F",                 # 5E 94
        "Craft_5F_95_4B10",                 # 5F 95
        "生命之息",                         # 60 96
        "圣灵之息",                         # 61 97
        "风之精灵",                         # 62 98
        "大治愈术",                         # 63 99
        "精灵之歌",                         # 64 100
        "Craft_65_101_4FBD",                # 65 101
        "Craft_66_102_4FBE",                # 66 102
        "Craft_67_103_4FBF",                # 67 103
        "时间减速",                         # 68 104
        "时间驱动",                         # 69 105
        "灾厄之爪",                         # 6A 106
        "Craft_6B_107_51E1",                # 6B 107
        "Craft_6C_108_51E2",                # 6C 108
        "Craft_6D_109_51E3",                # 6D 109
        "Craft_6E_110_51E4",                # 6E 110
        "Craft_6F_111_51E5",                # 6F 111
        "魔导祝福",                         # 70 112
        "A-反射屏障",                       # 71 113
        "圣灵苏生",                         # 72 114
        "纯净弧光",                         # 73 115
        "Craft_74_116_5520",                # 74 116
        "Craft_75_117_5521",                # 75 117
        "Craft_76_118_5522",                # 76 118
        "Craft_77_119_5523",                # 77 119
        "神圣祝福",                         # 78 120
        "虚空幻域",                         # 79 121
        "狂乱之月",                         # 7A 122
        "星之守护",                         # 7B 123
        "情报解析",                         # 7C 124
        "Craft_7D_125_58A0",                # 7D 125
        "Craft_7E_126_58A1",                # 7E 126
        "Craft_7F_127_58A2",                # 7F 127
        "回复术",                           # 80 128
        "中回复术",                         # 81 129
        "大回复术",                         # 82 130
        "水之幻影",                         # 83 131
        "封魔领域",                         # 84 132
        "中复苏术",                         # 85 133
        "复苏术",                           # 86 134
        "全回复术",                         # 87 135
        "Craft_88_136_5CC0",                # 88 136
        "Craft_88_136_5CC0",                # 89 137
        "Craft_88_136_5CC0",                # 8A 138
        "Craft_88_136_5CC0",                # 8B 139
    ))

    def Craft_移动(): pass

    label("移动")

    Return()

    # 移动 end

    def Craft_石之芒(): pass

    label("石之芒")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg010_00.eff")
    AS_78(0)
    Sleep(125)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(750)
    Yield()
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    AS_14(0x0)
    Call("loc_1D5")
    Return()

    label("loc_1D5")

    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    FreeEffect(0x3)
    FreeEffect(0x4)
    FreeEffect(0x5)
    FreeEffect(0x6)
    FreeEffect(0x7)
    CallReturn()

    # 石之芒 end

    def Craft_地震波(): pass

    label("地震波")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg011_00.eff")
    LoadEffect(0x1, "battle\\mg010_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 0, 0, 500)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1000)
    Yield()
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(600)
    Yield()
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(500)
    Yield()
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(500)
    Yield()
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(500)
    Yield()
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(250)
    Yield()
    EndChrThread(0xFF, 3)
    ResetTarget()

    label("loc_2E5")

    ForeachTarget("loc_30E")
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("loc_2E5")

    label("loc_37")

    ResetTarget()

    label("loc_38")

    ForeachTarget("loc_47")
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_38")

    label("loc_47")

    Return()

    label("loc_30E")

    Call("loc_2")
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    label("loc_2")

    ResetTarget()

    label("loc_3")

    ForeachTarget("loc_14")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_3")

    label("loc_14")

    CallReturn()

    # 地震波 end

    def Craft_石化之息(): pass

    label("石化之息")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg012_00.eff")
    LoadEffect(0x1, "battle\\mg012_01.eff")
    AS_78(0)
    Sleep(300)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    AS_3D(100, 100, 100, 200)
    Sleep(1200)
    Yield()
    LockCamera(0xFE, 0, 800, 0, 2000)
    AS_B0(0x1E, 0x7D0)
    Sleep(2400)
    Yield()
    AS_31(0x17, 0x1F4)
    Sleep(600)
    Yield()

    label("loc_3AE")

    ForeachTarget("loc_3D3")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    NextTarget()
    Jump("loc_3AE")

    label("loc_3D3")

    Call("loc_2")
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 石化之息 end

    def Craft_大地之矛(): pass

    label("大地之矛")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg013_00.eff")
    AS_78(0)
    Sleep(300)
    Yield()
    SetBrightness(0x0, 0x0, 300)
    Fade(0x1, 500, 0x0)
    AS_60(0xF7)
    AS_5F(0xFC, 0x0)
    AS_5F(0xFF, 0x0)
    AS_31(0x11, 0x0)
    AS_3A(0xFF92, 0x0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(300, 28, 20)
    AS_B0(0x14, 0x0)
    Sleep(500)
    Yield()
    AS_3D(100, 100, 100, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    PlayEffect(0xFF, 0xFF, 0x0, 0x4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    SetCameraDistance(23000, 600)
    AS_3D(300, 300, 300, 500)
    Sleep(400)
    Yield()
    AS_B0(0x1E, 0x320)
    AS_3A(0xFFF6, 0x3E8)
    Sleep(200)
    Yield()
    AS_3D(200, 200, 200, 1300)
    CancelBlur(300)
    Sleep(1200)
    Yield()
    SetCameraDistance(21000, 100)
    Sleep(500)
    Yield()
    SetCameraDistance(24000, 600)
    AS_3D(600, 600, 600, 800)
    Sleep(500)
    Yield()
    Sleep(400)
    Yield()
    ResetBrightness(500)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 20, 30)
    Sleep(500)
    Yield()
    ResetTarget()
    AS_83(0x0)

    label("loc_4CE")

    ForeachTarget("loc_4DF")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(30)
    Yield()
    NextTarget()
    Jump("loc_4CE")

    label("loc_4DF")

    WaitChrThread(0xFF, 1)
    SetBrightness(0x0, 0x1, 0)
    WaitEffect(0xFF, 0x4)
    FreeEffect(0x0)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_5F(0xF7, 0x1)
    AS_31(0x17, 0x0)
    Call("loc_1D5")
    Return()

    # 大地之矛 end

    def Craft_世界之树(): pass

    label("世界之树")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg014_00.eff")
    LoadEffect(0x1, "battle\\mg014_01.eff")
    LoadEffect(0x2, "battle\\mg014_02.eff")
    AS_78(0)
    Sleep(300)
    Yield()
    AS_43(0x0, 0x12C, 0x0)
    SetBrightness(0x0, 0x0, 500)
    Sleep(300)
    Yield()
    Fade(0x1, 300, 0x0)
    AS_60(0xF7)
    LockCamera(0xFB, 0, 0, 0, 0)
    SetCameraDistance(35000, 0)
    SetCameraDegree(15, 35, 0, 0)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    LockCamera(0xFB, 0, 12000, -5000, 2500)
    Sleep(500)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x1, 0x0, 0x0)
    SetCameraDistance(48000, 1500)
    Sleep(1000)
    Yield()
    SetCameraDegree(-15, 35, 0, 3000)
    Sleep(2500)
    Yield()
    LockCamera(0xFB, 0, 0, 0, 1000)
    AS_B0(0x12, 0x1F4)
    SetCameraDistance(25000, 500)
    Sleep(500)
    Yield()
    FreeEffect(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    SetCameraDistance(33000, 0)
    AS_B0(0x1E, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Sleep(200)
    Yield()
    CancelBlur(500)
    ResetBrightness(500)
    AS_5F(0xF7, 0x1)
    PlayEffect(0xFF, 0xFB, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1800)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 20)
    Sleep(200)
    Yield()
    ResetTarget()

    label("loc_669")

    ForeachTarget("loc_692")
    PlayEffect(0xFF, 0xFE, 0x2, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(300)
    Yield()
    NextTarget()
    Jump("loc_669")

    label("loc_692")

    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    AS_14(0x0)
    AS_14(0x1)
    AS_14(0x2)
    Call("loc_1D5")
    SetBrightness(0x0, 0x1, 0)
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    Return()

    # 世界之树 end

    def Craft_巨神狂怒震(): pass

    label("巨神狂怒震")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg015_00.eff")
    LoadEffect(0x1, "battle\\mg015_01.eff")
    LoadEffect(0x2, "battle\\mg015_02.eff")
    LoadEffect(0x3, "battle\\mg015_03.eff")
    AS_8E(0x1, 0x0, "ef_titan")
    AS_8E(0x7, 0x0, 0xFFFFFF, 0x0, 0x0, 0x0)
    AS_78(0)
    Call("loc_17D")
    AS_34()
    LockCamera(0xFD, 8200, 1800, -5000, 0)
    SetCameraDegree(171, 21, 0, 0)
    SetCameraDistance(40000, 0)
    SetBattleSpeed(600)
    SetCameraDegree(140, 40, 0, 2500)
    LockCamera(0xFD, 6800, 3100, -3800, 2500)
    SetCameraDistance(20000, 2500)
    AS_3D(200, 200, 200, 500)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 8000, 0, -5000, 0, 0, 0, 800, 800, 800, -1)
    Sleep(750)
    Yield()
    AS_3D(500, 500, 500, 1000)
    SetBattleSpeed(1000)
    AS_8E(0x5, 0x0, 0xFD, 0x1F40, 0xFFFFFE0C, 0xFFFFEC78)
    AS_8E(0xB, 0x0, 0x19A, 0x19A, 0x19A, 0x0)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 3)
    Sleep(450)
    Yield()
    AS_8E(0xC, 0x0, 0x1E, 0x0, 0x0, 0x0)
    AS_8E(0x7, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    AS_8E(0x6, 0x0, 0x1, 0x0, 0x0, 0x0)
    AS_8E(0x2, 0x0, 0x28, 0x0, 0x0, 0x0)
    Sleep(1100)
    Yield()
    AS_8E(0x6, 0x0, 0x28, 0x0, 0x0, 0x0)
    AS_8E(0x2, 0x0, 0xA5, 0x0, 0x0, 0x0)
    Sleep(1000)
    Yield()
    LockCamera(0xFD, 8000, 5500, -4000, 1200)
    AS_B0(0x0, 0x9C4)
    SetCameraDistance(28000, 800)
    Sleep(300)
    Yield()
    SoundEx(166, 0x0)
    Sleep(200)
    Yield()
    SetCameraDegree(180, -40, 0, 1000)
    LockCamera(0xFD, 8600, 2200, -1000, 2500)
    Sleep(400)
    Yield()
    SetCameraDistance(10000, 1500)
    SetBattleSpeed(600)
    Sleep(400)
    Yield()
    SoundEx(332, 0x0)
    Sleep(600)
    Yield()
    SetBattleSpeed(250)
    Sleep(300)
    Yield()
    SetBattleSpeed(1000)
    SoundEx(200, 0x0)
    SetCameraDistance(17000, 600)
    AS_B0(0xFFFB, 0x258)
    SoundEx(342, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(300)
    Yield()
    SetBattleSpeed(700)
    Sleep(1100)
    Yield()
    SetBattleSpeed(1000)
    Fade(0x1, 1000, 0x0)
    AS_8E(0x5, 0x0, 0xFD, 0x1F40, 0xFFFFFE0C, 0xFFFFEC78)
    AS_8E(0xB, 0x0, 0x1A4, 0x1A4, 0x1A4, 0x0)
    AS_8E(0x7, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    AS_8E(0x6, 0x0, 0xA5, 0x0, 0x0, 0x0)
    AS_8E(0x2, 0x0, 0xFF, 0x0, 0x0, 0x0)
    CancelBlur(0)
    SetBattleSpeed(600)
    SoundEx(175, 0x0)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, 0, 0, 0, -12, 1000, 1000, 1000, 4)
    AS_1A(0xFF, 0x4, 0x7D0)
    LockCamera(0xFD, 8500, 4000, -5200, 0)
    SetCameraDegree(100, -10, 0, 0)
    SetCameraDistance(20000, 0)
    SetCameraDegree(235, -10, 0, 2000)
    SetCameraDistance(17500, 2000)
    SoundEx(319, 0x0)
    Sleep(1450)
    Yield()
    Play3DEffect(0xFF, 0xEF, "Null_effects", 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1400, 1400, 1400, 5)
    SoundEx(339, 0x0)
    LockCamera(0xFD, 11400, 2800, -4000, 2800)
    SetCameraDegree(210, 0, -10, 2750)
    SetCameraDistance(16500, 2750)
    SoundEx(273, 0x0)
    Sleep(500)
    Yield()
    SetBattleSpeed(500)
    Sleep(1300)
    Yield()
    AS_3D(600, 600, 600, 1300)
    StopEffect(0xFF, 0x4)
    StopEffect(0xFF, 0x3)
    SetBattleSpeed(1000)
    AS_8E(0x5, 0x0, 0xFD, 0x1F40, 0xFFFFFE0C, 0xFFFFEC78)
    AS_8E(0xB, 0x0, 0x1C2, 0x1C2, 0x1C2, 0x0)
    AS_8E(0x7, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    AS_8E(0x6, 0x0, 0x100, 0x0, 0x0, 0x0)
    AS_8E(0x2, 0x0, 0x12C, 0x0, 0x0, 0x0)
    LockCamera(0xFD, 7300, 6000, 14700, 100)
    AS_0B(0xFF4C, 0x64)
    AS_B0(0xF, 0x64)
    SetCameraDistance(5000, 100)
    CancelEffect(0xFF, 0x5)
    SoundEx(339, 0x0)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, 0, 0, 0, -11, 1000, 1000, 1000, 6)
    AS_1A(0xFF, 0x6, 0x12C0)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, 0, 0, 0, -11, 1000, 1000, 1000, 3)
    AS_1A(0xFF, 0x3, 0x2710)
    AS_5F(0xFC, 0x0)
    Sleep(200)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x2, 0x0, 9600, 0, 10000, 0, 0, 0, 1000, 1000, 1000, -1)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x1, 0x0, 0x0)
    Sleep(600)
    Yield()
    SetCameraDistance(18000, 500)
    LockCamera(0xFD, 7300, 3500, 14700, 500)
    AS_3D(800, 800, 800, 500)
    Sleep(500)
    Yield()
    SetBattleSpeed(900)
    SetCameraDistance(23000, 1500)
    Sleep(300)
    Yield()
    SoundEx(238, 0x0)
    AS_43(0x0, 0x320, 0xFFFFFFFF)
    CancelBlur(1000)
    Sleep(700)
    Yield()
    SetBattleSpeed(1000)
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(1000)
    Yield()
    EndChrThread(0xFF, 3)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    Call("loc_1D5")
    AS_8E(0x4, 0x0, 0x0, 0x0, 0x0, 0x0)
    Call("loc_1A3")
    Call("loc_1CA")
    Return()

    label("loc_17D")

    AS_43(0x0, 0x1F4, 0xFF000000)
    Sleep(500)
    Yield()
    SetBrightness(0x0, 0x0, 0)
    AS_6D(0x20000)
    AS_6D(0x40000)
    AS_60(0xF7)
    Fade(0x0, 500, 0xFF000000)
    CallReturn()

    label("loc_1A3")

    Fade(0x1, 500, 0x0)
    AS_7A(0x1)
    ShowChr(0xFF, 0)
    AS_5F(0xF7, 0x0)
    ResetBrightness(0)
    SetBrightness(0x0, 0x1, 0)
    AS_31(0x17, 0x0)
    AS_31(0x3, 0x0)
    Call("loc_2")
    AS_8F(0x0)
    CallReturn()

    label("loc_1CA")

    AS_6E(0x20000)
    AS_6E(0x40000)
    CallReturn()

    # 巨神狂怒震 end

    def Craft_10_16_BE5(): pass

    label("Craft_10_16_BE5")

    Return()

    # Craft_10_16_BE5 end

    def Craft_11_17_D69(): pass

    label("Craft_11_17_D69")

    AS_78(1)
    LoadEffect(0x5, "battle\\mg017_00.eff")
    LoadEffect(0x6, "battle\\mg017_01.eff")
    AS_78(0)
    LockCamera(0xF3, 0, -1000, 0, 1000)
    SetCameraDistance(33000, 1000)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x6, 0x0, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(278, 0x0)
    Call("loc_CEF")
    ResetTarget()

    label("loc_DDA")

    ForeachTarget("loc_E06")
    PlayEffect(0xFF, 0xFE, 0x5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Call("loc_CEF")
    Sleep(250)
    Yield()
    NextTarget()
    Jump("loc_DDA")

    label("loc_CEF")

    Jc(0x15, 0x1, 0x11, "loc_D02")
    SetEffectColor(0xFF, 129, 0xFF834A2C)
    Jump("loc_D68")

    label("loc_D02")

    Jc(0x15, 0x1, 0x1B, "loc_D15")
    SetEffectColor(0xFF, 129, 0xFF5375E8)
    Jump("loc_D68")

    label("loc_D15")

    Jc(0x15, 0x1, 0x25, "loc_D28")
    SetEffectColor(0xFF, 129, 0xFFFF673C)
    Jump("loc_D68")

    label("loc_D28")

    Jc(0x15, 0x1, 0x2F, "loc_D3B")
    SetEffectColor(0xFF, 129, 0xFF5AE09A)
    Jump("loc_D68")

    label("loc_D3B")

    Jc(0x15, 0x1, 0x39, "loc_D4E")
    SetEffectColor(0xFF, 129, 0xFFCB52A7)
    Jump("loc_D68")

    label("loc_D4E")

    Jc(0x15, 0x1, 0x43, "loc_D61")
    SetEffectColor(0xFF, 129, 0xFFB4A94E)
    Jump("loc_D68")

    label("loc_D61")

    SetEffectColor(0xFF, 129, 0xFF8E8EA6)

    label("loc_D68")

    CallReturn()

    label("loc_E06")

    Sleep(1000)
    Yield()
    Call("loc_15")
    Sleep(1000)
    Yield()
    AS_14(0x5)
    AS_14(0x6)
    Call("loc_1D5")
    Return()

    label("loc_15")

    ResetTarget()

    label("loc_16")

    ForeachTarget("loc_23")
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_16")

    label("loc_23")

    CallReturn()

    # Craft_11_17_D69 end

    def Craft_防壁之符文(): pass

    label("防壁之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg018_00.eff")
    LoadEffect(0x3B, "battle\\mg018_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg018_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    label("loc_BE6")

    AS_5F(0xFF, 0x0)
    AS_89(0xFF)
    ChrSetPos(0xFF, 0xFD, 0, 0, 0)
    AS_03(0xFF, 0x0)
    SetCameraDegree(150, 20, -7, 0)
    AS_3A(0x2F8, 0x1F40)
    AS_B0(0x5, 0xFA0)
    LockCamera(0xFF, 0, 300, 0, 0)
    SetCameraDistance(9000, 0)
    SetCameraDistance(20000, 5000)
    AS_3E(0x2BC, 0x0)
    PlayEffect(0xFF, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    SoundEx(371, 0x0)
    SoundEx(223, 0x0)
    Fade(0x0, 500, 0xFF000000)
    Sleep(1500)
    Yield()
    LockCamera(0xFF, 0, 2000, 0, 4000)
    SoundEx(323, 0x0)
    Sleep(600)
    Yield()
    SoundEx(199, 0x0)
    Sleep(1900)
    Yield()
    SoundEx(211, 0x0)
    Sleep(1000)
    Yield()
    SoundEx(231, 0x0)
    Sleep(1000)
    Yield()
    Sleep(1000)
    Yield()
    AS_43(0x0, 0x1F4, 0xFF000000)
    Sleep(500)
    Yield()
    SoundEx(341, 0x0)
    StopEffect(0xFF, 0x3)
    AS_8D(0x4F, 0x0, 0x0, 0x0, 0x0)
    ResetBrightness(0)
    AS_6E(0x20000)
    AS_0A(0xFF, 0x5, 0x0, 0x0)
    AS_31(0x16, 0x0)
    TurnDirection(0xFF, 0xFB, 0, 0, 0x0)
    AS_5F(0xF7, 0x1)
    Fade(0x0, 500, 0xFF000000)
    Sleep(200)
    Yield()
    AS_14(0x2D)
    FreeEffect(0x0)
    CallReturn()

    # 防壁之符文 end

    def Craft_冰之刃(): pass

    label("冰之刃")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg020_00.eff")
    LoadEffect(0x1, "battle\\mg020_01.eff")
    AS_78(0)
    Sleep(125)
    Yield()
    PlayEffect(0xFF, 0xF9, 0x0, 0x4, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1250)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 800)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 冰之刃 end

    def Craft_冰蓝之泪(): pass

    label("冰蓝之泪")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg021_00.eff")
    LoadEffect(0x1, "battle\\mg021_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 2400, 0, 600)
    Sleep(800)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 1300, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(600)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 1500)
    Sleep(3200)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 1300, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Call("loc_2")
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xF4, 0, 0, 0, 0)
    Return()

    # 冰蓝之泪 end

    def Craft_冰之锤(): pass

    label("冰之锤")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg022_00.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    SetCameraDistance(25000, 1200)
    LockCamera(0xFE, 0, 4000, 0, 1200)
    Sleep(300)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(2400)
    Yield()
    LockCamera(0xFE, 0, 1000, 0, 200)
    SetCameraDistance(20000, 200)
    Sleep(200)
    Yield()
    AS_3D(100, 100, 100, 500)
    Call("loc_2")
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 冰之锤 end

    def Craft_水流轰击(): pass

    label("水流轰击")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg023_00.eff")
    AS_78(0)
    LockCamera(0xF9, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x0, 0x4, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(600)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x1, 0x0, 0x0)
    Sleep(600)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 20, 30)
    AS_B0(0x1E, 0x12C)
    Sleep(1000)
    Yield()
    BeginChrThread(0xFF, 3, "loc_24", 0x0)
    CancelBlur(500)
    WaitEffect(0xFF, 0x4)
    FreeEffect(0x0)
    WaitChrThread(0xFF, 3)
    Return()

    label("loc_24")

    ResetTarget()

    label("loc_25")

    ForeachTarget("loc_36")
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_25")

    label("loc_36")

    CallReturn()

    # 水流轰击 end

    def Craft_钻石星尘(): pass

    label("钻石星尘")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg024_00.eff")
    LoadEffect(0x1, "battle\\mg024_01.eff")
    LoadEffect(0x2, "battle\\mg024_02.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFE, 0, 500, 0, 500)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    PlayEffect(0xFF, 0xFE, 0x2, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(4400)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    WaitEffect(0xFF, 0x4)
    AS_14(0x1)
    AS_14(0x2)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    Return()

    # 钻石星尘 end

    def Craft_大海啸(): pass

    label("大海啸")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg025_00.eff")
    LoadEffect(0x1, "battle\\mg025_01.eff")
    AS_78(0)
    Sleep(500)
    Yield()
    SetBrightness(0x0, 0x0, 500)
    LockCamera(0xFF, 0, 1500, 0, 600)
    Sleep(600)
    Yield()
    AS_34()
    Fade(0x1, 800, 0x0)
    AS_60(0xF7)
    LockCamera(0xF3, 0, 0, -100000, 0)
    SetCameraDistance(20000, 0)
    SetCameraDegree(178, 20, 0, 0)
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SetCameraDegree(180, 30, 0, 2500)
    LockCamera(0xF3, 0, 0, -99000, 2500)
    SetCameraDistance(21800, 500)
    Sleep(1800)
    Yield()
    Fade(0x1, 1000, 0x0)
    AS_5F(0xFC, 0x0)
    LockCamera(0xF3, 0, 0, 0, 0)
    AS_31(0x17, 0xBB8)
    SetCameraDistance(33000, 3000)
    Sleep(1500)
    Yield()
    ResetTarget()

    label("loc_1276")

    ForeachTarget("loc_129F")
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(60)
    Yield()
    NextTarget()
    Jump("loc_1276")

    label("loc_129F")

    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    ResetBrightness(500)
    Sleep(1500)
    Yield()
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    SetBrightness(0x0, 0x1, 0)
    AS_5F(0xF7, 0x1)
    AS_31(0x17, 0x0)
    LockCamera(0xF4, 0, 0, 0, 0)
    Return()

    # 大海啸 end

    def Craft_灭世冥寒灾(): pass

    label("灭世冥寒灾")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg026_00.eff")
    LoadEffect(0x1, "battle\\mg026_01.eff")
    LoadEffect(0x2, "battle\\mg026_02.eff")
    LoadEffect(0x3, "battle\\mg026_03.eff")
    AS_78(0)
    Call("loc_17D")
    AS_34()
    AS_3E(0xFA, 0x0)
    LockCamera(0xFD, 0, 0, -10000, 0)
    SetCameraDegree(0, 20, -10, 0)
    SetCameraDistance(20000, 0)
    Fade(0x1, 1500, 0x0)
    Sleep(500)
    Yield()
    SetBattleSpeed(1200)
    LockCamera(0xFD, 0, -200, -10000, 4000)
    AS_0B(0x0, 0xFA0)
    AS_B0(0x1E, 0xFA0)
    SetCameraDistance(28000, 4000)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    PlayEffect(0xFF, 0xFD, 0x2, 0x0, 0, 0, -10000, 0, 0, 0, 600, 600, 600, 3)
    SoundEx(183, 0x0)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(1500)
    Yield()
    AS_0B(0x28, 0x7D0)
    AS_B0(0xFFFB, 0x7D0)
    SoundEx(187, 0x0)
    SetBattleSpeed(800)
    Sleep(1000)
    Yield()
    SetCameraDistance(36000, 1000)
    Sleep(600)
    Yield()
    SoundEx(360, 0x0)
    Sleep(400)
    Yield()
    SetBattleSpeed(700)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x4)
    SetBattleSpeed(1000)
    Fade(0x1, 800, 0x0)
    SoundEx(233, 0x0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x1130)
    SetBattleSpeed(450)
    LockCamera(0xFD, -200, -2600, -9900, 0)
    SetCameraDistance(13520, 0)
    SetCameraDegree(30, 10, 0, 0)
    LockCamera(0xFD, 0, 1900, -9700, 1800)
    SetCameraDistance(15600, 1800)
    SetCameraDegree(330, -13, 0, 1800)
    Sleep(1500)
    Yield()
    SetBattleSpeed(300)
    Sleep(300)
    Yield()
    StopEffect(0xFF, 0x2)
    SetBattleSpeed(1000)
    Fade(0x1, 1000, 0x0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x1B58)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 4)
    AS_1A(0xFF, 0x4, 0x1DB0)
    SetBattleSpeed(500)
    LockCamera(0xFD, 1000, 1900, -12500, 0)
    SetCameraDegree(340, 10, 0, 0)
    SetCameraDistance(13000, 0)
    SoundEx(339, 0x0)
    LockCamera(0xFD, 1500, 2600, -13300, 2500)
    SetCameraDistance(4500, 2000)
    Sleep(1000)
    Yield()
    SetBattleSpeed(900)
    Sleep(500)
    Yield()
    StopEffect(0xFF, 0x3)
    LockCamera(0xFD, 0, 100, -14000, 350)
    SetCameraDegree(35, 2, -10, 350)
    SetCameraDistance(28000, 350)
    SoundEx(321, 0x0)
    Sleep(500)
    Yield()
    SetBattleSpeed(1000)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x4)
    Fade(0x1, 500, 0x0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x2904)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 4)
    AS_1A(0xFF, 0x4, 0x2B5C)
    SetBattleSpeed(1300)
    PlayEffect(0xFF, 0xFD, 0x2, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 3)
    SoundEx(339, 0x0)
    LockCamera(0xFD, 0, 2000, -13000, 0)
    SetCameraDegree(25, 10, -5, 0)
    SetCameraDistance(13000, 0)
    AS_0B(0x5, 0x3E8)
    LockCamera(0xFD, 1200, 2100, -10000, 1000)
    SetCameraDistance(9200, 1000)
    Sleep(1000)
    Yield()
    StopEffect(0xFF, 0x3)
    AS_0B(0xFFF1, 0x258)
    LockCamera(0xFD, 0, 1000, -11000, 600)
    AS_B0(0xF, 0x1F4)
    SetCameraDistance(28000, 600)
    SoundEx(321, 0x0)
    Sleep(1000)
    Yield()
    SetBattleSpeed(1000)
    Fade(0x1, 500, 0x0)
    AS_5F(0xFC, 0x0)
    LockCamera(0xFD, 8000, 2000, 1000, 0)
    AS_0B(0xFFA6, 0x0)
    AS_B0(0x0, 0x0)
    SetCameraDistance(58000, 0)
    LockCamera(0xFD, 8000, 1600, 8000, 800)
    AS_0B(0x0, 0x320)
    SetCameraDistance(60000, 800)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x4)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 8000, 1000, 8000, 0, 0, 0, 1000, 1000, 1000, 2)
    Sleep(800)
    Yield()
    ResetTarget()

    label("loc_16E6")

    ForeachTarget("loc_16F0")
    EndChrThread(0xFE, 255)
    NextTarget()
    Jump("loc_16E6")

    label("loc_16F0")

    Sleep(300)
    Yield()
    SoundEx(321, 0x0)
    Sleep(300)
    Yield()
    SoundEx(293, 0x0)
    Sleep(1400)
    Yield()
    AS_60(0xFC)
    AS_A8(0x0, 0x1)
    Fade(0x1, 500, 0x0)
    SetBattleSpeed(1150)
    LockCamera(0xFD, 200, 1900, -10700, 0)
    AS_0B(0x140, 0x0)
    AS_B0(0xF, 0x0)
    SetCameraDistance(9000, 0)
    StopEffect(0xFF, 0x2)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 5)
    AS_1A(0xFF, 0x5, 0x34BC)
    Sleep(200)
    Yield()
    Sleep(800)
    Yield()
    SetCameraDistance(14000, 3000)
    Sleep(2000)
    Yield()
    AS_A8(0x0, 0x0)
    SetBattleSpeed(1000)
    Fade(0x1, 500, 0x0)
    AS_5F(0xFC, 0x0)
    LockCamera(0xFD, 8000, 1600, 8000, 0)
    SetCameraDegree(0, 15, 0, 0)
    SetCameraDistance(60000, 0)
    StopEffect(0xFF, 0x2)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 7500, 1000, -5000, 0, 0, 0, 800, 800, 800, 2)
    AS_1A(0xFF, 0x2, 0xC80)
    Sleep(800)
    Yield()
    AS_8D(0x8, 0x0, 0x0, 0x0, 0x0)
    Sleep(100)
    Yield()
    AS_60(0xFC)
    SoundEx(185, 0x0)
    Sleep(800)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    AS_43(0x0, 0x320, 0xFFFFFFFF)
    SoundEx(312, 0x0)
    Sleep(300)
    Yield()
    SetBattleSpeed(400)
    Sleep(600)
    Yield()
    CancelBlur(500)
    WaitEffect(0xFF, 0x2)
    SetBattleSpeed(1000)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    Call("loc_1D5")
    AS_6E(0x40000)
    Call("loc_1A3")
    Call("loc_1CA")
    Return()

    # 灭世冥寒灾 end

    def Craft_1B_27_1832(): pass

    label("Craft_1B_27_1832")

    Jump("Craft_11_17_D69")

    # Craft_1B_27_1832 end

    def Craft_慈爱之符文(): pass

    label("慈爱之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg028_00.eff")
    LoadEffect(0x3B, "battle\\mg028_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg028_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    # 慈爱之符文 end

    def Craft_火之矢(): pass

    label("火之矢")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg030_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    PlayEffect(0xFF, 0xF9, 0x0, 0x4, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1200)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 1000)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 火之矢 end

    def Craft_灼热之波(): pass

    label("灼热之波")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg031_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(3600)
    Yield()
    Call("loc_2")
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 灼热之波 end

    def Craft_熔岩之息(): pass

    label("熔岩之息")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg032_00.eff")
    AS_78(0)
    Sleep(400)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(900)
    Yield()
    SetCameraDistance(26000, 2500)
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(400)
    Yield()
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(400)
    Yield()
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(400)
    Yield()
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(300)
    Yield()
    DamageCue(0xFE)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 熔岩之息 end

    def Craft_炎蝶之舞(): pass

    label("炎蝶之舞")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg033_00.eff")
    LoadEffect(0x1, "battle\\mg033_01.eff")
    AS_78(0)
    Sleep(400)
    Yield()
    LockCamera(0xFB, 0, 0, 0, 600)
    SetCameraDistance(23000, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(2300)
    Yield()
    AS_B0(0x19, 0x4B0)
    Sleep(600)
    Yield()
    AS_3D(100, 100, 100, 500)
    Sleep(500)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    Yield()
    SetCameraDistance(28000, 300)
    AS_3D(250, 250, 250, 3000)
    PlayEffect(0xFF, 0xFB, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(3000)
    Yield()
    CancelBlur(500)
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    WaitChrThread(0xFF, 3)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Return()

    # 炎蝶之舞 end

    def Craft_赤红射线(): pass

    label("赤红射线")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg034_00.eff")
    LoadEffect(0x1, "battle\\mg034_01.eff")
    AS_78(0)
    Sleep(300)
    Yield()
    SetBrightness(0x0, 0x0, 800)
    AS_34()
    Fade(0x1, 800, 0x0)
    AS_60(0xF7)
    AS_5F(0xFC, 0x0)
    LockCamera(0xFE, 0, 15000, 0, 0)
    SetCameraDistance(24000, 0)
    SetCameraDegree(0, 30, 0, 0)
    Sleep(800)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    AS_03(0xFC, 0xB4)
    Sleep(1900)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 500)
    AS_B0(0x23, 0x190)
    Sleep(400)
    Yield()
    AS_3D(200, 100, 200, 2700)
    Sleep(2400)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x7)
    Sleep(350)
    Yield()
    SetCameraDistance(15000, 700)
    AS_B0(0x1C, 0x258)
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    Sleep(700)
    Yield()
    AS_3D(500, 500, 500, 3500)
    SetCameraDegree(0, 15, -5, 500)
    AS_B0(0x19, 0x5DC)
    SetCameraDistance(35000, 4200)
    Sleep(2000)
    Yield()
    SetCameraDegree(-30, 25, -5, 2800)
    LockCamera(0xFE, 0, 2000, 0, 2800)
    SetBattleSpeed(700)
    Sleep(2800)
    Yield()
    SetBattleSpeed(1000)
    Fade(0x1, 500, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFE, 0, 0, 0, 0)
    StopEffect(0xFF, 0x2)
    AS_0A(0xFC, 0x1, 0x0, 0x0)
    ResetBrightness(0)
    AS_5F(0xF7, 0x1)
    CancelBlur(500)
    Sleep(300)
    Yield()
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    SetBrightness(0x0, 0x1, 0)
    AS_8F(0x0)
    Return()

    # 赤红射线 end

    def Craft_龙皇炼狱火(): pass

    label("龙皇炼狱火")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg035_00.eff")
    LoadEffect(0x1, "battle\\mg035_01.eff")
    LoadEffect(0x2, "battle\\mg035_02.eff")
    LoadEffect(0x3, "battle\\mg035_03.eff")
    LoadEffect(0x4, "battle\\mg035_04.eff")
    LoadEffect(0x5, "battle\\mg035_05.eff")
    LoadEffect(0x6, "battle\\mg035_06.eff")
    LoadEffect(0x7, "battle\\mg015_03.eff")
    AS_78(0)
    Call("loc_17D")
    AS_34()
    LockCamera(0xFD, 100, 500, -11200, 0)
    SetCameraDegree(0, 10, 0, 0)
    SetCameraDistance(22000, 0)
    AS_AC(0x3E8, 0x927C0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    SoundEx(197, 0x0)
    Sleep(1100)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x4, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 3)
    Sleep(300)
    Yield()
    Fade(0x1, 500, 0x0)
    SetBattleSpeed(600)
    SoundEx(320, 0x0)
    LockCamera(0xFD, 0, 1300, -10900, 0)
    AS_0B(0xDC, 0x0)
    SetCameraDistance(6500, 0)
    AS_0B(0x190, 0x3E8)
    SetCameraDistance(3000, 1000)
    AS_B0(0x28, 0x708)
    Sleep(500)
    Yield()
    AS_B0(0x28, 0x1F4)
    LockCamera(0xFD, -1300, 4400, -11100, 700)
    SoundEx(339, 0x0)
    Sleep(500)
    Yield()
    BlurSwitch(0xC8, 0xBBFFFFFF, 0x1, 0x0, 0x0)
    SetCameraDistance(6000, 500)
    SoundEx(261, 0x0)
    Sleep(1500)
    Yield()
    SoundEx(320, 0x0)
    CancelBlur(1000)
    SetBattleSpeed(1000)
    AS_B0(0x46, 0x3E8)
    Sleep(1500)
    Yield()
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x14B4)
    PlayEffect(0xFF, 0xFD, 0x4, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 3)
    AS_1A(0xFF, 0x3, 0x1388)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 6000, -10000, 0, 0, 0, 900, 900, 900, 4)
    AS_1A(0xFF, 0x4, 0x2710)
    LockCamera(0xFD, 800, 4000, -10000, 0)
    AS_B0(0x54, 0x0)
    AS_3C(0xFFD8, 0x0)
    AS_0B(0x0, 0x0)
    SetCameraDistance(16000, 0)
    LockCamera(0xFD, -1000, 36000, -4000, 1800)
    SetCameraDistance(17000, 1800)
    SoundEx(251, 0x0)
    Sleep(300)
    Yield()
    BlurSwitch(0x32, 0xBBFFFFFF, 0x1, 0x0, 0x0)
    Sleep(700)
    Yield()
    CancelBlur(1000)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    StopEffect(0xFF, 0x4)
    Fade(0x1, 200, 0x0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x1FA4)
    LockCamera(0xFD, 0, 35000, -10000, 0)
    AS_0B(0xFFB0, 0x0)
    AS_B0(0x19, 0x0)
    AS_3C(0xA, 0x0)
    SetCameraDistance(10000, 0)
    SetCameraDistance(13000, 500)
    LockCamera(0xFD, 0, 43500, -10000, 2000)
    AS_0B(0xFFC4, 0x7D0)
    AS_B0(0xFFF6, 0x7D0)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 6000, -10000, 0, 0, 0, 900, 900, 900, 3)
    SoundEx(375, 0x0)
    Sleep(1500)
    Yield()
    SoundEx(204, 0x0)
    Sleep(250)
    Yield()
    SoundEx(253, 0x0)
    Sleep(550)
    Yield()
    CancelEffect(0xFF, 0x3)
    Sleep(1000)
    Yield()
    Fade(0x1, 600, 0x0)
    LockCamera(0xFD, 0, 43800, -11400, 0)
    AS_B0(0x1, 0x0)
    AS_3C(0x0, 0x0)
    AS_0B(0xFFFF, 0x0)
    SetCameraDistance(600, 0)
    PlayEffect(0xFF, 0xFD, 0x6, 0x0, 0, 42500, -11000, 0, 0, 0, 1200, 1200, 1200, 4)
    PlayEffect(0xFF, 0xFD, 0x7, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(320, 0x0)
    SetCameraDistance(3000, 3500)
    SoundEx(371, 0x0)
    Sleep(2500)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x2, 0x0, 0, 43300, -11000, 15, 180, 0, 150, 150, 150, -1)
    AS_0B(0xFFF6, 0x76C)
    Sleep(1900)
    Yield()
    LockCamera(0xFD, 0, 43000, -12000, 500)
    AS_0B(0xFFEC, 0x5DC)
    AS_B0(0xA, 0x5DC)
    SetCameraDistance(10000, 800)
    Sleep(800)
    Yield()
    AS_A8(0x0, 0x7)
    CancelEffect(0xFF, 0x4)
    AS_A8(0x0, 0x2)
    Fade(0x1, 500, 0x0)
    LockCamera(0xFD, 10000, 1000, 8000, 0)
    AS_0B(0x91, 0x0)
    AS_B0(0x14, 0x0)
    AS_3C(0x0, 0x0)
    SetCameraDistance(30000, 0)
    LockCamera(0xFD, 6000, 1000, 8000, 2000)
    AS_0B(0x73, 0x7D0)
    SetCameraDistance(19000, 3000)
    AS_5F(0xFC, 0x0)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x5, 0x0, 8000, 0, 8000, 0, 90, 0, 1000, 1000, 1000, 2)
    Sleep(2700)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 8000, 0, 8000, 0, 90, 0, 1200, 1200, 1200, -1)
    AS_0B(0x64, 0x7D0)
    SetCameraDistance(25000, 3000)
    SoundEx(367, 0x0)
    Sleep(2300)
    Yield()
    BeginChrThread(0xFF, 3, "loc_37", 0x0)
    Sleep(500)
    Yield()
    AS_43(0x0, 0x1F4, 0xFFFFFFFF)
    Sleep(1500)
    Yield()
    EndChrThread(0xFF, 3)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    Call("loc_1D5")
    Call("loc_1A3")
    Call("loc_1CA")
    Return()

    # 龙皇炼狱火 end

    def Craft_24_36_2131(): pass

    label("Craft_24_36_2131")

    Return()

    # Craft_24_36_2131 end

    def Craft_25_37_2132(): pass

    label("Craft_25_37_2132")

    Jump("Craft_11_17_D69")

    # Craft_25_37_2132 end

    def Craft_胜利之符文(): pass

    label("胜利之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg038_00.eff")
    LoadEffect(0x3B, "battle\\mg038_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg038_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    # 胜利之符文 end

    def Craft_雷电击(): pass

    label("雷电击")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg040_00.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 3500, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1000)
    Yield()
    LockCamera(0xFE, 0, 1000, 0, 200)
    AS_3D(200, 200, 200, 200)
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 雷电击 end

    def Craft_风之镰(): pass

    label("风之镰")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg041_00.eff")
    LoadEffect(0x1, "battle\\mg041_01.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    PlayEffect(0xFF, 0xF9, 0x0, 0x5, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1000)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 20, 30)
    Sleep(400)
    Yield()
    ResetTarget()
    AS_83(0x0)

    label("loc_2276")

    ForeachTarget("loc_22A5")
    PlayEffect(0xFF, 0xF8, 0x1, 0x10, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("loc_2276")

    label("loc_22A5")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 风之镰 end

    def Craft_风之领域(): pass

    label("风之领域")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg042_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xFB, 0, 0, 0, 600)
    SetCameraDistance(18700, 1000)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(800)
    Yield()
    AS_3D(100, 100, 100, 3200)
    Sleep(300)
    Yield()
    BlurSwitch(0x190, 0xBBFFFFFF, 0x1, 0x0, 0x0)
    Sleep(400)
    Yield()
    AS_B0(0x15, 0x7D0)
    LockCamera(0xFB, 0, 1800, 0, 2400)
    SetCameraDistance(22000, 2400)
    Sleep(3200)
    Yield()
    Fade(0x1, 500, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Sleep(800)
    Yield()
    CancelBlur(500)
    Call("loc_2")
    AS_14(0x0)
    FreeEffect(0x0)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Return()

    # 风之领域 end

    def Craft_闪电之力(): pass

    label("闪电之力")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg043_00.eff")
    LoadEffect(0x1, "battle\\mg043_01.eff")
    AS_78(0)
    LockCamera(0xF4, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(1700)
    Yield()
    ResetTarget()

    label("loc_23F7")

    ForeachTarget("loc_2426")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_23F7")

    label("loc_2426")

    WaitEffect(0xFF, 0x4)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 闪电之力 end

    def Craft_雷光龙卷(): pass

    label("雷光龙卷")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg044_00.eff")
    LoadEffect(0x1, "battle\\mg043_01.eff")
    AS_78(0)
    SetBrightness(0x0, 0x0, 800)
    Sleep(200)
    Yield()
    SetCameraDistance(26000, 600)
    LockCamera(0xFB, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    AS_60(0xF7)
    AS_5F(0xFC, 0x0)
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(1000)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x4)
    AS_B0(0x14, 0xBB8)
    Sleep(3200)
    Yield()
    SetCameraDistance(30000, 300)
    AS_B0(0x1E, 0x12C)
    Sleep(300)
    Yield()
    CancelBlur(500)
    Fade(0x1, 300, 0x0)
    AS_5F(0xF7, 0x1)
    Sleep(200)
    Yield()
    ResetTarget()

    label("loc_24E3")

    ForeachTarget("loc_250C")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_24E3")

    label("loc_250C")

    ResetBrightness(500)
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    WaitEffect(0xFF, 0x4)
    Call("loc_1D5")
    Sleep(600)
    Yield()
    SetBrightness(0x0, 0x1, 0)
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Return()

    # 雷光龙卷 end

    def Craft_终焉三重奏(): pass

    label("终焉三重奏")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x1, "battle\\mg045_01.eff")
    LoadEffect(0x2, "battle\\mg045_02.eff")
    LoadEffect(0x3, "battle\\mg045_03.eff")
    LoadEffect(0x4, "battle\\mg045_04.eff")
    LoadEffect(0x5, "battle\\mg045_05.eff")
    LoadEffect(0x6, "battle\\mg045_06.eff")
    AS_78(0)
    Call("loc_17D")
    ClearChipModeFlags(0x0, 0xFC, 0x1)
    AS_34()
    Fade(0x1, 1000, 0x0)
    AS_AC(0x3E8, 0xFFFFFFFF)
    LockCamera(0xFD, 0, 14400, -12000, 0)
    SetCameraDegree(0, -10, 0, 0)
    SetCameraDistance(32000, 0)
    SetCameraDistance(27500, 2000)
    SoundEx(132, 0x1)
    PlayEffect(0xFF, 0xFD, 0x4, 0x0, 0, 10000, -10000, 0, 0, 0, 1000, 1000, 1000, 3)
    PlayEffect(0xFF, 0xFD, 0x6, 0x0, 0, 12000, -10000, 0, 0, 0, 600, 600, 600, 6)
    SoundEx(359, 0x1)
    Sleep(2400)
    Yield()
    CancelEffect(0xFF, 0x6)
    Sleep(100)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x5, 0x0, 0, 13000, -10000, 0, 0, 0, 1000, 1000, 1000, 5)
    SoundEx(200, 0x0)
    Sleep(300)
    Yield()
    CancelEffect(0xFF, 0x4)
    SetBattleSpeed(600)
    StopSound(359)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 13000, -10000, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(500)
    Yield()
    CancelEffect(0xFF, 0x5)
    CancelEffect(0xFF, 0x2)
    SoundEx(359, 0x1)
    LockCamera(0xFD, 0, 11000, -11700, 0)
    SetCameraDistance(3850, 0)
    AS_B0(0xFFEC, 0x0)
    Fade(0x1, 500, 0x0)
    CancelEffect(0xFF, 0x3)
    LockCamera(0xFD, 0, 20200, -11700, 2000)
    AS_B0(0xA, 0x7D0)
    Sleep(1800)
    Yield()
    StopSound(359)
    Fade(0x1, 500, 0x0)
    LockCamera(0xFD, 0, 14300, -11100, 0)
    SetCameraDistance(32000, 0)
    AS_B0(0xFFF6, 0x0)
    Sleep(300)
    Yield()
    CancelEffect(0xFF, 0x5)
    SetBattleSpeed(1000)
    PlayEffect(0xFF, 0xFD, 0x5, 0x0, 0, 13000, -10000, 0, 0, 0, 800, 800, 800, 5)
    AS_1A(0xFF, 0x5, 0x7D0)
    StopSound(132)
    Sleep(1150)
    Yield()
    Fade(0x1, 500, 0x0)
    LockCamera(0xFD, 8000, 500, 8000, 0)
    AS_0B(0x1E, 0x0)
    AS_B0(0xA, 0x0)
    AS_3C(0x5, 0x0)
    SetCameraDistance(27000, 0)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    StopEffect(0xFF, 0x4)
    ChrSetPos(0xFF, 0xF3, 0, 0, 0)
    AS_8D(0x1, 0x0, 0x0, 0x0, 0x0)
    ResetTarget()

    label("loc_27B2")

    ForeachTarget("loc_27D8")
    AS_05(0xFE, 0x2, 0x0)

    def lambda_27C0():
        AS_21(0x1, 0xFF, -2500, 0)
        Return()

    QueueWorkItem(0xFE, 1, lambda_27C0)
    TurnDirection(0xFE, 0xFF, 0, 0, 0x0)
    NextTarget()
    Jump("loc_27B2")

    label("loc_27D8")

    WaitChrThread(0xFC, 1)
    AS_5F(0xFC, 0x0)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x5, 0x0, 8000, 0, 8000, 0, 0, 0, 1000, 1000, 1000, 5)
    AS_1A(0xFF, 0x5, 0xFA0)
    AS_0B(0x2D, 0x320)
    AS_B0(0x1E, 0x320)
    SetCameraDistance(32000, 800)
    PlayEffect(0xFF, 0xFD, 0x4, 0x0, 0, 10000, -10000, 0, 0, 0, 1000, 1000, 1000, 3)
    AS_1A(0xFF, 0x3, 0x2710)
    Sleep(300)
    Yield()
    ResetTarget()

    label("loc_283E")

    ForeachTarget("loc_2849")
    DamageAnime(0xFE, 0x0, 0x32)
    NextTarget()
    Jump("loc_283E")

    label("loc_2849")

    Sleep(850)
    Yield()
    Fade(0x1, 1000, 0x0)
    AS_5F(0xFC, 0x0)
    LockCamera(0xFD, 8000, 35900, 8000, 0)
    SetCameraDistance(12800, 0)
    AS_0B(0xF, 0x0)
    AS_B0(0xFFE7, 0x0)
    AS_3C(0xFFF6, 0x0)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 8000, 36500, 8000, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x1770)
    SoundEx(238, 0x0)
    Sleep(400)
    Yield()
    SoundEx(339, 0x0)
    Sleep(600)
    Yield()
    SoundEx(375, 0x0)
    Sleep(1000)
    Yield()
    LockCamera(0xFD, 8000, 36500, 8000, 300)
    SetCameraDistance(28000, 300)
    Sleep(200)
    Yield()
    BlurSwitch(0x258, 0xBBFFFFFF, 0x1, 0x1, 0xA)
    SetBattleSpeed(400)
    Sleep(300)
    Yield()
    SetBattleSpeed(1000)
    Sleep(1200)
    Yield()
    LockCamera(0xFD, 8000, 1000, 8000, 500)
    AS_B0(0x5, 0x1F4)
    Sleep(500)
    Yield()
    CancelBlur(500)
    PlayEffect(0xFF, 0xFD, 0x2, 0x0, 8000, 0, 8000, 0, 0, 0, 750, 750, 750, 3)
    SoundEx(210, 0x0)
    SetCameraDistance(26000, 300)
    AS_0B(0x0, 0x9C4)
    AS_B0(0xF, 0x9C4)
    Sleep(1200)
    Yield()
    SetCameraDistance(33000, 2500)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 8000, 0, 8000, 0, 0, 0, 800, 800, 800, 4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0x7)
    AS_A6(0xFF, 0x4, 0x4B0, 0x3E8, 0x0)
    SoundEx(359, 0x1)
    Sleep(1000)
    Yield()
    AS_43(0x0, 0x1F4, 0xFFFFFFFF)
    CancelBlur(1000)
    Sleep(1000)
    Yield()
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    AS_A8(0x0, 0x4)
    AS_A8(0x0, 0x5)
    AS_A8(0x0, 0x6)
    StopSound(359)
    Sleep(500)
    Yield()
    AS_8D(0xA, 0x0, 0x0, 0x0, 0x0)
    Call("loc_1D5")
    Call("loc_1A3")
    EndChrThread(0xFC, 1)
    Call("loc_1CA")
    Return()

    # 终焉三重奏 end

    def Craft_2E_46_29DE(): pass

    label("Craft_2E_46_29DE")

    Return()

    # Craft_2E_46_29DE end

    def Craft_2F_47_29DF(): pass

    label("Craft_2F_47_29DF")

    Jump("Craft_11_17_D69")

    # Craft_2F_47_29DF end

    def Craft_暴风之符文(): pass

    label("暴风之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg048_00.eff")
    LoadEffect(0x3B, "battle\\mg048_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg048_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    # 暴风之符文 end

    def Craft_心灵之霞(): pass

    label("心灵之霞")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg050_00.eff")
    LoadEffect(0x1, "battle\\mg050_01.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    PlayEffect(0xFF, 0xF9, 0x0, 0x4, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1500)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 300)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 心灵之霞 end

    def Craft_死亡螺旋(): pass

    label("死亡螺旋")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg051_00.eff")
    LoadEffect(0x1, "battle\\mg051_01.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    SetCameraDistance(22000, 600)
    Sleep(450)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1300)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(2000)
    Yield()
    Call("loc_2")
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 死亡螺旋 end

    def Craft_暗影裁决(): pass

    label("暗影裁决")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg052_00.eff")
    LoadEffect(0x1, "battle\\mg052_01.eff")
    LoadEffect(0x2, "battle\\mg052_02.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    SetBrightness(0x0, 0x0, 500)
    AS_43(0x0, 0x1F4, 0x0)
    Sleep(800)
    Yield()
    Fade(0x1, 500, 0x0)
    AS_60(0xF7)
    LockCamera(0xFD, -1500, -25000, -4000, 0)
    SetCameraDegree(0, 320, -22, 0)
    SetCameraDistance(50000, 0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_3D(50, 50, 50, 1800)
    LockCamera(0xFD, 1100, 5000, 0, 1600)
    Sleep(200)
    Yield()
    SetCameraDistance(13000, 1300)
    SetCameraDegree(20, 300, -22, 1200)
    Sleep(1200)
    Yield()
    BlurSwitch(0xC8, 0xBBFFFFFF, 0x0, 0x1, 0x7)
    LockCamera(0xFD, 1800, 15000, 4000, 400)
    AS_43(0x0, 0x12C, 0x0)
    SetCameraDistance(5000, 300)
    Sleep(300)
    Yield()
    StopEffect(0xFF, 0x2)
    CancelBlur(0)
    Fade(0x1, 300, 0x0)
    ResetBrightness(500)
    AS_5F(0xF7, 0x1)
    AS_31(0x17, 0x0)
    LockCamera(0xF4, 0, 3000, 0, 0)
    SetCameraDistance(25000, 0)
    AS_B0(0x21, 0x0)
    Sleep(500)
    Yield()
    PlayEffect(0xFE, 0xF2, 0x0, 0x0, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    AS_1A(0xFE, 0x3, 0xBB8)
    LockCamera(0xF4, 0, 0, 0, 400)
    Sleep(1200)
    Yield()
    ResetTarget()

    label("loc_2CC8")

    ForeachTarget("loc_2CF1")
    PlayEffect(0xFF, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("loc_2CC8")

    label("loc_2CF1")

    Sleep(1600)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(300, 28, 20)
    AS_B0(0x16, 0x320)
    PlayEffect(0xFF, 0xF9, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(300)
    Yield()
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    Sleep(2500)
    Yield()
    SetBrightness(0x0, 0x1, 0)
    WaitEffect(0xFF, 0x4)
    AS_14(0x1)
    AS_14(0x2)
    Call("loc_1D5")
    Return()

    # 暗影裁决 end

    def Craft_灾厄镰刃(): pass

    label("灾厄镰刃")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg053_00.eff")
    LoadEffect(0x1, "battle\\mg050_01.eff")
    AS_78(0)
    SoundEx(222, 0x0)
    Sleep(250)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x0, 0x4, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1100)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 20, 30)
    Sleep(400)
    Yield()
    ResetTarget()
    AS_83(0x0)

    label("loc_2DB0")

    ForeachTarget("loc_2DDF")
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("loc_2DB0")

    label("loc_2DDF")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    Return()

    # 灾厄镰刃 end

    def Craft_堕天使暗翼(): pass

    label("堕天使暗翼")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg054_00.eff")
    LoadEffect(0x1, "battle\\mg054_01.eff")
    LoadEffect(0x2, "battle\\mg054_02.eff")
    LoadEffect(0x3, "battle\\mg054_03.eff")
    AS_78(0)
    Call("loc_17D")
    AS_60(0xFC)
    AS_8D(0xB, 0x0, 0x0, 0x0, 0x0)
    ChrSetPos(0xFF, 0xF3, 0, 0, -2500)
    AS_AC(0x1F4, 0xFFFFFFFF)
    LockCamera(0xF3, 0, 100, -9500, 0)
    SetCameraDegree(320, 30, -8, 0)
    SetCameraDistance(15000, 0)
    SetCameraDegree(180, 26, 0, 4500)
    SetCameraDistance(8300, 4500)
    PlayEffect(0xFF, 0xF3, 0x0, 0x0, 0, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 2)
    PlayEffect(0xFF, 0xF3, 0x3, 0x0, 0, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 3)
    SoundEx(215, 0x0)
    AS_52(0x1)

    label("loc_2EF6")

    ForeachTarget("loc_2F0B")
    Jc(0x4, 0x2, 0x100, "loc_2F07")
    AS_53(0x1)
    Jump("loc_2F0B")

    label("loc_2F07")

    NextTarget()
    Jump("loc_2EF6")

    label("loc_2F0B")

    ResetTarget()
    ResetTarget()
    AS_83(0x0)
    Jc(0x5, 0x1, 0x1, "loc_2F2D")
    AS_8D(0x7, 0xFC, 0x1F4, 0x1F4, 0x1F4)
    Jump("loc_2F3F")

    label("loc_2F2D")

    AS_8D(0x7, 0xFC, 0x12C, 0x12C, 0x12C)

    label("loc_2F3F")

    Sleep(4100)
    Yield()
    AS_5F(0xFC, 0x0)
    SetCameraDegree(180, -2, 0, 1500)
    Sleep(400)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x2, 0x0, 0, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 4)
    SetCameraDistance(20000, 1000)
    Sleep(500)
    Yield()
    LockCamera(0xF3, 0, 1600, -8500, 2000)
    SetCameraDegree(180, 0, 0, 2000)
    SetCameraDistance(38000, 2000)
    Sleep(1000)
    Yield()
    StopEffect(0xFF, 0x2)
    CancelEffect(0xFF, 0x3)
    PlayEffect(0xFF, 0xF3, 0x1, 0x0, 0, 0, -9500, 0, 0, 0, 1000, 1000, 1000, 3)
    SetCameraDistance(40000, 3500)
    SetCameraDegree(205, -10, 0, 3500)
    AS_A6(0xFF, 0x3, 0x4B0, 0x3E8, 0x0)
    Sleep(3200)
    Yield()
    SoundEx(173, 0x0)
    AS_43(0x0, 0x1F4, 0xFFFFFFFF)
    Sleep(1000)
    Yield()
    EndChrThread(0xFC, 1)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    Call("loc_1D5")
    AS_6E(0x40000)
    Fade(0x1, 500, 0x0)
    AS_7A(0x1)
    ShowChr(0xFF, 0)
    AS_5F(0xF7, 0x0)
    ResetBrightness(0)
    SetBrightness(0x0, 0x1, 0)
    AS_31(0x17, 0x0)
    AS_31(0x3, 0x0)
    Call("loc_2")
    AS_8F(0x0)
    AS_31(0x17, 0x3E8)
    Return()

    # 堕天使暗翼 end

    def Craft_37_55_3063(): pass

    label("Craft_37_55_3063")

    Return()

    # Craft_37_55_3063 end

    def Craft_38_56_3064(): pass

    label("Craft_38_56_3064")

    Return()

    # Craft_38_56_3064 end

    def Craft_39_57_3065(): pass

    label("Craft_39_57_3065")

    Jump("Craft_11_17_D69")

    # Craft_39_57_3065 end

    def Craft_刹那之符文(): pass

    label("刹那之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg058_00.eff")
    LoadEffect(0x3B, "battle\\mg058_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg058_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    # 刹那之符文 end

    def Craft_暗物质(): pass

    label("暗物质")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg060_00.eff")
    AS_78(0)
    Sleep(400)
    Yield()
    LockCamera(0xFB, 0, 1000, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_3D(100, 100, 100, 1400)
    Sleep(1000)
    Yield()
    AS_8D(0x9, 0x3, 0x7D0, 0x0, 0x0)
    AS_8D(0x7, 0xFC, 0x3E8, 0x384, 0x3E8)
    Sleep(300)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x320, 0x3E8)
    Sleep(300)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x384, 0x3E8)
    Sleep(300)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x320, 0x3E8)
    Sleep(300)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x2BC, 0x3E8)
    Sleep(200)
    Yield()
    AS_52(0x5)

    label("loc_31AC")

    Jc(0x5, 0x3, 0x0, "loc_31E6")
    AS_8D(0x7, 0xFC, 0x3E8, 0x258, 0x3E8)
    Sleep(100)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x1F4, 0x3E8)
    Sleep(100)
    Yield()
    AS_53(0x1)
    Jump("loc_31AC")

    label("loc_31E6")

    CancelEffect(0xFF, 0x2)
    AS_8D(0xA, 0x0, 0x0, 0x0, 0x0)
    Call("loc_2")
    AS_8D(0x7, 0xFC, 0x3E8, 0x2BC, 0x3E8)
    Sleep(100)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x384, 0x3E8)
    Sleep(100)
    Yield()
    AS_8D(0x7, 0xFC, 0x3E8, 0x3E8, 0x3E8)
    AS_3D(200, 200, 200, 500)
    WaitEffect(0xFF, 0x2)
    FreeEffect(0x0)
    Return()

    # 暗物质 end

    def Craft_光子飞射(): pass

    label("光子飞射")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg061_00.eff")
    AS_78(0)
    SoundEx(199, 0x0)
    Sleep(250)
    Yield()
    PlayEffect(0xFF, 0xF9, 0x0, 0x4, 0, 0, 500, 0, 0, 0, 800, 800, 800, -1)
    Sleep(1000)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 300)
    Sleep(200)
    Yield()
    DamageCue(0xFE)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 光子飞射 end

    def Craft_大灾变(): pass

    label("大灾变")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg062_00.eff")
    LoadEffect(0x1, "battle\\mg062_01.eff")
    AS_78(0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 28, 20)
    Sleep(600)
    Yield()
    AS_3D(500, 500, 500, 1800)
    SoundEx(247, 0x0)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x0, 0x4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1000)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    Sleep(500)
    Yield()
    Jc(0x16, 0x1, 0x0, "loc_3347")
    LockCamera(0xFF, 0, -3500, 0, 500)
    Jump("loc_335A")

    label("loc_3347")

    ForeachTarget("loc_335A")
    LockCamera(0xFC, 0, -3500, 0, 500)

    label("loc_335A")

    Sleep(400)
    Yield()
    SetBrightness(0x0, 0x0, 300)
    Fade(0x1, 300, 0x0)
    CancelBlur(200)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    FreeEffect(0x0)
    CancelEffect(0xFF, 0x4)
    AS_60(0xF7)
    AS_5F(0xFC, 0x0)
    AS_8D(0xF, 0x0, 0x0, 0x0, 0x0)
    AS_03(0xFC, 0xB4)
    LockCamera(0xFD, 0, 0, 0, 0)
    SetCameraDegree(25, 35, 0, 0)
    Sleep(100)
    Yield()
    SetCameraDistance(26000, 300)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SetCameraDistance(30000, 1000)
    Sleep(1000)
    Yield()
    Fade(0x1, 400, 0x0)
    SetCameraDistance(18000, 200)
    CancelBlur(200)
    Sleep(200)
    Yield()
    BlurSwitch(0xC8, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(25000, 3000)
    Sleep(500)
    Yield()
    AS_3D(300, 300, 200, 5500)
    Sleep(1500)
    Yield()
    AS_B0(0x8, 0x9C4)
    Sleep(1200)
    Yield()
    SetCameraDegree(25, 35, -7, 0)
    Sleep(800)
    Yield()
    AS_60(0xF7)
    Sleep(2500)
    Yield()
    Fade(0x1, 500, 0x0)
    CancelBlur(500)
    ResetBrightness(0)
    SetBrightness(0x0, 0x1, 0)
    AS_31(0x17, 0x0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0, 22, 32)
    AS_8D(0xA, 0x0, 0x0, 0x0, 0x0)
    AS_0A(0xFC, 0x1, 0x0, 0x0)
    AS_7A(0x1)
    AS_5F(0xF7, 0x1)
    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 500, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFF, 0, 0, 0, 0)
    Return()

    # 大灾变 end

    def Craft_金耀辉环(): pass

    label("金耀辉环")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg063_00.eff")
    LoadEffect(0x1, "battle\\mg063_01.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xFB, 0, 0, 0, 600)
    SetCameraDistance(18700, 1000)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 550, 550, 550, -1)
    PlayEffect(0xFF, 0xFB, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 550, 550, 550, -1)
    Sleep(800)
    Yield()
    Sleep(700)
    Yield()
    AS_B0(0x15, 0x7D0)
    LockCamera(0xFB, 0, 1200, 0, 2400)
    SetCameraDistance(21000, 2400)
    Sleep(3000)
    Yield()
    Fade(0x1, 500, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Sleep(800)
    Yield()
    CancelBlur(500)
    Call("loc_2")
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    Return()

    # 金耀辉环 end

    def Craft_天劫轮回光(): pass

    label("天劫轮回光")

    AS_78(1)
    LoadEffect(0x0, "battle\\mg064_00.eff")
    LoadEffect(0x1, "battle\\mg064_01.eff")
    LoadEffect(0x2, "battle\\mg064_02.eff")
    LoadEffect(0x3, "battle\\mg064_03.eff")
    LoadEffect(0x4, "battle\\mg064_04.eff")
    LoadEffect(0x5, "battle/sc036000.eff")
    LoadEffect(0x6, "battle/ms00001.eff")
    LoadEffect(0x7, "battle\\mg064_05.eff")
    AS_78(0)
    ResetTarget()
    Call("loc_17D")
    ClearChipModeFlags(0x0, 0xFC, 0x1)
    AS_3E(0x1F4, 0x0)
    AS_5F(0xFC, 0x0)
    AS_8D(0xB, 0x0, 0x0, 0x0, 0x0)
    LockCamera(0xF3, 0, 0, 0, 0)
    SetCameraDegree(138, 39, 0, 0)
    SetCameraDistance(21000, 0)
    AS_AC(0x3E8, 0xFFFFFFFF)
    LockCamera(0xF3, 0, 1500, 0, 3500)
    SetCameraDistance(17500, 3500)
    SetCameraDegree(0, -5, 10, 3000)
    PlayEffect(0xFF, 0xFF, 0x5, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    SetEffectColor(0xFF, 129, 0xFFFCDE69)
    Sleep(700)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x4, 0x0, 0, 3000, 0, 0, 0, 0, 400, 400, 400, 3)
    SoundEx(359, 0x1)
    Sleep(800)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x3, 0x0, 0, 4000, 10000, 0, 0, 0, 1100, 1100, 1100, -1)
    Sleep(1500)
    Yield()
    CancelEffect(0xFF, 0x3)
    StopSound(359)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x6, 0x0, 0, 4000, 10000, 0, 0, 0, 1800, 1800, 1800, -1)
    SetEffectColor(0xFF, 129, 0xFFDD71F9)
    CancelEffect(0xFF, 0x4)
    Sleep(1500)
    Yield()
    SetBattleSpeed(850)
    PlayEffect(0xFF, 0xF3, 0x0, 0x0, 0, 4000, 9500, 0, 0, 0, 500, 500, 500, 2)
    SetCameraDistance(19000, 2200)
    SetBattleSpeed(650)
    Sleep(2600)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x1, 0x0, 0, 4000, 10000, 0, 0, 0, 400, 400, 400, -1)
    Sleep(200)
    Yield()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    ResetTarget()

    label("loc_37D8")

    ForeachTarget("loc_3802")

    def lambda_37DF():
        ChrMove(0xFF, 0xF3, 0, 3500, 10000, 3000, 0x0)
        Return()

    QueueWorkItem(0xFE, 1, lambda_37DF)
    BeginChrThread(0xFE, 3, "loc_393C", 0x0)
    Sleep(30)
    Yield()
    NextTarget()
    Jump("loc_37D8")

    label("loc_3802")

    Sleep(2300)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x7, 0x0, 0, 3500, 9500, 0, 0, 0, 500, 500, 500, 2)
    Sleep(2000)
    Yield()
    AS_A8(0x0, 0x3)
    Sleep(400)
    Yield()
    AS_A8(0x0, 0x1)
    PlayEffect(0xFF, 0xF3, 0x5, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SetEffectColor(0xFF, 129, 0xFFFCDE69)
    SoundEx(359, 0x1)
    AS_A6(0xFF, 0x2, 0x2EE, 0x640, 0x0)
    SoundEx(269, 0x0)
    CancelBlur(1000)
    Sleep(500)
    Yield()
    StopSound(359)
    SetBattleSpeed(1000)
    PlayEffect(0xFF, 0xF3, 0x6, 0x0, 0, 4000, 10000, 0, 0, 0, 3000, 3000, 3000, -1)
    SoundEx(566, 0x0)
    Sleep(100)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x2, 0x0, 0, 3500, 9500, -20, 0, 0, 750, 750, 750, 3)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    SetCameraDistance(4000, 2000)
    AS_3E(0x3E8, 0x7D0)
    SetBattleSpeed(800)
    SoundEx(220, 0x0)
    Sleep(1000)
    Yield()
    CancelEffect(0xFF, 0x2)
    Sleep(1000)
    Yield()
    CancelBlur(1000)
    AS_43(0x0, 0x1F4, 0xFFFFFFFF)
    Sleep(1000)
    Yield()
    SetBattleSpeed(1000)
    AS_8D(0xA, 0x0, 0x0, 0x0, 0x0)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    AS_A8(0x0, 0x4)
    AS_A8(0x0, 0x5)
    AS_A8(0x0, 0x6)
    AS_A8(0x0, 0x7)
    Call("loc_1D5")
    AS_6E(0x40000)
    Call("loc_1A3")
    EndChrThread(0xFC, 1)
    Call("loc_1CA")
    Return()

    label("loc_393C")

    AS_8D(0x7, 0xFF, 0x3B6, 0x3B6, 0x3B6)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x384, 0x384, 0x384)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x352, 0x352, 0x352)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x320, 0x320, 0x320)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x2EE, 0x2EE, 0x2EE)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x2BC, 0x2BC, 0x2BC)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x28A, 0x28A, 0x28A)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x258, 0x258, 0x258)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x226, 0x226, 0x226)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x1F4, 0x1F4, 0x1F4)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x1C2, 0x1C2, 0x1C2)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x190, 0x190, 0x190)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x15E, 0x15E, 0x15E)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x12C, 0x12C, 0x12C)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0xFA, 0xFA, 0xFA)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0xC8, 0xC8, 0xC8)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x96, 0x96, 0x96)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x64, 0x64, 0x64)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x32, 0x32, 0x32)
    Sleep(150)
    Yield()
    AS_8D(0x7, 0xFF, 0x0, 0x0, 0x0)
    Sleep(150)
    Yield()
    Return()

    # 天劫轮回光 end

    def Craft_41_65_3AF5(): pass

    label("Craft_41_65_3AF5")

    Return()

    # Craft_41_65_3AF5 end

    def Craft_42_66_3AF6(): pass

    label("Craft_42_66_3AF6")

    Return()

    # Craft_42_66_3AF6 end

    def Craft_43_67_3AF7(): pass

    label("Craft_43_67_3AF7")

    Jump("Craft_11_17_D69")

    # Craft_43_67_3AF7 end

    def Craft_震天之符文(): pass

    label("震天之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg068_00.eff")
    LoadEffect(0x3B, "battle\\mg068_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg068_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    # 震天之符文 end

    def Craft_混沌烙印(): pass

    label("混沌烙印")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg070_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 750, 750, 750, -1)
    Sleep(600)
    Yield()
    LockCamera(0xFE, 0, 1000, 0, 600)
    Sleep(3000)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 300)
    AS_3D(300, 300, 300, 200)
    Sleep(200)
    Yield()
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 混沌烙印 end

    def Craft_幻影之塔(): pass

    label("幻影之塔")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg071_00.eff")
    LoadEffect(0x1, "battle\\mg071_01.eff")
    LoadEffect(0x2, "battle\\mg071_02.eff")
    AS_78(0)
    AS_43(0x0, 0x258, 0xFF000000)
    LockCamera(0xFB, 0, 3000, 0, 600)
    Sleep(600)
    Yield()
    SetBrightness(0x0, 0x0, 0)
    Fade(0x0, 500, 0xFF000000)
    AS_60(0xF7)
    LockCamera(0xFB, 0, 3000, 0, 0)
    SetCameraDegree(0, 10, 3, 0)
    SetCameraDistance(25000, 0)
    Sleep(300)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    LockCamera(0xFB, 0, 2000, 0, 0)
    Sleep(1000)
    Yield()
    SetCameraDistance(18000, 2400)
    AS_3D(100, 100, 100, 3000)
    Sleep(400)
    Yield()
    LockCamera(0xFB, 0, 14000, -4000, 2800)
    SetCameraDegree(15, -15, 5, 1800)
    SetCameraDistance(30000, 1500)
    Sleep(900)
    Yield()
    AS_43(0x0, 0x320, 0xFFFFFFFF)
    Sleep(800)
    Yield()
    Fade(0x1, 500, 0xFFFFFFFF)
    Sleep(150)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x2, 0x0, 0, 18000, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    Sleep(1250)
    Yield()
    LockCamera(0xFB, 0, 18000, -2000, 2000)
    Sleep(1000)
    Yield()
    AS_43(0x0, 0x1F4, 0x0)
    Sleep(500)
    Yield()
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    FreeEffect(0x0)
    FreeEffect(0x2)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    AS_B0(0xA, 0x0)
    LockCamera(0xFB, 0, 4000, 0, 0)
    LockCamera(0xFB, 0, 0, 0, 4000)
    SetCameraDistance(30000, 0)
    SetCameraDistance(25000, 3000)
    AS_5F(0xFC, 0x0)
    PlayEffect(0xFF, 0xFB, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(100)
    Yield()
    AS_3D(100, 100, 100, 2000)
    Sleep(500)
    Yield()
    AS_B0(0x14, 0xBB8)
    Sleep(1500)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    Sleep(1000)
    Yield()
    SetBattleSpeed(700)
    Sleep(200)
    Yield()
    SetBattleSpeed(500)
    AS_43(0x0, 0x12C, 0xFFFFFFFF)
    Sleep(400)
    Yield()
    SetBattleSpeed(1000)
    CancelBlur(200)
    Fade(0x1, 300, 0xFFFFFFFF)
    ResetBrightness(0)
    AS_31(0x17, 0x0)
    CancelBlur(0)
    SetBrightness(0x0, 0x1, 0)
    AS_5F(0xF7, 0x1)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0, 22, 32)
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    Sleep(500)
    Yield()
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    LockCamera(0xF2, 0, 0, 0, 0)
    Return()

    # 幻影之塔 end

    def Craft_天国之门(): pass

    label("天国之门")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg072_00.eff")
    LoadEffect(0x1, "battle\\mg072_01.eff")
    LoadEffect(0x2, "battle\\mg072_02.eff")
    AS_78(0)
    Sleep(300)
    Yield()
    LockCamera(0xFF, 0, 1500, 0, 600)
    SetBrightness(0x0, 0x0, 500)
    Sleep(500)
    Yield()
    Fade(0x1, 300, 0x0)
    AS_60(0xF7)
    SetCameraDegree(-45, 17, 0, 0)
    LockCamera(0xF3, 0, 40000, 0, 0)
    SetCameraDistance(27500, 0)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x0, 0x0, 0, 40000, 0, 180, 0, 0, 1000, 1000, 1000, 4)
    LockCamera(0xF3, 0, 41000, 0, 1000)
    PlayEffect(0xFF, 0xF3, 0x2, 0x0, 0, 38000, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    Sleep(2500)
    Yield()
    Fade(0x1, 300, 0x0)
    SetCameraDegree(0, 8, 0, 0)
    SetCameraDistance(24000, 0)
    Sleep(1200)
    Yield()
    SetCameraDistance(35000, 1000)
    AS_B0(0xFFFD, 0x5DC)
    Sleep(1200)
    Yield()
    AS_43(0x0, 0x258, 0x0)
    ResetBrightness(500)
    Fade(0x1, 600, 0x0)
    CancelEffect(0xFF, 0x4)
    CancelEffect(0xFF, 0x3)
    FreeEffect(0x0)
    FreeEffect(0x2)
    LockCamera(0xF3, 0, 3000, 0, 0)
    AS_31(0x17, 0x0)
    AS_3A(0x23, 0x0)
    AS_B0(0x23, 0x0)
    SetCameraDistance(28000, 0)
    AS_5F(0xF7, 0x0)
    AS_3A(0xFFDD, 0x1194)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xF3, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    AS_B0(0x14, 0xDAC)
    LockCamera(0xF3, 0, 0, 0, 3300)
    Sleep(3300)
    Yield()
    SetCameraDistance(32000, 300)
    AS_B0(0x20, 0x12C)
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    SetBrightness(0x0, 0x1, 0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xF4, 0, 0, 0, 0)
    AS_5F(0xF7, 0x1)
    Return()

    # 天国之门 end

    def Craft_银色荆刺(): pass

    label("银色荆刺")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg073_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 900, 900, 900, -1)
    Sleep(600)
    Yield()
    LockCamera(0xFE, 0, 1000, 0, 600)
    Sleep(3000)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 300)
    Sleep(200)
    Yield()

    label("loc_40A7")

    ForeachTarget("loc_40B8")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("loc_40A7")

    label("loc_40B8")

    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 银色荆刺 end

    def Craft_幻银方舟炮(): pass

    label("幻银方舟炮")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg074_00.eff")
    LoadEffect(0x1, "battle\\mg074_01.eff")
    LoadEffect(0x2, "battle\\mg074_02.eff")
    LoadEffect(0x3, "battle\\mg074_03.eff")
    LoadEffect(0x4, "battle\\com000.eff")
    LoadEffect(0x5, "battle\\mg074_04.eff")
    LoadEffect(0x6, "battle\\mg074_05.eff")
    LoadEffect(0x7, "battle\\mg074_06.eff")
    AS_8E(0x1, 0x0, "ef_ship")
    AS_8E(0x7, 0x0, 0xFFFFFF, 0x0, 0x0, 0x0)
    AS_78(0)
    Call("loc_17D")
    AS_3E(0xFA, 0x0)
    AS_AC(0x7D0, 0xFFFFFFFF)
    Fade(0x1, 500, 0x0)
    SetBattleSpeed(700)
    AS_34()
    LockCamera(0xFD, 0, 2000, 10000, 0)
    SetCameraDegree(35, 0, 0, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(20000, 3500)
    SetCameraDegree(45, -15, 0, 4500)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    Sleep(300)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 2000, 10000, -20, 0, 0, 1000, 1000, 1000, 2)
    SoundEx(359, 0x1)
    Sleep(500)
    Yield()
    SetBattleSpeed(850)
    Sleep(4500)
    Yield()
    SoundEx(239, 0x0)
    AS_34()
    LockCamera(0xFD, 700, 700, 4200, 1200)
    SetCameraDegree(7, -23, -10, 1500)
    SetCameraDistance(28500, 1500)
    StopSound(359)
    Sleep(2000)
    Yield()
    SetBattleSpeed(1000)
    Fade(0x1, 500, 0x0)
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    AS_34()
    LockCamera(0xFD, -300, 700, 200, 0)
    SetCameraDegree(227, -4, 0, 0)
    SetCameraDistance(6000, 0)
    AS_3E(0x258, 0x0)
    LockCamera(0xFD, -300, 0, 200, 3000)
    SetCameraDegree(233, -23, 0, 3000)
    SetCameraDistance(7500, 3000)
    PlayEffect(0xFF, 0xFD, 0x5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    AS_1A(0xFF, 0x3, 0x1A2C)
    SoundEx(239, 0x0)
    Sleep(4500)
    Yield()
    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x3)
    Fade(0x1, 500, 0x0)
    AS_3E(0x1F4, 0x0)
    AS_5F(0xFC, 0x0)
    AS_34()
    LockCamera(0xF2, 0, 500, 0, 0)
    SetCameraDegree(45, 20, 0, 0)
    SetCameraDistance(26000, 0)
    AS_3E(0x1F4, 0x0)
    SetCameraDegree(90, 20, 0, 4000)
    SetCameraDistance(29000, 4000)
    AS_3E(0x320, 0xFA0)
    AS_8E(0x7, 0x0, 0xFFFFFF, 0x0, 0x0, 0x0)
    StopEffect(0xFF, 0x3)
    StopEffect(0xFF, 0x6)
    AS_A8(0x0, 0x2)
    PlayEffect(0xFF, 0xF2, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 900, 900, 900, -1)
    Sleep(650)
    Yield()
    BeginChrThread(0xFF, 3, "loc_475F", 0x0)
    Sleep(2500)
    Yield()
    EndChrThread(0xFF, 3)
    AS_A8(0x0, 0x3)
    Fade(0x1, 800, 0x0)
    AS_8E(0x7, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    AS_8E(0x6, 0x0, 0xC8, 0x0, 0x0, 0x0)
    AS_8E(0x2, 0x0, 0x15E, 0x0, 0x0, 0x0)
    AS_8E(0xB, 0x0, 0x4B0, 0x3E8, 0x3E8, 0x0)
    AS_60(0xFC)
    SoundEx(239, 0x0)
    PlayEffect(0xFF, 0xFD, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 3)
    AS_1A(0xFF, 0x3, 0x2EE0)
    AS_34()
    LockCamera(0xFD, 0, 800, 20900, 0)
    SetCameraDegree(185, -4, -1, 0)
    SetCameraDistance(3700, 0)
    AS_3E(0x3E8, 0x0)
    AS_AC(0x3E8, 0xFFFFFFFF)
    LockCamera(0xFD, -600, 1100, 20200, 3300)
    SetCameraDegree(252, -8, -11, 3300)
    SetCameraDistance(3200, 3300)
    Sleep(2500)
    Yield()
    SetBattleSpeed(850)
    Play3DEffect(0xFF, 0xEF, "Null_right01", 0x2, 0x1, 0, -50, -70, 0, 80, 0, 250, 250, 250, -1)
    Play3DEffect(0xFF, 0xEF, "Null_left01", 0x2, 0x1, 0, -50, -70, 0, 280, 0, 250, 250, 250, -1)
    SoundEx(258, 0x0)
    Sleep(100)
    Yield()
    Play3DEffect(0xFF, 0xEF, "Null_right02", 0x2, 0x1, 0, -50, 0, 0, 90, 0, 250, 250, 250, -1)
    Play3DEffect(0xFF, 0xEF, "Null_left02", 0x2, 0x1, 0, -50, 0, 0, 270, 0, 250, 250, 250, -1)
    Sleep(100)
    Yield()
    Play3DEffect(0xFF, 0xEF, "Null_right03", 0x2, 0x1, 0, -50, 0, 0, 95, 0, 250, 250, 250, -1)
    Play3DEffect(0xFF, 0xEF, "Null_left03", 0x2, 0x1, 0, -50, 0, 0, 265, 0, 250, 250, 250, -1)
    Sleep(1000)
    Yield()
    SetBattleSpeed(1200)
    LockCamera(0xFD, -1000, 600, 19900, 1200)
    SetCameraDistance(6500, 1200)
    SetCameraDegree(258, -16, -17, 1200)
    SoundEx(321, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(1500)
    Yield()
    CancelBlur(500)
    StopEffect(0xFF, 0x3)
    StopEffect(0xFF, 0x6)
    AS_A8(0x0, 0x2)
    Fade(0x1, 500, 0x0)
    SetBattleSpeed(1000)
    AS_3E(0x1F4, 0x0)
    AS_8E(0x7, 0x0, 0xFFFFFF, 0x0, 0x0, 0x0)
    AS_34()
    LockCamera(0xFD, -13500, 42000, -9900, 0)
    SetCameraDegree(50, -3, 0, 0)
    SetCameraDistance(14000, 0)
    AS_3E(0x1F4, 0x0)
    SetCameraDegree(50, 20, 0, 1000)
    LockCamera(0xFD, -13500, 45000, -9900, 1000)
    Sleep(200)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    PlayEffect(0xFF, 0xF2, 0x7, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    Sleep(350)
    Yield()
    CancelEffect(0xFF, 0x2)
    SetBattleSpeed(700)
    Sleep(700)
    Yield()
    AS_A8(0x0, 0x7)
    Fade(0x1, 500, 0x0)
    AS_3E(0x1F4, 0x0)
    AS_5F(0xFC, 0x0)
    AS_34()
    LockCamera(0xF2, 0, 8000, 0, 0)
    SetCameraDegree(45, 3, 0, 0)
    SetCameraDistance(22000, 0)
    AS_3E(0x1F4, 0x0)
    SetCameraDegree(90, 20, 0, 2500)
    LockCamera(0xF2, 0, 1500, 0, 1500)
    Sleep(500)
    Yield()
    AS_3E(0x320, 0x9C4)
    StopEffect(0xFF, 0x3)
    StopEffect(0xFF, 0x6)
    AS_A8(0x0, 0x2)
    Sleep(200)
    Yield()
    SetBattleSpeed(1000)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0xFF, 0xF2, 0x6, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(500)
    Yield()
    SetCameraDistance(25000, 2000)
    BeginChrThread(0xFF, 3, "loc_475F", 0x0)
    Sleep(2500)
    Yield()
    AS_43(0x0, 0x1F4, 0xFFFFFFFF)
    Sleep(1000)
    Yield()
    CancelBlur(500)
    EndChrThread(0xFF, 2)
    EndChrThread(0xFF, 3)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    AS_A8(0x0, 0x4)
    AS_A8(0x0, 0x5)
    AS_A8(0x0, 0x6)
    AS_A8(0x0, 0x7)
    Call("loc_1D5")
    AS_8E(0x4, 0x0, 0x0, 0x0, 0x0, 0x0)
    AS_6E(0x40000)
    Call("loc_1A3")
    Call("loc_1CA")
    Return()

    label("loc_475F")

    AS_3D(200, 200, 200, 500)
    BeginChrThread(0xFF, 2, "loc_37", 0x0)
    WaitChrThread(0xFF, 2)
    Yield()
    Jump("loc_475F")

    # 幻银方舟炮 end

    def Craft_4B_75_4774(): pass

    label("Craft_4B_75_4774")

    Return()

    # Craft_4B_75_4774 end

    def Craft_4C_76_4775(): pass

    label("Craft_4C_76_4775")

    Return()

    # Craft_4C_76_4775 end

    def Craft_4D_77_4776(): pass

    label("Craft_4D_77_4776")

    Jump("Craft_11_17_D69")

    # Craft_4D_77_4776 end

    def Craft_幻影之符文(): pass

    label("幻影之符文")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg078_00.eff")
    LoadEffect(0x3B, "battle\\mg078_01.eff")
    LoadEffect(0x3C, "battle\\mg018_02.eff")
    LoadEffect(0x3D, "battle\\mg078_03.eff")
    AS_78(0)
    Call("loc_17D")
    Call("loc_BE6")
    Return()

    # 幻影之符文 end

    def Craft_大地治愈(): pass

    label("大地治愈")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg080_00.eff")
    AS_78(0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(200, 20, 30)
    Sleep(600)
    Yield()

    label("loc_4806")

    ForeachTarget("loc_4831")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4806")

    label("loc_4831")

    Sleep(1450)
    Yield()
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 大地治愈 end

    def Craft_结晶防护(): pass

    label("结晶防护")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg081_00.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1800)
    Yield()
    DamageCue(0xFE)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 结晶防护 end

    def Craft_结晶防护复(): pass

    label("结晶防护·复")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x1, "battle\\mg082_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()

    label("loc_48C1")

    ForeachTarget("loc_48EC")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    DamageCue(0xFE)
    NextTarget()
    Jump("loc_48C1")

    label("loc_48EC")

    AS_14(0x1)
    FreeEffect(0x1)
    Return()

    # 结晶防护·复 end

    def Craft_坚韧守护(): pass

    label("坚韧守护")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg083_00.eff")
    LoadEffect(0x1, "battle\\mg083_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(950)
    Yield()

    label("loc_4958")

    ForeachTarget("loc_4981")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4958")

    label("loc_4981")

    Sleep(2600)
    Yield()
    ResetTarget()

    label("loc_4986")

    ForeachTarget("loc_4993")
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4986")

    label("loc_4993")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 坚韧守护 end

    def Craft_54_84_499B(): pass

    label("Craft_54_84_499B")

    Return()

    # Craft_54_84_499B end

    def Craft_55_85_499C(): pass

    label("Craft_55_85_499C")

    Return()

    # Craft_55_85_499C end

    def Craft_56_86_499D(): pass

    label("Craft_56_86_499D")

    Return()

    # Craft_56_86_499D end

    def Craft_57_87_499E(): pass

    label("Craft_57_87_499E")

    Return()

    # Craft_57_87_499E end

    def Craft_强音之力(): pass

    label("强音之力")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg088_00.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    SoundEx(197, 0x0)
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 强音之力 end

    def Craft_强音之力复(): pass

    label("强音之力·复")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x1, "battle\\mg088_00.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()

    label("loc_4A24")

    ForeachTarget("loc_4A51")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(197, 0x0)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4A24")

    label("loc_4A51")

    AS_14(0x1)
    FreeEffect(0x1)
    Return()

    # 强音之力·复 end

    def Craft_振奋之激(): pass

    label("振奋之激")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg090_00.eff")
    LoadEffect(0x1, "battle\\mg090_01.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    SoundEx(201, 0x0)
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1350)
    Yield()

    label("loc_4AC5")

    ForeachTarget("loc_4AF2")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(202, 0x0)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4AC5")

    label("loc_4AF2")

    Sleep(800)
    Yield()
    ResetTarget()

    label("loc_4AF7")

    ForeachTarget("loc_4B04")
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4AF7")

    label("loc_4B04")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 振奋之激 end

    def Craft_5B_91_4B0C(): pass

    label("Craft_5B_91_4B0C")

    Return()

    # Craft_5B_91_4B0C end

    def Craft_5C_92_4B0D(): pass

    label("Craft_5C_92_4B0D")

    Return()

    # Craft_5C_92_4B0D end

    def Craft_5D_93_4B0E(): pass

    label("Craft_5D_93_4B0E")

    Return()

    # Craft_5D_93_4B0E end

    def Craft_5E_94_4B0F(): pass

    label("Craft_5E_94_4B0F")

    Return()

    # Craft_5E_94_4B0F end

    def Craft_5F_95_4B10(): pass

    label("Craft_5F_95_4B10")

    Return()

    # Craft_5F_95_4B10 end

    def Craft_生命之息(): pass

    label("生命之息")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg096_00.eff")
    LoadEffect(0x1, "battle\\mg096_01.eff")
    AS_78(0)
    Sleep(125)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(800)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 20)

    label("loc_4B86")

    ForeachTarget("loc_4BB5")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    Sleep(250)
    Yield()
    NextTarget()
    Jump("loc_4B86")

    label("loc_4BB5")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 生命之息 end

    def Craft_圣灵之息(): pass

    label("圣灵之息")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg097_00.eff")
    LoadEffect(0x1, "battle\\mg097_01.eff")
    AS_78(0)
    LockCamera(0xF8, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1000)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(500, 18, 20)

    label("loc_4C2E")

    ForeachTarget("loc_4C5D")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    Sleep(250)
    Yield()
    NextTarget()
    Jump("loc_4C2E")

    label("loc_4C5D")

    Sleep(600)
    Yield()
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 圣灵之息 end

    def Craft_风之精灵(): pass

    label("风之精灵")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg098_00.eff")
    LoadEffect(0x1, "battle\\mg098_01.eff")
    AS_78(0)
    LockCamera(0xF4, 0, 1000, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xF2, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(500)
    Yield()
    LockCamera(0xF4, 0, 0, 0, 1500)
    Sleep(4000)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 20)
    Sleep(1000)
    Yield()
    ResetTarget()

    label("loc_4CF3")

    ForeachTarget("loc_4D22")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(234, 0x0)
    Sleep(200)
    Yield()
    DamageCue(0xFE)
    NextTarget()
    Jump("loc_4CF3")

    label("loc_4D22")

    WaitEffect(0xFF, 0x4)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 风之精灵 end

    def Craft_大治愈术(): pass

    label("大治愈术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg099_00.eff")
    LoadEffect(0x1, "battle\\mg099_01.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFB, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x1, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1200)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 20)
    ResetTarget()

    label("loc_4DA1")

    ForeachTarget("loc_4DCA")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4DA1")

    label("loc_4DCA")

    BeginChrThread(0xFF, 3, "loc_15", 0x0)
    WaitChrThread(0xFF, 3)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 大治愈术 end

    def Craft_精灵之歌(): pass

    label("精灵之歌")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg100_00.eff")
    LoadEffect(0x1, "battle\\mg100_01.eff")
    LoadEffect(0x2, "battle\\mg100_02.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    Sleep(600)
    Yield()
    Fade(0x1, 500, 0x0)
    AS_60(0xF7)
    SetBrightness(0x0, 0x0, 300)
    AS_34()
    SetCameraDegree(35, 25, 0, 0)
    SetCameraDistance(20000, 0)
    LockCamera(0xF3, 0, 0, 0, 0)
    PlayEffect(0xFF, 0xF3, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    AS_3D(150, 300, 150, 700)
    Sleep(500)
    Yield()
    LockCamera(0xF3, 0, 4000, 0, 2000)
    Sleep(1500)
    Yield()
    SetCameraDegree(-15, 40, 0, 2500)
    PlayEffect(0xFF, 0xF3, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(2800)
    Yield()
    Fade(0x1, 500, 0x0)
    SetCameraDegree(-100, 25, 0, 0)
    SetCameraDistance(20000, 0)
    LockCamera(0xF3, 0, 5000, -3000, 0)
    SetCameraDegree(20, -20, 0, 2500)
    Sleep(300)
    Yield()
    Sleep(500)
    Yield()
    LockCamera(0xF3, -2000, 0, -2000, 2000)
    SetCameraDistance(30000, 2000)
    Sleep(1000)
    Yield()
    SetBattleSpeed(700)
    Sleep(1000)
    Yield()
    AS_43(0x0, 0x190, 0x0)
    Sleep(400)
    Yield()
    FreeEffect(0x0)
    Fade(0x1, 300, 0x0)
    SetBattleSpeed(1000)
    AS_31(0x17, 0x0)
    ResetBrightness(0)
    AS_5F(0xF7, 0x1)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0, 25, 30)
    ResetTarget()

    label("loc_4F5B")

    ForeachTarget("loc_4F86")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_4F5B")

    label("loc_4F86")

    Sleep(2000)
    Yield()
    CancelBlur(500)
    SetBrightness(0x0, 0x1, 0)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)
    Fade(0x1, 300, 0x0)
    AS_31(0x17, 0x0)
    LockCamera(0xF2, 0, 0, 0, 0)
    Return()

    # 精灵之歌 end

    def Craft_65_101_4FBD(): pass

    label("Craft_65_101_4FBD")

    Return()

    # Craft_65_101_4FBD end

    def Craft_66_102_4FBE(): pass

    label("Craft_66_102_4FBE")

    Return()

    # Craft_66_102_4FBE end

    def Craft_67_103_4FBF(): pass

    label("Craft_67_103_4FBF")

    Return()

    # Craft_67_103_4FBF end

    def Craft_时间减速(): pass

    label("时间减速")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg104_00.eff")
    LoadEffect(0x1, "battle\\mg104_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(3300)
    Yield()
    ResetTarget()

    label("loc_5028")

    ForeachTarget("loc_5055")
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(212, 0x0)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_5028")

    label("loc_5055")

    Sleep(400)
    Yield()
    ResetTarget()

    label("loc_505A")

    ForeachTarget("loc_506B")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_505A")

    label("loc_506B")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 时间减速 end

    def Craft_时间驱动(): pass

    label("时间驱动")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg105_00.eff")
    LoadEffect(0x1, "battle\\mg105_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(3400)
    Yield()

    label("loc_50DA")

    ForeachTarget("loc_5103")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_50DA")

    label("loc_5103")

    Sleep(400)
    Yield()
    ResetTarget()

    label("loc_5108")

    ForeachTarget("loc_5115")
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_5108")

    label("loc_5115")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 时间驱动 end

    def Craft_灾厄之爪(): pass

    label("灾厄之爪")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg106_00.eff")
    LoadEffect(0x1, "battle\\mg106_01.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xF2, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xF2, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(800)
    Yield()
    AS_3D(100, 100, 100, 5000)
    Sleep(1600)
    Yield()
    ResetTarget()

    label("loc_5196")

    ForeachTarget("loc_51BF")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_5196")

    label("loc_51BF")

    Sleep(800)
    Yield()
    AS_3D(250, 250, 250, 200)
    Sleep(900)
    Yield()
    BeginChrThread(0xFF, 3, "loc_2", 0x0)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    Return()

    # 灾厄之爪 end

    def Craft_6B_107_51E1(): pass

    label("Craft_6B_107_51E1")

    Return()

    # Craft_6B_107_51E1 end

    def Craft_6C_108_51E2(): pass

    label("Craft_6C_108_51E2")

    Return()

    # Craft_6C_108_51E2 end

    def Craft_6D_109_51E3(): pass

    label("Craft_6D_109_51E3")

    Return()

    # Craft_6D_109_51E3 end

    def Craft_6E_110_51E4(): pass

    label("Craft_6E_110_51E4")

    Return()

    # Craft_6E_110_51E4 end

    def Craft_6F_111_51E5(): pass

    label("Craft_6F_111_51E5")

    Return()

    # Craft_6F_111_51E5 end

    def Craft_魔导祝福(): pass

    label("魔导祝福")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg112_00.eff")
    LoadEffect(0x1, "battle\\mg112_01.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFB, 0, 600, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(1000)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 20)
    ResetTarget()

    label("loc_525C")

    ForeachTarget("loc_5289")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(228, 0x0)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_525C")

    label("loc_5289")

    Sleep(1000)
    Yield()
    BeginChrThread(0xFF, 3, "loc_15", 0x0)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    Return()

    # 魔导祝福 end

    def Craft_A反射屏障(): pass

    label("A-反射屏障")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg113_00.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 500)
    Sleep(400)
    Yield()
    BeginChrThread(0xFF, 3, "loc_5328", 0x0)
    PlayEffect(0xFF, 0xFE, 0x0, 0x8, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(500)
    Yield()
    Sleep(1200)
    Yield()
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    Sleep(300)
    Yield()
    AS_3D(180, 180, 180, 100)
    CancelBlur(100)
    Sleep(200)
    Yield()
    DamageCue(0xFE)
    WaitChrThread(0xFF, 3)
    WaitEffect(0xFF, 0x4)
    FreeEffect(0x0)
    Return()

    label("loc_5328")

    SoundEx(173, 0x0)
    SoundEx(182, 0x0)
    Sleep(2000)
    Yield()
    SoundEx(190, 0x0)
    Return()

    # A-反射屏障 end

    def Craft_圣灵苏生(): pass

    label("圣灵苏生")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg114_00.eff")
    LoadEffect(0x1, "battle\\mg114_01.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFB, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    AS_3D(100, 100, 100, 300)
    Sleep(1500)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 22)
    ResetTarget()

    label("loc_53B8")

    ForeachTarget("loc_53E1")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(800)
    Yield()
    NextTarget()
    Jump("loc_53B8")

    label("loc_53E1")

    Sleep(2000)
    Yield()
    ResetTarget()

    label("loc_53E6")

    ForeachTarget("loc_53F7")
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_53E6")

    label("loc_53F7")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    Return()

    # 圣灵苏生 end

    def Craft_纯净弧光(): pass

    label("纯净弧光")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg115_00.eff")
    LoadEffect(0x1, "battle\\mg115_01.eff")
    AS_78(0)
    SetBrightness(0x0, 0x0, 1000)
    Sleep(250)
    Yield()
    Fade(0x1, 500, 0x0)
    Sleep(200)
    Yield()
    LockCamera(0xFB, 0, 13000, 0, 0)
    AS_B0(0xFFDD, 0x0)
    Sleep(800)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1000)
    Yield()
    Fade(0x1, 750, 0x0)
    ResetBrightness(500)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    SetCameraDistance(27000, 0)
    AS_B0(0x28, 0x5DC)
    Sleep(1400)
    Yield()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x3)
    AS_3D(200, 200, 200, 1500)
    Sleep(2500)
    Yield()
    CancelBlur(500)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(300, 18, 20)
    SoundEx(186, 0x0)
    ResetTarget()

    label("loc_54DD")

    ForeachTarget("loc_5506")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_54DD")

    label("loc_5506")

    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 3, "loc_15", 0x0)
    SetBrightness(0x0, 0x1, 0)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    WaitChrThread(0xFF, 3)
    Return()

    # 纯净弧光 end

    def Craft_74_116_5520(): pass

    label("Craft_74_116_5520")

    Return()

    # Craft_74_116_5520 end

    def Craft_75_117_5521(): pass

    label("Craft_75_117_5521")

    Return()

    # Craft_75_117_5521 end

    def Craft_76_118_5522(): pass

    label("Craft_76_118_5522")

    Return()

    # Craft_76_118_5522 end

    def Craft_77_119_5523(): pass

    label("Craft_77_119_5523")

    Return()

    # Craft_77_119_5523 end

    def Craft_神圣祝福(): pass

    label("神圣祝福")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg120_00.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(1000)
    Yield()
    DamageCue(0xFE)
    WaitEffect(0xFF, 0x4)
    FreeEffect(0x0)
    Return()

    # 神圣祝福 end

    def Craft_虚空幻域(): pass

    label("虚空幻域")

    AS_78(1)
    LoadEffect(0x0, "battle\\mg121_00.eff")
    AS_78(0)
    Sleep(200)
    Yield()
    LockCamera(0xF4, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    SoundEx(238, 0x0)

    ResetTarget()

    label("虚空幻域_loop")

    ForeachTarget("虚空幻域_loop_end")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    DamageCue(0xFE)
    Yield()
    NextTarget()
    Jump("虚空幻域_loop")

    label("虚空幻域_loop_end")


    ResetTarget()
    WaitEffect(0xFE, 0x4)

    FreeEffect(0x0)
    Return()

    # 虚空幻域 end

    def Craft_狂乱之月(): pass

    label("狂乱之月")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg122_00.eff")
    LoadEffect(0x1, "battle\\mg122_01.eff")
    AS_78(0)
    SetBrightness(0x0, 0x0, 1000)
    Sleep(350)
    Yield()
    Fade(0x1, 800, 0x0)
    LockCamera(0xFB, 0, 30000, 0, 0)
    SetCameraDegree(0, 0, 0, 0)
    SetCameraDistance(14000, 0)
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 30000, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x5)
    Sleep(2800)
    Yield()
    AS_3D(50, 50, 50, 2500)
    SetCameraDistance(17000, 2700)
    Sleep(2300)
    Yield()
    AS_43(0x0, 0x320, 0x0)
    Sleep(800)
    Yield()
    Fade(0x1, 300, 0x0)
    CancelBlur(500)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 0, 0, 0)
    ResetBrightness(300)
    Sleep(300)
    Yield()
    ResetTarget()

    label("loc_56B5")

    ForeachTarget("loc_56E0")
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    DamageCue(0xFE)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("loc_56B5")

    label("loc_56E0")

    Sleep(500)
    Yield()
    WaitEffect(0xFF, 0x4)
    AS_14(0x1)
    Call("loc_1D5")
    SetBrightness(0x0, 0x1, 0)
    Return()

    # 狂乱之月 end

    def Craft_星之守护(): pass

    label("星之守护")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg116_00.eff")
    LoadEffect(0x1, "battle\\mg116_01.eff")
    AS_78(0)
    SetBrightness(0x0, 0x0, 1000)
    ResetTarget()
    Sleep(400)
    Yield()
    Fade(0x1, 800, 0x0)
    LockCamera(0xFB, 0, 9000, 0, 0)
    SetCameraDegree(40, 10, 0, 0)
    SetCameraDistance(20000, 0)
    AS_60(0xF7)
    AS_6D(0x40000)
    Sleep(600)
    Yield()
    SetCameraDegree(0, -30, 0, 2850)
    SetCameraDistance(17000, 3000)
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    SoundEx(359, 0x1)
    Sleep(2050)
    Yield()
    SetCameraDistance(29000, 1000)
    SoundEx(312, 0x0)
    Sleep(850)
    Yield()
    AS_5F(0xF7, 0x1)
    AS_31(0x17, 0x0)
    LockCamera(0xFB, 0, 500, 0, 0)
    SetCameraDegree(70, 15, 0, 0)
    SetCameraDistance(24000, 0)
    SoundEx(186, 0x0)
    LockCamera(0xFB, 0, 0, 0, 1200)
    AS_B0(0x14, 0x4B0)
    AS_0B(0x2D, 0xBB8)
    Sleep(600)
    Yield()
    StopSound(359)
    ResetTarget()

    label("loc_57F2")

    ForeachTarget("loc_581B")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(300)
    Yield()
    NextTarget()
    Jump("loc_57F2")

    label("loc_581B")

    Sleep(1000)
    Yield()
    ResetBrightness(500)
    BeginChrThread(0xFF, 3, "loc_15", 0x0)
    AS_14(0x0)
    WaitEffect(0xFF, 0x4)
    AS_14(0x1)
    Call("loc_1D5")
    SetBrightness(0x0, 0x1, 0)
    Return()

    # 星之守护 end

    def Craft_情报解析(): pass

    label("情报解析")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x1, "battle/mg124_00.eff")
    AS_78(0)
    ResetLookingTargetData()
    LockCamera(0xF8, 0, 0, 0, 1500)
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1500)
    Yield()
    DamageCue(0xFE)
    AS_14(0x1)
    Call("loc_1D5")
    AS_8D(0x4A, 0x0, 0x0, 0x0, 0x0)
    Return()

    # 情报解析 end

    def Craft_7D_125_58A0(): pass

    label("Craft_7D_125_58A0")

    Return()

    # Craft_7D_125_58A0 end

    def Craft_7E_126_58A1(): pass

    label("Craft_7E_126_58A1")

    Return()

    # Craft_7E_126_58A1 end

    def Craft_7F_127_58A2(): pass

    label("Craft_7F_127_58A2")

    Return()

    # Craft_7F_127_58A2 end

    def Craft_回复术(): pass

    label("回复术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg128_00.eff")
    AS_78(0)
    Sleep(125)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    SoundEx(226, 0x0)
    PlayEffect(0xFF, 0xF8, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(2000)
    Yield()
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 回复术 end

    def Craft_中回复术(): pass

    label("中回复术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg129_00.eff")
    AS_78(0)
    Sleep(125)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 600)
    Sleep(700)
    Yield()
    BeginChrThread(0xFF, 3, "loc_5970", 0x0)
    PlayEffect(0xFF, 0xF8, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(2250)
    Yield()
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    WaitChrThread(0xFF, 3)
    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    label("loc_5970")

    SoundEx(226, 0x0)
    Sleep(150)
    Yield()
    SoundEx(221, 0x0)
    Return()

    # 中回复术 end

    def Craft_大回复术(): pass

    label("大回复术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg130_00.eff")
    LoadEffect(0x1, "battle\\mg130_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    BeginChrThread(0xFF, 3, "loc_5A1D", 0x0)
    PlayEffect(0xFF, 0xF8, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1120)
    Yield()
    PlayEffect(0xFF, 0xF8, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(500)
    Yield()
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    WaitChrThread(0xFF, 3)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    label("loc_5A1D")

    SoundEx(227, 0x0)
    Sleep(400)
    Yield()
    SoundEx(226, 0x0)
    Sleep(700)
    Yield()
    SoundEx(228, 0x0)
    Return()

    # 大回复术 end

    def Craft_水之幻影(): pass

    label("水之幻影")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg131_00.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()

    label("loc_5A61")

    ForeachTarget("loc_5A8A")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_5A61")

    label("loc_5A8A")

    Sleep(1500)
    Yield()
    ResetTarget()

    label("loc_5A8F")

    ForeachTarget("loc_5A9C")
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_5A8F")

    label("loc_5A9C")

    AS_14(0x0)
    FreeEffect(0x0)
    Return()

    # 水之幻影 end

    def Craft_封魔领域(): pass

    label("封魔领域")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg132_00.eff")
    LoadEffect(0x1, "battle\\mg132_01.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 500, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1100)
    Yield()

    label("loc_5B08")

    ForeachTarget("loc_5B2D")
    PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    NextTarget()
    Jump("loc_5B08")

    label("loc_5B2D")

    Sleep(1900)
    Yield()
    ResetTarget()

    label("loc_5B32")

    ForeachTarget("loc_5B43")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(200)
    Yield()
    NextTarget()
    Jump("loc_5B32")

    label("loc_5B43")

    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    # 封魔领域 end

    def Craft_中复苏术(): pass

    label("中复苏术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg133_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    BeginChrThread(0xFF, 3, "loc_5BB5", 0x0)
    PlayEffect(0xFF, 0xF8, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(3000)
    Yield()
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    WaitChrThread(0xFF, 3)
    WaitEffect(0xFF, 0x4)
    FreeEffect(0x0)
    Return()

    label("loc_5BB5")

    SoundEx(549, 0x0)
    SoundEx(227, 0x0)
    Sleep(2100)
    Yield()
    SoundEx(230, 0x0)
    Return()

    # 中复苏术 end

    def Craft_复苏术(): pass

    label("复苏术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg134_00.eff")
    AS_78(0)
    Sleep(250)
    Yield()
    LockCamera(0xF8, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    BeginChrThread(0xFF, 3, "loc_5C2D", 0x0)
    PlayEffect(0xFF, 0xF8, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 4)
    Sleep(3000)
    Yield()
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    WaitEffect(0xFF, 0x4)
    FreeEffect(0x0)
    Return()

    label("loc_5C2D")

    SoundEx(183, 0x0)
    SoundEx(186, 0x0)
    Sleep(1800)
    Yield()
    SoundEx(230, 0x0)
    Return()

    # 复苏术 end

    def Craft_全回复术(): pass

    label("全回复术")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg135_00.eff")
    AS_78(0)
    LockCamera(0xFE, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    BeginChrThread(0xFF, 3, "loc_5CA3", 0x0)
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 10, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    Sleep(1620)
    Yield()
    SoundEx(8, 0x0)
    DamageCue(0xFE)
    AS_14(0x0)
    AS_14(0x1)
    Call("loc_1D5")
    Return()

    label("loc_5CA3")

    SoundEx(183, 0x0)
    Sleep(100)
    Yield()
    SoundEx(226, 0x0)
    Sleep(1050)
    Yield()
    SoundEx(178, 0x0)
    Sleep(150)
    Yield()
    SoundEx(228, 0x0)
    Return()

    # 全回复术 end

    def Craft_88_136_5CC0(): pass

    label("Craft_88_136_5CC0")


    # Craft_88_136_5CC0 end

    SaveToFile()

Try(main)
