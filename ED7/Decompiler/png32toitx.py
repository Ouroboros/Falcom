from ml import *
from itp2itc import *
import subprocess

ITPCNV_PATH     = os.path.join(os.path.dirname(__file__), r'tools\itpcnv.exe')
PNGQUANT_PATH   = os.path.join(os.path.dirname(__file__), r'tools\pngquant.exe')
NCONVERT_PATH   = os.path.join(os.path.dirname(__file__), r'tools\nconvert.exe')

PNG_TO_ITP = 0
PNG_TO_ITC = 1

def detectInputType(name):
    parts = name.rsplit('_', 1)
    if len(parts) == 1:
        return PNG_TO_ITP, None

    prefix, seq = parts
    seq = os.path.splitext(seq)[0]
    if not seq.isdigit():
        return PNG_TO_ITP, None

    return PNG_TO_ITC, (prefix, seq)

def replaceExt(input, ext):
    return os.path.splitext(input)[0] + ext

def call(*args):
    p = subprocess.Popen(args, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    p.wait()
    return p

def png2itp(input, output):
    png8 = input + '.8bit.png'
    tmppng8 = png8 + '.tmp'

    for f in [png8, tmppng8]:
        try:
            os.remove(f)
        except FileNotFoundError:
            pass

    p = call(PNGQUANT_PATH, '--force', '256', input, '--output', tmppng8)
    if p.returncode != 0:
        print(p.stderr.read().decode('mbcs').strip())
        raise Exception('convert %s to png8 failed' % input)

    p = call(NCONVERT_PATH, '-quiet', '-o', png8, tmppng8)
    os.remove(tmppng8)
    if p.returncode != 0:
        print(p.stderr.read())
        raise Exception('nconvert %s failed' % input)

    for mode in ['-v6', '-v4', '-v2', '-v0']:
        p = call(ITPCNV_PATH, mode, png8, output)
        if p.returncode == 0 and os.path.exists(output):
            break

        print(p.stdout.read().decode('mbcs'))
        p.returncode = -1

    os.remove(png8)
    if p.returncode != 0:
        raise Exception('convert %s to itp failed with ret code = %X' % (input, p.returncode))

def png2itc(prefix, namelen, output):
    format = '%0{len}d'.format(len = namelen)
    print('%s_%s.itp => %s ...' % (prefix, format, output))

    index = 0
    itc = fileio.FileStream(output, 'wb')
    itc.Position = SIZE_OF_MAGIC + ITC_ENTRY_COUNT * ITC_ENTRY_SIZE + SIZE_OF_SCALE_INFO

    entries = []
    offset = 0

    while True:
        name = (format % index) + '.png'
        name = prefix + '_' + name
        if not os.path.exists(name):
            break

        print('\r%s' % name, end = '')

        tmpitp = name + '.tmp.itp'
        index += 1

        png2itp(name, tmpitp)
        itp = fileio.FileStream(tmpitp, 'rb')

        entry = ItcEntry(itc.Position, itp.Length)
        entries.append(entry)

        itc.Write(itp.Read())
        itp.Close()

        os.remove(tmpitp)

    itc.Position = 0
    itc.Write(b'V101')
    for entry in entries:
        itc.WriteULong(entry.offset)
        itc.WriteULong(entry.size)

    itc.Position = SIZE_OF_MAGIC + ITC_ENTRY_COUNT * ITC_ENTRY_SIZE

    for info in ScaleInfo:
        itc.WriteULong(info)

    print()

def handleFile(name):
    type, extra = detectInputType(name)

    if type == PNG_TO_ITP:
        output = replaceExt(name, '.itp')
        print('%s -> %s ...' % (name, output))
        png2itp(name, output)

    elif type == PNG_TO_ITC:
        prefix, seq = extra
        png2itc(prefix, len(seq), prefix + '.itc')

def main():
    for name in sys.argv[1:]:
        handleFile(os.path.abspath(name))

    console.pause('done')

if __name__ == '__main__':
    Try(main)
