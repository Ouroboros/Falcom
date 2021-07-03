// MSEditorDlg.h : header file
//

#if !defined(AFX_MSEDITORDLG_H__1AF0F99D_4BF3_4C2C_B0C9_C2E562DE9F61__INCLUDED_)
#define AFX_MSEDITORDLG_H__1AF0F99D_4BF3_4C2C_B0C9_C2E562DE9F61__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "Page_Status.h"
#include "Page_Risist.h"
#include "Page_Item.h"
#include "Page_Trophy.h"
#include "Page_Skill.h"
#include "MSFileStruct.h"

/////////////////////////////////////////////////////////////////////////////
// CMSEditorDlg dialog

class CMSEditorDlg : public CDialog
{
// Construction
public:
	CMSEditorDlg(LPSTR lpCmdLine = NULL, CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CMSEditorDlg)
	enum { IDD = IDD_MSEDITOR };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMSEditorDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	int			m_iArgc;
	CFont		*m_pFont;
	HICON		m_hIcon;
	PBYTE		m_pbFile;
	DWORD		m_dwFileSize;
	CString		m_strFilePath;
	HANDLE		m_hFile;
	LPSTR		m_lpCmdLine, *m_lpArgv;
	MSFileInfo	m_msfi;

protected:
	CPage_Status	m_pageStatus;
	CPage_Risist	m_pageRisist;
	CPage_Item		m_pageItem;
	CPage_Trophy	m_pageTrophy;
	CPage_Skill		m_pageAttack;
	CPage_Skill		m_pageMagic;
	CPage_Skill		m_pageCraft;
	CPage_Skill		m_pageSCraft;
	CPropertySheet	m_Sheet;

	// Generated message map functions
	//{{AFX_MSG(CMSEditorDlg)
	virtual BOOL OnInitDialog();
	virtual void OnDestroy();

	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnDropFiles(HDROP hDrop);
	afx_msg void OnOpenFile();
	afx_msg void OnSaveFile();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()

protected:
	bool OpenFile();
	void CloseFile();
	void Display();
	bool Parser(LPMSFileInfo msfi);
	bool IsValidMSFile(PBYTE pbFile, DWORD dwSize);
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MSEDITORDLG_H__1AF0F99D_4BF3_4C2C_B0C9_C2E562DE9F61__INCLUDED_)
