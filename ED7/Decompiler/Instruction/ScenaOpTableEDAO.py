from Assembler.InstructionTable import *
from Base.EDAOBase import *
from GameData.ItemNameMap import *

def GetOpCode(fs):
    return fs.ReadByte()

def WriteOpCode(fs, op):
    return fs.WriteByte(op)

edao_op_table = InstructionTable(GetOpCode, WriteOpCode, DefaultGetLabelName, CODE_PAGE)

InstructionNames = {}

InstructionNames[0x00]  = 'ExitThread'
InstructionNames[0x01]  = 'Return'
InstructionNames[0x02]  = 'Jc'
InstructionNames[0x03]  = 'Jump'
InstructionNames[0x04]  = 'Switch'
InstructionNames[0x05]  = 'Call'
InstructionNames[0x06]  = 'NewScene'
InstructionNames[0x07]  = 'IdleLoop'
InstructionNames[0x08]  = 'Sleep'
InstructionNames[0x09]  = 'SetMapFlags'
InstructionNames[0x0A]  = 'ClearMapFlags'
InstructionNames[0x0B]  = 'FadeToDark'
InstructionNames[0x0C]  = 'FadeToBright'
InstructionNames[0x0D]  = 'OP_0D'
InstructionNames[0x0E]  = 'Fade'
InstructionNames[0x0F]  = 'Battle'
InstructionNames[0x10]  = 'OP_10'
InstructionNames[0x11]  = 'OP_11'
InstructionNames[0x12]  = 'StopSound'
InstructionNames[0x13]  = 'OP_13'
InstructionNames[0x14]  = 'BlurSwitch'
InstructionNames[0x15]  = 'CancelBlur'
InstructionNames[0x16]  = 'OP_16'
InstructionNames[0x17]  = 'ShowSaveMenu'
InstructionNames[0x19]  = 'EventBegin'
InstructionNames[0x1A]  = 'EventEnd'
InstructionNames[0x1B]  = 'OP_1B'
InstructionNames[0x1C]  = 'OP_1C'
InstructionNames[0x1D]  = 'SetBarrier'
InstructionNames[0x1E]  = 'PlayBGM'
InstructionNames[0x1F]  = 'OP_1F'
InstructionNames[0x20]  = 'VolumeBGM'
InstructionNames[0x21]  = 'StopBGM'
InstructionNames[0x22]  = 'WaitBGM'
InstructionNames[0x23]  = 'Sound'
InstructionNames[0x24]  = 'OP_24'
InstructionNames[0x25]  = 'OP_25'
InstructionNames[0x26]  = 'SoundDistance'
InstructionNames[0x27]  = 'SoundLoad'
InstructionNames[0x28]  = 'Yield'
InstructionNames[0x29]  = 'OP_29'
InstructionNames[0x2A]  = 'OP_2A'
InstructionNames[0x2B]  = 'OP_2B'
InstructionNames[0x2C]  = 'OP_2C'
InstructionNames[0x2D]  = 'OP_2D'
InstructionNames[0x2E]  = 'AddParty'
InstructionNames[0x2F]  = 'RemoveParty'
InstructionNames[0x30]  = 'ClearParty'
InstructionNames[0x31]  = 'OP_31'
InstructionNames[0x32]  = 'OP_32'
InstructionNames[0x35]  = 'RemoveCraft'
InstructionNames[0x36]  = 'AddCraft'
InstructionNames[0x37]  = 'OP_37'
InstructionNames[0x38]  = 'OP_38'
InstructionNames[0x39]  = 'AddSepith'
InstructionNames[0x3A]  = 'SubSepith'
InstructionNames[0x3B]  = 'AddMira'
InstructionNames[0x3C]  = 'SubMira'
InstructionNames[0x3D]  = 'OP_3D'
InstructionNames[0x3E]  = 'OP_3E'
InstructionNames[0x3F]  = 'AddItemNumber'
InstructionNames[0x40]  = 'SubItemNumber'
InstructionNames[0x41]  = 'GetItemNumber'
InstructionNames[0x42]  = 'OP_42'
InstructionNames[0x43]  = 'GetPartyIndex'
InstructionNames[0x44]  = 'BeginChrThread'
InstructionNames[0x45]  = 'EndChrThread'
InstructionNames[0x46]  = 'QueueWorkItem'
InstructionNames[0x47]  = 'QueueWorkItem2'
InstructionNames[0x48]  = 'WaitChrThread'
InstructionNames[0x49]  = 'OP_49'
InstructionNames[0x4A]  = 'Event'
InstructionNames[0x4B]  = 'OP_4B'
InstructionNames[0x4C]  = 'OP_4C'
InstructionNames[0x4D]  = 'OP_4D'
InstructionNames[0x4E]  = 'RunExpression'
InstructionNames[0x4F]  = 'OP_4F'
InstructionNames[0x50]  = 'OP_50'
InstructionNames[0x51]  = 'OP_51'
InstructionNames[0x52]  = 'OP_52'
InstructionNames[0x53]  = 'TalkBegin'
InstructionNames[0x54]  = 'TalkEnd'
InstructionNames[0x55]  = 'AnonymousTalk'
InstructionNames[0x56]  = 'OP_56'
InstructionNames[0x57]  = 'OP_57'
InstructionNames[0x58]  = 'MenuTitle'
InstructionNames[0x59]  = 'CloseMessageWindow'
InstructionNames[0x5A]  = 'OP_5A'
InstructionNames[0x5B]  = 'SetMessageWindowPos'
InstructionNames[0x5C]  = 'ChrTalk'
InstructionNames[0x5D]  = 'NpcTalk'
InstructionNames[0x5E]  = 'Menu'
InstructionNames[0x5F]  = 'MenuEnd'
InstructionNames[0x60]  = 'OP_60'
InstructionNames[0x61]  = 'SetChrName'
InstructionNames[0x62]  = 'OP_62'
InstructionNames[0x63]  = 'OP_63'
InstructionNames[0x64]  = 'OP_64'
InstructionNames[0x65]  = 'OP_65'
InstructionNames[0x66]  = 'OP_66'
InstructionNames[0x67]  = 'OP_67'
InstructionNames[0x68]  = 'OP_68'
InstructionNames[0x69]  = 'OP_69'
InstructionNames[0x6A]  = 'OP_6A'
InstructionNames[0x6B]  = 'OP_6B'
InstructionNames[0x6C]  = 'SetCameraDistance'
InstructionNames[0x6D]  = 'MoveCamera'
InstructionNames[0x6E]  = 'OP_6E'
InstructionNames[0x6F]  = 'OP_6F'
InstructionNames[0x70]  = 'OP_70'
InstructionNames[0x71]  = 'OP_71'
InstructionNames[0x72]  = 'SetMapObjFlags'
InstructionNames[0x73]  = 'ClearMapObjFlags'
InstructionNames[0x74]  = 'OP_74'
InstructionNames[0x75]  = 'OP_75'
InstructionNames[0x76]  = 'SetMapObjFrame'
InstructionNames[0x77]  = 'OP_77'
InstructionNames[0x78]  = 'OP_78'
InstructionNames[0x79]  = 'OP_79'
InstructionNames[0x7A]  = 'SetEventSkip'
InstructionNames[0x7B]  = 'OP_7B'
InstructionNames[0x7D]  = 'OP_7D'
InstructionNames[0x82]  = 'OP_82'
InstructionNames[0x83]  = 'SetChrChip'
InstructionNames[0x84]  = 'OP_84'
InstructionNames[0x85]  = 'LoadEffect'
InstructionNames[0x86]  = 'PlayEffect'
InstructionNames[0x87]  = 'OP_87'
InstructionNames[0x88]  = 'StopEffect'
InstructionNames[0x89]  = 'OP_89'
InstructionNames[0x8A]  = 'OP_8A'
InstructionNames[0x8B]  = 'OP_8B'
InstructionNames[0x8C]  = 'SetChrChipByIndex'
InstructionNames[0x8D]  = 'SetChrSubChip'
InstructionNames[0x8E]  = 'OP_8E'
InstructionNames[0x8F]  = 'SetChrPos'
InstructionNames[0x90]  = 'OP_90'
InstructionNames[0x91]  = 'TurnDirection'
InstructionNames[0x92]  = 'OP_92'
InstructionNames[0x93]  = 'OP_93'
InstructionNames[0x94]  = 'OP_94'
InstructionNames[0x95]  = 'OP_95'
InstructionNames[0x96]  = 'OP_96'
InstructionNames[0x97]  = 'OP_97'
InstructionNames[0x98]  = 'OP_98'
InstructionNames[0x99]  = 'OP_99'
InstructionNames[0x9A]  = 'OP_9A'
InstructionNames[0x9B]  = 'OP_9B'
InstructionNames[0x9C]  = 'OP_9C'
InstructionNames[0x9D]  = 'OP_9D'
InstructionNames[0x9E]  = 'OP_9E'
InstructionNames[0x9F]  = 'OP_9F'
InstructionNames[0xA0]  = 'OP_A0'
InstructionNames[0xA1]  = 'OP_A1'
InstructionNames[0xA2]  = 'SetChrFlags'
InstructionNames[0xA3]  = 'ClearChrFlags'
InstructionNames[0xA4]  = 'SetChrBattleFlags'
InstructionNames[0xA5]  = 'ClearChrBattleFlags'
InstructionNames[0xA6]  = 'OP_A6'
InstructionNames[0xA7]  = 'OP_A7'
InstructionNames[0xA8]  = 'OP_A8'
InstructionNames[0xA9]  = 'SetScenarioFlags'
InstructionNames[0xAA]  = 'ClearScenarioFlags'
InstructionNames[0xAB]  = 'OP_AB'
InstructionNames[0xAC]  = 'OP_AC'
InstructionNames[0xAD]  = 'OP_AD'
InstructionNames[0xAE]  = 'OP_AE'
InstructionNames[0xAF]  = 'OP_AF'
InstructionNames[0xB2]  = 'OP_B2'
InstructionNames[0xB3]  = 'OutputDebugInt'
InstructionNames[0xB4]  = 'OP_B4'
InstructionNames[0xB5]  = 'OP_B5'
InstructionNames[0xB6]  = 'LoadOps'
InstructionNames[0xB7]  = 'ModifyEventFlags'
InstructionNames[0xB8]  = 'PlayMovie'
InstructionNames[0xB9]  = 'OP_B9'
InstructionNames[0xBA]  = 'ReplaceBGM'
InstructionNames[0xBC]  = 'OP_BC'
InstructionNames[0xBD]  = 'UseItem'
InstructionNames[0xBE]  = 'OP_BE'
InstructionNames[0xBF]  = 'OP_BF'
InstructionNames[0xC0]  = 'SetChrChipPat'
InstructionNames[0xC2]  = 'LoadChrChipPat'
InstructionNames[0xC3]  = 'OP_C3'
InstructionNames[0xC4]  = 'OP_C4'
InstructionNames[0xC5]  = 'MiniGame'
InstructionNames[0xC7]  = 'OP_C7'
InstructionNames[0xC9]  = 'OP_C9'
InstructionNames[0xCA]  = 'CreatePortrait'
InstructionNames[0xCB]  = 'OP_CB'
InstructionNames[0xCC]  = 'OP_CC'
InstructionNames[0xCD]  = 'PlaceName2'
InstructionNames[0xCE]  = 'PartySelect'
InstructionNames[0xCF]  = 'OP_CF'
InstructionNames[0xD0]  = 'MenuCmd'
InstructionNames[0xD1]  = 'OP_D1'
InstructionNames[0xD2]  = 'OP_D2'
InstructionNames[0xD3]  = 'OP_D3'
InstructionNames[0xD4]  = 'OP_D4'
InstructionNames[0xD5]  = 'OP_D5'
InstructionNames[0xD6]  = 'LoadChrToIndex'
InstructionNames[0xD7]  = 'OP_D7'
InstructionNames[0xD8]  = 'OP_D8'
InstructionNames[0xD9]  = 'OP_D9'
InstructionNames[0xDA]  = 'OP_DA'
InstructionNames[0xDC]  = 'OP_DC'
InstructionNames[0xDD]  = 'OP_DD'
InstructionNames[0xDE]  = 'OP_DE'
InstructionNames[0xDF]  = 'LoadAnimeChip'
InstructionNames[0xE0]  = 'OP_E0'
InstructionNames[0xE2]  = 'OP_E2'
InstructionNames[0xE3]  = 'OP_E3'
InstructionNames[0xE4]  = 'OP_E4'
InstructionNames[0xE5]  = 'OP_E5'
InstructionNames[0xE6]  = 'OP_E6'
InstructionNames[0xE7]  = 'OP_E7'
InstructionNames[0xE8]  = 'OP_E8'
InstructionNames[0xE9]  = 'ShowSaveClearMenu'
InstructionNames[0xF0]  = 'OP_F0'
InstructionNames[0xF3]  = 'OP_F3'
InstructionNames[0xF4]  = 'OP_F4'
InstructionNames[0xFA]  = 'OP_FA'
InstructionNames[0xFB]  = 'OP_FB'
InstructionNames[0xFC]  = 'OP_FC'
InstructionNames[0xFD]  = 'OP_FD'
InstructionNames[0xFE]  = 'OP_FE'
InstructionNames[0xFF]  = 'OP_FF'

