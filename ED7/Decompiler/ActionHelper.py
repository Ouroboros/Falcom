from BattleActionScript import *
import random
import uuid

def GenerateUniqueLable():
    return uuid.uuid4().hex
    #return '%X' % int(random.random() * 100000000000)

def JumpToLabelIfHasTarget(label_name):
    Jc(0x16, 0x1, 0x0, label_name)

def Random_Execute(Probability, LabelName):
    Jc(0x14, 0x4, Probability, LabelName)

def ChrSetSize(chr, x, z, y):
    AS_8D(0x7, chr, x, z, y)

def ForeachTargetEx(func, reset = True):
    if reset:
        ResetTarget()

    foreach_begin   = GenerateUniqueLable()
    foreach_end     = GenerateUniqueLable()

    label(foreach_begin)

    ForeachTarget(foreach_end)

    func()

    NextTarget()
    Jump(foreach_begin)

    label(foreach_end)

def SetCondition(target, buf, rate, time):
    AS_8D(0x15, target, buf, rate, time)

def ClearCondition(target, buf):
    AS_8D(0x4B, target, buf, buf != CraftConditionFlags.Vanish and -1 or 0, 0)

class _ResourceLock:
    def __enter__(self):
        AS_78(1)

    def __exit__(self, *exc_info):
        AS_78(0)

ResourceLock = _ResourceLock()
del _ResourceLock

def nativeCall(function, param1 = 0, param2 = 0, param3 = 0, param4 = 0):
    AS_8D(function, param1, param2, param3, param4)

def ReiJiMaiGo():
    nativeCall(0x70)

def LoadAvatar(msFile):
    nativeCall(0x71, BattleScriptFileIndex(msFile).Index())
