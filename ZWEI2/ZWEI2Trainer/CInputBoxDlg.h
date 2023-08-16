#if !defined(AFX_CINPUTBOXDLG_H__2A0BA17F_E8BE_4CAC_ADCF_58E8B8870131__INCLUDED_)
#define AFX_CINPUTBOXDLG_H__2A0BA17F_E8BE_4CAC_ADCF_58E8B8870131__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// CInputBoxDlg.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CInputBoxDlg dialog

class CInputBoxDlg : public CDialog
{
// Construction
public:
	CInputBoxDlg(CWnd* pParent = NULL);   // standard constructor

// Dialog Data
	//{{AFX_DATA(CInputBoxDlg)
	enum { IDD = IDD_INPUTBOX };
	CString	m_cstrTipText;
	DWORD	m_dwInput;
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA


// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CInputBoxDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:

	// Generated message map functions
	//{{AFX_MSG(CInputBoxDlg)
	// NOTE: the ClassWizard will add member functions here
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_CINPUTBOXDLG_H__2A0BA17F_E8BE_4CAC_ADCF_58E8B8870131__INCLUDED_)
