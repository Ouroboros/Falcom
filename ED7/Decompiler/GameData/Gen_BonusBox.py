from ml import *
from ItemNameMap import *

scena_path = 'D:\\Game\\Falcom\\ED_AO\\data\\scena\\'

class ItemInfo:
    def __init__(self):
        self.Offset             = 0
        self.Bit                = 0
        self.Item               = ''
        self.Line               = 0
        self.File               = ''

        self.TriggerX           = 0
        self.TriggerZ           = 0
        self.TriggerY           = 0
        self.TriggerRange       = 0
        self.ActorX             = 0
        self.ActorZ             = 0
        self.ActorY             = 0
        self.TalkScenaIndex     = 0
        self.TalkFunctionIndex  = 0


class ScenaInfo:
    def __init__(self):
        self.MapName    = ''
        self.Items      = []


def MakeScenarioFlags(offset, bit):
    return (offset << 3) | (bit & 7)


def getscenaname(file):
    file = os.path.basename(file)
    return file.split('.')[0]

def getparam(line):
    line = line.replace(' ', '')
    index = line.find('(')
    return line[index + 1 : -1].split(',')

def lookupactor(actor, func_index):
    for act in actor:
        TriggerX, TriggerZ, TriggerY, TriggerRange, ActorX, ActorZ, ActorY, Flags, TalkScenaIndex, TalkFunctionIndex, Unknown_22 = act
        TalkFunctionIndex   = int(TalkFunctionIndex)
        TalkScenaIndex      = int(TalkScenaIndex)

        if TalkScenaIndex != 0:
            raise Exception('what the fuck')

        if TalkFunctionIndex == func_index:
            return act

    raise Exception('can not find actor')


def main():
    scena = fileio.getDirectoryFiles(scena_path, '*.py')

    scena_info = {}

    global_flags_map = {}

    for file in scena:
        console.setTitle(file)
        lines = fileio.readLines(file)

        file = getscenaname(file)

        mapname = lines[7].split('# ')[1]
        if mapname == 'MapIndex':
            mapname = file

        info = ScenaInfo()
        scena_info[file] = info

        info.MapName = mapname

        actor       = []
        scenaflags  = None
        func        = []

        current_func = ''
        current_item = ''

        for i in range(len(lines)):
            l = lines[i].strip()

            if l.startswith('DeclActor('):

                p = getparam(l)
                actor.append(p)

            elif l.startswith('"Function_'):

                f = l.split(',')[0][1:-1]
                func.append(f)

            elif l.startswith('def Function_'):

                current_func = l[l.find('Function_'):l.find('(): pass')]

            elif l.startswith('Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags'):

                current_item = ''

            elif l.find('AddItemNumber(') != -1:

                prefix = 'AddItemNumber('
                idx = l.find(prefix)
                item = l[idx + len(prefix):]
                item = item[:item.find(', ')]

                #if not eval('%s in ItemTrueNameMap' % item):
                #    continue
                #current_item = eval('ItemTrueNameMap[%s]' % item)
                current_item = eval(item)

            elif l.startswith('SetScenarioFlags'):

                scenaflags = getparam(l)

            elif l.find('"宝箱里什么') != -1:

                if current_item == '':
                    current_item = '耀晶片'

                TriggerX, TriggerZ, TriggerY, TriggerRange, ActorX, ActorZ, ActorY, Flags, TalkScenaIndex, TalkFunctionIndex, Unknown_22 = lookupactor(actor, func.index(current_func))

                item = ItemInfo()
                item.Offset = int(scenaflags[0], 16)
                item.Bit    = int(scenaflags[1], 10)
                item.Item   = current_item
                item.Line   = i + 1
                item.File   = file

                item.TriggerX           = int(TriggerX)
                item.TriggerZ           = int(TriggerZ)
                item.TriggerY           = int(TriggerY)
                item.TriggerRange       = int(TriggerRange)
                item.ActorX             = int(ActorX)
                item.ActorZ             = int(ActorZ)
                item.ActorY             = int(ActorY)
                item.TalkScenaIndex     = int(TalkScenaIndex)
                item.TalkFunctionIndex  = int(TalkFunctionIndex)


                if not MakeScenarioFlags(item.Offset, item.Bit) in global_flags_map:
                    info.Items.append(item)
                    global_flags_map[MakeScenarioFlags(item.Offset, item.Bit)] = True
                else:
                    print('0x%X, %d, %s: %s' % (item.Offset, item.Bit, mapname, current_item))

                current_item = ''
                scenaflags = None

    items = []

    for file in sorted(scena_info):
        info = scena_info[file]
        for item in info.Items:
            items.append((info, item))

    items = sorted(items, key = lambda item : MakeScenarioFlags(item[1].Offset, item[1].Bit))

    lines = []
    num = 0

    lines.append('[')

    lines.append('    {')
    lines.append('        "SavePath" : "J:\\\\Falcom\\\\ED_AO\\\\savedata"')
    lines.append('    },')
    lines.append('')

    for info, item in items:
        #lines.append('    "item_%X_%d" : {' % (item.Offset, item.Bit))
        lines.append('    {')

        itemid = 'item_%X_%d' % (item.Offset, item.Bit)

        lines.append('        "ID"                  : "%s",'                    % itemid)
        lines.append('        "Map"                 : "%s",'                    % info.MapName)
        lines.append('        "Offset"              : "0x%X",'                  % item.Offset)
        lines.append('        "Bit"                 : %s,'                      % item.Bit)
        lines.append('        "Item"                : "%s",'                    % item.Item)
        lines.append('        "Line"                : %s,'                      % item.Line)
        lines.append('        "File"                : "%s",'                    % item.File)

        lines.append('        "TriggerX"            : %s,'                      % item.TriggerX)
        lines.append('        "TriggerZ"            : %s,'                      % item.TriggerZ)
        lines.append('        "TriggerY"            : %s,'                      % item.TriggerY)
        lines.append('        "TriggerRange"        : %s,'                      % item.TriggerRange)
        lines.append('        "ActorX"              : %s,'                      % item.ActorX)
        lines.append('        "ActorZ"              : %s,'                      % item.ActorZ)
        lines.append('        "ActorY"              : %s,'                      % item.ActorY)
        lines.append('        "TalkScenaIndex"      : %s,'                      % item.TalkScenaIndex)
        lines.append('        "TalkFunctionIndex"   : %s,'                      % item.TalkFunctionIndex)

        lines.append('        "Description"         : "%s",'                    % '')
        lines.append('        "Screenshot"          : "Screenshot\\\\%s.png",'  % itemid)


        lines[-1] = lines[-1][:-1]
        lines.append('    },')
        lines.append('')

    lines.pop(-1)
    lines[-1] = lines[-1][:-1]
    lines.append(']')
    lines.append('')

    #lines.insert(1, '    "NumberOfItems" : %d,\r\n' % len(items))

    open('box.json', 'wb').write('\r\n'.join(lines).encode('U16'))

Try(main)
