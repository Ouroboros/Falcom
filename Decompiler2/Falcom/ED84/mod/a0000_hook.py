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

def TK_MiniGame_Debug():
    chrmap = {
        ChrTable['黎恩']: ChrTable['鋼之阿瑞安赫德'],
    }

    FormationReset(0)
    FormationAddMember(0x00)
    # FormationAddMember(0x05)
    # FormationAddMember(0x0C)
    # FormationAddMember(0x10)
    FormationSetLeader(0)
    # FormationAddMember(0xA)

    for chrid, newchrid in chrmap.items():
        notset = genLabel()
        end = genLabel()

        If(
            (
                (Expr.Eval, f'ModelGetBattleStyle({chrid})'),
                (Expr.PushLong, 0x2000),
                Expr.Lss,
                Expr.Return,
            ),
            notset,
        )

        ModelSetChrId(chrid, newchrid)
        ModelSetBattleStyle(chrid, 0)

        Jump(end)

        label(notset)

        ModelSetChrId(chrid, chrid)
        ModelSetBattleStyle(chrid, 0)

        label(end)

        AnimeClipRefreshSkin(chrid)

    Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    return Return()
