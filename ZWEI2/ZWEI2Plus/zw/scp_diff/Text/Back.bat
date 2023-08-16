:: 将Tran.txt里所有的文本写入文件（需要先解包）。

@ECHO OFF
Call splitter.bat
Call Copy.bat>NUL
Call import.bat
Del MES_*.*