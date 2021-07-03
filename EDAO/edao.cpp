#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "edao.h"
#include "SoundArc.h"
#include "MyLibrary.cpp"
#include "edao_vm.h"

using ml::String;

#if !D3D9_VER
    #undef ENABLE_LOG
    #define ENABLE_LOG 0
    #define DEBUG_DISABLE_PATCH 0
#endif

#define ENABLE_LOG  0

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved);

TYPE_OF(&NtOpenFile)            StubNtOpenFile;
TYPE_OF(&NtCreateFile)          StubNtCreateFile;
TYPE_OF(&NtQueryAttributesFile) StubNtQueryAttributesFile;


void WriteLog(PCWSTR Format, ...)
{
#if ENABLE_LOG

    NtFileDisk log;
    WCHAR Buffer[0xFF0];

    log.CreateIfNotExist(L"log.txt");
    if (log.GetSize32() == 0)
    {
        ULONG BOM = BOM_UTF16_LE;
        log.Write(&BOM, 2);
    }

    log.Seek(0, FILE_END);

    log.Write(Buffer, vswprintf(Buffer, Format, (va_list)(&Format + 1)) * 2);
    log.Write(L"\r\n", 4);

#endif
}

#if !ENABLE_LOG
    #define WriteLog(...)
#endif
/*
VOID THISCALL EDAO::Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6)
{
    if (GetAsyncKeyState(VK_LSHIFT) >= 0)
        (this->*StubFade)(Param1, Param2, Param3, Param4, Param5, Param6);
}
float Rate = 200.f;
float fuck = 0.17f;

NAKED VOID FadeInRate()
{
    INLINE_ASM
    {
        //fld     dword ptr [eax+0x40];
        fld     fuck;
        fmul    Rate;
        ret;
    }
}
*/

BOOL    Turbo;
WNDPROC WindowProc;

SHORT NTAPI AoGetKeyState(int VirtualKey)
{
    switch (VirtualKey)
    {
        case VK_LSHIFT:
            VirtualKey = VK_SHIFT;

        case VK_SHIFT:
            if (!Turbo)
                break;

            ++*EDAO::GlobalGetEDAO()->GetMap()->GetFrameNumber();

            return (SHORT)0xFFFF8001;
    }

    return GetKeyState(VirtualKey);
}

LRESULT NTAPI MainWndProc(HWND Window, UINT Message, WPARAM wParam, LPARAM lParam)
{
    switch (Message)
    {
        case WM_KEYUP:
            switch (LOWORD(wParam))
            {
                case 'T':
                    Turbo ^= TRUE;
                    break;

                //case 'J':
                //    EDAO::GlobalGetEDAO()->JumpToMap();
                //    break;
            }
            break;
    }

    return WindowProc(Window, Message, wParam, lParam);
}

VOID ChangeMainWindowProc(HWND GameWindow)
{
    if (GameWindow != nullptr)
        WindowProc = (WNDPROC)SetWindowLongPtrA(GameWindow, GWL_WNDPROC, (LONG_PTR)MainWndProc);
}

HWND WINAPI CreateWindowExCenterA(ULONG dwExStyle, LPCSTR lpClassName, LPCSTR lpWindowName, ULONG dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
{
    HWND    Window;
    RECT    rcWordArea;
    ULONG   Length;
    PWSTR   pszClassName, pszWindowName;

    Length = StrLengthA(lpClassName) + 1;
    pszClassName = (PWSTR)AllocStack(Length * sizeof(WCHAR));
    AnsiToUnicode(pszClassName, Length, lpClassName, Length);

    Length = StrLengthA(lpWindowName) + 1;
    pszWindowName = (PWSTR)AllocStack(Length * sizeof(WCHAR));
    AnsiToUnicode(pszWindowName, Length, lpWindowName, Length);

    if (SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcWordArea, 0))
    {
        X = ((rcWordArea.right - rcWordArea.left) - nWidth) / 2;
        Y = ((rcWordArea.bottom - rcWordArea.top) - nHeight) / 2;
    }

    Window = CreateWindowExW(dwExStyle, pszClassName, pszWindowName, dwStyle, X, Y, nWidth, nHeight, hWndParent, hMenu, hInstance, lpParam);
    ChangeMainWindowProc(Window);

    return Window;
}

