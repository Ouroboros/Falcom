@_MOD 16
"Ë²ÒÆ"

@_MOD 16
#Craft_12

;Goto(TELEPORT_2:s)

AddEff(0:s, "map\\mp049_22.eff")
Turn(Self, Dest, 0x1F4:s)
OP_3F(Self)
SelectChip(Self, 0x5:b)
SubChip(Self, 0x0:b)
Sleep(0x1F4:i)
Update
ShowEff(0x0:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x0:b)
SeEx(0xB8:s, 0x0:b)
Sleep(200)
Update
Hide(Self, 0x1F4:i)
Sleep(1500)
Update
Teleport(Self, Dest, 0x0:i, 0x0:i, 0x0:i)
KeepAngle(Dest, 0x0:i, 0x0:i, 0x0:i, 0x12C:i)
Sleep(0xC8:i)
Update
ShowEff(0x0:b, 0xFF:b, Dest, 0x0:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x0:b)
Update
OP_C(0xFF:b, 0xFF:b, 0x0:s, 0x0:s, 0x0:b)
SeEx(0xB8:s, 0x0:b)
Show(Self, 0x1F4:i)
WaitEff(Self, 0x0:b)
Update
End

#TELEPORT_2
BeginThread(Self, Thread1, TELEPORT_HELIX:s, 0x0:b)
Sleep(3000)
Update
SuspendThread(Self, Thread1)
ClearChipModeFlag(0x0:b, Self, 0x2:s)
RotateChar(Self, 0x0:s, 0x0:s, 0:s, 0:i, 0x1:b)
Update
End

#TELEPORT_HELIX
LoadSChip(0xC:b, 0x270474:i, 0x27047D:i)
SetChipModeFlag(0x0:b, Self, 0x2:s)
SelectChip(Self, 0xC:b)
SubChip(Self, 36:b)
Update
RotateChar(Self, 0x0:s, 0x0:s, 45:s, 0:i, 0x1:b)

#TELEPORT_HELIX_LOOP
SubChip(Self, 36:b)
Sleep(50)
Update
SubChip(Self, 37:b)
Sleep(50)
Update
SubChip(Self, 38:b)
Sleep(50)
Update
SubChip(Self, 39:b)
Sleep(50)
Update
SubChip(Self, 40:b)
Sleep(50)
Update
Goto(TELEPORT_HELIX_LOOP:s)

;4679 frame 35 ... 41


