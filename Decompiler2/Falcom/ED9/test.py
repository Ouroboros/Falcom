from Falcom import ED9
from Falcom.Common import *
import pathlib

from hexdump import hexdump

def test(filename, output):
    if pathlib.Path(filename).stem in [
        ]:
        return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    fs.Encoding = GlobalConfig.DefaultEncoding
    scena = ED9.Parser.ScenaParser(fs)

    console.setTitle(filename)
    scena.parse()

    py = scena.generatePython(os.path.basename(filename))

    open(output, 'wb').write('\n'.join(py).encode('UTF8'))

def procfile(f: str):
    console.setTitle(os.path.basename(f))

    output = pathlib.Path(f)
    os.makedirs(output.parent / 'py', exist_ok = True)
    output = output.parent / 'py' / (output.stem + '.py')
    # if output.exists(): continue

    test(f, output)

def main():
    scena = [
        r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\\',
        # r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\minigame\dat\\',
        # r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\talk\dat\\',
        r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\battle\dat\\',
        r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\ani\dat\\',
    ]

    output_dir = None
    # output_dir = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\ouroboros\scripts\scena\dat\\'

    for s in scena:
        break
        iterlib.forEachFileMP(procfile, s, '*.dat', subdir = False)
        continue

        for f in fileio.getDirectoryFiles(s, '*.dat', subdir = False):
            console.setTitle(os.path.basename(f))

            output = pathlib.Path(f)
            os.makedirs(output.parent / 'py', exist_ok = True)
            output = output.parent / 'py' / (output.stem + '.py')
            if output.exists(): continue

            test(f, output)

    else:
        return

    path = r'D:\Game\Steam\steamapps\common\THE LEGEND OF HEROES KURO NO KISEKI\decrypted\tc\f\script\scena\system.dat'
    path = r'D:\Game\Steam\steamapps\common\THE LEGEND OF HEROES KURO NO KISEKI\decrypted\tc\f\script\ani\common.dat'

    path = pathlib.Path(path)

    output_dir = r'D:\Dev\Source\Falcom\Decompiler2\Falcom\ED9\\'

    if output_dir:
        output = output_dir + (path.stem + '.py')
    else:
        output = path.stem + '.py'

    test(str(path), output)

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