for op, name in InstructionNames.items():
    expr = '%s = 0x%08X' % (name, op)
    exec(expr)


def GetItemName(id):
    return ItemNameMap[id] if id in ItemNameMap else '0x%X' % id

def GetItemTrueName(id):
    return '\'%s\'' % ItemTrueNameMap[id] if id in ItemTrueNameMap else '0x%X' % id


ScpStrCodeMap = {}

ScpStrCodeMap[-1]       = 'SCPSTR_CODE_STRING'
ScpStrCodeMap[0x1F]     = 'SCPSTR_CODE_ITEM'
ScpStrCodeMap[0x01]     = 'SCPSTR_CODE_LINE_FEED'
ScpStrCodeMap[0x02]     = 'SCPSTR_CODE_ENTER'
ScpStrCodeMap[0x03]     = 'SCPSTR_CODE_CLEAR'
ScpStrCodeMap[0x05]     = 'SCPSTR_CODE_05'
ScpStrCodeMap[0x07]     = 'SCPSTR_CODE_COLOR'
ScpStrCodeMap[0x09]     = 'SCPSTR_CODE_09'

for code, name in ScpStrCodeMap.items():
    expr = '%s = %d' % (name, code)
    exec(expr)

def GetStrCode(code):
    return ScpStrCodeMap[code] if code in ScpStrCodeMap else '0x%X' % code

