from Assembler.Assembler2 import *
from Base.EDAOBase import *
import Instruction.ActionOpTableEDAO as edao
import BattleMonsterStatus as MSFile

INVALID_ACTION_OFFSET = 0xFFFF
EMPTY_ACTION    = INVALID_ACTION_OFFSET

class CharacterPositionFactor:

    def __init__(self, fs = None):
        if fs == None:
            return

        self.X = fs.ReadByte()
        self.Y = fs.ReadByte()

class BattleActionScriptInfo:

    ActionFileType_Normal   = 0
    ActionFileType_Arts     = 1
    ActionFileType_Item     = 2

    def __init__(self):
        self.ActionListOffset       = 0
        self.ChrPosFactorOffset     = 0
        self.Reserve                = 0
        self.PreloadChipList        = []
        self.ModelXFile             = ''
        self.ActionList             = []

        self.ChrPosFactor = []
        self.CraftActions = []

        self.GlobalLabelTable = {}

        self.ChrName = None
        self.ASFileName = ''

        self.ActionFileType = self.ActionFileType_Normal

    def open(self, asname):
        fs = fileio.FileStream()
        fs.Open(asname)

        self.ASFileName = asname

        asname = os.path.basename(asname).lower()

        if asname == 'as90000.dat':
            self.ActionFileType = self.ActionFileType_Arts
        elif asname == 'as90001.dat':
            self.ActionFileType = self.ActionFileType_Item
        else:
            self.ActionFileType = self.ActionFileType_Normal


        self.ActionListOffset   = fs.ReadUShort()

        if self.ActionFileType == self.ActionFileType_Normal:
            self.ChrPosFactorOffset = fs.ReadUShort()
            self.Reserve            = fs.ReadUShort()

            while True:
                index = fs.ReadULong()
                if index == 0xFFFFFFFF:
                    break

                self.PreloadChipList.append(ChipFileIndex(index))

            fs.seek(self.ChrPosFactorOffset)
            for i in range(8):
                self.ChrPosFactor.append(CharacterPositionFactor(fs))

        minoffset = 0xFFFFFFFF

        fs.seek(self.ActionListOffset)
        while True:
            if fs.tell() >= minoffset:
                break

            offset = fs.ReadUShort()
            if offset == 0:
                break

            minoffset = min(minoffset, offset)

            self.ActionList.append(offset)

        if len(self.ActionList) == 0:
            raise Exception('action number == 0')

        self.CraftActions = self.DisassembleCraftActions(fs)

        return

        for i in range(0x69, fs.Length):
            if i not in offsetlist:
                print('%X' % i)
                #input()

        input()

    def GetBuiltinNames(self):

        if self.ActionFileType == self.ActionFileType_Arts:

            BuiltinArtsNames = []

            try:
                offsetlist = []
                t_magic = os.path.abspath(os.path.dirname(os.path.abspath(self.ASFileName)) + '\\..\\..\\text\\t_magic._dt')
                if not os.path.exists(t_magic):
                    if t_magic.endswith('\\patch\\text\\t_magic._dt'):
                        t_magic = t_magic.replace('\\patch\\text\\t_magic._dt', '\\data\\text\\t_magic._dt')
                    elif t_magic.endswith('\\patch2\\text\\t_magic._dt'):
                        t_magic = t_magic.replace('\\patch2\\text\\t_magic._dt', '\\data\\text\\t_magic._dt')

                magic = fileio.FileStream()
                magic.Open(t_magic)
                for i in range(len(self.ActionList)):
                    offsetlist.append(magic.ReadUShort())
                    BuiltinArtsNames.append('')

                NameConflict = {}

                for i in range(len(offsetlist)):
                    offset = offsetlist[i]

                    if i != len(offsetlist) - 1 and offsetlist[i + 1] - offset < 0x1C:
                        continue

                    #print('%X' % offset)

                    magic.seek(offset + 0x18)

                    offset = magic.ReadUShort()
                    if offset == 0:
                        continue

                    magic.seek(offset)
                    name = magic.ReadMultiByte().replace(' ', '')

                    if name == '':
                        continue

                    if name not in NameConflict:
                        NameConflict[name] = 1
                    else:
                        NameConflict[name] += 1
                        name += '_%d' % NameConflict[name]

                    BuiltinArtsNames[i] = name
            except:
                BuiltinArtsNames = []


            return BuiltinArtsNames

        elif self.ActionFileType == self.ActionFileType_Normal:
            BuiltinCraftNames = \
            [
                'SysCraft_Init',                # 00 0
                'SysCraft_Stand',               # 01 1
                'SysCraft_Move',                # 02 2
                'SysCraft_UnderAttack',         # 03 3
                'SysCraft_Dead',                # 04 4
                'SysCraft_NormalAttack',        # 05 5
                'SysCraft_ArtsAria',            # 06 6
                'SysCraft_ArtsCast',            # 07 7
                'SysCraft_Win',                 # 08 8
                'SysCraft_EnterBattle',         # 09 9
                'SysCraft_UseItem',             # 0A 10
                'SysCraft_Stun',                # 0B 11
                'SysCraft_Unknown2',            # 0C 12
                'SysCraft_Reserve1',            # 0D 13
                'SysCraft_Reserve2',            # 0E 14
                'SysCraft_Counter',             # 0F 15

                '',                             # 10 16
                '',                             # 11 17
                '',                             # 12 18
                '',                             # 13 19
                '',                             # 14 20
                '',                             # 15 21
                '',                             # 16 22
                '',                             # 17 23
                '',                             # 18 24
                '',                             # 19 25
                '',                             # 1A 26
                '',                             # 1B 27
                '',                             # 1C 28
                '',                             # 1D 29

                'SysCraft_TeamRushInit',        # 1E 30
                'SysCraft_TeamRushAction',      # 1F 31
            ]

            return BuiltinCraftNames

        return []

    def DiasmInstructionCallback(self, data):
        return

    def DisassembleCraftActions(self, fs):

        CraftNameMap = {}

        msfile = None
        try:
            msfile = MSFile.BattleMonsterStatus()
            msfile.open(os.path.dirname(self.ASFileName) + '\\ms' + os.path.basename(self.ASFileName)[2:])
            self.ChrName = None if msfile.Name == '' or msfile.Name == ' ' else msfile.Name
        except:
            msfile = None

        BuiltinCraftNames = self.GetBuiltinNames()

        disasm = Disassembler(edao.edao_as_op_table, self.DiasmInstructionCallback)

        index = -1
        codeblocks = []
        blockoffsetmap = {}
        for func in self.ActionList:
            index += 1
            if func == INVALID_ACTION_OFFSET:
                codeblocks.append(CodeBlock(INVALID_ACTION_OFFSET))
                continue

            if func in blockoffsetmap:
                codeblocks.append(blockoffsetmap[func])
                continue

            fs.seek(func)

            data = Disassembler.DisasmData()
            data.Stream = fs
            data.GlobalLabelTable = self.GlobalLabelTable

            block = disasm.DisasmBlock2(data)

            if index >= len(BuiltinCraftNames) or BuiltinCraftNames[index] == '':
                name = 'Craft_%X_%d_%X' % (index, index, block.Offset)
                if msfile != None:
                    craft = msfile.FindCraftByActionIndex(index)
                    if craft != None:
                        if craft.Name != '' and craft.Name != ' ':
                            name += '_' + craft.Name.replace(' ', '_').replace('　', '_').replace('·', '')

                block.Name = name

            else:
                block.Name = BuiltinCraftNames[index]

            codeblocks.append(block)

            blockoffsetmap[func] = block

        return codeblocks

    def FormatCodeBlocks(self):
        disasm = Disassembler(edao.edao_as_op_table)

        blocks = []
        blockoffsetmap = {}
        for block in self.CraftActions:
            if block.Offset == INVALID_ACTION_OFFSET:
                continue

            if block.Offset in blockoffsetmap:
                continue

            blockoffsetmap[block.Offset] = True

            data = Disassembler.FormatData()

            data.Block = block
            data.GlobalLabelTable   = self.GlobalLabelTable

            name = GetValidLabelName(block.Name)
            if not name.startswith('Craft_'): name = 'Craft_' + name

            blocks.append(['def %s(): pass' % name])
            blocks.append(disasm.FormatCodeBlock2(data))

        #for x in disasmtbl: print('%08X' % x)
        #input()

        return blocks

    def SaveToFile(self, filename):
        lines = []

        #lines.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
        lines.append('from ActionHelper import *')
        lines.append('')

        name = os.path.splitext(os.path.basename(filename))[0]
        name = os.path.splitext(name)[0]

        if self.ActionFileType == self.ActionFileType_Arts:

            lines.append('CreateArtsAction("%s")' % (name + '.dat'))

        else:

            tmp = []
            for pos in self.ChrPosFactor:
                tmp.append('(%d, %d)' % (pos.X, pos.Y))

            lines.append('CreateBattleAction("%s", (%s))' % (name + '.dat', ', '.join(tmp)))
            lines.append('')
            lines.append('AddPreloadChip((')

            index = 0
            for chip in self.PreloadChipList:
                x = ljust_cn('    "%s",' % chip.Name(), 30)
                x += ' # %02X %d' % (index, index)
                lines.append(x)
                index += 1

            lines.append('))')

        lines.append('')

        lines.append('CraftAction((')
        index = 0
        for craft in self.CraftActions:
            name = ('"%s"'% craft.Name) if craft.Offset != INVALID_ACTION_OFFSET else 'EMPTY_ACTION'
            lines.append( ljust_cn('    %s,' % name, 40) + ('# %02X %d' % (index, index)))
            index += 1

        lines.append('))')
        lines.append('')


        blocks = self.FormatCodeBlocks()

        for block in blocks:
            lines += block

        lines.append('SaveToFile()')
        lines.append('')

        txt = '\r\n'.join(lines)

        lines = txt.replace('\r\n', '\n').replace('\r', '\n').split('\n')

        for i in range(2, len(lines)):
            if lines[i] != '':
                lines[i] = '    %s' % lines[i]

        lines.insert(2, 'def main():')
        lines.append('Try(main)')
        lines.append('')

        if self.ChrName != None:
            lines.insert(2, '# %s' % self.ChrName)
            lines.insert(3, '')

        fs = open(filename, 'wb')
        fs.write(''.encode('utf_8_sig'))
        fs.write('\r\n'.join(lines).encode('UTF8'))


