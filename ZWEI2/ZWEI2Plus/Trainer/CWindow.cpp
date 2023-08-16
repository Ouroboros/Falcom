#include "CWindow.h"

CWindow* CWindow::m_This = NULL;

THandlerArray Base_Handlers[] =
{
    { &CWindow::OnCreate,      WM_CREATE    },
    { &CWindow::OnKeyDown,     WM_KEYDOWN   },
    { &CWindow::OnRButtonUp,   WM_RBUTTONUP },
    { &CWindow::OnLButtonUp,   WM_LBUTTONUP },
    { &CWindow::OnLButtonDown, WM_LBUTTONDOWN },
    { &CWindow::OnCommand,     WM_COMMAND   },
    { &CWindow::OnPaint,       WM_PAINT     },
    { &CWindow::OnDestroy,     WM_DESTROY   },
};

CWindow::CWindow()
{
    m_hHeap = GetProcessHeap();
    m_lpHandlers = NULL;
    m_lpClassName = NULL;
    m_hMenuPopup = NULL;
    m_hFont = NULL;
}

CWindow::~CWindow()
{
    if (m_lpHandlers)
        HeapFree(m_hHeap, 0, m_lpHandlers);

    if (m_lpClassName)
        HeapFree(m_hHeap, 0, m_lpClassName);
}

LRESULT CWindow::Show(HINSTANCE hInstance, int nShow, TCHAR *szClassName, TCHAR *szWindowName)
{
    MSG msg;
    if (RegisterClass(hInstance, szClassName) == NULL)
        return -1;
    if (InitInstance(hInstance, nShow, szClassName, szWindowName) == False)
        return -1;

    return MessageLoop(&msg);
}

ATOM CWindow::RegisterClass(HINSTANCE hInstance, TCHAR *szClassName)
{
    WNDCLASSEX wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style			= CS_HREDRAW|CS_VREDRAW|CS_OWNDC;
    wcex.lpfnWndProc	= WndProc;
    wcex.cbClsExtra		= 0;
    wcex.cbWndExtra		= 0;
    wcex.hInstance		= hInstance;
    wcex.hIcon			= LoadIcon(NULL, IDI_APPLICATION);
    wcex.hCursor		= LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground	= (HBRUSH)COLOR_WINDOW;
    wcex.lpszMenuName	= NULL;
    wcex.lpszClassName	= szClassName;
    wcex.hIconSm        = NULL;

    m_lpClassName = (LPTSTR)HeapAlloc(m_hHeap, 0, lstrlen(szClassName) + 1);
    lstrcpy(m_lpClassName, szClassName);

    return ::RegisterClassEx(&wcex);
}

BOOL CWindow::InitMessageHandler(LPVOID Handlers, DWORD dwHandlerCount, UINT uMsgMax)
{
    MessageHandlers *pHandler;
    THandlerArray *h = (THandlerArray *)Handlers;

    pHandler = (MessageHandlers *)HeapAlloc(m_hHeap, HEAP_ZERO_MEMORY, sizeof(*pHandler) * uMsgMax);
    m_lpHandlers = pHandler;
    if (pHandler)
    {
        for (UINT i = 0; i != dwHandlerCount; ++i)
            pHandler[h[i].Message] = h[i].Handler;
        m_uMsgMax = uMsgMax;

        return True;
    }

    return False;
}

LRESULT CWindow::InitInstance(HINSTANCE hInstance, int nCmdShow, TCHAR *szClassName, TCHAR *szWindowName)
{
    HWND hWnd;
    DWORD dwStyle;

    m_This  = this;
    m_hInst = hInstance;

    if (InitMessageHandler(Base_Handlers, countof(Base_Handlers), WM_USER) == False)
        return False;

    dwStyle = WS_OVERLAPPEDWINDOW;
    dwStyle &= ~WS_MAXIMIZEBOX & ~WS_SIZEBOX;
    hWnd = CreateWindowEx(0, szClassName, szWindowName, 
                dwStyle,CW_USEDEFAULT, 0, 270, 200, NULL, NULL, hInstance, NULL);

    if (!hWnd)
    {
        return False;
    }

    CenterWindow(hWnd, NULL);
    ShowWindow(hWnd, nCmdShow);
    UpdateWindow(hWnd);
    m_hWnd = hWnd;

    return True;
}

