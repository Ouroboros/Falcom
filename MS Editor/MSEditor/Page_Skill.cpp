// Page_Skill.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "Page_Skill.h"
#include "AIEditor.h"

extern char *cMagicName;

TCHAR *szColumnNames[] =
{
	"名字", "概率(%)", "条件", "参数", "目标", "参数",
};

/////////////////////////////////////////////////////////////////////////////
// CPage_Skill property page
#if _MASK_ & _MSC_VER > 1300
IMPLEMENT_DYNCREATE(CPage_Skill, CMyPropertyPage)
#else
IMPLEMENT_DYNCREATE(CPage_Skill, CPropertyPage)
#endif

CPage_Skill::CPage_Skill(MSFileInfo *pmsfi, PBYTE *ppbFile, const WORD IDD)
		: CMyPropertyPage(pmsfi, ppbFile, IDD)
{
	m_pbAIData = NULL;
	m_bySkillNum = 0;
}

void CPage_Skill::DoDataExchange(CDataExchange* pDX)
{
	CPropertyPage::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CPage_Skill)
	DDX_Control(pDX, IDC_SKILL_LIST, m_cList);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CPage_Skill, CPropertyPage)
	//{{AFX_MSG_MAP(CPage_Skill)
	ON_NOTIFY(LVN_ITEMCHANGED, IDC_SKILL_LIST, OnItemchangedSkillList)
	ON_BN_CLICKED(IDC_SKILL_DELETE, OnSkillDelete)
	ON_BN_CLICKED(IDC_SKILL_EDIT, OnSkillEdit)
	//}}AFX_MSG_MAP
	ON_CONTROL_RANGE(BN_CLICKED, IDC_SKILL_MOVEUP, IDC_SKILL_MOVEDOWN, OnSkillMove)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CPage_Skill message handlers
BOOL CPage_Skill::OnInitDialog()
{
	CMyPropertyPage::OnInitDialog();

	int		nWidth;
	RECT	rcRect;
	DWORD	dwSize = sizeof(szColumnNames) / sizeof(*szColumnNames);

	m_cList.GetClientRect(&rcRect);
	nWidth = (rcRect.right - rcRect.left) / dwSize;

	for (DWORD i = 0; i != dwSize; ++i)
	{
		m_cList.InsertColumn(i, szColumnNames[i], LVCFMT_LEFT, nWidth);
	}
	m_cList.SetExtendedStyle(LVS_EX_GRIDLINES|LVS_EX_FULLROWSELECT|m_cList.GetExtendedStyle());

	return TRUE;
}

BOOL CPage_Skill::OnSetActive()
{
	GetDlgItem(IDC_SKILL_ADD)->EnableWindow(m_pMsFileInfo->SkillDataCount < MAX_SKILL_NUM);
	for (DWORD dwID = IDC_SKILL_EDIT; dwID != IDC_SKILL_MOVEDOWN + 1; ++dwID)
	{
		GetDlgItem(dwID)->EnableWindow(0);
	}

	return CMyPropertyPage::OnSetActive();
}

void CPage_Skill::Display()
{
	if (*m_ppbFile == NULL) return;

	if (m_cList.GetItemCount() != 0)
	{
		m_cList.DeleteAllItems();
	}

	for (BYTE i = 0; i != m_bySkillNum; ++i)
	{
		AddOneItemToList(&m_cList, m_pbAIData + i * LEN_OF_AIDATA, i);
	}
}

void CPage_Skill::AddOneItemToList(CListCtrl *cList, PBYTE pbSkillData, int nItem)
{
	char	szBuffer[64];
	WORD	wSkillID;
	DWORD	dwParam;
	LPSTR	lpName;

	if (m_pbAIData == NULL) return;

	wSkillID = *(WORD *)(pbSkillData + 6);
	if (wSkillID < 0x3E8)
	{
		lpName = cMagicName + *((WORD *)cMagicName + wSkillID);
	}
	else
	{
		lpName = m_pMsFileInfo->lpSkillName[wSkillID - 0x3E8];
	}
	cList->InsertItem(nItem, lpName);
	wsprintfA(szBuffer, "%d", *(pbSkillData + 1));
	cList->SetItemText(nItem, 1, szBuffer);
	cList->SetItemText(nItem, 2, condition[*pbSkillData].szDescription);
	dwParam = *(DWORD *)(pbSkillData + 8);
	wsprintfA(szBuffer, "%d", dwParam);
	cList->SetItemText(nItem, 3, szBuffer);
	cList->SetItemText(nItem, 4, target[*(pbSkillData + 2)].szDescription);
	dwParam = *(DWORD *)(pbSkillData + 16);
	bswap(dwParam);
	wsprintfA(szBuffer, "%.8X", dwParam);
	cList->SetItemText(nItem, 5, szBuffer);
}

