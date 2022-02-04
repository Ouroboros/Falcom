from Falcom import ED83
from Falcom.Common import *
import pathlib

from hexdump import hexdump

def test(filename, output):
    if pathlib.Path(filename).stem in [
            'r4400',
            'chr_enemy_template',
            'mon_template',
            'mon000s',
            'mon037_c00',
            'mon042_c00',
            'mon042_c01',
            'mon046_c00',
            'ply000',
            'ply001',
            'rob013_c00',
        ]:
        return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    fs.Encoding = GlobalConfig.DefaultEncoding
    scena = ED83.Parser.ScenaParser(fs)

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
        # break
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

    scp = [
        'a0000.dat',
        'a0308.dat',
    ][-1]

    path = scena[-1] + scp
    # path = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\system.dat'
    path = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\a0000.dat'
    # path = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\m3050.dat'
    # path = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\battle\dat\alchr033.dat'
    # path = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\scena\dat\r0090.dat'
    # path = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\scripts\ani\dat\chr033.dat'

    path = pathlib.Path(path)

    if output_dir:
        output = output_dir + (path.stem + '.py')
    else:
        output = (path.parent / 'py') / (path.stem + '.py')

    test(str(path), output)

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
