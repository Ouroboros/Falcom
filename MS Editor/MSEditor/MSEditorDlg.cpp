/*******************************************************************
	作用	:	主窗口,负责打开,解析,保存MS文件
	文件名	: 	MSEditorDlg.cpp
	创建时间:	2009-5-17	12:00
	最后修改:	2009-5-18   23:12

	更新历史:	2009-5-17	创建文件,完成大部分解析
			2009-7-11	完成魔法,战技的解析
			2009-8-14	添加普通攻击AI显示
*********************************************************************/

#include "stdafx.h"
#include "MSEditor.h"
#include "MSEditorDlg.h"
#include <Psapi.h>
#include "ItemName.h"
#include "MagicName.h"
extern "C"
{
	#include "LzmaDec.h"
	#include "7zAlloc.h"
}

#pragma comment(lib, "Psapi.lib")

extern char	*cItemName = NULL;
extern char *cMagicName = NULL;
extern "C" HANDLE hHeap = INVALID_HANDLE_VALUE;

/////////////////////////////////////////////////////////////////////////////
// CMSEditorDlg dialog

CMSEditorDlg::CMSEditorDlg(LPSTR lpCmdLine /*=NULL*/, CWnd* pParent /*=NULL*/)
: m_pageStatus(&m_msfi, &m_pbFile, IDD_PAGE_STATUS), m_pageRisist(&m_msfi, &m_pbFile, IDD_PAGE_RISIST), 
  m_pageItem(&m_msfi, &m_pbFile, IDD_PAGE_ITEM), m_pageTrophy(&m_msfi, &m_pbFile, IDD_PAGE_TROPHY), 
  m_pageAttack(&m_msfi, &m_pbFile, IDD_PAGE_SKILL), m_pageMagic(&m_msfi, &m_pbFile, IDD_PAGE_SKILL), 
  m_pageCraft(&m_msfi, &m_pbFile, IDD_PAGE_SKILL), m_pageSCraft(&m_msfi, &m_pbFile, IDD_PAGE_SKILL), 
CDialog(CMSEditorDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
	//{{AFX_DATA_INIT(CMSEditorDlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32

	m_pbFile		= NULL;
	m_lpCmdLine		= lpCmdLine;
	hHeap			= GetProcessHeap();
	m_lpArgv		= CmdLineToArgv(m_lpCmdLine, &m_iArgc);
	m_strFilePath	= m_lpArgv[0];
	m_hFile			= INVALID_HANDLE_VALUE;

	ZeroMemory(&m_msfi, sizeof(m_msfi));

	UInt64	outSize64;
	SizeT outSize, inSize;
	Lzma86_GetUnpackSize((Byte *)_ITEMNAMES_LZMA_, sizeof(_ITEMNAMES_LZMA_), &outSize64);
	outSize = (SizeT)outSize64;
	inSize = sizeof(_ITEMNAMES_LZMA_);
	cItemName = (char *)HeapAlloc(hHeap, 0, outSize);
	Lzma86_Decode((Byte *)cItemName, &outSize, (Byte *)_ITEMNAMES_LZMA_, &inSize);

	Lzma86_GetUnpackSize((Byte *)_MAGICNAMES_LZMA_, sizeof(_MAGICNAMES_LZMA_), &outSize64);
	outSize = (SizeT)outSize64;
	inSize = sizeof(_MAGICNAMES_LZMA_);
	cMagicName = (char *)HeapAlloc(hHeap, 0, outSize);
	Lzma86_Decode((Byte *)cMagicName, &outSize, (Byte *)_MAGICNAMES_LZMA_, &inSize);
}

void CMSEditorDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CMSEditorDlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CMSEditorDlg, CDialog)
	//{{AFX_MSG_MAP(CMSEditorDlg)
	ON_WM_PAINT()
	ON_WM_DESTROY()
	ON_WM_DROPFILES()
	ON_WM_QUERYDRAGICON()
	ON_COMMAND(IDC_OPEN, OnOpenFile)
	ON_COMMAND(IDC_SAVE, OnSaveFile)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CMSEditorDlg message handlers

