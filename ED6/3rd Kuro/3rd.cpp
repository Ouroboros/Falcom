// 3rd.cpp : Defines the class behaviors for the application.
//

#include "stdafx.h"
#include "3rd.h"
#include "3rdDlg.h"

/*
#pragma comment(linker,"/SECTION:.text,ERW /ALIGN:0x1000")
#pragma comment(linker,"/merge:.data=.text")
#pragma comment(linker,"/merge:.rdata=.text")
#pragma comment (linker, "/Filealign:0x200")
#pragma optimize("gsy", on)
#pragma comment (linker, "/OPT:NOWIN98")
/*

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif
*/


/////////////////////////////////////////////////////////////////////////////
// CMy3rdApp

BEGIN_MESSAGE_MAP(CMy3rdApp, CWinApp)
	//{{AFX_MSG_MAP(CMy3rdApp)
	//}}AFX_MSG
	ON_COMMAND(ID_HELP, CWinApp::OnHelp)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMy3rdApp construction

CMy3rdApp::CMy3rdApp()
{
}

/////////////////////////////////////////////////////////////////////////////
// The one and only CMy3rdApp object

CMy3rdApp theApp;

/////////////////////////////////////////////////////////////////////////////
// CMy3rdApp initialization

BOOL CMy3rdApp::InitInstance()
{
	// Standard initialization
/*
#ifdef _AFXDLL
	Enable3dControls();			// Call this when using MFC in a shared DLL
#else
	Enable3dControlsStatic();	// Call this when linking to MFC statically
#endif
*/
	CMy3rdDlg dlg;
	m_pMainWnd = &dlg;
	int nResponse = dlg.DoModal();
	if (nResponse == IDOK)
	{
	}
	else if (nResponse == IDCANCEL)
	{
	}

	// Since the dialog has been closed, return FALSE so that we exit the
	//  application, rather than start the application's message pump.
	return FALSE;
}
