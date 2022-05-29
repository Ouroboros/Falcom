from Falcom.Common import IntEnum2

L_ARM_POINT     = 'L_arm_point'
R_ARM_POINT     = 'R_arm_point'

L_HAND_POINT    = 'L_hand_point'
R_HAND_POINT    = 'R_hand_point'

NODE_L_HAND     = 'NODE_L_HAND'
NODE_R_HAND     = 'NODE_R_HAND'

MAX_REG_ID      = 0x20

DummyCharBaseId             = 0xB5E
TempCharBaseId              = 0xB68

class PseudoChrId(IntEnum2):
    Party1                  = 0xF000
    Party2                  = 0xF001
    Party3                  = 0xF002
    Party4                  = 0xF003
    Party5                  = 0xF004
    Party6                  = 0xF005
    Party7                  = 0xF006
    Party8                  = 0xF007

    Enemy1                  = 0xF043
    Enemy2                  = 0xF044
    Enemy3                  = 0xF045
    Enemy4                  = 0xF046
    Enemy5                  = 0xF047
    Enemy6                  = 0xF048
    Enemy7                  = 0xF049
    Enemy8                  = 0xF04A

    Saved                   = 0xFFF4
    SelectedPos             = 0xFFF5
    Current                 = 0xFFFB
    Self                    = 0xFFFE

class AbnormalStatus(IntEnum2):
    Poison                  = 0x00000001
    Seal                    = 0x00000002
    Mute                    = 0x00000004
    Blind                   = 0x00000008
    Sleep                   = 0x00000010
    Burn                    = 0x00000020
    Freeze                  = 0x00000040
    Petrify                 = 0x00000080
    Faint                   = 0x00000100
    Confuse                 = 0x00000200
    Charm                   = 0x00000400
    Deathblow               = 0x00000800
    Nightmare               = 0x00001000
    Delay                   = 0x00002000
    Vanish                  = 0x00004000
    STRDown                 = 0x00008000
    DEFDown                 = 0x00010000
    ATSDown                 = 0x00020000
    ADFDown                 = 0x00040000
    SPDDown                 = 0x00080000
    MOVDown                 = 0x00100000
    Insight                 = 0x00200000
    SlowHPRecover           = 0x00400000
    SlowCPRecover           = 0x00800000
    CraftGuard              = 0x01000000
    MagicReflect            = 0x02000000
    PhysicalReflect         = 0x04000000
    SpiritUnification       = 0x08000000
    Possess                 = 0x10000000
    Stealth                 = 0x20000000
    BalanceDown             = 0x40000000
    Death                   = 0x80000000

class AbnormalStatus2(IntEnum2):
    BurningHeart            = 0x00000001
    HPUpDownVitality        = 0x00000002
    AlmightyConflagration   = 0x00000004
    TemporaryHPboost        = 0x00000008
    GuardBreak              = 0x00000010
    LinkBreak               = 0x00000020
    Enhanced                = 0x00000040
    Brandish                = 0x00000100
    ProtectionAgainstAll    = 0x00000200
    AbsoluteReflect         = 0x00000400
    CantMove                = 0x00000800
    ElementWeakness         = 0x00001000
    Hide                    = 0x00004000

class BattleChrFlags(IntEnum2):
    Enemy                   = 0x00000001
    NoErase                 = 0x00000002
    NoKnockBack             = 0x00000008
    Controllable            = 0x00000800
    Party                   = 0x00040000
    NoSwap                  = 0x10000000
    NoDamage                = 0x80000000

class BattleFlags(IntEnum2):
    DisableRun              = 0x00000001
    DisableItem             = 0x00000004
    DisableArts             = 0x00000008
    DisableOrder            = 0x00000020

class BattleButtonId(IntEnum2):
    Move                    = 0
    Craft                   = 1
    Item                    = 2
    Run                     = 3
    Attack                  = 4
    Arts                    = 5
    Swap                    = 6
    Order                   = 7