#if !defined(AFX_PAGE_ITEM_H__011E7727_E798_479C_A743_75D59667235A__INCLUDED_)
#define AFX_PAGE_ITEM_H__011E7727_E798_479C_A743_75D59667235A__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Page_Item.h : header file
//
#include "MyPropertyPage.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Item dialog

class CPage_Item : public CMyPropertyPage
{
	DECLARE_DYNCREATE(CPage_Item)

// Construction
public:
	CPage_Item(LPMSFileInfo pMsFileInfo = NULL, PBYTE *ppbFile = NULL, const WORD IDD = 0);

protected:
	virtual void Display();
	void OnUpdateUI(UINT nID);

// Dialog Data
	//{{AFX_DATA(CPage_Item)
		// NOTE - ClassWizard will add data members here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_DATA


// Overrides
	// ClassWizard generate virtual function overrides
	//{{AFX_VIRTUAL(CPage_Item)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL
	virtual BOOL OnInitDialog();

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CPage_Item)
		// NOTE: the ClassWizard will add member functions here
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()

};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PAGE_ITEM_H__011E7727_E798_479C_A743_75D59667235A__INCLUDED_)
