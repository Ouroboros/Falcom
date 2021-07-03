@echo off
cd/d "%~dp0"

rd/s/q small
timeout /t 2 >NUL 2>NUL
md small

for %%i in (ed7*.wav) do (
    "E:\Multimedia\VideoEncoding\ffmpeg_full.exe" -y -i "%%i" -ac 1 -ar 22000 "small\%%~nxi" >NUL 2>NUL
)

del small\*_old.wav
move /y small\*.wav D:\Game\Falcom\ED_AO\Ouroboros\se
rd small