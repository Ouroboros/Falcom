// AIEditor.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "AIEditor.h"

/////////////////////////////////////////////////////////////////////////////
// CAIEditor dialog

CAIEditor::CAIEditor(LPMSFileInfo pMsFileInfo,
					 PBYTE pbAIData,
					 BYTE  bySkillNum,
					 INT nSkillIndex,
					 CWnd* pParent /*=NULL*/)
	: CDialog(CAIEditor::IDD, pParent)
{
	//{{AFX_DATA_INIT(CAIEditor)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	m_pParent = pParent;
	Initialization(pMsFileInfo, pbAIData, bySkillNum, nSkillIndex);
}

void CAIEditor::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAIEditor)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAIEditor, CDialog)
	//{{AFX_MSG_MAP(CAIEditor)
	ON_CBN_EDITCHANGE(IDC_SKILL_PROPERTY, OnEditchangeSkillProperty)
	ON_CBN_KILLFOCUS(IDC_SKILL_PROPERTY, OnEditchangeSkillProperty)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CAIEditor message handlers

BOOL CAIEditor::OnInitDialog()
{
	CDialog::OnInitDialog();

	CDC        *dc;
	INT        dwMaxLength;
	LPAIData   pAIData;
	CString    cstrBuffer;
	TEXTMETRIC TextMetric;
	CComboBox *pComboID, *pComboDataIndex;

	dc = GetDC();
	dwMaxLength = 0;
	pAIData = (LPAIData)m_pbAIData;
	pComboID = (CComboBox *)GetDlgItem(IDC_SKILL_ID);
	pComboDataIndex = (CComboBox *)GetDlgItem(IDC_SKILL_PROPERTY);
	GetTextMetrics(dc->m_hDC, &TextMetric);

	for (int i = 0; i != m_bySKillNum; ++i)
	{
		cstrBuffer.Format("%.2X", HIBYTE(pAIData->wEffectIndex));
		pComboID->InsertString(i, cstrBuffer);
		cstrBuffer.Format("%.2X%.2X  %s",
			LOBYTE(pAIData->wSkillDataIndex),
			HIBYTE(pAIData->wSkillDataIndex),
			m_pMsFileInfo->lpSkillName[pAIData->wSkillDataIndex - CUSTOM_SKILL_BASE]);
		pComboDataIndex->InsertString(i, cstrBuffer);

		if (cstrBuffer.GetLength() > dwMaxLength)
		{
			dwMaxLength = cstrBuffer.GetLength();
		}

		if (i == m_nSkillIndex)
		{
			pComboID->SetCurSel(i);
			pComboDataIndex->SetCurSel(i);
			cstrBuffer.Format("%.2X  %s", pAIData->byCondition, condition[pAIData->byCondition].szDescription);
			SetDlgItemText(IDC_SKILL_CONDITION, cstrBuffer);
			cstrBuffer.Format("%I64X", *(PULONG64)pAIData->cParam1);
			SetDlgItemText(IDC_SKILL_PARAM1, cstrBuffer);
			cstrBuffer.Format("%.2X  %s", pAIData->byTarget, target[pAIData->byTarget].szDescription);
			SetDlgItemText(IDC_SKILL_TARGET, cstrBuffer);
			cstrBuffer.Format("%I64X", *(PULONG64)pAIData->cParam2);
			SetDlgItemText(IDC_SKILL_PARAM2, cstrBuffer);
		}
		++pAIData;
	}

	pComboDataIndex->SetDroppedWidth(dwMaxLength * TextMetric.tmAveCharWidth);
	ReleaseDC(dc);

//	Update();

	return TRUE;
}

void CAIEditor::Update()
{
	CString  cstrBuffer;
	LPAIData pAIData;
	CComboBox *pComboID, *pComboDataIndex;

	pComboID = (CComboBox *)GetDlgItem(IDC_SKILL_ID);
	pComboDataIndex = (CComboBox *)GetDlgItem(IDC_SKILL_PROPERTY);
	pAIData = (LPAIData)(m_pbAIData + m_nSkillIndex * LEN_OF_AIDATA);
}

LPAIData CAIEditor::GetAIDateBuffer()
{
	return &m_AIData;
}

void CAIEditor::UpdateMsFileBuffer()
{
	;
}

void CAIEditor::OnEditchangeSkillProperty() 
{
	CEdit  *pEdit;
	DWORD   dwSkillDataIndex;
	CString cstrBuffer;

	GetDlgItem(IDC_SKILL_PROPERTY)->GetWindowText(cstrBuffer);
	cstrBuffer.SetAt(4, 0);
	strtoul(cstrBuffer, NULL, 16);
	__asm
	{
		xchg  al, ah;
		mov   dwSkillDataIndex, eax;
	}

	if (dwSkillDataIndex >= CUSTOM_SKILL_BASE)
	{
		dwSkillDataIndex -= CUSTOM_SKILL_BASE;
		pEdit = (CEdit *)GetDlgItem(IDC_SKILL_NAME);
		if (dwSkillDataIndex <= m_pMsFileInfo->SkillDataCount)
		{
			pEdit->SetWindowText(m_pMsFileInfo->lpSkillName[dwSkillDataIndex]);
		}
	}
}