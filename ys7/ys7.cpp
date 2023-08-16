#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(linker, "/EXPORT:DirectInput8Create=DINPUT8.DirectInput8Create")

#include "MyLibrary.cpp"

PVOID NTAPI HookRtlAllocateHeap(HANDLE HeapBase, ULONG Flags, SIZE_T Bytes)
{
    ULONG_PTR Protect, Size;
    PVOID First, Memory, Second;

    Size = ROUND_UP(Bytes, MEMORY_PAGE_SIZE) + MEMORY_PAGE_SIZE * 2;

    Memory = NULL;
    Nt_AllocateMemory(NtCurrentProcess(), &Memory, Size, PAGE_EXECUTE_READWRITE, MEM_RESERVE);
    Nt_AllocateMemory(NtCurrentProcess(), &Memory, Size - MEMORY_PAGE_SIZE, PAGE_EXECUTE_READWRITE, MEM_COMMIT);

    Second = PtrAdd(Memory, Size - MEMORY_PAGE_SIZE);
    Nt_AllocateMemory(NtCurrentProcess(), &Second, MEMORY_PAGE_SIZE, PAGE_READONLY, MEM_COMMIT);

    Memory = PtrSub(Second, Bytes);
    *(PULONG_PTR)PtrSub(Memory, sizeof(PVOID)) = Bytes;

    return Memory;
}

BOOL NTAPI HookRtlFreeHeap(HANDLE HeapBase, ULONG Flags, LPVOID Memory)
{
    Memory = (PVOID)ROUND_DOWN((ULONG_PTR)Memory, MEMORY_PAGE_SIZE);
    Nt_FreeMemory(NtCurrentProcess(), PtrSub(Memory, MEMORY_PAGE_SIZE));
    return TRUE;
}

PVOID NTAPI HookRtlReAllocateHeap(HANDLE HeapBase, ULONG Flags, PVOID Memory, SIZE_T Bytes)
{
    PVOID NewMemory;

    NewMemory = HookRtlAllocateHeap(HeapBase, Flags, Bytes);

    Bytes = MY_MIN(((PULONG_PTR)Memory)[-1], Bytes);
    CopyMemory(NewMemory, Memory, Bytes);

    HookRtlFreeHeap(HeapBase, Flags, Memory);

    return NewMemory;
}

ULONG_PTR NTAPI HookRtlSizeHeap(HANDLE HeapBase, ULONG Flags, PVOID Memory)
{
    return ((PULONG_PTR)Memory)[-1];
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    PLDR_MODULE ExeModule;

    LdrDisableThreadCalloutsForDll(BaseAddress);

    BaseAddress = Nt_FindLdrModuleByHandle(NULL)->DllBase;

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(HookRtlAllocateHeap,   sizeof(PVOID), IATLookupRoutineRVAByEntry(BaseAddress, RtlAllocateHeap)),
        PATCH_MEMORY(HookRtlReAllocateHeap, sizeof(PVOID), IATLookupRoutineRVAByEntry(BaseAddress, RtlReAllocateHeap)),
        PATCH_MEMORY(HookRtlFreeHeap,       sizeof(PVOID), IATLookupRoutineRVAByEntry(BaseAddress, RtlFreeHeap)),
        PATCH_MEMORY(HookRtlSizeHeap,       sizeof(PVOID), IATLookupRoutineRVAByEntry(BaseAddress, RtlSizeHeap)),
    };
    
    Nt_LoadLibrary(L"D3DCompiler_43.dll");
    Nt_LoadLibrary(L"ole32.dll");

//    Nt_PatchMemory(p, countof(p), NULL, 0, BaseAddress);

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

/*++

00602722  |> \53            push    ebx                                         ; /pMemory
00602723  |.  57            push    edi                                         ; |Flags
00602724  |.  68 10717800   push    00787110                                    ; |hHeap = 00787110
00602729  |.  FF15 08316200 call    dword ptr [<&KERNEL32.HeapSize>]            ; \HeapSize
0060272F  |.  8BF0          mov     esi, eax
00602731  |>  8BC6          mov     eax, esi
00602733  |>  E8 41CBFFFF   call    005FF279
00602738  \.  C3            ret

->

push    ebx                                         ; /pMemory
push    edi                                         ; |Flags
push    dword ptr [00787110]                        ; |hHeap
call    dword ptr [<&KERNEL32.HeapSize>]            ; \HeapSize

--*/