class ScpString:
    def __init__(self, CtrlCode, Value = None):
        self.CtrlCode   = CtrlCode
        self.Value      = Value

    def binary(self):
        pass

    def __str__(self):
        if self.CtrlCode == SCPSTR_CODE_STRING:
            return '"%s"' % self.Value

        value = self.Value
        code = GetStrCode(self.CtrlCode)

        if value == None:
            return 'scpstr(%s)' % code

        value = GetItemTrueName(value) if self.CtrlCode == SCPSTR_CODE_ITEM else '0x%X' % value

        return 'scpstr(%s, %s)' % (code, value)

def BuildStringListFromObjectList(strlist):
    s = []
    laststrindex = None
    for x in strlist:
        if  x.CtrlCode == SCPSTR_CODE_LINE_FEED or \
            x.CtrlCode == SCPSTR_CODE_ENTER     or \
            x.CtrlCode == SCPSTR_CODE_CLEAR     or \
            x.CtrlCode == SCPSTR_CODE_05        or \
            x.CtrlCode == SCPSTR_CODE_COLOR     or \
            x.CtrlCode == SCPSTR_CODE_09:

            if len(s) != laststrindex:

                s.append(str(x))

            else:

                if x.CtrlCode == SCPSTR_CODE_COLOR:
                    tmp = '\\x%02X\\x%02X' % (x.CtrlCode, x.Value)
                else:
                    tmp = '\\x%02X' % x.CtrlCode
                s[-1] = '"%s%s"' % (s[-1][1:-1], tmp)

        elif x.CtrlCode == SCPSTR_CODE_STRING:

            s.append(str(x))
            laststrindex = len(s)

        else:

            s.append(str(x))

    return s

def FormatFuncString(data, oprfmt, mark_number = None):

    entry = data.TableEntry
    ins = data.Instruction

    txt = [ '', '%s(' % entry.OpName ]

    maxlen = 0

    for i in range(len(oprfmt)):
        opr = oprfmt[i]
        if opr != 'S':
            paramlist = BuildFormatOperandParameterList([opr], [ins.Operand[i]])
            txt.append('    %s,' % entry.FormatAllOperand(paramlist))
            #bp()
            #txt.append('    0x%X,' % ins.Operand[i])
        else:
            strlist = BuildStringListFromObjectList(ins.Operand[i])

            if len(strlist) == 1:
                s = '    %s' % strlist[0]

                if i != len(oprfmt):
                    s += ','

                txt.append(s)
                continue

            index = 0
            txt.append('    (')
            for s in strlist:
                tmp = '        %s,' % s
                if mark_number:
                    if strlen(tmp) > maxlen:
                        maxlen = strlen(tmp)

                    tmp = ljust_cn(tmp, mark_number)
                    tmp += ' # %d' % index

                txt.append(tmp)
                index += 1

            txt.append('    )')

    if mark_number == -1 and maxlen != 0:
        return FormatFuncString(data, oprfmt, maxlen + 5)

    txt.append(')')
    txt.append('')

    return txt

class EDAOScenaInstructionTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

    def WriteOperand(self, data, opr, value):

        fs = data.FileStream
        labels = data.Instruction.Labels

        def wexpr(value):
            for expr in value:
                expr.WriteExpression(data)

        def wstr(value, recursion = False):
            if type(value) == str:
                value = value.encode(CODE_PAGE)
                if not recursion:
                    value += b'\x00'

            elif IsTupleOrList(value):
                for x in value:
                    wstr(x, True)

                fs.WriteByte(0)
                return

            fs.write(value)

        oprtype = \
        {
            'E' : wexpr,
            'S' : wstr,
            'M' : lambda value : fs.WriteShort(BGMFileIndex(value).Index()),
            'T' : lambda value : fs.WriteUShort(ItemTrueNameMap[value] if type(value) == str else value),
        }

        return oprtype[opr](value) if opr in oprtype else super().WriteOperand(data, opr, value)

    def FormatOperand(self, param):
        value   = param.Value
        opr     = param.Operand
        flags   = param.Flags

        def formatstr(strlist):
            s = BuildStringListFromObjectList(strlist)

            if not flags.ArgNewLine:
                if len(s) == 0:
                    return '""'
                elif len(s) == 1:
                    return s[0]

                return '(' + ', '.join(s) + ')'

            raise Exception('not implement')

        def formatbgm(bgm):
            bgm = BGMFileIndex(bgm)
            return ('"%s"' % bgm.Name()) if not bgm.IsInvalid() else ('0x%08X' % (bgm.Index() & 0xFFFFFFFF))

        oprtype = \
        {
            'E' : lambda : FormatExpressionList(value),
            'S' : lambda : formatstr(value),
            'M' : lambda : BGMFileIndex(value).param(),
            'T' : lambda : GetItemTrueName(value),
        }

        return oprtype[opr]() if opr in oprtype else super().FormatOperand(param)

    def GetOperand(self, opr, fs):

        def readstr():
            string = []
            tmpstr = ''

            while True:
                buf = fs.read(1)

                if buf < b' ':
                    if tmpstr != '':
                        string.append(ScpString(SCPSTR_CODE_STRING, tmpstr.replace('\\', '\\\\')))
                        tmpstr = ''

                    code = struct.unpack('<B', buf)[0]

                    if code == 0:
                        break

                    strobj = ScpString(code)

                    if code == SCPSTR_CODE_COLOR:

                        # dummy byte ?
                        strobj.Value = fs.ReadByte()

                    elif code == SCPSTR_CODE_LINE_FEED or code == 0x0A:

                        # line feed
                        pass

                    elif code == SCPSTR_CODE_ENTER:

                        # need press enter
                        pass

                    elif code == SCPSTR_CODE_CLEAR or code == 0x04:

                        # unknown
                        pass

                    elif code == 0x05:

                        pass

                    elif code == 0x06:

                        # unknown
                        pass

                    elif code == 0x18:

                        pass

                    elif code == SCPSTR_CODE_ITEM:

                        # item id
                        strobj.Value = fs.ReadUShort()

                    string.append(strobj)

                    continue

                elif buf >= b'\x80':

                    buf += fs.read(1)

                tmpstr += buf.decode(self.Container.CodePage)

            return string

        oprtype = \
        {
            'S' : readstr,
            'M' : lambda : fs.ReadShort(),
            'T' : lambda : fs.ReadUShort(),
        }

        return oprtype[opr]() if opr in oprtype else super().GetOperand(opr, fs)

    def GetOperandSize(self, opr, fs):
        if opr == 'M':
            return 2

        if opr != 'S':
            return super().GetOperandSize(opr, fs)

        pos = fs.tell()
        self.GetOperand(opr, fs)
        oprsize = fs.tell() - pos
        fs.seek(pos)
        return oprsize

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return EDAOScenaInstructionTableEntry(op, InstructionNames[op], operand, flags, handler)

ExpressionOperantions = {}

