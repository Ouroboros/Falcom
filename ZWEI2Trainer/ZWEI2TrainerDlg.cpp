/*******************************************************************
	作用	:	各菜单功能												
	文件名	: 	ZWEI2TrainerDlg.cpp								
	创建时间:	2009/02/24   14:19							
	最后修改:	2009/02/26   19:23							
*********************************************************************/

// ZWEI2TrainerDlg.cpp : implementation file
//

#include "stdafx.h"
#include <Psapi.h>
#include "ZWEI2Trainer.h"
#include "CInputBoxDlg.h"
#include "ZWEI2TrainerDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CZWEI2TrainerDlg dialog

CZWEI2TrainerDlg::CZWEI2TrainerDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CZWEI2TrainerDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CZWEI2TrainerDlg)
	dwLevel = dwHPCur = dwHPUp = dwExp = dwNext = dwMoney = 0;
	bChecked = 0;
	m_hZwei2Wnd = NULL;
	//}}AFX_DATA_INIT
	m_cstrHP.Format("%u/%u", dwHPCur, dwHPUp);
	m_cstrMP = "0/0";
	m_cstrNextRemainder.Format("%u(%u)", dwNext, dwNext - dwExp);
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CZWEI2TrainerDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CZWEI2TrainerDlg)
	DDX_Text(pDX, IDC_STATUS_LEVEL_TEXT,	dwLevel);
	DDX_Text(pDX, IDC_STATUS_HP_TEXT,		m_cstrHP);
	DDX_Text(pDX, IDC_STATUS_MP_TEXT,		m_cstrMP);
	DDX_Text(pDX, IDC_STATUS_EXP_TEXT,		dwExp);
	DDX_Text(pDX, IDC_STATUS_NEXT_TEXT,		m_cstrNextRemainder);
	DDX_Text(pDX, IDC_STATUS_MONEY_TEXT,	dwMoney);
	//}}AFX_DATA_MAP
//	DDV_MaxChars(pDX, m_cstrHP, 43);
//	DDV_MaxChars(pDX, m_cstrNextRemainder, 44);
}

BEGIN_MESSAGE_MAP(CZWEI2TrainerDlg, CDialog)
	//{{AFX_MSG_MAP(CZWEI2TrainerDlg)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_WM_TIMER()
	ON_WM_SYSCOMMAND()
	ON_WM_CONTEXTMENU()
//	ON_MESSAGE(WM_HOTKEY,OnHotkey)
	ON_COMMAND(ID_EXIT, OnCancel)
	ON_COMMAND_EX(ID_OPENSAVEFOLDER, ProcMsg)
	ON_COMMAND_EX_RANGE(ID_REFRESHDATA, ID_JOY_ALWEN_RAGNAORIGIN, ProcMsg)
//	ON_WM_INITMENUPOPUP()
//	ON_COMMAND_EX_RANGE(ID_JOY_RAGNA_ORIGIN, ID_JOY_RAGNA_SUBARUTAPEUP, ProcMsg)
//	ON_COMMAND_EX_RANGE(ID_JOY_ALWEN_ORIGIN, ID_JOY_ALWEN_SUBARUTAPEUP, ProcMsg)
//	ON_UPDATE_COMMAND_UI_RANGE(ID_JOY_RAGNA_ORIGIN, ID_JOY_RAGNA_SUBARUTAPEUP, OnUpdateDress)
//	ON_UPDATE_COMMAND_UI_RANGE(ID_JOY_ALWEN_ORIGIN, ID_JOY_ALWEN_SUBARUTAPEUP, OnUpdateDress)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()
/*
static UINT indicators[] =
{
		ID_SEPARATOR,           // status line indicator
		ID_INDICATOR_CAPS,
		ID_INDICATOR_NUM,
		ID_INDICATOR_SCRL,
};
*/
/////////////////////////////////////////////////////////////////////////////
// CZWEI2TrainerDlg message handlers

void CZWEI2TrainerDlg::OnContextMenu(CWnd* pWnd, CPoint pos)
{
	if (pos.x == -1 && pos.y == -1)
	{
		CRect rect;
		GetClientRect(rect);
		ClientToScreen(rect);
		pos = rect.TopLeft();
		pos.Offset(85, 20);
	}
	m_Menu.GetSubMenu(1)->TrackPopupMenu(TPM_LEFTALIGN, pos.x, pos.y, pWnd);
}

