from Falcom.Common  import *
from Assembler      import *
from Falcom         import ED85

def map_operand_type(t: OperandType) -> str:
    return {
        OperandType.SInt8               : 'sint8',
        OperandType.SInt16              : 'sint8',
        OperandType.SInt32              : 'sint32',
        OperandType.SInt64              : 'sint64',
        OperandType.UInt8               : 'uint8',
        OperandType.UInt16              : 'uint16',
        OperandType.UInt32              : 'uint32',
        OperandType.UInt64              : 'uint64',
        OperandType.Float32             : 'float32',
        OperandType.Float64             : 'float64',
        OperandType.MBCS                : 'str',
        ED85.ED85OperandType.Text       : 'str | tuple',
        ED85.ED85OperandType.Offset     : 'str',
        ED85.ED85OperandType.ScenaFlags : 'uint16',
        ED85.ED85OperandType.ChrId      : 'uint16',
        ED85.ED85OperandType.Item       : 'uint16',
        ED85.ED85OperandType.ScriptId   : 'uint8',
        ED85.ED85OperandType.Expression : 'tuple | list',
        ED85.ED85OperandType.ThreadValue: 'tuple | list',
    }[t]

def main():
    import pathlib
    filename = pathlib.Path(__file__)
    filename = filename.parent / ('scena_writer_gen.py')

    lines = [
        'from Falcom.ED85.Parser.scena_writer import _gScena',
        '',
        'sint8 = int',
        'uint8 = int',
        'sint16 = int',
        'uint16 = int',
        'sint32 = int',
        'uint32 = int',
        'float32 = float | int',
        '',
    ]

    for desc in sorted(ED85.ScenaOpTable, key = lambda desc: desc.opcode):
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
                if not parameters:
                    parameters = []
                else:
                    parameters = list(parameters)

                parameters.extend([f'arg{i + 1}' for i in range(len(parameters), len(desc.operands))])

                for i, opr in enumerate(desc.operands):
                    typeHint = map_operand_type(opr.format.type)
                    name = parameters[i]
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
                f'    _gScena.handleOpCode({", ".join(args)})',
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
