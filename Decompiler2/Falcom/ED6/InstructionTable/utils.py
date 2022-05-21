from Falcom.Common  import *
from Assembler      import *

def genVariadicFuncStub(desc: InstructionDescriptor, *types, parameters = None) -> List[str]:
    params = []
    args = []
    assertion = []

    if parameters is None:
        parameters = list(desc.parameters)

    if not parameters:
        parameters = []

    parameters.extend([f'arg{i + 1}' for i in range(len(parameters), len(types))])

    for i, t in enumerate(types):
        typeName = t.__name__

        if t is float:
            typeName = 'float | int'

        params.append(f'{parameters[i]}: {typeName}')
        args.append(f'{parameters[i]}')
        assertion.append(f'    assert isinstance({parameters[i]}, {typeName})')

    if types:
        params.append('')
        args.append('')

    return [
        f'def {desc.mnemonic}({", ".join(params)}*args):',
        f'    # 0x{desc.opcode:02X}',
        *assertion,
        f'    return _gScena.handleOpCode(0x{desc.opcode:02X}, {", ".join(args)}*args)',
        '',
    ]

def readAllOperands(ctx: InstructionHandlerContext, fmts: str) -> List[Operand]:
    from .scena import ED6OperandDescriptor
    return ctx.instructionTable.readAllOperands(ctx, ED6OperandDescriptor.fromFormatString(fmts))

def peekByte(ctx: InstructionHandlerContext) -> int:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.ReadByte()

def peekWord(ctx: InstructionHandlerContext) -> int:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.ReadUShort()

def peekWords(ctx: InstructionHandlerContext, n: int) -> List[int]:
    with ctx.disasmContext.fs.PositionSaver:
        return [ctx.disasmContext.fs.ReadUShort() for _ in range(n)]

def peekBytes(ctx: InstructionHandlerContext, n: int) -> bytes:
    with ctx.disasmContext.fs.PositionSaver:
        return ctx.disasmContext.fs.Read(n)

def formatText(t: str) -> str:
    s = []
    for ch in t:
        if ch == '\\':
            s.append('\\\\')
        elif ch in ["'", '"']:
            s.append(f'\\x{ord(ch):02X}')
        elif ch >= ' ':
            s.append(ch)
        elif ch == '\n':
            s.append('\\n')
        elif ch == '\t':
            s.append('\\t')
        else:
            s.append(f'\\x{ord(ch):02x}')

    return f"'{''.join(s)}'"
