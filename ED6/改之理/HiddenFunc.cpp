/*******************************************************************
作用	:	隐藏功能												
文件名	: 	HiddenFunc.h
创建时间:	2009-3-14   2:03
最后修改:	2009-3-15   12:34

更新历史:	2009-3-14	创建文件
			2009-3-15	添加32位BMP转4444,1555功能
			2009-3-24	批量转换
*********************************************************************/
#pragma warning(disable:4800)

#include "StdWx.h"
#include "MainFrame.h"
#include <wx/filedlg.h>
#include "HiddenFunc.h"
#include "my_image.h"
#include "img/IMG_HiddenFunc.h"

enum
{
	ID_HIDDEN_IMPORT = wxID_HIGHEST + 1,
};

const wxString kinds[] =
{
		wxT("4444:针对有渐变的Alpha图片"),
		wxT("1555:针对黑白的Alpha图片"),
};

BEGIN_EVENT_TABLE(HiddenFunc, wxDialog)
	EVT_BUTTON(ID_HIDDEN_IMPORT, HiddenFunc::OnButtonImport)
	EVT_CHAR_HOOK(HiddenFunc::OnCharHook)
END_EVENT_TABLE()

void HiddenFunc::OnCharHook(wxKeyEvent &event)
{
    if (event.m_keyCode == WXK_ESCAPE)
    {
        wxCommandEvent cancelEvent(wxEVT_COMMAND_BUTTON_CLICKED, wxID_CANCEL);
		cancelEvent.SetEventObject(this);
		GetEventHandler()->ProcessEvent(cancelEvent);
		return;
    }
    event.Skip();
}

HiddenFunc::HiddenFunc(wxWindow *parent) : wxDialog(parent, 
												wxID_ANY, 
												wxT("隐藏功能"),
												wxDefaultPosition,
												wxDefaultSize,
												wxDEFAULT_DIALOG_STYLE)
{
	m_TipText.Printf(wxT("本功能可以让你自己制作ED6全系列的单帧图片.")
					 wxT("自己依照导出的格式制作好后,插入Alpha层,")
					 wxT("保存为32位TGA或32位BMP格式,最后选择导入即可."));
	wxFont font(12,	wxMODERN, wxNORMAL, wxNORMAL, false, wxT("宋体"), wxFONTENCODING_SYSTEM);
	m_Sizer = new wxBoxSizer(wxVERTICAL);
	m_StaticTipText = new wxStaticText(this, wxID_ANY, m_TipText);
	m_Sizer->Add(m_StaticTipText, 1, wxALL&~wxBOTTOM|wxEXPAND, 11);
	m_StaticTipText->SetFont(font);

	wxMemoryInputStream mis(_IMG_HiddenFunc_jpg, sizeof(_IMG_HiddenFunc_jpg));
	wxImage image;
	image.LoadFile(mis);
	m_Bitmap = new wxStaticBitmap(this, wxID_ANY, wxBitmap(image));
	m_Sizer->Add(m_Bitmap, 0, wxALL&~wxBOTTOM, 5);

	m_BottomSizer = new wxBoxSizer(wxHORIZONTAL);
	m_Mode = new wxRadioBox(this, wxID_ANY, _T("转换参数"),
						wxDefaultPosition, wxDefaultSize, WXSIZEOF(kinds), kinds, 1);
	m_BottomSizer->Add(m_Mode, 1, wxALL, 10);

	m_ConvertResult = new wxStaticText(this, wxID_ANY, wxEmptyString);
	m_BottomSizer->Add(m_ConvertResult, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 10);

	m_Import = new wxButton(this, ID_HIDDEN_IMPORT, wxT("导入"));
	m_Import->SetDefault();
	m_BottomSizer->Add(m_Import, 0, wxALIGN_CENTER_VERTICAL|wxLEFT, 180);

	m_Sizer->Add(m_BottomSizer);
	SetSizer(m_Sizer);
	m_Sizer->Fit(m_StaticTipText);
	SetSize(518, 481);
	CenterOnParent();
}

