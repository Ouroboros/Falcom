/*******************************************************************
	作用	:	读取存档
	文件名	: 	LoadSave.h
	创建时间:	2009-3-15   13:54
	最后修改:	2009-3-15   13:54

	更新历史:	2009-3-15	创建文件
				2009-3-16	成员变量m_parent由wxWindow *改为MyFrame *
*********************************************************************/

#ifndef _LOADSAVE_H_
#define _LOADSAVE_H_

#include <wx/panel.h>
#include <wx/mstream.h>

class MyFrame;

class LoadSave : public wxPanel
{
public:
	LoadSave(wxNotebook *notebook, long ID, MyFrame *parent);
	virtual ~LoadSave();

protected:
	void RefreshSaveList();

	void OnLBPrevSave(wxCommandEvent &event);
	void OnRBChangeGameVer(wxCommandEvent &event);
	void OnLBDClickOpenSave(wxCommandEvent &event);
	void OnButtonChangePath(wxCommandEvent &event);
	void OnButtonSaveSetting(wxCommandEvent &event);

private:
	int m_brbCurSel;
	MyFrame *m_parent;
	wxListBox *m_lbSaveList;
	wxStaticBitmap *m_sbSavePrev;
	wxRadioBox *m_rbChooseGameVer;
	wxSizer *RSizer, *GSizer, *BNSizer;
	wxButton *m_bnChangePath, *m_bnSaveOpt;
	wxString m_strSaveFolder[3];
	DECLARE_EVENT_TABLE()
};

#endif	/* _LOADSAVE_H_ */