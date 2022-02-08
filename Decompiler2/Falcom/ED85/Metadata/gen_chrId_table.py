from ml import *

def main():
    from t_name import entries

    nameset = set()
    chrmap = {}
    lines = ['chrIdTable = {']

    for e in entries:
        if e.chrId == 0xFFFF:
            continue

        name = e.chrName
        i = 1

        while name in nameset:
            i += 1
            name = f'{e.chrName}{i}'

        nameset.add(name)
        chrmap[name] = e.chrId

    for k, v in chrmap.items():
        lines.append(f'  "{k}": 0x{v:04X},')

    for k, v in chrmap.items():
        lines.append(f'  0x{v:04X}: "{k}",')

    lines.append('}')

    open('chrId_table.py', 'wb').write('\n'.join(lines).encode())


if __name__ == '__main__':
    Try(main)
