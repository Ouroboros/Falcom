from Falcom import ED62
from Falcom.Common import *
import pathlib

def main(filename):
    # GlobalConfig.DefaultEncoding = 'SJIS'
    t_name = ED62.DataTable(filename = filename)
    path = pathlib.Path(filename)
    open(f'{path.parent / path.stem.strip()}.py', 'wb').write('\n'.join(t_name.toPython(path.name)).encode('UTF8'))
    # console.pause('done')

if __name__ == '__main__':
    for i in sys.argv[1:]:
        Try(main, i)
