@_MOD 16
"万象天引"

;ED6SE145.WAV   ED6SE186.WAV    20044

@_MOD 16
#Craft_18
;AddEff(0x0:s, "magic\\mg070_0.eff")
Turn(Self, Dest, 200:s)
SelectChip(Self, 6:b)
SubChip(Self, 0:b)
Voice(0x792:s)
Sleep(1400)
Update
SubChip(Self, 1:b)
Update

SetAngleTarget(0xFC:b, "", 0x0:s)
SetAngleTarget(Self, "", 0x0:s)
MoveAngle(0x1F4:i, 2100:s, 3000:s)

Random(0x14:b, 0x4:b, 20:i, BANSHOU_THROW:s)

SeEx(0x91:s, 0:b)
SetBattleMode(0x2:b, 0x400:i)

#BANSHOU_RAISE
LoopTargetBegin(BANSHOU_RAISE_END:s)
Turn(Target, Self, 0x0:s)
OP_89(Target)
SuspendThread(Target, 0xFF:b)
SelectChip(Target, 0x3:b)
SubChip(Target, 0x0:b)
Move(Target, Target, 0x0:i, 500:i, 0:i, 32:i, 0x0:b)
Update
LoopTargetEnd
Goto(BANSHOU_RAISE:s)

#BANSHOU_RAISE_END

BeginThread(Self, Thread1, BANSHOU_SLIDE:s, 0:b)
OP_8D(0:b, 33:s, 0:b, Dest, Self, 0:s, 0:i, 0:i, 0:b)
OP_8D(0x9:b, 0x3:i, 15000:i, 0x0:i, 0x0:i)
OP_8D(0xA:b, 0:i, 0:i, 0x0:i, 0x0:i)
SuspendThread(Self, Thread1)
SetBattleSpeed(1000:i)
Sleep(500)
Update
ResetLoopTarget
Random(0x14:b, 0x4:b, 50:i, BANSHOU_NOT_BEAT:s)
BeatBack(1:b)
Update

#BANSHOU_BEAT
LoopTargetBegin(BANSHOU_BEAT_END:s)
BeginThread(Target, Thread1, BANSHOU_JUMP:s, 0:b)
Damage(Target)
Sleep(0x32:i)
Update
LoopTargetEnd
Goto(BANSHOU_BEAT:s)

#BANSHOU_BEAT_END

SetBattleMode(0x3:b, 0x400:i)

#BANSHOU_COMMON_END

Sleep(1000)
Update
End

#BANSHOU_NOT_BEAT
LoopTargetBegin(BANSHOU_NOT_BEAT_END:s)
ResetChipStatus(Target)
Update
LoopTargetEnd
Goto(BANSHOU_NOT_BEAT:s)

#BANSHOU_NOT_BEAT_END
Goto(BANSHOU_BEAT_END:s)

#BANSHOU_JUMP
JumpBack(10:s, 450:s)
DamageAnime(Self, 0x1:b, 0x32:i)
WaitThread(Self, CurThread)
ResetChipStatus(Self)
Update
End

#BANSHOU_SLIDE
SetBattleSpeed(100:i)
Sleep(30)
Update
SetBattleSpeed(200:i)
Sleep(50)
Update
SetBattleSpeed(300:i)
Sleep(70)
Update
SetBattleSpeed(400:i)
Sleep(90)
Update
SetBattleSpeed(500:i)
Sleep(110)
Update
SetBattleSpeed(600:i)
Sleep(130)
Update
SetBattleSpeed(700:i)
Sleep(150)
Update
SetBattleSpeed(800:i)
Sleep(180)
Update
SetBattleSpeed(900:i)
Sleep(210)
Update
SetBattleSpeed(1000:i)
Sleep(250)
Update
WaitThread(Self, CurThread)
Update
End

#BANSHOU_THROW

Random(0x14:b, 0x4:b, 00:i, BANSHOU_ROCK:s)

LoadSChip(0xC:b, 0x00260422:i, 0x00260427:i)
Clone(Clone1, Self)
Hide(Clone1, 0:i)
Teleport(Clone1, Dest, 0:i, 20000:i, 0:i)
SetChipModeFlag(0:b, Clone1, 2:s)
SelectChip(Clone1, 0xC:b)
SubChip(Clone1, 7:b)
OP_8D(0x7:b, Clone1:i, 20000:i, 20000:i, 10000:i)
Update
Show(Clone1, 500:i)
Sleep(1000:i)
Update
TipText("肾斗士似乎领悟了什么...", 2000:i)
DropDown(Clone1, 0x0:i, -20000:i, 0x0:i, 0x0:s, 0x1F40:s)
ShakeScreen(2000:i, 2000:i, 2000:i, 500:i)
Update
Hide(Clone1, 3000:i)
BeatBack(0:b)
ResetLoopTarget

#BANSHOU_GANG_KUI
LoopTargetBegin(BANSHOU_BEAT_END:s)
OP_8D(0x7:b, Target:i, 1000:i, 600:i, 1000:i)
DamageAnime(Target, 0x1:b, 50:i)
Damage(Target)
Sleep(0x32:i)
Update
LoopTargetEnd
Goto(BANSHOU_GANG_KUI:s)

Update
End

#BANSHOU_ROCK
OP_78(0x1:b)
AddEff(0x0:s, "magic\\mg013_0.eff")
OP_78(0x0:b)
KeepAngle(Dest, 0x0:i, 0x0:i, 0x0:i, 0x258:i)
Sleep(0x190:i)
Update
ShowEff(0x1:b, 0xFF:b, Dest, 0x0:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 3000:s, 3000:s, 3000:s, 0x0:b)
WaitEff(Self, 0x0:b)
ReleaseEff(0x0:s)
End




