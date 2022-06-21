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
    scena = ED6.Parser.ScenaParser(pathlib.Path(filename).stem.strip(), fs)

    scena.parse()

    # print(scena)

    py = scena.generatePython(os.path.basename(filename))

    open(output, 'wb').write('\n'.join(py).encode('UTF8'))

def procfile(f: str, encoding: str = 'GBK'):
    console.setTitle(os.path.basename(f))

    GlobalConfig.DefaultEncoding = encoding

    output = pathlib.Path(f)
    os.makedirs(output.parent / 'py', exist_ok = True)
    output = output.parent / 'py' / (output.stem.strip() + '.py')
    # if output.exists(): continue

    test(f, output)

def procfile_psv(f: str):
    procfile(f, 'SJIS')

def procfile_cn(f: str):
    procfile(f, 'GBK')

def main():
    scena = [
        # (procfile_cn, r'E:\Game\Steam\steamapps\common\Trails in the Sky FC\DAT\ED6_DT01'),
        (procfile_psv, r'E:\Desktop\falcomtools\PSV EVO\Eiyuu Densetsu - Sora no Kiseki FC Evolution CHS+DLC-3DM\PCSH00179\gamedata\data\scenario\0'),
    ]

    output_dir = None
    # output_dir = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\ouroboros\scripts\scena\dat\\'

    for cb, s in scena:
        # break
        # iterlib.forEachFileMP(cb, s, '*.bin', subdir = False)
        # continue

        for f in fileio.getDirectoryFiles(s, '*.bin', subdir = False):
            console.setTitle(os.path.basename(f))

            output = pathlib.Path(f)
            os.makedirs(output.parent / 'py', exist_ok = True)
            output = output.parent / 'py' / (output.stem.strip() + '.py')
            if output.exists(): continue

            cb(f)

    else:
        return

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
