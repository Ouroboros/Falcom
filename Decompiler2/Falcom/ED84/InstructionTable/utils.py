# from Falcom.Common  import *
# from Assembler      import *
from Falcom.ED83.InstructionTable.utils import *

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    from .scena import ED84OperandDescriptor
    return ctx.instructionTable.readAllOperands(ctx, ED84OperandDescriptor.fromFormatString(fmts))

def ScriptThread_getFunctionStrWorkValue(threadId: int) -> str:
    return 'B' + {
        0x11: 'LB',
        # 0x22: 'LB',
        0x33: 'LB',
        0x44: 'LB',
        0x55: 'LB',
        0xDD: 'S',
        0xEE: 'fB',
        0xFF: 'LB',
    }[threadId]
