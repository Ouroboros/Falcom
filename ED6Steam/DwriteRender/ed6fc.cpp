// this file must be compiled under zh-CN locale

#pragma comment(linker, "/ENTRY:DllMain")
//#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
//#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(linker, "/EXPORT:CreateDWriteRenderer=_CreateDWriteRenderer@12")
#pragma comment(linker, "/EXPORT:DWriteRendererDrawRune=_DWriteRendererDrawRune@24")

#include "ed6fc.h"
#include "ml.cpp"
#include "DWriteRenderer.h"

#pragma comment(lib, "dwrite.lib")
#pragma comment(lib, "d2d1.lib")

ML_OVERLOAD_NEW

EXTC DWriteRenderer* NTAPI CreateDWriteRenderer(PCWSTR FontPath, PCWSTR FaceName, ULONG FontSize)
{
    DWriteRenderer* renderer;

    renderer = new DWriteRenderer();
    if (renderer == nullptr)
        return nullptr;

    renderer->Initialize(FontPath, FaceName, FontSize);

    return renderer;
}

EXTC NTSTATUS NTAPI DWriteRendererDrawRune(
        DWriteRenderer* renderer,
        WCHAR           ch,
        ULONG           color,
        PVOID           output,
        ULONG           outputStride,
        PULONG          runeWidth
    )
{
    return renderer->DrawRune(ch, color, output, outputStride, runeWidth);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}
