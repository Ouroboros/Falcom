from ml import *
import re

emojiTable = dict([(x, f'<{x.hex().upper()}>'.encode('ASCII')) for x in [
        b'\x87\x8A',
        b'\x87\x40',
        b'\x87\x41',
        b'\x87\x42',
        b'\x87\x43',
        b'\x87\x44',
        b'\x87\x55',
        b'\x87\x56',
        b'\x87\x58',
        b'\x87\x59',
        b'\x87\x5B',
        b'\x87\x5D',
        b'\x92\x87',
    ]])

def replaceEmoji(b: bytes) -> bytearray:
    b = bytes(b)
    buf = bytearray()

    index = 0
    while index < len(b):
        if b[index] < 0x80:
            buf.append(b[index])
            index += 1
            continue

        ch = b[index:index + 2]
        buf.extend(emojiTable.get(ch, ch))

        index += 2

    return buf

def readText(fs: fileio.FileStream) -> str:
    buf = bytearray()
    pos = fs.Position
    while True:
        ch = fs.ReadByte()
        if ch == 0:
            break

        if ch >= 0x20:
            buf.append(ch)
            continue

        buf.append(ch)

        match ch:
            case 0x07:
                buf.append(fs.ReadByte())

            case 0x1F:
                buf.extend(f'<item:{fs.Read(2).hex().upper()}>'.encode('ASCII'))

    # print(f'{pos:X} {bytes(buf)}\n')
    return replaceEmoji(buf).decode(fs.Encoding)

voiceRegex = re.compile('#[0-9]*V', re.DOTALL)

def procfile(input: str):
    console.setTitle(os.path.basename(input))

    msgs = []

    output = f'{os.path.splitext(input)[0]}.json'
    # if os.path.exists(output): return

    fs = fileio.FileStream(encoding = 'SJIS')
    fs.Open(input)

    count = fs.ReadULong()
    indexes = [(fs.ReadULong(), fs.ReadULong()) for _ in range(count)]

    startOffset = fs.Position

    for index, (typ, offset) in enumerate(indexes):
        if typ == 0 and offset == 0:
            break

        fs.Position = offset + startOffset

        assert fs.ReadByte() == 0

        chrId = fs.ReadUShort()
        if typ == 2:
            chrName = readText(fs)
        else:
            chrName = ''

        msg = readText(fs).split('\x03')
        for i, m in enumerate(msg[:-1]):
            msg[i] = m + '\x03'

        msgs.append({
            'index' : index + 1,
            'offset': f'{offset + startOffset:X}',
            'type'  : typ,
            'chrId' : chrId,
            'chrName': chrName,
            'msg'   : [{
                'text'  : m,
                'voice' : ''.join([v[1:-1] for v in voiceRegex.findall(m)]),
            } for m in msg]
        })

    data = json.dumps(msgs, ensure_ascii = False, indent = '  ').encode('UTF8')
    open(output, 'wb').write(data)

def main():
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            for f in fileio.getDirectoryFiles(arg, '*.mbin', subdir = False):
                procfile(f)

        else:
            procfile(arg)

if __name__ == '__main__':
    Try(main)
