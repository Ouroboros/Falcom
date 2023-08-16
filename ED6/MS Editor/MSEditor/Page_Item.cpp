// Page_Item.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "Page_Item.h"

extern char	*cItemName;

/////////////////////////////////////////////////////////////////////////////
// CPage_Item property page
#if _MASK_ & _MSC_VER > 1300
IMPLEMENT_DYNCREATE(CPage_Item, CMyPropertyPage)
#else
IMPLEMENT_DYNCREATE(CPage_Item, CPropertyPage)
#endif

CPage_Item::CPage_Item(MSFileInfo *pmsfi, PBYTE *ppbFile, const WORD IDD) 
		: CMyPropertyPage(pmsfi, ppbFile, IDD)
{
	//{{AFX_DATA_INIT(CPage_Item)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
}

void CPage_Item::DoDataExchange(CDataExchange* pDX)
{
	CMyPropertyPage::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CPage_Item)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}


BEGIN_MESSAGE_MAP(CPage_Item, CMyPropertyPage)
	//{{AFX_MSG_MAP(CPage_Item)
		// NOTE: the ClassWizard will add message map macros here
		//}}AFX_MSG_MAP
	ON_CONTROL_RANGE(CBN_SELCHANGE, IDC_ITEM_EQUIP1, IDC_ITEM_ORB4, OnUpdateUI)
	ON_CONTROL_RANGE(EN_KILLFOCUS, IDC_ITEM_EQUIP_ID1, IDC_ITEM_ORB_ID4, OnUpdateUI)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPage_Item message handlers

DWORD WINAPI AddItemName(LPVOID lParam)
{	
	char		*szItemName;
	HWND		hComboBox;
	WORD		wOffset, wItemCount = *(WORD *)cItemName >> 1;

	for (DWORD dwItemID = IDC_ITEM_EQUIP1; dwItemID != IDC_ITEM_ORB4 + 1; ++dwItemID)
	{
		hComboBox = GetDlgItem((HWND)lParam, dwItemID);
		SetWindowLong(hComboBox, GWL_STYLE, GetWindowLong(hComboBox, GWL_STYLE)&~CBS_SORT);
		for (WORD wCount = 0; wCount != wItemCount; ++wCount)
		{
			wOffset = *((WORD *)cItemName + wCount);
			switch (wOffset)
			{
			case 0xFFFF: szItemName = "-"; break;
			case 0xFEFF: szItemName = " "; break;
			default: 
				szItemName = cItemName + wOffset;
			}
			SendMessage(hComboBox, CB_ADDSTRING, 0, (LPARAM)szItemName);
		}
	}

	return TRUE;
}

BOOL CPage_Item::OnInitDialog()
{
	CMyPropertyPage::OnInitDialog();
	CreateThread(NULL, 0, AddItemName, (LPVOID)m_hWnd, 0, NULL);
	return TRUE;
}

void CPage_Item::Display()
{
	if (*m_ppbFile == NULL) return;

	WORD	wItemID, wOffset;
	char	*szItemName;
	CString strItemID;

	for (WORD nID = 0; nID != IDC_ITEM_ORB4 - IDC_ITEM_EQUIP1 + 1; ++nID)
	{
		wItemID = m_pMsFileInfo->Equip[nID];

		if (wItemID != 0 && wItemID < MAX_ITEM_INDEX)
		{
			wOffset = *((WORD *)cItemName + wItemID - 0x64);
			switch (wOffset)
			{
			case 0xFFFF: szItemName = "-"; break;
			case 0xFEFF: szItemName = " "; break;
			default: szItemName = cItemName + wOffset;
			}
		}
		else
		{
			szItemName = "гнгнгн";
		}

		strItemID.Format("%.2X%.2X", LOBYTE(wItemID), HIBYTE(wItemID));
		SetDlgItemText(nID + IDC_ITEM_EQUIP_ID1,	strItemID);
		SetDlgItemText(nID + IDC_ITEM_EQUIP1,		szItemName);
	}
}

void CPage_Item::OnUpdateUI(UINT nID)
{
	if (*m_ppbFile == NULL) return;

	WORD wItemID;
	char szItemID[6] = {0};
	CComboBox *pComboBox;

	if (nID >= IDC_ITEM_EQUIP_ID1 && nID <= IDC_ITEM_ORB_ID4)
	{
		GetDlgItemText(nID, szItemID, sizeof(szItemID));
		szItemID[4] = 0;
		strtoul(szItemID, NULL, 16);
		__asm
		{
			xchg  al, ah;
			mov   wItemID, ax;
		}
	m_pMsFileInfo->Equip[nID - IDC_ITEM_EQUIP_ID1] = wItemID;
	}
	else
	{
		pComboBox = (CComboBox *)GetDlgItem(nID);
		wItemID = pComboBox->GetCurSel() + 0x64;
		m_pMsFileInfo->Equip[nID - IDC_ITEM_EQUIP1] = wItemID;
	}
	Display();
}