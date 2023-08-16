// MyListCtrl.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "MyListCtrl.h"

BEGIN_MESSAGE_MAP(CMyListCtrl, CListCtrl)
	//{{AFX_MSG_MAP(CMyListCtrl)
		// NOTE - the ClassWizard will add and remove mapping macros here.
	//}}AFX_MSG_MAP
	ON_NOTIFY_REFLECT(NM_CUSTOMDRAW, OnCustomdraw)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMyListCtrl message handlers

UINT CMyListCtrl::m_nSelectedItem = -1;

void CMyListCtrl::OnCustomdraw(NMHDR *pNMHDR, LRESULT *pResult)
{
	NMLVCUSTOMDRAW *pLVCD = (NMLVCUSTOMDRAW*)pNMHDR;
	int nItem = pLVCD->nmcd.dwItemSpec;

	switch(pLVCD->nmcd.dwDrawStage)
	{
	case CDDS_PREPAINT:
		*pResult = CDRF_NOTIFYITEMDRAW;
		break;
		
	case CDDS_ITEMPREPAINT:
		*pResult = CDRF_NOTIFYSUBITEMDRAW;
		break;

	case CDDS_ITEMPREPAINT|CDDS_SUBITEM:
		if (nItem == m_nSelectedItem)
		{
			pLVCD->clrText   = RGB(255, 255, 255);
			pLVCD->clrTextBk = RGB(51, 153, 254);
		}
	default:
		*pResult = CDRF_DODEFAULT;
	}
}