
//acgn
VOID THISCALL CBattle::LoadMSFile(PMONSTER_STATUS MSData, ULONG MSFileIndex)
{
    ULONG i, v15;
    char it3Path[MAX_PATH];
    TYPE_OF(&CBattle::LoadMonsterIt3) StubLoadMonsterIt3;
    *(PVOID*)&StubLoadMonsterIt3 = (PVOID)0x00673FB3;


    for (i = 0; i < 20; ++i)
    {
        v15 = (i << 8) | 0x88000;
        if ( (MSFileIndex & 0xFFFFFF00) == ((i << 8) | 0x30088000) )
        {
            sprintf(it3Path, (const char*)0xB8FCD8, v15, v15 + 80); //"data/monster/ch%x/ch%x.it3"
            (this->*StubLoadMonsterIt3)(MSData->CharPosition, 0, it3Path);
            break;
            //sub_673FB3(i + 8, 0, &Dest);
        }
    }
    (this->*StubLoadMSFile)(MSData, MSFileIndex);
}


NAKED VOID CBattle::NakedAS_8D_5F()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0Ch];
        push	[ebp + 08h];
        call    CBattle::AS_8D_5F;
        push	009D3675h;
        retn;
    }
}

VOID THISCALL CBattle::AS_8D_5F(PMONSTER_STATUS ChrMSData)
{
    int i, start, end;
    PMONSTER_STATUS MSData;

    if (ChrMSData->CharPosition >= 8 && ChrMSData->CharPosition < 0x10)
    {
        start = 0;
        end = 4;
    }
    else
    {
        start = 8;
        end = 0x10;
    }

    for (i=start; i<end; i++)
    {
        MSData = this->GetMonsterStatus()+i;
        if (MSData->State & 0x8000)
            continue;
        UnsetCondition(MSData, 0x8000);
        SetCondition(MSData, 0, 0x8000, 0, 0);
    }
}



#if !D3D9_VER

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/EXPORT:Direct3DCreate9=d3d9.Direct3DCreate9")

#else // D3D9_VER

#include <d3d9.h>

#pragma comment(linker, "/EXPORT:Direct3DCreate9=_Arianrhod_Direct3DCreate9@4")
#pragma comment(linker, "/EXPORT:DirectInput8Create=_Arianrhod_DirectInput8Create@20")

NoInline BOOL IsCodeDecompressed()
{
    SEH_TRY
    {
        static ULONG Signature[] =
        {
            0xe9003ffa, 0x0024ca08, 0x0e8a03e9, 0x78cee900,
            0xf9e90025, 0xe900276e, 0x00225f64, 0x0c354fe9,
            0x54dae900, 0xb5e90025, 0xe900033e, 0x004ebe90
        };

        return RtlCompareMemory((PVOID)0x672020, Signature, sizeof(Signature)) == sizeof(Signature);
    }
    SEH_EXCEPT(EXCEPTION_EXECUTE_HANDLER)
    {
        return FALSE;
    }
}

EXTC IDirect3D9* STDCALL Arianrhod_Direct3DCreate9(UINT SDKVersion)
{
    static TYPE_OF(Arianrhod_Direct3DCreate9) *Direct3DCreate9;

    if (Direct3DCreate9 == nullptr)
    {
        ULONG           Length;
        NTSTATUS        Status;
        PVOID           d3d9;
        WCHAR           D3D9Path[MAX_NTPATH];

        Length = Nt_GetSystemDirectory(D3D9Path, countof(D3D9Path));
        CopyStruct(D3D9Path + Length, L"d3d9.dll", sizeof(L"d3d9.dll"));

        d3d9 = Ldr::LoadDll(D3D9Path);
        if (d3d9 == nullptr)
            return nullptr;

        LdrAddRefDll(GET_MODULE_HANDLE_EX_FLAG_PIN, d3d9);

        *(PVOID *)&Direct3DCreate9 = GetRoutineAddress(d3d9, "Direct3DCreate9");
        if (Direct3DCreate9 == nullptr)
            return nullptr;
    }

#if ENABLE_LOG
    {
        NtFileDisk f;
        f.Create(L"log.txt");
    }
#endif

    WriteLog(L"%08X\n", _ReturnAddress());

    if (IsCodeDecompressed())
    {
        DllMain(&__ImageBase, DLL_PROCESS_ATTACH, 0);
        ChangeMainWindowProc(*(HWND *)0xDB2E54);
    }

    return Direct3DCreate9(SDKVersion);
}

EXTC
HRESULT
STDCALL
Arianrhod_DirectInput8Create(
    HINSTANCE   hinst,
    ULONG       Version,
    REFIID      riidltf,
    PVOID*      ppvOut,
    LPUNKNOWN   punkOuter
)
{
    static TYPE_OF(Arianrhod_DirectInput8Create) *DirectInput8Create;

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

#if ENABLE_LOG
    {
        NtFileDisk f;
        f.Create(L"log.txt");
    }
#endif

    WriteLog(L"%08X\n", _ReturnAddress());

    static BOOL Hooked = FALSE;

    if (!Hooked && IsCodeDecompressed())
    {
        DllMain(&__ImageBase, DLL_PROCESS_ATTACH, 0);
        ChangeMainWindowProc(*(HWND *)0xDB2E54);
        Hooked = TRUE;
    }

    return DirectInput8Create(hinst, Version, riidltf, ppvOut, punkOuter);
}

#endif
