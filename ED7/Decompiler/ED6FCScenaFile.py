from ED6FCScenarioScript import *
from Instruction.ScenaOpTableED6FC import *
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

scena = None

def CreateScenaFile(
        FileName,
        MapName,
        Location,
        MapIndex,
        MapDefaultBGM,
        Flags,
        EntryFunctionIndex,
        Reserved,
        IncludedScenario,
    ):

    global scena

    scena = ScenarioInfoPort()

    scena.MapName               = MapName
    scena.Location              = Location
    scena.MapIndex              = MapIndex
    scena.MapDefaultBGM         = BGMFileIndex(MapDefaultBGM)
    scena.Flags                 = Flags
    scena.EntryFunctionIndex    = EntryFunctionIndex
    scena.Reserved              = Reserved

    if len(IncludedScenario) > NUMBER_OF_INCLUDE_FILE:
        raise Exception('incorrect include list length')

    while len(IncludedScenario) < NUMBER_OF_INCLUDE_FILE:
        IncludedScenario.append('')

    scena.IncludedScenario = [ScenarioFileIndex(scp).Index() for scp in IncludedScenario]

    scena.fs = fileio.FileStream(FileName, 'wb+')
    scena.fs.seek(0x64)

    updateScnInfoOffset(-1)

def BuildStringList(*strlist):
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

def AddCharChip(*chips):
    scena.ScnInfoOffset[SCN_INFO_CHIP] = scena.fs.tell()
    scena.ScnInfoNumber[SCN_INFO_CHIP] = len(chips)

    plog('chip index: %X' % scena.fs.tell())

    for chip in chips:
        chip = ScenarioChipInfo(chip)
        scena.fs.write(chip.binary())

    scena.fs.WriteByte(0xFF)

    updateScnInfoOffset(SCN_INFO_CHIP_PAT)

def AddCharChipPat(*pats):
    scena.ScnInfoOffset[SCN_INFO_CHIP_PAT] = scena.fs.tell()
    scena.ScnInfoNumber[SCN_INFO_CHIP_PAT] = len(pats)

    plog('chip index: %X' % scena.fs.tell())

    for chip in pats:
        chip = ScenarioChipInfo(chip)
        scena.fs.write(chip.binary())

    scena.fs.WriteByte(0xFF)

    updateScnInfoOffset(SCN_INFO_CHIP_PAT)

def declImpl(type, kwargs):
    obj = type()

    for k, v in kwargs.items():
        getattr(obj, k)
        setattr(obj, k, v)

    scena.fs.write(obj.binary())

def updateScnInfoOffset(current):
    scena.HeaderEndOffset = scena.fs.tell()
    for i in range(current + 1, SCN_INFO_MAXIMUM):
        scena.ScnInfoOffset[i] = scena.HeaderEndOffset

def DeclEntryPoint(**kwargs):
    declImpl(ScenarioEntryPoint, kwargs)
    updateScnInfoOffset(-1)

def DeclNpc(**kwargs):
    AddScnInfo(SCN_INFO_NPC)
    declImpl(ScenarioNpcInfo, kwargs)
    updateScnInfoOffset(SCN_INFO_NPC)

def DeclMonster(**kwargs):
    AddScnInfo(SCN_INFO_MONSTER)
    declImpl(ScenarioMonsterInfo, kwargs)
    updateScnInfoOffset(SCN_INFO_MONSTER)

def DeclEvent(**kwargs):
    AddScnInfo(SCN_INFO_EVENT)
    declImpl(ScenarioEventInfo, kwargs)
    updateScnInfoOffset(SCN_INFO_EVENT)

def DeclActor(**kwargs):
    AddScnInfo(SCN_INFO_ACTOR)
    declImpl(ScenarioActorInfo, kwargs)
    updateScnInfoOffset(SCN_INFO_ACTOR)

def ScpFunction(*FunctionList):
    scena.ScenaFunctionTable.Offset = scena.fs.tell()
    scena.ScenaFunctionTable.Size += len(FunctionList) * 4

    for func in FunctionList:
        scena.ScpFunctionList.append(func)

def GetFuntionId(FunctionLabel):
    return scena.ScpFunctionList.index(FunctionLabel)

for op, inst in ed6fc.ed6fc_op_table.items():

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
    entry = ed6fc.ed6fc_op_table[op]

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

    # fs.write(b'\x00' * (16 - fs.tell() % 16))

    scena.ScenaFunctionTable.Offset = fs.tell()
    scena.ScenaFunctionTable.Size = len(scena.ScpFunctionList) * 2

    for func in scena.ScpFunctionList:
        fs.WriteUShort(getlabel(func))

    scena.StringTableOffset = fs.tell()

    fs.Write('\x00'.join(scena.StringTable).encode(CODE_PAGE) + b'\x00\x00')

    zerostr = fs.tell() - 1

    for lb in scena.DelayFixLabels:
        fs.seek(lb.Offset)
        fs.WriteUShort(getlabel(lb.Label))

    for lb in scena.DelayFixString:
        raise
        fs.seek(lb.Offset)
        pos = zerostr if lb.Label == '' else scena.StringListTable[lb.Label]

        plog('%X -> %X : %s' % (lb.Offset, pos, lb.Label))

        fs.WriteUShort(pos)

    for i in range(len(scena.ScnInfoOffset)):
        plog('%04X : %02X' % (scena.ScnInfoOffset[i], scena.ScnInfoNumber[i]))

    fs.seek(0)
    fs.write(scena.binary())

    fs.close()

    print('done')

    #input()