BOOL CMSEditorDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	DragAcceptFiles();
	
	CEdit *pEdit;
	LOGFONT lfLogFont = {0};

	pEdit = (CEdit *)GetDlgItem(IDC_FILE);
	m_pFont	= pEdit->GetFont();
	m_pFont->GetLogFont(&lfLogFont);
	lfLogFont.lfHeight -= 3;
	m_pFont->CreateFontIndirect(&lfLogFont);
	pEdit->SetFont(m_pFont);

	for (WORD wID = IDC_FILE + 1; wID != IDC_AS + 1; ++wID)
	{
		GetDlgItem(wID)->SetFont(m_pFont);
	}

	TCITEM tci;
	RECT rcSheet, rcName;

	GetDlgItem(IDC_S_NAME)->GetWindowRect(&rcName);
	GetDlgItem(IDC_STATIC_DATA)->GetWindowRect(&rcSheet);
	ScreenToClient(&rcName);
	ScreenToClient(&rcSheet);

	m_Sheet.AddPage(&m_pageStatus);
	m_Sheet.AddPage(&m_pageRisist);
	m_Sheet.AddPage(&m_pageItem);
	m_Sheet.AddPage(&m_pageTrophy);
	m_Sheet.AddPage(&m_pageAttack);
	m_Sheet.AddPage(&m_pageMagic);
	m_Sheet.AddPage(&m_pageCraft);
	m_Sheet.AddPage(&m_pageSCraft);
	m_Sheet.Create(this, WS_CHILD, WS_EX_CONTROLPARENT);

	tci.mask    = TCIF_TEXT;
	tci.pszText = _T("普通攻击");
	m_Sheet.GetTabControl()->SetItem(m_Sheet.GetPageIndex(&m_pageAttack), &tci);
	tci.pszText = _T("普通战技");
	m_Sheet.GetTabControl()->SetItem(m_Sheet.GetPageIndex(&m_pageCraft), &tci);
	tci.pszText = _T("S技");
	m_Sheet.GetTabControl()->SetItem(m_Sheet.GetPageIndex(&m_pageSCraft), &tci);

	m_Sheet.SetWindowPos(NULL, 
		rcSheet.left + 10, 
		rcName.bottom + 10, 
		rcSheet.right - rcSheet.left - 25, 
		rcSheet.bottom - rcName.bottom - rcName.bottom + rcName.top + 6, 
		SWP_NOZORDER|SWP_SHOWWINDOW);

	if (m_iArgc != 0)
	{
		if (OpenFile() == true)
		{
			Display();
		}
	}

	m_Sheet.SetActivePage(&m_pageCraft);
	EmptyWorkingSet((HANDLE)-1);
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CMSEditorDlg::OnPaint() 
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

void CMSEditorDlg::OnDestroy()
{
	if (m_pbFile != NULL)
	{
		CloseFile();
	}
	m_Sheet.DestroyWindow();
	HeapFree(hHeap, 0, cItemName);
	HeapFree(hHeap, 0, cMagicName);
	CDialog::OnDestroy();
}

HCURSOR CMSEditorDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CMSEditorDlg::OnDropFiles(HDROP hDrop)
{
	TCHAR szDropFilePath[MAX_PATH] = {0};
	DragQueryFile(hDrop, 0, szDropFilePath, sizeof(szDropFilePath));
	if (*szDropFilePath)
	{
		m_strFilePath = szDropFilePath;
		if (OpenFile() == true)
		{
			Display();
		}
	}
}

void CMSEditorDlg::CloseFile()
{
	if (m_hFile == INVALID_HANDLE_VALUE)
		return;

	HeapFree(hHeap, 0, m_pbFile);
	HeapFree(hHeap, 0, m_msfi.lpSkillName);
	HeapFree(hHeap, 0, m_msfi.lpSkillDescription);
	m_pbFile = NULL;
	m_hFile  = INVALID_HANDLE_VALUE;
}

