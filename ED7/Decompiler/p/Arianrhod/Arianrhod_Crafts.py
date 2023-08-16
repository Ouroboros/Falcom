from ActionHelper import *


arts_aria_eff_id = 0

def TeamRushInit():
    LoadChrChip(7, "chr/ch04252.itc", 0xFF)
    Return()

class TeamRushState:

    Prepare         = 1,
    PrepareDone     = 2,
    MoveToTarget    = 3,

def TeamRushAction():

    Call("tr_init_call")

    AS_78(1)
    LoadEffect(0, "battle/ms00001.eff")
    LoadEffect(1, 'event/ev14016.eff')
    AS_78(0)

    AS_89(0xFF)
    AS_83(0x0)
    TurnDirection(0xFF, 0xFE, 0, 500, 0x0)
    AS_05(0xFF, 0x0, 0x0)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)

    #AS_21(0x1, 0xFF, 4000, 12000)
    #ChrTurnAndMove(0x0, CraftTarget.Self, CraftTarget.TargetChr, -1000, 50000)

    EndChrThread(0xFF, 1)
    Jc(0x10, 0x1, 0xFFFFFFFF, "loc_2DA0")
    ResetLookingTargetData()
    AS_36(0xD)
    AS_35(0xFD, 8000, 0, 8000, 3000)
    AS_B0(0xF, 0xBB8)
    SetCameraDistance(18000, 3000)
    Jump("loc_2DAE")

    label("loc_2DA0")

    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0x1F4, 0x8, 0xF)

    label("loc_2DAE")

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    Sleep(70)
    Yield()
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    SoundEx(358, 0x0)
    Sleep(100)
    Yield()

    SendMessage(0x2)

    Voice(0x0, 3859, 3860, 3861, 0, 0xFE)

    SoundEx(287, 0)
    SoundEx(270, 0)
    SoundEx(225, 0)
    SoundEx(833, 0)
    SoundEx(825, 0)

    PlayEffect(0xFF, 0xFF, 0x01, 4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x4)
    PlayEffect(0xFF, 0xFF, 0x82, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    BeginChrThread(0xFF, 1, "tr_attack_anime_thread", 0x0)
    BeginChrThread(0xFF, 2, "tr_damage_anime_thread", 0x0)

    AS_3D(150, 150, 150, 600)
    Sleep(3000)
    Yield()

    EndChrThread(0xFF, 2)
    BeginChrThread(0xFF, 2, "tr_damage_thread", 0x0)
    Sleep(500)
    Yield()

    CancelEffect(0xFF, 0x2)
    CancelEffect(0xFF, 0x4)

    EndChrThread(0xFF, 1)
    EndChrThread(0xFF, 2)
    Yield()

    AS_21(0x1, 0xFF, 300, 20000)
    CancelBlur(0x12C)
    Sleep(100)
    Yield()

    SetChrSubChip(0xFF, 1)
    Sleep(800)
    Yield()

    #ChrJumpBack(1000, 5000)

    SetChrChip(0xFF, 0x0)
    SetChrSubChip(0xFF, 0x0)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    Sleep(500)
    Yield()

    EndChrThread(0xFF, 1)
    FreeEffect(0)
    FreeEffect(1)

    Return()


    label("tr_attack_anime_thread")

    SetChrSubChip(0xFF, 0x4)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x3)
    Sleep(50)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    Sleep(50)
    Yield()
    Jump("tr_attack_anime_thread")



    label("tr_damage_anime_thread")

    ResetTarget()

    label("tr_da_next_target")

    ForeachTarget("tr_da_end_target")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    AS_A7(0xFF, 0x3, 0xFE, 0xFF38, 0x1F4, 0xFF38, 0xC8, 0x3E8, 0xC8, 0x0)
    DamageAnime(0xFE, 0x0, 0x32)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("tr_da_next_target")

    label("tr_da_end_target")

    Sleep(100)
    Yield()
    Jump("tr_damage_anime_thread")


    label("tr_damage_thread")

    ResetTarget()

    label("tr_damage_next_target")

    ForeachTarget("tr_damage_end_target")
    PlayEffect(0xFF, 0xFE, 0x0, 0x0, 0, 500, 0, 0, 0, 0, 500, 500, 500, 0x3)
    AS_A7(0xFF, 0x3, 0xFE, 0xFF38, 0x1F4, 0xFF38, 0xC8, 0x3E8, 0xC8, 0x0)
    DamageAnime(0xFE, 0x0, 0x32)
    DamageCue(0xFE)
    Sleep(100)
    Yield()
    NextTarget()
    Jump("tr_damage_next_target")

    label("tr_damage_end_target")

    Return()


    label("tr_init_call")

    ResetTarget()

    #Voice(0x0, 2056, 2055, 0, 0, 0xFE)

    AS_0E(0x1)

    # if main chr is self, then exec codes between AS_0E(1) and AS_0E(2) ???

    AS_0E(0x2)

    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    HideChr(0xFF, 500)
    ChrMove(0xFF, 0xFD, 8000, 0, 16000, 500, 0x0)
    EndChrThread(0xFF, 1)
    AS_0E(0x3)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    ShowChr(0xFF, 500)

    label("loc_2FA8")

    AS_05(0xFF, 0x4, 0x0)
    AS_21(0x1, 0xFF, 1000, 7500)
    Jc(0x1, 0x4, 0x4, "loc_2FA8")
    Jump("loc_2FC6")

    label("loc_2FC6")

    EndChrThread(0xFF, 1)
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    AS_0E(0x5)
    EndChrThread(0xFF, 1)
    Jc(0x10, 0x1, 0xFFFFFFFF, "loc_300F")
    Sleep(200)
    Yield()
    PlayEffect(0xFF, 0xF9, 0x2, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SoundEx(183, 0x0)
    Sleep(800)
    Yield()

    label("loc_300F")

    CallReturn()


def Dead():

    AS_6C()

    SoundEx(3868, 0)
    SetChrChip(0xFF, 0)
    SetChrSubChip(0xFF, 0)
    Sleep(1000)
    Yield()

    StopSound(3868)
    Yield()

    Return()

def ArtsAria():

    TurnDirection(0xFF, 0xFB, 0x0, 500, 0x0)
    Jc(0x8, 0x1, 0x0, "arts_effect_end")
    Jc(0x2D, 0x1, 0x1, "other_voice")
    PlayEffect(0xFF, 0xFF, 0x80, 0x41, 0, 50, 0, 0, 0, 0, -1, -1, -1, arts_aria_eff_id)
    AS_A9(0xFF, 0x0, 0xFFFF0000)
    Jump("arts_effect_end")

    label("other_voice")

    PlayEffect(0xFF, 0xFF, 0x80, 0x41, 0, 50, 0, 0, 0, 0, -1, -1, -1, arts_aria_eff_id)
    Voice(0x0, 3864, 3883, 3884, 0, 0xFE)
    SoundEx(509, 0x0)

    label("arts_effect_end")

    SendMessage(0x1)
    Call("set_arts_chip")
    Return()

    label("set_arts_chip")

    SetChrChip(0xFF, 0x3)

    label("arts_chip_loop")

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
    Jump("arts_chip_loop")

def ArtsCast():

    Jc(0x2D, 0x3, 0x2, "arts_cast_skip_voice")
    #PlayEffect(0xFF, 0xF9, 0x81, 0x0, 0, 50, 0, 0, 0, 0, -1, -1, -1, 0)
    CancelEffect(0xFF, arts_aria_eff_id)
    SoundEx(510, 0x0)
    TurnDirection(0xFF, 0xFB, 0, 500, 0x0)
    Sleep(200)
    Yield()
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x3)
    Sleep(300)
    Yield()
    Voice(0x0, 3875, 3876, 0, 0, 0xFE)
    SetChrSubChip(0xFF, 0x4)
    Sleep(0)
    Yield()

    label("arts_cast_skip_voice")

    ArtsUsing(0xFFFF)
    ArtsEnd()
    Return()

