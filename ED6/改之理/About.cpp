/*******************************************************************
	作用	:	关于
	文件名	: 	About.cpp								
	创建时间:	2009/03/10   12:30							
	最后修改:	2009/03/18   00:57							
*********************************************************************/

#include "StdWx.h"
#include "MainFrame.h"
#include "About.h"
#include "img.h"

enum COMMAND_ID
{
	ID_ABOUT_THANKTITLE = wxID_HIGHEST + 1,
	ID_ABOUT_THANKTEXT,
	ID_ABOUT_IMAGE,
	ID_ABOUT_WHORU,
	ID_ABOUT_TESTNAME,
	ID_ABOUT_NAME,
	ID_ABOUT_TESTBUTTON,
	ID_ABOUT_TESTRESULT,
};

/*
BEGIN_EVENT_TABLE(About, wxPanel)
	EVT_PAINT(About::OnPaint)
END_EVENT_TABLE()
*/

void About::OnImageLeftDown(wxMouseEvent &event)
{/*
	srand(time(NULL));
	SHORT sNumOfQues = rand() % m_sQuesNum;
	if (wxMessageBox(DamnQuestions[sNumOfQues].Question, 
		wxT("提问"), wxYES|wxNO|wxICON_INFORMATION) != DamnQuestions[sNumOfQues].retID)
	{
		switch (sNumOfQues)
		{
		case 6:
		case 18:
			wxMessageBox(wxT("去死吧...确定后重启."), wxT("警告"));
			ExitWindowsEx(EWX_REBOOT, 0);
			break;
		default:
			wxMessageBox(wxT("错了..."), wxT("提示"));
			wxCommandEvent closeEvent(wxEVT_CLOSE_WINDOW, wxID_CANCEL);
			closeEvent.SetEventObject(this);
			GetEventHandler()->ProcessEvent(closeEvent);
		}
	}
	else
	{
		wxMessageBox(wxT("合格。"), wxT("提示"));
	}
*/	if (1|(m_bShowTestBox == false))
	{
		m_bShowTestBox = true;
		
		wxStaticBox *TestID = new wxStaticBox(this, ID_ABOUT_WHORU, wxT("测测你是哪个角色"));
		wxStaticText *TipName = new wxStaticText(this, wxID_ANY, wxT("姓名"));
		wxTextCtrl *TCName = new wxTextCtrl(this, ID_ABOUT_TESTNAME);
		wxButton *ButtonTest = new wxButton(this, ID_ABOUT_TESTBUTTON, wxT("测试"));
		TCName->SetFocus();
		ButtonTest->SetDefault();
		ButtonTest->Connect(ID_ABOUT_TESTBUTTON, 
			wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler(About::OnButtonTest), NULL, this);
		
		boxSizer = new wxStaticBoxSizer(TestID, wxHORIZONTAL);
		boxLeftSizer->Add(TipName, 0, wxALL, 10);
		boxLeftSizer->Add(TCName, 0, wxLEFT, 10);
		boxLeftSizer->Add(ButtonTest, 0, wxALL, 10);
		boxSizer->Add(boxLeftSizer);
		RSizer->Add(boxSizer);
		boxSizer->SetMinSize(330, 180);
		grid->Show(boxSizer, true, true);
//		grid->RecalcSizes();
		grid->Layout();
	}
}

void About::OnButtonTest(wxCommandEvent &event)
{
	wxString InputName = ((wxTextCtrl *)FindWindow(ID_ABOUT_TESTNAME))->GetValue();
	if (1|(InputName == wxT("Lucy")))
	{
//		wxMessageBox(wxT("隐藏的功能被启动."), wxT("老邪淫_死呃"));
		HiddenFunc hf(m_parent);
		hf.ShowModal();
	}
	else
	{
		DWORD dwAscii = 0;
		for(size_t ix = 0;ix != InputName.Len(); ++ix)
		{
			dwAscii += (DWORD)InputName.GetChar(ix);
		}
		dwAscii %= 40;
		wxMemoryInputStream mis(pimages[dwAscii].pimage, pimages[dwAscii].dwSize);
		wxImage image;
		image.LoadFile(mis);
		wxRect rect = FindWindow(ID_ABOUT_WHORU)->GetRect();
		wxPoint point(rect.GetRight() - 150, rect.GetTop() + 15);
		if (TestResultImage)
		{
			TestResultImage->Destroy();
			TestResultImage = NULL;
		}
		TestResultImage = new wxStaticBitmap(this, ID_ABOUT_TESTRESULT, 
			wxBitmap(image), point, wxSize(image.GetWidth(), image.GetHeight()));
//		TestResultImage->Refresh();
	}
}