void CPage_Skill::OnSkillMove(UINT nID)
{
	UINT nNewPos = SwapTwoSkill(nID == IDC_SKILL_MOVEDOWN);
	if (nNewPos != -1)
	{
		m_cList.SetFocus();
		m_cList.SetItemState(nNewPos, LVIS_FOCUSED|LVIS_SELECTED, LVIS_FOCUSED|LVIS_SELECTED);
	}
}

UINT CPage_Skill::SwapTwoSkill(bool bNext)
{
	INT32 nItem;
	CHAR  cSkillBuffer[LEN_OF_AIDATA];
	PBYTE pbSkill, pbSkillToSwap;
	POSITION pos = m_cList.GetFirstSelectedItemPosition();

	if (pos == NULL)
	{
		return -1;
	}

	nItem = m_cList.GetNextSelectedItem(pos);
	pbSkill = m_pbAIData + nItem * LEN_OF_AIDATA;
	if (bNext == true)
	{
		++nItem;
		pbSkillToSwap = pbSkill + LEN_OF_AIDATA;
	}
	else
	{
		--nItem;
		pbSkillToSwap = pbSkill - LEN_OF_AIDATA;
	}

	memcpy(cSkillBuffer, pbSkill, LEN_OF_AIDATA);
	memcpy(pbSkill, pbSkillToSwap, LEN_OF_AIDATA);
	memcpy(pbSkillToSwap, cSkillBuffer, LEN_OF_AIDATA);
	Display();
	return nItem;
}

void CPage_Skill::OnItemchangedSkillList(NMHDR* pNMHDR, LRESULT* pResult)
{
	BOOL bEnable;
	POSITION pos;
	NMLISTVIEW* pNMListView = (NMLISTVIEW*)pNMHDR;

	pos = m_cList.GetFirstSelectedItemPosition();
	if (pos == 0)
	{
		for (DWORD dwID = IDC_SKILL_EDIT; dwID != IDC_SKILL_MOVEDOWN + 1; ++dwID)
		{
			GetDlgItem(dwID)->EnableWindow(FALSE);
		}
	}
	else
	{
		bEnable = (pNMListView->iItem != m_cList.GetItemCount() - 1);
		GetDlgItem(IDC_SKILL_MOVEDOWN)->EnableWindow(bEnable);
		GetDlgItem(IDC_SKILL_EDIT)->EnableWindow(TRUE);
		GetDlgItem(IDC_SKILL_DELETE)->EnableWindow(m_bySkillNum);
		GetDlgItem(IDC_SKILL_MOVEUP)->EnableWindow(pNMListView->iItem);
		GetDlgItem(IDC_SKILL_ADD)->EnableWindow(m_pMsFileInfo->SkillDataCount < MAX_SKILL_NUM);
	}

	*pResult = 0;
}

void CPage_Skill::OnSkillDelete()
{
	bool		bDataShared;
	WORD		wSkillID;
	UINT		nItemIndex;
	PBYTE		pbSKillData;
	POSITION	pos = m_cList.GetFirstSelectedItemPosition();

	if (pos == NULL)
	{
		return;
	}
	nItemIndex = m_cList.GetNextSelectedItem(pos);

	bDataShared = false;
	pbSKillData = m_pbAIData + nItemIndex * LEN_OF_AIDATA;
	wSkillID = *(WORD *)(pbSKillData + 6);
	if (wSkillID > 0x3E7)
	{
		;
	}
	memmove(m_pbAIData + nItemIndex * LEN_OF_AIDATA,
		m_pbAIData + (nItemIndex + 1) * LEN_OF_AIDATA,
		(m_bySkillNum - nItemIndex - 1) * LEN_OF_AIDATA);
	ZeroMemory(m_pbAIData + (m_bySkillNum - 1) * LEN_OF_AIDATA, LEN_OF_AIDATA);
	--m_bySkillNum;
	Display();
	if (m_bySkillNum)
	{
		m_cList.SetFocus();
		if (nItemIndex == m_cList.GetItemCount())
		{
			--nItemIndex;
		}
		m_cList.SetItemState(nItemIndex, LVIS_FOCUSED|LVIS_SELECTED, LVIS_FOCUSED|LVIS_SELECTED);
	}
}

void CPage_Skill::OnSkillEdit() 
{
	INT nItemIndex;
	POSITION pos;

	pos = m_cList.GetFirstSelectedItemPosition();
	if (pos == NULL)
	{
		return;
	}

	nItemIndex = m_cList.GetNextSelectedItem(pos);

	CAIEditor AIEditor(m_pMsFileInfo, m_pbAIData, m_bySkillNum, nItemIndex);

	if (AIEditor.DoModal() == IDOK)
	{
		AIEditor.UpdateMsFileBuffer();
	}
}