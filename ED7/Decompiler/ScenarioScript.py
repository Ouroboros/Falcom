from Assembler.Assembler2 import *
from Base.EDAOBase import *
import Instruction.ScenaOpTableEDAO as edao

CODE_PAGE = edao.CODE_PAGE

'''

version = ED_AO

enum CHIP_TYPE
{
    CHIP_TYPE_CHAR      = 7,
    CHIP_TYPE_APL       = 8,
    CHIP_TYPE_MONSTER   = 9,
};

total actor <= 0x80

enum SCN_INFO_INDEX
{
    SCN_INFO_CHIP       = 0,        // ULONG
    SCN_INFO_NPC        = 1,        // SCENARIO_NPC
    SCN_INFO_MONSTER    = 2,        // SCENARIO_MONSTER
    SCN_INFO_EVENT      = 3,        // SCENARIO_EVENT
    SCN_INFO_ACTOR      = 4,        // SCENARIO_ACTOR

    SCN_INFO_MAXIMUM    = 5,
};

typedef struct  // 0x1C
{
/* 0x00 */  ULONG   X;
/* 0x04 */  ULONG   Y;
/* 0x08 */  ULONG   Z;
/* 0x0C */  USHORT  Unknown1;
/* 0x0E */  USHORT  Unknown2;
/* 0x10 */  UCHAR   Unknown[4];

/* 0x14 */  UCHAR   InitScenaIndex;
/* 0x15 */  UCHAR   InitFunctionIndex;
/* 0x16 */  UCHAR   TalkScenaIndex;
/* 0x17 */  UCHAR   TalkFunctionIndex;
/* 0x18 */  USHORT  Unknown4;
/* 0x1A */  USHORT  Unknown5;

} SCENARIO_NPC;

typedef struct  // 0x20
{
/* 0x00 */    ULONG   X;
/* 0x04 */    ULONG   Y;
/* 0x08 */    ULONG   Z;
/* 0x0C */    ULONG   Unknown_0C;
/* 0x10 */    USHORT  BattleInfoOffset;
/* 0x12 */    USHORT  Unknown_12;
/* 0x14 */    USHORT  ChipIndex;
/* 0x16 */    USHORT  Unknown_16;
/* 0x18 */    ULONG   Unknown_18;
/* 0x1C */    ULONG   Unknown_1C;

} SCENARIO_MONSTER;

typedef struct  // 0x60
{
    UCHAR Dummy[0x60];

} SCENARIO_EVENT;

typedef struct  // 0x24
{
    UCHAR Dummy[0x24];

} SCENARIO_ACTOR;

7B8 - sn buf

3A  -   7C0
3C  -   7C4
3E  -   7C8
40  -   7CC

#define INVALID_SCN_INFO_NUMBER        -1
#define MINIMUM_CHAR_NUMBER             8

typedef struct  // 0x40
{
/* 0x00 */  UCHAR Dummy[0x3C];
/* 0x3C */  UCHAR InitScenaIndex;
/* 0x3D */  UCHAR InitFunctionIndex;
/* 0x3E */  UCHAR EntryScenaIndex;
/* 0x3F */  UCHAR EntryFunctionIndex;

} SCENARIO_INFORMATION;

typedef struct
{
    USHORT Offset;
    USHORT Size;

} SCENARIO_ENTRY;

typedef struct
{
/* 0x00 */   CHAR                     MapName[0xA];                         // %s/%s/%s.it3
/* 0x0A */   CHAR                     Location[0xA];
/* 0x14 */   USHORT                   MapIndex;
/* 0x16 */   USHORT                   MapDefaultBGM;
/* 0x18 */   ULONG                    Flags;
/* 0x1C */   ULONG                    IncludedScenario[6];
/* 0x34 */   ULONG                    StringTableOffset;                    // multi-sz, max-len = 0x20
/* 0x38 */   USHORT                   ScnInfoOffset[SCN_INFO_MAXIMUM];
/* 0x42 */   SCENARIO_ENTRY           ScenaFunctionTable;
/* 0x46 */   USHORT                   ChipFrameInfoOffset;
/* 0x48 */   USHORT                   PlaceNameOffset;                        // ???
/* 0x4A */   UCHAR                    PlaceNameNumber;
/* 0x4B */   UCHAR                    PreInitFunctionIndex;
/* 0x4C */   CHAR                     ScnInfoNumber[SCN_INFO_MAXIMUM];
/* 0x51 */   UCHAR                    Unknown_51[3];
/* 0x54 */   SCENARIO_INFORMATION     Information;

} SCENARIO_HEADER;

op count: 227

'''


NUMBER_OF_INCLUDE_FILE          = 6

SCN_INFO_CHIP       = 0
SCN_INFO_NPC        = 1
SCN_INFO_MONSTER    = 2
SCN_INFO_EVENT      = 3
SCN_INFO_ACTOR      = 4
SCN_INFO_MAXIMUM    = 5

class ScenarioEntry:
    def __init__(self, offset = 0, size = 0):
        self.Offset = offset
        self.Size = size

