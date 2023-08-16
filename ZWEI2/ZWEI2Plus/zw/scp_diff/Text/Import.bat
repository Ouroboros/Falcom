:: 将提取的文本写回脚本中。

@FOR %%i in (EV*.txt) DO @(
	Title Importing %%~nxi
	ZWEI2Scp.exe -i "MES_%%~nxi" "%%~nxi"
)