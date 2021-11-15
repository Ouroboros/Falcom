from Falcom.Common  import *
from Assembler      import *
from .types         import *

__all__ = (
    'ScenaOpTable',
    'ED83InstructionTable',
    'ED83OperandType',
    'ED83OperandFormat',
    'ED83OperandDescriptor'
)

NoOperand = InstructionDescriptor.NoOperand

class ED83InstructionTable(InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        return fs.ReadByte()

    def writeOpCode(self, fs: fileio.FileStream, inst: Instruction):
        fs.WriteByte(inst.opcode)

    def readOperand(self, context: InstructionHandlerContext, inst: Instruction, desc: ED83OperandDescriptor) -> ED83OperandType:
        opr = super().readOperand(context, inst, desc)
        if desc.format.type == ED83OperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, fs: fileio.FileStream, operand: ED83OperandType):
        raise NotImplementedError


def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = []) -> InstructionDescriptor:
    if operandfmts is NoOperand:
        operands = NoOperand
        if parameters:
            raise

    else:
        operands = ED83OperandDescriptor.fromFormatString(operandfmts)
        if parameters and len(operands) != len(parameters):
            raise

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler, parameters = parameters)

def Handler_Switch():
    pass

ScenaOpTable = ED83InstructionTable([
    inst(0x00,  'ExitThread',                   NoOperand,          Flags.EndBlock),
    inst(0x01,  'Return',                       NoOperand,          Flags.EndBlock),
    inst(0x02,  'Call',                         'BSB',              Flags.StartBlock, parameters = ('type', 'name', 'type2')),
    inst(0x03,  'Jump',                         'o',                Flags.Jump, parameters = ('label', )),
    inst(0x04,  'OP_04',                        'BS'),
    inst(0x06,  'Switch',                       NoOperand,          Flags.EndBlock,     Handler_Switch),
    inst(0x2B,  'Battle',                       ''),
])

del inst
