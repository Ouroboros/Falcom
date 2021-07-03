@_MOD 16
"ÉñÁ_ÌìÕ÷"

@_MOD 16
#Craft_13
;OP_89(Self)
;OP_F(0xA:s, 0x7:s)
;OP_10(2000:s, 3000:s)
;Sleep(2000)
;End

AddEff(0x0:s, "monster\\\\ms04671a.eff")
AddEff(0x106:s, "monster\\ms31004a.eff")
SelectChip(Self, 0x6:b)
SubChip(Self, 0x0:b)
Sleep(500:i)
Update
ShowEff(0x1:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x0:b)
Sleep(800)
Update

Voice(0x793:s)
OP_8D(0x15:b, Self:i, 0x00010000:i, 0x64:i, 0x270F:i)
Update
OP_8D(0x15:b, Self:i, 0x00040000:i, 0x64:i, 0x270F:i)
Update
OP_8D(0x15:b, Self:i, 0x40000000:i, 0x64:i, 0x270F:i)
Update
OP_8D(0x15:b, Self:i, 0x00400000:i, 0x64:i, 0x270F:i)
Update
OP_8D(0x15:b, Self:i, 0x00100000:i, 0x64:i, 0x270F:i)
Update
OP_8D(0x15:b, Self:i, 0x01000000:i, 0x64:i, 0x270F:i)
Update
OP_8D(0x15:b, Self:i, 0x00004000:i, 0x64:i, 0x270F:i)
OP_8D(0:b, 32:s, 0:b, 4000:s, 4000:s, 0x106:s, 0xA:s, 100:i, 0:b)
OP_8D(0:b, 15:s, 0:b, 3:i, 0:i, 100:i, 0:b)
OP_95
SetAngleTarget(0xFC:b, "", 0x0:s)
SetAngleTarget(Self, "", 0x0:s)
MoveAngle(0x1F4:i, 2100:s, 3000:s)
Sleep(0x3E8:i)
Update
SubChip(Self, 0x1:b)
Update
BeatBack(0xA:b)
OP_8D(0xC:b, 0x0:i, 0x0:i, 0x2:i, 0x0:i)
Sleep(600)
Update
ShowEff(0x0:b, 0xFF:b, Self, 0x106:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 3500:s, 3500:s, 3500:s, 0xA:b)

#SHINRA_LOOP_RAISE

LoopTargetBegin(SHINRA_LOOP_RAISE_END:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Damage(Target)
LoopTargetEnd
Goto(SHINRA_LOOP_RAISE:s)

#SHINRA_LOOP_RAISE_END

SuspendThread(Self, Thread1)
;FinishEff(Self, 0:b)
Sleep(1000)
Update
;WaitEff(Self, 0x0:b)
;Update
;KeepAngle(Self, 0x0:i, 0x0:i, 0x0:i, 500:i)
Sleep(1000)
Update
Sleep(0x190:i)
Update
End

