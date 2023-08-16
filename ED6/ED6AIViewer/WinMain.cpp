#pragma comment(linker,"/ENTRY:WinMain")

#include "ED6AIViewer.h"

ForceInline int WINAPI WinMain2(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    MSG msg;
    CWindow wnd;

    if (wnd.RegisterClass(hInstance, "AV") == 0)
    {
        MessageBoxA(NULL, "RegisterClassEx() failed.", NULL, 64);
        return False;
    }

    if (!wnd.InitMessageHandler() || !wnd.InitInstance(hInstance, nCmdShow, "AV", "AI Viewer"))
    {
        return False;
    }

    return wnd.MessageLoop(&msg);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    CHAR end;
    lpCmdLine = GetCommandLine();
    end = *lpCmdLine++ == '\"' ? '\"' : ' ';
    while (*lpCmdLine && *lpCmdLine != end) ++lpCmdLine;
    if (*lpCmdLine)
    {
        ++lpCmdLine;
        while (*lpCmdLine == ' ' || *lpCmdLine == '\t') ++lpCmdLine;
    }
    ExitProcess(WinMain2(GetModuleHandleA(NULL), 0, lpCmdLine, SW_SHOWDEFAULT));
}