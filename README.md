# Falcom 工具集

包含下列游戏的各种程序

- 英雄传说6 空之轨迹 FC
- 英雄传说6 空之轨迹 SC
- 英雄传说6 空之轨迹 the 3rd
- 英雄传说 零之轨迹
- 英雄传说 碧之轨迹
- 英雄传说 闪之轨迹3
- 英雄传说 闪之轨迹4
- 双星物语2 Plus


闪之轨迹3
=============

## <a href="https://github.com/Ouroboros/Falcom/tree/master/ed83/frida" target="_blank">ED83 Frida</a>

写于 2021-06-01

闪之轨迹3的增强模块，目前没什么功能



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ed83/loader" target="_blank">ED83 Loader</a>

写于 2021-07-03

就是`frida`的加载器，初始化`frida`，然后附加本进程，加载`js`脚本



## <a href="https://github.com/Ouroboros/Falcom/tree/master/Decompiler2" target="_blank">Decompiler2</a>

2017-06-28 ~ 2021-12-06

第三代反汇编器，目前支持闪之轨迹3

得益于法国老哥的 [SenScriptsDecompiler](https://github.com/TwnKey/SenScriptsDecompiler) ，大大缩短了调试过程

* [闪之轨迹3](https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED83)
  * 2021-11-12 ~ 2021-12-03

* [闪之轨迹4](https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED84)
  * 2021-12-03 ~ 2021-12-06


空之轨迹
=============

## <a href="https://github.com/Ouroboros/Falcom/tree/master/3rd%20Kuro" target="_blank">3rd Kuro</a>

可能写于 2008 年

最古老的第一版 3rd 日文版黑骑士补丁，基于 SC 首个剑帝补丁`Chaltier.exe`仿制而来

使用计时器不停检测远程进程内存，进入战斗后马上用内置的 MS、AS 覆盖



## <a href="https://github.com/Ouroboros/Falcom/tree/master/3rdText" target="_blank">3rdText</a>

可能写于 2008 年

用于处理娱乐通汉化的 3rd 文本编码，所有文本都被编码成`|CAB9|D3C3|B5C0|BEDF`形式的 hex string



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED63Loader" target="_blank">ED63Loader</a>

可能写于 2008 年

用于破解娱乐通汉化的 3rd，原理是把壳解压的代码 dump 下来，CREATE_SUSPEND 后预先写进固定的地址实现脱壳，最早实现来源于贴吧一位 IP 老兄



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ed63cn" target="_blank">ed63cn</a>

在 2008 ~ 2010 年之间

空之轨迹 3rd 日文版汉化增加模块，包含汉化、MOD 增强（使用敌方角色，战技、S技修正）

汉化部分逆向自 <a href="https://github.com/dwing4g" target="_blank">dwing</a> 发布的 3rd 汉化补丁



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ed63cn/ASDecompiler" target="_blank">ED63 ASDecompiler</a>

于 2011-06-01 完成

第一代反汇编器，把空之轨迹 3rd AS 战技脚本，反汇编成 ToB（by <a href="https://github.com/dwing4g" target="_blank">dwing</a>）语言

[有帖为证](https://tieba.baidu.com/p/1096499559)



## <a href="https://github.com/Ouroboros/Falcom/tree/master/tobc" target="_blank">tobc</a>

写于 2011-05

为 ToB（by <a href="https://github.com/dwing4g" target="_blank">dwing</a>）添加新指令
- @_FILE
- @_INCLUDE
- @_MOD
- @_DEFF



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Back" target="_blank">ED6Back</a>

写于 2008 年或更早

实现了空之轨迹三部曲 DAT 的压缩算法

抄自 <a href="https://github.com/prefetchnta" target="_blank">prefetchnta</a> 最早在其 blog 公开的 FALCOM.exe 和 ED6back.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Walk" target="_blank">ED6Walk</a>

在 2010 ~ 2014 年之间

把一系列 bmp 转换为空之轨迹三部曲的 ._CH 和 ._CP 动画文件

抄自 <a href="https://github.com/prefetchnta" target="_blank">prefetchnta</a> 最早在其 blog 公开的 EDWalk.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/tga2_ch" target="_blank">tga2_ch</a>

时间不详

把单个 tga 转换为空之轨迹三部曲的 ._CH 文件

抄自 <a href="https://github.com/dwing4g" target="_blank">dwing</a> 的 tga2_ch.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6DatCreator" target="_blank">ED6DatCreator</a>

写于 2007 ~ 2008 年

代码我也看不懂



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Extract" target="_blank">ED6Extract</a>

时间不详

空之轨迹 DAT 解包器，把 DAT 解压到同名目录



## <a href="https://github.com/Ouroboros/Falcom/tree/master/MS Editor" target="_blank">MS Editor</a>

写于 2011 年之前

基于 MFC 实现的空之轨迹 MS 文件编辑器



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6FC%20Steam" target="_blank">ED6FC Steam</a>

写于 2015-11

空之轨迹 FC Steam 版汉化模块，用 DWrite 实现字符绘制



零之轨迹、碧之轨迹
=============

## <a href="https://github.com/Ouroboros/Falcom/tree/master/EDZero" target="_blank">EDZero</a>

写于 2011-08

零之轨迹破解增强模块，脱了 exe 的 SecuROM 壳，还原了 VM 部分的 freetype 代码

实现了 MOD 基础功能



## <a href="https://github.com/Ouroboros/Falcom/tree/master/EDZero/ASDecompiler" target="_blank">EDZero ASDecompiler</a>

写于 2011-09

第一代反汇编器第二版，将零之轨迹 AS 战技脚本，反汇编成 ToB（by <a href="https://github.com/dwing4g" target="_blank">dwing</a>）语言



## <a href="https://github.com/Ouroboros/Falcom/tree/master/YamaNeko" target="_blank">YamaNeko</a>

写于 2011-09

零、碧之轨迹 itc、itp 解码工具



## <a href="https://github.com/Ouroboros/Falcom/tree/master/EDAO" target="_blank">EDAO</a>

写于 2013-04

碧之轨迹破解模块，整合了 SoundArc 进程，解决声音不同步 bug，实现了 MOD 基础功能

碧轨是最深度修改的版本



## <a href="https://github.com/Ouroboros/Falcom/tree/master/EDAO/RecordViewer" target="_blank">碧之轨迹存档宝箱查看器</a>

写于 2015-07

可以查看所有宝箱取得情况，包含了宝箱的地图和具体坐标(x, y, z)



## <a href="https://github.com/Ouroboros/Falcom/tree/master/Decompiler" target="_blank">Decompiler</a>

写于 2015-07

第二代反汇编器，碧之轨迹集大成编辑工具，支持下列格式与`.py`相互转换
- scena 剧情
- ms*.dat 怪物状态
- as*.dat 战技脚本
- fachr*._bn 场景攻击
- eff 特效
- t_name._dt
- t_dbmon._dt



双星物语2
=============

## <a href="https://github.com/Ouroboros/Falcom/tree/master/ZWEI2" target="_blank">ZWEI2</a>

时间不详

itm 加/解密工具，逆向自游侠论坛的 `jiacat`



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ZWEI2Scp" target="_blank">ZWEI2Scp</a>

时间不详

从 itm 里提取文本的工具



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ZWEI2Plus" target="_blank">ZWEI2Plus</a>

2010-04

双星物语2加强版汉化模块，文本从`双星物语2`提取，文本外挂加密，实时替换

文字绘制类似于 3rd



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ZWEI2Trainer" target="_blank">ZWEI2Trainer</a>

时间不详

双星物语2作弊器，作用不明，看代码功能还挺多



bin
=============

| 原版                          | 描述
|------------------------------|----------
|Chaltier.7z                   | 最早的日文版 SC 1.0.2.0 剑帝补丁，当约修亚在队伍第一时，进入战斗时会替换成剑帝，由 `Leon` 于 2006 ~ 2007年发布在 `FALCOMCHINA`，可以说是本人编程生涯的起点
|ED6back.exe                   | 原版的 ED6back，来自 `prefetchnta` 的 blog
|FALCOM.exe                    | 最早的 ED6 压缩程序，来自 `prefetchnta` 的 blog
|ED6walk.7z                    | 原版的 ED6walk，来自 `prefetchnta` 的 blog
|Loader.exe                    | 最早的 3rd 娱乐通版破解程序，来自空之轨迹吧 IP 老兄
|ed6_win(debug mode).rar       | 娱乐通版 FC，开启了 debug mode，来自 `dwing`
|tga2_ch.7z                    | 原版的 tga2_ch，来自 `dwing`
|ed62.dll                      | 日文版 SC 的汉化模块，来自 `dwing`
|ed63cn2.dll                   | 日文版 3rd 的汉化模块，来自 `dwing`
|ed3rdcn.7z                    | 日文版 3rd 的汉化，来自 `dwing` & `lancer`，里面还包含了`褪色的照片`的剧情翻译
|FinalVersion.7z               | `双星物语2`的汉化文本和加解密、导入程序，由 `jiacat` 发布在游侠论坛上


| 汉化补丁                      | 描述
|------------------------------|----------
|YSF                           | [详见 release](https://github.com/Ouroboros/Falcom/releases/tag/1.0)
|YS6                           |
|YSO                           |
|YS8                           |


其他
=============

## <a href="https://github.com/Ouroboros/Falcom/tree/master/%E6%94%B9%E4%B9%8B%E7%90%86" target="_blank">改之理</a>

时间不详

山寨的`改之理`，只写了一小部分界面



