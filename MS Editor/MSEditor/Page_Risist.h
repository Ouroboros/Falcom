#if !defined(AFX_PAGE_RISIST_H__72C59F6E_9A68_4D44_8D5A_FDCC8F9B49A2__INCLUDED_)
#define AFX_PAGE_RISIST_H__72C59F6E_9A68_4D44_8D5A_FDCC8F9B49A2__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Page_Risist.h : header file
//
#include "MyPropertyPage.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Risist dialog

class CPage_Risist : public CMyPropertyPage
{
	DECLARE_DYNCREATE(CPage_Risist)

// Construction
public:
	CPage_Risist(LPMSFileInfo pMsFileInfo = NULL, PBYTE *ppbFile = NULL, const WORD IDD = 0);

protected:
	bool m_bInput;

protected:
	virtual void Display();

// Dialog Data
	//{{AFX_DATA(CPage_Risist)
		// NOTE - ClassWizard will add data members here.
		enum { IDD = IDD_PAGE_RISIST };
	//}}AFX_DATA


// Overrides
	// ClassWizard generate virtual function overrides
	//{{AFX_VIRTUAL(CPage_Risist)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CPage_Risist)
	afx_msg void OnRisistSelall();
	afx_msg void OnRisistSelnone();
	afx_msg void OnRisistCustom();
	afx_msg void OnRisistReset();
	//}}AFX_MSG
	afx_msg BOOL OnSetRisist(UINT nID);
	DECLARE_MESSAGE_MAP()

};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PAGE_RISIST_H__72C59F6E_9A68_4D44_8D5A_FDCC8F9B49A2__INCLUDED_)
