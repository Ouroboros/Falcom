from ml import *
import Assembler

from Falcom import ED6FC

def test():
    print(ED6FC.ScenaOpTable)
    print()

    dis = Assembler.Disassembler(ED6FC.ScenaOpTable)

    fs = fileio.FileStream()
    fs.OpenMemory(open('tests\\T2610_1 ._SN', 'rb').read())

    fs.Position = 0x64

    info = Assembler.DisassembleInfo(fs)

    fun = dis.disasmFunction(info)

    fun.name = 'test'

    print('\n'.join(dis.formatFuncion(fun)))

def main():
    test()

    console.pause('done')

if __name__ == '__main__':
    Try(main)
