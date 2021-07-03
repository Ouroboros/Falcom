@ECHO OFF
cd/d "%~dp0"

call cl.bat

Set FileList1="Patch\ED6T1938.wav" "Patch\ED6T1939.wav" "BS00039 ._DT" "BS00038 ._DT" "Patch\BS00037 ._DT"
Set FileList2="MS14650 ._DT" "AS00260 ._DT" "MS00260 ._DT" "MS00261 ._DT" "MS00480 ._DT" "MS00481f._DT" "MS04450f._DT" "MS04540f._DT" "T_BTSET1._DT"
Set FileList3="Patch\U7000   ._SN" "Patch\ZTSTATUS._DT" "Patch\TX0117  ._DS" "Patch\TX0118  ._DS" "Patch\TX0119  ._DS" "Patch\TX0120  ._DS"
Set FileList4="Patch\CH20829 ._CH" "Patch\CH20829P._CP" "Patch\CH03477 ._CH" "Patch\CH03477P._CP"
Set FileList=%FileList1% %FileList3% %FileList4%
::call Patch.bat %FileList%
::move /y "E:\Desktop\Source\Hooks\ed63cn\ASDecompiler\debug_BS00039 ._DT" "BS00039 ._DT" 2>NUL
J:\Falcom\ED_SORA3\ED6Back.exe J:\Falcom\ED_SORA3\Patch.dat "BS00039 ._DT"
J:\Falcom\ED_SORA3\ED6Back.exe J:\Falcom\ED_SORA3\Patch.dat "BS00038 ._DT"
J:\Falcom\ED_SORA3\ED6Back.exe J:\Falcom\ED_SORA3\Patch.dat "%~dp0Patch\ED6T1939.wav"
J:\Falcom\ED_SORA3\ED6Back.exe J:\Falcom\ED_SORA3\Patch.dat "%~dp0Patch\ED6T1938.wav"
::for %%i in (%FileList2%) do J:\Falcom\ED_SORA3\ED6Back.exe J:\Falcom\ED_SORA3\Patch.dat "%%~fi"
::J:\Falcom\ED_SORA3\ED6Back.exe J:\Falcom\ED_SORA3\Patch.dat "MS14650 ._DT"
IF  [%1]==[] (
	start "" J:\Falcom\ED_SORA3\ed6_win3_m.exe
) ELSE (
	start "" J:\Falcom\ED_SORA3\Ê±¹ìÎÞ¸ñµ².exe
)