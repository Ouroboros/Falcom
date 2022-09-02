## 支持文件类型

* script\\*.dat


## 脚本分析

本作的指令有了大幅改动

1. 由原来的每条指令都是系统调用, 改为了基于栈的虚拟机, 并且有专门的系统调用指令
2. 函数参数有默认值, 在 `defer` 或者由程序调用时才会用到, 脚本中调用不起作用
3. 全局变量, 变量名有保留, 有专有读写指令
4. 每个函数里的所有函数调用, 都有对应的的调式信息, 但是参数最多保留了4个

```py

g_combo_count       = IntGlobalVar(0, 'combo_count')
g_is_armed          = IntGlobalVar(1, 'is_armed')
g_last_avoid_frame  = IntGlobalVar(2, 'last_avoid_frame')
g_ladder_arm        = IntGlobalVar(3, 'ladder_arm')
g_is_show_weapon    = IntGlobalVar(4, 'is_show_weapon')
g_motion_speed_mem  = IntGlobalVar(5, 'motion_speed_mem')
g_is_play_wait2     = IntGlobalVar(6, 'is_play_wait2')
g_walk_last_x       = IntGlobalVar(7, 'walk_last_x')
g_walk_last_z       = IntGlobalVar(8, 'walk_last_z')

@scena.Code('CommonGetMotionSpeedMem')
def CommonGetMotionSpeedMem():
    DEBUG_SET_LINENO(1059)
    LOAD_GLOBAL(5)
    SET_REG(0)

    RETURN()

@scena.Code('CommonSetMotionSpeedMem')
def CommonSetMotionSpeedMem(arg1: int | float):
    DEBUG_SET_LINENO(1062)
    LOAD_STACK(-4)
    SET_GLOBAL(5)
    DEBUG_SET_LINENO(1063)
    PUSH(0x00000000)
    SET_REG(0)
    POP(4)

    RETURN()
```

参考了 `Binary Ninja` 的 MediumLevelILInstruction, 简单地把栈指令转换成了 MLIL, 输出结果如下

```py
@scena.Code('CommonGetMotionSpeedMem')
def CommonGetMotionSpeedMem():
    var_00 = g_motion_speed_mem.load()
    SetReg(0, var_00)

    Return()

@scena.Code('CommonSetMotionSpeedMem')
def CommonSetMotionSpeedMem(arg1: int | float):
    var_04 = arg1
    g_motion_speed_mem.set(var_04)
    var_04 = 0x00000000
    SetReg(0, var_04)
    del arg1

    Return()
```