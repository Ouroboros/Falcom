from Falcom.ED83.Parser.scena_writer_helper import *

def funcCallBack(name: str, f: Callable):
    match name:
        case 'TK_MiniGame_Debug': return TK_MiniGame_Debug
        case _: pass

    pass

def _init():
    from Falcom.ED83.Parser.scena_writer import _gScena as scena
    scena.registerFuncCallback(funcCallBack)

_init()

def TK_MiniGame_Debug():
    off = genLabel()
    end = genLabel()

    chrmap = {
        ChrTable['黎恩']: 0x2000,
        # ChrTable['悠娜']: 0x2001,
    }

    FormationReset()
    FormationAddMember(0)
    FormationSetLeader(0)
    # FormationAddMember(0xA)

    # CraftCtrl(0x00, ChrTable['黎恩'], 0xD4B)
    # CraftCtrl(0x04, ChrTable['黎恩'], 0xD4B)
    # SetChrModelChrId(ChrTable['黎恩'], ChrTable['黎恩'])
    # SetBattleStyle(ChrTable['黎恩'], ChrTable['黎恩'])
    # ChrRefreshSkin(0)

    # flag = ScenaFlag(0x00A7, 0, 0x538)

    # If(
    #     (
    #         (Expr.TestScenaFlags, flag),
    #         Expr.Return,
    #     ),
    #     off,
    # )

    # ClearScenaFlags(flag)

    # for chrid in chrmap.keys():
    #     SetChrModelChrId(chrid, chrid)
    #     SetBattleStyle(chrid, chrid)

    # Jump(end)

    # label(off)
    # SetScenaFlags(flag)
    # for id1, id2 in chrmap.items():
    #     SetChrModelChrId(id1, id2)
    #     SetBattleStyle(id1, id2)

    # label(end)

    # for chrid in chrmap.keys():
    #     ChrRefreshSkin(chrid)

    SetScenaFlags(ScenaFlag(0x0080, 0, 0x400))
    SetScenaFlags(ScenaFlag(0x0080, 1, 0x401))
    SetScenaFlags(ScenaFlag(0x0080, 2, 0x402))
    Battle(0x00, 0x00000005, 0x00, 0x00, 0xFFFFFFFF, 0x00, 0xFFFFFFFF, 0x00)

    Return()

    return