void HiddenFunc::OnButtonImport(wxCommandEvent &event)
{
	bool bSingleFile;
	DWORD dwFileNum;
	wxString strOutput, temp;
	wxArrayString InputFiles;
	wxFileDialog fd(this, 
		wxT("Open Image files"),
		wxEmptyString, 
		wxEmptyString,
		wxT("TGA and BMP files (*.tga;*.bmp)|*.tga;*.bmp"),
		wxFD_MULTIPLE);
	fd.ShowModal();
	fd.GetPaths(InputFiles);
	dwFileNum = InputFiles.GetCount();
	bSingleFile = dwFileNum & true;
	while (dwFileNum--)
	{
		strOutput = InputFiles[dwFileNum];
		strOutput.replace(strOutput.Last('.'), WXSIZEOF(wxT("._ch")), wxT("._ch"));
		if (bSingleFile == true)
		{
			strOutput = wxFileSelector(wxT("Save _CH file"),
				(const wxChar *)NULL,
				strOutput,
				wxT("_ch"), wxT("_ch file (*._ch)|*._ch"),
				wxFD_SAVE|wxFD_OVERWRITE_PROMPT);
		}
		if (!strOutput.IsEmpty())
		{
			wxString Err;
			bool bSuccess;
			BYTE bMode;
			PBYTE pbSrc, pbDst;
			DWORD dwSrcSize, dwDstSize;
			HANDLE hSrc, hDst, hMapSrc, hMapDst;
			hSrc = CreateFile(InputFiles[dwFileNum], 
				GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
			if (hSrc == INVALID_HANDLE_VALUE)
			{
				wxString Err;
				Err.Printf(wxT("无法打开%s."), InputFiles[dwFileNum]);
				m_ConvertResult->SetLabel(Err);
				return;
			}
			dwSrcSize = GetFileSize(hSrc, NULL);
			hMapSrc = CreateFileMapping(hSrc, NULL, PAGE_READONLY, 0, dwSrcSize, NULL);
			CloseHandle(hSrc);
			if (hMapSrc == NULL)
			{
				Err.Printf(wxT("无法创建%s的映射对象."), InputFiles[dwFileNum]);
				m_ConvertResult->SetLabel(Err);
				return;
			}
			pbSrc = (PBYTE) MapViewOfFile(hMapSrc, FILE_MAP_READ, 0, 0, 0);
			CloseHandle(hMapSrc);
			if (pbSrc == NULL)
			{
				Err.Printf(wxT("无法映射%s."), InputFiles[dwFileNum]);
				m_ConvertResult->SetLabel(Err);
				return;
			}
			if (*(WORD *)pbSrc == 0x4D42)		// BMP
			{
				if (*(pbSrc + 0x1C) != 0x20)
				{
					m_ConvertResult->SetLabel(wxT("不是32位的BMP."));
					UnmapViewOfFile(pbSrc);
					SetFocus();
					return;
				}
				dwDstSize = *(DWORD *)(pbSrc + 0x12) * *(DWORD *)(pbSrc + 0x16) * 2;
			}
			else								// TGA
			{
				dwDstSize = *(WORD *)(pbSrc + 0x0C) * *(WORD *)(pbSrc + 0x0E) * 2;
			}
			hDst = CreateFile(strOutput, 
				GENERIC_READ|GENERIC_WRITE, 
				FILE_SHARE_READ|FILE_SHARE_WRITE, 
				NULL, 
				CREATE_ALWAYS, 
				FILE_ATTRIBUTE_NORMAL, 
				NULL);
			if (hDst == INVALID_HANDLE_VALUE)
			{
				Err.Printf(wxT("无法打开%s."), strOutput);
				m_ConvertResult->SetLabel(Err);
				return;
			}
			hMapDst = CreateFileMapping(hDst, NULL, PAGE_READWRITE, 0, dwDstSize, NULL);
			CloseHandle(hDst);
			if (hMapDst == NULL)
			{
				Err.Printf(wxT("无法%s的映射对象."), strOutput);
				UnmapViewOfFile(pbSrc);
				return;
			}
			pbDst = (PBYTE) MapViewOfFile(hMapDst, FILE_MAP_ALL_ACCESS, 0, 0, 0);
			CloseHandle(hMapDst);
			if (pbDst == NULL)
			{
				Err.Printf(wxT("无法映射%s."), strOutput);
				m_ConvertResult->SetLabel(Err);
				UnmapViewOfFile(pbSrc);
				return;
			}
			bMode = (m_Mode->GetSelection()) + 4;
			if (*(WORD *)pbSrc == 0x4D42)		// BMP
			{
				bSuccess = Pixel32ToCH(pbSrc, pbDst, dwDstSize, bMode);
			}
			else								// TGA
			{
				bSuccess = tga2ch(pbSrc, pbDst, dwDstSize, bMode);
			}
			if (bSuccess == true)
			{
				m_ConvertResult->SetLabel(wxT("转换完毕."));
			}
			UnmapViewOfFile(pbSrc);
			UnmapViewOfFile(pbDst);
		}
	}
	SetFocus();
}

bool HiddenFunc::Pixel32ToCH(PBYTE pbSrc, PBYTE pbDst, DWORD dwDstSize, const BYTE &bMode)
{
	pbSrc += *(pbSrc + 0x0A);
	dwDstSize /= 2;
	while (dwDstSize--)
	{
		if (bMode == 4)
		{
			Pixel32To4444((unsigned short *)pbDst, *(unsigned int *)pbSrc);
		}
		else
		{
			Pixel32To1555((unsigned short *)pbDst, *(unsigned int *)pbSrc);
		}
		pbDst += 2;
		pbSrc += 4;
	}
	return true;
}

bool HiddenFunc::tga2ch(PBYTE pbSrc, PBYTE pbDst, DWORD dwDstSize, const BYTE &bMode)
{
	pbSrc += 0x12;
	dwDstSize /= 2;
	while (dwDstSize--)
	{
		__asm
		{
			mov eax,dword ptr [pbSrc];
			mov eax,dword ptr [eax];
			mov ecx,eax;
			mov edx,eax;
			cmp bMode, 4;
			je _4444;
			shr edx,13h;
			shr ecx,0Bh;
			and edx,01Fh;
			and ecx,01Fh;
			shl edx,5h;
			add edx,ecx;
			mov ecx,eax;
			shr ecx,3h;
			shr eax,10h;
			shl edx,5h;
			and ecx,01Fh;
			and eax,8000h;
			jmp end;
_4444:		shr edx,14h;
			shr ecx,0Ch;
			and edx,0Fh;
			and ecx,0Fh;
			shl edx,4h;
			add edx,ecx;
			mov ecx,eax;
			shr ecx,10h;
			shr eax,4h;
			shl edx,4h;
			and ecx,0F000h;
			and eax,0Fh;
end:		add edx,ecx;
			add edx,eax;
			mov eax, pbDst;
			mov word ptr [eax],dx;
			add pbSrc,4;
			add pbDst,2;
		}
	}
	return true;
}