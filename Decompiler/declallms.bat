@echo off

cd/d "%~dp0"

del /q D:\Game\Falcom\ED_AO\data\battle\dat\ms*.py

BattleMonsterStatus.py D:\Game\Falcom\ED_AO\data\battle\dat\
