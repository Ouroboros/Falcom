from Falcom import ED83
from Falcom.Common import *
import pathlib

from hexdump import hexdump

def test(filename, output = None):
    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    scena = ED83.Parser.ScenaParser(fs)

    scena.parse()

    py = scena.generatePython(os.path.basename(filename))

    if output is None:
        output = pathlib.Path((filename))
        os.makedirs(output.parent / 'py', exist_ok = True)
        output = output.parent / 'py' / (output.name + '.py')

    open(output, 'wb').write('\n'.join(py).encode('UTF8'))

def main():
    scp = [
        'a0000.dat',
        'chr009.dat',
        # 'm3040.dat',
        # 'm4000.dat',
        # 'system3.dat',
        # 'common.dat',
        # 'alchr009.dat',
        # 'alchr033_1.dat',
    ][-1]

    scena = r'E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\\'
    scena = r'E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\ani\dat\\'
    # scena = r'E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\battle\dat\\'

    # for f in fileio.getDirectoryFiles(scena, '*.dat'):
    #     console.setTitle(os.path.basename(f))
    #     test(f)

    test(scena + scp, scp + '.py')

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
