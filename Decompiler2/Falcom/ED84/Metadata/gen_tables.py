from ml import *

def gen_name_table():
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

def gen_item_table():
    from t_item import entries

    nameset = set()
    chrmap = {}
    lines = ['itemIdTable = {']

    for e in entries:
        name = e.name

        nameset.add(name)
        chrmap[name] = e.itemId

    for k, v in chrmap.items():
        lines.append(f'  "{k}": 0x{v:04X},')

    for k, v in chrmap.items():
        lines.append(f'  0x{v:04X}: "{k}",')

    lines.append('}')

    open('itemId_table.py', 'wb').write('\n'.join(lines).encode())

def gen_craft_table():
    from t_magic import entries

    nameset = set()
    chrmap = {}
    lines = ['craftIdTable = {']

    for e in entries:
        if e.__class__.__name__ != 'MagicTableData':
            continue

        name = e.name
        if name in nameset:
            name = f'{e.name}_{e.id:04X}'

        nameset.add(name)
        chrmap[name] = e.id

    for k, v in chrmap.items():
        lines.append(f'  "{k}": 0x{v:04X},')

    for k, v in chrmap.items():
        lines.append(f'  0x{v:04X}: "{k}",')

    lines.append('}')

    open('craftId_table.py', 'wb').write('\n'.join(lines).encode())

def main():
    for f in [
        gen_name_table,
        gen_item_table,
        gen_craft_table,
    ]:
        try:
            f()
        except ModuleNotFoundError as e:
            pass

if __name__ == '__main__':
    Try(main)
