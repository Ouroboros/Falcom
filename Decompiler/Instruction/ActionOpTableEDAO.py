from Assembler.InstructionTable import *
from Base.EDAOBase import *

def GetOpCode(fs):
    return fs.ReadByte()

def WriteOpCode(fs, op):
    return fs.WriteByte(op)

edao_as_op_table = InstructionTable(GetOpCode, WriteOpCode, DefaultGetLabelName, CODE_PAGE)

InstructionNames = {}

InstructionNames[0x00] = 'Return'
InstructionNames[0x01] = 'Jump'
InstructionNames[0x02] = 'SetChrSubChip'
InstructionNames[0x03] = 'AS_03'
InstructionNames[0x04] = 'AS_04'
InstructionNames[0x05] = 'AS_05'
InstructionNames[0x06] = 'Sleep'
InstructionNames[0x07] = 'Yield'
InstructionNames[0x08] = 'ChrSetPos'
InstructionNames[0x09] = 'AS_09'
InstructionNames[0x0A] = 'AS_0A'
InstructionNames[0x0B] = 'AS_0B'
InstructionNames[0x0C] = 'TurnDirection'
InstructionNames[0x0D] = 'ChrJump'
InstructionNames[0x0E] = 'SetTeamRushState'
InstructionNames[0x0F] = 'ChrJumpToMonster'
InstructionNames[0x10] = 'ChrJumpBack'
InstructionNames[0x11] = 'ChrMove'
InstructionNames[0x12] = 'LoadEffect'
InstructionNames[0x13] = 'FreeEffect'
InstructionNames[0x14] = 'AS_14'
InstructionNames[0x15] = 'WaitEffect'
InstructionNames[0x16] = 'StopEffect'
InstructionNames[0x17] = 'CancelEffect'
InstructionNames[0x18] = 'PlayEffect'
InstructionNames[0x19] = 'Play3DEffect'
InstructionNames[0x1A] = 'AS_1A'
InstructionNames[0x1B] = 'SetChrChip'
InstructionNames[0x1C] = 'DamageCue'
InstructionNames[0x1D] = 'DamageAnime'
InstructionNames[0x1E] = 'AS_1E'
InstructionNames[0x1F] = 'AS_1F'
InstructionNames[0x20] = 'ChrTurnAndMove'
InstructionNames[0x21] = 'AS_21'
InstructionNames[0x22] = 'BeginChrThread'
InstructionNames[0x23] = 'WaitChrThread'
InstructionNames[0x24] = 'SetChipModeFlags'
InstructionNames[0x25] = 'ClearChipModeFlags'
InstructionNames[0x26] = 'SetMSDataState'
InstructionNames[0x27] = 'ClearMSDataState'
InstructionNames[0x28] = 'Say'
InstructionNames[0x29] = 'AS_29'
InstructionNames[0x2A] = 'ShowInfoText'
InstructionNames[0x2B] = 'AS_2B'
InstructionNames[0x2C] = 'ShowChrTrails'
InstructionNames[0x2D] = 'HideChrTrails'
InstructionNames[0x2E] = 'ShakeChr'
InstructionNames[0x2F] = 'EndChrThread'
InstructionNames[0x31] = 'AS_31'
InstructionNames[0x32] = 'AS_32'
InstructionNames[0x33] = 'AS_33'
InstructionNames[0x34] = 'AS_34'
InstructionNames[0x35] = 'LockCamera'
InstructionNames[0x36] = 'AS_36'
InstructionNames[0x39] = 'SetCameraDegree'
InstructionNames[0x3A] = 'AS_3A'
InstructionNames[0x3B] = 'SetCameraDistance'
InstructionNames[0x3C] = 'AS_3C'
InstructionNames[0x3D] = 'ShakeScreen'
InstructionNames[0x3E] = 'AS_3E'
InstructionNames[0x3F] = 'AS_3F'
InstructionNames[0x40] = 'AS_40'
InstructionNames[0x43] = 'AS_43'
InstructionNames[0x44] = 'Fade'
InstructionNames[0x45] = 'AS_45'
InstructionNames[0x46] = 'AS_46'
InstructionNames[0x47] = 'AS_47'
InstructionNames[0x48] = 'AS_48'
InstructionNames[0x49] = 'SetControl'
InstructionNames[0x4A] = 'AS_4A'
InstructionNames[0x4B] = 'Jc'
InstructionNames[0x4C] = 'ForeachTarget'
InstructionNames[0x4D] = 'ResetTarget'
InstructionNames[0x4E] = 'NextTarget'
InstructionNames[0x4F] = 'AS_4F'
InstructionNames[0x50] = 'Call'
InstructionNames[0x51] = 'CallReturn'
InstructionNames[0x52] = 'AS_52'
InstructionNames[0x53] = 'AS_53'
InstructionNames[0x54] = 'SendMessage'
InstructionNames[0x55] = 'ArtsUsing'
InstructionNames[0x56] = 'ArtsEnd'
InstructionNames[0x57] = 'AS_57'
InstructionNames[0x58] = 'Knockback'
InstructionNames[0x59] = 'AS_59'
InstructionNames[0x5A] = 'SetBrightness'
InstructionNames[0x5B] = 'ResetBrightness'
InstructionNames[0x5C] = 'ShowChr'
InstructionNames[0x5D] = 'HideChr'
InstructionNames[0x5E] = 'AS_5E'
InstructionNames[0x5F] = 'AS_5F'
InstructionNames[0x60] = 'AS_60'
InstructionNames[0x61] = 'SetBattleSpeed'
InstructionNames[0x62] = 'Voice'
InstructionNames[0x64] = 'Sound'
InstructionNames[0x65] = 'SoundEx'
InstructionNames[0x66] = 'StopSound'
InstructionNames[0x67] = 'AS_67'
InstructionNames[0x68] = 'AS_68'
InstructionNames[0x6A] = 'LoadChrChip'
InstructionNames[0x6B] = 'AS_6B'
InstructionNames[0x6C] = 'Dead'
InstructionNames[0x6D] = 'AS_6D'
InstructionNames[0x6E] = 'AS_6E'
InstructionNames[0x6F] = 'AS_6F'
InstructionNames[0x70] = 'AS_70'
InstructionNames[0x71] = 'AS_71'
InstructionNames[0x72] = 'AS_72'
InstructionNames[0x73] = 'AS_73'
InstructionNames[0x74] = 'AS_74'
InstructionNames[0x77] = 'AS_77'
InstructionNames[0x78] = 'AS_78'
InstructionNames[0x79] = 'AS_79'
InstructionNames[0x7A] = 'AS_7A'
InstructionNames[0x7B] = 'AS_7B'
InstructionNames[0x7C] = 'AS_7C'
InstructionNames[0x7D] = 'AS_7D'
InstructionNames[0x7E] = 'AS_7E'
InstructionNames[0x7F] = 'BlurSwitch'
InstructionNames[0x80] = 'CancelBlur'
InstructionNames[0x82] = 'AS_82'
InstructionNames[0x83] = 'SortTarget'
InstructionNames[0x84] = 'ChrRotate'
InstructionNames[0x85] = 'AS_85'
InstructionNames[0x87] = 'AS_87'
InstructionNames[0x89] = 'AS_89'
InstructionNames[0x8A] = 'ChrDuplicate'
InstructionNames[0x8B] = 'UseItemBegin'
InstructionNames[0x8C] = 'UseItemEnd'
InstructionNames[0x8D] = 'AS_8D'
InstructionNames[0x8E] = 'AS_8E'
InstructionNames[0x8F] = 'AS_8F'
InstructionNames[0x91] = 'AS_91'
InstructionNames[0x92] = 'ChrSetRelativePos'
InstructionNames[0x93] = 'AS_93'
InstructionNames[0x94] = 'AS_94'
InstructionNames[0x95] = 'ResetLookingTargetData'
InstructionNames[0x96] = 'LookingTargetAdd'
InstructionNames[0x97] = 'LookingTarget'
InstructionNames[0x98] = 'AS_98'
InstructionNames[0x99] = 'AS_99'
InstructionNames[0x9A] = 'AS_9A'
InstructionNames[0x9B] = 'AS_9B'
InstructionNames[0x9C] = 'AS_9C'
InstructionNames[0x9E] = 'AS_9E'
InstructionNames[0x9F] = 'AS_9F'
InstructionNames[0xA0] = 'AS_A0'
InstructionNames[0xA1] = 'PlayEffectIfConditionExist'
InstructionNames[0xA6] = 'AS_A6'
InstructionNames[0xA7] = 'AS_A7'
InstructionNames[0xA8] = 'AS_A8'
InstructionNames[0xA9] = 'SetEffectColor'
InstructionNames[0xAC] = 'AS_AC'
InstructionNames[0xAD] = 'AS_AD'
InstructionNames[0xAE] = 'QueueWorkItem'
InstructionNames[0xAF] = 'AS_AF'
InstructionNames[0xB0] = 'AS_B0'
InstructionNames[0xB1] = 'AS_B1'
InstructionNames[0xB2] = 'PlayBGM'
InstructionNames[0xB3] = 'SetScenarioFlags'
InstructionNames[0xB4] = 'SetChrCalcEnable'
InstructionNames[0xB5] = 'LoadCclm'
InstructionNames[0xB6] = 'UnlockCclm'
InstructionNames[0xB7] = 'AS_B7'
InstructionNames[0xB8] = 'AS_B8'

