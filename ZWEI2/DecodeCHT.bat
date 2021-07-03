@ECHO OFF
CD/D "%~dp0"

For %%i In (%*) Do (
	ZWEI2Itm.exe -dy %%i
)