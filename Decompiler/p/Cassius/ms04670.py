from BattleMonsterStatus import *

def main():
    Name               = "钢盔肾斗士"
    Description        = "结社钢盔肾女座下，\\n八十八个『肾斗士』第一位。"
    ASFile             = "as04670.dat"
    Symbol             = "sy04670.itp"

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

    Level              = 120
    MaximumHP          = 59000
    InitialHP          = 59000
    MaximumEP          = 9000
    InitialEP          = 9000
    MaximumCP          = 200
    InitialCP          = 0

    SPD                = 120
    MoveSPD            = 10
    MOV                = 6
    STR                = 3450
    DEF                = 3114
    ATS                = 2219
    ADF                = 2391
    DEX                = 150
    AGL                = 32
    RNG                = 1

    Unknown_2A         = 0x0
    EXP                = 1024
    Unknown_2E         = 0x0
    Unknown_30         = 0x0
    AIType             = 0xFF
    Unknown_33         = 0x3E8
    Unknown_35         = 0x9
    Unknown_36         = 0xA280
    EnemyFlags         = 0x0000
    BattleFlags        = 0x0804

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
    #Resistance         = 0xF0008FFF
    AttributeRate      = [ 100, 100, 100, 100, 100, 100, 100 ]
    Sepith             = [ 255, 255, 255, 255, 255, 255, 255 ]
    DropItem           = [ 0x01FF, 0x0000 ]
    DropRate           = [ 100, 0 ]
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
                    CraftState.Physical, CraftState.QueryMonsterInfo,
                    0, 0,
                    0, 30,
                    0,
                    0,
                    60, 0,
                    0, 0,
               )

    百烈击 = CreateCraft(
                    "百烈击",
                    "百龙霸",
                    0x05, 0x12, 0,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.Physical, CraftState.NoneState,
                    3, 1,
                    0, 35,
                    0,
                    2,
                    50, 0,
                    0, 0,
               )

    钢盔回旋踢 = CreateCraft(
                    "钢盔回旋踢",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.CircleOnSelf,
                    CraftState.Physical, CraftState.NoneState,
                    1, 1,
                    0, 40,
                    0,
                    10,
                    70, 0,
                    0, 0,
               )

    钢盔断 = CreateCraft(
                    "钢盔断",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.LineOnLocation,
                    CraftState.Physical, CraftState.ATDelay,
                    54, 100,
                    0, 40,
                    0,
                    5,
                    50, 0,
                    50, 0,
               )

    神罗天征 = CreateCraft(
                    "神罗天征",
                    "",
                    0x05, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.FullMap,
                    CraftState.Physical, CraftState.NoneState,
                    1, 100,
                    0, 100,
                    0,
                    0,
                    100, 0,
                    0, 0,
               )

    # 精神分裂 = CreateCraft(
    #                 "精神分裂",
    #                 "",
    #                 0x5, 0x12, 0x21,
    #                 CraftAttribute.NoAttribute,
    #                 CraftRange.SelectLocation,
    #                 CraftState.NoneState, CraftState.NoneState,
    #                 0, 0,
    #                 0, 0,
    #                 0,
    #                 1,
    #                 0, 1,
    #                 0xFF, 1,
    #            )

    精神分裂 = CreateCraft(
                    "精神分裂",
                    "",
                    0x93, 0x12, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.SelectLocation,
                    CraftState.NoneState, CraftState.NoneState,
                    0, 0,
                    0, 0,
                    0,
                    0,
                    0, 0,
                    0xFF, 1,
               )

    精神分裂2 = CreateCraft(
                    "精神分裂2",
                    " ",
                    0x91, 0x42, 0x1,
                    CraftAttribute.NoAttribute,
                    CraftRange.Target,
                    CraftState.NoneState, CraftState.NoneState,
                    0, 0,
                    0, 0,
                    0,
                    0,
                    0, 0,
                    0, 0,
               )

    CraftList = CreateCraftList([
                    Craft_03E8,
                    百烈击,
                    钢盔回旋踢,
                    钢盔断,
                    神罗天征,
                    精神分裂,
                    精神分裂2,
                ])

    Attack = CreateAI(0x1, 0,   0x0, 0x1, 0x00, 0x05, Craft_03E8,         [0,     0,      1,      0])

    Craft_百烈击        = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x10, 百烈击,         [30,    1,      0,      0])
    Craft_钢盔回旋踢    = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x11, 钢盔回旋踢,      [30,    1,      0,      0])
    Craft_钢盔断        = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x12, 钢盔断,         [30,    1,      0,      0])
    Craft_神罗天征      = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x13, 神罗天征,         [30,    1,      0,      0])
    Craft_精神分裂      = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x14, 精神分裂,         [30,    1,      0,      0])
    Craft_精神分裂2     = CreateAI(0x3,  100,  0x0,  0x1,  0x00, 0x14, 精神分裂2,         [30,    1,      0,      0])

    # SCraft_圣技大十字    = CreateAI(0xA, 100, 0x0, 0x1, 0x00, 0x1A, 圣技大十字,         [100,   0,      0,      0])


    ArtsAIList          = []
    CraftAIList         = [Craft_精神分裂2, Craft_精神分裂, Craft_神罗天征, Craft_钢盔断, Craft_钢盔回旋踢, Craft_百烈击]
    SCraftAIList        = []
    SupportCraftAIList  = []

    SaveToMS("ms04670.dat", locals())

Try(main)