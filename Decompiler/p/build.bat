@echo off
cd/d "%~dp0"

::for /f %%i in ('dir/s/b sysatk*.py') do %%i
::for /f %%i in ('dir/s/b fachr*.py') do %%i
::for /f %%i in ('dir/s/b as*.py') do %%i
::for /f %%i in ('dir/s/b ms*.py') do %%i

for /f %%i in ('dir/s/b Cassius\?s*.py') do %%i
for /f %%i in ('dir/s/b Cassius\*.eff.py') do %%i
::for /f %%i in ('dir/s/b Arianrhod\?s*.py') do %%i

move /y *._bn D:\Game\Falcom\ED_AO\Ouroboros\system
move /y *._dt D:\Game\Falcom\ED_AO\Ouroboros\text
move /y *.bin D:\Game\Falcom\ED_AO\Ouroboros\scena
move /y *.dat D:\Game\Falcom\ED_AO\Ouroboros\battle\dat
move /y sysatk*.eff D:\Game\Falcom\ED_AO\Ouroboros\effect\eff
move /y *.eff D:\Game\Falcom\ED_AO\Ouroboros\effect\battle

start D:\Game\Falcom\ED_AO\ED_AO_CRACK.exe

