
#if !defined(AFX_STDAFX_H_)
#define AFX_STDAFX_H_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#define WINVER 0x501
#define VC_EXTRALEAN		// Exclude rarely-used stuff from Windows headers

#define UNICODE
#define _UNICODE
#define WXUSINGDLL

#include <wx/wx.h>
#include <wx/panel.h>
#include <wx/notebook.h>
#include <Psapi.h>
#pragma warning(disable: 4530)

#pragma comment(lib, "Psapi.lib")

#ifndef WXUSINGDLL
#pragma comment(lib, "winmm.lib")
#pragma comment(lib, "comctl32.lib")
#pragma comment(lib, "rpcrt4.lib")
#pragma comment(lib, "wsock32.lib")
#pragma comment(lib, "odbc32.lib")
#endif

#ifdef UNICODE
#pragma comment(lib, "wxmsw29u_core.lib")
#pragma comment(lib, "wxbase29u.lib")
#pragma comment(lib, "wxregexu.lib")
#else
#pragma comment(lib, "wxmsw29_core.lib")
#pragma comment(lib, "wxbase29.lib")
#pragma comment(lib, "wxregex.lib")
#endif	// UNICODE

#endif
