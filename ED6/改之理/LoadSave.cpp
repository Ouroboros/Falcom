/*******************************************************************
	作用	:	读取存档
	文件名	: 	LoadSave.cpp
	创建时间:	2009-3-15   13:57
	最后修改:	2009-3-15   13:57

	更新历史:	2009-3-15	创建文件,完成所有基本功能
				2009-3-16	放大预览图片
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"
#include <wx/mstream.h>
#include "LoadSave.h"
#include "my_image.h"

const DWORD dwInPrevImageSize	= 0x9600,
			dwOutPrevImageSize	= 0x12C36;

// 存档缩略图BMP头

unsigned char bmpheader[] =
{//	 00    01    02    03    04    05    06    07    08    09    0A    0B    0C    0D    0E    0F
	0x42, 0x4D, 0x36, 0x2C, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x36, 0x00, 0x00, 0x00, 0x28, 0x00,
	0x00, 0x00, 0xA0, 0x00, 0x00, 0x00, 0x78, 0x00, 0x00, 0x00, 0x01, 0x00, 0x20, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
};

enum COMMAND_ID
{
	ID_LOADSAVE_SAVLIST = wxID_HIGHEST + 1,
	ID_LOADSAVE_GAMEVER,
	ID_LOADSAVE_CHANGEPATH,
	ID_LOADSAVE_SAVESET,
	ID_LOADSAVE_SAVEPREV,
};

static const wxString DefaultSaveFolder[] =
{
	wxT("ED6"),
	wxT("ED_SORA2"),
	wxT("ED_SORA3"),
};

static const wxString strSection = wxT("SavePath");

static wxString strVersions[] =
{
	wxT("FC "),
	wxT("\0"),
	wxT("SC "),
	wxT("\0"),
	wxT("3rd"),
};

BEGIN_EVENT_TABLE(LoadSave, wxPanel)
	EVT_LISTBOX(ID_LOADSAVE_SAVLIST,		LoadSave::OnLBPrevSave)
	EVT_LISTBOX_DCLICK(ID_LOADSAVE_SAVLIST,	LoadSave::OnLBDClickOpenSave)
	EVT_RADIOBOX(ID_LOADSAVE_GAMEVER,		LoadSave::OnRBChangeGameVer)
	EVT_BUTTON(ID_LOADSAVE_SAVESET,			LoadSave::OnButtonSaveSetting)
	EVT_BUTTON(ID_LOADSAVE_CHANGEPATH,		LoadSave::OnButtonChangePath)
END_EVENT_TABLE()

LoadSave::LoadSave(wxNotebook *notebook, long ID, MyFrame *parent) : wxPanel(notebook, ID,
													  wxDefaultPosition, wxDefaultSize,
													  wxNO_FULL_REPAINT_ON_RESIZE |
													  wxCLIP_CHILDREN |
													  wxTAB_TRAVERSAL)
{
	BNSizer		= new wxBoxSizer(wxHORIZONTAL);
	RSizer		= new wxBoxSizer(wxVERTICAL);
	GSizer		= new wxBoxSizer(wxHORIZONTAL);
	m_sbSavePrev = NULL;

	m_lbSaveList = new wxListBox(this, ID_LOADSAVE_SAVLIST, wxDefaultPosition, wxSize(175, 315));

	m_rbChooseGameVer = new wxRadioBox(this, ID_LOADSAVE_GAMEVER, wxT("版本"),
		wxDefaultPosition, wxDefaultSize, WXSIZEOF(strVersions), strVersions, 1/*, wxRA_SPECIFY_COLS*/);
	m_rbChooseGameVer->Show(1, false);
	m_rbChooseGameVer->Show(3, false);
	m_brbCurSel = GetPrivateProfileInt(strSection, wxT("Default"), 2, MyFrame::strCfgFileName) << 1;
	m_brbCurSel = m_brbCurSel > 4 ? 4 : m_brbCurSel;
	m_rbChooseGameVer->SetSelection(m_brbCurSel);

	OnRBChangeGameVer(wxCommandEvent(wxEVT_COMMAND_RADIOBOX_SELECTED, wxID_ANY));

	m_bnChangePath	= new wxButton(this, ID_LOADSAVE_CHANGEPATH, wxT("更改默认路径"));
	m_bnSaveOpt		= new wxButton(this, ID_LOADSAVE_SAVESET, wxT("保存设置"));

	RSizer->Add(m_rbChooseGameVer, 0, wxGROW|wxALL, 10);
	BNSizer->Add(m_bnChangePath, 0, wxALL, 0);
	BNSizer->Add(m_bnSaveOpt, 0, wxLEFT, 10);
	RSizer->Add(BNSizer, 0, wxRIGHT&~wxBOTTOM|wxALIGN_RIGHT, 10);
	GSizer->Add(m_lbSaveList, 0, wxALL|wxGROW, 10);
	GSizer->Add(RSizer, 1, wxGROW);
	SetSizer(GSizer);
}

LoadSave::~LoadSave()
{
	;
}

void LoadSave::OnButtonChangePath(wxCommandEvent &event)
{
	wxString strNewDir;
	strNewDir.Printf(wxT("请选择新的%s存档目录."), strVersions[m_brbCurSel]);
	strNewDir.Replace(wxT(" "), wxT(""));
	strNewDir = wxDirSelector(strNewDir, m_strSaveFolder[m_brbCurSel / 2]);
	if (!strNewDir.IsEmpty())
	{
		m_strSaveFolder[m_brbCurSel / 2] = strNewDir;
		m_rbChooseGameVer->SetString(m_brbCurSel,
		strVersions[m_brbCurSel] + wxT("     ") + strNewDir);
		RefreshSaveList();
	}
}