ExpressionOperantions[0x00] = 'EXPR_PUSH_LONG'
ExpressionOperantions[0x01] = 'EXPR_END'
ExpressionOperantions[0x02] = 'EXPR_EQU'
ExpressionOperantions[0x03] = 'EXPR_NEQ'
ExpressionOperantions[0x04] = 'EXPR_LSS'
ExpressionOperantions[0x05] = 'EXPR_GTR'
ExpressionOperantions[0x06] = 'EXPR_LEQ'
ExpressionOperantions[0x07] = 'EXPR_GE'
ExpressionOperantions[0x08] = 'EXPR_EQUZ'
ExpressionOperantions[0x09] = 'EXPR_NEQUZ_I64'
ExpressionOperantions[0x0A] = 'EXPR_AND'
ExpressionOperantions[0x0B] = 'EXPR_OR'
ExpressionOperantions[0x0C] = 'EXPR_ADD'
ExpressionOperantions[0x0D] = 'EXPR_SUB'
ExpressionOperantions[0x0E] = 'EXPR_NEG'
ExpressionOperantions[0x0F] = 'EXPR_XOR'
ExpressionOperantions[0x10] = 'EXPR_IMUL'
ExpressionOperantions[0x11] = 'EXPR_IDIV'
ExpressionOperantions[0x12] = 'EXPR_IMOD'
ExpressionOperantions[0x13] = 'EXPR_STUB'
ExpressionOperantions[0x14] = 'EXPR_IMUL_SAVE'
ExpressionOperantions[0x15] = 'EXPR_IDIV_SAVE'
ExpressionOperantions[0x16] = 'EXPR_IMOD_SAVE'
ExpressionOperantions[0x17] = 'EXPR_ADD_SAVE'
ExpressionOperantions[0x18] = 'EXPR_SUB_SAVE'
ExpressionOperantions[0x19] = 'EXPR_AND_SAVE'
ExpressionOperantions[0x1A] = 'EXPR_XOR_SAVE'
ExpressionOperantions[0x1B] = 'EXPR_OR_SAVE'
ExpressionOperantions[0x1C] = 'EXPR_EXEC_OP'
ExpressionOperantions[0x1D] = 'EXPR_NOT'
ExpressionOperantions[0x1E] = 'EXPR_TEST_SCENA_FLAGS'
ExpressionOperantions[0x1F] = 'EXPR_GET_RESULT'
ExpressionOperantions[0x20] = 'EXPR_PUSH_VALUE_INDEX'
ExpressionOperantions[0x21] = 'EXPR_GET_CHR_WORK'
ExpressionOperantions[0x22] = 'EXPR_RAND'
ExpressionOperantions[0x23] = 'EXPR_23'

for opr, expr in ExpressionOperantions.items():
    exec('EXPR_%02X = 0x%X' % (opr, opr))
    exec('%s = 0x%X' % (expr, opr))

class ScpExpression:
    def __init__(self, operation = None, operand = None):
        self.Operation = operation
        self.Operand = operand if operand != None else []

    def binary(self):
        return b''

    def WriteExpression(self, handlerdata):

        operation = self.Operation
        fs = handlerdata.FileStream

        def expr_exec():
            handlerdata.Assemble(self.Operand[0])

        operationmap = \
        {
            EXPR_PUSH_LONG          : lambda : fs.WriteULong(self.Operand[0]),
            EXPR_TEST_SCENA_FLAGS   : lambda : fs.WriteUShort(self.Operand[0]),
            EXPR_GET_RESULT         : lambda : fs.WriteUShort(self.Operand[0]),
            EXPR_PUSH_VALUE_INDEX   : lambda : fs.WriteByte(self.Operand[0]),
            EXPR_23                 : lambda : fs.WriteByte(self.Operand[0]),
            EXPR_GET_CHR_WORK       : lambda : fs.write(struct.pack('<HB', *self.Operand)),
            EXPR_EXEC_OP            : lambda : handlerdata.Assemble(self.Operand[0]),
        }

        fs.WriteByte(operation)

        if operation in operationmap:
            operationmap[operation]()

    def __str__(self):
        if self.Operation == EXPR_TEST_SCENA_FLAGS:

            offset, bit = SplitScenarioFlags(self.Operand[0])
            return 'scpexpr(%s, MakeScenarioFlags(0x%X, %d))' % (ExpressionOperantions[self.Operation], offset, bit)

        elif self.Operation != EXPR_EXEC_OP:

            txt = 'scpexpr(%s' % ExpressionOperantions[self.Operation]
            for opr in self.Operand:
                txt += ', 0x%X' % opr

            txt += ')'
            return txt

        from Assembler import Assembler2

        asm = Assembler2.Disassembler(edao_op_table)

        txt = 'scpexpr(%s' % ExpressionOperantions[self.Operation]
        for inst in self.Operand:
            data = HandlerData(HANDLER_REASON_FORMAT)
            data.Instruction    = inst
            data.TableEntry     = edao_op_table[inst.OpCode]
            txt += ', "%s"' % CombineMultiline(asm.FormatInstruction(data))

        txt += ')'
        return txt

def FormatExpressionList(exprlist):
    exprtxt = '%s' % exprlist[0]
    for expr in exprlist[1:]:
        exprtxt += ', %s' % expr

    return '(%s)' % exprtxt

def ParseScpExpression(data):
    expr = []
    fs = data.FileStream

    # stack size == 0xB0 ?

    while True:
        operation = fs.ReadByte()

        scpexpr = ScpExpression(operation)

        if operation == EXPR_PUSH_LONG:

            scpexpr.Operand.append(fs.ReadULong())

        elif operation == EXPR_END:

            break

        elif operation == EXPR_EQU            or \
             operation == EXPR_NEQ            or \
             operation == EXPR_LSS            or \
             operation == EXPR_GTR            or \
             operation == EXPR_LEQ            or \
             operation == EXPR_GE             or \
             operation == EXPR_EQUZ           or \
             operation == EXPR_NEQUZ_I64      or \
             operation == EXPR_AND            or \
             operation == EXPR_OR             or \
             operation == EXPR_ADD            or \
             operation == EXPR_SUB            or \
             operation == EXPR_NEG            or \
             operation == EXPR_XOR            or \
             operation == EXPR_IMUL           or \
             operation == EXPR_IDIV           or \
             operation == EXPR_IMOD           or \
             operation == EXPR_STUB           or \
             operation == EXPR_IMUL_SAVE      or \
             operation == EXPR_IDIV_SAVE      or \
             operation == EXPR_IMOD_SAVE      or \
             operation == EXPR_ADD_SAVE       or \
             operation == EXPR_SUB_SAVE       or \
             operation == EXPR_AND_SAVE       or \
             operation == EXPR_XOR_SAVE       or \
             operation == EXPR_OR_SAVE        or \
             operation == EXPR_NOT:

            # pop all operand, and push result
            pass

        elif operation == EXPR_EXEC_OP:

            # execute one op code

            execdata = data.CreateBranch()
            #execdata.Instruction.OpCode = data.TableEntry.Container.GetOpCode(fs)
            #execdata.TableEntry = data.TableEntry.Container[execdata.Instruction.OpCode]
            execinst = execdata.Disasm(execdata)
            scpexpr.Operand.append(execinst)

        elif operation == EXPR_TEST_SCENA_FLAGS or \
             operation == EXPR_GET_RESULT:

            scpexpr.Operand.append(fs.ReadUShort())

        elif operation == EXPR_PUSH_VALUE_INDEX:

            scpexpr.Operand.append(fs.ReadByte())

        elif operation == EXPR_GET_CHR_WORK:

            scpexpr.Operand.append(fs.ReadUShort())
            scpexpr.Operand.append(fs.ReadByte())

        elif operation == EXPR_RAND:

            pass

        elif operation == EXPR_23:

            scpexpr.Operand.append(fs.ReadByte())

        expr.append(scpexpr)

    expr.append(scpexpr)

    return expr

