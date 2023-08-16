@ECHO OFF & SETLOCAL ENABLEDELAYEDEXPANSION
CD/D "%~dp0"

Set Exe=E:\Desktop\Source\Hooks\ZWEI2Plus\EncryptText\PeekText\PeekText.exe
Set Out=text_cn.txt
Set Out2=text_jp.txt
Set In=scp_plus
Set In2=scp_plus_jp
del %Out%
del %Out2%

For /r %In% %%i In (.) Do (
	Call:RipDir %%i
)

Goto:Eof

:RipDir
For %%i In (%1\*.txt) Do (
	Title %%~nxi
	Set cn=%%i
	Set jp=!cn:\%In%\=\%In2%\!
	Set cn=!cn:\%In%\=\scp_ywt\!
	%Exe% %%i !cn! NUL %Out%
	%Exe% !jp! !cn! %%i %Out2%
)