typedef struct
{
    String Original;
    String Redirected;

} FILE_REDIRECT_ENTRY, *PFILE_REDIRECT_ENTRY;

typedef GrowableArray<FILE_REDIRECT_ENTRY> FILE_REDIRECT_ENTRY_VEC, *PFILE_REDIRECT_ENTRY_VEC;

PFILE_REDIRECT_ENTRY_VEC GlobalRedirectEntry;

NTSTATUS InitializeRedirectEntry()
{
    NTSTATUS        Status;
    PLDR_MODULE     Module;
    UNICODE_STRING  ExeNtPathString;

    auto RedirectSubDirectory = new GrowableArray<FILE_REDIRECT_ENTRY>;

    if (RedirectSubDirectory == nullptr)
        return STATUS_NO_MEMORY;

    GlobalRedirectEntry = RedirectSubDirectory;

    String ExeNtPath, DataPath;

    Module = FindLdrModuleByHandle(nullptr);
    FAIL_RETURN(NtFileDisk::QueryFullNtPath(Module->FullDllName.Buffer, &ExeNtPathString));

    ExeNtPath = ExeNtPathString;
    RtlFreeUnicodeString(&ExeNtPathString);

    ExeNtPath = ExeNtPath.SubString(0, ExeNtPath.GetCount() - Module->BaseDllName.Length / sizeof(Module->BaseDllName.Buffer[0]));
    DataPath = ExeNtPath + L"data\\";

    RedirectSubDirectory->Add({});
    RedirectSubDirectory->Add({ DataPath, ExeNtPath + L"Ouroboros\\" });
    RedirectSubDirectory->Add({ DataPath, ExeNtPath + L"patch\\" });

    for (ULONG_PTR index = 1; ;++index)
    {
        auto patch = String::Format(L"%spatch%d\\", ExeNtPath, index);

        if (Io::IsPathExists(patch) == FALSE)
            break;

        RedirectSubDirectory->Add({ DataPath, patch});
    }

    return STATUS_SUCCESS;
}

NTSTATUS GetRedirectedFileName(PUNICODE_STRING OriginalFile, PUNICODE_STRING RedirectedFile)
{
    ULONG_PTR                   Length, BufferLength;
    PWSTR                       Buffer;
    NTSTATUS                    Status;
    UNICODE_STRING              SubFilePath, Redirected, OriginalPath;
    OBJECT_ATTRIBUTES           oa;
    FILE_BASIC_INFORMATION      FileBasic;
    PFILE_REDIRECT_ENTRY        Entry;

    RtlInitEmptyString(RedirectedFile);

    if (GlobalRedirectEntry == nullptr)
        return STATUS_FLT_NOT_INITIALIZED;

    if (OriginalFile == nullptr || OriginalFile->Buffer == nullptr)
    {
        return STATUS_INVALID_PARAMETER;
    }

    Status = NtFileDisk::QueryFullNtPath(OriginalFile->Buffer, &OriginalPath);
    FAIL_RETURN(Status);

    BufferLength = MAX_NTPATH * sizeof(WCHAR);
    Buffer = (PWSTR)AllocStack(BufferLength);
    SubFilePath = OriginalPath;

    FOR_EACH_VEC_REVERSE(Entry, *GlobalRedirectEntry)
    {
        if (!Entry->Original)
            return STATUS_NOT_FOUND;

        auto RedirectedSize = Entry->Redirected.GetSize();
        auto OriginalSize = Entry->Original.GetSize();

        if (OriginalPath.Length <= OriginalSize)
            continue;

        SubFilePath.Length = OriginalSize;
        if (!RtlEqualUnicodeString(&SubFilePath, Entry->Original, TRUE))
            continue;

        Length = RedirectedSize + OriginalPath.Length - SubFilePath.Length + sizeof(WCHAR);
        if (Length > BufferLength)
        {
            Buffer = (PWSTR)AllocStack(Length - BufferLength);
            BufferLength = Length;
        }

        Length = OriginalPath.Length - SubFilePath.Length;

        CopyMemory(Buffer, (PCWSTR)Entry->Redirected, RedirectedSize);
        CopyMemory(PtrAdd(Buffer, RedirectedSize), PtrAdd(OriginalPath.Buffer, SubFilePath.Length), Length);
        Length += RedirectedSize;
        *PtrAdd(Buffer, Length) = 0;

        Redirected.Length           = (USHORT)Length;
        Redirected.MaximumLength    = Redirected.Length;
        Redirected.Buffer           = Buffer;

        InitializeObjectAttributes(&oa, &Redirected, OBJ_CASE_INSENSITIVE, nullptr, 0);
        Status = StubNtQueryAttributesFile(&oa, &FileBasic);
        if (NT_SUCCESS(Status) &&
            FileBasic.FileAttributes != INVALID_FILE_ATTRIBUTES &&
            FLAG_OFF(FileBasic.FileAttributes, FILE_ATTRIBUTE_DIRECTORY))
        {
            Status = RtlDuplicateUnicodeString(RTL_DUPSTR_ADD_NULL, &Redirected, RedirectedFile);
            if (NT_SUCCESS(Status))
                break;
        }
    }

    RtlFreeUnicodeString(&OriginalPath);

    return STATUS_SUCCESS;
}

