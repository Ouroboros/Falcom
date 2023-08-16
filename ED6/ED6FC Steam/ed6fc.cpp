// this file must be compiled under zh-CN locale

#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "ed6fc.h"
#include "ml.cpp"
#include "DWriteRender.h"

#pragma comment(lib, "dwrite.lib")
#pragma comment(lib, "d2d1.lib")

ML_OVERLOAD_NEW

BOOL SleepFix;
PED6_FC_FONT_RENDER GameFontRender;
API_POINTER(CreateFileA) StubCreateFileA;

BYTE FontSizeTable[] =
{
    0x08, 0x0c, 0x10, 0x14,
    0x18, 0x20, 0x12, 0x1a,
    0x1e, 0x24, 0x28, 0x2c,
    0x30, 0x32, 0x36, 0x3c,
    0x40, 0x48, 0x50, 0x60,
    0x80, 0x90, 0xa0, 0xc0,
};

USHORT FontColorTable[] =
{
    0x0fff, 0x0fc7, 0x0f52, 0x08cf, 0x0fb4, 0x08fa, 0x0888, 0x0fee, 0x0853, 0x0333,
    0x0ca8, 0x0fdb, 0x0ace, 0x0cff, 0x056b, 0x0632, 0x0135, 0x0357, 0x0bbb,
};

DWriteRender *DWriteMBCSRenders[countof(FontSizeTable)];
DWriteRender *DWriteAnsiRenders[countof(FontSizeTable)];
DWriteRender *DWriteSJISRenders[countof(FontSizeTable)];

VOID (NTAPI *StubGetGlyphsBitmap)(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex);

BOOL TranslateChar(PCSTR Text, USHORT& translated)
{
    USHORT ch;

    ch = *(PUSHORT)Text;

#if 1

    switch (ch)
    {
        default:
            return FALSE;

        case 0xA181:
        case 0xF6A1:
            translated = L'■';
            break;

        case 0x4881:
            translated = L'？';
            break;

        case 0x9F81:
            translated = L'◆';
            break;

        case 0xAA84:
            translated = L'━';
            break;

        case 0x4081:
        case 0xA1A1:
            translated = L'　';
            break;

        case 0x9A81:
            translated = L'★';
            break;

        case 0x4C87:
            translated = L'⑬';
            break;

        case 0x4D87:
            translated = L'⑭';
            break;

        case 0x5C81:    // 手册
            // translated = 0x9F84;
            translated = L'―';
            break;

        case 0x5AA9:
            translated = L'♥';
            break;

        case 0xD1A1:
            translated = L'♪';
            break;

        case 0xADA1:
            translated = L'…';
            break;

        case 0xA4A1:
            translated = L'・';
            break;
    }

#else

    switch (ch)
    {
        default:
            return FALSE;

        case 0xA181:    // 仭
        case 0x9F81:    // 仧   菱形
        case 0xAA84:    // 劒   横杠
        case 0x4081:    // 丂   空格
        case 0x9A81:    // 仛   ★
        case 0x4C87:    // 圆圈13
        case 0x4D87:    // 圆圈14
            translated = ch;
            break;

        case 0xA1A1:    // 全角空格
            translated = 0x4081;
            break;

        case 0x5C81:    // 乗   横杠
            translated = 0x9F84;
            break;

        case 0x5AA9:    // ㈱ 心形
            translated = 0x8A87;    // TAG2('噴');
            break;

        case 0xD1A1:    // ⊙ 音符
            translated = 0xF481;  // TAG2('侓');
            break;

        case 0xF6A1:    // ■ 方块
            translated = 0xA181;
            break;

        case 0xADA1:    // … 中文省略号
            translated = 0x6381;
            break;

        case 0xA4A1:    // 中点
            translated = 0x4581;
            break;
    }

#endif

    return TRUE;
}

