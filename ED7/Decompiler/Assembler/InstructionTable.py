from Base.EDAOBase import *

def DefaultOpCodeHandler(data):
    entry   = data.TableEntry
    fs      = data.FileStream
    inst    = data.Instruction
    oprs    = inst.OperandFormat
    values  = data.Arguments

    entry.Container.WriteOpCode(fs, inst.OpCode)

    if len(oprs) != len(values):
        raise Exception('operand: does not match values')

    for i in range(len(oprs)):
        entry.WriteOperand(data, oprs[i], values[i])

    return inst

def OpCodeHandlerPrivate(data):
    op = data.Instruction.OpCode
    entry = data.TableEntry

    handler = entry.Handler if entry.Handler != None else DefaultOpCodeHandler
    inst = handler(data)

    if inst == None:
        inst = DefaultOpCodeHandler(data)

    return inst


HANDLER_REASON_DISASM       = 0
HANDLER_REASON_WRITE        = 1
HANDLER_REASON_FORMAT       = 2
HANDLER_REASON_FUNCTION     = 3
HANDLER_REASON_ASSEMBLE     = 4

class HandlerData:
    def __init__(self, reason):
        self.Reason         = reason
        self.FileStream     = None
        self.Instruction    = None
        self.Arguments      = None
        self.LabelMap       = {}

        # list of LabelEntry
        self.Labels = []

        self.InstructionTable   = None
        self.TableEntry         = None

        self.Disasm         = None
        self.DisasmBlock    = None
        self.Format         = None
        self.Assemble       = None

    def CreateBranch(self):
        data = HandlerData(self.Reason)

        data.FileStream         = self.FileStream
        data.Instruction        = Instruction()

        data.Labels             = []
        data.InstructionTable   = self.InstructionTable
        data.TableEntry         = None

        data.Disasm             = self.Disasm
        data.DisasmBlock        = self.DisasmBlock
        data.Format             = self.Format
        data.Assemble           = self.Assemble

        if self.Reason == HANDLER_REASON_FORMAT:
            data.LabelMap = self.LabelMap

        return data

#
#   def inst_handler(data):
#
#       if data.Reason == HANDLER_REASON_DISASM:
#
#           data.fs = BytesStream
#           return Instruction object
#
#       elif data.Reason == HANDLER_REASON_WRITE:
#
#           data.inst = Instruction object
#           data.inst.labels.append(LabelEntry('label name', label_offset_in_bytes))
#           return Instruction object
#
#       elif data.Reason == HANDLER_REASON_FORMAT:
#
#           return 'formatted instruction'
#
#       return None
#

def DefaultGetLabelName(offset):
    return 'loc_%X' % offset

class InstructionTable(dict):
    def __init__(self, GetOpCode, WriteOpCode, GetLabelName = DefaultGetLabelName, CodePage = CODE_PAGE):
        self.GetOpCode      = GetOpCode
        self.WriteOpCode    = WriteOpCode
        self.GetLabelName   = GetLabelName
        self.CodePage       = CodePage

NO_OPERAND = ''

class FormatOperandParameter:
    def __init__(self, Operand = NO_OPERAND, Value = None, Flags = None, LabelMap = None):
        self.Operand     = Operand
        self.Value       = Value
        self.Flags       = Flags
        self.LabelMap    = LabelMap if LabelMap != None else {}

def BuildFormatOperandParameterList(OperandFormats, ValueList, Flags = 0, LabelMap = None):
    oprs = list(OperandFormats)
    values = ValueList

    if len(oprs) != len(values):
        raise Exception('operand: does not match values (%d / %d)' % (len(oprs), len(values)))

    paramlist = []
    for i in range(len(oprs)):
        paramlist.append(FormatOperandParameter(oprs[i], values[i], Flags, LabelMap))

    return paramlist

