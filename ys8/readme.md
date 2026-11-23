|ys8.js|ys8_1.js|ys8_2.js|
|-|-|-|
|原版汉化.js|禁用CreateFile 和 CheckDLC 两个 Hook|只禁用CreateFile|
|似乎与自定义dlc服装mod并不兼容|与自定义dlc服装mod兼容，游戏内汉化文本正常且过剧情没崩溃|游戏内汉化文本正常，但过剧情之后的载入阶段崩溃|

测试较少，刚弄完没推多少剧情\
我是先装的自定义dlc服装mod，并且按照相应要求（使用十六进制编辑器比如[WerWolv / ImHex](https://github.com/WerWolv/ImHex)对ys8.exr替换 `0F 84 B8 00 00 00 89 5C` to `90 90 90 90 90 90 89 5C`）直接解锁了dlc

如果想同时用汉化mod和自定义dlc服装mod并出现游戏崩溃或异常建议尝试ys8_1.js（改名替换），其后ys8_2.js

另外在装汉化mod之前如果使用过[Ys VIII Save Editor](https://www.nexusmods.com/ysviii/mods/7) 进行某些修改（上次玩ys8还是一年多前所以不记得了）叠加上面某一者或者两者，会有各种bug（虽然其实我也不太确定是不是它的问题）：
- 没有汉化mod 的状态下：特定存档出现dlc自定义服装明明未领取但是全部都是已领取的状态，故无法领取与无法生效
- 还表现为载入某些存档时直接崩溃闪退
- ...

存档问题可通过[下载正常存档](https://home.gamer.com.tw/artwork.php?sn=4259147)解决

音量有问题的重装DirectX End-User Runtimes：
https://www.microsoft.com/en-us/download/details.aspx?id=8109
