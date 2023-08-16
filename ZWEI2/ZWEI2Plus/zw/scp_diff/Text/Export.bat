:: 从解压的脚本里提取文本。
@ECHO OFF
FOR %%i in (EV*.txt) DO (
	Title Exporting %%~nxi
	ZWEI2Scp.exe -o "%%i" "MES_%%~nxi"
	Call:NULLFile "MES_%%~nxi"
)
GOTO:EOF

:NULLFile
IF %~z1==0 Del %1