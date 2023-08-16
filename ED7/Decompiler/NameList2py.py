from Base.EDAOBase import *

LAST_CHAR_ID            = 0x3E7
NAME_LIST_ENTRY_SIZE    = 0x14

class NameListEntry:

    # size = 0x14
    def __init__(self, fs = None):
        if fs == None:
            return

        self.Id = fs.ReadUShort()

        if self.Id == LAST_CHAR_ID:
            return

        self.NameOffset     = fs.ReadUShort()
        self.WalkChip       = ChipFileIndex(fs.ReadULong())
        self.RunChip        = ChipFileIndex(fs.ReadULong())
        self.BattleScript   = BattleScriptFileIndex(fs.ReadULong())
        self.Unknown_14     = fs.ReadULong()

        pos = fs.tell()
        fs.seek(self.NameOffset)
        self.Name = fs.ReadMultiByte()
        fs.seek(pos)

    def param(self):
        walk = self.WalkChip.Name()
        if not self.WalkChip.IsInvalid(): walk = '"%s"' % walk

        run = self.RunChip.Name()
        if not self.RunChip.IsInvalid(): run = '"%s"' % run

        sym = self.BattleScript.Name()
        if not self.BattleScript.IsInvalid(): sym = '"%s"' % sym

        return '0x%04X, "%s", %s, %s, %s, 0x%08X' % (self.Id, self.Name, walk, run, sym, self.Unknown_14)

    def binary(self):
        return struct.pack('<HHLLLL', self.Id, self.NameOffset, self.WalkChip.Index(), self.RunChip.Index(), self.BattleScript.Index(), self.Unknown_14)

charlist = []

def AddChar(Id, Name, WalkChip, RunChip, BattleScript, Unknown_14):

    entry = NameListEntry()

    entry.NameOffset    = -1

    entry.Id            = Id
    entry.Name          = Name
    entry.WalkChip      = ChipFileIndex(WalkChip)
    entry.RunChip       = ChipFileIndex(RunChip)
    entry.BattleScript  = BattleScriptFileIndex(BattleScript)
    entry.Unknown_14    = Unknown_14

    charlist.append(entry)

def SaveTo(filename):
    fs = open(filename, 'wb+')

    endchar = NameListEntry()
    endchar.Id              = LAST_CHAR_ID
    endchar.Name            = ' '
    endchar.WalkChip        = ChipFileIndex(0)
    endchar.RunChip         = ChipFileIndex(0)
    endchar.BattleScript    = BattleScriptFileIndex(0)
    endchar.Unknown_14      = 0

    charlist.append(endchar)

    offsets = []

    fs.seek(len(charlist) * NAME_LIST_ENTRY_SIZE)

    for entry in charlist:
        entry.NameOffset = fs.tell()
        fs.write(entry.Name.encode(CODE_PAGE) + b'\x00')

    fs.seek(0)
    for entry in charlist:
        fs.write(entry.binary())

def main(filename):
    fs = BytesStream()

    fs.open(filename)

    lines = []
    lines.append('from %s import *' % os.path.splitext(os.path.basename(__file__))[0])
    lines.append('')

    while True:
        entry = NameListEntry(fs)
        if entry.Id == LAST_CHAR_ID:
            break

        lines.append('AddChar(%s)' % entry.param())

    lines.append('')
    lines.append('SaveTo("%s")' % os.path.basename(filename))

    open(os.path.splitext(filename)[0] + '.py', 'wb').write('\r\n'.join(lines).encode('utf_8_sig'))

if __name__ == '__main__':
    for i in sys.argv[1:]:
        Try(main, i)
