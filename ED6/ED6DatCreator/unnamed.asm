@_MOD 16
#Craft_0F
OP_78(0x1:b)
AddEff(0x0:s, "monster\\msc0535.eff")
AddEff(0x1:s, "monster\\ms30000b.eff")
AddEff(0x2:s, "monster\\ms30805c.eff")
OP_78(0x0:b)
ResetLoopTarget
Turn(Self, Dest, 0x320:s)
Say(Self, "×°µ¯Íê±Ï£¡", 0x3E8:i)
Voice(0x76E:s)
Sleep(0x320:i)
Update
SelectChip(Self, 0x2:b)

LoadSChip(0xC:b, 0x2705B1:i, 0x2705B5:i)
Clone(Clone1, Self)
Hide(Clone1, 0:i)
Teleport(Clone1, Self, 0:i, 1000:i, 0:i)
SelectChip(Clone1, 0xC:b)
SubChip(Clone1, 0:b)
;RotateChar(Clone1, 0x0:s, 0x0:s, 0x0:s, 0x0:i, 90:b)
Turn(Clone1, Dest, 0:s)
Show(Clone1, 0x1F4:i)

BeginThread(Self, Thread1, loc_09DD:s, 0x0:b)
BeginThread(Clone1, Thread1, CLONE_ROTATING:s, 0x0:b)
ShowEff(0x0:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0x0:i, 0x3E8:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x3:b)
Sleep(0x3E8:i)
Update
Voice(0x76F:s)
Say(Self, "½ÓÕÐ£¡", 0x1F4:i)

Sleep(0x3E8:i)
Update
Voice(0x770:s)
Say(Self, "³¢³¢¸Ö¿øµÄ·ßÅ­°É£¡£¡", 0x7D0:i)
Sleep(0x1F4:i)
Update
;ShowEff(0x0:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0x7D0:i, 0x0:s, 0x0:s, 0x0:s, 0x1F4:s, 0x1F4:s, 0x1F4:s, 0x2:b)
Sleep(0x64:i)
Update
OP_95
SetAngleTarget(Self, "", 0x0:s)
SetAngleTarget(0xFC:b, "", 0x0:s)
SetAngleTarget(Dest, "", 0x0:s)
MoveAngle(0xC8:i, 0x3E8:s, 0x4B0:s)
SubChip(Self, 0x3:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1E:i)
Update
BeginThread(Self, Thread2, loc_09AB:s, 0x0:b)
Sleep(0xDAC:i)
Update
SuspendThread(Self, Thread1)

SuspendThread(Clone1, Thread1)
SubChip(Clone1, 0:b)
Update
Hide(Clone1, 0x1F4:i)

SubChip(Self, 0x2:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x0:b)
Sleep(0x50:i)
Update
SuspendThread(Self, Thread2)
FinishEff(Self, 0x2:b)
ReleaseEff(0x0:s)
ReleaseEff(0x1:s)
ReleaseEff(0x2:s)
End

#loc_09AB
SortTarget(0x0:b)
ResetLoopTarget

#loc_09AE
LoopTargetBegin(loc_09DC:s)
ShowEff(0x1:b, 0xFF:b, Target, 0x2:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
Damage(Target)
Sleep(0x64:i)
Update
LoopTargetEnd
Goto(loc_09AE:s)

#loc_09DC
End

;Ç¹¿Ú¶¶¶¯
#loc_09DD
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1E:i)
Update
Goto(loc_09DD:s)

#CLONE_ROTATING
SubChip(Self, 0:b)
Sleep(30)
Update
SubChip(Self, 1:b)
Sleep(30)
Update
SubChip(Self, 2:b)
Sleep(30)
Update
SubChip(Self, 3:b)
Sleep(30)
Update
SubChip(Self, 4:b)
Sleep(30)
Update
SubChip(Self, 5:b)
Sleep(30)
Update
SubChip(Self, 6:b)
Sleep(30)
Update
SubChip(Self, 7:b)
Sleep(30)
Update
Goto(CLONE_ROTATING:s)

