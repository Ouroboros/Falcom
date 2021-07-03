@_FILE "debug_AS0adoVC._DT"
@_INCLUDE "as_def.txt"

@UnknownFlag_0x04 0

(CraftOffsetTable:s)
(CraftOffsetTableEnd:s)
(UnknownFlag_0x04:s)

; Char chip pattern info  CH_Index, CH_DAT_Index, CP_Index, CP_DAT_Index
 (0x0085:s, 0x0038:s, 0x0095:s, 0x0038:s) (0x0078:s, 0x0038:s, 0x0088:s, 0x0038:s)
 (0x007C:s, 0x0038:s, 0x008C:s, 0x0038:s) (0x0083:s, 0x0038:s, 0x0093:s, 0x0038:s)
 (0x0084:s, 0x0038:s, 0x0094:s, 0x0038:s) (0x0000:s, 0x0006:s, 0x0005:s, 0x0006:s)
 (0x0100:s, 0x0006:s, 0x0006:s, 0x0006:s)
[FF FF FF FF]

; 3d model file
""

#CraftOffsetTable
 (SysCraft_MagicEffect:s)
 (SysCraft_Stand:s)
 (SysCraft_Move:s)
 (SysCraft_UnderAttack:s)
 (SysCraft_Dead:s)
 (SysCraft_NormalAttack:s)
 (SysCraft_MagicChant:s)
 (SysCraft_MagicCast:s)
 (SysCraft_Win:s)
 (SysCraft_Unknown:s)
 (SysCraft_Unknown:s)
 (SysCraft_Stun:s)
 (SysCraft_Stand:s)
 (SysCraft_Unknown:s) (SysCraft_Unknown:s) (SysCraft_Unknown:s) (Craft_10:s) (SysCraft_MagicChant:s)
 (Craft_12:s) (Craft_13:s) (Craft_14:s) (Craft_15:s) (Craft_16:s)
 (Craft_17:s) (Craft_18:s) (Craft_19:s) (Craft_1A:s) (Craft_1B:s)
 (SysCraft_Unknown:s) (Craft_1D:s) (Craft_1E:s)
#CraftOffsetTableEnd

[80 B0 80 B0 80 B0 80 B0 80 B0 80 B0 80 B0 80 B0]


@_MOD 16
#SysCraft_Unknown
End


@_MOD 16
#SysCraft_Stand
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x82:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x82:i)
Update
Goto(loc_3000:s)

#loc_041E
ShakeChar(Self, 0xFFFFFF38:i, 0x0:i, 0xFFFFFF38:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xC8:i, 0x0:i, 0xC8:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xFFFFFF38:i, 0x0:i, 0xFFFFFF38:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xC8:i, 0x0:i, 0xC8:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xFFFFFF6A:i, 0x0:i, 0xFFFFFF6A:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0x96:i, 0x0:i, 0x96:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xFFFFFF9C:i, 0x0:i, 0xFFFFFF9C:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0x64:i, 0x0:i, 0x64:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xFFFFFFCE:i, 0x0:i, 0xFFFFFFCE:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0x32:i, 0x0:i, 0x32:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0xFFFFFFCE:i, 0x0:i, 0xFFFFFFCE:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0x32:i, 0x0:i, 0x32:i)
Sleep(0x32:i)
Update
ShakeChar(Self, 0x0:i, 0x0:i, 0x0:i)
Sleep(0x32:i)
Update
Ret

#loc_089A
Update
Update
Update

#loc_0920
LoadSChip(0xF:b, 0x380079:i, 0x380089:i)
SelectChip(Self, 0xF:b)
SubChip(Self, 0x0:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x28:i)
Update
Goto(loc_0920:s)

#loc_0990
OP_1E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
End

