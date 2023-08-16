#include "ED6AIViewer.h"
#include "nt_api.h"

CWindow* CWindow::m_This = NULL;

THandlerArray Handlers[] =
{
    { &CWindow::OnCreate,     WM_CREATE     },
    { &CWindow::OnChar,       WM_CHAR       },
    { &CWindow::OnCommand,    WM_COMMAND    },
    { &CWindow::OnSize,       WM_SIZE       },
    { &CWindow::OnPaint,      WM_PAINT      },
    { &CWindow::OnVScroll,    WM_VSCROLL    },
    { &CWindow::OnMouseWheel, WM_MOUSEWHEEL },
    { &CWindow::OnRButtonUp,  WM_RBUTTONUP  },
    { &CWindow::OnDestroy,    WM_DESTROY    },
};

ATOM CWindow::RegisterClass(HINSTANCE hInstance, TCHAR *szClassName)
{
    WNDCLASSEX wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style			= CS_HREDRAW|CS_VREDRAW;
    wcex.lpfnWndProc	= WndProc;
    wcex.cbClsExtra		= 0;
    wcex.cbWndExtra		= 0;
    wcex.hInstance		= hInstance;
    wcex.hIcon			= LoadIcon(NULL, IDI_APPLICATION);
    wcex.hCursor		= LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground	= (HBRUSH)COLOR_WINDOWFRAME;
    wcex.lpszMenuName	= NULL;
    wcex.lpszClassName	= szClassName;
    wcex.hIconSm        = NULL;

    m_hHeap = GetProcessHeap();
    m_lpClassName = (LPTSTR)HeapAlloc(m_hHeap, 0, lstrlen(szClassName) + 1);
    lstrcpy(m_lpClassName, szClassName);

    return ::RegisterClassEx(&wcex);
}

BOOL CWindow::InitMessageHandler()
{
    MessageHandlers *pHandler;

    pHandler = (MessageHandlers *)HeapAlloc(m_hHeap, HEAP_ZERO_MEMORY, sizeof(*pHandler) * WM_USER);
    m_lpHandlers = pHandler;
    if (pHandler)
    {
        for (UINT i = 0; i != countof(Handlers); ++i)
            pHandler[Handlers[i].Message] = Handlers[i].Handler;

        return True;
    }

    return False;
}

BOOL CWindow::InitInstance(HINSTANCE hInstance, int nCmdShow, TCHAR *szClassName, TCHAR *szWindowName)
{
    HWND hWnd;

    m_This = this;
    m_hInst = hInstance;

    hWnd = CreateWindowEx(0, szClassName, szWindowName,
        WS_VSCROLL|WS_HSCROLL|WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, NULL, NULL, hInstance, NULL);

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
    HeapFree(m_hHeap, 0, m_lpHandlers);
    HeapFree(m_hHeap, 0, m_lpClassName);

    return pMsg->wParam;
}

LRESULT CALLBACK CWindow::WndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    CWindow *p = m_This;
    MessageHandlers *pHandler = (MessageHandlers *)p->m_lpHandlers;

    if (uMsg < WM_USER && pHandler[uMsg].lpfn != NULL)
    {
        LRESULT Status;

        Status = (p->*pHandler[uMsg].lpfn)(hWnd, uMsg, wParam, lParam);
        if (Status == ERROR_SUCCESS)
            return Status;
    }

    return DefWindowProc(hWnd, uMsg, wParam, lParam);
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

#include "FontSubSet.h"

