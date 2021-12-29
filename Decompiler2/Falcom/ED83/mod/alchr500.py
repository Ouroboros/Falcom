import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *

scena = createScenaWriter('alchr500.dat')

# id: 0x0000 offset: 0x4C
@scena.ActionTable('ActionTable')
def ActionTable():
    return ScenaActionTable(
        ScenaActionTableEntry(
            craftId       = 0x3E8,
            type          = 0x01,
            byte03        = 0x00,
            rangeType     = 0x0C,
            rng           = 0x04,
            area          = 0x03,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 15,
            word18        = 0x0001,
            word1A        = 0x0000,
            word1C        = 0x0000,
            word1E        = 0x0000,
            word20        = 0x0000,
            damage        = 100,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 0,
            dword34       = 0,
            dword38       = 0,
            dword3C       = 0,
            dword40       = 0,
            dword44       = 0,
            dword48       = 0,
            dword4C       = 0,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EB',
            action        = 'AniBtlAttack',
            name          = '',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3E9,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x12,
            rng           = 0x14,
            area          = 0x06,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 20,
            word18        = 0x0001,
            word1A        = 0x0016,
            word1C        = 0x0000,
            word1E        = 0x0000,
            word20        = 0x0000,
            damage        = 120,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 100,
            dword34       = 10,
            dword38       = 0,
            dword3C       = 0,
            dword40       = 0,
            dword44       = 0,
            dword48       = 0,
            dword4C       = 0,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EBI',
            action        = 'AniBtlCraft00',
            name          = '疾風穿刺',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3EA,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x1F,
            rng           = 0x64,
            area          = 0x64,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 20,
            word18        = 0x0002,
            word1A        = 0x0019,
            word1C        = 0x000B,
            word1E        = 0x002B,
            word20        = 0x0000,
            damage        = 110,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 100,
            dword34       = 0,
            dword38       = 0,
            dword3C       = 50,
            dword40       = 2,
            dword44       = 0,
            dword48       = 0,
            dword4C       = 0,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EBI',
            action        = 'AniBtlCraft01',
            name          = '大地轟雷錘',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3EB,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x10,
            rng           = 0x01,
            area          = 0x0A,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 20,
            word18        = 0x0001,
            word1A        = 0x001F,
            word1C        = 0x0021,
            word1E        = 0x0022,
            word20        = 0x0000,
            damage        = 120,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 25,
            dword34       = 4,
            dword38       = 0,
            dword3C       = 25,
            dword40       = 4,
            dword44       = 0,
            dword48       = 25,
            dword4C       = 4,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EBI',
            action        = 'AniBtlCraft02',
            name          = '橫掃千軍',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3ED,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x12,
            rng           = 0x14,
            area          = 0x06,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 20,
            word18        = 0x0001,
            word1A        = 0x0016,
            word1C        = 0x0000,
            word1E        = 0x0000,
            word20        = 0x0000,
            damage        = 0,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 100,
            dword34       = 10,
            dword38       = 0,
            dword3C       = 0,
            dword40       = 0,
            dword44       = 0,
            dword48       = 0,
            dword4C       = 0,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EBI',
            action        = 'AniBtlCraft03',
            name          = '奧義·絕影',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3EE,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x0A,
            rng           = 0x01,
            area          = 0x01,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 20,
            word18        = 0x0001,
            word1A        = 0x0013,
            word1C        = 0x0000,
            word1E        = 0x0000,
            word20        = 0x0000,
            damage        = 120,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 20,
            dword34       = 2,
            dword38       = 0,
            dword3C       = 0,
            dword40       = 0,
            dword44       = 0,
            dword48       = 0,
            dword4C       = 0,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EB',
            action        = 'AniBtlCraft04',
            name          = '影技・七柱陣',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3EF,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x0E,
            rng           = 32,
            area          = 6,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 40,
            word18        = 0x0001,
            word1A        = 0x001F,
            word1C        = 0x0021,
            word1E        = 0x0022,
            word20        = 0x0000,
            damage        = 70,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 25,
            dword34       = 4,
            dword38       = 0,
            dword3C       = 25,
            dword40       = 4,
            dword44       = 0,
            dword48       = 25,
            dword4C       = 4,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EBI',
            action        = 'AniBtlCraft05',
            name          = '暴雨疾風槍',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3EC,
            type          = 0x1E,
            byte03        = 0x00,
            rangeType     = 0x0B,
            rng           = 0x01,
            area          = 0x01,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 20,
            word18        = 0x005D,
            word1A        = 0x0064,
            word1C        = 0x0066,
            word1E        = 0x0055,
            word20        = 0x0000,
            damage        = 0,
            dword28       = 5,
            dword2C       = 0,
            dword30       = 10000,
            dword34       = 0,
            dword38       = 0,
            dword3C       = 200,
            dword40       = 0,
            dword44       = 0,
            dword48       = 30,
            dword4C       = 3,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'PMBI',
            action        = 'AniBtlTensionMax',
            name          = '神聖光輝',
        ),
        ScenaActionTableEntry(
            craftId       = 0x3FF,
            type          = 0x1F,
            byte03        = 0x00,
            rangeType     = 0x1F,
            rng           = 0x64,
            area          = 0x64,
            float08       = 45.0,
            float0C       = 100.0,
            float10       = -100.0,
            ariaATDelay   = 0,
            atDelay       = 40,
            word18        = 0x0001,
            word1A        = 0x0000,
            word1C        = 0x0000,
            word1E        = 0x0000,
            word20        = 0x0000,
            damage        = 100,
            dword28       = 0,
            dword2C       = 0,
            dword30       = 0,
            dword34       = 0,
            dword38       = 0,
            dword3C       = 0,
            dword40       = 0,
            dword44       = 0,
            dword48       = 0,
            dword4C       = 0,
            dword50       = 0,
            dword54       = 0,
            dword58       = 0,
            dword5C       = 0,
            cp            = 0,
            flags         = 'EBI',
            action        = 'AniBtlSCraft00',
            name          = '極·奧義·聖技·大十字·改',
        ),
    )

# id: 0x0001 offset: 0x548
@scena.AlgoTable('AlgoTable')
def AlgoTable():
    return ScenaAlgoTable(
        ScenaAlgoTableEntry(
            craftId            = 0x3EF,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
        ScenaAlgoTableEntry(
            craftId            = 0x3E8,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
        ScenaAlgoTableEntry(
            craftId            = 0x3E9,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
        ScenaAlgoTableEntry(
            craftId            = 0x3EA,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
        ScenaAlgoTableEntry(
            craftId            = 0x3EB,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
        ScenaAlgoTableEntry(
            craftId            = 0x3EC,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
        # ScenaAlgoTableEntry(
        #     craftId            = 0x3ED,
        #     aiType             = 0,
        #     probability        = 0,
        #     maxNumOfUses       = 0,
        #     targetType         = 0,
        #     parameters1        = [0, 0, 0],
        #     parameters2        = [0, 0, 0],
        # ),
        # ScenaAlgoTableEntry(
        #     craftId            = 0x3EE,
        #     aiType             = 0,
        #     probability        = 0,
        #     maxNumOfUses       = 0,
        #     targetType         = 0,
        #     parameters1        = [0, 0, 0],
        #     parameters2        = [0, 0, 0],
        # ),
        ScenaAlgoTableEntry(
            craftId            = 0x3FF,
            aiType             = 0,
            probability        = 0,
            maxNumOfUses       = 0,
            targetType         = 0,
            parameters1        = [0, 0, 0],
            parameters2        = [0, 0, 0],
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
