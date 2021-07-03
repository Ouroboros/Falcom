from Base.BaseType import *

CODE_PAGE = 'GBK'

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

class ScenarioChipInfo:
    # ULONG chipindex
    def __init__(self, fs = None):

        if fs == None:
            return
        elif type(fs) == str:
            name = fs

            monster ='monster/'
            apl ='apl/'
            chr ='chr/'

            if name[:len(monster)].lower() == monster:
                chiptype = CHIP_TYPE_MONSTER
                name = name[len(monster):]
            elif name[:len(apl)].lower() == apl:
                chiptype = CHIP_TYPE_APL
                name = name[len(apl):]
            elif name[:len(chr)].lower() == chr:
                chiptype = CHIP_TYPE_CHAR
                name = name[len(chr):]
            else:
                raise Exception('unknown chip type')

            chipindex = int(os.path.splitext(name[2:])[0], 16)

            self.ChipIndex = (chiptype << 20) | chipindex

        elif type(fs) == int:

            self.ChipIndex = fs

        else:
            self.ChipIndex = fs.ReadULong()

    def __str__(self):
        chiptype = self.ChipIndex >> 20
        chipindex = self.ChipIndex & 0xFFFFF

        chipdir = 'monster' if chiptype == CHIP_TYPE_MONSTER else 'apl' if chiptype == CHIP_TYPE_APL else 'chr'

        return '%s/ch%05X.itc' % (chipdir, chipindex)

    def fileindex(self):
        return self.ChipIndex

    def binary(self):
        return struct.pack('<L', self.ChipIndex)

    def param(self):
        return '"%s"' % self.__str__()

class FileIndexBase:
    def __init__(self, param):
        self.Value = param

class BGMFileIndex:

    def __init__(self, param):

        self.Value = param
        self.IsIndexInvalid = False

        if type(param) == int:

            if param == -1:
                self.IsIndexInvalid = True
                return

            self.FileName = 'ed7%03d' % param
            self.FileIndex = param

        elif type(param) == str:

            param = param.lower()

            if param[:3] != 'ed7':
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


class ScenarioFileIndex:

    # c1000_2

    def __init__(self, param):

        FilePrefix = '0atcrmeb'
        #self.IsIndexInvalid = bool(param == 0)

        if type(param) == int:

            if param == 0xFFFFFFFF:
                self.FileIndex = param
                self.FileName = ''
                return

            ftype       = (param >> 0x14) & 0xF
            findex      = (param >> 4) & 0xFFFF
            fsubindex   = param & 0xF

            if fsubindex == 0:
                name = '%s%04X' % (FilePrefix[ftype], findex)
            else:
                name = '%s%04X_%X' % (FilePrefix[ftype], findex, fsubindex)

            self.FileName = name
            self.FileIndex = param

        elif type(param) == str:

            if param == '':
                self.FileIndex = 0xFFFFFFFF
                self.FileName = param
                return

            name = os.path.splitext(param)[0]

            ftype = FilePrefix.find(name[0])
            if ftype == -1:
                raise Exception('invalid scena file name')

            name = name[1:].split('_', 1)
            findex = int(name[0], 16)

            fsubindex = 0 if len(name) == 1 else int(name[1], 16)

            self.FileName = param
            self.FileIndex = 0x21000000 | (ftype << 0x14) | (findex << 4) | fsubindex

        else:

            raise Exception('unsupported input type')

    def Name(self):
        return self.FileName

    def Index(self):
        return self.FileIndex


