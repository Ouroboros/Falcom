from Cassius import *

def main():
    Self = CraftTarget.Self
    TargetChr = CraftTarget.TargetChr
    TargetPos = CraftTarget.TargetPos

    attackChip      = 7

    showEff         = 0
    ShinraTenseiEff = 1
    ShinraTenseiEarthEff = 2

    effList = [
        showEff,
        ShinraTenseiEff,
    ]

    ResetTarget()

    with ResourceLock:
        LoadEffect(showEff,                 "battle/cr007200.eff")
        LoadEffect(ShinraTenseiEff,         "battle/cr94670a.eff")
        LoadEffect(ShinraTenseiEarthEff,    "battle/cr94670b.eff")

    PlayBGM(0, 9999)

    ResetLookingTargetData()
    LookingTargetAdd(Self, "", 0x0)
    LookingTarget(2000, 38, 0)
    SetChrChip(0xFF, 5)
    SetChrSubChip(0xFF, 0)
    Sleep(800)
    Yield()

    # SoundEx(卡西乌斯_YAREYARE, 0)
    Sleep(500)
    Yield()

    HideChr(CraftTarget.Self, 300)
    SoundEx(卡西乌斯_音效_雷光击_现身, 0)
    PlayEffect(0xFF, 0xFF, showEff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    Sleep(300)
    Yield()
    ChrMove(Self, TargetPos, 0, 3000, 0, 0, 0)
    Sleep(500)
    Yield()

    def ariaThread():
        label('神罗天征_ariaThread')
        for i in range(0, 4):
            SetChrSubChip(Self, i)
            Sleep(130)
            Yield()
        Jump('神罗天征_ariaThread')

    SetChrChip(Self, 3)
    QueueWorkItem(Self, 1, ariaThread)

    ShowChr(Self, 200)
    ChrMove(Self, TargetPos, 0, 4000, 0, 500, 0)
    Sleep(2000)
    Yield()
    PlayEffect(Self, Self, ShinraTenseiEff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
    Sleep(300)
    Yield()

    SoundEx(687, 0x1)
    SoundEx(693, 0x1)
    Voice(0, 卡西乌斯_神罗天征_ここより, 0, 0, 0, 0xFE)
    Sleep(3100)
    Yield()

    Voice(0, 卡西乌斯_神罗天征_世界に痛みを, 0, 0, 0, 0xFE)
    Sleep(6200 - 3100)
    Yield()

    Voice(0, 卡西乌斯_神罗天征, 0, 0, 0, 0xFE)
    EndChrThread(Self, 1)
    SetChrChip(Self, 3)
    SetChrSubChip(Self, 4)
    Sleep(100)
    Yield()

    def damageThread():
        Sleep(300)
        Yield()

        label('continue_attack')

        def damage():
            Knockback(1)
            DamageAnime(CraftTarget.TargetChr, 1, 50)
            DamageCue(CraftTarget.TargetChr)
            Yield()

        ForeachTargetEx(damage)

        Sleep(50)
        Jump('continue_attack')

    QueueWorkItem(Self, 1, damageThread)
    SetChrSubChip(Self, 5)
    StopSound(693)
    StopSound(687)
    for i in range(10):
        PlayEffect(Self, TargetPos, ShinraTenseiEarthEff, 0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF)
        Sleep(200)
        Yield()
        SoundEx(248, 0x0)

    EndChrThread(Self, 1)
    Sleep(2000)
    Yield()

    SetChrSubChip(Self, 4)
    HideChr(Self, 200)
    Sleep(200)
    Yield()

    ChrMove(Self, 0xF0, 0, 1000, 0, 0, 0)
    SetChrChip(Self, 5)
    SetChrSubChip(Self, 0)
    Sleep(800)
    Yield()

    ShowChr(Self, 200)
    ChrMove(Self, 0xF0, 0, 0, 0, 500, 0)
    Sleep(1000)
    Yield()

    for eff in effList:
        FreeEffect(eff)

    return
