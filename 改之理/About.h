/*******************************************************************
	作用	:	关于
	文件名	: 	About.h								
	创建时间:	2009/03/10   12:30							
	最后修改:	2009/03/16   17:13						
*********************************************************************/


#ifndef _ABOUT_H_
#define _ABOUT_H_

#include <wx/panel.h>
#include <wx/mstream.h>
#include "HiddenFunc.h"

struct QUESTION
{
	wxString Question;
	int retID;
};

static const QUESTION DamnQuestions[] =
{
	{wxT("判断题，CFD全称计算流体力学。"), wxYES},
	{wxT("判断题，PSP改之理正在制作中。"), wxNO},
	{wxT("判断题，_尐拉菲_其实是¨_尛柒晍學℡。"), wxYES},
	{wxT("判断题，fish生日是12月31日。"), wxNO},
	{wxT("判断题，lv_a提供了写轮眼的功能。"), wxNO},
	{wxT("判断题，zlzhcqblf最爱看EVA。"), wxYES},
	{wxT("判断题，改之理的作者实际是abcfy2。"), wxNO},
	{wxT("判断题，改之理可以让YSO的adol进入空轨。"), wxNO},
	{wxT("判断题，改之理使用Visual C++6.0编写。"), wxNO},
	{wxT("判断题，绝·漆黑の牙和漆黑の牙是一个人。"), wxNO},
	{wxT("判断题，绝热过程熵变不一定为0。"), wxYES},
	{wxT("判断题，某人最爱Saber和Arcueid。"), wxYES},
	{wxT("判断题，纳维-斯托克斯方程、连续性方程、能量方程是CFD求解的基础。"), wxYES},
	{wxT("判断题，你点的那幅图其实是小猫の轨迹的自画像。"), wxYES},
	{wxT("判断题，你会选否。"), -1},
	{wxT("判断题，其实这版有个隐藏的功能。"), wxYES},
	{wxT("判断题，上一版的隐藏功能密码是我爱娱乐通。"), wxNO},
	{wxT("判断题，小猫の轨迹是Loli。"), wxNO},
	{wxT("判断题，这版改之理里面植入了我亲手写的木马。"), wxNO},
};

typedef int (__stdcall *DECODEUCI) (const void *src, // 输入UCI数据指针(不能为null)
									int srclen,      // 输入UCI数据长度(不能<0)
									void *dst,       // 输出RAW数据指针(BGR或BGRA格式,可以为null,表示只返回最后3个参数)
									int dstlen,      // 输出RAW数据缓冲区的长度(不能<0)
									int *w,          // 输出图像的宽度值(可以为null)
									int *h,          // 输出图像的高度值(可以为null)
									int *b);         // 输出图像的bpp值(每像素位数,可以为null)

class MyFrame;

class About : public wxPanel
{
public:
	About(wxNotebook *notebook, long ID, MyFrame *parent);
	virtual ~About();
	wxPanel *GetPanel();
	void HideTestBox();
	void OnButtonTest(wxCommandEvent &WXUNUSED(event));
private:
	MyFrame *m_parent;
	bool m_bShowTestBox;
	SHORT m_sQuesNum;
	wxString thank, title;
	wxSizer *grid, *LSizer, *RSizer, *boxSizer, *boxLeftSizer, *boxRightSizer;
	wxStaticBitmap *TestResultImage;
	DECODEUCI DecodeUCI;

	void OnImageLeftDown(wxMouseEvent &event);
//	DECLARE_EVENT_TABLE()
};

#endif	/* _ABOUT_H_ */