from Falcom import ED62
from Falcom.Common import *
from Assembler.instruction import Instruction
from Falcom.ED6.InstructionTable.types import TextObject
import pathlib

from hexdump import hexdump

def exportText(output: str, stringTable: list[str], talkInsts: dict[int, Instruction]):
    text = []

    def parseText(t: list[TextObject]) -> list[str]:
        text = []
        for s in t:
            text.append({
                'code': s.code,
                'value': s.value,
            })

        return text

    for index, offset in enumerate(sorted(talkInsts.keys())):
        inst: Instruction = talkInsts[offset]

        index = len(text) + 1

        match inst.opcode:
            case 0x54:
                text.append({
                    'index'     : index,
                    'offset'    : inst.offset,
                    'type'      : 3,
                    'chrId'     : 255,
                    'chrName'   : '',
                    'msg'       : parseText(inst.operands[0].value),
                })

            case 0x5B:
                text.append({
                    'index'     : index,
                    'offset'    : inst.offset,
                    'type'      : 1,
                    'chrId'     : inst.operands[0].value,
                    'chrName'   : '',
                    'msg'       : parseText(inst.operands[1].value),
                })

            case 0x5C:
                text.append({
                    'index'     : index,
                    'offset'    : inst.offset,
                    'type'      : 2,
                    'chrId'     : inst.operands[0].value,
                    'chrName'   : inst.operands[1].value,
                    'msg'       : parseText(inst.operands[2].value),
                })


            case 0xCC | 0xDE:
                pass

            # case 0x60:
            #     text.append({
            #         'index'     : index,
            #         'offset'    : inst.offset,
            #         'type'      : -1,
            #         'chrId'     : -1,
            #         'chrName'   : inst.operands[0].value,
            #         'msg'       : None,
            #     })

    json.dump({'count': len(text), 'msg': text}, open(output.replace('.py', '.json'), 'w', encoding = 'UTF8'), ensure_ascii = False, indent = '  ')

def importText(output: str, stringTable: list[str], talkInsts: dict[int, Instruction]):
    translation = f'merge\\{os.path.basename(output).rsplit(".", maxsplit = 1)[0]}.json'
    try:
        translation = json.load(open(translation, 'r', encoding = 'UTF8'))
    except FileNotFoundError:
        raise
        return

    try:
        raise FileNotFoundError
        voiceTable = json.load(open(r'D:\Dev\Source\Falcom\ED6Steam\tools\msg\\' + os.path.basename(output).rsplit('.', maxsplit = 1)[0] + '.json', 'r', encoding = 'UTF8'))
        voices = []

        for v in voiceTable:
            for m in v.get('msg', []):
                voices.append(m['voice'])

        if not any(voices):
            return

        count = 0
        for v in talkInsts.values():
            count += v.opcode != 0x60

        if len(voiceTable) != count:
            raise NotImplementedError(f'{os.path.basename(output)} talk count {count} : {len(voiceTable)}')

    except FileNotFoundError:
        voiceTable = None

    def importVoice(msg: dict, t: list[TextObject]):
        if not voiceTable:
            return

        index, chrId = msg['index'], msg['chrId']

        v = voiceTable[index - 1]

        vmsg = v.get('msg', [])

        if not any([m['voice'] for m in vmsg]):
            return

        # if msg['type'] != v['type']:
        #     raise NotImplementedError(f'type mismatch @ {index}: {v["type"]} != {msg["type"]}')

        if v['chrId'] != chrId:
            raise NotImplementedError(f'chrId mismatch @ {index}: {v["chrId"]} != {chrId}')

        size = t.count(TextObject(3)) + 1
        if size != len(vmsg):
            err = f'msg count mismatch @ index = {index}: {size} != {len(vmsg)}'
            print(err)
            # ibp()
            raise NotImplementedError(err)

        idx = 0
        inserted = False
        for i, o in enumerate(t):
            if o.code == 3:
                inserted = False
                continue

            if not inserted and o.code is None:
                # print(vmsg[idx])
                voiceId = vmsg[idx]['voice']
                if voiceId:
                    o.value = f"#{voiceId}v" + o.value

                inserted = True
                idx += 1

    stringTable.clear()
    stringTable.extend(translation['strings'])

    def toTextObjects(msg) -> list[TextObject]:
        return [TextObject(code = m['code'], value = m['value']) for m in msg]

    for msg in translation['msg']:
        inst: Instruction = talkInsts[msg['offset']]

        textList = None
        match inst.opcode:
            case 0x54:
                textList = toTextObjects(msg['msg'])
                inst.operands[0].value = textList

            case 0x5B:
                textList = toTextObjects(msg['msg'])
                inst.operands[1].value = textList

            case 0x5C:
                textList = toTextObjects(msg['msg'])
                inst.operands[1].value = msg['chrName']
                inst.operands[2].value = textList

            case 0x60:
                inst.operands[0].value = msg['chrName']

        if not textList:
            continue

        # importVoice(msg, textList)