PVOID NTAPI GetGlyphsBitmap(PCSTR Text, PVOID Buffer, ULONG Stride, ULONG ColorIndex)
{
    DWriteRender    *mbcsRender, *ansiRender, *sjisRender;
    ULONG_PTR       fontSize, fontIndex, color, width, runeWidth;

    fontIndex   = GameFontRender->FontSizeIndex;
    fontSize    = FontSizeTable[fontIndex];
    mbcsRender  = DWriteMBCSRenders[fontIndex];
    ansiRender  = DWriteAnsiRenders[fontIndex];
    sjisRender  = DWriteSJISRenders[fontIndex];
    color       = FontColorTable[ColorIndex];

    for (auto &chr : String::Decode(Text, StrLengthA(Text), CP_GBK))
    {
        USHORT translated;
        CHAR ansi = Text[0];

        if (ansi == ' ')
        {
            width = fontSize / 2;
            ++Text;
        }
        else if (ansi > 0)
        {
            ansiRender->DrawRune(chr, color, Buffer, Stride, &runeWidth);
            width = fontSize / 2;
            ++Text;
        }
        else if (TranslateChar(Text, translated))
        {
            CHAR tmp[3] = { translated & 0xFF, translated >> 8 };
            //StubGetGlyphsBitmap(tmp, Buffer, Stride, ColorIndex);

            sjisRender->DrawRune(translated, color, Buffer, Stride, &runeWidth);
            width = fontSize;
            Text += 2;
        }
        else
        {
            mbcsRender->DrawRune(chr, color, Buffer, Stride, &runeWidth);
            width = fontSize;
            Text += 2;
        }

        Buffer = PtrAdd(Buffer, (LONG_PTR)width * 2);
    }

    return Buffer;
}

PVOID FASTCALL DrawTalkText(PVOID thiz, PVOID, PVOID Buffer, ULONG Stride, PCSTR Text, ULONG ColorIndex)
{
    CHAR tmp[3] = { Text[0], Text[0] < 0 ? Text[1] : 0 };
    return GetGlyphsBitmap(tmp, Buffer, Stride * 2, ColorIndex);
}

NAKED PVOID NakedDrawDialogText(PVOID thiz, PVOID, PVOID Buffer, ULONG Stride, PCSTR Text, ULONG ColorIndex)
{
    INLINE_ASM
    {
        movzx   ebx, bl;
        push    ebx;
        lea     ebx, [esp];
        push    edx;                    // colorIndex
        mov     edx, [esp+10h];
        lea     edx, [edx*2];
        push    edx;                    // stride
        push    eax;                    // buffer
        push    ebx;                    // text
        call    GetGlyphsBitmap;
        pop     ebx;
        ret     8;
    }
}

/************************************************************************
  load file
************************************************************************/

BOOL CDECL LoadFileFromDat(PVOID buffer, ULONG datIndex, ULONG datOffset, ULONG fileSize)
{
    PED6_DIR_ENTRY entry;

    entry = DirCacheTable[datIndex];
    if (entry == nullptr)
        return FALSE;

    LOOP_FOREVER
    {
        if (entry->Offset == datOffset && entry->Size == fileSize)
            break;

        ++entry;
    }

    String path;
    NtFileDisk dat;

    GetModuleDirectory(path, nullptr);

    if (NT_SUCCESS(dat.Open(path + String::Format(L"DAT\\ED6_DT%02X\\%.*S", datIndex, sizeof(entry->FileName), entry->FileName))))
    {
#if DBG
        PrintConsoleW(L"%S\n", entry->FileName);
#endif

        *(PULONG)PtrAdd(buffer, 0) = fileSize;
        *(PULONG)PtrAdd(buffer, 4) = RAW_FILE_MAGIC;
        *(PULONG)PtrAdd(buffer, 8) = dat.GetSize32();
        return NT_SUCCESS(dat.Read(PtrAdd(buffer, 12)));
    }

    if (NT_FAILED(dat.Open(path + String::Format(L"ED6_DT%02X.dat", datIndex))))
        return FALSE;

    dat.Seek(datOffset);
    return NT_SUCCESS(dat.Read(buffer, fileSize));
}

