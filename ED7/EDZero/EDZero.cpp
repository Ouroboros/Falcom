#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(lib, "d3d9.lib")
#pragma comment(lib, "freetype.lib")

#define USE_NT_VER      1
#define CONSOLE_DEBUG   0

#include "EDZero.h"
#include "my_commsrc.h"

static const EDZero_ShowImageFunc   ShowImage = CastMethodAddress<EDZero_ShowImageFunc>(FUNC_SHOWIMAGE);
static const EDZero_LoadItpFunc     pfLoadItp   = CastMethodAddress<EDZero_LoadItpFunc>(FUNC_LOADITP);

#if 0

typedef VOID (CDECL *SecuromInitFunc)(...);

typedef struct
{
    PVOID pKey;
    PVOID BaseAddress;
    ULONG Length;
} SR_DATA_HEADER;

LONG STDCALL Callback(PVOID, LPWIN32_FIND_DATAW pFindData, SecuromInitFunc Init2)
{
    HANDLE hFile;
    ULONG  Bytes;
    BYTE   Buffer[0x1000];
    SR_DATA_HEADER *hdr;

    hFile = CreateFileW(
                pFindData->cFileName,
                GENERIC_READ,
                FILE_SHARE_READ,
                NULL,
                OPEN_ALWAYS,
                FILE_ATTRIBUTE_NORMAL,
                NULL);

    ReadFile(hFile, Buffer, sizeof(Buffer), &Bytes, NULL);
    CloseHandle(hFile);

    hdr = (SR_DATA_HEADER *)Buffer;
/*
    PVOID  pBase;
    pBase = VirtualAllocEx(NtCurrentProcess(), NULL, 0x1000, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);
    if (pBase == NULL)
        __asm nop;

    CopyMemory(pBase, hdr + 1, hdr->Length);

    PBYTE p, pend;
    ULONG_PTR v, Beg, End;

    Beg = (ULONG_PTR)hdr->BaseAddress;
    End = Beg + hdr->Length;

    p = (PBYTE)pBase;
    pend = p + hdr->Length;
    while (p < pend)
    {
        v = *(PULONG_PTR)p;
        if (v >= Beg && v <= End)
        {
            *(PULONG_PTR)p = v - (ULONG_PTR)hdr->BaseAddress + (ULONG_PTR)pBase;
            p += 4;
        }
        else
        {
            ++p;
        }
    }
*/
//    *(bool *)((ULONG_PTR)hdr->pKey + 0x14) = true;
    Init2(hdr->pKey, hdr->BaseAddress);

    return 0;
}

#include "SecuRomData.h"

VOID InitSecuRom()
{
    ULONG Value1, Value2;

    union
    {
        HMODULE     hModule;
        ULONG_PTR   BaseAddress;
    };

    SecuromInitFunc Init1 = (SecuromInitFunc)0xE59426;
    SecuromInitFunc Init2 = (SecuromInitFunc)0xC06CF3;

    MessageBoxW(NULL, NULL, NULL, NULL);

    hModule = GetModuleHandleW(NULL);

    MEMORY_PATCH p[] =
    {
        // static data
        { NULL,                                     4, 0x125BC58 },     // pointer
        { NULL,                                     4, 0x125BC6C },     // pointer
        { (ULONG_PTR)SRData3,                       4, 0x1220964 },     // data
        { (ULONG_PTR)VM_HANDLER_PTR,                       4, 0x122097C },     // data
        { *(PULONG_PTR)(0x93E3E0 + BaseAddress),    4, 0x1343CDC },     // SR CRT hHeap
        { (ULONG_PTR)VM,                            4, 0x13456BC },     // VM
        { 0xB8,                                     1, 0x0C068EE },     // skip decrypt code call

        // IAT

        { (ULONG_PTR)HeapAlloc,                 4, 0x1512E34 },   // SR IAT HeapAlloc
        { (ULONG_PTR)HeapReAlloc,               4, 0x1512D2C },   // SR IAT HeapReAlloc
        { (ULONG_PTR)HeapFree,                  4, 0x1512E38 },   // SR IAT HeapFree
        { (ULONG_PTR)EnterCriticalSection,      4, 0x1512D7C },   // SR IAT EnterCriticalSection
        { (ULONG_PTR)LeaveCriticalSection,      4, 0x1512D80 },   // SR IAT LeaveCriticalSection
    };

    PatchMemory(p, countof(p), NULL, 0, hModule);

    *(PULONG_PTR)&VM[0x78] = (ULONG_PTR)SRDataPtr1;
    *(PULONG_PTR)&VM[0xCC] = (ULONG_PTR)SRData3;
    *(PULONG_PTR)&VM[0xDA] = (ULONG_PTR)VM_HANDLER_PTR;

    for (ULONG Count = countof(VM_HANDLER_PTR), *p = VM_HANDLER_PTR; Count; ++p, --Count)
    {
        *p = *p + (ULONG_PTR)VM_HANDLER - (ULONG_PTR)VM;
    }

    InitializeCriticalSection((LPCRITICAL_SECTION)(0x125BC34 + BaseAddress));

    *(PULONG_PTR)&Init1 += BaseAddress;
    *(PULONG_PTR)&Init2 += BaseAddress;

    Value1 = 0;
    Value2 = 4;
    Init1(0x125BC6C + BaseAddress, 0, 0, 0, 0, &Value1, &Value2);

    EnumDirectoryFiles(
        NULL,
        L"*.*",
        0,
        L"J:\\Falcom\\ED_Zero\\SRData",
        NULL,
        (FEnumDirectoryFilesCallBack)Callback,
        (ULONG_PTR)Init2,
        0
    );

//    Init2(0x176BD6F + BaseAddress, NULL/* pEnctyptData */);
}

ASM
INT
WINAPI
OldZeroWinMain(
    HINSTANCE   /* hInstance */,
    HINSTANCE   /* hPrevInstance */,
    LPSTR       /* lpCmdLine */,
    INT         /* nShowCmd */
)
{
    ASM_DUMMY_AUTO();
}

INT WINAPI ZeroWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, INT nShowCmd)
{
    InitSecuRom();
    return OldZeroWinMain(hInstance, hPrevInstance, lpCmdLine, nShowCmd);
}

VOID Init()
{
    HMODULE hModule;

    MEMORY_FUNCTION_PATCH f[] =
    {
        { JUMP, 0x2609F8, ZeroWinMain, 0, OldZeroWinMain },
    };

    hModule = GetModuleHandleW(NULL);

    PatchMemory(NULL, 0, f, countof(f), hModule);
}

#else

ULONG g_AppPathLength, g_BufferSize;
PVOID g_pvBuffer, g_AppPathBuffer;

ULONG CEDZeroBattle::m_AvatarIndex = 0;

HWND WINAPI MyCreateWindowExA(DWORD dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, DWORD dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
{
    RECT    rcWordArea;
    ULONG   Length;
    LPWSTR  pszClassName, pszWindowName;

    Length = StrLengthA(lpClassName) + 1;
    pszClassName = (LPWSTR)AllocStack(Length * sizeof(WCHAR));
    Nt_AnsiToUnicode(pszClassName, Length, lpClassName, Length);

    Length = StrLengthA(lpWindowName) + 1;
    pszWindowName = (LPWSTR)AllocStack(Length * sizeof(WCHAR));
    Nt_AnsiToUnicode(pszWindowName, Length, lpWindowName, Length);

    if (SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcWordArea, 0))
    {
        X = ((rcWordArea.right - rcWordArea.left) - nWidth) / 2;
        Y = ((rcWordArea.bottom - rcWordArea.top) - nHeight) / 2;
    }

    return CreateWindowExW(dwExStyle, pszClassName, pszWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam);
}

