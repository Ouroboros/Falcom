/*******************************************************************
	作用	:	内存修改设置
	文件名	: 	MemOpt.h
	创建时间:	2009-3-17   13:04
	最后修改:	2009-3-17   13:04

	更新历史:	2009-3-17	创建文件
*********************************************************************/

#ifndef _MEMOPT_H_
#define _MEMOPT_H_

#include <vector>
#include <wx/panel.h>

class MyFrame;

class MemOpt : public wxPanel
{
public:
	MemOpt(wxNotebook *notebook, long ID, MyFrame *parent);
	virtual ~MemOpt();

protected:
	void OnRBGameVerFC(wxCommandEvent &event);
	void OnRBGameVerSC(wxCommandEvent &event);
	void OnLBSelWindow(wxCommandEvent &event);
	void OnBnSaveOption(wxCommandEvent &event);
	void OnRBGameVer3rd(wxCommandEvent &event);
	void OnBnChangeTitle(wxCommandEvent &event);
	static BOOL CALLBACK EnumWindowsProc(HWND hwnd,LPARAM lParam);

private:
	static MemOpt *This;
	BYTE m_bGameVer;

	// 选择游戏版本
	wxStaticBox *m_StaticBox;
	wxRadioButton *m_rbGameVer[3];

	// 保存, 更改标题, 改地址
	wxButton *m_bnSave,
			 *m_bnChangeTitle,
			 *m_bnChangeAddress;

	// 当前所有窗口列表
	wxListBox *m_lbWindowList;

	// 游戏标题
	wxTextCtrl *m_tcGameTitle[3];

	// 第一人HP地址
	wxTextCtrl *m_tcFirstHPAddress[3];

	// 提示文本
	wxStaticText *m_tcTipText;

	// 全局Sizer
	wxSizer *m_GSizer;

	// 存放窗口句柄
	std::vector<HWND> m_vhWnd;
	DECLARE_EVENT_TABLE()
};

#endif	/* _MEMOPT_H_ */