class ChipFileIndex:

    def __init__(self, param = 0):

        self.Value = param

        try:
            self.IsIndexInvalid = bool(int(param) == 0 or (int(param) == 0xFFFFFFFF))
        except:
            self.IsIndexInvalid = False

        monster ='monster/'
        apl ='apl/'
        chr ='chr/'

        if type(param) == int:

            chiptype = param >> 20
            chipindex = param & 0xFFFFF

            chipdir = monster if chiptype == CHIP_TYPE_MONSTER else apl if chiptype == CHIP_TYPE_APL else chr

            self.ChipName = '%sch%05X.itc' % (chipdir, chipindex)
            self.ChipIndex = param

        elif type(param) == str:

            if self.IsIndexInvalid:
                return

            name = param
            nameLower = name.lower()

            if nameLower.startswith(monster):

                chiptype = CHIP_TYPE_MONSTER
                name = name[len(monster):]

            elif nameLower.startswith(apl):

                chiptype = CHIP_TYPE_APL
                name = name[len(apl):]

            elif nameLower.startswith(chr):

                chiptype = CHIP_TYPE_CHAR
                name = name[len(chr):]

            else:

                raise Exception('unknown chip type')

            chipindex = int(os.path.splitext(name[2:])[0], 16)

            self.ChipIndex = (chiptype << 20) | chipindex
            self.ChipName = param

        else:

            raise Exception('unsupported input type')

    def IsInvalid(self):
        return self.IsIndexInvalid

    def Name(self):
        return self.ChipName if not self.IsIndexInvalid else self.Value

    def Index(self):
        return self.ChipIndex if not self.IsIndexInvalid else self.Value


class SymbolFileIndex:

    def __init__(self, param):

        try:
            self.IsIndexInvalid = bool(int(param) == 0)
        except:
            self.IsIndexInvalid = False

        if type(param) == int:

            self.SymbolIndex = param
            self.SymbolName = 'sy%05x.itp' % (param & 0xFFFFFF)

        elif type(param) == str:

            if self.IsIndexInvalid:
                return

            self.SymbolIndex = int(os.path.splitext(os.path.basename(param))[0][2:], 16) | 0x31000000
            self.SymbolName = param

        else:

            raise Exception('unsupported input type')

    def IsInvalid(self):
        return self.IsIndexInvalid

    def Name(self):
        return self.SymbolName if not self.IsIndexInvalid else 0

    def Index(self):
        return self.SymbolIndex if not self.IsIndexInvalid else 0

class BattleScriptFileIndex:

    def __init__(self, param = None):

        if param == None:
            param = 0

        try:
            self.IsIndexInvalid = bool(int(param) == 0)
        except:
            self.IsIndexInvalid = False

        if self.IsIndexInvalid:
            return

        prefix = [ 'ms', 'as', 'bs' ]
        datindex = 0x30000000

        if type(param) == int:

            ftype = (param >> 0x14) & 0xF
            findex = param & 0xFFFFF

            if ftype > len(prefix):
                raise Exception('unknown file type')

            self.FileIndex = param
            self.FileName = '%s%05x.dat' % (prefix[ftype], param & 0xFFFFF)

        elif type(param) == str:

            name = os.path.splitext(os.path.basename(param))[0]

            ftype = prefix.index(name[:2])

            self.FileIndex = int(name[2:], 16) | datindex | (ftype << 0x14)
            self.FileName = param

        else:

            raise Exception('unsupported input type')

    def IsInvalid(self):
        return self.IsIndexInvalid

    def Name(self):
        return self.FileName if not self.IsIndexInvalid else 0

    def Index(self):
        return self.FileIndex if not self.IsIndexInvalid else 0

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
    if attr[:2] == '__' and attr[-2:] == '__':
        continue

    expr = 'CraftAttributeNames[0x%X] = "CraftAttribute.%s"' % (getattr(CraftAttribute, attr), attr)
    exec(expr)

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
    if attr[:2] == '__' and attr[-2:] == '__':
        continue

    expr = 'CraftRangeNames[0x%X] = "CraftRange.%s"' % (getattr(CraftRange, attr), attr)
    exec(expr)

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
    if attr[:2] == '__' and attr[-2:] == '__':
        continue

    expr = 'CraftStateNames[0x%X] = "CraftState.%s"' % (getattr(CraftState, attr), attr)
    exec(expr)


class CraftTarget:
    TargetChr   = 0xFE
    TargetPos   = 0xFB
    Self        = 0xFF
    InitialPos  = 0xFD
    OriginalPos = 0xF0

