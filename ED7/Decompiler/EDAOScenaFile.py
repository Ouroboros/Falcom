from ScenarioScript import *
from Instruction.ScenaOpTableEDAO import *
from GameData.ItemNameMap import *

def plog(*value, sep = ' ', end = '\n', file = sys.stdout, flush = False):
    pass

#plog = print

def VerifyTupleOrList(param):
    if not IsTupleOrList(param):
        raise Exception('accept tuple or list only')

class ScenarioInfoPort(ScenarioInfo):
    def __init__(self):
        super().__init__()

        self.fs                 = None
        self.Labels             = {}    # map<name, offset>
        self.StringListTable    = {}    # map<string_list_item, offset>
        self.DelayFixLabels     = []    # list of LabelEntry
        self.DelayFixString     = []    # list of LabelEntry
        self.PrevousHandlerData = None

        self.ScpFunctionList    = []

scena = ScenarioInfoPort()

def CreateScenaFile(FileName, MapName, Location, MapIndex, MapDefaultBGM, Flags, IncludeList, Unknown_4A, PreInitFunctionIndex, Unknown_51, InitData):
    scena.MapName               = MapName
    scena.Location              = Location
    scena.MapIndex              = MapIndex
    scena.MapDefaultBGM         = BGMFileIndex(MapDefaultBGM)
    scena.Flags                 = Flags
    scena.IncludedScenario      = list(IncludeList)
    scena.Unknown_4A            = Unknown_4A
    scena.PreInitFunctionIndex  = PreInitFunctionIndex
    scena.Unknown_51            = Unknown_51

    if type(InitData) == bytes:
        InitData = ScenarioInitData(fileio.FileStream(InitData))
    elif IsTupleOrList(InitData):
        InitData = ScenarioInitData(InitData)
    else:
        raise Exception('unknown InitData type: %s' % type(InitData))


    scena.InitData = InitData

    if len(IncludeList) != 6:
        raise Exception('incorrect include list length')

    for i in range(len(IncludeList)):
        scena.IncludedScenario[i] = ScenarioFileIndex(IncludeList[i]).Index()

    scena.fs = fileio.FileStream(FileName, 'wb+')
    scena.fs.seek(0x94)

    pos = scena.fs.tell()

    scena.ChipFrameInfoOffset = pos
    scena.PlaceNameOffset = pos

    for i in range(SCN_INFO_MAXIMUM):
        scena.ScnInfoOffset[i] = pos
        scena.ScnInfoNumber[i] = 0

def BuildStringList(strlist):
    scena.StringTable = list(strlist)

def AddStringToStringList(string, offset):
    scena.DelayFixString.append(LabelEntry(string, offset))
    if string not in scena.StringTable:
        scena.StringTable.append(string)

def AddScnInfo(index):
    if len(scena.ScnInfo[index]) == 0:
        scena.ScnInfo[index].append(0)
        scena.ScnInfoOffset[index] = scena.fs.tell()

    scena.ScnInfoNumber[index] += 1

def label(labelname):
    pos = scena.fs.tell()
    if scena.PrevousHandlerData is not None:
        pos += scena.PrevousHandlerData.FileStream.tell()

    plog('%08X: %s' % (pos, labelname))
    if labelname in scena.Labels and scena.Labels[labelname] != pos:
        raise Exception('label name conflict')

    scena.Labels[labelname] = pos

def getlabel(name):
    return scena.Labels[name]

def ATBonus(name, Nothing, HP_HEAL_10, HP_HEAL_50, EP_HEAL_10, EP_HEAL_50, CP_HEAL_10, CP_HEAL_50, SEPITH, CRITICAL, VANISH, DEATH, GUARD, RUSH, ARTS_GUARD, TEAMRUSH, Unknown):
    label(name)

    atbonus = BattleATBonus()

    atbonus.Nothing     = Nothing
    atbonus.HP_HEAL_10  = HP_HEAL_10
    atbonus.HP_HEAL_50  = HP_HEAL_50
    atbonus.EP_HEAL_10  = EP_HEAL_10
    atbonus.EP_HEAL_50  = EP_HEAL_50
    atbonus.CP_HEAL_10  = CP_HEAL_10
    atbonus.CP_HEAL_50  = CP_HEAL_50
    atbonus.SEPITH      = SEPITH
    atbonus.CRITICAL    = CRITICAL
    atbonus.VANISH      = VANISH
    atbonus.DEATH       = DEATH
    atbonus.GUARD       = GUARD
    atbonus.RUSH        = RUSH
    atbonus.ARTS_GUARD  = ARTS_GUARD
    atbonus.TEAMRUSH    = TEAMRUSH
    atbonus.Unknown     = Unknown

    scena.fs.write(atbonus.binary())

