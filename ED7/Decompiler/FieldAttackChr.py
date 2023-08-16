from Assembler.Assembler2 import *
from Base.EDAOBase import *

def GetOpCode(fs):
    return fs.ReadByte()

def WriteOpCode(fs, op):
    return fs.WriteByte(op)

edao_fa_op_table = InstructionTable(GetOpCode, WriteOpCode, DefaultGetLabelName, CODE_PAGE)

InstructionNames = {}

InstructionNames[0x00] = 'Return'
InstructionNames[0x01] = 'SetChrSubChip'
InstructionNames[0x02] = 'Sleep'
InstructionNames[0x03] = 'PlayEffect'
InstructionNames[0x04] = 'Sound'
InstructionNames[0x05] = 'Voice'
InstructionNames[0x06] = 'FA_06'
InstructionNames[0x07] = 'FA_07'
InstructionNames[0x08] = 'FA_08'
InstructionNames[0x09] = 'FA_09'
InstructionNames[0x0A] = 'BlurSwitch'
InstructionNames[0x0B] = 'FA_0B'
InstructionNames[0x0C] = 'FA_0C'
InstructionNames[0x0D] = 'FA_0D'


for op, name in InstructionNames.items():
    expr = '%s = 0x%08X' % (name, op)
    exec(expr)

class EDAOFAOpTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return EDAOFAOpTableEntry(op, InstructionNames[op], operand, flags, handler)


edao_fa_op_list = \
[
    inst(Return,             NO_OPERAND,             INSTRUCTION_END_BLOCK),
    inst(SetChrSubChip,     'C'),
    inst(Sleep,             'H'),
    inst(PlayEffect,        'WHHHHHB'),
    inst(Sound,             'H'),
    inst(Voice,             'HHHH'),
    inst(FA_06,             NO_OPERAND),
    inst(FA_07,             NO_OPERAND),
    inst(FA_08,             'h'),
    inst(FA_09,             'HH'),
    inst(BlurSwitch,        'HH'),
    inst(FA_0B,             'H'),
    inst(FA_0C,             'WW'),
    inst(FA_0D,             NO_OPERAND),
]


for op in edao_fa_op_list:
    edao_fa_op_table[op.OpCode] = op
    op.Container = edao_fa_op_table


class FieldAttackFileInfo:

    def __init__(self):
        self.HeaderSize     = 0
        self.ChipFile       = ChipFileIndex()
        self.EffectName     = ''
        self.CodeBlock      = None

    def open(self, buf):
        if type(buf) == str:
            buf = open(buf, 'rb').read()

        fs = fileio.FileStream(buf)

        self.HeaderSize = fs.ReadUShort()
        self.ChipFile   = ChipFileIndex(fs.ReadULong())
        self.EffectName = fs.ReadMultiByte()

        fs.seek(self.HeaderSize)

        self.CodeBlock = Disassembler(edao_fa_op_table).DisasmBlock(fs)

    def SaveToFile(self, filename):

        lines = []

        lines.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
        lines.append('')

        name = os.path.splitext(os.path.basename(filename))[0]
        name = os.path.splitext(name)[0]

        lines.append('CreateFieldAttack("%s", "%s", "%s")' % (name + '._bn', self.ChipFile.Name(), self.EffectName))
        lines.append('')

        LabelMap = { self.CodeBlock.Offset : '' }

        blocks = [Disassembler(edao_fa_op_table).FormatCodeBlock(self.CodeBlock, LabelMap)]
        for block in blocks:
            lines += block

        txt = '\r\n'.join(lines)

        lines = txt.replace('\r\n', '\n').replace('\r', '\n').split('\n')

        for i in range(2, len(lines)):
            if lines[i] != '':
                lines[i] = '    %s' % lines[i]

        lines.insert(2, 'def main():')
        lines.append('Try(main)')
        lines.append('')

        fs = open(filename, 'wb')
        fs.write(''.encode('utf_8_sig'))
        fs.write('\r\n'.join(lines).encode('UTF8'))


############################################################################################
# support functions
############################################################################################

fafile = None

def label(*args):
    pass

def CreateFieldAttack(FileName, ChipFile, EffectName):
    EffectName = EffectName.encode(CODE_PAGE) + b'\x00'

    global fafile

    fafile = fileio.FileStream(FileName, 'wb')
    hdrsize = 2 + 4 + len(EffectName)

    fafile.WriteUShort(hdrsize)
    fafile.WriteULong(ChipFileIndex(ChipFile).Index())
    fafile.Write(EffectName)


for op, inst in edao_fa_op_table.items():

    func = []
    func.append('def %s(*args):' % inst.OpName)
    func.append('    return OpCodeHandler(0x%02X, args)' % inst.OpCode)
    func.append('')

    exec('\r\n'.join(func))

    opx = 'FA_%02X' % inst.OpCode

    if inst.OpName != opx:
        func[0] = 'def %s(*args):' % opx
        exec('\r\n'.join(func))


def OpCodeHandler(op, args):
    entry = edao_fa_op_table[op]
    fs = fafile

    data = HandlerData(HANDLER_REASON_ASSEMBLE)
    data.Instruction    = Instruction(op)
    data.Arguments      = list(args)
    data.FileStream     = fs
    data.TableEntry     = entry

    data.Instruction.OperandFormat = entry.Operand

    data.FileStream = fileio.FileStream(b'')

    #print(entry.OpName)
    inst = OpCodeHandlerPrivate(data)

    data.FileStream.seek(0)
    fs.write(data.FileStream.read())

    return inst



if __name__ == '__main__':

    def procfile(file):
        print('disasm %s' % file)
        asdat = FieldAttackFileInfo()
        asdat.open(file)
        asdat.SaveToFile(file + '.py')

    def main():
        ForEachFile(sys.argv[1:], procfile, '*._bn')

    Try(main)