PWCHAR
GetFileName(
    PWCHAR  pszHooked,
    ULONG   HookedBufferCount,
    PWCHAR  pszOriginal,
    ULONG   OriginalCount,
    LPCSTR  lpFileName,
    BOOL    IsInputUnicode = FALSE
)
{
    ULONG   Length, AppPathLength;
    PWCHAR  pszFileName;

    static WCHAR szDataPath[]   = L"data\\";
    static WCHAR szPatch[]      = L"patch\\\\\\";
    static WCHAR szDataSc[]     = L"data_sc\\";

    if (IsInputUnicode)
    {
        lstrcpyW(pszOriginal, (LPWSTR)lpFileName);
    }
    else
    {
        Nt_AnsiToUnicode(pszOriginal, OriginalCount, (PCHAR)lpFileName, -1);
    }

    Length = RtlGetFullPathName_U(pszOriginal, HookedBufferCount * sizeof(WCHAR), pszHooked, NULL);
    Length = Length / sizeof(WCHAR) + 1;
    AppPathLength = g_AppPathLength;
    pszFileName = pszHooked + AppPathLength;
    LOOP_ONCE
    {
        if (StrNICompareW(pszFileName, szDataPath, countof(szDataPath) - 1) ||
            StrNICompareW((PWCHAR)g_AppPathBuffer, pszHooked, AppPathLength))
        {
            pszFileName = pszOriginal;
            break;
        }

        pszFileName += countof(szDataPath) - 2;
        RtlMoveMemory(
            pszFileName + countof(szDataSc) - countof(szDataPath),
            pszFileName,
            (Length - (pszFileName - pszHooked)) * sizeof(*pszFileName)
        );

        pszFileName -= countof(szDataPath) - 2;
        CopyStruct(pszFileName, szPatch, sizeof(szPatch) - sizeof(*szPatch));
        if (Nt_IsPathExists(pszHooked))
        {
            pszFileName = pszHooked;
            break;
        }

        CopyStruct(pszFileName, szDataSc, sizeof(szDataSc) - sizeof(*szDataSc));
        if (!Nt_IsPathExists(pszHooked))
            pszFileName = pszOriginal;
        else
            pszFileName = pszHooked;
    }
/*
    AllocConsole();
    PrintConsoleW(L"%s\n", pszFileName);
    if (!StrICompareW(findextw(pszFileName), L".it3"))
        __asm nop;
*/
#if CONSOLE_DEBUG
    PrintConsoleW(L"%s\n", pszFileName);
#endif

    return pszFileName;
}

ULONG UnicodeWin32FindDataToAnsi(LPWIN32_FIND_DATAW pwfdW, LPWIN32_FIND_DATAA pwfdA)
{
    CopyStruct(pwfdA, pwfdW, FIELD_OFFSET(WIN32_FIND_DATAW, cFileName));
    Nt_UnicodeToAnsi(pwfdA->cFileName, sizeof(pwfdA->cFileName), pwfdW->cFileName, -1);
    return Nt_UnicodeToAnsi(pwfdA->cAlternateFileName, sizeof(pwfdA->cAlternateFileName), pwfdW->cAlternateFileName, -1);
}

HANDLE WINAPI MyFindFirstFileA(LPCSTR lpFileName, LPWIN32_FIND_DATAA lpFindFileData)
{
    HANDLE hFind;
    WIN32_FIND_DATAW wfd;
    WCHAR szHook[MAX_PATH], szOriginal[MAX_PATH];

    hFind = Nt_FindFirstFile(GetFileName(szHook, countof(szHook), szOriginal, countof(szOriginal), lpFileName), &wfd);
    if (hFind != INVALID_HANDLE_VALUE)
    {
        UnicodeWin32FindDataToAnsi(&wfd, lpFindFileData);
        Nt_FindClose(hFind);
        hFind = INVALID_HANDLE_VALUE;
    }

    return hFind;
}

HANDLE
WINAPI
MyCreateFileA(
    LPCSTR                  lpFileName,
    DWORD                   dwDesiredAccess,
    DWORD                   dwShareMode,
    LPSECURITY_ATTRIBUTES   lpSecurityAttributes,
    DWORD                   dwCreationDisposition,
    DWORD                   dwFlagsAndAttributes,
    HANDLE                  hTemplateFile
)
{
    WCHAR szFile[MAX_PATH], szFullPath[MAX_PATH];

    return Nt_CreateFileW(
                GetFileName(szFullPath, countof(szFullPath), szFile, countof(szFile), lpFileName),
                dwDesiredAccess,
                dwShareMode,
                lpSecurityAttributes,
                dwCreationDisposition,
                dwFlagsAndAttributes,
                hTemplateFile
           );
}

ASM
FILE*
CDECL
old_fopen(
    const char * /*filename*/,
    const char * /*mode*/
)
{
    ASM_DUMMY_AUTO();
}

typedef FILE* (CDECL *pfopen)(const char *filename, const char *mode);
typedef size_t (CDECL *pfread)(void *buffer,size_t size,size_t count,FILE *stream);
typedef int (CDECL *pfseek)(FILE *stream,long offset,int origin);
typedef long (CDECL *pftell)(FILE *stream);
typedef int (CDECL *pfclose)(FILE *stream);

LONG STDCALL DecCallback(PVOID, LPWIN32_FIND_DATAW pfd, ULONG_PTR)
{
    ULONG Header;
    NTSTATUS Status;
    CNtFileDisk file;

    file.Open(pfd->cFileName);
    file.Read(&Header, 4);
    file.Close();

    if (Header != TAG4('SDFA'))
        return 0;

    CHAR FileName[MAX_PATH];

    PrintConsoleW(L"%s\n", pfd->cFileName);
    Nt_UnicodeToAnsi(FileName, countof(FileName), pfd->cFileName);

    pfopen  fopen   = (pfopen) 0x6585C3;
    pfseek  fseek   = (pfseek) 0x658587;
    pftell  ftell   = (pftell) 0x6585B9;
    pfread  fread   = (pfread) 0x6580FA;
    pfclose fclose  = (pfclose)0x65994B;

    fopen = old_fopen;

//    fclose = (pfclose)0x659955;     // zero_tc

    FILE *fp = fopen(FileName, "rb");
    fseek(fp, 0, SEEK_END);
    Header = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    PBYTE p = (PBYTE)AllocateMemory(Header);
    if (fread(p, Header, 1, fp) == 0)
        PrintConsoleW(L"failed\n");

    fclose(fp);

    ULONG len;
    static WCHAR suffix[] = L"_sc";
    static WCHAR folder[] = L"data";

    len = StrLengthW(pfd->cFileName) + 1;
    RtlMoveMemory(
        pfd->cFileName + CONST_STRLEN(folder) + CONST_STRLEN(suffix),
        pfd->cFileName + CONST_STRLEN(folder),
        len * 2 - CONST_STRLEN(folder) * sizeof(WCHAR)
    );

    CopyMemory(
        pfd->cFileName + CONST_STRLEN(folder),
        suffix,
        sizeof(suffix) - sizeof(WCHAR)
    );

    WCHAR c, *pname;

    pname = findnamew(pfd->cFileName);
    c = *pname;
    *pname = 0;
    MyCreateDirectoryW(pfd->cFileName);
    *pname = c;

    Status = file.Create(pfd->cFileName);
//    PrintConsoleW(L"file.Create(): %08X\n", Status);

    if (NT_SUCCESS(Status))
    {
        Status = file.Write(p, Header);
//        PrintConsoleW(L"file.Write(): Status = %08X, Size = %08X\n", Status, Header);
    }

    FreeMemory(p);

//    getch();

    return 0;
}

