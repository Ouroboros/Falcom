from ml import *
from Base.BaseType import *

def getname(name):
    filter = \
    [
        (' ', ''),
        ('-', ''),
        ('_', ''),
        ('　', ''),
        ('·', ''),
        ('＋', 'Plus'),
        ('％', ''),
        ('『', '_'),
        ('』', ''),
        ('「', '_'),
        ('」', ''),
        ('！', ''),

        ('①', '1'),
        ('②', '2'),
        ('③', '3'),
        ('④', '4'),
        ('⑤', '5'),
        ('⑥', '6'),
        ('⑦', '7'),
        ('⑧', '8'),
        ('⑨', '9'),
        ('⑩', '10'),
        ('⑾', '11'),
        ('⑿', '12'),
    ]
    for f in filter:
        name = name.replace(f[0], f[1])

    return name

def peek(file):
    fs = fileio.FileStream(file)

    fs.seek(fs.ReadUShort())

    offsetlist = []
    minoffset = 0xFFFFFFFF
    while True:
        if fs.tell() >= minoffset:
            break

        offset = fs.ReadUShort()
        minoffset = min(minoffset, offset)
        offsetlist.append(offset)

    offsetmap = {}
    itemidmap = {}
    itemtruename = {}

    fs.seek(offsetlist[0])
    id = fs.ReadULong() - 1

    for offset in offsetlist:
        #if offset in offsetmap: continue
        #offsetmap[offset] = True

        id += 1

        fs.seek(offset)
        id = fs.ReadULong()

        #if id == 0xCE: bp()

        #if id in itemidmap: bp()

        nameoffset = fs.ReadUShort()
        fs.seek(nameoffset)
        truename = fs.ReadMultiByte()
        name = getname(truename)

        if name == '':
            continue

        itemidmap[id] = name
        itemtruename[id] = truename

    items = []
    for id in sorted(itemidmap):
        if id == 9999:
            continue

        name = itemidmap[id]
        if name[:1].isdigit():
            name = 'Item_' + name

        if name == '':
            name = 'Item_%X' % id

        truename = itemtruename[id]
        if truename == '':
            truename = name

        items.append([id, name, truename])

    return items


def main():
    items = peek('D:\\Game\\Falcom\\ED_AO\\data\\text\\t_ittxt._dt')
    items += peek('D:\\Game\\Falcom\\ED_AO\\data\\text\\t_ittxt2._dt')

    items += [[0xCD, '物理反射', '物理反射'], [0xCE, '魔法反射', '魔法反射']]

    items = sorted(items)

    lines = ['#encoding=utf8']

    lines.append('')
    lines.append('from ml import *')
    lines.append('')

    lines.append('ItemNameMap = {}')
    lines.append('ItemTrueNameMap = {}')
    lines.append('')

    ItemNameMap = {}
    for id, name, truename in items:
        if name not in ItemNameMap:
            ItemNameMap[name] = 0

        ItemNameMap[name] += 1

    for id, name, truename in items:
        namecount = ItemNameMap[name]
        if namecount != 1:
            if name == '':
                name
            name = name + '_%X' % id

        lines.append('ItemNameMap[0x%04X] = "%s"' % (id, name))

    lines.append('')

    for id, name, truename in items:
        lines.append('ItemTrueNameMap[0x%04X] = "%s"' % (id, truename))

    lines.append('')
    lines.append('for id, name in ItemNameMap.items(): exec("%s = 0x%04X" % (name, id))')
    lines.append('')
    lines.append('''for id, name in list(ItemTrueNameMap.items()): exec('ItemTrueNameMap["%s"] = %d' % (name, id))''')
    lines.append('')

    open('ItemNameMap.py', 'wb').write('\r\n'.join(lines).encode('UTF8'))

Try(main)
