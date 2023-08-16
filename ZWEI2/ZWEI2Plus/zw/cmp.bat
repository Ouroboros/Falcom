@ECHO OFF & SETLOCAL ENABLEDELAYEDEXPANSION
CD/D "%~dp0"

For /R jp %%i In (.\*.*) Do (
	Set n=%%i
	Set n=!n:\jp\=\p\!
	Title %%i
	fc/b "!n!" "%%i" >NUL 2>NUL
	IF "!ERRORLEVEL!"=="0" (
		ECHO !n!>>same.txt
	)
)
Pause