#if !defined(AFX_MYPROPERTYPAGE_H__6EC6AC69_CE11_42E8_95B4_B44F92B103A6__INCLUDED_)
#define AFX_MYPROPERTYPAGE_H__6EC6AC69_CE11_42E8_95B4_B44F92B103A6__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// MyPropertyPage.h : header file
//

#include "MSFileStruct.h"

/////////////////////////////////////////////////////////////////////////////
// CMyPropertyPage dialog

#define _MASK_ 0

class CMyPropertyPage : public CPropertyPage
{
public:
	CMyPropertyPage(LPMSFileInfo pMsFileInfo = NULL, PBYTE *ppbFile = NULL, const WORD IDD = 0);

protected:
	PBYTE		*m_ppbFile;
	MSFileInfo	*m_pMsFileInfo;
	virtual BOOL OnSetActive();
	virtual void Display()	= NULL;
};

#endif