VOID dec()
{
    SetPriorityClass(NtCurrentProcess(), BELOW_NORMAL_PRIORITY_CLASS);
    AllocConsole();
    Nt_SetExecuteDirectoryAsCurrent();

    EnumDirectoryFiles(
        NULL,
        L"*.*",
        0,
        L"data",
        NULL,
        DecCallback,
        0,
        ENUM_DIRECTORY_FILES_FLAG_ENUMSUBDIR
    );

    FreeConsole();

    Nt_ExitProcess(0);
}

FILE*
CDECL
my_fopen(
    const char *filename,
    const char *mode
)
{
    CHAR    Path[MAX_PATH];
    WCHAR   *NewFileName, szFile[MAX_PATH], szFullPath[MAX_PATH];

    NewFileName = GetFileName(szFullPath, countof(szFullPath), szFile, countof(szFile), filename);

    if (NewFileName == szFullPath)
    {
        Nt_UnicodeToAnsi(Path, sizeof(Path), NewFileName, -1);
        filename = Path;
    }

    return old_fopen(filename, mode);
}

ASM ULONG FASTCALL UCL_NRV2E_DecompressASMFast32(PVOID /* pvInput */, PVOID /* pvOutput */)
{
    INLINE_ASM
    {
        add     esp, -0x18;
        mov     [esp + 0x00], ebx;
        mov     [esp + 0x04], ebp;
        mov     [esp + 0x08], esi;
        mov     [esp + 0x0C], edi;
        mov     [esp + 0x10], edx;
        cld;
        mov     esi, ecx;
        mov     edi, edx;
        or      ebp, 0xFFFFFFFF;
        xor     ecx, ecx;
        jmp L029;

        INLINE_ASM __emit 0x8D INLINE_ASM __emit 0xB4 INLINE_ASM __emit 0x26 INLINE_ASM __emit 0x00 INLINE_ASM __emit 0x00 INLINE_ASM __emit 0x00 INLINE_ASM __emit 0x00;   // lea esi, [esi]
        INLINE_ASM __emit 0x8D INLINE_ASM __emit 0xB4 INLINE_ASM __emit 0x26 INLINE_ASM __emit 0x00 INLINE_ASM __emit 0x00 INLINE_ASM __emit 0x00 INLINE_ASM __emit 0x00;   // lea esi, [esi]
L022:
        mov     al, byte ptr [esi];
        inc     esi;
        mov     byte ptr [edi], al;
        inc     edi;
L026:
        add     ebx, ebx;
        jnb L033;
        jnz L022;
L029:
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
        jb L022;
L033:
        mov     eax, 0x1;
L034:
        add     ebx, ebx;
        jnz L039;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
L039:
        adc     eax, eax;
        add     ebx, ebx;
        jnb L047;
        jnz L055;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
        jb L055;
L047:
        dec     eax;
        add     ebx, ebx;
        jnz L053;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
L053:
        adc     eax, eax;
        jmp L034;
L055:
        sub     eax, 0x3;
        jb L072;
        shl     eax, 0x8;
        mov     al, byte ptr [esi];
        inc     esi;
        xor     eax, 0xFFFFFFFF;
        je L120;
        sar     eax, 1;
        mov     ebp, eax;
        jnb L078;
L065:
        add     ebx, ebx;
        jnz L070;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
L070:
        adc     ecx, ecx;
        jmp L099;
L072:
        add     ebx, ebx;
        jnz L077;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
L077:
        jb L065;
L078:
        inc     ecx;
        add     ebx, ebx;
        jnz L084;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
L084:
        jb L065;
L085:
        add     ebx, ebx;
        jnz L090;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
L090:
        adc     ecx, ecx;
        add     ebx, ebx;
        jnb L085;
        jnz L098;
        mov     ebx, dword ptr [esi];
        sub     esi, -0x4;
        adc     ebx, ebx;
        jnb L085;
L098:
        add     ecx, 0x2;
L099:
        cmp     ebp, -0x500;
        adc     ecx, 0x2;
        lea     edx, dword ptr [edi+ebp];
        cmp     ebp, -0x4;
        jbe L111;
L104:
        mov     al, byte ptr [edx];
        inc     edx;
        mov     byte ptr [edi], al;
        inc     edi;
        dec     ecx;
        jnz L104;
        jmp L026;
L111:
        mov     [esp + 0x14], ecx;
        and     ecx, ~3;
        jecxz   L111_END;
L111_:
        mov     eax, dword ptr [edx];
        add     edx, 0x4;
        mov     dword ptr [edi], eax;
        add     edi, 0x4;
        sub     ecx, 0x4;
        ja L111_;

L111_END:

        mov     ecx, [esp + 0x14];
        and     ecx, 3;
        jecxz   L111_LOOP_2_END;
        mov     [esp + 0x14], ecx;

L111_LOOP_2:
            mov     al, [edx];
            mov     [edi], al;
            inc     edx;
            inc     edi;
        loop    L111_LOOP_2;

        mov     ecx, [esp + 0x14];
        sub     edx, ecx;
        add     edx, 4;

L111_LOOP_2_END:

//        add     edi, ecx;
        xor     ecx, ecx;
        jmp L026;
L120:
        mov     eax, edi;
        mov     ebx, [esp + 0x00];
        mov     ebp, [esp + 0x04];
        mov     esi, [esp + 0x08];
        mov     edi, [esp + 0x0C];
        sub     eax, [esp + 0x10];
        add     esp, 0x18;
        ret;
    }
}

ULONG
CEDZeroFileStream::
Read(
    PVOID pvBuffer,
    ULONG Size,
    ULONG Count,
    ULONG Unknown /* = 0 */,
    ULONG Unknown2 /* = 0 */
)
{
    EDZero_ReadFunc pfRead = CastMethodAddress<EDZero_ReadFunc>(FUNC_READ);
    return (this->*pfRead)(pvBuffer, Size, Count, Unknown, Unknown2);
}

BOOL CEDZeroFileStream::Seek(LONG Offset, ULONG SeekMethod)
{
    EDZero_SeekFunc pfSeek = CastMethodAddress<EDZero_SeekFunc>(FUNC_SEEK);

    if (m_BufferIndex != 0 && m_BufferFlags != 0)
    {
        switch (SeekMethod)
        {
            case SEEK_SET:
                m_Position = Offset;
                break;

            case SEEK_CUR:
                m_Position += Offset;
                break;

            case SEEK_END:
                m_Position = m_Size + Offset;
                break;
        }

        return TRUE;
    }

    return (this->*pfSeek)(Offset, SeekMethod);
}

