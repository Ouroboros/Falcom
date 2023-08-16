// ED6TrainerDlg.h : header file
//

#if !defined(AFX_ED6TRAINERDLG_H__4D3A3A8F_B646_41D1_981D_1F04E4FCB61B__INCLUDED_)
#define AFX_ED6TRAINERDLG_H__4D3A3A8F_B646_41D1_981D_1F04E4FCB61B__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CED6TrainerDlg dialog

class CED6TrainerDlg : public CDialog
{
// Construction
public:
	CED6TrainerDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CED6TrainerDlg)
	enum { IDD = IDD_ED6TRAINER_DIALOG };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CED6TrainerDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON		m_hIcon;
	CTabCtrl	*m_TabCtrl;

	// Generated message map functions
	//{{AFX_MSG(CED6TrainerDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg void OnDestroy();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg LRESULT OnHotKey(WPARAM wParam, LPARAM lParam);
	afx_msg void OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_ED6TRAINERDLG_H__4D3A3A8F_B646_41D1_981D_1F04E4FCB61B__INCLUDED_)
