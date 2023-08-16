@echo off
cd/d "%~dp0"

for %%i in (scena\*.bin.py) do %%i

t_name.py
t_dbmon.py

for /f %%i in ('dir/s/b sysatk*.py') do %%i
for /f %%i in ('dir/s/b fachr*.py') do %%i
for /f %%i in ('dir/s/b as*.py') do %%i
for /f %%i in ('dir/s/b ms*.py') do %%i

move /y *._bn D:\Game\Falcom\ED_AO\Ouroboros\system
move /y *._dt D:\Game\Falcom\ED_AO\Ouroboros\text
move /y *.bin D:\Game\Falcom\ED_AO\Ouroboros\scena
move /y *.dat D:\Game\Falcom\ED_AO\Ouroboros\battle\dat
move /y sysatk*.eff D:\Game\Falcom\ED_AO\Ouroboros\effect\eff

rem start D:\Game\Falcom\ED_AO\ED_AO_CRACK.exe
