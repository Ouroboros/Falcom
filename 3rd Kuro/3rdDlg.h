// 3rdDlg.h : header file
//
#pragma comment(lib,"mfc42u.lib")
#include "afxwin.h"
#if !defined(AFX_3RDDLG_H__0D66488D_68E1_47F6_B55C_13C14338CA96__INCLUDED_)
#define AFX_3RDDLG_H__0D66488D_68E1_47F6_B55C_13C14338CA96__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif

class CMy3rdDlg : public CDialog
{
public:
	CMy3rdDlg(CWnd* pParent = NULL);
	enum { IDD = IDD_MY3RD_DIALOG };
	void sora3_fenshen();
	void sora3(unsigned nIDEvent);
	void DebugMenu();

protected:
	virtual BOOL OnInitDialog();
	afx_msg void On_start();
	afx_msg void OnTimer(UINT nIDEvent);
	afx_msg void On_stop();
	void OnDestroy();
	HANDLE hProcess;
	unsigned MemberID;
	WORD isbattle,SBreak,LastMem,push;
	DWORD NameAdd,_0Bstatus,RiesLen,RiesAdd,snadd,Dir30,YLen,
		  KLen,YAdd,KAdd,Xor,MSFile,MemberAdd,DirAdd,HeadAdd,SNPtr;
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnLbnSelchangeList1();
};

#endif