BOOL CZWEI2TrainerDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	m_hAccelTable=::LoadAccelerators(AfxGetInstanceHandle(),MAKEINTRESOURCE(IDR_ACCELERATOR1));
	m_Menu.LoadMenu(IDR_MENU1);
	SetMenu(&m_Menu);
	SetTimer(1, 100, NULL);
//	RegisterHotKey(m_hZwei2Wnd, ID_LOCKHP, NULL, VK_F5);
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CZWEI2TrainerDlg::OnPaint()
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

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CZWEI2TrainerDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CZWEI2TrainerDlg::OnTimer(UINT nIDEvent)
{
	if (m_hZwei2Wnd = ::FindWindow("Kernel Class",NULL))
	{
		GetWindowThreadProcessId(m_hZwei2Wnd,&openProcId);
		hProcess = OpenProcess(PROCESS_ALL_ACCESS|PROCESS_TERMINATE|PROCESS_VM_OPERATION|PROCESS_VM_READ|PROCESS_VM_WRITE,FALSE,openProcId);
		ReadProcessMemory(hProcess, LPVOID(0x5B859C), &dwLevel, sizeof(dwLevel), NULL);
		ReadProcessMemory(hProcess, LPVOID(0x5B85A0), &dwHPUp,	sizeof(dwHPUp), NULL);
		ReadProcessMemory(hProcess, LPVOID(0x5B85CC), &dwHPCur,	sizeof(dwHPCur), NULL);
		ReadProcessMemory(hProcess, LPVOID(0x5B85D0), &dwMP,	sizeof(dwMP), NULL);
		ReadProcessMemory(hProcess, LPVOID(0x5B85AC), &dwExp,	sizeof(dwExp), NULL);
		ReadProcessMemory(hProcess, LPVOID(0x5EEEF4 + dwLevel * 0x20), &dwNext,	sizeof(dwNext), NULL);
		ReadProcessMemory(hProcess, LPVOID(0x5B85B0), &dwMoney, sizeof(dwMoney), NULL);
		m_cstrHP.Format("%u/%u", dwHPCur, dwHPUp);
		m_cstrMP.Format("%u/%u", dwMP, 0x1388);
		m_cstrNextRemainder.Format("%u(%u)", dwNext, dwNext - dwExp);
	}
	else
	{
		dwLevel = dwHPCur = dwHPUp = dwExp = dwNext = dwMoney = 0;
		m_cstrMP = "0/0";
		m_cstrHP.Format("%u/%u", dwHPCur, dwHPUp);
		m_cstrNextRemainder.Format("%u(%u)", dwNext, dwNext - dwExp);
		if (bChecked)
		{
			for (DWORD id = ID_LOCKHP; id != ID_JOY_ALWEN_RAGNAORIGIN + 1; ++id)
			{
				m_Menu.CheckMenuItem(id, MF_UNCHECKED);
			}
			bChecked = 0;
		}
	}
	UpdateData(0);
}
/*

void CZWEI2TrainerDlg::OnHotkey(WPARAM wParam, LPARAM lParam)
{
	ProcMsg(wParam);
}
*/

