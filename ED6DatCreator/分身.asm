@_MOD 16
"小钢盔"

@_MOD 16
#Craft_17
ResetLoopTarget
OP_78(0x1:b)
AddEff(0x0:s, "craft\\cr000_00.eff")
AddEff(0x3:s, "scraft\\sc000_00.eff")
OP_78(0x0:b)
Turn(Self, Dest, 0x1F4:s)
OP_3F(Self)
ShowEff(0x1:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
Sleep(0xC8:i)
Update
Turn(Self, Dest, 0x64:s)
Random(0x14:b, 0x4:b, 0x32:i, loc_2DC5:s)
Voice(0x698:s)
Say(Self, "出来吧!幻影!", 0x3E8:i)
Goto(loc_2DDD:s)

#loc_2DC5
Voice(0x699:s)
Say(Self, "看得破吗?", 0x3E8:i)
Sleep(0x320:i)

#loc_2DDD
Update
SelectChip(Self, 0x5:b)
SubChip(Self, 0x0:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x0:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x0:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x3C:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x3C:i)
Update
SeEx(0x389:s, 0x0:b)
SelectChip(Self, 0x6:b)
SubChip(Self, 0x0:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x50:i)
Update
OP_8D(0x0:b, 0:s, 0:b, 0x300027:i, 0x0:i, 0x0:i, 0x0:b)
Teleport(Target, Dest, 0x0:i, 0x0:i, 0x0:i)
Turn(Target, 0xEC:b, 0x0:s)
OP_54(0x2:b)
Update
Sleep(0x1E:i)
Update
End