class ScenarioNpcInfo:
    def __init__(self, fs = None):
        if fs == None:
            return

        # size = 0x1C

        self.X                  = fs.ReadULong()
        self.Z                  = fs.ReadULong()
        self.Y                  = fs.ReadULong()
        self.Direction          = fs.ReadUShort()   # 0 90 270 360
        self.Unknown2           = fs.ReadUShort()

        self.ChipIndex          = fs.ReadByte()
        self.Unknown_11         = fs.ReadByte()
        self.NpcIndex           = fs.ReadByte()
        self.Unknown_14         = fs.ReadByte()

        self.InitScenaIndex     = fs.ReadByte()
        self.InitFunctionIndex  = fs.ReadByte()
        self.TalkScenaIndex     = fs.ReadByte()
        self.TalkFunctionIndex  = fs.ReadByte()

        self.Unknown4           = fs.ReadUShort()
        self.Unknown5           = fs.ReadUShort()

    def __str__(self):
        return str(self.binary())

    def param(self):
        p = '%d, %d, %d, %d, %d, 0x%X, %d, %d, %d, %d, %d, %d, %d, %d, %d' % (
                    LONG(self.X).value,
                    LONG(self.Z).value,
                    LONG(self.Y).value,
                    LONG(self.Direction).value,
                    LONG(self.Unknown2).value,
                    ULONG(self.ChipIndex).value,
                    LONG(self.Unknown_11).value,
                    LONG(self.NpcIndex).value,
                    LONG(self.Unknown_14).value,
                    LONG(self.InitScenaIndex).value,
                    LONG(self.InitFunctionIndex).value,
                    LONG(self.TalkScenaIndex).value,
                    LONG(self.TalkFunctionIndex).value,
                    LONG(self.Unknown4).value,
                    LONG(self.Unknown5).value
                )

        space = [9, 9, 9, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6]
        return AdjustParam(p, space)

    def binary(self):
        return struct.pack('<LLLHHBBBBBBBBHH',
                    ULONG(self.X).value,
                    ULONG(self.Z).value,
                    ULONG(self.Y).value,
                    ULONG(self.Direction).value,
                    ULONG(self.Unknown2).value,
                    ULONG(self.ChipIndex).value,
                    ULONG(self.Unknown_11).value,
                    ULONG(self.NpcIndex).value,
                    ULONG(self.Unknown_14).value,
                    ULONG(self.InitScenaIndex).value,
                    ULONG(self.InitFunctionIndex).value,
                    ULONG(self.TalkScenaIndex).value,
                    ULONG(self.TalkFunctionIndex).value,
                    ULONG(self.Unknown4).value,
                    ULONG(self.Unknown5).value
                )

class BattleSepith:

    # size = 7

    def __init__(self, fs = None):
        self.Value = []

        if fs == None:
            for i in range(7):
                self.Value.append(0)
            return

        self.Offset = fs.tell()

        for i in range(7):
            self.Value.append(fs.ReadByte())

    def param(self):
        p = []
        for v in self.Value:
            p.append('%d' % v)

        p = ', '.join(p)

        space = [5] * 7
        return AdjustParam(p, space)

    def binary(self):
        return struct.pack('<' + 'B' * len(self.Value), *self.Value)

class BattleATBonus:

    # size = 0x10

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset     = fs.tell()

        self.Nothing    = fs.ReadByte()
        self.HP_HEAL_10 = fs.ReadByte()
        self.HP_HEAL_50 = fs.ReadByte()
        self.EP_HEAL_10 = fs.ReadByte()
        self.EP_HEAL_50 = fs.ReadByte()
        self.CP_HEAL_10 = fs.ReadByte()
        self.CP_HEAL_50 = fs.ReadByte()
        self.SEPITH     = fs.ReadByte()
        self.CRITICAL   = fs.ReadByte()
        self.VANISH     = fs.ReadByte()
        self.DEATH      = fs.ReadByte()
        self.GUARD      = fs.ReadByte()
        self.RUSH       = fs.ReadByte()
        self.ARTS_GUARD = fs.ReadByte()
        self.TEAMRUSH   = fs.ReadByte()
        self.Unknown    = fs.ReadByte()

    def param(self):
        return '"ATBonus_%X", %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d' % (
                    self.Offset,
                    self.Nothing,
                    self.HP_HEAL_10,
                    self.HP_HEAL_50,
                    self.EP_HEAL_10,
                    self.EP_HEAL_50,
                    self.CP_HEAL_10,
                    self.CP_HEAL_50,
                    self.SEPITH,
                    self.CRITICAL,
                    self.VANISH,
                    self.DEATH,
                    self.GUARD,
                    self.RUSH,
                    self.ARTS_GUARD,
                    self.TEAMRUSH,
                    self.Unknown
                )

    def __str__(self):
        return str(self.binary())

    def binary(self):
        return struct.pack(
                    '<' + 'B' * 0x10,
                    self.Nothing,
                    self.HP_HEAL_10,
                    self.HP_HEAL_50,
                    self.EP_HEAL_10,
                    self.EP_HEAL_50,
                    self.CP_HEAL_10,
                    self.CP_HEAL_50,
                    self.SEPITH,
                    self.CRITICAL,
                    self.VANISH,
                    self.DEATH,
                    self.GUARD,
                    self.RUSH,
                    self.ARTS_GUARD,
                    self.TEAMRUSH,
                    self.Unknown
                )

class BattleMonsterPostion:

    # size = 4

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset = fs.tell()

        self.X      = fs.ReadByte()
        self.Y      = fs.ReadByte()
        self.Degree = fs.ReadUShort()

    def __str__(self):
        return str(self.binary())

    def binary(self):
        return struct.pack('<BBH', self.X, self.Y, self.Degree)

    def param(self):
        return '"MonsterBattlePostion_%X", %d, %d, %d' % (self.Offset, self.X, self.Y, self.Degree)

class BattleMonsterInfo:

    # size = 0x2C

    def __init__(self, fs = None):
        if fs == None:
            self.MsFileIndex = [BattleScriptFileIndex()] * 8
            return

        self.Offset = fs.tell()

        self.MsFileIndex = []
        for i in range(8):
            self.MsFileIndex.append(BattleScriptFileIndex(fs.ReadULong()))

        self.PositionNormalOffset           = fs.ReadUShort()
        self.PositionEnemyAdvantageOffset   = fs.ReadUShort()
        self.BgmNormal                      = fs.ReadUShort()
        self.BgmDanger                      = fs.ReadUShort()
        self.ATBonusOffset                  = fs.ReadULong()

        pos = fs.tell()

        self.PositionNormal = []
        fs.seek(self.PositionNormalOffset)
        for i in range(len(self.MsFileIndex)):
            self.PositionNormal.append(BattleMonsterPostion(fs))

        self.PositionEnemyAdvantage = []
        fs.seek(self.PositionEnemyAdvantageOffset)
        for i in range(len(self.MsFileIndex)):
            self.PositionEnemyAdvantage.append(BattleMonsterPostion(fs))

        fs.seek(self.ATBonusOffset)
        self.ATBonus = BattleATBonus(fs)

        fs.seek(pos)

    def param(self):
        p = ''
        for ms in self.MsFileIndex:
            name = '0' if ms.IsInvalid() else ('"%s"' % ms.Name())
            p += '%s, ' % name

        return p + '"MonsterBattlePostion_%X", "MonsterBattlePostion_%X", "%s", "%s", "ATBonus_%X"' % (
                    self.PositionNormalOffset,
                    self.PositionEnemyAdvantageOffset,
                    BGMFileIndex(self.BgmNormal).Name(),
                    BGMFileIndex(self.BgmDanger).Name(),
                    self.ATBonusOffset
                )

    def binary(self):
        if len(self.MsFileIndex) != 8:
            raise Exception('incorrect ms file count')

        buf = b''
        for i in self.MsFileIndex:
            buf += struct.pack('<L', i.Index())

        return buf + struct.pack('<HHHHL', self.PositionNormalOffset, self.PositionEnemyAdvantageOffset, self.BgmNormal, self.BgmDanger, self.ATBonusOffset)

