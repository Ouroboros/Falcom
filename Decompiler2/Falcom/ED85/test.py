from Falcom import ED85
from Falcom.Common import *
import pathlib

from hexdump import hexdump

bypass = set([
    # same with CS3
    'a0106',
    'chr_enemy_template',
    'mon_template',
    'mon000s',
    'mon027_c00',
    'mon037_c00',
    'mon042_c00',
    'mon042_c01',
    'mon046_c00',
    'mon093',
    'npcx00',
    'npcx02',
    'npcx03',
    'npcx04',
    'ply000',
    'ply001',
    'rob013_c00',

    # corrupt
    'chr003_mg16',
    'chr970_c00',
    'mon426',
    'mon462_mg16',
    'rob030',

    # missing terminator entry
    'almon355_c01',
])

def test(filename, output):
    if pathlib.Path(filename).stem in bypass:
        return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    fs.Encoding = GlobalConfig.DefaultEncoding
    scena = ED85.Parser.ScenaParser(fs)

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
        r'E:\Game\Steam\steamapps\common\THE LEGEND OF HEROES HAJIMARI NO KISEKI\data_decrypted\scripts_tc\ani\dat\\',
        r'E:\Game\Steam\steamapps\common\THE LEGEND OF HEROES HAJIMARI NO KISEKI\data_decrypted\scripts_tc\battle\dat\\',
        r'E:\Game\Steam\steamapps\common\THE LEGEND OF HEROES HAJIMARI NO KISEKI\data_decrypted\scripts_tc\scena\dat\\',
        # r'E:\Game\Steam\steamapps\common\THE LEGEND OF HEROES HAJIMARI NO KISEKI\data_decrypted\scripts_tc\talk\dat\\',
        # r'E:\Game\Steam\steamapps\common\THE LEGEND OF HEROES HAJIMARI NO KISEKI\data_decrypted\scripts_tc\minigame\dat\\',
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
            if output.exists(): continue

            test(f, output)

    else:
        return

    scp = [
        'a0000.dat',
        'a0308.dat',
    ][-1]

    path = scena[-1] + scp
    path = r'E:\Game\Steam\steamapps\common\THE LEGEND OF HEROES HAJIMARI NO KISEKI\data_decrypted\scripts_tc\scena\dat\m6040.dat'

    path = pathlib.Path(path)
    os.makedirs(path.parent / 'py', exist_ok = True)

    test(str(path), (path.parent / 'py') / (path.name + '.py'))

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
