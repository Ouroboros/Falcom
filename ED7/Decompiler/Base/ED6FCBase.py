from Base.BaseType import *

CODE_PAGE = 'GBK'

GAME_PATH = r'E:\Game\Steam\steamapps\common\Trails in the Sky FC'

SEPITH_CHI  = 0
SEPITH_MIZU = 1
SEPITH_HONO = 3
SEPITH_KAZE = 2
SEPITH_TOKI = 4
SEPITH_SORA = 5
SEPITH_GEN  = 6

CHIP_TYPE_CHAR      = 7
CHIP_TYPE_APL       = 8
CHIP_TYPE_MONSTER   = 9

DatFileNameTable = CaseInsensitiveDict()

def initDatFileNameTable(gamePath):
    if not os.path.exists(gamePath):
        print('[warning] %s not exists' % gamePath)
        return

    for file in fileio.getDirectoryFiles(gamePath, '*.dir'):
        fs = fileio.FileStream(file)
        if fs.Length <= 0x10:
            continue

        file = os.path.splitext(os.path.basename(file))[0]
        names = []

        fs.Position = 0x10
        buf = fs.Read()
        for i in range(0, len(buf), 0x24):
            n = buf[i:i+0x10].split(b'\x00', 1)[0].decode(CODE_PAGE)
            if n != '/_______.___':
                names.append(n)

        DatFileNameTable[file] = names

initDatFileNameTable(GAME_PATH)

class FileIndexBase:
    def __init__(self, param):
        self.Value = param
        self.IsIndexInvalid = False

        if isinstance(param, int):
            self.FileIndex = param

            if param == 0xFFFFFFFF:
                self.FileName = ''
                return

            dat = 'ED6_DT%02d' % (param >> 16)
            self.FileName = '%s/%s' % (dat, DatFileNameTable[dat][param & 0xFFFF])

        elif isinstance(param, str):
            self.FileName = param
            if not param:
                self.FileIndex = 0xFFFFFFFF
                return

            dat, name = param.replace('\\', '/').split('/', 1)
            index = DatFileNameTable[dat].index(name)

            self.FileIndex = (int(dat[-2:], 16) << 16) | index

        else:
            raise Exception('unsupported input type')

    def Name(self):
        return self.FileName

    def Index(self):
        return self.FileIndex

class ScenarioChipInfo(FileIndexBase):
    def __init__(self, fs = None):
        if isinstance(fs, fileio.FileStream):
            fs = fs.ReadULong()

        super().__init__(fs)

    def __str__(self):
        return self.Name()

    def fileindex(self):
        return self.Index()

    def binary(self):
        return struct.pack('<L', self.FileIndex)

    def param(self):
        return repr(str(self))

class BGMFileIndex:
    def __init__(self, param):

        self.Value = param
        self.IsIndexInvalid = False

        if type(param) == int:

            if param == -1:
                self.IsIndexInvalid = True
                return

            self.FileName = 'ed6%04d' % param
            self.FileIndex = param

        elif type(param) == str:

            param = param.lower()

            if param[:3] != 'ed6':
                raise Exception('incorrect bgm file name: %s' % param)

            self.FileName = param
            self.FileIndex = int(os.path.splitext(param)[0][3:])

        else:

            raise Exception('unsupported input type')

    def Name(self):
        return self.FileName if not self.IsInvalid() else self.Value

    def Index(self):
        return self.FileIndex if not self.IsInvalid() else self.Value

    def IsInvalid(self):
        return self.IsIndexInvalid

    def param(self):
        return '-1' if self.IsInvalid() else ('"%s"' % self.Name())


class ScenarioFileIndex(FileIndexBase):
    pass

class ChipFileIndex(FileIndexBase):
    pass

class SymbolFileIndex(FileIndexBase):
    pass

class BattleScriptFileIndex(FileIndexBase):
    pass

class CraftConditionFlags:
    Poison              = 0x00000001
    Freeze              = 0x00000002
    Petrify             = 0x00000004
    Sleeping            = 0x00000008
    BanArts             = 0x00000010
    Blind               = 0x00000020
    Seal                = 0x00000040
    Confuse             = 0x00000080
    Faint               = 0x00000100
    OnehitKill          = 0x00000200
    Burning             = 0x00000400
    Rage                = 0x00000800
    ArtsGuard           = 0x00001000
    CraftGuard          = 0x00002000

    MaxGuard            = 0x00004000
    Vanish              = 0x00008000
    Str                 = 0x00010000
    Def                 = 0x00020000
    Ats                 = 0x00040000
    Adf                 = 0x00080000
    Dex                 = 0x00100000
    Agl                 = 0x00200000
    Mov                 = 0x00400000
    Spd                 = 0x00800000
    HPRecovery          = 0x01000000
    CPRecovery          = 0x02000000

    Stealth             = 0x04000000
    ArtsReflect         = 0x08000000

    Boost               = 0x10000000

    CraftReflect        = 0x20000000
    Reserve_2           = 0x20000000

    GreenPepper         = 0x40000000

    Dead                = 0x80000000



