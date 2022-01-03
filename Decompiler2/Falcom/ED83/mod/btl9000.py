import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *

scena = createScenaWriter('btl9000.dat')

# id: 0x0000 offset: 0x9C
@scena.Code('BattleInit')
def BattleInit():
    Return()

# id: 0x0001 offset: 0xA0
@scena.Code('BattleSetting')
def BattleSetting():
    # OP_54(0x3A, 0xF043, 0xFFEB, -1.5, -3.8, 15.0, 0.0, 0x01)
    BattleSetChrAbnormalCondition2(0xF043, AbnormalCondition2.Enhanced, 9, 9, 0)
    BattleSetFlags(0x00000040)
    BattleSetFlags(0x00F00000)
    Return()

# id: 0x0002 offset: 0xB8
@scena.Code('BattleStart')
def BattleStart():
    Return()

@scena.Code('BattleTurn')
def BattleTurn():
    BattleSetChrAbnormalCondition2(0xF043, AbnormalCondition2.Enhanced, 9, 9, 0)
    Return()

# id: 0x0003 offset: 0x1B4
@scena.Code('BattleCheckResult')
def BattleCheckResult():
    Return()

# id: 0x0004 offset: 0x1DC
@scena.Code('BattleRetry')
def BattleRetry():
    Return()


def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
