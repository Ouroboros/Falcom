@cd/d "%~dp0"
@rd/s/q __pycache__ >NUL 2>NUL
@for /F "delims=" %%i in ('dir/b/s "%~dp0\__pycache__"') do rd/s/q "%%i" >NUL 2>NUL
