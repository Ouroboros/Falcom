from Falcom import ED84
from Falcom.Common import *
import pathlib

from hexdump import hexdump

bypass = set([
    # same with CS3
    'a0102',
    'a0104',
    'a0106',
    'a0108',
    'a2050',
    'chr_enemy_template',
    'mon_template',
    'mon000s',
    'mon027_c00',
    'mon037_c00',
    'mon042_c00',
    'mon042_c01',
    'mon046_c00',
    'mon093',
    'npcx03',
    'npcx04',
    'ply000',
    'ply001',
    'rob013_c00',

    # corrupt
    'mon426',
    'rob030',

    # missing terminator entry
    # 'almon355_c00',
    # 'almon355_c01',
])

def test(filename, output):
    if pathlib.Path(filename).stem in bypass:
        return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    fs.Encoding = GlobalConfig.DefaultEncoding
    scena = ED84.Parser.ScenaParser(fs)

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
    scp = [
        'a0000.dat',
        'a0308.dat',
    ][-1]

    scena = [
        r'E:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\data_cn\scripts\ani\dat\\',
        r'E:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\data_cn\scripts\battle\dat\\',
        r'E:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\data_cn\scripts\scena\dat\\',
        # r'E:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\data_cn\scripts\talk\dat\\',
        # r'E:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\data_cn\scripts\minigame\dat\\',
    ]

    for s in scena:
        # break
        iterlib.forEachFileMP(procfile, s, '*.dat', subdir = False)
        continue

        for f in fileio.getDirectoryFiles(s, '*.dat', subdir = False):
            console.setTitle(os.path.basename(f))

            output = pathlib.Path(f)
            os.makedirs(output.parent / 'py', exist_ok = True)
            output = output.parent / 'py' / (output.stem + '.py')
            # if output.exists(): continue

            test(f, output)

    else:
        return

    path = scena[-1] + scp
    path = r'E:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\data_cn\scripts\scena\dat\m6040.dat'
    path = r'a0000汉化调试地图V0.5.dat'

    path = pathlib.Path(path)
    os.makedirs(path.parent / 'py', exist_ok = True)

    test(str(path), (path.parent / 'py') / (path.name + '.py'))

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