def Sepith(name, v1, v2, v3, v4, v5, v6, v7):
    label(name)

    sepith = BattleSepith()
    sepith.Value[0] = v1
    sepith.Value[1] = v2
    sepith.Value[2] = v3
    sepith.Value[3] = v4
    sepith.Value[4] = v5
    sepith.Value[5] = v6
    sepith.Value[6] = v7

    buf = sepith.binary()
    buf += b'\x00' * (16 - len(buf) % 16)

    scena.fs.write(buf)

def MonsterBattlePostion(name, x, y, degree):
    label(name)

    monpos = BattleMonsterPostion()
    monpos.X        = x
    monpos.Y        = y
    monpos.Degree   = degree

    scena.fs.write(monpos.binary())

def BattleInfo(name, Flags, Level, Unknown_04, Vision, MoveRange, CanMove, MoveSpeed, Unknown_0A, BattleMap, SepithName, Probability1, Probability2, Probability3, Probability4, BattleMonsterInfoList):
    label(name)

    btinfo = ScenarioBattleInfo()

    probability = [ Probability1, Probability2, Probability3, Probability4 ]

    btinfo.Flags            = Flags
    btinfo.Level            = Level
    btinfo.Unknown_04       = Unknown_04
    btinfo.Vision           = Vision
    btinfo.MoveRange        = MoveRange
    btinfo.CanMove          = CanMove
    btinfo.MoveSpeed        = MoveSpeed
    btinfo.Unknown_0A       = Unknown_0A
    btinfo.BattleMapOffset  = INVALID_OFFSET
    btinfo.SepithOffset     = 0 if SepithName == 0 else getlabel(SepithName)
    btinfo.Probability      = probability

    scena.fs.write(btinfo.binary())

    AddStringToStringList(BattleMap, scena.fs.tell() - 0xC)

    for i in range(len(probability)):
        if probability[i] == 0:
            continue

        btmon = BattleMonsterInfoList[i]

        btmoninfo = BattleMonsterInfo()

        # error if not >= 8
        for i in range(len(btmoninfo.MsFileIndex)):
            btmoninfo.MsFileIndex[i] = BattleScriptFileIndex(btmon[i])

        normalpos   = btmon[8]
        enemyadvpos = btmon[9]
        normalbgm   = int(os.path.splitext(btmon[10])[0][3:], 10)
        dangerbgm   = int(os.path.splitext(btmon[11])[0][3:], 10)
        atbonus     = btmon[12]

        btmoninfo.PositionNormalOffset          = getlabel(normalpos)
        btmoninfo.PositionEnemyAdvantageOffset  = getlabel(enemyadvpos)
        btmoninfo.BgmNormal                     = normalbgm
        btmoninfo.BgmDanger                     = dangerbgm
        btmoninfo.ATBonusOffset                 = getlabel(atbonus)

        scena.fs.write(btmoninfo.binary())

def AddCharChip(chipindexlist):

    VerifyTupleOrList(chipindexlist)

    scena.ScnInfoOffset[SCN_INFO_CHIP] = scena.fs.tell()
    scena.ScnInfoNumber[SCN_INFO_CHIP] = len(chipindexlist)

    plog('chip index: %X' % scena.fs.tell())

    for chip in chipindexlist:
        chip = ScenarioChipInfo(chip)
        scena.fs.write(chip.binary())

def DeclNpc(X, Z, Y, Direction, Unknown2, ChipIndex, Unknown_11, NpcIndex, Unknown_14, InitScenaIndex, InitFunctionIndex, TalkScenaIndex, TalkFunctionIndex, Unknown4, Unknown5):

    AddScnInfo(SCN_INFO_NPC)

    npcinfo = ScenarioNpcInfo()

    npcinfo.X                  = X
    npcinfo.Z                  = Z
    npcinfo.Y                  = Y
    npcinfo.Direction          = Direction
    npcinfo.Unknown2           = Unknown2

    npcinfo.ChipIndex          = ChipIndex
    npcinfo.Unknown_11         = Unknown_11
    npcinfo.NpcIndex           = NpcIndex
    npcinfo.Unknown_14         = Unknown_14

    npcinfo.InitScenaIndex     = InitScenaIndex
    npcinfo.InitFunctionIndex  = InitFunctionIndex
    npcinfo.TalkScenaIndex     = TalkScenaIndex
    npcinfo.TalkFunctionIndex  = TalkFunctionIndex
    npcinfo.Unknown4           = Unknown4
    npcinfo.Unknown5           = Unknown5

    scena.fs.write(npcinfo.binary())

