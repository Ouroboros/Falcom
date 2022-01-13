from Falcom.Common import *
from . import utils

__all__ = (
    'DataTable',
    'TableNameEntry',
    'TableDataEntry',
    'NameTableData',
    'AttachTableData',
    'EventTableData',
    'StatusTableData',
    'VoiceTableData',
    'SETableData',
    'BGMTableData',
)

class TableNameEntry:
    def __init__(self, fs: fileio.FileStream):
        self.name = fs.ReadMultiByte()
        self.entryCount = fs.ReadULong()

    def __str__(self):
        return f'{self.name} @ {self.entryCount}'

    __repr__ = __str__

class TableDataEntry:
    ENTRY_NAME = ''

    def __init__(self, fs: fileio.FileStream):
        if not fs:
            return

        self.entryName  = fs.ReadMultiByte()
        self.entrySize  = fs.ReadUShort()

    def toPython(self) -> List[str]:
        raise NotImplementedError

    def __str__(self):
        return '\n'.join(self.toPython())

    __repr__ = __str__

class NameTableData(TableDataEntry):
    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.chrId          = fs.ReadUShort()
            self.chrName        = fs.ReadMultiByte()
            self.model          = fs.ReadMultiByte()
            self.ani            = fs.ReadMultiByte()
            self.faceModel      = fs.ReadMultiByte()
            self.faceTexture    = fs.ReadMultiByte()
            self.name2          = fs.ReadMultiByte()
            self.dword1         = fs.ReadULong()
            self.dword2         = fs.ReadULong()
            self.dword3         = fs.ReadULong()
            self.dword4         = fs.ReadULong()
            self.word5          = fs.ReadUShort()
            self.byte6          = fs.ReadByte()

    def toPython(self) -> List[str]:
        return [
            'NameTableData(',
            f'    chrId         = 0x{self.chrId:04X},',
            f"    chrName       = '{self.chrName}',",
            f"    model         = '{self.model}',",
            f"    ani           = '{self.ani}',",
            f"    faceModel     = '{self.faceModel}',",
            f"    faceTexture   = '{self.faceTexture}',",
            f"    name2         = '{self.name2}',",
            f'    dword1        = 0x{self.dword1:08X},',
            f'    dword2        = 0x{self.dword2:08X},',
            f'    dword3        = 0x{self.dword3:08X},',
            f'    dword4        = 0x{self.dword4:08X},',
            f'    word5         = 0x{self.word5:04X},',
            f'    byte6         = 0x{self.byte6:02X},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.chrId, 2))
        body.extend(utils.str_to_bytes(self.chrName))
        body.extend(utils.str_to_bytes(self.model))
        body.extend(utils.str_to_bytes(self.ani))
        body.extend(utils.str_to_bytes(self.faceModel))
        body.extend(utils.str_to_bytes(self.faceTexture))
        body.extend(utils.str_to_bytes(self.name2))
        body.extend(utils.int_to_bytes(self.dword1, 4))
        body.extend(utils.int_to_bytes(self.dword2, 4))
        body.extend(utils.int_to_bytes(self.dword3, 4))
        body.extend(utils.int_to_bytes(self.dword4, 4))
        body.extend(utils.int_to_bytes(self.word5, 2))
        body.extend(utils.int_to_bytes(self.byte6, 1))

        return bytes(body)

class AttachTableData(TableDataEntry):
    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.chrId      = fs.ReadUShort()
            self.type       = fs.ReadULong()        # 5: face model   9: face animeclip
            self.itemId     = fs.ReadULong()
            self.scenaFlags = fs.ReadULong()
            self.dword0E    = fs.ReadULong()
            self.dword12    = fs.ReadULong()
            self.model      = fs.ReadMultiByte()
            self.str17      = fs.ReadMultiByte()

    def toPython(self) -> List[str]:
        return [
            'AttachTableData(',
            f'    chrId      = 0x{self.chrId:04X},',
            f"    type       = {self.type},",
            f"    itemId     = 0x{self.itemId:08X},",
            f"    scenaFlags = 0x{self.scenaFlags:08X},",
            f"    dword0E    = {self.dword0E},",
            f"    dword12    = {self.dword12},",
            f"    model      = '{self.model}',",
            f"    str17      = '{self.str17}',",
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.chrId, 2))
        body.extend(utils.int_to_bytes(self.type, 4))
        body.extend(utils.int_to_bytes(self.itemId, 4))
        body.extend(utils.int_to_bytes(self.scenaFlags, 4))
        body.extend(utils.int_to_bytes(self.dword0E, 4))
        body.extend(utils.int_to_bytes(self.dword12, 4))
        body.extend(utils.str_to_bytes(self.model))
        body.extend(utils.str_to_bytes(self.str17))

        return bytes(body)

