@_FILE "debug_as04200.dat"
@_INCLUDE "as_def.txt"

@UnknownFlag_0x04 0

(CraftOffsetTable:s)
(CraftOffsetTableEnd:s)
(UnknownFlag_0x04:s)

; Char chip pattern info  CH_Index, CH_DAT_Index, CP_Index, CP_DAT_Index
 (0x4250:s, 0x0070:s) (0x4251:s, 0x0070:s)
 (0x4253:s, 0x0070:s) (0x4254:s, 0x0070:s)

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
 [FF FF]
 [FF FF]
 [FF FF]
 [FF FF]
 [FF FF]
 (SysCraft_Stun:s)
 (SysCraft_Unknown2:s)
 [FF FF]
 [FF FF]
 (SysCraft_Counter:s)
 (Craft_10:s) (Craft_11:s) (Craft_12:s) (Craft_13:s) (Craft_14:s)
 (Craft_15:s) [FF FF] [FF FF] [FF FF] [FF FF]
 (Craft_1A:s) [FF FF] [FF FF] [FF FF] [00 00]

#CraftOffsetTableEnd

[80 B0 80 B0 80 B0 80 B0 80 B0 80 B0 80 B0 80 B0]



@_MOD 16
#SysCraft_Stand
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x1:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x2:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x1:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x0:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x3:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x4:b)
Sleep(0x82:s)
Update
SubChip(Self, 0x3:b)
Sleep(0x82:s)
Update
Goto(SysCraft_Stand:s)
Goto(SysCraft_Stand:s)


@_MOD 16
#SysCraft_Move
SelectChip(Self, 0x1:b)
SubChip(Self, 0x0:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x1:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x2:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x1:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x0:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x3:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x4:b)
Sleep(0x28:s)
Update
SubChip(Self, 0x3:b)
Sleep(0x28:s)
Update
Goto(SysCraft_Move:s)
Goto(SysCraft_Move:s)


@_MOD 16
#SysCraft_UnderAttack
SelectChip(Self, 0x2:b)
SubChip(Self, 0x0:b)
Sleep(0x28:s)
Update
Call(loc_0211:s)
End

#loc_0115
SelectChip(Self, 0x2:b)
SubChip(Self, 0x1:b)
Sleep(0xB4:s)
Update
SubChip(Self, 0x2:b)
Sleep(0xB4:s)
Update
SeEx(0x202:s, 0x0:b)
Goto(loc_012A:s)


@_MOD 16
#SysCraft_Stun
SelectChip(Self, 0x2:b)
SubChip(Self, 0x1:b)
Sleep(0x64:s)
Update
SubChip(Self, 0x2:b)
Sleep(0x64:s)
Update
SubChip(Self, 0x3:b)
Sleep(0x64:s)
Update
End


@_MOD 16
#SysCraft_Unknown2
SelectChip(Self, 0x0:b)
SubChip(Self, 0x0:b)
Sleep(0x64:s)
Update
End

#loc_0211
ShakeChar(Self, 0xFFFFFF38:i, 0x0:i, 0xFFFFFF38:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xC8:i, 0x0:i, 0xC8:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xFFFFFF38:i, 0x0:i, 0xFFFFFF38:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xC8:i, 0x0:i, 0xC8:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xFFFFFF6A:i, 0x0:i, 0xFFFFFF6A:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0x96:i, 0x0:i, 0x96:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xFFFFFF9C:i, 0x0:i, 0xFFFFFF9C:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0x64:i, 0x0:i, 0x64:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xFFFFFFCE:i, 0x0:i, 0xFFFFFFCE:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0x32:i, 0x0:i, 0x32:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0xFFFFFFCE:i, 0x0:i, 0xFFFFFFCE:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0x32:i, 0x0:i, 0x32:i)
Sleep(0x32:s)
Update
ShakeChar(Self, 0x0:i, 0x0:i, 0x0:i)
Sleep(0x32:s)
Update
Ret

