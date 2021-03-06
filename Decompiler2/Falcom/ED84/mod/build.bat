@echo off
cd/d "%~dp0"

set "PATCH_PATH=D:\Game\Steam\steamapps\common\The Legend of Heroes Trails of Cold Steel IV\ouroboros"

if "%~f1"=="" goto:START

"%~f1"

set "filename=%~nx1"
set "output=%~dpn1.dat"
set "output_tbl=%~dpn1.tbl"

if /i "%filename:~0,5%" == "alchr" (
    mkdir "%PATCH_PATH%\scripts\battle\dat\" >NUL 2>NUL
    move "%output%" "%PATCH_PATH%\scripts\battle\dat\" >NUL

)  else if /i "%filename:~0,3%" == "btl" (
    mkdir "%PATCH_PATH%\scripts\battle\dat\" >NUL 2>NUL
    move "%output%" "%PATCH_PATH%\scripts\battle\dat\" >NUL

) else if /i "%filename:~0,3%" == "chr" (
    mkdir "%PATCH_PATH%\scripts\ani\dat\" >NUL 2>NUL
    move "%output%" "%PATCH_PATH%\scripts\ani\dat\" >NUL

)  else if /i "%filename:~0,3%" == "rob" (
    mkdir "%PATCH_PATH%\scripts\ani\dat\" >NUL 2>NUL
    move "%output%" "%PATCH_PATH%\scripts\ani\dat\" >NUL

) else if /i "%filename:~0,2%" == "t_" (
    mkdir "%PATCH_PATH%\text\dat\" >NUL 2>NUL
    move "%output_tbl%" "%PATCH_PATH%\text\dat\" >NUL

) else (
    mkdir "%PATCH_PATH%\scripts\scena\dat\" >NUL 2>NUL
    move "%output%" "%PATCH_PATH%\scripts\scena\dat\" >NUL
)

goto:EOF

:START

mkdir "%PATCH_PATH%\asset\D3D11\" >NUL 2>NUL

for %%i in (
    C_CHR550.pkg
    C_CHR551.pkg
    C_CHR552.pkg
) do (
    copy NUL "%PATCH_PATH%\asset\D3D11\%%i" >NUL 2>NUL
)

copy/y config.json5 "%PATCH_PATH%\" >NUL 2>NUL

call ..\Parser\gen_op.py

for %%i in (
    alchr*.py
    t_*.py
    m????.py
    a????.py
    f????.py
    system?.py
    debug.py
    chr???.py
    rob???.py
    btl????.py
) do (
    start /B "" /D "%~dp0" cmd /c " "%~f0" "%%~fi" "
)
