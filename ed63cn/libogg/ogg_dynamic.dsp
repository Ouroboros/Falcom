# Microsoft Developer Studio Project File - Name="ogg_dynamic" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Dynamic-Link Library" 0x0102

CFG=ogg_dynamic - Win32 Release
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "ogg_dynamic.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "ogg_dynamic.mak" CFG="ogg_dynamic - Win32 Release"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "ogg_dynamic - Win32 Release" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=cl.exe
MTL=midl.exe
RSC=rc.exe
# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "ogg_dynamic___Win32_Release"
# PROP BASE Intermediate_Dir "ogg_dynamic___Win32_Release"
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "Release"
# PROP Intermediate_Dir "Release"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MT /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "OGG_DYNAMIC_EXPORTS" /YX /FD /c
# ADD CPP /nologo /Gr /MD /W4 /GR- /O2 /Ob1 /I "include" /D "NDEBUG" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /GS- /GL /MP /c
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x409 /d "NDEBUG"
# ADD RSC /l 0x409 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=link.exe
# ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /machine:I386
# ADD LINK32 MyLib.lib ntdll.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /dll /machine:I386 /out:"J:\Falcom\ED_SORA3\d3d8.dll" /NOENTRY /LTCG
# SUBTRACT LINK32 /pdb:none
# Begin Target

# Name "ogg_dynamic - Win32 Release"
# Begin Source File

SOURCE=bitwise.c
# PROP Exclude_From_Build 1
# End Source File
# Begin Source File

SOURCE=.\ed63.cpp
DEP_CPP_ED63_=\
	".\ed63.h"\
	{$(INCLUDE)}"basetsd.h"\
	{$(INCLUDE)}"bugcodes.h"\
	{$(INCLUDE)}"clfslsn.h"\
	{$(INCLUDE)}"CLS\FileBase.h"\
	{$(INCLUDE)}"CLS\Mem.h"\
	{$(INCLUDE)}"CLS\SafeTypes.h"\
	{$(INCLUDE)}"CLS\Vector.hpp"\
	{$(INCLUDE)}"d3d8.h"\
	{$(INCLUDE)}"d3d8caps.h"\
	{$(INCLUDE)}"d3d8types.h"\
	{$(INCLUDE)}"devpropdef.h"\
	{$(INCLUDE)}"dpfilter.h"\
	{$(INCLUDE)}"driverspecs.h"\
	{$(INCLUDE)}"DsfHrmPorts.h"\
	{$(INCLUDE)}"evntprov.h"\
	{$(INCLUDE)}"evntrace.h"\
	{$(INCLUDE)}"FileDisk.h"\
	{$(INCLUDE)}"guiddef.h"\
	{$(INCLUDE)}"hde32.h"\
	{$(INCLUDE)}"ia64reg.h"\
	{$(INCLUDE)}"include\crt_h.h"\
	{$(INCLUDE)}"include\getmainargs.h"\
	{$(INCLUDE)}"include\my_algo.h"\
	{$(INCLUDE)}"include\my_audio.h"\
	{$(INCLUDE)}"include\my_common.h"\
	{$(INCLUDE)}"include\my_conio.h"\
	{$(INCLUDE)}"include\my_crtadd.h"\
	{$(INCLUDE)}"include\my_headers.h"\
	{$(INCLUDE)}"include\my_image.h"\
	{$(INCLUDE)}"include\my_mem.h"\
	{$(INCLUDE)}"include\my_objbase.h"\
	{$(INCLUDE)}"include\my_wintypes.h"\
	{$(INCLUDE)}"include\mylib_init.h"\
	{$(INCLUDE)}"include\nt_defs.h"\
	{$(INCLUDE)}"include\nt_fileio.h"\
	{$(INCLUDE)}"include\nt_status.h"\
	{$(INCLUDE)}"include\undoc_api.h"\
	{$(INCLUDE)}"kernelspecs.h"\
	{$(INCLUDE)}"ktmtypes.h"\
	{$(INCLUDE)}"mce.h"\
	{$(INCLUDE)}"Mem.cpp"\
	{$(INCLUDE)}"my_api.cpp"\
	{$(INCLUDE)}"my_api.h"\
	{$(INCLUDE)}"my_commsrc.h"\
	{$(INCLUDE)}"my_crt.h"\
	{$(INCLUDE)}"my_crtadd.cpp"\
	{$(INCLUDE)}"my_macros.h"\
	{$(INCLUDE)}"my_types.h"\
	{$(INCLUDE)}"MyCPPLib.h"\
	{$(INCLUDE)}"MyString.h"\
	{$(INCLUDE)}"nt_api.h"\
	{$(INCLUDE)}"ntddk.h"\
	{$(INCLUDE)}"ntdef.h"\
	{$(INCLUDE)}"ntifs.h"\
	{$(INCLUDE)}"ntintsafe.h"\
	{$(INCLUDE)}"ntiologc.h"\
	{$(INCLUDE)}"ntnls.h"\
	{$(INCLUDE)}"ntstatus.h"\
	{$(INCLUDE)}"pragma_once.h"\
	{$(INCLUDE)}"sal.h"\
	{$(INCLUDE)}"sal_supp.h"\
	{$(INCLUDE)}"sdkddkver.h"\
	{$(INCLUDE)}"sdv_driverspecs.h"\
	{$(INCLUDE)}"specstrings.h"\
	{$(INCLUDE)}"specstrings_strict.h"\
	{$(INCLUDE)}"specstrings_supp.h"\
	{$(INCLUDE)}"specstrings_undef.h"\
	{$(INCLUDE)}"wdm.h"\
	{$(INCLUDE)}"WindowsSafeTypes.h"\
	
# End Source File
# Begin Source File

SOURCE=.\ed63.def
# End Source File
# Begin Source File

SOURCE=.\ed63.h
# End Source File
# Begin Source File

SOURCE=framing.c
# PROP Exclude_From_Build 1
# End Source File
# Begin Source File

SOURCE=ogg.def
# PROP Exclude_From_Build 1
# End Source File
# Begin Source File

SOURCE=include\ogg\ogg.h
# PROP Exclude_From_Build 1
# End Source File
# Begin Source File

SOURCE=include\ogg\os_types.h
# PROP Exclude_From_Build 1
# End Source File
# End Target
# End Project
