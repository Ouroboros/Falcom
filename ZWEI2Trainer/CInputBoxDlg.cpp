// CInputBoxDlg.cpp : implementation file
//

#include "stdafx.h"
#include "ZWEI2Trainer.h"
#include "CInputBoxDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CInputBoxDlg dialog


CInputBoxDlg::CInputBoxDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CInputBoxDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CInputBoxDlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
}


void CInputBoxDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CInputBoxDlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	DDX_Text(pDX, IDC_INPUTBOX_TIPTEXT, m_cstrTipText);
	DDX_Text(pDX, IDC_INPUTBOX_INPUT, m_dwInput);
	//}}AFX_DATA_MAP
}

BOOL CInputBoxDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	return TRUE;
}

BEGIN_MESSAGE_MAP(CInputBoxDlg, CDialog)
	//{{AFX_MSG_MAP(CInputBoxDlg)
		// NOTE: the ClassWizard will add message map macros here
		ON_WM_PAINT()
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

void CInputBoxDlg::OnPaint()
{
	CDialog::OnPaint();
	((CEdit *)(GetDlgItem(IDC_INPUTBOX_INPUT)))->SetFocus();
	((CEdit *)(GetDlgItem(IDC_INPUTBOX_INPUT)))->SetSel(0, -1);
}
/////////////////////////////////////////////////////////////////////////////
// CInputBoxDlg message handlers
