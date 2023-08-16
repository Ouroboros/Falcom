// ZWEI2Trainer.h : main header file for the ZWEI2TRAINER application
//

#if !defined(AFX_ZWEI2TRAINER_H__3C3E748F_35DD_4C4C_88C0_E05E3D7ED37E__INCLUDED_)
#define AFX_ZWEI2TRAINER_H__3C3E748F_35DD_4C4C_88C0_E05E3D7ED37E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CZWEI2TrainerApp:
// See ZWEI2Trainer.cpp for the implementation of this class
//

class CZWEI2TrainerApp : public CWinApp
{
public:
	CZWEI2TrainerApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CZWEI2TrainerApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CZWEI2TrainerApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_ZWEI2TRAINER_H__3C3E748F_35DD_4C4C_88C0_E05E3D7ED37E__INCLUDED_)
