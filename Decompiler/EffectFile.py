from ml import *
from Base.EDAOBase import *
import xmltodict

CODE_PAGE = '932'
partDataCount = 16
NameByteArray = BYTE * 16
MagicByteArray = BYTE * 4

class EDAOEffFileHeader(Structure):
    _fields_ = [
        ('Magic',           MagicByteArray),    #  0x0000
        ('Name',            NameByteArray),     #  0x0004
        ('Unknown',         USHORT),            #  0x0014
        ('Padding',         USHORT),            #  0x0016
        ('Flags',           USHORT),            #  0x0018
        ('PartDataBits',    USHORT),            #  0x001A
        ('Texture',         NameByteArray * 4), #  0x001C
        ('Children',        NameByteArray * 2), #  0x005C
    ]
    # PartData        [16][]EDAOPartData  #  0x007C


class EffCoord(Structure):
    _fields_ = [
        ('X',   FLOAT),
        ('Y',   FLOAT),
        ('Z',   FLOAT),
    ]

    def serialize(self):
        return '%s, %s, %s' % (self.X, self.Y, self.Z)
        return OrderedDict([
            ('@X', str(self.X)),
            ('@Y', str(self.Y)),
            ('@Z', str(self.Z)),
        ])

    def unserialize(self, data):
        data = data.split(',')
        self.X = FLOAT(float(data[0].strip()))
        self.Y = FLOAT(float(data[1].strip()))
        self.Z = FLOAT(float(data[2].strip()))
        return self

class PartDataFlags:
    NoTextureName   = 0x00000001
    BlendMode1      = 0x00000002
    BlendMode2      = 0x00000004
    BlendMode3      = 0x00000040
    Culling1        = 0x00000800
    Culling2        = 0x00008000

