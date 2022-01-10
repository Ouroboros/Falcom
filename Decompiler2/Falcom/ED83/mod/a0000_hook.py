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
    FormationAddMember(0x00)
    FormationAddMember(0x05)
    # FormationAddMember(0x0C)
    # FormationAddMember(0x10)
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
    #     SetBattleStyle(chrid, 0)

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

    return Return()

    SetScenaFlags(ScenaFlag(0x016F, 7, 0xB7F))
    SetScenaFlags(ScenaFlag(0x016F, 6, 0xB7E))
    SetScenaFlags(ScenaFlag(0x016F, 5, 0xB7D))
    SetScenaFlags(ScenaFlag(0x016F, 4, 0xB7C))
    SetScenaFlags(ScenaFlag(0x016F, 3, 0xB7B))
    SetScenaFlags(ScenaFlag(0x016F, 2, 0xB7A))
    SetScenaFlags(ScenaFlag(0x016F, 1, 0xB79))
    SetScenaFlags(ScenaFlag(0x016F, 0, 0xB78))
    SetScenaFlags(ScenaFlag(0x016E, 7, 0xB77))
    SetScenaFlags(ScenaFlag(0x016E, 6, 0xB76))
    SetScenaFlags(ScenaFlag(0x016E, 5, 0xB75))
    SetScenaFlags(ScenaFlag(0x016E, 4, 0xB74))
    SetScenaFlags(ScenaFlag(0x016E, 3, 0xB73))
    SetScenaFlags(ScenaFlag(0x018E, 2, 0xC72))
    SetScenaFlags(ScenaFlag(0x018E, 1, 0xC71))
    SetScenaFlags(ScenaFlag(0x016E, 2, 0xB72))
    SetScenaFlags(ScenaFlag(0x016E, 1, 0xB71))
    SetScenaFlags(ScenaFlag(0x016E, 0, 0xB70))
    SetScenaFlags(ScenaFlag(0x016D, 7, 0xB6F))
    SetScenaFlags(ScenaFlag(0x016D, 6, 0xB6E))
    SetScenaFlags(ScenaFlag(0x016D, 5, 0xB6D))
    SetScenaFlags(ScenaFlag(0x016D, 4, 0xB6C))
    SetScenaFlags(ScenaFlag(0x018E, 6, 0xC76))
    SetScenaFlags(ScenaFlag(0x016D, 3, 0xB6B))
    SetScenaFlags(ScenaFlag(0x016D, 2, 0xB6A))
    SetScenaFlags(ScenaFlag(0x016D, 1, 0xB69))
    SetScenaFlags(ScenaFlag(0x016D, 0, 0xB68))
    SetScenaFlags(ScenaFlag(0x016C, 7, 0xB67))
    SetScenaFlags(ScenaFlag(0x016C, 6, 0xB66))
    SetScenaFlags(ScenaFlag(0x016C, 5, 0xB65))
    SetScenaFlags(ScenaFlag(0x016C, 4, 0xB64))
    SetScenaFlags(ScenaFlag(0x016C, 3, 0xB63))
    SetScenaFlags(ScenaFlag(0x016C, 2, 0xB62))
    SetScenaFlags(ScenaFlag(0x016C, 1, 0xB61))
    SetScenaFlags(ScenaFlag(0x016C, 0, 0xB60))
    SetScenaFlags(ScenaFlag(0x016B, 7, 0xB5F))
    SetScenaFlags(ScenaFlag(0x016B, 6, 0xB5E))
    SetScenaFlags(ScenaFlag(0x016B, 5, 0xB5D))
    SetScenaFlags(ScenaFlag(0x016B, 4, 0xB5C))
    SetScenaFlags(ScenaFlag(0x016B, 4, 0xB5C))
    SetScenaFlags(ScenaFlag(0x016B, 2, 0xB5A))
    SetScenaFlags(ScenaFlag(0x016B, 1, 0xB59))
    SetScenaFlags(ScenaFlag(0x016B, 0, 0xB58))
    SetScenaFlags(ScenaFlag(0x016A, 7, 0xB57))
    SetScenaFlags(ScenaFlag(0x016A, 6, 0xB56))
    SetScenaFlags(ScenaFlag(0x016A, 5, 0xB55))
    SetScenaFlags(ScenaFlag(0x016A, 4, 0xB54))

    ClearScenaFlags(ScenaFlag(0x0072, 4, 0x394))

    OP_18(
        0xF9,
        (
            (Expr.Expr23, 0xF7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    loc_413E6 = genLabel()

    If(
        (
            (Expr.Expr23, 0xF9),
            (Expr.PushLong, 0x30C3),
            Expr.Gtr,
            Expr.Return,
        ),
        loc_413E6,
    )

    OP_18(
        0xF9,
        (
            (Expr.PushLong, 0x30C3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    label(loc_413E6)

    # EventJump(0x00003123)
    EventJump(0x3140)
    OP_14(0x04000000)

    Return()
