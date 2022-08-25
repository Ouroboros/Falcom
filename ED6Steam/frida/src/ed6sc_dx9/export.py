from ml import *

def main():
    text = []
    text2 = []
    offset = 0x581000 - 0x400000
    for t in json.load(open('ed6sc_text.json', 'r', encoding = 'UTF-8-SIG')):
        translation = t['translation'] or t['original']

        text.append({
            'rva': t['rva'],
            'text': translation.replace('・', '·'),
        })

        # text2.append({
        #     'rva': t['rva'],
        #     'original': t['original'],
        #     'translation': t['translation'] or t['original'],
        # })

    json.dump(text, open('ed6sc.text.json', 'w', encoding = 'UTF8'), ensure_ascii = False, indent = None)
    # json.dump(text2, open('ed6sc_text.json', 'w', encoding = 'UTF8'), ensure_ascii = False, indent = '  ')

if __name__ == '__main__':
    Try(main)