WPARAM CWindow::MessageLoop(LPMSG pMsg)
{
    while (GetMessage(pMsg, NULL, 0, 0))
    {
        TranslateMessage(pMsg);
        DispatchMessage(pMsg);
    }

    UnregisterClass(m_lpClassName, m_hInst);

    return pMsg->wParam;
}

LRESULT CALLBACK CWindow::RealWndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    MessageHandlers *pHandler = (MessageHandlers *)m_lpHandlers;

    if (uMsg < m_uMsgMax && pHandler[uMsg].lpfn != NULL)
    {
        LRESULT Status;

        Status = (this->*pHandler[uMsg].lpfn)(hWnd, uMsg, wParam, lParam);
        if (Status == ERROR_SUCCESS)
            return Status;
    }

    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}

LRESULT CALLBACK CWindow::WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    return m_This->RealWndProc(hWnd, uMsg, wParam, lParam);
}

VOID CWindow::CenterWindow(HWND hWnd, HWND hWndParant)
{
    int  x, y;
    RECT rcWnd, rcDesktop;

    if (hWndParant == NULL)
    {
        SystemParametersInfoA(SPI_GETWORKAREA, 0, &rcDesktop, 0);
    }
    else
    {
        GetClientRect(hWndParant, &rcDesktop);
    }
    GetWindowRect(hWnd, &rcWnd);
    x = ((rcDesktop.right - rcDesktop.left) - (rcWnd.right - rcWnd.left)) >> 1;
    y = ((rcDesktop.bottom - rcDesktop.top) - (rcWnd.bottom - rcWnd.top)) >> 1;
    SetWindowPos(hWnd, HWND_TOP, x, y, 0, 0, SWP_NOSIZE);
}

HMENU WINAPI CreateCombinedMenu(TMenuItem *pMenuItem, DWORD dwItemCount, BOOL bPopup)
{
    HMENU hMenu, hSubMenu;

    if (pMenuItem == NULL || dwItemCount == 0)
        return NULL;

    hMenu = bPopup ? CreatePopupMenu() : CreateMenu();
    if (hMenu == NULL)
        return hMenu;

    for (DWORD i = 0; i != dwItemCount; ++i)
    {
        if (pMenuItem[i].uFlags & MF_POPUP)
        {
            hSubMenu = CreateCombinedMenu(pMenuItem[i].pSubMenuItem, pMenuItem[i].dwSubMenuCount, True);
            if (hSubMenu)
            {
                AppendMenuA(hMenu, pMenuItem[i].uFlags, (UINT)hSubMenu, pMenuItem[i].lpNewItem);
            }
        }
        else
        {
            AppendMenuA(hMenu, pMenuItem[i].uFlags, pMenuItem[i].uIDNewItem, pMenuItem[i].lpNewItem);
        }
    }

    return hMenu;
}

HFONT WINAPI CreateFontFromFileA(int cHeight, int cWidth, int cEscapement, int cOrientation, int cWeight, DWORD bItalic, DWORD bUnderline, DWORD bStrikeOut, DWORD iCharSet, DWORD iOutPrecision, DWORD iClipPrecision, DWORD iQuality, DWORD iPitchAndFamily, LPCSTR lpszFontName, LPCTSTR lpszFontRes)
{
    HFONT hFont;

    if (AddFontResourceExA(lpszFontName, FR_PRIVATE, 0) == 0)
        return NULL;

    hFont = CreateFontA(cHeight, cWidth, cEscapement, cOrientation, cWeight, bItalic, bUnderline, bStrikeOut, iCharSet, iOutPrecision, iClipPrecision, iQuality, iPitchAndFamily, lpszFontRes);
    if (hFont == NULL)
    {
        RemoveFontResourceExA(lpszFontName, FR_PRIVATE, 0);
    }

    return hFont;
}