BOOL CZWEI2TrainerDlg::ProcMsg(UINT nID)
{
	if (nID == ID_ABOUT)
    {
        dlg.Create(IDD_INPUTBOX, this);
        dlg.ShowWindow(SW_SHOW);
/*
        GetFont();
		MessageBox("妖精的旋律", "Lucy", MB_ICONASTERISK);
*/
	}
	if (!m_hZwei2Wnd)
	{
		return FALSE;
	}
	if (nID == ID_REFRESHDATA)
	{
		MessageBox("我一直都在刷新好不...", "...", MB_ICONERROR);
	}
	else if (nID == ID_OPENSAVEFOLDER)
	{
		char SavePath[_MAX_FNAME + 18] = "explorer /select,";
		STARTUPINFO si;
		PROCESS_INFORMATION pi;
		ZeroMemory(&si,sizeof(si));
		si.cb = sizeof(si);
		ZeroMemory(&pi,sizeof(pi));
		ReadProcessMemory(hProcess, LPVOID(0x33ED7E8), SavePath + 17, _MAX_FNAME, NULL);
		if (*(SavePath + 18) != ':')
		{
			char buff[_MAX_FNAME], *p;
			GetModuleFileNameEx(hProcess, NULL, buff, _MAX_FNAME);
			for (p = buff + lstrlen(buff); *p != '\\'; --p);
			*p++ = 0;
			MoveMemory(SavePath + 17 + (p - buff), SavePath + 17, lstrlen(SavePath + 17));
			lstrcpy(SavePath + 17, buff);
			SavePath[16 + p - buff] = '\\';
		}
		CreateProcess(NULL, SavePath, NULL,	NULL, FALSE, 0, NULL, NULL, &si, &pi);
	}
	else
	{
		CString cszData[10];
		DWORD dwAddress[10], nByteToWrite[10], dwWriteTimes = 0;
		UINT uMenuStatus = m_Menu.GetMenuState(nID, MF_CHECKED);
		if (uMenuStatus == MF_UNCHECKED)
		{
			switch (nID)
			{
			case ID_LOCKHP:
				cszData[0] = "\xEB\x03";
				dwAddress[0] = 0x4153D2, nByteToWrite[0] = 2;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_LOCKMP:
				cszData[0] = "\xEB\x04";
				cszData[1] = "\xEB\x04";
				dwAddress[0] = 0x40FE39, nByteToWrite[0] = 2;
				dwAddress[1] = 0x40F4A7, nByteToWrite[1] = 2;
				dwWriteTimes = 2;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_LOCKOUGI:
				cszData[0] = "\xEB\x04";
				cszData[1] = "\x0C";
				dwAddress[0] = 0x40F476, nByteToWrite[0] = 2;
				dwAddress[1] = 0x5B8282, nByteToWrite[1] = 1;
				dwWriteTimes = 2;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_GOLD:
			case ID_STEP:{
				CInputBoxDlg InputBox;
				if (nID == ID_GOLD)
				{
					InputBox.m_cstrTipText = "请输入金钱数量";
					dwAddress[0] = 0x5B85B0;
				}
				else
				{
					InputBox.m_cstrTipText = "请输入万步计数目";
					dwAddress[0] = 0x5B4DD8;
				}
				ReadProcessMemory(hProcess, 
						LPVOID(dwAddress[0]), &InputBox.m_dwInput, 4, NULL);
				if (InputBox.DoModal() == IDOK)
				{
					InputBox.m_dwInput = InputBox.m_dwInput > INT_MAX ? INT_MAX : InputBox.m_dwInput;
					WriteProcessMemory(hProcess, 
						LPVOID(dwAddress[0]), &InputBox.m_dwInput, 4, NULL);
				}
				return TRUE;
						 }
			case ID_MAX_GOLD:
				cszData[0] = "\xFF\xFF\xFF\x7F";
				dwAddress[0] = 0x5B85B0, nByteToWrite[0] = 4;
				dwWriteTimes = 1;
				break;
			case ID_MAX_EVENTITEM:
				AppendCString(cszData[0], 27, '\x01');
				dwAddress[0] = 0x5B5CD8;
				dwWriteTimes = 1;
				break;
			case ID_MAX_CD:
				cszData[0] = "\xFF\x07";
				dwAddress[0] = 0x5B508E;
				dwWriteTimes = 1;
				break;
			case ID_MAX_TREASURE:
				cszData[0] = "\xE0\xFF\xFF\xFF\xFF\xFF\x1F";
				dwAddress[0] = 0x5B5077;
				dwWriteTimes = 1;
				break;
			case ID_MAX_USE:
				AppendCString(cszData[0], 3, '\x63');
				dwAddress[0] = 0x5B5D30;
				dwWriteTimes = 1;
				break;
			case ID_MAX_FOOD:
				AppendCString(cszData[0], 44, '\x63');
				dwAddress[0] = 0x5B5CF8;
				dwWriteTimes = 1;
				break;
			case ID_MAX_EQUIPMENT:
				AppendCString(cszData[0], 5, '\x01');
				AppendCString(cszData[1], 7, '\x01');
				dwAddress[0] = 0x5B5C58;
				dwAddress[1] = 0x5B5C60;
				dwWriteTimes = 2;
				break;
			case ID_MAX_ACCESSORYSOCKET:
				AppendCString(cszData[0], 9, '\x01');
				dwAddress[0] = 0x5B5D3E;
				dwWriteTimes = 1;
				break;
			case ID_MAX_OUGI:
				AppendCString(cszData[0], 7, '\x01');
				dwAddress[0] = 0x5B5CB8;
				dwWriteTimes = 1;
				break;
			case ID_MAX_CLOTHES:
				AppendCString(cszData[0], 8, '\x01');
				cszData[1] = cszData[0];
				dwAddress[0] = 0x5B5C70;
				dwAddress[1] = 0x5B5C80;
				dwWriteTimes = 2;
				break;
			case ID_MAX_ACCESSORY:
				AppendCString(cszData[0], 33, '\x01');
				dwAddress[0] = 0x5B5C98;
				dwWriteTimes = 1;
				break;
			case ID_MAX_GADGET:
				AppendCString(cszData[0], 15, '\x01');
				cszData[0].Replace(1, 0);
				cszData[1] = "\x01";
				dwAddress[0] = 0x5B5CC0;
				dwAddress[1] = 0x5B5CE6;
				dwWriteTimes = 2;
				break;
			case ID_MAX_PET:
				AppendCString(cszData[0], 6, '\x01');
				dwAddress[0] = 0x5B5C68;
				dwWriteTimes = 1;
				break;
			case ID_MAX_CHAR:
				cszData[0] = "\x0F\x80\xFD\x6F\x01\xFF\xFF\xBF\xFF\x7F\x7F";
				cszData[1] = "\xF0\x01\xD8\xFF\x06\xF0\xFF\xFF\xFB\xFF\xF7\x07\x01\x0F\x80\xFD\x6F\x01\xFF\xFF\xBF\xFF\x7F\x7F\x01\xF0\x01\xD8\xFF\x06\xF0\xFF\xFF\xFB\xFF\xF7\x07";
				cszData[0].Replace(1, 0);
				cszData[1].Replace(1, 0);
				dwAddress[0] = 0x5B5020;
				dwAddress[1] = 0x5B502C;
				dwWriteTimes = 2;
				break;
			case ID_MAX_MONSTER:
				cszData[0] = "\xE0\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x7F\xFF\xFF\xCF\xFF\x01";
				cszData[1] = cszData[0];
				dwAddress[0] = 0x5B5090;
				dwAddress[1] = 0x5B50A9;
				dwWriteTimes = 2;
				break;
			case ID_JOY_RAGNA_ORIGIN:
			case ID_JOY_ALWEN_RAGNAORIGIN:
				cszData[0] = "003l.it3";
				break;
			case ID_JOY_RAGNA_BLUEHAIR:
			case ID_JOY_ALWEN_RAGNABLUEHAIR:
				cszData[0] = "003b.it3";
				break;
			case ID_JOY_RAGNA_NOEYEPATCH:
			case ID_JOY_ALWEN_RAGNANOEYEPATCH:
				cszData[0] = "003c.it3";
				break;
			case ID_JOY_RAGNA_EYEPATCH:
			case ID_JOY_ALWEN_RAGNAEYEPATCH:
				cszData[0] = "003d.it3";
				break;
			case ID_JOY_RAGNA_HOTSPRING:
			case ID_JOY_ALWEN_RAGNAHOTSPRING:
				cszData[0] = "003f.it3";
				break;
			case ID_JOY_RAGNA_TAPEUP:
			case ID_JOY_ALWEN_RAGNATAPEUP:
				cszData[0] = "003g.it3";
				break;
			case ID_JOY_RAGNA_ERMINE:
			case ID_JOY_ALWEN_RAGNAERMINE:
				cszData[0] = "003i.it3";
				break;
			case ID_JOY_RAGNA_ALWENORIGIN:
			case ID_JOY_ALWEN_ORIGIN:
				cszData[0] = "004l.it3";
				break;
			case ID_JOY_RAGNA_ALWENREDHAIR:
			case ID_JOY_ALWEN_REDHAIR:
				cszData[0] = "004b.it3";
				break;
			case ID_JOY_RAGNA_ALWENHOTSPRING:
			case ID_JOY_ALWEN_HOTSPRING:
				cszData[0] = "004c.it3";
				break;
			case ID_JOY_RAGNA_ALWENSAILORSUIT:
			case ID_JOY_ALWEN_SAILORSUIT:
				cszData[0] = "004d.it3";
				break;
			case ID_JOY_RAGNA_SUBARUORIGIN:
			case ID_JOY_ALWEN_SUBARUORIGIN:
				cszData[0] = "020.it3";
				cszData[0] += '\x0';
				break;
			case ID_JOY_RAGNA_SUBARUNOSHOE:
			case ID_JOY_ALWEN_SUBARUNOSHOE:
				cszData[0] = "020b.it3";
				break;
			case ID_JOY_RAGNA_SUBARUHOTSPRING:
			case ID_JOY_ALWEN_SUBARUHOTSPRING:
				cszData[0] = "020c.it3";
				break;
			case ID_JOY_RAGNA_SUBARUTAPEUP:
			case ID_JOY_ALWEN_SUBARUTAPEUP:
				cszData[0] = "020d.it3";
				break;
			case ID_JOY_FOLLOW_NONE:
				cszData[0] += '\x0';
				cszData[1] += '\x0';
				break;
			case ID_JOY_FOLLOW_LUE:
				cszData[0] = '\x10';
				cszData[1] += '\x0';
				break;
			case ID_JOY_FOLLOW_MIA:
				cszData[0] += '\x0';
				cszData[1] = '\x10';
				break;
			case ID_OTHER_UNDEAD:
				cszData[0] = "\x90\xE9";
				dwAddress[0] = 0x419B44;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_ONEFOODUPLV:
				cszData[0] = '\xEB';
				dwAddress[0] = 0x42C3EA;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_ONEHIT:
				cszData[0] = "\x33\xC0";
				dwAddress[0] = 0x4147F8;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_QSPS:
				cszData[0] = "\x08";
				dwAddress[0] = 0x40F387;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_UNLIMITEDJUMP:
				cszData[0] = "\x80";
				dwAddress[0] = 0x40D895;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_FASTMOVE:
				cszData[0] = "\xC8";
				dwAddress[0] = 0x40D27E;
				dwWriteTimes = 1;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_EVAPLAT:
				cszData[0] = "\xEB";
				cszData[1] = "\x89\x1C\x85\xB8\x35\x5B\x01\x46\x33\xC9\x46\x88";
				cszData[2] = "\x8B\x99";
				cszData[3] = "\x91\x88\xD3\x97\x01\x88\x90\xD8\x4E\x5B\x01\x0F\x81\x1F";
				cszData[4] = "\x4B\x90\xBE\x07";
				cszData[1].Replace(1, 0);
				cszData[3].Replace(1, 0);
				dwAddress[0] = 0x408139;
				dwAddress[1] = 0x40814D;
				dwAddress[2] = 0x40820A;
				dwAddress[3] = 0x40821D;
				dwAddress[4] = 0x408215;
				dwWriteTimes = 5;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_OTHER_FIGURE:
				cszData[0] = "\xEB";
				cszData[1] = cszData[0];
				dwAddress[0] = 0x414B2F;
				dwAddress[1] = 0x4150FC;
				dwWriteTimes = 2;
				uMenuStatus = MF_CHECKED;
				break;
			case ID_SKI_LV1:
			case ID_SKI_LV2:
			case ID_SKI_LV3:
			case ID_SKI_LV4:
				cszData[0] += char(nID - ID_SKI_LV1 + 1);
				dwAddress[0] = 0x5B8118;
				dwWriteTimes = 1;
				break;
			}
		}
		else
		{
			switch (uMenuStatus = MF_UNCHECKED, nID)
			{
			case ID_LOCKHP:
				dwAddress[0] = 0x4153D2;
				cszData[0] = "\xA3\xCC";
				nByteToWrite[0] = 2;
				dwWriteTimes = 1;
				break;
			case ID_LOCKMP:
				cszData[0] = "\x29\x05";
				cszData[1] = "\x89\x3D";
				dwAddress[0] = 0x40FE39, nByteToWrite[0] = 2;
				dwAddress[1] = 0x40F4A7, nByteToWrite[1] = 2;
				dwWriteTimes = 2;
				break;
			case ID_LOCKOUGI:
				cszData[0] = "\xFE\x0D";
				dwAddress[0] = 0x40F476, nByteToWrite[0] = 2;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_UNDEAD:
				cszData[0] = "\x0F\x85";
				dwAddress[0] = 0x419B44;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_ONEFOODUPLV:
				cszData[0] = '\x7E';
				dwAddress[0] = 0x42C3EA;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_ONEHIT:
				cszData[0] = "\x2B\xC6";
				dwAddress[0] = 0x4147F8;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_QSPS:
				cszData[0] = "\x02";
				dwAddress[0] = 0x40F387;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_UNLIMITEDJUMP:
				cszData[0] = "\x8D";
				dwAddress[0] = 0x40D895;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_FASTMOVE:
				cszData[0] = "\x20";
				dwAddress[0] = 0x40D27E;
				dwWriteTimes = 1;
				break;
			case ID_OTHER_EVAPLAT:
				cszData[0] = "\x75";
				cszData[1] = "\x8A\x88\xD8\x4E\x5B\x02\x84\xC9\x75\x01\x46\x8A";
				cszData[2] = "\x3B\x91";
				cszData[3] = "\x90\xD8\x4E\x5B\x01\x3A\x91\x88\xD3\x97\x01\x0F\x82\x2A";
				cszData[4] = "\x7D\x05\xBE\x08";
				cszData[1].Replace(2, 0);
				cszData[3].Replace(1, 0);
				dwAddress[0] = 0x408139;
				dwAddress[1] = 0x40814D;
				dwAddress[2] = 0x40820A;
				dwAddress[3] = 0x40821D;
				dwAddress[4] = 0x408215;
				dwWriteTimes = 5;
				break;
			case ID_OTHER_FIGURE:
				cszData[0] = "\x74";
				cszData[1] = cszData[0];
				dwAddress[0] = 0x414B2F;
				dwAddress[1] = 0x4150FC;
				dwWriteTimes = 2;
				break;
			default:
				return TRUE;
			}
		}
		if (nID >= ID_JOY_RAGNA_ORIGIN)
		{
			uMenuStatus = MF_CHECKED;
			if (nID <= ID_JOY_RAGNA_SUBARUTAPEUP)
			{
				dwAddress[0] = 0x641553;
				dwWriteTimes = 1;
				for (DWORD id = ID_JOY_RAGNA_ORIGIN; id != ID_JOY_RAGNA_SUBARUTAPEUP + 1; ++id)
				{
					m_Menu.CheckMenuItem(id, MF_UNCHECKED);
				}
			}
			else if (nID >= ID_JOY_ALWEN_ORIGIN)
			{
				dwAddress[0] = 0x64162F;
				dwWriteTimes = 1;
				for (DWORD id = ID_JOY_ALWEN_ORIGIN; id != ID_JOY_ALWEN_RAGNAORIGIN + 1; ++id)
				{
					m_Menu.CheckMenuItem(id, MF_UNCHECKED);
				}
			}
			else
			{
				dwAddress[0] = 0x5B4FE5;
				dwAddress[1] = 0x5B4FEB;
				dwWriteTimes = 2;
				for (DWORD id = ID_JOY_FOLLOW_NONE; id != ID_JOY_FOLLOW_MIA + 1; ++id)
				{
					m_Menu.CheckMenuItem(id, MF_UNCHECKED);
				}
			}
		}
		m_Menu.CheckMenuItem(nID, uMenuStatus);
		bChecked = 1;
		for (DWORD dwTimes = 0; dwTimes != dwWriteTimes; ++dwTimes)
		{
			WriteProcessMemory(hProcess, 
				LPVOID(dwAddress[dwTimes]), 
				cszData[dwTimes], 
				cszData[dwTimes].GetLength(), 
				NULL);
		}
	}
	return TRUE;
}

