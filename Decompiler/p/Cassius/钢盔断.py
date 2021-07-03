from Cassius import *

def main():
    Self = CraftTarget.Self
    TargetChr = CraftTarget.TargetChr
    TargetPos = CraftTarget.TargetPos

    attackChip      = 7

    hitEff          = 0
    earthEff        = 1

    effList = [
        hitEff,
        earthEff,
    ]

    ResetTarget()

    with ResourceLock:
        LoadEffect(hitEff,      "battle/ms00000.eff")
        LoadEffect(earthEff,    "battle/cr432000.eff")
        LoadChrChip(attackChip, CHR_Cassius_Attack, 0xFF)

    ResetLookingTargetData()
    LookingTargetAdd(Self, "", 0x0)
    LookingTarget(500, 0x8, 0xF)
    Sleep(50)
    Yield()

    TurnDirection(Self, TargetPos, 0, 0, 0x0)
    SetChrChip(Self, attackChip)
    SetChrSubChip(Self, 5)
    Sleep(60)
    Yield()

    SetChrSubChip(Self, 8)
    Sleep(100)
    Yield()

    ShakeScreen(200, 200, 200, 500)
    # jump eff
    # jump eff

    Voice(0, 卡西乌斯_钢盔断_起跳, 0, 0, 0, 0xFE)
    SoundEx(卡西乌斯_音效_钢盔断_起跳, 0)
    ShowChrTrails(Self, 50, 200)

    def attackInTheSky():

        # SetChrSubChip(Self, 6)
        # Sleep(60)
        # Yield()
        SetChrSubChip(Self, 7)
        Sleep(30)
        Yield()
        SetChrSubChip(Self, 8)
        Sleep(500)
        Yield()

        for i in range(9, 12):
            SetChrSubChip(Self, i)
            Sleep(50)
            Yield()

        Return()

    def jumpInTheSky():
        SetChrSubChip(Self, 6)
        Sleep(598)
        Yield()
        SetChrSubChip(Self, 5)
        Sleep(100)
        Yield()
        SetChrSubChip(Self, 4)
        Sleep(100)
        Yield()
        SetChrSubChip(Self, 5)
        Sleep(100)
        Yield()
        Return()

    QueueWorkItem(Self, 1, jumpInTheSky)
    ChrJump(Self, Self, 0, 0, 0, 3000, 2000)
    WaitChrThread(Self, 1)

    QueueWorkItem(Self, 1, attackInTheSky)
    Sleep(10)
    Yield()

    PlayEffect(Self, Self, earthEff, 5, 0, 0, 0, 0, 0, 0, 800, 2000, 800, 0xFF)
    PlayEffect(Self, Self, earthEff, 5, 1000, 0, 0, 0, 0, 0, 800, 2000, 800, 0xFF)
    PlayEffect(Self, Self, earthEff, 5, -1000, 0, 0, 0, 0, 0, 800, 2000, 800, 0xFF)
    Sleep(10)
    Yield()

    SoundEx(256, 0)

    HideChrTrails(Self)
    ShakeScreen(200, 200, 200, 500)
    # CancelEffect(Self, jump eff 2)
    BlurSwitch(0, 0xBBFFFFFF, 0, 1, 3)

    def damage():
        Sleep(100)
        Yield()

        SortTarget(0)

        def damageloop():
            TurnDirection(TargetChr, Self, 0, 0, 0x0)

            def underattack():
                EndChrThread(Self, 0)
                SetChrChip(0xFF, 0x2)
                SetChrSubChip(0xFF, 0x0)

                AS_89(Self)
                ChrJump(Self, Self, 0, 0, 0, 3000, 1000)
                # ChrMove(Self, 0xF0, 0, 0, 0, 0, 0)
                AS_9C(Self)
                Yield()
                Return()

            QueueWorkItem(TargetChr, 1, underattack)

            PlayEffect(TargetChr, TargetChr, hitEff, 3, 0, -500, 0, 0, 0, 0, 500, 500, 500, 0xFF)
            Yield()

        ForeachTargetEx(damageloop)

        WaitChrThread(0xFC, 1)
        WaitChrThread(0xFC, 2)

        def damageloop():
            WaitChrThread(TargetChr, 1)
            DamageCue(TargetChr)
            Yield()

        ForeachTargetEx(damageloop)

        AS_8F(0)
        Return()

    ResetLookingTargetData()
    LookingTargetAdd(0xFC, "", 0)
    LookingTargetAdd(Self, "", 0)
    LookingTarget(500, 20, 20)
    CancelBlur(1500)

    # QueueWorkItem(Self, 2, damage)
    # Sleep(500)
    damage()
    Yield()

    WaitChrThread(Self, 1)
    WaitChrThread(Self, 2)
    SetChrChip(Self, 0)
    SetChrSubChip(Self, 0)
    Sleep(500)
    Yield()

    for eff in effList:
        FreeEffect(eff)
