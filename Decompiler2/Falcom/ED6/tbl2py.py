from Falcom import ED6
from Falcom.Common import *
import pathlib

def main(filename):
    t_name = ED6.DataTable(filename = filename)
    path = pathlib.Path(filename)
    open(f'{path.parent / path.stem}.py', 'wb').write('\n'.join(t_name.toPython(path.name)).encode('UTF8'))
    # console.pause('done')

if __name__ == '__main__':
    for i in sys.argv[1:]:
        Try(main, i)