/*
void CZWEI2TrainerDlg::OnUpdateDress(CCmdUI* pCmdUI) 
{
	if (pCmdUI->m_nID <= ID_JOY_RAGNA_SUBARUTAPEUP && pCmdUI->m_nID >= ID_JOY_RAGNA_ORIGIN)
		pCmdUI->SetCheck(DressCheck[0][pCmdUI->m_nID - ID_JOY_RAGNA_ORIGIN]);
	else if (pCmdUI->m_nID <= ID_JOY_ALWEN_SUBARUTAPEUP && pCmdUI->m_nID >= ID_JOY_ALWEN_ORIGIN)
		pCmdUI->SetCheck(DressCheck[1][pCmdUI->m_nID - ID_JOY_ALWEN_ORIGIN]);
	switch (dwRagna_Alwen)
	{
	case 0:
	case 1:
		pCmdUI->SetCheck(DressCheck[dwRagna_Alwen][pCmdUI->m_nID - dwFirstID]);
	}
}
*/

BOOL CZWEI2TrainerDlg::PreTranslateMessage(MSG* pMsg)
{
	int iResult;
	//针对WM_KEYDOWN消息和WM_SYSKEYDOWN消息，翻译快捷键
	switch(pMsg->message)
	{
	case WM_KEYDOWN:
	case WM_SYSKEYDOWN:
		iResult = TranslateAccelerator(m_hWnd,m_hAccelTable,pMsg);
		//翻译快捷键成功，返回TRUE
		if(iResult)
		{
			return TRUE;
		}
	}
	return CDialog::PreTranslateMessage(pMsg);
}

