from audioop import maxpp
from ml import *

def main():
    path = r'E:\Game\Steam\steamapps\common\Trails in the Sky SC'

    dirTable = {}

    for f in fileio.getDirectoryFiles(path, 'ED6_DT*.dir', subdir = False):
        console.setTitle(f)

        datIndex = os.path.basename(f)
        datIndex = int(datIndex[6:8], 16)

        with open(f, 'rb') as fs:
            if fs.read(8) != b'LB DIR\x1A\x00':
                print(f'{f} invalid magic')
                continue

            count = int.from_bytes(fs.read(4), 'little', signed = False)

            fs.seek(4, io.SEEK_CUR)

            for index in range(count):
                try:
                    name = fs.read(0x10).rstrip(b'\x00').decode()
                except UnicodeDecodeError:
                    print(f'{f} {fs.seek(0, io.SEEK_CUR):X}')
                    continue

                size = int.from_bytes(fs.read(4), 'little', signed = False)
                fs.seek(0xC, io.SEEK_CUR)
                offset = int.from_bytes(fs.read(4), 'little', signed = False)

                if name in ['', '/_______.___']:
                    continue

                dirTable[f'%04X%04X' % (datIndex, index)] = name

    j = json.dumps(dirTable, indent = '  ', ensure_ascii = False)
    open('dirTable.py', 'w', encoding = 'UTF8').write('dirTable = ' + j)

if __name__ == '__main__':
    Try(main)