NTSTATUS
NTAPI
AoOpenFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    ULONG               ShareAccess,
    ULONG               OpenOptions
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectedFileName(ObjectAttributes->ObjectName, &Redirected);
        FAIL_BREAK(Status);

        LocalObjectAttributes               = *ObjectAttributes;
        LocalObjectAttributes.ObjectName    = &Redirected;
        LocalObjectAttributes.RootDirectory = nullptr;

        CLEAR_FLAG(LocalObjectAttributes.Attributes, OBJ_INHERIT);

        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtOpenFile(FileHandle, DesiredAccess, ObjectAttributes, IoStatusBlock, ShareAccess, OpenOptions);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

NTSTATUS
NTAPI
AoCreateFile(
    PHANDLE             FileHandle,
    ACCESS_MASK         DesiredAccess,
    POBJECT_ATTRIBUTES  ObjectAttributes,
    PIO_STATUS_BLOCK    IoStatusBlock,
    PLARGE_INTEGER      AllocationSize,
    ULONG               FileAttributes,
    ULONG               ShareAccess,
    ULONG               CreateDisposition,
    ULONG               CreateOptions,
    PVOID               EaBuffer,
    ULONG               EaLength
)
{
    NTSTATUS            Status;
    UNICODE_STRING      RedirectedFile;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;

    RtlInitEmptyString(&RedirectedFile);

    if (ObjectAttributes != nullptr)
    {
        if (NT_SUCCESS(GetRedirectedFileName(ObjectAttributes->ObjectName, &RedirectedFile)))
        {
            LocalObjectAttributes               = *ObjectAttributes;
            LocalObjectAttributes.ObjectName    = &RedirectedFile;
            LocalObjectAttributes.RootDirectory = nullptr;

            CLEAR_FLAG(LocalObjectAttributes.Attributes, OBJ_INHERIT);

            ObjectAttributes = &LocalObjectAttributes;
        }
    }

    Status = StubNtCreateFile(
                FileHandle,
                DesiredAccess,
                ObjectAttributes,
                IoStatusBlock,
                AllocationSize,
                FileAttributes,
                ShareAccess,
                CreateDisposition,
                CreateOptions,
                EaBuffer,
                EaLength
            );

    RtlFreeUnicodeString(&RedirectedFile);

    return Status;
}

