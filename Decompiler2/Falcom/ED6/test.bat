@echo off
cd/d "%~dp0"

call Parser\gen_op.py
call test.py
@REM call tbl2py.py "E:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\data_cn\text\dat\t_name.tbl"
pause