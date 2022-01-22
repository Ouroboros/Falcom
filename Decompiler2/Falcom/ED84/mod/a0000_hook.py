from Falcom.ED84.Parser.scena_writer_helper import *

def funcCallBack(name: str, f: Callable):
    match name:
        case 'TK_MiniGame_Debug': return TK_MiniGame_Debug
        case _: pass

    pass

def _init():
    from Falcom.ED84.Parser.scena_writer import _gScena as scena
    scena.registerFuncCallback(funcCallBack)

_init()

def test_menu():
    import debug_hook
    debug_hook.FC_ActMenu_Ouroboros()

def TK_MiniGame_Debug():
    PlayBGM(922, 1.0, 0x0000, 0x00000000, 0x00)
    # BGMCtrl(0x03, 1.0, 500, 0x00)
    # return test_menu()

    chrmap = {
        ChrTable['黎恩']: 0x2002,
    }

    # for chrid, newchrid in chrmap.items():
    #     notset = genLabel()
    #     end = genLabel()

    #     If(
    #         (
    #             (Expr.Eval, f'ModelGetBattleStyle({chrid})'),
    #             # (Expr.PushLong, 0),
    #             # Expr.Equ,
    #             Expr.Ez,
    #             Expr.Return,
    #         ),
    #         notset,
    #     )

    #     DebugString('set chrid')

    #     ModelSetChrId(chrid, newchrid)
    #     ModelSetBattleStyle(chrid, newchrid)

    #     Jump(end)

    #     label(notset)

    #     DebugString('unset chrid')

    #     ModelSetChrId(chrid, chrid)
    #     ModelSetBattleStyle(chrid, 0)

    #     label(end)

    #     AnimeClipRefreshSkin(chrid)

    # Call(ScriptId.Debug, 'EV_Party_Set', (0xFF, 0x1, 0x0))



    # Call(ScriptId.System, 'FC_TSMenu_Reset')
    # OP_C4(0x02, 0x00, ChrTable['黎恩'])
    # OP_C4(0x02, 0x01, ChrTable['尤娜'])
    # OP_C4(0x02, 0x01, ChrTable['庫爾特'])
    # OP_C4(0x02, 0x01, ChrTable['亞爾緹娜'])
    # OP_C4(0x02, 0x01, ChrTable['繆潔'])
    # OP_C4(0x02, 0x01, ChrTable['亞修'])
    # OP_C4(0x02, 0x01, ChrTable['亞莉莎'])
    # OP_C4(0x02, 0x01, ChrTable['艾略特'])
    # OP_C4(0x02, 0x01, ChrTable['勞拉'])
    # OP_C4(0x02, 0x02, ChrTable['馬奇亞斯'])
    # OP_C4(0x02, 0x02, ChrTable['艾瑪'])
    # OP_C4(0x02, 0x02, ChrTable['尤西斯'])
    # OP_C4(0x02, 0x02, ChrTable['菲'])
    # OP_C4(0x02, 0x02, ChrTable['蓋烏斯'])
    # OP_C4(0x02, 0x02, ChrTable['莎拉'])
    # OP_C4(0x02, 0x02, ChrTable['克洛'])
    # OP_C4(0x02, 0x02, ChrTable['杜巴莉'])
    # OP_C4(0x02, 0x03, ChrTable['安潔莉卡'])
    # OP_C4(0x02, 0x03, ChrTable['提妲'])
    # OP_C4(0x02, 0x03, ChrTable['蘭迪'])
    # OP_C4(0x02, 0x03, ChrTable['雪倫'])
    # # MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    # SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    # ExecExpressionWithVar(
    #     0x2B,
    #     (
    #         (Expr.PushLong, 0x7),
    #         Expr.Nop,
    #         Expr.Return,
    #     ),
    # )

    # ExecExpressionWithVar(
    #     0x2C,
    #     (
    #         (Expr.PushLong, 0x8),
    #         Expr.Nop,
    #         Expr.Return,
    #     ),
    # )

    # ExecExpressionWithVar(
    #     0x2D,
    #     (
    #         (Expr.PushLong, 0x8),
    #         Expr.Nop,
    #         Expr.Return,
    #     ),
    # )

    # ExecExpressionWithVar(
    #     0x2E,
    #     (
    #         (Expr.PushLong, 0x4),
    #         Expr.Nop,
    #         Expr.Return,
    #     ),
    # )

    # OP_C5(0x00, 0x01, 0x00)
    # OP_C5(0x01)
    # Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')

    # FormationReset(0x00)
    # OP_C4(0x01, 0x00)

    # FormationReset(0)
    # FormationAddMember(0)
    # FormationSetLeader(0)

    FormationCtrl(0x18)

    # FormationCtrl(0x11, 0xF000)
    # FormationCtrl(0x11, 0xF001)
    # FormationCtrl(0x11, 0xF002)
    # FormationCtrl(0x11, 0xF003)

    for i in range(0x40):
        FormationCtrl(0x11, i)

    Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)
    # Battle(0x01, 0x00000005, 0x00, 0x00, 0x0000, 0x0001, 0x0002, 0x0003)

    return Return()