NTSTATUS
NTAPI
AoQueryAttributesFile(
    POBJECT_ATTRIBUTES      ObjectAttributes,
    PFILE_BASIC_INFORMATION FileInformation
)
{
    NTSTATUS            Status;
    OBJECT_ATTRIBUTES   LocalObjectAttributes;
    UNICODE_STRING      Redirected;

    RtlInitEmptyString(&Redirected);

    LOOP_ONCE
    {
        if (ObjectAttributes == nullptr)
            break;

        Status = GetRedirectedFileName(ObjectAttributes->ObjectName, &Redirected);
        FAIL_BREAK(Status);

        LocalObjectAttributes               = *ObjectAttributes;
        LocalObjectAttributes.ObjectName    = &Redirected;
        LocalObjectAttributes.RootDirectory = nullptr;

        CLEAR_FLAG(LocalObjectAttributes.Attributes, OBJ_INHERIT);

        ObjectAttributes = &LocalObjectAttributes;
    }

    Status = StubNtQueryAttributesFile(ObjectAttributes, FileInformation);

    RtlFreeUnicodeString(&Redirected);

    return Status;
}

HANDLE NTAPI AoFindFirstFileA(PCSTR FileName, PWIN32_FIND_DATAA FindFileData)
{
    NTSTATUS        Status;
    HANDLE          FindHandle;
    ML_FIND_DATA    FindData;
    UNICODE_STRING  FileToFind, RedirectedFile;

    Status = AnsiToUnicodeString(&FileToFind, FileName);
    if (NT_FAILED(Status))
        return nullptr;

    Status = GetRedirectedFileName(&FileToFind, &RedirectedFile);
    Status = QueryFirstFile(
                    &FindHandle,
                    NT_SUCCESS(Status) ? RedirectedFile.Buffer : FileToFind.Buffer,
                    &FindData
                );

    RtlFreeUnicodeString(&FileToFind);
    RtlFreeUnicodeString(&RedirectedFile);

    FindFileData->cFileName[0] = 0;

    if (NT_FAILED(Status))
        return nullptr;

    UnicodeToAnsi(FindFileData->cFileName, countof(FindFileData->cFileName), FindData.FileName);

    return FindHandle;
}

BOOL AoIsFileExist(PCSTR FileName)
{
    BOOL            Exists;
    NTSTATUS        Status;
    UNICODE_STRING  FileToCheck;

    Status = AnsiToUnicodeString(&FileToCheck, FileName);
    if (NT_FAILED(Status))
        return FALSE;

    Exists = IsPathExists(FileToCheck.Buffer);

    RtlFreeUnicodeString(&FileToCheck);

    return Exists;
}

LONG NTAPI ShowExitMessageBox(HWND hWnd, PCSTR Text, PCSTR Caption, UINT Type)
{
    ULONG_PTR   Length;
    PSTR        Buffer;

    Length = StrLengthA(Text) + 1;
    Buffer = (PSTR)AllocStack(Length + 3);

    *(PULONG)&Buffer[0] = TAG3('#5C');
    CopyMemory(Buffer + 3, Text, Length);

    return EDAO::GlobalGetEDAO()->AoMessageBox(Buffer) == TRUE ? IDYES : IDNO;
}

// [0xC29988]+78f84

