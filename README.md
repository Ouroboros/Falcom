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

大概在 2008 ~ 2010 年之间

空之轨迹 3rd 日文版汉化增加模块，包含汉化、MOD 增强（使用敌方角色，战技、S技修正）

汉化部分逆向自 <a href="https://github.com/dwing4g" target="_blank">dwing</a> 发布的 3rd 汉化补丁



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Back" target="_blank">ED6Back</a>

写于 2008 年或更早

实现了空之轨迹三部曲 DAT 的压缩算法

抄自 <a href="https://github.com/prefetchnta" target="_blank">prefetchnta</a> 最早在其 blog 公开的 FALCOM.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Walk" target="_blank">ED6Walk</a>

大概在 2010 ~ 2014 年之间

把一系列 bmp 转换为 实现了空之轨迹三部曲 ._CH 和 ._CP 动画文件

抄自 <a href="https://github.com/prefetchnta" target="_blank">prefetchnta</a> 最早在其 blog 公开的 EDWalk.exe



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6DatCreator" target="_blank">ED6DatCreator</a>

写于 2007 ~ 2008 年

代码我也看不懂



## <a href="https://github.com/Ouroboros/Falcom/tree/master/ED6Extract" target="_blank">ED6Extract</a>

时间不详

空之轨迹 DAT 解包器，把 DAT 解压到同名目录

