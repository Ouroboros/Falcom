from Falcom import ED6
from Falcom.Common import *
import pathlib

from hexdump import hexdump

def test(filename, output):
    if pathlib.Path(filename).stem in [
        ]:
        return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    fs.Encoding = GlobalConfig.DefaultEncoding
    scena = ED6.Parser.ScenaParser(fs)

    scena.parse()

    # print(scena)

    py = scena.generatePython(os.path.basename(filename))

    open(output, 'wb').write('\n'.join(py).encode('UTF8'))

def procfile(f: str):
    console.setTitle(os.path.basename(f))

    output = pathlib.Path(f)
    os.makedirs(output.parent / 'py', exist_ok = True)
    output = output.parent / 'py' / (output.stem.strip() + '.py')
    # if output.exists(): continue

    test(f, output)

def main():
    scena = [
        r'E:\Game\Steam\steamapps\common\Trails in the Sky FC\DAT\ED6_DT01',
    ]

    output_dir = None
    # output_dir = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\ouroboros\scripts\scena\dat\\'

    for s in scena:
        # break
        iterlib.forEachFileMP(procfile, s, '*._SN', subdir = False)
        continue

        for f in fileio.getDirectoryFiles(s, '*._SN', subdir = False):
            console.setTitle(os.path.basename(f))

            output = pathlib.Path(f)
            os.makedirs(output.parent / 'py', exist_ok = True)
            output = output.parent / 'py' / (output.stem.strip() + '.py')
            if output.exists(): continue

            test(f, output)

    else:
        return

    scp = [
        'a0000.dat',
        'a0308.dat',
    ][-1]

    path = r'E:\Game\Steam\steamapps\common\Trails in the Sky FC\DAT\ED6_DT01\T0001   ._SN'
    path = pathlib.Path(path)

    output_dir = '.\\'

    if output_dir:
        output = output_dir + (path.stem.strip() + '.py')
    else:
        output = (path.parent / 'py') / (path.stem.strip() + '.py')

    test(str(path), output)

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
