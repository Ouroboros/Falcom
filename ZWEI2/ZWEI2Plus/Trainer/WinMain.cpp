#pragma comment(linker,"/MERGE:.data=.Kanade")

#include "CWindow.h"

MY_DLL_EXPORT CWindow* STDCALL Create()
{
    return new CWindow;
}

MY_DLL_EXPORT Void STDCALL Destroy(CWindow *wnd)
{
    delete wnd;
}