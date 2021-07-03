#if !defined(AFX_PAGE_TROPHY_H__C213D1D8_A0FA_484B_B8FB_A420B54B09A9__INCLUDED_)
#define AFX_PAGE_TROPHY_H__C213D1D8_A0FA_484B_B8FB_A420B54B09A9__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Page_Trophy.h : header file
//
#include "MyPropertyPage.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Trophy dialog

class CPage_Trophy : public CMyPropertyPage
{
	DECLARE_DYNCREATE(CPage_Trophy)

// Construction
public:
	CPage_Trophy(LPMSFileInfo pMsFileInfo = NULL, PBYTE *ppbFile = NULL, const WORD IDD = 0);

// Dialog Data
	//{{AFX_DATA(CPage_Trophy)
	//}}AFX_DATA


// Overrides
	// ClassWizard generate virtual function overrides
	//{{AFX_VIRTUAL(CPage_Trophy)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL
	virtual void Display();
	virtual BOOL OnInitDialog();

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CPage_Trophy)
	//}}AFX_MSG
	afx_msg void OnDeltaposTrophySepith(UINT nID, NMHDR* pNMHDR, LRESULT* pResult);
	afx_msg void OnEditTrophySepith(UINT nID);
	DECLARE_MESSAGE_MAP()

};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PAGE_TROPHY_H__C213D1D8_A0FA_484B_B8FB_A420B54B09A9__INCLUDED_)
