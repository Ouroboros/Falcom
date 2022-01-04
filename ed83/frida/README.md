## 闪之轨迹 3/4 增强模块

**需要配合 [loader](https://github.com/Ouroboros/Falcom/tree/master/ed83/loader) 使用，[下载](https://github.com/Ouroboros/Falcom/releases/download/1.0/loader.7z)**

目前支持
* 闪之轨迹3 繁体中文版
* 闪之轨迹4 日文版

--------------------

## 闪之轨迹3 繁体中文版

* traceScriptVM: trace 脚本 opcode 执行流程，不包含参数
* hookIoRedirection: 重定向 `data/` 目录下所有文件，优先依次从下列路径读取
  1. `patch/`
  2. `ouroboros/`
  3. `data_cn/`

* hookCharacterModelInit: 修改了一些模型加载逻辑
  * 切换模型时 (ChangeSkin) 会根据模型从 `t_name` 根据 `model` 查找对应的 `face` 和 `ani` 并重新加载
  * asset 映射，比如 `C_CHR500 -> C_CHR033`，方便在 `t_name` 新增一个使用相同人物时，无法与原 chrId 区分

* hookBattle: 进入战斗时，如果人物的模型被替换(chrId >= 0x2000，利用 `BattleStyle` 实现)
  * 不会从 `t_status` 查找 `alchr*.dat`，而是在 `t_name`里根据 `model` 查找
  * 战技不会从 `t_magic` 里读取，而是从 `alchr*.dat` 里读取
  * SBreak 会自动选择 `alchr*.dat` 里最后一个S技

### 如何替换模型

1. 修改
    * [t_name](https://github.com/Ouroboros/Falcom/blob/e674b61cbde691317a1628278dee29ca3bd8cf9e/Decompiler2/Falcom/ED83/mod/t_name.py#L23719)
    * [t_attach](https://github.com/Ouroboros/Falcom/blob/e674b61cbde691317a1628278dee29ca3bd8cf9e/Decompiler2/Falcom/ED83/mod/t_attach.py#L1524)
2. 改脚本
    * [例子](https://github.com/Ouroboros/Falcom/blob/e674b61cbde691317a1628278dee29ca3bd8cf9e/Decompiler2/Falcom/ED83/mod/hack.py#L29)

----------------

## 闪之轨迹4 日文版

* hookIoRedirection: 重定向 `data/` 目录下所有文件，优先依次从下列路径读取
  1. `patch/`
  2. `ouroboros/`
  3. `data_cn/`

* hookCharacterModelInit: 修改了一些模型加载逻辑
  * 创建模型时，会根据模型从 根据 `model` 从 `t_name` 查找对应的 `face` 和 `ani` 加载
  * asset 映射，比如 `C_CHR500 -> C_CHR033`，方便在 `t_name` 新增一个使用相同人物时，无法与原 chrId 区分

### 实例
  * https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED84/mod