def DeclMonster(X, Z, Y, Unknown_0C, BattleInfoName, Unknown_12, ChipIndex, Unknown_16, StandFrameInfoIndex, MoveFrameInfoIndex):

    AddScnInfo(SCN_INFO_MONSTER)

    moninfo = ScenarioMonsterInfo()

    moninfo.X                   = X
    moninfo.Z                   = Z
    moninfo.Y                   = Y
    moninfo.Unknown_0C          = Unknown_0C
    moninfo.BattleInfoOffset    = getlabel(BattleInfoName)
    moninfo.Unknown_12          = Unknown_12
    moninfo.ChipIndex           = ChipIndex
    moninfo.Unknown_16          = Unknown_16
    moninfo.StandFrameInfoIndex = StandFrameInfoIndex
    moninfo.MoveFrameInfoIndex  = MoveFrameInfoIndex

    scena.fs.write(moninfo.binary())

def DeclEvent(Flags, ScenaIndex, FunctionIndex, X, Y, Z, Range, UnknownFloat_10):

    VerifyTupleOrList(UnknownFloat_10)

    if len(UnknownFloat_10) != 0x10:
        raise Exception('length not 0x10')

    AddScnInfo(SCN_INFO_EVENT)

    ev = ScenarioEventInfo()

    ev.X                = float(X)
    ev.Y                = float(Y)
    ev.Z                = float(Z)
    ev.Range            = float(Range)
    ev.UnknownFloat_10  = UnknownFloat_10
    ev.Flags            = Flags
    ev.ScenaIndex       = ScenaIndex
    ev.FunctionIndex    = FunctionIndex

    scena.fs.write(ev.binary())


def DeclActor(TriggerX, TriggerZ, TriggerY, TriggerRange, ActorX, ActorZ, ActorY, Flags, TalkScenaIndex, TalkFunctionIndex, Unknown_22):

    AddScnInfo(SCN_INFO_ACTOR)

    actor = ScenarioActorInfo()

    actor.TriggerX          = TriggerX
    actor.TriggerZ          = TriggerZ
    actor.TriggerY          = TriggerY
    actor.TriggerRange      = TriggerRange
    actor.ActorX            = ActorX
    actor.ActorZ            = ActorZ
    actor.ActorY            = ActorY
    actor.Flags             = Flags
    actor.TalkScenaIndex    = TalkScenaIndex
    actor.TalkFunctionIndex = TalkFunctionIndex
    actor.Unknown_22        = Unknown_22

    scena.fs.write(actor.binary())

def ScpFunction(FunctionList):

    if not IsTupleOrList(FunctionList):
        raise Exception('accept function list only')

    scena.ScenaFunctionTable.Offset = scena.fs.tell()
    scena.ScenaFunctionTable.Size += len(FunctionList) * 4

    for func in FunctionList:
        scena.DelayFixLabels.append(LabelEntry(func, scena.fs.tell()))
        scena.ScpFunctionList.append(func)
        scena.fs.write(struct.pack('<I', INVALID_OFFSET))


def GetFuntionId(FunctionLabel):
    return scena.ScpFunctionList.index(FunctionLabel)

def PlaceName(X, Z, Y, Flags1, Flags2, Name):

    if len(scena.PlaceName) == 0:
        scena.PlaceName.append(0)
        scena.PlaceNameOffset = scena.fs.tell()

    scena.PlaceNameNumber += 1

    place = ScenarioPlaceNameInfo()

    place.X             = X
    place.Z             = Z
    place.Y             = Y
    place.Flags1        = Flags1
    place.Flags2        = Flags2
    place.NameOffset    = INVALID_OFFSET

    scena.fs.write(place.binary())

    AddStringToStringList(Name, scena.fs.tell() - 4)

def ChipFrameInfo(speed, reserve, subchipindexlist = None):

    if len(scena.ChipFrameInfo) == 0:
        scena.ChipFrameInfo.append(0)
        scena.ChipFrameInfoOffset = scena.fs.tell()

    if subchipindexlist == None:
        subchipindexlist = []

    frame = ScenarioChipFrameInfo()

    frame.Speed         = speed
    frame.Reserve       = reserve
    frame.SubChipCount  = len(subchipindexlist)
    frame.SubChipIndex  = list(subchipindexlist)

    scena.fs.write(frame.binary())

