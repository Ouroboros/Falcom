# from Falcom.Common  import *
# from Assembler      import *
from Falcom.ED83.InstructionTable.utils import *

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    from .scena import ED84OperandDescriptor
    return ctx.instructionTable.readAllOperands(ctx, ED84OperandDescriptor.fromFormatString(fmts))

# def ScriptThread_getFunctionStrWorkValue(threadId: int) -> str:
#     return 'B' + {
#         0x11: 'LB',     # arg reg
#         # 0x22: 'LB',
#         0x33: 'LB',     # arg int
#         0x44: 'LB',     # arg str
#         0x55: 'LB',
#         0xDD: 'S',      # param str
#         0xEE: 'fB',     # param float
#         0xFF: 'LB',     # param long
#     }[threadId]