void CZWEI2TrainerDlg::WinHelp(DWORD dwData, UINT nCmd)
{
}

void CZWEI2TrainerDlg::OnOK()
{
}

void CZWEI2TrainerDlg::AppendCString(CString &csz, const DWORD &n, const char &c)
{
	for (DWORD t = 0; t != n; ++t, csz += c);
}
/*
void CZWEI2TrainerDlg::OnInitMenuPopup(CMenu *pPopupMenu, UINT nIndex,BOOL bSysMenu)
{
	ASSERT(pPopupMenu != NULL);

	CCmdUI state;
	state.m_pMenu = pPopupMenu;
	ASSERT(state.m_pOther == NULL);
	ASSERT(state.m_pParentMenu == NULL);

	HMENU hParentMenu;
	if (AfxGetThreadState()->m_hTrackingMenu == pPopupMenu->m_hMenu)
		state.m_pParentMenu = pPopupMenu;
	else if ((hParentMenu = ::GetMenu(m_hWnd)) != NULL)
	{
		CWnd* pParent = this;
		if (pParent != NULL &&
			(hParentMenu = ::GetMenu(pParent->m_hWnd)) != NULL)
		{
			int nIndexMax = ::GetMenuItemCount(hParentMenu);
			for (int nIndex = 0; nIndex < nIndexMax; nIndex++)
			{
				if (::GetSubMenu(hParentMenu, nIndex) == pPopupMenu->m_hMenu)
				{
					state.m_pParentMenu = CMenu::FromHandle(hParentMenu);
					break;
				}
			}
		}
	}

	state.m_nIndexMax = pPopupMenu->GetMenuItemCount();
	for (state.m_nIndex = 0; state.m_nIndex < state.m_nIndexMax;
	state.m_nIndex++)
	{
		state.m_nID = pPopupMenu->GetMenuItemID(state.m_nIndex);
		if (state.m_nID == 0)
			continue;

		ASSERT(state.m_pOther == NULL);
		ASSERT(state.m_pMenu != NULL);
		if (state.m_nID == (UINT)-1)
		{
			state.m_pSubMenu = pPopupMenu->GetSubMenu(state.m_nIndex);
			if (state.m_pSubMenu == NULL ||
				(state.m_nID = state.m_pSubMenu->GetMenuItemID(0)) == 0 ||
				state.m_nID == (UINT)-1)
			{
				continue;
			}
			state.DoUpdate(this, TRUE);
		}
		else
		{
			state.m_pSubMenu = NULL;
			state.DoUpdate(this, FALSE);
		}

		UINT nCount = pPopupMenu->GetMenuItemCount();
		if (nCount < state.m_nIndexMax)
		{
			state.m_nIndex -= (state.m_nIndexMax - nCount);
			while (state.m_nIndex < nCount &&
				pPopupMenu->GetMenuItemID(state.m_nIndex) == state.m_nID)
			{
				state.m_nIndex++;
			}
		}
		state.m_nIndexMax = nCount;
	}
}
*/
