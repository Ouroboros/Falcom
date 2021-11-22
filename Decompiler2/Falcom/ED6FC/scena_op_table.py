from Common     import *
from Assembler  import *
from .types     import *

__all__ = (
    'ScenaOpTable',
)

NoOperand = InstructionDescriptor.NoOperand

class ED6FCInstructionTable(InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        return fs.ReadByte()

    def writeOpCode(self, fs: fileio.FileStream, opcode: int):
        fs.WriteByte(opcode)

    def readOperand(self, context: 'handlers.InstructionHandlerContext', desc: OperandDescriptor) -> 'instruction.Operand':
        opr = super().readOperand(context, desc)
        if desc.format.type == ED6FCOperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, fs: fileio.FileStream, operand: Operand):
        raise NotImplementedError

for i in ED6FCOperandType:
    globals()[i.name] = i

for i in TextCtrlCode:
    globals()[i.name] = i

def Handler_If(info: InstructionHandlerContext):
    pass

def Handler_Switch(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_NewScene(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_16(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_28(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_29(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_2A(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_41(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_QueueWorkItem(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_QueueWorkItem2(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_RunExpression(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_4F(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_51(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_AnonymousTalk(info: InstructionHandlerContext):
    return

def Handler_ChrTalk(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_NpcTalk(info: InstructionHandlerContext):
    raise NotImplementedError

def Handler_Menu(info: InstructionHandlerContext):
    raise NotImplementedError

def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None) -> InstructionDescriptor:
    if operandfmts is NoOperand:
        operands = NoOperand
    else:
        operands = ED6FCOperandDescriptor.fromFormatString(operandfmts)

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler)

ScenaOpTable = ED6FCInstructionTable([
    inst(0x00,  'ExitThread'),
    inst(0x01,  'Return',                       NoOperand,          Flags.EndBlock),
    inst(0x02,  'If',                           'Eo',               Flags.StartBlock,   Handler_If),
    inst(0x03,  'Jump',                         'o',                Flags.Jump),
    inst(0x04,  'Switch',                       NoOperand,          Flags.EndBlock,     Handler_Switch),
    inst(0x05,  'Call',                         'CH'),                                                      # Call(scp index, func index)
    inst(0x06,  'NewScene',                     'LCCC',             Flags.Empty,        Handler_NewScene),
    inst(0x07,  'IdleLoop'),
    inst(0x08,  'Sleep',                        'I'),
    inst(0x09,  'SetMapFlags',                  'L'),
    inst(0x0A,  'ClearMapFlags',                'L'),
    inst(0x0B,  'FadeToDark',                   'iic'),
    inst(0x0C,  'FadeToLight',                  'ii'),
    inst(0x0D,  'OP_0D'),
    inst(0x0E,  'Fade',                         'I'),
    inst(0x0F,  'Battle',                       'LLBWB'),
    inst(0x10,  'OP_10',                        'BB'),
    inst(0x11,  'OP_11',                        'BBBLLL'),
    inst(0x12,  'StopSound',                    'LLL'),
    inst(0x13,  'SetPlaceName',                 'W'),
    inst(0x14,  'BlurSwitch'),
    inst(0x15,  'OP_15'),
    inst(0x16,  'OP_16',                        NoOperand,          Flags.Empty,        Handler_16),
    inst(0x17,  'ShowSaveMenu'),
    inst(0x18,  'OP_18'),
    inst(0x19,  'EventBegin',                   'B'),
    inst(0x1A,  'EventEnd',                     'B'),
    inst(0x1B,  'OP_1B',                        'BBW'),
    inst(0x1C,  'OP_1C',                        'BBW'),
    inst(0x1D,  'OP_1D',                        'B'),
    inst(0x1E,  'OP_1E'),
    inst(0x1F,  'OP_1F',                        'BL'),
    inst(0x20,  'OP_20',                        'L'),
    inst(0x21,  'OP_21'),
    inst(0x22,  'OP_22',                        'WBB'),
    inst(0x23,  'OP_23',                        'W'),
    inst(0x24,  'OP_24',                        'WB'),
    inst(0x25,  'SoundDistance',                'WLLLLLBL'),
    inst(0x26,  'SoundLoad',                    'H'),
    inst(0x27,  'Yield'),
    inst(0x28,  'OP_28',                        NoOperand,          Flags.Empty,        Handler_28),
    inst(0x29,  'OP_29',                        NoOperand,          Flags.Empty,        Handler_29),
    inst(0x2A,  'OP_2A',                        NoOperand,          Flags.Empty,        Handler_2A),
    inst(0x2B,  'OP_2B',                        'WW'),
    inst(0x2C,  'OP_2C',                        'WW'),
    inst(0x2D,  'AddParty',                     'BB'),
    inst(0x2E,  'RemoveParty',                  'BB'),
    inst(0x2F,  'ClearParty'),
    inst(0x30,  'OP_30',                        'B'),
    inst(0x31,  'OP_31',                        'BBW'),
    inst(0x32,  'OP_32',                        'BW'),
    inst(0x33,  'OP_33',                        'BW'),
    inst(0x34,  'OP_34',                        'BW'),
    inst(0x35,  'OP_35',                        'BW'),
    inst(0x36,  'OP_36',                        'BW'),
    inst(0x37,  'OP_37',                        'BW'),
    inst(0x38,  'AddSepith',                    'BW'),  # AddSepith(0~6, number)
    inst(0x39,  'SubSepith',                    'BW'),
    inst(0x3A,  'AddMira',                      'H'),
    inst(0x3B,  'SubMira',                      'H'),
    inst(0x3C,  'OP_3C',                        'H'),
    inst(0x3D,  'OP_3D',                        'H'),
    inst(0x3E,  'OP_3E',                        'Wh'),
    inst(0x3F,  'OP_3F',                        'Wh'),
    inst(0x40,  'OP_40',                        'W'),
    inst(0x41,  'OP_41',                        NoOperand,          Flags.Empty,        Handler_41),
    inst(0x42,  'OP_42',                        'B'),
    inst(0x43,  'BeginChrThread',               'WBBW'),
    inst(0x44,  'EndChrThread',                 'WB'),
    inst(0x45,  'QueueWorkItem',                NoOperand,          Flags.Empty,        Handler_QueueWorkItem),
    inst(0x46,  'QueueWorkItem2',               NoOperand,          Flags.Empty,        Handler_QueueWorkItem2),
    inst(0x47,  'WaitChrThread',                'WW'),
    inst(0x48,  'OP_48'),
    inst(0x49,  'Event',                        'CH'),
    inst(0x4A,  'OP_4A',                        'WC'),
    inst(0x4B,  'OP_4B',                        'WC'),
    inst(0x4C,  'OP_4C'),
    inst(0x4D,  'RunExpression',                NoOperand,          Flags.Empty,        Handler_RunExpression),
    inst(0x4E,  'OP_4E'),
    inst(0x4F,  'OP_4F',                        NoOperand,          Flags.Empty,        Handler_4F),
    inst(0x50,  'OP_50'),
    inst(0x51,  'OP_51',                        NoOperand,          Flags.Empty,        Handler_51),
    inst(0x52,  'TalkBegin',                    'W'),
    inst(0x53,  'TalkEnd',                      'W'),
    inst(0x54,  'AnonymousTalk',                'S',                Flags.Empty,        Handler_AnonymousTalk),
    inst(0x55,  'OP_55'),
    inst(0x56,  'OP_56',                        'B'),
    inst(0x57,  'OP_57'),
    inst(0x58,  'WaitAndCloseMessageWindow'),
    inst(0x59,  'OP_59'),
    inst(0x5A,  'SetMessageWindowPos',          'hhhh'),  # SetMessageWindowPos(x, y, -1, -1)
    inst(0x5B,  'ChrTalk',                      NoOperand,          Flags.Empty,        Handler_ChrTalk),
    inst(0x5C,  'NpcTalk',                      NoOperand,          Flags.Empty,        Handler_NpcTalk),
    inst(0x5D,  'Menu',                         NoOperand,          Flags.Empty,        Handler_Menu),
    inst(0x5E,  'MenuEnd',                      'W'),
    inst(0x5F,  'OP_5F',                        'W'),
    inst(0x60,  'SetChrName',                   'S'),
    inst(0x61,  'OP_61',                        'W'),
    inst(0x62,  'OP_62',                        'WLIBBLB'),
    inst(0x63,  'OP_63',                        'W'),
    inst(0x64,  'OP_64',                        'BW'),
    inst(0x65,  'OP_65',                        'BW'),
    inst(0x66,  'OP_66',                        'W'),
    inst(0x67,  'OP_67',                        'iiii'),
    inst(0x68,  'OP_68',                        'W'),
    inst(0x69,  'OP_69',                        'WL'),
    inst(0x6A,  'OP_6A',                        'W'),
    inst(0x6B,  'OP_6B',                        'ii'),  # SetCameraDistance(distance, duration)
    inst(0x6C,  'OP_6C',                        'ii'),
    inst(0x6D,  'OP_6D',                        'iiii'),
    inst(0x6E,  'OP_6E',                        'ii'),
    inst(0x6F,  'OP_6F',                        'Wi'),
    inst(0x70,  'OP_70',                        'WL'),
    inst(0x71,  'OP_71',                        'WW'),
    inst(0x72,  'OP_72',                        'WW'),
    inst(0x73,  'OP_73',                        'W'),
    inst(0x74,  'OP_74',                        'WLW'),
    inst(0x75,  'OP_75',                        'BLB'),
    inst(0x76,  'OP_76',                        'WLWLLLBB'),
    inst(0x77,  'OP_77',                        'BBBLB'),
    inst(0x78,  'OP_78',                        'BBB'),
    inst(0x79,  'OP_79',                        'BW'),
    inst(0x7A,  'OP_7A',                        'BW'),
    inst(0x7B,  'OP_7B'),
    inst(0x7C,  'OP_7C',                        'LLLL'),
    inst(0x7D,  'OP_7D',                        'B'),
    inst(0x7E,  'OP_7E',                        'WWWBL'),
    inst(0x7F,  'LoadEffect',                   'BS'),
    inst(0x80,  'PlayEffect',                   'BBWiiihhhiiiwiiii'),
    inst(0x81,  'Play3DEffect',                 'BBBSLLLWWWLLLL'),
    inst(0x82,  'OP_82',                        'BB'),
    inst(0x83,  'OP_83',                        'BB'),
    inst(0x84,  'OP_84',                        'B'),
    inst(0x85,  'OP_85',                        'W'),
    inst(0x86,  'SetChrChipByIndex',            'WH'),
    inst(0x87,  'SetChrSubChip',                'WH'),
    inst(0x88,  'SetChrPos',                    'Wiiih'),
    inst(0x89,  'OP_89',                        'Wiiih'),
    inst(0x8A,  'TurnDirection',                'WWH'),
    inst(0x8B,  'OP_8B',                        'WLLW'),
    inst(0x8C,  'OP_8C',                        'Whh'),
    inst(0x8D,  'OP_8D',                        'Wiiiii'),
    inst(0x8E,  'OP_8E',                        'WLLLLB'),
    inst(0x8F,  'OP_8F',                        'WLLLLB'),
    inst(0x90,  'OP_90',                        'WLLLLB'),
    inst(0x91,  'OP_91',                        'WLLLLB'),
    inst(0x92,  'OP_92',                        'WWLLB'),
    inst(0x93,  'OP_93',                        'WWLLB'),
    inst(0x94,  'OP_94',                        'BWWLLB'),
    inst(0x95,  'OP_95',                        'WLLLLL'),
    inst(0x96,  'OP_96',                        'WLLLLL'),
    inst(0x97,  'OP_97',                        'WLLLLW'),
    inst(0x98,  'OP_98',                        'WLLLL'),
    inst(0x99,  'OP_99',                        'WBBL'),
    inst(0x9A,  'SetChrFlags',                  'WW'),
    inst(0x9B,  'ClearChrFlags',                'WW'),
    inst(0x9C,  'SetChrBattleFlags',            'WW'),
    inst(0x9D,  'ClearChrBattleFlags',          'WW'),
    inst(0x9E,  'OP_9E',                        'WLLLL'),
    inst(0x9F,  'OP_9F',                        'WBBBBL'),
    inst(0xA0,  'OP_A0',                        'WBBBL'),
    inst(0xA1,  'OP_A1',                        'WW'),
    inst(0xA2,  'OP_A2',                        'W'),
    inst(0xA3,  'OP_A3',                        'W'),
    inst(0xA4,  'OP_A4',                        'W'),
    inst(0xA5,  'OP_A5',                        'W'),
    inst(0xA6,  'OP_A6',                        'W'),
    inst(0xA7,  'OP_A7',                        'WW'),
    inst(0xA8,  'OP_A8',                        'BBBBB'),
    inst(0xA9,  'OP_A9',                        'B'),
    inst(0xAA,  'OP_AA'),
    inst(0xAB,  'OP_AB'),
    inst(0xAC,  'OP_AC',                        'W'),
    inst(0xAD,  'OP_AD',                        'LWWL'),
    inst(0xAE,  'OP_AE',                        'L'),
    inst(0xAF,  'OP_AF',                        'BW'),
    inst(0xB0,  'OP_B0',                        'WB'),
    inst(0xB1,  'OP_B1',                        'S'),
    inst(0xB2,  'OP_B2',                        'BBW'),
    inst(0xB3,  'PlayMovie',                    'BS'),
    inst(0xB4,  'OP_B4',                        'B'),
    inst(0xB5,  'OP_B5',                        'WB'),
    inst(0xB6,  'OP_B6',                        'B'),
    inst(0xB7,  'OP_B7',                        'WB'),
    inst(0xB8,  'OP_B8',                        'B'),
    inst(0xB9,  'OP_B9',                        'WW'),
    inst(0xBA,  'OP_BA',                        'BW'),
    inst(0xBB,  'OP_BB',                        'BB'),
    inst(0xBC,  'SaveClearData'),
])

del inst
