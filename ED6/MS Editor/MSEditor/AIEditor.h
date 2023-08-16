#if !defined(AFX_AIEDITOR_H__C5A9719A_985B_400A_A946_C1AAEE3A1C8E__INCLUDED_)
#define AFX_AIEDITOR_H__C5A9719A_985B_400A_A946_C1AAEE3A1C8E__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// AIEditor.h : header file
//

//#include "my_common.h"
#include "MSFileStruct.h"

/////////////////////////////////////////////////////////////////////////////
// CAIEditor dialog

class CAIEditor : public CDialog
{
// Construction
public:
	CAIEditor(LPMSFileInfo pMsFileInfo, 
			  PBYTE pbAIData, 
			  BYTE  bySkillNum, 
			  INT nSkillIndex, 
			  CWnd* pParent = NULL);   // standard constructor
	FORCEINLINE void Initialization(LPMSFileInfo pMsFileInfo, PBYTE pbAIData, BYTE bySkillNum, INT nSkillIndex);
	void     UpdateMsFileBuffer();
	LPAIData GetAIDateBuffer();

protected:
	void Update();

// Dialog Data
	//{{AFX_DATA(CAIEditor)
	enum { IDD = IDD_AIEDITOR };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAIEditor)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CAIEditor)
	virtual BOOL OnInitDialog();
	afx_msg void OnEditchangeSkillProperty();
	//}}AFX_MSG

protected:
	CWnd    *m_pParent;
	INT      m_nSkillIndex;
	BYTE     m_bySKillNum;
	PBYTE    m_pbAIData;
	TAIData  m_AIData;
	LPMSFileInfo m_pMsFileInfo;

	DECLARE_MESSAGE_MAP()
};

FORCEINLINE void CAIEditor::Initialization(LPMSFileInfo pMsFileInfo, PBYTE pbAIData, BYTE bySKillNum, INT nSkillIndex)
{
	m_pbAIData    = pbAIData;
	m_bySKillNum  = bySKillNum;
	m_pMsFileInfo = pMsFileInfo;
	m_nSkillIndex = nSkillIndex;
}

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_AIEDITOR_H__C5A9719A_985B_400A_A946_C1AAEE3A1C8E__INCLUDED_)
