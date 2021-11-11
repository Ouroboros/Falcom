from Common     import *
from Assembler  import *
from .types     import *

__all__ = (
    'ScenaOpTable',
)

NoOperand = InstructionDescriptor.NoOperand

class ED83InstructionTable(InstructionTable):
    def readOpCode(self, fs: fileio.FileStream) -> int:
        return fs.ReadByte()

    def writeOpCode(self, fs: fileio.FileStream, inst: 'Instruction'):
        fs.WriteByte(inst.opcode)

    def readOperand(self, context: 'handlers.InstructionHandlerContext', inst: 'instruction.Instruction', desc: OperandDescriptor) -> 'instruction.Operand':
        opr = super().readOperand(context, inst, desc)
        if desc.format.type == ED83OperandType.Offset:
            opr.value = context.addBranch(opr.value)

        return opr

    def writeOperand(self, fs: fileio.FileStream, operand: 'instruction.Operand'):
        raise NotImplementedError


def inst(opcode: int, mnemonic: str, operandfmts: str = None, flags: Flags = Flags.Empty, handler: InstructionHandler = None, *, parameters = None) -> InstructionDescriptor:
    if operandfmts is NoOperand:
        operands = NoOperand
    else:
        operands = ED83OperandDescriptor.fromFormatString(operandfmts)

    if parameters:
        for i, param in enumerate(parameters):
            operands[i].paramName = param

    return InstructionDescriptor(opcode = opcode, mnemonic = mnemonic, operands = operands, flags = flags, handler = handler)

ScenaOpTable = ED83InstructionTable([
    inst(0x00,  'ExitThread'),
    inst(0x01,  'Return',                       NoOperand,          Flags.EndBlock),
])

del inst
