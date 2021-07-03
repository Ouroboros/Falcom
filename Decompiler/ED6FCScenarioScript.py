from Assembler.Assembler2 import *
from Base.ED6FCBase import *
import Instruction.ScenaOpTableED6FC as ed6fc

ExtractText = not True
# ed6fc.CODE_PAGE = '932'
CODE_PAGE = ed6fc.CODE_PAGE

NUMBER_OF_INCLUDE_FILE  = 8

SCN_INFO_CHIP           = 0
SCN_INFO_CHIP_PAT       = 1
SCN_INFO_NPC            = 2
SCN_INFO_MONSTER        = 3
SCN_INFO_EVENT          = 4
SCN_INFO_ACTOR          = 5
SCN_INFO_MAXIMUM        = 6

textPosTable = OrderedDict()
replaceOption = {}

class ScenarioEntry:
    def __init__(self, offset = 0, size = 0):
        self.Offset = offset
        self.Size = size

class ScenarioEntryPoint:
    def __init__(self, fs = None):
        # size = 0x44

        if fs is None:
            fs = fileio.FileStream(b'\x00' * 0x44)

        self.Unknown_00         = fs.ReadLong()
        self.Unknown_04         = fs.ReadLong()
        self.Unknown_08         = fs.ReadLong()
        self.Unknown_0C         = fs.ReadUShort()
        self.Unknown_0E         = fs.ReadUShort()
        self.Unknown_10         = fs.ReadLong()
        self.Unknown_14         = fs.ReadLong()
        self.Unknown_18         = fs.ReadLong()
        self.Unknown_1C         = fs.ReadLong()
        self.Unknown_20         = fs.ReadLong()
        self.Unknown_24         = fs.ReadLong()
        self.Unknown_28         = fs.ReadLong()
        self.Unknown_2C         = fs.ReadLong()
        self.Unknown_30         = fs.ReadUShort()
        self.Unknown_32         = fs.ReadUShort()
        self.Unknown_34         = fs.ReadUShort()
        self.Unknown_36         = fs.ReadUShort()
        self.Unknown_38         = fs.ReadUShort()
        self.Unknown_3A         = fs.ReadUShort()
        self.InitScenaIndex     = fs.ReadUShort()
        self.InitFunctionIndex  = fs.ReadUShort()        # byte
        self.EntryScenaIndex    = fs.ReadUShort()
        self.EntryFunctionIndex = fs.ReadUShort()       # byte

    def params(self):
        align = 24
        return [
            '%s %s,' % (alignFormatKw(align, 'Unknown_00'),         self.Unknown_00),
            '%s %s,' % (alignFormatKw(align, 'Unknown_04'),         self.Unknown_04),
            '%s %s,' % (alignFormatKw(align, 'Unknown_08'),         self.Unknown_08),
            '%s %s,' % (alignFormatKw(align, 'Unknown_0C'),         self.Unknown_0C),
            '%s %s,' % (alignFormatKw(align, 'Unknown_0E'),         self.Unknown_0E),
            '%s %s,' % (alignFormatKw(align, 'Unknown_10'),         self.Unknown_10),
            '%s %s,' % (alignFormatKw(align, 'Unknown_14'),         self.Unknown_14),
            '%s %s,' % (alignFormatKw(align, 'Unknown_18'),         self.Unknown_18),
            '%s %s,' % (alignFormatKw(align, 'Unknown_1C'),         self.Unknown_1C),
            '%s %s,' % (alignFormatKw(align, 'Unknown_20'),         self.Unknown_20),
            '%s %s,' % (alignFormatKw(align, 'Unknown_24'),         self.Unknown_24),
            '%s %s,' % (alignFormatKw(align, 'Unknown_28'),         self.Unknown_28),
            '%s %s,' % (alignFormatKw(align, 'Unknown_2C'),         self.Unknown_2C),
            '%s %s,' % (alignFormatKw(align, 'Unknown_30'),         self.Unknown_30),
            '%s %s,' % (alignFormatKw(align, 'Unknown_32'),         self.Unknown_32),
            '%s %s,' % (alignFormatKw(align, 'Unknown_34'),         self.Unknown_34),
            '%s %s,' % (alignFormatKw(align, 'Unknown_36'),         self.Unknown_36),
            '%s %s,' % (alignFormatKw(align, 'Unknown_38'),         self.Unknown_38),
            '%s %s,' % (alignFormatKw(align, 'Unknown_3A'),         self.Unknown_3A),
            '%s %s,' % (alignFormatKw(align, 'InitScenaIndex'),     self.InitScenaIndex),
            '%s %s,' % (alignFormatKw(align, 'InitFunctionIndex'),  self.InitFunctionIndex),
            '%s %s,' % (alignFormatKw(align, 'EntryScenaIndex'),    self.EntryScenaIndex),
            '%s %s,' % (alignFormatKw(align, 'EntryFunctionIndex'), self.EntryFunctionIndex),
        ]

    def binary(self):
        return struct.pack('<LLLHHLLLLLLLLHHHHHHHHHH',
                    ULONG(self.Unknown_00).value,
                    ULONG(self.Unknown_04).value,
                    ULONG(self.Unknown_08).value,
                    USHORT(self.Unknown_0C).value,
                    USHORT(self.Unknown_0E).value,
                    ULONG(self.Unknown_10).value,
                    ULONG(self.Unknown_14).value,
                    ULONG(self.Unknown_18).value,
                    ULONG(self.Unknown_1C).value,
                    ULONG(self.Unknown_20).value,
                    ULONG(self.Unknown_24).value,
                    ULONG(self.Unknown_28).value,
                    ULONG(self.Unknown_2C).value,
                    USHORT(self.Unknown_30).value,
                    USHORT(self.Unknown_32).value,
                    USHORT(self.Unknown_34).value,
                    USHORT(self.Unknown_36).value,
                    USHORT(self.Unknown_38).value,
                    USHORT(self.Unknown_3A).value,
                    USHORT(self.InitScenaIndex).value,
                    USHORT(self.InitFunctionIndex).value,
                    USHORT(self.EntryScenaIndex).value,
                    USHORT(self.EntryFunctionIndex).value,
                )