class ScenarioBattleInfo:

    # size = 0x18

    def binary(self):
        return struct.pack(
                    '<HHBBBBHHLLBBBB',
                    self.Flags,
                    self.Level,
                    self.Unknown_04,
                    self.Vision,
                    self.MoveRange,
                    self.CanMove,
                    self.MoveSpeed,
                    self.Unknown_0A,
                    self.BattleMapOffset,
                    self.SepithOffset,
                    self.Probability[0],
                    self.Probability[1],
                    self.Probability[2],
                    self.Probability[3]
                )

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset             = fs.tell()

        self.Flags              = fs.ReadUShort()
        self.Level              = fs.ReadUShort()
        self.Unknown_04         = fs.ReadByte()
        self.Vision             = fs.ReadByte()
        self.MoveRange          = fs.ReadByte()
        self.CanMove            = fs.ReadByte()
        self.MoveSpeed          = fs.ReadUShort()
        self.Unknown_0A         = fs.ReadUShort()
        self.BattleMapOffset    = fs.ReadULong()
        self.SepithOffset       = fs.ReadULong()
        self.Probability        = [ fs.ReadByte(), fs.ReadByte(), fs.ReadByte(), fs.ReadByte() ]

        pos = fs.tell()

        fs.seek(self.BattleMapOffset)
        self.BattleMap = fs.ReadMultiByte(CODE_PAGE)

        self.Sepith = None
        if self.SepithOffset != 0:
            fs.seek(self.SepithOffset)
            self.Sepith = BattleSepith(fs)

        fs.seek(pos)

        self.MonsterBattleInfo = []
        for p in self.Probability:
            if p == 0:
                self.MonsterBattleInfo.append(BattleMonsterInfo())
                continue

            self.MonsterBattleInfo.append(BattleMonsterInfo(fs))

        fs.seek(pos)

    def param(self):
        sepithfmt = '"Sepith_%X"' if self.Sepith != None else '0x%08X'
        return ('"BattleInfo_%X", 0x%04X, %d, %d, %d, %d, %d, %d, %d, "%s", ' + sepithfmt + ', %d, %d, %d, %d') % (
                    ULONG(self.Offset).value,
                    LONG(self.Flags).value,
                    LONG(self.Level).value,
                    LONG(self.Unknown_04).value,
                    LONG(self.Vision).value,
                    LONG(self.MoveRange).value,
                    LONG(self.CanMove).value,
                    LONG(self.MoveSpeed).value,
                    LONG(self.Unknown_0A).value,
                    self.BattleMap,
                    ULONG(self.SepithOffset).value,
                    LONG(self.Probability[0]).value,
                    LONG(self.Probability[1]).value,
                    LONG(self.Probability[2]).value,
                    LONG(self.Probability[3]).value
                )

class ScenarioChipFrameInfo:

    # size = 0xC

    def __init__(self, fs = None):
        if fs == None:
            return

        self.Offset = fs.tell()

        self.Speed          = fs.ReadUShort()
        self.Reserve        = fs.ReadByte()
        self.SubChipCount   = fs.ReadByte()
        self.SubChipIndex   = struct.unpack('<' + 'B' * self.SubChipCount, fs.read(self.SubChipCount))

        if self.SubChipCount != 8:
            fs.seek(8 - self.SubChipCount, io.SEEK_CUR)

    def param(self):
        s = ''
        if len(self.SubChipIndex) != 0:
            s = ', ['
            for idx in self.SubChipIndex:
                s += '%d, ' % idx

            s = s[:-2] + ']'

        return ('%d, %d' % (self.Speed, self.Reserve)) + s

    def binary(self):
        buf = struct.pack('<HBB' + 'B' * len(self.SubChipIndex), self.Speed, self.Reserve, len(self.SubChipIndex), *self.SubChipIndex)

        if len(buf) < 0xC:
            buf += b'\x00' * (0xC - len(buf))
        elif len(buf) > 0xC:
            raise Exception('too long')

        return buf

class ScenarioMonsterInfo:
    def __init__(self, fs = None):
        if fs == None:
            return

        # size = 0x20

        self.X                      = fs.ReadULong()
        self.Z                      = fs.ReadULong()
        self.Y                      = fs.ReadULong()
        self.Unknown_0C             = fs.ReadULong()
        self.BattleInfoOffset       = fs.ReadUShort()
        self.Unknown_12             = fs.ReadUShort()
        self.ChipIndex              = fs.ReadUShort()
        self.Unknown_16             = fs.ReadUShort()
        self.StandFrameInfoIndex    = fs.ReadULong()
        self.MoveFrameInfoIndex     = fs.ReadULong()

        pos = fs.tell()
        fs.seek(self.BattleInfoOffset)
        self.BattleInfo = ScenarioBattleInfo(fs)
        fs.seek(pos)

    def __str__(self):
        return str(self.binary())

    def param(self):
        p = '%d, %d, %d, 0x%X, "BattleInfo_%X", %d, %d, 0x%X, %d, %d' % (
                    LONG(self.X).value,
                    LONG(self.Y).value,
                    LONG(self.Z).value,
                    ULONG(self.Unknown_0C).value,
                    ULONG(self.BattleInfoOffset).value,
                    LONG(self.Unknown_12).value,
                    LONG(self.ChipIndex).value,
                    USHORT(self.Unknown_16).value,
                    LONG(self.StandFrameInfoIndex).value,
                    LONG(self.MoveFrameInfoIndex).value
                )

        space = [9, 9, 9, strlen('BattleInfo') + 4, 5, 5, 5, 4, 4]
        return AdjustParam(p, space)

    def binary(self):
        return struct.pack('<LLLLHHHHLL',
                    ULONG(self.X).value,
                    ULONG(self.Y).value,
                    ULONG(self.Z).value,
                    ULONG(self.Unknown_0C).value,
                    ULONG(self.BattleInfoOffset).value,
                    ULONG(self.Unknown_12).value,
                    ULONG(self.ChipIndex).value,
                    ULONG(self.Unknown_16).value,
                    ULONG(self.StandFrameInfoIndex).value,
                    ULONG(self.MoveFrameInfoIndex).value
                )

