@ECHO OFF
Set/P GamePath=<Gamepath.ini
FOR /F "tokens=* delims=" %%i IN ('Dir/B/S %GamePath%\DATA\scp\map\EV*.itm') DO (
	Copy %%i ..\Data>NUL 2>NUL
)
..\Data\DecodeItm.exe>NUL
Del ..\Data\EV*.itm
Move ..\DecodeData\EV*.txt .>NUL
Call Export.bat>NUL
Del EV*.txt
Call combine.bat>NUL
Del MES_*.txt