def EnterBattle():
    BeginChrThread(0xFF, 1, "SysCraft_Stand", 0x0)
    Voice(0x0, 3881, 3882, 0, 0, 0xFE)
    Yield()
    EndChrThread(0xFF, 1)
    Return()

def UnderAttack():
    AS_78(1)

    LoadEffect(1, "eff/trapdmg2.eff")

    AS_78(0)

    Knockback(0)
    #SoundEx(511, 0)
    SoundEx(115, 0)
    PlayEffect(0xFF, 0xFF, 1, 0, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SetChrChip(CraftTarget.Self, 4)
    SetChrSubChip(CraftTarget.Self, 3)
    Sleep(1000)
    Yield()

    FreeEffect(1)

def BattleWin():

    #LoadChrChip(7, "apl/ch51408.itc", 0xFF)
    LoadChrChip(8, "chr/ch0355A.itc", 0xFF)
    #LoadEffect(1, 'event/ev14015.eff')

    Voice(0x0, 3868, 0, 0, 0, 0xFE)

    SetChipModeFlags(0x0, CraftTarget.Self, 0x2)
    SetChrChip(CraftTarget.Self, 8)
    SetChrSubChip(CraftTarget.Self, 13)
    Sleep(2000)
    Yield()

    Seq = \
    [
        (12, 100),
        (11, 100),
        (10, 100),
        (9, 100),
        (8, 100),
        (7, 100),
        (6, 100),
        (5, 100),
        (4, 100),
        (3, 100),
        (2, 800),
        (1, 100),
        (0, 100),
    ]

    for x in Seq:
        SetChrSubChip(CraftTarget.Self, x[0])
        Sleep(x[1])
        Yield()

    Return()

def UseItem():
    SetChrChip(0xFF, 0x3)
    SetChrSubChip(0xFF, 0x0)
    Sleep(300)
    Yield()
    Voice(0x0, 3881, 3906, 0, 0, 0xFE)
    SetChrSubChip(0xFF, 0x4)
    Sleep(300)
    Yield()
    PlayEffect(0xFF, 0xFF, 0x2A, 0x2, 0, 1000, 500, 0, 0, 0, 65535, 65535, 65535, 0xFF)
    Sleep(500)
    Yield()
    UseItemBegin()
    UseItemEnd()
    Return()


def Longinus(enemy_version = False):

    #enemy_version = True

    chip_gun        = 9
    chip_attack     = 8
    chip_raise_gun  = 7

    eff_cloud       = 0
    eff_lightning   = 1
    eff_beam        = 2
    eff_boom        = 3
    eff_damage      = 4
    eff_gun_appear  = 5
    eff_gun_falldown= 6

    chr_gun         = 0x12

    show_lightning_thread   = GenerateUniqueLable()
    damage_thread           = GenerateUniqueLable()
    continue_find_target    = GenerateUniqueLable()

    if enemy_version:
        AS_5F(0xFF, 0)
        for i in range(17):
            AS_5F(i, 0)

        Yield()

    AS_78(0x1)

    LoadChrChip(chip_gun,       "apl/ch51544.itc", 0xFF)
    LoadChrChip(chip_raise_gun, "chr/ch04257.itc", 0xFF)

    LoadEffect(eff_cloud,       "battle/cr035200.eff")
    LoadEffect(eff_lightning,   "battle/cr035201.eff")
    LoadEffect(eff_beam,        "event/ev15100.eff")
    LoadEffect(eff_boom,        "event/ev15101.eff")
    LoadEffect(eff_damage,      "battle/cr035202.eff")
    LoadEffect(eff_gun_appear,  "event/ev14015.eff")
    LoadEffect(eff_gun_falldown,"battle/sc031004.eff")

    AS_78(0)

    if enemy_version:

        continue_find_target    = GenerateUniqueLable()
        next_target             = GenerateUniqueLable()
        end_of_loop_target      = GenerateUniqueLable()
        target_found            = GenerateUniqueLable()
        target_not_found        = GenerateUniqueLable()


        label(continue_find_target)

        ResetTarget()

        label(next_target)
        ForeachTarget(end_of_loop_target)

        Random_Execute(75, target_not_found)
        Jump(target_found)
        label(target_not_found)

        NextTarget()
        Jump(next_target)

        label(end_of_loop_target)

        Jump(continue_find_target)


        label(target_found)

        TargetPos = CraftTarget.TargetChr
        TargetChr = CraftTarget.TargetChr

    else:

        TargetPos = CraftTarget.TargetPos
        TargetChr = CraftTarget.TargetChr


    TurnDirection(CraftTarget.Self, TargetPos, 0x0, 400, 0x0)

    height = 33000

    Fade(1, 500, 0)
    LockCamera(TargetPos, 0, 750, 0, 500)
    SetCameraDistance(height + 1000, 0)
    SetCameraDistance(height, 500)
    Yield()

    Voice(0x0, 3864, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    SoundEx(358, 0x0)
    Sleep(1000)
    Yield()

    gun_height = 6500

    ChrDuplicate(chr_gun, 0xFF)
    HideChr(chr_gun, 0)
    AS_8D(0x7, chr_gun, 3000, 3000, 3000)

    ChrSetPos(chr_gun, TargetPos, 0, gun_height, 0)
    SetChrChip(chr_gun, chip_gun)
    SetChrSubChip(chr_gun, 0)

    BeginChrThread(0xFF, 1, show_lightning_thread, 0)
    Sleep(1200)
    Yield()

    SoundEx(970, 0)
    SoundEx(920, 0)
    SoundEx(202, 0)
    PlayEffect(chr_gun, chr_gun, eff_gun_appear, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, eff_gun_appear)
    ShowChr(chr_gun, 500)
    Sleep(500)
    Yield()

    EndChrThread(0xFF, 1)
    CancelEffect(CraftTarget.Self, eff_lightning)

    SoundEx(288, 0)
    PlayEffect(0xFF, TargetPos, eff_beam, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, eff_beam)
    PlayEffect(0xFF, TargetPos, eff_boom, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, eff_boom)

    if not enemy_version:
        PlayEffect(0xFF, TargetPos, eff_gun_falldown, 0, 0, 4000, 0, 90, 0, 0, 800, 800, 800, eff_gun_falldown)

    ChrMove(chr_gun, chr_gun, 0, -gun_height - 10000, 0, 70, 0)
    Sleep(70)
    Yield()

    if enemy_version:
        Fade(1, 500, 0)
        LockCamera(TargetPos, 0, 750, 0, 500)
        SetCameraDistance(21000, 0)
        SetCameraDistance(20000, 500)
        Yield()

    BeginChrThread(CraftTarget.Self, 1, damage_thread, 0)
    WaitChrThread(CraftTarget.Self, 1)
    WaitEffect(-1, eff_beam)

    HideChr(chr_gun, 0)
    Sleep(500)
    Yield()

    CancelEffect(-1, eff_boom)
    Sleep(1000)
    Yield()

    ChrSetPos(chr_gun, CraftTarget.InitialPos, 0, 0, 0)
    FreeEffect(eff_cloud)
    FreeEffect(eff_lightning)
    FreeEffect(eff_beam)
    FreeEffect(eff_boom)
    FreeEffect(eff_damage)
    FreeEffect(eff_gun_appear)
    FreeEffect(eff_gun_falldown)

    Return()

    ####################################################################

    label(show_lightning_thread)

    StopEffect(0xFF, eff_lightning)
    PlayEffect(0xFF, TargetPos, eff_lightning, 0, 0, -3200, -500, 0, 0, 0, 1000, 1000, 1000, eff_lightning)
    Sleep(1700)
    Yield()

    Jump(show_lightning_thread)

    #####################################################################

    label(damage_thread)

    next_target = GenerateUniqueLable()
    end_of_loop = GenerateUniqueLable()
    next_damage = GenerateUniqueLable()
    no_dead     = GenerateUniqueLable()
    damage_end  = GenerateUniqueLable()


    if not enemy_version:

        label(next_damage)

        ResetTarget()

        label(next_target)
        ForeachTarget(end_of_loop)


    PlayEffect(CraftTarget.Self, TargetChr, eff_damage, 1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    DamageAnime(TargetChr, 0, 50)

    if enemy_version:

        Random_Execute(50, no_dead)
        AS_8D(0x15, TargetChr, CraftConditionFlags.OnehitKill, 0, 0)
        Jump(damage_end)

        label(no_dead)

        DamageCue(TargetChr)

        label(damage_end)

    else:

        Random_Execute(90, no_dead)

        AS_8D(0x15, TargetChr, CraftConditionFlags.OnehitKill, 0, 0)
        Jump(damage_end)

        label(no_dead)

        DamageCue(TargetChr)

        label(damage_end)

    Sleep(50)
    Yield()

    if not enemy_version:

        NextTarget()
        Jump(next_target)

        label(end_of_loop)


    Return()




def EnumaElish():

    chip_raise_gun  = 7
    chip_attack     = 8

    eff_whirl       = 8

    eff_whirl_layers = 2

    loop_sound_thread   = GenerateUniqueLable()

    AS_78(0x1)

    LoadChrChip(chip_raise_gun, "chr/ch04257.itc", 0xFF)
    LoadChrChip(chip_attack,    "chr/ch04252.itc", 0xFF)
    LoadEffect(eff_whirl,       "battle/cr034201.eff")

    AS_78(0x0)

    ClearChipModeFlags(0x0, 0xFF, 0x2)

    TurnDirection(CraftTarget.Self, CraftTarget.TargetPos, 0x0, 1500, 0x0)
    Sleep(50)
    Yield()

    Voice(0x0, 3857, 0, 0, 0, 0xFE)
    Sleep(2500)
    Yield()

    SetChrChip(0xFF, chip_raise_gun)

    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    SoundEx(358, 0x0)
    Sleep(1500)
    Yield()

    SoundEx(207, 0)

    for i in range(300, 1100, 100):
        PlayEffect(0xFF, 0xFF, eff_whirl, 0x04, 0, 0, -1800, 90, 0, 0, i, i, i, eff_whirl)
        Sleep(400)
        Yield()

    BeginChrThread(CraftTarget.Self, 1, loop_sound_thread, 0)

    SoundEx(288, 0)
    SoundEx(308, 0)
    SoundEx(358, 0)

    Voice(0, 3872, 0, 0, 0, 0xFE)
    SetChrChip(-1, chip_attack)
    SetChrSubChip(-1, 1)
    Yield()

    Fade(0x1, 1000, 0x0)
    Yield()


    for size in range(1100, 3000, 200):
        for i in range(eff_whirl_layers):
            PlayEffect(0xFF, 0xFF, eff_whirl, 0x04, 0, -1300, 0, 180, 0, 0, size, size, size, eff_whirl + i)
            Sleep(200)
            Yield()

    #Sleep(4000)
    #Yield()

    SetChrSubChip(0xFF, 4)
    Yield()
    Voice(0, 3873, 0, 0, 0, 0xFE)

    Call('ea_1_cancel_all_layers')

    SoundEx(358, 0x0)

    PlayEffect(0xFF, 0xFF, eff_whirl, 0x04, 0, -1300, 0, 180, 0, 0, 5000, 5000, 5000, eff_whirl)
    EndChrThread(CraftTarget.Self, 1)

    import ea_2
    ea_2.ea_2()

    #CancelEffect(CraftTarget.Self, eff_whirl)
    #Yield()

    #for i in range(2200, 0, -200):
    #    PlayEffect(0xFF, 0xFF, eff_whirl, 0x04, 0, -1300, 0, 180, 0, 0, i, i, i, eff_whirl)
    #    Sleep(50)
    #    Yield()

    WaitChrThread(CraftTarget.Self, 1)

    #CancelEffect(CraftTarget.Self, eff_whirl)
    Sleep(1300)
    Yield()

    FreeEffect(eff_whirl)

    Return()


    ##############################################################################

    label('ea_1_cancel_all_layers')

    for i in range(eff_whirl_layers):
        CancelEffect(CraftTarget.Self, eff_whirl + i)

    Yield()

    CallReturn()


    ##############################################################################

    label(loop_sound_thread)
    SoundEx(175, 0)
    Sleep(2700)
    Yield()

    Jump(loop_sound_thread)


def unmask(enemy_version = False):

    AS_78(0x1)
    LoadChrChip(7, "chr/ch0355A.itc", 0xFF)
    LoadEffect(0x0, "battle/cr035400.eff")
    AS_78(0x0)

    Fade(0x1, 500, 0x0)
    SetChipModeFlags(0x0, 0xFF, 0x2)

    AS_34()
    LockCamera(0xFF, 0, 750, 0, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 500)

    Voice(0x0, 3868, 0, 0, 0, 0xFE)


    SetChipModeFlags(0x0, CraftTarget.Self, 0x2)
    SetChrChip(CraftTarget.Self, 7)
    SetChrSubChip(CraftTarget.Self, 13)
    Sleep(2000)
    Yield()

    Seq = \
    [
        (12, 100),
        (11, 100),
        (10, 100),
        (9, 100),
        (8, 100),
        (7, 100),
        (6, 100),
        (5, 100),
        (4, 100),
        (3, 100),
        (2, 1000),
    ]

    for x in Seq:
        SetChrSubChip(CraftTarget.Self, x[0])
        Sleep(x[1])
        Yield()

    SoundEx(158, 0x0)
    for i in range(2, 14):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(100)
        Yield()

    SetBrightness(0x0, 0x2, 0x7D0)
    Voice(0x0, 3869, 0, 0, 0, 0xFE)
    #SetChrChip(0xFF, 0x7)

    SetChrSubChip(0xFF, 14)

    Sleep(100)
    Yield()
    BeginChrThread(0xFF, 1, "boost_thread", 0x0)
    SoundEx(366, 0x0)
    SetCameraDistance(16000, 2000)
    AS_3D(100, 100, 100, 2000)
    AS_7F(0x7D0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    PlayEffect(0xFF, 0xFF, 0x0, 0x1, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0x2)
    Sleep(2000)
    Yield()
    AS_7F(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    CancelBlur(0x3E8)
    SetCameraDistance(21000, 100)
    AS_3D(500, 500, 500, 500)
    SoundEx(321, 0x0)
    Sleep(500)
    Yield()

    SoundEx(881, 0x0)
    EndChrThread(0xFF, 1)
    Yield()

    class BuffInfo:
        def __init__(self, rate, time, prob, flag):
            self.Rate           = rate
            self.Time           = time
            self.Probability    = prob
            self.Flag           = flag

    if enemy_version:

        BuffUp = \
        [
            BuffInfo(100,       10,     50,     CraftConditionFlags.Str),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Def),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Ats),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Adf),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Dex),
            BuffInfo(10,        10,     50,     CraftConditionFlags.Agl),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Mov),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Spd),
            BuffInfo(1,         1,      50,     CraftConditionFlags.MaxGuard),
        ]

    else:

        BuffUp = \
        [
            BuffInfo(100,       10,     50,     CraftConditionFlags.Str),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Def),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Ats),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Adf),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Dex),
            BuffInfo(10,        10,     50,     CraftConditionFlags.Agl),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Mov),
            BuffInfo(100,       10,     50,     CraftConditionFlags.Spd),
            BuffInfo(100,       3,      50,     CraftConditionFlags.HPRecovery),
            BuffInfo(100,       3,      50,     CraftConditionFlags.CPRecovery),
            BuffInfo(1,         1,      50,     CraftConditionFlags.MaxGuard),
        ]

    Sleep(2000)
    Yield()

    CancelEffect(0xFF, 0x2)

    ConditionFlags = 0

    for buf in BuffUp:
        ConditionFlags |= buf.Flag
        AS_8D(0x4B, CraftTarget.Self, buf.Flag, 0, 0)

        no_buff = GenerateUniqueLable()

        if enemy_version:
            Random_Execute(100 - buf.Probability, no_buff)

        AS_8D(0x15, CraftTarget.Self, buf.Flag, buf.Rate, buf.Time)
        label(no_buff)

    ConditionFlags &= ~ (CraftConditionFlags.MaxGuard | CraftConditionFlags.HPRecovery | CraftConditionFlags.CPRecovery)
    PlayEffectIfConditionExist(CraftTarget.Self, ConditionFlags, 0x83, '')

    Sleep(500)
    Yield()

    FreeEffect(0x0)
    AS_6B()
    ResetBrightness(1000)
    Fade(0x1, 0x1F4, 0x0)
    AS_31(0x17, 0x0)
    ClearChipModeFlags(0x0, 0xFF, 0x2)
    SetChrChip(0xFF, 0)
    SetChrSubChip(0xFF, 5)
    Yield()
    Return()

    if not enemy_version:
        label("boost_thread")

        SetChrSubChip(0xFF, 0xF)
        Sleep(100)
        Yield()
        SetChrSubChip(0xFF, 0x11)
        Sleep(100)
        Yield()
        SetChrSubChip(0xFF, 0x10)
        Sleep(100)
        Yield()
        Jump("boost_thread")

        Return()