class ScenarioEventInfo:
    # 0x60 bytes

    def __init__(self, fs = None):
        if fs == None:
            return

        self.X              = fs.ReadFloat()                # 0x00
        self.Y              = fs.ReadFloat()                # 0x04
        self.Z              = fs.ReadFloat()                # 0x08
        self.Range          = fs.ReadFloat()                # 0x0C

        self.UnknownFloat_10 = [0] * 0x10
        for i in range(len(self.UnknownFloat_10)):
            self.UnknownFloat_10[i] = fs.ReadFloat()        # 0x10 - 0x4C

        self.Flags          = fs.ReadUShort()       # 0x50
        self.ScenaIndex     = fs.ReadUShort()       # 0x52
        self.FunctionIndex  = fs.ReadUShort()       # 0x54
        self.Reserve        = fs.read(0xA)        # 0x56

        if self.Reserve != b'\x00' * len(self.Reserve): bp()

    #def __str__(self):
    #    return str(self.Binary)

    def param(self):
        #x = str(self.X)
        #z = str(self.Z)
        #y = str(self.Y)
        #rng = str(self.Range)
        #maxlen = max(len(x), len(z))
        #maxlen = max(maxlen, len(y))
        #maxlen = max(maxlen, len(rng))

        p = '0x%04X, %d, %d, %s, %s, %s, %s, ' % (
                    self.Flags,
                    self.ScenaIndex,
                    self.FunctionIndex,

                    self.X,
                    self.Y,
                    self.Z,
                    self.Range,
                )

        floats = ''
        for v in self.UnknownFloat_10:
            floats += '%s, ' % v

        floats = '[%s]' % floats[:-2]

        p = p + floats

        space = [8, 3, 5] + [23] * 4 + [23] * len(self.UnknownFloat_10)
        return AdjustParam(p, space)

    def binary(self):
        p = struct.pack(
                '<ffff' + 'f' * len(self.UnknownFloat_10),
                self.X, self.Y, self.Z, self.Range,
                *self.UnknownFloat_10
            )

        data = struct.pack('<HHH', self.Flags, self.ScenaIndex, self.FunctionIndex)

        bin = p + data
        return bin + b'\x00' * (0x60 - len(bin))

class ScenarioActorInfo:
    def __init__(self, fs = None):
        if fs == None:
            return

        # size = 0x24

        self.TriggerX           = fs.ReadULong()
        self.TriggerZ           = fs.ReadULong()
        self.TriggerY           = fs.ReadULong()
        self.TriggerRange       = fs.ReadULong()
        self.ActorX             = fs.ReadULong()
        self.ActorZ             = fs.ReadULong()
        self.ActorY             = fs.ReadULong()
        self.Flags              = fs.ReadUShort()
        self.TalkScenaIndex     = fs.ReadUShort()
        self.TalkFunctionIndex  = fs.ReadUShort()
        self.Unknown_22         = fs.ReadUShort()

    def __str__(self):
        return str(self.Binary)

    def param(self):
        p = '%d, %d, %d, %d, %d, %d, %d, 0x%04X, %d, %d, 0x%04X' % (
                    LONG(self.TriggerX).value,
                    LONG(self.TriggerZ).value,
                    LONG(self.TriggerY).value,
                    LONG(self.TriggerRange).value,
                    LONG(self.ActorX).value,
                    LONG(self.ActorZ).value,
                    LONG(self.ActorY).value,

                    USHORT(self.Flags).value,
                    USHORT(self.TalkScenaIndex).value,
                    USHORT(self.TalkFunctionIndex).value,
                    USHORT(self.Unknown_22).value,
                )

        space = [9, 9, 9, 9, 9, 9, 9, 4, 4, 4, 4]
        return AdjustParam(p, space)

    def binary(self):
        return struct.pack('<lllllllHHHH',
                    LONG(self.TriggerX).value,
                    LONG(self.TriggerZ).value,
                    LONG(self.TriggerY).value,
                    LONG(self.TriggerRange).value,
                    LONG(self.ActorX).value,
                    LONG(self.ActorZ).value,
                    LONG(self.ActorY).value,

                    USHORT(self.Flags).value,
                    USHORT(self.TalkScenaIndex).value,
                    USHORT(self.TalkFunctionIndex).value,
                    USHORT(self.Unknown_22).value
                )

class ScenarioPlaceNameInfo:

    # size = 0x14

    def __init__(self, fs = None):
        if fs == None:
            return

        self.X          = fs.ReadFloat()
        self.Z          = fs.ReadFloat()
        self.Y          = fs.ReadFloat()
        self.Flags1     = fs.ReadUShort()
        self.Flags2     = fs.ReadUShort()
        self.NameOffset = fs.ReadULong()

        pos = fs.tell()
        fs.seek(self.NameOffset)

        self.Name = fs.ReadMultiByte(CODE_PAGE)

        fs.seek(pos)

    def param(self):
        return '%s, %s, %s, 0x%04X, 0x%04X, "%s"' % (self.X, self.Z, self.Y, self.Flags1, self.Flags2, self.Name)

    def binary(self):
        return struct.pack('<fffHHL', self.X, self.Z, self.Y, self.Flags1, self.Flags2, self.NameOffset)


