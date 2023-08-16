@ECHO OFF
FOR %%i IN (AllocPieces\*.lzma) DO (
	Title %%~nxi
	bin2h.exe "%%~fi"
)
Move /Y AllocPieces\*.h E:\Desktop\Source\ED63Loader\AllocPieces\ >NUL 2>NUL

GOTO:EOF