bool CMSEditorDlg::OpenFile()
{
	DWORD dwRead;
	
	if (m_pbFile != NULL)
	{
		CloseFile();
	}

	SetDlgItemText(IDC_FILE, m_strFilePath);
	m_hFile = CreateFile(m_strFilePath, 
		GENERIC_READ, 
		FILE_SHARE_READ, 
		NULL, 
		OPEN_EXISTING, 
		FILE_ATTRIBUTE_NORMAL, 
		NULL);
	if (m_hFile == INVALID_HANDLE_VALUE)
	{
		return false;
	}

	m_dwFileSize = GetFileSize(m_hFile, NULL);
	if (m_dwFileSize > ((100 << 10) << 10))
	{
		if (IDCANCEL == 
			MessageBox(TEXT("文件大于100兆, 确定要打开吗?"), 0, 0x40|MB_OKCANCEL))
		{
			return false;
		}
	}
	m_pbFile = (PBYTE)HeapAlloc(hHeap, 0, m_dwFileSize);
	ReadFile(m_hFile, m_pbFile, m_dwFileSize, &dwRead, NULL);
	CloseHandle(m_hFile);	
	if (IsValidMSFile(m_pbFile, m_dwFileSize) == false)
	{
		SetWindowText("非法的MS文件");
		CloseFile();
		return false;
	}
	SetWindowText(m_strFilePath);
	Parser(&m_msfi);
	return true;
}

void CMSEditorDlg::OnOpenFile()
{	
	CFileDialog FileDialog(TRUE, TEXT("._DT"), 
		m_strFilePath, 
		OFN_HIDEREADONLY, 
		TEXT("._DT文件|*._DT|所有文件(*.*)|*.*"));

	if (FileDialog.DoModal() == IDOK)
	{
		m_strFilePath = FileDialog.GetPathName();
		if (OpenFile() == true)
		{
			Display();
		}
	}
}

void CMSEditorDlg::OnSaveFile()
{
	if (m_hFile != INVALID_HANDLE_VALUE && m_pbFile != NULL)
	{
		m_hFile = CreateFile(m_strFilePath, 
					GENERIC_WRITE, 
					FILE_SHARE_WRITE, 
					NULL, 
					OPEN_ALWAYS, 
					FILE_ATTRIBUTE_NORMAL, 
					NULL);
		if (m_hFile == INVALID_HANDLE_VALUE)
		{
			MessageBox("创建文件失败.", NULL, 0x40);
			return;
		}

		DWORD dwWritten;

		WriteFile(m_hFile, m_pbFile, m_dwFileSize, &dwWritten, NULL);
	}
}