ASM
ULONG
CEDZeroFileStream::
OldUncompress(
    PVOID /* pvBuffer */,
    ULONG /* BlockSize */,
    ULONG /* BlockCount */
)
{
    ASM_DUMMY_AUTO();
}

ULONG CEDZeroFileStream::Uncompress(PVOID pvOutput, ULONG BlockSize, ULONG BlockCount)
{
    PVOID   pvBuffer;
    HANDLE  hHeap;
    UCL_COMPRESS_HEADER Header;

    Read(&Header, sizeof(Header));
    if (Header.Magic != UCL_COMPRESS_MAGIC)
    {
        Seek(-sizeof(Header), SEEK_CUR);
        return OldUncompress(pvOutput, BlockSize, BlockCount);
    }

    hHeap = CMem::GetGlobalHeap();

    pvBuffer = g_pvBuffer;
    if (pvBuffer == NULL)
    {
        g_BufferSize = Header.CompressedSize;
        pvBuffer = RtlAllocateHeap(hHeap, 0, g_BufferSize);
        g_pvBuffer = pvBuffer;
    }
    else if (Header.CompressedSize > g_BufferSize)
    {
        g_BufferSize = Header.CompressedSize;
        pvBuffer = RtlReAllocateHeap(hHeap, 0, pvBuffer, g_BufferSize);
        if (pvBuffer == NULL)
        {
            RtlFreeHeap(hHeap, 0, g_pvBuffer);
        }

        g_pvBuffer = pvBuffer;
    }

    if (pvBuffer == NULL)
        return 0;

    Read(pvBuffer, Header.CompressedSize);

    return UCL_NRV2E_DecompressASMFast32(pvBuffer, pvOutput);
}

ASM
LONG
CEDZero::
OldLoadItp(
    PCHAR,              //  pszFileName,
    ULONG,              //  FileNameBufferIndex,
    ULONG,              //  Unknown1,
    ULONG,              //  Unknown2,
    CEDZeroFileStream*, //  pStream,
    ULONG,              //  Unknown3,
    ULONG               //  Unknown4
)
{
    ASM_DUMMY_AUTO();
}

LONG
CEDZero::
LoadItp(
    PCHAR               pszFileName,
    ULONG               Index,
    ULONG               Unknown1,
    ULONG               Unknown2,
    CEDZeroFileStream  *pStream,
    ULONG               Unknown3,
    ULONG               Unknown4
)
{
    ULONG       Header, BytesPerPixel, UciStreamSize, RGBSize, AlphaSize;
    PVOID       pvUciBuffer;
    PBYTE       pbRGB, pbAlpha, pbRaw;
    HANDLE      hHeap;
    UCI_INFO    uci;

    static PVOID s_pvUciBuffer, s_pvRGB, s_pvAlpha;
    static ULONG s_UciBufferSize, s_RGBBufferSize, s_AlphaBufferSize;

    pStream->Read(&Header, 4);
    if (Header != ITP_TYPE_UCI_32)
    {
        pStream->Seek(-4, SEEK_CUR);
        return OldLoadItp(pszFileName, Index, Unknown1, Unknown2, pStream, Unknown3, Unknown4);
    }

    pStream->Read(&UciStreamSize, sizeof(&UciStreamSize));

    hHeap = CMem::GetGlobalHeap();
    pvUciBuffer = s_pvUciBuffer;
    if (pvUciBuffer == NULL)
    {
        s_UciBufferSize = UciStreamSize;
        pvUciBuffer = RtlAllocateHeap(hHeap, 0, s_UciBufferSize);
        s_pvUciBuffer = pvUciBuffer;
    }
    else if (UciStreamSize > s_UciBufferSize)
    {
        s_UciBufferSize = UciStreamSize;
        pvUciBuffer = RtlReAllocateHeap(hHeap, 0, pvUciBuffer, s_UciBufferSize);
        if (pvUciBuffer == NULL)
        {
            RtlFreeHeap(hHeap, 0, s_pvUciBuffer);
            s_pvUciBuffer = NULL;
        }
    }

    if (pvUciBuffer == NULL)
        return -1;

    pStream->Read(pvUciBuffer, UciStreamSize);
    if (UCIDecodeEx(pvUciBuffer, UciStreamSize, &uci, FALSE) < 0)
        return -1;

    RGBSize     = ROUND_UP(uci.Width * uci.Height * 3, 4);
    AlphaSize   = RGBSize;

    pbRGB = (PBYTE)s_pvRGB;
    if (pbRGB == NULL)
    {
        pbRGB = (PBYTE)RtlAllocateHeap(hHeap, 0, RGBSize);
        s_pvRGB = pbRGB;
    }
    else if (RGBSize > s_RGBBufferSize)
    {
        s_RGBBufferSize = RGBSize;
        pbRGB = (PBYTE)RtlReAllocateHeap(hHeap, 0, pbRGB, s_RGBBufferSize);
        if (pbRGB == NULL)
        {
            RtlFreeHeap(hHeap, 0, s_pvRGB);
            s_pvRGB = NULL;
        }
    }

    if (pbRGB == NULL)
    {
        UCIFreeEx(&uci);
        return -1;
    }

    pbAlpha = (PBYTE)s_pvAlpha;
    if (pbAlpha == NULL)
    {
        pbAlpha = (PBYTE)RtlAllocateHeap(hHeap, 0, AlphaSize);
        s_pvAlpha = pbAlpha;
    }
    else if (AlphaSize > s_AlphaBufferSize)
    {
        s_AlphaBufferSize = RGBSize;
        pbAlpha = (PBYTE)RtlReAllocateHeap(hHeap, 0, pbRGB, s_AlphaBufferSize);
        if (pbAlpha == NULL)
        {
            RtlFreeHeap(hHeap, 0, s_pvAlpha);
            s_pvAlpha = NULL;
        }
    }

    if (pbAlpha == NULL)
    {
        UCIFreeEx(&uci);
        return -1;
    }

    BytesPerPixel = uci.BitsPerPixel / 8;
    pbRaw = uci.pbBuffer;

    if (BytesPerPixel == 4)
    {
        for (ULONG Height = uci.Height; Height; --Height)
        {
            PBYTE p = pbRaw;

            for (ULONG Width = uci.Width; Width; --Width)
            {
                ULONG Color = *(PULONG)p;

                *(PULONG)pbRGB = Color;
                Color >>= 24;
                Color = Color | (Color << 8) | (Color << 16);
                *(PULONG)pbAlpha = Color;

                pbRGB   += 3;
                pbAlpha += 3;
                p += 4;
            }

            pbRaw += uci.Stride;
        }
    }

    YAMANEKO_IMAGE_OBJECT *pImageObject;
    EDZero_ShowImageFunc ShowImage = CastMethodAddress<EDZero_ShowImageFunc>(FUNC_SHOWIMAGE);

    pImageObject = &m_ImageObject[Index];
    (((CEDZero *)pImageObject)->*ShowImage)(uci.Width, uci.Height, s_pvRGB, s_pvAlpha, Unknown1);

//    pImageObject->Unknown   = -1;
    pImageObject->Unknown2  = 0;
    m_Unknown[Index]        = 1;

    CopyStruct(m_ImageFileName[Index], pszFileName, sizeof(m_ImageFileName[0]));

    UCIFreeEx(&uci);

    return Index;
}