LRESULT CWindow::OnCreate(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    HDC hDC;
    static CHAR szMenuText[] = "&Exit";
    TEXTMETRIC TextMetrics;

    hDC = GetDC(hWnd);
    m_hFont = CreateFont(15, 0, 0, 0, FW_NORMAL, 0, 0, 0,
        GB2312_CHARSET, 0, 0, CLEARTYPE_QUALITY, DEFAULT_PITCH, "Tahoma");
    GetTextMetrics(hDC, &TextMetrics);
    iVScrollPos = 0;
    cxChar = TextMetrics.tmAveCharWidth;
    cyChar = TextMetrics.tmHeight + TextMetrics.tmExternalLeading;
    cxCaps = (TextMetrics.tmPitchAndFamily & 1) ? (int)(cxChar + cxChar / 2) : cxChar;

    m_hMenu = CreateMenu();
    m_hMenuPopup = CreatePopupMenu();

    MENUITEMINFOA mii = { sizeof(mii) };

    mii.fMask = MIIM_ID;
    mii.fType = MFT_STRING;
    mii.dwTypeData = szMenuText;
    mii.fState = MF_ENABLED;
    mii.wID = IDM_EXIT;
    mii.cch = sizeof(szMenuText) - 1;

    AppendMenuA(m_hMenuPopup, MF_ENABLED, IDM_EXIT, szMenuText);
    AppendMenuA(m_hMenu, MF_POPUP, (UINT)m_hMenuPopup, "&File");

    if (SetMenu(hWnd, m_hMenu) == False)
    {
//        MessageBoxErrorW(hWnd, GetLastError(), NULL, 64);
    }

    ReleaseDC(hWnd, hDC);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnChar(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    if (wParam == VK_ESCAPE)
        DestroyWindow(hWnd);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnCommand(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    int wmId, wmEvent;

    wmId    = LOWORD(wParam);
    wmEvent = HIWORD(wParam);

    switch (wmId)
    {
    case IDM_EXIT:
        DestroyWindow(hWnd);
        break;

    default:
        return -1;
    }

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnSize(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    SCROLLINFO si;

    cxClient = LOWORD(lParam);
    cyClient = HIWORD(lParam);
    si.cbSize = sizeof(si);
    si.nMin   = 0;
    si.nMax   = countof(szErrorString) - 1 + cyClient / cyChar / 3;
    si.nPage  = cyClient / cyChar;
    si.fMask  = SIF_RANGE|SIF_PAGE;
    SetScrollInfo(hWnd, SB_VERT, &si, True);
    si.nMax   = 0;
    SetScrollInfo(hWnd, SB_HORZ, &si, True);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnPaint(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    int iLineCount, iColumnCount;
    PAINTSTRUCT ps;

    BeginPaint(hWnd, &ps);
    iLineCount = cyClient / cyChar;
    iColumnCount = cxClient / cxChar;
    SelectObject(ps.hdc, m_hFont);

    for (UInt32 i = 0, j = min(countof(szErrorString), iLineCount); i != j; ++i)
    {
        int len = lstrlen(szErrorString[i + iVScrollPos]);
        if (i + iVScrollPos < countof(szErrorString))
        {
            TextOut(ps.hdc, 10, i * cyChar, szErrorString[i + iVScrollPos], min(len, iColumnCount));
        }
    }

    PBYTE pbBuffer;
    DWORD dwSize;
    GLYPHMETRICS gm;
    MAT2 m2 = { {0, 1}, {0, 0}, {0, 0}, {0, 1} };
    BYTE m_matrix[32];
    char buf[100];

    dwSize = GetGlyphOutlineA(ps.hdc, 0xB8DF, GGO_BITMAP, &gm, 0, NULL, &m2);
    if (dwSize != GDI_ERROR)
    {
        pbBuffer = (PBYTE)malloc(dwSize);
        GetGlyphOutlineA(ps.hdc, 0xB8DF, GGO_BITMAP, &gm, dwSize, pbBuffer, &m2);
        for(DWORD i = 0; i < dwSize / 4; ++i)
        {
            m_matrix[i*2] = pbBuffer[4*i];
            m_matrix[i*2+1] = pbBuffer[4*i+1];

            wsprintf(buf, "0x%02X 0x%02X", m_matrix[i*2], m_matrix[i*2+1]);
        }
        free(pbBuffer);
    }

    wsprintf(buf, "%d", GetDeviceCaps(ps.hdc, PLANES) * GetDeviceCaps(ps.hdc, BITSPIXEL));
    SetWindowText(hWnd, buf);
    GetNearestColor(ps.hdc, RGB(123, 321, 123));
    EndPaint(hWnd, &ps);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnVScroll(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    SCROLLINFO si;

    si.cbSize = sizeof(si);
    si.fMask  = SIF_ALL;
    GetScrollInfo(hWnd, SB_VERT, &si);

    switch (LOWORD(wParam))
    {
    case SB_THUMBTRACK:
    case SB_THUMBPOSITION:
        si.nPos = HIWORD(wParam);
        break;

    case SB_PAGEDOWN:
        si.nPos += si.nPage;
        break;

    case SB_PAGEUP:
        si.nPos -= si.nPage;
        break;

    case SB_LINEUP:
        --si.nPos;
        break;

    case SB_LINEDOWN:
        ++si.nPos;
        break;
    }

    si.fMask = SIF_POS;
    SetScrollInfo(hWnd, SB_VERT, &si, True);
    GetScrollInfo(hWnd, SB_VERT, &si);
    if (iVScrollPos != si.nPos)
    {
        ScrollWindow(hWnd, 0, cyChar * (iVScrollPos - si.nPos), NULL, NULL);
        iVScrollPos = si.nPos;
        UpdateWindow(hWnd);
    }

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnMouseWheel(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    INT16 iScroll = HIWORD(wParam);
    SCROLLINFO si;

    si.cbSize = sizeof(si);
    si.fMask  = SIF_ALL;
    GetScrollInfo(hWnd, SB_VERT, &si);
    si.nPos -= iScroll / (INT16)WHEEL_DELTA * 3;
    if (si.nPos < 0)
    {
        si.nPos = 0;
    }
    si.fMask = SIF_POS;
    SetScrollInfo(hWnd, SB_VERT, &si, True);

    if (iVScrollPos != si.nPos)
    {
        ScrollWindow(hWnd, 0, cyChar * (iVScrollPos - si.nPos), NULL, NULL);
        iVScrollPos = si.nPos;
        UpdateWindow(hWnd);
    }

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnRButtonUp(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    POINT pt;

    pt.x = LOWORD(lParam);
    pt.y = HIWORD(lParam);
    ClientToScreen(hWnd, &pt);
    TrackPopupMenuEx(m_hMenuPopup, 0, pt.x, pt.y, hWnd, NULL);

    return ERROR_SUCCESS;
}

LRESULT CWindow::OnDestroy(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    DestroyMenu(m_hMenu);
    DestroyMenu(m_hMenuPopup);
    DeleteObject(m_hFont);
    PostQuitMessage(0);
    return ERROR_SUCCESS;
}