for op, name in InstructionNames.items():
    expr = '%s = 0x%08X' % (name, op)
    exec(expr)

class EDAOASOpTableEntry(InstructionTableEntry):
    def __init__(self, op, name = '', operand = NO_OPERAND, flags = 0, handler = None):
        super().__init__(op, name, operand, flags, handler)

    def GetOperand(self, opr, fs):
        val = super().GetOperand(opr, fs)
        if opr == 'S':
            val = val.replace('\\', '\\\\')
        return val

def inst(op, operand = NO_OPERAND, flags = 0, handler = None):
    return EDAOASOpTableEntry(op, InstructionNames[op], operand, flags, handler)


class ActionTarget:
    Self        = 0xFF
    Target      = 0xFE


def as_op_0c(data):
    def getopr(target):
        operand = 'HHB'
        if target == 0xFC:
            operand = 'WWW' + operand
        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        opr1, target = entry.GetAllOperand('BB', fs)

        inst.Operand = [opr1, target]

        operand = getopr(target)
        inst.Operand += entry.GetAllOperand(operand, fs)

        inst.OperandFormat = 'BB' + operand

        return inst

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        inst = data.Instruction
        target = data.Arguments[1]
        inst.OperandFormat = 'BB' + getopr(target)

def as_load_chr_chip(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        inst.Operand = entry.GetAllOperand('BLB', fs)
        inst.Operand[1] = ChipFileIndex(inst.Operand[1]).Name()

        inst.OperandFormat = 'BSB'

        return inst

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        inst = data.Instruction
        data.Arguments[1] = ChipFileIndex(data.Arguments[1]).Index()

        inst.OperandFormat = 'BLB'

def as_op_8e(data):

    def getopr(opr1, opr2):

        if opr1 == 1:
            operand = 'S'
        else:
            operand = 'LLLL'
            if opr1 == 0xD:
                operand += 'L'

        return operand

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        opr1, opr2 = entry.GetAllOperand('BB', fs)
        inst.Operand = [opr1, opr2]
        operand = getopr(opr1, opr2)
        inst.Operand += entry.GetAllOperand(operand, fs)

        inst.OperandFormat = 'BB' + operand

        return inst

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Instruction.OperandFormat = 'BB' + getopr(data.Arguments[0], data.Arguments[1])

def as_op_91(data):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        inst = data.Instruction
        entry = data.TableEntry

        opr = entry.GetOperand('B', fs)
        inst.Operand = [opr]

        if opr == 0:
            for i in range(0xA):
                inst.Operand.append(fs.ReadByte())
                if inst[-1] == 0xFF:
                    break

        inst.OperandFormat = 'B' * len(inst.Operand)

        return inst


def as_lambda_worker(data, extra_length):

    if data.Reason == HANDLER_REASON_DISASM:

        fs = data.FileStream
        ins = data.Instruction

        target, tid, length = data.TableEntry.GetAllOperand('BBB', fs)

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

        entry.WriteOperand(data, 'B', target)
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

def as_op_ae(data):

    return as_lambda_worker(data, 1)        # Return

def as_load_cclm(data):

    if data.Reason == HANDLER_REASON_DISASM:

        inst = data.Instruction
        entry = data.TableEntry

        inst.Operand = entry.GetAllOperand('LWBB', data.FileStream)
        inst.Operand[0] = BattleScriptFileIndex(inst.Operand[0]).Name()

        inst.OperandFormat = 'SWBB'

        return inst

    elif data.Reason == HANDLER_REASON_ASSEMBLE:

        data.Arguments[0] = BattleScriptFileIndex(data.Arguments[0]).Index()
        data.Instruction.OperandFormat = 'LWBB'

def as_unlock_cclm(data):

    return as_load_cclm(data)

edao_as_op_list = \
[
    inst(Return,                        NO_OPERAND,             INSTRUCTION_END_BLOCK),
    inst(Jump,                          'o',                    INSTRUCTION_JUMP),
    inst(SetChrSubChip,                 'BB'),
    inst(AS_03,                         'BW'),
    inst(AS_04,                         'BBh'),
    inst(AS_05,                         'BBL'),
    inst(Sleep,                         'H'),
    inst(Yield),
    inst(ChrSetPos,                     'BBiii'),           # ChrSetPos(target, src, x, z, y)
    inst(AS_09,                         'B'),
    inst(AS_0A,                         'BBBL'),
    inst(AS_0B,                         'WW'),
    inst(TurnDirection,                 NO_OPERAND,             0,                          as_op_0c),
    inst(ChrJump,                       'BBiiihh'),         # ChrJump(src, target, X, Z, Y, height, speed)
    inst(SetTeamRushState,              'B'),
    inst(ChrJumpToMonster,              'HH'),              # ChrJumpToMonster(hight, speed)
    inst(ChrJumpBack,                   'HH'),
    inst(ChrMove,                       'BBiiiiB'),         # ChrMove(chr, target, x, y, z, time, 0)
    inst(LoadEffect,                    'BS'),              # LoadEffect(effId, effPath[:10])
    inst(FreeEffect,                    'B'),
    inst(AS_14,                         'B'),
    inst(WaitEffect,                    'BB'),
    inst(StopEffect,                    'BB'),
    inst(CancelEffect,                  'BB'),
    inst(PlayEffect,                    'BBBBiiihhhhhhc'),      # PlayEffect(eff_owner, pos, eff_index, flag, x, z, y, degree_vert, degree_horz, unknown, size_x, size_z, size_y, eff_handle)
    inst(Play3DEffect,                  'BBSBBiiihhhhhhc'),
    inst(AS_1A,                         'BBW'),
    inst(SetChrChip,                    'BB'),
    inst(DamageCue,                     'B'),
    inst(DamageAnime,                   'BBB'),
    inst(AS_1E,                         'L'),
    inst(AS_1F,                         'WWB'),
    inst(ChrTurnAndMove,                'BBBII'),       # ChrTurnAndMove(0, src, target, target_pos_offset, speed)
    inst(AS_21,                         'BBii'),
    inst(BeginChrThread,                'BCoB',                 INSTRUCTION_START_BLOCK),
    inst(WaitChrThread,                 'BC'),
    inst(SetChipModeFlags,              'BBW'),
    inst(ClearChipModeFlags,            'BBW'),
    inst(SetMSDataState,                'CBW'),         # SetMSDataState(state 1 or 2, chr, flags)
    inst(ClearMSDataState,              'CBW'),
    inst(Say,                           'BSL'),
    inst(AS_29,                         'B'),
    inst(ShowInfoText,                  'SI'),
    inst(AS_2B),
    inst(ShowChrTrails,                 'BHH'),         # ShowChrTrails(target, interval, number)
    inst(HideChrTrails,                 'B'),
    inst(ShakeChr,                      'Biii'),
    inst(EndChrThread,                  'BC'),
    inst(AS_31,                         'BW'),
    inst(AS_32,                         'BB'),
    inst(AS_33,                         'BB'),
    inst(AS_34),
    inst(LockCamera,                    'BiiiH'),       # LockCamera(target, x, z, y, move_time)
    inst(AS_36,                         'B'),
    inst(SetCameraDegree,               'hhhh'),        # SetCameraDegree(horizon, vertical, height, 0)
    inst(AS_3A,                         'WW'),
    inst(SetCameraDistance,             'ih'),          # SetCameraDistance(Distance, MoveToTime)
    inst(AS_3C,                         'WW'),
    inst(ShakeScreen,                   'HHHH'),
    inst(AS_3E,                         'WW'),
    inst(AS_3F,                         'B'),
    inst(AS_40,                         'B'),
    inst(AS_43,                         'BWL'),
    inst(Fade,                          'BHL'),         # Fade(0 or 1, time, 0x0)
    inst(AS_45,                         'BL'),
    inst(AS_46,                         'BLL'),
    inst(AS_47,                         'B'),
    inst(AS_48,                         'BL'),
    inst(SetControl,                    'BW'),
    inst(AS_4A,                         'B'),
    inst(Jc,                            'BBLo',                 INSTRUCTION_START_BLOCK),
    inst(ForeachTarget,                 'o',                    INSTRUCTION_START_BLOCK),
    inst(ResetTarget),
    inst(NextTarget),
    inst(AS_4F),
    inst(Call,                          'o',                    INSTRUCTION_CALL),    # ret stack size == 4
    inst(CallReturn,                    NO_OPERAND,             INSTRUCTION_END_BLOCK),
    inst(AS_52,                         'B'),
    inst(AS_53,                         'B'),
    inst(SendMessage,                   'B'),
    inst(ArtsUsing,                     'W'),
    inst(ArtsEnd),
    inst(AS_57,                         'BB'),
    inst(Knockback,                     'B'),
    inst(AS_59,                         'BW'),
    inst(SetBrightness,                 'BBH'),         # SetBrightness
    inst(ResetBrightness,               'H'),           # ResetBrightness(time)
    inst(ShowChr,                       'BH'),
    inst(HideChr,                       'BH'),
    inst(AS_5E,                         'B'),
    inst(AS_5F,                         'BB'),
    inst(AS_60,                         'B'),
    inst(SetBattleSpeed,                'I'),
    inst(Voice,                         'BHHHHB'),
    inst(Sound,                         'H'),
    inst(SoundEx,                       'HB'),          # SoundEx(se, repeat)
    inst(StopSound,                     'H'),           # StopSound(se)
    inst(AS_67,                         'WBB'),
    inst(AS_68,                         'BBL'),
    inst(LoadChrChip,                   NO_OPERAND,             0,                          as_load_chr_chip),
    inst(AS_6B),
    inst(Dead),
    inst(AS_6D,                         'L'),
    inst(AS_6E,                         'L'),
    inst(AS_6F,                         'BB'),
    inst(AS_70,                         'BBWWWW'),
    inst(AS_71,                         'B'),
    inst(AS_72),
    inst(AS_73,                         'B'),
    inst(AS_74,                         'BW'),
    inst(AS_77,                         'B'),
    inst(AS_78,                         'C'),
    inst(AS_79,                         'B'),
    inst(AS_7A,                         'B'),
    inst(AS_7B,                         'W'),
    inst(AS_7C,                         'BB'),
    inst(AS_7D,                         'BL'),
    inst(AS_7E,                         'L'),
    inst(BlurSwitch,                    'WLBBB'),       # BlurSwitch(0, rgba, 0, 1, 3)
    inst(CancelBlur,                    'I'),
    inst(AS_82),
    inst(SortTarget,                    'B'),
    inst(ChrRotate,                     'BHHHIB'),      # ChrRotate(TargetChr, Degree, xx, xxx, xxxx, 4)
    inst(AS_85,                         'BBL'),
    inst(AS_87,                         'WB'),
    inst(AS_89,                         'B'),
    inst(ChrDuplicate,                  'BB'),          # ChrDuplicate(TargetChr, SourceChr)
    inst(UseItemBegin),
    inst(UseItemEnd),
    inst(AS_8D,                         'BLLLL'),
    inst(AS_8E,                         NO_OPERAND,             0,                          as_op_8e),
    inst(AS_8F,                         'B'),
    inst(AS_91,                         NO_OPERAND,             0,                          as_op_91),
    inst(ChrSetRelativePos,             'BBiiihi'),
    inst(AS_93,                         'BBS'),
    inst(AS_94,                         'BSL'),
    inst(ResetLookingTargetData),
    inst(LookingTargetAdd,              'BSB'),
    inst(LookingTarget,                 'HCC'),
    inst(AS_98,                         'B'),
    inst(AS_99,                         'B'),
    inst(AS_9A,                         'L'),
    inst(AS_9B,                         'B'),
    inst(AS_9C,                         'B'),
    inst(AS_9E,                         'BS'),
    inst(AS_9F,                         'BB'),
    inst(AS_A0,                         'BL'),
    inst(PlayEffectIfConditionExist,    'BLWS'),            # PlayEffectIfConditionExist(target, condition_flags, eff_index, '')
    inst(AS_A6,                         'BBLLB'),
    inst(AS_A7,                         'BBBhhhhhhh'),
    inst(AS_A8,                         'BB'),
    inst(SetEffectColor,                'BCL'),             # SetEffectColor(owner, eff_handle, rgba)
    inst(AS_AC,                         'LL'),
    inst(AS_AD,                         'B'),
    inst(QueueWorkItem,                 NO_OPERAND,             0,                          as_op_ae),
    inst(AS_AF,                         'W'),
    inst(AS_B0,                         'WW'),
    inst(AS_B1,                         'BSBL'),
    inst(PlayBGM,                       'BW'),
    inst(SetScenarioFlags,              'BW'),
    inst(SetChrCalcEnable,              'BB'),
    inst(LoadCclm,                      NO_OPERAND,             0,                          as_load_cclm),
    inst(UnlockCclm,                    NO_OPERAND,             0,                          as_unlock_cclm),
    inst(AS_B7),
    inst(AS_B8,                         'B'),
]

#del inst

for op in edao_as_op_list:
    edao_as_op_table[op.OpCode] = op
    op.Container = edao_as_op_table


def DynamicAddInstruction(op, name, operand = NO_OPERAND, flags = 0, handler = None):
    entry = EDAOASOpTableEntry(op, name, operand, flags, handler)
    edao_as_op_list.append(entry)

    edao_as_op_table[op] = entry
    entry.Container = edao_as_op_table


'''

set chr size
AS_8D(0x7, 0x13, 0x28A, 0x28A, 0x28A)


'''

if __name__ == '__main__':
    valid = 0
    for inst in edao_as_op_list:
        if inst.OpName[:3] != 'AS_':
            valid += 1
    print('known: %d (%d%%)' % (valid, valid / len(edao_as_op_list) * 100))
    print('total: %d' % len(edao_as_op_list))
    console.pause()