ASM PVOID CEDZero::OldFormatSEPath(PCHAR /* pszPath */, ULONG /* SEIndex */)
{
    ASM_DUMMY_AUTO();
}

PVOID CEDZero::FormatSEPath(PCHAR pszPath, ULONG SEIndex)
{
    PVOID pSEIndexData;
    WCHAR szHook[MAX_PATH], szOriginal[MAX_PATH], *pszFile;

    pSEIndexData = OldFormatSEPath(pszPath, SEIndex);
    pszFile = GetFileName(szHook, countof(szHook), szOriginal, countof(szOriginal), pszPath);
    if (pszFile != szOriginal)
        Nt_UnicodeToAnsi(pszPath, 0x40, pszFile, -1);

    return pSEIndexData;
}

BOOL THISCALL CEDZeroBattle::IsCharControllable(ULONG CharID)
{
    PUSHORT pMappedCharId;

    pMappedCharId = GetMappedCharId();
    if (IS_CHAR_CUSTOM(pMappedCharId[CharID]))
        return FALSE;

    return CharID <= 0xC;
}

ASM T_STATUS_LEVEL_DATA* THISCALL CEDZeroBattle::OldCalcCharStatusData(ULONG /* CharID */, ULONG /* Level */)
{
    ASM_DUMMY_AUTO();
}

T_STATUS_LEVEL_DATA* THISCALL CEDZeroBattle::CalcCharStatusData(ULONG CharID, ULONG Level)
{
    PUSHORT pMappedCharId;
    CEDZeroBattle *pThis;
    T_STATUS_LEVEL_DATA *pStatus;

    pStatus = OldCalcCharStatusData(CharID, Level);
    if (pStatus == NULL)
        return pStatus;

    pThis = (CEDZeroBattle *)((ULONG_PTR)this + ZERO_BATTLE_OFFSET_TO_BASE);
    pMappedCharId = pThis->GetMappedCharId();
    if (!IS_CHAR_CUSTOM(pMappedCharId[CharID]))
        return pStatus;

    pStatus->HP             *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->STR            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->DEF            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->ATS            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->ADF            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->DEX            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->AGL            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->MOV            *= CHAR_STATUS_INCRESE_FACTOR;
    pStatus->SPD            *= CHAR_STATUS_INCRESE_FACTOR / 2.f;
    pStatus->AGLAddition    *= CHAR_STATUS_INCRESE_FACTOR;

    pStatus->AGL = 0;
    pStatus->AGLAddition = 0;

    return pStatus;
}

ASM VOID CEDZeroBattle::NakedSkipCopyCharStatusData()
{
    INLINE_ASM
    {
        mov     dword ptr [ebp-0x20], 0x0;
        mov     eax, [ebp+0x8];
        mov     ecx, [ebp-0x8];
        mov     ecx, [ecx + LOAD_STATUS_MEM_OFFSET_TO_BASE];
        add     ecx, ZERO_BATTLE_OFFSET_TO_BASE;
        push    eax;
        call    SkipCopyCharStatusData;
        test    eax, eax;
        mov     ecx, [esp];
        mov     eax, 0x974B6D;
        cmovne  ecx, eax;
        mov     [esp], ecx;
        ret;
    }
}

BOOL CEDZeroBattle::SkipCopyCharStatusData(ED_ZERO_MONSTER_STATUS_DATA *pMsData)
{
    ULONG   CharID;
    PUSHORT pMappedCharId;

    CharID = pMsData->CharID;
    pMappedCharId = GetMappedCharId();

    return IS_CHAR_CUSTOM(pMappedCharId[CharID]);
}

ASM VOID CEDZeroBattle::GetCraftData()
{
    INLINE_ASM
    {
        movzx   ecx, word ptr [eax+0xA];
        mov     eax, [ebp - 0x8];
        mov     eax, [eax + LOAD_STATUS_MEM_OFFSET_TO_BASE];
        mov     eax, [eax + ZERO_BATTLE_OFFSET_TO_BASE]CEDZeroBattle.m_pbInfo1;
        movzx   edx, word ptr [eax + ecx * 2 + ZERO_BATTLE_MAPPED_ID_OFFSET];
        cmp     edx, 0xC;
        jle     NOT_CUSTOM_CHAR;
        cmp     edx, 0x1F;
        ja      NOT_CUSTOM_CHAR;
        mov     ecx, edx;

NOT_CUSTOM_CHAR:
        cmp     ecx, 0xB;
        ret;
    }
}

ASM ULONG CEDZeroBattle::NakedGetTurnVoice()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0xC];
        mov     edx, [ebp-0x230];
        mov     eax, [ebp-0x224];
        push    edx;
        push    eax;
        call    GetTurnVoice;
        ret;
    }
}

static USHORT DefaultTurnVoice[MAX_CUSTOM_CHAR_ID][TURN_VOICE_COUNT] =
{
    0x03E8, 0x03E9, 0x03EA, 0x03EB, 0x03EC, 0x03ED, 0x044A, 0x044B, 0x044C, 0x044D, 0x044E, 0x044F, 0x04A7, 0x04A8, 0x04A9, 0x04AA,
    0x04AB, 0x04AC, 0x0507, 0x0508, 0x0509, 0x050A, 0x050B, 0x050C, 0x0565, 0x0566, 0x0567, 0x0568, 0x0569, 0x056A, 0x0620, 0x0621,
    0x0622, 0x0623, 0x0624, 0x0625, 0x066A, 0x066B, 0x066C, 0x066D, 0x066E, 0x066F, 0x06B3, 0x06B4, 0x06B5, 0x06B6, 0x06B7, 0x06B8,
    0x05A2, 0x05A3, 0x05A4, 0x05A5, 0x05A6, 0x05A7, 0x05E2, 0x05E3, 0x05E4, 0x05E5, 0x05E6, 0x05E7,
};

ULONG CEDZeroBattle::GetTurnVoice(ULONG CharID, ULONG RandomIndex)
{
    HANDLE          hFile;
    USHORT         (*pTurnVoice)[TURN_VOICE_COUNT];
    PUSHORT         pMappedCharId;
    CEDZeroBattle  *pThis = PtrToZeroBattle1(this);

    static BOOL     Loaded;
    static USHORT   TurnVoice[MAX_CUSTOM_CHAR_ID][TURN_VOICE_COUNT];

    pMappedCharId = pThis->GetMappedCharId();
    if (IS_CHAR_CUSTOM(pMappedCharId[CharID]))
        CharID = pMappedCharId[CharID];

    if (!Loaded)
    {
        Loaded = TRUE;
        hFile = MyCreateFileA(
                    TURN_VOICE_MAP_PATH,
                    GENERIC_READ,
                    FILE_SHARE_READ,
                    NULL,
                    OPEN_EXISTING,
                    FILE_ATTRIBUTE_NORMAL,
                    NULL
                );

        if (hFile == INVALID_HANDLE_VALUE)
        {
            pTurnVoice = DefaultTurnVoice;
            CopyStruct(TurnVoice, DefaultTurnVoice, sizeof(DefaultTurnVoice));
        }
        else
        {
            LARGE_INTEGER   BytesRead;
            NTSTATUS        Status;

            Status = CNtFileDisk::Read(hFile, TurnVoice, sizeof(TurnVoice), &BytesRead);
            NtClose(hFile);

            pTurnVoice = (NT_SUCCESS(Status) && BytesRead.LowPart == sizeof(TurnVoice)) ? TurnVoice : DefaultTurnVoice;
        }
    }
    else
    {
        pTurnVoice = TurnVoice;
    }

    return pTurnVoice[CharID][RandomIndex];
}

