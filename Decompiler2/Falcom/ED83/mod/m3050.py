import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *
import m3050_hook

scena = createScenaWriter('m3050.dat')

# id: 0x0000 offset: 0x404
@scena.Code('')
def func_404():
    Return()

# id: 0x0001 offset: 0x408
@scena.BattleSetting('')
def func_408():
    return ScenaBattleSetting(
        mapName        = '',
        x              = -44.29999923706055,
        y              = 114.0,
        z              = 0.05000000074505806,
        direction      = 69.9000015258789,
        length         = 20.0,
        width          = -1.0,
        word28         = 411,
        flags          = 0x00000009,
        bgm            = 465,
        dangerBGM      = 465,
        word34         = 0,
        word36         = 0,
        atBonus        = 3,
        battleScript   = 'btl0411',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr033_0', 'chr035_1', 'chr037_0', 'chr039_0', '', '', '', ''],
                encounterProbability    = [100, 100, 100, 100, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0002 offset: 0x508
@scena.BattleSetting('')
def func_508():
    return ScenaBattleSetting(
        mapName        = '',
        x              = -46.25,
        y              = 114.0,
        z              = 0.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 1009,
        flags          = 0x00000000,
        bgm            = 460,
        dangerBGM      = 460,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl1009',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['rob022_1', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0003 offset: 0x608
@scena.BattleSetting('')
def func_608():
    return ScenaBattleSetting(
        mapName        = '',
        x              = -46.25,
        y              = 114.0,
        z              = 0.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 1010,
        flags          = 0x00000000,
        bgm            = 460,
        dangerBGM      = 460,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl1010',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['rob022_2', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0004 offset: 0x708
@scena.BattleSetting('')
def func_708():
    return ScenaBattleSetting(
        mapName        = '',
        x              = -46.25,
        y              = 114.0,
        z              = 0.0,
        direction      = 90.0,
        length         = 20.0,
        width          = -1.0,
        word28         = 1011,
        flags          = 0x00000000,
        bgm            = 460,
        dangerBGM      = 460,
        word34         = 0,
        word36         = 0,
        atBonus        = 0,
        battleScript   = 'btl1011',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['rob022_3', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0005
@scena.BattleSetting('')
def func_408():
    return ScenaBattleSetting(
        mapName        = 'f6000',
        x              = 0.0,
        y              = -3.8,
        z              = 15.0,
        direction      = 0.0,
        length         = 20.0,
        width          = 20.0,
        word28         = 411,
        flags          = 0x00000009,
        bgm            = 466,
        dangerBGM      = 466,
        word34         = 0,
        word36         = 0,
        atBonus        = 3,
        battleScript   = 'btl9000',
        monsterSet     = [
            ScenaBattleMonsterSet(
                id                      = 0x0,
                monsters                = ['chr500_0', '', '', '', '', '', '', ''],
                encounterProbability    = [100, 0, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )

# id: 0x0005 offset: 0x808
@scena.Code('PreInit')
def PreInit():
    Call(ScriptId.System, 'FC_Change_MapColor')
    OP_AC(0x00, 0x00)

    Return()

# id: 0x0006 offset: 0x824
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_78(0x00, 'go_m3020_a2')"),
            Expr.Return,
        ),
        'loc_83C',
    )

    SetScenaFlags(ScenaFlag(0x0465, 7, 0x232F))

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.Eval, "OP_78(0x00, 'go_m3030_b0')"),
            Expr.Return,
        ),
        'loc_854',
    )

    SetScenaFlags(ScenaFlag(0x0466, 0, 0x2330))

    def _loc_854(): pass

    label('loc_854')

    Call(ScriptId.Sound, 'Init_ENVSE')
    Call(ScriptId.Sound, 'Init_BGM')
    OP_54(0x14, 'BreakObj00', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj01', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj02', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj03', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj04', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj05', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj06', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj07', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj08', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj09', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x14, 'BreakObj10', 'FC_dropItem', 0x0000, 0x0028, 0x0081, 0x0000, 0x0000, 0x0000)
    OP_54(0x19, 'HealObj00', 'LP_healobject0')
    OP_54(0x19, 'HealObj01', 'LP_healobject1')
    Call(ScriptId.Current, 'Init_Replay')
    OP_86(0xFF, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, '')

    Return()

# id: 0x0007 offset: 0xA68
@scena.Code('Init_Replay')
def Init_Replay():
    OP_68(0x01, 'Cockpit01', 0x0001)
    OP_68(0x01, 'Cockpit01', 0x0002)
    OP_68(0x00, 'Cockpit01', 0x0004)
    OP_68(0x01, 'Cockpit02', 0x0001)
    OP_68(0x01, 'Cockpit02', 0x0002)
    OP_68(0x00, 'Cockpit02', 0x0004)
    SetLookpointFlag(0x01, 'LP_EV_03_80_01_A', 0x0001)
    SetLookpointFlag(0x01, 'LP_EV_03_80_01_B', 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x016F, 4, 0xB7C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0170, 0, 0xB80)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B1E',
    )

    SetLookpointFlag(0x00, 'LP_EV_03_80_01_A', 0x0001)
    SetLookpointFlag(0x00, 'LP_EV_03_80_01_B', 0x0001)

    def _loc_B1E(): pass

    label('loc_B1E')

    OP_50((0xDD, 'bridge00'), 'close1_c')
    OP_50((0xDD, 'bridge01'), 'close1_c')
    OP_50((0xDD, 'switch00'), 'locked')
    OP_50((0xDD, 'switch01'), 'locked')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Return,
        ),
        'loc_20FC',
    )

    OP_50((0xDD, 'cannon00'), 'wait0')
    OP_50((0xDD, 'cannon01'), 'wait0')
    OP_50((0xDD, 'cannon02'), 'wait0')
    OP_50((0xDD, 'cannon03'), 'wait0')
    OP_50((0xDD, 'cannon04'), 'wait0')
    OP_50((0xDD, 'cannon05'), 'wait0')
    OP_50((0xDD, 'cannon06'), 'wait0')
    OP_50((0xDD, 'cannon07'), 'wait0')
    OP_50((0xDD, 'cannon08'), 'wait0')
    OP_50((0xDD, 'cannon09'), 'wait0')
    OP_50((0xDD, 'cannon10'), 'wait0')
    OP_50((0xDD, 'cannon11'), 'wait0')
    OP_50((0xDD, 'cannon12'), 'wait0')
    OP_50((0xDD, 'cannon13'), 'wait0')
    OP_50((0xDD, 'cannon14'), 'wait0')
    OP_50((0xDD, 'cannon15'), 'wait0')
    OP_50((0xDD, 'cannon16'), 'wait0')
    OP_50((0xDD, 'cannon17'), 'wait0')
    OP_50((0xDD, 'cannon18'), 'wait0')
    OP_50((0xDD, 'cannon19'), 'wait0')
    OP_50((0xDD, 'cannon20'), 'wait0')
    OP_50((0xDD, 'cannon21'), 'wait0')
    OP_50((0xDD, 'cannon22'), 'wait0')
    OP_50((0xDD, 'cannon23'), 'wait0')
    OP_50((0xDD, 'cannon24'), 'wait0')
    OP_68(0x01, 'emblem', 0x0001)
    OP_68(0x01, 'emblem', 0x0002)
    OP_68(0x00, 'emblem', 0x0004)
    OP_68(0x01, 'flag_r00', 0x0001)
    OP_68(0x01, 'flag_r00', 0x0002)
    OP_68(0x00, 'flag_r00', 0x0004)
    OP_68(0x01, 'flag_r01', 0x0001)
    OP_68(0x01, 'flag_r01', 0x0002)
    OP_68(0x00, 'flag_r01', 0x0004)
    OP_68(0x01, 'flag_r02', 0x0001)
    OP_68(0x01, 'flag_r02', 0x0002)
    OP_68(0x00, 'flag_r02', 0x0004)
    OP_68(0x01, 'flag_r03', 0x0001)
    OP_68(0x01, 'flag_r03', 0x0002)
    OP_68(0x00, 'flag_r03', 0x0004)
    OP_68(0x01, 'kemuri01', 0x0001)
    OP_68(0x01, 'kemuri01', 0x0002)
    OP_68(0x00, 'kemuri01', 0x0004)
    OP_68(0x01, 'kemuri02', 0x0001)
    OP_68(0x01, 'kemuri02', 0x0002)
    OP_68(0x00, 'kemuri02', 0x0004)
    OP_68(0x01, 'kemuri03', 0x0001)
    OP_68(0x01, 'kemuri03', 0x0002)
    OP_68(0x00, 'kemuri03', 0x0004)
    OP_68(0x01, 'kemuri04', 0x0001)
    OP_68(0x01, 'kemuri04', 0x0002)
    OP_68(0x00, 'kemuri04', 0x0004)
    OP_68(0x01, 'kemuri05', 0x0001)
    OP_68(0x01, 'kemuri05', 0x0002)
    OP_68(0x00, 'kemuri05', 0x0004)
    OP_68(0x01, 'kemuri06', 0x0001)
    OP_68(0x01, 'kemuri06', 0x0002)
    OP_68(0x00, 'kemuri06', 0x0004)
    OP_68(0x01, 'kemuri07', 0x0001)
    OP_68(0x01, 'kemuri07', 0x0002)
    OP_68(0x00, 'kemuri07', 0x0004)
    OP_68(0x01, 'kemuri08', 0x0001)
    OP_68(0x01, 'kemuri08', 0x0002)
    OP_68(0x00, 'kemuri08', 0x0004)
    OP_68(0x01, 'kemuri09', 0x0001)
    OP_68(0x01, 'kemuri09', 0x0002)
    OP_68(0x00, 'kemuri09', 0x0004)
    OP_68(0x01, 'kemuri10', 0x0001)
    OP_68(0x01, 'kemuri10', 0x0002)
    OP_68(0x00, 'kemuri10', 0x0004)
    OP_68(0x01, 'kemuri11', 0x0001)
    OP_68(0x01, 'kemuri11', 0x0002)
    OP_68(0x00, 'kemuri11', 0x0004)
    OP_68(0x01, 'kemuri12', 0x0001)
    OP_68(0x01, 'kemuri12', 0x0002)
    OP_68(0x00, 'kemuri12', 0x0004)
    OP_68(0x01, 'kemuri13', 0x0001)
    OP_68(0x01, 'kemuri13', 0x0002)
    OP_68(0x00, 'kemuri13', 0x0004)
    OP_68(0x01, 'kemuri14', 0x0001)
    OP_68(0x01, 'kemuri14', 0x0002)
    OP_68(0x00, 'kemuri14', 0x0004)
    OP_68(0x01, 'kemuri15', 0x0001)
    OP_68(0x01, 'kemuri15', 0x0002)
    OP_68(0x00, 'kemuri15', 0x0004)
    OP_68(0x01, 'kemuri16', 0x0001)
    OP_68(0x01, 'kemuri16', 0x0002)
    OP_68(0x00, 'kemuri16', 0x0004)
    OP_68(0x01, 'kemuri17', 0x0001)
    OP_68(0x01, 'kemuri17', 0x0002)
    OP_68(0x00, 'kemuri17', 0x0004)
    OP_68(0x01, 'kemuri18', 0x0001)
    OP_68(0x01, 'kemuri18', 0x0002)
    OP_68(0x00, 'kemuri18', 0x0004)
    OP_68(0x01, 'kemuri19', 0x0001)
    OP_68(0x01, 'kemuri19', 0x0002)
    OP_68(0x00, 'kemuri19', 0x0004)
    OP_68(0x01, 'kemuri20', 0x0001)
    OP_68(0x01, 'kemuri20', 0x0002)
    OP_68(0x00, 'kemuri20', 0x0004)
    OP_68(0x01, 'kemuri21', 0x0001)
    OP_68(0x01, 'kemuri21', 0x0002)
    OP_68(0x00, 'kemuri21', 0x0004)
    OP_68(0x01, 'kemuri22', 0x0001)
    OP_68(0x01, 'kemuri22', 0x0002)
    OP_68(0x00, 'kemuri22', 0x0004)
    OP_68(0x01, 'kemuri23', 0x0001)
    OP_68(0x01, 'kemuri23', 0x0002)
    OP_68(0x00, 'kemuri23', 0x0004)
    OP_68(0x01, 'kemuri24', 0x0001)
    OP_68(0x01, 'kemuri24', 0x0002)
    OP_68(0x00, 'kemuri24', 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_193F',
    )

    OP_50((0xDD, 'cannon00'), 'down1_c')
    OP_50((0xDD, 'cannon01'), 'down1_c')
    OP_50((0xDD, 'cannon02'), 'down1_c')
    OP_50((0xDD, 'cannon03'), 'down1_c')
    OP_50((0xDD, 'cannon04'), 'down1_c')
    OP_50((0xDD, 'cannon05'), 'down1_c')
    OP_50((0xDD, 'cannon06'), 'down1_c')
    OP_50((0xDD, 'cannon07'), 'down1_c')
    OP_50((0xDD, 'cannon08'), 'down1_c')
    OP_50((0xDD, 'cannon09'), 'down1_c')
    OP_50((0xDD, 'cannon10'), 'down1_c')
    OP_50((0xDD, 'cannon11'), 'down1_c')
    OP_50((0xDD, 'cannon12'), 'down1_c')
    OP_50((0xDD, 'cannon13'), 'down1_c')
    OP_50((0xDD, 'cannon14'), 'down1_c')
    OP_50((0xDD, 'cannon15'), 'down1_c')
    OP_50((0xDD, 'cannon16'), 'down1_c')
    OP_50((0xDD, 'cannon17'), 'down1_c')
    OP_50((0xDD, 'cannon18'), 'down1_c')
    OP_50((0xDD, 'cannon19'), 'down1_c')
    OP_50((0xDD, 'cannon20'), 'down1_c')
    OP_50((0xDD, 'cannon21'), 'down1_c')
    OP_50((0xDD, 'cannon22'), 'down1_c')
    OP_50((0xDD, 'cannon23'), 'down1_c')
    OP_50((0xDD, 'cannon24'), 'down1_c')
    OP_68(0x00, 'emblem', 0x0001)
    OP_68(0x00, 'emblem', 0x0002)
    OP_68(0x01, 'emblem', 0x0004)
    OP_68(0x05, 'emblem')
    OP_68(0x00, 'flag_r00', 0x0001)
    OP_68(0x00, 'flag_r00', 0x0002)
    OP_68(0x01, 'flag_r00', 0x0004)
    OP_68(0x05, 'flag_r00')
    OP_68(0x00, 'flag_r01', 0x0001)
    OP_68(0x00, 'flag_r01', 0x0002)
    OP_68(0x01, 'flag_r01', 0x0004)
    OP_68(0x05, 'flag_r01')
    OP_68(0x00, 'flag_r02', 0x0001)
    OP_68(0x00, 'flag_r02', 0x0002)
    OP_68(0x01, 'flag_r02', 0x0004)
    OP_68(0x05, 'flag_r02')
    OP_68(0x00, 'flag_r03', 0x0001)
    OP_68(0x00, 'flag_r03', 0x0002)
    OP_68(0x01, 'flag_r03', 0x0004)
    OP_68(0x05, 'flag_r03')
    OP_68(0x00, 'kemuri00', 0x0001)
    OP_68(0x00, 'kemuri00', 0x0002)
    OP_68(0x01, 'kemuri00', 0x0004)
    OP_68(0x05, 'kemuri00')
    OP_68(0x00, 'kemuri01', 0x0001)
    OP_68(0x00, 'kemuri01', 0x0002)
    OP_68(0x01, 'kemuri01', 0x0004)
    OP_68(0x05, 'kemuri01')
    OP_68(0x00, 'kemuri02', 0x0001)
    OP_68(0x00, 'kemuri02', 0x0002)
    OP_68(0x01, 'kemuri02', 0x0004)
    OP_68(0x05, 'kemuri02')
    OP_68(0x00, 'kemuri03', 0x0001)
    OP_68(0x00, 'kemuri03', 0x0002)
    OP_68(0x01, 'kemuri03', 0x0004)
    OP_68(0x05, 'kemuri03')
    OP_68(0x00, 'kemuri04', 0x0001)
    OP_68(0x00, 'kemuri04', 0x0002)
    OP_68(0x01, 'kemuri04', 0x0004)
    OP_68(0x05, 'kemuri04')
    OP_68(0x00, 'kemuri05', 0x0001)
    OP_68(0x00, 'kemuri05', 0x0002)
    OP_68(0x01, 'kemuri05', 0x0004)
    OP_68(0x05, 'kemuri05')
    OP_68(0x00, 'kemuri06', 0x0001)
    OP_68(0x00, 'kemuri06', 0x0002)
    OP_68(0x01, 'kemuri06', 0x0004)
    OP_68(0x05, 'kemuri06')
    OP_68(0x00, 'kemuri07', 0x0001)
    OP_68(0x00, 'kemuri07', 0x0002)
    OP_68(0x01, 'kemuri07', 0x0004)
    OP_68(0x05, 'kemuri07')
    OP_68(0x00, 'kemuri08', 0x0001)
    OP_68(0x00, 'kemuri08', 0x0002)
    OP_68(0x01, 'kemuri08', 0x0004)
    OP_68(0x05, 'kemuri08')
    OP_68(0x00, 'kemuri09', 0x0001)
    OP_68(0x00, 'kemuri09', 0x0002)
    OP_68(0x01, 'kemuri09', 0x0004)
    OP_68(0x05, 'kemuri09')
    OP_68(0x00, 'kemuri10', 0x0001)
    OP_68(0x00, 'kemuri10', 0x0002)
    OP_68(0x01, 'kemuri10', 0x0004)
    OP_68(0x05, 'kemuri10')
    OP_68(0x00, 'kemuri11', 0x0001)
    OP_68(0x00, 'kemuri11', 0x0002)
    OP_68(0x01, 'kemuri11', 0x0004)
    OP_68(0x05, 'kemuri11')
    OP_68(0x00, 'kemuri12', 0x0001)
    OP_68(0x00, 'kemuri12', 0x0002)
    OP_68(0x01, 'kemuri12', 0x0004)
    OP_68(0x05, 'kemuri12')
    OP_68(0x00, 'kemuri13', 0x0001)
    OP_68(0x00, 'kemuri13', 0x0002)
    OP_68(0x01, 'kemuri13', 0x0004)
    OP_68(0x05, 'kemuri13')
    OP_68(0x00, 'kemuri14', 0x0001)
    OP_68(0x00, 'kemuri14', 0x0002)
    OP_68(0x01, 'kemuri14', 0x0004)
    OP_68(0x05, 'kemuri14')
    OP_68(0x00, 'kemuri15', 0x0001)
    OP_68(0x00, 'kemuri15', 0x0002)
    OP_68(0x01, 'kemuri15', 0x0004)
    OP_68(0x05, 'kemuri15')
    OP_68(0x00, 'kemuri16', 0x0001)
    OP_68(0x00, 'kemuri16', 0x0002)
    OP_68(0x01, 'kemuri16', 0x0004)
    OP_68(0x05, 'kemuri16')
    OP_68(0x00, 'kemuri17', 0x0001)
    OP_68(0x00, 'kemuri17', 0x0002)
    OP_68(0x01, 'kemuri17', 0x0004)
    OP_68(0x05, 'kemuri17')
    OP_68(0x00, 'kemuri18', 0x0001)
    OP_68(0x00, 'kemuri18', 0x0002)
    OP_68(0x01, 'kemuri18', 0x0004)
    OP_68(0x05, 'kemuri18')
    OP_68(0x00, 'kemuri19', 0x0001)
    OP_68(0x00, 'kemuri19', 0x0002)
    OP_68(0x01, 'kemuri19', 0x0004)
    OP_68(0x05, 'kemuri19')
    OP_68(0x00, 'kemuri20', 0x0001)
    OP_68(0x00, 'kemuri20', 0x0002)
    OP_68(0x01, 'kemuri20', 0x0004)
    OP_68(0x05, 'kemuri20')
    OP_68(0x00, 'kemuri21', 0x0001)
    OP_68(0x00, 'kemuri21', 0x0002)
    OP_68(0x01, 'kemuri21', 0x0004)
    OP_68(0x05, 'kemuri21')
    OP_68(0x00, 'kemuri22', 0x0001)
    OP_68(0x00, 'kemuri22', 0x0002)
    OP_68(0x01, 'kemuri22', 0x0004)
    OP_68(0x05, 'kemuri22')
    OP_68(0x00, 'kemuri23', 0x0001)
    OP_68(0x00, 'kemuri23', 0x0002)
    OP_68(0x01, 'kemuri23', 0x0004)
    OP_68(0x05, 'kemuri23')
    OP_68(0x00, 'kemuri24', 0x0001)
    OP_68(0x00, 'kemuri24', 0x0002)
    OP_68(0x01, 'kemuri24', 0x0004)
    OP_68(0x05, 'kemuri24')

    Jump('loc_20FC')

    def _loc_193F(): pass

    label('loc_193F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x016E, 3, 0xB73)),
            (Expr.TestScenaFlags, ScenaFlag(0x0170, 0, 0xB80)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20FC',
    )

    OP_50((0xDD, 'cannon00'), 'down1_c')
    OP_50((0xDD, 'cannon01'), 'down1_c')
    OP_50((0xDD, 'cannon02'), 'down1_c')
    OP_50((0xDD, 'cannon03'), 'down1_c')
    OP_50((0xDD, 'cannon04'), 'down1_c')
    OP_50((0xDD, 'cannon05'), 'down1_c')
    OP_50((0xDD, 'cannon06'), 'down1_c')
    OP_50((0xDD, 'cannon07'), 'down1_c')
    OP_50((0xDD, 'cannon08'), 'down1_c')
    OP_50((0xDD, 'cannon09'), 'down1_c')
    OP_50((0xDD, 'cannon10'), 'down1_c')
    OP_50((0xDD, 'cannon11'), 'down1_c')
    OP_50((0xDD, 'cannon12'), 'down1_c')
    OP_50((0xDD, 'cannon13'), 'down1_c')
    OP_50((0xDD, 'cannon14'), 'down1_c')
    OP_50((0xDD, 'cannon15'), 'down1_c')
    OP_50((0xDD, 'cannon16'), 'down1_c')
    OP_50((0xDD, 'cannon17'), 'down1_c')
    OP_50((0xDD, 'cannon18'), 'down1_c')
    OP_50((0xDD, 'cannon19'), 'down1_c')
    OP_50((0xDD, 'cannon20'), 'down1_c')
    OP_50((0xDD, 'cannon21'), 'down1_c')
    OP_50((0xDD, 'cannon22'), 'down1_c')
    OP_50((0xDD, 'cannon23'), 'down1_c')
    OP_50((0xDD, 'cannon24'), 'down1_c')
    OP_68(0x00, 'emblem', 0x0001)
    OP_68(0x00, 'emblem', 0x0002)
    OP_68(0x01, 'emblem', 0x0004)
    OP_68(0x05, 'emblem')
    OP_68(0x00, 'flag_r00', 0x0001)
    OP_68(0x00, 'flag_r00', 0x0002)
    OP_68(0x01, 'flag_r00', 0x0004)
    OP_68(0x05, 'flag_r00')
    OP_68(0x00, 'flag_r01', 0x0001)
    OP_68(0x00, 'flag_r01', 0x0002)
    OP_68(0x01, 'flag_r01', 0x0004)
    OP_68(0x05, 'flag_r01')
    OP_68(0x00, 'flag_r02', 0x0001)
    OP_68(0x00, 'flag_r02', 0x0002)
    OP_68(0x01, 'flag_r02', 0x0004)
    OP_68(0x05, 'flag_r02')
    OP_68(0x00, 'flag_r03', 0x0001)
    OP_68(0x00, 'flag_r03', 0x0002)
    OP_68(0x01, 'flag_r03', 0x0004)
    OP_68(0x05, 'flag_r03')
    OP_68(0x00, 'kemuri00', 0x0001)
    OP_68(0x00, 'kemuri00', 0x0002)
    OP_68(0x01, 'kemuri00', 0x0004)
    OP_68(0x05, 'kemuri00')
    OP_68(0x00, 'kemuri01', 0x0001)
    OP_68(0x00, 'kemuri01', 0x0002)
    OP_68(0x01, 'kemuri01', 0x0004)
    OP_68(0x05, 'kemuri01')
    OP_68(0x00, 'kemuri02', 0x0001)
    OP_68(0x00, 'kemuri02', 0x0002)
    OP_68(0x01, 'kemuri02', 0x0004)
    OP_68(0x05, 'kemuri02')
    OP_68(0x00, 'kemuri03', 0x0001)
    OP_68(0x00, 'kemuri03', 0x0002)
    OP_68(0x01, 'kemuri03', 0x0004)
    OP_68(0x05, 'kemuri03')
    OP_68(0x00, 'kemuri04', 0x0001)
    OP_68(0x00, 'kemuri04', 0x0002)
    OP_68(0x01, 'kemuri04', 0x0004)
    OP_68(0x05, 'kemuri04')
    OP_68(0x00, 'kemuri05', 0x0001)
    OP_68(0x00, 'kemuri05', 0x0002)
    OP_68(0x01, 'kemuri05', 0x0004)
    OP_68(0x05, 'kemuri05')
    OP_68(0x00, 'kemuri06', 0x0001)
    OP_68(0x00, 'kemuri06', 0x0002)
    OP_68(0x01, 'kemuri06', 0x0004)
    OP_68(0x05, 'kemuri06')
    OP_68(0x00, 'kemuri07', 0x0001)
    OP_68(0x00, 'kemuri07', 0x0002)
    OP_68(0x01, 'kemuri07', 0x0004)
    OP_68(0x05, 'kemuri07')
    OP_68(0x00, 'kemuri08', 0x0001)
    OP_68(0x00, 'kemuri08', 0x0002)
    OP_68(0x01, 'kemuri08', 0x0004)
    OP_68(0x05, 'kemuri08')
    OP_68(0x00, 'kemuri09', 0x0001)
    OP_68(0x00, 'kemuri09', 0x0002)
    OP_68(0x01, 'kemuri09', 0x0004)
    OP_68(0x05, 'kemuri09')
    OP_68(0x00, 'kemuri10', 0x0001)
    OP_68(0x00, 'kemuri10', 0x0002)
    OP_68(0x01, 'kemuri10', 0x0004)
    OP_68(0x05, 'kemuri10')
    OP_68(0x00, 'kemuri11', 0x0001)
    OP_68(0x00, 'kemuri11', 0x0002)
    OP_68(0x01, 'kemuri11', 0x0004)
    OP_68(0x05, 'kemuri11')
    OP_68(0x00, 'kemuri12', 0x0001)
    OP_68(0x00, 'kemuri12', 0x0002)
    OP_68(0x01, 'kemuri12', 0x0004)
    OP_68(0x05, 'kemuri12')
    OP_68(0x00, 'kemuri13', 0x0001)
    OP_68(0x00, 'kemuri13', 0x0002)
    OP_68(0x01, 'kemuri13', 0x0004)
    OP_68(0x05, 'kemuri13')
    OP_68(0x00, 'kemuri14', 0x0001)
    OP_68(0x00, 'kemuri14', 0x0002)
    OP_68(0x01, 'kemuri14', 0x0004)
    OP_68(0x05, 'kemuri14')
    OP_68(0x00, 'kemuri15', 0x0001)
    OP_68(0x00, 'kemuri15', 0x0002)
    OP_68(0x01, 'kemuri15', 0x0004)
    OP_68(0x05, 'kemuri15')
    OP_68(0x00, 'kemuri16', 0x0001)
    OP_68(0x00, 'kemuri16', 0x0002)
    OP_68(0x01, 'kemuri16', 0x0004)
    OP_68(0x05, 'kemuri16')
    OP_68(0x00, 'kemuri17', 0x0001)
    OP_68(0x00, 'kemuri17', 0x0002)
    OP_68(0x01, 'kemuri17', 0x0004)
    OP_68(0x05, 'kemuri17')
    OP_68(0x00, 'kemuri18', 0x0001)
    OP_68(0x00, 'kemuri18', 0x0002)
    OP_68(0x01, 'kemuri18', 0x0004)
    OP_68(0x05, 'kemuri18')
    OP_68(0x00, 'kemuri19', 0x0001)
    OP_68(0x00, 'kemuri19', 0x0002)
    OP_68(0x01, 'kemuri19', 0x0004)
    OP_68(0x05, 'kemuri19')
    OP_68(0x00, 'kemuri20', 0x0001)
    OP_68(0x00, 'kemuri20', 0x0002)
    OP_68(0x01, 'kemuri20', 0x0004)
    OP_68(0x05, 'kemuri20')
    OP_68(0x00, 'kemuri21', 0x0001)
    OP_68(0x00, 'kemuri21', 0x0002)
    OP_68(0x01, 'kemuri21', 0x0004)
    OP_68(0x05, 'kemuri21')
    OP_68(0x00, 'kemuri22', 0x0001)
    OP_68(0x00, 'kemuri22', 0x0002)
    OP_68(0x01, 'kemuri22', 0x0004)
    OP_68(0x05, 'kemuri22')
    OP_68(0x00, 'kemuri23', 0x0001)
    OP_68(0x00, 'kemuri23', 0x0002)
    OP_68(0x01, 'kemuri23', 0x0004)
    OP_68(0x05, 'kemuri23')
    OP_68(0x00, 'kemuri24', 0x0001)
    OP_68(0x00, 'kemuri24', 0x0002)
    OP_68(0x01, 'kemuri24', 0x0004)
    OP_68(0x05, 'kemuri24')

    def _loc_20FC(): pass

    label('loc_20FC')

    Return()

# id: 0x0008 offset: 0x2100
@scena.Code('Reinit')
def Reinit():
    Call(ScriptId.Current, 'Npc_Table')
    OP_AC(0x00, 0x01)

    Return()

# id: 0x0009 offset: 0x2114
@scena.Code('LP_EV_03_80_01_A')
def LP_EV_03_80_01_A():
    EventJump(0x00003120)
    OP_14(0x04000000)

    Return()

# id: 0x000A offset: 0x2120
@scena.Code('LP_EV_03_80_01_B')
def LP_EV_03_80_01_B():
    EventJump(0x00003120)
    OP_14(0x04000000)

    Return()

# id: 0x000B offset: 0x212C
@scena.Code('EV_switch00_setflag')
def EV_switch00_setflag():
    SetScenaFlags(ScenaFlag(0x02E8, 5, 0x1745))

    Return()

# id: 0x000C offset: 0x2130
@scena.Code('EV_switch00_resetflag00')
def EV_switch00_resetflag00():
    ClearScenaFlags(ScenaFlag(0x02E8, 5, 0x1745))

    Return()

# id: 0x000D offset: 0x2134
@scena.Code('EV_switch00_resetflag01')
def EV_switch00_resetflag01():
    ClearScenaFlags(ScenaFlag(0x02E8, 5, 0x1745))

    Return()

# id: 0x000E offset: 0x2138
@scena.Code('EV_switch01_setflag')
def EV_switch01_setflag():
    SetScenaFlags(ScenaFlag(0x02E8, 6, 0x1746))

    Return()

# id: 0x000F offset: 0x213C
@scena.Code('EV_switch01_resetflag00')
def EV_switch01_resetflag00():
    ClearScenaFlags(ScenaFlag(0x02E8, 6, 0x1746))

    Return()

# id: 0x0010 offset: 0x2140
@scena.Code('EV_switch01_resetflag01')
def EV_switch01_resetflag01():
    ClearScenaFlags(ScenaFlag(0x02E8, 6, 0x1746))

    Return()

# id: 0x0011 offset: 0x2144
@scena.Code('LP_healobject0')
def LP_healobject0():
    Call(ScriptId.System, 'FC_LpBegin')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'EV_healobject', (0xDD, 'HealObj00'))
    Call(ScriptId.System, 'FC_LpEnd')

    Return()

# id: 0x0012 offset: 0x2184
@scena.Code('LP_healobject1')
def LP_healobject1():
    Call(ScriptId.System, 'FC_LpBegin')

    OP_18(
        0xF8,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'EV_healobject', (0xDD, 'HealObj01'))
    Call(ScriptId.System, 'FC_LpEnd')

    Return()

# id: 0x0013 offset: 0x21C4
@scena.Code('AV_03047')
def AV_03047():
    OP_74(0x270F, 0x01)
    OP_74(0x0072, 0x00, 0x00000000)

    Return()

# id: 0x0014 offset: 0x21D4
@scena.Code('AV_D_EDA')
def AV_D_EDA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 6, 0x12FE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21E8',
    )

    SetScenaFlags(ScenaFlag(0x025F, 6, 0x12FE))
    ClearScenaFlags(ScenaFlag(0x025B, 3, 0x12DB))
    OP_74(0x0005, 0x04)

    def _loc_21E8(): pass

    label('loc_21E8')

    Return()

# id: 0x0015 offset: 0x21EC
@scena.Code('Npc_Table')
def Npc_Table():
    Return()

# id: 0x0016 offset: 0x21F0
@scena.Code('EV_03_76_02')
def EV_03_76_02():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3109, 0x0))
    LoadEffect(0xFFFF, 0xC8, 'battle/cr011_02_3.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom000.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evbom001.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xD2, 'event/evc35_00.eff')
    LoadEffect(0xFFFF, 0xD3, 'event/evc35_01.eff')
    LoadEffect(0xFFFF, 0xD4, 'event/evr22_04.eff')
    ChrSetPhysicsFlags(0xF011, 0x00000001)
    CreateChr(ChrTable['巴勒德侯爵'], 'C_CHR068', '巴勒德侯爵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0622, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0623, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0624, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0625, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0626, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0627, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0628, 'C_CHR386', '紫色獵兵', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    AnimeClipChangeSkin(ChrTable['鋼之雅里安洛德'], 'C_CHR033_C00')
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0622, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0623, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0624, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0625, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0626, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0627, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0628, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['巴勒德侯爵'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['巴勒德侯爵'], 0x00, 'AniEv09005', 'AniEv09010', 'AniEv09020', 'AniEvInori', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['神速杜巴莉'], 0x00, 'AniEv34540', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvUdegumiF', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvSianF', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0623, 0x00, 'AniEvGyu', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvk1023', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_28FC',
    )

    PlayBGM(512, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3A(0x06, 0x0200)

    def _loc_28FC(): pass

    label('loc_28FC')

    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['永世α'], 0x00000040)
    ChrSetPhysicsFlags(0x0622, 0x00000040)
    ChrSetPhysicsFlags(0x0623, 0x00000040)
    ChrSetPhysicsFlags(0x0624, 0x00000040)
    ChrSetPhysicsFlags(0x0625, 0x00000040)
    ChrSetPhysicsFlags(0x0626, 0x00000040)
    ChrSetPhysicsFlags(0x0627, 0x00000040)
    ChrSetPhysicsFlags(0x0628, 0x00000040)
    ChrSetPhysicsFlags(ChrTable['巴勒德侯爵'], 0x00000100)
    SetChrPos(ChrTable['巴勒德侯爵'], -14.79, 114.0, -2.36, 31.4)
    SetChrFace(0x03, ChrTable['巴勒德侯爵'], '8[autoE8]', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['鋼之雅里安洛德'], -14.71, 114.0, -1.4, 280.6)
    SetChrPos(ChrTable['神速杜巴莉'], -21.32, 114.0, -1.36, 95.4)
    SetChrPos(ChrTable['剛毅艾奈絲'], -20.28, 114.0, -2.78, 37.5)
    SetChrPos(ChrTable['魔弓恩奈雅'], -20.22, 114.0, -0.11, 127.6)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000001)
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000010)
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrPos(ChrTable['永世α'], -36.86, 114.0, 3.01, 91.8)
    ChrSetRGBA(ChrTable['永世α'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    SetChrPos(0x0622, -16.0, 114.0, -0.06, 146.7)
    SetChrPos(0x0623, -15.68, 114.0, 0.68, 157.3)
    SetChrPos(0x0624, -17.01, 114.0, -0.04, 131.3)
    SetChrPos(0x0625, 0.0, 0.0, 0.0, 0.0)
    SetChrPos(0x0626, 0.0, 0.0, 0.0, 0.0)
    SetChrPos(0x0627, 0.0, 0.0, 0.0, 0.0)
    SetChrPos(0x0628, 0.0, 0.0, 0.0, 0.0)
    ChrSetPhysicsFlags(0x0625, 0x00000010)
    OP_38(0x0625, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0625, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0625, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0626, 0x00000010)
    OP_38(0x0626, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0626, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0626, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0627, 0x00000010)
    OP_38(0x0627, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0627, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0627, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0628, 0x00000010)
    OP_38(0x0628, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0628, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0628, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    OP_50((0xDD, 'bridge00'), 'open1_c')
    OP_50((0xDD, 'bridge01'), 'open1_c')
    OP_50((0xDD, 'cannon23'), 'down1')
    OP_50((0xDD, 'cannon22'), 'down1')
    OP_50((0xDD, 'cannon21'), 'down1')
    OP_50((0xDD, 'cannon20'), 'down1')
    OP_50((0xDD, 'cannon19'), 'down1')
    OP_50((0xDD, 'cannon18'), 'down1')
    OP_50((0xDD, 'cannon06'), 'down1')
    OP_50((0xDD, 'cannon08'), 'down1')
    OP_50((0xDD, 'cannon07'), 'down1')
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 58.810001373291016, 0x0), (0xEE, 47.86000061035156, 0x0), (0xEE, -26.15999984741211, 0x0), 0.0, 0.0, 0.0, (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 59.5099983215332, 0x0), (0xEE, 46.06999969482422, 0x0), (0xEE, -37.95000076293945, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 63.68000030517578, 0x0), (0xEE, 46.58000183105469, 0x0), (0xEE, 61.970001220703125, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 63.88999938964844, 0x0), (0xEE, 46.58000183105469, 0x0), (0xEE, 78.44999694824219, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 58.29999923706055, 0x0), (0xEE, 45.34000015258789, 0x0), (0xEE, 27.440000534057617, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 16.520000457763672, 0x0), (0xEE, 53.529998779296875, 0x0), (0xEE, -64.11000061035156, 0x0), 0.0, 0.0, 0.0, (0xEE, 3.5, 0x0), (0xEE, 3.5, 0x0), (0xEE, 3.5, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 32.189998626708984, 0x0), (0xEE, 46.5099983215332, 0x0), (0xEE, 41.68000030517578, 0x0), 0.0, 0.0, 0.0, (0xEE, 3.5, 0x0), (0xEE, 3.5, 0x0), (0xEE, 3.5, 0x0), 0xFF)
    CameraSetPos(0x03, -13.23, 115.61, 1.08, 0)
    CameraRotate(0x03, 7.0, 9.0, 354.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 30.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    CameraSetPos(0x03, -10.93, 115.34, 3.32, 2500)
    CameraRotate(0x03, 357.0, 50.0, 354.0, 2500, 0x01)
    MoveType(ChrTable['巴勒德侯爵'], 0xFFFF, -11.48, 114.0, 3.06, 2.8, 0x02, 0x0000)
    OP_6C(ChrTable['巴勒德侯爵'], 0.8)
    OP_3B(0x00, (0xFF, 0x76F3, 0x0), 0.3, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x76F4, 0x0), 0.3, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_44(0x008B, 0x10, 0.15, 0x0000, 0.0)
    OP_41(0x008B, 0x00)
    OP_44(0x008B, 0xFF, 0.0, 0x0000, 0.0)
    OP_3D(ChrTable['巴勒德侯爵'], 98.3, 10.0, 0x00)
    OP_45(ChrTable['巴勒德侯爵'], 0.0, -20.0, 0.0, 0x03E8, 0x0000)
    OP_3F(ChrTable['巴勒德侯爵'])
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -10.66, 115.53, 3.71, 0)
    CameraRotate(0x03, 42.0, 302.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 2.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -10.85, 115.53, 3.37, 20000)
    CameraRotate(0x03, 43.0, 287.0, 3.0, 20000, 0x01)
    Fade(0xFF, 0, 0x0000)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x755C, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.05, 0.05, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xCA, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 50.81999969482422, 0x0), (0xEE, 41.56999969482422, 0x0), (0xEE, -22.8700008392334, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), 0xFF)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['巴勒德侯爵'], '#E_8#M_E#B_0')

    ChrTalk(
        ChrTable['巴勒德侯爵'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E89),
            '本、本來打算睡回籠覺，\n',
            '卻發生這種事……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'AniEvInori', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['巴勒德侯爵'], '#E[9]#M_E#B_0')

    ChrTalk(
        ChrTable['巴勒德侯爵'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E8A),
            '女神啊……！\n',
            '我到底是做錯了什麼啊！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('女子的聲音', 0xFFFF)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E8B),
            '#3C──怠惰和貪婪就是你的罪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            (TxtCtl.Voice, 0x8E8C),
            '#3C給我認清楚，以你的能力根本不可能\n',
            '治理帝國最大的領邦。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_27('', 0xFFFF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -10.88, 115.45, 3.25, 0)
    CameraRotate(0x03, 6.0, 54.0, 355.0, 0, 0x01)
    CameraSetDistance(0x03, 0.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -10.88, 115.43, 3.25, 1000)
    CameraRotate(0x03, 1.0, 63.0, 357.0, 10000, 0x01)
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'AniEvInori', -1.0, 1.0, 0x00000002)
    OP_45(ChrTable['巴勒德侯爵'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['巴勒德侯爵'], '#E[C]#M[J]#B_0')

    ChrTalk(
        ChrTable['巴勒德侯爵'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E8D),
            '什……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_3D(ChrTable['巴勒德侯爵'], 265.5, 10.0, 0x00)
    OP_3F(ChrTable['巴勒德侯爵'])
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -16.14, 115.09, 2.45, 0)
    CameraRotate(0x03, 352.0, 98.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 2.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -16.36, 114.81, 2.35, 5000)
    CameraRotate(0x03, 346.0, 101.0, 10.0, 5000, 0x01)
    CameraSetDistance(0x03, 2.6, 5000)
    SetChrPos(ChrTable['巴勒德侯爵'], -17.23, 114.0, 2.76, -91.0)
    ChrClearPhysicsFlags(ChrTable['永世α'], 0x00000040)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x765D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x765F, 0x0), 0.7, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xD4, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(100)
    ChrSetRGBA(ChrTable['永世α'], 1.0, 1.0, 1.0, 1.0, 400, 0x03)
    Sleep(300)
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'StopChrAnimeClip', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'AniEv09005', -1.0, 1.0, 0x00000000)
    OP_3B(0x00, (0xFF, 0x756B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['巴勒德侯爵'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['巴勒德侯爵'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E8E),
            '#4S啊──……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -16.42, 114.58, 2.46, 0)
    CameraRotate(0x03, 14.0, 153.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -15.61, 115.05, 2.93, 5000)
    CameraRotate(0x03, 29.0, 308.0, 23.0, 5000, 0x01)
    CameraSetDistance(0x03, 2.0, 5000)
    ChrClearPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -15.13, 114.0, 2.82, 276.2)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -20.0, 0.0, 0x0000, 0x0000)
    SetChrPos(ChrTable['巴勒德侯爵'], -17.23, 114.0, 2.76, -91.0)
    SetChrFace(0x03, ChrTable['巴勒德侯爵'], 'C', 'H', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x7562, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'AniEv09010', -1.0, 1.0, 0x00000000)
    Sleep(1800)
    OP_3B(0x00, (0xFF, 0x7565, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.02, 0.02, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    Sleep(2200)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['巴勒德侯爵'], '#E[11CCCCCCCCCB]#M_6#B_0')

    ChrTalk(
        ChrTable['巴勒德侯爵'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E8F),
            '#4S噫──……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -16.8, 114.75, 3.96, 0)
    CameraRotate(0x03, 1.0, 137.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 4.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -16.8, 115.17, 3.96, 6000)
    CameraRotate(0x03, 8.0, 140.0, 7.0, 6000, 0x01)
    SetChrPos(ChrTable['巴勒德侯爵'], -16.52, 114.0, 3.3, 234.2)
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['巴勒德侯爵'], 0x0000)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    SetChrPos(ChrTable['神速杜巴莉'], -22.71, 114.0, 11.42, 142.3)
    ChrSetRGBA(ChrTable['神速杜巴莉'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    PlayEffect(ChrTable['神速杜巴莉'], (0xFF, 0xD2, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x65)
    OP_3B(0x00, (0xFF, 0x770F, 0x0), 0.5, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75BB, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    MoveType(ChrTable['巴勒德侯爵'], 0xFFFF, -21.66, 114.0, 10.14, 2.8, 0x02, 0x0000)
    OP_6C(ChrTable['巴勒德侯爵'], 0.8)
    OP_44(0x008B, 0x10, 0.15, 0x0000, 0.0)
    Fade(0xFF, 0, 0x0000)
    OP_27('女孩的聲音', 0xFFFF)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E90),
            '不會讓你逃了！',
            0x8,
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)
    OP_63(0xFFFF, 0x00)
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3B(0x01, (0xFF, 0x770F, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x00, (0xFF, 0x75BE, 0x0), 0.7, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -22.13, 114.87, 10.76, 0)
    CameraRotate(0x03, 21.0, 347.0, 354.0, 0, 0x01)
    CameraSetDistance(0x03, 3.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -22.04, 114.85, 10.7, 3500)
    CameraRotate(0x03, 20.0, 351.0, 354.0, 3500, 0x01)
    CameraSetDistance(0x03, 2.7, 3500)
    OP_41(0x008B, 0x01)
    OP_44(0x008B, 0xFF, 0.0, 0x0000, 0.0)
    SetChrPos(ChrTable['巴勒德侯爵'], -22.05, 114.0, 10.79, 234.2)
    SetChrFace(0x03, ChrTable['巴勒德侯爵'], 'BBBBBBBBBBBBC', 'J', '0[autoB0]', '#b', '0')
    EffectCtrl(0x0E, 0x006D, 0x65, 0x00)
    ChrSetRGBA(ChrTable['神速杜巴莉'], 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['巴勒德侯爵'], 0x0000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEv34540', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['巴勒德侯爵'], 0x00, 'AniEv09020', -1.0, 1.0, 0x00000000)
    CameraCtrl(0x0A, 0.03, 0.03, 0.0, 0x0064, 0x015E, 0x0064, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x7569, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x756B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(500)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -21.639999389648438, 0x0), (0xEE, 114.16999816894531, 0x0), (0xEE, 10.100000381469727, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.75, 0x0), (0xEE, 0.75, 0x0), (0xEE, 0.75, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.03, 0.03, 0.0, 0x0064, 0x015E, 0x0064, 0x0000, 0x0000, 0x00)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -21.19, 114.64, 9.95, 0)
    CameraRotate(0x03, 354.0, 105.0, 354.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -21.65, 114.8, 10.11, 20000)
    CameraRotate(0x03, 355.0, 114.0, 356.0, 20000, 0x01)
    CameraSetDistance(0x03, 1.7, 20000)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrSetRGBA(ChrTable['剛毅艾奈絲'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(ChrTable['魔弓恩奈雅'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    SetChrPos(ChrTable['巴勒德侯爵'], -22.01, 114.0, 10.36, 222.8)
    SetChrPos(ChrTable['神速杜巴莉'], -22.77, 114.0, 11.63, 142.3)
    SetChrPos(ChrTable['剛毅艾奈絲'], -24.65, 114.0, 10.92, 80.3)
    SetChrPos(ChrTable['魔弓恩奈雅'], -24.97, 114.0, 12.02, 124.6)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['巴勒德侯爵'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['巴勒德侯爵'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['巴勒德侯爵'], 0x0000)
    OP_45(ChrTable['神速杜巴莉'], 0.0, -5.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['剛毅艾奈絲'], 20.0, -5.0, 0.0, 0x0000, 0x0000)
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], 'A', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], 'A', '2[autoM2]', '0[autoB0]', '#b', '0')
    PlayEffect(ChrTable['剛毅艾奈絲'], (0xFF, 0xD2, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x66)
    PlayEffect(ChrTable['魔弓恩奈雅'], (0xFF, 0xD2, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    OP_3B(0x00, (0xFF, 0x770F, 0x0), 0.7, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['剛毅艾奈絲'], (0xFF, 0xD3, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x75BB, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['魔弓恩奈雅'], (0xFF, 0xD3, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(1700)
    OP_3B(0x00, (0xFF, 0x75BE, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0E, 0x006E, 0x66, 0x00)
    ChrSetRGBA(ChrTable['剛毅艾奈絲'], 1.0, 1.0, 1.0, 1.0, 500, 0x03)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x75BE, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0E, 0x006F, 0x67, 0x00)
    ChrSetRGBA(ChrTable['魔弓恩奈雅'], 1.0, 1.0, 1.0, 1.0, 500, 0x03)
    OP_3B(0x01, (0xFF, 0x770F, 0x0), (0xFF, 0x3E8, 0x0))
    Sleep(500)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_45(ChrTable['巴勒德侯爵'], -25.0, 5.0, 0.0, 0x05DC, 0x0000)
    SetChrFace(0x04, ChrTable['巴勒德侯爵'], '#E_6#M_E#B_0')

    ChrTalk(
        ChrTable['巴勒德侯爵'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E91),
            '妳、妳們……！\n',
            '竟敢對下一個凱恩公爵如此無禮！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E[7777777777776]#M_2#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E92),
            '哼……不僅領民，\n',
            '你連來參加會議的同胞都見死不救。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvSianF', -1.0, 1.0, 0x00000000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['魔弓恩奈雅'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E93),
            '哎呀呀。\n',
            '真是臭不可聞的貴族啊。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -15.67, 115.66, 2.3, 0)
    CameraRotate(0x03, 4.0, 127.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.3, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 30.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -15.6, 115.4, 2.26, 15000)
    CameraRotate(0x03, 8.0, 107.0, 1.0, 15000, 0x01)
    ChrClearPhysicsFlags(0x0622, 0x00000040)
    ChrClearPhysicsFlags(0x0623, 0x00000040)
    ChrClearPhysicsFlags(0x0624, 0x00000040)
    ChrClearPhysicsFlags(0x0625, 0x00000040)
    ChrClearPhysicsFlags(0x0626, 0x00000040)
    ChrClearPhysicsFlags(0x0627, 0x00000040)
    ChrClearPhysicsFlags(0x0628, 0x00000040)
    SetChrPos(0x0622, -17.9, 114.0, 2.18, 84.6)
    SetChrPos(0x0623, -18.77, 114.0, 3.24, 97.6)
    SetChrPos(0x0624, -18.49, 114.0, 1.24, 77.0)
    SetChrPos(0x0625, -19.28, 114.0, 0.29, 105.4)
    SetChrPos(0x0626, -19.78, 114.0, 4.36, 107.2)
    SetChrPos(0x0627, -20.12, 114.0, 1.53, 80.5)
    SetChrPos(0x0628, -20.32, 114.0, 2.81, 89.0)
    OP_46(0x00, 0x0622, ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, 0x0623, ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, 0x0624, ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, 0x0625, ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, 0x0626, ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, 0x0627, ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, 0x0628, ChrTable['鋼之雅里安洛德'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    MoveType(0x0622, 0xFFFF, -17.45, 114.0, 2.22, 0.9, 0x01, 0x0000)
    OP_6C(0x0622, 0.7)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], 0x0622, 0x03E8)
    OP_41(0x0622, 0x00)
    SetChrFace(0x04, 0x0622, '#E_0#M_2#B_0')

    ChrTalk(
        0x0622,
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E94),
            '非常感謝您──\n',
            '給了我們赴死之地。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(0x0623, 0x00, 'AniEvGyu', -1.0, 1.0, 0x00000000)
    SetChrFace(0x04, 0x0623, '#E_0#M_2#B_0')

    ChrTalk(
        0x0623,
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E95),
            '這麼一來自治州首府#10R哈利亞斯克#被攻陷的人情，\n',
            '就能償還了。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1]#M_A#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E96),
            '呵呵，無須道謝。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -15.65, 115.47, 2.99, 0)
    CameraRotate(0x03, 16.0, 309.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.2, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    CameraSetPos(0x03, -15.5, 115.43, 2.87, 10000)
    CameraRotate(0x03, 3.0, 310.0, 6.0, 10000, 0x01)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x8E97),
            '那麼，戰爭現在才要正式開始──\n',
            '讓我看看你們最後立下的功勞吧。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3B(0x01, (0xFF, 0x76F3, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x01, (0xFF, 0x76F4, 0x0), (0xFF, 0x3E8, 0x0))
    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x00)
    OP_AC(0x06)

    Return()

# id: 0x0017 offset: 0x4638
@scena.Code('EV_03_76_02_END')
def EV_03_76_02_END():
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    ReleaseEffect(0xFFFF, 0xCB)
    ReleaseEffect(0xFFFF, 0xD2)
    ReleaseEffect(0xFFFF, 0xD3)
    ReleaseEffect(0xFFFF, 0xD4)
    AnimeClipCtrl(0x09, ChrTable['巴勒德侯爵'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['神速杜巴莉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['剛毅艾奈絲'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['魔弓恩奈雅'], 0x00)
    AnimeClipCtrl(0x09, 0x0623, 0x00)
    AnimeClipCtrl(0x09, ChrTable['永世α'], 0x00)
    ChrClearPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['巴勒德侯爵'], 0x00000100)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    EventJump(0x00000000)
    OP_14(0x04000000)

    Return()

# id: 0x0018 offset: 0x46C0
@scena.Code('EV_03_80_01')
def EV_03_80_01():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3120, 0x0))
    ChrSetPhysicsFlags(0xF011, 0x00000001)
    CreateChr(ChrTable['黎恩'], 'C_CHR000', '黎恩', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    SetChrPos(ChrTable['尤西斯'], -26.1, 110.0, 55.16, 84.7)
    SetChrPos(ChrTable['米莉亞姆'], -25.65, 110.0, 54.55, 54.6)
    SetChrPos(ChrTable['黎恩'], -24.93, 110.0, 55.41, 89.0)
    SetChrPos(ChrTable['莎拉'], -26.41, 110.0, 54.08, 54.2)
    SetChrPos(ChrTable['蓋烏斯'], -26.88, 110.0, 55.41, 111.1)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -24.85, 110.0, 53.99, 30.6)
    SetChrPos(ChrTable['安潔莉卡'], -25.23, 94.0, -80.71, 124.4)
    SetChrPos(ChrTable['悠娜'], -25.38, 94.0, -81.66, 99.3)
    SetChrPos(ChrTable['庫爾特'], -25.9, 94.0, -82.41, 78.4)
    SetChrPos(ChrTable['亞爾緹娜'], -26.04, 94.0, -81.05, 103.5)
    SetChrPos(ChrTable['亞修'], -26.83, 94.0, -82.36, 75.4)
    SetChrPos(ChrTable['妙婕'], -26.61, 94.0, -81.62, 92.9)

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CB2',
    )

    CameraSetPos(0x03, -26.23, 111.62, 54.65, 0)
    CameraRotate(0x03, 22.0, 229.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraRotate(0x03, 17.0, 236.0, 0.0, 20000, 0x01)

    Jump('loc_4CF9')

    def _loc_4CB2(): pass

    label('loc_4CB2')

    CameraSetPos(0x03, -24.84, 95.27, -81.72, 0)
    CameraRotate(0x03, 14.0, 300.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraRotate(0x03, 9.0, 307.0, 0.0, 20000, 0x01)

    def _loc_4CF9(): pass

    label('loc_4CF9')

    OP_AC(0x05, 0x0001)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E8, 5, 0x1745)),
            (Expr.TestScenaFlags, ScenaFlag(0x02E8, 6, 0x1746)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_502C',
    )

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DF1',
    )

    SetChrFace(0x04, ChrTable['黎恩'], '#E_2#M[0]#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            '#4K#1U（Ｂ組也抵達機關了。\n',
            '　再來只剩攻入瞭望台。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#E[3]#M[2]#B_0#1U（等著我們的恐怕是……\n',
            '　必須做好萬全的準備才行。）',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_4EBE')

    def _loc_4DF1(): pass

    label('loc_4DF1')

    SetChrFace(0x04, ChrTable['悠娜'], '#E_0#M[2]#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            '#3K#1U（Ａ組似乎也抵達了對面那邊。\n',
            '　現在可以解除機關了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#E[1]#M[2]#B_0#1U（那邊已經先抵達了，\n',
            '　不知道準備充不充分……？）',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    def _loc_4EBE(): pass

    label('loc_4EBE')

    Fade(0x00, 300, 0.3, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x2F49, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00AE, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '機關解除後，首先由Ａ組進攻。\n',
            '建議做好萬全的準備再開始。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    Fade(0x64, 300, 0.3, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Fade(0x00, 300, 0.3, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00AE, 0x00)

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, '解除機關', 0x00000001)
    OP_75(0x01, 0x00, '離去', 0x00000002)
    OP_75(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF6)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    Fade(0x64, 300, 0.3, 0x0000)
    Fade(0xFF, 0, 0x0000)

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5027',
    )

    Jump('loc_5027')

    def _loc_5027(): pass

    label('loc_5027')

    Jump('loc_50AA')

    def _loc_502C(): pass

    label('loc_502C')

    Fade(0x00, 300, 0.3, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00AE, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '什麼事也沒發生。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Talk(
        0xFFFF,
        (
            0xB,
            '另一條路線的機關\n',
            '必須同時啟動。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)
    def _loc_50AA(): pass

    label('loc_50AA')

    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x00)
    OP_AC(0x06)

    Return()

# id: 0x0019 offset: 0x50D0
@scena.Code('EV_03_80_01_END')
def EV_03_80_01_END():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E8, 5, 0x1745)),
            (Expr.TestScenaFlags, ScenaFlag(0x02E8, 6, 0x1746)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_514C',
    )

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_514C',
    )

    OP_23(0x05, 0xFFFF, 0x02EE, 0x044C, 0x00AE, 0x00)

    OP_18(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, '解除機關', 0x00000001)
    OP_75(0x01, 0x00, '離去', 0x00000002)
    OP_75(0x02, 0x00, 0x01, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF6)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    def _loc_514C(): pass

    label('loc_514C')

    If(
        (
            (Expr.Expr23, 0xF6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_518B',
    )

    Call(ScriptId.Sound, 'Init_ENVSE')
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    EventJump(0x00000000)
    OP_14(0x04000000)

    Jump('loc_5223')

    def _loc_518B(): pass

    label('loc_518B')

    Call(ScriptId.Sound, 'Init_ENVSE')

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51BF',
    )

    SetChrPos(0xF011, -24.86, 110.0, 55.03, 270.0)

    Jump('loc_51D2')

    def _loc_51BF(): pass

    label('loc_51BF')

    SetChrPos(0xF011, -25.47, 94.0, -81.83, 270.0)

    def _loc_51D2(): pass

    label('loc_51D2')

    If(
        (
            (Expr.Expr23, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51F7',
    )

    CameraRotate(0x03, 3.0, 229.0, 0.0, 0, 0x01)

    Jump('loc_5209')

    def _loc_51F7(): pass

    label('loc_51F7')

    CameraRotate(0x03, -1.0, 303.0, 0.0, 0, 0x01)

    def _loc_5209(): pass

    label('loc_5209')

    Call(ScriptId.System, 'FC_EventEnd', (0xFF, 0x0, 0x0))
    OP_14(0x04000000)

    def _loc_5223(): pass

    label('loc_5223')

    Return()

# id: 0x001A offset: 0x5224
@scena.Code('EV_03_80_02')
def EV_03_80_02():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3121, 0x0))
    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    ChrSetPhysicsFlags(0xF011, 0x00000001)
    CreateChr(ChrTable['黎恩'], 'C_CHR000', '黎恩', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 500.0)
    OP_7E(0x06, 0x0001)
    SetChrPos(ChrTable['尤西斯'], -26.1, 110.0, 55.16, 84.7)
    SetChrPos(ChrTable['米莉亞姆'], -25.65, 110.0, 54.55, 54.6)
    SetChrPos(ChrTable['黎恩'], -24.93, 110.0, 55.41, 89.0)
    SetChrPos(ChrTable['莎拉'], -26.41, 110.0, 54.08, 54.2)
    SetChrPos(ChrTable['蓋烏斯'], -26.88, 110.0, 55.41, 111.1)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -24.85, 110.0, 53.99, 30.6)
    SetChrPos(ChrTable['安潔莉卡'], -25.23, 94.0, -80.71, 124.4)
    SetChrPos(ChrTable['悠娜'], -25.38, 94.0, -81.66, 99.3)
    SetChrPos(ChrTable['庫爾特'], -25.9, 94.0, -82.41, 78.4)
    SetChrPos(ChrTable['亞爾緹娜'], -26.04, 94.0, -81.05, 103.5)
    SetChrPos(ChrTable['亞修'], -26.83, 94.0, -82.36, 75.4)
    SetChrPos(ChrTable['妙婕'], -26.61, 94.0, -81.62, 92.9)
    CameraSetPos(0x03, -25.23, 95.27, -81.67, 0)
    CameraRotate(0x03, 13.0, 299.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -24.88, 95.27, -81.84, 2000)
    CameraRotate(0x03, 13.0, 299.0, 0.0, 2000, 0x01)
    OP_AC(0x05, 0x0001)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_50((0xDD, 'switch01'), 'l_to_u')
    CreateThread(0xFFFF, 0x05, ScriptId.Sound, 'SE_GIM_M30_SW')
    Sleep(1000)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -25.98, 111.56, 54.81, 0)
    CameraRotate(0x03, 14.0, 242.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -25.69, 111.56, 55.02, 2000)
    CameraRotate(0x03, 14.0, 242.0, 0.0, 2000, 0x01)
    Fade(0xFF, 0, 0x0000)
    OP_50((0xDD, 'switch00'), 'l_to_u')
    CreateThread(0xFFFF, 0x05, ScriptId.Sound, 'SE_GIM_M30_SW')
    Sleep(1000)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -17.96, 114.95, 33.12, 0)
    CameraRotate(0x03, 21.0, 143.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 9.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -18.19, 116.86, 26.8, 4000)
    CameraRotate(0x03, 19.0, 127.0, 0.0, 4000, 0x01)
    CameraSetDistance(0x03, 11.2, 4000)
    Fade(0xFF, 0, 0x0000)
    OP_50((0xDD, 'bridge00'), 'open1')
    CreateThread(0xFFFF, 0x05, ScriptId.Sound, 'SE_GIM_M30_BRIDGE')
    Sleep(2000)
    CameraCtrl(0x09, 0.15, 0.15, 1.0)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -35.9, 114.38, -51.63, 0)
    CameraRotate(0x03, 43.0, 322.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -35.11, 114.38, -46.49, 5000)
    CameraRotate(0x03, 13.0, 241.0, 0.0, 5000, 0x01)
    CameraSetDistance(0x03, 11.7, 5000)
    Sleep(1800)
    OP_50((0xDD, 'bridge01'), 'open1')
    CreateThread(0xFFFF, 0x05, ScriptId.Sound, 'SE_GIM_M30_BRIDGE')
    Sleep(2000)
    CameraCtrl(0x09, 0.15, 0.15, 1.0)
    CameraCtrl(0x07, 0x00BF)
    Sleep(1000)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    SetChrPos(ChrTable['黎恩'], -26.91, 110.0, 49.71, 181.2)
    SetChrPos(ChrTable['尤西斯'], -27.7, 110.0, 50.55, 179.1)
    SetChrPos(ChrTable['米莉亞姆'], -27.86, 110.0, 49.98, 175.8)
    SetChrPos(ChrTable['莎拉'], -26.69, 110.0, 51.06, 178.8)
    SetChrPos(ChrTable['蓋烏斯'], -28.55, 110.0, 51.02, 169.3)
    SetChrPos(ChrTable['莎拉'], -26.69, 110.0, 51.06, 178.8)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -26.31, 110.0, 50.19, 190.6)
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    CameraSetPos(0x03, -26.71, 111.46, 49.17, 0)
    CameraRotate(0x03, 358.0, 162.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -26.63, 111.46, 48.91, 15000)
    CameraRotate(0x03, 357.0, 161.0, 357.0, 15000, 0x01)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_6#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            '終於要抵達了嗎……！！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['黎恩'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            '#1P有路可以通過了──大家上吧！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_27('舊Ⅶ班', 0xFFFF)
    CameraCtrl(0x09, 0.02, 0.02, 0.25)
    OP_23(0x01, 0x04B0, 0x0096, 0x00, 0x0A)
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '[3333333332]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '[3333333332]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '[3333333332]', '0[autoB0]', '#b', '0')
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            '#0T#2U#5S喔！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    OP_27('', 0xFFFF)
    CameraCtrl(0x00)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    OP_3D(ChrTable['黎恩'], 180.0, 0.0, 0x00)
    OP_3D(ChrTable['尤西斯'], 180.0, 0.0, 0x00)
    OP_3D(ChrTable['米莉亞姆'], 180.0, 0.0, 0x00)
    OP_3D(ChrTable['莎拉'], 180.0, 0.0, 0x00)
    OP_3D(ChrTable['蓋烏斯'], 180.0, 0.0, 0x00)
    OP_3D(ChrTable['莎拉'], 180.0, 0.0, 0x00)
    OP_3D(ChrTable['奧蕾莉亞分校長'], 180.0, 0.0, 0x00)
    MoveType(ChrTable['黎恩'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    MoveType(ChrTable['尤西斯'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    MoveType(ChrTable['米莉亞姆'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    MoveType(ChrTable['莎拉'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    MoveType(ChrTable['蓋烏斯'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    MoveType(ChrTable['莎拉'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    MoveType(ChrTable['奧蕾莉亞分校長'], 0xFE00, 0.0, 0.0, 10.0, 3.3, 0x02, 0x0000)
    CameraSetPos(0x03, -27.05, 111.4, 50.15, 0)
    CameraRotate(0x03, 355.0, 357.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 30.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -27.36, 112.04, 47.28, 6000)
    CameraRotate(0x03, 9.0, 344.0, 0.0, 6000, 0x01)
    Fade(0xFF, 0, 0x0000)
    Sleep(1500)
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrPos(ChrTable['安潔莉卡'], -26.41, 94.0, -82.08, 344.5)
    SetChrPos(ChrTable['悠娜'], -25.48, 94.0, -80.05, 341.1)
    SetChrPos(ChrTable['庫爾特'], -26.08, 94.0, -81.0, 344.5)
    SetChrPos(ChrTable['亞爾緹娜'], -26.18, 94.0, -79.77, 343.1)
    SetChrPos(ChrTable['妙婕'], -26.71, 94.0, -80.55, 347.0)
    SetChrPos(ChrTable['亞修'], -27.3, 94.0, -81.39, 351.0)
    OP_45(ChrTable['悠娜'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['庫爾特'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['亞爾緹娜'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['妙婕'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['亞修'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['安潔莉卡'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    SetChrFace(0x03, ChrTable['悠娜'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    CameraSetPos(0x03, -26.21, 95.3, -80.11, 0)
    CameraRotate(0x03, 19.0, 3.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -26.21, 95.3, -80.11, 30000)
    CameraRotate(0x03, 21.0, 343.0, 0.0, 30000, 0x01)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.0)
    OP_7E(0x06, 0x0001)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['庫爾特'], '#E_2#M_0#B_0')

    ChrTalk(
        ChrTable['庫爾特'],
        0x00000000,
        (
            '#2P好，機關好像啟動了！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['亞修'], '#E_2#M_A#B_0')

    ChrTalk(
        ChrTable['亞修'],
        0x00000000,
        (
            '#2P哈，我們也攻過去吧！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            '#2P嗯，去支援教官他們──',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_44(0x0012, 0x0E, 0.15, 0x0000, 0.0)
    OP_44(0x000A, 0x0E, 0.15, 0x0000, 0.0)
    OP_44(0x000B, 0x0E, 0.15, 0x0000, 0.0)
    OP_44(0x000C, 0x0E, 0.15, 0x0000, 0.0)
    OP_44(0x000E, 0x0E, 0.15, 0x0000, 0.0)
    OP_44(0x000D, 0x0E, 0.15, 0x0000, 0.0)
    SetChrFace(0x03, ChrTable['悠娜'], 'C', '8[autoM8]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], 'C', '8[autoM8]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], 'C', '8[autoM8]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], 'C', '8[autoM8]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(1500)
    OP_3A(0x01, 0x1770, 0x00)
    CameraCtrl(0x00)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraSetPos(0x03, -27.26, 96.09, -80.06, 0)
    CameraRotate(0x03, 359.0, 166.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -27.34, 96.36, -80.01, 3500)
    CameraRotate(0x03, 347.0, 143.0, 0.0, 3500, 0x01)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 60.0)
    OP_7E(0x06, 0x0001)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            '#K這是……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['妙婕'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['妙婕'],
        0x00000000,
        (
            '#2K#F……薄霧嗎？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_3A(0x02, 0x00)
    OP_AC(0x06)

    Return()

# id: 0x001B offset: 0x64DC
@scena.Code('EV_03_80_02_END')
def EV_03_80_02_END():
    ReleaseEffect(0xFFFF, 0xC8)
    OP_50((0xDD, 'bridge00'), 'open1_c')
    OP_50((0xDD, 'bridge01'), 'open1_c')
    OP_50((0xDD, 'switch00'), 'unlocked')
    OP_50((0xDD, 'switch01'), 'unlocked')
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    EventJump(0x00000000)
    OP_14(0x04000000)

    Return()

# id: 0x001C offset: 0x6550
@scena.Code('EV_03_81_00')
def EV_03_81_00():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3122, 0x0))
    OP_55(0x00, 0x01E0, 0x01BE, 0x0628, 0x0286, 0x0000, 0x0000, 0x0000, 0x0000, 0x0400, 0x00C0, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_TVIS0070', '')
    OP_55(0x01, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_SVIS0316', '')
    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evc35_00.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evc35_01.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evc35_02.eff')
    LoadEffect(0xFFFF, 0xCC, 'event/evc33_02.eff')
    LoadEffect(0xFFFF, 0xCD, 'event/evc21_00.eff')
    LoadEffect(0xFFFF, 0xCE, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCF, 'event/evc33_03.eff')
    LoadEffect(0xFFFF, 0xD0, 'battle/cr011_02_3.eff')
    LoadEffect(0xFFFF, 0xD1, 'battle/sc033_00_2.eff')
    LoadEffect(0xFFFF, 0xD2, 'battle/sc035_00_2.eff')
    LoadEffect(0xFFFF, 0xD3, 'battle/cr037_00_0.eff')
    LoadEffect(0xFFFF, 0xD4, 'battle/cr039_00_0.eff')
    LoadEffect(0xFFFF, 0xD5, 'battle/cr033_00_0.eff')
    LoadEffect(0xFFFF, 0xD6, 'battle/cr033_00_1.eff')
    LoadEffect(0xFFFF, 0xD7, 'battle/cr000_02_1.eff')
    LoadEffect(0xFFFF, 0xD8, 'battle/cr000_02_4.eff')
    LoadEffect(0xFFFF, 0xD9, 'battle/cr000_02_5.eff')
    LoadEffect(0xFFFF, 0xDA, 'battle/sc017_10_14.eff')
    LoadEffect(0xFFFF, 0xDB, 'battle/cr006_01_0.eff')
    LoadEffect(0xFFFF, 0xDC, 'battle/atk950_0.eff')
    LoadEffect(0xFFFF, 0xDD, 'event/evr22_01.eff')
    LoadEffect(0xFFFF, 0xDE, 'battle/sc021_00_05.eff')
    FormationCtrl(0x12)
    OP_C4(0x01, 0x00)
    OP_C4(0x01, 0x01)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    CreateChr(ChrTable['銀臂2'], 'C_CHR950', '銀臂', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    AnimeClipChangeSkin(ChrTable['鋼之雅里安洛德'], 'C_CHR033_C00')
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['銀臂2'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEv35000', 'AniEvCraft03', 'AniEvCraft03_1', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['尤西斯'], 0x00, 'AniEv35000', 'AniEvCraft01', 'AniEvCraft01_2', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['米莉亞姆'], 0x00, 'AniEv35000', 'AniEvTeMune', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['蓋烏斯'], 0x00, 'AniEv35000', 'AniEvSCraft20_1', 'AniEvSCraft20_2', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['莎拉'], 0x00, 'AniEv35000', 'AniEvUdegumiF', 'AniEvSCraft10_12', 'AniEvSCraft10_13', '', '', '', '', '', '', '', '', '', '', '', '')

    AnimeClipLoadMultiple(
        ChrTable['奧蕾莉亞分校長'],
        0x00,
        'AniEv35000',
        'AniEv30005',
        'AniEvBtlWait',
        'AniEvSCraft00',
        'AniEvSCraft00_1',
        'AniEvSCraft00_5',
        'AniEvSCraft00_6',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    )

    AnimeClipLoadMultiple(ChrTable['亞修'], 0x00, 'AniEvIdle', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv35000', 'AniEv86000', 'AniEv86000b', 'AniEvCraft00', 'AniEvCraft00_1', '', '', '', '', '', '', '', '', '', '', '')

    AnimeClipLoadMultiple(
        ChrTable['神速杜巴莉'],
        0x00,
        'AniEv35000',
        'AniEvSquat',
        'AniEvRyoteKosi',
        'AniEvKincho',
        'AniEvKinchoTeburi',
        'AniEvSCraft01_02',
        'AniEvSCraft01_04',
        'AniEvSCraft01_05',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    )

    AnimeClipLoadMultiple(ChrTable['魔弓恩奈雅'], 0x00, 'AniEv35000', 'AniEvSquat', 'AniEvCraft00', 'AniEvCraft00_1', 'AniEvCraft00_2', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['剛毅艾奈絲'], 0x00, 'AniEv35000', 'AniEvSquat', 'AniEvUdegumiF', 'AniEvCraft00_1', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvk1023', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['銀臂2'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['安潔莉卡'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['悠娜'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['庫爾特'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['亞爾緹娜'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    OP_50((0xDD, 'bridge00'), 'open1_c')
    OP_50((0xDD, 'bridge01'), 'open1_c')
    SetChrPos(ChrTable['黎恩'], -28.67, 114.0, 12.52, 214.8)
    SetChrPos(ChrTable['尤西斯'], -26.17, 114.0, 12.34, 221.0)
    SetChrPos(ChrTable['米莉亞姆'], -28.05, 114.0, 14.23, 220.3)
    SetChrPos(ChrTable['蓋烏斯'], -26.97, 114.0, 13.91, 221.0)
    SetChrPos(ChrTable['莎拉'], -29.28, 114.0, 13.86, 219.6)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -27.71, 114.0, 11.99, 215.5)
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['安潔莉卡'], -32.78, 114.0, -14.73, 314.0)
    SetChrPos(ChrTable['悠娜'], -33.07, 114.0, -13.37, 316.1)
    SetChrPos(ChrTable['庫爾特'], -33.56, 114.0, -15.3, 306.2)
    SetChrPos(ChrTable['亞爾緹娜'], -31.63, 114.0, -13.97, 319.4)
    SetChrPos(ChrTable['亞修'], -31.47, 114.0, -15.19, 312.9)
    SetChrPos(ChrTable['妙婕'], -32.07, 114.0, -16.02, 311.8)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -48.43, 114.0, -1.24, 300.9)
    OP_45(ChrTable['鋼之雅里安洛德'], -40.0, 35.0, 0.0, 0x0000, 0x0000)
    SetChrPos(ChrTable['神速杜巴莉'], -44.15, 114.0, -2.92, 47.2)
    SetChrPos(ChrTable['剛毅艾奈絲'], -44.02, 114.0, -4.17, 40.7)
    SetChrPos(ChrTable['魔弓恩奈雅'], -45.43, 114.0, -2.83, 55.8)
    SetChrPos(ChrTable['永世α'], -60.45, 114.0, -0.3, 90.0)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1023', -1.0, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraSetPos(0x03, -37.09, 117.02, 5.03, 0)
    CameraRotate(0x03, 357.0, 191.0, 359.0, 0, 0x01)
    CameraSetDistance(0x03, 4.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 80.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    OP_56(0x00, 0x03, 0x02, 1.0, 1.0, 1.0, 1.0, 1000.0)
    OP_56(0x00, 0x00, 0x02, 96.0, 0.0, 1000.0, 0.0, 0.0)
    OP_57(0x00, 0x03)
    OP_57(0x00, 0x00)
    Sleep(2000)
    OP_56(0x00, 0x03, 0x01, 1.0, 1.0, 1.0, 0.0, 1000.0)
    OP_56(0x00, 0x00, 0x01, 192.0, 0.0, 1000.0, 0.0, 0.0)
    OP_57(0x00, 0x03)
    OP_57(0x00, 0x00)
    Sleep(500)
    Call(ScriptId.Sound, 'Init_ENVSE')
    OP_8D(0x0000, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x0010, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x000F, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x0006, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x0009, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x0008, 1.0, 1.0, 1.5, 0.5)
    MoveType(ChrTable['黎恩'], 0xFFFF, -35.32, 114.0, 5.9, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['黎恩'], 0.55)
    Sleep(150)
    MoveType(ChrTable['奧蕾莉亞分校長'], 0xFFFF, -34.33, 114.0, 5.35, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['奧蕾莉亞分校長'], 0.5)
    Sleep(150)
    MoveType(ChrTable['莎拉'], 0xFFFF, -35.62, 114.0, 7.29, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['莎拉'], 0.55)
    Sleep(150)
    MoveType(ChrTable['尤西斯'], 0xFFFF, -33.32, 114.0, 4.94, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['尤西斯'], 0.4)
    Sleep(150)
    MoveType(ChrTable['米莉亞姆'], 0xFFFF, -34.73, 114.0, 7.11, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['米莉亞姆'], 0.4)
    Sleep(150)
    MoveType(ChrTable['蓋烏斯'], 0xFFFF, -33.46, 114.0, 6.97, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['蓋烏斯'], 0.5)
    CameraSetPos(0x03, -35.04, 115.27, 6.03, 5000)
    CameraRotate(0x03, 353.0, 259.0, 354.0, 5000, 0x01)
    CameraSetDistance(0x03, 3.5, 5000)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_41(0x0000, 0x00)
    OP_41(0x0010, 0x00)
    OP_41(0x000F, 0x00)
    OP_41(0x0006, 0x00)
    OP_41(0x0009, 0x00)
    OP_41(0x0008, 0x00)
    CameraCtrl(0x07, 0x00BF)
    Sleep(300)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -33.34, 115.47, 4.95, 0)
    CameraRotate(0x03, 4.0, 179.0, 353.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -33.37, 115.47, 5.01, 15000)
    CameraRotate(0x03, 358.0, 187.0, 353.0, 15000, 0x01)
    CameraSetDistance(0x03, 1.4, 15000)
    SetChrPos(ChrTable['尤西斯'], -33.04, 114.0, 5.23, -136.0)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_45(ChrTable['尤西斯'], -30.0, 0.0, 0.0, 0x07D0, 0x0000)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x902C),
            '這是……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['蓋烏斯'], 20.0, 0.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x902D),
            '出現了薄霧……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    PlayBGM(311, 1.0, 0x0000, 0x00000000, 0x00)
    Fade(0x65, 1000, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -48.65, 115.32, -0.55, 0)
    CameraRotate(0x03, 350.0, 75.0, 351.0, 0, 0x01)
    CameraSetDistance(0x03, 3.1, 0)
    CameraCtrl(0x0B, 0x03, 37.5, 0x0000)
    CameraSetPos(0x03, -48.65, 115.32, -0.55, 5000)
    CameraRotate(0x03, 346.0, 79.0, 351.0, 5000, 0x01)
    OP_45(ChrTable['尤西斯'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['尤西斯'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], 0xFFFF, 0x0000)
    OP_45(ChrTable['蓋烏斯'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['蓋烏斯'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -48.86, 115.41, -0.99, 0)
    CameraRotate(0x03, 16.0, 244.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 1.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -48.83, 115.26, -0.86, 20000)
    CameraRotate(0x03, 5.0, 258.0, 358.0, 20000, 0x01)
    CameraSetDistance(0x03, 1.7, 20000)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -48.43, 114.0, -1.24, 318.7)
    SetChrPos(ChrTable['黎恩'], -36.05, 114.0, 4.08, 246.9)
    SetChrPos(ChrTable['尤西斯'], -33.64, 114.0, 2.23, 240.9)
    SetChrPos(ChrTable['米莉亞姆'], -35.03, 114.0, 5.77, 243.9)
    SetChrPos(ChrTable['蓋烏斯'], -33.11, 114.0, 3.22, 254.3)
    SetChrPos(ChrTable['莎拉'], -35.85, 114.0, 6.06, 242.4)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -35.37, 114.0, 3.58, 251.5)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_45(ChrTable['鋼之雅里安洛德'], -80.0, 50.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['鋼之雅里安洛德'], -30.0, 25.0, 0.0, 0x0320, 0x0000)
    Sleep(800)
    OP_45(ChrTable['鋼之雅里安洛德'], 40.0, 0.0, 0.0, 0x07D0, 0x0000)
    Sleep(1000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    SetChrFace(0x04, ChrTable['米莉亞姆'], '#E[11111110]#M_2#B_0')

    ChrTalk(
        ChrTable['米莉亞姆'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x902E),
            '（吞口水）……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['莎拉'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x902F),
            '結社的使徒，第七柱……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.88, 115.48, 3.8, 0)
    CameraRotate(0x03, 4.0, 218.0, 356.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.52, 115.5, 4.0, 15000)
    CameraRotate(0x03, 0.0, 225.0, 357.0, 15000, 0x01)
    OP_45(ChrTable['黎恩'], 0.0, -15.0, 0.0, 0x0000, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '33332', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[2]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9030),
            '《鋼之聖女》雅里安洛德……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_45(ChrTable['黎恩'], 0.0, -10.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '223', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(100)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Call(ScriptId.Sound, 'Stop_ENVSE_VAR', (0xFF, 0x1F4, 0x0))
    OP_3A(0x03, 0.4, 0x01F4, 0x00)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 1000.0)
    OP_57(0x01, 0x03)
    Sleep(2000)
    Call(ScriptId.Sound, 'Init_ENVSE_VAR', (0xFF, 0x3E8, 0x0))
    OP_3A(0x03, 0.7, 0x03E8, 0x00)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 1000.0)
    OP_57(0x01, 0x03)
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '33332', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(100)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[2]#M[2]#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9031),
            '（果然很像……\n',
            '　２年前在羅恩格林城的那個背影。）',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -47.95, 114.73, -1.75, 0)
    CameraRotate(0x03, -2.0, 116.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 3.0)
    OP_7E(0x06, 0x0002)
    CameraSetPos(0x03, -47.62, 115.17, -0.92, 14000)
    CameraRotate(0x03, 347.0, 95.0, 4.0, 14000, 0x01)
    CameraSetDistance(0x03, 1.2, 14000)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_98(0x03E9, 1.0, 0x01)
    OP_98(0x03E8, 0.0, 0x01)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_0#M_A#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9032),
            '呵呵……我還以為會是\n',
            '地精的協力者前來挑戰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            (TxtCtl.Voice, 0x9033),
            '#E_0#M_0#B_0結果是令人出乎意料的代打呢。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Sleep(500)
    OP_3D(ChrTable['鋼之雅里安洛德'], 78.1, 2.5, 0x00)
    OP_3F(ChrTable['鋼之雅里安洛德'])
    Sleep(1000)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -35.79, 115.02, 3.09, 0)
    CameraRotate(0x03, 0.0, 76.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -35.85, 115.3, 3.03, 15000)
    CameraRotate(0x03, 4.0, 80.0, 1.0, 15000, 0x01)
    CameraSetDistance(0x03, 2.5, 15000)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.8, 114.0, -0.56, 64.2)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['奧蕾莉亞分校長'], 0x0000)
    ChrSetPhysicsFlags(ChrTable['蓋烏斯'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['尤西斯'], 0x00000040)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -10.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1111111110]#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9034),
            '呵……雖然我也覺得孩子氣，\n',
            '但好歹這裡也曾是我的居城。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_2#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9035),
            '趁這個機會就請他們讓我出馬了。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.84, 115.39, 2.73, 0)
    CameraRotate(0x03, 9.0, 225.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.84, 115.36, 2.73, 15000)
    CameraRotate(0x03, 356.0, 234.0, 2.0, 15000, 0x01)
    ChrClearPhysicsFlags(ChrTable['蓋烏斯'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['尤西斯'], 0x00000040)
    SetChrPos(ChrTable['尤西斯'], -33.88, 114.0, 2.64, 252.0)
    SetChrPos(ChrTable['蓋烏斯'], -33.25, 114.0, 3.71, 254.3)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -10.0, 0.0, 0x0000, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '1', '0[autoM0]', '0[autoB0]', '#b', '0')
    OP_8D(0x0010, 0.0, 0.0, 1.2, 0.4)
    MoveType(ChrTable['奧蕾莉亞分校長'], 0xFFFF, -36.73, 114.0, 2.84, 1.2, 0x01, 0x0000)
    OP_6C(ChrTable['奧蕾莉亞分校長'], 0.3)
    Fade(0xFF, 0, 0x0000)
    OP_41(0x0010, 0x00)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[11111111111111111111111110]#M_0#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9036),
            '奧蕾莉亞・勒瑰恩──\n',
            '請多指教。',
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[336]#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9037),
            '《結社》第七使徒，《鋼之聖女》閣下。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -45.56, 115.2, -0.49, 0)
    CameraRotate(0x03, 0.0, 27.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -45.56, 115.42, -0.49, 20000)
    CameraRotate(0x03, 5.0, 91.0, 356.0, 20000, 0x01)
    CameraSetDistance(0x03, 1.2, 20000)
    OP_98(0x03E9, 1.0, 0x01)
    OP_98(0x03E8, 0.0, 0x01)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1]#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9038),
            '《黃金羅剎》奧蕾莉亞將軍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            (TxtCtl.Voice, 0x9039),
            '#E_0#M_0#B_0妳窮究了范德爾流與亞爾賽德流的事蹟\n',
            '我早有耳聞。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -10.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1]#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x903A),
            '原來如此──本人更是在傳聞之上啊。',
            TxtCtl.Enter,
        ),
    )

    Sleep(800)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -38.11, 115.3, 2.53, 0)
    CameraRotate(0x03, 358.0, 266.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -38.51, 115.46, 2.24, 20000)
    CameraRotate(0x03, 4.0, 256.0, 351.0, 20000, 0x01)
    CameraSetDistance(0x03, 1.8, 20000)
    SetChrPos(ChrTable['黎恩'], -35.75, 114.0, 4.15, 241.6)
    SetChrPos(ChrTable['尤西斯'], -33.49, 114.0, 2.3, 267.1)
    SetChrPos(ChrTable['米莉亞姆'], -34.92, 114.0, 5.62, 234.5)
    SetChrPos(ChrTable['蓋烏斯'], -33.13, 114.0, 3.29, 242.6)
    SetChrPos(ChrTable['莎拉'], -35.82, 114.0, 5.69, 222.7)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -37.38, 114.0, 2.7, 255.7)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], 0xFFFF, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '1', 'A[autoMA]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x903B),
            '不敢當。能讓『傳說』聽過我的名字，\n',
            '實在讓人欣喜。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEv35000', -1.0, 0.8, 0x00000000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[333333332]#M_2#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x903C),
            '但妳不摘下頭盔嗎？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            (TxtCtl.Voice, 0x903D),
            '#E[3333333333333333F]#M_2#B_0已經沒有必要隱藏了──\n',
            '拿下妳的面具吧？',
            TxtCtl.Enter,
        ),
    )

    Sleep(2500)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEv30005', -1.0, 0.8, 0x00000000)
    OP_5E(0x00, 0x0000, 0.4, 0x0320, 0x03E8, 0x03E8, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x03E8)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_44(0x0000, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0006, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0009, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000F, 0x15, 0.15, 0x0000, 0.0)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['奧蕾莉亞分校長'], 0x03E8)
    SetChrFace(0x03, ChrTable['黎恩'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Sleep(20)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['奧蕾莉亞分校長'], 0x03E8)
    SetChrFace(0x03, ChrTable['尤西斯'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Sleep(20)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['奧蕾莉亞分校長'], 0x03E8)
    SetChrFace(0x03, ChrTable['米莉亞姆'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Sleep(20)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['奧蕾莉亞分校長'], 0x03E8)
    SetChrFace(0x03, ChrTable['蓋烏斯'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Sleep(20)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['奧蕾莉亞分校長'], 0x03E8)
    SetChrFace(0x03, ChrTable['莎拉'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Sleep(1000)
    OP_27('女孩的聲音', 0xFFFF)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x903E),
            '#3C#5S妳、太無禮了……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -43.24, 114.84, 0.97, 0)
    CameraRotate(0x03, 8.0, 36.0, 359.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 10.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -43.85, 115.23, -0.4, 10000)
    CameraRotate(0x03, 355.0, 71.0, 5.0, 10000, 0x01)
    CameraSetDistance(0x03, 1.3, 10000)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -47.41, 114.0, -1.39, 64.2)
    SetChrPos(ChrTable['神速杜巴莉'], -44.42, 114.0, -0.8, 63.7)
    SetChrPos(ChrTable['剛毅艾奈絲'], -45.24, 114.0, -2.02, 51.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -46.39, 114.0, 0.16, 79.4)
    ChrSetRGBA(ChrTable['神速杜巴莉'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(ChrTable['魔弓恩奈雅'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    ChrSetRGBA(ChrTable['剛毅艾奈絲'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '6', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3B(0x00, (0xFF, 0x770F, 0x0), 0.5, (0xFF, 0x1F4, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['神速杜巴莉'], (0xFF, 0xC9, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    Sleep(500)
    PlayEffect(ChrTable['魔弓恩奈雅'], (0xFF, 0xC9, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x65)
    Sleep(300)
    PlayEffect(ChrTable['剛毅艾奈絲'], (0xFF, 0xC9, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x66)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x75BB, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCA, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(500)
    PlayEffect(0xFFFF, (0xFF, 0xCA, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(300)
    PlayEffect(0xFFFF, (0xFF, 0xCA, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(1900)
    OP_3B(0x00, (0xFF, 0x75BE, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetRGBA(ChrTable['神速杜巴莉'], 1.0, 1.0, 1.0, 1.0, 800, 0x03)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x75BE, 0x0), 0.8, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetRGBA(ChrTable['魔弓恩奈雅'], 1.0, 1.0, 1.0, 1.0, 800, 0x03)
    Sleep(300)
    OP_3B(0x01, (0xFF, 0x770F, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x00, (0xFF, 0x75BE, 0x0), 0.8, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetRGBA(ChrTable['剛毅艾奈絲'], 1.0, 1.0, 1.0, 1.0, 800, 0x03)
    Sleep(300)
    EffectCtrl(0x0E, 0x006D, 0x64, 0x00)
    EffectCtrl(0x0E, 0x006F, 0x65, 0x00)
    EffectCtrl(0x0E, 0x006E, 0x66, 0x00)
    OP_5E(0x01, 0x03E8)
    Sleep(5100)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.83, 115.36, 5.79, 0)
    CameraRotate(0x03, 2.0, 50.0, 354.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -35.75, 115.22, 5.82, 15000)
    CameraRotate(0x03, 357.0, 54.0, 358.0, 15000, 0x01)
    CameraSetDistance(0x03, 2.5, 15000)
    SetChrPos(ChrTable['莎拉'], -35.96, 114.0, 6.45, 236.0)
    SetChrPos(ChrTable['米莉亞姆'], -34.99, 114.0, 5.81, 249.4)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['神速杜巴莉'], 0x0000)
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000002)
    Sleep(500)
    SetChrFace(0x04, ChrTable['米莉亞姆'], '#E_8#M_0#B_0')

    ChrTalk(
        ChrTable['米莉亞姆'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x903F),
            '（鐵機隊……\n',
            '　已經回來了啊。）',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000000)
    SetChrFace(0x04, ChrTable['莎拉'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9040),
            '（真棘手……\n',
            '　不過，現在也夠棘手了。）',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -37.6, 115.47, 2.64, 0)
    CameraRotate(0x03, 15.0, 223.0, 357.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -37.6, 115.42, 2.64, 20000)
    CameraRotate(0x03, 355.0, 234.0, 359.0, 20000, 0x01)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], 'H', 'A[autoMA]', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x75BC, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -15.0, 0.0, 0x05DC, 0x0000)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[2222223]#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9041),
            '呵呵，氣勢真驚人啊。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], 'F', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(300)
    CameraCtrl(0x09, 0.05, 0.05, 0.2)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[F]#M_2#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9042),
            '#4S──但別來打斷我。\n',
            '我正在跟她說話。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -44.92, 115.15, -0.59, 0)
    CameraRotate(0x03, 359.0, 256.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 3.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -45.0, 115.1, -0.6, 20000)
    CameraRotate(0x03, 355.0, 263.0, 7.0, 20000, 0x01)
    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvKincho', -1.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E_2#M[2]#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9043),
            '……唔………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9044),
            '……原來如此。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['魔弓恩奈雅'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9045),
            '羅剎的外號……\n',
            '並非浪得虛名呢。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -44.01, 115.35, -0.62, 0)
    CameraRotate(0x03, 5.0, 38.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 0.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 10.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -44.22, 115.35, -0.49, 20000)
    CameraRotate(0x03, 1.0, 57.0, 9.0, 20000, 0x01)
    ChrClearPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '7', 'F[autoMF]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['神速杜巴莉'], 0.0, -10.0, 0.0, 0x0320, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[33333332]#M_6#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9046),
            '哼，主人的容貌\n',
            '是只有強者才能瞻仰的榮耀！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    WaitForMsg()
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvKinchoTeburi', -1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '6', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(200)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[7]#M_6#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9047),
            '只要妳無法證明妳有多強，\n',
            '就不可能──',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9048),
            '算了，無妨。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_44(0x006D, 0x15, 0.15, 0x0000, 0.0)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '11C', 'H', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['神速杜巴莉'], -60.0, 0.0, 0.0, 0x0258, 0x0000)
    Sleep(1000)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -46.59, 115.13, -0.78, 0)
    CameraRotate(0x03, 1.0, 254.0, 9.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 30.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -46.59, 115.38, -0.78, 15000)
    CameraRotate(0x03, 1.0, 256.0, 7.0, 15000, 0x01)
    CameraSetDistance(0x03, 2.6, 15000)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    SetChrPos(ChrTable['魔弓恩奈雅'], -46.5, 114.0, 0.73, 79.4)
    SetChrPos(ChrTable['剛毅艾奈絲'], -45.08, 114.0, -2.23, 51.8)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], 0xFFFF, 0x0000)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x0000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv86000', -1.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x7562, 0x0), 0.3, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitForThreadExit(ChrTable['鋼之雅里安洛德'], 0x00)
    AnimeClipChangeSkin(ChrTable['鋼之雅里安洛德'], 'C_CHR033')
    AnimeClipLoadMultiple(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv35000', 'AniEv86000b', 'AniEvCraft00', 'AniEvCraft00_1', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniAttachEQU442', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv86000b', -1.0, 1.0, 0x00000000)
    OP_3B(0x00, (0xFF, 0x7571, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M_0#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9049),
            '………啊…………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000002)
    SetChrFace(0x04, ChrTable['莎拉'], '#E[C]#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x904A),
            '這……是………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -46.71, 115.25, -1.21, 0)
    CameraRotate(0x03, 9.0, 91.0, 10.0, 0, 0x01)
    CameraSetDistance(0x03, 0.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 3.0)
    OP_7E(0x06, 0x0002)
    CameraSetPos(0x03, -46.97, 115.48, -1.18, 5500)
    CameraRotate(0x03, 8.0, 81.0, 6.0, 5500, 0x01)
    CameraSetDistance(0x03, 0.7, 5500)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -47.41, 114.0, -1.39, 69.0)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '1', 'A', '0[autoB0]', '#b', '0')
    OP_6C(ChrTable['鋼之雅里安洛德'], 1.0)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -5.0, 0.0, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(3000)
    OP_45(ChrTable['鋼之雅里安洛德'], 15.0, 0.0, 0.0, 0x03E8, 0x0000)
    Sleep(300)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '0', 'A', '0[autoB0]', '#b', '0')
    CameraCtrl(0x07, 0x00BF)
    CameraSetPos(0x03, -47.09, 115.44, -1.05, 20000)
    CameraRotate(0x03, 2.0, 33.0, 0.0, 20000, 0x01)
    CameraSetDistance(0x03, 0.7, 20000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['米莉亞姆'], '#E[C]#M_0#B_0')

    ChrTalk(
        ChrTable['米莉亞姆'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x904B),
            '……好美………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['尤西斯'], '#E[11111110]#M_0#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x904C),
            '《槍之聖女》……\n',
            '莉安娜・桑德羅特……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x904D),
            '……看來與流傳下來的故事\n',
            '分毫不差啊。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -37.92, 115.43, 2.47, 0)
    CameraRotate(0x03, 1.0, 272.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 0.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -37.71, 115.47, 2.52, 10000)
    CameraRotate(0x03, 6.0, 269.0, 3.0, 10000, 0x01)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], 0xFFFF, 0x0000)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -10.0, 0.0, 0x0000, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '1', 'A[autoMA]', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniDetachEQU442', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x904E),
            '呵呵，比保存下來的\n',
            '大量繪畫還更英姿煥發……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '111I', 'A[autoMA]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[I]#M_4#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x904F),
            '看來可以更加期待\n',
            '騎兵槍的厲害了呢？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -38.14, 115.44, 2.65, 0)
    CameraRotate(0x03, 5.0, 55.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 2.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -38.14, 115.52, 2.65, 10000)
    CameraRotate(0x03, 6.0, 61.0, 1.0, 10000, 0x01)
    CameraSetDistance(0x03, 2.3, 10000)
    SetChrPos(ChrTable['黎恩'], -35.99, 114.0, 4.59, 241.6)
    SetChrPos(ChrTable['尤西斯'], -33.99, 114.0, 2.13, 267.1)
    SetChrPos(ChrTable['米莉亞姆'], -34.99, 114.0, 5.81, 249.4)
    SetChrPos(ChrTable['蓋烏斯'], -33.8, 114.0, 3.41, 242.6)
    SetChrPos(ChrTable['莎拉'], -35.96, 114.0, 6.45, 236.0)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -37.38, 114.0, 2.7, 246.5)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -47.84, 114.0, -1.78, 67.3)
    SetChrPos(ChrTable['神速杜巴莉'], -44.68, 114.0, -1.45, 63.7)
    SetChrPos(ChrTable['剛毅艾奈絲'], -45.36, 114.0, -2.99, 51.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -46.5, 114.0, 0.48, 79.4)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['奧蕾莉亞分校長'], 0x0000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['奧蕾莉亞分校長'], 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['奧蕾莉亞分校長'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['奧蕾莉亞分校長'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['奧蕾莉亞分校長'], 0x0000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[11111I]#M_4#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9050),
            '是啊……\n',
            '就如同妳的那艷紅的寶劍。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3A(0x01, 0x2710, 0x00)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -47.34, 115.49, -1.55, 0)
    CameraRotate(0x03, 5.0, 38.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -47.21, 114.88, -1.29, 4000)
    CameraRotate(0x03, 347.0, 93.0, 8.0, 4000, 0x01)
    CameraSetDistance(0x03, 2.7, 4000)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -47.83, 114.0, -2.09, 64.5)
    SetChrPos(ChrTable['神速杜巴莉'], -44.68, 114.0, -1.44, 63.7)
    SetChrPos(ChrTable['剛毅艾奈絲'], -44.99, 114.0, -3.15, 51.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -46.16, 114.0, 0.61, 68.9)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '1', '0[autoM0]', '0[autoB0]', '#b', '0')
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_6C(ChrTable['鋼之雅里安洛德'], 0.8)
    Fade(0xFF, 0, 0x0000)
    Sleep(600)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    CreateThread(0xFFFF, 0x02, ScriptId.Sound, 'SE_03_60_01_ARIANLOAD_YARI')
    Sleep(800)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['鋼之雅里安洛德'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '0', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(100)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniAttachMainWeapon', -1.0, 1.0, 0x00000000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -47.41, 115.04, -1.49, 0)
    CameraRotate(0x03, 3.0, 256.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 3.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -47.41, 115.02, -1.49, 12000)
    CameraRotate(0x03, 357.0, 261.0, 7.0, 12000, 0x01)
    CameraSetDistance(0x03, 3.3, 12000)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9051),
            '杜巴莉、艾奈絲、恩奈雅。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9052),
            '──我允許妳們使出全力。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_44(0x006D, 0x01, 0.15, 0x0000, 0.0)
    Sleep(50)
    OP_44(0x006E, 0x01, 0.15, 0x0000, 0.0)
    Sleep(50)
    OP_44(0x006F, 0x01, 0.15, 0x0000, 0.0)
    Sleep(1000)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Sleep(500)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -43.14, 115.44, -0.26, 0)
    CameraRotate(0x03, 1.0, 31.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 0.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -42.66, 114.65, 1.24, 3000)
    CameraRotate(0x03, 350.0, 37.0, 355.0, 3000, 0x01)
    CameraSetDistance(0x03, 1.4, 3000)
    SetChrPos(ChrTable['神速杜巴莉'], -44.12, 114.0, -1.1, 63.7)
    SetChrPos(ChrTable['剛毅艾奈絲'], -44.84, 114.0, -4.04, 51.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -45.47, 114.0, 0.32, 83.0)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '7', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '7', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '7', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3B(0x00, (0xFF, 0x7715, 0x0), 0.6, (0xFF, 0x1F4, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '6', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '6', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '6', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    OP_27('女騎士們', 0xFFFF)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[6]#M_2#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9054),
            '#6S是，主人！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3A(0x02, 0x00)
    PlayBGM(465, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3B(0x01, (0xFF, 0x7715, 0x0), (0xFF, 0x3E8, 0x0))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -43.53, 115.35, -0.7, 0)
    CameraRotate(0x03, 1.0, 57.0, 14.0, 0, 0x01)
    CameraSetDistance(0x03, 3.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -33.29, 115.28, 5.89, 3500)
    CameraRotate(0x03, 359.0, 58.0, 354.0, 3500, 0x01)
    CameraSetDistance(0x03, 3.9, 3500)
    OP_5E(0x00, 0x0004, 0.6, 0x0000, 0x07D0, 0x03E8, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    SetChrPos(ChrTable['黎恩'], -36.29, 114.0, 4.9, 226.0)
    SetChrPos(ChrTable['尤西斯'], -34.2, 114.0, 1.72, 246.8)
    SetChrPos(ChrTable['米莉亞姆'], -34.9, 114.0, 6.42, 230.2)
    SetChrPos(ChrTable['蓋烏斯'], -33.85, 114.0, 3.51, 242.6)
    SetChrPos(ChrTable['莎拉'], -36.93, 114.0, 6.5, 224.4)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -36.27, 114.0, 3.15, 242.9)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -46.4, 114.0, -2.31, 61.1)
    SetChrPos(ChrTable['神速杜巴莉'], -44.57, 114.0, -3.02, 51.6)
    SetChrPos(ChrTable['剛毅艾奈絲'], -45.5, 114.0, -5.16, 51.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -47.17, 114.0, -0.38, 69.9)
    PlayEffect(0xFFFF, (0xFF, 0xCF, 0x0), ChrTable['鋼之雅里安洛德'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    PlayEffect(0xFFFF, (0xFF, 0xCD, 0x0), ChrTable['奧蕾莉亞分校長'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FAD, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F78, 0x0), 0.6, (0xFF, 0x64, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7714, 0x0), 0.6, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEv30005', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    Sleep(100)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    Sleep(100)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    Sleep(100)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    Sleep(100)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEv35000', -1.0, 1.0, 0x00000000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(300)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -55.86, 118.77, 0.87, 0)
    CameraRotate(0x03, 350.0, 45.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 3.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -57.01, 119.48, 0.22, 3000)
    CameraRotate(0x03, 350.0, 54.0, 7.0, 3000, 0x01)
    CameraSetDistance(0x03, 3.3, 3000)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Fade(0xFF, 0, 0x0000)
    Sleep(1000)
    PlayEffect(0xFFFF, (0xFF, 0xDD, 0x0), ChrTable['永世α'], 0x0000000C, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x763C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(300)
    OP_3B(0x03, (0xFF, 0x7714, 0x0), 0.2, 0x01F4)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -29.37, 115.45, -17.42, 0)
    CameraRotate(0x03, 5.0, 270.0, 8.0, 0, 0x01)
    CameraSetDistance(0x03, 2.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -30.86, 115.25, -12.05, 3000)
    CameraRotate(0x03, 354.0, 356.0, 6.0, 3000, 0x01)
    ChrClearPhysicsFlags(ChrTable['安潔莉卡'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['悠娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['庫爾特'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞爾緹娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    SetChrPos(ChrTable['安潔莉卡'], -29.03, 114.0, -19.66, 333.7)
    SetChrPos(ChrTable['悠娜'], -27.71, 114.0, -17.85, 329.3)
    SetChrPos(ChrTable['庫爾特'], -28.48, 114.0, -18.7, 326.7)
    SetChrPos(ChrTable['亞爾緹娜'], -26.08, 114.0, -18.14, 331.5)
    SetChrPos(ChrTable['亞修'], -27.43, 114.0, -20.24, 330.4)
    SetChrPos(ChrTable['妙婕'], -26.37, 114.0, -19.14, 329.2)
    OP_8D(0x000A, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x000B, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x000C, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x0012, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x000D, 1.0, 1.0, 1.5, 0.5)
    OP_8D(0x000E, 1.0, 1.0, 1.5, 0.5)
    MoveType(ChrTable['悠娜'], 0xFFFF, -30.97, 114.0, -12.36, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['悠娜'], 0.45)
    Sleep(80)
    MoveType(ChrTable['庫爾特'], 0xFFFF, -31.32, 114.0, -13.45, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['庫爾特'], 0.5)
    Sleep(80)
    MoveType(ChrTable['亞爾緹娜'], 0xFFFF, -29.88, 114.0, -12.03, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['亞爾緹娜'], 0.45)
    Sleep(80)
    MoveType(ChrTable['安潔莉卡'], 0xFFFF, -31.74, 114.0, -14.92, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['安潔莉卡'], 0.5)
    Sleep(80)
    MoveType(ChrTable['妙婕'], 0xFFFF, -29.94, 114.0, -13.12, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['妙婕'], 0.48)
    Sleep(80)
    MoveType(ChrTable['亞修'], 0xFFFF, -30.27, 114.0, -15.08, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['亞修'], 0.49)
    Fade(0xFF, 0, 0x0000)
    OP_3A(0x03, 0.8, 0x01F4, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[999999999C]#M_2#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9057),
            '呼～呼～……\n',
            '讓大家久等了──欸！',
            TxtCtl.Enter,
        ),
    )

    CameraCtrl(0x07, 0x00BF)
    CameraSetPos(0x03, -30.78, 115.25, -12.19, 6000)
    CameraRotate(0x03, 351.0, 351.0, 6.0, 6000, 0x01)
    CameraSetDistance(0x03, 2.0, 6000)
    OP_44(0x000A, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000B, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000C, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000D, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000E, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0012, 0x15, 0.15, 0x0000, 0.0)
    SetChrFace(0x03, ChrTable['庫爾特'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['安潔莉卡'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    WaitForMsg()
    OP_41(0x000A, 0x00)
    OP_41(0x000B, 0x00)
    OP_41(0x000C, 0x00)
    OP_41(0x000D, 0x00)
    OP_41(0x000E, 0x00)
    OP_41(0x0012, 0x00)
    OP_3B(0x03, (0xFF, 0x7714, 0x0), 0.4, 0x01F4)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -34.14, 117.26, -7.23, 0)
    CameraRotate(0x03, 15.0, 144.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 9.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -31.93, 115.3, -10.28, 6000)
    CameraRotate(0x03, 4.0, 144.0, 0.0, 6000, 0x01)
    CameraSetDistance(0x03, 9.8, 6000)
    SetChrPos(ChrTable['安潔莉卡'], -30.44, 114.0, -15.75, -29.8)
    SetChrPos(ChrTable['悠娜'], -28.77, 114.0, -13.64, -30.7)
    SetChrPos(ChrTable['庫爾特'], -29.66, 114.0, -14.6, -28.4)
    SetChrPos(ChrTable['亞爾緹娜'], -27.76, 114.0, -12.82, -31.9)
    SetChrPos(ChrTable['亞修'], -29.4, 114.0, -15.83, -28.8)
    SetChrPos(ChrTable['妙婕'], -27.82, 114.0, -13.98, 325.2)
    ChrClearPhysicsFlags(ChrTable['銀臂2'], 0x00000040)
    SetChrPos(ChrTable['銀臂2'], -34.82, 114.0, 8.33, 226.3)
    ChrSetRGBA(ChrTable['銀臂2'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvBtlWait', 0.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvSCraft00', 1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvCraft00', 1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvSCraft01_02', 1.0, 1.0, 0x00000000)
    Sleep(500)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvCraft00_1', 1.0, 1.0, 0x00000000)
    Sleep(500)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvCraft01', 1.0, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xDC, 0x0), ChrTable['銀臂2'], 0x0000000C, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    ChrSetRGBA(ChrTable['銀臂2'], 1.0, 1.0, 1.0, 1.0, 500, 0x03)
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9058),
            '教官、各位……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['妙婕'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['妙婕'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9059),
            '聖女對上羅剎嗎……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -30.44, 115.49, -15.12, 0)
    CameraRotate(0x03, 10.0, 310.0, 352.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -30.36, 115.4, -15.28, 15000)
    CameraRotate(0x03, 358.0, 297.0, 352.0, 15000, 0x01)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvSCraft01_04', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvSCraft00_5', -1.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvIdle', -1.0, 1.0, 0x00000000)
    SetChrFace(0x04, ChrTable['亞修'], '#E[EEEEEEEEEEEEEEEEEEEEG]#M_4#B_0')

    ChrTalk(
        ChrTable['亞修'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x905A),
            '哈哈、真的假的……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['安潔莉卡'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['安潔莉卡'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x905B),
            '這下……可是見證了一場\n',
            '非常不得了的對決啊。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3B(0x03, (0xFF, 0x7714, 0x0), 0.6, 0x01F4)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -29.09, 121.46, 9.91, 0)
    CameraRotate(0x03, 35.0, 31.0, 354.0, 0, 0x01)
    CameraSetDistance(0x03, 14.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.51, 114.79, 2.14, 4500)
    CameraRotate(0x03, 351.0, 83.0, 350.0, 4500, 0x01)
    CameraSetDistance(0x03, 3.0, 4500)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    SetChrPos(ChrTable['黎恩'], -35.16, 114.0, 5.84, 233.0)
    SetChrPos(ChrTable['尤西斯'], -31.6, 114.0, 0.16, 246.8)
    SetChrPos(ChrTable['米莉亞姆'], -33.44, 114.0, 7.59, 230.2)
    SetChrPos(ChrTable['銀臂2'], -33.25, 114.0, 9.83, 226.3)
    SetChrPos(ChrTable['蓋烏斯'], -31.13, 114.0, 2.43, 247.3)
    SetChrPos(ChrTable['莎拉'], -35.82, 114.0, 8.09, 224.4)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -35.07, 114.0, 3.17, 244.3)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -47.66, 114.0, -3.01, 61.1)
    SetChrPos(ChrTable['神速杜巴莉'], -45.33, 114.0, -4.36, 51.6)
    SetChrPos(ChrTable['剛毅艾奈絲'], -45.4, 114.0, -6.96, 51.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -48.17, 114.0, 0.24, 69.9)
    Fade(0xFF, 0, 0x0000)
    Sleep(300)
    OP_23(0x01, 0xFFFF, 0x0357, 0x05, 0x64)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    OP_27('奧蕾莉亞／雅里安洛德', 0xFFFF)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x905C),
            '#5S喔～～～～～～～……！／喝啊～～～～～～～……！',
            0x8,
            TxtCtl.Enter,
        ),
    )

    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvCraft00', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['鋼之雅里安洛德'], (0xFF, 0xD5, 0x0), ChrTable['鋼之雅里安洛德'], 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(500)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvSCraft10_12', 1.0, 1.0, 0x00000000)
    Sleep(500)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvCraft00_1', 1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvSCraft00_6', 1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvCraft03', 1.0, 1.0, 0x00000000)
    Sleep(300)
    OP_4E(0.6, 0.0, 0x03)
    OP_3B(0x00, (0xFF, 0x8FAD, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F78, 0x0), 0.6, (0xFF, 0x64, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75BA, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(50)
    MoveType(ChrTable['奧蕾莉亞分校長'], 0xFFFF, -38.87, 114.0, 1.03, 5.5, 0x00, 0x0000)
    PlayEffect(ChrTable['奧蕾莉亞分校長'], (0xFF, 0xDE, 0x0), ChrTable['奧蕾莉亞分校長'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    MoveType(ChrTable['鋼之雅里安洛德'], 0xFFFF, -42.08, 114.0, -0.5, 5.0, 0x00, 0x0000)
    Sleep(100)
    PlayEffect(ChrTable['鋼之雅里安洛德'], (0xFF, 0xD6, 0x0), ChrTable['鋼之雅里安洛德'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -1.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.25, 0.25, 0.0, 0x0032, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    Sleep(100)
    PlayEffect(ChrTable['奧蕾莉亞分校長'], (0xFF, 0xD0, 0x0), ChrTable['奧蕾莉亞分校長'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), 0xFF)
    PlayEffect(ChrTable['鋼之雅里安洛德'], (0xFF, 0xD0, 0x0), ChrTable['鋼之雅里安洛德'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), 0xFF)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvCraft00_2', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['魔弓恩奈雅'], (0xFF, 0xD4, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvSCraft20_1', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['尤西斯'], (0xFF, 0xDB, 0x0), ChrTable['尤西斯'], 0x00000003, (0xDD, 'R_arm_point:NODE_EFFECT01'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 1.100000023841858, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.25, 0x0), (0xEE, 1.25, 0x0), (0xEE, 1.25, 0x0), 0xFF)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvSCraft20_2', -1.0, 1.0, 0x00000000)
    Sleep(30)
    OP_4E(0.3, 0.0, 0x03)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvCraft03_1', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['黎恩'], (0xFF, 0xD9, 0x0), ChrTable['黎恩'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(50)
    PlayEffect(ChrTable['黎恩'], (0xFF, 0xD7, 0x0), ChrTable['黎恩'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.800000011920929, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['黎恩'], (0xFF, 0xD8, 0x0), ChrTable['黎恩'], 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['神速杜巴莉'], (0xFF, 0xD2, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvSCraft01_05', -1.0, 1.0, 0x00000000)
    CameraCtrl(0x0A, 0.15, 0.15, 0.0, 0x0014, 0x012C, 0x07D0, 0x0000, 0x0000, 0x00)
    Sleep(50)
    MoveType(ChrTable['黎恩'], 0xFFFF, -38.73, 114.0, 2.85, 7.5, 0x00, 0x0000)
    MoveType(ChrTable['神速杜巴莉'], 0xFFFF, -41.48, 114.0, -1.99, 6.0, 0x00, 0x0000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvSCraft10_13', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['莎拉'], (0xFF, 0xDA, 0x0), ChrTable['莎拉'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.75, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    Sleep(50)
    MoveType(ChrTable['莎拉'], 0xFFFF, -39.64, 114.0, 4.55, 9.0, 0x00, 0x0000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvCraft00_1', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['剛毅艾奈絲'], (0xFF, 0xD3, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_6C(ChrTable['剛毅艾奈絲'], 0.8)
    MoveType(ChrTable['剛毅艾奈絲'], 0xFFFF, -41.55, 114.0, -3.93, 6.0, 0x00, 0x0000)
    Sleep(300)
    OP_63(0xFFFF, 0x00)
    OP_56(0x17, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 300.0)
    OP_4E(0.1, 0.0, 0x03)
    Sleep(45)
    OP_27('', 0xFFFF)
    OP_3B(0x01, (0xFF, 0x7714, 0x0), (0xFF, 0x1F4, 0x0))
    OP_AC(0x06)

    Return()

# id: 0x001D offset: 0xBD30
@scena.Code('EV_03_81_00_END')
def EV_03_81_00_END():
    OP_58(0xFF)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_4E(1.0, 0.0, 0x03)
    OP_6C(ChrTable['剛毅艾奈絲'], 1.0)
    ChrClearPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['銀臂2'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['安潔莉卡'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['悠娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['庫爾特'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞爾緹娜'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    SetScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))
    Battle(0x00, 0x00000001, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

# id: 0x001E offset: 0xBDD8
@scena.Code('EV_03_81_01')
def EV_03_81_01():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3123, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_BE15',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_BE15(): pass

    label('loc_BE15')

    OP_55(0x00, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_SVIS0318', '')
    OP_55(0x01, 0x0000, 0x0000, 0x0780, 0x0438, 0x0000, 0x0000, 0x0000, 0x0000, 0x0780, 0x0438, 1.0, 1.0, 1.0, 0.0, 0x00, 0x00, 'I_SVIS0318_01', '')
    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evret_01.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evr22_00.eff')
    LoadEffect(0xFFFF, 0xCC, 'event/evr22_01.eff')
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEvDead1', 'AniEv00025', 'AniEvSquat', 'AniEv00024', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['尤西斯'], 0x00, 'AniEvDead1', 'AniEvSquat', 'AniEvGyu', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['米莉亞姆'], 0x00, 'AniEvDead1', 'AniEvSquat', 'AniEvRyoteGyu', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['蓋烏斯'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['莎拉'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvDead1', 'AniEvWeak', 'AniEvBtlWait', 'AniEvFieldAttackEnd', 'AniEv34085', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['悠娜'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', 'AniEvPhoneTalk', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', 'AniEvPhoneLook', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvDead1', 'AniEv32030', 'AniEvPhoneHold', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['神速杜巴莉'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvDead1', 'AniEvSquat', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvk1023', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ClearScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))
    OP_3B(0x37, 0x00002B60)
    OP_3B(0x37, 0x00002BC6)
    OP_3B(0x37, 0x00002C28)
    OP_3B(0x37, 0x00002CF1)
    OP_3B(0x37, 0x00002C8D)
    OP_3B(0x37, 0x00002F45)
    OP_3B(0x37, 0x0000300D)
    OP_3B(0x37, 0x00003071)
    OP_3B(0x37, 0x000030D5)
    SetChrPos(ChrTable['黎恩'], -35.96, 114.0, -2.89, 283.0)
    SetChrPos(ChrTable['尤西斯'], -34.95, 114.0, -1.53, 267.0)
    SetChrPos(ChrTable['米莉亞姆'], -33.56, 114.0, 0.16, 250.7)
    SetChrPos(ChrTable['蓋烏斯'], -34.12, 114.0, -4.59, 274.5)
    SetChrPos(ChrTable['莎拉'], -35.32, 114.0, 0.35, 265.3)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -38.02, 114.0, -0.83, 270.6)
    ChrSetPhysicsFlags(ChrTable['黎恩'], 0x00000010)
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['尤西斯'], 0x00000010)
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['米莉亞姆'], 0x00000010)
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['蓋烏斯'], 0x00000010)
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['莎拉'], 0x00000010)
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['奧蕾莉亞分校長'], 0x00000010)
    OP_38(ChrTable['奧蕾莉亞分校長'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['奧蕾莉亞分校長'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEv34085', -1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['黎恩'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '9', 'E[autoME]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['莎拉'], 0.0, 35.0, 0.0, 0x0000, 0x0000)
    SetChrPos(ChrTable['安潔莉卡'], -35.79, 114.0, -16.17, 354.3)
    SetChrPos(ChrTable['悠娜'], -34.68, 114.0, -14.7, 340.8)
    SetChrPos(ChrTable['庫爾特'], -35.08, 114.0, -15.6, 341.4)
    SetChrPos(ChrTable['亞爾緹娜'], -33.74, 114.0, -14.7, 333.3)
    SetChrPos(ChrTable['亞修'], -33.85, 114.0, -15.6, 333.5)
    SetChrPos(ChrTable['妙婕'], -33.0, 114.0, -15.1, 325.2)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvOdoroki', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvOdoroki', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000001)
    SetChrFace(0x03, ChrTable['悠娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.25, 114.0, -0.97, 84.7)
    SetChrPos(ChrTable['神速杜巴莉'], -48.35, 114.0, -2.69, 72.0)
    SetChrPos(ChrTable['剛毅艾奈絲'], -49.23, 114.0, -5.26, 62.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -47.69, 114.0, -0.0, 98.0)
    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000010)
    OP_38(ChrTable['鋼之雅里安洛德'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['鋼之雅里安洛德'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000010)
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['神速杜巴莉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000010)
    OP_38(ChrTable['剛毅艾奈絲'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['剛毅艾奈絲'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000010)
    OP_38(ChrTable['魔弓恩奈雅'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['魔弓恩奈雅'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvDead1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniAttachMainWeapon', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniAttachMainWeapon', -1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '1', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['神速杜巴莉'], 'C', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '8', 'E[autoME]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['鋼之雅里安洛德'], 0x0000)
    SetChrPos(ChrTable['永世α'], -60.45, 114.0, -0.3, 90.0)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1023', -1.0, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    CameraSetPos(0x03, -38.45, 116.82, -2.22, 0)
    CameraRotate(0x03, 351.0, 99.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    PlayBGM(311, 1.0, 0x0000, 0x00000000, 0x00)
    Call(ScriptId.Sound, 'Init_ENVSE')
    CameraSetPos(0x03, -34.22, 114.92, -2.24, 6000)
    CameraRotate(0x03, 357.0, 104.0, 354.0, 6000, 0x01)
    CameraSetDistance(0x03, 4.3, 6000)
    Fade(0x64, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -38.71, 115.27, -1.96, 0)
    CameraRotate(0x03, 17.0, 232.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -36.75, 114.87, -1.5, 12000)
    CameraRotate(0x03, 10.0, 232.0, 0.0, 12000, 0x01)
    CameraSetDistance(0x03, 1.6, 12000)
    Fade(0xFF, 0, 0x0000)
    Sleep(1500)
    OP_45(ChrTable['尤西斯'], 0.0, 30.0, 0.0, 0x05DC, 0x0000)
    SetChrFace(0x03, ChrTable['尤西斯'], '9998[autoE8]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_8#M_E#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x905E),
            '這就是……極致嗎。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['莎拉'], '#E[9]#M_E#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x905F),
            '唔，修行還不夠呢……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -45.28, 114.74, -0.27, 0)
    CameraRotate(0x03, 8.0, 52.0, 352.0, 0, 0x01)
    CameraSetDistance(0x03, 2.5, 0)
    CameraCtrl(0x0B, 0x03, 32.9, 0x0000)
    CameraSetPos(0x03, -45.99, 114.64, -1.06, 15000)
    CameraRotate(0x03, 6.0, 43.0, 1.0, 15000, 0x01)
    CameraSetDistance(0x03, 2.1, 15000)
    OP_45(ChrTable['尤西斯'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['尤西斯'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], 0xFFFF, 0x0000)
    OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['莎拉'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['莎拉'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E_8#M_8#B_0')

    ChrTalk(
        ChrTable['魔弓恩奈雅'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9060),
            '主人居然會……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E_8#M_2#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9061),
            '被打敗……？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['神速杜巴莉'], 20.0, -30.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[B]#M_8#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9062),
            '不、不可能……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -34.66, 115.17, -14.32, 0)
    CameraRotate(0x03, 358.0, 351.0, 355.0, 0, 0x01)
    CameraSetDistance(0x03, 2.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -34.67, 115.25, -14.43, 20000)
    CameraRotate(0x03, 356.0, 2.0, 355.0, 20000, 0x01)
    CameraSetDistance(0x03, 1.6, 20000)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], 0xFFFF, 0x0000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvWait1', 1.0, 0.8, 0x00000000)
    SetChrFace(0x04, ChrTable['亞修'], '#E[C]#M[H]#B_0')

    ChrTalk(
        ChrTable['亞修'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x2CF3),
            '………………………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['庫爾特'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['庫爾特'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9064),
            '武的化境……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['安潔莉卡'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['安潔莉卡'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['安潔莉卡'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9065),
            '這已經可以\n',
            '紀錄在帝國史上了……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -43.86, 114.41, -1.24, 0)
    CameraRotate(0x03, 13.0, 126.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 0.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -44.29, 114.55, -1.17, 15000)
    CameraRotate(0x03, 6.0, 119.0, 4.0, 15000, 0x01)
    OP_45(ChrTable['安潔莉卡'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['安潔莉卡'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['安潔莉卡'], 0xFFFF, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(2000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9066),
            '……老實說，我很驚訝。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -45.11, 114.79, -0.6, 0)
    CameraRotate(0x03, 3.0, 281.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 2.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -45.08, 115.14, -0.58, 3000)
    CameraRotate(0x03, 4.0, 288.0, 358.0, 25000, 0x01)
    CameraSetDistance(0x03, 2.1, 25000)
    SetChrPos(ChrTable['尤西斯'], -34.42, 114.0, -2.13, 272.9)
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['黎恩'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['鋼之雅里安洛德'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['鋼之雅里安洛德'], 0x0000)
    SetChrPos(ChrTable['神速杜巴莉'], -48.58, 114.0, -2.76, 72.0)
    SetChrPos(ChrTable['魔弓恩奈雅'], -48.12, 114.0, 0.76, 98.0)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEv32030', -1.0, 0.7, 0x00000000)
    CameraCtrl(0x07, 0x0002)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9067),
            '現在的妳\n',
            '已經比曾經的我更強了……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -44.87, 115.46, -0.97, 0)
    CameraRotate(0x03, 8.0, 61.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 0.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 5.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -44.87, 115.46, -0.97, 10000)
    CameraRotate(0x03, 2.0, 66.0, 3.0, 10000, 0x01)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.25, 114.0, -0.97, 90.4)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], 'E', 'A[autoMA]', '0[autoB0]', '#b', '0')
    OP_45(ChrTable['鋼之雅里安洛德'], -20.0, -8.0, 0.0, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[EEEEEEEEEEEE0]#M_A#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9068),
            '呵呵，雖然很不甘心，\n',
            '但我不得不承認。',
            TxtCtl.Enter,
        ),
    )

    Sleep(800)
    OP_45(ChrTable['鋼之雅里安洛德'], -5.0, 0.0, 0.0, 0x05DC, 0x0000)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -37.07, 114.79, -2.79, 0)
    CameraRotate(0x03, 8.0, 308.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 0.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 20.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -36.98, 114.79, -2.83, 20000)
    CameraRotate(0x03, 3.0, 300.0, 1.0, 20000, 0x01)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M[H]#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9069),
            '啊……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906A),
            '……所以是，超越了聖女嗎。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906B),
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -38.46, 115.46, -0.85, 0)
    CameraRotate(0x03, 11.0, 281.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -38.38, 115.45, -0.85, 20000)
    CameraRotate(0x03, 0.0, 294.0, 0.0, 20000, 0x01)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvBtlWait', 1.0, 0.8, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_0#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906C),
            '因為我的年紀\n',
            '比活著時的妳還要多一倍……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '1', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[1]#M_2#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906D),
            '然而……我能到達的境界\n',
            '就到此為止了嗎。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvFieldAttackEnd', -1.0, 0.8, 0x00000000)
    Sleep(1500)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -43.69, 115.2, -0.72, 0)
    CameraRotate(0x03, 354.0, 67.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -44.37, 115.3, -0.82, 15000)
    CameraRotate(0x03, 352.0, 72.0, 0.0, 15000, 0x01)
    OP_45(ChrTable['奧蕾莉亞分校長'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -5.0, 0.0, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1111111110]#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906E),
            '是的──再往上，\n',
            '就是與《巨碩之存在》有關之人的領域了。',
            TxtCtl.Enter,
        ),
    )

    Sleep(800)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.85, 115.13, -2.41, 0)
    CameraRotate(0x03, 358.0, 101.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.2, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraRotate(0x03, 359.0, 102.0, 6.0, 20000, 0x01)
    CameraSetDistance(0x03, 5.7, 1500)
    SetChrPos(ChrTable['米莉亞姆'], -33.78, 114.0, -0.59, 250.7)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['鋼之雅里安洛德'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_44(0x0000, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0006, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0009, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0008, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000F, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0010, 0x15, 0.15, 0x0000, 0.0)
    Sleep(1000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x906F),
            '什麼……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['莎拉'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9070),
            '那個詞……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9071),
            '在那個《夢幻迴廊》的盡頭\n',
            '所聽到的……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Call(ScriptId.Sound, 'Stop_ENVSE_VAR', (0xFF, 0x1F4, 0x0))
    OP_3A(0x03, 0.4, 0x01F4, 0x00)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    OP_57(0x00, 0x03)
    Sleep(1500)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 1.0, 300.0)
    OP_57(0x01, 0x03)
    CameraCtrl(0x00)
    Sleep(1500)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], 0xFFFF, 0x0000)
    SetChrPos(ChrTable['黎恩'], -35.96, 114.0, -2.89, 271.3)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -45.25, 114.0, -0.97, 104.5)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniDetachMainWeapon', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_46(0x00, ChrTable['鋼之雅里安洛德'], ChrTable['黎恩'], 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    CameraSetPos(0x03, -44.69, 115.44, -1.25, 0)
    CameraRotate(0x03, 2.0, 122.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -44.75, 115.44, -1.37, 15000)
    CameraRotate(0x03, 351.0, 106.0, 0.0, 15000, 0x01)
    Call(ScriptId.Sound, 'Init_ENVSE_VAR', (0xFF, 0x3E8, 0x0))
    OP_3A(0x03, 0.7, 0x03E8, 0x00)
    OP_56(0x00, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 0.0)
    OP_56(0x01, 0x03, 0x00, 1.0, 1.0, 1.0, 0.0, 750.0)
    OP_57(0x01, 0x03)
    Sleep(750)
    OP_3A(0x01, 0x0FA0, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9072),
            '《灰》之啟動者，\n',
            '黎恩・舒華澤。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['鋼之雅里安洛德'], 30.0, 0.0, 0.0, 0x05DC, 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '33332[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9073),
            '以及準啟動者們。\n',
            '──你們都做好覺悟了吧？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.43, 115.49, -2.93, 0)
    CameraRotate(0x03, 3.0, 240.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.1, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.43, 115.49, -2.93, 6000)
    CameraRotate(0x03, 0.0, 243.0, 0.0, 6000, 0x01)
    CameraSetDistance(0x03, 1.0, 6000)
    SetChrPos(ChrTable['永世α'], -60.45, 114.0, -1.94, 90.0)
    SetChrPos(ChrTable['安潔莉卡'], -37.23, 114.0, -13.0, 356.4)
    SetChrPos(ChrTable['悠娜'], -35.89, 114.0, -10.7, 355.2)
    SetChrPos(ChrTable['庫爾特'], -36.63, 114.0, -11.46, 356.2)
    SetChrPos(ChrTable['亞爾緹娜'], -35.21, 114.0, -11.19, 354.8)
    SetChrPos(ChrTable['亞修'], -34.51, 114.0, -12.48, 346.4)
    SetChrPos(ChrTable['妙婕'], -34.02, 114.0, -11.49, 347.8)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['悠娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞修'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞修'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['黎恩'], 0x0000)
    ChrClearPhysicsFlags(ChrTable['黎恩'], 0x00000010)
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['黎恩'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEvSquat', -1.0, 0.8, 0x00000002)
    SetChrFace(0x03, ChrTable['黎恩'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    Sleep(800)
    CameraCtrl(0x0A, 0.02, 0.02, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9074),
            '#4S正合我意──！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_3A(0x02, 0x00)
    PlayBGM(460, 0.7, 0x0000, 0x00000000, 0x00)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.38, 115.54, -2.64, 0)
    CameraRotate(0x03, 9.0, 320.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 1.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.38, 115.56, -2.64, 20000)
    CameraRotate(0x03, 8.0, 349.0, 4.0, 20000, 0x01)
    SetChrFace(0x03, ChrTable['黎恩'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv00024', 1.0, 1.0, 0x00000000)
    SetChrPos(ChrTable['尤西斯'], -33.48, 114.0, -1.66, 272.9)
    SetChrPos(ChrTable['米莉亞姆'], -33.8, 114.0, -0.53, 250.7)
    SetChrPos(ChrTable['莎拉'], -35.32, 114.0, 0.35, 265.3)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -36.33, 114.0, -0.66, 270.6)
    ChrClearPhysicsFlags(ChrTable['莎拉'], 0x00000010)
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['莎拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrClearPhysicsFlags(ChrTable['尤西斯'], 0x00000010)
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['尤西斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrClearPhysicsFlags(ChrTable['米莉亞姆'], 0x00000010)
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['米莉亞姆'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['黎恩'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9075),
            '接下來才是重頭戲……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['黎恩'], -50.0, 0.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '336[autoE6]', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(300)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9076),
            '悠娜、庫爾特、亞爾緹娜、\n',
            '亞修和妙婕！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['黎恩'], 0.0, -10.0, 0.0, 0x04B0, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '6667', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[7]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9077),
            '以及尤西斯、米莉亞姆、\n',
            '蓋烏斯和莎拉教官！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.69, 116.49, -2.09, 0)
    CameraRotate(0x03, 355.0, 90.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 5.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 50.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -34.33, 115.6, -2.13, 8000)
    CameraRotate(0x03, 355.0, 91.0, 6.0, 8000, 0x01)
    CameraSetDistance(0x03, 4.8, 8000)
    SetChrPos(ChrTable['黎恩'], -35.95, 114.0, -2.56, 271.3)
    SetChrPos(ChrTable['蓋烏斯'], -33.87, 114.0, -3.95, 274.5)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['黎恩'], 0x0000)
    ChrClearPhysicsFlags(ChrTable['蓋烏斯'], 0x00000010)
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniEvDetachEquip')
    OP_38(ChrTable['蓋烏斯'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['黎恩'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9078),
            '#4S請你們──助我一臂之力！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvRyoteGyu', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvGyu', -1.0, 1.0, 0x00000000)
    CreateThread(ChrTable['莎拉'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    CreateThread(ChrTable['蓋烏斯'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    Sleep(500)
    CameraCtrl(0x0A, 0.02, 0.02, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0004, 0.5, 0x012C, 0x0320, 0x01F4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CreateThread(0xFFFF, 0x02, ScriptId.Sound, 'VOICE_YES_03_81_01')
    OP_27('新舊Ⅶ班', 0xFFFF)
    SetChrFace(0x04, ChrTable['悠娜'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x2B60),
            '#6S喔！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -55.47, 119.19, -3.17, 0)
    CameraRotate(0x03, 6.0, 128.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 9.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -51.95, 117.17, 1.36, 6000)
    CameraRotate(0x03, 348.0, 56.0, 352.0, 6000, 0x01)
    CameraSetDistance(0x03, 11.2, 6000)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x763C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(800)
    OP_3B(0x00, (0xFF, 0x7737, 0x0), 0.7, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7593, 0x0), 0.5, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCB, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    OP_3B(0x01, (0xFF, 0x7737, 0x0), (0xFF, 0xFA0, 0x0))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.75, 115.39, -2.78, 0)
    CameraRotate(0x03, 3.0, 312.0, 13.0, 0, 0x01)
    CameraSetDistance(0x03, 1.7, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[7777777777776]#M_2#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x2B0A),
            '#5S來吧─#20W─\n',
            '#1000W《灰之騎神》瓦利瑪！！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)
    CameraCtrl(0x09, 0.05, 0.05, 0.2)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv00025', 1.0, 1.0, 0x00000000)
    CameraSetPos(0x03, -35.98, 115.65, -2.7, 1200)
    CameraRotate(0x03, 28.0, 270.0, 350.0, 1200, 0x01)
    CameraSetDistance(0x03, 1.5, 1200)
    CameraCtrl(0x0B, 0x03, 34.0, 0x04B0)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.81, 115.34, -10.21, 0)
    CameraRotate(0x03, 9.0, 19.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    CameraSetPos(0x03, -35.8, 115.28, -10.43, 15000)
    CameraRotate(0x03, 359.0, 28.0, 6.0, 15000, 0x01)
    SetChrPos(ChrTable['悠娜'], -35.89, 114.0, -10.7, 355.2)
    SetChrPos(ChrTable['庫爾特'], -36.66, 114.0, -11.3, 26.8)
    SetChrPos(ChrTable['亞爾緹娜'], -35.39, 114.0, -11.21, 354.8)
    SetChrPos(ChrTable['亞修'], -34.82, 114.0, -12.28, 30.3)
    SetChrPos(ChrTable['妙婕'], -33.67, 114.0, -11.63, 295.7)
    SetChrFace(0x03, ChrTable['悠娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['悠娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['亞修'], ChrTable['黎恩'], 0x0000)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['黎恩'], 0x0000)
    SetChrAniFunction(ChrTable['庫爾特'], 0x00, 'AniEvPhoneTalk', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvPhoneLook', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvPhoneTalk', -1.0, 1.2, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    Sleep(1800)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[3322222222222222222332]#M_2#B[777777777777777777770]')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x907B),
            '緹妲，拜託妳！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['庫爾特'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['庫爾特'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x907C),
            '勇士和鷹隼就拜託了！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x907D),
            '現在地點，以信標修正！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -34.56, 115.33, -11.9, 0)
    CameraRotate(0x03, 7.0, 247.0, 5.0, 0, 0x01)
    CameraSetDistance(0x03, 1.7, 0)
    CameraCtrl(0x0B, 0x03, 34.0, 0x0000)
    CameraSetPos(0x03, -34.56, 115.4, -11.9, 6000)
    CameraRotate(0x03, 10.0, 253.0, 5.0, 6000, 0x01)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_46(0x00, ChrTable['亞修'], ChrTable['妙婕'], 0x03E8)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['亞修'], 0x03E8)
    Sleep(1500)
    OP_45(ChrTable['亞修'], 0.0, -20.0, 0.0, 0x01F4, 0x0000)
    OP_45(ChrTable['妙婕'], 0.0, -20.0, 0.0, 0x01F4, 0x0000)
    SetChrFace(0x03, ChrTable['亞修'], '33333332', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '33333332', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    OP_45(ChrTable['亞修'], 0.0, 0.0, 0.0, 0x01F4, 0x0000)
    OP_45(ChrTable['妙婕'], 0.0, 0.0, 0.0, 0x01F4, 0x0000)
    Sleep(1000)
    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_AC(0x06)

    Return()

# id: 0x001F offset: 0xF424
@scena.Code('EV_03_81_01_END')
def EV_03_81_01_END():
    OP_58(0xFF)
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    ReleaseEffect(0xFFFF, 0xCB)
    ReleaseEffect(0xFFFF, 0xCC)
    AnimeClipCtrl(0x09, ChrTable['黎恩'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['尤西斯'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['米莉亞姆'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['蓋烏斯'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['莎拉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['奧蕾莉亞分校長'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['悠娜'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['庫爾特'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['亞爾緹娜'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鋼之雅里安洛德'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['神速杜巴莉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['魔弓恩奈雅'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['剛毅艾奈絲'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['永世α'], 0x00)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3A(0x06, 0x01CC)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    EventJump(0x00000000)
    OP_14(0x04000000)

    Return()

# id: 0x0020 offset: 0xF4C4
@scena.Code('EV_03_81_03')
def EV_03_81_03():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3125, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_F501',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_F501(): pass

    label('loc_F501')

    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evr00_00.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evr00_01.eff')
    LoadEffect(0xFFFF, 0xCC, 'event/evr00_02.eff')
    LoadEffect(0xFFFF, 0xCD, 'event/evret_05.eff')
    LoadEffect(0xFFFF, 0xCE, 'battle/cr011_02_3.eff')
    LoadEffect(0xFFFF, 0xCF, 'event/evret_08.eff')
    LoadEffect(0xFFFF, 0xD0, 'event/evret_01.eff')
    LoadEffect(0xFFFF, 0xD1, 'event/evret_00.eff')
    LoadEffect(0xFFFF, 0xD2, 'event/evret_02.eff')
    LoadEffect(0xFFFF, 0xD3, 'event/evret_04.eff')
    LoadEffect(0xFFFF, 0xD4, 'event/evret_07.eff')
    LoadEffect(0xFFFF, 0xD5, 'event/evcet_03.eff')
    LoadEffect(0xFFFF, 0xD6, 'battle_sys/link_ring1.eff')
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['騎神瓦利瑪'], 'C_ROB000', '騎神瓦利瑪', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['勇士貳型（亞修機）'], 'C_ROB012_C00', '勇士貳型', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鷹隼β（妙婕機）'], 'C_ROB013_C00', '鷹隼β', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['騎神瓦利瑪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['勇士貳型（亞修機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鷹隼β（妙婕機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEv45005', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['亞修'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['妙婕'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['米莉亞姆'], 0x00, 'AniEvRyoteGyu', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['莎拉'], 0x00, 'AniEvUdegumiF', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['尤西斯'], 0x00, 'AniEvTeMune', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['神速杜巴莉'], 0x00, 'AniEvUdegumiF', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')

    AnimeClipLoadMultiple(
        ChrTable['騎神瓦利瑪'],
        0x00,
        'AniEvk0003',
        'AniEvk0005',
        'AniEvk0023',
        'AniEvk0030',
        'AniEvk0020',
        'AniEvk0032',
        'AniEvk0050',
        'AniEvk0530',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    )

    AnimeClipLoadMultiple(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvk1132', 'AniEvk1120', 'AniEvBtlWait', 'AniEvWaitCRAFT01A', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvk1132', 'AniEvk1120', 'AniEvBtlWait', 'AniEvWaitCRAFT01M', '', '', '', '', '', '', '', '', '', '', '', '')
    ClearScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_FFF8',
    )

    PlayBGM(460, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3A(0x06, 0x01CC)

    def _loc_FFF8(): pass

    label('loc_FFF8')

    ChrSetPhysicsFlags(ChrTable['黎恩'], 0x00000200)
    ChrSetPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000200)
    ChrSetPhysicsFlags(ChrTable['勇士貳型（亞修機）'], 0x00000200)
    ChrSetPhysicsFlags(ChrTable['鷹隼β（妙婕機）'], 0x00000200)
    ChrSetPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000080)
    ChrSetPhysicsFlags(ChrTable['勇士貳型（亞修機）'], 0x00000080)
    ChrSetPhysicsFlags(ChrTable['鷹隼β（妙婕機）'], 0x00000080)
    SetChrPos(ChrTable['黎恩'], -41.82, 114.0, -9.98, 14.4)
    SetChrPos(ChrTable['尤西斯'], -33.12, 114.0, -14.26, 11.0)
    SetChrPos(ChrTable['米莉亞姆'], -34.74, 114.0, -14.14, 9.1)
    SetChrPos(ChrTable['蓋烏斯'], -33.76, 114.0, -12.59, 14.1)
    SetChrPos(ChrTable['莎拉'], -35.71, 114.0, -13.08, 10.2)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -34.3, 114.0, -16.72, 7.5)
    OP_46(0x00, ChrTable['黎恩'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['騎神瓦利瑪'], 0x0000)
    SetChrPos(ChrTable['安潔莉卡'], -37.73, 114.0, -15.69, 8.8)
    SetChrPos(ChrTable['悠娜'], -37.74, 114.0, -13.94, 15.8)
    SetChrPos(ChrTable['庫爾特'], -38.72, 114.0, -14.08, 25.6)
    SetChrPos(ChrTable['亞爾緹娜'], -37.21, 114.0, -14.56, 6.3)
    SetChrPos(ChrTable['亞修'], -30.91, 114.0, -15.13, 14.1)
    SetChrPos(ChrTable['妙婕'], -32.38, 114.0, -16.63, 6.6)
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['亞修'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['妙婕'], ChrTable['騎神瓦利瑪'], 0x0000)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -58.2, 114.0, -12.02, 68.2)
    SetChrPos(ChrTable['神速杜巴莉'], -56.71, 114.0, -12.57, 72.0)
    SetChrPos(ChrTable['剛毅艾奈絲'], -57.75, 114.0, -14.05, 62.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -59.52, 114.0, -11.41, 73.0)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000001)
    SetChrPos(ChrTable['永世α'], -63.43, 114.0, -0.28, 87.1)
    SetChrPos(ChrTable['騎神瓦利瑪'], -27.07, 116.93, 0.96, -91.4)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -14.67, 118.13, 7.6, -93.5)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -16.9, 116.97, -7.63, -83.8)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniAttachEQU251', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniAttachEQU252', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0032', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvk1132', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvk1132', -1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['騎神瓦利瑪'], (0xFF, 0xCB, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_R_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    PlayEffect(ChrTable['騎神瓦利瑪'], (0xFF, 0xCB, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_L_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x65)
    PlayEffect(ChrTable['勇士貳型（亞修機）'], (0xFF, 0xCF, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, 'NODE_BACK'), (0xEE, 0.0, 0x0), (0xEE, 0.800000011920929, 0x0), (0xEE, -0.800000011920929, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x66)
    PlayEffect(ChrTable['勇士貳型（亞修機）'], (0xFF, 0xCF, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, 'NODE_BACK'), (0xEE, 1.0, 0x0), (0xEE, 1.2999999523162842, 0x0), (0xEE, -2.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    PlayEffect(ChrTable['勇士貳型（亞修機）'], (0xFF, 0xCF, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, 'NODE_BACK'), (0xEE, -1.0, 0x0), (0xEE, 1.2999999523162842, 0x0), (0xEE, -2.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x68)
    PlayEffect(ChrTable['鷹隼β（妙婕機）'], (0xFF, 0xCF, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, 'NODE_R_FIRE0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x69)
    PlayEffect(ChrTable['鷹隼β（妙婕機）'], (0xFF, 0xCF, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, 'NODE_R_FIRE1'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x6A)
    PlayEffect(ChrTable['鷹隼β（妙婕機）'], (0xFF, 0xCF, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, 'NODE_L_FIRE0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x6B)
    PlayEffect(ChrTable['鷹隼β（妙婕機）'], (0xFF, 0xCF, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, 'NODE_L_FIRE1'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x6C)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD0, 0x0), ChrTable['黎恩'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x6E)
    OP_68(0x00, 'M_V4000', 0x0001)
    OP_68(0x00, 'M_V4000', 0x0002)
    OP_68(0x01, 'M_V4000', 0x0004)
    OP_68(0x05, 'M_V4000')
    CameraSetPos(0x03, -40.71, 115.79, -15.79, 0)
    CameraRotate(0x03, 2.0, 203.0, 359.0, 0, 0x01)
    CameraSetDistance(0x03, 7.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 100.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    OP_8D(0x0320, 0.0, 0.0, 3.0, 0.3)
    OP_8D(0x0335, 0.0, 0.0, 3.0, 0.3)
    OP_8D(0x0332, 0.0, 0.0, 3.0, 0.3)
    MoveType(ChrTable['騎神瓦利瑪'], 0xFFFF, -32.55, 114.0, 0.82, 6.0, 0x00, 0x0000)
    MoveType(ChrTable['鷹隼β（妙婕機）'], 0xFFFF, -25.06, 114.0, -6.74, 5.0, 0x00, 0x0000)
    MoveType(ChrTable['勇士貳型（亞修機）'], 0xFFFF, -22.66, 114.0, 5.99, 4.0, 0x00, 0x0000)
    CameraSetPos(0x03, -38.0, 116.12, -12.16, 4000)
    CameraRotate(0x03, 349.0, 220.0, 353.0, 4000, 0x01)
    CameraSetDistance(0x03, 7.6, 4000)
    OP_5E(0x00, 0x0000, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, (0xFF, 0x75CA, 0x0), 0.5, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7724, 0x0), 0.2, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x64, 800, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_R_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_L_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0020', 0.5, 1.0, 0x00000000)
    CreateThread(0xFFFF, 0x02, ScriptId.Sound, 'SE_ROB000_AniEvk0020')
    EffectCtrl(0x0E, 0x0320, 0x64, 0x00)
    EffectCtrl(0x0E, 0x0320, 0x65, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xCE, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCD, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.3, 0.3, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    Sleep(600)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvk1120', 0.5, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xCE, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCD, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    EffectCtrl(0x0E, 0x0335, 0x69, 0x00)
    EffectCtrl(0x0E, 0x0335, 0x6A, 0x00)
    EffectCtrl(0x0E, 0x0335, 0x6B, 0x00)
    EffectCtrl(0x0E, 0x0335, 0x6C, 0x00)
    CameraCtrl(0x0A, 0.3, 0.3, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x7612, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvk1120', 0.5, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xCE, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCD, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    EffectCtrl(0x0E, 0x0332, 0x66, 0x00)
    EffectCtrl(0x0E, 0x0332, 0x67, 0x00)
    EffectCtrl(0x0E, 0x0332, 0x68, 0x00)
    CameraCtrl(0x0A, 0.3, 0.3, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x7594, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7599, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_41(0x0320, 0x00)
    OP_41(0x0335, 0x00)
    OP_41(0x0332, 0x00)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    OP_3B(0x03, (0xFF, 0x7724, 0x0), 0.7, 0x01F4)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -40.24, 114.91, -7.11, 0)
    CameraRotate(0x03, 6.0, 269.0, 2.0, 0, 0x01)
    CameraSetDistance(0x03, 2.2, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -35.52, 118.91, -1.35, 6000)
    CameraRotate(0x03, 353.0, 220.0, 1.0, 6000, 0x01)
    SetChrPos(ChrTable['黎恩'], -39.99, 114.0, -7.57, 33.2)
    SetChrPos(ChrTable['妙婕'], -31.9, 114.0, -12.5, 31.4)
    SetChrPos(ChrTable['亞修'], -33.0, 114.0, -12.62, 28.2)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniSitWait', 2.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniSitWait', 1.5, 1.0, 0x00000000)
    OP_8D(0x0000, 0.0, 0.0, 1.0, 0.5)
    MoveType(ChrTable['黎恩'], 0xFFFF, -36.06, 114.0, -2.0, 3.3, 0x02, 0x0000)
    OP_6C(ChrTable['黎恩'], 0.5)
    OP_45(ChrTable['黎恩'], 0.0, 30.0, 0.0, 0x0000, 0x0000)
    Sleep(100)
    MoveType(ChrTable['妙婕'], 0xFFFF, -26.55, 114.0, -9.27, 2.8, 0x02, 0x0000)
    Sleep(300)
    MoveType(ChrTable['亞修'], 0xFFFF, -24.84, 114.0, 2.63, 3.3, 0x02, 0x0000)
    OP_41(0x0000, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xD2, 0x0), ChrTable['黎恩'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x75E8, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)
    ChrSetRGBA(ChrTable['黎恩'], 1.0, 1.0, 1.0, 0.0, 500, 0x03)
    PlayEffect(0xFFFF, (0xFF, 0xD1, 0x0), ChrTable['黎恩'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    Sleep(400)
    EffectCtrl(0x0E, 0xFFFF, 0x6E, 0x00)
    MoveType(ChrTable['黎恩'], 0xFFFF, -33.2, 117.97, 0.76, 3.5, 0x01, 0x0000)
    OP_41(0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x75E9, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x7724, 0x0), (0xFF, 0x3E8, 0x0))
    PlayEffect(0xFFFF, (0xFF, 0xD3, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_CORE'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_5E(0x00, 0x0004, 0.3, 0x0064, 0x01F4, 0x00FA, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    EffectCtrl(0x0E, 0x0320, 0x64, 0x00)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -34.12, 119.12, -0.75, 0)
    CameraRotate(0x03, 16.0, 249.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 10.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -34.74, 117.18, 0.89, 5000)
    CameraRotate(0x03, 350.0, 287.0, 13.0, 5000, 0x01)
    OP_41(0x000E, 0x01)
    OP_41(0x000D, 0x01)
    ChrSetPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    SetChrPos(ChrTable['永世α'], -58.23, 114.0, -0.18, 88.9)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniAttachEQU228', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniWait', 2.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniAttachEQU227', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniWait', 1.5, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0050', -1.0, 1.0, 0x00000000)
    CreateThread(0xFFFF, 0x02, ScriptId.Sound, 'SE_ROB000_AniEvk0050')
    Sleep(1766)
    CameraCtrl(0x0A, 0.05, 0.05, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU200', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    Sleep(100)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['尤西斯'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['蓋烏斯'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['莎拉'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['米莉亞姆'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['亞爾緹娜'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['悠娜'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['庫爾特'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(800)
    OP_5E(0x00, 0x0004, 0.6, 0x0064, 0x01F4, 0x01F4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Sleep(100)
    CameraCtrl(0x0A, 0.05, 0.05, 0.0, 0x0064, 0x01F4, 0x01F4, 0x0000, 0x0000, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xD6, 0x0), ChrTable['騎神瓦利瑪'], 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0x6E)
    PlayEffect(0xFFFF, (0xFF, 0xD6, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0x6F)
    PlayEffect(0xFFFF, (0xFF, 0xD6, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0x70)
    OP_3B(0x00, (0xFF, 0x8BC4, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75BB, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x7631, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7715, 0x0), 0.6, (0xFF, 0x3E8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -33.53, 115.46, -13.35, 0)
    CameraRotate(0x03, 9.0, 23.0, 356.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCtrl(0x0B, 0x03, 36.6, 0x0000)
    CameraSetPos(0x03, -33.88, 115.46, -13.11, 20000)
    CameraRotate(0x03, 1.0, 15.0, 358.0, 20000, 0x01)
    SetChrPos(ChrTable['尤西斯'], -33.12, 114.0, -14.26, 11.0)
    SetChrPos(ChrTable['米莉亞姆'], -35.84, 114.0, -14.96, 341.8)
    SetChrPos(ChrTable['蓋烏斯'], -33.84, 114.0, -13.35, 4.3)
    SetChrPos(ChrTable['莎拉'], -34.74, 114.0, -14.06, 3.2)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -39.35, 114.0, -15.91, 7.5)
    SetChrPos(ChrTable['安潔莉卡'], -37.73, 114.0, -15.69, 8.8)
    SetChrPos(ChrTable['悠娜'], -37.74, 114.0, -13.94, 15.8)
    SetChrPos(ChrTable['庫爾特'], -38.72, 114.0, -14.08, 25.6)
    SetChrPos(ChrTable['亞爾緹娜'], -36.77, 114.0, -14.82, 27.8)
    OP_46(0x00, ChrTable['尤西斯'], 0xFFFF, 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['騎神瓦利瑪'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['騎神瓦利瑪'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000000)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9084),
            '這個我聽說過……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9085),
            '比內戰時更加深刻的……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000000)
    OP_45(ChrTable['莎拉'], 0.0, -15.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['莎拉'], 'E', 'A[autoMA]', '0[autoB0]', '#b', '0')
    Sleep(300)
    SetChrFace(0x04, ChrTable['莎拉'], '#E[E]#M_A#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9086),
            '呵呵……\n',
            '居然連我也被承認了。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.33, 115.17, -14.47, 0)
    CameraRotate(0x03, 9.0, 336.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.29, 115.13, -14.47, 15000)
    CameraRotate(0x03, 359.0, 10.0, 1.0, 15000, 0x01)
    CameraSetDistance(0x03, 1.4, 15000)
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '2', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['亞爾緹娜'], 0x03E8)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvRyoteGyu', -1.0, 1.0, 0x00000000)
    SetChrFace(0x04, ChrTable['米莉亞姆'], '#E_2#M_A#B_0')

    ChrTalk(
        ChrTable['米莉亞姆'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9087),
            '小亞，一起加油吧！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['米莉亞姆'], 0x03E8)
    Sleep(500)
    CreateThread(ChrTable['亞爾緹娜'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E[3333332]#M_0#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9088),
            '嗯……！\n',
            '也為了能幫忙教官！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1200)
    OP_45(ChrTable['亞爾緹娜'], -100.0, 20.0, 0.0, 0x04B0, 0x0000)
    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_3B(0x01, (0xFF, 0x7715, 0x0), (0xFF, 0x1F4, 0x0))
    Call(ScriptId.Sound, 'Stop_ENVSE_VAR', (0xFF, 0x1F4, 0x0))
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -224.01, -177.7, -63.71, 0)
    CameraRotate(0x03, 8.0, 302.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -223.53, -177.63, -64.32, 15000)
    CameraRotate(0x03, 5.0, 320.0, 0.0, 15000, 0x01)
    ChrSetRGBA(ChrTable['黎恩'], 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrClearPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv45005', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEv45000', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['妙婕'], 0x00, 'AniEv45000', 0.0, 1.0, 0x00000000)
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['黎恩'], 0xFFFF, 0x0000)
    SetChrPos(ChrTable['黎恩'], -223.55, -178.66, -64.71, 0.1)
    OP_68(0x02, 'Monitor0', -223.86, -177.56, -62.62)
    OP_68(0x03, 'Monitor0', 0.0, 180.0, 0.0)
    OP_50((0xDD, 'Monitor0'), 'open_c')
    OP_B9(0x00, 0x00000000, 0x000E, 'Monitor0', 'face', 0x00000032)
    SetChrFace(0x03, ChrTable['亞修'], '2', '2', '0[autoB0]', '#b', '0')
    OP_B9(0x01, 0x00000000, 0.0, 0.0, 0.0, -7.0, 0.0, 0.0, 0.55)
    OP_B9(0x02, 0x00000000, 6.54, -4.81, -158.68)
    OP_B9(0x03, 0x00000000)
    OP_68(0x02, 'Monitor1', -223.23, -177.56, -62.62)
    OP_68(0x03, 'Monitor1', 0.0, 180.0, 0.0)
    OP_50((0xDD, 'Monitor1'), 'open_c')
    OP_B9(0x00, 0x00000001, 0x000D, 'Monitor1', 'face', 0x00000032)
    SetChrFace(0x03, ChrTable['妙婕'], '2', '2', '0[autoB0]', '#b', '0')
    OP_B9(0x01, 0x00000001, 0.0, 0.0, 0.0, -7.0, 0.0, 0.0, 0.55)
    OP_B9(0x02, 0x00000001, 6.54, -4.81, -158.68)
    OP_B9(0x03, 0x00000001)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9089),
            '──就像剛才說的，\n',
            '那架機體能操縱『空間』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            (TxtCtl.Voice, 0x908A),
            '#E[3333333333333333333336]#M_2#B_0不知道它會做出什麼行動！\n',
            '我們要觀察狀況彼此合作……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -224.0, -177.66, -64.26, 0)
    CameraRotate(0x03, 1.0, 196.0, 358.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -223.97, -177.6, -64.13, 15000)
    CameraRotate(0x03, 357.0, 202.0, 358.0, 15000, 0x01)
    CameraSetDistance(0x03, 1.6, 15000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['亞修'], '#E_0#M_A#B_0')

    ChrTalk(
        ChrTable['亞修'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x908B),
            '#6C哈，就聽你的！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['妙婕'], '#E[333333332]#M_2#B_0')

    ChrTalk(
        ChrTable['妙婕'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x908C),
            '#6C知道了……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Call(ScriptId.Sound, 'Init_ENVSE_VAR', (0xFF, 0x3E8, 0x0))
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -38.56, 120.3, -0.29, 0)
    CameraRotate(0x03, 1.0, 90.0, 348.0, 0, 0x01)
    CameraSetDistance(0x03, 13.2, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -25.04, 119.2, -0.45, 4000)
    CameraRotate(0x03, 359.0, 90.0, 365.0, 4000, 0x01)
    CameraSetDistance(0x03, 21.0, 4000)
    OP_5E(0x00, 0x0004, 0.4, 0x0000, 0x07D0, 0x07D0, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    ChrSetPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x7597, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0530', -1.0, 1.0, 0x00000000)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.6, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvWaitCRAFT01A', -1.0, 1.0, 0x00000000)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x759C, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvWaitCRAFT01M', -1.0, 1.0, 0x00000000)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_AC(0x06)

    Return()

# id: 0x0021 offset: 0x12020
@scena.Code('EV_03_81_03_END')
def EV_03_81_03_END():
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    ReleaseEffect(0xFFFF, 0xCB)
    ReleaseEffect(0xFFFF, 0xCC)
    ReleaseEffect(0xFFFF, 0xCD)
    ReleaseEffect(0xFFFF, 0xCE)
    ReleaseEffect(0xFFFF, 0xCF)
    ReleaseEffect(0xFFFF, 0xD0)
    ReleaseEffect(0xFFFF, 0xD1)
    ReleaseEffect(0xFFFF, 0xD2)
    ReleaseEffect(0xFFFF, 0xD3)
    ReleaseEffect(0xFFFF, 0xD4)
    ReleaseEffect(0xFFFF, 0xD5)
    AnimeClipCtrl(0x09, ChrTable['黎恩'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['亞修'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['妙婕'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['米莉亞姆'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['莎拉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['神速杜巴莉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['尤西斯'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['騎神瓦利瑪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['勇士貳型（亞修機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鷹隼β（妙婕機）'], 0x00)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    ChrClearPhysicsFlags(ChrTable['黎恩'], 0x00000200)
    ChrClearPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000200)
    ChrClearPhysicsFlags(ChrTable['勇士貳型（亞修機）'], 0x00000200)
    ChrClearPhysicsFlags(ChrTable['鷹隼β（妙婕機）'], 0x00000200)
    ChrClearPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000080)
    ChrClearPhysicsFlags(ChrTable['勇士貳型（亞修機）'], 0x00000080)
    ChrClearPhysicsFlags(ChrTable['鷹隼β（妙婕機）'], 0x00000080)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetScenaFlags(ScenaFlag(0x00BA, 2, 0x5D2))
    OP_48(0x00, 0xFFFF, 0x002D, 0x0000)
    Call(ScriptId.System, 'SetKisinChange_Booster')
    Call(ScriptId.System, 'SetKisinChange_Paint2')
    Call(ScriptId.System, 'SetKisinChange_Spiegel')
    Call(ScriptId.System, 'SetKisinChange_Valimar')
    SetScenaFlags(ScenaFlag(0x0087, 1, 0x439))

    OP_18(
        0x31,
        (
            (Expr.PushLong, 0x2A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationCtrl(0x18)
    FormationCtrl(0x17, 0x0000, 0x0009)
    FormationCtrl(0x17, 0x000D, 0x000A)
    FormationCtrl(0x17, 0x000E, 0x000B)
    OP_B7(0x03, 0x0006)
    OP_B7(0x03, 0x0008)
    OP_B7(0x03, 0x0009)
    OP_B7(0x03, 0x000F)
    OP_B7(0x03, 0x000B)
    OP_B7(0x03, 0x000A)
    OP_B7(0x03, 0x000C)
    MenuCmd(0x03, 0x00)
    MenuCmd(0x03, 0x01)
    OP_BA(0x14, 0x01, 0x01)
    OP_BA(0x15)
    OP_CB(0x00)
    FormationCtrl(0x19)
    Battle(0x00, 0x00000002, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

# id: 0x0022 offset: 0x121BC
@scena.Code('EV_03_81_04')
def EV_03_81_04():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3126, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_121F9',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_121F9(): pass

    label('loc_121F9')

    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'battle/damage02.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evr00_02.eff')
    LoadEffect(0xFFFF, 0xCC, 'battle/cr011_02_3.eff')
    LoadEffect(0xFFFF, 0xCD, 'battle/rs000_00_2.eff')
    LoadEffect(0xFFFF, 0xD2, 'battle/rs022_00_0.eff')
    LoadEffect(0xFFFF, 0xD3, 'battle/rs022_00_1.eff')
    CreateChr(ChrTable['黎恩'], 'C_CHR000', '黎恩', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    ChrSetPhysicsFlags(ChrTable['黎恩'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['黎恩'], 0x00000020)
    ChrSetPhysicsFlags(ChrTable['亞修'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['亞修'], 0x00000020)
    ChrSetPhysicsFlags(ChrTable['妙婕'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['妙婕'], 0x00000020)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['騎神瓦利瑪'], 'C_ROB000', '黎恩', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['勇士貳型（亞修機）'], 'C_ROB012_C00', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鷹隼β（妙婕機）'], 'C_ROB013_C00', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['騎神瓦利瑪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['勇士貳型（亞修機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鷹隼β（妙婕機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['騎神瓦利瑪'], 0x00, 'AniSitWait', 'AniBtlDamage', 'AniEvk0058', 'AniEvk0503', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniBtlGuard1', 'AniEvCoopKamae', 'AniEvCoopDash', 'AniEvBtlWait', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniBtlGuard1', 'AniEvCoopKamae', 'AniEvCoopDash', 'AniEvBtlWait', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvkWait5', 'AniEvkWait0', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ClearScenaFlags(ScenaFlag(0x00BA, 2, 0x5D2))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_126BC',
    )

    PlayBGM(460, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3A(0x06, 0x01CC)

    def _loc_126BC(): pass

    label('loc_126BC')

    ChrSetPhysicsFlags(ChrTable['永世α'], 0x00000080)
    ChrSetPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000080)
    ChrSetPhysicsFlags(ChrTable['勇士貳型（亞修機）'], 0x00000080)
    ChrSetPhysicsFlags(ChrTable['鷹隼β（妙婕機）'], 0x00000080)
    LoadAsset('M_V4000')
    LoadAsset('M_V4200')
    SetChrPos(ChrTable['騎神瓦利瑪'], -42.96, 114.0, -0.01, 269.6)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -25.53, 114.0, 8.6, 261.5)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -24.89, 114.0, -7.18, 281.9)
    SetChrPos(ChrTable['永世α'], -60.59, 114.0, -0.5, 90.5)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU200', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniAttachEQU228', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniAttachEQU227', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU200', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0058', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniBtlGuard1', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniBtlGuard1', -1.0, 1.0, 0x00000000)
    OP_68(0x01, 'test_alpha', 0x0001)
    OP_68(0x01, 'test_alpha', 0x0002)
    OP_68(0x00, 'test_alpha', 0x0004)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraSetPos(0x03, -55.01, 121.67, 0.62, 0)
    CameraRotate(0x03, 5.0, 57.0, 352.0, 0, 0x01)
    CameraSetDistance(0x03, 11.1, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 200.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    CameraSetPos(0x03, -37.65, 123.07, -1.77, 9500)
    CameraRotate(0x03, 18.0, 121.0, 351.0, 9500, 0x01)
    CameraSetDistance(0x03, 44.4, 9500)
    CameraCtrl(0x0A, 0.1, 0.1, 0.0, 0x07D0, 0x2710, 0x07D0, 0x0000, 0x0000, 0x00)
    Fade(0x64, 800, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvkWait5', 1.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xD2, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 90.0, 0.0, 0.0, (0xEE, 4.0, 0x0), (0xEE, 4.0, 0x0), (0xEE, 4.0, 0x0), 0x64)
    Sleep(2000)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xD3, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, -20.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x65)
    OP_3B(0x00, (0xFF, 0x1130, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1500)
    OP_3B(0x00, (0xFF, 0x1137, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -1.6, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(900)
    OP_3B(0xFF, 0.5, 0.0, 0.1)
    OP_3B(0x00, (0xFF, 0x114F, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(100)
    OP_3B(0xFF, 0.1, 0.0, 0.3)
    OP_3B(0x00, (0xFF, 0x113D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x113E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    OP_5E(0x00, 0x0004, 0.8, 0x0064, 0x03E8, 0x01F4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CameraSetPos(0x03, -43.03, 121.2, -0.21, 1500)
    CameraRotate(0x03, 11.0, 109.0, 353.0, 1500, 0x01)
    CameraSetDistance(0x03, 10.6, 1500)
    CameraCtrl(0x07, 0x00BF)
    Sleep(800)
    OP_3B(0x00, (0xFF, 0x1157, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -1.5, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_5E(0x00, 0x0004, 0.8, 0x0064, 0x03E8, 0x03E8, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_A1(30.0, 0.0, 1.0, 0x09C4, 0x0003)
    CameraCtrl(0x0A, 0.8, 0.8, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    CameraCtrl(0x02, 0x02, -45.45, 119.72, 0.16, 2000)
    CameraCtrl(0x04, 0x02, 28.0, 121.0, 356.0, 2000, 0x01)
    CameraCtrl(0x05, 0x02, 84.0, 2000)
    CameraCtrl(0x07, 0x00BF)
    OP_3B(0x00, (0xFF, 0x8FAC, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 1.0, 0.5, 0.2)
    Sleep(500)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -32.92, 119.24, -0.63, 0)
    CameraRotate(0x03, 21.0, 225.0, 356.0, 0, 0x01)
    CameraSetDistance(0x03, 11.1, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    CameraSetPos(0x03, -35.79, 119.77, -1.24, 3500)
    CameraRotate(0x03, 15.0, 253.0, 352.0, 3500, 0x01)
    CameraSetDistance(0x03, 3.2, 3500)
    OP_A1(0.0, 0.0, 1.0, 0x000A, 0x0000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU450', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    CameraCtrl(0x0A, 0.05, 0.05, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0503', -1.0, 1.0, 0x00000000)
    Sleep(166)
    OP_8D(0x0320, 0.0, 0.0, 2.0, 0.5)
    MoveType(ChrTable['騎神瓦利瑪'], 0xFFFF, -31.11, 114.0, 0.34, 10.0, 0x00, 0x0001)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_R_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_L_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['騎神瓦利瑪'], (0xFF, 0xCC, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 4.0, 0x0), (0xEE, 4.0, 0x0), (0xEE, 4.0, 0x0), 0xFF)
    Sleep(1000)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.15, 0.15, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    PlayEffect(ChrTable['騎神瓦利瑪'], (0xFF, 0xCC, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), 0xFF)
    OP_41(0x0320, 0x00)
    Sleep(500)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0058', 1.0, 1.0, 0x00000000)
    OP_3B(0x00, (0xFF, 0x7597, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0E, 0x0339, 0x64, 0x00)
    EffectCtrl(0x0E, 0x0339, 0x65, 0x00)
    CameraCtrl(0x07, 0x00BF)
    CameraSetPos(0x03, -35.79, 119.77, -1.24, 10000)
    CameraRotate(0x03, 9.0, 261.0, 351.0, 10000, 0x01)
    CameraSetDistance(0x03, 3.2, 10000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    OP_45(ChrTable['騎神瓦利瑪'], -40.0, 10.0, 0.0, 0x03E8, 0x0000)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000000, 0.6, 0.03, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000001, 1.0, 0.03, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000002, 0.7, 0.47, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000003, 1.0, 0.47, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x09, 0x0000, (0xFF, 0x0, 0x0), 0.0, -0.06, 12.0, 0.0, 0.0, 1.5, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0x0, 0x0), 0x00)
    AttachEquip(0x0000, 'M_V4000', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x0000, '', 'up_point', 0x01)
    OP_76(ChrTable['黎恩'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEv45005', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv45005', -1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['黎恩'], '7', 'F', '0[autoB0]', '#b', '0')
    OP_BC(0x04, 0x0000, (0xFF, 0x0, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xFFFF, 0x0))
    SetChrFace(0x04, ChrTable['黎恩'], '#E_6#M_2#B[7]')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x46A),
            '#4S唔、塞姆利亞石的太刀……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_BC(0x05, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xFFFF, 0x0))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000000, 0.7, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000001, 1.0, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000002, 0.6, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000003, 1.0, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x09, 0x0000, (0xFF, 0xE, 0x0), 0.0, -0.06, 12.0, 0.0, 0.0, 1.5, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0xE, 0x0), 0x00)
    AttachEquip(0x000E, 'M_V4200', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x000E, '', 'up_point', 0x01)
    OP_76(ChrTable['亞修'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['亞修'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEv45000', -1.0, 1.0, 0x00000000)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000000, 0.0, 0.03, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000001, 0.4, 0.03, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000002, 0.0, 0.47, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000003, 0.3, 0.47, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x09, 0x0000, (0xFF, 0xD, 0x0), 0.0, -0.06, -12.0, 0.0, 0.0, 1.5, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0xD, 0x0), 0x00)
    AttachEquip(0x000D, 'M_V4200', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x000D, '', 'up_point', 0x01)
    OP_76(ChrTable['妙婕'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['妙婕'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['妙婕'], 0x00, 'AniEv45000', -1.0, 1.0, 0x00000000)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.24, 119.06, 1.83, 0)
    CameraRotate(0x03, 4.0, 243.0, 356.0, 0, 0x01)
    CameraSetDistance(0x03, 9.4, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    CameraSetPos(0x03, -39.74, 117.64, -3.39, 8000)
    CameraRotate(0x03, 352.0, 232.0, 344.0, 8000, 0x01)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -29.12, 114.0, -6.66, 280.8)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -30.97, 114.0, 7.35, 243.0)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvkWait0', 1.0, 1.0, 0x00000000)
    MoveType(ChrTable['勇士貳型（亞修機）'], 0xFFFF, -34.79, 114.0, 6.42, 1.5, 0x01, 0x0000)
    CreateThread(0xFFFF, 0x02, ScriptId.Sound, 'SE_KIKOU_2_AniWalk_2D')
    Fade(0xFF, 0, 0x0000)
    MoveType(ChrTable['鷹隼β（妙婕機）'], 0xFFFF, -36.58, 114.0, -5.38, 1.5, 0x01, 0x0000)
    OP_41(0x0332, 0x00)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['亞修'], '6', 'F', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2', '2', '0[autoB0]', '#b', '0')
    OP_BC(0x04, 0x0000, (0xFF, 0xE, 0x0), 0x00FA, 0x0003)
    OP_BC(0x04, 0x0000, (0xFF, 0xD, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xFFFF, 0x0))
    SetChrFace(0x04, ChrTable['亞修'], '#E_6#M_6#B_0')

    ChrTalk(
        ChrTable['亞修'],
        0x00000000,
        (
            (TxtCtl.Voice, 0xA78),
            '#4S呿、你退下吧──！',
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvCoopKamae', 1.0, 1.0, 0x00000000)
    OP_41(0x0332, 0x00)
    OP_1F(0xFFFF, 0x02)
    Sleep(1000)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitForMsg()
    Sleep(500)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvCoopKamae', 1.0, 1.0, 0x00000000)
    OP_3B(0x00, (0xFF, 0x759C, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x04, ChrTable['妙婕'], '#E_2#M_6#B_0')

    ChrTalk(
        ChrTable['妙婕'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x94C),
            '#4S這裡就交給我們──！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0x0335, 0x01)
    OP_BC(0x05, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xFFFF, 0x0))
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -17.52, 123.47, -7.39, 0)
    CameraRotate(0x03, 23.0, 118.0, 341.0, 0, 0x01)
    CameraSetDistance(0x03, 14.7, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    CameraSetPos(0x03, -41.83, 119.35, -2.21, 1800)
    CameraRotate(0x03, 357.0, 100.0, 341.0, 1800, 0x01)
    CameraSetDistance(0x03, 10.3, 1800)
    OP_5E(0x00, 0x0004, 0.9, 0x0000, 0x05DC, 0x03E8, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    SetChrPos(ChrTable['騎神瓦利瑪'], -26.51, 114.0, 0.37, 269.6)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -33.06, 114.0, -6.36, -80.3)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -33.07, 114.0, 6.84, -103.7)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvCoopDash', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvCoopDash', -1.0, 1.0, 0x00000000)
    Sleep(30)
    OP_3B(0x00, (0xFF, 0x75C9, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    MoveType(ChrTable['鷹隼β（妙婕機）'], 0xFFFF, -44.18, 114.0, -4.45, 9.0, 0x00, 0x0000)
    MoveType(ChrTable['勇士貳型（亞修機）'], 0xFFFF, -45.2, 114.0, 3.89, 9.0, 0x00, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCD, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCD, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.3, 0.3, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['勇士貳型（亞修機）'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['鷹隼β（妙婕機）'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), 0xFF)
    Sleep(1000)
    OP_AC(0x06)

    Return()

# id: 0x0023 offset: 0x13CC8
@scena.Code('EV_03_81_04_END')
def EV_03_81_04_END():
    CameraCtrl(0x00)
    OP_41(0x0335, 0x01)
    OP_41(0x0332, 0x01)
    OP_BC(0x03, 0x0000, (0xFF, 0xFFFF, 0x0))
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    ReleaseEffect(0xFFFF, 0xCB)
    ReleaseEffect(0xFFFF, 0xCC)
    ReleaseEffect(0xFFFF, 0xCD)
    ReleaseEffect(0xFFFF, 0xD2)
    ReleaseEffect(0xFFFF, 0xD3)
    AnimeClipCtrl(0x09, ChrTable['騎神瓦利瑪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['勇士貳型（亞修機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鷹隼β（妙婕機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['永世α'], 0x00)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_A1(0.0, 0.0, 1.0, 0x0000, 0x0000)
    ChrClearPhysicsFlags(ChrTable['永世α'], 0x00000080)
    ChrClearPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000080)
    ChrClearPhysicsFlags(ChrTable['勇士貳型（亞修機）'], 0x00000080)
    ChrClearPhysicsFlags(ChrTable['鷹隼β（妙婕機）'], 0x00000080)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    SetScenaFlags(ScenaFlag(0x00BA, 3, 0x5D3))
    OP_48(0x00, 0xFFFF, 0x002D, 0x0000)
    OP_CC(0x00)
    OP_CB(0x00)
    FormationCtrl(0x1A)
    FormationCtrl(0x19)
    Battle(0x00, 0x00000003, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

# id: 0x0024 offset: 0x13DA0
@scena.Code('EV_03_81_05')
def EV_03_81_05():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3127, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_13DDD',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_13DDD(): pass

    label('loc_13DDD')

    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evr00_05.eff')
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['騎神瓦利瑪'], 'C_ROB000', '黎恩', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['勇士貳型（亞修機）'], 'C_ROB012_C00', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鷹隼β（妙婕機）'], 'C_ROB013_C00', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['騎神瓦利瑪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['勇士貳型（亞修機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鷹隼β（妙婕機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvkWait4', 'AniEvkWait0', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvBtlWait', 'AniEvCoopKamae', 'AniEvCoopDash', 'AniEvk0058', 'AniEvk0530', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvEscape', 'AniEvBtlWait', 'AniEvCoopKamae', 'AniEvCoopDash', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvGuardB', 'AniEvBtlWait', 'AniEvCoopKamae', 'AniEvCoopDash', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ClearScenaFlags(ScenaFlag(0x00BA, 3, 0x5D3))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_141CF',
    )

    PlayBGM(460, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3A(0x06, 0x01CC)

    def _loc_141CF(): pass

    label('loc_141CF')

    LoadAsset('M_V4000')
    LoadAsset('M_V4200')
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000000, 0.0, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000001, 0.3, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000002, 0.0, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0x0, 0x0), 0x00000003, 0.4, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x09, 0x0000, (0xFF, 0x0, 0x0), 0.0, -0.06, -12.0, 0.0, 0.0, 1.5, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0x0, 0x0), 0x00)
    AttachEquip(0x0000, 'M_V4000', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x0000, '', 'up_point', 0x01)
    OP_76(ChrTable['黎恩'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['黎恩'], 0x00, 'AniEv45005', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['黎恩'], 0x00, 'AniEv45005', -1.0, 1.0, 0x00000000)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000000, 0.0, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000001, 0.3, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000002, 0.0, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xD, 0x0), 0x00000003, 0.4, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x09, 0x0000, (0xFF, 0xD, 0x0), 0.0, -0.06, -12.0, 0.0, 0.0, 1.5, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0xD, 0x0), 0x00)
    AttachEquip(0x000D, 'M_V4200', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x000D, '', 'up_point', 0x01)
    OP_76(ChrTable['妙婕'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['妙婕'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['妙婕'], 0x00, 'AniEv45000', -1.0, 1.0, 0x00000000)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000000, 0.7, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000001, 1.0, 0.53, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000002, 0.6, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x01, 0x0000, (0xFF, 0xE, 0x0), 0x00000003, 1.0, 0.97, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.75506e-40)
    OP_BC(0x09, 0x0000, (0xFF, 0xE, 0x0), 0.0, -0.06, 12.0, 0.0, 0.0, 1.5, 0x0000, 3)
    OP_BC(0x08, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00000001)
    OP_BC(0x02, 0x0000, (0xFF, 0xE, 0x0), 0x00)
    AttachEquip(0x000E, 'M_V4200', 'up_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0x000E, '', 'up_point', 0x01)
    OP_76(ChrTable['亞修'], 'up_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    AnimeClipLoadMultiple(ChrTable['亞修'], 0x00, 'AniEv45000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['亞修'], 0x00, 'AniEv45000', -1.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000040)
    SetChrPos(ChrTable['永世α'], -60.59, 114.0, -0.5, 90.5)
    SetChrPos(ChrTable['騎神瓦利瑪'], -24.87, 114.0, -0.19, 272.3)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -36.18, 114.0, 4.8, 266.5)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -36.79, 114.0, -6.06, 279.4)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU450', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniAttachEQU228', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniAttachEQU227', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0058', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvEscape', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvGuardB', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvkWait4', 0.0, 1.0, 0x00000000)
    OP_68(0x01, 'test_alpha', 0x0001)
    OP_68(0x01, 'test_alpha', 0x0002)
    OP_68(0x00, 'test_alpha', 0x0004)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraSetPos(0x03, -44.51, 121.08, -0.55, 0)
    CameraRotate(0x03, 359.0, 90.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 11.9, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 100.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    CameraSetPos(0x03, -37.55, 118.04, -0.47, 6000)
    CameraRotate(0x03, 352.0, 79.0, 6.0, 6000, 0x01)
    CameraSetDistance(0x03, 14.5, 6000)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvkWait0', 2.0, 1.0, 0x00000000)
    Fade(0x64, 800, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(2000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 2.0, 1.0, 0x00000000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -31.33, 118.74, 0.57, 0)
    CameraRotate(0x03, 8.0, 324.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 4.2, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    CameraSetPos(0x03, -32.23, 118.34, -0.15, 5000)
    CameraRotate(0x03, 345.0, 285.0, 6.0, 5000, 0x01)
    ChrClearPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000040)
    SetChrPos(ChrTable['騎神瓦利瑪'], -29.29, 114.0, -0.01, 272.3)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -35.98, 114.0, 7.35, 248.5)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -36.14, 114.0, -6.6, 282.9)
    OP_6C(ChrTable['永世α'], 1.0)
    OP_3B(0x00, (0xFF, 0x75C7, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_45(ChrTable['騎神瓦利瑪'], -20.0, -15.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    OP_5E(0x00, 0x0002, 0.2, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    PlayEffect(ChrTable['騎神瓦利瑪'], (0xFF, 0xCA, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    OP_3B(0x00, (0xFF, 0x7645, 0x0), 1.0, (0xFF, 0x3E8, 0x0), 0.0, 2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7743, 0x0), 0.3, (0xFF, 0x1F4, 0x0), 0.0, 2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -39.73, 119.44, 5.72, 0)
    CameraRotate(0x03, 14.0, 304.0, 9.0, 0, 0x01)
    CameraSetDistance(0x03, 7.6, 0)
    CameraCtrl(0x0B, 0x03, 36.4, 0x0000)
    CameraSetPos(0x03, -39.73, 119.01, 5.72, 15000)
    CameraRotate(0x03, 5.0, 312.0, 9.0, 15000, 0x01)
    OP_BC(0x04, 0x0000, (0xFF, 0xE, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xE, 0x0))
    SetChrFace(0x03, ChrTable['亞修'], '2', 'F', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['妙婕'], '2', '2', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_45(ChrTable['勇士貳型（亞修機）'], -60.0, 0.0, 0.0, 0x05DC, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['亞修'], '#E[C]#M_8#B[A]')

    ChrTalk(
        ChrTable['亞修'],
        0x00000000,
        (
            (TxtCtl.Voice, 0xA79),
            '怎、怎麼回事……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_BC(0x04, 0x0000, (0xFF, 0xD, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xD, 0x0))
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 1.0, 1.0, 0x00000000)
    OP_45(ChrTable['鷹隼β（妙婕機）'], 60.0, 0.0, 0.0, 0x05DC, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['妙婕'], '#E[CCCCCCCCC332]#M_8#B[A]')

    ChrTalk(
        ChrTable['妙婕'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x94D),
            '這是……藉由ＡＲＣＵＳ\n',
            '聚集著大家的力量……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0x0335, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -33.41, 119.83, -1.23, 0)
    CameraRotate(0x03, 16.0, 254.0, 357.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCtrl(0x0B, 0x03, 42.1, 0x0000)
    CameraSetPos(0x03, -34.09, 120.82, -2.41, 4000)
    CameraRotate(0x03, 30.0, 247.0, 353.0, 4000, 0x01)
    CameraSetDistance(0x03, 1.5, 4000)
    CameraCtrl(0x0B, 0x03, 48.4, 0x0FA0)
    OP_3B(0x00, (0xFF, 0x1151, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75D2, 0x0), 0.7, (0xFF, 0x1F4, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU451', -1.0, 1.0, 0x00000000)
    OP_BC(0x05, 0x0000, (0xFF, 0xD, 0x0), 0x00FA, 0x0003)
    OP_BC(0x05, 0x0000, (0xFF, 0xE, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xE, 0x0))
    OP_BC(0x06, 0x0000, (0xFF, 0xD, 0x0))
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x00, (0xFF, 0x75D2, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_45(ChrTable['騎神瓦利瑪'], -50.0, 40.0, 0.0, 0x07D0, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -30.61, 118.88, -4.05, 0)
    CameraRotate(0x03, 353.0, 111.0, 356.0, 0, 0x01)
    CameraSetDistance(0x03, 5.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -26.29, 117.43, -2.79, 10000)
    CameraRotate(0x03, 352.0, 105.0, 350.0, 10000, 0x01)
    CameraSetDistance(0x03, 10.3, 10000)
    OP_BC(0x04, 0x0000, (0xFF, 0x0, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0x0, 0x0))
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['黎恩'], 0.0, -15.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[3]#M_3#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x46B),
            '我接收到\n',
            '大家的意志了──',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0x0258, 0x0000)
    SetChrFace(0x03, ChrTable['黎恩'], '336', '0[autoM0]', '0[autoB0]', '#b', '0')
    Sleep(500)
    CameraCtrl(0x09, 0.05, 0.05, 0.2)
    SetChrFace(0x04, ChrTable['黎恩'], '#E[6]#M_3#B_0')

    ChrTalk(
        ChrTable['黎恩'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x46C),
            '#5S好──開始反擊！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_BC(0x05, 0x0000, (0xFF, 0xFFFF, 0x0), 0x00FA, 0x0003)
    OP_BC(0x06, 0x0000, (0xFF, 0xFFFF, 0x0))
    OP_5E(0x00, 0x0004, 1.0, 0x0320, 0x03E8, 0x09C4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0530', 1.0, 1.0, 0x00000000)
    Sleep(200)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniBtlCoopKamae', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniBtlCoopKamae', -1.0, 1.0, 0x00000000)
    Sleep(1000)
    OP_3B(0x01, (0xFF, 0x7743, 0x0), (0xFF, 0x1F4, 0x0))
    OP_AC(0x06)

    Return()

# id: 0x0025 offset: 0x15278
@scena.Code('EV_03_81_05_END')
def EV_03_81_05_END():
    CameraCtrl(0x00)
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    AnimeClipCtrl(0x09, ChrTable['永世α'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['騎神瓦利瑪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['勇士貳型（亞修機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鷹隼β（妙婕機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['黎恩'], 0x00)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    ChrClearPhysicsFlags(ChrTable['騎神瓦利瑪'], 0x00000040)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    OP_3A(0x06, 0x0001)
    OP_BC(0x03, 0x0000, (0xFF, 0xFFFF, 0x0))
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    SetScenaFlags(ScenaFlag(0x00BA, 4, 0x5D4))
    OP_48(0x00, 0xFFFF, 0x002D, 0x0000)
    OP_CC(0x00)
    FormationCtrl(0x1A)
    Battle(0x00, 0x00000004, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

# id: 0x0026 offset: 0x15308
@scena.Code('EV_03_81_06')
def EV_03_81_06():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x3128, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_15345',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_15345(): pass

    label('loc_15345')

    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evr00_05.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evr00_02.eff')
    LoadEffect(0xFFFF, 0xCC, 'battle/cr011_02_3.eff')
    LoadEffect(0xFFFF, 0xCD, 'battle/rc022_10_0.eff')
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['騎神瓦利瑪'], 'C_ROB000', '騎神瓦利瑪', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['勇士貳型（亞修機）'], 'C_ROB012_C00', '勇士貳型', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鷹隼β（妙婕機）'], 'C_ROB013_C00', '鷹隼β', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0636, 'O_S00EVT00', '視角', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['騎神瓦利瑪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['勇士貳型（亞修機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鷹隼β（妙婕機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0636, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvBtlWait', 'AniEvk0058', 'AniEvk0530', 'AniEvk0503', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 'AniEvWaitCRAFT01A', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 'AniEvWaitCRAFT01M', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvkWait0', 'AniEvk1026', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['悠娜'], 0x00, 'AniEvRyoteGyu', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    ClearScenaFlags(ScenaFlag(0x00BA, 4, 0x5D4))
    SetChrPos(0x0636, -39.21, 118.99, -0.01, 0.0)
    SetChrPos(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0.0)
    SetChrPos(ChrTable['尤西斯'], -32.64, 114.0, -17.36, 345.1)
    SetChrPos(ChrTable['米莉亞姆'], -35.09, 114.0, -16.81, 327.1)
    SetChrPos(ChrTable['蓋烏斯'], -33.73, 114.0, -16.54, 346.1)
    SetChrPos(ChrTable['莎拉'], -34.25, 114.0, -17.48, 334.6)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -39.01, 114.0, -17.57, 0.7)
    OP_46(0x00, ChrTable['尤西斯'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['莎拉'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], 0x0636, 0x0000)
    SetChrPos(ChrTable['安潔莉卡'], -38.26, 114.0, -17.77, 359.7)
    SetChrPos(ChrTable['悠娜'], -36.8, 114.0, -17.08, 347.4)
    SetChrPos(ChrTable['庫爾特'], -37.57, 114.0, -16.98, 347.0)
    SetChrPos(ChrTable['亞爾緹娜'], -36.3, 114.0, -16.69, 334.7)
    OP_46(0x00, ChrTable['安潔莉卡'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['悠娜'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], 0x0636, 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], 0x0636, 0x0000)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000001)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -58.67, 114.0, -15.2, 42.8)
    SetChrPos(ChrTable['神速杜巴莉'], -58.46, 114.0, -16.55, 47.3)
    SetChrPos(ChrTable['剛毅艾奈絲'], -56.77, 114.0, -16.87, 32.8)
    SetChrPos(ChrTable['魔弓恩奈雅'], -60.52, 114.0, -15.74, 46.9)
    SetChrPos(ChrTable['永世α'], -55.48, 114.0, -0.54, 90.5)
    SetChrPos(ChrTable['騎神瓦利瑪'], -44.14, 114.0, 0.61, 270.1)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -30.88, 114.0, -6.82, 280.4)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -30.49, 114.0, 6.76, 244.2)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU451', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniAttachEQU228', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniAttachEQU227', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvWaitCRAFT01A', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvWaitCRAFT01M', 0.0, 1.0, 0x00000000)
    PlayEffect(ChrTable['騎神瓦利瑪'], (0xFF, 0xCA, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_SHOULDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_SHOULDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_D_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_D_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_LEG'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_LEG'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_BINDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCD, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_BINDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_68(0x01, 'm30evt00', 0x0001)
    OP_68(0x01, 'm30evt00', 0x0002)
    OP_68(0x00, 'm30evt00', 0x0004)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -23.670000076293945, 0x0), (0xEE, 114.0, 0x0), (0xEE, -15.329999923706055, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraSetPos(0x03, -36.85, 121.79, 0.43, 0)
    CameraRotate(0x03, 5.0, 79.0, 11.0, 0, 0x01)
    CameraSetDistance(0x03, 17.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 80.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    CameraSetPos(0x03, -33.33, 118.29, -4.66, 4000)
    CameraRotate(0x03, 356.0, 128.0, 6.0, 4000, 0x01)
    CameraSetDistance(0x03, 19.9, 4000)
    Call(ScriptId.Sound, 'Init_ENVSE')
    OP_3B(0x00, (0xFF, 0x7703, 0x0), 0.4, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x64, 800, 1.0, 0x0000)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1026', 1.0, 0.2, 0x00000000)
    OP_3B(0x00, (0xFF, 0x764A, 0x0), 0.6, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7649, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x765D, 0x0), 0.2, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.05, 0.05, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0503', -1.0, 1.0, 0x00000000)
    Sleep(166)
    OP_8D(0x0320, 0.0, 0.0, 2.0, 0.5)
    MoveType(ChrTable['騎神瓦利瑪'], 0xFFFF, -34.18, 114.0, 0.59, 10.0, 0x00, 0x0001)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_R_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, 'NODE_L_WING0'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 4.0, 0x0), (0xEE, 4.0, 0x0), (0xEE, 4.0, 0x0), 0xFF)
    Sleep(1000)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.15, 0.15, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['騎神瓦利瑪'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), 0xFF)
    OP_41(0x0320, 0x00)
    Sleep(500)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0058', 1.0, 1.0, 0x00000000)
    Sleep(2500)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7599, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75C8, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.15, 0.15, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    PlayEffect(0xFFFF, (0xFF, 0xCC, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), (0xEE, 7.0, 0x0), 0xFF)
    CameraCtrl(0x07, 0x00BF)
    CameraSetPos(0x03, -33.76, 118.29, -5.07, 8000)
    CameraRotate(0x03, 356.0, 124.0, 2.0, 8000, 0x01)
    CameraSetDistance(0x03, 17.6, 8000)
    Sleep(500)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x908D),
            '#5S──漂亮！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    PlayBGM(159, 0.7, 0x0000, 0x00000000, 0x00)
    OP_3B(0x01, (0xFF, 0x7703, 0x0), (0xFF, 0xFA0, 0x0))
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -37.49, 115.46, -16.09, 0)
    CameraRotate(0x03, 13.0, 312.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -37.29, 115.34, -16.26, 15000)
    CameraRotate(0x03, 5.0, 324.0, 0.0, 15000, 0x01)
    CameraSetDistance(0x03, 1.4, 15000)
    SetChrFace(0x03, ChrTable['悠娜'], '4', '4[autoM4]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvRyoteGyu', -1.0, 1.0, 0x00000000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[5]#M_5#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x908E),
            '#5S成功了！！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    CreateThread(ChrTable['庫爾特'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    SetChrFace(0x04, ChrTable['庫爾特'], '#E[1111111110]#M_4#B_0')

    ChrTalk(
        ChrTable['庫爾特'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x908F),
            '亞修和妙婕\n',
            '也非常厲害……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['亞爾緹娜'], 0.0, -10.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E[E]#M_4#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9090),
            '太好了，這麼一來……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 800, 1.0, 0x0000)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0xFF, 0, 0x0000)
    OP_AC(0x06)

    Return()

# id: 0x0027 offset: 0x16B78
@scena.Code('EV_03_81_06_END')
def EV_03_81_06_END():
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    ReleaseEffect(0xFFFF, 0xCB)
    ReleaseEffect(0xFFFF, 0xCC)
    ReleaseEffect(0xFFFF, 0xCD)
    AnimeClipCtrl(0x09, ChrTable['悠娜'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['亞爾緹娜'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['永世α'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['騎神瓦利瑪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['勇士貳型（亞修機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鷹隼β（妙婕機）'], 0x00)
    OP_3A(0x06, 0x009F)
    OP_3A(0x03, 1.0, 0x03E8, 0x00)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    EventJump(0x00000000)
    OP_14(0x04000000)

    Return()

# id: 0x0028 offset: 0x16BF4
@scena.Code('EV_03_81_08')
def EV_03_81_08():
    Call(ScriptId.System, 'FC_EventBegin', (0xFF, 0x312A, 0x0))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_16C31',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    FormationReset()
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])

    def _loc_16C31(): pass

    label('loc_16C31')

    LoadEffect(0xFFFF, 0xC8, 'event/evmm30_00.eff')
    LoadEffect(0xFFFF, 0xC9, 'event/evbom010.eff')
    LoadEffect(0xFFFF, 0xCA, 'event/evc35_00.eff')
    LoadEffect(0xFFFF, 0xCB, 'event/evc35_01.eff')
    LoadEffect(0xFFFF, 0xCC, 'event/evc33_00.eff')
    LoadEffect(0xFFFF, 0xCD, 'event/evc33_01.eff')
    LoadEffect(0xFFFF, 0xCE, 'battle/rc022_10_0.eff')
    LoadEffect(0xFFFF, 0xCF, 'battle/clitical.eff')
    LoadEffect(0xFFFF, 0xD0, 'battle/cr011_02_3.eff')
    LoadEffect(0xFFFF, 0xD2, 'event/evr04_00.eff')
    LoadEffect(0xFFFF, 0xD3, 'event/evr04_01.eff')
    LoadEffect(0xFFFF, 0xD4, 'event/evr04_02.eff')
    LoadEffect(0xFFFF, 0xD5, 'event/evr04_03.eff')
    LoadEffect(0xFFFF, 0xD6, 'event/evbom001.eff')
    LoadEffect(0xFFFF, 0xD7, 'event/evret_10.eff')
    CreateChr(ChrTable['尤西斯'], 'C_CHR006', '尤西斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['米莉亞姆'], 'C_CHR009', '米莉亞姆', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蓋烏斯'], 'C_CHR008', '蓋烏斯', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['莎拉'], 'C_CHR017', '莎拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['奧蕾莉亞分校長'], 'C_CHR021', '奧蕾莉亞', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['安潔莉卡'], 'C_CHR019', '安潔莉卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['悠娜'], 'C_CHR011', '悠娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['庫爾特'], 'C_CHR010', '庫爾特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞爾緹娜'], 'C_CHR015', '亞爾緹娜', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['亞修'], 'C_CHR012', '亞修', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['妙婕'], 'C_CHR013', '妙婕', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鋼之雅里安洛德'], 'C_CHR033', '鋼之雅里安洛德', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['神速杜巴莉'], 'C_CHR035', '神速杜巴莉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['剛毅艾奈絲'], 'C_CHR037', '剛毅艾奈絲', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['魔弓恩奈雅'], 'C_CHR039', '魔弓恩奈雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['永世α'], 'C_ROB022', '神機永世αⅡ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['騎神亞格里昂'], 'C_ROB004', '亞格里昂', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['騎神瓦利瑪'], 'C_ROB000', '騎神瓦利瑪', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['勇士貳型（亞修機）'], 'C_ROB012_C00', '勇士貳型', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['鷹隼β（妙婕機）'], 'C_ROB013_C00', '鷹隼β', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['渥雷斯准將'], 'C_CHR020', '渥雷斯准將', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0654, 'C_CHR366', '領邦軍士兵00', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0655, 'C_CHR367', '領邦軍士兵01', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0656, 'C_CHR366', '領邦軍士兵02', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0657, 'C_CHR367', '領邦軍士兵03', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0658, 'C_CHR366', '領邦軍士兵04', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x0659, 'C_CHR367', '領邦軍士兵05', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x065A, 'C_CHR366', '領邦軍士兵06', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x065B, 'C_CHR367', '領邦軍士兵07', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x065C, 'C_CHR366', '領邦軍士兵08', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(0x065D, 'C_CHR367', '領邦軍士兵09', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蘭迪'], 'C_CHR042', '蘭迪', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['龍人Ⅱ（悠娜機）'], 'C_ROB010_C01', '龍人Ⅱ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['明鏡Ｓ（庫爾特機）'], 'C_ROB010_C11', '明鏡Ｓ', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['阿加特'], 'C_CHR016', '遊擊士阿加特', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['遊擊士托瓦爾'], 'C_CHR046', '遊擊士托瓦爾', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['維因'], 'C_CHR200', '維因', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['席德尼'], 'C_CHR201', '席德尼', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['弗雷迪'], 'C_CHR202', '弗雷迪', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['古斯塔夫'], 'C_CHR203', '古斯塔夫', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['潔西卡'], 'C_CHR600', '潔西卡', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['蕾歐諾拉'], 'C_CHR601', '蕾歐諾拉', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateChr(ChrTable['瑪雅'], 'C_CHR602', '瑪雅', '', 0x00, 0x00000001, 0x00000000, 0.0, 0.0, 0.0, 0.0, 1.0, 1.6, 0.09, '', '', 0xFFFFFFFF, 0x00, 0.0, 0.0, 0x0000)
    CreateThread(ChrTable['黎恩'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['尤西斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['米莉亞姆'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蓋烏斯'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['莎拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['奧蕾莉亞分校長'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['安潔莉卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['悠娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['庫爾特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞爾緹娜'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['亞修'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['妙婕'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鋼之雅里安洛德'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['神速杜巴莉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['剛毅艾奈絲'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['魔弓恩奈雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['永世α'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['騎神亞格里昂'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['騎神瓦利瑪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['勇士貳型（亞修機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['鷹隼β（妙婕機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['渥雷斯准將'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0654, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0655, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0656, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0657, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0658, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x0659, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x065A, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x065B, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x065C, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(0x065D, 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蘭迪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['阿加特'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['遊擊士托瓦爾'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['龍人Ⅱ（悠娜機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['明鏡Ｓ（庫爾特機）'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['維因'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['席德尼'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['弗雷迪'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['古斯塔夫'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['潔西卡'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['蕾歐諾拉'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    CreateThread(ChrTable['瑪雅'], 0x03, ScriptId.System, 'FC_chr_entry')
    Sleep(0)
    AnimeClipLoadMultiple(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['尤西斯'], 0x00, 'AniEvUdegumi', 'AniEvKincho2', 'AniEvUdegumiTeburi', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['蓋烏斯'], 0x00, 'AniEvKincho', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['安潔莉卡'], 0x00, 'AniEvKincho2', 'AniEvSian', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['米莉亞姆'], 0x00, 'AniEvKazetuyo3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['莎拉'], 0x00, 'AniEvKincho', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvUdegumiF', 'AniEvKincho3', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvGourei', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['神速杜巴莉'], 0x00, 'AniEvUdegumiF', 'AniEvKincho', 'AniEvKincho2', 'AniEvRyoteKosi', 'AniEvTeMune', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvTeKosi', 'AniEvKincho', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvOdoroki', 'AniEvUdegumiF', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['悠娜'], 0x00, 'AniEvKazetuyo3', 'AniEvKincho', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['安潔莉卡'], 0x00, 'AniEvKazetuyo', 'AniEvUdegumiF', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['亞爾緹娜'], 0x00, 'AniEvKazetuyo2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvBtlWait', 'AniEvk0058', 'AniEvk0530', 'AniEvk0503', 'AniEvk0530', 'AniEvk0052', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 'AniEvWaitCRAFT01A', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 'AniEvWaitCRAFT01M', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvkWait0', 'AniEvk1026', 'AniEvk1027', 'AniEvk1028', 'AniEvk1029', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['騎神亞格里昂'], 0x00, 'AniEvk1000', 'AniEvk1001', 'AniEvk1002', 'AniEvk1003', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['阿加特'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['蘭迪'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['龍人Ⅱ（悠娜機）'], 0x00, 'AniEvBtlWait', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['維因'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['席德尼'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['潔西卡'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['弗雷迪'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['古斯塔夫'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['蕾歐諾拉'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['瑪雅'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(ChrTable['渥雷斯准將'], 0x00, 'AniEvBtlMove', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0654, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0655, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0656, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0657, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0658, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x0659, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x065A, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x065B, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x065C, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    AnimeClipLoadMultiple(0x065D, 0x00, 'AniEv30020r', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00BA, 7, 0x5D7)),
            Expr.Return,
        ),
        'loc_1853A',
    )

    PlayBGM(159, 1.0, 0x0000, 0x00000000, 0x00)
    OP_3A(0x06, 0x009F)

    def _loc_1853A(): pass

    label('loc_1853A')

    ChrSetPhysicsFlags(ChrTable['騎神亞格里昂'], 0x00000040)
    SetChrPos(ChrTable['黎恩'], 0.0, 0.0, 0.0, 0.0)
    SetChrPos(ChrTable['尤西斯'], -36.07, 114.0, -9.64, 261.9)
    SetChrPos(ChrTable['米莉亞姆'], -35.46, 114.0, -11.6, 267.7)
    SetChrPos(ChrTable['蓋烏斯'], -35.28, 114.0, -7.79, 265.3)
    SetChrPos(ChrTable['莎拉'], -35.56, 114.0, -8.87, 260.9)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -35.28, 114.0, -6.78, 256.3)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['神速杜巴莉'], 0x0000)
    SetChrFace(0x03, ChrTable['尤西斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['米莉亞姆'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蓋烏斯'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['安潔莉卡'], -34.91, 114.0, -11.16, 267.9)
    SetChrPos(ChrTable['悠娜'], -35.1, 114.0, -10.14, 264.4)
    SetChrPos(ChrTable['庫爾特'], -34.27, 114.0, -13.05, 276.0)
    SetChrPos(ChrTable['亞爾緹娜'], -34.8, 114.0, -12.3, 269.9)
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['神速杜巴莉'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['神速杜巴莉'], 0x0000)
    SetChrFace(0x03, ChrTable['安潔莉卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['悠娜'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['庫爾特'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['亞爾緹娜'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['鋼之雅里安洛德'], -50.87, 114.0, -9.14, 86.7)
    SetChrPos(ChrTable['神速杜巴莉'], -50.86, 114.0, -11.79, 86.0)
    SetChrPos(ChrTable['剛毅艾奈絲'], -51.39, 114.0, -12.79, 69.7)
    SetChrPos(ChrTable['魔弓恩奈雅'], -51.47, 114.0, -11.16, 83.9)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000001)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '7', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '1', 'A[autoMA]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['騎神亞格里昂'], -56.75, 114.0, -4.62, 69.0)
    SetChrPos(ChrTable['永世α'], -57.28, 114.0, 14.03, 89.1)
    SetChrPos(ChrTable['騎神瓦利瑪'], -33.68, 114.0, -0.01, 255.3)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -31.82, 114.0, 9.9, 231.8)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -26.5, 114.0, -5.32, 263.2)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniAttachEQU450', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniAttachEQU228', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniAttachEQU227', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvBtlWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1026', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神亞格里昂'], 0x00, 'AniEvk1000', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神亞格里昂'], 0x00, 'AniAttachEQU204', 0.0, 1.0, 0x00000000)
    OP_76(ChrTable['騎神亞格里昂'], 'R_arm_point', 'mode1', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_SHOULDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_SHOULDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_D_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_D_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_LEG'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_LEG'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_L_BINDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(ChrTable['永世α'], (0xFF, 0xCE, 0x0), ChrTable['永世α'], 0x00000003, (0xDD, 'NODE_BTL_R_BINDER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrPos(ChrTable['渥雷斯准將'], 309.36, -10.26, -0.08, 269.5)
    SetChrPos(0x0654, 314.08, -10.38, 2.35, 267.6)
    SetChrPos(0x0655, 311.05, -10.33, 3.22, 267.6)
    SetChrPos(0x0656, 311.58, -10.31, -2.45, 267.6)
    SetChrPos(0x0657, 316.21, -10.43, 4.6, 267.6)
    SetChrPos(0x0658, 315.92, -10.41, -3.05, 267.6)
    SetChrPos(0x0659, 318.56, -10.48, -1.35, 267.6)
    SetChrPos(0x065A, 317.69, -10.01, 1.77, 267.6)
    SetChrPos(0x065B, 320.24, -10.49, 0.36, 267.6)
    SetChrPos(0x065C, 320.89, -10.5, 3.97, 267.6)
    SetChrPos(0x065D, 313.3, -10.35, -0.47, 267.6)
    ChrSetPhysicsFlags(ChrTable['渥雷斯准將'], 0x00000010)
    OP_38(ChrTable['渥雷斯准將'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['渥雷斯准將'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['渥雷斯准將'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0654, 0x00000010)
    OP_38(0x0654, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0654, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0654, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0655, 0x00000010)
    OP_38(0x0655, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0655, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0655, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0656, 0x00000010)
    OP_38(0x0656, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0656, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0656, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0657, 0x00000010)
    OP_38(0x0657, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0657, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0657, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0658, 0x00000010)
    OP_38(0x0658, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0658, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0658, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x0659, 0x00000010)
    OP_38(0x0659, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x0659, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x0659, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x065A, 0x00000010)
    OP_38(0x065A, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x065A, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x065A, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x065B, 0x00000010)
    OP_38(0x065B, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x065B, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x065B, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x065C, 0x00000010)
    OP_38(0x065C, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x065C, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x065C, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(0x065D, 0x00000010)
    OP_38(0x065D, 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(0x065D, 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(0x065D, 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['渥雷斯准將'], 0x00, 'AniEvBtlMove', -1.0, 0.9, 0x00000000)
    SetChrAniFunction(0x0654, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x0655, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x0656, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x0657, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x0658, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x0659, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x065A, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x065B, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x065C, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x065D, 0x00, 'AniAttachEQU110', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(0x0654, 0x00, 'AniEv30020r', 0.0, 1.05, 0x00000000)
    SetChrAniFunction(0x0655, 0x00, 'AniEv30020r', 0.0, 1.02, 0x00000000)
    SetChrAniFunction(0x0656, 0x00, 'AniEv30020r', 0.0, 0.98, 0x00000000)
    SetChrAniFunction(0x0657, 0x00, 'AniEv30020r', 0.0, 0.9, 0x00000000)
    SetChrAniFunction(0x0658, 0x00, 'AniEv30020r', 0.0, 0.95, 0x00000000)
    SetChrAniFunction(0x0659, 0x00, 'AniEv30020r', 0.0, 0.97, 0x00000000)
    SetChrAniFunction(0x065A, 0x00, 'AniEv30020r', 0.0, 1.01, 0x00000000)
    SetChrAniFunction(0x065B, 0x00, 'AniEv30020r', 0.0, 0.94, 0x00000000)
    SetChrAniFunction(0x065C, 0x00, 'AniEv30020r', 0.0, 0.99, 0x00000000)
    SetChrAniFunction(0x065D, 0x00, 'AniEv30020r', 0.0, 0.92, 0x00000000)
    SetChrPos(ChrTable['蘭迪'], 323.8, -10.53, 1.2, 267.6)
    SetChrPos(ChrTable['阿加特'], 333.58, -10.61, 0.35, 267.6)
    SetChrPos(ChrTable['遊擊士托瓦爾'], 333.08, -10.61, 2.39, 267.6)
    ChrSetPhysicsFlags(ChrTable['蘭迪'], 0x00000010)
    OP_38(ChrTable['蘭迪'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['蘭迪'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蘭迪'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['阿加特'], 0x00000010)
    OP_38(ChrTable['阿加特'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['阿加特'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['阿加特'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['遊擊士托瓦爾'], 0x00000010)
    OP_38(ChrTable['遊擊士托瓦爾'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['遊擊士托瓦爾'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['遊擊士托瓦爾'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['蘭迪'], 0x00, 'AniAttachMainWeapon', -1.0, 0.9, 0x00000000)
    SetChrAniFunction(ChrTable['蘭迪'], 0x00, 'AniEvBtlMove', -1.0, 0.9, 0x00000000)
    SetChrAniFunction(ChrTable['阿加特'], 0x00, 'AniEvBtlMove', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['遊擊士托瓦爾'], 0x00, 'AniRun', -1.0, 0.8, 0x00000000)
    SetChrPos(ChrTable['明鏡Ｓ（庫爾特機）'], 348.04, -10.68, 0.52, 267.6)
    SetChrPos(ChrTable['龍人Ⅱ（悠娜機）'], 341.84, -10.71, 3.66, 267.6)
    SetChrAniFunction(ChrTable['龍人Ⅱ（悠娜機）'], 0x00, 'AniAttachEQU240_C01', -1.0, 1.0, 0x00000000)
    SetChrPos(ChrTable['維因'], 326.12, -10.55, -0.23, 267.6)
    SetChrPos(ChrTable['席德尼'], 326.63, -10.55, 3.89, 267.6)
    SetChrPos(ChrTable['弗雷迪'], 329.83, -10.58, -1.03, 267.6)
    SetChrPos(ChrTable['古斯塔夫'], 325.79, -10.55, 2.16, 267.6)
    SetChrPos(ChrTable['潔西卡'], 328.65, -10.56, 0.75, 267.6)
    SetChrPos(ChrTable['蕾歐諾拉'], 331.25, -10.6, 3.97, 267.6)
    SetChrPos(ChrTable['瑪雅'], 329.2, -10.58, 2.5, 267.6)
    SetChrFace(0x03, ChrTable['維因'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['席德尼'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['潔西卡'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['弗雷迪'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['古斯塔夫'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['蕾歐諾拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['瑪雅'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    ChrSetPhysicsFlags(ChrTable['維因'], 0x00000010)
    OP_38(ChrTable['維因'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['維因'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['維因'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['席德尼'], 0x00000010)
    OP_38(ChrTable['席德尼'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['席德尼'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['席德尼'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['潔西卡'], 0x00000010)
    OP_38(ChrTable['潔西卡'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['潔西卡'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['潔西卡'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['弗雷迪'], 0x00000010)
    OP_38(ChrTable['弗雷迪'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['弗雷迪'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['弗雷迪'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['古斯塔夫'], 0x00000010)
    OP_38(ChrTable['古斯塔夫'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['古斯塔夫'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['古斯塔夫'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['蕾歐諾拉'], 0x00000010)
    OP_38(ChrTable['蕾歐諾拉'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['蕾歐諾拉'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['蕾歐諾拉'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    ChrSetPhysicsFlags(ChrTable['瑪雅'], 0x00000010)
    OP_38(ChrTable['瑪雅'], 0x00, 0x00, 'AniEvAttachEquip')
    OP_38(ChrTable['瑪雅'], 0x00, 0x00, 'AniSetWorkWait')
    SetChrAniFunction(ChrTable['瑪雅'], 0x00, 'AniWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['維因'], 0x00, 'AniEvBtlMove', -1.0, 0.9, 0x00000000)
    SetChrAniFunction(ChrTable['席德尼'], 0x00, 'AniEvBtlMove', -1.0, 0.95, 0x00000000)
    SetChrAniFunction(ChrTable['潔西卡'], 0x00, 'AniEvBtlMove', -1.0, 0.98, 0x00000000)
    SetChrAniFunction(ChrTable['弗雷迪'], 0x00, 'AniEvBtlMove', -1.0, 0.92, 0x00000000)
    SetChrAniFunction(ChrTable['古斯塔夫'], 0x00, 'AniEvBtlMove', -1.0, 0.97, 0x00000000)
    SetChrAniFunction(ChrTable['蕾歐諾拉'], 0x00, 'AniEvBtlMove', -1.0, 0.99, 0x00000000)
    SetChrAniFunction(ChrTable['瑪雅'], 0x00, 'AniEvBtlMove', -1.0, 1.0, 0x00000000)
    OP_68(0x00, 'm30evt00', 0x0001)
    OP_68(0x00, 'm30evt00', 0x0002)
    OP_68(0x01, 'm30evt00', 0x0004)
    OP_68(0x05, 'm30evt00')
    OP_68(0x00, 'm30evt00', 0x0004)
    CameraSetPos(0x03, -50.13, 115.16, -11.83, 0)
    CameraRotate(0x03, 356.0, 105.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 40.0)
    OP_7E(0x06, 0x0001)
    OP_AC(0x05, 0x0001)
    CameraSetPos(0x03, -50.52, 115.29, -11.81, 15000)
    CameraRotate(0x03, 359.0, 93.0, 4.0, 15000, 0x01)
    Fade(0x64, 800, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E[111111111110]#M_4#B_0')

    ChrTalk(
        ChrTable['魔弓恩奈雅'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9094),
            '呵呵……挺厲害的嘛。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    CreateThread(ChrTable['剛毅艾奈絲'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E[111111112]#M_4#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9095),
            '嗯……\n',
            '必須認可他們的實力。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvRyoteKosi', -1.0, 1.0, 0x00000000)
    OP_45(ChrTable['神速杜巴莉'], -50.0, 5.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9096),
            '哼……\n',
            '不管結果如何──',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -48.72, 115.41, -11.37, 0)
    CameraRotate(0x03, 7.0, 252.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -49.15, 115.24, -11.07, 18000)
    CameraRotate(0x03, 6.0, 250.0, 0.0, 18000, 0x01)
    SetChrFace(0x03, ChrTable['尤西斯'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrPos(ChrTable['永世α'], -57.08, 114.0, 0.99, 89.1)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvUdegumi', -1.0, 1.0, 0x00000000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9097),
            '──勝負已經確定了。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    Sleep(300)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvUdegumiTeburi', -1.0, 1.0, 0x00000000)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9098),
            '既然妳們已經輸了，\n',
            '可以告訴我們嗎？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvRyoteKosi', -1.0, 1.0, 0x00000002)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], 'C', '9', 'A', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x9099),
            '什麼……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.48, 115.53, -9.83, 0)
    CameraRotate(0x03, 18.0, 226.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -36.51, 115.43, -9.79, 20000)
    CameraRotate(0x03, 0.0, 243.0, 4.0, 20000, 0x01)
    CameraSetDistance(0x03, 1.3, 20000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x909A),
            '在沙薩蘭特、克洛斯貝爾之後，\n',
            '這次在拉瑪爾進行的第３次『實驗』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            (TxtCtl.Voice, 0x909B),
            '#E_2#M_2#B_0妳們真正的目的，以及之後會發生的事。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_46(0x00, ChrTable['悠娜'], ChrTable['尤西斯'], 0x03E8)
    SetChrFace(0x03, ChrTable['悠娜'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[C]#M[H]#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x909C),
            '啊……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    CreateThread(ChrTable['莎拉'], 0x02, ScriptId.System, 'FC_look_dir_Yes')
    SetChrFace(0x04, ChrTable['莎拉'], '#E[33333332]#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x909D),
            '沒錯……這就是我們\n',
            '最大的疑問呢。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.9, 115.21, -11.5, 0)
    CameraRotate(0x03, 3.0, 294.0, 1.0, 0, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -35.65, 115.27, -11.43, 15000)
    CameraRotate(0x03, 2.0, 283.0, 1.0, 15000, 0x01)
    SetChrFace(0x03, ChrTable['米莉亞姆'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['米莉亞姆'], '#E_8#M_2#B[3]')

    ChrTalk(
        ChrTable['米莉亞姆'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x909E),
            '的確，把已經完成職責的機體\n',
            '強化能力之後送出來戰鬥。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrAniFunction(ChrTable['安潔莉卡'], 0x00, 'AniEvSian', -1.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['安潔莉卡'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['安潔莉卡'], '#E[33333333333333333333332]#M_2#B_0')

    ChrTalk(
        ChrTable['安潔莉卡'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x909F),
            '『幻焰計畫』的奪回……\n',
            '就是你們的真正目的對吧？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -49.84, 115.3, -10.58, 0)
    CameraRotate(0x03, 0.0, 47.0, 354.0, 0, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -49.62, 115.28, -9.78, 8000)
    CameraRotate(0x03, 2.0, 49.0, 350.0, 8000, 0x01)
    CameraSetDistance(0x03, 1.4, 8000)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -50.36, 114.0, -9.7, 86.7)
    SetChrPos(ChrTable['神速杜巴莉'], -50.96, 114.0, -11.67, 82.1)
    SetChrPos(ChrTable['剛毅艾奈絲'], -51.17, 114.0, -12.79, 69.7)
    SetChrPos(ChrTable['魔弓恩奈雅'], -51.58, 114.0, -11.17, 83.9)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['尤西斯'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['尤西斯'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['尤西斯'], 0x0000)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '1', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '6[autoE6]', 'E[autoME]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_45(ChrTable['魔弓恩奈雅'], 0.0, -15.0, 0.0, 0x0320, 0x0000)
    Sleep(300)
    OP_45(ChrTable['剛毅艾奈絲'], 0.0, -15.0, 0.0, 0x0320, 0x0000)
    Sleep(500)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '6666666677', 'EEEEEEEEEEEEF', '0[autoB0]', '#b', '0')
    Sleep(300)
    OP_45(ChrTable['神速杜巴莉'], 30.0, -10.0, 0.0, 0x03E8, 0x0000)
    Sleep(2000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A0),
            '──原本應該無法使用的\n',
            '神機們的『奇蹟』之力。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -38.51, 115.42, -8.4, 0)
    CameraRotate(0x03, 2.0, 232.0, 359.0, 0, 0x01)
    CameraSetDistance(0x03, 1.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -38.78, 115.42, -8.39, 20000)
    CameraRotate(0x03, 350.0, 220.0, 9.0, 20000, 0x01)
    OP_8D(0x0008, 0.5, 0.5, 1.0, 0.4)
    MoveType(ChrTable['蓋烏斯'], 0xFFFF, -38.21, 114.0, -7.98, 1.2, 0x01, 0x0000)
    OP_6C(ChrTable['蓋烏斯'], 0.3)
    Fade(0xFF, 0, 0x0000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E[2]#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A1),
            '『人造至寶』在克洛斯貝爾\n',
            '讓該奇蹟化為可能。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_41(0x0008, 0x00)
    OP_45(ChrTable['蓋烏斯'], 0.0, -20.0, 0.0, 0x03E8, 0x0000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E[3]#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A2),
            '但至寶成為普通人類，\n',
            '已經沒有任何人能引發奇蹟了──',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['蓋烏斯'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    SetChrFace(0x03, ChrTable['蓋烏斯'], '336', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(500)
    SetChrFace(0x04, ChrTable['蓋烏斯'], '#E_6#M_2#B_0')

    ChrTalk(
        ChrTable['蓋烏斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A3),
            '那麼即使不完全，卻在經過這３次實驗後，\n',
            '將奇蹟化為可能的又是什麼？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['蓋烏斯'], 0x03E8)
    SetChrFace(0x03, ChrTable['奧蕾莉亞分校長'], '114[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E_0#M_A#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A4),
            '喔……？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_46(0x00, ChrTable['騎神瓦利瑪'], ChrTable['蓋烏斯'], 0x03E8)
    Sleep(300)
    OP_27('黎恩', 0xFFFF)
    SetChrFace(0x04, ChrTable['騎神瓦利瑪'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['騎神瓦利瑪'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A5),
            '蓋烏斯……？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -49.78, 115.47, -10.6, 0)
    CameraRotate(0x03, 9.0, 271.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.4, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -50.04, 115.48, -10.83, 15000)
    CameraRotate(0x03, 4.0, 265.0, 0.0, 15000, 0x01)
    CameraSetDistance(0x03, 4.6, 15000)
    OP_45(ChrTable['剛毅艾奈絲'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['剛毅艾奈絲'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], 0xFFFF, 0x0000)
    OP_45(ChrTable['魔弓恩奈雅'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['魔弓恩奈雅'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], 0xFFFF, 0x0000)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], 0xFFFF, 0x0000)
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['蓋烏斯'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['蓋烏斯'], 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['蓋烏斯'], 0x0000)
    OP_98(0x03E9, 1.0, 0x01)
    OP_98(0x03E8, 0.0, 0x01)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[C]#M_2#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A6),
            '怎、怎麼突然說什麼啊……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, -20.0, 0.0, 0x03E8, 0x0000)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[1]#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A7),
            '托爾茲的《Ⅶ班》──\n',
            '似乎成長為了不起的人呢。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_45(ChrTable['鋼之雅里安洛德'], 0.0, 0.0, 0.0, 0x04B0, 0x0000)
    Sleep(300)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A8),
            '但是話就說到這裡吧。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_44(0x0006, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x0009, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x0008, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x000F, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x0010, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x0012, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x000A, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x000B, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x000C, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x006D, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x006E, 0x01, 0.15, 0x0000, 0.0)
    OP_44(0x006F, 0x01, 0.15, 0x0000, 0.0)
    Sleep(1000)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, 300.86, -9.27, -2.17, 0)
    CameraRotate(0x03, 0.0, 245.0, 351.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, 304.34, -7.58, 4.63, 6000)
    CameraRotate(0x03, 9.0, 295.0, 359.0, 6000, 0x01)
    MoveType(ChrTable['維因'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['席德尼'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['潔西卡'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['弗雷迪'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['古斯塔夫'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['蕾歐諾拉'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['瑪雅'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['渥雷斯准將'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x0654, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x0655, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x0656, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x0657, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x0658, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x0659, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x065A, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x065B, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x065C, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(0x065D, 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['蘭迪'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['阿加特'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['遊擊士托瓦爾'], 0xFE00, 0.0, 0.0, 30.0, 2.8, 0x00, 0x0000)
    MoveType(ChrTable['龍人Ⅱ（悠娜機）'], 0xFE00, 0.0, 0.0, 30.0, 1.2, 0x01, 0x0000)
    Sleep(200)
    MoveType(ChrTable['明鏡Ｓ（庫爾特機）'], 0xFE00, 0.0, 0.0, 30.0, 1.2, 0x01, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(1000)
    SetChrFace(0x04, ChrTable['悠娜'], '#E_4#M_A#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90A9),
            '大家……！',
            0x8,
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)
    OP_63(0xFFFF, 0x00)
    SetChrFace(0x04, ChrTable['庫爾特'], '#E_4#M_A#B_0')

    ChrTalk(
        ChrTable['庫爾特'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90AA),
            '太好了，看來都沒事……！',
            0x8,
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)
    OP_63(0xFFFF, 0x00)
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_3A(0x01, 0x1F40, 0x00)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -37.7, 115.61, -10.75, 0)
    CameraRotate(0x03, 8.0, 93.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 6.6, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -37.63, 115.41, -10.66, 15000)
    CameraRotate(0x03, 1.0, 92.0, 0.0, 15000, 0x01)
    OP_41(0x0096, 0x01)
    OP_41(0x0097, 0x01)
    OP_41(0x00C8, 0x01)
    OP_41(0x0098, 0x01)
    OP_41(0x0099, 0x01)
    OP_41(0x00C9, 0x01)
    OP_41(0x00CA, 0x01)
    OP_41(0x0079, 0x01)
    OP_41(0x0011, 0x01)
    OP_41(0x007D, 0x01)
    OP_41(0x032C, 0x01)
    OP_41(0x032E, 0x01)
    OP_41(0x0654, 0x01)
    OP_41(0x0655, 0x01)
    OP_41(0x0656, 0x01)
    OP_41(0x0657, 0x01)
    OP_41(0x0658, 0x01)
    OP_41(0x0659, 0x01)
    OP_41(0x065A, 0x01)
    OP_41(0x065B, 0x01)
    OP_41(0x065C, 0x01)
    OP_41(0x065D, 0x01)
    ChrSetPhysicsFlags(ChrTable['維因'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['席德尼'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['潔西卡'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['弗雷迪'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['古斯塔夫'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['蕾歐諾拉'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['瑪雅'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['蘭迪'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['阿加特'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['遊擊士托瓦爾'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['龍人Ⅱ（悠娜機）'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['明鏡Ｓ（庫爾特機）'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['渥雷斯准將'], 0x00000001)
    ChrSetPhysicsFlags(0x0654, 0x00000001)
    ChrSetPhysicsFlags(0x0655, 0x00000001)
    ChrSetPhysicsFlags(0x0656, 0x00000001)
    ChrSetPhysicsFlags(0x0657, 0x00000001)
    ChrSetPhysicsFlags(0x0658, 0x00000001)
    ChrSetPhysicsFlags(0x0659, 0x00000001)
    ChrSetPhysicsFlags(0x065A, 0x00000001)
    ChrSetPhysicsFlags(0x065B, 0x00000001)
    ChrSetPhysicsFlags(0x065C, 0x00000001)
    ChrSetPhysicsFlags(0x065D, 0x00000001)
    SetChrPos(ChrTable['永世α'], -62.08, 114.0, 0.48, 90.5)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['安潔莉卡'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -46.900001525878906, 0x0), (0xEE, 114.05999755859375, 0x0), (0xEE, -0.7400000095367432, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    PlayEffect(0xFFFF, (0xFF, 0xC8, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -32.70000076293945, 0x0), (0xEE, 113.95999908447266, 0x0), (0xEE, -10.510000228881836, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x64)
    OP_3B(0x00, (0xFF, 0x75A8, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    Sleep(300)
    OP_44(0x0006, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000A, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000B, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000C, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0009, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000F, 0x15, 0.15, 0x0000, 0.0)
    Sleep(1500)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvTeMune', -1.0, 1.0, 0x00000000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['亞爾緹娜'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['亞爾緹娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90AB),
            '這、這是……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['米莉亞姆'], '#E_8#M_0#B_0')

    ChrTalk(
        ChrTable['米莉亞姆'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90AC),
            '霧……！？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['莎拉'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['莎拉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90AD),
            '就像雷格拉姆一樣……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 750, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -50.12, 115.52, -8.3, 0)
    CameraRotate(0x03, 11.0, 42.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 0.8, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -50.12, 115.52, -8.3, 8000)
    CameraRotate(0x03, 6.0, 51.0, 9.0, 8000, 0x01)
    CameraSetDistance(0x03, 0.6, 8000)
    SetChrPos(ChrTable['鋼之雅里安洛德'], -50.45, 114.0, -8.8, 69.6)
    OP_3D(ChrTable['鋼之雅里安洛德'], 25.0, 5.0, 0x00)
    ChrSetPhysicsFlags(ChrTable['永世α'], 0x00000040)
    Fade(0xFF, 0, 0x0000)
    OP_3F(ChrTable['鋼之雅里安洛德'])
    Sleep(300)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvGourei', -1.0, 1.0, 0x00000000)
    Sleep(300)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    SetChrFace(0x04, ChrTable['鋼之雅里安洛德'], '#E[333333333333332]#M_2#B_0')

    ChrTalk(
        ChrTable['鋼之雅里安洛德'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90AE),
            '#4S出來吧─#17W─#1000W《亞格里昂》。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    PlayBGM(512, 1.0, 0x0000, 0x00000000, 0x00)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -45.31, 120.05, -5.08, 0)
    CameraRotate(0x03, 25.0, 146.0, -5.0, 0, 0x01)
    CameraSetDistance(0x03, 10.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -43.75, 116.46, 2.95, 6000)
    CameraRotate(0x03, 344.0, 57.0, 350.0, 6000, 0x01)
    CameraSetDistance(0x03, 5.5, 6000)
    ChrClearPhysicsFlags(ChrTable['永世α'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['騎神亞格里昂'], 0x00000040)
    SetChrPos(ChrTable['騎神亞格里昂'], -49.54, 114.0, 0.37, 90.5)
    ChrSetRGBA(ChrTable['騎神亞格里昂'], 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x7737, 0x0), 0.3, (0xFF, 0x1F4, 0x0), 0.0, 2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7613, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['騎神亞格里昂'], (0xFF, 0xD7, 0x0), ChrTable['騎神亞格里昂'], 0x00000103, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x72)
    PlayEffect(ChrTable['騎神亞格里昂'], (0xFF, 0xD3, 0x0), ChrTable['騎神亞格里昂'], 0x00020003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, -5.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    Sleep(750)
    OP_3B(0x00, (0xFF, 0x7544, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetRGBA(ChrTable['騎神亞格里昂'], 1.0, 1.0, 1.0, 0.7, 500, 0x03)
    Sleep(1000)
    CameraCtrl(0x07, 0x00BF)
    Sleep(500)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.82, 117.45, -5.17, 0)
    CameraRotate(0x03, 355.0, 124.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 10.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -29.9, 116.41, -7.73, 10000)
    CameraRotate(0x03, 356.0, 125.0, 355.0, 10000, 0x01)
    CameraSetDistance(0x03, 11.6, 10000)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -26.5, 114.0, -5.32, 289.2)
    SetChrPos(ChrTable['尤西斯'], -36.3, 114.0, -8.56, 300.1)
    SetChrPos(ChrTable['米莉亞姆'], -35.83, 114.0, -11.13, 305.8)
    SetChrPos(ChrTable['蓋烏斯'], -36.19, 114.0, -6.74, 287.2)
    SetChrPos(ChrTable['莎拉'], -35.17, 114.0, -7.88, 294.4)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -34.84, 114.0, -5.91, 291.4)
    SetChrPos(ChrTable['安潔莉卡'], -35.08, 114.0, -10.74, 303.5)
    SetChrPos(ChrTable['悠娜'], -34.87, 114.0, -9.71, 302.3)
    SetChrPos(ChrTable['庫爾特'], -35.68, 114.0, -12.59, 308.4)
    SetChrPos(ChrTable['亞爾緹娜'], -34.68, 114.0, -12.18, 313.3)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['騎神亞格里昂'], 0x0000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniDetachEQU450', -1.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_44(0x0006, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0009, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0008, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000F, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0010, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x0012, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000A, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000B, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x000C, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x006D, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x006E, 0x15, 0.15, 0x0000, 0.0)
    OP_44(0x006F, 0x15, 0.15, 0x0000, 0.0)
    OP_6C(ChrTable['尤西斯'], 0.6)
    SetChrAniFunction(ChrTable['尤西斯'], 0x00, 'AniEvKincho2', -1.0, 1.0, 0x00000000)
    Sleep(50)
    OP_6C(ChrTable['莎拉'], 0.6)
    SetChrAniFunction(ChrTable['莎拉'], 0x00, 'AniEvKincho', -1.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvKincho3', -1.0, 1.0, 0x00000000)
    Sleep(50)
    OP_6C(ChrTable['安潔莉卡'], 0.6)
    SetChrAniFunction(ChrTable['安潔莉卡'], 0x00, 'AniEvKincho2', -1.0, 1.0, 0x00000000)
    Sleep(50)
    OP_6C(ChrTable['蓋烏斯'], 0.7)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvKincho', -1.0, 1.0, 0x00000000)
    Sleep(1500)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvWaitCRAFT01A', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvWaitCRAFT01M', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['騎神瓦利瑪'], 0x00, 'AniEvk0052', -1.0, 1.0, 0x00000000)
    OP_3A(0x03, 0.7, 0x01F4, 0x00)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.7, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    OP_27('黎恩', 0xFFFF)
    SetChrFace(0x04, ChrTable['騎神瓦利瑪'], '#E_2#M[2]#B_0')

    ChrTalk(
        ChrTable['騎神瓦利瑪'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x87CD),
            '……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_27('', 0xFFFF)
    SetChrFace(0x04, ChrTable['尤西斯'], '#E_2#M_2#B_0')

    ChrTalk(
        ChrTable['尤西斯'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B0),
            '那是……！',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -50.49, 115.3, -9.56, 0)
    CameraRotate(0x03, 10.0, 27.0, 4.0, 0, 0x01)
    CameraSetDistance(0x03, 2.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -50.57, 115.3, -9.88, 12000)
    CameraRotate(0x03, 2.0, 34.0, 4.0, 12000, 0x01)
    SetChrPos(ChrTable['神速杜巴莉'], -50.69, 114.0, -11.13, 21.3)
    SetChrPos(ChrTable['剛毅艾奈絲'], -50.29, 114.0, -12.24, 5.1)
    SetChrPos(ChrTable['魔弓恩奈雅'], -51.65, 114.0, -11.59, 23.7)
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvKincho2', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvKincho', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvOdoroki', -1.0, 1.0, 0x00000001)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['騎神亞格里昂'], 0x0000)
    SetChrFace(0x03, ChrTable['神速杜巴莉'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '4[autoE4]', 'H', '0[autoB0]', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    SetChrAniFunction(ChrTable['鋼之雅里安洛德'], 0x00, 'AniEvGourei', -1.0, 1.0, 0x00000002)
    SetChrFace(0x03, ChrTable['鋼之雅里安洛德'], '223', '2[autoM2]', '0[autoB0]', '#b', '0')
    Sleep(1000)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['鋼之雅里安洛德'], 0x03E8)
    Sleep(500)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[11C]#M_8#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B1),
            '主、主人……？',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E[C]#M_8#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B2),
            '那、那個難道是……',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -49.74, 117.87, -2.15, 0)
    CameraRotate(0x03, 20.0, 232.0, 3.0, 0, 0x01)
    CameraSetDistance(0x03, 12.2, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 15.0)
    OP_7E(0x06, 0x0001)
    CameraSetPos(0x03, -48.42, 116.87, 0.14, 3200)
    CameraRotate(0x03, 3.0, 277.0, 22.0, 3200, 0x01)
    CameraSetDistance(0x03, 4.5, 3200)
    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000080)
    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    ChrSetPhysicsFlags(ChrTable['永世α'], 0x00000040)
    OP_3D(ChrTable['騎神亞格里昂'], 268.1, 5.0, 0x00)
    OP_3B(0x00, (0xFF, 0x75C7, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_3F(ChrTable['騎神亞格里昂'])
    PlayChrAnimeClip(ChrTable['騎神亞格里昂'], 'evk1001', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 166.667, 167.667, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)
    OP_3B(0x00, (0xFF, 0x760D, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x759D, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_76(ChrTable['騎神亞格里昂'], 'R_arm_point', 'mode1_mode2', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)
    CameraCtrl(0x07, 0x00BF)
    Sleep(200)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -48.34, 119.42, -2.86, 0)
    CameraRotate(0x03, 346.0, 112.0, 346.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    OP_7E(0x00)
    OP_7E(0x02, 0x0001)
    OP_7E(0x05, 30.0)
    OP_7E(0x06, 0x0001)
    CameraCtrl(0x02, 0x02, -47.4, 117.48, -2.72, 500)
    CameraCtrl(0x04, 0x02, 345.0, 116.0, 375.0, 500, 0x01)
    CameraCtrl(0x05, 0x02, 10.9, 500)
    OP_5E(0x00, 0x0000, 0.6, 0x0000, 0x0064, 0x01F4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    PlayChrAnimeClip(ChrTable['騎神亞格里昂'], 'evk1001', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 167.633, 168.633, -1.0, 0x00, 0x00)
    OP_6C(ChrTable['騎神亞格里昂'], 0.8)
    ChrClearPhysicsFlags(ChrTable['永世α'], 0x00000040)
    SetChrPos(ChrTable['永世α'], -57.47, 114.0, 0.06, 90.5)
    Sleep(100)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1029', -1.0, 1.0, 0x00000000)
    OP_6C(ChrTable['永世α'], 0.9)
    OP_3B(0x00, (0xFF, 0x7598, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7635, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xD4, 0x0), ChrTable['騎神亞格里昂'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(100)
    OP_5E(0x00, 0x0004, 0.8, 0x0064, 0x00C8, 0x0320, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CameraCtrl(0x0A, 0.3, 0.3, 0.0, 0x000A, 0x01F4, 0x01F4, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x75C9, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCF, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -55.040000915527344, 0x0), (0xEE, 117.6500015258789, 0x0), (0xEE, 1.2599999904632568, 0x0), 0.0, 0.0, 0.0, (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), (0xEE, 5.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['騎神亞格里昂'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCtrl(0x07, 0x00BF)
    CameraSetPos(0x03, -48.39, 119.14, -3.27, 6000)
    CameraRotate(0x03, 344.0, 115.0, 7.0, 6000, 0x01)
    CameraSetDistance(0x03, 5.4, 6000)
    Sleep(1500)
    OP_3B(0x00, (0xFF, 0x75C9, 0x0), 1.0, (0xFF, 0x64, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75C8, 0x0), 1.0, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 1.0, 0.5, 0.2)
    OP_5E(0x00, 0x0004, 0.75, 0x0064, 0x00C8, 0x0320, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['騎神亞格里昂'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.4, 0.4, 0.0, 0x0064, 0x0064, 0x0190, 0x0000, 0x0000, 0x00)
    Sleep(1200)
    OP_3B(0x00, (0xFF, 0x75C9, 0x0), 1.0, (0xFF, 0x64, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x75C8, 0x0), 1.0, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 1.0, 0.5, 0.2)
    OP_5E(0x00, 0x0004, 0.75, 0x0064, 0x00C8, 0x0320, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    PlayEffect(0xFFFF, (0xFF, 0xD5, 0x0), ChrTable['騎神亞格里昂'], 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.4, 0.4, 0.0, 0x0064, 0x0064, 0x0190, 0x0000, 0x0000, 0x00)
    Sleep(1000)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -36.15, 116.04, -9.61, 0)
    CameraRotate(0x03, 354.0, 108.0, 352.0, 0, 0x01)
    CameraSetDistance(0x03, 3.7, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraCtrl(0x02, 0x02, -36.15, 116.04, -9.61, 3000)
    CameraCtrl(0x04, 0x02, 352.0, 110.0, 9.0, 3000, 0x01)
    CameraCtrl(0x05, 0x02, 7.4, 3000)
    OP_5E(0x00, 0x0004, 1.0, 0x0000, 0x03E8, 0x09C4, 0.5, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_4E(0.4, 0.0, 0x03)
    CameraCtrl(0x0A, 0.5, 0.5, 0.0, 0x0000, 0x01F4, 0x05DC, 0x0000, 0x0000, 0x00)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -35.08, 114.0, -6.37, 291.4)
    AnimeClipChangeSkin(ChrTable['永世α'], 'C_ROB022_C00')
    AnimeClipLoadMultiple(ChrTable['永世α'], 0x00, 'AniEvk1028', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    SetChrAniFunction(ChrTable['安潔莉卡'], 0x00, 'AniEvKazetuyo', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvKazetuyo2', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvKazetuyo3', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvKazetuyo3', -1.0, 1.0, 0x00000000)
    OP_3B(0xFF, 1.0, 0.5, 0.2)
    OP_3B(0x00, (0xFF, 0x75BA, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x755C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xD6, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -58.27000045776367, 0x0), (0xEE, 120.97000122070312, 0x0), (0xEE, -1.7799999713897705, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrAniFunction(ChrTable['永世α'], 0x00, 'AniEvk1028', -1.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_23(0x01, 0x0258, 0x0357, 0x05, 0x0D)
    Fade(0x06, 300)
    OP_AC(0x09, 0x0001)
    PlayEffect(0xFFFF, (0xFF, 0xD6, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -62.75, 0x0), (0xEE, 123.66999816894531, 0x0), (0xEE, 4.739999771118164, 0x0), 0.0, 0.0, 0.0, (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), 0xFF)
    SetChrFace(0x04, ChrTable['悠娜'], '#E[B]#M_E#B_0')

    ChrTalk(
        ChrTable['悠娜'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B3),
            '#5S呀啊──！？',
            0x8,
            TxtCtl.Enter,
        ),
    )

    Sleep(400)
    OP_3B(0x00, (0xFF, 0x755B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x758C, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xD6, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -56.95000076293945, 0x0), (0xEE, 116.79000091552734, 0x0), (0xEE, 1.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), 0xFF)
    Sleep(700)
    OP_63(0xFFFF, 0x00)
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -35.33, 115.51, -6.17, 0)
    CameraRotate(0x03, 15.0, 310.0, 367.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -35.29, 115.47, -6.16, 8000)
    CameraRotate(0x03, 6.0, 319.0, 367.0, 8000, 0x01)
    CameraSetDistance(0x03, 1.1, 8000)
    OP_4E(1.0, 0.0, 0x03)
    SetChrAniFunction(ChrTable['騎神亞格里昂'], 0x00, 'AniEvk1000', 0.0, 1.0, 0x00000000)
    SetChrFace(0x03, ChrTable['莎拉'], '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['騎神亞格里昂'], 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['奧蕾莉亞分校長'], '#E[776]#M_2#B_0')

    ChrTalk(
        ChrTable['奧蕾莉亞分校長'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B4),
            '……相同的動作嗎………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -46.02, 118.34, -1.32, 0)
    CameraRotate(0x03, 8.0, 263.0, 9.0, 0, 0x01)
    CameraSetDistance(0x03, 16.0, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -45.29, 118.64, -1.03, 15000)
    CameraRotate(0x03, 13.0, 253.0, 9.0, 15000, 0x01)
    CameraSetDistance(0x03, 14.0, 15000)
    EffectCtrl(0x0F, 0x0339, 0x00CE, 0x01)
    ChrSetPhysicsFlags(ChrTable['永世α'], 0x00000001)
    OP_68(0x01, 'm30evt00', 0x0004)
    SetChrPos(ChrTable['尤西斯'], -36.3, 114.0, -8.56, 300.1)
    SetChrPos(ChrTable['米莉亞姆'], -35.83, 114.0, -11.13, 305.8)
    SetChrPos(ChrTable['蓋烏斯'], -36.19, 114.0, -6.74, 287.2)
    SetChrPos(ChrTable['莎拉'], -35.17, 114.0, -7.88, 294.4)
    SetChrPos(ChrTable['奧蕾莉亞分校長'], -35.08, 114.0, -6.37, 291.4)
    SetChrPos(ChrTable['安潔莉卡'], -35.08, 114.0, -10.74, 303.5)
    SetChrPos(ChrTable['悠娜'], -34.87, 114.0, -9.71, 302.3)
    SetChrPos(ChrTable['庫爾特'], -35.68, 114.0, -12.59, 308.4)
    SetChrPos(ChrTable['亞爾緹娜'], -34.68, 114.0, -12.18, 313.3)
    SetChrPos(ChrTable['神速杜巴莉'], -50.69, 114.0, -11.13, 21.3)
    SetChrPos(ChrTable['剛毅艾奈絲'], -50.29, 114.0, -12.24, 5.1)
    SetChrPos(ChrTable['魔弓恩奈雅'], -51.65, 114.0, -11.59, 23.7)
    SetChrPos(ChrTable['騎神亞格里昂'], -51.75, 114.0, 0.4, 92.8)
    SetChrPos(ChrTable['騎神瓦利瑪'], -31.81, 114.0, -0.42, 274.6)
    SetChrPos(ChrTable['勇士貳型（亞修機）'], -27.49, 114.0, 7.37, 274.1)
    SetChrPos(ChrTable['鷹隼β（妙婕機）'], -26.21, 114.0, -7.72, 292.6)
    OP_46(0x00, ChrTable['尤西斯'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['米莉亞姆'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['蓋烏斯'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['莎拉'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['奧蕾莉亞分校長'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['安潔莉卡'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['悠娜'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['庫爾特'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['亞爾緹娜'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['神速杜巴莉'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['騎神瓦利瑪'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['勇士貳型（亞修機）'], ChrTable['騎神亞格里昂'], 0x0000)
    OP_46(0x00, ChrTable['鷹隼β（妙婕機）'], ChrTable['騎神亞格里昂'], 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xC9, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -67.44999694824219, 0x0), (0xEE, 114.62000274658203, 0x0), (0xEE, -4.349999904632568, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFF, (0xFF, 0xC9, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -70.79000091552734, 0x0), (0xEE, 115.19999694824219, 0x0), (0xEE, 0.8199999928474426, 0x0), 0.0, 0.0, 0.0, (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), 0xFF)
    OP_68(0x02, 'm30evt00', -67.61, 113.98, -0.89)
    OP_68(0x03, 'm30evt00', 0.0, 302.66, 0.0)
    Fade(0xFF, 0, 0x0000)
    OP_45(ChrTable['騎神亞格里昂'], 30.0, -5.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    OP_27('聖女的聲音', 0xFFFF)
    SetChrFace(0x04, ChrTable['騎神亞格里昂'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['騎神亞格里昂'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B5),
            '──所有\n',
            '『嘗試』的結果已經出來了。',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)
    WaitForMsg()
    OP_45(ChrTable['騎神亞格里昂'], 0.0, 0.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    SetChrFace(0x04, ChrTable['騎神亞格里昂'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['騎神亞格里昂'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B6),
            '會按照深淵的意思，\n',
            '抑或是『改寫』。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -41.5, 115.98, 0.17, 0)
    CameraRotate(0x03, 354.0, 82.0, 2.0, 0, 0x01)
    CameraSetDistance(0x03, 8.2, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -48.88, 118.27, 0.52, 15000)
    CameraRotate(0x03, 344.0, 121.0, 9.0, 15000, 0x01)
    CameraSetDistance(0x03, 11.8, 15000)
    Fade(0xFF, 0, 0x0000)
    SetChrAniFunction(ChrTable['騎神亞格里昂'], 0x00, 'AniEvk1003', -1.0, 1.0, 0x00000000)
    OP_3B(0x00, (0xFF, 0x759C, 0x0), 0.8, (0xFF, 0x64, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_27('聖女的聲音', 0xFFFF)
    SetChrFace(0x04, ChrTable['騎神亞格里昂'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['騎神亞格里昂'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B7),
            '時候已經近了──\n',
            '各自找出自己的答案吧。',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)
    OP_3B(0x00, (0xFF, 0x759A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(700)
    OP_3B(0x00, (0xFF, 0x7595, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xD0, 0x0), ChrTable['騎神亞格里昂'], 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.009999999776482582, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 3.0, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.05, 0.05, 0.0, 0x0064, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    WaitForMsg()
    OP_27('', 0xFFFF)
    OP_45(ChrTable['騎神亞格里昂'], 30.0, -20.0, 0.0, 0x03E8, 0x0000)
    Sleep(500)
    OP_27('聖女的聲音', 0xFFFF)
    SetChrFace(0x04, ChrTable['騎神亞格里昂'], '#E_0#M_0#B_0')

    ChrTalk(
        ChrTable['騎神亞格里昂'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B8),
            '鐵機隊撤退──走吧。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    OP_27('', 0xFFFF)
    OP_45(ChrTable['騎神亞格里昂'], 0.0, 0.0, 0.0, 0x05DC, 0x0000)
    OP_3B(0x00, (0xFF, 0x7613, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x7737, 0x0), (0xFF, 0x3E8, 0x0))
    PlayEffect(ChrTable['騎神亞格里昂'], (0xFF, 0xD3, 0x0), ChrTable['騎神亞格里昂'], 0x00020003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, -5.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0xFF)
    Sleep(300)
    OP_3B(0x00, (0xFF, 0x7544, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetRGBA(ChrTable['騎神亞格里昂'], 1.0, 1.0, 1.0, 0.0, 800, 0x03)
    Sleep(1000)
    EffectCtrl(0x0E, 0xFFFF, 0x64, 0x00)
    EffectCtrl(0x0E, 0xFFFF, 0x65, 0x00)
    EffectCtrl(0x0E, 0xFFFF, 0x66, 0x00)
    Sleep(1000)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -50.3, 115.37, -11.14, 0)
    CameraRotate(0x03, 16.0, 19.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 1.5, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -50.3, 115.37, -11.18, 10000)
    CameraRotate(0x03, 9.0, 29.0, 6.0, 10000, 0x01)
    CameraSetDistance(0x03, 0.9, 10000)
    ChrSetPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['騎神亞格里昂'], 0x00000001)
    SetChrPos(ChrTable['神速杜巴莉'], -50.37, 114.0, -11.22, 5.9)
    SetChrPos(ChrTable['魔弓恩奈雅'], -50.67, 114.0, -8.6, 165.3)
    SetChrPos(ChrTable['剛毅艾奈絲'], -48.41, 114.0, -9.13, 282.2)
    SetChrAniFunction(ChrTable['剛毅艾奈絲'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['魔弓恩奈雅'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    OP_46(0x00, ChrTable['魔弓恩奈雅'], ChrTable['神速杜巴莉'], 0x03E8)
    OP_46(0x00, ChrTable['神速杜巴莉'], 0xFFFF, 0x0000)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 15.0, 0.0, 0x0000, 0x0000)
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x04, ChrTable['神速杜巴莉'], '#E[C]#M[H]#B_0')

    ChrTalk(
        ChrTable['神速杜巴莉'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90B9),
            '………………………',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -50.07, 115.12, -10.76, 0)
    CameraRotate(0x03, 360.0, 166.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 2.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -50.15, 115.29, -10.69, 15000)
    CameraRotate(0x03, 1.0, 166.0, 6.0, 15000, 0x01)
    CameraSetDistance(0x03, 2.0, 15000)
    OP_3B(0x00, (0xFF, 0x770F, 0x0), 0.5, (0xFF, 0x1F4, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(ChrTable['魔弓恩奈雅'], (0xFF, 0xCA, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x67)
    MoveType(ChrTable['剛毅艾奈絲'], 0xFFFF, -49.61, 114.0, -8.58, 0.9, 0x01, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_41(0x006E, 0x00)
    PlayEffect(ChrTable['剛毅艾奈絲'], (0xFF, 0xCA, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x68)
    OP_3D(ChrTable['剛毅艾奈絲'], 190.9, 10.0, 0x00)
    OP_46(0x00, ChrTable['剛毅艾奈絲'], ChrTable['神速杜巴莉'], 0x03E8)
    OP_3F(ChrTable['剛毅艾奈絲'])
    SetChrFace(0x04, ChrTable['剛毅艾奈絲'], '#E_0#M_2#B_0')

    ChrTalk(
        ChrTable['剛毅艾奈絲'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90BA),
            '……走了。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    SetChrFace(0x04, ChrTable['魔弓恩奈雅'], '#E[2]#M_2#B_0')

    ChrTalk(
        ChrTable['魔弓恩奈雅'],
        0x00000000,
        (
            (TxtCtl.Voice, 0x90BB),
            '有問題之後再說。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()
    OP_63(0xFFFF, 0x01)
    Fade(0x6A, 300)
    OP_AC(0x09, 0x0000)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    SetChrAniFunction(ChrTable['神速杜巴莉'], 0x00, 'AniEvKincho2', -1.0, 1.0, 0x00000002)
    OP_45(ChrTable['神速杜巴莉'], 0.0, 0.0, 0.0, 0x0320, 0x0000)
    PlayEffect(ChrTable['神速杜巴莉'], (0xFF, 0xCA, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x69)
    Sleep(1000)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['魔弓恩奈雅'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(500)
    OP_3B(0x00, (0xFF, 0x75BB, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['剛毅艾奈絲'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(1500)
    PlayEffect(0xFFFF, (0xFF, 0xCB, 0x0), ChrTable['神速杜巴莉'], 0x00000003, (0xDD, ''), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    SetChrFace(0x03, ChrTable['魔弓恩奈雅'], '3', '2[autoM2]', '0[autoB0]', '#b', '0')
    CameraCtrl(0x00)
    CameraSetPos(0x03, -50.15, 115.29, -10.69, 5000)
    CameraRotate(0x03, 8.0, 164.0, 0.0, 5000, 0x01)
    CameraSetDistance(0x03, 4.6, 5000)
    OP_3B(0x00, (0xFF, 0x75BD, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0E, 0x006F, 0x67, 0x00)
    ChrSetRGBA(ChrTable['魔弓恩奈雅'], 1.0, 1.0, 1.0, 0.0, 500, 0x03)
    Sleep(300)
    OP_3B(0x00, (0xFF, 0x75BD, 0x0), 0.7, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x03, ChrTable['剛毅艾奈絲'], '1', '2[autoM2]', '0[autoB0]', '#b', '0')
    EffectCtrl(0x0E, 0x006E, 0x68, 0x00)
    ChrSetRGBA(ChrTable['剛毅艾奈絲'], 1.0, 1.0, 1.0, 0.0, 500, 0x03)
    Sleep(1500)
    OP_3B(0x00, (0xFF, 0x75BD, 0x0), 0.85, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetRGBA(ChrTable['神速杜巴莉'], 1.0, 1.0, 1.0, 0.0, 500, 0x03)
    EffectCtrl(0x0E, 0x006D, 0x69, 0x00)
    OP_3B(0x01, (0xFF, 0x770F, 0x0), (0xFF, 0x7D0, 0x0))
    Sleep(1500)
    CameraCtrl(0x07, 0x00BF)
    Fade(0x65, 800, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -44.32, 116.97, -9.09, 0)
    CameraRotate(0x03, 13.0, 124.0, 2.0, 0, 0x01)
    CameraSetDistance(0x03, 12.3, 0)
    CameraCtrl(0x0B, 0x03, 34.6, 0x0000)
    CameraSetPos(0x03, -39.23, 117.76, -7.61, 7000)
    CameraRotate(0x03, 18.0, 123.0, 6.0, 7000, 0x01)
    CameraSetDistance(0x03, 25.3, 7000)
    ChrSetPhysicsFlags(ChrTable['剛毅艾奈絲'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['魔弓恩奈雅'], 0x00000001)
    ChrSetPhysicsFlags(ChrTable['神速杜巴莉'], 0x00000001)
    SetChrAniFunction(ChrTable['蓋烏斯'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['奧蕾莉亞分校長'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['米莉亞姆'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['亞爾緹娜'], 0x00, 'AniEvWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['悠娜'], 0x00, 'AniEvKincho', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['安潔莉卡'], 0x00, 'AniEvUdegumiF', -1.0, 1.0, 0x00000001)
    SetChrAniFunction(ChrTable['勇士貳型（亞修機）'], 0x00, 'AniEvBtlWait', 0.0, 1.0, 0x00000000)
    SetChrAniFunction(ChrTable['鷹隼β（妙婕機）'], 0x00, 'AniEvBtlWait', 0.0, 1.0, 0x00000000)
    Fade(0xFF, 0, 0x0000)
    OP_3A(0x01, 0x0FA0, 0x00)
    Sleep(5500)
    Call(ScriptId.Sound, 'Stop_ENVSE')
    Fade(0x00, 1000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    CameraCtrl(0x00)
    OP_3A(0x02, 0x00)
    OP_AC(0x06)

    Return()

# id: 0x0029 offset: 0x1D834
@scena.Code('EV_03_81_08_END')
def EV_03_81_08_END():
    OP_4E(1.0, 0.0, 0x03)
    ReleaseEffect(0xFFFF, 0xC8)
    ReleaseEffect(0xFFFF, 0xC9)
    ReleaseEffect(0xFFFF, 0xCA)
    ReleaseEffect(0xFFFF, 0xCB)
    ReleaseEffect(0xFFFF, 0xCC)
    ReleaseEffect(0xFFFF, 0xCD)
    ReleaseEffect(0xFFFF, 0xCE)
    ReleaseEffect(0xFFFF, 0xCF)
    ReleaseEffect(0xFFFF, 0xD0)
    ReleaseEffect(0xFFFF, 0xD2)
    ReleaseEffect(0xFFFF, 0xD3)
    ReleaseEffect(0xFFFF, 0xD4)
    ReleaseEffect(0xFFFF, 0xD5)
    ReleaseEffect(0xFFFF, 0xD6)
    AnimeClipCtrl(0x09, ChrTable['尤西斯'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['蓋烏斯'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['莎拉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['米莉亞姆'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['奧蕾莉亞分校長'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['安潔莉卡'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['悠娜'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['亞爾緹娜'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['庫爾特'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鋼之雅里安洛德'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['神速杜巴莉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['剛毅艾奈絲'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['魔弓恩奈雅'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['永世α'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['騎神瓦利瑪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['勇士貳型（亞修機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['鷹隼β（妙婕機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['騎神亞格里昂'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['維因'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['席德尼'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['潔西卡'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['弗雷迪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['古斯塔夫'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['蕾歐諾拉'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['瑪雅'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['阿加特'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['蘭迪'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['龍人Ⅱ（悠娜機）'], 0x00)
    AnimeClipCtrl(0x09, ChrTable['渥雷斯准將'], 0x00)
    AnimeClipCtrl(0x09, 0x0654, 0x00)
    AnimeClipCtrl(0x09, 0x0655, 0x00)
    AnimeClipCtrl(0x09, 0x0656, 0x00)
    AnimeClipCtrl(0x09, 0x0657, 0x00)
    AnimeClipCtrl(0x09, 0x0658, 0x00)
    AnimeClipCtrl(0x09, 0x0659, 0x00)
    AnimeClipCtrl(0x09, 0x065A, 0x00)
    AnimeClipCtrl(0x09, 0x065B, 0x00)
    AnimeClipCtrl(0x09, 0x065C, 0x00)
    AnimeClipCtrl(0x09, 0x065D, 0x00)
    Fade(0x6A, 300)
    ClearScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    OP_23(0x01, 0xFFFF, 0xFFFF, 0x00, 0x0A)
    SetScenaFlags(ScenaFlag(0x0064, 4, 0x324))
    ChrClearPhysicsFlags(ChrTable['騎神亞格里昂'], 0x00000040)
    ChrClearPhysicsFlags(ChrTable['鋼之雅里安洛德'], 0x00000040)
    OP_3A(0x06, 0x0001)
    SetChrPos(0xF011, 0.0, 0.0, 0.0, 0.0)
    EventJump(0x00000000)
    OP_14(0x04000000)

    Return()

# id: 0x002A offset: 0x1D990
@scena.AnimeClips('_EV_03_76_02')
def _EV_03_76_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr011_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom000.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom001.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr22_04.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000076F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000076F4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000755C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E89,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E8A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E8B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E8C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E8D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000765D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000765F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000756B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E8E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007562,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007565,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E8F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000770F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E90,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007569,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000756B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000770F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E91,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E92,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E93,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E94,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E95,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E96,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00008E97,
            name   = '',
        ),
    )

# id: 0x002B offset: 0x1DFE0
@scena.AnimeClips('_EV_03_80_01')
def _EV_03_80_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
    )

# id: 0x002C offset: 0x1E040
@scena.AnimeClips('_EV_03_80_02')
def _EV_03_80_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
    )

# id: 0x002D offset: 0x1E0A0
@scena.AnimeClips('_EV_03_81_00')
def _EV_03_81_00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc33_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc21_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc33_03.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr011_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc035_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr037_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr039_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr000_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr000_02_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr000_02_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc017_10_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr006_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk950_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr22_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000902C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000902D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000902E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000902F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009030,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009031,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009032,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009033,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009034,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009035,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009036,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009037,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009038,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009039,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000903A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000903B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000903C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000903D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000903E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000770F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000903F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009040,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009041,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009042,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009043,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009044,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009045,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009046,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009047,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009048,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007562,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007571,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009049,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000904A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000904B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000904C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000904D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000904E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000904F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009050,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009051,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009052,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007715,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009054,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007714,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000763C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009057,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009058,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009059,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000905A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000905B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000905C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BA,
            name   = '',
        ),
    )

# id: 0x002E offset: 0x1EE20
@scena.AnimeClips('_EV_03_81_01')
def _EV_03_81_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr22_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr22_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000905E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000905F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009060,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009061,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009062,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00002CF3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009064,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009065,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009066,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009067,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009068,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009069,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000906A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000906B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000906C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000906D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000906E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000906F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009070,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009071,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009072,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009073,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009074,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009075,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009076,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009077,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009078,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00002B60,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000763C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007737,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007593,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00002B0A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000907B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000907C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000907D,
            name   = '',
        ),
    )

# id: 0x002F offset: 0x1F490
@scena.AnimeClips('_EV_03_81_03')
def _EV_03_81_03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr011_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_08.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_04.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_07.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evcet_03.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/link_ring1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075CA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007724,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007612,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007594,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007599,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075E8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075E9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BC4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007631,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007715,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009084,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009085,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009086,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009087,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009088,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009089,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000908A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000908B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000908C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007597,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000759C,
            name   = '',
        ),
    )

# id: 0x0030 offset: 0x1FAB0
@scena.AnimeClips('_EV_03_81_04')
def _EV_03_81_04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr011_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs000_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs022_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rs022_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'M_V4000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'M_V4200',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001130,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001137,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000114F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000113D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000113E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001157,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007597,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000046A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00000A78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000759C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000094C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C9,
            name   = '',
        ),
    )

# id: 0x0031 offset: 0x1FED0
@scena.AnimeClips('_EV_03_81_05')
def _EV_03_81_05():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'M_V4000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'M_V4200',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007645,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007743,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00000A79,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000094D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001151,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075D2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075D2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000046B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000046C,
            name   = '',
        ),
    )

# id: 0x0032 offset: 0x20160
@scena.AnimeClips('_EV_03_81_06')
def _EV_03_81_06():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr00_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr011_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rc022_10_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007703,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000764A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007649,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000765D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007599,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000908D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000908E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000908F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009090,
            name   = '',
        ),
    )

# id: 0x0033 offset: 0x20460
@scena.AnimeClips('_EV_03_81_08')
def _EV_03_81_08():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evmm30_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom010.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc35_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc33_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc33_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/rc022_10_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/clitical.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr011_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr04_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr04_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr04_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evr04_03.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evbom001.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evret_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009094,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009095,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009096,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009097,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009098,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x00009099,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000909A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000909B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000909C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000909D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000909E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x0000909F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090A9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090AA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075A8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090AB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090AC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090AD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090AE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007737,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007613,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007544,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000087CD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B2,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0324,
            dword4 = 0x00000000,
            name   = 'evk1001',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000760D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000759D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0324,
            dword4 = 0x00000000,
            name   = 'evk1001',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007598,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007635,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075C8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000755C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000755B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000758C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B4,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000759C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B7,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000759A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007595,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007613,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007544,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090B9,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000770F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090BA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0007,
            type2  = 0xFFFF,
            dword4 = 0x000090BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BD,
            name   = '',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