class CraftAttribute:
    NoAttribute = 0
    Chi         = 1
    Mizu        = 2
    Hono        = 3
    Kaze        = 4
    Toki        = 5
    Sora        = 6
    Gen         = 7

CraftAttributeNames = {}

for attr in dir(CraftAttribute):
    if attr.startswith('__') or attr.endswith('__'):
        continue

    CraftAttributeNames[getattr(CraftAttribute, attr)] = 'CraftAttribute.%s' % attr

class CraftRange:
    NoneRange                   = 0x00

    Target                      = 0x01
    CircleOnTarget              = 0x02
    LineOnTarget                = 0x03
    TargetWithoutMove           = 0x04
    CircleOnTargetNoMove        = 0x05

    CircleOnLocation            = 0x0B
    LineOnLocation              = 0x0C
    FullMap                     = 0x0D
    CircleOnSelf                = 0x0E
    CircleOnLocationExclude     = 0x0F

    LineOnLocationIncludeSelf   = 0x11
    CircleOnLocationIncludeAll  = 0x12

    SelectLocation              = 0x32

CraftRangeNames = {}

for attr in dir(CraftRange):
    if attr.startswith('__') or attr.endswith('__'):
        continue

    CraftRangeNames[getattr(CraftRange, attr)] = 'CraftRange.%s' % attr

class CraftState:
    NoneState               = 0x00

    Physical                = 0x01
    PhysicalForce           = 0x02
    Arts                    = 0x03

    Poison                  = 0x04
    Freeze                  = 0x05
    Burning                 = 0x06
    Seal                    = 0x07
    BanArts                 = 0x08
    Blind                   = 0x09
    Sleep                   = 0x0A
    Confuse                 = 0x0B
    Faint                   = 0x0D
    Petrifaction            = 0x0E

    OnehitKill              = 0x0F
    Vanish                  = 0x10
    ATDelay                 = 0x11
    InterruptAria           = 0x12
    Fat                     = 0x13
    GreenPepper             = 0x13

    LeechHP                 = 0x16
    LeechEP                 = 0x17
    LeechCP                 = 0x18
    DamageToHP              = 0x19
    DamageToEP              = 0x1A
    HPHeal                  = 0x1B
    EPHeal                  = 0x1C
    CPHeal                  = 0x1D

    HealPoison              = 0x1E
    HealFrozen              = 0x1F
    HealBurning             = 0x20
    HealBanCraft            = 0x21
    HealBanArts             = 0x22
    HealDarkness            = 0x23
    HealSleep               = 0x24
    HealConfusion           = 0x25
    HealFaint               = 0x26
    HealPetrifaction        = 0x27

    STRBuff                 = 0x28
    DEFBuff                 = 0x29
    ATSBuff                 = 0x2A
    ADFBuff                 = 0x2B
    SPDBuff                 = 0x2C
    AGLBuff                 = 0x2D
    MOVBuff                 = 0x2E

    State_2F                = 0x2F

    State_31                = 0x31
    State_32                = 0x32
    State_33                = 0x33
    State_34                = 0x34

    State_36                = 0x36
    State_37                = 0x37
    Stealth                 = 0x38
    CraftGuard              = 0x39
    ArtsGuard               = 0x3A
    ArtsReflection          = 0x3B
    Guard                   = 0x3C

    State_42                = 0x42
    State_45                = 0x45

    State_4D                = 0x4D
    State_4E                = 0x4E
    State_4F                = 0x4F

    State_50                = 0x50

    QueryMonsterInfo        = 0x51

    State_52                = 0x52

    StrSpdUp_Faint          = 0x55

    State_5F                = 0x5F
    State_60                = 0x60

CraftStateNames = {}

for attr in dir(CraftState):
    if attr.startswith('__') or attr.endswith('__'):
        continue

    CraftStateNames[getattr(CraftState, attr)] = 'CraftState.%s' % attr

class CraftTarget:
    TargetChr   = 0xFE
    TargetPos   = 0xFB
    Self        = 0xFF
    InitialPos  = 0xFD
    OriginalPos = 0xF0