class ScenarioNpcInfo:
    def __init__(self, fs = None):
        # size = 0x20
        if fs is None:
            fs = fileio.FileStream(b'\x00' * 0x20)

        self.X                  = fs.ReadULong()
        self.Z                  = fs.ReadULong()
        self.Y                  = fs.ReadULong()
        self.Direction          = fs.ReadUShort()   # 0 90 270 360
        self.Unknown2           = fs.ReadUShort()
        self.Unknown3           = fs.ReadULong()

        self.ChipIndex          = fs.ReadUShort()
        self.NpcIndex           = fs.ReadUShort()

        self.InitFunctionIndex  = fs.ReadUShort()
        self.InitScenaIndex     = fs.ReadUShort()
        self.TalkFunctionIndex  = fs.ReadUShort()
        self.TalkScenaIndex     = fs.ReadUShort()

    def __str__(self):
        return str(self.binary())

    def params(self):
        align = 20
        return [
            '%s %d,'   % (alignFormatKw(align, 'X'),                  LONG(self.X).value),
            '%s %d,'   % (alignFormatKw(align, 'Z'),                  LONG(self.Z).value),
            '%s %d,'   % (alignFormatKw(align, 'Y'),                  LONG(self.Y).value),
            '%s %d,'   % (alignFormatKw(align, 'Direction'),          LONG(self.Direction).value),
            '%s %s,'   % (alignFormatKw(align, 'Unknown2'),           SHORT(self.Unknown2).value),
            '%s %s,'   % (alignFormatKw(align, 'Unknown3'),           LONG(self.Unknown3).value),
            '%s 0x%X,' % (alignFormatKw(align, 'ChipIndex'),        SHORT(self.ChipIndex).value),
            '%s 0x%X,' % (alignFormatKw(align, 'NpcIndex'),         SHORT(self.NpcIndex).value),
            '%s %s,'   % (alignFormatKw(align, 'InitFunctionIndex'),  SHORT(self.InitFunctionIndex).value),
            '%s %s,'   % (alignFormatKw(align, 'InitScenaIndex'),     SHORT(self.InitScenaIndex).value),
            '%s %s,'   % (alignFormatKw(align, 'TalkFunctionIndex'),  SHORT(self.TalkFunctionIndex).value),
            '%s %s,'   % (alignFormatKw(align, 'TalkScenaIndex'),     SHORT(self.TalkScenaIndex).value),
        ]

    def binary(self):
        return struct.pack('<LLLHHLHHHHHH',
                    ULONG(self.X).value,
                    ULONG(self.Z).value,
                    ULONG(self.Y).value,
                    USHORT(self.Direction).value,
                    USHORT(self.Unknown2).value,
                    ULONG(self.Unknown3).value,
                    USHORT(self.ChipIndex).value,
                    USHORT(self.NpcIndex).value,
                    USHORT(self.InitFunctionIndex).value,
                    USHORT(self.InitScenaIndex).value,
                    USHORT(self.TalkFunctionIndex).value,
                    USHORT(self.TalkScenaIndex).value,
                )

