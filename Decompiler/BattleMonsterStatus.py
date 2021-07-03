from Base.EDAOBase import *
from GameData.ItemNameMap import *

INVALID_DROP_ITEM_ID        = 0xFFFF
MAXIMUM_ARTS_NUMBER        = 80
MAXIMUM_CRAFT_NUMBER        = 16
MAXIMUM_SCRAFT_NUMBER       = 5
MAXIMUM_CRAFT_INFO_NUMBER   = 16
MAXIMUM_SUPPORTCRAFT_NUMBER = 3

CUSTOM_CRAFT_INDEX_BASE = 0x3E8

class BattleCraftInfo:

    # size = 0x18

    def __init__(self, index = 0, fs = None):

        if fs == None:
            return

        '''

            Target  :   MSData.State
            0x10    :   0x1000 if party else 0x4000 (other side)
            0x20    :   ebp-39
            0x40    :   ebp-45
            0x80    :   0x1000 if enemy (self side)

        '''

        self.Index                  = CUSTOM_CRAFT_INDEX_BASE + index
        self.ActionIndex            = fs.ReadUShort()   # 0x00
        self.Target                 = fs.ReadByte()     # 0x02       # in fact, this is an ushort
        self.Unknown_3              = fs.ReadByte()     # 0x03
        self.Attribute              = fs.ReadByte()     # 0x04
        self.RangeType              = fs.ReadByte()     # 0x05       # CraftRange
        self.State1                 = fs.ReadByte()     # 0x06       # CraftState
        self.State2                 = fs.ReadByte()     # 0x07       # CraftState
        self.RNG                    = fs.ReadByte()     # 0x08
        self.RangeSize              = fs.ReadByte()     # 0x09
        self.AriaTime               = fs.ReadByte()     # 0x0A
        self.SkillTime              = fs.ReadByte()     # 0x0B
        self.EP_CP                  = fs.ReadUShort()   # 0x0C
        self.RangeSize2             = fs.ReadUShort()   # 0x0E
        self.State1Parameter        = fs.ReadShort()    # 0x10      e.g. damage factor
        self.State1Time             = fs.ReadShort()    # 0x12      e.g. frozen AT
        self.State2Parameter        = fs.ReadShort()    # 0x14
        self.State2Time             = fs.ReadShort()    # 0x16

        self.Name = fs.ReadMultiByte()
        self.Description = fs.ReadMultiByte()

    def binary(self):
        return struct.pack('<HBBBBBBBBBBHHhhhh',
                    self.ActionIndex,
                    self.Target,
                    self.Unknown_3,
                    self.Attribute,
                    self.RangeType,
                    self.State1,
                    self.State2,
                    self.RNG,
                    self.RangeSize,
                    self.AriaTime,
                    self.SkillTime,
                    self.EP_CP,
                    self.RangeSize2,
                    self.State1Parameter,
                    self.State1Time,
                    self.State2Parameter,
                    self.State2Time

                ) + (self.Name.encode(CODE_PAGE) + b'\x00') + (self.Description.encode(CODE_PAGE) + b'\x00')

    def param(self):
        #print('state1 = %X' % self.State1)
        #print('state2 = %X' % self.State2)
        #print('rangetype = %X' % self.RangeType)
        return '"%s", "%s", 0x%02X, 0x%X, 0x%X, %s, %s, %s, %s, %d, %d, %d, %d, %d, 0x%X, 0x%04X, %d, 0x%04X, %d' % (
                    self.Name,
                    self.Description,
                    self.ActionIndex,
                    self.Target,
                    self.Unknown_3,
                    CraftAttributeNames[self.Attribute],
                    CraftRangeNames[self.RangeType],
                    CraftStateNames[self.State1],
                    CraftStateNames[self.State2],
                    self.RNG,
                    self.RangeSize,
                    self.AriaTime,
                    self.SkillTime,
                    self.EP_CP,
                    self.RangeSize2,
                    self.State1Parameter,
                    self.State1Time,
                    self.State2Parameter,
                    self.State2Time
                )

    def paramlist(self):
        #print('state1 = %X' % self.State1)
        #print('state2 = %X' % self.State2)
        #print('rangetype = %X' % self.RangeType)

        params = []
        params.append('"%s"' % self.Name.replace('\\', '\\\\'))
        params.append('"%s"' % self.Description.replace('\\', '\\\\'))
        params.append('0x%02X, 0x%X, 0x%X' % (self.ActionIndex, self.Target, self.Unknown_3))
        params.append('%s' % CraftAttributeNames[self.Attribute])
        params.append('%s' % CraftRangeNames[self.RangeType])
        params.append('%s, %s' % (CraftStateNames[self.State1], CraftStateNames[self.State2]))
        params.append('%d, %d' % (self.RNG, self.RangeSize))
        params.append('%d, %d' % (self.AriaTime, self.SkillTime))
        params.append('%d' % (self.EP_CP))
        params.append('%d' % (self.RangeSize2))
        params.append('%d, %d' % (self.State1Parameter, self.State1Time))
        params.append('%d, %d' % (self.State2Parameter, self.State2Time))

        return params

