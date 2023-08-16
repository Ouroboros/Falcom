#include "ed6fc.h"

#pragma comment(linker, "/EXPORT:DirectInput8Create=_ED6FC_DirectInput8Create@20")

EXTC
HRESULT
STDCALL
ED6FC_DirectInput8Create(
    HINSTANCE   hinst,
    ULONG       Version,
    REFIID      riidltf,
    PVOID*      ppvOut,
    LPUNKNOWN   punkOuter
)
{
    static TYPE_OF(ED6FC_DirectInput8Create) *DirectInput8Create;

    if (DirectInput8Create == nullptr)
    {
        ULONG       Length;
        NTSTATUS    Status;
        PVOID       dinput8;
        WCHAR       DInput8Path[MAX_NTPATH];

        Length = Nt_GetSystemDirectory(DInput8Path, countof(DInput8Path));
        CopyStruct(DInput8Path + Length, L"dinput8.dll", sizeof(L"dinput8.dll"));

        dinput8 = Ldr::LoadDll(DInput8Path);
        if (dinput8 == nullptr)
            return E_FAIL;

        LdrAddRefDll(GET_MODULE_HANDLE_EX_FLAG_PIN, dinput8);

        *(PVOID *)&DirectInput8Create = GetRoutineAddress(dinput8, "DirectInput8Create");
        if (DirectInput8Create == nullptr)
            return E_FAIL;
    }

    return DirectInput8Create(hinst, Version, riidltf, ppvOut, punkOuter);
}
