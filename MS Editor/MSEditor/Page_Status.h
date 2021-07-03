#if !defined(AFX_PAGE_STATUS_H__490FC1AF_04DC_4E60_8183_E314B619DC24__INCLUDED_)
#define AFX_PAGE_STATUS_H__490FC1AF_04DC_4E60_8183_E314B619DC24__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Page_Status.h : header file
//
#include "MyPropertyPage.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Status dialog

class CPage_Status : public CMyPropertyPage
{
	DECLARE_DYNCREATE(CPage_Status)

// Construction
public:
	CPage_Status(LPMSFileInfo pMsFileInfo = NULL, PBYTE *ppbFile = NULL, const WORD IDD = 0);

protected:
	bool	m_bDisplayed;

protected:
	virtual void Display();
	void OnUpdateUI(UINT nID);
	void OnLimiteNum(UINT nID);

// Dialog Data
	//{{AFX_DATA(CPage_Status)
	//}}AFX_DATA


// Overrides
	// ClassWizard generate virtual function overrides
	//{{AFX_VIRTUAL(CPage_Status)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL
	virtual BOOL OnInitDialog();

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CPage_Status)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()

};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PAGE_STATUS_H__490FC1AF_04DC_4E60_8183_E314B619DC24__INCLUDED_)