void LoadSave::OnButtonSaveSetting(wxCommandEvent &event)
{
	wxString strSetting;
	strSetting.Printf(wxT("%u"), m_brbCurSel / 2);
	WritePrivateProfileString(strSection,
			wxT("Default"), strSetting, MyFrame::strCfgFileName);
	for (BYTE ix = 0; ix != 3; ++ix)
	{
		WritePrivateProfileString(strSection,
			strVersions[ix * 2], m_strSaveFolder[ix], MyFrame::strCfgFileName);
	}
}

void LoadSave::OnLBDClickOpenSave(wxCommandEvent &event)
{
	DWORD nBytesRead;
	HANDLE hSave = CreateFile(m_lbSaveList->GetStringSelection(),
		GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hSave == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("无法打开存档."));
	}
	else
	{
		if (MyFrame::cSaveBuff == NULL)
		{
			MyFrame::cSaveBuff = (char *)VirtualAlloc(NULL, dw3rdSavSize, MEM_COMMIT, PAGE_READWRITE);
		}
		ReadFile(hSave, MyFrame::cSaveBuff, dw3rdSavSize, &nBytesRead, NULL);
		CloseHandle(hSave);
		if (nBytesRead == 0)
		{
			wxMessageBox(wxT("无法读取存档."));
		}
		else
		{
			SetWindowText(GetActiveWindow(), wxT("当前存档: ") +
				m_strSaveFolder[m_brbCurSel / 2] + wxT("\\") + m_lbSaveList->GetStringSelection());
		}
	}
}

void LoadSave::OnLBPrevSave(wxCommandEvent &event)
{
	byte_t *ucInPrevBuff, *ucOutPrevBuff ,*p;
	DWORD nBytesRead;
	wxString strSavPath = m_lbSaveList->GetStringSelection();
	HANDLE hSave = CreateFile(strSavPath,
		GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hSave == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("无法打开存档."));
	}
	ucInPrevBuff		= (byte_t *) malloc(dwInPrevImageSize);
	ucOutPrevBuff		= (byte_t *) malloc(dwOutPrevImageSize + 0x36);
	p = ucOutPrevBuff + 0x36;
	memcpy(ucOutPrevBuff, bmpheader, 0x36);
	SetFilePointer(hSave, 0x2C, 0, FILE_BEGIN);
	ReadFile(hSave, ucInPrevBuff, dwInPrevImageSize, &nBytesRead, NULL);
	while (nBytesRead)
	{
		for (int w = 0; w != 160; w += 1, p += 4)
		{	// 转换的同时进行垂直翻转
			Pixel4444To32(p, *(uint16 *)(ucInPrevBuff + nBytesRead - 160 * 2 + w * 2));
		}
		nBytesRead -= 0x140;
	}
	CloseHandle(hSave);
	wxRect rect = m_rbChooseGameVer->GetRect();
	wxPoint point(rect.GetLeft(), rect.GetBottom() + 20);
	wxMemoryInputStream mis(ucOutPrevBuff, dwOutPrevImageSize);
	wxImage image;
	image.LoadFile(mis);
//	image = image.Scale(180, 135, wxIMAGE_QUALITY_HIGH);
	if (m_sbSavePrev)
	{
		m_sbSavePrev->Destroy();
		m_sbSavePrev = NULL;
	}
	m_sbSavePrev = new wxStaticBitmap(this, ID_LOADSAVE_SAVEPREV,
		wxBitmap(image), point, wxSize(image.GetWidth(), image.GetHeight()));
	free(ucInPrevBuff);
	free(ucOutPrevBuff);
}

void LoadSave::OnRBChangeGameVer(wxCommandEvent &event)
{
	if (m_sbSavePrev)
	{
		m_sbSavePrev->Destroy();
		m_sbSavePrev = NULL;
	}
	m_brbCurSel = m_rbChooseGameVer->GetSelection();

	wxChar PathBuff[_MAX_PATH];
	HANDLE hConfig = CreateFile(MyFrame::strCfgFileName,
		GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	if (hConfig == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("无法打开Config.ini"));
	}
	else
	{
		CloseHandle(hConfig);
	}

	for (BYTE ix = 0; ix != 3; ++ix)
	{
		if (!GetPrivateProfileString(strSection,
			strVersions[ix * 2], NULL, PathBuff, sizeof(PathBuff), MyFrame::strCfgFileName))
		{
			GetEnvironmentVariable(wxT("APPDATA"), PathBuff, sizeof(PathBuff));
			m_strSaveFolder[ix] = PathBuff;
			m_strSaveFolder[ix] +=  wxT("\\Falcom\\") + DefaultSaveFolder[ix];
		}
		else
		{
			m_strSaveFolder[ix] = PathBuff;
			if (m_strSaveFolder[ix].GetChar(m_strSaveFolder[ix].Length() - 1) == '\\')
			{
				m_strSaveFolder[ix].RemoveLast();
			}
		}
		m_rbChooseGameVer->SetString(ix * 2, strVersions[ix * 2] + wxT("     ") + m_strSaveFolder[ix]);
	}

	RefreshSaveList();
}

void LoadSave::RefreshSaveList()
{
	HANDLE hFindFile;
	WIN32_FIND_DATA winfd;
	m_lbSaveList->Clear();
	hFindFile = FindFirstFile(m_strSaveFolder[m_brbCurSel / 2] + wxT("\\*.sav"), &winfd);
	if (hFindFile != INVALID_HANDLE_VALUE)
	{
		m_lbSaveList->Append(winfd.cFileName);
		while (FindNextFile(hFindFile, &winfd))
		{
			m_lbSaveList->Append(winfd.cFileName);
		}
		FindClose(hFindFile);
	}
	SetCurrentDirectory(m_strSaveFolder[m_brbCurSel / 2]);
}