ASM PUSHORT CEDZeroBattle::NakedGetUnderAttackVoice()
{
    INLINE_ASM
    {
        push    edx;
        mov     edx, [ebp + 8];
        mov     ecx, [ebp - 0xC];
        call    CEDZeroBattle::GetUnderAttackVoice;
        pop     edx;
        test    eax, eax;
        lea     edx, [ebp + edx - 0x124];
        cmove   eax, edx;
        ret;
    }
}

PUSHORT FASTCALL CEDZeroBattle::GetUnderAttackVoice(ED_ZERO_MONSTER_STATUS_DATA *pMSData)
{
    PUSHORT  pMapped;

    pMapped = m_EDZero->GetMappedCharId();

    return IS_CHAR_CUSTOM(pMapped[pMSData->CharID]) ? DefaultTurnVoice[0x10] : NULL;
}

ULONG64 CEDZeroBattle::GetBFaceIndex()
{
    PUSHORT         pMappedCharId;
    ULONG_PTR       MsOffset, CharID;
    CEDZeroBattle  *pThis;

    INLINE_ASM mov MsOffset, eax;

    CharID          = m_MsData[MsOffset / sizeof(m_MsData[0])].CharID;
    pThis           = PtrToZeroBattle1(this);
    pMappedCharId   = pThis->GetMappedCharId();

    if (IS_CHAR_CUSTOM(pMappedCharId[CharID]))
        CharID = pMappedCharId[CharID];

    return (ULONG64)CharID << 32;
}

PVOID THISCALL CEDZeroBattle::GetMagicInfo(ULONG MagicIndex)
{
    CEDZero         *pEDZero;
    CEDZeroBattle   *pBattle;
    ED_ZERO_MONSTER_STATUS_DATA *pMSData;

    if (MagicIndex < 0x3E8)
    {
        PUSHORT pTMagic = (PUSHORT)((PULONG_PTR)this)[7];
        return (PBYTE)pTMagic + pTMagic[MagicIndex];
    }

    pEDZero = (CEDZero *)((ULONG_PTR)this - 0x4D27C);
    pBattle = pEDZero->m_Battle;
    pMSData = &pBattle->m_MsData[pBattle->m_CurrentCharIndex];

    return &pMSData->CraftInfo[MagicIndex - 0x3E8];
}

PVOID THISCALL CEDZeroBattle::GetMagicQueryTable(ULONG MagicIndex)
{
    PUSHORT pTMagicQrt;

    if (MagicIndex >= 0x3E8)
    {
        static USHORT MagicQueryTable[8] = { 0, 999, 999, 999, 999, 999, 999, 999 };
        return MagicQueryTable;
    }

    pTMagicQrt = (PUSHORT)((PULONG_PTR)this)[9];
    return (PBYTE)pTMagicQrt + pTMagicQrt[MagicIndex];
}

PVOID THISCALL CEDZeroBattle::GetMagicDescription(ULONG MagicIndex)
{
    CEDZero         *pEDZero;
    CEDZeroBattle   *pBattle;
    ED_ZERO_MONSTER_STATUS_DATA *pMSData;

    if (MagicIndex < 0x3E8)
    {
        PUSHORT pTMagic = (PUSHORT)((PULONG_PTR)this)[7];
        PVOID   pMagicInfo = GetMagicInfo(MagicIndex);
        return (PBYTE)pTMagic + ((PUSHORT)pMagicInfo)[15];
    }

    pEDZero = (CEDZero *)((ULONG_PTR)this - 0x4D27C);
    pBattle = pEDZero->m_Battle;
    pMSData = &pBattle->m_MsData[pBattle->m_CurrentCharIndex];

    return pMSData->CraftName[MagicIndex - 0x3E8].Description;
}

VOID FASTCALL CEDZeroBattle::GetSBreak(ULONG CharID, ED_ZERO_MONSTER_STATUS_DATA *pMSData)
{
    CEDZero *pEDZero;
    PUSHORT pMappedCharId;
    ED_ZERO_AI_INFO *pAI;

    INLINE_ASM mov pEDZero, eax;

    pMappedCharId = (PUSHORT)(*(PBYTE *)((ULONG_PTR)pEDZero + ZERO_BATTLE_OFFSET_TO_BASE) + ZERO_BATTLE_MAPPED_ID_OFFSET);
    if (!IS_CHAR_CUSTOM(pMappedCharId[CharID]))
    {
        pMSData->CurrentSkillInfoIndex = pEDZero->m_SBreakTable[CharID];
        return;
    }

    pAI = pMSData->SCraft;
    if (pAI->SkillInfoIndex == 0)
    {
        pMSData->CurrentSkillInfoIndex = 0;
        return;
    }

    for (ULONG Count = countof(pMSData->SCraft) - 1; Count; ++pAI, --Count)
    {
        if (pAI[1].SkillInfoIndex == 0)
            break;
    }

    pMSData->SelectedAsEffectIndex = pAI->AsEffectIndex;
    pMSData->CurrentSkillInfoIndex = pAI->SkillInfoIndex;
}

ASM bool CEDZeroBattle::OldIsAvatarLoaded(ULONG AvatarIndex)
{
    UNREFERENCED_PARAMETER(AvatarIndex);
    ASM_DUMMY_AUTO();
}

bool CEDZeroBattle::IsAvatarLoaded(ULONG AvatarIndex)
{
    return m_AvatarIndex != -1 ? true : OldIsAvatarLoaded(AvatarIndex);
}

ULONG CEDZeroBattle::FindEmptyPosition(BOOL FindEnemyOnly /* = FALSE */)
{
    ULONG Index = 0, PosFlags;
    ED_ZERO_MONSTER_STATUS_DATA *pMsData, *pEnd;

    if (m_AvatarIndex != -1)
        return m_AvatarIndex;

    PosFlags = 0x78080;

    Index   = FindEnemyOnly ? 8 : 0;
    pMsData = &m_MsData[Index];
    pEnd    = &m_MsData[countof(m_MsData)];

    do
    {
        if (TEST_BITS(pMsData->State, 0x8000))
        {
            if (!TEST_BITS(PosFlags, 1 << Index))
                return Index;
        }

        ++Index;
        ++pMsData;
    } while (pMsData < pEnd);

    return -1;
}

VOID
FASTCALL
CEDZeroBattle::
AS8DHandler(
    ULONG                        Param1,
    PBYTE                        pbAsBuffer,
    ED_ZERO_MONSTER_STATUS_DATA *pMsData
)
{
    AS_8D *pIns;

    if (Param1 != 0)
        return;

    pIns = (AS_8D *)(pbAsBuffer - sizeof(*pIns));
    switch ((ULONG)pIns->FunctionID)
    {
        case FUNC_AVATAR:
            Avatar(pIns, pMsData);
            break;
    }
}

