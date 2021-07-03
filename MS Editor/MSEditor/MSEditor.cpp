// MSEditor.cpp : Defines the class behaviors for the application.
//

#include "stdafx.h"
#include "MSEditor.h"
#include "MSEditorDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CMSEditorApp

BEGIN_MESSAGE_MAP(CMSEditorApp, CWinApp)
	//{{AFX_MSG_MAP(CMSEditorApp)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMSEditorApp construction

CMSEditorApp::CMSEditorApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

/////////////////////////////////////////////////////////////////////////////
// The one and only CMSEditorApp object

CMSEditorApp theApp;

/////////////////////////////////////////////////////////////////////////////
// CMSEditorApp initialization

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

BOOL CMSEditorApp::InitInstance()
{
	AfxEnableControlContainer();
    vector<int> v;
    for (int i = 0; i < 10; ++i) 
    {
        v.push_back(i);
    }
    
    // Count the number of even numbers in the vector by 
    // using the for_each function and a lambda expression.
    int evenCount = 0;
    for_each(v.begin(), v.end(), [&evenCount] (int n) {
        cout << n;
        
        if (n % 2 == 0) 
        {
            cout << " is even " << endl;
            
            // Increment the counter.
            evenCount++;
        }
        else 
        {
            cout << " is odd " << endl;
        }
   });
	// Standard initialization
	// If you are not using these features and wish to reduce the size
	//  of your final executable, you should remove from the following
	//  the specific initialization routines you do not need.
	CMSEditorDlg dlg(m_lpCmdLine);
	m_pMainWnd = &dlg;
	int nResponse = dlg.DoModal();
	if (nResponse == IDOK)
	{
		// TODO: Place code here to handle when the dialog is
		//  dismissed with OK
	}
	else if (nResponse == IDCANCEL)
	{
		// TODO: Place code here to handle when the dialog is
		//  dismissed with Cancel
	}

	// Since the dialog has been closed, return FALSE so that we exit the
	//  application, rather than start the application's message pump.
	return FALSE;
}

__declspec(dllimport) int AfxWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow);

int Entry()
{
	ExitProcess(AfxWinMain(GetModuleHandle(0), 0, GetCommandLine(), 10));
}
