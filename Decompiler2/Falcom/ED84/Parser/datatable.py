from Falcom.Common import *
from Falcom.ED83.Parser.datatable import *
from Falcom.ED83.Parser.datatable import createDataTable
from . import utils

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
            self.float4 = fs.ReadFloat()

    def toPython(self) -> List[str]:
        return [
            f'{self.__class__.__name__}(',
            f'    id     = {self.id},',
            f"    file   = '{self.file}',",
            f'    word3  = {self.word3},',
            f'    float4 = {self.float4:g},',
            ')',
        ]

    def serialize(self) -> bytes:
        body = bytearray()

        body.extend(utils.int_to_bytes(self.id, 2))
        body.extend(utils.str_to_bytes(self.file))
        body.extend(utils.int_to_bytes(self.word3, 2))
        body.extend(utils.float_to_bytes(self.float4))

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
            self.text   = fs.ReadMultiByte()

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
            f"    text      = '{self.text}',",
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
        body.extend(utils.str_to_bytes(self.text))

        return bytes(body)

class StatusTableData(TableDataEntry):
    ENTRY_NAME = 'status'

    FLAGS_TABLE = {
        'M':  0x00000001,
        'E':  0x00000002,
        'N':  0x00000004,
        'K':  0x00000008,
        'T':  0x00000010,
        'H':  0x00000020,
        'D':  0x00000040,
        'S':  0x00000080,
        'R':  0x00000200,
        'J':  0x00000400,
        'C':  0x00000800,
        'F':  0x00001000,
        'I':  0x00002000,
        'X':  0x00004000,
        'Z':  0x00008000,
        'V':  0x00010000,
        'W':  0x00020000,
        'O':  0x00040000,
        'G':  0x00080000,
        'U':  0x00100000,
        'A':  0x00200000,
        'Y':  0x00400000,
        'B':  0x00800000,
        'P':  0x01000000,
        'Q':  0x02000000,
        'L':  0x04000000,
    }

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
            self.str                = fs.ReadULong()
            self.strFactor          = fs.ReadFloat()
            self.def_               = fs.ReadULong()
            self.defFactor          = fs.ReadFloat()
            self.ats                = fs.ReadULong()
            self.atsFactor          = fs.ReadFloat()
            self.adf                = fs.ReadULong()
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
            self.chrId              = fs.ReadUShort()
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
            f"    chrId                     = 0x{self.chrId:04X},",
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
        body.extend(utils.int_to_bytes(self.str, 4))
        body.extend(utils.float_to_bytes(self.strFactor))
        body.extend(utils.int_to_bytes(self.def_, 4))
        body.extend(utils.float_to_bytes(self.defFactor))
        body.extend(utils.int_to_bytes(self.ats, 4))
        body.extend(utils.float_to_bytes(self.atsFactor))
        body.extend(utils.int_to_bytes(self.adf, 4))
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
        body.extend(utils.int_to_bytes(self.chrId, 2))
        body.extend(utils.str_to_bytes(self.name))
        body.extend(utils.str_to_bytes(self.description))

        return bytes(body)


DataTable.DataTableDataTypes.update({
    'bgm'   : BGMTableData,
    'voice' : VoiceTableData,
    'status': StatusTableData,
})

DataTable.PythonHeader = [
    'from Falcom.ED84.Parser.datatable import *',
    '',
    'entries = [',
]
