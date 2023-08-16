// ZWEI2TrainerDlg.h : header file
//

#if !defined(AFX_ZWEI2TRAINERDLG_H__FA8C9769_10F6_4A43_A9E5_CFD3EC2682B3__INCLUDED_)
#define AFX_ZWEI2TRAINERDLG_H__FA8C9769_10F6_4A43_A9E5_CFD3EC2682B3__INCLUDED_

#if _MSC_VER > 1000
#pragma once

#pragma comment(lib, "Psapi.lib")

#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CZWEI2TrainerDlg dialog

class CZWEI2TrainerDlg : public CDialog
{
// Construction
public:
	CZWEI2TrainerDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CZWEI2TrainerDlg)
	enum { IDD = IDD_ZWEI2TRAINER_DIALOG };
	CString	m_cstrHP;
	CString m_cstrMP;
	CString m_cstrNextRemainder;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CZWEI2TrainerDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	virtual void WinHelp(DWORD dwData, UINT nCmd);
	virtual void OnOK();
	virtual BOOL PreTranslateMessage(MSG* pMsg);
//	virtual void OnInitMenuPopup(CMenu *pPopupMenu, UINT nIndex,BOOL bSysMenu);
	//}}AFX_VIRTUAL

// Implementation
protected:
	bool	bChecked;
	DWORD	dwFirstID, dwLevel, dwHPCur, dwHPUp, dwMP, dwExp, dwNext, dwMoney;
	DWORD	openProcId;
	CMenu	m_Menu;
	HICON	m_hIcon;
	HACCEL	m_hAccelTable;
	HWND	m_hZwei2Wnd;
	HANDLE	hProcess;
	CStatusBar m_wndStatusBar;
    CDialog  dlg;

	// Generated message map functions
	//{{AFX_MSG(CZWEI2TrainerDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnTimer(UINT nIDEvent);
	afx_msg BOOL ProcMsg(UINT nID);
	afx_msg void OnHotkey(WPARAM wParam, LPARAM lParam);
	afx_msg void OnContextMenu(CWnd* pWnd, CPoint pos);
//	afx_msg void OnUpdateDress(CCmdUI* pCmdUI);
	//}}AFX_MSG
	void AppendCString(CString &csz, const DWORD &n, const char &c);
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_ZWEI2TRAINERDLG_H__FA8C9769_10F6_4A43_A9E5_CFD3EC2682B3__INCLUDED_)