class ScenarioInitData:

    # size = 0x40

    def __init__(self, fs = None):
        self.PackFormat = '<iiiiiiiiHHHHiiiHHHHBBBB'

        if fs == None:
            return

        if IsTupleOrList(fs):
            return self.__init__(fileio.FileStream(struct.pack(self.PackFormat, *fs)))

        self.Unknown_00             = fs.ReadLong()    # 0x00
        self.Unknown_04             = fs.ReadLong()    # 0x04
        self.Unknown_08             = fs.ReadLong()    # 0x08
        self.Unknown_0C             = fs.ReadLong()    # 0x0C
        self.Unknown_10             = fs.ReadLong()    # 0x10
        self.Unknown_14             = fs.ReadLong()    # 0x14
        self.Unknown_18             = fs.ReadLong()    # 0x18
        self.Unknown_1C             = fs.ReadLong()    # 0x1C
        self.Unknown_20             = fs.ReadUShort()   # 0x20
        self.Unknown_22             = fs.ReadUShort()   # 0x22
        self.Unknown_24             = fs.ReadUShort()   # 0x24
        self.Unknown_26             = fs.ReadUShort()   # 0x26
        self.Unknown_28             = fs.ReadLong()    # 0x28
        self.Unknown_2C             = fs.ReadLong()    # 0x2C
        self.Unknown_30             = fs.ReadLong()    # 0x30
        self.Unknown_34             = fs.ReadUShort()   # 0x34
        self.Unknown_36             = fs.ReadUShort()   # 0x36
        self.Flags                  = fs.ReadUShort()   # 0x38
        self.Unknown_3A             = fs.ReadUShort()   # 0x3A

        self.InitScenaIndex         = fs.ReadByte()     # 0x3C
        self.InitFunctionIndex      = fs.ReadByte()     # 0x3D
        self.EntryScenaIndex        = fs.ReadByte()     # 0x3E
        self.EntryFunctionIndex     = fs.ReadByte()     # 0x3F

    def param(self):
        p = ('%d, ' * 23) % (
                self.Unknown_00,
                self.Unknown_04,
                self.Unknown_08,
                self.Unknown_0C,
                self.Unknown_10,
                self.Unknown_14,
                self.Unknown_18,
                self.Unknown_1C,
                self.Unknown_20,
                self.Unknown_22,
                self.Unknown_24,
                self.Unknown_26,
                self.Unknown_28,
                self.Unknown_2C,
                self.Unknown_30,
                self.Unknown_34,
                self.Unknown_36,
                self.Flags,
                self.Unknown_3A,
                self.InitScenaIndex,
                self.InitFunctionIndex,
                self.EntryScenaIndex,
                self.EntryFunctionIndex,
            )

        return p[:-2]

    def binary(self):
        bin = struct.pack(self.PackFormat,
                self.Unknown_00,
                self.Unknown_04,
                self.Unknown_08,
                self.Unknown_0C,
                self.Unknown_10,
                self.Unknown_14,
                self.Unknown_18,
                self.Unknown_1C,
                self.Unknown_20,
                self.Unknown_22,
                self.Unknown_24,
                self.Unknown_26,
                self.Unknown_28,
                self.Unknown_2C,
                self.Unknown_30,
                self.Unknown_34,
                self.Unknown_36,
                self.Flags,
                self.Unknown_3A,
                self.InitScenaIndex,
                self.InitFunctionIndex,
                self.EntryScenaIndex,
                self.EntryFunctionIndex
            )

        return bin


