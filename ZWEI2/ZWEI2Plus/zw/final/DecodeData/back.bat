@ECHO OFF
CD/D "%~dp0"

rd/s/q ..\EncodeData\scp >NUL 2>NUL
EncodeItm.exe >NUL 2>NUL
ECHO D|xcopy/s/y ..\EncodeData\scp J:\Falcom\ZWEI2P\DATA\scp >NUL 2>NUL