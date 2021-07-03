@echo off
cd/d "%~dp0"

for %%i in (%*) do (
	Title %%~nxi
	Encoder.exe "%%~fi" "%%~dpni.lzma"
)