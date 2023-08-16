#ifndef _ED6AIVIEWER_H_
#define _ED6AIVIEWER_H_

#include "my_common.h"
#include <Windows.h>
#include "resource.h"

class CWindow
{
public:
    ATOM    RegisterClass(HINSTANCE hInstance, TCHAR *szClassName);
    BOOL    InitInstance(HINSTANCE hInstance, int nCmdShow, TCHAR *szClassName, TCHAR *szWindowName);
    BOOL    InitMessageHandler();
    LRESULT OnCreate    (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnChar      (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnCommand   (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnSize      (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnPaint     (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnVScroll   (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnMouseWheel(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnRButtonUp (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    LRESULT OnDestroy   (HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
    WPARAM  MessageLoop(LPMSG pMsg);

    static LRESULT CALLBACK WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

protected:
    VOID CenterWindow(HWND hWnd, HWND hWndParant);

protected:
    int       cxChar, cxCaps, cyChar, cxClient, cyClient, iVScrollPos;
    HWND      m_hWnd;
    HMENU     m_hMenuPopup, m_hMenu;
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

#endif /* _ED6AIVIEWER_H_ */