def Craft_暴雨疾风枪():

    attack_chip = 7

    eff_cutin       = 0
    eff_gun         = 1
    eff_knock_back  = 2
    eff_dash        = 3

    jump_sound = 844
    dash_sound = 250


    AS_78(0x1)

    LoadChrChip(attack_chip, "chr/ch04252.itc", 0xFF)

    LoadEffect(eff_cutin,       "eff/cutin42.eff")
    LoadEffect(eff_gun,         'event/ev14016.eff')
    LoadEffect(eff_knock_back,  'battle/ms00001.eff')
    LoadEffect(eff_dash,        "battle/cr024400.eff")

    AS_78(0x0)

    TurnDirection(CraftTarget.Self, CraftTarget.TargetPos, 0x0, 1500, 0x0)
    SoundEx(531, 0x0)
    Sleep(50)
    Yield()

    SetChrChip(CraftTarget.Self, attack_chip)
    SetChrSubChip(CraftTarget.Self, 0)
    Sleep(100)
    Yield()

    SetChrSubChip(CraftTarget.Self, 1)
    Sleep(200)
    Yield()

    SoundEx(548, 0x0)
    SoundEx(203, 0x0)
    PlayEffect(0xFF, 0xFF, 0x83, 0x41, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 1)
    AS_35(0xFF, 0, 750, 0, 1000)
    SetCameraDistance(17000, 1000)

    Voice(0x0, 3891, 0, 0, 0, 0xFE)
    Yield()

    PlayEffect(CraftTarget.Self, 0xFD, eff_cutin, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    WaitEffect(0xFF, 0x2)
    CancelBlur(0)
    Yield()

    SetChrChip(CraftTarget.Self, attack_chip)
    SetChrSubChip(CraftTarget.Self, 1)
    Sleep(1000)
    Yield()

    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(0x64, 0x14, 0x1E)

    PlayEffect(0xFF, 0xFF, eff_dash, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)

    SoundEx(dash_sound, 0)
    ShowChrTrails(CraftTarget.Self, 100, 300)
    ChrTurnAndMove(0x0, CraftTarget.Self, CraftTarget.TargetPos, -2000, 50000)
    Sleep(100)
    Yield()
    HideChrTrails(CraftTarget.Self)



    label('call_暴雨疾风枪')

    attack_thread           = GenerateUniqueLable()
    play_sound_thread       = GenerateUniqueLable()
    damage_thread           = GenerateUniqueLable()
    damage_anime_thread     = GenerateUniqueLable()
    knock_back_eff_thread   = GenerateUniqueLable()

    attack_thread_id            = 1
    play_sound_thread_id        = 2
    damage_thread_id            = 3
    damage_anime_thread_id      = 1
    knock_back_eff_thread_id    = 1

    BeginChrThread(CraftTarget.Self, attack_thread_id,      attack_thread, 0x0)
    BeginChrThread(CraftTarget.Self, play_sound_thread_id,  play_sound_thread, 0x0)
    BeginChrThread(CraftTarget.Self, damage_thread_id,      damage_thread, 0x0)

    Sleep(2000)
    Yield()

    CancelEffect(CraftTarget.Self, 2)
    #Sleep(50)
    Yield()


    EndChrThread(CraftTarget.Self, attack_thread_id)
    EndChrThread(CraftTarget.Self, damage_thread_id)
    WaitChrThread(CraftTarget.Self, play_sound_thread_id)

    BeginChrThread(CraftTarget.Self, damage_anime_thread_id, damage_anime_thread, 0)

    SetChrSubChip(CraftTarget.Self, 1)
    Sleep(800)
    Yield()

    EndChrThread(CraftTarget.Self, damage_anime_thread_id)

    Knockback(3)
    BeginChrThread(CraftTarget.Self, knock_back_eff_thread_id, knock_back_eff_thread, 0)
    SetChrSubChip(CraftTarget.Self, 5)

    CancelEffect(CraftTarget.Self, 1)
    SoundEx(jump_sound, 0x0)
    ShowChrTrails(CraftTarget.Self, 100, 300)
    ChrJump(CraftTarget.Self, 0xF0, 0, 0, 0, 300, 3000)
    Sleep(100)
    Yield()

    SetChrChip(CraftTarget.Self, 0)
    SetChrSubChip(CraftTarget.Self, 0)
    Sleep(400)
    Yield()

    HideChrTrails(CraftTarget.Self)
    WaitChrThread(CraftTarget.Self, knock_back_eff_thread_id)

    FreeEffect(eff_cutin)
    FreeEffect(eff_gun)
    FreeEffect(eff_knock_back)

    Return()

    #################################################

    label(attack_thread)
    PlayEffect(CraftTarget.Self, CraftTarget.Self, eff_gun, 4, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 2)

    SetChrChip(CraftTarget.Self, attack_chip)

    attack_thread_loop = attack_thread + 'loop'
    label(attack_thread_loop)

    for i in range(2, 5):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(50)
        Yield()

    Jump(attack_thread_loop)


    #################################################

    label(damage_thread)

    next_target = GenerateUniqueLable()
    end_of_loop = GenerateUniqueLable()
    next_damage = GenerateUniqueLable()

    label(next_damage)

    ResetTarget()

    label(next_target)

    ForeachTarget(end_of_loop)
    AS_8D(0x4B, CraftTarget.TargetChr, CraftConditionFlags.MaxGuard, 0, 0)
    AS_8D(0x4B, CraftTarget.TargetChr, CraftConditionFlags.CraftGuard, 0, 0)

    PlayEffect(CraftTarget.Self, CraftTarget.TargetChr, eff_knock_back, 1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    DamageAnime(CraftTarget.TargetChr, 0, 50)
    DamageCue(CraftTarget.TargetChr)
    Sleep(50)
    Yield()
    NextTarget()
    Jump(next_target)

    label(end_of_loop)

    Sleep(180)
    Yield()
    Jump(next_damage)

    #########################################################

    label(play_sound_thread)

    SoundEx(287, 0)
    SoundEx(270, 0)
    SoundEx(225, 0)
    SoundEx(833, 0)
    SoundEx(825, 0)
    Sleep(1000)
    Yield()

    SoundEx(271, 0)
    SoundEx(287, 0)
    Sleep(1000)
    Yield()

    StopSound(225)
    StopSound(825)

    Return()


    ####################################################

    label(damage_anime_thread)

    has_target = GenerateUniqueLable()
    JumpToLabelIfHasTarget(has_target)
    Return()

    label(has_target)

    next_target = GenerateUniqueLable()
    end_of_loop = GenerateUniqueLable()
    next_damage = GenerateUniqueLable()

    label(next_damage)

    ResetTarget()

    label(next_target)

    ForeachTarget(end_of_loop)
    DamageAnime(CraftTarget.TargetChr, 0, 50)
    Sleep(50)
    Yield()
    NextTarget()
    Jump(next_target)

    label(end_of_loop)

    Jump(next_damage)


    ##############################################################

    label(knock_back_eff_thread)

    has_target = GenerateUniqueLable()
    JumpToLabelIfHasTarget(has_target)
    Return()

    label(has_target)

    next_target = GenerateUniqueLable()
    end_of_loop = GenerateUniqueLable()
    next_damage = GenerateUniqueLable()
    no_stun     = GenerateUniqueLable()

    label(next_damage)

    SoundEx(369, 0)
    ResetTarget()

    label(next_target)

    ForeachTarget(end_of_loop)
    PlayEffect(CraftTarget.Self, CraftTarget.TargetChr, eff_knock_back, 1, 0, 800, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF)
    DamageAnime(CraftTarget.TargetChr, 1, 50)

    Random_Execute(90, no_stun)

    AS_8D(0x15, CraftTarget.TargetChr, CraftConditionFlags.Stun, 0, 5)

    label(no_stun)

    Sleep(50)
    Yield()
    NextTarget()
    Jump(next_target)

    label(end_of_loop)

    Return()


def Craft_大地轰雷锤(enemy_version = False):

    AS_78(0x1)
    LoadChrChip(0x7, "chr/ch04257.itc", 0xFF)
    LoadEffect(0x0, "battle/cr035200.eff")
    LoadEffect(0x1, "battle/cr035201.eff")
    LoadEffect(0x2, "battle/cr035202.eff")
    AS_78(0x0)

    damage_thread = GenerateUniqueLable()

    ResetTarget()
    AS_83(0x0)
    SetBrightness(0x0, 0x2, 0x7D0)
    Voice(0x0, 3864, 0, 0, 0, 0xFE)
    SetChrChip(0xFF, 0x7)
    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    SoundEx(358, 0x0)
    AS_95()
    AS_34()
    LockCamera(0xFF, 0, 3000, 0, 1000)
    AS_3B(20000, 1000)
    Sleep(1000)
    Yield()
    PlayEffect(0xFF, 0xFD, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x2)
    SoundEx(167, 0x0)
    Sleep(1500)
    Yield()
    Voice(0x0, 3865, 0, 0, 0, 0xFE)
    Sleep(750)
    Yield()

    PlayEffect(0xFF, 0xFF, 0x1, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    AS_3D(50, 50, 50, 1700)
    Sleep(1700)
    Yield()
    StopEffect(0xFF, 0x2)
    LockCamera(0xFF, 0, 1500, 0, 100)
    Sleep(80)
    Yield()
    AS_95()
    AS_96(0xFF, "", 0x0)
    AS_96(0xFC, "", 0x0)
    AS_97(0x32, 0x14, 0x1E)
    Sleep(500)
    Yield()

    BeginChrThread(0xFF, 1, damage_thread, 0x0)
    AS_14(0x1)
    BeginChrThread(0xFF, 2, "SysCraft_Stand", 0x0)
    AS_8F(0x0)
    EndChrThread(0xFF, 2)
    ResetBrightness(0x3E8)
    FreeEffect(0x0)
    FreeEffect(0x1)
    FreeEffect(0x2)
    AS_6B()
    Return()

    label(damage_thread)

    if enemy_version:
        for i in range(8):
            AS_8D(0x4B, i, CraftConditionFlags.Stealth, 0, 0)
    else:
        for i in range(8, 16):
            AS_8D(0x4B, i, CraftConditionFlags.Stealth, 0, 0)


    end_find_target     = GenerateUniqueLable()
    find_next_target    = GenerateUniqueLable()


    ResetTarget()

    label(find_next_target)

    ForeachTarget(end_find_target)
    PlayEffect(0xFF, 0xFE, 0x2, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    DamageAnime(0xFE, 0x1, 0x32)
    DamageCue(0xFE)
    Sleep(50)
    Yield()
    NextTarget()
    Jump(find_next_target)

    label(end_find_target)

    Return()

def 零时迷子():

    rei_ji_mai_go = GenerateUniqueLable()

    JumpToLabelIfHasTarget('rei_ji_mai_go_has_target')
    Return()

    label('rei_ji_mai_go_has_target')

    chip_raise_gun  = 7

    eff_bs890010    = 0
    eff_com000      = 1
    eff_bs890011    = 2
    eff_bs884013    = 3

    AS_78(0x1)

    LoadChrChip(chip_raise_gun, "chr/ch04257.itc", 0xFF)

    LoadEffect(eff_bs890010, "battle/bs890010.eff")
    LoadEffect(eff_com000, "battle/com000.eff")
    LoadEffect(eff_bs890011, "battle/bs890011.eff")
    LoadEffect(eff_bs884013, "battle/bs884013.eff")

    AS_78(0x0)

    Call('common_init_camera')

    Voice(0x0, 3858, 3857, 3881, 0, 0xFE)

    SetChrChip(0xFF, chip_raise_gun)

    SetChrSubChip(0xFF, 0x0)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x1)
    Sleep(100)
    Yield()
    SetChrSubChip(0xFF, 0x2)
    SoundEx(358, 0x0)
    Sleep(1000)
    Yield()

    Call(rei_ji_mai_go)

    ReiJiMaiGo()
    WaitEffect(0xff, 3)
    Yield()

    FreeEffect(eff_bs890010)
    FreeEffect(eff_com000)
    FreeEffect(eff_bs890011)
    FreeEffect(eff_bs884013)

    Return()


    label('common_init_camera')

    height = 43000

    Fade(1, 500, 0)
    LockCamera(-1, 0, 750, 0, 500)
    SetCameraDistance(height + 1000, 0)
    SetCameraDistance(height, 500)
    Yield()

    CallReturn()


    label(rei_ji_mai_go)

    height = 6000

    PlayEffect(0xFF, 0xFF, eff_bs884013, 0x0, 0, height, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF)
    SoundEx(688, 0x0)
    Sleep(200)
    Yield()
    PlayEffect(0xFF, 0xFF, eff_bs890010, 0x0, 0, height, 0, 0, 0, 0, 400, 400, 400, 0x3)
    SoundEx(687, 0x1)
    Sleep(1000)
    Yield()
    SoundEx(682, 0x0)
    Sleep(500)
    Yield()
    Fade(0x1, 500, 0x0)
    SetBattleSpeed(700)
    Sleep(200)
    Yield()
    Sleep(500)
    Yield()
    SoundEx(697, 0x1)
    Sleep(1000)
    Yield()
    AS_A0(0x2, 0x400)
    SoundEx(695, 0x0)
    StopSound(687)
    StopSound(697)
    SetBattleSpeed(80)
    Sleep(180)
    Yield()
    SetBattleSpeed(800)
    PlayEffect(0xFF, 0xFF, eff_com000, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x4)
    AS_A9(0xFF, 0x4, 0xFF6E6E6E)
    PlayEffect(0xFF, 0xFF, eff_bs890011, 0x0, 0, 0, 0, 65511, 180, 0, 3000, 3000, 3000, 0x5)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    SetCameraDistance(55000, 5000)
    Fade(0x1, 500, 0x0)
    AS_A0(0x3, 0x400)
    SoundEx(698, 0x0)
    SoundEx(687, 0x1)
    Sleep(500)
    Yield()
    SoundEx(697, 0x1)
    Sleep(1300)
    Yield()
    SoundEx(680, 0x0)
    Sleep(1200)
    Yield()
    SoundEx(689, 0x0)
    Sleep(500)
    Yield()
    AS_43(0x0, 0x320, 0xFFFFFFFF)
    SetBattleSpeed(1000)
    CancelBlur(0x3E8)
    Sleep(2000)
    Yield()
    StopEffect(0xFF, 4)
    StopEffect(0xFF, 5)

    AS_5F(0xF7, 0x1)

    StopSound(697)
    Call('common_init_camera')

    SoundEx(680, 0x0)
    SoundEx(682, 0x0)
    StopSound(687)

    CancelEffect(0xFF, 0x6)
    SoundEx(680, 0x0)

    ResetBrightness(0)

    CallReturn()


def 神速():

    fade_time = 600

    AS_78(1)
    LoadEffect(1, "event/ev202_00.eff")
    AS_78(0)

    ChrSetPos(0x11, 0xFF, 0, 0, 0)

    BeginChrThread(0xFF, 2, "SysCraft_Stand", 0x0)

    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTarget(0x64, 0x14, 0x1E)

    Voice(0x0, 3858, 0, 0, 0, 0xFE)

    HideChr(-1, fade_time)
    PlayEffect(0xFF, 0xFF, 1, 0, 0, 650, 0, 0, 0, 0, 1000, 1000, 1000, 1)

    Sleep(fade_time)
    Yield()

    ChrSetPos(-1, CraftTarget.TargetPos, 0, 0, 0)
    TurnDirection(-1, 0x11, 0, 0, 0x0)

    ShowChr(-1, fade_time)
    PlayEffect(0xFF, 0xFF, 1, 0, 0, 650, 0, 0, 0, 0, 1000, 1000, 1000, 2)

    BeginChrThread(0xFF, 1, "loc_17C", 0x0)

    Sleep(fade_time)
    Yield()

    CancelEffect(-1, 1)
    CancelEffect(-1, 2)
    WaitChrThread(-1, 1)

    ChrSetPos(0x11, CraftTarget.InitialPos, 0, 0, 0)

    Sleep(fade_time)
    Yield()

    EndChrThread(-1, 2)
    Yield()