ULONG_PTR NTAPI DecompressData(PBYTE& compressed, PBYTE& uncompressed)
{
    if (*(PULONG)&compressed[4] != RAW_FILE_MAGIC)
        return ~0u;

    ULONG size = *(PULONG)(compressed + 8);
    CopyMemory(uncompressed, compressed + 12, size);

    compressed += size + 12;
    uncompressed += size;

    return size;
}

NAKED VOID CDECL NakedLoadFileFromDat()
{
    INLINE_ASM
    {
        push    [esp + 0Ch];
        push    [esp + 0Ch];
        push    [esp + 0Ch];
        push    edi;
        call    LoadFileFromDat;
        add     esp, 10h;
        ret;
    }
}

PVOID StubNakedDecompressData;

NAKED VOID NakedDecompressData()
{
    INLINE_ASM
    {
        push    ebx;
        push    edi;
        call    DecompressData;
        inc     eax;
        jnz     UNCOMPRESSED;
        jmp     [StubNakedDecompressData];

UNCOMPRESSED:
        dec     eax;
        ret;
    }
}

/************************************************************************
  cpu usage
************************************************************************/

WNDPROC OrigGameWindowProc;

LRESULT NTAPI GameWindowProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
        case WM_ACTIVATEAPP:
            SleepFix = wParam == FALSE;
            break;
    }

    return OrigGameWindowProc(hwnd, message, wParam, lParam);
}

/************************************************************************
  init
************************************************************************/

PED6_FC_FONT_RENDER FindFontRender(PVOID BaseAddress)
{
    PVOID p;

     p = SearchPatternSafe(L"81 3D ?? ?? ?? ?? BC 02 00 00", BaseAddress, ImageNtHeaders(BaseAddress)->OptionalHeader.SizeOfImage);
     if (p == nullptr)
         return nullptr;

     return FIELD_BASE(*(PVOID *)PtrAdd(p, 2), ED6_FC_FONT_RENDER, FontWeight);
}

template<typename... ARGS>
PVOID FindAndAdvance(ULONG_PTR Advance, ARGS... args)
{
    PVOID p = SearchPatternSafe(args...);
    return p == nullptr ? IMAGE_INVALID_VA : PtrAdd(p, Advance);
}

NTSTATUS InitializeDWrite()
{
    NTSTATUS hr;
    ID2D1Factory*       factory;
    IDWriteFactory*     dwrite;
    IDWriteGdiInterop*  gdiInterop;

    factory = nullptr;
    dwrite = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        PBYTE           fontSize;
        DWriteRender**  mbcsRender = DWriteMBCSRenders;
        DWriteRender**  ansiRender = DWriteAnsiRenders;
        DWriteRender**  sjisRender = DWriteSJISRenders;

        auto createRender = [](DWriteRender**& render, PCWSTR fontPath, PCWSTR faceName, ULONG_PTR fontSize)
        {
            *render = new DWriteRender();
            if (*render == nullptr)
                return STATUS_NO_MEMORY;

            return (*render++)->Initialize(fontPath, faceName, fontSize);
        };

        FOR_EACH_ARRAY(fontSize, FontSizeTable)
        {
            hr = createRender(mbcsRender, L"font.ttf", nullptr, *fontSize);
            FAIL_BREAK(hr);

            hr = createRender(ansiRender, nullptr, L"SIMHEI", *fontSize);
            FAIL_BREAK(hr);

            hr = createRender(sjisRender, L"jpfont.ttf", nullptr, *fontSize);
            FAIL_BREAK(hr);
        }
    }

    SafeReleaseT(factory);
    SafeReleaseT(dwrite);

    return hr;
}

BOOL UnInitialize(PVOID BaseAddress)
{
#if DBG
    //PauseConsole(L"any key");
#endif

    return FALSE;
}

