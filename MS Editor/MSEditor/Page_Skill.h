#if !defined(AFX_PAGE_SKILL_H__65B2809C_D50E_406D_A359_C688A6AFA39A__INCLUDED_)
#define AFX_PAGE_SKILL_H__65B2809C_D50E_406D_A359_C688A6AFA39A__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// Page_Skill.h : header file
//
#include "MyPropertyPage.h"
#include "MyListCtrl.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Skill dialog

class CPage_Skill : public CMyPropertyPage
{
	DECLARE_DYNCREATE(CPage_Skill)

// Construction

public:
	CPage_Skill(LPMSFileInfo pMsFileInfo = NULL, PBYTE *ppbFile = NULL, const WORD IDD = 0);

public:
	BYTE  m_bySkillNum;
	PBYTE m_pbAIData;

protected:
	virtual void Display();
	virtual BOOL OnSetActive();
	virtual BOOL OnInitDialog();
	UINT SwapTwoSkill(bool bNext);
	void AddOneItemToList(CListCtrl *cList, PBYTE pbMagic, int nItem);

// Dialog Data
	//{{AFX_DATA(CPage_Skill)
		// NOTE - ClassWizard will add data members here.
	enum { IDD = IDD_PAGE_SKILL };
	CListCtrl	m_cList;
	//}}AFX_DATA

// Overrides
	// ClassWizard generate virtual function overrides
	//{{AFX_VIRTUAL(CPage_Skill)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	// Generated message map functions
	//{{AFX_MSG(CPage_Skill)
	afx_msg void OnItemchangedSkillList(NMHDR* pNMHDR, LRESULT* pResult);
	afx_msg void OnSkillDelete();
	afx_msg void OnSkillEdit();
	//}}AFX_MSG
	afx_msg void OnSkillMove(UINT nID);
	DECLARE_MESSAGE_MAP()

};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_PAGE_SKILL_H__65B2809C_D50E_406D_A359_C688A6AFA39A__INCLUDED_)
