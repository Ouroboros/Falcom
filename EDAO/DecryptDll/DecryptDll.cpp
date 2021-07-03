#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "MyLibrary.cpp"

LONG STDCALL DecCallback(PVOID, LPWIN32_FIND_DATAW pfd, ULONG_PTR)
{
    ULONG Header;
    NTSTATUS Status;
    NtFileDisk file, filesrc;

    file.Open(pfd->cFileName);
    file.Read(&Header, 4);
    file.Close();

    if (Header != TAG4('SDFA'))
        return 0;

    CHAR FileName[MAX_PATH];

    PrintConsoleW(L"%s\n", pfd->cFileName);

/*
    UnicodeToAnsi(FileName, countof(FileName), pfd->cFileName);

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
*/
    filesrc.Open(pfd->cFileName);
    Header = filesrc.GetSize32();
    PBYTE p = (PBYTE)AllocateMemory(Header);
    filesrc.Read(p, Header);
    filesrc.Close();

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
    CreateDirectoryRecursiveW(pfd->cFileName);
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

EXTC_EXPORT VOID CDECL dec()
{
    SetPriorityClass(NtCurrentProcess(), BELOW_NORMAL_PRIORITY_CLASS);
    AllocConsole();
    SetExeDirectoryAsCurrent();

    EnumDirectoryFiles(
        NULL,
        L"*.*",
        0,
        L"data",
        NULL,
        DecCallback,
        0,
        EDF_SUBDIR
    );

    FreeConsole();

    Ps::ExitProcess(0);
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{


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
