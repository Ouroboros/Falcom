// Page_Risist.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "Page_Risist.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Risist property page
#if _MASK_ & _MSC_VER > 1300
IMPLEMENT_DYNCREATE(CPage_Risist, CMyPropertyPage)
#else
IMPLEMENT_DYNCREATE(CPage_Risist, CPropertyPage)
#endif

CPage_Risist::CPage_Risist(MSFileInfo *pmsfi, PBYTE *ppbFile, const WORD IDD)
		: CMyPropertyPage(pmsfi, ppbFile, IDD)
{
	m_bInput = false;
}

void CPage_Risist::DoDataExchange(CDataExchange* pDX)
{
	CMyPropertyPage::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CPage_Risist)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CPage_Risist, CMyPropertyPage)
	//{{AFX_MSG_MAP(CPage_Risist)
	ON_BN_CLICKED(IDC_RISIST_SELALL, OnRisistSelall)
	ON_BN_CLICKED(IDC_RISIST_SELNONE, OnRisistSelnone)
	ON_BN_CLICKED(IDC_RISIST_CUSTOM, OnRisistCustom)
	ON_BN_CLICKED(IDC_RISIST_RESET, OnRisistReset)
	//}}AFX_MSG_MAP
	ON_COMMAND_EX_RANGE(IDC_RISIST_POISON, IDC_RISIST_FORCEDEAD, CPage_Risist::OnSetRisist)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPage_Risist message handlers

static const DWORD dwRisistBitmap[] =
{
//		毒			冻结		石化		睡眠
	0x00000001,	0x00000002,	0x00000004,	0x00000008,

//		封魔		黑暗		封技		混乱
	0x00000010,	0x00000020,	0x00000040,	0x00000080,

//		气绝		秒杀	 DEF DOWN		怒
	0x00000100,	0x00000200,	0x00000400,	0x00000800,

//	Arts Guard	Craft Guard	  MOV UP	 MOV DOWN
	0x00001000,	0x00002000,	0x00004000,	0x00008000,

//	  STR UP	 STR DOWN	  DEF UP	 DEF DOWN
	0x00010000,	0x00020000,	0x00040000,	0x00080000,

//	  SPD UP	 SPD DOWN	  ADF UP	 ADF DOWN
	0x00100000,	0x00200000,	0x00400000,	0x00800000,

//	  AGL UP	 AGL DOWN	 MAX GUARD	   VANISH
	0x01000000,	0x02000000,	0x04000000,	0x08000000,

//	Condition Guard	催肥	  ATS UP	强制战斗不能
	0x10000000,	0x20000000,	0x40000000,	0x80000000,
};

void CPage_Risist::Display()
{
	if (*m_ppbFile == NULL) return;

	BOOL bChecked;

	for (DWORD nID = IDC_RISIST_POISON; nID != IDC_RISIST_FORCEDEAD + 1; ++nID)
	{
		bChecked = (m_pMsFileInfo->Resistance & dwRisistBitmap[nID - IDC_RISIST_POISON]);
		((CButton *)GetDlgItem(nID))->SetCheck(bChecked);
	}
}

BOOL CPage_Risist::OnSetRisist(UINT nID)
{
	m_pMsFileInfo->Resistance ^= dwRisistBitmap[nID - IDC_RISIST_POISON];
	return TRUE;
}

void CPage_Risist::OnRisistSelall()
{
	if (*m_ppbFile != NULL)
	{
		m_pMsFileInfo->Resistance = -1;
		Display();
		if (m_bInput)
		{
			m_bInput = false;
			OnRisistCustom();
		}
	}
}

void CPage_Risist::OnRisistSelnone()
{
	if (*m_ppbFile != NULL)
	{
		m_pMsFileInfo->Resistance = 0;
		Display();
		if (m_bInput)
		{
			m_bInput = false;
			OnRisistCustom();
		}
	}
}

void CPage_Risist::OnRisistCustom()
{
	if (*m_ppbFile == NULL) return;

	DWORD	dwRisist;
	CString strRisist;
	CEdit	*pEdit   = (CEdit *)GetDlgItem(IDC_RISIST_CUS);
	CButton	*pButton = (CButton *)GetDlgItem(IDC_RISIST_CUSTOM);

	if (m_bInput == false)
	{
		dwRisist = m_pMsFileInfo->Resistance;
		bswap(dwRisist);

		strRisist.Format("%.8X", dwRisist);
		pEdit->SetWindowText(strRisist);
		pEdit->SetLimitText(8);
		pEdit->SetFocus();
		pEdit->SetSel(0, -1);
		pEdit->ShowWindow(SW_SHOW);
		pButton->SetWindowText(TEXT("应用(&F)"));
		m_bInput = true;
	}
	else
	{
		pEdit->GetWindowText(strRisist);
		strtoul(strRisist, 0, 16);
		__asm
		{
			bswap	eax;
			mov		dwRisist, eax;
		}

		m_pMsFileInfo->Resistance = dwRisist;
		Display();
		pEdit->ShowWindow(SW_HIDE);
		pButton->SetWindowText(TEXT("自定义(&C)..."));
		m_bInput = false;
	}
}

void CPage_Risist::OnRisistReset()
{
	if (*m_ppbFile != NULL)
	{
		m_pMsFileInfo->Resistance = *(DWORD *)((*m_ppbFile) + 0x5A);
		Display();
		if (m_bInput)
		{
			m_bInput = false;
			OnRisistCustom();
		}
	}
}