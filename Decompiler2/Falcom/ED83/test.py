from Falcom import ED83
from Falcom.Common import *
import pathlib

from hexdump import hexdump

def test(filename, output = None):
    if pathlib.Path(filename).stem == 'r4400':
        return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    fs.Encoding = GlobalConfig.DefaultEncoding
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
        # 'chr009.dat',
        # 'm3040.dat',
        # 'm4000.dat',
        # 'system3.dat',
        # 'common.dat',
        # 'alchr009.dat',
        # 'almon450_1.dat',
        # 'face.dat',
        # 'r4400.dat',
    ][-1]

    scena = [
        r'E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\\',
        # r'E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\ani\dat\\',
        # r'E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\battle\dat\\',
    ]

    # for s in scena:
    #     for f in fileio.getDirectoryFiles(s, '*.dat'):
    #         console.setTitle(os.path.basename(f))
    #         test(f)

    test(scena[-1] + scp, scp + '.py')

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