############################################################################################
# support functions
############################################################################################

class BattleActionScriptInfoPort(BattleActionScriptInfo):
    def __init__(self):
        super().__init__()

        self.FileName = ''
        self.Labels             = {}    # map<name, offset>
        self.DelayFixLabels     = []    # list of LabelEntry
        self.PrevousHandlerData = None
        self.fs                 = None

actionfile = None

def label(labelname):
    pos = actionfile.fs.tell()
    if actionfile.PrevousHandlerData is not None:
        pos += actionfile.PrevousHandlerData.FileStream.tell()

    plog('%08X: %s' % (pos, labelname))
    if labelname in actionfile.Labels and actionfile.Labels[labelname] != pos:
        raise Exception('label name conflict: %s' % labelname)

    actionfile.Labels[labelname] = pos

def getlabel(name):
    return actionfile.Labels[name]

def CreateBattleAction(filename, ChrPosFactorList = None):

    if not IsTupleOrList(ChrPosFactorList):
        raise Exception('ChrPosFactorList must be list')

    global actionfile
    actionfile = BattleActionScriptInfoPort()

    actionfile.fs = fileio.FileStream()
    actionfile.fs.Open(filename, 'wb+')

    actionfile.FileName = filename
    for factor in ChrPosFactorList:
        f = CharacterPositionFactor()
        f.X = factor[0]
        f.Y = factor[1]
        actionfile.ChrPosFactor.append(f)


