/*******************************************************************
	作用	:	主框架												
	文件名	: 	ED6TrainerDlg.cpp								
	创建时间:	2009/02/23   20:59							
	最后修改:	2009/02/23   20:59							
*********************************************************************/

// ED6TrainerDlg.cpp : implementation file
//

#include "stdafx.h"
#include "ED6Trainer.h"
#include "ED6TrainerDlg.h"
#include "Names.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CED6TrainerDlg dialog

CED6TrainerDlg::CED6TrainerDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CED6TrainerDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CED6TrainerDlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CED6TrainerDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CED6TrainerDlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CED6TrainerDlg, CDialog)
	//{{AFX_MSG_MAP(CED6TrainerDlg)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_WM_KEYDOWN()
	//}}AFX_MSG_MAP
	ON_WM_DESTROY()
	ON_MESSAGE(WM_HOTKEY, OnHotKey)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CED6TrainerDlg message handlers

LRESULT CED6TrainerDlg::OnHotKey(WPARAM wParam,LPARAM lParam)
{
/*	if (wParam== 1001||wParam==1002)
	{
		CWnd::SetForegroundWindow();//使得被激活窗口出现在前景  
		//用户可在此添加代码
	}
*/	
	if (wParam == 1001)
		MessageBox("1001", "Test", MB_OK|MB_ICONASTERISK);
	else if (wParam == 1002)
		MessageBox("1002", "Test", MB_OK|MB_ICONASTERISK);
	return 0;
}

void CED6TrainerDlg::OnDestroy()
{
	UnregisterHotKey(m_hWnd, 1001);
	UnregisterHotKey(m_hWnd, 1002);
	CDialog::OnDestroy();
}

BOOL CED6TrainerDlg::OnInitDialog()
{
	CDialog::OnInitDialog();
	RegisterHotKey(m_hWnd,1001, NULL, VK_F2);
	RegisterHotKey(m_hWnd,1002, NULL, VK_F3);

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	m_TabCtrl = (CTabCtrl *) GetDlgItem(IDC_TAB1);
	for (int i = 0; i != sizeof(strTabName) / 4; ++i)
		m_TabCtrl->InsertItem(i, strTabName[i]);
	m_TabCtrl->SetCurSel(17);
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CED6TrainerDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CED6TrainerDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CED6TrainerDlg::OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags) 
{
	// TODO: Add your message handler code here and/or call default
	MessageBox("KeyDown");
	Invalidate();
	CDialog::OnKeyDown(nChar, nRepCnt, nFlags);
}