typedef struct
{
    PVOID       GetGlyphsBitmap;
    PVOID       DrawTalkText;
    PVOID       DrawDialogText;
    PVOID       LoadFileFromDAT;
    PVOID       DecompressData;

} ED6_FC_HOOK_FUNCTIONS, *PED6_FC_HOOK_FUNCTIONS;

NTSTATUS SearchFunctions(PED6_FC_HOOK_FUNCTIONS functions)
{
    PVOID       Address;
    PLDR_MODULE Exe;

    Exe = Ldr::FindLdrModuleByHandle(nullptr);

    FillMemory(functions, sizeof(*functions), 0xFF);

    struct
    {
        PVOID*      Address;
        ULONG_PTR   Type;
        ULONG_PTR   SearchLength;
        PCSTR       Pattern;
    } hooks[] =
    {
        { &functions->GetGlyphsBitmap,  0, 0x10, "8B 55 14 83 EC 34 83 FA 13" },
        { &functions->DrawTalkText,     0, 0x20, "8B E9 0F B6 08 C1 E1 08 0B CA 81 F9 40 81 00 00" },
        { &functions->DrawDialogText,   0, 0x20, "8B F8 80 FB 20" },
        { &functions->LoadFileFromDAT,  2, 0x30, (PCSTR)L"ED6_DT%02x.DAT" },
        { &functions->DecompressData,   0, 0x05, "83 EC 18 8B 03 89 44 24 04 8B 07" },
    };

    for (ULONG_PTR i = 0; i != countof(hooks); i++)
    {
        switch (hooks[i].Type)
        {
            case 0:
                Address = SearchPatternSafe(hooks[i].Pattern, Exe->DllBase, Exe->SizeOfImage);
                if (Address != nullptr)
                    *hooks[i].Address = ReverseSearchFunctionHeader(Address, hooks[i].SearchLength);

                break;

            case 2:
                Address = SearchStringReference(Exe, (PVOID)hooks[i].Pattern, StrLengthW((PCWSTR)hooks[i].Pattern) + 2);
                if (Address != nullptr)
                    *hooks[i].Address = ReverseSearchFunctionHeader(PtrSub(Address, 1), hooks[i].SearchLength);

                break;
        }

#if DBG
        PrintConsole(L"%p\n", *hooks[i].Address);
#endif
    }

    return STATUS_SUCCESS;
}