class InstructionTableEntry:
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        self.OpCode     = op
        self.OpName     = name
        self.Operand    = operand
        self.Flags      = InstructionFlags(flags)
        self.Handler    = handler
        self.Container  = None

    def WriteOperand(self, data, opr, value):

        fs = data.FileStream
        labels = data.Instruction.Labels

        def wlabel():
            labels.append(LabelEntry(value, fs.tell()))
            fs.WriteULong(INVALID_OFFSET)

        def wlabelshort():
            labels.append(LabelEntry(value, fs.tell()))
            fs.WriteUShort(INVALID_OFFSET)

        oprtype = \
        {
            'c' : lambda : fs.WriteChar(value),
            'C' : lambda : fs.WriteByte(value),

            'b' : lambda : fs.WriteChar(value),
            'B' : lambda : fs.WriteByte(value),

            'w' : lambda : fs.WriteShort(value),
            'W' : lambda : fs.WriteUShort(value),

            'h' : lambda : fs.WriteShort(value),
            'H' : lambda : fs.WriteUShort(value),

            'l' : lambda : fs.WriteLong(value),
            'L' : lambda : fs.WriteULong(value),

            'i' : lambda : fs.WriteLong(value),
            'I' : lambda : fs.WriteULong(value),

            'q' : lambda : fs.WriteLong64(value),
            'Q' : lambda : fs.WriteULong64(value),

            'f' : lambda : fs.WriteFloat(value),
            'd' : lambda : fs.WriteFloat(value),

            's' : lambda : fs.Write(value),
            'S' : lambda : fs.Write(value.encode(data.TableEntry.Container.CodePage) + b'\x00'),

            'o' : wlabelshort,
            'O' : wlabel,
        }

        return oprtype[opr]()

    def FormatAllOperand(self, paramlist):
        oprs = 0
        values = 0
        for param in paramlist:
            if param.Operand != None: oprs += 1
            if param.Value   != None: values += 1

        if oprs != values:
            raise Exception('operand: does not match values (%d / %d)' % (oprs, values))

        if oprs == 0:
            return ''

        oprtext = self.FormatOperand(paramlist[0])

        for i in range(1, len(paramlist)):
            tmp = ', ' + self.FormatOperand(paramlist[i])
            oprtext += tmp

        return oprtext

    def FormatOperand(self, param):

        labelmap = param.LabelMap
        value = param.Value
        opr = param.Operand

        oprtype = \
        {
            'c' : lambda : '%d' % value,
            'C' : lambda : '%d' % value,

            'b' : lambda : '0x%X' % value,
            'B' : lambda : '0x%X' % value,

            'w' : lambda : '0x%X' % value,
            'W' : lambda : '0x%X' % value,

            'h' : lambda : '%d' % value,
            'H' : lambda : '%d' % value,

            'l' : lambda : '0x%X' % value,
            'L' : lambda : '0x%X' % value,

            'i' : lambda : '%d' % value,
            'I' : lambda : '%d' % value,

            'q' : lambda : '0x%X' % value,
            'Q' : lambda : '0x%X' % value,

            'f' : lambda : '%f' % value,
            'd' : lambda : '%f' % value,

            's' : lambda : '%s' % value,
            'S' : lambda : '"%s"' % value,

            'o' : lambda : '"%s"' % (labelmap[value] if value in labelmap else DefaultGetLabelName(value)),
            'O' : lambda : '"%s"' % (labelmap[value] if value in labelmap else DefaultGetLabelName(value)),
        }

        opr = oprtype[opr]
        return opr()

    def GetAllOperand(self, oprs, fs):
        operand = []
        for opr in oprs:
            operand.append(self.GetOperand(opr, fs))

        return operand

    def GetOperand(self, opr, fs):
        def readstr():
            string = fs.ReadMultiByte(self.Container.CodePage)
            return string

        oprtype = \
        {
            'c' : lambda : struct.unpack('<b', fs.read(1))[0],
            'C' : lambda : struct.unpack('<B', fs.read(1))[0],
            'b' : lambda : struct.unpack('<b', fs.read(1))[0],
            'B' : lambda : struct.unpack('<B', fs.read(1))[0],

            'h' : lambda : struct.unpack('<h', fs.read(2))[0],
            'H' : lambda : struct.unpack('<H', fs.read(2))[0],
            'w' : lambda : struct.unpack('<h', fs.read(2))[0],
            'W' : lambda : struct.unpack('<H', fs.read(2))[0],

            'i' : lambda : struct.unpack('<l', fs.read(4))[0],
            'I' : lambda : struct.unpack('<L', fs.read(4))[0],
            'l' : lambda : struct.unpack('<l', fs.read(4))[0],
            'L' : lambda : struct.unpack('<L', fs.read(4))[0],

            'q' : lambda : struct.unpack('<q', fs.read(8))[0],
            'Q' : lambda : struct.unpack('<Q', fs.read(8))[0],

            'f' : lambda : struct.unpack('<f', fs.read(4))[0],
            'd' : lambda : struct.unpack('<d', fs.read(8))[0],

            #'s' : readstr,
            'S' : readstr,

            'o' : lambda : struct.unpack('<H', fs.read(2))[0],
            'O' : lambda : struct.unpack('<L', fs.read(4))[0],
        }

        opr = oprtype[opr]
        return opr()

    def GetOperandSize(self, opr, fs):
        oprsize = \
        {
            'c' : lambda : 1,
            'C' : lambda : 1,
            'b' : lambda : 1,
            'B' : lambda : 1,

            'h' : lambda : 2,
            'H' : lambda : 2,
            'w' : lambda : 2,
            'W' : lambda : 2,

            'i' : lambda : 4,
            'I' : lambda : 4,
            'l' : lambda : 4,
            'L' : lambda : 4,

            'q' : lambda : 8,
            'Q' : lambda : 8,

            'f' : lambda : 4,
            'd' : lambda : 8,

            's' : lambda : self.GetOperand(opr, fs),
            'S' : lambda : self.GetOperand(opr, fs),

            'o' : lambda : 2,   # short offset
            'O' : lambda : 4,   # offset
        }

        pos = fs.tell()
        oprsize = oprsize[opr]()
        fs.seek(pos)
        return oprsize

    def __str__(self):
        s = []
        s.append('op        = %08X' % self.OpCode)
        s.append('name      = %s'   % self.OpName)
        s.append('operand   = %s' % (self.Operand if self.Operand != NO_OPERAND else 'NO_OPERAND'))
        s.append('flags     = %08X' % self.Flags.Flags)
        s.append('handler   = %s'   % self.Handler)

        return '\r\n'.join(s)
