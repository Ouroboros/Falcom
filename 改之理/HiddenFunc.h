/*******************************************************************
作用	:	隐藏功能												
文件名	: 	HiddenFunc.h
创建时间:	2009/03/14   2:03							
最后修改:	2009/03/14   2:03							
*********************************************************************/
#ifndef _HIDDENFUNC_H_
#define _HIDDENFUNC_H_

#include <wx/dialog.h>
#include <wx/mstream.h>

class HiddenFunc : public wxDialog
{
	friend class About;
public:
	HiddenFunc(wxWindow *parent);
	void OnButtonImport(wxCommandEvent &event);
	bool tga2ch(PBYTE pbSrc, PBYTE pbDst, DWORD dwDstSize, const BYTE &bMode);
	bool Pixel32ToCH(PBYTE pbSrc, PBYTE pbDst, DWORD dwDstSize, const BYTE &bMode);
	virtual void OnCharHook(wxKeyEvent &event);

private:
	wxString m_TipText;
	wxSizer *m_Sizer, *m_BottomSizer;
	wxRadioBox *m_Mode;
	wxButton *m_Import;
	wxStaticText *m_StaticTipText, *m_ConvertResult;
	wxStaticBitmap *m_Bitmap;
	DECLARE_EVENT_TABLE()
};

#endif	/* _HIDDENFUNC_H_ */