@ECHO OFF&SETLOCAL ENABLEDELAYEDEXPANSION
Del MES_*.txt>NUL 2>NUL
Set/P GamePath=<Gamepath.ini
FOR /F "tokens=* delims=" %%i IN ('Dir/B/S %GamePath%\DATA\scp\map\EV*.itm') DO (
	Copy %%i ..\Data>NUL 2>NUL
)
..\Data\DecodeItm.exe>NUL
Del ..\Data\EV*.itm
Move ..\DecodeData\EV*.txt .>NUL
Call splitter.bat>NUL
Call Import.bat>NUL
MD ..\Temp
Move ..\DecodeData\*.txt ..\Temp>NUL
Move EV*.txt ..\DecodeData>NUL
..\DecodeData\EncodeItm.exe>NUL
Del ..\DecodeData\*.txt
Move ..\Temp\*.txt ..\DecodeData>NUL
RD ..\Temp
Del MES_*.txt>NUL 2>NUL
CD/D ..\EncodeData
FOR %%i IN (EV*.itm) DO (
	Set File=%%i
	Set Folder=%GamePath%\DATA\scp\map\!File:~2,1!
	ECHO Move %%i !Folder!>>dir.txt
	Move %%i !Folder!>NUL 2>NUL
)