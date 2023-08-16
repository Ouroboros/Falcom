from BattleMonsterStatus import *

# 敌人

def main():
    Name               = "阿瑞安赫德"
    Description        = "结社『使徒』的第七柱，\\n使用超越人类认知的枪\\n技和S级的幸运，\\n可将任何敌人完全压制。"
    ASFile             = "as90010.dat"
    Symbol             = "sy04200.itp"

    Level              = 999
    MaximumHP          = 118000
    InitialHP          = 118000
    MaximumEP          = 0
    InitialEP          = 0
    MaximumCP          = 200
    InitialCP          = 200

    SPD                = 120
    MoveSPD            = 10
    MOV                = 6
    STR                = 3450
    DEF                = 3114
    ATS                = 2219
    ADF                = 9999
    DEX                = 150
    AGL                = 32
    RNG                = 2

    Unknown_2A         = 0x0
    EXP                = 9999
    Unknown_2E         = 0x0
    Unknown_30         = 0x0
    AIType             = 0x0
    Unknown_33         = 0x3E8
    Unknown_35         = 0x9
    Unknown_36         = 0xA280
    EnemyFlags         = 0x0000
    BattleFlags        = 0x0A04

    Unknown_3C         = 0x1
    Unknown_3E         = 0x0
    Sex                = 9
    Unknown_41         = 0x1
    CharSize           = 0x190
    DefaultEffectX     = 0x0
    DefaultEffectZ     = 0
    DefaultEffectY     = 0x0
    Unknown_52         = 0x60
    Unknown_53         = 0x50
    Unknown_54         = 0xA0
    Unknown_55         = 0xB0
    Resistance         = 0xFFFFFFFF
    AttributeRate      = [ 100, 100, 100, 100, 100, 100, 100 ]
    Sepith             = [ 255, 255, 255, 255, 255, 255, 255 ]
    DropItem           = [ 0x0000, 0x0000 ]
    DropRate           = [ 100, 100 ]
    Equipment          = [ 0x0009, 0x0000, 0x0000, 0x0000, 0x0000 ]
    Orbment            = [ 0x0000, 0x0000, 0x0000, 0x0000 ]

    RunawayType        = 0
    RunawayRate        = 0
    RunawayParam1      = 0
    Reserve1           = 0

    Craft_03E8 = CreateCraft(
                    "",
                    "",
                    0x05, 0x12, 0x15,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.Physical, CraftState.NoneState,
                    0, 0,
                    0, 30,
                    0,
                    0,
                    100, 0,
                    0, 0,
               )

    朗基努斯枪 = CreateCraft(
                    "朗基努斯枪",
                    "据说当年第七柱用这招杀了一个人。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Physical, CraftState.NoneState,
                    50, 50,
                    0, 30,
                    0,
                    5,
                    100, 0,
                    0, 0,
               )

    天地乖离 = CreateCraft(
                    "天地乖离",
                    "用超高速旋转的枪头形成的空间断层将所有敌人送入异次元空间。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.LineOnLocation,
                    CraftState.Physical, CraftState.NoneState,
                    54, 100,
                    0, 70,
                    0,
                    17,
                    200, 0,
                    0, 0,
               )

    疾风轰雷闪 = CreateCraft(
                    "疾风轰雷闪",
                    "突贯攻击",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.LineOnLocationIncludeSelf,
                    CraftState.Physical, CraftState.NoneState,
                    1, 50,
                    0, 30,
                    0,
                    3,
                    60, 0,
                    0, 0,
               )

    大地轰雷锤 = CreateCraft(
                    "大地轰雷锤",
                    "以自身为避雷针，落下轰击整个战场的巨雷。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Arts, CraftState.BanCraft,
                    1, 50,
                    0, 30,
                    0,
                    100,
                    100, 0,
                    100, 3,
               )

    横扫千军 = CreateCraft(
                    "横扫千军",
                    "用横扫攻击将前方的敌人击退。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnSelf,
                    CraftState.Physical, CraftState.Stun,
                    1, 4,
                    0, 30,
                    0,
                    6,
                    100, 0,
                    100, 5,
               )

    圣技大十字 = CreateCraft(
                    "圣技·大十字",
                    " ",
                    0x06, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Physical, CraftState.NoneState,
                    1, 50,
                    0, 30,
                    100,
                    100,
                    325, 0,
                    0, 0,
               )

    摘面具 = CreateCraft(
                    "摘面具",
                    "改",
                    0x05, 0x42, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.Physical, CraftState.NoneState,
                    1, 1,
                    0, 0,
                    0,
                    1,
                    0, 0,
                    0, 0,
               )

    暴雨疾风枪 = CreateCraft(
                    "暴雨疾风枪",
                    "以人类之身无法察觉的速度发出无数的枪把对手刺穿，一切防御\\n在这面前都显得苍白无力。此神技后来流传到某组织的No.3手上。",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnLocationExclude,
                    CraftState.Physical, CraftState.NoneState,
                    50, 10,
                    0, 40,
                    0,
                    4,
                    50, 0,
                    0, 0,
               )


    CraftList = CreateCraftList([
                    Craft_03E8,
                    朗基努斯枪,
                    天地乖离,
                    疾风轰雷闪,
                    大地轰雷锤,
                    横扫千军,
                    圣技大十字,
                    摘面具,
                    暴雨疾风枪,
                ])

    Attack = CreateAI(0x1,  0,    0x8,  0x1,  0x00, 0x05, Craft_03E8,      [0,     0,      1,      0])

    Craft_摘面具         = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x1C, 摘面具,          [50,    255,    0,      0])
    Craft_天地乖离       = CreateAI(0x2,  10,   0x7,  0x1,  0x00, 0x18, 天地乖离,        [30,    1,      1,      0])
    Craft_暴雨疾风枪     = CreateAI(0x2,  10,   0x7,  0x1,  0x00, 0x15, 暴雨疾风枪,      [0,     0,      1,      0])
    Craft_疾风轰雷闪     = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x10, 疾风轰雷闪,      [0,     0,      1,      0])
    Craft_横扫千军       = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x12, 横扫千军,        [0,     0,      1,      0])
    Craft_大地轰雷锤     = CreateAI(0x2,  30,   0x7,  0x1,  0x00, 0x1D, 大地轰雷锤,      [0,     0,      1,      0])

    SCraft_圣技大十字    = CreateAI(0xA,  100,  0x0,  0x1,  0x00, 0x1A, 圣技大十字,      [200,   0,      0,      0])
    SCraft_圣技大十字_2  = CreateAI(0xA,  30,   0x0,  0x1,  0x00, 0x1A, 圣技大十字,      [100,   0,      0,      0])
    SCraft_朗基努斯枪    = CreateAI(0x2,  100,  0x7,  0x1,  0x00, 0x1B, 朗基努斯枪,      [30,    1,      4,      0])

    ArtsAIList         = []
    CraftAIList        = [Craft_摘面具, Craft_天地乖离, Craft_暴雨疾风枪, Craft_疾风轰雷闪, Craft_横扫千军, Craft_大地轰雷锤]
    SCraftAIList       = [SCraft_圣技大十字, SCraft_圣技大十字_2, SCraft_朗基努斯枪]
    SupportCraftAIList = []

    SaveToMS("ms90011.dat", locals())

TryInvoke(main)