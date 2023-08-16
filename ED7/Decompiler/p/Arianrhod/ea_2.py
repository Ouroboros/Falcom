from ActionHelper import *

def ea_2():

    eff_mg064_00    = 3
    eff_mg064_01    = 4
    eff_mg064_02    = 5
    eff_mg064_04    = 6
    eff_mg064_05    = 7
    eff_sc036000    = 8
    eff_ms00001     = 9
    eff_whirl       = eff_sc036000

    AS_78(0x1)

    LoadEffect(eff_mg064_00,    "battle\mg064_00.eff")
    LoadEffect(eff_mg064_01,    "battle\mg064_01.eff")
    LoadEffect(eff_mg064_02,    "battle\mg064_02.eff")
    LoadEffect(eff_mg064_04,    "battle\mg064_04.eff")
    LoadEffect(eff_mg064_05,    "battle\mg064_05.eff")
    #LoadEffect(eff_sc036000,    "battle/sc036000.eff")
    LoadEffect(eff_ms00001,     "battle/ms00001.eff")

    AS_78(0x0)

    ResetTarget()

    Call("init_env")

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
    PlayEffect(0xFF, 0xFF, eff_sc036000, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x4)
    AS_A9(0xFF, 0x81, 0xFFFCDE69)
    Sleep(700)
    Yield()
    PlayEffect(0xFF, 0xF3, eff_mg064_04, 0x0, 0, 3000, 0, 0, 0, 0, 400, 400, 400, 0x3)
    SoundEx(359, 0x1)
    Sleep(800)
    Yield()

    CancelEffect(0xFF, 0x3)
    StopSound(359)
    Sleep(500)
    Yield()
    PlayEffect(0xFF, 0xF3, eff_ms00001, 0x0, 0, 4000, 10000, 0, 0, 0, 1800, 1800, 1800, 0xFF)
    AS_A9(0xFF, 0x81, 0xFFDD71F9)
    CancelEffect(0xFF, 0x4)
    Sleep(1500)
    Yield()
    SetBattleSpeed(0x352)
    PlayEffect(0xFF, 0xF3, eff_mg064_00, 0x0, 0, 4000, 9500, 0, 0, 0, 500, 500, 500, 0x2)
    SetCameraDistance(19000, 2200)
    SetBattleSpeed(0x28A)
    Sleep(2600)
    Yield()
    PlayEffect(0xFF, 0xF3, eff_mg064_01, 0x0, 0, 4000, 10000, 0, 0, 0, 400, 400, 400, 0xFF)
    Sleep(200)
    Yield()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    ResetTarget()

    label("loc_xxxxxxxxxxxx_37D8")

    ForeachTarget("loc_xxxxxxxxxxxx_3802")

    def lambda_37DF():
        ChrMove(0xFF, 0xF3, 0, 3500, 10000, 3000, 0x0)
        Return()

    QueueWorkItem(0xFE, 1, lambda_37DF)
    BeginChrThread(0xFE, 3, "loc_xxxxxxxxxxxx_393C", 0x0)
    Sleep(30)
    Yield()
    NextTarget()
    Jump("loc_xxxxxxxxxxxx_37D8")

    label("loc_xxxxxxxxxxxx_3802")

    Sleep(2300)
    Yield()
    PlayEffect(0xFF, 0xF3, eff_mg064_05, 0x0, 0, 3500, 9500, 0, 0, 0, 500, 500, 500, 0x2)
    Sleep(2000)
    Yield()
    AS_A8(0x0, 0x3)
    Sleep(400)
    Yield()
    AS_A8(0x0, 0x1)
    #PlayEffect(0xFF, 0xF3, eff_sc036000, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    AS_A9(0xFF, 0x81, 0xFFFCDE69)
    SoundEx(359, 0x1)
    AS_A6(0xFF, 0x2, 0x2EE, 0x640, 0x0)
    SoundEx(269, 0x0)
    AS_80(0x3E8)
    Sleep(500)
    Yield()
    StopSound(359)
    SetBattleSpeed(0x3E8)
    PlayEffect(0xFF, 0xF3, eff_ms00001, 0x0, 0, 4000, 10000, 0, 0, 0, 3000, 3000, 3000, 0xFF)
    SoundEx(566, 0x0)
    Sleep(100)
    Yield()
    PlayEffect(0xFF, 0xF3, eff_mg064_02, 0x0, 0, 3500, 9500, 65516, 0, 0, 750, 750, 750, 0x3)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    SetCameraDistance(4000, 2000)
    AS_3E(0x3E8, 0x7D0)
    SetBattleSpeed(0x320)
    SoundEx(220, 0x0)
    Sleep(1000)
    Yield()
    CancelEffect(0xFF, 0x2)
    Sleep(1000)
    Yield()
    AS_80(0x3E8)
    AS_43(0x0, 0x1F4, 0xFFFFFFFF)
    Sleep(1000)
    Yield()
    SetBattleSpeed(0x3E8)
    AS_8D(0xA, 0x0, 0x0, 0x0, 0x0)
    AS_A8(0x0, 0x0)
    AS_A8(0x0, 0x1)
    AS_A8(0x0, 0x2)
    AS_A8(0x0, 0x3)
    AS_A8(0x0, 0x4)
    AS_A8(0x0, 0x5)
    AS_A8(0x0, 0x6)
    AS_A8(0x0, 0x7)
    Call("release_all_eff")
    AS_6E(0x40000)

    Call("reset_all_chr_and_others")

    #EndChrThread(0xFC, 1)
    Call("loc_xxxxxxxxxxxx_1CA")
    #Return()

    Jump('ea_2_end')


    ##############################################################


    label('recycle_whirl')

    SetChrSubChip(0xFF, 1)
    for i in range(2200, 0, -200):
        PlayEffect(0xFF, 0xFF, eff_whirl, 0x04, 0, -1300, 0, 180, 0, 0, i, i, i, eff_whirl)
        Sleep(100)
        Yield()

    CancelEffect(CraftTarget.Self, eff_whirl)
    Return()

    label("reset_all_chr_and_others")

    #CancelEffect(CraftTarget.Self, eff_whirl)
    #Yield()
    PlayEffect(0xFF, 0xFF, eff_whirl, 0x04, 0, -1300, 0, 180, 0, 0, 2500, 2500, 2500, eff_whirl)
    BeginChrThread(CraftTarget.Self, 1, 'recycle_whirl', 0)

    Fade(0x1, 500, 0x0)
    AS_7A(0x1)
    ShowChr(0xFF, 0)
    AS_5F(0xF7, 0x0)
    ResetBrightness(0)
    #SetBrightness(0x0, 0x1, 0)
    AS_31(0x17, 0x0)
    AS_31(0x3, 0x0)

    Fade(1, 500, 0)
    LockCamera(0xFC, 0, 750, 0, 500)
    SetCameraDistance(51000, 0)
    SetCameraDistance(50000, 500)
    Yield()

    Call("ea_2_do_damage")
    AS_8F(0x0)
    CallReturn()

    ##############################################################

    label("ea_2_do_damage")

    ResetTarget()

    vanish_all_target = GenerateUniqueLable()
    vanish_next_target = GenerateUniqueLable()

    Random_Execute(10, vanish_all_target)

    label("ea_2_damage_next_target")

    ForeachTarget("ea_2_do_damage_end")
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump("ea_2_damage_next_target")

    label("ea_2_do_damage_end")

    CallReturn()


    label(vanish_all_target)

    label(vanish_next_target)

    ForeachTarget("ea_2_do_damage_end")

    AS_8D(0x15, CraftTarget.TargetChr, CraftConditionFlags.OnehitKill, 0, 0)
    AS_8D(0x15, CraftTarget.TargetChr, CraftConditionFlags.Vanish, 0, 9999)

    Sleep(50)
    Yield()

    NextTarget()
    Jump(vanish_next_target)


    ##############################################################

    label("loc_xxxxxxxxxxxx_1CA")

    AS_6E(0x20000)
    AS_6E(0x40000)
    CallReturn()


    ##############################################################

    label("release_all_eff")

    FreeEffect(eff_mg064_00)
    FreeEffect(eff_mg064_01)
    FreeEffect(eff_mg064_02)
    FreeEffect(eff_mg064_04)
    FreeEffect(eff_mg064_05)
    #FreeEffect(eff_sc036000)
    FreeEffect(eff_ms00001)

    CallReturn()


    ##############################################################

    label("loc_xxxxxxxxxxxx_393C")

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


    ##############################################################

    label("init_env")

    AS_43(0x0, 0x1F4, 0xFF000000)
    Sleep(500)
    Yield()
    SetBrightness(0x0, 0x0, 0)
    AS_6D(0x20000)
    AS_6D(0x40000)
    AS_60(0xF7)
    Fade(0x0, 500, 0xFF000000)
    CallReturn()


    label('ea_2_end')

    return

