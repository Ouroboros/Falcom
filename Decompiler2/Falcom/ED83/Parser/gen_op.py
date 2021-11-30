from Falcom.Common  import *
from Assembler      import *
from Falcom         import ED83

def map_operand_type(t: OperandType) -> str:
    return {
        OperandType.SInt8               : 'int',
        OperandType.SInt16              : 'int',
        OperandType.SInt32              : 'int',
        OperandType.SInt64              : 'int',
        OperandType.UInt8               : 'int',
        OperandType.UInt16              : 'int',
        OperandType.UInt32              : 'int',
        OperandType.UInt64              : 'int',
        OperandType.Float32             : 'float',
        OperandType.Float64             : 'float',
        OperandType.MBCS                : 'str',
        ED83.ED83OperandType.Text       : 'str | tuple',
        ED83.ED83OperandType.Offset     : 'str',
        ED83.ED83OperandType.ScenaFlags : 'int',
        ED83.ED83OperandType.Expression : 'tuple | list',
        ED83.ED83OperandType.ThreadValue: 'tuple | list',
    }[t]

def main():
    import pathlib
    filename = pathlib.Path(__file__)
    filename = filename.parent / ('scena_writer_gen.py')

    lines = [
        'from Falcom.ED83.Parser.scena_writer import _gScena as scena',
        '',
    ]

    for desc in ED83.ScenaOpTable.descriptors:
        desc: Assembler.InstructionDescriptor

        func = None

        if desc.handler:
            ctx = InstructionHandlerContext(HandlerAction.CodeGen, desc)
            try:
                func = desc.handler(ctx)
            except NotImplementedError:
                func = [
                    f'def {desc.mnemonic}():',
                    '    raise NotImplementedError',
                    '',
                ]

        if func is None:
            parameters = desc.parameters
            params = []
            args = []
            types = []

            if desc.operands:
                for i, opr in enumerate(desc.operands):
                    typeHint = map_operand_type(opr.format.type)
                    if parameters and parameters[i]:
                        name = parameters[i]
                    else:
                        name = f'arg{i + 1}'

                    params.append(f'{name}: {typeHint}')
                    args.append(name)
                    types.append(typeHint)

            checkTypes = []

            if types:
                for i, t in enumerate(types):
                    checkTypes.append(f'    assert isinstance({args[i]}, {t})')

            args.insert(0, f'0x{desc.opcode:02X}')

            func = [
                f'def {desc.mnemonic}({", ".join(params)}):',
                f'    # 0x{desc.opcode:02X}',
                *checkTypes,
                f'    scena.handleOpCode({", ".join(args)})',
                '',
            ]

        lines.extend(func)

        if not desc.mnemonic.startswith('OP_'):
            func[0] = func[0].replace(desc.mnemonic, f'OP_{desc.opcode:02X}')
            lines.extend(func)

    open(filename, 'wb').write('\n'.join(lines).encode('UTF8'))

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
