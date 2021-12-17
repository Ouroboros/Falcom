@echo off
cd/d "%~dp0"

set "PATCH_PATH=D:\Game\Steam\steamapps\common\The Legend of Heroes Sen no Kiseki III\ouroboros"

if "%~f1"=="" goto:START

"%~f1"

set "filename=%~nx1"
set "output=%~dpn1.dat"
set "output_tbl=%~dpn1.tbl"

if /i "%filename:~0,5%" == "alchr" (
    move "%output%" "%PATCH_PATH%\scripts\battle\dat\" >NUL

) else if /i "%filename:~0,3%" == "chr" (
    move "%output%" "%PATCH_PATH%\scripts\ani\dat\" >NUL

)  else if /i "%filename:~0,3%" == "rob" (
    rem move "%output%" "%PATCH_PATH%\scripts\ani\dat\" >NUL

) else if /i "%filename:~0,2%" == "t_" (
    move "%output_tbl%" "%PATCH_PATH%\text\dat\" >NUL

) else (
    move "%output%" "%PATCH_PATH%\scripts\scena\dat\" >NUL
)

goto:EOF

:START

call ..\Parser\gen_op.py

for %%i in (
    alchr*.py
    t_*.py
    m????.py
    a????.py
    chr*.py
) do (
    start /B "" /D "%~dp0" cmd /c " "%~f0" "%%~fi" "
)

