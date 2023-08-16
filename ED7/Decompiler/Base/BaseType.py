from ml import *

INVALID_OFFSET = 0xFFFFABCD

INSTRUCTION_END_BLOCK       = 1 << 0
INSTRUCTION_START_BLOCK     = 1 << 1
INSTRUCTION_CALL            = (1 << 2) | INSTRUCTION_START_BLOCK
INSTRUCTION_JUMP            = (1 << 3) | INSTRUCTION_END_BLOCK
INSTRUCTION_SWITCH          = 0

INSTRUCTION_FORMAT_ARG_NEW_LINE         = 1 << 4
INSTRUCTION_FORMAT_EMPTY_LINE           = 1 << 5

class InstructionFlags:
    def __init__(self, flags):
        self.Flags      = flags
        self.EndBlock   = bool(flags & INSTRUCTION_END_BLOCK)
        self.StartBlock = bool(flags & INSTRUCTION_START_BLOCK)
        self.Call       = bool(flags & INSTRUCTION_CALL & ~INSTRUCTION_START_BLOCK)
        self.Jump       = bool(flags & INSTRUCTION_JUMP & ~INSTRUCTION_END_BLOCK)
        self.ArgNewLine = bool(flags & INSTRUCTION_FORMAT_ARG_NEW_LINE)

class InstructionOperand:
    def __init__(self, operand, size):
        self.Operand = operand
        self.Size = size

class LabelEntry:
    def __init__(self, label, offset):
        self.Label = label          # label name
        self.Offset = offset        # label offset in instruction

class Instruction:
    def __init__(self, op = None, operand = None, flags = 0):
        self.OpCode             = op
        self.Operand            = operand if operand != None else []
        self.OperandFormat      = None
        self.BranchTargets      = []
        self.Flags              = InstructionFlags(flags)
        self.RefCount           = 0
        self.Offset             = -1
        self.Size               = 0
        self.BytesStream        = None
        self.Labels             = []        # list of LabelEntry(name, offset_in_self)

class CodeBlock:
    def __init__(self, Offset = -1):
        self.Offset = Offset
        self.Instructions = []
        self.Parent = None
        self.CodeBlocks = []
        self.Name = None

    def AddBlock(self, block):
        self.CodeBlocks.append(block)

    def AddInstruction(self, instruction):
        self.Instructions.append(instruction)


def IsTupleOrList(val):
    return isinstance(val, (list, tuple))

def strlen(string):
    n = 0
    for ch in string:
        if ch > '\x80':
            n += 1

    return n + len(string)

def ljust_cn(string, n):
    cncount = 0
    for ch in string:
        if ch > '\x80':
            cncount += 1

    return string.ljust(n - cncount)

def rjust_cn(string, n):
    cncount = 0
    for ch in string:
        if ch > '\x80':
            cncount += 1

    return string.rjust(n - cncount)

def AdjustParam(param, spacelist, sep = ', '):
    param = param.split(sep)
    for i in range(len(param) - 1):
        param[i] = ljust_cn(param[i] + sep, int(spacelist[i]))

    return ''.join(param)

def alignFormatArg(align, fmt, *params):
    if params:
        fmt = fmt % (params)

    return ljust_cn(fmt + ',', align)

def alignFormatKw(align, fmt, *params):
    if params:
        fmt = fmt % (params)

    return ljust_cn(fmt, align) + '='

def GetValidLabelName(name):
    filter = \
    [
        (' ', ''),
        ('-', ''),
        #('_', ''),
        ('　', ''),
        ('·', ''),
        ('＋', '_Plus'),
        ('％', ''),
        ('⑿', '12'),
        ('『', '_'),
        ('』', ''),
        ('「', '_'),
        ('」', ''),
        ('！', ''),

        ('①', '1'),
        ('②', '2'),
        ('③', '3'),
        ('④', '4'),
        ('⑤', '5'),
        ('⑥', '6'),
        ('⑦', '7'),
        ('⑧', '8'),
        ('⑨', '9'),
        ('⑩', '10'),
        ('⑾', '11'),
    ]

    for f in filter:
        name = name.replace(f[0], f[1])

    return name

def CombineMultiline(text):
    if len(text) == 1:
        return text[0]

    text2 = []
    for line in text:
        text2.append(line.strip())

    text2 = ' '.join(text2)
    return text2