from Falcom.Common import *
from Falcom import ED83

def test():
    print(ED83.ScenaOpTable)
    print()

    dis = Assembler.Disassembler(ED83.ScenaOpTable)

    fs = fileio.FileStream()
    fs.OpenMemory(open('tests\\T2610_1 ._SN', 'rb').read())

    fs.Position = 0x64

    ctx = Assembler.DisasmContext(fs)

    fun = dis.disasmFunction(ctx)

    fun.name = 'test'

    print('\n'.join(dis.formatFuncion(fun)))

def main():
    test()

    console.pause('done')

if __name__ == '__main__':
    Try(main)