bool CMSEditorDlg::Parser(LPMSFileInfo pMsFileInfo)
{
	PBYTE pbFile = m_pbFile;

	ZeroMemory(pMsFileInfo, sizeof(*pMsFileInfo));
	pMsFileInfo->MsFileSize = m_dwFileSize;

	// dwASIndex ～ wRNG
	CopyMemory(&pMsFileInfo->ASIndex, pbFile, 0x2A);
	pbFile += 0x2A;

	pbFile += 0x2;
	pMsFileInfo->EXP		= *(WORD *)(pbFile);
	pbFile += 0x2E;
	pMsFileInfo->Resistance	= *(DWORD *)(pbFile);
	pbFile += 0xF;

	// 属性有效率, 掉落晶片数
	CopyMemory(pMsFileInfo->ConditionGuard, 
		(pbFile), 
		sizeof(pMsFileInfo->ConditionGuard) + sizeof(pMsFileInfo->Sepith));
	pbFile += 0x1B;

	// 五个装备, 四个回路
	CopyMemory(pMsFileInfo->Equip, pbFile, sizeof(pMsFileInfo->Equip) + sizeof(pMsFileInfo->Orb));
	pbFile += 0x12;

	// 普通攻击AI
	m_pageAttack.m_bySkillNum = 1;
	m_pageAttack.m_pbAIData = pbFile;
	pbFile += 0x20;

	// 魔法数
	pMsFileInfo->MagicCount = m_pageMagic.m_bySkillNum = *pbFile;
	pMsFileInfo->pbMagic = m_pageMagic.m_pbAIData = ++pbFile;
	pbFile += pMsFileInfo->MagicCount * LEN_OF_AIDATA;

	// 战技数
	pMsFileInfo->CraftCount = m_pageCraft.m_bySkillNum = *pbFile;
	pMsFileInfo->pbCraft = m_pageCraft.m_pbAIData = ++pbFile;
	pbFile += pMsFileInfo->CraftCount * LEN_OF_AIDATA;

	// S技数
	pMsFileInfo->SCraftCount = m_pageSCraft.m_bySkillNum = *pbFile;
	pMsFileInfo->pbSCraft = m_pageSCraft.m_pbAIData = ++pbFile;
	pbFile += pMsFileInfo->SCraftCount * LEN_OF_AIDATA;

	// 技能数据
	pMsFileInfo->SkillDataCount = *pbFile;
	++pbFile;
	pMsFileInfo->pbSKillData = (PBYTE *)HeapAlloc(hHeap, 0, sizeof(PBYTE) * pMsFileInfo->SkillDataCount);
	pMsFileInfo->lpSkillName = (LPSTR *)HeapAlloc(hHeap, 0, sizeof(LPSTR) * pMsFileInfo->SkillDataCount);
	pMsFileInfo->lpSkillDescription = (LPSTR *)HeapAlloc(hHeap, 0, sizeof(LPSTR) * pMsFileInfo->SkillDataCount);

	for (BYTE iSkill = 0; iSkill != pMsFileInfo->SkillDataCount; ++iSkill)
	{
		pMsFileInfo->pbSKillData[iSkill] = pbFile;
		pbFile += LEN_OF_SKILLDATA;
		pMsFileInfo->lpSkillName[iSkill] = (LPSTR)pbFile;
		pbFile += lstrlenA((LPCSTR)pbFile);		// 战技名
		++pbFile;								// 0x00
		pMsFileInfo->lpSkillDescription[iSkill] = (LPSTR)pbFile;
		pbFile += lstrlenA((LPCSTR)pbFile);		// 战技说明
		++pbFile;								// 0x00
	}

	// 逃跑数据
	pbFile += 0x4;

	// 人物名
	pMsFileInfo->lpName = (LPSTR)pbFile;
	pbFile += lstrlenA((LPCSTR)pbFile) + 1;

	// 人物说明
	pMsFileInfo->lpDescription = (LPSTR)pbFile;
	pbFile += lstrlenA((LPCSTR)pbFile) + 1;

	return true;
}

void CMSEditorDlg::Display()
{
	DWORD	dwASIndex;
	CString strTemp;

	SetDlgItemInt(IDC_LEVEL, m_msfi.Level);
	SetDlgItemInt(IDC_EXP, m_msfi.EXP);

	dwASIndex = m_msfi.ASIndex;
	__asm
	{
		mov   eax, dwASIndex;
		bswap eax;
		mov   dwASIndex, eax;
	}
	strTemp.Format("%.8X", dwASIndex);

	SetDlgItemText(IDC_AS, strTemp);
	SetDlgItemText(IDC_NAME, m_msfi.lpName);
	m_Sheet.SetActivePage(m_Sheet.GetActiveIndex());
	SetForegroundWindow();
}

bool CMSEditorDlg::IsValidMSFile(PBYTE pbFile, DWORD dwSize)
{
	bool	bBreak = false;
	PBYTE	pbTemp, pbEnd = pbFile + dwSize;

	pbTemp = pbFile + *(WORD *)pbFile;

	do if (dwSize > 0xB6)
	{
		pbTemp = pbFile + 0xB6;
		if (*pbTemp > MAX_MAGIC_NUM)	// 最大魔法数
		{
			break;
		}

		for (BYTE i = 0; i != 3 && pbTemp < pbEnd; ++i)
		{
			if (*pbTemp > 0x12)		// 最大战技数
			{
				return false;
			}
			pbTemp += *pbTemp * 0x18 + 1;
		}
		
		if (*pbTemp > 0x12)
		{
			break;
		}

		if (pbTemp < pbEnd)
		{
			for (BYTE i = 0, e = *pbTemp++; i != e && pbTemp < pbEnd; ++i)
			{
				pbTemp += 0x1C;
				for (BYTE str = 0; str != 2; ++str)
					pbTemp += lstrlenA((LPSTR)pbTemp) + 1;
			}
			if (pbTemp - 2 <= pbEnd)
			{
				return true;
			}
		}
	} while(0);	// check for MS

	return false;
}
