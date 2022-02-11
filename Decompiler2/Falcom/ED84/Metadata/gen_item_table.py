from ml import *

def main():
    from t_item import entries

    nameset = set()
    chrmap = {}
    lines = ['itemIdTable = {']

    for e in entries:
        name = e.name
        i = 1

        nameset.add(name)
        chrmap[name] = e.itemId

    for k, v in chrmap.items():
        lines.append(f'  "{k}": 0x{v:04X},')

    for k, v in chrmap.items():
        lines.append(f'  0x{v:04X}: "{k}",')

    lines.append('}')

    open('itemId_table.py', 'wb').write('\n'.join(lines).encode())


if __name__ == '__main__':
    Try(main)
