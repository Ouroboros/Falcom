from EDAOScenaFile import *
import random, hashlib

SCENA_FLAGS_OFFSET_1    = 0x212


SCENA_FLAGS_BIT_ARIANRHOD   = 0

def GenerateUniqueLable():
    return '%X' % int(random.random() * 100000000000)

def UniqueLabel(LableName):
    sha256 = hashlib.sha256()
    sha256.update(LableName.encode(CODE_PAGE))

    return label(sha256.hexdigest())

def IfScenaFlagOn(offset, bit, default_label):
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(offset, bit)), scpexpr(EXPR_END)), default_label)

def IfScenaFlagOff(offset, bit, default_label):
    on_label = GenerateUniqueLable()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(offset, bit)), scpexpr(EXPR_END)), on_label)
    Jump(default_label)
    label(on_label)

def IfLastBattleLostGoto(lost_label):
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), lost_label)

def CreateMenuAndShow(itemlist, layer = 0, x = -1, y = -1):
    MenuCmd(0, layer)
    for item in itemlist:
        if strlen(item) >= 0x32:
            raise Exception('menu item too long, must be less than 0x32 bytes: %s' % item)

        MenuCmd(1, layer, item)

    MenuCmd(0x2, layer, x, y, 0x1)
    MenuEnd(0x0)