LRESULT CWindow::OnCreate(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    extern TMenuItem Menu_Main[];
    extern DWORD dwMenuCount;

    HDC hDC;

    m_hMenuMain = CreateCombinedMenu(Menu_Main, dwMenuCount, False);
    if (m_hMenuMain)
    {
        m_hMenuPopup = GetSubMenu(m_hMenuMain, 1);
        SetMenu(hWnd, m_hMenuMain);
    }

    m_hFont = CreateFontFromFileA(0, 0, 0, 0, 0, 0, 0, 0, GB2312_CHARSET, 0, 0, 5, 0, "DFGirl.ttf", "»ª¿µÉÙÅ®ÎÄ×Ö");

    hDC = GetDC(hWnd);

    SetBkMode(hDC, TRANSPARENT);
    if (m_hFont)
    {
        SelectObject(hDC, m_hFont);
    }    
    SetTextColor(hDC, RGB(255, 128, 64));

    ReleaseDC(hWnd, hDC);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnKeyDown(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (wParam)
    {
    case VK_ESCAPE:
        SendMessageA(hWnd, WM_COMMAND, ID_EXIT, 0);
        break;

    case VK_F1:
        SendMessageA(hWnd, WM_COMMAND, ID_ABOUT, 0);
        break;

    case VK_APPS:
        {
            RECT rcClient;
            MENUBARINFO mbi = { sizeof(mbi) };

            GetMenuBarInfo(hWnd, OBJID_MENU, 1, &mbi);
            GetClientRect(hWnd, &rcClient);
            lParam = ((rcClient.right - rcClient.left) / 2 - (mbi.rcBar.right - mbi.rcBar.left)) 
                | (((rcClient.bottom - rcClient.top) / 2 - (mbi.rcBar.bottom - mbi.rcBar.top)) << 16);
            OnRButtonUp(hWnd, uMsg, wParam, lParam);
        }
        break;
    }

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnCommand(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    int nItemID, nMsgSrc;

    nItemID = LOWORD(wParam);
    nMsgSrc = HIWORD(wParam);

    switch (nItemID)
    {
    case ID_EXIT:
        DestroyWindow(hWnd);
        break;

    case ID_ABOUT:
        {
            LPSTR lpText;

            lpText = (LPSTR)((PBYTE)m_hInst + *(LPDWORD)((PBYTE)m_hInst + 0x3C) + 0xF8 + 1);
            MessageBoxA(hWnd, lpText, lpText, 64);
        }
        break;
    }

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnPaint(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    PAINTSTRUCT ps;
    CHAR szText[] = "TestString²âÊÔ×Ö·û´®";
    static POINT pt[] = { { 100, 10 }, { 100, 100 }, { 10, 100 }, { 10, 10 } };

    BeginPaint(hWnd, &ps);

    TextOutA(ps.hdc, 0, 10, szText, sizeof(szText) - 1);
    MoveToEx(ps.hdc, pt[countof(pt) - 1].x, pt[countof(pt) - 1].y, NULL);
    PolylineTo(ps.hdc, pt, countof(pt));

    EndPaint(hWnd, &ps);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnRButtonUp(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    POINT pt = { LOWORD(lParam), HIWORD(lParam) };

    ClientToScreen(hWnd, &pt);
    TrackPopupMenuEx(m_hMenuPopup, 0, pt.x, pt.y, hWnd, NULL);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnLButtonUp(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    SendMessageA(hWnd, WM_NCLBUTTONUP, HTCAPTION, 0);
    
    return ERROR_SUCCESS;
}

LRESULT CWindow::OnLButtonDown(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    SendMessageA(hWnd, WM_NCLBUTTONDOWN, HTCAPTION, 0);
    
    return ERROR_SUCCESS;
}

LRESULT CWindow::OnDestroy(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    if (m_hMenuMain)
        DestroyMenu(m_hMenuMain);
    if (m_hMenuPopup)
        DestroyMenu(m_hMenuPopup);
    if (m_hFont)
        DeleteObject(m_hFont);
    PostQuitMessage(0);
    return ERROR_SUCCESS;
}