def scp_if(data):
    # if (expression)
    #   goto offset

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        expr = ParseScpExpression(data)
        ins.Operand.append(expr)

        offset = fs.ReadULong()
        ins.Operand.append(offset)
        ins.BranchTargets.append(offset)

        ins.OperandFormat = 'EO'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'EO'
        return None

SWITCH_DEFAULT  = -1

def scp_switch(data):

    # switch (expression)
    #     case option_id:
    #         goto option_offset;
    #     default:
    #         goto default_offset

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        expr = ParseScpExpression(data)
        optioncount = fs.ReadByte()
        options = []

        for i in range(optioncount):
            optionid, optionoffset = struct.unpack('<HL', fs.read(6))
            options.append((optionid, optionoffset))
            ins.BranchTargets.append(optionoffset)

        defaultoffset = fs.ReadULong()

        ins.BranchTargets.insert(0, defaultoffset)

        ins.Operand.append(expr)
        ins.Operand.append(options)
        ins.Operand.append(defaultoffset)

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:
        #   switch(
        #       Expression,
        #       (CaseID, CaseLabel),
        #       (CaseID, CaseLabel),
        #       (CaseID, CaseLabel),
        #       (-1,    DefaultLabel)
        #   )

        ins = data.Instruction
        entry = data.TableEntry

        txt = []
        txt.append('%s(' % entry.OpName)
        txt.append('    %s,' % FormatExpressionList(ins.Operand[0]))

        GetLabelName = entry.Container.GetLabelName
        #txt.append('    (')

        for case in ins.Operand[1]:
            txt.append('    (%d, "%s"),' % (case[0], GetLabelName(case[1])))

        txt.append('    (SWITCH_DEFAULT, "%s"),' % GetLabelName(ins.Operand[-1]))
        #txt.append('    )')
        txt.append(')')
        txt.append('')

        return txt

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        fs      = data.FileStream
        args    = data.Arguments
        entry   = data.TableEntry
        inst    = data.Instruction

        exprlist = args[0]
        optlist = args[1:]

        opts = []
        defaultoffset = None
        for opt in optlist:
            if opt[0] == SWITCH_DEFAULT:
                if defaultoffset != None:
                    raise Exception('multi default case')

                defaultoffset = opt[1]
            else:
                opts.append(opt)

        optlist = opts

        entry.Container.WriteOpCode(fs, inst.OpCode)

        for expr in exprlist:
            expr.WriteExpression(data)

        entry.WriteOperand(data, 'B', len(optlist))

        for opt in optlist:
            fs.WriteUShort(opt[0])
            inst.Labels.append(LabelEntry(opt[1], fs.tell()))
            fs.WriteULong(INVALID_OFFSET)

        inst.Labels.append(LabelEntry(defaultoffset, fs.tell()))
        fs.WriteULong(INVALID_OFFSET)

        return inst

def scp_new_scene(data):

    if data.Reason == HANDLER_REASON_DISASM:

        data.Instruction.OperandFormat = 'LCCC'

    elif data.Reason == HANDLER_REASON_FORMAT:

        ins = data.Instruction

        symbol = '%s("%s", %d, %d, %d)' % (
                    data.TableEntry.OpName, ScenarioFileIndex(ins.Operand[0]).Name(),
                    ins.Operand[1], ins.Operand[2], ins.Operand[3]
                )

        return [symbol]

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Arguments[0] = ScenarioFileIndex(data.Arguments[0]).Index()
        data.Instruction.OperandFormat = 'LCCC'

def scp_battle(data):

    operand_with_battle_info = 'OLBWWW'
    operand_without_battle_info = 'LLS' + ('L' * 4) + ('L' * 8) + 'WW'

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        entry = data.TableEntry

        BattleInfoOffset, opr2 = entry.GetAllOperand('LL', fs)

        ins.Operand.append(BattleInfoOffset)
        ins.Operand.append(opr2)

        if BattleInfoOffset != 0xFFFFFFFF:

            ins.Operand.append(fs.ReadByte())
            ins.Operand.append(fs.ReadUShort())
            ins.Operand.append(fs.ReadUShort())
            ins.Operand.append(fs.ReadUShort())

            ins.BranchTargets.append(BattleInfoOffset)

            ins.OperandFormat = operand_with_battle_info

            return ins

        name = entry.GetOperand('S', fs)
        ins.Operand.append(name)

        for i in range(4):
            ins.Operand.append(fs.ReadULong())

        for i in range(8):
            ins.Operand.append(fs.ReadULong())

        ins.Operand += entry.GetAllOperand('WW', fs)

        ins.OperandFormat = operand_without_battle_info

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        ins = data.Instruction
        entry = data.TableEntry

        BattleInfoOffset = ins.Operand[0]
        if BattleInfoOffset == 0xFFFFFFFF:
            return

        p = '%s("BattleInfo_%X", ' % (entry.OpName, BattleInfoOffset)

        paramlist = BuildFormatOperandParameterList(
                        ins.OperandFormat[1:],
                        ins.Operand[1:],
                        ins.Flags,
                        data.LabelMap
                    )

        return [p + entry.FormatAllOperand(paramlist) + ')']

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        ins = data.Instruction
        BattleInfoOffset = data.Arguments[0]
        ins.OperandFormat = operand_with_battle_info if type(BattleInfoOffset) == str else operand_without_battle_info


# SetBarrier(op_0, id, type, 0, x, z, y, cx, cy, degree * 1000)
# op: 0 = create
# type: 1 = line, 2 = circle

