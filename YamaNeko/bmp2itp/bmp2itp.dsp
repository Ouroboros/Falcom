# Microsoft Developer Studio Project File - Name="bmp2itp" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Console Application" 0x0103

CFG=bmp2itp - Win32 Release
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "bmp2itp.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "bmp2itp.mak" CFG="bmp2itp - Win32 Release"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "bmp2itp - Win32 Release" (based on "Win32 (x86) Console Application")
!MESSAGE "bmp2itp - Win32 bmp2itc" (based on "Win32 (x86) Console Application")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
RSC=rc.exe

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release"
# PROP BASE Intermediate_Dir "Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_CONSOLE" /D "_MBCS" /YX /FD /c
# ADD CPP /nologo /Gr /MD /W4 /GR- /O2 /Ob1 /D "WIN32" /D "NDEBUG" /D USE_NT_VER=1 /FD /GS- /GL /MP /c
# ADD BASE RSC /l 0x409 /d "NDEBUG"
# ADD RSC /l 0x409 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:console /machine:I386
# ADD LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:console /machine:I386 /out:"bmp2itp.exe" /ltcg /fixed
# SUBTRACT LINK32 /pdb:none /debug

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "bmp2itp___Win32_bmp2itc"
# PROP BASE Intermediate_Dir "bmp2itp___Win32_bmp2itc"
# PROP BASE Ignore_Export_Lib 0
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /Gr /MD /W4 /GR- /O2 /Ob1 /D "WIN32" /D "NDEBUG" /D "_CONSOLE" /D "_MBCS" /FD /GS- /GL /MP /c
# ADD CPP /nologo /Gr /MD /W4 /GR- /O2 /Ob1 /D "WIN32" /D "NDEBUG" /D "_CONSOLE" /D "_MBCS" /D "BMP_TO_ITC" /FD /GS- /GL /MP /c
# ADD BASE RSC /l 0x409 /d "NDEBUG"
# ADD RSC /l 0x409 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:console /machine:I386 /out:"bmp2itp.exe" /ltcg /fixed
# SUBTRACT BASE LINK32 /pdb:none /debug
# ADD LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:console /machine:I386 /out:"bmp2itc.exe" /ltcg /fixed
# SUBTRACT LINK32 /pdb:none /debug

!ENDIF 

# Begin Target

# Name "bmp2itp - Win32 Release"
# Name "bmp2itp - Win32 bmp2itc"
# Begin Group "CxImage"

# PROP Default_Filter ""
# Begin Source File

SOURCE=.\CxImage\ximabmp.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximaenc.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximage.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximagif.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximainfo.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximaint.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximalpha.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximalyr.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximapal.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximasel.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximath.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximatran.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\xmemfile.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# End Group
# Begin Source File

SOURCE=.\main.cpp
# End Source File
# Begin Source File

SOURCE=.\Quantize.cpp

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\Quantize.h

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\CxImage\ximacfg.h

!IF  "$(CFG)" == "bmp2itp - Win32 Release"

# PROP Exclude_From_Build 1

!ELSEIF  "$(CFG)" == "bmp2itp - Win32 bmp2itc"

# PROP BASE Exclude_From_Build 1
# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# End Target
# End Project
