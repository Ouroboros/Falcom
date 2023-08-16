@echo off
cd/d "%~dp0"

E:\Desktop\Captures\ffmpeg.exe -y -i "%~f1" "%~dpn1.wav"