#loc_0B40
ShowEff(0x1:b, 0xFF:b, Target, 0x0:s, 0x0:i, 0x258:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
Ret

#loc_12C0
DropDown(Self, 0x0:i, 0xFFFFF830:i, 0x0:i, 0x0:s, 0xBB8:s)
End

#loc_12E0
SubChip(Self, 0x0:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x28:i)
Update
End

#loc_1340
MagicWaitEff

#loc_1341
LoopTargetBegin(loc_137D:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0x19:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Call(loc_0B40:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Voice(0x79A:s)
Update
Update
LoopTargetEnd
Goto(loc_1341:s)

#loc_137D
Ret

#loc_1540
BeginThread(Self, Thread1, loc_0ADD:s, 0x0:b)
Sleep(0x70:i)
Update
MagicWaitEff
Update
ShowEff(0x0:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x4E8:s, 0x4E8:s, 0x4E8:s, 0xFF:b)
Sleep(0x70:i)
Update
Ret

#loc_1640
BeginThread(Self, Thread1, loc_0ADD:s, 0x0:b)
Sleep(0x70:i)
Update
MagicWaitEff
Update
ShowEff(0x0:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x9C4:s, 0x9C4:s, 0x9C4:s, 0xFF:b)
Sleep(0x70:i)
Update
Ret

#loc_1750
ShowEff(0x1:b, 0xFF:b, Dest, 0x1:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x1F4:s, 0xC8:s, 0x1F4:s, 0xFF:b)
End

#loc_1770
MagicWaitEff

#loc_1771
LoopTargetBegin(loc_179D:s)
Voice(0x79A:s)
BeatBack(0x0:b)
ShowEff(0x0:b, 0xFF:b, Target, 0x8:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x190:s, 0x3E8:s, 0xFF:b)
Update
LoopTargetEnd
Goto(loc_1771:s)

#loc_179D
Ret

#loc_1910
ShowEff(0x1:b, 0xFF:b, Dest, 0x1:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x190:s, 0xC8:s, 0x190:s, 0xFF:b)
End

#loc_1B40
ShowEff(0x1:b, 0xFF:b, Self, 0x100:s, 0x0:i, 0xC8:i, 0x3E8:i, 0x10E:s, 0x0:s, 0x0:s, 0x384:s, 0x320:s, 0x384:s, 0x3:b)
ShowEff(0x0:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0x0:i, 0x12C:i, 0x0:s, 0x0:s, 0x0:s, 0x258:s, 0x258:s, 0x258:s, 0xFF:b)
End

#loc_1B80
OP_8D(0xD:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
Update
OP_26(0x2:b, 0xFF:b, 0x20:s)
OP_8D(0xC:b, 0x0:i, 0xFFFFF830:i, 0x0:i, 0x0:i)
OP_26(0x2:b, 0xFC:b, 0x20:s)
OP_6D(0x100000:i)
Update
MagicWaitEff

#loc_1BB6
LoopTargetBegin(loc_1BEA:s)
Voice(0x79A:s)
Damage(Target)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
ShowEff(0x1:b, 0xFF:b, Target, 0x0:s, 0x0:i, 0x258:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
LoopTargetEnd
Goto(loc_1BB6:s)

#loc_1BEA
Ret

#loc_1D01
ShowEff(0x0:b, 0xFF:b, Self, 0x2:s, 0x0:i, 0x0:i, 0x320:i, 0x0:s, 0xB4:s, 0x0:s, 0x9C4:s, 0x9C4:s, 0x7D0:s, 0x4:b)
ShowEff(0x1:b, 0xFF:b, Self, 0x100:s, 0x0:i, 0xC8:i, 0x3E8:i, 0x10E:s, 0x0:s, 0x0:s, 0x3E8:s, 0x7D0:s, 0x3E8:s, 0x3:b)
ShowEff(0x0:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0x0:i, 0x320:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
End

#loc_1E90
ShowEff(0x1:b, 0xFF:b, Self, 0x2:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x168:s, 0x3E8:s, 0x168:s, 0x4:b)
Ret

#loc_1EB0
MagicWaitEff

#loc_1EB1
LoopTargetBegin(loc_1EBA:s)
Damage(Target)
LoopTargetEnd
Goto(loc_1EB1:s)

#loc_1EBA
Voice(0x79A:s)
Ret

#loc_1EC0
ShowEff(0x1:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0xFFFFF448:i, 0x5A:s, 0x0:s, 0x0:s, 0x2BC:s, 0x3E8:s, 0x2BC:s, 0x5:b)
ShowEff(0x1:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0xBB8:i, 0x10E:s, 0x0:s, 0x0:s, 0x2BC:s, 0x3E8:s, 0x2BC:s, 0x3:b)
Ret

#loc_1F00
ShowEff(0x1:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0xA8C:i, 0x5DC:i, 0x0:s, 0x0:s, 0x0:s, 0x44C:s, 0x44C:s, 0x44C:s, 0x8:b)
Sleep(0x64:i)
Update
Ret

#loc_2C10
Random(0x14:b, 0x4:b, 0x4B:i, loc_2C20:s)
Goto(loc_2E80:s)

#loc_2E80
Say(0x9:b, "#2018F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0xFF:b)
Say(0x9:b, "#2020F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0x9:b)
End

#loc_0ADD
SubChip(Self, 0x0:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x1D:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x1C:i)
Update
End

#loc_2C20
Random(0x14:b, 0x4:b, 0x46:i, loc_2C30:s)
Goto(loc_2E00:s)

#loc_2E00
Say(0x9:b, "#2016F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0xFF:b)
End

#loc_2C30
Random(0x14:b, 0x4:b, 0x39:i, loc_2C40:s)
Goto(loc_2C80:s)

#loc_2C80
Say(0x9:b, "#2010F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0x9:b)
End

#loc_2C40
Random(0x14:b, 0x4:b, 0x32:i, loc_2D80:s)
Goto(loc_2D00:s)

#loc_2D00
Say(0x9:b, "#2012F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0xFF:b)
End

#loc_2D80
Say(0x9:b, "#2014F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0xFF:b)
End

#loc_3000
OP_8D(0x16:b, Self:i, 0x1FF:i, 0x0:i, 0x0:i)
Goto(SysCraft_Stand:s)


@_MOD 16
#SysCraft_Move
SelectChip(Self, 0x1:b)
SubChip(Self, 0x0:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x28:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x28:i)
Update
Goto(SysCraft_Move:s)


@_MOD 16
#SysCraft_UnderAttack
SelectChip(Self, 0x3:b)
SubChip(Self, 0x0:b)
Sleep(0x28:i)
Update
Call(loc_041E:s)
End


@_MOD 16
#Craft_10
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
Random(0x8:b, 0x1:b, 0x0:i, loc_027E:s)
ShowEff(0x1:b, 0xFF:b, Self, 0x100:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0xFFFF:s, 0x258:s, 0xFFFF:s, 0x0:b)
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7C(0xFF:b, 0x1:b)
SuspendThread(Self, Thread1)

#loc_027E
OP_54(0x1:b)
Goto(SysCraft_Stand:s)


@_MOD 16
#SysCraft_Stun
SelectChip(Self, 0x4:b)
SubChip(Self, 0x0:b)
Sleep(0x64:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x64:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x64:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x64:i)
Update
End


@_MOD 16
#SysCraft_MagicEffect
AddEff(0x100:s, "battle\\zzstore.eff")
AddEff(0x101:s, "battle\\zzboost.eff")
End


@_MOD 16
#Craft_1D
OP_3F(Self)
LockAngle(Self)
Voice(0x797:s)
MagicWaitEff

#loc_0751
LoopTargetBegin(loc_075E:s)
Damage(Target)
SeEx(0x79A:s, 0x0:b)
LoopTargetEnd
Goto(loc_0751:s)

#loc_075E
Update
Update
Update
ShowEff(0x1:b, 0xFF:b, Self, 0x101:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xF:b)
Sleep(0xC8:i)
Update
OP_8D(0x9:b, 0x8:i, 0x370621:i, 0x0:i, 0x0:i)
End


@_MOD 16
#SysCraft_Dead
SeEx(0x799:s, 0x0:b)
Sleep(0x1F4:i)
Update
Update
SelectChip(Self, 0x4:b)
SubChip(Self, 0x0:b)
Sleep(0x5A:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x5A:i)
Update
SeEx(0x7A6:s, 0x0:b)
SubChip(Self, 0x2:b)
Sleep(0x5A:i)
Update
Update
Update
Update
Update
SubChip(Self, 0x3:b)
Sleep(0x5A:i)
Update
Die
Sleep(0x1F4:i)
Update
End


@_MOD 16
#SysCraft_MagicChant
Random(0x8:b, 0x1:b, 0x0:i, loc_084D:s)
ShowEff(0x1:b, 0xFF:b, Self, 0x100:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0xFFFF:s, 0x258:s, 0xFFFF:s, 0x0:b)

#loc_084D
OP_54(0x1:b)
Goto(SysCraft_Stand:s)


@_MOD 16
#SysCraft_NormalAttack
MagicWaitEff
SE(0x389:s)
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x50:i)
Update
Random(0x14:b, 0x4:b, 0x32:i, loc_089A:s)
Update
Update
Update
Goto(loc_089D:s)

#loc_089D
SubChip(Self, 0x1:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x50:i)
Update
SeEx(0x389:s, 0x0:b)
SubChip(Self, 0x4:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x50:i)
Update
ShowEff(0x0:b, 0xFF:b, Target, 0x8:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x3C:i)
Update
End


@_MOD 16
#Craft_1E
OP_78(0x1:b)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7E(0x64:i)
SuspendThread(Self, Thread1)
End


@_MOD 16
#Craft_12
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
LoadSChip(0xB:b, 0x38007B:i, 0x38008B:i)
LoadSChip(0xD:b, 0x38007D:i, 0x38008D:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_1E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Turn(Self, Target, 0x0:s)
Sleep(0x10:i)
Update
SelectChip(Self, 0xB:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x79C:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
Damage(Target)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x79D:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0x5:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0xD:b)
SubChip(Self, 0x0:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1C:i)
Update
SeEx(0x79E:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x1D:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0xA:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x1D:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x1D:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x1D:i)
Update
SelectChip(Self, 0xB:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x79F:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0xF:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x7A0:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0x14:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0xD:b)
SubChip(Self, 0x0:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x3C:i)
Update
SeEx(0x7A1:s, 0x0:b)
Sleep(0x40:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0x19:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
Sleep(0x0:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x12C:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x78:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x78:i)
Update
End


@_MOD 16
#Craft_13
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
LoadSChip(0xB:b, 0x38007B:i, 0x38008B:i)
LoadSChip(0xD:b, 0x38007D:i, 0x38008D:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_1E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Turn(Self, Target, 0x0:s)
Sleep(0x10:i)
Update
SelectChip(Self, 0xB:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x79C:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
Damage(Target)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x79D:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0x5:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0xD:b)
SubChip(Self, 0x0:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1C:i)
Update
SeEx(0x79E:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x1C:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x1D:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0xA:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x1D:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x1D:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x1D:i)
Update
SelectChip(Self, 0xB:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x79F:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0xF:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x20:i)
Update
SeEx(0x7A0:s, 0x0:b)
SubChip(Self, 0x3:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x20:i)
Update
Call(loc_0B40:s)
OP_8D(0x15:b, Target:i, 0x400:i, 0x14:i, 0x1:i)
Damage(Target)
OP_8D(0x16:b, Target:i, 0x400:i, 0x0:i, 0x0:i)
Voice(0x79A:s)
DamageAnime(Target, 0x1:b, 0x32:i)
Update
Update
BeginThread(Self, Thread1, loc_0990:s, 0x0:b)
SubChip(Self, 0x6:b)
Sleep(0x20:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x20:i)
Update
End


@_MOD 16
#Craft_14
LoadSChip(0x8:b, 0x380082:i, 0x380092:i)
LoadSChip(0x9:b, 0x38007A:i, 0x38008A:i)
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
Turn(Self, Dest, 0x0:s)
Sleep(0x10:i)
Update
SelectChip(Self, 0x8:b)
BeginThread(Self, Thread1, loc_12E0:s, 0x0:b)
Jump(Self, Dest, 0x0:i, 0x7D0:i, 0x0:i, 0xBB8:s, 0x1388:s)
BeginThread(Self, Thread2, loc_12C0:s, 0x0:b)
SelectChip(Self, 0x9:b)
SubChip(Self, 0x0:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1E:i)
Update
SeEx(0x79B:s, 0x0:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x50:i)
Update
Call(loc_1340:s)
OP_8D(0xD:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
Update
OP_26(0x2:b, 0xFF:b, 0x20:s)
OP_8D(0xC:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
OP_26(0x2:b, 0xFC:b, 0x20:s)
OP_6D(0x100000:i)
Update
ShowEff(0x1:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x7E8:s, 0x3E8:s, 0x7E8:s, 0xFF:b)
SubChip(Self, 0x4:b)
Sleep(0x50:i)
Update
Call(loc_1340:s)
OP_8D(0xD:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
Update
OP_26(0x2:b, 0xFF:b, 0x20:s)
OP_8D(0xC:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
OP_26(0x2:b, 0xFC:b, 0x20:s)
OP_6D(0x100000:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x50:i)
Update
Call(loc_1340:s)
OP_8D(0xD:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
Update
OP_26(0x2:b, 0xFF:b, 0x20:s)
OP_8D(0xC:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
OP_26(0x2:b, 0xFC:b, 0x20:s)
OP_6D(0x100000:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
Call(loc_1340:s)
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
Call(loc_1340:s)
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
Update
Update
Update
Sleep(0x12C:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x78:i)
Update
End


@_MOD 16
#Craft_15
LoadSChip(0xE:b, 0x38007E:i, 0x38008E:i)
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
AddEff(0x1:s, "map\\zzfire.eff")
MagicWaitEff
OP_3F(Self)
Update
Update
Turn(Self, Target, 0x0:s)
Sleep(0x10:i)
Update
SelectChip(Self, 0xE:b)
KeepAngle(Target, 0x0:i, 0x0:i, 0x0:i, 0x5DC:i)
Call(loc_1540:s)
Call(loc_1540:s)
Call(loc_1540:s)
Call(loc_1540:s)
Call(loc_1540:s)
Call(loc_1540:s)
Sleep(0x50:i)
Update
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Update
Sleep(0x300:i)
Update
End


@_MOD 16
#Craft_16
LoadSChip(0xE:b, 0x38007E:i, 0x38008E:i)
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
AddEff(0x1:s, "map\\zzBfire.eff")
MagicWaitEff
OP_3F(Self)
Voice(0x796:s)
Update
Update
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7C(0xFF:b, 0x1:b)
SuspendThread(Self, Thread1)
Turn(Self, Target, 0x3E8:s)
Sleep(0x10:i)
Update
SelectChip(Self, 0xE:b)
KeepAngle(Target, 0x0:i, 0x0:i, 0x0:i, 0x3E8:i)
Update
Update
Call(loc_1640:s)
Sleep(0x50:i)
Update
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Update
Sleep(0x300:i)
Update
End


@_MOD 16
#Craft_17
OP_78(0x1:b)
AddEff(0x0:s, "map\\zzstore.eff")
AddEff(0x1:s, "map\\zzwind.eff")
LoadSChip(0xE:b, 0x38007F:i, 0x38008F:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x64:i)
Update
SelectChip(Self, 0xE:b)
SubChip(Self, 0x0:b)
ShowEff(0x1:b, 0xFF:b, Self, 0x100:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x7D0:s, 0x2BC:s, 0x7D0:s, 0x3:b)
BeginThread(Self, Thread1, loc_1750:s, 0x0:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x5:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x7:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x9:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xA:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0xB:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xC:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0xD:b)
Sleep(0x12C:i)
Update
CancelEff(Self, 0x3:b)
End


@_MOD 16
#Craft_18
OP_78(0x1:b)
AddEff(0x0:s, "map\\zzstore.eff")
AddEff(0x1:s, "map\\zzBwind.eff")
LoadSChip(0xE:b, 0x38007F:i, 0x38008F:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
Voice(0x796:s)
Update
Update
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x64:i)
Update
SelectChip(Self, 0xE:b)
SubChip(Self, 0x0:b)
ShowEff(0x1:b, 0xFF:b, Self, 0x100:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0xBB8:s, 0x2BC:s, 0xBB8:s, 0x3:b)
BeginThread(Self, Thread1, loc_1910:s, 0x0:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x3:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x5:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x6:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x9:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xA:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xB:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0xC:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xD:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x8:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x9:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xA:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0xB:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xC:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xD:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0x7:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x9:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0xA:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xB:b)
Sleep(0x32:i)
Update
SubChip(Self, 0xC:b)
Sleep(0x32:i)
Update
Call(loc_1770:s)
SubChip(Self, 0xD:b)
Sleep(0x12C:i)
Update
CancelEff(Self, 0x3:b)
End


@_MOD 16
#Craft_19
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
AddEff(0x1:s, "map\\zzgold.eff")
AddEff(0x2:s, "map\\zzgoldex.eff")
LoadSChip(0xE:b, 0x380080:i, 0x380090:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x64:i)
Update
Turn(Self, Target, 0x3E8:s)
SelectChip(Self, 0xE:b)
SubChip(Self, 0x0:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x32:i)
Update
BeginThread(Self, Thread1, loc_1B40:s, 0x0:b)
SubChip(Self, 0x4:b)
Sleep(0x32:i)
Update
Call(loc_1B80:s)
SubChip(Self, 0x5:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x8:b)
Sleep(0x64:i)
Update
Call(loc_1B80:s)
Sleep(0xC8:i)
Update
CancelEff(Self, 0x3:b)
End


@_MOD 16
#Craft_1A
OP_78(0x1:b)
AddEff(0x0:s, "map\\mp009_00.eff")
AddEff(0x1:s, "map\\zzBgold.eff")
AddEff(0x2:s, "map\\zzgoldex.eff")
LoadSChip(0xE:b, 0x380080:i, 0x380090:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
Voice(0x796:s)
Update
Update
BeginThread(Self, Thread1, loc_0920:s, 0x0:b)
OP_7E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x64:i)
Update
Turn(Self, Target, 0x3E8:s)
SelectChip(Self, 0xE:b)
SubChip(Self, 0x0:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x32:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x32:i)
Update
BeginThread(Self, Thread1, loc_1D01:s, 0x0:b)
Call(loc_1B80:s)
SubChip(Self, 0x4:b)
Sleep(0x32:i)
Update
Call(loc_1B80:s)
SubChip(Self, 0x5:b)
Sleep(0x32:i)
Update
Call(loc_1B80:s)
SubChip(Self, 0x6:b)
Sleep(0x32:i)
Update
Call(loc_1B80:s)
SubChip(Self, 0x7:b)
Sleep(0x32:i)
Update
Call(loc_1B80:s)
SubChip(Self, 0x8:b)
CancelEff(Self, 0x4:b)
Sleep(0x64:i)
Update
Sleep(0x12C:i)
Update
CancelEff(Self, 0x3:b)
End


@_MOD 16
#SysCraft_MagicCast
LoadSChip(0x8:b, 0x380082:i, 0x380092:i)
LoadSChip(0x9:b, 0x38007A:i, 0x38008A:i)
OP_78(0x1:b)
AddEff(0x0:s, "map\\zzcupex.eff")
AddEff(0x1:s, "map\\zzburst.eff")
AddEff(0x2:s, "map\\zzcup.eff")
LoadSChip(0xE:b, 0x380080:i, 0x380090:i)
MagicWaitEff
OP_3F(Self)
LockAngle(Self)
CancelEff(Self, 0xF:b)
Turn(Self, Dest, 0x3E8:s)
Call(loc_1EC0:s)
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x384:i)
Update
Sleep(0x64:i)
Update
SelectChip(Self, 0x8:b)
BeginThread(Self, Thread1, loc_12E0:s, 0x0:b)
Jump(Self, Self, 0x0:i, 0x7D0:i, 0x0:i, 0xBB8:s, 0x1388:s)
BeginThread(Self, Thread2, loc_12C0:s, 0x0:b)
SelectChip(Self, 0x9:b)
SubChip(Self, 0x0:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x1:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x2:b)
Sleep(0x1E:i)
Update
SubChip(Self, 0x3:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x4:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x5:b)
Call(loc_1E90:s)
Sleep(0x50:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
Voice(0x798:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
Call(loc_1F00:s)
Call(loc_1EB0:s)
Call(loc_1F00:s)
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x6:b)
Sleep(0x50:i)
Update
SubChip(Self, 0x7:b)
Sleep(0x78:i)
Update
OP_8D(0x9:b, 0x8:i, 0x370616:i, 0x0:i, 0x0:i)
OP_8D(0xA:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
End


@_MOD 16
#Craft_1B
OP_8D(0x6:b, 0x4000000:i, 0x0:i, 0x0:i, 0x0:i)
Damage(Target)
End


@_MOD 16
#SysCraft_Win
Random(0x14:b, 0x4:b, 0x4C:i, loc_2C10:s)
Goto(loc_2F00:s)

#loc_2F00
Say(0x9:b, "#2023F#5P如果，这个世界能反映人的意念……", 0x3E8:i)
Sleep(0x9C4:i)
Update
OP_29(0xFF:b)
End