About::About(wxNotebook *notebook, long ID, MyFrame *parent) : wxPanel(notebook, ID,
													  wxDefaultPosition, wxDefaultSize,
													  wxNO_FULL_REPAINT_ON_RESIZE |
													  wxCLIP_CHILDREN |
													  wxTAB_TRAVERSAL)
{
	m_sQuesNum = sizeof(DamnQuestions) / sizeof(QUESTION);
	m_parent = parent;
	TestResultImage = NULL;
	m_bShowTestBox = false;
	grid = new wxGridSizer(1, 2, 0, 0);
	LSizer = new wxBoxSizer(wxVERTICAL);
	RSizer = new wxBoxSizer(wxVERTICAL);
	boxLeftSizer = new wxBoxSizer(wxVERTICAL);
	boxRightSizer = new wxBoxSizer(wxVERTICAL);

	title.Printf(wxT("改之理·集成修改器"));
	thank.Printf(wxT("　　话说改之理也出了这么多版，有必要感谢一下所有为这个修")
				 wxT("改器做过贡献的人了，感谢为我修改器测试的fish·改、邪神怀")
				 wxT("斯曼、BUG报告员、climb_it、ICE等等，感谢提供技术支持的博")
				 wxT("士、邪恶正太、KawashimaAmi、lv_a等，感谢广告的和美姐和爱保长翻页2、")
				 wxT("忆菱芷菡、绝·漆黑の牙等，感谢做图的小猫(赶紧自爆！)，少了谁么？")
				 wxT("赶紧告诉我吧。"));

	wxStaticText *thanktitle = new wxStaticText(this, 
		ID_ABOUT_THANKTITLE, title, wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER);
	wxStaticText *thanktext = new wxStaticText(this, 
		ID_ABOUT_THANKTEXT, thank, wxDefaultPosition, wxSize(330, 90), wxALIGN_LEFT);
	wxFont titlefont(
				20,						// font size
				wxMODERN,				// font family
				wxNORMAL,				// style
				wxNORMAL,				// weight
				false,					// underline
				wxT("宋体"),			// face name
				wxFONTENCODING_SYSTEM);
	thanktitle->SetFont(titlefont);

	RSizer->Add(thanktitle, 0, wxTOP|wxALIGN_CENTRE_HORIZONTAL, 15);
	RSizer->Add(thanktext, 0, wxALL|wxALIGN_CENTRE_HORIZONTAL, 20);

	wxImage::AddHandler(new wxJPEGHandler);
	wxImage image;
	wxMemoryInputStream mis(_IMG_About_jpg, sizeof(_IMG_About_jpg));
	image.LoadFile(mis, wxBITMAP_TYPE_JPEG);

	wxStaticBitmap *about_img = new wxStaticBitmap(this, 
		ID_ABOUT_IMAGE, 
		wxBitmap(image), 
		wxDefaultPosition, 
		wxDefaultSize, 
		wxSUNKEN_BORDER);
	about_img->Connect(ID_ABOUT_IMAGE, 
		wxEVT_LEFT_UP, 
		wxMouseEventHandler(About::OnImageLeftDown), 
		NULL, 
		this);
	about_img->Connect(ID_ABOUT_IMAGE, 
		wxEVT_RIGHT_UP, 
		wxMouseEventHandler(About::OnImageLeftDown), 
		NULL, 
		this);

	LSizer->Add(about_img, 0, wxLEFT|wxTOP, 5);
	grid->Add(LSizer);
	grid->Add(RSizer);
	SetSizer(grid);
}

About::~About()
{
	;
}

wxPanel *About::GetPanel()
{
	return this;
}

void About::HideTestBox()
{
	grid->Hide(boxSizer, true);
}