def CreateArtsAction(filename):

    global actionfile
    actionfile = BattleActionScriptInfoPort()

    actionfile.fs = fileio.FileStream()
    actionfile.fs.Open(filename, 'wb+')

    actionfile.ActionFileType = BattleActionScriptInfoPort.ActionFileType_Arts

    actionfile.ActionListOffset = 2
    actionfile.fs.WriteUShort(actionfile.ActionListOffset)


def AddPreloadChip(ChipFileList):

    if not IsTupleOrList(ChipFileList):
        raise Exception('ChipFileList must be list')

    fs = actionfile.fs
    fs.seek(6)

    for chip in ChipFileList:
        fs.WriteULong(ChipFileIndex(chip).Index())

    fs.WriteULong(0xFFFFFFFF)
    fs.WriteUShort(0)

    actionfile.ChrPosFactorOffset = fs.tell()
    for factor in actionfile.ChrPosFactor:
        fs.WriteByte(factor.X)
        fs.WriteByte(factor.Y)

    actionfile.ActionListOffset = fs.tell()
    actionfile.ActionListOffset += 16 - actionfile.ActionListOffset % 16

    fs.seek(0)
    fs.WriteUShort(actionfile.ActionListOffset)
    fs.WriteUShort(actionfile.ChrPosFactorOffset)
    fs.seek(actionfile.ActionListOffset)

