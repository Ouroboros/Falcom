// MyPropertyPage.cpp : implementation file
//

#include "stdafx.h"
#include "mseditor.h"
#include "MyPropertyPage.h"

CMyPropertyPage::CMyPropertyPage(MSFileInfo *pMsFileInfo, PBYTE *ppbFile, const WORD IDD)
			: CPropertyPage(IDD)
{
	m_pMsFileInfo = pMsFileInfo;
	m_ppbFile = ppbFile;
}

BOOL CMyPropertyPage::OnSetActive()
{
	Display();
	return CPropertyPage::OnSetActive();
}