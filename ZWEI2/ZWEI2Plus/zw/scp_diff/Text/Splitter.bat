:: ½«Tran.txt²ð·Ö³ÉMES_*.txt¡£

@ECHO OFF&SETLOCAL ENABLEDELAYEDEXPANSION
CD/D "%~dp0"
FOR /F "tokens=1* delims=" %%i IN (Tran.txt) DO (
	Set Line=%%i
	IF /I NOT "!Line:~0,5!"=="[END]" (
	IF /I "!Line:~0,10!"=="[FILENAME]" (
		Call:GetFileName "!Line!"
	) ELSE (
		ECHO !Line!>>"MES_!File!"
	))
)
GOTO:EOF

:GetFileName
Set/A char=-1
Set File=%1
Set File=!File:"=!
:Loop
FOR %%i IN (%char%) DO IF /I NOT "!File:~%%i,1!"=="\" (
	Set/A char-=1
	GOTO:Loop
) ELSE (
	Set File=!File:~%%i!
	Set File=!File:\=!
)
Set File=!File:~0,-4!.txt
Title Splitting !File!