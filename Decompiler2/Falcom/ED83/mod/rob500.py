import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *

scena = createScenaWriter('rob500.dat')

# id: 0x0000 offset: 0x2F4
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_ROB004_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_ROB004_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_ROB004_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_ROB004_DF1',
            symbol     = 'WALK_W',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1001',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1002',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1003',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1003a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1004',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_ROB004_EV1',
            symbol     = 'evk1032',
        ),
    )

@scena.Code('PreInit')
def PreInit():
    AnimeClipCtrl(0x0D, 0xFFFE)

    end = genLabel()

    If(
        (
            (Expr.Eval, "OP_54(0x0A, 0x00)"),
            Expr.Return,
        ),
        end,
    )

    If(
        (
            (Expr.Eval, "BattleCtrl(0x87)"),
            Expr.Ez,
            Expr.Return,
        ),
        end,
    )

    AnimeClipCtrl(0x0E, 0xFFFE, 0x00000400, 'C_ROB004_DF1', 'WAIT')

    def _loc_5509(): pass

    label(end)

    Return()

# id: 0x0001 offset: 0x5E8
@scena.Code('Init')
def Init():
    OP_B2(0x06, 0xFFFE)
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0002 offset: 0x5F8
@scena.Code('AniReset')
def AniReset():
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_76(0xFFFE, 'L_arm_point', 'wait1', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0003 offset: 0x640
@scena.Code('AniAttachEQU204')
def AniAttachEQU204():
    LoadAsset('C_EQU204')
    AttachEquip(0xFFFE, 'C_EQU204', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C2',
    )

    OP_76(0xFFFE, 'R_arm_point', 'wait0', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Jump('loc_6E9')

    def _loc_6C2(): pass

    label('loc_6C2')

    OP_76(0xFFFE, 'R_arm_point', 'wait1', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    def _loc_6E9(): pass

    label('loc_6E9')

    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x0004 offset: 0x6FC
@scena.Code('AniDetachEQU204')
def AniDetachEQU204():
    ReleaseAsset('C_EQU204')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x0005 offset: 0x740
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000100 | 0x01 | 0x02)

    Return()

# id: 0x0006 offset: 0x74C
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000100 | 0x01 | 0x02)

    Return()

# id: 0x0007 offset: 0x758
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0008 offset: 0x764
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0009 offset: 0x770
@scena.Code('AniWait')
def AniWait():
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x000A offset: 0x790
@scena.Code('AniSitWait')
def AniSitWait():
    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x000B offset: 0x7BC
@scena.Code('AniWalk')
def AniWalk():
    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x000C offset: 0x7E4
@scena.Code('AniWalk_W')
def AniWalk_W():
    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'WALK_W', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x000D offset: 0x80C
@scena.Code('AniTurn')
def AniTurn():
    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(250)
    OP_38(0xFFFE, 0x00, 0x00, 'AniWait')

    Return()

@scena.Code('AniBtlInit')
def AniBtlInit():
    ChrPhysicsCtrl(0x00, 0xFFFE, 0x00000010)

    OP_0A(
        0x05,
        (
            (Expr.Eval, "BattleCtrl(0x62, 0xFFFE, 0x00)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'Ani_BT1_Load')
    Call(ScriptId.Current, 'AniAttachEQU204')

    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

@scena.Code('AniBtlStart')
def AniBtlStart():
    Return()

# id: 0x000E offset: 0x844
@scena.Code('AniEvk1000')
def AniEvk1000():
    PlayChrAnimeClip(0xFFFE, 'evk1000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x000F offset: 0x870
@scena.Code('AniEvk1001')
def AniEvk1001():
    PlayChrAnimeClip(0xFFFE, 'evk1001', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0010 offset: 0x89C
@scena.Code('AniEvk1002')
def AniEvk1002():
    PlayChrAnimeClip(0xFFFE, 'evk1002', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0011 offset: 0x8C8
@scena.Code('AniEvk1003')
def AniEvk1003():
    PlayChrAnimeClip(0xFFFE, 'evk1003', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'evk1003a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0012 offset: 0x920
@scena.Code('AniAttachEQU200_C00')
def AniAttachEQU200_C00():
    LoadAsset('C_EQU200_C00')
    AttachEquip(0xFFFE, 'C_EQU200_C00', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_76(0xFFFE, 'R_arm_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0013 offset: 0x9AC
@scena.Code('AniDetachEQU200_C00')
def AniDetachEQU200_C00():
    ReleaseAsset('C_EQU200_C00')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x0014 offset: 0x9F8
@scena.Code('AniAttachEQU200_C01')
def AniAttachEQU200_C01():
    LoadAsset('C_EQU200_C01')
    AttachEquip(0xFFFE, 'C_EQU200_C01', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_76(0xFFFE, 'R_arm_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0015 offset: 0xA84
@scena.Code('AniDetachEQU200_C01')
def AniDetachEQU200_C01():
    ReleaseAsset('C_EQU200_C01')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x0016 offset: 0xAD0
@scena.Code('AniEvk1004')
def AniEvk1004():
    PlayChrAnimeClip(0xFFFE, 'evk1004', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0017 offset: 0xAFC
@scena.Code('AniEvk1032')
def AniEvk1032():
    PlayChrAnimeClip(0xFFFE, 'evk1032', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0018 offset: 0xB30
@scena.AnimeClips('_AniAttachEQU204')
def _AniAttachEQU204():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU204',
        ),
    )

# id: 0x0019 offset: 0xB90
@scena.AnimeClips('_AniWait')
def _AniWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x001A offset: 0xBF0
@scena.AnimeClips('_AniSitWait')
def _AniSitWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
    )

# id: 0x001B offset: 0xC50
@scena.AnimeClips('_AniWalk')
def _AniWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x001C offset: 0xCB0
@scena.AnimeClips('_AniWalk_W')
def _AniWalk_W():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK_W',
        ),
    )

# id: 0x001D offset: 0xD10
@scena.AnimeClips('_AniTurn')
def _AniTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x001E offset: 0xD70
@scena.AnimeClips('_AniEvk1000')
def _AniEvk1000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1000',
        ),
    )

# id: 0x001F offset: 0xDD0
@scena.AnimeClips('_AniEvk1001')
def _AniEvk1001():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1001',
        ),
    )

# id: 0x0020 offset: 0xE30
@scena.AnimeClips('_AniEvk1002')
def _AniEvk1002():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1002',
        ),
    )

# id: 0x0021 offset: 0xE90
@scena.AnimeClips('_AniEvk1003')
def _AniEvk1003():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1003',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1003a',
        ),
    )

# id: 0x0022 offset: 0xF10
@scena.AnimeClips('_AniAttachEQU200_C00')
def _AniAttachEQU200_C00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU200_C00',
        ),
    )

# id: 0x0023 offset: 0xF70
@scena.AnimeClips('_AniAttachEQU200_C01')
def _AniAttachEQU200_C01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU200_C01',
        ),
    )

# id: 0x0024 offset: 0xFD0
@scena.AnimeClips('_AniEvk1004')
def _AniEvk1004():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1004',
        ),
    )

# id: 0x0025 offset: 0x1030
@scena.AnimeClips('_AniEvk1032')
def _AniEvk1032():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'evk1032',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
