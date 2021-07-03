@ECHO OFF
CD/D "%~dp0"
For %%i IN (%*) DO ED6DatCreator.exe Patch.dat %%i
For %%i IN (%*) DO J:\Falcom\ED_SORA3\ED6Back.exe Patch.dat %%i
Move Patch.dat J:\Falcom\ED_SORA3
Move Patch.dir J:\Falcom\ED_SORA3