from Falcom.Common  import *
from Assembler      import *

def genVariadicFuncStub(desc: InstructionDescriptor, *types, parameters = None) -> List[str]:
    params = []
    args = []
    assertion = []

    if parameters is None:
        parameters = desc.parameters

    if not parameters:
        parameters = [f'arg{i + 1}' for i in range(len(types))]

    for i, t in enumerate(types):
        params.append(f'{parameters[i]}: {t.__name__}')
        args.append(f'{parameters[i]}')
        assertion.append(f'    assert isinstance({parameters[i]}, {t.__name__})')

    if types:
        params.append('')
        args.append('')

    return [
        f'def {desc.mnemonic}({", ".join(params)}*args):',
        f'    # 0x{desc.opcode:02X}',
        *assertion,
        f'    return scena.handleOpCode(0x{desc.opcode:02X}, {", ".join(args)}*args)',
        '',
    ]

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    from .scena import ED83OperandDescriptor
    return ctx.instructionTable.readAllOperands(ctx, ED83OperandDescriptor.fromFormatString(fmts))

def peekByte(ctx: InstructionHandlerContext) -> int:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.ReadByte()

def peekBytes(ctx: InstructionHandlerContext, n: int) -> bytes:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.Read(n)

def ScriptThread_getFunctionStrWorkValue(threadId: int) -> str:
    return 'B' + {
        0x11: 'LB',
        # 0x22: 'LB',
        # 0x33: 'LB',
        # 0x44: 'LB',
        0xDD: 'S',
        0xEE: 'fB',
        0xFF: 'LB',
    }[threadId]

def formatText(t: str) -> str:
    s = ''
    for ch in t:
        if ch >= ' ':
            s += ch
        else:
            s += f'\\x{ord(ch):02x}'

    return f"'{s}'"