class ScenarioMonsterInfo:
    def __init__(self, fs = None):
        # size = 0x1C
        if fs is None:
            fs = fileio.FileStream(b'\x00' * 0x1C)

        self.X                      = fs.ReadLong()
        self.Z                      = fs.ReadLong()
        self.Y                      = fs.ReadLong()
        self.Unknown_0C             = fs.ReadUShort()
        self.Unknown_0E             = fs.ReadUShort()
        self.Unknown_10             = fs.ReadByte()
        self.Unknown_11             = fs.ReadByte()
        self.Unknown_12             = fs.ReadULong()
        self.BattleIndex            = fs.ReadUShort()
        self.Unknown_18             = fs.ReadUShort()
        self.Unknown_1A             = fs.ReadUShort()

    def __str__(self):
        return str(self.binary())

    def params(self):
        align = 20
        return [
            '%s %d,'   % (alignFormatKw(align, 'X'),           self.X),
            '%s %d,'   % (alignFormatKw(align, 'Z'),           self.Z),
            '%s %d,'   % (alignFormatKw(align, 'Y'),           self.Y),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_0C'),  self.Unknown_0C),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_0E'),  self.Unknown_0E),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_10'),  self.Unknown_10),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_11'),  self.Unknown_11),
            '%s 0x%X,' % (alignFormatKw(align, 'Unknown_12'),  self.Unknown_12),
            '%s 0x%X,' % (alignFormatKw(align, 'BattleIndex'), self.BattleIndex),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_18'),  self.Unknown_18),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_1A'),  self.Unknown_1A),
        ]

    def binary(self):
        return struct.pack('<LLLHHBBLHHH',
                    ULONG(self.X).value,
                    ULONG(self.Z).value,
                    ULONG(self.Y).value,
                    USHORT(self.Unknown_0C).value,
                    USHORT(self.Unknown_0E).value,
                    BYTE(self.Unknown_10).value,
                    BYTE(self.Unknown_11).value,
                    ULONG(self.Unknown_12).value,
                    USHORT(self.BattleIndex).value,
                    USHORT(self.Unknown_18).value,
                    USHORT(self.Unknown_1A).value,
                )

class ScenarioEventInfo:
    def __init__(self, fs = None):
        # size = 0x20

        if fs is None:
            fs = fileio.FileStream(b'\x00' * 0x20)

        self.X              = fs.ReadLong()
        self.Y              = fs.ReadLong()
        self.Z              = fs.ReadLong()
        self.Range          = fs.ReadLong()
        self.Unknown_10     = fs.ReadULong()
        self.Unknown_14     = fs.ReadULong()
        self.Unknown_18     = fs.ReadULong()
        self.Unknown_1C     = fs.ReadULong()

    def __str__(self):
       return str(self.binary())

    def params(self):
        align = 20
        return [
            '%s %d,'   % (alignFormatKw(align, 'X'),            self.X),
            '%s %d,'   % (alignFormatKw(align, 'Y'),            self.Y),
            '%s %d,'   % (alignFormatKw(align, 'Z'),            self.Z),
            '%s %d,'   % (alignFormatKw(align, 'Range'),        self.Range),
            '%s 0x%X,' % (alignFormatKw(align, 'Unknown_10'),   self.Unknown_10),
            '%s 0x%X,' % (alignFormatKw(align, 'Unknown_14'),   self.Unknown_14),
            '%s 0x%X,' % (alignFormatKw(align, 'Unknown_18'),   self.Unknown_18),
            '%s %d,'   % (alignFormatKw(align, 'Unknown_1C'),   self.Unknown_1C),
        ]

    def binary(self):
        return struct.pack('<LLLLLLLL',
                    ULONG(self.X).value,
                    ULONG(self.Y).value,
                    ULONG(self.Z).value,
                    ULONG(self.Range).value,
                    ULONG(self.Unknown_10).value,
                    ULONG(self.Unknown_14).value,
                    ULONG(self.Unknown_18).value,
                    ULONG(self.Unknown_1C).value,
                )

