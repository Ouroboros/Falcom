/*******************************************************************
	作用	:	移花接木
	文件名	: 	Package.cpp
	创建时间:	2009-3-24   20:49
	最后修改:	2009-3-24   20:49

	更新历史:	2009-3-24	创建文件
				2009-3-25	完成布局
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"
#include "Package.h"
#include <wx/wxm>

enum ID_CONTROL
{
	ID_PKG_LISTBOX = wxID_HIGHEST + 1,
	ID_PKG_BNOPENDIR,
	ID_PKG_BNOPENDAT,
	ID_PKG_BNSAVE,
	ID_PKG_BNRESTORE,
	ID_PKG_BNPLAY,
	ID_PKG_BNCLOSEALL,
	ID_PKG_BNEXTRACT,
	ID_PKG_BNADDFILE,
	ID_PKG_BNFIND,
	ID_PKG_STATICBOX,
	ID_PKG_TCSEARCH,
	ID_PKG_COMPRESS,
	ID_PKG_NOENCODE,
	ID_PKG_DECOMPRESS,
	ID_PKG_KEEPNAME,
	ID_PKG_WARNING,
	ID_PKG_README,
};

static const wxString strReadme = wxT(\
"与上个模块作用不同,移花接木的作用\n\
在于从一个DAT文件中导出数据进入另\n\
外一个DAT,由于CH文件等算法未知,所\n\
以不能导入自定义资源进去,只能从某\n\
个文件中导出某个资源替换另外文件中\n\
的等同资源,包括WAV文件的DAT28是个\n\
例外,可以导入任意WAV文件进入DAT28\n\
(爱好配音的可以自己配音.....)如果不\n\
清楚某个文件是什么,可以用附带的解包\n\
器解开看......使用这个,甚至可以让黑\n\
骑士登陆FC/SC......另外,FC是DT08.");

static const wxString strWarning = wxT(\
"没有特殊需要请不要使用新建资源功能,这个功能会关闭\n\
\"保留文件名\"功能,没有保留文件名支持的话所有替换的\n\
资源后将不能被游戏识别,所以既要替换资源的又要写入\n\
新资源的时候务必分两步执行.");

BEGIN_EVENT_TABLE(Package, wxPanel)
//	EVT_CHECKLISTBOX(id, func)
	EVT_LISTBOX(ID_PKG_LISTBOX	, Package::OnLBShowInfo)
	EVT_BUTTON(ID_PKG_BNFIND	, Package::OnBnSearch)
	EVT_BUTTON(ID_PKG_BNOPENDIR	, Package::OnBnOpenDir)
	EVT_BUTTON(ID_PKG_BNCLOSEALL, Package::OnBnCloseAll)
END_EVENT_TABLE()

void Package::OnBnSearch(wxCommandEvent &event)
{
	int pos = m_clbFileList->FindString(m_tcSearch->GetValue(), false);
	if (pos != wxNOT_FOUND)
	{
		m_clbFileList->SetSelection(pos, true);
	}
}

void Package::OnBnOpenDir(wxCommandEvent &event)
{
	m_strDirPath = wxFileSelector(wxT("Open dir file"), wxEmptyString,
		wxEmptyString, wxT("dir"), wxT("Dir file (*.dir)|*.dir"));
	if (!m_strDirPath.IsEmpty())
	{
		OpenDirFile(m_strDirPath);
		EnableButton(true);
	}
	EmptyWorkingSet(GetCurrentProcess());
}

void Package::OpenDirFile(const wxString &strDirPath)
{	
	char	szFileName[0xD];szFileName[0xC] = 0;
	DWORD	dwDirFileNum, dwRead, dwDirOffset = 0x10, dwSize;
	HANDLE	hDir = CreateFile(strDirPath,
		GENERIC_READ,
		FILE_SHARE_READ,
		0,
		OPEN_EXISTING,
		FILE_ATTRIBUTE_NORMAL,
		NULL);
	if (hDir == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("无法打开dir文件."), wxT("警告"));
		return;
	}
	SetFilePointer(hDir, 0x8, 0, FILE_BEGIN);
	ReadFile(hDir, &dwDirFileNum, 4, &dwRead, NULL);
	if (dwRead == NULL)
	{
		wxMessageBox(wxT("读取dir失败."), wxT("警告"));
	}
	else if (dwDirFileNum > 0xFFFF)
	{
		wxMessageBox(wxT("非法的dir文件(文件数量过多)."), wxT("警告"));
	}
	else
	{
		dwSize = GetFileSize(hDir, NULL);
		m_clbFileList->Clear();
		while (dwDirFileNum--&&dwDirOffset < dwSize)
		{
			SetFilePointer(hDir, dwDirOffset, 0, FILE_BEGIN);
			ReadFile(hDir, szFileName, 0xC, &dwRead, NULL);
			m_clbFileList->Append(szFileName);
			dwDirOffset += 0x24;
		}
		m_bnSreach->SetDefault();
	}
	CloseHandle(hDir);
}

void Package::EnableButton(bool enable)
{
	for (size_t ID = ID_PKG_BNOPENDAT; ID != ID_PKG_BNFIND + 1; ++ID)
		(wxButton *)FindWindow(ID)->Enable(enable);
}

void Package::OnBnCloseAll(wxCommandEvent &event)
{
	m_clbFileList->Clear();
	m_bnOpenDir->SetDefault();
	m_StaticBox->SetLabel(wxT("解/封包器"));
	EnableButton(false);
	SetProcessWorkingSetSize(GetCurrentProcess(), -1, -1);
}

void Package::OnLBShowInfo(wxCommandEvent &event)
{
	char	cDirInfo[0x14];
	DWORD	dwRead;
	HANDLE	hDir = CreateFile(m_strDirPath,
		GENERIC_READ,
		FILE_SHARE_READ,
		0,
		OPEN_EXISTING,
		FILE_ATTRIBUTE_NORMAL,
		NULL);
	if (hDir == INVALID_HANDLE_VALUE)
	{
		wxMessageBox(wxT("无法打开dir文件."), wxT("警告"));
		return;
	}
	SetFilePointer(hDir, event.GetInt() * 0x24 + 0x20, 0, FILE_BEGIN);
	ReadFile(hDir, cDirInfo, 0x14, &dwRead, NULL);
	if (dwRead == NULL)
	{
		wxMessageBox(wxT("读取dir失败."), wxT("警告"));
		OnBnCloseAll(wxCommandEvent(wxEVT_NULL));
	}
	else
	{
		wxString strInfo;
		strInfo.Printf(wxT("文件起始位置: 0x%X, 文件大小: 0x%X bytes"), 
			*(DWORD *)(cDirInfo + 0x10), *(DWORD *)(cDirInfo));
		m_StaticBox->SetLabel(strInfo);
	}
	CloseHandle(hDir);
}

Package::Package(wxNotebook *notebook, long ID, MyFrame *parent) : wxPanel(notebook, ID,
															wxDefaultPosition, wxDefaultSize,
															wxNO_FULL_REPAINT_ON_RESIZE |
															wxCLIP_CHILDREN |
															wxTAB_TRAVERSAL)
{
	m_StaticBox = new wxStaticBox(this, ID_PKG_STATICBOX, wxT("解/封包器"));

	wxSizer *VSizer = new wxBoxSizer(wxVERTICAL),
			*HSizer = new wxBoxSizer(wxHORIZONTAL),
			*BoxSizer = new wxStaticBoxSizer(m_StaticBox, wxHORIZONTAL);
	m_GSizer = new wxBoxSizer(wxHORIZONTAL);

	// 文件列表
	m_clbFileList = new wxCheckListBox(this, ID_PKG_LISTBOX, 
		wxDefaultPosition, wxDefaultSize, 0, NULL, wxLB_SINGLE);
	VSizer->Add(m_clbFileList, 1, wxALL|wxGROW, 5);

	// 查找内容
	m_tcSearch = new wxTextCtrl(this, ID_PKG_TCSEARCH);
	HSizer->Add(m_tcSearch, 0, wxGROW|wxLEFT|wxTOP, 5);

	// 查找按钮
	m_bnSreach = new wxButton(this, ID_PKG_BNFIND, wxT("快速查找"));
	HSizer->Add(m_bnSreach, 0, wxLEFT|wxTOP|wxGROW, 5);

	VSizer->Add(HSizer);

	// 完成左半边的布局
	HSizer = new wxBoxSizer(wxHORIZONTAL);
	HSizer->Add(VSizer, 0, wxGROW, 10);

	// 开始右半边
	VSizer = new wxBoxSizer(wxVERTICAL);

	// 右半边的所有按钮
	m_bnOpenDir = new wxButton(this, ID_PKG_BNOPENDIR, wxT("打开DIR文件"));
	m_bnOpenDir->SetDefault();
	VSizer->Add(m_bnOpenDir, 0, wxTOP|wxGROW, 5);
	m_bnOpenDat = new wxButton(this, ID_PKG_BNOPENDAT, wxT("打开DAT文件"));
	VSizer->Add(m_bnOpenDat, 0, wxTOP|wxGROW, 10);
	m_bnExtract = new wxButton(this, ID_PKG_BNEXTRACT, wxT("解出此文件"));
	VSizer->Add(m_bnExtract, 0, wxTOP|wxGROW, 10);
	m_bnAddFile = new wxButton(this, ID_PKG_BNADDFILE, wxT("添加文件"));
	VSizer->Add(m_bnAddFile, 0, wxTOP|wxGROW, 10);
	m_bnSave = new wxButton(this, ID_PKG_BNSAVE, wxT("保存DAT/DIR"));
	VSizer->Add(m_bnSave, 0, wxTOP|wxGROW, 10);
	m_bnRestore = new wxButton(this, ID_PKG_BNRESTORE, wxT("还原DAT/DIR"));
	VSizer->Add(m_bnRestore, 0, wxTOP|wxGROW, 10);
	m_bnPlay = new wxButton(this, ID_PKG_BNPLAY, wxT("播放WAV(DT28)"));
	VSizer->Add(m_bnPlay, 0, wxTOP|wxGROW, 10);
	m_bnCloseAll = new wxButton(this, ID_PKG_BNCLOSEALL, wxT("关闭所有文件"));
	VSizer->Add(m_bnCloseAll, 0, wxTOP|wxGROW, 10);
	m_cbDecompress	= new wxCheckBox(this, ID_PKG_COMPRESS,		wxT("解压"));
	m_cbNoEncode	= new wxCheckBox(this, ID_PKG_NOENCODE,		wxT("不编码"));
	m_cbCompress	= new wxCheckBox(this, ID_PKG_DECOMPRESS,	wxT("压缩"));
	m_cbBackup		= new wxCheckBox(this, ID_PKG_KEEPNAME,		wxT("保留文件名"));
	VSizer->Add(m_cbDecompress, 0, wxTOP|wxLEFT|wxGROW, 10);
	VSizer->Add(m_cbNoEncode, 0, wxTOP|wxLEFT|wxGROW, 10);
	VSizer->Add(m_cbCompress, 0, wxTOP|wxLEFT|wxGROW, 10);
	VSizer->Add(m_cbBackup, 0, wxTOP|wxLEFT|wxGROW, 10);

	// 完成StaticBox
	HSizer->Add(VSizer, 0, wxGROW, 10);
	BoxSizer->Add(HSizer, 0, wxGROW|wxALL, 5);

	// 说明文字
	HSizer = new wxBoxSizer(wxVERTICAL);
	HSizer->Add(new wxStaticText(this, ID_PKG_README, strReadme), 0, wxGROW|wxALL, 10);
	HSizer->AddSpacer(150);
	HSizer->Add(new wxStaticText(this, ID_PKG_WARNING, strWarning), 0, wxGROW|wxALL, 10);
	((wxStaticText *)FindWindow(ID_PKG_WARNING))->SetForegroundColour(wxColour(206, 120, 166));

	m_GSizer->Add(BoxSizer, 0, wxGROW|wxALL, 5);
	m_GSizer->Add(HSizer, 0, wxGROW, 0);
	SetSizer(m_GSizer);
	EnableButton(false);
}

Package::~Package()
{
	;
}