class EDAOPartData(Structure):                  # 0x03B8 bytes
    class _Header(Structure):                   # 0x0050 bytes
        _fields_ = [
            ('Name',            NameByteArray), # 0x0000
            ('Index',           BYTE),          # 0x0010
            ('Byte_11',         BYTE),          # 0x0011
            ('ExtraCount',      BYTE),          # 0x0012
            ('Byte_13',         BYTE),          # 0x0013
            ('Flags',           ULONG),         # 0x0014
            ('Flags2',          ULONG),         # 0x0018
            ('Float_1C',        FLOAT),         # 0x001C
            ('Byte_1C',         BYTE * 0x1C),   # 0x0020
            ('Byte_3C',         BYTE),          # 0x003C
            ('Byte_3D',         BYTE),          # 0x003D
            ('TextureIndex',    BYTE),          # 0x003E
            ('Byte_3F',         BYTE),          # 0x003F
            ('Byte_40',         BYTE),          # 0x0040
            ('Byte_41',         BYTE),          # 0x0041
            ('Byte_42',         BYTE),          # 0x0042
            ('Byte_43',         BYTE),          # 0x0043
            ('Coord_44',        EffCoord),      # 0x0044
        ]

    class _Struct_3A4(Structure):
        _fields_ = [
            ('Ushort_3A4',      USHORT),        # 0x03A4
            ('Ushort_3A6',      USHORT),        # 0x03A6
            ('Uint_3A8',        ULONG),         # 0x03A8
            ('Uint_3AC',        ULONG),         # 0x03AC
            ('Uint_3B0',        ULONG),         # 0x03B0
            ('Uint_3B4',        ULONG),         # 0x03B4
        ]

    _fields_ = [
        ('Header',              _Header),       # 0x0000
        ('Coord_50',            EffCoord),      # 0x0050
        ('Coord_5C',            EffCoord),      # 0x005C
        ('Float_68',            FLOAT),         # 0x0068
        ('Float_6C',            FLOAT),         # 0x006C
        ('TexturePrecision',    FLOAT),         # 0x0070
        ('Float_74',            FLOAT),         # 0x0074
        ('Uint_78',             ULONG),         # 0x0078
        ('Float_7C',            FLOAT),         # 0x007C
        ('Float_80',            FLOAT),         # 0x0080
        ('Float_84',            FLOAT),         # 0x0084
        ('Float_88',            FLOAT),         # 0x0088
        ('Float_8C',            FLOAT),         # 0x008C
        ('Float_90',            FLOAT),         # 0x0090
        ('HitDistance',         FLOAT),         # 0x0094
        ('Float_98',            FLOAT),         # 0x0098
        ('Uint_9C',             ULONG),         # 0x009C
        ('Uint_A0',             ULONG),         # 0x00A0
        ('Coord_A4',            EffCoord),      # 0x00A4
        ('Coord_B0',            EffCoord),      # 0x00B0
        ('Coord_BC',            EffCoord),      # 0x00BC
        ('Ushort_C8',           USHORT),        # 0x00C8
        ('Ushort_CA',           USHORT),        # 0x00CA
        ('Ushort_CC',           USHORT),        # 0x00CC
        ('Ushort_CE',           USHORT),        # 0x00CE
        ('Sound',               USHORT),        # 0x00D0
        ('Ushort_D2',           USHORT),        # 0x00D2
        ('Uint_D4',             ULONG),         # 0x00D4
        ('Uint_D8',             ULONG),         # 0x00D8
        ('Float_DC',            FLOAT * 36),    # 0x00DC
        ('Float_16C',           FLOAT * 36),    # 0x016C
        ('Float_1FC',           FLOAT * 36),    # 0x01FC
        ('Float_28C',           FLOAT * 36),    # 0x028C
        ('Uint_31C',            ULONG * 16),    # 0x031C
        ('Uint_35C',            ULONG * 16),    # 0x035C
        ('Options',             BYTE * 8),      # 0x039C
        ('Struct_3A4',          _Struct_3A4),   # 0x039C

        # EDAOPartDataExtra[Header.ExtraCount]
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra = []     # EDAOPartDataExtra

class EDAOPartDataExtra(Structure):
    _fields_ = [
        ('Byte_00',     BYTE),
        ('PartIndex',   BYTE),
        ('Repeat',      BYTE),
        ('SpiritCount', BYTE),
        ('Uint_04',     ULONG),
        ('StartTime',   FLOAT),
        ('Interval',    EffCoord),
    ]

def bytesToString(b):
    return bytes(b).split(b'\x00', 1)[0].decode(CODE_PAGE)

def stringToBytes(s, typ):
    return typ.from_buffer_copy((s or '').encode(CODE_PAGE).ljust(ctypes.sizeof(typ), b'\x00'))

def stringToInt(s):
    return eval(s)
    return int(s, s.lower().startswith('0x') and 16 or 10)

def stringToFloat(s):
    return float(s) if s.lower() != 'nan' else struct.unpack('f', b'\xff\xff\xff\xff')[0]

def serializeStructure(obj):
    if hasattr(obj, 'serialize'):
        return obj.serialize()

    p = OrderedDict()
    for name, typ in obj._fields_:
        value = getattr(obj, name)

        if isinstance(value, Structure):
            p[name] = serializeStructure(value)

        elif not isinstance(value, ctypes.Array):
            if isinstance(value, int):
                value = '0x%X' % value

            p[name] = value

        else:
            if typ in (MagicByteArray, NameByteArray):
                p[name] = bytesToString(value)

            elif isinstance(value[0], NameByteArray):
                p[name] = [bytesToString(v) for v in value]

            else:
                p[name] = ', '.join([str(v) for v in value])

    return p

def unserializeStructure(obj, data):
    if hasattr(obj, 'unserialize'):
        obj.unserialize(data)
        return

    for name, typ in obj._fields_:
        value = getattr(obj, name)

        if isinstance(value, Structure):
            unserializeStructure(value, data[name])

        elif not isinstance(value, ctypes.Array):
            if typ is FLOAT:
                value = stringToFloat(data[name])
            else:
                i = data[name]
                value = stringToInt(i)

            setattr(obj, name, typ(value))

        else:
            if typ in (MagicByteArray, NameByteArray):
                setattr(obj, name, stringToBytes(data[name], typ))

            elif isinstance(value[0], NameByteArray):
                names = data[name]
                for i in range(min(len(value), len(names))):
                    value[i] = stringToBytes(names[i], NameByteArray)

            else:
                values = data[name].split(',')
                typ = type(value[0])
                for i, v in enumerate(values):
                    v = v.strip()
                    value[i] = stringToFloat(v) if typ is float else stringToInt(v)

def generateEff(xml):
    eff = EDAOEffectFile()
    eff.loadAndSave(xml)

class EDAOEffectFile:
    def __init__(self):
        self.header = EDAOEffFileHeader()
        self.partData = [None for _ in range(partDataCount)]
        self.name = ''

    @property
    def magic(self):
        return bytesToString(self.header.Magic)

    @property
    def partDataBits(self):
        return self.header.PartDataBits

    @property
    def textures(self):
        return [bytesToString(t) for t in self.header.Texture]

    @property
    def children(self):
        return [bytesToString(c) for c in self.header.Children]

    def open(self, efffile):
        fs = fileio.FileStream(efffile)
        self.header = EDAOEffFileHeader(fs)
        self.name = os.path.basename(efffile)

        for i in range(partDataCount):
            if ((1 << i) & self.partDataBits) == 0:
                continue

            part = EDAOPartData(fs)
            self.partData[i] = part

            for i in range(part.Header.ExtraCount):
                part.extra.append(EDAOPartDataExtra(fs))

    def saveTo(self, fileName):
        xml    = OrderedDict()
        root   = OrderedDict()
        parts  = []

        xml['eff'] = root
        root['FileName'] = self.name
        root['header'] = serializeStructure(self.header)
        root['parts'] = {'part': parts}

        for index, part in enumerate(self.partData):
            if not part:
                parts.append({'@index': '%X' % index})
                continue

            p = serializeStructure(part)
            if part.extra:
                p['extraData'] = {
                    'extra': [serializeStructure(e) for e in part.extra],
                }

                for e in p['extraData']['extra']:
                    part = self.partData[int(e['PartIndex'], 16)]
                    if part:
                        e['@name'] = bytesToString(part.Header.Name)

            p['@index'] = '%X' % index
            parts.append(p)

        xml = xmltodict.unparse(xml, pretty = True, indent = '  ').splitlines()
        xml.insert(0, "xml = '''\\")
        xml.append("'''")

        module = os.path.splitext(os.path.basename(__file__))[0]
        xml.extend([
            '',
            'def main():',
            '    generateEff(xml)',
            '',
            "if __name__ == '__main__':",
            '    from %s import *' % module,
            "    Try(main)",
            "",
        ])

        open(fileName, 'wb').write('\r\n'.join(xml).encode('utf8'))

    def loadAndSave(self, xml):
        xml = xmltodict.parse(xml)
        root = xml['eff']
        self.name = root['FileName']
        parts = root['parts']['part']

        unserializeStructure(self.header, root['header'])
        for i in range(len(self.partData)):
            if ((1 << i) & self.partDataBits) == 0:
                continue

            part = EDAOPartData()
            self.partData[i] = part
            unserializeStructure(part, parts[i])


            try:
                extra = parts[i]['extraData']['extra']
            except (KeyError, TypeError):
                part.Header.ExtraCount = 0
                continue

            if not isinstance(extra, (list, tuple)):
                extra = [extra]

            part.Header.ExtraCount = len(extra)
            for i in range(len(extra)):
                e = EDAOPartDataExtra()
                unserializeStructure(e, extra[i])
                part.extra.append(e)

        fs = fileio.FileStream(self.name, 'wb')
        fs.Write(bytes(self.header))

        for part in self.partData:
            if not part:
                continue

            fs.Write(bytes(part))
            for e in part.extra:
                fs.Write(bytes(e))

def procfile(file):
    print('processing %s' % file)
    ms = EDAOEffectFile()
    ms.open(file)
    ms.saveTo(file + '.py')

if __name__ == '__main__':
    iterlib.forEachFile(procfile, sys.argv[1:], '*.eff')
