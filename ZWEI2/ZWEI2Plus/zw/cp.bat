@ECHO OFF
CD/D "%~dp0"

For /F "delims=" %%i in (diff.txt) Do (
	ECHO %%i
	copy/y "%%i" ".\scp_diff\%%i" 2>NUL
)
pause