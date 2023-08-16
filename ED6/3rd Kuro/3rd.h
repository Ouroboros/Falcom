// 3rd.h : main header file for the 3RD application
//
#pragma comment(lib,"mfc42u.lib")
#if !defined(AFX_3RD_H__67F28486_A4E0_4DE7_BA62_787EA7EDF103__INCLUDED_)
#define AFX_3RD_H__67F28486_A4E0_4DE7_BA62_787EA7EDF103__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"

class CMy3rdApp : public CWinApp
{
public:
	CMy3rdApp();
	void OnAppExit();
	public:
	virtual BOOL InitInstance();
	DECLARE_MESSAGE_MAP()
};

#endif // !defined(AFX_3RD_H__67F28486_A4E0_4DE7_BA62_787EA7EDF103__INCLUDED_)
