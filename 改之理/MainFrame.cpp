/*******************************************************************
	作用	:	主框架
	文件名	: 	MainFrame.cpp
	创建时间:	2009/03/09   16:59
	最后修改:	2009/03/15   16:59
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"

enum ID_COMMANDS
{
		ID_MAINFRAME = wxID_HIGHEST + 1,
		ID_TAB ,								// 选项卡
		ID_TAB_MEMNORMAL,						// 内存常规修改
		ID_TAB_MEMITEM,							// 内存物品修改
		ID_TAB_MEMCRAFT,						// 内存技能修改
		ID_TAB_MEMDIALOG,						// 对话修改
		ID_TAB_MEMDIFF,							// 难度调整
		ID_TAB_BATTLEFIGURE,					// 战斗外形修改
		ID_TAB_SAVENORMAL,						// 存档常规修改
		ID_TAB_SAVEPOS,							// 存档位置修改
		ID_TAB_SAVEHANDBOOK,					// 存档手册修改
		ID_TAB_SAVEMISSION,						// 存档任务修改
		ID_TAB_SAVEITEM,						// 存档物品修改
		ID_TAB_SAVECRAFT,						// 存档战技修改
		ID_TAB_LOADSAVE,						// 读取存档
		ID_TAB_MEMOPT,							// 内存修改设置
		ID_TAB_TLHZ,							// 偷梁换柱
		ID_TAB_PACKAGE,							// 移花接木
		ID_TAB_LIMITED,							// 限定版本功能
		ID_TAB_ABOUT,							// 关于
};

static const wxChar *szTabName[] =
{
	wxT("内存常规修改"), wxT("内存物品修改"), wxT("内存技能修改"), 
	wxT("对话修改"),	 wxT("难度调整"),	  wxT("战斗外形修改"),

	wxT("存档常规修改"), wxT("存档位置修改"), wxT("存档手册修改"), 
	wxT("存档任务修改"), wxT("存档物品修改"), wxT("存档战技修改"),

	wxT("读取存档"), wxT("内存修改设置"),	wxT("偷梁换柱"), 
	wxT("移花接木"), wxT("限定版本的功能"), wxT("关于"),
};

DECLARE_APP(MyApp)
IMPLEMENT_APP(MyApp)

HWND		MyFrame::hWindow		= NULL;
wxString	MyFrame::strCurSavFile	= wxT("");
wxString	MyFrame::strCfgFileName	= wxT("");
char		*MyFrame::cSaveBuff		= NULL;

bool MyApp::OnInit()
{
	// get config file full path
	wxChar buff[_MAX_PATH];
	GetModuleFileName(GetModuleHandle(NULL), buff, sizeof(buff));
	MyFrame::strCfgFileName = buff;
	MyFrame::strCfgFileName.replace(MyFrame::strCfgFileName.Last('\\') + 1, 
		WXSIZEOF(wxT("Config.ini")), wxT("Config.ini"));

	// initialization MyFrame object frame
	MyFrame *frame = new MyFrame(wxT("改之理 Reload"));
	frame->SetSize(757, 463);
	wxSize wxFrameSize = frame->GetSize();
	frame->SetMaxSize(wxFrameSize);
	frame->SetMinSize(wxFrameSize);
	frame->CenterOnScreen();
	frame->SetWindowStyle(wxDEFAULT_FRAME_STYLE&~wxMAXIMIZE_BOX);
//	frame->ShowWithEffect(wxSHOW_EFFECT_BLEND);
	frame->Show(true);
//	frame->Refresh();

//	SetProcessWorkingSetSize(GetCurrentProcess(), -1, -1);
	EmptyWorkingSet(GetCurrentProcess());
	return true;
}

BEGIN_EVENT_TABLE(MyFrame, wxFrame)
	EVT_CLOSE(MyFrame::OnExit)
END_EVENT_TABLE()

MyFrame::MyFrame(const wxString &strTitle) : wxFrame(NULL, ID_MAINFRAME, strTitle)
{
	DWORD dwPosition = 0;
	SetIcon(wxICON(Lucy));
	m_dwTabNum = sizeof(szTabName) / 4;
	notebook = new wxNotebook(this, ID_TAB, wxDefaultPosition, wxDefaultSize, wxNB_MULTILINE);

	DlgPackage = new Package(notebook, ID_TAB_PACKAGE, this);
	notebook->InsertPage(dwPosition++, DlgPackage, wxT("移花接木"));

	DlgMemOpt = new MemOpt(notebook, ID_TAB_MEMOPT, this);
	notebook->InsertPage(dwPosition++, DlgMemOpt, wxT("内存修改设置"));

	DlgLoadSave = new LoadSave(notebook, ID_TAB_LOADSAVE, this);
	notebook->InsertPage(dwPosition++, DlgLoadSave, wxT("读取存档"));

	DlgAbout = new About(notebook, ID_TAB_ABOUT, this);
	notebook->InsertPage(dwPosition++, DlgAbout, wxT("关于"));
}

void MyFrame::OnExit(wxCloseEvent &event)
{
	if (cSaveBuff)
	{
		VirtualFree(cSaveBuff, 0, MEM_RELEASE);
	}
	Destroy();
}