def CreateCraft(
        Name,
        Description,
        ActionIndex,
        Target,
        Unknown_3,
        Attribute,
        RangeType,
        State1,
        State2,
        RNG,
        RangeSize,
        AriaTime,
        SkillTime,
        EP_CP,
        RangeSize2,
        State1Parameter,
        State1Time,
        State2Parameter,
        State2Time
    ):

    info = BattleCraftInfo()

    info.Name               = Name
    info.Description        = Description
    info.ActionIndex        = ActionIndex
    info.Target             = Target
    info.Unknown_3          = Unknown_3
    info.Attribute          = Attribute
    info.RangeType          = RangeType
    info.State1             = State1
    info.State2             = State2
    info.RNG                = RNG
    info.RangeSize          = RangeSize
    info.AriaTime           = AriaTime
    info.SkillTime          = SkillTime
    info.EP_CP              = EP_CP
    info.RangeSize2         = RangeSize2
    info.State1Parameter    = State1Parameter
    info.State1Time         = State1Time
    info.State2Parameter    = State2Parameter
    info.State2Time         = State2Time

    return info

def CreateCraftList(CraftList):
    CraftList = list(CraftList)

    if len(CraftList) > MAXIMUM_CRAFT_INFO_NUMBER:
        raise Exception('craft info %d >= %d' % (len(CraftList), MAXIMUM_CRAFT_INFO_NUMBER))

    index = CUSTOM_CRAFT_INDEX_BASE
    for craft in CraftList:
        craft.Index = index
        index += 1

    return CraftList


class BattleCraftAIInfo:

    # size = 0x18:

    def __init__(self, fs = None):

        if fs == None:
            return

        self.Condition                  = fs.ReadByte()
        self.Probability                = fs.ReadByte()
        self.Target                     = fs.ReadByte()
        self.TargetCondition            = fs.ReadByte()
        self.AriaActionIndex            = fs.ReadByte()
        self.ActionIndex                = fs.ReadByte()
        self.CraftIndex                 = fs.ReadUShort()
        self.Parameter                  = [0] * 4

        for i in range(len(self.Parameter)):
            self.Parameter[i] = fs.ReadULong()

    def binary(self):
        return struct.pack('<BBBBBBHLLLL',
                    self.Condition, self.Probability, self.Target, self.TargetCondition,
                    self.AriaActionIndex, self.ActionIndex, self.CraftIndex,
                    self.Parameter[0], self.Parameter[1], self.Parameter[2], self.Parameter[3]
                )

    def param(self):
        p = '0x%X, %d, 0x%X, 0x%X, 0x%02X, 0x%02X, 0x%04X, [%d, %d, %d, %d]' % (
                    self.Condition, self.Probability, self.Target, self.TargetCondition,
                    self.AriaActionIndex, self.ActionIndex, self.CraftIndex,
                    self.Parameter[0], self.Parameter[1], self.Parameter[2], self.Parameter[3]
                )

        return p

def CreateAI(Condition, Probability, Target, TargetCondition, AriaActionIndex, ActionIndex, CraftIndex, Parameters):
    if not IsTupleOrList(Parameters):
        raise Exception('Parameters must be list or tuple')

    if len(Parameters) > 4:
        Parameters = Parameters[:4]
    elif len(Parameters) < 4:
        Parameters += (4 - len(Parameters)) * [0]

    if type(CraftIndex) == BattleCraftInfo:
        CraftIndex = CraftIndex.Index

    ai = BattleCraftAIInfo()

    ai.Condition                = Condition
    ai.Probability              = Probability
    ai.Target                   = Target
    ai.TargetCondition          = TargetCondition
    ai.AriaActionIndex          = AriaActionIndex
    ai.ActionIndex              = ActionIndex
    ai.CraftIndex               = CraftIndex
    ai.Parameter                = Parameters

    return ai

