from Falcom import ED83
from Falcom.Common import *

from hexdump import hexdump

def test():
    scp = [
        'a0000.dat',
        # 'chr000.dat',
        # 'm3040.dat',
        # 'm4000.dat',
        'system3.dat',
    ][-1]

    scena = '''E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\\'''

    fs = fileio.FileStream().OpenMemory(open(scena + scp, 'rb').read())
    scena = ED83.Parser.SceneParser(fs)
    scena.readHeader()

    print(ED83.InstructionTable.ScenaOpTable)
    print()
    print(scena)

    scena.disasmFunctions()
    py = scena.generatePython('chr000.dat')

    open('out.py', 'wb').write('\n'.join(py).encode('UTF8'))


def main():
    test()

    console.pause('done')

if __name__ == '__main__':
    Try(main)
