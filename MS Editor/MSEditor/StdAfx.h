// stdafx.h : include file for standard system include files,
//  or project specific include files that are used frequently, but
//      are changed infrequently
//

#if !defined(AFX_STDAFX_H__17C63A29_2647_4863_A8A9_1687D000FA7F__INCLUDED_)
#define AFX_STDAFX_H__17C63A29_2647_4863_A8A9_1687D000FA7F__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#if _MSC_VER < 1300 
#define for if (1) for
#endif

#pragma warning(disable:4530)

#define VC_EXTRALEAN		// Exclude rarely-used stuff from Windows headers'

#define MAX_ITEM_INDEX 1550

#include <afxwin.h>         // MFC core and standard components
#include <afxext.h>         // MFC extensions
#include <afxdisp.h>        // MFC Automation classes
#include <afxdtctl.h>		// MFC support for Internet Explorer 4 Common Controls
#ifndef _AFX_NO_AFXCMN_SUPPORT
#include <afxcmn.h>			// MFC support for Windows Common Controls
#endif // _AFX_NO_AFXCMN_SUPPORT

#include "MyLibrary.h"

#define bswap(x) __asm mov eax, x \
                 __asm bswap eax \
				 __asm mov x, eax


//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_STDAFX_H__17C63A29_2647_4863_A8A9_1687D000FA7F__INCLUDED_)
