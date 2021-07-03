// Page_Status.cpp : implementation file
//
#include "stdafx.h"
#include "MSEditor.h"
#include "Page_Status.h"

/////////////////////////////////////////////////////////////////////////////
// CPage_Status property page
#if _MASK_ & _MSC_VER > 1300
IMPLEMENT_DYNCREATE(CPage_Status, CMyPropertyPage)
#else
IMPLEMENT_DYNCREATE(CPage_Status, CPropertyPage)
#endif

CPage_Status::CPage_Status(MSFileInfo *pmsfi, PBYTE *ppbFile, const WORD IDD) 
		: CMyPropertyPage(pmsfi, ppbFile, IDD)
{
	m_bDisplayed = false;
}

void CPage_Status::DoDataExchange(CDataExchange* pDX)
{
	CMyPropertyPage::DoDataExchange(pDX);

	//{{AFX_DATA_MAP(CPage_Status)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CPage_Status, CMyPropertyPage)
	//{{AFX_MSG_MAP(CPage_Status)
		// NOTE: the ClassWizard will add message map macros here
	//}}AFX_MSG_MAP
	ON_CONTROL_RANGE(EN_KILLFOCUS, IDC_STATUS_HP_UP, IDC_STATUS_RNG, CPage_Status::OnUpdateUI)
	ON_CONTROL_RANGE(EN_KILLFOCUS, IDC_STATUS_CHI,   IDC_STATUS_GEN, CPage_Status::OnUpdateUI)
	ON_CONTROL_RANGE(EN_CHANGE,    IDC_STATUS_HP_UP, IDC_STATUS_RNG, CPage_Status::OnLimiteNum)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPage_Status message handlers

BOOL CPage_Status::OnInitDialog()
{
	CMyPropertyPage::OnInitDialog();
	
	for (WORD nID = IDC_STATUS_HP_UP; nID != IDC_STATUS_HP_DEF + 1; ++nID)
	{
		((CEdit *)GetDlgItem(nID))->SetLimitText(11);
	}
	
	for (WORD nID = IDC_STATUS_EP_UP; nID != IDC_STATUS_RNG + 1; ++nID)
	{
		((CEdit *)GetDlgItem(nID))->SetLimitText(6);
	}

	CSpinButtonCtrl *pSpin;
	for (WORD nID = 0; nID != 7; ++nID)
	{
		pSpin = ((CSpinButtonCtrl *)GetDlgItem(IDC_STATUS_CHI_SPIN + nID));
		pSpin->SetBuddy(GetDlgItem(IDC_STATUS_CHI + nID));
		pSpin->SetRange(0, MAX_CONDITION);
	}

	return TRUE;
}

void CPage_Status::Display()
{
	if (*m_ppbFile == NULL) return;

	PBYTE pbMSFI = (PBYTE)&m_pMsFileInfo->HPMax;
	for (WORD nID = IDC_STATUS_HP_UP; nID != IDC_STATUS_HP_DEF + 1; ++nID)
	{
		SetDlgItemInt(nID, *(DWORD *)pbMSFI);
		pbMSFI += sizeof(DWORD);
	}

	for (WORD nID = IDC_STATUS_EP_UP; nID != IDC_STATUS_RNG + 1; ++nID)
	{
		SetDlgItemInt(nID, *(WORD *)pbMSFI);
		pbMSFI += sizeof(WORD);
	}

	CSpinButtonCtrl *pSpin;
	for (WORD nID = 0; nID != 7; ++nID)
	{
		pSpin = ((CSpinButtonCtrl *)GetDlgItem(IDC_STATUS_CHI_SPIN + nID));
		pSpin->SetPos(m_pMsFileInfo->ConditionGuard[nID]);
	}
}

void CPage_Status::OnUpdateUI(UINT nID)
{
	if (*m_ppbFile == NULL) return;

	PBYTE pbMSFI;

	if (nID <= IDC_STATUS_HP_DEF)
	{
		pbMSFI = (PBYTE)m_pMsFileInfo + 6;
		*((DWORD *)pbMSFI + (nID - IDC_STATUS_HP_UP)) = GetDlgItemInt(nID);
	}
	else if (nID <= IDC_STATUS_RNG)
	{
		pbMSFI = (PBYTE)m_pMsFileInfo + 0xE;
		*((WORD *)pbMSFI + (nID - IDC_STATUS_EP_UP)) = GetDlgItemInt(nID);
	}
	else
	{
		pbMSFI = (PBYTE)m_pMsFileInfo->ConditionGuard;
		*((WORD *)pbMSFI + (nID - IDC_STATUS_CHI)) = GetDlgItemInt(nID);
	}
}

void CPage_Status::OnLimiteNum(UINT nID)
{
	CString strNum;

	if (nID <= IDC_STATUS_HP_DEF)
	{
		LONG64 l64Num;

		GetDlgItemText(nID, strNum);
		l64Num = _ttoi64(strNum);
		if (l64Num > UINT_MAX)
		{
			strNum.Format("%u", UINT_MAX);
			SetDlgItemText(nID, strNum);
			((CEdit *)GetDlgItem(nID))->SetSel(10, 10);
		}
	}
	else
	{
		DWORD dwNum;

		dwNum = GetDlgItemInt(nID);
		if (dwNum > 0xFFFF)
		{
			SetDlgItemInt(nID, 0xFFFF);
			((CEdit *)GetDlgItem(nID))->SetSel(5, 5);
		}
	}
}