class EventTableData(TableDataEntry):
    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.eventId    = fs.ReadUShort()
            self.eventEntry = fs.ReadMultiByte()
            self.scena      = fs.ReadMultiByte()
            self.word01     = fs.ReadUShort()
            self.nextEventId= fs.ReadUShort()
            self.word03     = fs.ReadUShort()
            self.str04      = fs.ReadMultiByte()
            self.word05     = fs.ReadUShort()
            self.word06     = fs.ReadUShort()
            self.word07     = fs.ReadUShort()
            self.word08     = fs.ReadUShort()
            self.word09     = fs.ReadUShort()
            self.word0A     = fs.ReadUShort()
            self.word0B     = fs.ReadUShort()
            self.word0C     = fs.ReadUShort()
            self.word0D     = fs.ReadUShort()

    def toPython(self) -> List[str]:
        return [
            'EventTableData(',
            f'    eventId       = 0x{self.eventId:X},',
            f"    eventEntry    = '{self.eventEntry}',",
            f"    scena         = '{self.scena}',",
            f'    word01        = 0x{self.word01:X},',
            f'    nextEventId   = 0x{self.nextEventId:X},',
            f'    word03        = 0x{self.word03:X},',
            f"    str04         = '{self.str04}',",
            f'    word05        = 0x{self.word05:X},',
            f'    word06        = 0x{self.word06:X},',
            f'    word07        = 0x{self.word07:X},',
            f'    word08        = 0x{self.word08:X},',
            f'    word09        = 0x{self.word09:X},',
            f'    word0A        = 0x{self.word0A:X},',
            f'    word0B        = 0x{self.word0B:X},',
            f'    word0C        = 0x{self.word0C:X},',
            f'    word0D        = 0x{self.word0D:X},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.eventId, 2))
        body.extend(utils.str_to_bytes(self.eventEntry))
        body.extend(utils.str_to_bytes(self.scena))
        body.extend(utils.int_to_bytes(self.word01, 2))
        body.extend(utils.int_to_bytes(self.nextEventId, 2))
        body.extend(utils.int_to_bytes(self.word03, 2))
        body.extend(utils.str_to_bytes(self.str04))
        body.extend(utils.int_to_bytes(self.word05, 2))
        body.extend(utils.int_to_bytes(self.word06, 2))
        body.extend(utils.int_to_bytes(self.word07, 2))
        body.extend(utils.int_to_bytes(self.word08, 2))
        body.extend(utils.int_to_bytes(self.word09, 2))
        body.extend(utils.int_to_bytes(self.word0A, 2))
        body.extend(utils.int_to_bytes(self.word0B, 2))
        body.extend(utils.int_to_bytes(self.word0C, 2))
        body.extend(utils.int_to_bytes(self.word0D, 2))

        return bytes(body)

class StatusTableData(TableDataEntry):
    ENTRY_NAME = 'status'

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.algoFile           = fs.ReadMultiByte()
            self.model              = fs.ReadMultiByte()
            self.ani                = fs.ReadMultiByte()
            self.float1             = fs.ReadFloat()
            self.float2             = fs.ReadFloat()
            self.float3             = fs.ReadFloat()
            self.float4             = fs.ReadFloat()
            self.float5             = fs.ReadFloat()
            self.float6             = fs.ReadFloat()
            self.float7             = fs.ReadFloat()
            self.short8             = fs.ReadUShort()
            self.short9             = fs.ReadUShort()
            self.byte10             = fs.ReadByte()
            self.level              = fs.ReadByte()
            self.hpBase             = fs.ReadULong()
            self.hpFactor           = fs.ReadFloat()
            self.epMax              = fs.ReadUShort()
            self.epInit             = fs.ReadUShort()
            self.cpMax              = fs.ReadUShort()
            self.cpInit             = fs.ReadUShort()
            self.str                = fs.ReadUShort()
            self.strFactor          = fs.ReadFloat()
            self.def_               = fs.ReadUShort()
            self.defFactor          = fs.ReadFloat()
            self.ats                = fs.ReadUShort()
            self.atsFactor          = fs.ReadFloat()
            self.adf                = fs.ReadUShort()
            self.adfFactor          = fs.ReadFloat()
            self.dex                = fs.ReadUShort()
            self.dexFactor          = fs.ReadFloat()
            self.agl                = fs.ReadUShort()
            self.aglFactor          = fs.ReadFloat()
            self.evade              = fs.ReadUShort()
            self.spd                = fs.ReadUShort()
            self.spdFactor          = fs.ReadFloat()
            self.mov                = fs.ReadUShort()
            self.movFactor          = fs.ReadFloat()
            self.exp                = fs.ReadUShort()
            self.expFactor          = fs.ReadFloat()
            self.brk                = fs.ReadUShort()
            self.brkFactor          = fs.ReadFloat()

            self.efficacyEarth      = fs.ReadByte()
            self.efficacyWater      = fs.ReadByte()
            self.efficacyFire       = fs.ReadByte()
            self.efficacyWind       = fs.ReadByte()
            self.efficacyTime       = fs.ReadByte()
            self.efficacySpace      = fs.ReadByte()
            self.efficacyMirage     = fs.ReadByte()

            self.efficacyPoison     = fs.ReadByte()
            self.efficacySeal       = fs.ReadByte()
            self.efficacyMute       = fs.ReadByte()
            self.efficacyBLind      = fs.ReadByte()
            self.efficacySleep      = fs.ReadByte()
            self.efficacyBurn       = fs.ReadByte()
            self.efficacyFreeze     = fs.ReadByte()
            self.efficacyPetrify    = fs.ReadByte()
            self.efficacyFaint      = fs.ReadByte()
            self.efficacyConfuse    = fs.ReadByte()
            self.efficacyCharm      = fs.ReadByte()
            self.efficacyDeathblow  = fs.ReadByte()
            self.efficacyNightmare  = fs.ReadByte()
            self.efficacyATDelay    = fs.ReadByte()
            self.efficacyVanish     = fs.ReadByte()
            self.efficacySPDDown    = fs.ReadByte()

            self.efficacySlash      = fs.ReadUShort()
            self.efficacyThurst     = fs.ReadUShort()
            self.efficacyPierce     = fs.ReadUShort()
            self.efficacyStrike     = fs.ReadUShort()

            self.sepithEarth        = fs.ReadByte()
            self.sepithWater        = fs.ReadByte()
            self.sepithFire         = fs.ReadByte()
            self.sepithWind         = fs.ReadByte()
            self.sepithTime         = fs.ReadByte()
            self.sepithSpace        = fs.ReadByte()
            self.sepithMirage       = fs.ReadByte()
            self.sepithMass         = fs.ReadByte()

            self.sepithEarthFactor  = fs.ReadFloat()
            self.sepithWaterFactor  = fs.ReadFloat()
            self.sepithFireFactor   = fs.ReadFloat()
            self.sepithWindFactor   = fs.ReadFloat()
            self.sepithTimeFactor   = fs.ReadFloat()
            self.sepithSpaceFactor  = fs.ReadFloat()
            self.sepithMirageFactor = fs.ReadFloat()
            self.sepithMassFactor   = fs.ReadFloat()

            self.dropItemId1        = fs.ReadUShort()
            self.dropRate1          = fs.ReadByte()
            self.dropItemId2        = fs.ReadUShort()
            self.dropRate2          = fs.ReadByte()

            self.float11            = fs.ReadFloat()
            self.float12            = fs.ReadFloat()

            self.flags              = fs.ReadMultiByte()
            self.name               = fs.ReadMultiByte()
            self.description        = fs.ReadMultiByte()

    def toPython(self) -> List[str]:
        return [
            'StatusTableData(',
            f"    algoFile                  = '{self.algoFile}',",
            f"    model                     = '{self.model}',",
            f"    ani                       = '{self.ani}',",
            f'    float1                    = {self.float1:g},',
            f'    float2                    = {self.float2:g},',
            f'    float3                    = {self.float3:g},',
            f'    float4                    = {self.float4:g},',
            f'    float5                    = {self.float5:g},',
            f'    float6                    = {self.float6:g},',
            f'    float7                    = {self.float7:g},',
            f'    short8                    = 0x{self.short8:04X},',
            f'    short9                    = 0x{self.short9:04X},',
            f'    byte10                    = 0x{self.byte10:02X},',
            f'    level                     = {self.level},',
            f'    hpBase                    = {self.hpBase},',
            f'    hpFactor                  = {self.hpFactor},',
            f'    epMax                     = {self.epMax},',
            f'    epInit                    = {self.epInit},',
            f'    cpMax                     = {self.cpMax},',
            f'    cpInit                    = {self.cpInit},',
            f'    str                       = {self.str},',
            f'    strFactor                 = {self.strFactor},',
            f'    def_                      = {self.def_},',
            f'    defFactor                 = {self.defFactor},',
            f'    ats                       = {self.ats},',
            f'    atsFactor                 = {self.atsFactor},',
            f'    adf                       = {self.adf},',
            f'    adfFactor                 = {self.adfFactor},',
            f'    dex                       = {self.dex},',
            f'    dexFactor                 = {self.dexFactor},',
            f'    agl                       = {self.agl},',
            f'    aglFactor                 = {self.aglFactor},',
            f'    evade                     = {self.evade},',
            f'    spd                       = {self.spd},',
            f'    spdFactor                 = {self.spdFactor},',
            f'    mov                       = {self.mov},',
            f'    movFactor                 = {self.movFactor},',
            f'    exp                       = {self.exp},',
            f'    expFactor                 = {self.expFactor},',
            f'    brk                       = {self.brk},',
            f'    brkFactor                 = {self.brkFactor},',
            f'    efficacyEarth             = {self.efficacyEarth},',
            f'    efficacyWater             = {self.efficacyWater},',
            f'    efficacyFire              = {self.efficacyFire},',
            f'    efficacyWind              = {self.efficacyWind},',
            f'    efficacyTime              = {self.efficacyTime},',
            f'    efficacySpace             = {self.efficacySpace},',
            f'    efficacyMirage            = {self.efficacyMirage},',
            f'    efficacyPoison            = {self.efficacyPoison},',
            f'    efficacySeal              = {self.efficacySeal},',
            f'    efficacyMute              = {self.efficacyMute},',
            f'    efficacyBLind             = {self.efficacyBLind},',
            f'    efficacySleep             = {self.efficacySleep},',
            f'    efficacyBurn              = {self.efficacyBurn},',
            f'    efficacyFreeze            = {self.efficacyFreeze},',
            f'    efficacyPetrify           = {self.efficacyPetrify},',
            f'    efficacyFaint             = {self.efficacyFaint},',
            f'    efficacyConfuse           = {self.efficacyConfuse},',
            f'    efficacyCharm             = {self.efficacyCharm},',
            f'    efficacyDeathblow         = {self.efficacyDeathblow},',
            f'    efficacyNightmare         = {self.efficacyNightmare},',
            f'    efficacyATDelay           = {self.efficacyATDelay},',
            f'    efficacyVanish            = {self.efficacyVanish},',
            f'    efficacySPDDown           = {self.efficacySPDDown},',
            f'    efficacySlash             = {self.efficacySlash},',
            f'    efficacyThurst            = {self.efficacyThurst},',
            f'    efficacyPierce            = {self.efficacyPierce},',
            f'    efficacyStrike            = {self.efficacyStrike},',
            f'    sepithEarth               = {self.sepithEarth},',
            f'    sepithWater               = {self.sepithWater},',
            f'    sepithFire                = {self.sepithFire},',
            f'    sepithWind                = {self.sepithWind},',
            f'    sepithTime                = {self.sepithTime},',
            f'    sepithSpace               = {self.sepithSpace},',
            f'    sepithMirage              = {self.sepithMirage},',
            f'    sepithMass                = {self.sepithMass},',
            f'    sepithEarthFactor         = {self.sepithEarthFactor},',
            f'    sepithWaterFactor         = {self.sepithWaterFactor},',
            f'    sepithFireFactor          = {self.sepithFireFactor},',
            f'    sepithWindFactor          = {self.sepithWindFactor},',
            f'    sepithTimeFactor          = {self.sepithTimeFactor},',
            f'    sepithSpaceFactor         = {self.sepithSpaceFactor},',
            f'    sepithMirageFactor        = {self.sepithMirageFactor},',
            f'    sepithMassFactor          = {self.sepithMassFactor},',
            f'    dropItemId1               = 0x{self.dropItemId1:X},',
            f'    dropRate1                 = {self.dropRate1},',
            f'    dropItemId2               = 0x{self.dropItemId2:X},',
            f'    dropRate2                 = {self.dropRate2},',
            f'    float11                   = {self.float11:g},',
            f'    float12                   = {self.float12:g},',
            f"    flags                     = '{self.flags}',",
            f"    name                      = '{self.name}',",
            f"    description               = {repr(self.description)},",
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.str_to_bytes(self.algoFile))
        body.extend(utils.str_to_bytes(self.model))
        body.extend(utils.str_to_bytes(self.ani))
        body.extend(utils.float_to_bytes(self.float1))
        body.extend(utils.float_to_bytes(self.float2))
        body.extend(utils.float_to_bytes(self.float3))
        body.extend(utils.float_to_bytes(self.float4))
        body.extend(utils.float_to_bytes(self.float5))
        body.extend(utils.float_to_bytes(self.float6))
        body.extend(utils.float_to_bytes(self.float7))
        body.extend(utils.int_to_bytes(self.short8, 2))
        body.extend(utils.int_to_bytes(self.short9, 2))
        body.extend(utils.int_to_bytes(self.byte10, 1))
        body.extend(utils.int_to_bytes(self.level, 1))
        body.extend(utils.int_to_bytes(self.hpBase, 4))
        body.extend(utils.float_to_bytes(self.hpFactor))
        body.extend(utils.int_to_bytes(self.epMax, 2))
        body.extend(utils.int_to_bytes(self.epInit, 2))
        body.extend(utils.int_to_bytes(self.cpMax, 2))
        body.extend(utils.int_to_bytes(self.cpInit, 2))
        body.extend(utils.int_to_bytes(self.str, 2))
        body.extend(utils.float_to_bytes(self.strFactor))
        body.extend(utils.int_to_bytes(self.def_, 2))
        body.extend(utils.float_to_bytes(self.defFactor))
        body.extend(utils.int_to_bytes(self.ats, 2))
        body.extend(utils.float_to_bytes(self.atsFactor))
        body.extend(utils.int_to_bytes(self.adf, 2))
        body.extend(utils.float_to_bytes(self.adfFactor))
        body.extend(utils.int_to_bytes(self.dex, 2))
        body.extend(utils.float_to_bytes(self.dexFactor))
        body.extend(utils.int_to_bytes(self.agl, 2))
        body.extend(utils.float_to_bytes(self.aglFactor))
        body.extend(utils.int_to_bytes(self.evade, 2))
        body.extend(utils.int_to_bytes(self.spd, 2))
        body.extend(utils.float_to_bytes(self.spdFactor))
        body.extend(utils.int_to_bytes(self.mov, 2))
        body.extend(utils.float_to_bytes(self.movFactor))
        body.extend(utils.int_to_bytes(self.exp, 2))
        body.extend(utils.float_to_bytes(self.expFactor))
        body.extend(utils.int_to_bytes(self.brk, 2))
        body.extend(utils.float_to_bytes(self.brkFactor))

        body.extend(utils.int_to_bytes(self.efficacyEarth, 1))
        body.extend(utils.int_to_bytes(self.efficacyWater, 1))
        body.extend(utils.int_to_bytes(self.efficacyFire, 1))
        body.extend(utils.int_to_bytes(self.efficacyWind, 1))
        body.extend(utils.int_to_bytes(self.efficacyTime, 1))
        body.extend(utils.int_to_bytes(self.efficacySpace, 1))
        body.extend(utils.int_to_bytes(self.efficacyMirage, 1))

        body.extend(utils.int_to_bytes(self.efficacyPoison, 1))
        body.extend(utils.int_to_bytes(self.efficacySeal, 1))
        body.extend(utils.int_to_bytes(self.efficacyMute, 1))
        body.extend(utils.int_to_bytes(self.efficacyBLind, 1))
        body.extend(utils.int_to_bytes(self.efficacySleep, 1))
        body.extend(utils.int_to_bytes(self.efficacyBurn, 1))
        body.extend(utils.int_to_bytes(self.efficacyFreeze, 1))
        body.extend(utils.int_to_bytes(self.efficacyPetrify, 1))
        body.extend(utils.int_to_bytes(self.efficacyFaint, 1))
        body.extend(utils.int_to_bytes(self.efficacyConfuse, 1))
        body.extend(utils.int_to_bytes(self.efficacyCharm, 1))
        body.extend(utils.int_to_bytes(self.efficacyDeathblow, 1))
        body.extend(utils.int_to_bytes(self.efficacyNightmare, 1))
        body.extend(utils.int_to_bytes(self.efficacyATDelay, 1))
        body.extend(utils.int_to_bytes(self.efficacyVanish, 1))
        body.extend(utils.int_to_bytes(self.efficacySPDDown, 1))

        body.extend(utils.int_to_bytes(self.efficacySlash, 2))
        body.extend(utils.int_to_bytes(self.efficacyThurst, 2))
        body.extend(utils.int_to_bytes(self.efficacyPierce, 2))
        body.extend(utils.int_to_bytes(self.efficacyStrike, 2))

        body.extend(utils.int_to_bytes(self.sepithEarth, 1))
        body.extend(utils.int_to_bytes(self.sepithWater, 1))
        body.extend(utils.int_to_bytes(self.sepithFire, 1))
        body.extend(utils.int_to_bytes(self.sepithWind, 1))
        body.extend(utils.int_to_bytes(self.sepithTime, 1))
        body.extend(utils.int_to_bytes(self.sepithSpace, 1))
        body.extend(utils.int_to_bytes(self.sepithMirage, 1))
        body.extend(utils.int_to_bytes(self.sepithMass, 1))

        body.extend(utils.float_to_bytes(self.sepithEarthFactor))
        body.extend(utils.float_to_bytes(self.sepithWaterFactor))
        body.extend(utils.float_to_bytes(self.sepithFireFactor))
        body.extend(utils.float_to_bytes(self.sepithWindFactor))
        body.extend(utils.float_to_bytes(self.sepithTimeFactor))
        body.extend(utils.float_to_bytes(self.sepithSpaceFactor))
        body.extend(utils.float_to_bytes(self.sepithMirageFactor))
        body.extend(utils.float_to_bytes(self.sepithMassFactor))

        body.extend(utils.int_to_bytes(self.dropItemId1, 2))
        body.extend(utils.int_to_bytes(self.dropRate1, 1))
        body.extend(utils.int_to_bytes(self.dropItemId2, 2))
        body.extend(utils.int_to_bytes(self.dropRate2, 1))

        body.extend(utils.float_to_bytes(self.float11))
        body.extend(utils.float_to_bytes(self.float12))

        body.extend(utils.str_to_bytes(self.flags))
        body.extend(utils.str_to_bytes(self.name))
        body.extend(utils.str_to_bytes(self.description))

        return bytes(body)

class VoiceTableData(TableDataEntry):
    ENTRY_NAME = 'voice'

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.id     = fs.ReadUShort()
            self.symbol = fs.ReadMultiByte()
            self.file   = fs.ReadMultiByte()
            self.word4  = fs.ReadUShort()
            self.float5 = fs.ReadFloat()
            self.float6 = fs.ReadFloat()
            self.word7  = fs.ReadUShort()
            self.word8  = fs.ReadUShort()
            self.float9 = fs.ReadFloat()

    def toPython(self) -> List[str]:
        return [
            f'{self.__class__.__name__}(',
            f'    id        = 0x{self.id:04X},',
            f"    symbol    = '{self.symbol}',",
            f"    file      = '{self.file}',",
            f'    word4     = {self.word4},',
            f'    float5    = {self.float5},',
            f'    float6    = {self.float6},',
            f'    word7     = {self.word7},',
            f'    word8     = {self.word8},',
            f'    float9    = {self.float9},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.id, 2))
        body.extend(utils.str_to_bytes(self.symbol))
        body.extend(utils.str_to_bytes(self.file))
        body.extend(utils.int_to_bytes(self.word4, 2))
        body.extend(utils.float_to_bytes(self.float5))
        body.extend(utils.float_to_bytes(self.float6))
        body.extend(utils.int_to_bytes(self.word7, 2))
        body.extend(utils.int_to_bytes(self.word8, 2))
        body.extend(utils.float_to_bytes(self.float9))

        return bytes(body)

class SETableData(VoiceTableData):
    ENTRY_NAME = 'se'

class BGMTableData(TableDataEntry):
    ENTRY_NAME = 'bgm'

    def __init__(self, *, fs: fileio.FileStream = None, **kwargs):
        super().__init__(fs)

        for k, v in kwargs.items():
            setattr(self, k, v)

        if fs:
            self.id     = fs.ReadUShort()
            self.file   = fs.ReadMultiByte()
            self.word3  = fs.ReadUShort()

    def toPython(self) -> List[str]:
        return [
            f'{self.__class__.__name__}(',
            f'    id    = {self.id},',
            f"    file  = '{self.file}',",
            f'    word3 = {self.word3},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.id, 2))
        body.extend(utils.str_to_bytes(self.file))
        body.extend(utils.int_to_bytes(self.word3, 2))

        return bytes(body)

class DataTable:
    DataTableDataTypes = {
        'NameTableData'     : NameTableData,
        'AttachTableData'   : AttachTableData,
        'EventTableData'    : EventTableData,
        'status'            : StatusTableData,
        'voice'             : VoiceTableData,
        'se'                : SETableData,
        'bgm'               : BGMTableData,
    }

    PythonHeader = [
        'from Falcom.ED83.Parser.datatable import *',
        '',
        'entries = [',
    ]

    @staticmethod
    def create(*args, **kwargs):
        return createDataTable(*args, **kwargs)

    def __init__(self, *, fs: fileio.FileStream):
        self.fs = fs

        if fs:
            self.entryCount = fs.ReadUShort()
            self.tableCount = fs.ReadULong()
            self.tables = [TableNameEntry(fs) for _ in range(self.tableCount)]

            try:
                self.load(fs)
            except:
                print(f'pos = 0x{fs.Position:X}')
                raise

    def load(self, fs: fileio.FileStream):
        self.entries = []
        entryCount = sum([e.entryCount for e in self.tables])

        for _ in range(entryCount):
            with fs.PositionSaver:
                header = TableDataEntry(fs)

            cls = self.DataTableDataTypes[header.entryName]
            entry = cls(fs = fs)
            self.entries.append(entry)

    def toPython(self, filename: str) -> List[str]:
        f = self.PythonHeader.copy()

        for e in self.entries:
            f.extend([f'{GlobalConfig.DefaultIndent}{l}' for l in e.toPython()])
            f[-1] += ','

        f.extend([
            ']',
            '',
            "if __name__ == '__main__':",
            f"{GlobalConfig.DefaultIndent}DataTable.create('{filename}', *entries)",
            '',
        ])

        return f

    def serialize(self) -> bytes:
        raise NotImplementedError

    def __str__(self):
        return f'{self.tables}'

    __repr__ = __str__


def createDataTable(filename: str, *entries):
    table = bytearray()
    data = bytearray()

    table.extend(utils.int_to_bytes(len(entries), 2))

    entryCounter = {}

    for e in entries:
        tableName = e.ENTRY_NAME
        if not tableName:
            tableName = e.__class__.__name__

        entryCounter[tableName] = entryCounter.get(tableName, 0) + 1

        body = e.serialize()

        data.extend(utils.str_to_bytes(tableName))
        data.extend(utils.int_to_bytes(len(body), 2))
        data.extend(body)

    table.extend(utils.int_to_bytes(len(entryCounter), 4))
    for name, count in entryCounter.items():
        table.extend(utils.str_to_bytes(name))
        table.extend(utils.int_to_bytes(count, 4))

    table.extend(data)

    padding = b'\x00' * (((len(table) + 0x10) & ~0x0F) - len(table))
    table.extend(padding)

    open(filename, 'wb').write(table)

    return entries