class BattleMonsterStatus:

    def __init__(self):

        self.ASFile                 = BattleScriptFileIndex()

        self.Level                  = 0                     # 0x04

        self.MaximumHP              = 0                     # 0x06
        self.InitialHP              = 0                     # 0x0A
        self.MaximumEP              = 0                     # 0x0E
        self.InitialEP              = 0                     # 0x10
        self.MaximumCP              = 0                     # 0x12
        self.InitialCP              = 0                     # 0x14

        self.SPD                    = 0                     # 0x16
        self.MoveSPD                = 0                     # 0x18
        self.MOV                    = 0                     # 0x1A
        self.STR                    = 0                     # 0x1C
        self.DEF                    = 0                     # 0x1E
        self.ATS                    = 0                     # 0x20
        self.ADF                    = 0                     # 0x22
        self.DEX                    = 0                     # 0x24
        self.AGL                    = 0                     # 0x26
        self.RNG                    = 0                     # 0x28

        self.Unknown_2A             = 0                     # 0x2A
        self.EXP                    = 0                     # 0x2C  (Target.Level - self.Level) * EXP
        self.Unknown_2E             = 0                     # 0x2E
        self.Unknown_30             = 0                     # 0x30
        self.AIType                 = 0                     # 0x31  00 01 02 10 13 14 FF
        self.Unknown_33             = 0                     # 0x33
        self.Unknown_35             = 0                     # 0x35
        self.Unknown_36             = 0                     # 0x36  ignore ?
        self.EnemyFlags             = 0                     # 0x38  0x10: enemy  0x40: self
        self.BattleFlags            = 0                     # 0x3A  0x04    死后留在战场上
                                                            #       0x0800  抵抗 ATDelay
                                                            #       0x0200  不被击退
                                                            #       0x0100  被攻击不转身(3D)
        self.Unknown_3C             = 0                     # 0x3C
        self.Unknown_3E             = 0                     # 0x3E
        self.Sex                    = 0                     # 0x40  1: male     0: female
        self.Unknown_41             = 0                     # 0x41
        self.CharSize               = 0                     # 0x42  / 2 / 400
        self.DefaultEffectX         = 0                     # 0x46
        self.DefaultEffectZ         = 0                     # 0x4A
        self.DefaultEffectY         = 0                     # 0x4E
        self.Unknown_52             = 0                     # 0x52
        self.Unknown_53             = 0                     # 0x53
        self.Unknown_54             = 0                     # 0x54
        self.Unknown_55             = 0                     # 0x55
        self.Symbol                 = SymbolFileIndex(0)    # 0x56
        self.Resistance             = 0                     # 0x5A  异常状态抵抗
        self.AttributeRate          = [0] * 7               # 0x5E  USHORT [7]
        self.Sepith                 = [0] * 7               # 0x6C  BYTE [7]
        self.DropItem               = [0] * 2               # 0x73  USHORT [2]
        self.DropRate               = [0] * 2               # 0x77  BYTE[2]
        self.Equipment              = [0] * 5               # 0x79
        self.Orbment                = [0] * 4               # 0x83

        self.Attack                 = BattleCraftAIInfo()   # 0x8B
        self.ArtsNumber            = 0                     # 0x8B + sizeof(BattleCraftAIInfo), BYTE
        self.Arts                   = []                    # ArtsNumber * BattleCraftAIInfo
        self.CraftNumber            = 0
        self.Craft                  = []
        self.SCraftNumber           = 0
        self.SCraft                 = []
        self.SupportCraftNumber     = 0
        self.SupportCraft           = []
        self.CraftInfoNumber        = 0
        self.CraftInfo              = []

        self.RunawayType            = 0                     # BYTE  0, 1, 2, 3
        self.RunawayRate            = 0                     # BYTE  percent
        self.RunawayParam1          = 0                     # BYTE
        self.Reserve1               = 0                     # BYTE

        self.Name            = ''
        self.Description     = ''

    def binary(self):
        asfile = struct.pack('L', self.ASFile.Index())
        base = struct.pack(
                    '<HLLHHHH' 'HHHHHHHHHH',
                    self.Level,
                    self.MaximumHP, self.InitialHP,
                    self.MaximumEP, self.InitialEP,
                    self.MaximumCP, self.InitialCP,

                    self.SPD, self.MoveSPD, self.MOV, self.STR, self.DEF,
                    self.ATS, self.ADF, self.DEX, self.AGL, self.RNG
                )

        misc = struct.pack(
                    '<HHHBHHBHHHHH' 'BBLLLLBBBB' 'LL',
                    self.Unknown_2A, self.EXP, self.Unknown_2E, self.Unknown_30, self.AIType,
                    self.Unknown_33, self.Unknown_35, self.Unknown_36, self.EnemyFlags,
                    self.BattleFlags, self.Unknown_3C, self.Unknown_3E,

                    self.Sex, self.Unknown_41, self.CharSize, self.DefaultEffectX,
                    self.DefaultEffectZ, self.DefaultEffectY, self.Unknown_52, self.Unknown_53,
                    self.Unknown_54, self.Unknown_55,

                    self.Symbol.Index(), self.Resistance
                )

        AttributeRate = struct.pack('<' + 'H' * len(self.AttributeRate), *self.AttributeRate)
        Sepith = bytes(self.Sepith)
        DropItem = struct.pack('HHBB', self.DropItem[0], self.DropItem[1], self.DropRate[0], self.DropRate[1])

        EquipmentAndOrbment = self.Equipment + self.Orbment
        EquipmentAndOrbment = struct.pack('<' + 'H' * len(EquipmentAndOrbment), *EquipmentAndOrbment)

        Crafts = self.Attack.binary()

        def packcraftlist(craftlist):
            buf = struct.pack('<B', len(craftlist))
            for craft in craftlist:
                buf += craft.binary()

            return buf

        Crafts += packcraftlist(self.Arts)
        Crafts += packcraftlist(self.Craft)
        Crafts += packcraftlist(self.SCraft)
        Crafts += packcraftlist(self.SupportCraft)
        Crafts += packcraftlist(self.CraftInfo)

        Runaway = struct.pack('<BBBB', self.RunawayType, self.RunawayRate, self.RunawayParam1, self.Reserve1)

        NameAndDescription = self.Name.encode(CODE_PAGE) + b'\x00' + self.Description.encode(CODE_PAGE) + b'\x00'

        return asfile + base + misc + AttributeRate + Sepith + DropItem + EquipmentAndOrbment + Crafts + Runaway + NameAndDescription

    def open(self, msfilename):
        def GetItemName(id):
            return '%s' % ItemNameMap[id] if id in ItemNameMap else '0x%04X' % id

        fs = fileio.FileStream(msfilename)

        self.ASFile                 = BattleScriptFileIndex(fs.ReadULong())

        self.Level                  = fs.ReadUShort()

        self.MaximumHP              = fs.ReadULong()
        self.InitialHP              = fs.ReadULong()
        self.MaximumEP              = fs.ReadUShort()
        self.InitialEP              = fs.ReadUShort()
        self.MaximumCP              = fs.ReadUShort()
        self.InitialCP              = fs.ReadUShort()

        self.SPD                    = fs.ReadUShort()
        self.MoveSPD                = fs.ReadUShort()
        self.MOV                    = fs.ReadUShort()
        self.STR                    = fs.ReadUShort()
        self.DEF                    = fs.ReadUShort()
        self.ATS                    = fs.ReadUShort()
        self.ADF                    = fs.ReadUShort()
        self.DEX                    = fs.ReadUShort()
        self.AGL                    = fs.ReadUShort()
        self.RNG                    = fs.ReadUShort()

        self.Unknown_2A             = fs.ReadUShort()
        self.EXP                    = fs.ReadUShort()
        self.Unknown_2E             = fs.ReadUShort()
        self.Unknown_30             = fs.ReadByte()
        self.AIType                 = fs.ReadUShort()
        self.Unknown_33             = fs.ReadUShort()
        self.Unknown_35             = fs.ReadByte()
        self.Unknown_36             = fs.ReadUShort()
        self.EnemyFlags             = fs.ReadUShort()
        self.BattleFlags            = fs.ReadUShort()
        self.Unknown_3C             = fs.ReadUShort()
        self.Unknown_3E             = fs.ReadUShort()

        self.Sex                    = fs.ReadByte()
        self.Unknown_41             = fs.ReadByte()
        self.CharSize               = fs.ReadULong()
        self.DefaultEffectX         = fs.ReadULong()
        self.DefaultEffectZ         = fs.ReadULong()
        self.DefaultEffectY         = fs.ReadULong()
        self.Unknown_52             = fs.ReadByte()
        self.Unknown_53             = fs.ReadByte()
        self.Unknown_54             = fs.ReadByte()
        self.Unknown_55             = fs.ReadByte()

        self.Symbol                 = SymbolFileIndex(fs.ReadULong())
        self.Resistance             = fs.ReadULong()
        self.AttributeRate          = struct.unpack('<HHHHHHH', fs.read(2 * 7))
        self.Sepith                 = list(fs.read(7))
        self.DropItem               = [ fs.ReadUShort(), fs.ReadUShort() ]
        self.DropRate               = list(fs.read(2))
        self.Equipment              = list(struct.unpack('<HHHHH', fs.read(2 * 5)))
        self.Orbment                = list(struct.unpack('<HHHH', fs.read(2 * 4)))

        for l in [self.DropItem, self.Equipment, self.Orbment]:
            for i in range(len(l)):
                l[i] = GetItemName(l[i])

        self.Attack                 = BattleCraftAIInfo(fs)

        self.ArtsNumber = fs.ReadByte()
        for i in range(self.ArtsNumber):
            self.Arts.append(BattleCraftAIInfo(fs))

        self.CraftNumber = fs.ReadByte()
        for i in range(self.CraftNumber):
            self.Craft.append(BattleCraftAIInfo(fs))

        self.SCraftNumber = fs.ReadByte()
        for i in range(self.SCraftNumber):
            self.SCraft.append(BattleCraftAIInfo(fs))

        self.SupportCraftNumber = fs.ReadByte()
        for i in range(self.SupportCraftNumber):
            self.SupportCraft.append(BattleCraftAIInfo(fs))

        index = 0
        self.CraftInfoNumber = fs.ReadByte()
        for i in range(self.CraftInfoNumber):
            info = BattleCraftInfo(index, fs)
            self.CraftInfo.append(info)
            index += 1

        self.RunawayType            = fs.ReadByte()
        self.RunawayRate            = fs.ReadByte()
        self.RunawayParam1          = fs.ReadByte()
        self.Reserve1               = fs.ReadByte()

        self.Name                   = fs.ReadMultiByte()
        self.Description            = fs.ReadMultiByte()

    def FindCraftByActionIndex(self, ActionIndex):
        craftindex = None
        craftlist = [self.SCraft, self.Craft, self.Arts]

        for i in range(len(craftlist)):
            for craft in craftlist[i]:
                if craft.ActionIndex != ActionIndex:
                    continue

                if craft.CraftIndex < CUSTOM_CRAFT_INDEX_BASE:
                    continue

                craftindex = craft.CraftIndex
                break

            if craftindex != None:
                break

        if craftindex == None:
            return None

        for x in self.CraftInfo:
            if x.Index == craftindex:
                return x

        return None

    def SaveTo(self, filename):

        lines = []
        header = []

        def add(l):
            lines.append(l)

        def fmtlist(l, fmt = '%d'):
            tmp = []
            for rate in l:
                tmp.append(fmt % rate)

            return ', '.join(tmp)

        header.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
        header.append('')
        header.append('def main():')

        add('Name               = "%s"' % self.Name.replace('\\', '\\\\'))
        add('Description        = "%s"' % self.Description.replace('\\', '\\\\'))
        add('ASFile             = "%s"' % self.ASFile.Name())
        add('Symbol             = "%s"' % self.Symbol.Name())
        add('')
        add('Level              = %d' % self.Level)
        add('MaximumHP          = %d' % self.MaximumHP)
        add('InitialHP          = %d' % self.InitialHP)
        add('MaximumEP          = %d' % self.MaximumEP)
        add('InitialEP          = %d' % self.InitialEP)
        add('MaximumCP          = %d' % self.MaximumCP)
        add('InitialCP          = %d' % self.InitialCP)
        add('')
        add('SPD                = %d' % self.SPD)
        add('MoveSPD            = %d' % self.MoveSPD)
        add('MOV                = %d' % self.MOV)
        add('STR                = %d' % self.STR)
        add('DEF                = %d' % self.DEF)
        add('ATS                = %d' % self.ATS)
        add('ADF                = %d' % self.ADF)
        add('DEX                = %d' % self.DEX)
        add('AGL                = %d' % self.AGL)
        add('RNG                = %d' % self.RNG)
        add('')
        add('Unknown_2A         = 0x%X' % self.Unknown_2A)
        add('EXP                = %d' % self.EXP)
        add('Unknown_2E         = 0x%X' % self.Unknown_2E)
        add('Unknown_30         = 0x%X' % self.Unknown_30)
        add('AIType             = 0x%X' % self.AIType)
        add('Unknown_33         = 0x%X' % self.Unknown_33)
        add('Unknown_35         = 0x%X' % self.Unknown_35)
        add('Unknown_36         = 0x%X' % self.Unknown_36)
        add('EnemyFlags         = 0x%04X' % self.EnemyFlags)
        add('BattleFlags        = 0x%04X' % self.BattleFlags)
        add('')
        add('Unknown_3C         = 0x%X' % self.Unknown_3C)
        add('Unknown_3E         = 0x%X' % self.Unknown_3E)
        add('Sex                = %d' % self.Sex)
        add('Unknown_41         = 0x%X' % self.Unknown_41)
        add('CharSize           = 0x%X' % self.CharSize)
        add('DefaultEffectX     = 0x%X' % self.DefaultEffectX)
        add('DefaultEffectZ     = %d' % self.DefaultEffectZ)
        add('DefaultEffectY     = 0x%X' % self.DefaultEffectY)
        add('Unknown_52         = 0x%X' % self.Unknown_52)
        add('Unknown_53         = 0x%X' % self.Unknown_53)
        add('Unknown_54         = 0x%X' % self.Unknown_54)
        add('Unknown_55         = 0x%X' % self.Unknown_55)
        add('Resistance         = 0x%08X' % self.Resistance)
        add('AttributeRate      = [ %s ]' % fmtlist(self.AttributeRate))
        add('Sepith             = [ %s ]' % fmtlist(self.Sepith))
        add('DropItem           = [ %s ]' % fmtlist(self.DropItem, '%s'))
        add('DropRate           = [ %s ]' % fmtlist(self.DropRate))
        add('Equipment          = [ %s ]' % fmtlist(self.Equipment, '%s'))
        add('Orbment            = [ %s ]' % fmtlist(self.Orbment, '%s'))
        add('')
        add('RunawayType        = %d' % self.RunawayType)
        add('RunawayRate        = %d' % self.RunawayRate)
        add('RunawayParam1      = %d' % self.RunawayParam1)
        add('Reserve1           = %d' % self.Reserve1)
        add('')

        CraftNameMap = {}
        AINameConfict = {}
        CraftNameConfict = {}

        def GetMaxCraftNameLength():
            maxnamelen = 0
            for index, name in CraftNameMap.items():
                if strlen(name) > maxnamelen:
                    maxnamelen = strlen(name)

            return maxnamelen + len('SCraft_')

        def CreateCraftName(craft):
            if craft.Name != '' and craft.Name != ' ':
                filter = \
                [
                    ('-', ''),
                    (' ', '_'),
                    ('　', '_'),
                    ('·', '')
                ]

                name = craft.Name
                for x in filter:
                    name = name.replace(x[0], x[1])

            else:
                name = 'Craft_%04X' % craft.Index

            index = 1
            newname = name
            while newname in CraftNameConfict:
                index += 1
                newname = '%s_%d' % (name, index)

            CraftNameConfict[newname] = True
            CraftNameMap[craft.Index] = newname

            return newname

        def GetCraftName(craft):
            return CraftNameMap[craft.Index]

        def GetCraftNameFromAI(ai):
            if ai.CraftIndex >= CUSTOM_CRAFT_INDEX_BASE:
                return CraftNameMap[ai.CraftIndex]
            else:
                return '%04X' % ai.CraftIndex

        def fmtai(ai):
            param = ai.param()
            namelen = 8
            if ai.CraftIndex >= CUSTOM_CRAFT_INDEX_BASE:
                namelen = len(CraftNameMap[ai.CraftIndex])
                param = param.replace(', 0x%04X, ' % ai.CraftIndex, ', %s, ' % (CraftNameMap[ai.CraftIndex]))

            spacelist = [6, 6, 6, 6, 6, 6, GetMaxCraftNameLength(), 8, 8, 8, 8]
            return 'CreateAI(%s)' % AdjustParam(param, spacelist)

        def fmtcraft(cft):
            return 'CreateCraft(%s)' % cft.param()

        def gencraft(craftlist):
            for craft in craftlist:
                paramlist = craft.paramlist()

                add('%s = CreateCraft(' % CreateCraftName(craft))
                for param in paramlist:
                    add('                %s,' % param)
                add('           )')
                add('')

            l = []
            for craft in craftlist:
                l.append('                %s,' % GetCraftName(craft))

            add('')
            add('CraftList = CreateCraftList([')
            add('%s' % '\r\n'.join(l))
            add('            ])')

        def genai(prefix, ailist):

            ainames = []

            if len(ailist) != 0:
                maxnamelen = GetMaxCraftNameLength()

                for ai in ailist:
                    name = '%s_%s' % (prefix, GetCraftNameFromAI(ai))
                    if name not in AINameConfict:
                        AINameConfict[name] = 0

                    AINameConfict[name] += 1
                    if AINameConfict[name] != 1:
                        name += '_%d' % AINameConfict[name]

                    ainames.append(name)
                    add('%s = %s' % (ljust_cn(name, maxnamelen + len('_10')), fmtai(ai)))

                add('')

            return ainames

            #add('%sAIList = [%s]' % (prefix, ', '.join(ainames)))
            #add('')

        gencraft(self.CraftInfo)
        add('')
        add('Attack = %s' % fmtai(self.Attack))
        add('')

        arts        = genai('Arts', self.Arts)
        crafts      = genai('Craft', self.Craft)
        scrafts     = genai('SCraft', self.SCraft)
        supports    = genai('SupportCraft', self.SupportCraft)

        add('ArtsAIList         = [%s]' % ', '.join(arts))
        add('CraftAIList        = [%s]' % ', '.join(crafts))
        add('SCraftAIList       = [%s]' % ', '.join(scrafts))
        add('SupportCraftAIList = [%s]' % ', '.join(supports))
        add('')

        add('SaveToMS("%s", locals())' % (os.path.splitext(os.path.basename(filename))[0] + '.dat'))


        txt = '\r\n'.join(lines)

        lines = txt.replace('\r\n', '\n').replace('\r', '\n').split('\n')

        for l in lines:
            header.append(l if l == '' else ('    %s' % l))

        header.append('')
        header.append('Try(main)')

        open(filename, 'wb').write('\r\n'.join(header).encode('utf_8_sig'))

    def __str__(self):

        l = []
        l.append('Level             = %d' % self.Level)
        l.append('HP                = %d / %d' % (self.InitialHP, self.MaximumHP))
        l.append('EP                = %d / %d' % (self.InitialEP, self.MaximumEP))
        l.append('CP                = %d / %d' % (self.InitialCP, self.MaximumCP))
        l.append('')
        l.append('SPD               = %d' % self.SPD)
        l.append('MoveSPD           = %d' % self.MoveSPD)
        l.append('MOV               = %d' % self.MOV)
        l.append('STR               = %d' % self.STR)
        l.append('DEF               = %d' % self.DEF)
        l.append('ATS               = %d' % self.ATS)
        l.append('ADF               = %d' % self.ADF)
        l.append('DEX               = %d' % self.DEX)
        l.append('AGL               = %d' % self.AGL)
        l.append('RNG               = %d' % self.RNG)
        l.append('')
        l.append('EXP               = %d' % self.EXP)
        l.append('AIType            = %X' % self.AIType)
        l.append('Resistance        = %08X' % self.Resistance)
        l.append('AttributeRate     = %d, %d, %d, %d, %d, %d, %d' % (self.AttributeRate[0], self.AttributeRate[1], self.AttributeRate[2], self.AttributeRate[3], self.AttributeRate[4], self.AttributeRate[5], self.AttributeRate[6]))
        l.append('Sepith            = %d, %d, %d, %d, %d, %d, %d' % (self.Sepith[0], self.Sepith[1], self.Sepith[2], self.Sepith[3], self.Sepith[4], self.Sepith[5], self.Sepith[6]))
        l.append('DropItem          = %04X (%d), %04X (%d)' % (self.DropItem[0], self.DropRate[0], self.DropItem[1], self.DropRate[1]))
        l.append('Equipment         = %04X, %04X, %04X, %04X, %04X' % (self.Equipment[0], self.Equipment[1], self.Equipment[2], self.Equipment[3], self.Equipment[4]))
        l.append('Orbment           = %04X, %04X, %04X, %04X' % (self.Orbment[0], self.Orbment[1], self.Orbment[2], self.Orbment[3]))

        l.append('')
        l.append('%s' % self.Name)
        l.append('%s' % self.Description)
        l.append('')
        l.append('%s' % self.ASFile.Name())
        l.append('%s' % self.Symbol.Name())
        l.append('')

        l.append('CraftInfo: %d' % self.CraftInfoNumber)
        for cftinfo in self.CraftInfo:
            l.append('    %s: %s' % (cftinfo.Name, cftinfo.Description))

        return '\r\n'.join(l)

