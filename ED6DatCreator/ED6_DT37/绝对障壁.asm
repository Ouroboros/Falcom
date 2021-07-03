@_FILE "debug_¾ø¶ÔÕÏ±Ú._DT"
@_INCLUDE "as_def.txt"

@UnknownFlag_0x04 31

(CraftOffsetTable:s)
(CraftOffsetTableEnd:s)
(UnknownFlag_0x04:s)

; Char chip pattern info  CH_Index, CH_DAT_Index, CP_Index, CP_DAT_Index

[FF FF FF FF]

; 3d model file
"boss31000\\CH31000.x"
""
[00 46]

#CraftOffsetTable
 (SysCraft_MagicEffect:s)
 (SysCraft_Stand:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s)
 (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s) (Craft_11:s)
 (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s)
 (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s)
 (SysCraft_Move:s) (SysCraft_Move:s) (SysCraft_Move:s)
#CraftOffsetTableEnd

[80 B0 80 B0 80 B0 80 B0 80 B0 80 B0 80 B0 80 B0]


@_MOD 16
#SysCraft_Move
End

#loc_038B
MagicWaitEff

#loc_038C
LoopTargetBegin(loc_039B:s)
Damage(Target)
Sleep(0x32:i)
Update
LoopTargetEnd
Goto(loc_038C:s)

#loc_039B
Ret


@_MOD 16
#SysCraft_MagicEffect
ShakeChar(Self, 0x0:i, 0x9C4:i, 0x0:i)
AddEff(0x102:s, "monster\\ms31004a.eff")
ShowEff(0x0:b, 0xFF:b, Self, 0x102:s, 0x0:i, 0xFA0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x2710:s, 0x4E20:s, 0x2710:s, 0xA:b)
SelectChip(Self, 0x0:b)
OP_45(Self, 0xB:i)
End


@_MOD 16
#SysCraft_Stand
ShakeChar(Self, 0x0:i, 0x9C4:i, 0x0:i)
OP_48(Self, 0x1F4:i)
Call(loc_0539:s)
Goto(SysCraft_Stand:s)

#loc_0539
SelectChip(Self, 0x0:b)
OP_46(Self, 0xB:i, 0x32:i)
OP_47(Self)
Ret


@_MOD 16
#Craft_11
ShakeChar(Self, 0x0:i, 0x9C4:i, 0x0:i)
OP_78(0x1:b)
AddEff(0x0:s, "monster\\ms31002a.eff")
AddEff(0x1:s, "monster\\ms31002b.eff")
AddEff(0x2:s, "monster\\ms31002c.eff")
AddEff(0x3:s, "monster\\ms31002d.eff")
OP_78(0x0:b)
OP_5A(0x0:b, 0x0:b, 0x0:i)
OP_86(0xFE0C:s, 0xFC18:s, 0xFE0C:s, 0x60:b, 0x0:i)
OP_5F(Self, 0x0:b)
OP_5F(0xFC:b, 0x0:b)
Teleport(Self, Dest, 0x0:i, 0xFFFFFC18:i, 0x3A98:i)
OP_3(Self, 0xB4:s)
OP_31(0x11:b, 0x0:i)
SetAngle(0x14F:i, 0x0:i)
ShowEff(0x0:b, 0xFF:b, Self, 0x3:s, 0x0:i, 0x0:i, 0x0:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x5:b)
RotationAngleHorz(0x2EE:i, 0x1388:i)
RotationAngle(0x0:i, 0x32C8:i, 0xFFFF8AD0:i, 0x0:i)
KeepAngle(Self, 0x0:i, 0xBB8:i, 0x0:i, 0x0:i)
KeepAngle(Self, 0x0:i, 0x1F40:i, 0xFFFFF830:i, 0x1F40:i)
Sleep(0x1F4:i)
Update
OP_48(Self, 0x1F4:i)
OP_46(Self, 0xD3:i, 0xDC:i)
OP_47(Self)
OP_48(Self, 0x1F4:i)
BeginThread(Self, Thread1, loc_0774:s, 0x0:b)
ShowEff(0x1:b, 0xFF:b, Self, 0x2:s, 0x0:i, 0x1838:i, 0x258:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x4:b)
SetAngle(0x13B:i, 0x7D0:i)
Sleep(0x3E8:i)
Update
Sleep(0x3E8:i)
Update
ShowEff(0x1:b, 0xFF:b, Self, 0x0:s, 0x0:i, 0x1838:i, 0x258:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0x2:b)
RotationAngleHorz(0x3E8:i, 0x1388:i)
Sleep(0x1F4:i)
Update
CancelEff(Self, 0x4:b)
OP_95
SetAngleTarget(0xFC:b, "", 0x0:s)
MoveAngle(0xC8:i, 0x3E8:s, 0x4B0:s)
RotationAngle(0x0:i, 0x1B58:i, 0xFFFF8AD0:i, 0x1388:i)
MagicWaitEff

#loc_0727
LoopTargetBegin(loc_0753:s)
ShowEff(0x1:b, 0xFF:b, Self, 0x1:s, 0x0:i, 0xFA0:i, 0x1F4:i, 0x0:s, 0x0:s, 0x0:s, 0x3E8:s, 0x3E8:s, 0x3E8:s, 0xFF:b)
Sleep(0x12C:i)
Update
LoopTargetEnd
Goto(loc_0727:s)

#loc_0753
OP_14(0x1:s)
Call(loc_038B:s)
OP_8F(0x0:b)
SuspendThread(Self, Thread1)
ZoomAngle(0x1:b, 0x12C:i, 0x0:i)
OP_5B(0x0:i)
OP_31(0x17:b, 0x0:i)
End

#loc_0774
OP_46(Self, 0xFB:i, 0x122:i)
OP_47(Self)
Goto(loc_0774:s)

