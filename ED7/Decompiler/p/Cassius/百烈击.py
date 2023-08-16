from Cassius import *

def main():
    chip = 7
    attackChip = 8
    hitEff = 0
    criticalHitEff = 1
    preCriticalHitEff = 2

    effList = [hitEff, criticalHitEff, preCriticalHitEff]

    with ResourceLock:
        LoadChrChip(chip,               CHR_Cassius_BaiLieJi, 0xFF)
        LoadChrChip(attackChip,         CHR_Cassius_Attack, 0xFF)
        LoadEffect(hitEff,              "battle/ms00001.eff")
        LoadEffect(criticalHitEff,      "battle/cr006402.eff")
        LoadEffect(preCriticalHitEff,   "battle/cr006401.eff")

    ResetTarget()
    ResetLookingTargetData()
    LookingTargetAdd(0xFF, "", 0x0)
    LookingTargetAdd(0xFC, "", 0x0)
    LookingTarget(100, 20, 30)
    BeginChrThread(0xFF, 1, "SysCraft_Move", 0x0)
    AS_1E(0xFFFFFFFF)
    EndChrThread(0xFF, 1)
    TurnDirection(0xFF, 0xFE, 0, 0, 0x0)
    AS_6D(0x200000)
    AS_89(0xFF)

    SetChrChip(CraftTarget.Self, chip)
    Voice(0, 卡西乌斯_百烈击, 0, 0, 0, 0xFE)
    for t in range(12):
        for i in range(3):
            SetChrSubChip(CraftTarget.Self, i)
            Sleep(40)
            Yield()

        SoundEx(卡西乌斯_音效_百烈击, 0)

        if t % 2 == 0:
            DamageAnime(CraftTarget.TargetChr, 0, 0x32)
            DamageCue(CraftTarget.TargetChr)
            PlayEffect(0xFF, 0xFE, hitEff, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, -1)

    DamageAnime(CraftTarget.TargetChr, 0, 0x32)
    DamageCue(CraftTarget.TargetChr)
    SetChrChip(CraftTarget.Self, attackChip)
    SetChrSubChip(CraftTarget.Self, 0x0)
    Yield()

    PlayEffect(0xFF, 0xFF, preCriticalHitEff, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 2)
    Sleep(200)
    Yield()

    SoundEx(183, 0)
    BeginChrThread(CraftTarget.Self, 1, "shake_self", 0x0)
    Sleep(0xA)
    Yield()
    Sleep(0x1F4)
    Yield()
    Voice(0, 卡西乌斯_百烈击2, 0, 0, 0, 0xFE)

    for i in range(1, 7):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(0x32)
        Yield()

    Knockback(8)
    DamageAnime(CraftTarget.TargetChr, 1, 0x32)
    DamageCue(0xFE)
    SetCondition(CraftTarget.TargetChr, CraftConditionFlags.Stun, 90, 1)
    SoundEx(卡西乌斯_音效_百烈击_结尾, 0)
    PlayEffect(0xFF, 0xFF, criticalHitEff, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 3)

    SetChrSubChip(CraftTarget.Self, 0x7)
    Sleep(0x32)
    Yield()

    SetChrSubChip(CraftTarget.Self, 0x8)
    Sleep(0x5DC)
    Yield()

    for i in range(9, 12):
        SetChrSubChip(CraftTarget.Self, i)
        Sleep(0x32)
        Yield()

    AS_14(0x2)

    for eff in effList:
        FreeEffect(eff)

    Return()

    label('shake_self')

    for _ in range(4):
        ShakeChr(CraftTarget.Self, -50, 0x0, -50)
        Sleep(0x1E)
        Yield()
        ShakeChr(CraftTarget.Self, 0x0, 0x0, 0x0)
        Sleep(0x1E)
        Yield()

    Jump('shake_self')