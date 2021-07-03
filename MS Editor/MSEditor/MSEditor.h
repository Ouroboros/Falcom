// MSEditor.h : main header file for the MSEDITOR application
//

#if !defined(AFX_MSEDITOR_H__954E5A95_4777_448D_82E7_E0D2FDAEF464__INCLUDED_)
#define AFX_MSEDITOR_H__954E5A95_4777_448D_82E7_E0D2FDAEF464__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CMSEditorApp:
// See MSEditor.cpp for the implementation of this class
//
//#undef _MSC_VER
//#define _MSC_VER 1
class CMSEditorApp : public CWinApp
{
public:
	CMSEditorApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMSEditorApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CMSEditorApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MSEDITOR_H__954E5A95_4777_448D_82E7_E0D2FDAEF464__INCLUDED_)