def CraftAction(CraftNameList):

    if not IsTupleOrList(CraftNameList):
        raise Exception('CraftNameList must be list')

    fs = actionfile.fs
    fs.seek(actionfile.ActionListOffset)

    actionfile.ActionList = list(CraftNameList)

    for craft in CraftNameList:
        if craft != INVALID_ACTION_OFFSET:
            actionfile.DelayFixLabels.append(LabelEntry(craft, fs.tell()))

        fs.WriteUShort(INVALID_ACTION_OFFSET)

    fs.write(b'\x00' * (16 - len(CraftNameList) * 2 % 16))


for op, inst in edao.edao_as_op_table.items():

    func = []
    func.append('def %s(*args):' % inst.OpName)
    func.append('    return OpCodeHandler(0x%02X, args)' % inst.OpCode)
    func.append('')

    exec('\r\n'.join(func))

    opx = 'AS_%02X' % inst.OpCode

    if inst.OpName != opx:
        func[0] = 'def %s(*args):' % opx
        exec('\r\n'.join(func))

def AssembleForExec(expr):
    return eval(expr)

def OpCodeHandler(op, args):
    entry = edao.edao_as_op_table[op]

    data = HandlerData(HANDLER_REASON_ASSEMBLE)
    data.Instruction    = Instruction(op)
    data.Arguments      = list(args)
    data.TableEntry     = entry
    data.Assemble       = AssembleForExec

    data.Instruction.OperandFormat = entry.Operand

    UsePrevous = bool(actionfile.PrevousHandlerData != None)

    if UsePrevous:
        data.FileStream = actionfile.PrevousHandlerData.FileStream
        data.Instruction.Labels = actionfile.PrevousHandlerData.Instruction.Labels
    else:
        data.FileStream = fileio.FileStream(b'')
        actionfile.PrevousHandlerData = data

    #print(entry.OpName)
    inst = OpCodeHandlerPrivate(data)

    if UsePrevous:
        return inst

    actionfile.PrevousHandlerData = None

    offset = actionfile.fs.tell()
    for lb in inst.Labels:
        actionfile.DelayFixLabels.append(LabelEntry(lb.Label, lb.Offset + offset))

    data.FileStream.seek(0)
    actionfile.fs.write(data.FileStream.read())

    return inst

def SaveToFile():
    fs = actionfile.fs

    for lb in actionfile.DelayFixLabels:
        fs.seek(lb.Offset)
        fs.WriteUShort(getlabel(lb.Label))




'''

if has_target: jump label
Jc(0x16, 0x1, 0x0, "loc_A4A")




'''

def procfile(file):
    console.setTitle(os.path.basename(file))
    print('disasm %s' % file)
    asdat = BattleActionScriptInfo()
    asdat.open(file)
    asdat.SaveToFile(file + '.py')

if __name__ == '__main__':
    iterlib.forEachFileMP(procfile, sys.argv[1:], 'as*.dat')
