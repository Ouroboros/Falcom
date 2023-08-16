from ActionHelper import *

# 小丑肯帕雷拉

def main():
    CreateBattleAction("as90020.dat", ((128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176), (128, 176)))

    AddPreloadChip((
        "chr/ch03650.itc",         # 00 0
        "chr/ch03651.itc",         # 01 1
        "chr/ch03653.itc",         # 02 2
        "chr/ch03654.itc",         # 03 3
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
        EMPTY_ACTION,                       # 0D 13
        EMPTY_ACTION,                       # 0E 14
        "SysCraft_Counter",                 # 0F 15
        "Craft_10_16_8F0_真实之镜",         # 10 16
        "Craft_11_17_A02_相位重置",         # 11 17
        "Craft_12_18_B82_置换",             # 12 18
        "Craft_13_19_C3D_废话1",            # 13 19
        "Craft_14_20_CF8_空间转移",         # 14 20
        "Craft_15_21_DB0_魔反取消",         # 15 21
        "Craft_16_22_1360_废话2",           # 16 22
        "Craft_玻璃渣",                   # 17 23
        "闪电之力",                         # 18 24
        "Craft_时空追放",                   # 19 25
        "Craft_1A_26_DFB_伪盐之桩",         # 1A 26
        EMPTY_ACTION,                       # 1B 27
        EMPTY_ACTION,                       # 1C 28
        EMPTY_ACTION,                       # 1D 29

        EMPTY_ACTION,                       # 1E 30
        EMPTY_ACTION,                       # 1F 31
    ))

    arts_aria_eff_id = 0

    def Craft_SysCraft_Init(): pass

    label("SysCraft_Init")

    LoadEffect(0x80, "event/ev17050.eff")
    LoadEffect(0x81, "event/ev17051.eff")
    LoadEffect(0x82, "battle/cr036302.eff")
    LoadEffect(0x83, "battle/cr036010.eff")
    #Call("loc_50A")
    AS_8D(0x15, 0xFF, CraftConditionFlags.ArtsReflect, 0x0, 9999)
    Call('set_spirit_eff')
    Return()

    label('set_spirit_eff')

    PlayEffect(0xFF, 0xFF, 0x83, 0x41, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 10)
    SetEffectColor(0xFF, 10, 0xFF1D5622)
    CallReturn()

    label("loc_50A")

    Random_Execute(50, 'start_voice_2')
    Voice(0x3, 3697, 0, 0, 0, 0xFE)
    CallReturn()

    label('start_voice_2')

    def labmda_start_voice_2():
        SoundEx(3724, 0)
        Sleep(4800)
        Yield()

        SoundEx(3725, 0)
        Return()

    QueueWorkItem(0xFF, 3, labmda_start_voice_2)
    CallReturn()

    # SysCraft_Init end

    def Craft_SysCraft_Stand(): pass

    label("SysCraft_Stand")

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

    def Craft_SysCraft_Move(): pass

    label("SysCraft_Move")

    SetChrChip(0xFF, 0x1)
    SetChrSubChip(0xFF, 0x0)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(130)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(130)
    Yield()
    Jump("SysCraft_Move")

    # SysCraft_Move end

    def Craft_SysCraft_UnderAttack(): pass

    label("SysCraft_UnderAttack")

    AS_78(1)
    LoadEffect(0x1, "event/ev15061.eff")
    AS_78(0)

    Knockback(0)

    #Jc(0x8, 0x1, 0x0, "under_attack_no_action")
    #BeginChrThread(0xFF, 1, 'SysCraft_Stand', 0)
    #label("under_attack_no_action")

    PlayEffect(0xFF, 0xFF, 1, 0x4, 0, 2000, 0, 0, 0, 0, 500, 500, 500, 4)

    Sleep(500)
    Yield()

    WaitEffect(0xFF, 4)
    Yield()

    EndChrThread(0xFF, 1)
    Return()


    # SysCraft_UnderAttack end

    def Craft_SysCraft_Dead(): pass

    label("SysCraft_Dead")

    for i in range(4):
        ClearMSDataState(1, i, 0x1000)
        SetMSDataState(1, i, 0x4000)


    AS_6C()
    Jc(0x2, 0x2, 0x10, "loc_523")
    Jump("loc_12A")

    label("loc_12A")

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(180)
    Yield()
    Return()

    label("loc_523")

    Jc(0xA, 0x1, 0x2, "loc_538")
    Jc(0xB, 0x1, 0x3, "loc_538")
    Jump("loc_558")

    label("loc_538")

    Voice(0x0, 3693, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x1)
    Sleep(300)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(300)
    Yield()
    SoundEx(514, 0x0)

    label("loc_558")

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(300)
    Yield()
    Sleep(3000)
    Yield()
    Return()

    # SysCraft_Dead end

    label('shadow_chr_init')

    chr_shadow = 0x12

    ChrDuplicate(chr_shadow, 0xFF)
    HideChr(chr_shadow, 0)
    ChrSetPos(chr_shadow, 0xFB, 0, 0, 0)

    CallReturn()


    def Craft_SysCraft_NormalAttack(): pass

    label("SysCraft_NormalAttack")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch03652.itc", 0xFF)
    LoadEffect(0x0, "battle/cr036003.eff")
    LoadEffect(0x1, "battle/cr036001.eff")
    LoadEffect(0x2, "battle/cr034001.eff")
    AS_78(0x0)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 16, 16)
    SetBrightness(0x0, 0x2, 2000)
    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()

    Call('shadow_chr_init')

    Voice(0x0, 3676, 3677, 0, 0, 0xFE)

    SetChrSubChip(0xFF, 0x1)
    Sleep(500)
    Yield()
    ResetLookingTargetData()
    Sleep(100)
    Yield()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(30, 20, 30)
    AS_3D(100, 100, 100, 300)
    PlayEffect(0xFF, 0xFF, 0x1, 0x4, -100, 1100, 600, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(325, 0x0)
    SetChrSubChip(0xFF, 0x2)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    Sleep(100)
    Yield()
    CancelBlur(0)
    Sleep(200)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(chr_shadow, "", 0x0)
    #LookingTarget(50, 25, 35)
    LookingTarget(50, 40, 40)
    Sleep(300)
    Yield()

    AS_3D(100, 100, 100, 300)

    BeginChrThread(0xFF, 1, 'NormalAttack_Damage_Thread', 0)
    Yield()

    WaitChrThread(0xFF, 1)
    Yield()

    CancelEffect(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    ResetBrightness(1000)
    ChrSetPos(chr_shadow, CraftTarget.InitialPos, 0, 0, 0)
    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    AS_6B()
    Return()

    label("NormalAttack_Damage_Thread")

    ResetTarget()

    label("NormalAttack_Damage_Anime_Next")

    ForeachTarget("NormalAttack_Damage_Anime_End")

    PlayEffect(0xFF, 0xFE, 0x0, 0x1, 0, 700, 0, 0, 0, 0, 1200, 1200, 1200, 255)
    PlayEffect(0xFF, 0xFE, 0x2, 0x1, 0, 700, 0, 0, 0, 0, 500, 500, 500, 2)
    AS_67(0x121, 0xFF, 0xFE)

    DamageAnime(0xFE, 0x1, 0x32)
    Sleep(50)
    Yield()

    NextTarget()
    Jump("NormalAttack_Damage_Anime_Next")

    label("NormalAttack_Damage_Anime_End")


    Sleep(50)
    Yield()


    ResetTarget()

    label("NormalAttack_Damage_Next")

    ForeachTarget("NormalAttack_Damage_End")

    DamageCue(0xFE)
    Sleep(50)
    Yield()

    NextTarget()
    Jump("NormalAttack_Damage_Next")

    label("NormalAttack_Damage_End")

    Return()

    # SysCraft_NormalAttack end

    def Craft_SysCraft_ArtsAria(): pass

    label("SysCraft_ArtsAria")

    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    Jc(0x8, 0x1, 0x0, "loc_743")
    Jc(0x2D, 0x1, 0x1, "loc_716")
    PlayEffect(0xFF, 0xFF, 0x80, 0x41, 0, 50, 0, 0, 0, 0, 500, 500, 500, arts_aria_eff_id)
    SetEffectColor(0xFF, 0, 0xFFFF0000)
    Jump("loc_743")

    label("loc_716")

    PlayEffect(0xFF, 0xFF, 0x80, 0x41, 0, 50, 0, 0, 0, 0, 500, 500, 500, arts_aria_eff_id)
    Voice(0x0, 3689, 3690, 0, 0, 0xFE)
    SoundEx(509, 0x0)

    label("loc_743")

    SendMessage(0x1)
    Call("loc_135")
    Return()

    label("loc_135")

    SetChrChip(0xFF, 0x3)

    label("loc_138")

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
    Jump("loc_138")

    # SysCraft_ArtsAria end

    def Craft_SysCraft_ArtsCast(): pass

    label("SysCraft_ArtsCast")

    ResetTarget()
    Jc(0x2D, 0x3, 0x2, "loc_79D")
    Call('arts_cast_prepare')

    label("loc_79D")

    ArtsUsing(0xFFFF)
    ArtsEnd()
    Return()


    label('arts_cast_prepare')
    #PlayEffect(0xFF, 0xF9, 0x81, 0x0, 0, -1000, 0, 0, 0, 0, -1, -1, -1, arts_aria_eff_id)
    CancelEffect(0xFF, arts_aria_eff_id)
    SoundEx(510, 0x0)
    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    Sleep(200)
    Yield()
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x3)
    Sleep(300)
    Yield()
    Voice(0x0, 3691, 3692, 0, 0, 0xFE)
    SetChrSubChip(0xFF, 0x4)
    Sleep(0)
    Yield()

    CallReturn()

    # SysCraft_ArtsCast end

    def SysCraft_Win(): pass

    label('SysCraft_Win')

    LoadChrChip(7, "apl/ch51117.itc", 0xFF)

    SetMSDataState(2, 0xFF, 0x4000)

    SetChrSubChip(0xFF, 0)
    SetChipModeFlags(0x0, CraftTarget.Self, 0x2)
    SetChrChip(CraftTarget.Self, 7)
    ChrSetPos(0xFF, 0xFF, 0, 200, 0)
    Yield()

    SetChrSubChip(0xFF, 0x2)
    Sleep(500)
    Yield()

    SoundEx(898, 0)
    SetChrSubChip(0xFF, 0x1)
    Sleep(150)
    Yield()

    SetChrSubChip(0xFF, 0x0)
    Sleep(300)
    Yield()

    SoundEx(3717, 0)
    Sleep(6000)
    Yield()

    SoundEx(3718, 0)
    Sleep(3000)
    Yield()

    Return()


    def Craft_SysCraft_EnterBattle(): pass

    label("SysCraft_EnterBattle")

    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    Call("loc_50A")
    WaitChrThread(0xFF, 3)
    Yield()
    EndChrThread(0xFF, 1)
    Return()

    # SysCraft_EnterBattle end

    def SysCraft_UseItem(): pass

    label('SysCraft_UseItem')

    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x0)
    Sleep(300)
    Yield()
    Voice(0x0, 3674, 3675, 3683, 0, 0xFE)
    SetChrSubChip(0xFF, 0x4)
    Sleep(300)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x2A, 0x2, 0, 1000, 500, 0, 0, 0, -1, -1, -1, 0xFF)
    Sleep(500)
    Yield()
    UseItemBegin()
    UseItemEnd()
    Return()


    def Craft_SysCraft_Stun(): pass

    label("SysCraft_Stun")

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

    def Craft_SysCraft_Unknown2(): pass

    label("SysCraft_Unknown2")

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    Return()

    # SysCraft_Unknown2 end

    def Craft_SysCraft_Counter(): pass

    label("SysCraft_Counter")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch03652.itc", 0xFF)
    LoadEffect(0x0, "battle/cr036003.eff")
    LoadEffect(0x1, "battle/cr036001.eff")
    LoadEffect(0x2, "battle/cr034001.eff")
    AS_78(0x0)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 16, 16)
    TurnDirection(0xFF, 0xFE, 0, 500, 0x0)
    Voice(0x0, 3696, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(600)
    Yield()
    ResetLookingTargetData()
    Sleep(100)
    Yield()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(30, 20, 30)
    AS_3D(100, 100, 100, 300)
    PlayEffect(0xFF, 0xFF, 0x1, 0x4, -100, 1100, 600, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(325, 0x0)
    SetChrSubChip(0xFF, 0x2)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    Sleep(100)
    Yield()
    CancelBlur(0)
    Sleep(200)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(0xFE, "", 0x0)
    LookingTarget(50, 20, 30)
    Sleep(300)
    Yield()
    AS_3D(100, 100, 100, 300)
    PlayEffect(0xFF, 0xFE, 0x0, 0x1, 0, 700, 0, 0, 0, 0, 1200, 1200, 1200, 255)
    PlayEffect(0xFF, 0xFE, 0x2, 0x1, 0, 700, 0, 0, 0, 0, 500, 500, 500, 2)
    AS_67(0x121, 0xFF, 0xFE)
    DamageAnime(0xFE, 0x1, 0x32)
    Sleep(50)
    Yield()
    DamageCue(0xFE)
    CancelEffect(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    AS_6B()
    Return()

    # SysCraft_Counter end

    def Craft_10_16_8F0_真实之镜(): pass

    label("Craft_10_16_8F0_真实之镜")

    ShowInfoText('　绝对暗示　', 1000)

    AS_6D(0x80000000)
    AS_78(0x1)
    LoadEffect(0x0, "battle/cr036100.eff")
    LoadEffect(0x1, "battle/cr036101.eff")
    AS_78(0x0)
    SetBrightness(0x0, 0x2, 2000)
    AS_6D(0x40000)

    Call('shadow_chr_init')

    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(chr_shadow, "", 0x0)
    LookingTarget(50, 40, 40)

    #TurnDirection(0xFF, chr_shadow, 0, 500, 0x0)

    Voice(0x0, 3678, 0, 0, 0, 0xFE)

    def lambda_set_mirror_thread():
        PlayEffect(0xFF, 0xFF, 0x1, 0x5, 0, 0, 0, 0, 0, 0, 900, 900, 900, 9)
        PlayEffect(0xFF, 0xFF, 0x0, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, -1)
        #AS_67(0xD0, 0xFF, 0xFE)

        Sleep(1700)
        Yield()

        Sleep(1000)
        Yield()

        StopSound(3679)
        SoundEx(3679, 0)

        Random_Execute(50, 'change_from_party_to_enemy')

        ClearMSDataState(1, 0xFF, 0x1000)
        SetMSDataState(1, 0xFF, 0x4000)
        Jump('party_enemy_change_end')

        label('change_from_party_to_enemy')

        ClearMSDataState(1, 0xFF, 0x4000)
        SetMSDataState(1, 0xFF, 0x1000)

        label('party_enemy_change_end')

        Return()


    def lambda_照妖镜_select_target():

        Random_Execute(50, 'lambda_照妖镜_select_target_end')

        QueueWorkItem(0xFE, 3, lambda_set_mirror_thread)
        DamageCue(0xFE)

        label('lambda_照妖镜_select_target_end')

        Yield()


    SoundEx(335, 0x0)
    ForeachTargetEx(lambda_照妖镜_select_target)

    BeginChrThread(0xFF, 1, "loc_135", 0x0)
    Sleep(1700)
    Yield()

    EndChrThread(0xFF, 1)

    SetChrSubChip(0xFF, 0x3)
    Sleep(300)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    SoundEx(325, 0x0)

    Sleep(1000)
    Yield()

    AS_6E(0x80000000)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    AS_14(0x0)
    EndChrThread(0xFF, 1)
    ResetBrightness(1000)
    Sleep(30)
    Yield()
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    Sleep(300)
    Yield()
    FreeEffect(0x0)
    FreeEffect(0x1)
    AS_6B()
    Return()

    # Craft_10_16_8F0_真实之镜 end

    def Craft_11_17_A02_相位重置(): pass

    label("Craft_11_17_A02_相位重置")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch03652.itc", 0xFF)
    LoadEffect(0x1, "battle/cr036200.eff")
    LoadEffect(0x2, "battle/cr036201.eff")
    LoadEffect(0x3, "battle/cr036001.eff")
    AS_78(0x0)
    SetBrightness(0x0, 0x2, 2000)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 20, 30)
    TurnDirection(0xFF, 0xFE, 0, 500, 0x0)
    Voice(0x0, 3680, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(500)
    Yield()
    AS_3D(50, 50, 50, 300)
    PlayEffect(0xFF, 0xFF, 0x3, 0x4, -100, 1000, 600, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(325, 0x0)
    SetChrSubChip(0xFF, 0x2)
    Sleep(300)
    Yield()
    ResetLookingTargetData()
    AS_31(0xB, 0x3E8)
    Sleep(1000)
    Yield()
    ResetTarget()

    label("loc_ABF")

    ForeachTarget("loc_AF6")
    PlayEffect(0xFF, 0xF8, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(190, 0x0)
    BeginChrThread(0xFE, 3, "loc_B7B", 0x0)
    Sleep(100)
    Yield()
    SoundEx(253, 0x0)
    NextTarget()
    Jump("loc_ABF")

    label("loc_AF6")

    AS_14(0x1)
    AS_8D(0x9, 0x6, 0x0, 0x0, 0x0)
    AS_8D(0xA, 0x0, 0x0, 0x0, 0x0)
    Voice(0x0, 3681, 0, 0, 0, 0xFE)
    Sleep(500)
    Yield()
    ResetTarget()

    label("loc_B2C")

    ForeachTarget("loc_B5C")
    PlayEffect(0xFF, 0xF8, 0x2, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(253, 0x0)
    Sleep(100)
    Yield()
    AS_5F(0xFE, 0x1)
    NextTarget()
    Jump("loc_B2C")

    label("loc_B5C")

    AS_14(0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    ResetBrightness(1000)
    FreeEffect(0x1)
    FreeEffect(0x2)
    FreeEffect(0x3)
    AS_6B()
    Return()

    label("loc_B7B")

    Sleep(300)
    Yield()
    AS_60(0xFF)
    Return()

    # Craft_11_17_A02_相位重置 end

    def Craft_12_18_B82_置换(): pass

    label("Craft_12_18_B82_置换")

    AS_78(0x1)
    LoadEffect(0x0, "battle/cr036300.eff")
    LoadEffect(0x1, "battle/cr036303.eff")
    AS_78(0x0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 20, 30)
    SetBrightness(0x0, 0x2, 2000)
    Voice(0x0, 3682, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x3)
    Sleep(750)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    SoundEx(590, 0x0)
    PlayEffect(0xFF, 0xFF, 0x1, 0x1, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    PlayEffect(0xFF, 0xFF, 0x0, 0x1, 0, 1100, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(229, 0x0)
    Sleep(800)
    Yield()
    SetMSDataState(0x2, 0xFF, 0x4000)
    Sleep(1500)
    Yield()

    AS_8D(0x16, 0xFF, CraftConditionFlags.ArtsReflect, 0, 0)
    AS_8D(0x16, 0xFF, CraftConditionFlags.CraftReflect, 0, 0)

    AS_8D(0x15, 0xFF, CraftConditionFlags.ArtsReflect, 0, 9999)
    AS_8D(0x15, 0xFF, CraftConditionFlags.CraftReflect, 0, 1)

    ResetBrightness(1000)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_14(0x0)
    EndChrThread(0xFF, 1)
    FreeEffect(0x0)
    FreeEffect(0x1)
    Return()

    # Craft_12_18_B82_置换 end

    def Craft_13_19_C3D_废话1(): pass

    label("Craft_13_19_C3D_废话1")

    AS_78(0x1)
    LoadEffect(0x0, "battle/cr036301.eff")
    LoadEffect(0x1, "battle/cr036303.eff")
    AS_78(0x0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 20, 30)
    SetBrightness(0x0, 0x2, 2000)
    Voice(0x0, 3683, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x3)
    SoundEx(278, 0x0)
    PlayEffect(0xFF, 0xFF, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    PlayEffect(0xFF, 0xFF, 0x0, 0x1, 0, 1100, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(183, 0x0)
    Sleep(1800)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    SoundEx(211, 0x0)
    AS_27(0x2, 0xFF, 0x4000)
    Sleep(750)
    Yield()
    ResetBrightness(1000)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_14(0x0)
    EndChrThread(0xFF, 1)
    FreeEffect(0x0)
    FreeEffect(0x1)
    Return()

    # Craft_13_19_C3D_废话1 end

    def Craft_14_20_CF8_空间转移(): pass

    label("Craft_14_20_CF8_空间转移")

    AS_78(0x1)
    LoadEffect(0x0, "battle/cr036002.eff")
    AS_78(0x0)
    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 20, 30)
    Sleep(500)
    Yield()
    TurnDirection(0xFF, 0xFD, 180, 500, 0x0)
    Voice(0x0, 3684, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x1)
    SetChrSubChip(0xFF, 0x4)
    PlayEffect(0xFF, 0xFF, 0x0, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(341, 0x0)
    HideChr(0xFF, 300)

    def lambda_D64():
        ChrMove(0xFF, 0xFF, 0, 0, 500, 500, 0x0)
        Return()

    QueueWorkItem(0xFF, 1, lambda_D64)

    Sleep(300)
    Yield()
    AS_60(0xFF)
    WaitChrThread(0xFF, 1)
    AS_14(0x0)
    ResetLookingTargetData()
    #AS_1F(0x1, 0x61A8, 0x0)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    ChrSetPos(0xFF, 0xFB, 0, 0, 0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 20, 30)
    Sleep(500)
    Yield()
    AS_5F(0xFF, 0x0)
    Call('set_spirit_eff')
    ShowChr(0xFF, 300)
    Sleep(300)
    Yield()
    EndChrThread(0xFF, 1)
    FreeEffect(0x0)
    Return()

    # Craft_14_20_CF8_空间转移 end

    def Craft_15_21_DB0_魔反取消(): pass

    label("Craft_15_21_DB0_魔反取消")

    LoadCclm("as03600.dat", 0x15, 0x0, 0x0)
    Jc(0x11, 0x1, 0x0, "loc_DC9")
    Sleep(100)
    Yield()
    Jump("Craft_15_21_DB0_魔反取消")

    label("loc_DC9")

    Voice(0x0, 3675, 0, 0, 0, 0xFE)
    CancelEffect(0xFF, 0xA)
    Sleep(2000)
    Yield()
    AS_8D(0x16, 0xFF, 0x8000000, 0x0, 0x270F)
    SoundEx(640, 0x0)
    UnlockCclm("as03600.dat", 0x15, 0x0, 0x1)
    Return()

    # Craft_15_21_DB0_魔反取消 end

    def Craft_16_22_1360_废话2(): pass

    label("Craft_16_22_1360_废话2")

    ResetTarget()
    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch03652.itc", 0xFF)
    AS_78(0x0)
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(100, 20, 30)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    Voice(0x0, 3674, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(2000)
    Yield()
    SoundEx(590, 0x0)
    SetChrSubChip(0xFF, 0x2)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    AS_6B()
    Return()

    # Craft_16_22_1360_废话2 end

    def Craft_1A_26_DFB_伪盐之桩(): pass

    label("Craft_1A_26_DFB_伪盐之桩")

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch03652.itc", 0xFF)
    LoadEffect(0x0, "eff/cutin36.eff")
    LoadEffect(0x1, "battle/sc036000.eff")
    LoadEffect(0x2, "battle/sc036001.eff")
    LoadEffect(0x3, "battle/sc036002.eff")
    LoadEffect(0x4, "battle/sc036003.eff")
    LoadEffect(0x5, "battle/sc036004.eff")
    LoadEffect(0x6, "battle/cr036001.eff")
    LoadEffect(0x7, "battle/sc036005.eff")
    AS_78(0x0)
    Call("loc_2FC")
    ChrSetPos(0xFF, 0xF3, 0, 0, 0)
    AS_8D(0x1, 0x0, 0x0, 0x0, 0x0)
    AS_03(0xFC, 0xB4)
    ChrSetPos(0xFF, 0xFD, 0, 0, -15000)
    AS_03(0xFF, 0x0)
    HideChr(0xFF, 0)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    AS_5F(0xFF, 0x0)
    AS_34()
    LockCamera(0xFD, 0, 750, -10000, 0)
    SetCameraDistance(12000, 0)
    SetCameraDegree(180, 10, 5, 0)
    AS_AC(0x3E8, 0xFFFFFFFF)
    SetCameraDegree(180, 5, 0, 1500)
    SetCameraDistance(13000, 1500)
    Voice(0x0, 3685, 0, 0, 0, 0xFE)
    PlayEffect(0xFF, 0xFF, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    ShowChr(0xFF, 2000)
    ChrMove(0xFF, 0xFD, 0, 0, -10000, 2000, 0x0)
    SoundEx(239, 0x0)
    EndChrThread(0xFF, 1)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    Sleep(500)
    Yield()
    EndChrThread(0xFF, 1)
    BeginChrThread(0xFF, 1, "loc_135", 0x0)
    Sleep(1500)
    Yield()
    Fade(0x1, 500, 0x0)
    LockCamera(0xFF, 0, 1500, -500, 0)
    SetCameraDegree(135, 15, 10, 0)
    SetCameraDistance(14000, 0)
    LockCamera(0xFF, 0, 2000, 2000, 3500)
    SetCameraDegree(120, 10, 10, 3500)
    SetCameraDistance(17000, 3500)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x2, 0x0, 5000, 2500, -10000, 0, 0, 0, 1000, 1000, 1000, 2)
    SoundEx(272, 0x0)
    Sleep(500)
    Yield()
    AS_3D(30, 30, 30, 2500)
    SoundEx(247, 0x0)
    SoundEx(203, 0x0)
    Sleep(500)
    Yield()
    Voice(0x0, 3686, 0, 0, 0, 0xFE)
    Sleep(2750)
    Yield()
    StopEffect(0xFF, 0x2)
    Fade(0x1, 500, 0x0)
    SetCameraDistance(14000, 1050)
    PlayEffect(0xFF, 0xFF, 0x2, 0x0, 5000, 2500, -2200, 0, 0, 0, 1000, 1000, 1000, 2)
    AS_1A(0xFF, 0x2, 0x2710)
    SoundEx(247, 0x0)
    EndChrThread(0xFF, 1)
    SetChrSubChip(0xFF, 0x3)
    Sleep(1050)
    Yield()
    SetChrSubChip(0xFF, 0x4)
    SoundEx(248, 0x0)
    SetCameraDistance(22000, 300)
    LockCamera(0xFF, 0, 2000, 3000, 300)
    Sleep(500)
    Yield()
    Fade(0x1, 500, 0x0)
    Voice(0x0, 3687, 0, 0, 0, 0xFE)
    AS_60(0xFF)
    AS_34()
    LockCamera(0xFD, 0, 0, 12000, 0)
    SetCameraDegree(155, 10, 10, 0)
    SetCameraDistance(17000, 0)
    AS_3E(0x1F4, 0x0)
    LockCamera(0xFD, 0, 0, 8000, 2200)
    SetCameraDegree(160, 10, 10, 2200)
    SetCameraDistance(16000, 2200)
    AS_3D(50, 50, 50, 1500)
    StopEffect(0xFF, 0x2)
    PlayEffect(0xFF, 0xFD, 0x3, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    SoundEx(175, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x1)
    Sleep(1500)
    Yield()
    AS_3D(120, 120, 120, 500)
    Sleep(500)
    Yield()
    CancelBlur(0)
    Fade(0x1, 500, 0x0)
    AS_60(0xFF)
    AS_5F(0xFC, 0x0)
    AS_34()
    LockCamera(0xF3, 0, 10000, -10000, 0)
    SetCameraDegree(40, 25, -3, 0)
    SetCameraDistance(25000, 0)
    AS_3E(0x3E8, 0x0)
    SetCameraDegree(45, 30, -5, 4000)
    SetCameraDistance(27500, 4000)
    LockCamera(0xF3, 0, 500, 0, 750)
    AS_3E(0x1F4, 0x2EE)
    StopEffect(0xFF, 0x2)
    PlayEffect(0xFF, 0xF3, 0x7, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    Sleep(750)
    Yield()
    AS_3D(300, 300, 300, 700)
    SoundEx(193, 0x0)
    SoundEx(332, 0x0)
    DamageAnime(0xFC, 0x0, 0x32)
    Sleep(700)
    Yield()
    SoundEx(343, 0x0)
    ResetTarget()

    label("loc_11F0")

    ForeachTarget("loc_1226")
    EndChrThread(0xFE, 0)
    Sleep(1)
    Yield()
    BeginChrThread(0xFE, 0, "loc_1359", 0x0)
    PlayEffect(0xFF, 0xFE, 0x4, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    HideChr(0xFE, 2000)
    NextTarget()
    Jump("loc_11F0")

    label("loc_2FC")

    AS_8D(0x4C, 0x0, 0x0, 0x0, 0x0)
    ResetTarget()
    SetBrightness(0x0, 0x0, 0)
    AS_60(0xF7)
    AS_6D(0x40000)
    ClearChipModeFlags(0x0, 0xFF, 0x1)
    CallReturn()

    label("loc_1226")

    AS_3D(50, 50, 50, 2000)
    Sleep(2000)
    Yield()
    Fade(0x1, 500, 0x0)
    Voice(0x0, 3688, 0, 0, 0, 0xFE)
    ChrSetPos(0xFF, 0xF3, -11000, 0, -11000)
    AS_03(0xFF, 0x2D)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_5F(0xFF, 0x0)
    LockCamera(0xF3, 0, 0, 0, 0)
    SetCameraDegree(45, 6, 10, 0)
    SetCameraDistance(23000, 0)
    AS_3E(0x2EE, 0x0)
    SetCameraDistance(23500, 1000)
    Sleep(1750)
    Yield()
    TurnDirection(0xFF, 0xFD, 225, 500, 0x0)
    EndChrThread(0xFF, 1)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(400)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x6, 0x5, -200, 1000, 600, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(325, 0x0)
    SetChrSubChip(0xFF, 0x2)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(300)
    Yield()
    CancelBlur(500)
    SoundEx(344, 0x0)
    Sleep(2000)
    Yield()
    AS_8D(0x8, 0x0, 0x0, 0x0, 0x0)
    Sleep(1)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x5, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(185, 0x0)
    AS_60(0xF7)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    AS_A8(0x0, 0x4)
    AS_A8(0x0, 0x6)
    AS_A8(0x0, 0x7)
    Sleep(1000)
    Yield()
    SoundEx(312, 0x0)
    Sleep(2000)
    Yield()
    AS_43(0x0, 0x0, 0xFFFFFFFF)
    Sleep(100)
    Yield()
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
    ResetBrightness(0)
    Fade(0x1, 500, 0x0)
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

    label("loc_1359")

    SetChrChip(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x0)
    Return()

    # Craft_1A_26_DFB_伪盐之桩 end


    def Craft_玻璃渣(): pass

    label('Craft_玻璃渣')

    桩出现 = 2
    桩移动慢 = 3
    结晶 = 4
    破碎 = 5
    闪光 = 6
    桩插 = 7

    chr_响指 = 7

    AS_78(1)

    LoadChrChip(chr_响指, "chr/ch03652.itc", 0xFF)

    #LoadEffect(桩出现,    "battle/sc036001.eff")
    #LoadEffect(桩移动慢,  "battle/sc036002.eff")
    #LoadEffect(结晶,      "battle/sc036003.eff")
    #LoadEffect(破碎,      "battle/sc036004.eff")
    LoadEffect(闪光,      "battle/cr036001.eff")
    LoadEffect(桩插,      "battle/sc036005.eff")

    AS_78(0)

    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 16, 16)
    SetBrightness(0x0, 0x2, 2000)
    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    SetChrChip(0xFF, chr_响指)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()

    Voice(0x0, 3676, 3677, 0, 0, 0xFE)

    SetChrSubChip(0xFF, 0x1)
    Sleep(500)
    Yield()
    ResetLookingTargetData()
    Sleep(100)
    Yield()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(30, 20, 30)
    AS_3D(100, 100, 100, 300)
    PlayEffect(0xFF, 0xFF, 闪光, 0x4, -100, 1100, 600, 0, 0, 0, 1000, 1000, 1000, -1)
    SoundEx(325, 0x0)
    SetChrSubChip(0xFF, 0x2)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    Sleep(100)
    Yield()
    CancelBlur(0)
    Sleep(200)
    Yield()

    Call('shadow_chr_init')


    LookingTargetAdd(chr_shadow, "", 0x0)
    LookingTarget(50, 40, 40)
    Sleep(300)
    Yield()

    AS_3D(100, 100, 100, 300)

    # PlayEffect(eff_owner, pos, eff_index, flag, x, z, y, degree_vert, degree_horz, unknown, size_x, size_z, size_y, eff_handle)

    loop_count = 15
    interval = 80
    eff_size = 300

    def lambda_Damage_Anime_Thread():

        JumpToLabelIfHasTarget('玻璃渣_Damage_Anime_Thread_Entry')
        Return()

        label("玻璃渣_Damage_Anime_Thread_Entry")

        Sleep(800)
        Yield()

        label("玻璃渣_Damage_Anime_Thread_Start")

        ResetTarget()

        label("玻璃渣_Damage_Anime_Anime_Next")

        ForeachTarget("玻璃渣_Damage_Anime_Anime_End")

        AS_67(0x121, 0xFF, 0xFE)

        DamageAnime(0xFE, 0x1, 0x32)
        DamageCue(0xFE)
        Yield()

        NextTarget()
        Jump("玻璃渣_Damage_Anime_Anime_Next")

        label("玻璃渣_Damage_Anime_Anime_End")

        Sleep(200)
        Yield()
        Jump('玻璃渣_Damage_Anime_Thread_Start')

        Return()


    def lambda_play_sound():
        Sleep(700)
        Yield()

        for i in range(loop_count):
            SoundEx(193, 0x0)
            Sleep(int(interval * 1.2))
            Yield()

        Return()

    Knockback(0)

    QueueWorkItem(0xFF, 1, lambda_Damage_Anime_Thread)
    QueueWorkItem(0xFF, 2, lambda_play_sound)

    Yield()

    for i in range(loop_count):
        random_x = int(random.random() * 10000)
        random_y = int(random.random() * 10000)

        random_x = random_x if random_x <= 4500 else -(10000 - random_x)
        random_y = random_y if random_y <= 4500 else -(10000 - random_y)

        PlayEffect(0xFF, 0xFB, 桩插, 0x4, random_x, -1500, random_y, 10, 0, 0, eff_size, eff_size, eff_size, i)
        Sleep(interval)
        Yield()

    Sleep(600)
    Yield()

    EndChrThread(0xFF, 1)

    Sleep(600)
    Yield()

    for i in range(loop_count):
        CancelEffect(0xFF, i)

    Call('set_spirit_eff')
    Sleep(400)
    Yield()

    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()

    ChrSetPos(chr_shadow, CraftTarget.InitialPos, 0, 0, 0)
    ResetBrightness(1000)
    FreeEffect(桩插)

    Return()


    # Craft_玻璃渣 end

    def Craft_闪电之力(): pass

    label("闪电之力")

    ResetTarget()
    AS_78(1)
    LoadEffect(0x0, "battle\\mg043_00.eff")
    LoadEffect(0x1, "battle\\mg043_01.eff")
    AS_78(0)

    Call('arts_cast_prepare')

    LockCamera(0xF4, 0, 0, 0, 600)
    Sleep(600)
    Yield()
    PlayEffect(0xFF, 0xFB, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 4)

    def attack_anime():
        PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 50, 0, 0, 0, 0, 800, 800, 800, -1)
        DamageAnime(0xFE, 0x0, 0x32)
        Sleep(50)
        Yield()

    ForeachTargetEx(attack_anime)

    Sleep(1700)
    Yield()


    def attack_action():
        PlayEffect(0xFF, 0xFE, 0x1, 0x0, 0, 0, 0, 0, 0, 0, 500, 500, 500, -1)
        DamageAnime(0xFE, 0x0, 0x32)
        DamageCue(0xFE)
        Sleep(50)
        Yield()

    ForeachTargetEx(attack_action)

    WaitEffect(0xFF, 0x4)
    AS_14(0x1)

    FreeEffect(0x0)
    FreeEffect(0x1)

    Return()

    # 闪电之力 end



    def Craft_时空追放(): pass

    label("Craft_时空追放")

    AS_78(0x1)

    LoadChrChip(0x7, "chr/ch03652.itc", 0xFF)
    LoadEffect(0x0, "battle/cr036003.eff")
    LoadEffect(0x1, "battle/cr036001.eff")
    LoadEffect(0x2, "event/ev10002.eff")

    AS_78(0x0)

    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(100, 16, 16)
    SetBrightness(0x0, 0x2, 2000)
    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()

    Call('shadow_chr_init')

    Random_Execute(50, '时空追放_Voice_2')

    Voice(0x0, 3703, 3726, 3683, 0, 0xFE)
    Jump('时空追放_Voice_End')

    label('时空追放_Voice_2')
    Voice(0x0, 3688, 3732, 3735, 0, 0xFE)


    label('时空追放_Voice_End')

    SetChrSubChip(0xFF, 0x1)
    Sleep(500)
    Yield()
    ResetLookingTargetData()
    Sleep(100)
    Yield()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(30, 20, 30)
    AS_3D(100, 100, 100, 300)
    PlayEffect(0xFF, 0xFF, 0x1, 0x4, -100, 1100, 600, 0, 0, 0, 1000, 1000, 1000, 255)
    SoundEx(325, 0x0)
    SetChrSubChip(0xFF, 0x2)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    Sleep(100)
    Yield()
    CancelBlur(0)
    Sleep(200)
    Yield()
    ResetLookingTargetData()
    LookingTargetAdd(chr_shadow, "", 0x0)
    LookingTarget(50, 40, 40)
    Sleep(300)
    Yield()

    AS_3D(100, 100, 100, 300)

    BeginChrThread(0xFF, 1, '时空追放_Damage_Thread', 0)
    Yield()

    WaitChrThread(0xFF, 1)
    Yield()

    Sleep(1000)
    Yield()

    CancelEffect(0xFF, 0x2)
    SetChrSubChip(0xFF, 0x3)
    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 1)
    ResetBrightness(1000)
    ChrSetPos(chr_shadow, CraftTarget.InitialPos, 0, 0, 0)
    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    AS_6B()
    Return()

    ############################################################################

    label("时空追放_Damage_Thread")

    ResetTarget()

    label("时空追放_Damage_Anime_Next")

    ForeachTarget("时空追放_Damage_Anime_End")

    Random_Execute(50, '时空追放_Vanish_Fail')
    BeginChrThread(0xFE, 3, '时空追放_Target_Vanish_Thread', 0)
    DamageCue(0xFE)
    Jump('时空追放_Damage_Anime_Continue')

    label('时空追放_Vanish_Fail')
    #BeginChrThread(0xFE, 3, '时空追放_Target_Vanish_Fail_Thread', 0)

    label("时空追放_Damage_Anime_Continue")

    Yield()

    NextTarget()
    Jump("时空追放_Damage_Anime_Next")

    label("时空追放_Damage_Anime_End")


    Yield()
    Return()

    ############################################################################

    label('时空追放_Target_Vanish_Thread')

    #ClearMSDataState(1, 0xFF, 0x1000)
    #SetMSDataState(1, 0xFF, 0x4000)
    #Return()

    StopSound(4135)
    SoundEx(4135, 0)
    PlayEffect(0xFF, 0xFF, 2, 0x1, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 5)
    HideChr(0xFF, 700)
    Sleep(500)
    Yield()

    CancelEffect(0xFF, 5)
    Sleep(250)
    Yield()

    AS_8D(0x15, 0xFF, CraftConditionFlags.Vanish, 0, 9999)
    Sleep(250)
    Yield()

    Return()

    ############################################################################

    label('时空追放_Target_Vanish_Fail_Thread')

    PlayEffect(0xFF, 0xFF, 2, 0x1, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 5)
    HideChr(0xFF, 700)
    Sleep(1500)
    Yield()

    ShowChr(0xFF, 500)
    Sleep(500)
    Yield()

    CancelEffect(0xFF, 5)
    Sleep(700)
    Yield()

    Return()


    # 时空追放 end



    SaveToFile()

Try(main)
