# Falcom 工具集

包含下列游戏的各种程序

- 英雄传说6 空之轨迹 FC
- 英雄传说6 空之轨迹 SC
- 英雄传说6 空之轨迹 the 3rd
- 英雄传说 零之轨迹
- 英雄传说 碧之轨迹
- 英雄传说 闪之轨迹3
- 双星物语2
- 双星物语2 Plus


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

将空之轨迹 3rd AS 战技脚本，反汇编成 ToB（by <a href="https://github.com/dwing4g" target="_blank">dwing</a>）语言



## <a href="https://github.com/Ouroboros/Falcom/tree/master/tobc" target="_blank">tobc</a>

时间不详

为 ToB（by <a href="https://github.com/dwing4g" target="_blank">dwing</a>）添加新指令
- @_FILE
- @_INCLUDE
- @_MOD
- @_DEFF



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Back" target="_blank">ED6Back</a>

写于 2008 年或更早

实现了空之轨迹三部曲 DAT 的压缩算法

抄自 <a href="https://github.com/prefetchnta" target="_blank">prefetchnta</a> 最早在其 blog 公开的 FALCOM.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Walk" target="_blank">ED6Walk</a>

在 2010 ~ 2014 年之间

把一系列 bmp 转换为空之轨迹三部曲的 ._CH 和 ._CP 动画文件

抄自 <a href="https://github.com/prefetchnta" target="_blank">prefetchnta</a> 最早在其 blog 公开的 EDWalk.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/tga2_ch" target="_blank">tga2_ch</a>

时间不详

把单个 tga 转换为空之轨迹三部曲的 ._CH 文件

抄自 <a href="https://github.com/dwing4g" target="_blank">dwing</a> 的 tga2ch.exe



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

将零之轨迹 AS 战技脚本，反汇编成 ToB（by <a href="https://github.com/dwing4g" target="_blank">dwing</a>）语言



## <a href="https://github.com/Ouroboros/Falcom/tree/master/EDAO" target="_blank">EDAO</a>

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

碧之轨迹集大成编辑工具，支持下列格式与`.py`相互转换
- scena 剧情
- ms*.dat 怪物状态
- as*.dat 战技脚本
- fachr*._bn 场景攻击
- eff 特效
- t_name._dt
- t_dbmon._dt