for op, inst in edao.edao_op_table.items():

    func = []
    func.append('def %s(*args):' % inst.OpName)
    func.append('    return OpCodeHandler(0x%02X, args)' % inst.OpCode)
    func.append('')

    exec('\r\n'.join(func))

    opx = 'OP_%02X' % inst.OpCode

    if inst.OpName != opx:
        func[0] = 'def %s(*args):' % opx
        exec('\r\n'.join(func))

def AssembleForExec(expr):
    return eval(expr)

def OpCodeHandler(op, args):
    entry = edao.edao_op_table[op]

    data = HandlerData(HANDLER_REASON_ASSEMBLE)
    data.Instruction    = Instruction(op)
    data.Arguments      = list(args)
    data.TableEntry     = entry
    data.Assemble       = AssembleForExec

    data.Instruction.OperandFormat = entry.Operand

    UsePrevous = bool(scena.PrevousHandlerData != None)

    if UsePrevous:
        data.FileStream = scena.PrevousHandlerData.FileStream
        data.Instruction.Labels = scena.PrevousHandlerData.Instruction.Labels
    else:
        data.FileStream = fileio.FileStream(b'')
        scena.PrevousHandlerData = data

    #print(entry.OpName)
    inst = OpCodeHandlerPrivate(data)

    if UsePrevous:
        return inst

    scena.PrevousHandlerData = None

    offset = scena.fs.tell()
    for lb in inst.Labels:
        scena.DelayFixLabels.append(LabelEntry(lb.Label, lb.Offset + offset))

    data.FileStream.seek(0)
    scena.fs.write(data.FileStream.read())

    return inst

def scpexpr(operation, *args):
    return ScpExpression(operation, list(args))

def scpstr(ctrlcode, value = None):
    if type(ctrlcode) == str:
        return ctrlcode

    if ctrlcode == SCPSTR_CODE_ITEM and type(value) == str:
        value = ItemTrueNameMap[value]

    ScpStrCtrlCode = \
    {
        SCPSTR_CODE_COLOR       : lambda : '\\x%02X\\x%02X' % (ctrlcode, value),
        SCPSTR_CODE_LINE_FEED   : lambda : '\\x%02X' % (ctrlcode),
        0x0A                    : lambda : '\\x%02X' % (ctrlcode),
        SCPSTR_CODE_ENTER       : lambda : '\\x%02X' % (ctrlcode),
        SCPSTR_CODE_CLEAR       : lambda : '\\x%02X' % (ctrlcode),
        0x04                    : lambda : '\\x%02X' % (ctrlcode),
        0x05                    : lambda : '\\x%02X' % (ctrlcode),
        0x06                    : lambda : '\\x%02X' % (ctrlcode),
        0x09                    : lambda : '\\x%02X' % (ctrlcode),
        0x18                    : lambda : '\\x%02X' % (ctrlcode),
        SCPSTR_CODE_ITEM        : lambda : '\\x%02X\\x%02X\\x%02X' % (ctrlcode, value & 0xFF, value >> 8),
    }

    string = ScpStrCtrlCode[ctrlcode]()

    string = eval('b"%s"' % string)

    return string

def SaveToFile():
    fs = scena.fs

    fs.write(b'\x00' * (16 - fs.tell() % 16))

    scena.StringTableOffset = fs.tell()
    for string in scena.StringTable:
        plog('%s <--> %X' % (string, fs.tell()))

        scena.StringListTable[string] = fs.tell()
        fs.write(string.encode(CODE_PAGE) + b'\x00')

    zerostr = fs.tell() - 1

    for lb in scena.DelayFixLabels:
        fs.seek(lb.Offset)
        fs.WriteULong(getlabel(lb.Label))

    for lb in scena.DelayFixString:
        fs.seek(lb.Offset)
        pos = zerostr if lb.Label == '' else scena.StringListTable[lb.Label]

        plog('%X -> %X : %s' % (lb.Offset, pos, lb.Label))

        fs.WriteULong(pos)

    for i in range(len(scena.ScnInfoOffset)):
        plog('%04X : %02X' % (scena.ScnInfoOffset[i], scena.ScnInfoNumber[i]))

    fs.seek(0)
    fs.write(scena.binary())

    print('done')

    #input()
