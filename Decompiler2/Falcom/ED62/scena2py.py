from Falcom import ED62
from Falcom.Common import *
import pathlib

def importVoice(output, stringTable, talkInsts):
    from Falcom.ED6.InstructionTable.types import TextObject

    try:
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

    if not voiceTable:
        return

    index = -1

    for _, offset in enumerate(sorted(talkInsts.keys())):
        inst = talkInsts[offset]
        textobjs: list = None
        chrId = None

        match inst.opcode:
            case 0x54:
                chrId = 255
                textobjs = inst.operands[0].value

            case 0x5B:
                chrId = inst.operands[0].value
                textobjs = inst.operands[1].value

            case 0x5C:
                chrId = inst.operands[0].value
                textobjs = inst.operands[2].value

        if not textobjs:
            continue

        index += 1

        v = voiceTable[index]

        vmsg = v.get('msg', [])

        if not any([m['voice'] for m in vmsg]):
            return

        # if msg['type'] != v['type']:
        #     raise NotImplementedError(f'type mismatch @ {index + 1}: {v["type"]} != {msg["type"]}')

        if v['chrId'] == 268:
            v['chrId'] = 0x110

        if v['chrId'] != chrId:
            raise NotImplementedError(f'chrId mismatch @ {index + 1}: {v["chrId"]} != {chrId}')

        while textobjs[0].code is not None:
            textobjs.pop(0)

        size = textobjs.count(TextObject(3)) + 1
        if size != len(vmsg):
            err = f'msg count mismatch @ index = {index + 1}: {size} != {len(vmsg)}'
            print(err)
            # ibp()
            raise NotImplementedError(err)

        idx = 0
        inserted = False
        for i, o in enumerate(textobjs):
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

def main(filename):
    scena = ED62.Parser.ScenaParser(pathlib.Path(filename).stem.strip(), fs = fileio.FileStream(filename, encoding = GlobalConfig.DefaultEncoding, endian = GlobalConfig.StructEndian))

    talkInsts = {}

    def cb(inst):
        match inst.opcode:
            case 0x54 | 0x5B | 0x5C | 0x60:
                talkInsts[inst.offset] = inst

    # scena.setInstructionCallback(cb)
    scena.parse()

    path = pathlib.Path(filename)
    output = f'{path.parent / path.stem.strip()}.py'

    if talkInsts:
        from test import exportText
        # exportText(output, scena.stringTable, talkInsts)
        importVoice(output, scena.stringTable, talkInsts)

    open(output, 'wb').write('\n'.join(scena.generatePython(path.name)).encode('UTF8'))
    # console.pause('done')

if __name__ == '__main__':
    for i in sys.argv[1:]:
        Try(main, i)
