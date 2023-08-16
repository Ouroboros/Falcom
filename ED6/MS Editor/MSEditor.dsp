# Microsoft Developer Studio Project File - Name="MSEditor" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Application" 0x0101

CFG=MSEditor - Win32 Release
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "MSEditor.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "MSEditor.mak" CFG="MSEditor - Win32 Release"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "MSEditor - Win32 Release" (based on "Win32 (x86) Application")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
MTL=midl.exe
RSC=rc.exe
# PROP BASE Use_MFC 6
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "Release"
# PROP BASE Intermediate_Dir "Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 6
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MD /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_AFXDLL" /Yu"stdafx.h" /FD /c
# ADD CPP /nologo /Gz /MD /W3 /O1 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_AFXDLL" /Yu"stdafx.h" /FD /GL /GS- /MP /c
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x804 /d "NDEBUG" /d "_AFXDLL"
# ADD RSC /l 0x804 /d "NDEBUG" /d "_AFXDLL"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 /nologo /subsystem:windows /machine:I386
# ADD LINK32 /nologo /subsystem:windows /machine:I386 /out:"MSEditor.exe" /MERGE:.text=.Kaede /SECTION:.Kaede,ERW /MERGE:.data=.Kaede /DYNAMICBASE:NO /MERGE:.rdata=.Kaede /LTCG
# SUBTRACT LINK32 /pdb:none
# Begin Target

# Name "MSEditor - Win32 Release"
# Begin Group "Source Files"

# PROP Default_Filter "cpp;c;cxx;rc;def;r;odl;idl;hpj;bat"
# Begin Source File

SOURCE=.\MSEditor\7zAlloc.c
# SUBTRACT CPP /YX /Yc /Yu
# End Source File
# Begin Source File

SOURCE=.\MSEditor\AIEditor.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\LzmaDec.c
# SUBTRACT CPP /YX /Yc /Yu
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MSEditor.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MSEditorDlg.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MyListCtrl.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MyPropertyPage.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Item.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Risist.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Skill.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Status.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Trophy.cpp
# End Source File
# Begin Source File

SOURCE=.\MSEditor\StdAfx.cpp
# ADD CPP /Yc"stdafx.h"
# End Source File
# End Group
# Begin Group "Header Files"

# PROP Default_Filter "h;hpp;hxx;hm;inl"
# Begin Source File

SOURCE=.\MSEditor\7zAlloc.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\AIEditor.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\ItemName.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\LzmaDec.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MagicName.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MSEditor.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MSEditorDlg.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MSFileStruct.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MyListCtrl.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\MyPropertyPage.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Item.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Risist.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Skill.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Status.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\Page_Trophy.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\resource.h
# End Source File
# Begin Source File

SOURCE=.\MSEditor\StdAfx.h
# End Source File
# End Group
# Begin Group "Resource Files"

# PROP Default_Filter "ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe"
# Begin Source File

SOURCE=.\MSEditor\MSEditor.rc
# End Source File
# Begin Source File

SOURCE=.\MSEditor\res\MSEditor.rc2
# End Source File
# Begin Source File

SOURCE=.\MSEditor\res\XPStyle.manifest
# End Source File
# End Group
# End Target
# End Project