def test(filename, output):
    output = str(output)

    if pathlib.Path(filename).stem.strip() in [
            # 'C5313_1',
            # 'E0001',
        ]:
        return

    output_name = pathlib.Path(output).name
    # if os.path.exists(f'tools\\patch\\{output_name}'):
    #     shutil.copy2(f'tools\\patch\\{output_name}', output)
    #     return

    fs = fileio.FileStream().OpenMemory(open(filename, 'rb').read())
    if fs.GetSize() == 0:
        return

    fs.Encoding = GlobalConfig.DefaultEncoding
    scena = ED62.Parser.ScenaParser(pathlib.Path(filename).stem.strip(), fs)

    talkInsts = {}

    def cb(inst: Instruction):
        match inst.opcode:
            case 0x54 | 0x5B | 0x5C | 0x60:
                talkInsts[inst.offset] = inst

    scena.setInstructionCallback(cb)
    scena.parse()

    if talkInsts:
        exportText(output, scena.stringTable, talkInsts)
        # importText(output, scena.stringTable, talkInsts)

    py = scena.generatePython(os.path.basename(filename))

    open(output, 'wb').write('\n'.join(py).encode('UTF8'))

def procfile(f: str, encoding: str = 'GBK'):
    console.setTitle(os.path.basename(f))

    GlobalConfig.DefaultEncoding = encoding

    output = pathlib.Path(f)
    os.makedirs(output.parent / 'py', exist_ok = True)
    output = output.parent / 'py' / (output.stem.strip() + '.py')
    # if output.exists(): continue

    test(f, output)

def procfile_en(f: str):
    procfile(f, 'SJIS')

def procfile_cn(f: str):
    procfile(f, 'GBK')

def main():
    scena = [
        # (procfile_en, r'E:\Game\Steam\steamapps\common\Trails in the Sky SC\ED6_DT21'),
        # (procfile_en, r'E:\Desktop\falcomtools\PSV EVO\Eiyuu Densetsu Sora no Kiseki SC Evolution PCSG00489 (v01.00)\gamedata\data_sc\scenario\1'),
        # (procfile_cn, r'E:\Game\Falcom\ED_SORA2\ED6_DT21'),
        (procfile_cn, r'E:\Game\Steam\steamapps\common\Trails in the Sky SC\DAT\ED6_DT21'),
    ]

    output_dir = None
    # output_dir = r'D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\ouroboros\scripts\scena\dat\\'

    for cb, s in scena:
        # break
        # iterlib.forEachFileMP(cb, s, '*._SN', subdir = False)
        # continue

        for f in fileio.getDirectoryFiles(s, '*._SN', subdir = False):
            # console.setTitle(os.path.basename(f))

            output = pathlib.Path(f)
            os.makedirs(output.parent / 'py', exist_ok = True)
            output = output.parent / 'py' / (output.stem.strip() + '.py')
            # if output.exists(): continue

            cb(f)
            # test(f, output)

    else:
        return

    path = r'D:\Dev\Source\Falcom\Decompiler2\Falcom\ED62\C5308   ._SN'
    path = pathlib.Path(path)

    output_dir = '.\\'

    if output_dir:
        output = output_dir + (path.stem.strip() + '.py')
    else:
        output = (path.parent / 'py') / (path.stem.strip() + '.py')

    test(str(path), output)

    # console.pause('done')

if __name__ == '__main__':
    Try(main)