#loc_02FC
OP_8D(0x4C:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
ResetLoopTarget
OP_5A(0x0:b, 0x0:b, 0xF7600000:i)
OP_6D(0x40000:i)
ClearChipModeFlag(0x0:b, Self, 0x1:s)
Ret


@_MOD 16
#SysCraft_MagicEffect
AddEff(0x82:b, "battle/cr035000.eff")
ShowEff(0xFF:b, 0xFF:b, 0x4137:s, 0x0:s, 0x44C0000:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x4B0A:s, 0x9:b)
Goto(loc_0107:s)

#loc_0107
WaitEff(0x1:b)
Condition(0xB:b, 0x1:b, 0x3:i, loc_0115:s)
Goto(loc_012A:s)

#loc_012A
SelectChip(Self, 0x2:b)
SubChip(Self, 0x3:b)
Sleep(0xB4:s)
Update
End


@_MOD 16
#SysCraft_Dead
Die
Condition(0x2:b, 0x2:b, 0x10:i, loc_04A2:s)
Goto(loc_012A:s)
Goto(loc_012A:s)

#loc_04A2
Condition(0xA:b, 0x1:b, 0x2:i, loc_04B7:s)
Condition(0xB:b, 0x1:b, 0x3:i, loc_04B7:s)
Goto(loc_04D7:s)

#loc_04D7
SelectChip(Self, 0x2:b)
SubChip(Self, 0x3:b)
Sleep(0x12C:s)
Update
Sleep(0xFA0:s)
Update
End

#loc_04B7
Voice(0x0:b, 0xF25:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
SelectChip(Self, 0x2:b)
SubChip(Self, 0x1:b)
Sleep(0x12C:s)
Update
SubChip(Self, 0x2:b)
Sleep(0x12C:s)
Update
SeEx(0x202:s, 0x0:b)
Goto(loc_04D7:s)


@_MOD 16
#SysCraft_NormalAttack
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704252:i, 0xFF:b)
AddEff(0x0:b, "battle/ms00001.eff")
OP_78(0x0:b)
ResetLoopTarget
OP_95
SetAngleTarget(Self, "", 0x0:b)
SetAngleTarget(0xFC:b, "", 0x0:b)
MoveAngle(0x64:s, 0xF:b, 0xF:b)
BeginThread(Self, Thread1, SysCraft_Move:s, 0x0:b)
OP_1E(0xFFFFFFFF:i)
SuspendThread(Self, Thread1)
TurnDirection(Self, Target, 0x0:s, 0x0:s, 0x0:b)
SelectChip(Self, 0x7:b)
SubChip(Self, 0x0:b)
Sleep(0x64:s)
Update
SubChip(Self, 0x1:b)
SeEx(0x166:s, 0x0:b)
OP_6D(0x200000:i)
SaveCurPos(Self)
OP_5(Self, 0x0:b, 0x0:i)
OP_21(0x1:b, MainThread, 0xFFFFFF6A:i, 0x4E20:i)
Sleep(0x12C:s)
Update
Condition(0x14:b, 0x4:b, 0x32:i, loc_0570:s)
Voice(0x0:b, 0xF13:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
Goto(loc_0592:s)

#loc_0570
Condition(0x14:b, 0x4:b, 0x32:i, loc_0587:s)
Voice(0x0:b, 0xF14:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
Goto(loc_0592:s)
Goto(loc_0592:s)

#loc_0587
Voice(0x0:b, 0xF15:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
Goto(loc_0592:s)

#loc_0592
Blur(0xFFFF0000:i, 0xBBFF:i, 0xFFFF1801:i, 0x82:b, 0x3:i)
End


@_MOD 16
#SysCraft_Counter
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704252:i, 0xFF:b)
AddEff(0x0:b, "battle/ms00001.eff")
OP_78(0x0:b)
ResetLoopTarget
OP_95
SetAngleTarget(Self, "", 0x0:b)
SetAngleTarget(0xFC:b, "", 0x0:b)
MoveAngle(0x64:s, 0xF:b, 0xF:b)
TurnDirection(Self, Target, 0x0:s, 0x0:s, 0x0:b)
Voice(0x0:b, 0xF28:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
SelectChip(Self, 0x7:b)
SubChip(Self, 0x0:b)
Sleep(0x64:s)
Update
SubChip(Self, 0x1:b)
SeEx(0x166:s, 0x0:b)
OP_6D(0x200000:i)
SaveCurPos(Self)
OP_5(Self, 0x0:b, 0x0:i)
OP_21(0x1:b, MainThread, 0xFFFFFF6A:i, 0x4E20:i)
Sleep(0x12C:s)
Update
Blur(0xFFFF0000:i, 0xBBFF:i, 0xFFFF1801:i, 0x82:b, 0x3:i)
End


@_MOD 16
#Craft_10
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704252:i, 0xFF:b)
LoadSChip(0x6:b, 0x704256:i, 0xFF:b)
AddEff(0x0:b, "battle/cr035100.eff")
AddEff(0x1:b, "battle/cr035101.eff")
AddEff(0x2:b, "battle/ms00000.eff")
Teleport(Self, Dest, 0x0:i, 0x0:i, 0x0:i)
OP_6D(0x200000:i)
SaveCurPos(Self)
OP_A(Self, 0x1:b, 0x0:b, 0x0:i)
OP_78(0x0:b)
ResetLoopTarget
SortTarget(0x0:b)
OP_26(0x2:b, 0xFF:b, 0x10:s)
OP_95
SetAngleTarget(Self, "", 0x0:b)
MoveAngle(0x64:s, 0x14:b, 0x1E:b)
TurnDirection(Self, Dest, 0x0:s, 0x1F4:s, 0x0:b)
OP_5A(0x0:b, 0x2:b, 0x6207D0:i)
FinishEff(0xF:b, 0x0:b)
End


@_MOD 16
#Craft_11
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704257:i, 0xFF:b)
AddEff(0x0:b, "battle/cr035200.eff")
AddEff(0x1:b, "battle/cr035201.eff")
AddEff(0x2:b, "battle/cr035202.eff")
OP_78(0x0:b)
ResetLoopTarget
SortTarget(0x0:b)
OP_5A(0x0:b, 0x2:b, 0x6207D0:i)
ShowEff(0xF:b, 0x0:b, 0x0:s, 0x0:s, 0xFF1BFE00:i, 0xFF0207:i, 0x7006406:i, 0xFF02:s, 0x601:s, 0x64:s, 0x207:s, 0x2FF:s, 0x6665:s, 0x1:b)
End


@_MOD 16
#Craft_12
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704258:i, 0xFF:b)
AddEff(0x0:b, "battle/cr035300.eff")
AddEff(0x1:b, "battle/cr035301.eff")
OP_78(0x0:b)
ResetLoopTarget
OP_5A(0x0:b, 0x2:b, 0xFF3507D0:i)
End


@_MOD 16
#Craft_13
End


@_MOD 16
#Craft_1A
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704259:i, 0xFF:b)
LoadSChip(0x6:b, 0x704252:i, 0xFF:b)
LoadSChip(0x5:b, 0x704256:i, 0xFF:b)
AddEff(0x0:b, "eff/cutin42.eff")
AddEff(0x1:b, "battle/sc035000.eff")
AddEff(0x2:b, "battle/sc035001.eff")
AddEff(0x3:b, "battle/cm008_01.eff")
AddEff(0x4:b, "battle/com004.eff")
AddEff(0x5:b, "battle/cr035100.eff")
AddEff(0x6:b, "battle/cr035101.eff")
AddEff(0x7:b, "battle/sc035003.eff")
OP_78(0x0:b)
Call(loc_02FC:s)
Teleport(Self, 0xF3:b, 0x0:i, 0x0:i, 0x0:i)
OP_8D(0x1:b, 0x0:i, 0x0:i, 0x0:i, 0x0:i)
Voice(0x0:b, 0xF1E:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
Teleport(Self, 0xFD:b, 0x0:i, 0x0:i, 0xFFFFD8F0:i)
OP_3(Self, 0x0:s)
BeginThread(Self, Thread1, SysCraft_Stand:s, 0x0:b)
OP_5F(Self, 0x0:b)
OP_3(0xFC:b, 0xB4:s)
OP_34
KeepAngle(0xFD:b, 0x0:i, 0x2EE:i, 0xFFFFD8F0:i, 0xC83B0000:i)
OP_32(0x0:b, 0x0:b)
End


@_MOD 16
#Craft_14
ResetLoopTarget
OP_78(0x1:b)
OP_78(0x0:b)
OP_95
SetAngleTarget(Self, "", 0x0:b)
SetAngleTarget(0xFC:b, "", 0x0:b)
MoveAngle(0x64:s, 0x14:b, 0x1E:b)
TurnDirection(Self, Target, 0x0:s, 0x0:s, 0x0:b)
Voice(0x0:b, 0xF11:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
SelectChip(Self, 0x0:b)
BeginThread(Self, Thread1, SysCraft_Stand:s, 0x0:b)
Sleep(0xBB8:s)
Update
SuspendThread(Self, Thread1)
End


@_MOD 16
#Craft_15
ResetLoopTarget
OP_78(0x1:b)
LoadSChip(0x7:b, 0x704252:i, 0xFF:b)
OP_78(0x0:b)
OP_95
SetAngleTarget(Self, "", 0x0:b)
SetAngleTarget(0xFC:b, "", 0x0:b)
MoveAngle(0x64:s, 0x14:b, 0x1E:b)
TurnDirection(Self, Target, 0x0:s, 0x0:s, 0x0:b)
Voice(0x0:b, 0xF12:s, 0x0:s, 0x0:s, 0x0:s, 0xFE:b)
SelectChip(Self, 0x0:b)
BeginThread(Self, Thread1, SysCraft_Stand:s, 0x0:b)
Sleep(0xFA0:s)
Update
SuspendThread(Self, Thread1)
End

