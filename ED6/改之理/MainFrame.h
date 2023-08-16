/*******************************************************************
	作用	:
	文件名	: 	MainFrame.h
	创建时间:	2009/03/09   16:42
	最后修改:	2009/03/15   14:04
*********************************************************************/
#ifndef _MAINFRAME_H_
#define _MAINFRAME_H_

#include "StdWx.h"
#include "About.h"
#include "LoadSave.h"
#include "MemOpt.h"
#include "Package.h"

class MyApp : public wxApp
{
public:
	virtual bool OnInit();
};

const DWORD dw3rdSavSize = 167792;		// max

class MyFrame : public wxFrame
{
public:
	static HWND		hWindow;
	static wxString	strCurSavFile;
	static wxString	strCfgFileName;
	static char		*cSaveBuff;

public:
    MyFrame(const wxString &strTitle);

private:
	DWORD m_dwTabNum;
	About *DlgAbout;
	MemOpt *DlgMemOpt;
	Package *DlgPackage;
	LoadSave *DlgLoadSave;
	wxNotebook *notebook;

	void OnExit(wxCloseEvent &event);
	// any class wishing to process wxWidgets events must use this macro
	DECLARE_EVENT_TABLE()
};
#endif	/* _MAINFRAME_H_ */