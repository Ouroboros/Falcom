from BattleActionScript import *
import Arianrhod_Crafts as Arianrhod

def main():
    CreateBattleAction("as90010.dat", ((128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176)))

    AddPreloadChip((
        "chr/ch04250.itc",         # 00 0
        "chr/ch04251.itc",         # 01 1
        "chr/ch04253.itc",         # 02 2
        "chr/ch04254.itc",         # 03 3
        "chr/ch03554.itc",         # 04 4
    ))

    CraftAction((
        "SysCraft_Init",                    # 00 0
        "SysCraft_Stand",                   # 01 1
        "SysCraft_Move",                    # 02 2
        "SysCraft_UnderAttack",             # 03 3
        "SysCraft_Dead",                    # 04 4
        "SysCraft_NormalAttack",            # 05 5
        "SysCraft_ArtsAria",                # 06 6
        "SysCraft_ArtsCast",                # 07 7
        "SysCraft_Win",                     # 08 8
        "SysCraft_EnterBattle",             # 09 9
        "SysCraft_UseItem",                 # 0A 10
        "SysCraft_Stun",                    # 0B 11
        "SysCraft_Unknown2",                # 0C 12
        'stub_craft',                       # 0D 13
        'stub_craft',                       # 0E 14
        "SysCraft_Counter",                 # 0F 15
        "Craft_疾风轰雷闪",                 # 10 16
        "Craft_大地轰雷锤",                 # 11 17
        "Craft_横扫千军",                   # 12 18
        "unmask",                           # 13 19
        "Craft_零时迷子",                   # 14 20
        "Craft_暴雨疾风枪",                 # 15 21
        'Craft_麒麟功',                     # 16 22
        'Craft_朗基努斯枪',                 # 17 23
        'Craft_EnumaElish',                 # 18 24
        'Craft_神速',                       # 19 25
        "Craft_圣技大十字",                 # 1A 26
        'Craft_朗基努斯枪_EnemyVersion',    # 1B 27
        'Craft_unmask_EnemyVersion',        # 1C 28
        'Craft_大地轰雷锤_EnemyVersion',    # 1D 29

        'SysCraft_TeamRushInit',            # 1E 30
        'SysCraft_TeamRushAction',          # 1F 31
        EMPTY_ACTION,                       # 20 32
        EMPTY_ACTION,                       # 21 33
        EMPTY_ACTION,                       # 22 34
        EMPTY_ACTION,                       # 23 35
        EMPTY_ACTION,                       # 24 36
        EMPTY_ACTION,                       # 25 37
        EMPTY_ACTION,                       # 26 38

        EMPTY_ACTION,                       # 27 39
        EMPTY_ACTION,                       # 28 40
        EMPTY_ACTION,                       # 29 41
        EMPTY_ACTION,                       # 2A 42
        EMPTY_ACTION,                       # 2B 43
        EMPTY_ACTION,                       # 2C 44
        EMPTY_ACTION,                       # 2D 45
    ))


    label('SysCraft_TeamRushInit')
    Arianrhod.TeamRushInit()
    Return()

    label('SysCraft_TeamRushAction')
    Arianrhod.TeamRushAction()
    Return()

    label('Craft_麒麟功')

    AS_8D(0x4B, 0xFF, 0x10000, 0xFFFFFFFF, 0x0)
    AS_8D(0x4B, 0xFF, 0x800000, 0xFFFFFFFF, 0x0)
    DamageCue(0xFE)
    AS_A1(0xFF, 0x10000, 0x83, "")
    Return()

    label('Craft_朗基努斯枪')
    Arianrhod.Longinus()
    Return()

    label('Craft_朗基努斯枪_EnemyVersion')
    Arianrhod.Longinus(True)
    Return()

    label('Craft_unmask_EnemyVersion')
    Arianrhod.unmask(True)
    Return()

    label('Craft_大地轰雷锤_EnemyVersion')
    Arianrhod.Craft_大地轰雷锤(True)
    Return()

    label('Craft_EnumaElish')
    Arianrhod.EnumaElish()
    Return()

    label('Craft_神速')
    Arianrhod.神速()
    Return()

    label('stub_craft')
    Return()


    label("SysCraft_ArtsAria")

    Call('clear_all_debuff')
    Arianrhod.ArtsAria()
    Return()


    label("SysCraft_ArtsCast")

    Arianrhod.ArtsCast()
    Return()


    label("SysCraft_Win")

    Arianrhod.BattleWin()
    Return()


    label("SysCraft_EnterBattle")

    Arianrhod.EnterBattle()
    Return()


    label("SysCraft_UseItem")

    Arianrhod.UseItem()
    Return()

    label("SysCraft_Init")

    #LoadEffect(0x80, "battle/mgaria0.eff")
    #LoadEffect(0x81, "battle/mgaria1.eff")

    LoadEffect(0x80, "event/ev10006.eff")
    LoadEffect(0x81, "event/ev10007.eff")

    LoadEffect(0x82, "battle/cr035000.eff")
    LoadEffect(0x83, "battle/cr035100.eff")

    #PlayEffect(0xFF, 0xFF, 0x37, 0x41, 0, 1100, 0, 0, 0, 0, 1000, 1000, 1000, 0xA)
    Jc(0x9, 0x1, 0x107, "loc_48A")
    AS_74(0x0, 0x100)
    Jump("loc_48E")

    label("loc_48A")

    AS_74(0x0, 0x20)

    label("loc_48E")

    AS_6E(0x400000)
    Return()

    # SysCraft_Init end

    label('clear_all_debuff')

    not_clear = \
    [
        CraftConditionFlags.MaxGuard,
        CraftConditionFlags.HPRecovery,
        CraftConditionFlags.CPRecovery,
        CraftConditionFlags.Stealth,
        CraftConditionFlags.Dead,
        CraftConditionFlags.Vanish,
    ]

    flag = 1
    for i in range(32):
        if not flag in not_clear:
            AS_8D(0x4B, CraftTarget.Self, flag, -1, 0)
        flag <<= 1

    AS_8D(0x4B, CraftTarget.Self, CraftConditionFlags.Vanish, 0, 0)

    CallReturn()


    label("SysCraft_Stand")

    Call('clear_all_debuff')

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x0)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(130)
    Yield()
    Jump("SysCraft_Stand")

    # SysCraft_Stand end


    label("SysCraft_Move")

    SetChrChip(0xFF, 0x1)
    SetChrSubChip(0xFF, 0x0)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x0)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    Sleep(40)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(40)
    Yield()
    Jump("SysCraft_Move")

    # SysCraft_Move end


    label("SysCraft_UnderAttack")

    Arianrhod.UnderAttack()
    Return()

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x0)
    Sleep(40)
    Yield()
    Call("loc_211")
    Return()

    label("loc_211")

    ShakeChr(0xFF, -200, 0, -200)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 200, 0, 200)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, -200, 0, -200)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 200, 0, 200)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, -150, 0, -150)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 150, 0, 150)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, -100, 0, -100)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 100, 0, 100)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, -50, 0, -50)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 50, 0, 50)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, -50, 0, -50)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 50, 0, 50)
    Sleep(50)
    Yield()
    ShakeChr(0xFF, 0, 0, 0)
    Sleep(50)
    Yield()
    CallReturn()

    # SysCraft_UnderAttack end


    label("SysCraft_Dead")

    Arianrhod.Dead()
    Return()

    '''
    AS_6C()
    Jc(0x2, 0x2, 0x10, "loc_4A2")
    Jump("loc_12A")

    label("loc_12A")

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(180)
    Yield()
    Return()

    label("loc_4A2")

    Jc(0xA, 0x1, 0x2, "loc_4B7")
    Jc(0xB, 0x1, 0x3, "loc_4B7")
    Jump("loc_4D7")

    label("loc_4B7")

    Voice(0x0, 3877, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x1)
    Sleep(300)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(300)
    Yield()
    SoundEx(514, 0x0)

    label("loc_4D7")

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(300)
    Yield()
    Sleep(4000)
    Yield()
    Return()

    '''

    # SysCraft_Dead end


    label("SysCraft_NormalAttack")


    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04252.itc", 0xFF)
    LoadEffect(0x0, "battle/ms00001.eff")
    AS_78(0x0)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0x64, 0xF, 0xF)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    AS_1E(0xFFFFFFFF)
    EndChrThread(0xFF, 1)
    TurnDirection(0xFF, 0xFE, 0x0, 0x0, 0x0)
    Voice(0x0, 3859, 3860, 3861, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    SoundEx(358, 0x0)
    AS_6D(0x200000)
    AS_89(0xFF)
    AS_05(0xFF, 0x0, 0x0)
    AS_21(0x1, 0xFF, -150, 20000)
    Sleep(300)
    Yield()
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    PlayEffect(0xFF, 0xFF, 0x82, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    BeginChrThread(0xFF, 1, "loc_65A", 0x0)
    BeginChrThread(0xFF, 2, "loc_672", 0x0)
    SoundEx(324, 0x0)
    AS_3D(150, 150, 150, 600)
    Sleep(500)
    Yield()
    CancelEffect(0xFF, 0x2)
    AS_21(0x1, 0xFF, 300, 20000)
    CancelBlur(0x12C)
    Sleep(100)
    Yield()
    EndChrThread(0xFF, 1)
    EndChrThread(0xFF, 2)
    AS_3D(200, 200, 200, 300)
    LookingTarget(0x1E, 0x14, 0x1E)
    ResetTarget()
    StopEffect(0xFF, 0x3)
    PlayEffect(0xFF, 0xFE, 0x0, 0x1, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    AS_67(0x10A, 0xFF, 0xFE)
    SetChrSubChip(0xFF, 0x5)
    Sleep(500)
    Yield()
    AS_21(0x1, 0xFF, -150, 20000)
    AS_10(0x1, 0x4E20)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    AS_6E(0x200000)
    FreeEffect(0x0)
    AS_6B()
    Return()

    '''

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04252.itc", 0xFF)
    LoadEffect(0x0, "battle/ms00001.eff")
    AS_78(0x0)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0x64, 0xF, 0xF)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    AS_1E(0xFFFFFFFF)
    EndChrThread(0xFF, 1)
    TurnDirection(0xFF, 0xFE, 0x0, 0x0, 0x0)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    SoundEx(358, 0x0)
    AS_6D(0x200000)
    AS_89(0xFF)
    AS_05(0xFF, 0x0, 0x0)
    AS_21(0x1, 0xFF, -150, 20000)
    Sleep(300)
    Yield()
    Jc(0x14, 0x4, 0x32, "loc_570")
    Voice(0x0, 3859, 0, 0, 0, 0xFE)
    Jump("loc_592")

    label("loc_570")

    Jc(0x14, 0x4, 0x32, "loc_587")
    Voice(0x0, 3860, 0, 0, 0, 0xFE)
    Jump("loc_592")

    label("loc_587")

    Voice(0x0, 3861, 0, 0, 0, 0xFE)

    label("loc_592")

    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    PlayEffect(0xFF, 0xFF, 0x82, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    BeginChrThread(0xFF, 1, "loc_65A", 0x0)
    BeginChrThread(0xFF, 2, "loc_672", 0x0)
    SoundEx(324, 0x0)
    AS_3D(150, 150, 150, 600)
    Sleep(1300)
    Yield()
    CancelEffect(0xFF, 0x2)
    AS_21(0x1, 0xFF, 300, 20000)
    CancelBlur(0x12C)
    Sleep(100)
    Yield()
    EndChrThread(0xFF, 1)
    EndChrThread(0xFF, 2)
    AS_3D(200, 200, 200, 300)
    LookingTarget(0x1E, 0x14, 0x1E)
    ResetTarget()
    StopEffect(0xFF, 0x3)
    PlayEffect(0xFF, 0xFE, 0x0, 0x1, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    AS_67(0x10A, 0xFF, 0xFE)
    SetChrSubChip(0xFF, 0x5)
    Sleep(500)
    Yield()
    AS_21(0x1, 0xFF, -150, 20000)
    AS_10(0x1, 0x4E20)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    AS_6E(0x200000)
    FreeEffect(0x0)
    AS_6B()
    Return()

    '''

    label("loc_65A")

    SetChrSubChip(0xFF, 0x4)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(50)
    Yield()
    Jump("loc_65A")

    label("loc_672")

    ResetTarget()

    #label("loc_673")

    #ForeachTarget("loc_6B2")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    AS_A7(0xFF, 0x3, 0xFE, 0xFF38, 0x1F4, 0xFF38, 0xC8, 0x3E8, 0xC8, 0x0)
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(100)
    Yield()
    #NextTarget()
    #Jump("loc_673")

    label("loc_6B2")

    Sleep(100)
    Yield()
    Jump("loc_672")

    # SysCraft_NormalAttack end


    label("SysCraft_Stun")

    Call('clear_all_debuff')

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x1)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    Return()

    # SysCraft_Stun end


    label("SysCraft_Unknown2")

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    Return()

    # SysCraft_Unknown2 end


    label("SysCraft_Counter")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04252.itc", 0xFF)
    LoadEffect(0x0, "battle/ms00001.eff")
    AS_78(0x0)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0x64, 0xF, 0xF)
    TurnDirection(0xFF, 0xFE, 0x0, 0x0, 0x0)
    Voice(0x0, 3880, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    SoundEx(358, 0x0)
    AS_6D(0x200000)
    AS_89(0xFF)
    AS_05(0xFF, 0x0, 0x0)
    AS_21(0x1, 0xFF, -150, 20000)
    Sleep(300)
    Yield()
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    PlayEffect(0xFF, 0xFF, 0x82, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    BeginChrThread(0xFF, 1, "loc_65A", 0x0)
    BeginChrThread(0xFF, 2, "loc_672", 0x0)
    SoundEx(324, 0x0)
    AS_3D(150, 150, 150, 600)
    Sleep(500)
    Yield()
    CancelEffect(0xFF, 0x2)
    AS_21(0x1, 0xFF, 300, 20000)
    CancelBlur(0x12C)
    Sleep(100)
    Yield()
    EndChrThread(0xFF, 1)
    EndChrThread(0xFF, 2)
    AS_3D(200, 200, 200, 300)
    LookingTarget(0x1E, 0x14, 0x1E)
    ResetTarget()
    StopEffect(0xFF, 0x3)
    PlayEffect(0xFF, 0xFE, 0x0, 0x1, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    AS_67(0x10A, 0xFF, 0xFE)
    SetChrSubChip(0xFF, 0x5)
    Sleep(500)
    Yield()
    AS_21(0x1, 0xFF, -150, 20000)
    AS_10(0x1, 0x4E20)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    AS_6E(0x200000)
    FreeEffect(0x0)
    AS_6B()
    Return()

    # SysCraft_Counter end


    label("Craft_疾风轰雷闪")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04252.itc", 0xFF)
    LoadChrChip(0x6, "chr/ch04256.itc", 0xFF)
    LoadEffect(0x0, "battle/cr035100.eff")
    LoadEffect(0x1, "battle/cr035101.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    ChrSetPos(0xFF, 0xFB, 0, 0, 0)
    AS_6D(0x200000)
    AS_89(0xFF)
    AS_0A(0xFF, 0x1, 0x0, 0x0)
    AS_78(0x0)
    ResetTarget()
    AS_83(0x0)
    AS_26(0x2, 0xFF, 0x10)
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(0x64, 0x14, 0x1E)
    TurnDirection(0xFF, 0xFB, 0x0, 0x1F4, 0x0)
    SetBrightness(0x0, 0x2, 0x7D0)
    Voice(0x0, 3862, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    BeginChrThread(0xFF, 1, "loc_D02", 0x0)
    PlayEffect(0xFF, 0xFF, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    SoundEx(548, 0x0)
    SoundEx(203, 0x0)
    Sleep(1500)
    Yield()
    StopEffect(0xFF, 0x2)
    EndChrThread(0xFF, 1)
    ShakeChr(0xFF, 0, 0, 0)
    Voice(0x0, 3863, 0, 0, 0, 0xFE)
    PlayEffect(0xFF, 0xFF, 0x1, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x3)
    AS_3D(150, 150, 150, 10000)
    SetChrChip(0xFF, 0x6)
    SetChrSubChip(0xFF, 0x0)
    SoundEx(250, 0x0)
    Knockback(0x2)
    AS_8D(0xC, 0x0, 0xFFFFD8F0, 0x0, 0x0)
    BeginChrThread(0xFF, 2, "loc_991", 0x0)
    ShowChrTrails(0xFF, 0xC8, 0x12C)
    ChrTurnAndMove(0x0, 0xFF, 0xFB, 0, 40000)
    HideChrTrails(0xFF)
    EndChrThread(0xFF, 2)
    Knockback(0x1)
    CancelEffect(0xFF, 0x3)
    AS_3D(0, 0, 0, 0)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x5)
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    Sleep(300)
    Yield()
    CancelBlur(0x1F4)
    AS_8F(0x0)
    ResetBrightness(0x3E8)
    AS_27(0x2, 0xFF, 0x10)
    AS_6E(0x200000)
    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    AS_6B()
    Return()

    label("loc_991")

    Jc(0x16, 0x1, 0x0, "loc_99B")
    Return()

    label("loc_99B")

    ResetTarget()

    label("loc_99C")

    ForeachTarget("loc_9EA")
    AS_9C(0xFE)
    AS_8D(0x10, 0x7D0, 0xFE, 0x0, 0x0)
    Jc(0x11, 0x1, 0x1, "loc_9E6")
    PlayEffect(0xFF, 0xFE, 0x13, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SoundEx(204, 0x0)
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()

    label("loc_9E6")

    NextTarget()
    Jump("loc_99C")

    label("loc_9EA")

    Sleep(50)
    Yield()
    ResetTarget()
    Jump("loc_99C")


    label("loc_D02")

    ShakeChr(0xFF, -15, 0, -15)
    Sleep(30)
    Yield()
    ShakeChr(0xFF, 15, 0, 15)
    Sleep(30)
    Yield()
    Jump("loc_D02")

    # Craft_疾风轰雷闪 end


    label("Craft_大地轰雷锤")
    Arianrhod.Craft_大地轰雷锤()

    # Craft_大地轰雷锤 end


    label("Craft_横扫千军")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04258.itc", 0xFF)
    LoadEffect(0x0, "battle/cr035300.eff")
    LoadEffect(0x1, "battle/cr035301.eff")
    AS_78(0x0)
    ResetTarget()
    SetBrightness(0x0, 0x2, 0x7D0)
    LockCamera(0xFF, 0, 750, 0, 1000)
    AS_3B(17000, 1000)
    TurnDirection(0xFF, 0xFE, 0x2D, 0x1F4, 0x0)
    Voice(0x0, 3866, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    PlayEffect(0xFF, 0xFF, 0x0, 0x1, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    SoundEx(548, 0x0)
    SoundEx(183, 0x0)
    BeginChrThread(0xFF, 1, "loc_D02", 0x0)
    Sleep(1500)
    Yield()
    EndChrThread(0xFF, 1)
    ShakeChr(0xFF, 0, 0, 0)
    CancelEffect(0xFF, 0x2)
    Knockback(0x3)
    Voice(0x0, 3867, 0, 0, 0, 0xFE)
    Sleep(300)
    Yield()
    TurnDirection(0xFF, 0xFE, 0x0, 0x1F4, 0x0)
    BeginChrThread(0xFF, 1, "loc_D29", 0x0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0x64, 0x14, 0x1E)
    PlayEffect(0xFF, 0xFF, 0x1, 0x5, 0, 500, 0, 0, 0, 0, 550, 550, 550, 0xFF)
    SoundEx(248, 0x0)
    Sleep(250)
    Yield()
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    DamageAnime(0xFC, 0x1, 0x32)
    SoundEx(282, 0x0)
    SetBattleSpeed(0x64)
    Sleep(100)
    Yield()
    SetBattleSpeed(0x3E8)
    CancelBlur(0x12C)
    Sleep(300)
    Yield()
    AS_3D(150, 150, 150, 500)
    WaitChrThread(0xFF, 1)
    BeginChrThread(0xFF, 1, "loc_18F", 0x0)
    BeginChrThread(0xFF, 2, "SysCraft_Stand", 0x0)
    WaitChrThread(0xFF, 1)
    AS_8F(0x0)
    EndChrThread(0xFF, 2)
    ResetBrightness(0x3E8)
    FreeEffect(0x0)
    FreeEffect(0x1)
    AS_6B()
    Return()

    label("loc_18F")

    ResetTarget()

    label("loc_190")

    ForeachTarget("loc_19D")
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_190")

    label("loc_19D")

    Return()

    label("loc_D29")

    SoundEx(532, 0x0)
    SetChrSubChip(0xFF, 0x1)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x5)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x6)
    Return()

    # Craft_横扫千军 end


    label("unmask")

    Arianrhod.unmask()

    Return()

    # Craft_D54 end


    label("Craft_零时迷子")
    Arianrhod.零时迷子()
    Return()

    # Craft_零时迷子 end


    label("Craft_暴雨疾风枪")

    Arianrhod.Craft_暴雨疾风枪()
    Return()

    # Craft_暴雨疾风枪 end


    label("Craft_圣技大十字")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04259.itc", 0xFF)
    LoadChrChip(0x6, "chr/ch04252.itc", 0xFF)
    LoadChrChip(0x5, "chr/ch04256.itc", 0xFF)
    LoadEffect(0x0, "eff/cutin42.eff")
    LoadEffect(0x1, "battle/sc035000.eff")
    LoadEffect(0x2, "battle/sc035001.eff")
    LoadEffect(0x3, "battle/cm008_01.eff")
    LoadEffect(0x4, "battle/com004.eff")
    LoadEffect(0x5, "battle/cr035100.eff")
    LoadEffect(0x6, "battle/cr035101.eff")
    LoadEffect(0x7, "battle/sc035003.eff")
    AS_78(0x0)
    Call("loc_2FC")
    ChrSetPos(0xFF, 0xF3, 0, 0, 0)
    AS_8D(0x1, 0x0, 0x0, 0x0, 0x0)
    Voice(0x0, 3870, 0, 0, 0, 0xFE)
    ChrSetPos(0xFF, 0xFD, 0, 0, -10000)
    AS_03(0xFF, 0x0)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_5F(0xFF, 0x0)
    #AS_03(0xFC, 0xB4)
    #AS_34()
    LockCamera(0xFD, 0, 750, -10000, 0)
    AS_3B(13000, 0)
    AS_39(180, 20, 5, 0)
    AS_39(180, 15, 0, 1500)
    AS_3B(16000, 1500)
    PlayEffect(0xFF, 0xFF, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x3)
    SoundEx(197, 0x0)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    WaitEffect(0xFF, 0x2)
    EndChrThread(0xFF, 1)
    LockCamera(0xFD, 0, 2000, -10000, 1500)
    SetChipModeFlags(0x0, 0xFF, 0x2)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    Sleep(100)
    Yield()
    SoundEx(321, 0x0)
    AS_3D(20, 20, 20, 10000)
    Sleep(1500)
    Yield()
    SetChrSubChip(0xFF, 0x5)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x6)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x7)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x8)
    SoundEx(358, 0x0)
    AS_43(0x0, 0x0, 0xFFFFFFFF)
    AS_44(0x0, 0x1F4, 0xFFFFFFFF)
    Voice(0x0, 3871, 0, 0, 0, 0xFE)
    AS_8A(0x12, 0xFF)
    ClearChipModeFlags(0x0, 0x12, 0x80)
    ChrSetPos(0x12, 0xFF, 0, 0, -10000)
    SoundEx(321, 0x0)
    SoundEx(207, 0x0)
    AS_60(0x12)
    CancelEffect(0xFF, 0x3)
    LockCamera(0xFD, 0, 2050, -10000, 3000)
    AS_3B(18000, 3000)
    AS_39(180, -10, -15, 3000)
    AS_3D(50, 50, 50, 10000)
    PlayEffect(0xFF, 0xFF, 0x7, 0x0, 0, 200, -10000, 0, 0, 0, 1000, 1000, 1000, 0x3)
    PlayEffect(0xFF, 0x12, 0x2, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x4)
    SoundEx(207, 0x0)
    Sleep(1500)
    Yield()
    ClearChipModeFlags(0x0, 0xFF, 0x2)
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(500)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    SoundEx(206, 0x0)
    AS_11(0x12, 0xFF, 10000, -2500, -5000, 1000, 0x0)
    AS_11(0x12, 0xFF, 0, -7500, 10000, 1000, 0x0)
    AS_44(0x1, 0x1F4, 0x0)
    CancelEffect(0xFF, 0x3)
    SoundEx(207, 0x0)
    AS_60(0xFF)
    Voice(0x0, 3872, 0, 0, 0, 0xFE)
    ChrSetPos(0x12, 0xF2, 0, 0, -20000)
    AS_03(0xFC, 0xB4)
    AS_5F(0xFC, 0x0)
    LockCamera(0x12, 0, 3500, 5000, 0)
    AS_3B(25000, 0)
    AS_39(135, 30, 15, 0)
    LockCamera(0xF2, 0, 2500, 0, 3000)
    AS_3B(30000, 3000)
    AS_39(45, 10, -15, 3000)
    AS_3D(50, 50, 50, 10000)
    AS_11(0x12, 0xF2, 0, 0, 0, 3000, 0x0)
    BeginChrThread(0xFF, 2, "loc_14B6", 0x0)
    BeginChrThread(0xFF, 3, "loc_1530", 0x0)
    Sleep(1500)
    Yield()
    AS_44(0x1, 0x1F4, 0x0)
    PlayEffect(0xFF, 0xF2, 0x4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x6)
    AS_A9(0xFF, 0x6, 0xFFFFF0CE)
    SoundEx(207, 0x0)
    EndChrThread(0xFF, 2)
    EndChrThread(0xFC, 1)
    BeginChrThread(0xFF, 2, "loc_149C", 0x0)
    ChrSetPos(0xFF, 0xF2, 0, 0, -30000)
    Voice(0x0, 3873, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x6)
    SetChrSubChip(0xFF, 0x0)
    AS_5F(0xFF, 0x0)
    LockCamera(0xFF, 0, 500, 5000, 0)
    AS_3B(13000, 0)
    AS_39(25, 5, -5, 0)
    AS_3E(0x2EE, 0x0)
    Sleep(1000)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    PlayEffect(0xFF, 0xFF, 0x5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x7)
    SoundEx(548, 0x0)
    SoundEx(203, 0x0)
    BeginChrThread(0xFF, 1, "loc_D02", 0x0)
    Sleep(2000)
    Yield()
    CancelEffect(0xFF, 0x7)
    EndChrThread(0xFF, 1)
    ShakeChr(0xFF, 0, 0, 0)
    PlayEffect(0xFF, 0xFF, 0x6, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x8)
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    SoundEx(251, 0x0)
    HideChr(0xFF, 0x12C)
    SetChrChip(0xFF, 0x5)
    SetChrSubChip(0xFF, 0x0)
    AS_11(0xFF, 0xF2, 0, 500, 0, 500, 0x0)
    EndChrThread(0xFF, 3)
    AS_43(0x0, 0x0, 0x0)
    EndChrThread(0xFF, 2)
    AS_A8(0x0, 0x2)
    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    FreeEffect(0x3)
    FreeEffect(0x4)
    FreeEffect(0x5)
    FreeEffect(0x6)
    FreeEffect(0x7)
    AS_78(0x1)
    LoadEffect(0x0, "battle/sc035002.eff")
    LoadEffect(0x1, "battle/sc035004.eff")
    AS_78(0x0)
    CancelBlur(0x12C)
    ChrSetPos(0xFF, 0xF3, 0, 0, 0)
    AS_8D(0x1, 0x0, 0x0, 0x0, 0x0)
    AS_60(0xF7)
    ShowChr(0xFF, 0x0)
    AS_5F(0xFF, 0x0)
    SetChipModeFlags(0x0, 0x12, 0x80)
    Voice(0x0, 3874, 0, 0, 0, 0xFE)
    AS_52(0x1)
    ResetTarget()

    label("loc_1283")

    ForeachTarget("loc_1364")
    Jc(0x6, 0x1, 0xFF, "loc_12A5")
    ChrSetPos(0xFF, 0xFE, 0, 0, -10000)
    SoundEx(569, 0x0)
    Jump("loc_12DB")

    label("loc_2FC")

    AS_8D(0x4C, 0x0, 0x0, 0x0, 0x0)
    ResetTarget()
    SetBrightness(0x0, 0x0, 0x0)
    AS_60(0xF7)
    AS_6D(0x40000)
    ClearChipModeFlags(0x0, 0xFF, 0x1)
    CallReturn()

    label("loc_12A5")

    Jc(0x5, 0x1, 0x1, "loc_12C6")
    ChrSetPos(0xFF, 0xFE, -5000, 0, -8500)
    SoundEx(569, 0x0)
    AS_53(0x1)
    Jump("loc_12DB")

    label("loc_12C6")

    ChrSetPos(0xFF, 0xFE, 5000, 0, -8500)
    SoundEx(569, 0x0)
    AS_52(0x1)

    label("loc_12DB")

    TurnDirection(0xFF, 0xFE, 0x0, 0x0, 0x0)
    AS_05(0xFF, 0x0, 0x0)
    TurnDirection(0xFE, 0xFF, 0x0, 0x0, 0x0)
    AS_5F(0xFE, 0x0)
    LockCamera(0xFE, 0, 750, 0, 0)
    AS_39(90, 30, 0, 0)
    AS_3B(16000, 0)
    AS_3E(0x1F4, 0x0)
    AS_44(0x0, 0x64, 0xFFFFFFFF)
    DamageAnime(0xFE, 0x0, 0x32)
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 700, 0, 0, 0, 0, 600, 600, 600, 0x2)
    AS_21(0x1, 0xFF, 20000, 80000)
    AS_43(0x0, 0x64, 0x0)
    Sleep(100)
    Yield()
    AS_60(0xFE)
    StopEffect(0xFF, 0x2)
    NextTarget()
    Jump("loc_1283")

    label("loc_1364")

    StopEffect(0xFF, 0x2)
    StopEffect(0xFF, 0x6)
    AS_5F(0xFF, 0x0)
    AS_5F(0xFC, 0x0)
    ResetTarget()
    ChrSetPos(0xFF, 0xFE, 0, 1500, 0)
    ResetTarget()

    label("loc_1381")

    ForeachTarget("loc_13D3")
    ChrSetPos(0xFE, 0xFF, 0, 0, 0)
    ChrSetPos(0xFF, 0xFE, 1500, 0, 0)
    AS_9C(0xFE)
    EndChrThread(0xFE, 0)
    Sleep(1)
    Yield()
    BeginChrThread(0xFE, 0, "loc_14AF", 0x0)
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 500, 0, 0, 0, 0, 700, 700, 700, 0xFF)
    NextTarget()
    Jump("loc_1381")

    label("loc_13D3")

    ChrSetPos(0xFF, 0xF2, 0, 0, 28000)
    AS_03(0xFF, 0x0)
    SetChipModeFlags(0x0, 0xFF, 0x2)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x9)
    SoundEx(285, 0x0)
    LockCamera(0xFF, 0, 500, -5000, 0)
    AS_3B(19000, 0)
    AS_39(165, 5, 5, 0)
    AS_44(0x0, 0x12C, 0xFFFFFFFF)
    CancelEffect(0xFF, 0x8)
    AS_11(0xFF, 0xF2, 0, 0, 30000, 500, 0x0)
    ClearChipModeFlags(0x0, 0xFF, 0x2)
    SoundEx(183, 0x0)
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x3)
    Sleep(1000)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    SoundEx(172, 0x0)
    BeginChrThread(0xFF, 1, "loc_149C", 0x0)
    PlayEffect(0xFF, 0xF4, 0x1, 0x0, 3000, 0, 0, 0, 175, 0, 900, 900, 900, 0xFF)
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    SoundEx(200, 0x0)
    Sleep(1000)
    Yield()
    AS_43(0x0, 0x3E8, 0xFFFFFFFF)
    Sleep(1500)
    Yield()
    EndChrThread(0xFF, 1)
    CancelBlur(0x0)
    Call("loc_321")
    Return()

    label("loc_321")

    EndChrThread(0xFF, 1)
    EndChrThread(0xFF, 2)
    EndChrThread(0xFF, 3)
    HideChrTrails(0xFF)
    ClearChipModeFlags(0x0, 0xFF, 0x2)
    SetChrSubChip(0xFF, 0x0)
    SetChrChip(0xFF, 0x0)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    AS_A8(0x0, 0x4)
    AS_A8(0x0, 0x5)
    AS_A8(0x0, 0x6)
    AS_A8(0x0, 0x7)
    AS_7A(0x1)
    ResetBrightness(0x0)
    AS_44(0x1, 0x1F4, 0x0)
    AS_6E(0x40000)
    Jc(0x2C, 0x2, 0x20, "loc_387")
    AS_31(0x17, 0x0)
    LockCamera(0xFD, -10000, -10000, -10000, 0)
    Jump("loc_3A6")

    label("loc_387")

    AS_31(0x17, 0x0)
    LockCamera(0xF4, 0, 0, 0, 0)
    BeginChrThread(0xFF, 3, "loc_17C", 0x0)
    WaitChrThread(0xFF, 3)
    AS_8F(0x0)

    label("loc_3A6")

    CallReturn()

    label("loc_17C")

    ResetTarget()

    label("loc_17D")

    ForeachTarget("loc_18E")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_17D")

    label("loc_18E")

    Return()

    label("loc_149C")

    ResetTarget()

    label("loc_149D")

    ForeachTarget("loc_14AC")
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("loc_149D")

    label("loc_14AC")

    Jump("loc_149C")

    label("loc_14AF")

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x0)
    Return()

    label("loc_14B6")

    ResetTarget()

    label("loc_14B7")

    ForeachTarget("loc_14DF")
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(100)
    Yield()

    def lambda_14C6():
        ChrMove(0xFF, 0xFF, 0, 120, 0, 100, 0x0)
        Return()

    QueueWorkItem(0xFE, 1, lambda_14C6)
    NextTarget()
    Jump("loc_14B7")

    label("loc_14DF")

    ResetTarget()

    label("loc_14E0")

    ForeachTarget("loc_152D")
    PlayEffect(0xFF, 0xFE, 0x3, 0x1, 0, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF)
    AS_A9(0xFF, 0x81, 0xFFF9A480)
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(50)
    Yield()

    def lambda_1514():
        ChrMove(0xFF, 0xFF, 0, 120, 0, 50, 0x0)
        Return()

    QueueWorkItem(0xFE, 1, lambda_1514)
    NextTarget()
    Jump("loc_14E0")

    label("loc_152D")

    Jump("loc_14DF")

    label("loc_1530")

    SoundEx(501, 0x0)
    Sleep(130)
    Yield()
    SoundEx(246, 0x0)
    Sleep(130)
    Yield()
    Jump("loc_1530")

    # Craft_圣技大十字 end

    SaveToFile()

Try(main)
