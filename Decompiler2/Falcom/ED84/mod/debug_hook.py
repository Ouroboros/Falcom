from Falcom.ED84.Parser.scena_writer_helper import *

def funcCallBack(name: str, f: Callable):
    match name:
        case _: pass

    pass

def runCallBack(g):
    from Falcom.ED84.Parser.scena_writer import _gScena as scena
    for f in [
        FC_ActMenu_Ouroboros,
    ]:
        scena.Code(f.__name__)(f)

def _init():
    from Falcom.ED84.Parser.scena_writer import _gScena as scena
    # scena.registerFuncCallback(funcCallBack)
    scena.registerRunCallback(runCallBack)

_init()

def getPartyList():
    from Falcom.ED84.Metadata.chrId_table import chrIdTable

    chrList = []

    for chrId, chrName in chrIdTable.items():
        if not isinstance(chrId, int):
            continue

        if chrId <= 0x28:   # 瑟蕾奴
            chrList.append((chrId, chrName))

    return sorted(chrList, key = lambda e: e[0])

def getBossList():
    return [
        (0x2000, '鋼之阿瑞安赫德'),
        (0x2001, '劫炎馬克邦'),
        (0x2002, '小丑肯帕雷拉'),
        (0x2003, '卡西烏斯中將'),
        (0x2004, '盟主'),

        (0x0069, '獵兵王路嘉'),
        (0x006D, '馬克邦魔神'),
        (0x0087, '賽德利克皇太子'),
        (0x008C, '黑之艾爾貝里希'),
        (0x0090, '奧斯本宰相'),
        (0x00EC, '瑪麗亞貝爾'),
    ]

def DebugMenu(menuVar):
    def allItems():
        AddItem(0x04, 0x0000, 10000)
        AddItem(0x07, 0x00F1, 10000)
        AddItem(0x07, 0x00F2, 10000)
        AddItem(0x07, 0x00F3, 10000)
        AddItem(0x07, 0x00F4, 10000)
        AddItem(0x07, 0x00F5, 10000)
        AddItem(0x07, 0x00F6, 10000)
        AddItem(0x07, 0x00F7, 10000)
        AddItem(0x07, 0x00F8, 10000)

        for i in range(0x80, 0xFF):
            AddItem(0x0F, i, 1000)

        # AddItem(0x0F, 0x0081, 900)
        # AddItem(0x0F, 0x008C, 900)
        # AddItem(0x0F, 0x00BE, 900)
        # AddItem(0x0F, 0x00BF, 900)
        # AddItem(0x0F, 0x00C0, 900)
        # AddItem(0x0F, 0x00C8, 900)

        AddItem(0x00, 0x0000, 900)
        AddItem(0x00, 0x0005, 900)
        AddItem(0x00, 0x000A, 900)
        AddItem(0x00, 0x003C, 900)
        AddItem(0x18, 0x0000, 900)

    ShowMenu(
        menuVar,
        1,
        ('SelectArea',          lambda: Call(ScriptId.Debug, 'SelectArea')),
        ('SelectFlag_System',   lambda: Call(ScriptId.Debug, 'SelectFlag_System')),
        ('SelectFlag',          lambda: Call(ScriptId.Debug, 'SelectFlag')),
        ('Mg01_Parts',          lambda: Call(ScriptId.Debug, 'Mg01_Parts')),
        ('AllItems',            allItems),
        fontSize = 33.0,
    )

def ChangeModelMenu(menuVar):
    def doChange(chrId: int, targetChrId: int):
        DebugString(f'ModelSetBattleStyle(0x{chrId:X}, 0x{targetChrId:X})')
        ModelSetBattleStyle(chrId, targetChrId)
        ModelSetChrId(chrId, targetChrId)
        # AnimeClipRefreshSkin(chrId)

    def restore():
        for chrId, _ in getPartyList():
            ModelSetBattleStyle(chrId, 0)
            # AnimeClipRefreshSkin(chrId)

    def showBossMenu(chrId: int, chrName: str):
        DebugString(f'替换 0x{chrId:X}')

        OP_23(0x05, 0xFFFF, 100, 0xFFFF, 0xFFFF, 0x00)

        Talk(
            0xFFFF,
            (
                0xB,
                TxtCtl.ShowAll,
                f'要把 {chrName} 替换成',
                # TxtCtl.Enter,
            ),
        )

        items = []
        for bossChrId, bossName in getBossList():
            items.append((
                f'{bossName} (0x{bossChrId:04X})', wrapper(doChange, chrId, bossChrId),
            ))

        ShowMenu(
            menuVar + 1,
            2,
            *items,
            autoExit = True,
            fontSize = 33.0,
            pos = (-1, 230),
            height = 25,
        )

        OP_25(0x00)
        OP_25(0x01)
        OP_23(0x05, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0x00)

    def wrapper(f, *args, **kwargs):
        return lambda: f(*args, **kwargs)

    items = []

    for chrId, chrName in getPartyList():
        items.append((
            f'{chrName}', wrapper(showBossMenu, chrId, chrName),
        ))

    items.append(('全部还原', lambda: restore()))

    ShowMenu(
        menuVar,
        1,
        *items,
        fontSize = 33.0,
        pos = (500, 24),
        height = 25,
    )

    FormationCmd(0x1B, 0x01)
    FormationCmd(0x1C, 0x01)

def FC_ActMenu_Ouroboros():
    def showDebugMenu():
        DebugMenu(0xF7)

    def showChangeModelMenu():
        ChangeModelMenu(0xF7)

    Call(ScriptId.Debug, 'BeginDebugScript')

    ShowMenu(
        0xF6,
        0,
        ('换人',        showChangeModelMenu),
        ('DEBUG菜单',   showDebugMenu),
        fontSize = 33.0,
    )

    Call(ScriptId.Debug, 'EndDebugScript')

    return Return()