def scp_1d(data):

    def getopr(opr1):
        operand = ''

        if opr1 == 0:
            operand = 'BBiiiiii'
        elif opr1 == 2 or opr1 == 3:
            operand = 'B'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('BB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = getopr(opr1)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'BB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr1 = data.Arguments[0]
        operand = getopr(opr1)

        data.Instruction.OperandFormat = 'BB' + operand

def scp_29(data):

    def getopr(opr2):
        operand = ''

        if opr2 == 1 or opr2 == 2:
            operand = 'W'
        elif opr2 == 3 or opr2 == 4:
            operand = 'B'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('WB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = getopr(opr2)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WB' + getopr(data.Arguments[1])

def scp_2a(data):

    def getopr(opr2): return 'W' if opr2 == 1 else 'B'

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('WB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = getopr(opr2)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr2 = data.Arguments[1]
        data.Instruction.OperandFormat = 'WB' + getopr(opr2)

def scp_2b(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        for i in range(0xC):
            opr = fs.ReadUShort()
            ins.Operand.append(opr)
            if opr == 0xFFFF:
                break

        ins.OperandFormat = 'W' * len(ins.Operand)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'W' * min(0xC, len(data.Arguments))

def scp_38(data):

    def getopr(opr2):
        operand = ''

        if opr2 == 0x7F:
            operand = 'B'
        elif opr2 >= 0x80 and opr2 <= 0x87:
            operand = 'B'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr1, opr2 = data.TableEntry.GetAllOperand('BB', fs)

        ins.Operand.append(opr1)
        ins.Operand.append(opr2)

        operand = getopr(opr2)

        if opr2 == 0x7F:
            operand = 'B'
        elif opr2 >= 0x80 and opr2 <= 0x87:
            operand = 'B'

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'BB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BB' + getopr(data.Arguments[1])


def scp_lambda_worker(data, extra_length):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        target, tid, length = data.TableEntry.GetAllOperand('WBB', fs)

        length += extra_length

        pos = fs.tell()
        block = data.DisasmBlock(pos, length)
        fs.seek(pos + length)

        ins.Operand = [target, tid, block]

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        '''

        def lambda_xxx():
            OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
            OP_00()

        X(ChrId, ChrThreadId, lambda_xxx)

        '''

        ins = data.Instruction
        entry = data.TableEntry
        target, tid, lambdablock = ins.Operand

        lambda_name = 'lambda_%X' % lambdablock.Offset

        txt = ['', 'def %s():' % lambda_name]

        for inst in lambdablock.Instructions:
            lambdadata = data.CreateBranch()
            lambdadata.Instruction = inst
            lambdabody = lambdadata.Format(lambdadata)
            for i in range(len(lambdabody)):
                if lambdabody[i] == '':
                    continue
                lambdabody[i] = '    ' + lambdabody[i]

            txt += lambdabody

        txt.append('')

        txt.append('%s(0x%X, %d, %s)' % (data.TableEntry.OpName, target, tid, lambda_name))

        return txt


    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        fs      = data.FileStream
        entry   = data.TableEntry
        inst    = data.Instruction

        target, tid, lambdafunc = data.Arguments

        entry.Container.WriteOpCode(fs, inst.OpCode)

        entry.WriteOperand(data, 'W', target)
        entry.WriteOperand(data, 'B', tid)

        fs.seek(1, io.SEEK_CUR)
        pos = fs.tell()

        lambdafunc()

        pos2 = fs.tell()

        if pos2 - pos > 0xFF:
            raise Exception('lambda must be smaller than 0x100 bytes: current = %X' % (pos2 - pos))

        fs.seek(pos - 1)
        entry.WriteOperand(data, 'B', pos2 - pos - extra_length)

        fs.seek(pos2)

        return inst


def scp_46(data):
    return scp_lambda_worker(data, 1)               # ExitThread

def scp_47(data):
    return scp_lambda_worker(data, 1 + 5)       # Yield, Jump(Offset)


def scp_4e(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('W', fs)
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'WE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WE'

def scp_50(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.ReadByte())
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'BE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BE'

def scp_52(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WB', fs)
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'WBE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WBE'

def scp_anonymous_talk(data):

    if data.Reason == HANDLER_REASON_DISASM:
        fs = data.FileStream
        ins = data.Instruction

        target, text = data.TableEntry.GetAllOperand('WS', fs)

        ins.Operand.append(target)
        ins.Operand.append(text)

        ins.OperandFormat = 'WS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WS'

def scp_create_chr_talk(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand = data.TableEntry.GetAllOperand('WS', fs)

        ins.OperandFormat = 'WS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WS'

def scp_create_npc_talk(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        target, name, text = data.TableEntry.GetAllOperand('WSS', fs)

        ins.Operand.append(target)
        ins.Operand.append(name)
        ins.Operand.append(text)

        ins.OperandFormat = 'WSS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat)

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WSS'

def scp_create_menu(data):

    # max 10 line ?

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('hhhc', fs)
        menuitems = data.TableEntry.GetOperand('S', fs)
        ins.Operand.append(menuitems)

        ins.OperandFormat = 'hhhcS'

        return ins

    elif data.Reason == HANDLER_REASON_FORMAT:

        return FormatFuncString(data, data.Instruction.OperandFormat, -1)

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'hhhcS'

def scp_76(data):

    def getopr(opr3):
        operand = ''
        if opr3 == 0 or \
           opr3 == 1 or \
           opr3 == 3:

            operand = 'L'

        elif opr3 == 2:

            operand = 'S'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('BSB', fs)

        opr3 = ins.Operand[2]

        operand = getopr(opr3)
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'BSB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        opr3 = data.Arguments[2]

        data.Instruction.OperandFormat = 'BSB' + getopr(opr3)

def scp_set_event_skip(data):

    if data.Reason == HANDLER_REASON_DISASM:

        ins = data.Instruction
        fs = data.FileStream

        cleareventskip, offset = data.TableEntry.GetAllOperand('BL', fs)
        ins.OperandFormat = 'BL' if cleareventskip else 'BO'
        ins.Operand = [cleareventskip, offset]

        if not cleareventskip:
            ins.BranchTargets.append(offset)

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        ins = data.Instruction
        cleareventskip, offset = data.Arguments[0], data.Arguments[1]

        ins.OperandFormat = 'BL' if cleareventskip else 'BO'

def scp_9f(data):

    def getopr(opr):

        if opr == 0:
            operand = 'W'
        elif opr == 1:
            operand = 'iii'
        else:
            operand = 'WiB'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('B', fs)

        opr = ins.Operand[0]
        operand = getopr(opr)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'B' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'B' + getopr(data.Arguments[0])

def scp_a1(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        ins.Operand = data.TableEntry.GetAllOperand('WWB', fs)

        operand = 'B' * ins.Operand[-1]
        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'WWB' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'WWB' + 'B' * (len(data.Arguments) - 3)
        return None


def MakeScenarioFlags(offset, bit):
    return (offset << 3) | (bit & 7)

def SplitScenarioFlags(flags):
    return (flags >> 3), (flags & 7)

def scp_set_scenario_flags(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        offset, bit = SplitScenarioFlags(data.TableEntry.GetOperand('W', fs))

        ins.Operand = [offset, bit]
        ins.OperandFormat = 'WC'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'W'

        if len(data.Arguments) == 2:
            offset, bit = data.Arguments[0], data.Arguments[1]
            if offset >= 0x220:
                raise Exception('offset must be less than 0x220')

            data.Arguments = [MakeScenarioFlags(offset, bit)]

def scp_clear_scenario_flags(data):
    return scp_set_scenario_flags(data)

def scp_cf(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        operand = 'BB'
        ins.Operand = data.TableEntry.GetAllOperand(operand, fs)

        if ins.Operand[0] != 0:
            ins.Operand += data.TableEntry.GetAllOperand('B', fs)
            operand += 'B'

        ins.OperandFormat = operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BB' + ('B' if data.Arguments[0] != 0 else '')

def scp_menu_cmd(data):

    def getopr(menutype):
        operand = ''

        if menutype == 0: pass
        elif menutype == 1: operand = 'S'
        elif menutype == 2: operand = 'hhC'
        elif menutype == 3: operand = 'B'
        elif menutype == 4: operand = 'B'
        elif menutype == 5: operand = 'B'
        elif menutype == 6: pass

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream

        ins = Instruction()
        ins = data.Instruction

        menutype, layer = data.TableEntry.GetAllOperand('BC', fs)

        ins.Operand.append(menutype)
        ins.Operand.append(layer)

        operand = getopr(menutype)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'CC' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BB' + getopr(data.Arguments[0])

def scp_d2(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction
        ins.Operand.append(fs.ReadByte())
        ins.Operand.append(ParseScpExpression(data))

        ins.OperandFormat = 'BE'

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BE'

def scp_load_chr(data):

    if data.Reason == HANDLER_REASON_DISASM:

        data.Instruction.OperandFormat = 'LB'

    elif data.Reason == HANDLER_REASON_FORMAT:

        ins = data.Instruction

        return ['%s("%s", 0x%X)' % (data.TableEntry.OpName, ScenarioChipInfo(ins.Operand[0]), ins.Operand[1])]

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Arguments[0] = ScenarioChipInfo(data.Arguments[0]).fileindex()
        data.Instruction.OperandFormat = 'LB'

def scp_e4(data):

    def getopr(opr):
        operand = ''
        if opr == 0: operand = 'BB'
        elif opr == 1: operand = 'B'
        elif opr == 2: operand = 'B'
        elif opr == 3: pass

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        opr = data.TableEntry.GetOperand('B', fs)
        ins.Operand.append(opr)

        operand = getopr(opr)

        ins.Operand += data.TableEntry.GetAllOperand(operand, fs)

        ins.OperandFormat = 'B' + operand

        return ins

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'B' + getopr(data.Arguments[0])

edao_op_list = \
[
    inst(ExitThread),
    inst(Return,                    NO_OPERAND,             INSTRUCTION_END_BLOCK),
    inst(Jc,                        NO_OPERAND,             INSTRUCTION_START_BLOCK,    scp_if),
    inst(Jump,                      'O',                    INSTRUCTION_JUMP),
    inst(Switch,                    NO_OPERAND,             INSTRUCTION_END_BLOCK,      scp_switch),
    inst(Call,                      'CC'),          # Call(scp index, func index)
    inst(NewScene,                  NO_OPERAND,             0,                          scp_new_scene),
    inst(IdleLoop),
    inst(Sleep,                     'H'),
    inst(SetMapFlags,               'L'),
    inst(ClearMapFlags,             'L'),
    inst(FadeToDark,                'iic'),
    inst(FadeToBright,              'ii'),
    inst(OP_0D),
    inst(Fade,                      'I'),
    inst(Battle,                    NO_OPERAND,             0,                          scp_battle),
    inst(OP_10,                     'BB'),
    inst(OP_11,                     'BBBLLL'),
    inst(StopSound,                 'HHC'),
    inst(OP_13,                     'W'),   # poswnd
    inst(BlurSwitch,                'WLWBW'),
    inst(CancelBlur,                'I'),
    inst(OP_16,                     'B'),
    inst(ShowSaveMenu),
    inst(EventBegin,                'B'),
    inst(EventEnd,                  'B'),
    inst(OP_1B,                     'BBW'),
    inst(OP_1C,                     'BBBBBBWW'),
    inst(SetBarrier,                NO_OPERAND,             0,                          scp_1d),    # see scp_1d
    inst(PlayBGM,                   'MC'),
    inst(OP_1F),
    inst(VolumeBGM,                 'BL'),
    inst(StopBGM,                   'L'),
    inst(WaitBGM),
    inst(Sound,                     'HCCC'),
    inst(OP_24,                     'W'),
    inst(OP_25,                     'WB'),
    inst(SoundDistance,             'WLLLLLBL'),
    inst(SoundLoad,                 'H'),
    inst(Yield),
    inst(OP_29,                     NO_OPERAND,             0,                          scp_29),
    inst(OP_2A,                     NO_OPERAND,             0,                          scp_2a),
    inst(OP_2B,                     NO_OPERAND,             0,                          scp_2b),
    inst(OP_2C,                     'WW'),
    inst(OP_2D,                     'WW'),
    inst(AddParty,                  'BBB'),
    inst(RemoveParty,               'BB'),
    inst(ClearParty),
    inst(OP_31,                     'B'),
    inst(OP_32,                     'BBW'),
    inst(RemoveCraft,               'BW'),
    inst(AddCraft,                  'BW'),
    inst(OP_37),
    inst(OP_38,                     NO_OPERAND,             0,                          scp_38),
    inst(AddSepith,                 'BH'),          # AddSepith(0~6 or 0xFF, number)
    inst(SubSepith,                 'BH'),
    inst(AddMira,                   'H'),
    inst(SubMira,                   'H'),
    inst(OP_3D,                     'W'),
    inst(OP_3E,                     'W'),
    inst(AddItemNumber,             'Th'),
    inst(SubItemNumber,             'Th'),
    inst(GetItemNumber,             'TB'),
    inst(OP_42,                     'BWB'),
    inst(GetPartyIndex,             'B'),           # GetPartyIndex(chr_id)     return chr index of team member
    inst(BeginChrThread,            'WCCC'),
    inst(EndChrThread,              'WB'),
    inst(QueueWorkItem,             NO_OPERAND,             0,                          scp_46),
    inst(QueueWorkItem2,            NO_OPERAND,             0,                          scp_47),
    inst(WaitChrThread,             'WC'),
    inst(OP_49),
    inst(Event,                     'CC'),
    inst(OP_4B,                     'WB'),
    inst(OP_4C,                     'WB'),
    inst(OP_4D),
    inst(RunExpression,             NO_OPERAND,             0,                          scp_4e),
    inst(OP_4F),
    inst(OP_50,                     NO_OPERAND,             0,                          scp_50),
    inst(OP_51),
    inst(OP_52,                     NO_OPERAND,             0,                          scp_52),
    inst(TalkBegin,                 'W'),
    inst(TalkEnd,                   'W'),
    inst(AnonymousTalk,             NO_OPERAND,             0,                          scp_anonymous_talk),
    inst(OP_56),
    inst(OP_57,                     'B'),
    inst(MenuTitle,                 'hhhS'),
    inst(CloseMessageWindow),
    inst(OP_5A),
    inst(SetMessageWindowPos,       'hhhh'),        # SetMessageWindowPos(x, y, -1, -1)
    inst(ChrTalk,                   NO_OPERAND,             0,                          scp_create_chr_talk),
    inst(NpcTalk,                   NO_OPERAND,             0,                          scp_create_npc_talk),
    inst(Menu,                      NO_OPERAND,             0,                          scp_create_menu),
    inst(MenuEnd,                   'W'),
    inst(OP_60,                     'W'),
    inst(SetChrName,                'S'),
    inst(OP_62,                     'W'),
    inst(OP_63,                     'WLIBBLB'),
    inst(OP_64,                     'W'),
    inst(OP_65,                     'BW'),
    inst(OP_66,                     'BW'),
    inst(OP_67,                     'W'),
    inst(OP_68,                     'iiii'),
    inst(OP_69,                     'BW'),
    inst(OP_6A,                     'WL'),
    inst(OP_6B,                     'W'),
    inst(SetCameraDistance,         'ii'),          # SetCameraDistance(distance, duration)
    inst(MoveCamera,                'hhhi'),        # MoveCamera(horizon, vertical, obliquity, duration)
    inst(OP_6E,                     'ii'),
    inst(OP_6F,                     'B'),
    inst(OP_70,                     'BW'),
    inst(OP_71,                     'BWWWL'),
    inst(SetMapObjFlags,            'BL'),
    inst(ClearMapObjFlags,          'BL'),
    inst(OP_74,                     'WB'),
    inst(OP_75,                     'BBL'),
    inst(SetMapObjFrame,            NO_OPERAND,             0,                          scp_76),
    inst(OP_77,                     'BW'),
    inst(OP_78,                     'BW'),
    inst(OP_79,                     'W'),
    inst(SetEventSkip,              NO_OPERAND,             INSTRUCTION_START_BLOCK,    scp_set_event_skip),
    inst(OP_7B,                     'B'),
    inst(OP_7D,                     'BBBBL'),
    inst(OP_82,                     'LLLL'),
    inst(SetChrChip,                'BWWW'),
    inst(OP_84,                     'BB'),
    inst(LoadEffect,                'BS'),
    inst(PlayEffect,                'BBWWiiihhhiiiwiiii'),
    inst(OP_87,                     'BBBSWLLLWWWLLLL'),
    inst(StopEffect,                'BB'),
    inst(OP_89,                     'BB'),
    inst(OP_8A,                     'B'),
    inst(OP_8B,                     'W'),
    inst(SetChrChipByIndex,         'WB'),
    inst(SetChrSubChip,             'WB'),
    inst(OP_8E,                     'WS'),
    inst(SetChrPos,                 'WiiiH'),
    inst(OP_90,                     'Wiiih'),
    inst(TurnDirection,             'WWH'),
    inst(OP_92,                     'WLLW'),
    inst(OP_93,                     'WWW'),
    inst(OP_94,                     'WLLLLL'),
    inst(OP_95,                     'WiiiiB'),
    inst(OP_96,                     'WLLLLB'),
    inst(OP_97,                     'WLLLLB'),
    inst(OP_98,                     'WLLLLB'),
    inst(OP_99,                     'WWLLB'),
    inst(OP_9A,                     'WWLLB'),
    inst(OP_9B,                     'BWWLLB'),
    inst(OP_9C,                     'WLLLLL'),
    inst(OP_9D,                     'WLLLLL'),
    inst(OP_9E,                     'WLLLLW'),
    inst(OP_9F,                     NO_OPERAND,             0,                          scp_9f),
    inst(OP_A0,                     'WHBB'),
    inst(OP_A1,                     NO_OPERAND,             0,                          scp_a1),
    inst(SetChrFlags,               'WW'),
    inst(ClearChrFlags,             'WW'),
    inst(SetChrBattleFlags,         'WW'),
    inst(ClearChrBattleFlags,       'WW'),
    inst(OP_A6,                     'WLLLL'),
    inst(OP_A7,                     'WBBBBL'),
    inst(OP_A8,                     'WBBBL'),
    inst(SetScenarioFlags,          NO_OPERAND,             0,                          scp_set_scenario_flags),
    inst(ClearScenarioFlags,        NO_OPERAND,             0,                          scp_clear_scenario_flags),
    inst(OP_AB,                     'W'),
    inst(OP_AC,                     'W'),
    inst(OP_AD,                     'W'),
    inst(OP_AE,                     'WW'),
    inst(OP_AF,                     'B'),
    inst(OP_B2,                     'W'),
    inst(OutputDebugInt,            'B'),
    inst(OP_B4,                     'B'),
    inst(OP_B5,                     'BW'),
    inst(LoadOps),                                                  # obsolete
    inst(ModifyEventFlags,          'CCW'),     # ModifyEventFlags(set_or_clear, event_index, flags)   0: set, 1: clear
    inst(PlayMovie,                 'BSWW'),
    inst(OP_B9,                     'B'),
    inst(ReplaceBGM,                'MM'),
    inst(OP_BC,                     'B'),
    inst(UseItem,                   'WW'),
    inst(OP_BE,                     'BW'),
    inst(OP_BF,                     'BB'),
    inst(SetChrChipPat,             'BBL'),                         # SetChrChipPat(chr_id, func_id, param)
    inst(LoadChrChipPat),
    inst(OP_C3,                     'BBWWWBiiiiii'),
    inst(OP_C4,                     'BBWW'),
    inst(MiniGame,                  'BLLLLLLLL'),
    inst(OP_C7,                     'BB'),
    inst(OP_C9,                     'BL'),
    inst(CreatePortrait,            'CHHHHHHHHHHHHLBS'),
    inst(OP_CB,                     'BBLLLL'),
    inst(OP_CC,                     'BBB'),
    inst(PlaceName2,                'hhSBh'),       # PlaceName2(x, y, itp_name, 0, duration)
    inst(PartySelect,               'C'),           # PartySelect(0 = select menu, save = 1, restore = 2)
    inst(OP_CF,                     NO_OPERAND,             0,                          scp_cf),
    inst(MenuCmd,                   NO_OPERAND,             0,                          scp_menu_cmd),
    inst(OP_D1,                     'W'),
    inst(OP_D2,                     NO_OPERAND,             0,                          scp_d2),
    inst(OP_D3,                     'WBS'),
    inst(OP_D4,                     'LL'),
    inst(OP_D5,                     'WLLLL'),
    inst(LoadChrToIndex,            NO_OPERAND,             0,                          scp_load_chr),
    inst(OP_D7,                     'B'),
    inst(OP_D8,                     'BB'),
    inst(OP_D9,                     'BB'),
    inst(OP_DA,                     'B'),
    inst(OP_DC,                     'B'),
    inst(OP_DD),
    inst(OP_DE,                     'S'),
    inst(LoadAnimeChip,             'WBB'),
    inst(OP_E0,                     'BB'),
    inst(OP_E2,                     'B'),
    inst(OP_E3,                     'LLL'),
    inst(OP_E4,                     NO_OPERAND,             0,                          scp_e4),
    inst(OP_E5,                     'B'),
    inst(OP_E6,                     'BBBBBBL'),
    inst(OP_E7),
    inst(OP_E8),
    inst(ShowSaveClearMenu),
    inst(OP_F0,                     'BW'),
    inst(OP_F3,                     'i'),
    inst(OP_F4,                     'B'),
    inst(OP_FA,                     'W'),
    inst(OP_FB,                     'WB'),
    inst(OP_FC,                     'W'),
    inst(OP_FD,                     'WW'),
    inst(OP_FE,                     'B'),
    inst(OP_FF,                     'BLLL'),
]

del inst

for op in edao_op_list:
    edao_op_table[op.OpCode] = op
    op.Container = edao_op_table



'''

MenuCmd(0x0, 1)
cmd: 0 = create
layer: 1

MenuCmd(0x1, 1, '莉夏')
cmd: 1 = add item
layer: 1
text:

MenuCmd(0x2, 1, 15, 45, 0x1)
cmd: 2 = show
layer: 1
x: 15
y: 45
unknown: 1



羁绊
OP_50(chr_offset, (scpexpr(EXPR_PUSH_LONG, const), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
0x64: 琪雅
0x65: 艾莉
0x66: 缇欧
0x67: 兰迪
0x68: 诺艾尔
0x69: 瓦吉
0x6A: 莉夏
0x6C: 伊莉娅
0x6D: 塞茜尔
0x6E: 芙兰
0x6F: 修利

'''




if __name__ == '__main__':
    valid = 0
    for inst in edao_op_list:
        if inst.OpName[:3] != 'OP_':
            valid += 1
    print('known: %d (%d%%)' % (valid, valid / len(edao_op_list) * 100))
    print('total: %d' % len(edao_op_list))
    console.pause()
