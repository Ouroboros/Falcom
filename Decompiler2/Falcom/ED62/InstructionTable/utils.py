from Falcom.ED6.InstructionTable.utils import *

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    from .scena import ED62OperandDescriptor
    return ctx.instructionTable.readAllOperands(ctx, ED62OperandDescriptor.fromFormatString(fmts))
