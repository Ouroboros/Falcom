from Falcom import ED83
from Falcom.Common import *
import pathlib

class NameTableEntry:
    def __init__(self, fs: fileio.FileStream):
        self.tableName  = fs.ReadMultiByte()
        self.entrySize  = fs.ReadUShort()
        self.charId     = fs.ReadUShort()
        self.name       = fs.ReadMultiByte()
        self.C_CHR      = fs.ReadMultiByte()
        self.chr        = fs.ReadMultiByte()
        self.C_CHR_FC   = fs.ReadMultiByte()
        self.FC_CHR     = fs.ReadMultiByte()
        self.name2      = fs.ReadMultiByte()
        self.unknown1   = fs.ReadULong()
        self.unknown2   = fs.ReadULong()
        self.unknown3   = fs.ReadULong()
        self.unknown4   = fs.ReadULong()
        self.unknown5   = fs.ReadUShort()
        self.unknown6   = fs.ReadByte()

    def __str__(self):
        return '\n'.join([
            'NameTableEntry(',
            f'    tableName     = \'{self.tableName}\'',
            # f'    entrySize     = {self.entrySize}',
            f'    charId        = 0x{self.charId:04X}',
            f'    name          = \'{self.name}\'',
            f'    C_CHR         = \'{self.C_CHR}\'',
            f'    chr           = \'{self.chr}\'',
            f'    C_CHR_FC      = \'{self.C_CHR_FC}\'',
            f'    FC_CHR        = \'{self.FC_CHR}\'',
            f'    name2         = \'{self.name2}\'',
            f'    unknown1      = 0x{self.unknown1:08X}',
            f'    unknown2      = 0x{self.unknown2:08X}',
            f'    unknown3      = 0x{self.unknown3:08X}',
            f'    unknown4      = 0x{self.unknown4:08X}',
            f'    unknown5      = 0x{self.unknown5:08X}',
            f'    unknown6      = 0x{self.unknown6:08X}',
            ')',
            '',
        ])

    __repr__ = __str__

class NameTable(ED83.Parser.DataTable):
    def __init__(self, fs):
        super().__init__(fs)
        self.entries = [NameTableEntry(self.data) for _ in range(self.entryCount)]

def main(filename):
    t_name = NameTable(fileio.FileStream(filename, encoding = GlobalConfig.DefaultEncoding))
    # print(t_name.entries)
    open(f'{pathlib.Path(filename).stem}.txt', 'wb').write(str(t_name.entries).encode('UTF8'))

if __name__ == '__main__':
    for i in sys.argv[1:]:
        Try(main, i)