ASM VOID NakedAS8DHandler()
{
    INLINE_ASM
    {
        lea     esp, [esp-0xC];
        mov     ecx, [ebp-0x394];
        mov     [esp+0], eax;
        mov     [esp+4], ecx;
        mov     [esp+8], edx;

        push    [ebp+8];
        mov     eax, [ebp+0xC];
        push    [eax+0x20];
        mov     edx, ecx;
        mov     ecx, [ebp-0xC];
        call    CEDZeroBattle::AS8DHandler;

        mov     eax, [esp+0];
        mov     ecx, [esp+4];
        mov     edx, [esp+8];
        lea     esp, [esp+0xC];

        ret;
    }
}

VOID CEDZeroBattle::Avatar(AS_8D *pIns, ED_ZERO_MONSTER_STATUS_DATA *pMStatus)
{
    CloneMsDataFunc pfCloneMSData   = CastMethodAddress<CloneMsDataFunc>(FUNC_CLONE_MS_DATA);
    ResetMSDataFunc pfResetMSData   = CastMethodAddress<ResetMSDataFunc>(FUNC_RESET_MS_DATA);
    ResetMSDataFunc pfResetCtrlData = CastMethodAddress<ResetMSDataFunc>(FUNC_RESET_CTRL_DATA);
    LoadMsDataFunc  pfLoadMSData    = CastMethodAddress<LoadMsDataFunc>(FUNC_LOAD_MS_FILE);

    ULONG            MsFileIndex, CharPosition;
    COORD            TargetPos;
    ED_ZERO_AI_INFO *pAIInfo;

    if (pMStatus->SkillType != SKILL_TYPE_CRAFT)
        return;

    MsFileIndex = pIns->Param[0];
    if (MsFileIndex == 0)
        return;

    CharPosition = FindEmptyPosition(!TEST_BITS(pMStatus->State, 0x4000));
    if (CharPosition == -1)
        return;

    m_AvatarIndex = CharPosition;

    pAIInfo = &pMStatus->Craft[pMStatus->CurrentCraftIndex];

    LOOP_ONCE
    {
        TargetPos = pMStatus->CraftTargetPosition;
        if (!(this->*pfCloneMSData)(pMStatus, pMStatus->CurrentSkillInfoIndex, pAIInfo))
            break;

        pMStatus->CraftTargetPosition = TargetPos;
        (this->*pfResetCtrlData)(CharPosition);
        (this->*pfResetMSData)(CharPosition);
        if (!(this->*pfLoadMSData)(MsFileIndex, CharPosition))
            break;

        *(PULONG)((ULONG_PTR)this + 0xCB37C) = TargetPos.X;
        *(PULONG)((ULONG_PTR)this + 0xCB380) = TargetPos.Y;

        *(float *)((ULONG_PTR)this + 0x6E0 + CharPosition * 0x320) = TargetPos.X;
        *(float *)((ULONG_PTR)this + 0x6E8 + CharPosition * 0x320) = TargetPos.Y;
    }

    m_AvatarIndex = -1;
}

ASM VOID OldFixAvatarAngle_Magic93Handler()
{
    ASM_DUMMY_AUTO();
}

ASM VOID FixAvatarAngle_Magic93Handler()
{
    INLINE_ASM
    {
        push 01F4h;
        push 9;
        mov  ecx, [ebp-0xC];
        mov  eax, FUNC_SET_ANGLE;
        call eax;
        jmp  OldFixAvatarAngle_Magic93Handler;
    }
}

ASM
VOID
THISCALL
CEDZero::
OldFade(
    ULONG Param1,
    ULONG Param2,
    ULONG Param3,
    ULONG Param4,
    ULONG Param5,
    ULONG Param6
)
{
    UNREFERENCED_PARAMETER(Param1);
    UNREFERENCED_PARAMETER(Param2);
    UNREFERENCED_PARAMETER(Param3);
    UNREFERENCED_PARAMETER(Param4);
    UNREFERENCED_PARAMETER(Param5);
    UNREFERENCED_PARAMETER(Param6);
    ASM_DUMMY_AUTO();
}

VOID
THISCALL
CEDZero::
Fade(
    ULONG Param1,
    ULONG Param2,
    ULONG Param3,
    ULONG Param4,
    ULONG Param5,
    ULONG Param6
)
{
    if (GetAsyncKeyState(VK_LSHIFT) >= 0)
        OldFade(Param1, Param2, Param3, Param4, Param5, Param6);
}

float Rate = 200.f;

ASM VOID FadeInRate()
{
    INLINE_ASM
    {
        fld     dword ptr [eax+0x40];
        fmul    Rate;
        ret;
    }
}

