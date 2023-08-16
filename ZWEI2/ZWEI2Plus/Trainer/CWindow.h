#ifndef _ED6AIVIEWER_H_
#define _ED6AIVIEWER_H_

#include <Windows.h>
#include <TChar.h>
#include "resource.h"
#include "my_common.h"

#ifdef TRAINER_EXPORTS
    #define MY_DLL_SPEC 
#else
    #define MY_DLL_SPEC MY_DLL_IMPORT
#endif

class MY_DLL_SPEC CWindow
{
public:
    typedef LRESULT (CWindow::*F_MsgHandler)(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
public:
    CWindow();
    ~CWindow();

public:
    virtual LRESULT Show(HINSTANCE hInstance, int nShow, TCHAR *szClassName, TCHAR *szWindowName);
    LRESULT OnCreate     (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnKeyDown    (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnRButtonUp  (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnLButtonUp  (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnLButtonDown(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnCommand    (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnPaint      (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnDestroy    (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    WPARAM  MessageLoop  (LPMSG pMsg);
    LRESULT CALLBACK RealWndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

    static LRESULT CALLBACK WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

protected:
    void CenterWindow(HWND hWnd, HWND hWndParant);
    BOOL InitMessageHandler(LPVOID Handlers, DWORD dwHandlerCount, UINT uMsgMax);
    ATOM RegisterClass(HINSTANCE hInstance, TCHAR *szClassName);
    LRESULT InitInstance(HINSTANCE hInstance, int nCmdShow, TCHAR *szClassName, TCHAR *szWindowName);

protected:
    int       cxChar, cxCaps, cyChar, cxClient, cyClient, iVScrollPos;
    UINT      m_uMsgMax;
    HWND      m_hWnd;
    HMENU     m_hMenuMain, m_hMenuPopup;
    HFONT     m_hFont;
    HANDLE    m_hHeap;
    HINSTANCE m_hInst;
    LPVOID    m_lpHandlers;
    LPTSTR    m_lpClassName;

    static CWindow *m_This;
};

typedef union
{
    LRESULT (CWindow::*lpfn)     (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

    LRESULT (CWindow::*OnCreate) (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT (CWindow::*OnChar)   (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT (CWindow::*OnCommand)(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT (CWindow::*OnSize)   (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT (CWindow::*OnPaint)  (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT (CWindow::*OnVScroll)(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT (CWindow::*OnDestroy)(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
} MsgHandlers, MessageHandlers;

typedef struct
{
    MsgHandlers Handler;
    UINT        Message;
} THandlerArray;

typedef struct _tagMenuItem
{
    UINT   uIDNewItem;
    UINT   uFlags;
    LPCSTR lpNewItem;
    struct _tagMenuItem *pSubMenuItem;
    DWORD  dwSubMenuCount;
} TMenuItem;

#endif /* _ED6AIVIEWER_H_ */