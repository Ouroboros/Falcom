@ECHO OFF
CD/D "E:\Desktop\cm"
Type NUL>"%~dp0Log.txt"
For %%i IN (ED6_DT21\*.* ED6_DT22\*.* ED6_DT30\*.* J:\Falcom\ED_SORA3\*.* %WinDir%\system32\*.*) DO (
	Title %%i
	"%~dp03rdText.exe" "%%~fi">>"%~dp0Log.txt"
)