class ScenarioActorInfo:
    def __init__(self, fs = None):
        # size = 0x24
        if fs is None:
            fs = fileio.FileStream(b'\x00' * 0x24)

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

    def params(self):
        align = 20
        p = [
            '%s %d,' % (alignFormatKw(align, 'TriggerX'),           LONG(self.TriggerX).value),
            '%s %d,' % (alignFormatKw(align, 'TriggerZ'),           LONG(self.TriggerZ).value),
            '%s %d,' % (alignFormatKw(align, 'TriggerY'),           LONG(self.TriggerY).value),
            '%s %d,' % (alignFormatKw(align, 'TriggerRange'),       LONG(self.TriggerRange).value),
            '%s %s,' % (alignFormatKw(align, 'ActorX'),             LONG(self.ActorX).value),
            '%s %s,' % (alignFormatKw(align, 'ActorZ'),             LONG(self.ActorZ).value),
            '%s %s,' % (alignFormatKw(align, 'ActorY'),             LONG(self.ActorY).value),
            '%s 0x%X,' % (alignFormatKw(align, 'Flags'),            USHORT(self.Flags).value),
            '%s %s,' % (alignFormatKw(align, 'TalkScenaIndex'),     SHORT(self.TalkScenaIndex).value),
            '%s %s,' % (alignFormatKw(align, 'TalkFunctionIndex'),  SHORT(self.TalkFunctionIndex).value),
            '%s %s,' % (alignFormatKw(align, 'Unknown_22'),         USHORT(self.Unknown_22).value),
        ]

        return p

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

        # file header end

        self.ScenaFunctions     = []
        self.PlaceName          = ''
        self.StringTable        = []
        self.ScnInfo            = []
        self.CodeBlocks         = []

        self.GlobalLabelTable   = {}

        for i in range(SCN_INFO_MAXIMUM):
            self.ScnInfo.append([])
            #self.ScnInfoOffset.append(0)
            #self.ScnInfoNumber.append(0)

    def binary(self):
        buffer = fileio.FileStream(b'')

        buffer.Write(self.MapName.encode(CODE_PAGE).ljust(0xA, b'\x00')[:0xA])
        buffer.Write(self.Location.encode(CODE_PAGE).ljust(0xE, b'\x00')[:0xE])
        buffer.WriteUShort(self.MapIndex)
        buffer.WriteUShort(self.MapDefaultBGM.Index())
        buffer.WriteUShort(self.Flags)
        buffer.WriteUShort(self.EntryFunctionIndex)

        for inc in self.IncludedScenario:
            buffer.WriteULong(inc)

        buffer.WriteUShort(self.Reserved)

        for i in range(len(self.ScnInfoOffset)):
            buffer.WriteUShort(self.ScnInfoOffset[i])
            buffer.WriteUShort(self.ScnInfoNumber[i])

        buffer.WriteUShort(self.StringTableOffset)
        buffer.WriteULong(self.HeaderEndOffset)

        buffer.WriteUShort(self.ScenaFunctionTable.Offset)
        buffer.WriteUShort(self.ScenaFunctionTable.Size)

        buffer.Position = 0

        return buffer.Read()

    def open(self, scenafile):
        fs = fileio.FileStream(scenafile)
        if fs.Length == 0:
            return False

        self.InitMapNameList(scenafile)

        self.scenaName = os.path.splitext(os.path.basename(scenafile))[0].strip().upper()
        self.scenaTextIndex = 1

        # file header

        self.MapName            = fs.read(0xA).decode(CODE_PAGE).split('\x00', 1)[0]
        self.Location           = fs.read(0xE).decode(CODE_PAGE).split('\x00', 1)[0]
        self.MapIndex           = fs.ReadUShort()
        self.MapDefaultBGM      = BGMFileIndex(fs.ReadUShort())
        self.Flags              = fs.ReadUShort()
        self.EntryFunctionIndex = fs.ReadUShort()
        self.IncludedScenario   = list(struct.unpack('<' + 'I' * NUMBER_OF_INCLUDE_FILE, fs.read(NUMBER_OF_INCLUDE_FILE * 4)))
        self.Reserved           = fs.ReadUShort()
        self.ScnInfoOffset      = [ScenarioEntry(fs.ReadUShort(), fs.ReadUShort()) for _ in range(SCN_INFO_MAXIMUM)]
        self.StringTableOffset  = fs.ReadUShort()
        self.HeaderEndOffset    = fs.ReadULong()
        self.ScenaFunctionTable = ScenarioEntry(fs.ReadUShort(), fs.ReadUShort())

        self.IncludedScenario.index(0xFFFFFFFF)

        self.EntryPoint = [ScenarioEntryPoint(fs) for i in range((self.ScnInfoOffset[0].Offset - fs.Position) // 0x44)]

        # file header end

        self.InitScenaInfo(fs)
        self.InitOtherInfo(fs)

        self.CodeBlocks = self.DisassembleBlocks(fs)


    def InitMapNameList(self, scenafile):
        self.MapNameList = []

        try:
            t_town = os.path.abspath(os.path.join(GAME_PATH, 'ED6_DT02\\T_TOWN  ._DT'))
            town = fileio.FileStream(t_town)

            offsetlist = []
            for i in range(town.ReadUShort()):
                offsetlist.append(town.ReadUShort())

            for offset in offsetlist:
                town.seek(offset)
                self.MapNameList.append(town.ReadMultiByte('GBK'))

        except:
            self.MapNameList = []

    def GetMapNameByIndex(self, index):
        if self.MapName.startswith('map'):
            return '调试地图'

        if index == 1:
            return {
                'rolent'    : '洛连特',
                'zeiss'     : '蔡斯',
                'grancel'   : '格兰赛尔',
                'ruan'      : '卢安',
                'bose'      : '柏斯',
            }.get(self.MapName.lower(), '')

        if index >= len(self.MapNameList):
            return ''

        return self.MapNameList[index]

    def InitScenaInfo(self, fs):
        ScnInfoTypes = \
        [
            ScenarioChipInfo,
            ScenarioChipInfo,
            ScenarioNpcInfo,
            ScenarioMonsterInfo,
            ScenarioEventInfo,
            ScenarioActorInfo,
        ]

        for i in range(len(self.ScnInfoOffset)):
            fs.seek(self.ScnInfoOffset[i].Offset)
            ScnInfoType = ScnInfoTypes[i]
            for n in range(self.ScnInfoOffset[i].Size):
                self.ScnInfo[i].append(ScnInfoType(fs))

    def InitOtherInfo(self, fs):
        fs.seek(self.ScenaFunctionTable.Offset)
        self.ScenaFunctions = list(struct.unpack('<' + 'H' * int(self.ScenaFunctionTable.Size / 2), fs.read(self.ScenaFunctionTable.Size)))

        fs.seek(self.StringTableOffset)

        buf = fs.read()
        endmz = buf.find(b'\x00\x00')
        if endmz != -1:
            buf = buf[:endmz]

        self.StringTable = buf.decode(CODE_PAGE).rstrip('\x00').split('\x00')

        if ExtractText:
            textPosTable[self.scenaName] = [self.StringTable]
        else:
            try:
                strtbl = textPosTable[self.scenaName][0]
                if len(strtbl) != len(self.StringTable):
                    raise Exception('%s\n\n%s' % (strtbl, self.StringTable))
                self.StringTable = strtbl
            except KeyError:
                pass

    def DiasmInstructionCallback(self, data):
        if data.Reason != HANDLER_REASON_DISASM:
            return

        inst, fs = data.Instruction, data.FileStream

        if inst.OpCode == ed6fc.SetPlaceName:
            self.PlaceName = self.GetMapNameByIndex(inst.Operand[0])

        if inst.OpCode not in [
                ed6fc.ChrTalk,
                ed6fc.AnonymousTalk,
                ed6fc.NpcTalk,
                ed6fc.Menu,
                ed6fc.SetChrName
            ]:
            return

        if ExtractText:
            if inst.OpCode == ed6fc.ChrTalk:
                text = inst.Operand[1]
                textPosTable[self.scenaName].append([s.dump() for s in text])

            elif inst.OpCode == ed6fc.AnonymousTalk:
                text = inst.Operand[0]
                textPosTable[self.scenaName].append([s.dump() for s in text])

            elif inst.OpCode == ed6fc.NpcTalk:
                for text in inst.Operand[1:]:
                    textPosTable[self.scenaName].append([s.dump() for s in text])

            elif inst.OpCode in [ed6fc.Menu, ed6fc.SetChrName]:
                text = inst.Operand[-1]
                textPosTable[self.scenaName].append([s.dump() for s in text])

        else:
            try:
                cntext = textPosTable[self.scenaName]
            except KeyError:
                return

            try:
                ignoreText = replaceOption[self.scenaName]['text']
            except KeyError:
                ignoreText = None

            def checkIgnore(oprlist):
                if ignoreText is None:
                    return

                for i in oprlist:
                    for string in inst.Operand[i]:
                        string = str(string)
                        for t in ignoreText:
                            if t in string:
                                return True

                return False

            if inst.OpCode == ed6fc.ChrTalk:
                if checkIgnore([1]):
                    return

                inst.Operand[1] = self.loadScpStringList(cntext[self.scenaTextIndex])

            elif inst.OpCode == ed6fc.AnonymousTalk:
                if checkIgnore([0]):
                    return

                inst.Operand[0] = self.loadScpStringList(cntext[self.scenaTextIndex])

            elif inst.OpCode == ed6fc.NpcTalk:
                if checkIgnore([1, 2]):
                    return

                inst.Operand[1] = self.loadScpStringList(cntext[self.scenaTextIndex])
                inst.Operand[2] = self.loadScpStringList(cntext[self.scenaTextIndex + 1])
                self.scenaTextIndex += 1

            elif inst.OpCode in [ed6fc.Menu, ed6fc.SetChrName]:
                if checkIgnore([-1]):
                    return

                inst.Operand[-1] = self.loadScpStringList(cntext[self.scenaTextIndex])

            self.scenaTextIndex += 1

    def loadScpStringList(self, paramList):
        return [ed6fc.ScpString(**p) for p in paramList]

    def DisassembleBlocks(self, fs):
        disasm = Disassembler(ed6fc.ed6fc_op_table, self.DiasmInstructionCallback)

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

    def FormatInstructionCallback(self, data, text):
        if data.Instruction.OpCode == ed6fc.SetPlaceName and self.PlaceName:
            return [text[0] + ' # ' + self.PlaceName]

    def FormatCodeBlocks(self):
        ed6fc.ed6fc_op_table.FunctionLabelList = self.GenerateFunctionLabelList(self.CodeBlocks)
        disasm = Disassembler(ed6fc.ed6fc_op_table, self.FormatInstructionCallback)

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

    def GenerateStringList(self):

        lines = []

        if len(self.StringTable) == 0:
            return lines

        index = 8
        lines.append('BuildStringList(')
        for string in self.StringTable:
            lines.append('    %s# %d' % (alignFormatArg(40, '%s' % repr(string)), index))
            index += 1

        lines.append(')')
        lines.append('')

        return lines

    def GenerateHeader(self, filename):
        filename = os.path.splitext(os.path.splitext(os.path.basename(filename))[0])[0] + '._SN'

        mapname = self.PlaceName or self.GetMapNameByIndex(self.MapIndex)

        align = 20

        hdr = []
        hdr.append('from ED6ScenarioHelper import *')
        hdr.append('')

        if mapname:
            hdr.append('# ' + mapname)
            hdr.append('')

        hdr.append('CreateScenaFile(')

        hdr.append('    %s %r,'     % (alignFormatKw(align, 'FileName'),            filename))
        hdr.append('    %s %r,'     % (alignFormatKw(align, 'MapName'),             self.MapName))
        hdr.append('    %s %r,'     % (alignFormatKw(align, 'Location'),            self.Location))
        hdr.append('    %s %s,'     % (alignFormatKw(align, 'MapIndex'),            self.MapIndex))
        hdr.append('    %s %s,'     % (alignFormatKw(align, 'MapDefaultBGM'),       self.MapDefaultBGM.param()))
        hdr.append('    %s %s,'     % (alignFormatKw(align, 'Flags'),               self.Flags))
        hdr.append('    %s %s,'     % (alignFormatKw(align, 'EntryFunctionIndex'),  self.EntryFunctionIndex == 0xFFFF and '0xFFFF' or self.EntryFunctionIndex))
        hdr.append('    %s %s,'     % (alignFormatKw(align, 'Reserved'),            self.Reserved))
        hdr.append('    %s [\n            %s\n        ],'   % (alignFormatKw(align, 'IncludedScenario'),  ',\n            '.join([repr(ScenarioFileIndex(scp).Name()) for scp in self.IncludedScenario])))

        hdr.append(')')
        hdr.append('')

        hdr += self.GenerateStringList()

        def AppendScpInfo(info, func):
            if len(info) == 0:
                return

            for i in info:
                if hasattr(i, 'params'):
                    params = i.params()
                    hdr.append('%s(' % func)
                    hdr.extend(['    ' + p for p in params])
                    hdr.append(')')
                else:
                    hdr.append('%s(%s)' % (func, i.param()))

                hdr.append('')

            hdr.append('')

        AppendScpInfo(self.EntryPoint, 'DeclEntryPoint')

        if len(self.ScnInfo[SCN_INFO_CHIP]) != 0:
            hdr.append('AddCharChip(')

            index = 0
            for chip in self.ScnInfo[SCN_INFO_CHIP]:
                x = ('    %s,' % chip.param()).ljust(40)
                x += ' # %02X' % index
                hdr.append(x)
                index += 1

            hdr.append(')')
            hdr.append('')

        if len(self.ScnInfo[SCN_INFO_CHIP_PAT]) != 0:
            hdr.append('AddCharChipPat(')

            index = 0
            for chip in self.ScnInfo[SCN_INFO_CHIP_PAT]:
                x = ('    %s,' % chip.param()).ljust(40)
                x += ' # %02X' % index
                hdr.append(x)
                index += 1

            hdr.append(')')
            hdr.append('')

        AppendScpInfo(self.ScnInfo[SCN_INFO_NPC],       'DeclNpc')
        AppendScpInfo(self.ScnInfo[SCN_INFO_MONSTER],   'DeclMonster')
        AppendScpInfo(self.ScnInfo[SCN_INFO_EVENT],     'DeclEvent')
        AppendScpInfo(self.ScnInfo[SCN_INFO_ACTOR],     'DeclActor')

        hdr.append('ScpFunction(')
        index = 0
        for block in self.CodeBlocks:
            s = ljust_cn('    "%s",' % block.Name, 30)
            s += ' # %02X, %d' % (index, index)
            hdr.append(s)
            index += 1

        hdr.append(')')
        hdr.append('')
        hdr.append('')

        return hdr

    def SaveToFile(self, filename, append_place_name = True):
        lines = []

        basename, ext = os.path.splitext(filename)
        basename = basename.strip()

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

        filename = '%s%s' % (basename, ext)

        if append_place_name:
            if not self.PlaceName:
                self.PlaceName = self.GetMapNameByIndex(self.MapIndex)

            if self.PlaceName:
                filename = '%s.%s%s' % (basename, self.PlaceName, ext)

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
    if scena.open(file) is not False:
        scena.SaveToFile(os.path.splitext(file)[0] + '.py')

def main():
    global textPosTable, replaceOption

    os.chdir(os.path.dirname(__file__))

    if not ExtractText:
        textPosTable = json.load(open('fc_sn_text_final.json', 'r', encoding = 'utf-8-sig'))
        replaceOption = json.load(open('replace_option.json', 'r', encoding = 'utf-8-sig'))

    if len(sys.argv) == 1:
        sys.argv.append(r"T0001   ._SN")
    iterlib.forEachFile(procfile, sys.argv[1:], '*._SN')

    if ExtractText:
        open('fc_sn_text.json', 'wb').write(json.dumps(textPosTable, indent = 2, ensure_ascii = False).encode('utf_8_sig'))

if __name__ == '__main__':
    Try(main)
