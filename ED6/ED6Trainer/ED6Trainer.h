// ED6Trainer.h : main header file for the ED6TRAINER application
//

#if !defined(AFX_ED6TRAINER_H__5254BE2D_8E0A_4B7B_93FA_D3F81B7C0619__INCLUDED_)
#define AFX_ED6TRAINER_H__5254BE2D_8E0A_4B7B_93FA_D3F81B7C0619__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CED6TrainerApp:
// See ED6Trainer.cpp for the implementation of this class
//

class CED6TrainerApp : public CWinApp
{
public:
	CED6TrainerApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CED6TrainerApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CED6TrainerApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_ED6TRAINER_H__5254BE2D_8E0A_4B7B_93FA_D3F81B7C0619__INCLUDED_)