BOOL Initialize(PVOID BaseAddress)
{
    using namespace Mp;

    BOOL                    Success;
    ULONG_PTR               SizeOfImage;
    PVOID                   FaceBuffer;
    PLDR_MODULE             ExeModule;
    ED6_FC_HOOK_FUNCTIONS   Functions;

    LdrDisableThreadCalloutsForDll(BaseAddress);

    if (ImageNtHeaders(Ps::CurrentPeb()->ImageBaseAddress)->FileHeader.TimeDateStamp != 0x590BDEA4)
        return TRUE;

    ml::MlInitialize();

#if DBG

    AllocConsole();

#endif

    BaseAddress = GetExeModuleHandle();

    //
    // FT_Load_Glyph
    // FT_Get_Glyph
    // FT_Render_Glyph
    // FT_Glyph_To_Bitmap
    //

    Rtl::SetExeDirectoryAsCurrent();

    Success = NT_SUCCESS(InitializeDWrite());
    PatchExeText(BaseAddress);

    //DWriteRenders[9]->DrawRune(L'P', FontColorTable[0], 0, 0, 0), Ps::ExitProcess(0);

    if (Success)
    {
        GameFontRender = FindFontRender(BaseAddress);
        Success = GameFontRender != nullptr;
    }

    FAIL_RETURN(SearchFunctions(&Functions));

    ExeModule = FindLdrModuleByHandle(nullptr);

    /*
        char width
        004B1A31   |.  56                  push    esi
        004B1A32   |.  8D71 E0             lea     esi, dword ptr [ecx-0x20]
        004B1A35   |.  83FE 5F             cmp     esi, 0x5F
        004B1A38   |.  5E                  pop     esi
        004B1A39   |.  76 29               jbe     short 0x4B1A64
        004B1A3B   |.  3C 80               cmp     al, 0x80
        004B1A3D   |.  72 08               jb      short 0x4B1A47
        004B1A3F   |.  3C A0               cmp     al, 0xA0
        004B1A41   |.  72 18               jb      short 0x4B1A5B
        004B1A43   |.  3C E0               cmp     al, 0xE0
        004B1A45   |.  73 14               jnb     short 0x4B1A5B
    */
    SearchAllPatterns(
        L"76 ?? ?? 80 72 ?? ?? A0 72 ?? ?? E0 73 ??",
        ExeModule->DllBase,
        ExeModule->SizeOfImage,
        [](const ml::GrowableArray<PVOID>& references)
        {
            PVOID* addr;

            FOR_EACH_VEC(addr, references)
            {
                BYTE data = 0xC;
                Mm::WriteProtectMemory(CurrentProcess, PtrAdd(*addr, 1), &data, 1);
            }
        }
    );

    /*
        004667DA    .  80F9 80             cmp     cl, 0x80
        004667DD    .  72 31               jb      short 0x466810
        004667DF    .  80F9 A0             cmp     cl, 0xA0
        004667E2    .  72 05               jb      short 0x4667E9
        004667E4    .  80F9 E0             cmp     cl, 0xE0
        004667E7    .  72 4B               jb      short 0x466834
    */
    SearchAllPatterns(
        L"80 ?? 80 72 ?? 80 ?? A0 72 ?? 80 ?? E0",
        ExeModule->DllBase,
        ExeModule->SizeOfImage,
        [](const ml::GrowableArray<PVOID>& references)
        {
            PVOID* addr;

            FOR_EACH_VEC(addr, references)
            {
                BYTE data = 0xEB;
                Mm::WriteProtectMemory(CurrentProcess, PtrAdd(*addr, 8), &data, 1);
            }
        }
    );

    /*
        004837F0    .  3C 80               cmp     al, 0x80
        004837F2    .  72 0F               jb      short 0x483803
        004837F4    .  3C A0               cmp     al, 0xA0
        004837F6    .  72 04               jb      short 0x4837FC
        004837F8    .  3C E0               cmp     al, 0xE0
        004837FA    .  72 07               jb      short 0x483803
    */
    SearchAllPatterns(
        L"3C 80 72 ?? 3C A0 72 ?? 3C E0",
        ExeModule->DllBase,
        ExeModule->SizeOfImage,
        [](const ml::GrowableArray<PVOID>& references)
        {
            PVOID* addr;

            FOR_EACH_VEC(addr, references)
            {
                BYTE data = 0xEB;
                Mm::WriteProtectMemory(CurrentProcess, PtrAdd(*addr, 6), &data, 1);
            }
        }
    );
    
    /*
        00476198   |.  3C 80               |cmp     al, 0x80
        0047619A   |.  0F82 50010000       |jb      0x4762F0
        004761A0   |.  3C A0               |cmp     al, 0xA0
        004761A2       72 08               |jb      short 0x4761AC
        004761A4   |.  3C E0               |cmp     al, 0xE0
        004761A6   |.  0F82 44010000       |jb      0x4762F0
    */
    SearchAllPatterns(
        L"3C 80 0F ?? ?? ?? ?? ?? 3C A0 72 ?? 3C E0",
        ExeModule->DllBase,
        ExeModule->SizeOfImage,
        [](const ml::GrowableArray<PVOID>& references)
        {
            PVOID* addr;

            FOR_EACH_VEC(addr, references)
            {
                BYTE data = 0xEB;
                Mm::WriteProtectMemory(CurrentProcess, PtrAdd(*addr, 0xA), &data, 1);
            }
        }
    );

    /*
        00483950   |> /8801                /mov     byte ptr [ecx], al
        00483952   |. |3C 80               |cmp     al, 0x80
        00483954   |. |73 04               |jnb     short 0x48395A
        00483956   |. |33C0                |xor     eax, eax
        00483958   |. |EB 10               |jmp     short 0x48396A
        0048395A   |> |3C A0               |cmp     al, 0xA0
        0048395C   |. |73 07               |jnb     short 0x483965
        0048395E   |. |B8 01000000         |mov     eax, 0x1
        00483963   |. |EB 05               |jmp     short 0x48396A

        copy chr name
    */
    SearchAllPatterns(
        L"3C 80 73 ?? 33 C0 EB ?? 3C A0 73 ?? ?? 01 00 00 00 EB ??",
        ExeModule->DllBase,
        ExeModule->SizeOfImage,
        [](const ml::GrowableArray<PVOID>& references)
        {
            PVOID* addr;

            FOR_EACH_VEC(addr, references)
            {
                BYTE data = 0;
                Mm::WriteProtectMemory(CurrentProcess, PtrAdd(*addr, 0xB), &data, 1);
            }
        }
    );

    static FLOAT DefaultPlaceNameTextDeltaX = 0;

    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchVa(
            (ULONG64)(API_POINTER(::CreateFileA))[] (LPCSTR lpFileName, DWORD dwDesiredAccess, DWORD dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, DWORD dwCreationDisposition, DWORD dwFlagsAndAttributes, HANDLE hTemplateFile) -> HANDLE
            {
                if (StrCompareA(lpFileName, "dll\\lang_jpn.dll") == 0)
                {
                    lpFileName = "ed6_win.exe";
                }

                return StubCreateFileA(lpFileName, dwDesiredAccess, dwShareMode, lpSecurityAttributes, dwCreationDisposition, dwFlagsAndAttributes, hTemplateFile);
            },
            sizeof(PVOID), LookupImportTable(BaseAddress, nullptr, KERNEL32_CreateFileA)
        ),

        MemoryPatchVa(
            (ULONG64)(API_POINTER(::Sleep))[] (ULONG ms) -> VOID
            {
                Ps::Sleep(SleepFix ? ms == 0 ? 1 : ms : ms);
            },
            sizeof(PVOID), LookupImportTable(BaseAddress, nullptr, KERNEL32_Sleep)
        ),

        MemoryPatchVa(
            (ULONG64)(API_POINTER(SetWindowPos))[](HWND Wnd, HWND InsertAfter, int X, int Y, int cx, int cy, UINT Flags) -> BOOL
            {
                if (Flags == SWP_NOMOVE)
                {
                    RECT WorkArea;

                    SystemParametersInfoW(SPI_GETWORKAREA, 0, &WorkArea, 0);
                    X = ((WorkArea.right - WorkArea.left) - cx) / 2;
                    Y = ((WorkArea.bottom - WorkArea.top) - cy) / 2;

                    CLEAR_FLAG(Flags, SWP_NOMOVE);

                    OrigGameWindowProc = (WNDPROC)SetWindowLongPtrW(Wnd, GWLP_WNDPROC, (LONG_PTR)GameWindowProc);
                }

                return SetWindowPos(Wnd, InsertAfter, X, Y, cx, cy, Flags);
            },
            sizeof(PVOID),
            LookupImportTable(GetExeModuleHandle(), nullptr, USER32_SetWindowPos)
        ),

        // cmp r8, 80
        // 80 ?? 80 72 ?? 80 ?? A0 72 ?? 80 ?? E0 72 ??
        // 3C 80 72 ?? 3C A0 72 ?? 3C E0 72 ??
        // 3C 80 72 ?? 3C A0 72 ?? 3C E0 73 ??
        //MemoryPatchVa(0xEBull, 1, 0x46A2E2),
        //MemoryPatchVa(0xEBull, 1, 0x479C27),
        //MemoryPatchVa(0xEBull, 1, 0x47B8A1),
        //MemoryPatchVa(0xEBull, 1, 0x48540B),
        //MemoryPatchVa(0xEBull, 1, 0x485941),
        //MemoryPatchVa(0xEBull, 1, 0x4888E5),
        //MemoryPatchVa(0x00ull, 1, 0x488A6D),
        //MemoryPatchVa(0xEBull, 1, 0x488E37),
        //MemoryPatchVa(0xEBull, 1, 0x4B8FE1),
        //MemoryPatchVa(0xEBull, 1, 0x4B9044),
        //MemoryPatchVa(0xEBull, 1, 0x4B90C5),
        //MemoryPatchVa(0xEBull, 1, 0x4B915D),
        //MemoryPatchVa(0xEBull, 1, 0x4B930C),
        //MemoryPatchVa(0xEBull, 1, 0x4B937C),
        //MemoryPatchVa(0xEBull, 1, 0x4B942B),
        //MemoryPatchVa(0xEBull, 1, 0x4DB6CD),

        /************************************************************************
         calc ansi char width

        004B7926    .  8D51 E0             lea     edx, dword ptr [ecx-0x20]
        004B7929    .  83FA 5F             cmp     edx, 0x5F
        004B792C       76 40               jbe     short 0x4B796E                   <--
        004B792E    .  3C 80               cmp     al, 0x80
        004B7930    .  72 08               jb      short 0x4B793A
        004B7932    .  3C A0               cmp     al, 0xA0
        004B7934    .  EB 23               jmp     short 0x4B7959                   <==
        004B7936    .  3C E0               cmp     al, 0xE0
        004B7938    .  73 1F               jnb     short 0x4B7959

        76 ?? ?? 80 72 ?? ?? A0 72 ?? ?? E0 73 ??
        ************************************************************************/
        // MemoryPatchVa(0xCull, 1, 0x4B8FDA),
        // MemoryPatchVa(0xCull, 1, 0x4B792D),
        // MemoryPatchVa(0xCull, 1, 0x4B79AE),
        // MemoryPatchVa(0xCull, 1, 0x4B7A46),
        // MemoryPatchVa(0xCull, 1, 0x4B7D14),

        // 物品已有个数窗口位置
        //CWindow::CWindow(104, 14, ...)         // 4743A0
        MemoryPatchVa(0x104ull, 4, 0x49345F),  // x
        MemoryPatchVa(0x14ull,  4, 0x493473),  // width
        MemoryPatchVa(0x104ull, 4, 0x49689C),  // x
        MemoryPatchVa(0x14ull,  4, 0x4968B0),  // width

        // 战斗状态
        MemoryPatchVa(0xC98B0000003Eull,  6, 0x43AEA9),  // hp fixed x

        // char type switch table
        MemoryPatchVa(0x0404ull,    2, 0x48102E),

        // jp font size limit
        MemoryPatchVa(0xEBull,      1, 0x4D6FA4),

        // HP EP font size
        MemoryPatchVa(0x02ull,      1, 0x47223B),

        // place name text X delta
        MemoryPatchVa((ULONG64)&DefaultPlaceNameTextDeltaX,      4, 0x4B1C41),

        FunctionJumpVa(Success ? Functions.GetGlyphsBitmap       : IMAGE_INVALID_VA, GetGlyphsBitmap, &StubGetGlyphsBitmap),
        FunctionJumpVa(Success ? Functions.DrawTalkText          : IMAGE_INVALID_VA, DrawTalkText),
        FunctionJumpVa(Success ? Functions.DrawDialogText        : IMAGE_INVALID_VA, NakedDrawDialogText),

        FunctionJumpVa(Functions.LoadFileFromDAT,    LoadFileFromDat),
        FunctionJumpVa(Functions.DecompressData,     NakedDecompressData, &StubNakedDecompressData),
    };

    PatchMemory(p, countof(p), BaseAddress);

    *(PVOID *)&StubCreateFileA = (PVOID)p[0].Memory.Backup;

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
