from BattleMonsterStatus import *

def main():
    Name               = "小丑肯帕雷拉"
    Description        = "以小丑般形式展开行动\\n的执行者ＮＯ．０，　　\\n操使奇妙的火焰幻术，\\n将敌人迫向绝望。"
    ASFile             = "as90020.dat"
    Symbol             = "sy03600.itp"

    Resistance = CraftConditionFlags.Poison         | \
                 CraftConditionFlags.Frozen         | \
                 CraftConditionFlags.Landification  | \
                 CraftConditionFlags.Sleeping       | \
                 CraftConditionFlags.BanArts        | \
                 CraftConditionFlags.Darkness       | \
                 CraftConditionFlags.BanCraft       | \
                 CraftConditionFlags.Confusion      | \
                 CraftConditionFlags.Stun           | \
                 CraftConditionFlags.OnehitKill     | \
                 CraftConditionFlags.Burning        | \
                 CraftConditionFlags.Rage           | \
                 CraftConditionFlags.Vanish         | \
                 CraftConditionFlags.Reserve_2      | \
                 CraftConditionFlags.GreenPepper    | \
                 CraftConditionFlags.Dead           | \
                 CraftConditionFlags.Str            | \
                 CraftConditionFlags.Def            | \
                 CraftConditionFlags.Ats            | \
                 CraftConditionFlags.Adf            | \
                 CraftConditionFlags.Dex            | \
                 CraftConditionFlags.Agl            | \
                 CraftConditionFlags.Mov            | \
                 CraftConditionFlags.Spd

    Level              = 90
    MaximumHP          = 37170
    InitialHP          = 37170
    MaximumEP          = 60000
    InitialEP          = 60000
    MaximumCP          = 200
    InitialCP          = 180

    SPD                = 120*1
    MoveSPD            = 7
    MOV                = 6
    STR                = 1805
    DEF                = 1727
    ATS                = 1394
    ADF                = 1286
    DEX                = 105
    AGL                = 16
    RNG                = 50

    Unknown_2A         = 0x0
    EXP                = 512
    Unknown_2E         = 0x0
    Unknown_30         = 0x0
    AIType             = 0x0
    Unknown_33         = 0x3E8
    Unknown_35         = 0x9
    Unknown_36         = 0xA280
    EnemyFlags         = 0x0000
    BattleFlags        = 0x0804

    Unknown_3C         = 0x1
    Unknown_3E         = 0x0
    Sex                = 9
    Unknown_41         = 0x0
    CharSize           = 0x190
    DefaultEffectX     = 0x0
    DefaultEffectZ     = 800
    DefaultEffectY     = 0x0
    Unknown_52         = 0x60
    Unknown_53         = 0x50
    Unknown_54         = 0xA0
    Unknown_55         = 0xB0
    AttributeRate      = [ 100, 100, 0, 100, 100, 100, 100 ]
    Sepith             = [ 50, 50, 50, 50, 50, 50, 50 ]
    DropItem           = [ 0x0000, 0x0000 ]
    DropRate           = [ 0, 0 ]
    Equipment          = [ 练习用武器, 0x0000, 0x0000, 0x0000, 0x0000 ]
    Orbment            = [ 0x0000, 0x0000, 0x0000, 0x0000 ]

    RunawayType        = 0
    RunawayRate        = 0
    RunawayParam1      = 0
    Reserve1           = 0

    Craft_03E8 = CreateCraft(
                    "",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.TargetWithoutMove,
                    CraftState.Physical, CraftState.NoneState,
                    1, 100,
                    0, 20,
                    0,
                    100,
                    100, 0,
                    0, 0,
               )

    相位重置 = CreateCraft(
                    "相位重置",
                    "",
                    0x05, 0x92, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.NoneState, CraftState.NoneState,
                    1, 50,
                    0, 10,
                    0,
                    100,
                    0, 0,
                    0, 0,
               )

    置换 = CreateCraft(
                    "置换",
                    "",
                    0x05, 0x42, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnSelf,
                    CraftState.NoneState, CraftState.NoneState,
                    1, 1,
                    0, 10,
                    0,
                    1,
                    0, 0,
                    0, 0,
               )

    空间转移 = CreateCraft(
                    "空间转移",
                    " ",
                    0x05, 0x12, 0x0,
                    CraftAttribute.NoAttribute,
                    CraftRange.SelectLocation,
                    CraftState.NoneState, CraftState.NoneState,
                    0, 100,
                    0, 5,
                    0,
                    50,
                    0, 0,
                    0, 0,
               )

    伪盐之桩 = CreateCraft(
                    "伪·盐之桩",
                    "召唤曾使一个国家毁灭的盐之桩（只是幻术的伪造品），\\n使敌方全员化为盐之碎粒。",
                    0x06, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnLocation,
                    CraftState.Physical, CraftState.NoneState,
                    1, 50,
                    0, 30,
                    100,
                    100,
                    175, 0,
                    0, 0,
               )

    死亡之指 = CreateCraft(
                    "死亡之指",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Physical, CraftState.NoneState,
                    1, 100,
                    0, 25,
                    0,
                    100,
                    150, 0,
                    0, 0,
               )

    时空追放 = CreateCraft(
                    "时空追放",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.NoneState, CraftState.NoneState,
                    1, 100,
                    0, 50,
                    0,
                    100,
                    0, 0,
                    0, 0,
               )

    真实之镜 = CreateCraft(
                    "照妖镜",
                    "",
                    0x05, 0x92, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.NoneState, CraftState.NoneState,
                    1, 100,
                    0, 50,
                    0,
                    100,
                    0, 0,
                    0, 0,
               )

    玻璃渣 = CreateCraft(
                    "玻璃渣",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnLocation,
                    CraftState.Physical, CraftState.NoneState,
                    1, 100,
                    0, 30,
                    0,
                    5,
                    60, 0,
                    0, 0,
               )


    #################################################################################
    # arts                                                                          #
    #################################################################################

    龙皇炼狱火 = CreateCraft(
                    "伪·龙皇炼狱火",
                    "",
                    0x23, 0x12, 0x21,
                    CraftAttribute.Hono,
                    CraftRange.FullMap,
                    CraftState.Arts, CraftState.Burning,
                    135, 100,
                    0, 20,
                    0,
                    100,
                    410, 0,
                    15, 3,
               )

    闪电之力 = CreateCraft(
                    "伪·闪电之力",
                    "",
                    0x05, 0x12, 0x21,
                    CraftAttribute.Kaze,
                    CraftRange.FullMap,
                    CraftState.Arts, CraftState.BanCraft,
                    135, 100,
                    0, 15,
                    0,
                    100,
                    270, 0,
                    30, 3,
               )

    虚空幻域 = CreateCraft(
                    "伪·虚空幻域",
                    "",
                    0x79, 0xC2, 0x21,
                    CraftAttribute.Gen,
                    CraftRange.FullMap,
                    CraftState.Stealth, CraftState.NoneState,
                    135, 100,
                    0, 25,
                    0,
                    100,
                    1, 9999,
                    0, 0,
               )

    #################################################################################
    # arts end                                                                      #
    #################################################################################

    CraftList = CreateCraftList([
                    Craft_03E8,
                    相位重置,
                    置换,
                    空间转移,

                    伪盐之桩,
                    死亡之指,
                    玻璃渣,
                    时空追放,
                    真实之镜,

                    龙皇炼狱火,
                    闪电之力,
                    虚空幻域,
                ])

    Attack = CreateAI(0x1,  100,  0x8,  0x1,  0x00, 0x05, Craft_03E8,      [0,     0,      0,      0])

    Arts_龙皇炼狱火      = CreateAI(0x2,  30,   0x7,  0x1,  0x06, 0x07, 龙皇炼狱火,        [0,     0,      1,      0])
    Arts_闪电之力        = CreateAI(0x2,  30,   0x7,  0x1,  0x06, 0x18, 闪电之力,        [0,     0,      1,      0])
    Arts_虚空幻域        = CreateAI(0x2,  30,   0x7,  0x1,  0x06, 0x07, 虚空幻域,        [0,     0,      1,      0])

    Craft_置换           = CreateAI(0x8,  100,  0x0,  0x1,  0x00, 0x12, 置换,            [100,   1,      0,      0])
    Craft_相位重置       = CreateAI(0x2,  25,   0x0,  0x1,  0x00, 0x11, 相位重置,        [0,     0,      0,      0])
    Craft_空间转移       = CreateAI(0x6,  50,   0x17, 0x1,  0x00, 0x14, 空间转移,        [3500,  2,      0,      2])
    Craft_死亡之指       = CreateAI(0x6,  50,   0x17, 0x1,  0x00, 0x05, 死亡之指,        [3500,  2,      0,      2])
    Craft_玻璃渣         = CreateAI(0x6,  50,   0x17, 0x1,  0x00, 0x17, 玻璃渣,        [3500,  2,      0,      2])
    Craft_时空追放       = CreateAI(0x6,  50,   0x17, 0x1,  0x00, 0x19, 时空追放,      [3500,  2,      0,      2])
    Craft_真实之镜       = CreateAI(0x6,  50,   0x17, 0x1,  0x00, 0x10, 真实之镜,      [3500,  2,      0,      2])

    SCraft_伪盐之桩      = CreateAI(0xA,  100,  0x0,  0x1,  0x00, 0x1A, 伪盐之桩,        [200,   0,      0,      0])

    ArtsAIList         = [Arts_虚空幻域, Arts_龙皇炼狱火, Arts_闪电之力]
    CraftAIList        = [Craft_死亡之指, Craft_真实之镜, Craft_时空追放, Craft_玻璃渣, Craft_置换, Craft_相位重置, Craft_空间转移]
    SCraftAIList       = [SCraft_伪盐之桩]
    SupportCraftAIList = []

    SaveToMS("ms90020.dat", locals())

Try(main)
