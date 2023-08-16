#if !defined(AFX_MYLISTCTRL_H__F49791EA_32C3_4805_9500_3E852C80E0E3__INCLUDED_)
#define AFX_MYLISTCTRL_H__F49791EA_32C3_4805_9500_3E852C80E0E3__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// MyListCtrl.h : header file
//

/////////////////////////////////////////////////////////////////////////////
// CMyListCtrl window

class CMyListCtrl : public CListCtrl
{
public:
	static UINT m_nSelectedItem;

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMyListCtrl)
	//}}AFX_VIRTUAL

	// Generated message map functions
protected:
	//{{AFX_MSG(CMyListCtrl)
		// NOTE - the ClassWizard will add and remove member functions here.
	//}}AFX_MSG	
	afx_msg void OnCustomdraw(NMHDR *pNMHDR, LRESULT *pResult);

	DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MYLISTCTRL_H__F49791EA_32C3_4805_9500_3E852C80E0E3__INCLUDED_)