VOID Init()
{
    HMODULE hModule;
    UNICODE_STRING DllPath;

    RTL_CONST_STRING(DllPath, L"D3DCompiler_42.dll");
    LdrLoadDll(NULL, 0, &DllPath, &hModule);

    hModule = Nt_GetExeModuleHandle();

    MEMORY_PATCH p[] =
    {
//        { 0xCD,                             4, 0x340147 },

        PATCH_MEMORY(0x06,      1, 0x3F4551),    // win
        PATCH_MEMORY(0x01,      1, 0x3ED34D), // cpu usage
//        PATCH_MEMORY(0x43EB,    2, 0x346DBD), // skip load warning.itp
//        PATCH_MEMORY(0x00,      1, 0x2DC5DF), // no encounter
        PATCH_MEMORY(0x91,      1, 0x2E0220), // one hit
        PATCH_MEMORY(0x0B81,    4, 0x34FD5C), // skip show warning.itp
        PATCH_MEMORY(0x0B81,    4, 0x35225F), // skip show warning.itp
        PATCH_MEMORY(0x0F81,    4, 0x352936), // skip show warning.itp
        PATCH_MEMORY(0xEB,      1, 0x33FC90), // skip load_interface
        PATCH_MEMORY(0xEB,      1, 0x33FC9F), // skip save_interface
        PATCH_MEMORY(3500,      4, 0x4E55FE), // max se index
        PATCH_MEMORY(3500,      4, 0x4E50A6), // max se index
        PATCH_MEMORY(0x00,      4, 0x57164E), // skip max bface index check
        PATCH_MEMORY(0x3FEB,    2, 0x436428), // save check_sum
        PATCH_MEMORY(0x0FEB,    2, 0x565AB3), // force counter_cmp ms index and test own-site flag
        PATCH_MEMORY(0x00,      1, 0x563ED4), // boss check
        PATCH_MEMORY(0x00,      1, 0x5A2200), // boss check
        PATCH_MEMORY(0x00,      1, 0x5FDD25), // boss check
        PATCH_MEMORY(0x982702,  4, 0x582BE0), // bypass avatar unknown check
        PATCH_MEMORY(0x00,      1, 0x322D75), // force open map

        PATCH_MEMORY(MyCreateWindowExA, 4, 0x94095C),

#if !D3D9_VERSION
        PATCH_MEMORY(MyCreateFileA, 4, 0x940764),
#endif

//        { 0xA97F10,                     4, 0x4A68C + (ULONG_PTR)GetModuleHandleW(L"freetype.dll") - (ULONG_PTR)hModule  },
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
#if !D3D9_VERSION
        PATCH_FUNCTION(JUMP, 0, 0x25804B, FT_Init_FreeType),
//        { JUMP, 0x25C5AB, FT_New_Face           },
//        { JUMP, 0x25C817, FT_Get_Glyph          },
///        { JUMP, 0x25D109, FT_Get_Char_Index     },
///        { JUMP, 0x25834D, FT_Select_Charmap     },
//        { JUMP, 0x25A030, FT_Set_Pixel_Sizes    },
//        { JUMP, 0x25E1D0, FT_Load_Glyph         },
//        { JUMP, 0x25BB15, FT_Render_Glyph       },
//        { JUMP, 0x25BF52, FT_Glyph_To_Bitmap    },

#endif

//        { JUMP, 0x25D221, GET_METHOD1(LoadItp),             0, GET_METHOD1(OldLoadItp) },

        PATCH_FUNCTION(JUMP, 0, 0x25B93A, GET_METHOD1(Fade),                        0, GET_METHOD1(OldFade)),
        PATCH_FUNCTION(CALL, 0, 0x5CCF32, FadeInRate,                               1),
        PATCH_FUNCTION(JUMP, 0, 0x259FAE, GET_METHOD2(Uncompress),                  0, GET_METHOD2(OldUncompress)),
        PATCH_FUNCTION(JUMP, 0, 0x25F5EE, GET_METHOD1(FormatSEPath),                0, GET_METHOD1(OldFormatSEPath)),
        PATCH_FUNCTION(JUMP, 0, 0x25F91D, GET_METHOD3(CalcCharStatusData),          0, GET_METHOD3(OldCalcCharStatusData)),
        PATCH_FUNCTION(CALL, 0, 0x57165F, GET_METHOD3(GetBFaceIndex),               3),
        PATCH_FUNCTION(CALL, 0, 0x574A42, GET_METHOD3(NakedSkipCopyCharStatusData), 2),
        PATCH_FUNCTION(CALL, 0, 0x542DEA, GET_METHOD3(GetCraftData),                2),
        PATCH_FUNCTION(CALL, 0, 0x5AE65E, GET_METHOD3(NakedGetTurnVoice),           5),
        PATCH_FUNCTION(CALL, 0, 0x5ADEB8, GET_METHOD3(NakedGetUnderAttackVoice),    2),
        PATCH_FUNCTION(JUMP, 0, 0x25D85C, GET_METHOD3(GetMagicInfo),                0),
        PATCH_FUNCTION(JUMP, 0, 0x25B043, GET_METHOD3(GetMagicQueryTable),          0),
        PATCH_FUNCTION(JUMP, 0, 0x25C957, GET_METHOD3(GetMagicDescription),         0),
        PATCH_FUNCTION(CALL, 0, 0x5A1286, NakedAS8DHandler,                         1),
        PATCH_FUNCTION(CALL, 0, 0x5876A6, GET_METHOD3(FindEmptyPosition),           0),
        PATCH_FUNCTION(JUMP, 0, 0x25CDBC, GET_METHOD3(IsAvatarLoaded),              0, GET_METHOD3(OldIsAvatarLoaded)),
        PATCH_FUNCTION(CALL, 0, 0x5826B2, FixAvatarAngle_Magic93Handler,            2, OldFixAvatarAngle_Magic93Handler),
        PATCH_FUNCTION(CALL, 0, 0x5EF96F, GET_METHOD3(GetSBreak),                   10),
        PATCH_FUNCTION(CALL, 0, 0x47002A, MyFindFirstFileA,                         1),

//        { CALL, 0x47002A, MyFindFirstFileA, 1 },

#if D3D9_VERSION
//        { JUMP, 0x2585C3, my_fopen, 0, old_fopen },
        PATCH_FUNCTION(JUMP, 0, 0x2585C3, my_fopen, 0, old_fopen),
#endif

    };

    Nt_PatchMemory(p, countof(p), f, countof(f), hModule);

    g_AppPathBuffer = RtlAllocateHeap(CMem::GetGlobalHeap(), 0, (MAX_PATH * 2) * sizeof(WCHAR));
    g_AppPathLength = Nt_GetExecuteDirectory((PWCHAR)g_AppPathBuffer, MAX_PATH + 2);

    DllPath.Length = g_AppPathLength * 2;
    DllPath.MaximumLength = DllPath.Length;
    DllPath.Buffer = (PWCHAR)g_AppPathBuffer;
    RtlSetCurrentDirectory_U(&DllPath);

    CEDZeroBattle::m_AvatarIndex = -1;
}

LONG CALLBACK VectoredHandler(PEXCEPTION_POINTERS ExceptionInfo)
{
    SYSTEMTIME st;

    GetLocalTime(&st);
    PrintConsoleW(
        L"%02d:%02d:%02d: code = %08X, addr = %08X\r\n",
        st.wHour, st.wMinute, st.wSecond,
        ExceptionInfo->ExceptionRecord->ExceptionCode,
        ExceptionInfo->ExceptionRecord->ExceptionAddress
    );

    return EXCEPTION_CONTINUE_SEARCH;
}

#endif

#if D3D9_VERSION

#pragma comment(linker, "/EXPORT:Direct3DCreate9=_Direct3DCreate9@4")

#include <d3d9.h>

EXTC IDirect3D9* STDCALL Direct3DCreate9(UINT SDKVersion)
{
    static IDirect3D9* (STDCALL *pfDirect3DCreate9)(UINT SDKVersion);

    if (pfDirect3DCreate9 == NULL)
    {
        ULONG           Length;
        NTSTATUS        Status;
        HMODULE         hModule;
        WCHAR           szPath[MAX_NTPATH];
        UNICODE_STRING  DllPath;

        MyLib_Initialize();

        Length = Nt_GetSystemDirectory(szPath, countof(szPath));

        StrCopyW(szPath + Length, L"d3d9.dll");
        DllPath.Buffer = szPath;
        DllPath.Length = (Length + CONST_STRLEN(L"d3d9.dll")) * sizeof(WCHAR);
        DllPath.MaximumLength = DllPath.Length;

        Status = LdrLoadDll(NULL, 0, &DllPath, &hModule);
        if (!NT_SUCCESS(Status))
            return NULL;

        LdrAddRefDll(GET_MODULE_HANDLE_EX_FLAG_PIN, hModule);

        *(FARPROC *)&pfDirect3DCreate9 = Nt_GetProcAddress(hModule, "Direct3DCreate9");
        if (pfDirect3DCreate9 == NULL)
            return NULL;

#if CONSOLE_DEBUG
        AllocConsole();
#endif
    }

    if ((ULONG_PTR)_ReturnAddress() == 0x7E9045)
    {
        Init();
    }

    return pfDirect3DCreate9(SDKVersion);
}

#else

#pragma comment(linker,"/ENTRY:DllMain")
#pragma comment(linker, "/EXPORT:Direct3DCreate9=d3d9.Direct3DCreate9")

BOOL WINAPI DllMain(HINSTANCE hInstance, ULONG Reason, LPVOID lpReserved)
{
    UNREFERENCED_PARAMETER(lpReserved);

    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            LdrDisableThreadCalloutsForDll(hInstance);
            MyLib_Initialize();
            Init();
//            AddVectoredExceptionHandler(TRUE, VectoredHandler);
#if CONSOLE_DEBUG
            AllocConsole();
#endif
            break;

        case DLL_PROCESS_DETACH:
            MyLib_UnInitialize();
            break;
    }

    return TRUE;
}

#endif