def SaveToMS(filename, local):
    ms = BattleMonsterStatus()

    ms.Name                 = local['Name']
    ms.Description          = local['Description']
    ms.ASFile               = BattleScriptFileIndex(local['ASFile'])
    ms.Symbol               = SymbolFileIndex(local['Symbol'])

    ms.Level                = local['Level']
    ms.MaximumHP            = local['MaximumHP']
    ms.InitialHP            = local['InitialHP']
    ms.MaximumEP            = local['MaximumEP']
    ms.InitialEP            = local['InitialEP']
    ms.MaximumCP            = local['MaximumCP']
    ms.InitialCP            = local['InitialCP']

    ms.SPD                  = local['SPD']
    ms.MoveSPD              = local['MoveSPD']
    ms.MOV                  = local['MOV']
    ms.STR                  = local['STR']
    ms.DEF                  = local['DEF']
    ms.ATS                  = local['ATS']
    ms.ADF                  = local['ADF']
    ms.DEX                  = local['DEX']
    ms.AGL                  = local['AGL']
    ms.RNG                  = local['RNG']

    ms.Unknown_2A           = local['Unknown_2A']
    ms.EXP                  = local['EXP']
    ms.Unknown_2E           = local['Unknown_2E']
    ms.Unknown_30           = local['Unknown_30']
    ms.AIType               = local['AIType']
    ms.Unknown_33           = local['Unknown_33']
    ms.Unknown_35           = local['Unknown_35']
    ms.Unknown_36           = local['Unknown_36']
    ms.EnemyFlags           = local['EnemyFlags']
    ms.BattleFlags          = local['BattleFlags']

    ms.Unknown_3C           = local['Unknown_3C']
    ms.Unknown_3E           = local['Unknown_3E']
    ms.Sex                  = local['Sex']
    ms.Unknown_41           = local['Unknown_41']
    ms.CharSize             = local['CharSize']
    ms.DefaultEffectX       = local['DefaultEffectX']
    ms.DefaultEffectZ       = local['DefaultEffectZ']
    ms.DefaultEffectY       = local['DefaultEffectY']
    ms.Unknown_52           = local['Unknown_52']
    ms.Unknown_53           = local['Unknown_53']
    ms.Unknown_54           = local['Unknown_54']
    ms.Unknown_55           = local['Unknown_55']
    ms.Resistance           = local['Resistance']
    ms.AttributeRate        = local['AttributeRate']
    ms.Sepith               = local['Sepith']
    ms.DropItem             = local['DropItem']
    ms.DropRate             = local['DropRate']
    ms.Equipment            = local['Equipment']
    ms.Orbment              = local['Orbment']

    ms.RunawayType          = local['RunawayType']
    ms.RunawayRate          = local['RunawayRate']
    ms.RunawayParam1        = local['RunawayParam1']
    ms.Reserve1             = local['Reserve1']

    ms.Attack               = local['Attack']
    ms.Arts                 = local['ArtsAIList']
    ms.Craft                = local['CraftAIList']
    ms.SCraft               = local['SCraftAIList']
    ms.SupportCraft         = local['SupportCraftAIList']
    ms.CraftInfo            = local['CraftList']

    if not isinstance(ms.Attack, BattleCraftAIInfo):    raise Exception(' incorrect Attack type')
    if not isinstance(ms.Arts, list):                   raise Exception(' ArtsAIList must be list')
    if not isinstance(ms.Craft, list):                  raise Exception(' CraftAIList must be list')
    if not isinstance(ms.SCraft, list):                 raise Exception(' SCraftAIList must be list')
    if not isinstance(ms.SupportCraft, list):           raise Exception(' SupportCraftAIList must be list')
    if not isinstance(ms.Craft, list):                  raise Exception(' CraftList must be list')

    if len(ms.Arts)         > MAXIMUM_ARTS_NUMBER:          raise Exception('Arts >= %d' % MAXIMUM_ARTS_NUMBER)
    if len(ms.Craft)        > MAXIMUM_CRAFT_NUMBER:         raise Exception('craft >= %d' % MAXIMUM_CRAFT_NUMBER)
    if len(ms.SCraft)       > MAXIMUM_SCRAFT_NUMBER:        raise Exception('scraft >= %d' % MAXIMUM_SCRAFT_NUMBER)
    if len(ms.SupportCraft) > MAXIMUM_SUPPORTCRAFT_NUMBER:  raise Exception('supportcraft >= %d' % MAXIMUM_SUPPORTCRAFT_NUMBER)
    if len(ms.CraftInfo)    > MAXIMUM_CRAFT_INFO_NUMBER:    raise Exception('craftinfo >= %d' % MAXIMUM_CRAFT_INFO_NUMBER)

    open(filename, 'wb').write(ms.binary())

def procfile(file):
    print('disasm %s' % file)
    ms = BattleMonsterStatus()
    ms.open(file)
    ms.SaveTo(os.path.splitext(file)[0] + '.py')

if __name__ == '__main__':
    iterlib.forEachFileMP(procfile, sys.argv[1:], 'ms*.dat')
