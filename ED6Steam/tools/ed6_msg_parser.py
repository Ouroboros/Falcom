from ml import *
import re

def main():
    voiceRegex = re.compile('#[0-9]*V', re.DOTALL)

    for arg in sys.argv[1:]:
        msgs = []

        fs = fileio.FileStream(encoding = 'UTF8')
        fs.Open(arg)

        count = fs.ReadULong()
        indexes = [(fs.ReadULong(), fs.ReadULong()) for _ in range(count)]

        startOffset = fs.Position

        for index, (typ, offset) in enumerate(indexes):
            if typ == 0 and offset == 0:
                break

            fs.Position = offset + startOffset

            assert fs.ReadByte() == 0

            chrId = fs.ReadUShort()
            msg = fs.ReadMultiByte().split('\x03')
            for i, m in enumerate(msg[:-1]):
                msg[i] = m + '\x03'

            msgs.append({
                'index' : index + 1,
                'type'  : typ,
                'chrId' : chrId,
                'msg'   : [{
                    'text'  : m,
                    'voice' : ''.join([v[1:-1] for v in voiceRegex.findall(m)]),
                } for m in msg]
            })

            open(f'{os.path.splitext(arg)[0]}.json', 'wb').write(json.dumps(msgs, ensure_ascii = False, indent = '  ').encode('UTF8'))

if __name__ == '__main__':
    Try(main)
