from ml import *

def main():
    en = json.load(open(r'D:\Desktop\Source\Falcom\Decompiler\fc_sn_text_en.json', 'r', encoding = 'utf-8-sig'))
    cn = json.load(open(r'D:\Desktop\Source\Falcom\Decompiler\fc_sn_text_cn.json', 'r', encoding = 'utf-8-sig'))
    opt = json.load(open(r'D:\Desktop\Source\Falcom\Decompiler\replace_option.json', 'r', encoding = 'utf-8-sig'))

    cn2 = {}

    for k, v in cn.items():
        if len(v) == len(en[k]) or k in opt:
            cn2[k] = v
        else:
            print(k.ljust(10), len(v) - len(en[k]))

    open('fc_sn_text_final.json', 'wb').write(json.dumps(cn2, indent = 2, ensure_ascii = False).encode('utf-8-sig'))

if __name__ == '__main__':
    Try(main)