LONG64 InitWarningItpTimeStamp()
{
    return -1;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

#define METHOD_PTR(_method) PtrAdd((PVOID)NULL, _method)

#include "xxoo.hpp"

VOID NTAPI PrintOP(LONG sub, LONG offset, PBYTE base)
{
    //if (sub == 0) offset -= 4;

    if (offset == 0x1572)
        MessageBoxW(0,0,0,0);

    //AllocConsole();PrintConsoleA("%02X, %08X, %02X\n", sub, offset, base[offset]);
    WriteLog(L"%02X, %08X, %02X", sub, offset, base[offset]);
}

NAKED VOID xxx()
{
    INLINE_ASM
    {
        push    eax;
        push    edx;
        push    dword ptr [ecx + 2];
        and     dword ptr [esp], 0xFF;
        mov     al, byte ptr [eax+edx];
        mov     byte ptr [ebp-0x29], al;
        call    PrintOP;
        ret;
    }
}

// 90F793

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();

    LdrDisableThreadCalloutsForDll(BaseAddress);
    SetExeDirectoryAsCurrent();

    InitializeRedirectEntry();

    static DOUBLE DefaultDistance = 0.f;

    BYTE PushActorDistance[6] = { 0xDD, 0x05 };

    *(DOUBLE **)&PushActorDistance[2] = &DefaultDistance;

    using namespace Mp;

    PATCH_MEMORY_DATA p[] =
    {
        MemoryPatchRva(0xEB,      1, 0x2C15B7),    // bypass CGlobal::SetStatusDataForChecking

#if !DEBUG_DISABLE_PATCH

        MemoryPatchRva(0x06,              1, 0x410731),   // win
        MemoryPatchRva(0x06,              1, 0x410AD1),   // win
        MemoryPatchRva(0x01,              1, 0x40991D),   // cpu
        MemoryPatchRva(0x91,              1, 0x2F9EE3),   // one hit
        MemoryPatchRva(0x3FEB,            2, 0x452FD1),   // bypass savedata checksum
        MemoryPatchRva(0x20000,           4, 0x4E71B2),   // chrimg max buffer size

        MemoryPatchRva(CraftConditions::CraftReflect, 4, 0x7E1858),    // predefined flag

        // debug AT

        MemoryPatchRva(0x49EB,    2, 0x5F668D),    // disable orig at
        MemoryPatchRva(0x81,      1, 0x5F66D9),    // disable orig at
        MemoryPatchRva(0x80,      1, 0x5F68A4),    // force show debug at
        MemoryPatchRva(0x2C,      1, 0x5F693D),    // debug at pos.X advance

        // tweak

        MemoryPatchRva(PushActorDistance, sizeof(PushActorDistance), 0x6538EF),
        MemoryPatchRva(PushActorDistance, sizeof(PushActorDistance), 0x653BBE),

        MemoryPatchRva(0x00ull,   1, 0x653972),       // box height
        MemoryPatchRva(0x00ull,   1, 0x653C31),       // monster height
        MemoryPatchRva(0x00ull,   1, 0x655E64),       // actor height (mini map)

        MemoryPatchRva(0xEB,      1,  0x2CAA98),      // enable shimmer when width > 1024
        MemoryPatchRva(0xEB,      1,  0x2C33BE),      // enable blur when width > 1024
        MemoryPatchRva(0xEB,      1,  0x2EFBB8),      // capture ?

        MemoryPatchRva(0x00ull,   1,  0x55F6E1),      // ±¬Áé

        // monster info
        MemoryPatchRva(0xEB,      1,  0x626AC8),      // bypass check is enemy


        // buf fix
        MemoryPatchRva(0xEB,      1,  0x60CC8F),      // burst energy
        MemoryPatchRva(0x32,      1,  0x54FDA4),      // text length of menu item created by MenuCmd(1, x, x)
        // MemoryPatchRva(0x37,      1,  0x5006B8),      // dead lock while exiting

        //MemoryPatchRva(0x00,  1,  0x5304C9),      // skip op Sleep

        // iat hook

        MemoryPatchRva((ULONG64)AoGetKeyState,         4, 0x9D5A00),        // GetKeyState

#if !D3D9_VER

        MemoryPatchRva(0x1CEB,                2, 0x64ACFE),                 // remove crappy mouse control @ PositionWindow
        MemoryPatchRva(0x00ull,               4, 0x329851),                 // disable stupid get joy stick pos
        MemoryPatchRva(8 * sizeof(ULONG_PTR), 4, 0x403E92),                 // fix WNDCLASS::cbWndExtra
        MemoryPatchRva((ULONG64)CreateWindowExCenterA, 4, 0x9D59E8),        // CreateWindowExA

#endif

#endif // DEBUG_DISABLE_PATCH

        // crack

#if !D3D9_VER

        FunctionJumpRva(0x27969D, &CBattle::SetSelectedAttack),
        FunctionJumpRva(0x275DF4, &CBattle::SetSelectedCraft),
        FunctionJumpRva(0x272AB9, &CBattle::SetSelectedSCraft),

        FunctionJumpRva(0x279986, &CSSaveData::SaveData2SystemData),
        FunctionJumpRva(0x279FA8, &CSSaveData::SystemData2SaveData),

#endif // D3D9_VER

        FunctionJumpRva(0x279553, &CBattle::SetSelectedMagic),
        // FunctionCallRva(0x51E1C7, xxx),

#if !DEBUG_DISABLE_PATCH

        // tweak

        // FunctionCallRva(0x40492A, ShowExitMessageBox),
        FunctionCallRva(0x3640A1, InitWarningItpTimeStamp),   // bypass show warning.itp
        FunctionCallRva(0x3E2B42, EDAO::NakedLoadSaveDataThumb),
        FunctionCallRva(0x465F08, EDAO::NakedSetSaveDataScrollStep),

        FunctionJumpRva(0x279AA3, &EDAO::CheckItemEquipped, &EDAO::StubCheckItemEquipped),
        FunctionCallRva(0x5DE1D9, &CBattle::NakedNoResistConditionUp),

        FunctionCallRva(0x5F690B, CBattle::FormatBattleChrAT),
        FunctionCallRva(0x5B05C6, CBattle::ShowSkipCraftAnimeButton),

        FunctionJumpRva(0x46B6A0, &CSoundPlayer::GetSoundControlWindow),
        FunctionJumpVa (LookupExportTable(FindLdrModuleByName(&WCS2US(L"USER32.dll"))->DllBase, USER32_SendMessageA), CSoundPlayer::StaticDispatchCtrlCode, &CSoundPlayer::StubStaticDispatchCtrlCode),

        FunctionCallRva(0x328C77, &CInput::HandleMainInterfaceInputState, &CInput::StubHandleMainInterfaceInputState),

        // patch max se index

        MemoryPatchRva((ULONG64)0xEB, 1, 0x50EC22),
        FunctionJumpRva(0x2795B2, &CSound::GetSoundPathByIndex, &CSound::StubGetSoundPathByIndex),

        // bug fix

        FunctionCallRva(0x5B1BE6, &CBattleATBar::LookupReplaceAtBarEntry),
        FunctionJumpRva(0x275DAE, &CBattle::ExecuteActionScript, &CBattle::StubExecuteActionScript),
        FunctionJumpRva(0x550C90, &CScript::ScpSaveRestoreParty, &CScript::StubScpSaveRestoreParty),

        FunctionCallRva(0x6A58FF, CMiniGame::HorrorHouse_GetMonsterPosition),


        // file redirection

        FunctionJumpVa (NtOpenFile,               AoOpenFile,             &StubNtOpenFile),
        FunctionJumpVa (NtCreateFile,             AoCreateFile,           &StubNtCreateFile),
        FunctionJumpVa (NtQueryAttributesFile,    AoQueryAttributesFile,  &StubNtQueryAttributesFile),
        FunctionCallRva(0x48C1EA,                 AoFindFirstFileA),
        FunctionCallRva(0x48C206,                 NtClose),
        FunctionCallRva(0x4E6A0B,                 EDAO::GetCampImage),
        FunctionCallRva(0x5A05B4,                 EDAO::GetBattleFace),
        FunctionCallRva(0x2F9101,                 EDAO::GetFieldAttackChr),
        FunctionCallRva(0x4948B9,                 &EDAO::GetCFace),
        FunctionCallRva(0x4948DF,                 &EDAO::GetCFace),


        // custom format itp / itc
        //INLINE_HOOK_JUMP_RVA(0x273D24, METHOD_PTR(&EDAOFileStream::Uncompress), EDAOFileStream::StubUncompress),


        // hack for boss

        FunctionCallRva(0x5D1ED5, &CBattle::   NakedAS8DDispatcher),
        FunctionCallRva(0x56F7C7, &CBattle::   NakedGetChrIdForSCraft),
        FunctionCallRva(0x5E027B, &CBattle::   NakedGetTurnVoiceChrId),
        FunctionCallRva(0x5E1015, &CBattle::   NakedGetRunawayVoiceChrId),
        FunctionCallRva(0x5E0CA3, &CBattle::   NakedGetReplySupportVoiceChrId),
        FunctionCallRva(0x5E09E0, &CBattle::   NakedGetTeamRushVoiceChrId),
        FunctionCallRva(0x5DFA1B, &CBattle::   NakedGetUnderAttackVoiceChrId),
        FunctionCallRva(0x5E081E, &CBattle::   NakedGetUnderAttackVoiceChrId2),
        FunctionCallRva(0x5E062B, &CBattle::   NakedGetSBreakVoiceChrId),
        FunctionCallRva(0x5A3644, &CBattle::   NakedCopyMagicAndCraftData),
        FunctionCallRva(0x5A3814, &CBattle::   NakedOverWriteBattleStatusWithChrStatus),
        FunctionCallRva(0x578368, &CBattle::   NakedIsChrStatusNeedRefresh),
        FunctionCallRva(0x622C83, &EDAO::      NakedGetChrSBreak),
        FunctionJumpRva(0x277776, &CGlobal::   GetMagicData,                    &CGlobal::StubGetMagicData),
        FunctionJumpRva(0x274E18, &CGlobal::   GetMagicQueryTable,              &CGlobal::StubGetMagicQueryTable),
        FunctionJumpRva(0x2767E0, &CGlobal::   GetMagicDescription,             &CGlobal::StubGetMagicDescription),
        FunctionCallRva(0x332B26, &EDAO::      GetStatusIcon),
        FunctionCallRva(0x2F82B8, &EDAO::      GetLeaderChangeVoice),
        FunctionCallRva(0x4A7487, &CSSaveData::GetTeamAttackMemberId),
        FunctionCallRva(0x4A74A7, &CSSaveData::GetTeamAttackMemberId),
        FunctionCallRva(0x5EB9E7, &CGlobal::   FixWeaponShapeAndRange,          &CGlobal::StubFixWeaponShapeAndRange),  // weapon shape
        FunctionCallRva(0x5EC037, &CGlobal::   FixWeaponShapeAndRange),                                                 // weapon RNG
        FunctionCallRva(0x5AF055, &CBattle::   NakedFindReplaceChr),
        FunctionCallRva(0x58B258, &CBattle::   NakedCheckCraftTargetBits),
        FunctionJumpRva(0x27A2A0, &CBattle::   GetConditionIconPosByIndex),
        FunctionJumpRva(0x27AF52, &CBattle::   IsTargetCraftReflect,            &CBattle::StubIsTargetCraftReflect),
        FunctionJumpRva(0x276EA2, &CBattle::   OnSetChrConditionFlag,           &CBattle::StubOnSetChrConditionFlag),
        FunctionCallRva(0x5AA2FF, &CBattle::   NakedUpdateCraftReflectLeftTime),


        // avatar

        FunctionJumpRva(0x273469, &CBattle::FindEmptyPosition),
        //FunctionJumpRva(0x276C81, &CBattle::IsAvatarLoaded),
        MemoryPatchRva((ULONG64)0x9B2AE2, 4, 0x5B2EC0),


        // inherit custom flags

        FunctionCallRva(0x358457, &CScript::NakedInheritSaveData),


        // enemy sbreak

        FunctionCallRva(0x56526F, &CBattle::NakedGetBattleState),
        FunctionJumpRva(0x599100, &CBattle::SetCurrentActionChrInfo, &CBattle::StubSetCurrentActionChrInfo),
        FunctionCallRva(0x591C3A, &CBattle::NakedEnemyThinkAction),


        // monster info box

        FunctionCallRva(0x626AEA, &CBattleInfoBox::SetMonsterInfoBoxSize),
        FunctionJumpRva(0x27AC8C, &CBattleInfoBox::DrawMonsterStatus, &CBattleInfoBox::StubDrawMonsterStatus),


        // acgn

        FunctionJumpRva(0x275EFD, &CBattle::LoadMSFile, &CBattle::StubLoadMSFile),  //it3
        FunctionJumpRva(0x5D3545, &CBattle::NakedAS_8D_5F),                         //Ê±¿Õ´ó±À»µ


        //FunctionJumpRva(0x275755, &EDAO::Fade, &EDAO::StubFade),
        //FunctionCallRva(0x601122, FadeInRate),

#endif // DEBUG_DISABLE_PATCH

    };

    PatchMemory(p, countof(p), GetExeModuleHandle());

#if D3D9_VER

    Ldr::LoadDll(L"ed_ao_ex.dll");

#else

    Turbo = TRUE;

#endif

    return TRUE;
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    //PrintConsoleW(L"%d", FIELD_OFFSET(MONSTER_STATUS, SummonCount));

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
