from BaseType import *
from InstructionTable import *

def plog(*args):
    pass

#plog = print

offsetlist = {}
disasmtbl = {}
fuck = False

class Disassembler:
    def __init__(self, InstructionTable, DiasmInstructionCallback = None):
        self.InstructionTable = InstructionTable
        self.DiasmInstructionCallback = DiasmInstructionCallback
        self.DisasmTable = {}

    def DisasmBlock(self, Stream, InstructionTable = None):
        if InstructionTable == None:
            InstructionTable = self.InstructionTable

        DisasmTable = self.DisasmTable

        ret = self.DisasmBlockWorker(Stream, InstructionTable, DisasmTable)

        #for offset, inst in DisasmTable.items(): disasmtbl[offset] = inst

        return ret

    def DefaultDisasmInstruction(self, data):
        inst = data.Instruction
        fs = data.FileStream
        entry = data.TableEntry

        for opr in inst.OperandFormat:
            inst.Operand.append(entry.GetOperand(opr, fs))
            if opr.lower() == 'o':
                inst.BranchTargets.append(inst.Operand[-1])

        return inst

    def DisasmInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        inst.OperandFormat = entry.Operand

        handler = entry.Handler if entry.Handler != None else self.DefaultDisasmInstruction
        inst = handler(data)
        if inst == None:
            inst = self.DefaultDisasmInstruction(data)

        if self.DiasmInstructionCallback:
            self.DiasmInstructionCallback(inst, data.FileStream)

        return inst

    def DisasmBlockWorker(self, Stream, InstructionTable, DisasmTable):
        pos = Stream.tell()

        if pos in DisasmTable:
            inst = DisasmTable[pos]
            inst.RefCount += 1
            return None

        block = CodeBlock(pos)
        block.Name = InstructionTable.GetLabelName(pos)

        plog('block: %08X' % block.Offset)

        blockref = {}

        IsJumpTarget = False

        while True:
            pos = Stream.tell()
            #if pos in DisasmTable: break

            offsetlist[pos] = True

            print('%08X: ' % pos, end = '')
            op = InstructionTable.GetOpCode(Stream)
            print('%02X' % op)

            entry = InstructionTable[op]

            plog('    %08X: %s' % (pos, entry.OpName))

            data = HandlerData(HANDLER_REASON_DISASM)

            data.Instruction        = Instruction(op)
            data.Instruction.Flags  = entry.Flags
            data.Instruction.Offset = pos
            data.FileStream         = Stream
            data.TableEntry         = entry
            data.Disasm             = self.DisasmInstruction

            inst = self.DisasmInstruction(data)

            if IsJumpTarget:
                inst.RefCount += 1
                IsJumpTarget = False

            if inst == None:
                raise Exception('disasm op %02X @ %08X failed' % (op, pos))

            for i in range(pos, Stream.tell()): offsetlist[i] = True

            DisasmTable[inst.Offset] = inst
            block.AddInstruction(inst)

            targets = []

            if inst.Flags.EndBlock:
                if len(inst.BranchTargets) == 0:
                    break

                elif len(inst.BranchTargets) != 1:
                    raise Exception('end block instruction has multiple branch')

                #Stream.seek(inst.BranchTargets[0])
                #block.Instructions.pop()
                #IsJumpTarget = True
                #continue
                targets = inst.BranchTargets

            elif inst.Flags.StartBlock:
                targets = inst.BranchTargets

            if len(targets) == 0:
                continue

            inst.BranchTargets = []
            for offset in targets:
                blockref[offset] = inst

        plog('block end: %08X' % block.Offset)

        for offset, inst in blockref.items():
            Stream.seek(offset)
            newblock = self.DisasmBlockWorker(Stream, InstructionTable, DisasmTable)
            if newblock != None:
                newblock.Parent = block
                block.AddBlock(newblock)
                inst.BranchTargets.append(newblock)

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

        return '%s(%s)' % (opname, oprlist)

    def FormatInstruction(self, data):
        inst = data.Instruction
        entry = data.TableEntry

        handler = entry.Handler if entry.Handler != None else self.DefaultFormatInstruction
        inst = handler(data)
        if inst == None:
            inst = self.DefaultFormatInstruction(data)

        return inst

    def FormatCodeBlock(self, block, InstructionTable = None, LabeledMap = None):
        if InstructionTable == None:
            InstructionTable = self.InstructionTable

        if LabeledMap == None:
            LabeledMap = {}

        text = []

        def AddLabel(name):
            text.append('')
            text.append('label("%s")' % name)
            text.append('')

        if block.Offset not in LabeledMap:
            AddLabel(block.Name if block.Name != None else InstructionTable.GetLabelName(block.Offset))
            LabeledMap[block.Offset] = block.Name

        for inst in block.Instructions:

            data = HandlerData(HANDLER_REASON_FORMAT)

            data.Instruction    = inst
            data.TableEntry     = InstructionTable[inst.OpCode]
            data.Format         = self.FormatInstruction
            data.LabeledMap     = LabeledMap

            #print('%08X' % inst.Offset)
            #del disasmtbl[inst.Offset]

            #print('%08X %02X: ' % (inst.Offset, inst.OpCode), end  = '')
            symbol = self.FormatInstruction(data)
            #print(symbol)

            if inst.RefCount != 0:
                name = InstructionTable.GetLabelName(inst.Offset)
                if inst.Offset not in LabeledMap or name != LabeledMap[inst.Offset]:
                    AddLabel(name)

            text.append(symbol)

        text.append('')

        for subblock in block.CodeBlocks:
            text += self.FormatCodeBlock(subblock, InstructionTable)

        return text
