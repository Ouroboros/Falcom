from Falcom import ED6
from Falcom.Common import *
import pathlib

def main(filename):
    scena = ED6.Parser.ScenaParser(fs = fileio.FileStream(filename, encoding = GlobalConfig.DefaultEncoding, endian = GlobalConfig.StructEndian))
    scena.parse()
    path = pathlib.Path(filename)
    open(f'{path.parent / path.stem}.py', 'wb').write('\n'.join(scena.generatePython(path.name)).encode('UTF8'))
    # console.pause('done')

if __name__ == '__main__':
    for i in sys.argv[1:]:
        Try(main, i)
