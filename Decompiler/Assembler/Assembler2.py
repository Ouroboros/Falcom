from Base.BaseType import *
from Assembler.InstructionTable import *

def plog(*args):
    pass

#plog = print

offsetlist = {}
disasmtbl = {}
fuck = False

class Disassembler:

    class DisasmData:
        Stream              = None
        StreamSize          = None
        DisasmTable         = None
        Block               = None
        InstructionTable    = None
        GlobalLabelTable    = None
        EndOffset           = INVALID_OFFSET

        def Duplicate(self):
            data = Disassembler.DisasmData()

            data.DisasmTable        = self.DisasmTable
            data.Block              = self.Block
            data.InstructionTable   = self.InstructionTable
            data.GlobalLabelTable   = self.GlobalLabelTable
            data.EndOffset          = self.EndOffset
            return data


    def __init__(self, InstructionTable = None, HandleInstructionCallback = None):
        self.InstructionTable           = InstructionTable
        self.HandleInstructionCallback  = HandleInstructionCallback
        self.DisasmTable                = {}
        self.GlobalLabelTable           = {}
        self.LabelMap                   = {}
        self.FormattedBlock             = {}

    def DisasmBlock(self, Stream, InstructionTable = None, DisasmTable = None, GlobalLabelTable = None):

        data = self.DisasmData()

        data.Stream             = Stream
        data.InstructionTable   = InstructionTable if InstructionTable != None else self.InstructionTable
        data.DisasmTable        = DisasmTable if DisasmTable != None else {}
        data.GlobalLabelTable   = GlobalLabelTable if GlobalLabelTable != None else self.GlobalLabelTable
        data.Block              = CodeBlock(Stream.tell())

        ret = self.DisasmBlockWorker(data)

        #for offset, inst in DisasmTable.items(): disasmtbl[offset] = inst

        return data.Block

    def DisasmBlock2(self, disasmdata):

        data = disasmdata

        if data.InstructionTable == None:
            data.InstructionTable = self.InstructionTable

        if data.DisasmTable == None:
            data.DisasmTable = {}

        if data.GlobalLabelTable == None:
            data.GlobalLabelTable = self.GlobalLabelTable

        data.Block = CodeBlock(data.Stream.tell())

        self.DisasmBlockWorker(disasmdata)

        return disasmdata.Block

    def DefaultDisasmInstruction(self, data):
        inst = data.Instruction
        fs = data.FileStream
        entry = data.TableEntry

        for opr in inst.OperandFormat:
            inst.Operand.append(entry.GetOperand(opr, fs))
            if opr.lower() == 'o':
                inst.BranchTargets.append(inst.Operand[-1])

        return inst

    def DisasmBlockWorker(self, data):

        #InstructionTable    = data.InstructionTable
        Stream              = data.Stream
        StreamSize          = data.StreamSize
        DisasmTable         = data.DisasmTable
        GlobalLabelTable    = data.GlobalLabelTable

        block = data.Block

        pos = Stream.tell()

        if pos in DisasmTable:
            DisasmTable[pos].RefCount += 1
            return None

        plog('block: %08X' % block.Offset)

        blockref = {}


        def DisasmBlockExport(offset, size):

            pos = Stream.tell()

            data2 = data.Duplicate()
            data2.Stream = Stream
            data2.StreamSize = size
            data2.Block = CodeBlock(offset)

            Stream.seek(offset)

            block = self.DisasmBlockWorker(data2)

            Stream.seek(pos)

            return block


        def DisasmInstruction(data):
            fs = data.FileStream
            InstructionTable = data.InstructionTable

            pos = fs.tell()

            # print('%08X: ' % pos, end = '')
            op = InstructionTable.GetOpCode(fs)
            # print('%02X' % op)

            entry = InstructionTable[op]

            plog('    %08X: %s' % (pos, entry.OpName))

            data.Instruction        = Instruction(op)
            data.Instruction.Flags  = entry.Flags
            data.Instruction.Offset = pos
            data.TableEntry         = entry
            data.Disasm             = DisasmInstruction
            data.DisasmBlock        = DisasmBlockExport

            data.Instruction.OperandFormat = entry.Operand

            handler = entry.Handler if entry.Handler != None else self.DefaultDisasmInstruction
            inst = handler(data)
            if inst == None:
                inst = self.DefaultDisasmInstruction(data)

            if inst == None:
                raise Exception('disasm op %02X @ %08X failed' % (op, pos))

            inst.Size = fs.tell() - pos
            DisasmTable[inst.Offset] = inst

            if self.HandleInstructionCallback:
                self.HandleInstructionCallback(data)

            return inst

        endofblock = Stream.Length if StreamSize == None else (pos + StreamSize)

        while True:
            pos = Stream.tell()
            if pos in DisasmTable: break
            if pos >= endofblock: break

            #offsetlist[pos] = True

            handlerdata                     = HandlerData(HANDLER_REASON_DISASM)
            handlerdata.FileStream          = Stream
            handlerdata.InstructionTable    = data.InstructionTable

            inst = DisasmInstruction(handlerdata)

            #for i in range(pos, Stream.tell()): offsetlist[i] = True

            block.AddInstruction(inst)

            if not inst.Flags.EndBlock and not inst.Flags.StartBlock:
                continue

            targets = inst.BranchTargets
            inst.BranchTargets = []

            for offset in targets:
                blockref[offset] = inst

            if inst.Flags.EndBlock:
                break

        plog('block end: %08X' % block.Offset)

        for offset in sorted(blockref):
            inst = blockref[offset]

            Stream.seek(offset)

            newdata = data.Duplicate()
            newdata.Stream = Stream

            newblock = self.DisasmBlock2(newdata)
            if newblock == None or len(newblock.Instructions) == 0:
                continue

            GlobalLabelTable[newblock.Instructions[0].Offset] = True

            newblock.Instructions[0].RefCount += 1

            if offset >= block.Instructions[-1].Offset or offset < block.Instructions[0].Offset:
                block.Instructions += newblock.Instructions
            else:
                for i in range(len(block.Instructions)):
                    if offset >= block.Instructions[i].Offset:
                        continue

                    block.Instructions = block.Instructions[:i] + newblock.Instructions + block.Instructions[i:]
                    break

        return block

    def DefaultFormatInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        opname = entry.OpName
        oprlist = entry.FormatAllOperand(
                        BuildFormatOperandParameterList(
                            inst.OperandFormat,
                            inst.Operand,
                            inst.Flags,
                            data.LabelMap
                        )
                    )

        return ['%s(%s)' % (opname, oprlist)]

    class FormatData:
        Block               = None
        LabelMap            = None
        FormattedBlock      = None
        InstructionTable    = None
        GlobalLabelTable    = None

        def Duplicate(self):

            data = FormatData()

            data.LabelMap           = self.LabelMap
            data.FormattedBlock     = self.FormattedBlock
            data.InstructionTable   = self.InstructionTable
            data.GlobalLabelTable   = self.GlobalLabelTable

    def FormatCodeBlock(self, block, LabelMap = None, FormattedBlock = None, InstructionTable = None, GlobalLabelTable = None):

        data = self.FormatData()

        data.Block              = block
        data.LabelMap           = LabelMap if LabelMap != None else self.LabelMap
        data.FormattedBlock     = FormattedBlock if FormattedBlock != None else self.FormattedBlock
        data.InstructionTable   = InstructionTable if InstructionTable != None else self.InstructionTable
        data.GlobalLabelTable   = GlobalLabelTable if GlobalLabelTable != None else self.GlobalLabelTable

        return self.FormatCodeBlockWorker(data)

    def FormatCodeBlock2(self, formatdata):

        data = formatdata

        if data.LabelMap == None:
            data.LabelMap = self.LabelMap

        if data.FormattedBlock == None:
            data.FormattedBlock = self.FormattedBlock

        if data.InstructionTable == None:
            data.InstructionTable = self.InstructionTable

        if data.GlobalLabelTable == None:
            data.GlobalLabelTable = self.GlobalLabelTable

        return self.FormatCodeBlockWorker(data)

    def FormatInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        handler = entry.Handler if entry.Handler != None else self.DefaultFormatInstruction
        text = handler(data)
        if text == None:
            text = self.DefaultFormatInstruction(data)

        if self.HandleInstructionCallback:
            symbol = self.HandleInstructionCallback(data)
            text = symbol if symbol else text

        return text

    def FormatCodeBlockWorker(self, data):
        InstructionTable    = data.InstructionTable
        GlobalLabelTable    = data.GlobalLabelTable
        LabelMap            = data.LabelMap
        FormattedBlock      = data.FormattedBlock
        block               = data.Block

        if block.Offset in FormattedBlock:
            return []

        FormattedBlock[block.Offset] = True

        text = []

        def AddLabel(name, list):
            list.append('')
            list.append('label("%s")' % name)
            list.append('')

        def EndLabel(name, list):
            list.append('')
            list.append('# %s end' % name)

        blockname = None
        if block.Offset not in LabelMap:
            blockname = block.Name if block.Name != None else InstructionTable.GetLabelName(block.Offset)
            AddLabel(blockname, text)
            LabelMap[block.Offset] = block.Name

        def FormatInstructionWrap(data):
            inst = data.Instruction

            FormattedBlock[inst.Offset] = True

            text = []
            if inst.RefCount != 0 or inst.Offset in GlobalLabelTable:
                name = InstructionTable.GetLabelName(inst.Offset)
                if inst.Offset not in LabelMap:
                    AddLabel(name, text)
                    LabelMap[inst.Offset] = name

            text += self.FormatInstruction(data)

            return text

        def FormatInstructionWrapExport(data):
            data.TableEntry = InstructionTable[data.Instruction.OpCode]
            return FormatInstructionWrap(data)


        for inst in block.Instructions:
            if inst.Offset != block.Offset and inst.Offset in FormattedBlock:
                continue

            handlerdata = HandlerData(HANDLER_REASON_FORMAT)

            handlerdata.Instruction     = inst
            handlerdata.TableEntry      = InstructionTable[inst.OpCode]
            handlerdata.LabelMap        = LabelMap
            handlerdata.Format          = FormatInstructionWrapExport

            #print('%08X' % inst.Offset)
            #del disasmtbl[inst.Offset]

            #print('%08X %02X: ' % (inst.Offset, inst.OpCode), end  = '')
            symbol = FormatInstructionWrap(handlerdata)
            #print(symbol)

            text += symbol

        if blockname != None:
            EndLabel(blockname, text)

        text.append('')

        for subblock in block.CodeBlocks:
            newdata = data.Duplicate()
            newdata.Block = subblock
            text += self.FormatCodeBlock2(newdata)

        return text
