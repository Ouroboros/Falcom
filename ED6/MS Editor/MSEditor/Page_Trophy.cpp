
// Page_Trophy.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "Page_Trophy.h"

extern char *cItemName;
/////////////////////////////////////////////////////////////////////////////
// CPage_Trophy property page
#if _MASK_ & _MSC_VER > 1300
IMPLEMENT_DYNCREATE(CPage_Trophy, CMyPropertyPage)
#else
IMPLEMENT_DYNCREATE(CPage_Trophy, CPropertyPage)
#endif

CPage_Trophy::CPage_Trophy(MSFileInfo *pmsfi, PBYTE *ppbFile, const WORD IDD) 
	: CMyPropertyPage(pmsfi, ppbFile, IDD)
{
	//{{AFX_DATA_INIT(CPage_Trophy)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
}

void CPage_Trophy::DoDataExchange(CDataExchange* pDX)
{
	CMyPropertyPage::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CPage_Trophy)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CPage_Trophy, CMyPropertyPage)
	//{{AFX_MSG_MAP(CPage_Trophy)
	//}}AFX_MSG_MAP
	ON_CONTROL_RANGE(EN_KILLFOCUS, IDC_TROPHY_SEPITH_CHI, IDC_TROPHY_SEPITH_GEN, OnEditTrophySepith)
	ON_NOTIFY_RANGE(UDN_DELTAPOS, IDC_TROPHY_SEPITH_CHI_SPIN, IDC_TROPHY_SEPITH_GEN_SPIN, OnDeltaposTrophySepith)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPage_Trophy message handlers

BOOL CPage_Trophy::OnInitDialog()
{
	CMyPropertyPage::OnInitDialog();

	CSpinButtonCtrl *pSpin;
	for (WORD nID = 0; nID != MAX_SEPITH_KIND; ++nID)
	{		
		pSpin = (CSpinButtonCtrl *)GetDlgItem(IDC_TROPHY_SEPITH_CHI_SPIN + nID);
		pSpin->SetBuddy(GetDlgItem(IDC_TROPHY_SEPITH_CHI + nID));
		pSpin->SetRange(0, MAX_SEPITH_DROP);
	}

	return TRUE;
}

void CPage_Trophy::Display()
{
	CSpinButtonCtrl *pSpin;

	for (DWORD dwID = 0; dwID != MAX_SEPITH_KIND; ++dwID)
	{
		pSpin = (CSpinButtonCtrl *)GetDlgItem(IDC_TROPHY_SEPITH_CHI_SPIN + dwID);
		pSpin->SetPos(m_pMsFileInfo->Sepith[dwID]);
	}
}

void CPage_Trophy::OnDeltaposTrophySepith(UINT nID, NMHDR* pNMHDR, LRESULT* pResult) 
{
	NMUPDOWN* pNMUpDown = (NMUPDOWN*)pNMHDR;
	
	m_pMsFileInfo->Sepith[nID - IDC_TROPHY_SEPITH_CHI_SPIN] = pNMUpDown->iPos - 1;
	*pResult = 0;
}

void CPage_Trophy::OnEditTrophySepith(UINT nID)
{
	m_pMsFileInfo->Sepith[nID - IDC_TROPHY_SEPITH_CHI] = GetDlgItemInt(nID);
}