class ScenarioInfo:
    def __init__(self):
        # file header

        self.MapName                    = ''
        self.Location                   = ''
        self.MapIndex                   = 0
        self.MapDefaultBGM              = -1
        self.Flags                      = 0
        self.IncludedScenario           = []
        self.StringTableOffset          = 0
        self.ScnInfoOffset              = [0] * SCN_INFO_MAXIMUM
        self.ScenaFunctionTable         = ScenarioEntry()
        self.ChipFrameInfoOffset        = 0
        self.PlaceNameOffset            = 0
        self.PlaceNameNumber            = 0
        self.PreInitFunctionIndex       = 0
        self.ScnInfoNumber              = [0] * SCN_INFO_MAXIMUM
        self.Unknown_51                 = b''
        self.InitData                   = ScenarioInitData()

        # file header end

        self.ScenaFunctions     = []
        self.PlaceName          = []
        self.ChipFrameInfo      = []
        self.StringTable        = []
        self.ScnInfo            = []
        self.CodeBlocks         = []
        self.BattleInfoRefs     = []

        self.GlobalLabelTable   = {}

        for i in range(SCN_INFO_MAXIMUM):
            self.ScnInfo.append([])
            #self.ScnInfoOffset.append(0)
            #self.ScnInfoNumber.append(0)

    def binary(self):
        MapName = self.MapName.encode(CODE_PAGE)
        if len(MapName) < 0xA:
            MapName += b'\x00' * (0xA - len(MapName))
        elif len(MapName) > 0xA:
            MapName = MapName[:0xA]

        Location = self.Location.encode(CODE_PAGE)
        if len(Location) < 0xA:
            Location += b'\x00' * (0xA - len(Location))
        elif len(Location) > 0xA:
            Location = Location[:0xA]

        MapIndex = struct.pack('<H', self.MapIndex)
        MapDefaultBGM = struct.pack('<h', self.MapDefaultBGM.Index())
        Flags = struct.pack('<L', self.Flags)

        IncludedScenario = b''
        for inc in self.IncludedScenario:
            IncludedScenario += struct.pack('<L', inc)

        StringTableOffset = struct.pack('<L', self.StringTableOffset)

        ScnInfoOffset = b''
        ScnInfoNumber = b''
        for i in range(len(self.ScnInfoNumber)):
            ScnInfoOffset += struct.pack('<H', self.ScnInfoOffset[i])
            ScnInfoNumber += struct.pack('<B', self.ScnInfoNumber[i])

        ScenaFunctionTable = struct.pack('<HH', self.ScenaFunctionTable.Offset, self.ScenaFunctionTable.Size)

        ChipFrameInfoOffset = struct.pack('<H', self.ChipFrameInfoOffset)

        PlaceNameOffset = struct.pack('<H', self.PlaceNameOffset)
        PlaceNameNumber = struct.pack('<B', self.PlaceNameNumber)

        PreInitFunctionIndex = struct.pack('<B', self.PreInitFunctionIndex)
        Unknown_51 = struct.pack('<BBB', self.Unknown_51[0], self.Unknown_51[1], self.Unknown_51[2])

        Information = self.InitData.binary()

        return MapName + \
                Location + \
                MapIndex + MapDefaultBGM + \
                Flags + \
                IncludedScenario + \
                StringTableOffset + \
                ScnInfoOffset + \
                ScenaFunctionTable + \
                ChipFrameInfoOffset + \
                PlaceNameOffset + \
                PlaceNameNumber + \
                PreInitFunctionIndex + \
                ScnInfoNumber + \
                Unknown_51 + \
                Information

    def open(self, scenafile):

        fs = fileio.FileStream(scenafile)

        # file header

        self.MapName                    = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.Location                   = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.MapIndex                   = fs.ReadUShort()
        self.MapDefaultBGM              = BGMFileIndex(fs.ReadShort())
        self.Flags                      = fs.ReadULong()
        self.IncludedScenario           = list(struct.unpack('<' + 'I' * NUMBER_OF_INCLUDE_FILE, fs.read(NUMBER_OF_INCLUDE_FILE * 4)))
        self.StringTableOffset          = fs.ReadULong()
        self.ScnInfoOffset              = list(struct.unpack('<' + 'H' * SCN_INFO_MAXIMUM, fs.read(SCN_INFO_MAXIMUM * 2)))
        self.ScenaFunctionTable         = ScenarioEntry(fs.ReadUShort(), fs.ReadUShort())
        self.ChipFrameInfoOffset        = fs.ReadUShort()
        self.PlaceNameOffset            = fs.ReadUShort()
        self.PlaceNameNumber            = fs.ReadByte()
        self.PreInitFunctionIndex       = fs.ReadByte()
        self.ScnInfoNumber              = list(struct.unpack('<' + 'B' * SCN_INFO_MAXIMUM, fs.read(SCN_INFO_MAXIMUM * 1)))
        self.Unknown_51                 = fs.read(3)
        self.InitData                   = ScenarioInitData(fs)

        self.IncludedScenario.index(0xFFFFFFFF)

        # file header end

        #if self.PlaceNameOffset != 0: raise Exception('not implemented')

        self.InitScenaInfo(fs)
        self.InitOtherInfo(fs)

        self.CodeBlocks = self.DisassembleBlocks(fs)

        self.InitMapNameList(scenafile)


    def InitMapNameList(self, scenafile):

        self.MapNameList = []

        try:
            t_town = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(scenafile)), '../text/t_town._dt'))
            town = BytesStream()
            town.open(t_town)

            offsetlist = []
            for i in range(town.ReadUShort()):
                offsetlist.append(town.ReadUShort())

            for offset in offsetlist:
                town.seek(offset)
                self.MapNameList.append(town.ReadMultiByte(CODE_PAGE))

        except:
            self.MapNameList = []

    def GetMapNameByIndex(self, index):
        if index == 0 or index >= len(self.MapNameList):
            return ''

        return self.MapNameList[index]

    def InitScenaInfo(self, fs):
        ScnInfoTypes = \
        [
            ScenarioChipInfo,
            ScenarioNpcInfo,
            ScenarioMonsterInfo,
            ScenarioEventInfo,
            ScenarioActorInfo,
        ]

        for i in range(len(self.ScnInfoOffset)):
            fs.seek(self.ScnInfoOffset[i])
            ScnInfoType = ScnInfoTypes[i]
            for n in range(self.ScnInfoNumber[i]):
                self.ScnInfo[i].append(ScnInfoType(fs))

    def InitOtherInfo(self, fs):

        fs.seek(self.PlaceNameOffset)
        for i in range(self.PlaceNameNumber):
            self.PlaceName.append(ScenarioPlaceNameInfo(fs))

        fs.seek(self.ScenaFunctionTable.Offset)
        self.ScenaFunctions = list(struct.unpack('<' + 'I' * int(self.ScenaFunctionTable.Size / 4), fs.read(self.ScenaFunctionTable.Size)))


        ChipFrameInfoNumber = 0
        for monster in self.ScnInfo[SCN_INFO_MONSTER]:
            ChipFrameInfoNumber = max(ChipFrameInfoNumber, max(monster.StandFrameInfoIndex, monster.MoveFrameInfoIndex))

        fs.seek(self.ChipFrameInfoOffset)
        self.ChipFrameInfo = []
        for i in range(ChipFrameInfoNumber + 1):
            self.ChipFrameInfo.append(ScenarioChipFrameInfo(fs))

        fs.seek(self.StringTableOffset)

        buf = fs.read()
        endmz = buf.find(b'\x00\x00')
        if endmz != -1:
            buf = buf[:endmz]

        stringtable = buf.decode(CODE_PAGE).rstrip('\x00').split('\x00')
        for string in stringtable:
            #if string in self.StringTable: continue
            self.StringTable.append(string)

    def DiasmInstructionCallback(self, data):
        if data.Reason != HANDLER_REASON_DISASM:
            return

        inst, fs = data.Instruction, data.FileStream

        if inst.OpCode == edao.Battle:
            BattleInfoOffset = inst.Operand[0]
            if BattleInfoOffset == 0xFFFFFFFF:
                return

            pos = fs.tell()
            fs.seek(BattleInfoOffset)
            self.BattleInfoRefs.append(ScenarioBattleInfo(fs))
            fs.seek(pos)

    def DisassembleBlocks(self, fs):
        disasm = Disassembler(edao.edao_op_table, self.DiasmInstructionCallback)

        index = -1
        codeblocks = []
        blockoffsetmap = {}
        for func in self.ScenaFunctions:
            index += 1
            if func in blockoffsetmap:
                codeblocks.append(blockoffsetmap[func])
                continue

            fs.seek(func)

            data = Disassembler.DisasmData()
            data.Stream = fs
            data.GlobalLabelTable = self.GlobalLabelTable

            block = disasm.DisasmBlock2(data)

            block.Name = 'Function_%d_%X' % (index, block.Offset)
            codeblocks.append(block)

            blockoffsetmap[func] = block

        #for i in range(fs.size()): if i not in offsetlist: print('%X' % i)
        #input()

        return codeblocks

    def GenerateFunctionLabelList(self, blocks):
        l = []
        for block in blocks:
            l.append(block.Name)
            l += self.GenerateFunctionLabelList(block.CodeBlocks)

        return l

    def FormatInstructionCallback(self, data):
        pass

    def FormatCodeBlocks(self):

        edao.edao_op_table.FunctionLabelList = self.GenerateFunctionLabelList(self.CodeBlocks)
        disasm = Disassembler(edao.edao_op_table, self.FormatInstructionCallback)

        blocks = []
        blockoffsetmap = {}

        for block in self.CodeBlocks:
            if block.Offset in blockoffsetmap:
                continue

            blockoffsetmap[block.Offset] = True

            data = Disassembler.FormatData()

            data.Block = block
            data.GlobalLabelTable = self.GlobalLabelTable

            blocks.append(['def %s(): pass' % block.Name])
            blocks.append(disasm.FormatCodeBlock2(data))

        #for x in disasmtbl: print('%08X' % x)
        #input()

        return blocks

    def GenerateSingleBattleInfo(self, btinfo, offsetmap):
        battleinfolines = []
        sepithlines     = []
        monposlines     = []
        atbonuslines    = []

        if btinfo.Offset in offsetmap:
            return (battleinfolines, sepithlines, monposlines, atbonuslines)

        offsetmap[btinfo.Offset] = True

        if btinfo.Sepith != None and btinfo.Sepith.Offset not in offsetmap:
            offsetmap[btinfo.Sepith.Offset] = True
            sepithlines.append('Sepith("Sepith_%X", %s)' % (btinfo.Sepith.Offset, btinfo.Sepith.param()))

        monbtinfolines = []
        monbtinfolines.append('    (')

        for i in range(len(btinfo.Probability)):
            if btinfo.Probability[i] == 0:
                monbtinfolines.append('        (),')
                continue

            monbtinfo = btinfo.MonsterBattleInfo[i]

            for posinfo in monbtinfo.PositionNormal:
                if posinfo.Offset in offsetmap:
                    continue

                offsetmap[posinfo.Offset] = True
                monposlines.append('MonsterBattlePostion(%s)' % posinfo.param())

            for posinfo in monbtinfo.PositionEnemyAdvantage:
                if posinfo.Offset in offsetmap:
                    continue

                offsetmap[posinfo.Offset] = True
                monposlines.append('MonsterBattlePostion(%s)' % posinfo.param())

            if monbtinfo.ATBonus.Offset not in offsetmap:
                offsetmap[monbtinfo.ATBonus.Offset] = True
                atbonuslines.append('ATBonus(%s)' % monbtinfo.ATBonus.param())

            monbtinfolines.append('        (%s),' % monbtinfo.param())

        monbtinfolines.append('    )')

        battleinfolines.append('BattleInfo(')
        battleinfolines.append('    %s,' % btinfo.param())
        battleinfolines += monbtinfolines
        battleinfolines.append(')')
        battleinfolines.append('')

        return (battleinfolines, sepithlines, monposlines, atbonuslines)

    def GenerateBattleInfo(self):
        battleinfolines = []
        sepithlines     = []
        monposlines     = []
        atbonuslines    = []

        btcount = 0

        offsetmap = {}

        for monster in self.ScnInfo[SCN_INFO_MONSTER]:
            btcount += 1
            btinfo = monster.BattleInfo

            r = self.GenerateSingleBattleInfo(btinfo, offsetmap)

            battleinfolines += r[0]
            sepithlines     += r[1]
            monposlines     += r[2]
            atbonuslines    += r[3]

        if len(self.BattleInfoRefs) != 0:
            battleinfolines.append('# event battle count: %d' % len(self.BattleInfoRefs))
            battleinfolines.append('')

            for btinfo in self.BattleInfoRefs:
                r = self.GenerateSingleBattleInfo(btinfo, offsetmap)
                battleinfolines += r[0]
                sepithlines     += r[1]
                monposlines     += r[2]
                atbonuslines    += r[3]

        if len(atbonuslines) != 0:
            atbonuslines += ['']

        if len(sepithlines) != 0:
            sepithlines += ['']

        if len(monposlines) != 0:
            monposlines += ['']

        if len(battleinfolines) != 0:
            battleinfolines.insert(0, '# monster count: %d' % btcount)
            battleinfolines.insert(1, '')

        return atbonuslines + sepithlines + monposlines + battleinfolines

    def GenerateStringList(self):

        lines = []

        if len(self.StringTable) == 0:
            return lines

        index = 0
        lines.append('BuildStringList((')
        for string in self.StringTable:
            x = ljust_cn('    "%s",' % string, 30)
            lines.append(x + '# %d' % index)
            index += 1

        lines.append('))')
        lines.append('')

        return lines

    def GenerateHeader(self, filename):

        filename = os.path.splitext(os.path.splitext(os.path.basename(filename))[0])[0] + '.bin'

        mapname = self.GetMapNameByIndex(self.MapIndex)
        mapname = mapname if mapname != '' else 'MapIndex'

        hdr = []
        hdr.append('from ScenarioHelper import *')
        hdr.append('')
        hdr.append('CreateScenaFile(')
        hdr.append('    "%s",                # FileName'        % filename)
        hdr.append('    "%s",                    # MapName'     % self.MapName)
        hdr.append('    "%s",                    # Location'    % self.Location)
        hdr.append('    0x%04X,                     # %s'       % (self.MapIndex, mapname))
        hdr.append('    %s,'                                    % self.MapDefaultBGM.param())
        hdr.append('    0x%08X,                 # Flags'        % self.Flags)

        include = ''
        for scp in self.IncludedScenario:
            include += '"%s", ' % ScenarioFileIndex(scp).Name()

        hdr.append('    (%s),   # include' % include[:-2])
        hdr.append('    0x%02X,                       # PlaceNameNumber' % self.PlaceNameNumber)
        hdr.append('    0x%02X,                       # PreInitFunctionIndex' % self.PreInitFunctionIndex)
        hdr.append('    %s,            # Unknown_51' % self.Unknown_51)
        hdr.append('')
        hdr.append('    # Information')
        hdr.append('    [%s],' % self.InitData.param())

        hdr.append(')')
        hdr.append('')

        hdr += self.GenerateStringList()
        hdr += self.GenerateBattleInfo()

        if len(self.ScnInfo[SCN_INFO_CHIP]) != 0:
            hdr.append('AddCharChip((')

            index = 0
            for chip in self.ScnInfo[SCN_INFO_CHIP]:
                x = ('    %s,' % chip.param()).ljust(40)
                x += ' # %02X' % index
                hdr.append(x)
                index += 1

            hdr.append('))')
            hdr.append('')

        def AppendScpInfo(info, func):
            if len(info) == 0:
                return

            for i in info:
                hdr.append('%s(%s)' % (func, i.param()))

            hdr.append('')

        AppendScpInfo(self.ScnInfo[SCN_INFO_NPC],       'DeclNpc')
        AppendScpInfo(self.ScnInfo[SCN_INFO_MONSTER],   'DeclMonster')
        AppendScpInfo(self.ScnInfo[SCN_INFO_EVENT],     'DeclEvent')
        AppendScpInfo(self.ScnInfo[SCN_INFO_ACTOR],     'DeclActor')

        if len(self.PlaceName) != 0:
            for place in self.PlaceName:
                s = 'PlaceName(%s)' % place.param()
                hdr.append(s)

            hdr.append('')

        if len(self.ChipFrameInfo) != 0:
            #hdr.append('ChipFrameList((')
            index = 0
            for frame in self.ChipFrameInfo:
                func = 'ChipFrameInfo(%s)' % frame.param()
                hdr.append('%s # %d' % (ljust_cn(func, 60), index))
                index += 1

            #hdr.append('))')
            hdr.append('')

        hdr.append('ScpFunction((')
        index = 0
        for block in self.CodeBlocks:
            s = ljust_cn('    "%s",' % block.Name, 30)
            s += ' # %02X, %d' % (index, index)
            hdr.append(s)
            index += 1

        hdr.append('))')
        hdr.append('')

        hdr.append('')

        return hdr

    def SaveToFile(self, filename, append_place_name = True):
        lines = []

        lines += self.GenerateHeader(filename)

        blocks = self.FormatCodeBlocks()

        for block in blocks:
            lines += block

        lines.append('SaveToFile()')
        lines.append('')

        #txt = '\r\n'.join(lines)
        #lines = txt.replace('\r\n', '\n').replace('\r', '\n').split('\n')

        for i in range(2, len(lines)):
            if lines[i] != '':
                lines[i] = '    ' + lines[i]

        lines.insert(2, 'def main():')
        lines.append('Try(main)')
        lines.append('')

        if append_place_name:
            debugmap = ['a0000', 'map1', 'a0002']
            if self.MapName.lower() not in debugmap:
                mapname = self.GetMapNameByIndex(self.MapIndex)

                if mapname != '':
                    ext = ''
                    while True:
                        filename, ext2 = os.path.splitext(filename)
                        if ext2 == '':
                            break
                        ext = ext2 + ext

                    filename = '%s.%s%s' % (filename, mapname, ext)

        fs = open(filename, 'wb')
        fs.write(''.encode('utf_8_sig'))
        fs.write('\r\n'.join(lines).encode('UTF8'))

    def __str__(self):
        info = []
        info.append('MapName                = %s' % self.MapName)
        info.append('Location               = %s' % self.Location)
        info.append('MapIndex               = %08X' % self.MapIndex)
        info.append('MapDefaultBGM          = %s' % self.MapDefaultBGM.Name())
        info.append('Flags                  = %08X' % self.Flags)

        buf = 'IncludedScenario       = '
        for include in self.IncludedScenario:
            buf += '%08X ' % include

        info.append(buf)

        info.append('StringTableOffset          = %08X' % (self.StringTableOffset))

        info.append('')
        info.append('ScnInfoOffset    ScnInfoNumber')
        for i in range(len(self.ScnInfoOffset)):
            info.append('  %08X          %08X' % (self.ScnInfoOffset[i], self.ScnInfoNumber[i]))
        info.append('')

        ScnInfoNames = \
        [
            'ChipInfo',
            'NpcInformation',
            'MonsterInformation',
            'ScpInfo',
            'InfoUnknown1',
        ]

        info.append('ScnInfo:')
        for i in range(len(self.ScnInfo)):
            info.append('  %s:' % ScnInfoNames[i])
            for scninfo in self.ScnInfo[i]:
                info.append('    %s' % scninfo)

            info.append('')

        info.append('')

        info.append('ScenaFunctionTable         = %04X, %04X' % (self.ScenaFunctionTable.Offset, self.ScenaFunctionTable.Size))
        info.append('ChipFrameInfoOffset        = %04X' % self.ChipFrameInfoOffset)
        info.append('PlaceNameOffset            = %04X' % self.PlaceNameOffset)
        info.append('PlaceNameNumber            = %02X' % (self.PlaceNameNumber))
        info.append('PreInitFunctionIndex       = %02X' % (self.PreInitFunctionIndex))
        info.append('Unknown_51                 = %s' % self.Unknown_51)

        info.append('')
        #info.append('Information:')
        #info.append('%s' % (self.InitData))
        #info.append('')

        info.append('ScenaFunctions:')
        for sec in self.ScenaFunctions:
            info.append('  %08X' % sec)
        info.append('')

        info.append('NpcName:')
        for i in range(len(self.NpcName)):
            info.append('  %2d.%s' % (i + 1, self.NpcName[i]))
        info.append('')

        return '\r\n'.join(info)


def procfile(file):
    console.setTitle(os.path.basename(file))
    print('disasm %s' % file)
    scena = ScenarioInfo()
    scena.open(file)
    scena.SaveToFile(file + '.py')

if __name__ == '__main__':
    iterlib.forEachFileMP(procfile, sys.argv[1:], '*.bin')
