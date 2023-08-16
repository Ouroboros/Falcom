from Cassius import *

def main():
    attackChip      = 7

    showupEff       = 0
    turnAroundEff   = 1
    kickEff         = 2
    hitEff          = 3

    effList = [
        showupEff,
        turnAroundEff,
        kickEff,
        hitEff,
    ]

    with ResourceLock:
        LoadEffect(showupEff,       "battle/cr007200.eff")
        LoadEffect(turnAroundEff,   "battle/cr007100.eff")
        LoadEffect(kickEff,         "battle/cr007400.eff")
        LoadEffect(hitEff,          "battle/ms00000.eff")
        LoadChrChip(attackChip,     CHR_Cassius_Attack, 0xFF)

    # ResetLookingTargetData()
    # LookingTargetAdd(0xFF, "", 0x0)
    # LookingTarget(2000, 1000, 1200)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    AS_89(0xFF)
    AS_83(0)

    PlayEffect(0xFF, 0xFF, turnAroundEff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SoundEx(卡西乌斯_音效_雷光击_旋转, 0)
    SoundEx(卡西乌斯_音效_雷光击_起跳, 0)
    SetChrChip(CraftTarget.Self, attackChip)

    for i in range(4):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(30)
        Yield()

    HideChr(CraftTarget.Self, 300)

    for i in range(6):
        AS_04(CraftTarget.Self, 1, -45)
        Sleep(20)
        Yield()

    AS_60(CraftTarget.Self)

    Voice(0, 卡西乌斯_攻击7, 0, 0, 0, 0xFE)
    LockCamera(0xF8, 0, 0, 0, 2000)
    Sleep(1000)
    Yield()

    SoundEx(卡西乌斯_音效_雷光击_移动, 0)
    # eff 4

    Knockback(2)
    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTargetAdd(CraftTarget.Self, "", 0x0)
    LookingTarget(100, 20, 30)

    def damage():
        PlayEffect(0xFF, 0xF9, kickEff, 0x400, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
        ChrMove(CraftTarget.Self, CraftTarget.TargetChr, 0, 0, 0, 50, 0)
        PlayEffect(0xFF, 0xF8, hitEff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
        AS_8D(0x1F, CraftTarget.Self, 0xF0, 0x0, 0x0)
        SoundEx(卡西乌斯_音效_雷光击_击中, 0)
        DamageAnime(CraftTarget.TargetChr, 0, 50)
        DamageCue(CraftTarget.TargetChr)
        LockCamera(0xF8, 0, 0, 0, 100)
        Sleep(50)
        Yield()

    ForeachTargetEx(damage)

    # CancelEffect(CraftTarget.Self, 4)
    Sleep(500)
    Yield()

    ResetTarget()

    AS_5F(CraftTarget.Self, 0x0)
    HideChr(CraftTarget.Self, 0)
    ShowChr(CraftTarget.Self, 500)
    SetChrChip(CraftTarget.Self, attackChip)
    SetChrSubChip(CraftTarget.Self, 6)
    Sleep(0)
    Yield()

    SetChrChip(CraftTarget.Self, 3)
    SetChrSubChip(CraftTarget.Self, 0)
    AS_0A(CraftTarget.Self, 1, 0, 0)
    ChrSetPos(CraftTarget.Self, 0xF0, 0, 0, 0)
    Yield()

    PlayEffect(0xFF, 0xFF, showupEff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    SoundEx(卡西乌斯_音效_雷光击_现身, 0)

    TurnDirection(CraftTarget.Self, CraftTarget.TargetChr, 0, 0, 0x0)
    ShowChr(CraftTarget.Self, 100)
    Sleep(800)
    Yield()

    for eff in effList:
        FreeEffect(eff)
