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
    import system_hook
    system_hook.FC_ActMenu_Ouroboros()
    Return()

def TK_MiniGame_Debug():
    PlayBGM(922, 1.0, 0x0000, 0x00000000, 0x00)
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

    # FormationReset(0)
    # FormationAddMember(0x00)
    # FormationSetLeader(0)

    # SetScenaFlags(ScenaFlag(0x00BA, 1, 0x5D1))
    # SetScenaFlags(ScenaFlag(0x0076, 0, 0x3B0))
    # ClearScenaFlags(ScenaFlag(0x0076, 0, 0x3B0))
    ClearScenaFlags(ScenaFlag(0x0077, 7, 0x3BF))
    # ClearScenaFlags(ScenaFlag(0x0076, 0, 0x3B0))
    # ClearScenaFlags(0xFFFF)

    # Call(ScriptId.System, 'FC_EVENT_NEXT', (0xFF, 0x19, 0x0))
    Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)
    # Battle(0x00, 0x00000005, 0x00, 0x00, 0x00000005, 0x01, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    return Return()
