#pragma comment(linker,"/ENTRY:DllMain")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#pragma comment(lib, "d3d8.lib")

#include "ed63.h"
#include "my_commsrc.h"

#define CONSOLE_DEBUG 1

PBYTE   pbCurrentChar = (PBYTE)0x5B1758;
PBYTE   pbCurMagicSN = (PBYTE)0x2725454;
BOOL    g_bPatchFileModified, g_bForceHookIAT;
ULONG   g_PathLength, g_Count, g_AvatarIndex;
HANDLE  g_hHeap;
HMODULE hModuleD3D8;
WCHAR   g_szExePath[MAX_PATH];
CRITICAL_SECTION g_cs;
CUSTOM_BATTLE_INFO* CED6Battle::m_pBattleInfo = NULL;

FReadFileToBuffer pfReadFileToBuffer = (FReadFileToBuffer)0x4870D0;

OVERLOAD_CPP_METHOD_NEW_WITH_HEAP(g_hHeap)

INT WINAPI MylstrcmpiA(LPCSTR lpString1, LPCSTR lpString2)
{
    return StrICompareA(lpString1, lpString2);
}

BOOL WINAPI MyPeekMessageA(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg)
{
    BOOL Result = PeekMessageA(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax, wRemoveMsg);

    if (Result == FALSE)
    {
        ULONG TickCount;
        static ULONG LastTickCount;

        TickCount = GetTickCount();
        if (TickCount - LastTickCount < 10 && --g_Count == 0)
        {
            g_Count = 4;
            SleepEx(1, FALSE);
        }
        LastTickCount = TickCount;
    }

    return Result;
}

HGLOBAL WINAPI MyGlobalAlloc(UINT uFlags, SIZE_T dwBytes)
{
    if (dwBytes == OLD_CHIP_BUF_SIZE)
        dwBytes = NEW_CHIP_BUF_SIZE;

    return GlobalAlloc(uFlags, dwBytes);
}

BOOL CDECL ShowGameWindow(BOOL bShow)
{
    HWND hWnd = *(HWND *)0x2DE92D0;

    if (!bShow)
    {
        SetWindowLongW(hWnd, GWL_STYLE, WS_VISIBLE|WS_POPUP);
        return TRUE;
    }

    INT32 x, y, w, h;
    RECT  rcWorkArea, rcGame = {0, 0, *(PINT32)0x5B8644, *(PINT32)0x5B8648};

    SetWindowLongW(hWnd, GWL_STYLE, WS_POPUP|WS_CAPTION|WS_SYSMENU|WS_GROUP);
    AdjustWindowRectEx(&rcGame, GetWindowLongW(hWnd, GWL_STYLE), FALSE, GetWindowLongW(hWnd, GWL_EXSTYLE));

    SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcWorkArea, 0);
    w = rcGame.right - rcGame.left;
    h = rcGame.bottom - rcGame.top;
    x = ((rcWorkArea.right - rcWorkArea.left) - w) >> 1;
    y = ((rcWorkArea.bottom - rcWorkArea.top) - h) >> 1;
    SetWindowPos(hWnd, HWND_TOP, x, y, w, h, SWP_SHOWWINDOW);

    return TRUE;
}

ED6_DIR_HEADER* OpenPatchDir()
{
    WCHAR  szFile[MAX_PATH];
    ULONG  FileSize;
    HANDLE hFile;

    static ULONG           DirBufferSize;
    static ED6_DIR_HEADER *pDirInfo;

    EnterCriticalSection(&g_cs);

    if (!_InterlockedCompareExchange((PLONG)&g_bPatchFileModified, FALSE, TRUE))
    {
        LeaveCriticalSection(&g_cs);
        return pDirInfo;
    }

    lstrcpyW(szFile, g_szExePath);
    lstrcpyW(szFile + g_PathLength, PATCH_DIR_NAME);
    hFile = CreateFileW(
                szFile,
                GENERIC_READ,
                FILE_SHARE_VALID_FLAGS,
                NULL,
                OPEN_EXISTING,
                FILE_ATTRIBUTE_NORMAL,
                NULL);

    if (hFile == INVALID_HANDLE_VALUE)
    {
        LeaveCriticalSection(&g_cs);
        return NULL;
    }

    LOOP_ONCE
    {
        FileSize = GetFileSize(hFile, NULL);
        if (FileSize < sizeof(ED6_DIR_HEADER))
            break;

        if (pDirInfo == NULL)
        {
            pDirInfo = (ED6_DIR_HEADER *)HeapAlloc(g_hHeap, 0, FileSize);
            if (pDirInfo == NULL)
                break;

            DirBufferSize = FileSize;
        }
        else if (DirBufferSize < FileSize)
        {
            ED6_DIR_HEADER *pDir;

            pDir = (ED6_DIR_HEADER *)HeapReAlloc(g_hHeap, 0, pDirInfo, FileSize);
            if (pDir == NULL)
                break;

            DirBufferSize = FileSize;
        }

        ReadFile(hFile, pDirInfo, FileSize, &pDirInfo->EntrySize, NULL);
    }

    CloseHandle(hFile);

    LeaveCriticalSection(&g_cs);
    return pDirInfo;
}

ED6_DIR_ENTRY* FindFileInPatch(LPCSTR lpFileName, ED6_DIR_HEADER *pDirInfo)
{
    ED6_DIR_ENTRY *pEntry, *pEntryEnd;

    if (lpFileName == NULL || pDirInfo == NULL)
        return NULL;

#if CONSOLE_DEBUG
    PrintConsoleW(L"%S\n", lpFileName);
#endif

    pEntry    = pDirInfo->Entry;
    pEntryEnd = (ED6_DIR_ENTRY *)((ULONG_PTR)pDirInfo + pDirInfo->EntrySize);
    while (pEntry < pEntryEnd)
    {
        if (!StrNICompareA(lpFileName, pEntry->FileName, sizeof(pEntry->FileName)))
            return pEntry;

        ++pEntry;
    }

    return NULL;
}

ULONG ReadFileToBuffer(PBYTE pbBuffer, ED6_DIR_ENTRY *pEntry)
{
    WCHAR   szFile[MAX_PATH];
    HANDLE  hFile;
    ULONG   BytesRead;

    if (pEntry->Size == 0)
        return 0;

    if (pEntry->Size > MAX_BUFFER_SIZE)
    {
        wsprintfW(szFile, L"\"%S\"太大, 已超过缓冲区大小(%d字节).", pEntry->FileName, MAX_BUFFER_SIZE);
        MessageBoxW(*(HWND *)0x2DE92D0, szFile, 0, 0x40);
        return 0;
    }

    lstrcpyW(szFile, g_szExePath);
    lstrcpyW(szFile + g_PathLength, L"Patch.dat");
    hFile = CreateFileW(szFile,
                    GENERIC_READ,
                    FILE_SHARE_READ,
                    NULL,
                    OPEN_EXISTING,
                    FILE_ATTRIBUTE_NORMAL,
                    NULL);
    if (hFile == INVALID_HANDLE_VALUE)
        return 0;

    if (SetFilePointer(hFile, pEntry->Offset, NULL, FILE_BEGIN) == -1 && GetLastError() != NO_ERROR)
    {
        CloseHandle(hFile);
        return 0;
    }

    ReadFile(hFile, pbBuffer, pEntry->Size, &BytesRead, NULL);
    CloseHandle(hFile);

    return BytesRead;
}

ASM ULONG CDECL OldLoadFileByIndex(PBYTE pbBuffer, ULONG FileIndex)
{
    UNREFERENCED_PARAMETER(pbBuffer);
    UNREFERENCED_PARAMETER(FileIndex);
    ASM_DUMMY_AUTO();
}

ULONG CDECL LoadFileByIndex(PBYTE pbBuffer, ULONG FileIndex)
{
    ULONG           DatIndex;
    ED6_DIR_ENTRY  *pEntry;
    ED6_DIR_HEADER *pDirInfo;

    LOOP_ONCE
    {
        if (FileIndex == 0)
            return 0;

        DatIndex  = HIWORD(FileIndex);
        pEntry = *((ED6_DIR_ENTRY **)0x2CA9538 + DatIndex);
        if (pEntry == NULL)
            break;

        pEntry += LOWORD(FileIndex);
        pDirInfo = OpenPatchDir();
        if (pDirInfo == NULL)
            break;

        pEntry = FindFileInPatch(pEntry->FileName, pDirInfo);
        if (pEntry != NULL && pEntry->Size != 0)
            return ReadFileToBuffer(pbBuffer, pEntry);
    }

    return OldLoadFileByIndex(pbBuffer, FileIndex);
}

ASM ULONG CDECL OldLoadFileByName(PBYTE pbBuffer, ULONG DatIndex, LPCSTR pszFileName)
{
    UNREFERENCED_PARAMETER(pbBuffer);
    UNREFERENCED_PARAMETER(DatIndex);
    UNREFERENCED_PARAMETER(pszFileName);
    ASM_DUMMY_AUTO();
}

ULONG CDECL LoadFileByName(PBYTE pbBuffer, ULONG DatIndex, LPCSTR pszFileName)
{
    CHAR            szFileName[0x10];
    ULONG           Length, ExtLength;
    LPCSTR          pszExtension;
    ED6_DIR_ENTRY  *pEntry;
    ED6_DIR_HEADER *pDirInfo;

    if (pszFileName == NULL || *pszFileName == 0)
        return 0;

    LOOP_ONCE
    {
        pDirInfo = OpenPatchDir();
        if (pDirInfo == NULL)
            break;

        pszExtension = findexta(pszFileName);
        Length = pszExtension - pszFileName;
        if (Length > 8)
            break;

        ExtLength = StrLengthA(pszExtension);
        if (ExtLength > 4)
            break;

        FillMemory(szFileName, sizeof(szFileName), ' ');
        CopyMemory(szFileName, pszFileName, Length);
        CopyMemory(szFileName + 8, pszExtension, ExtLength + 1);

        pEntry = FindFileInPatch(szFileName, pDirInfo);
        if (pEntry != NULL && pEntry->Size != 0)
            return ReadFileToBuffer(pbBuffer, pEntry);
    }

    return OldLoadFileByName(pbBuffer, DatIndex, pszFileName);
}

VOID CenterWindow()
{
    int  x, y;
    RECT rcGame, rcSys;
    HWND hWnd = *(HWND *)0x2DE92D0;

    if (hWnd == NULL)
        return;

    SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcSys, 0);
    GetWindowRect(hWnd, &rcGame);
    x = ((rcSys.right - rcSys.left) - (rcGame.right - rcGame.left)) >> 1;
    y = ((rcSys.bottom - rcSys.top) - (rcGame.bottom - rcGame.top)) >> 1;
    SetWindowPos(hWnd, HWND_TOP, x, y, 0, 0, SWP_NOSIZE);
}

VOID WatchPatchFile()
{
    HANDLE hDirectory;
    ULONG  nBytesReturned;
    ULONG  dwNotifyFilter = FILE_NOTIFY_CHANGE_LAST_WRITE;

    hDirectory = CreateFileW(g_szExePath,
                    FILE_LIST_DIRECTORY,
                    FILE_SHARE_READ,
                    NULL,
                    OPEN_EXISTING,
                    FILE_FLAG_BACKUP_SEMANTICS|FILE_FLAG_OVERLAPPED,
                    NULL);
    if (hDirectory == INVALID_HANDLE_VALUE)
        return;

    LOOP_ALWAYS
    {
        BOOL  bSucceed;
        WCHAR Notify[MAX_PATH + sizeof(FILE_NOTIFY_INFORMATION)];
        FILE_NOTIFY_INFORMATION *pFileNotifyInfo = (PFILE_NOTIFY_INFORMATION)Notify;

        SleepEx(100, FALSE);

        ZeroMemory(Notify, sizeof(Notify));
        bSucceed = ReadDirectoryChangesW(hDirectory,
                        Notify,
                        sizeof(Notify),
                        FALSE,
                        dwNotifyFilter,
                        &nBytesReturned,
                        NULL,
                        NULL);
        if (!bSucceed || pFileNotifyInfo->Action != FILE_ACTION_MODIFIED)
            continue;

        pFileNotifyInfo->FileName[pFileNotifyInfo->FileNameLength] = 0;
        if (StrICompareW(pFileNotifyInfo->FileName, PATCH_DIR_NAME) &&
            StrICompareW(pFileNotifyInfo->FileName, PATCH_DAT_NAME))
            continue;

//        EnterCriticalSection(&g_cs);
        _InterlockedExchange((PLONG)&g_bPatchFileModified, TRUE);
//        OpenPatchDir();
//        LeaveCriticalSection(&g_cs);
    }

//    CloseHandle(hDirectory);
}

ULONG WINAPI PatchTName(PVOID lParam)
{
    WCHAR szKey[0x20], szConfig[MAX_PATH];
    ULONG dwVal, dwCharID, dwMaxCharID, dwCount = (ULONG)lParam;
    PBYTE pbTName, pbChar;

    do
    {
        SleepEx(500, FALSE);
        pbTName = **(PBYTE **)0x4A1912;
    } while (pbTName == NULL);

//    SetExecuteDirectoryAsCurrentW();
    lstrcpyW(szConfig, g_szExePath);
    lstrcpyW(szConfig + g_PathLength, CONFIG_FILE_NAME);

    SleepEx(1000, FALSE);
    dwMaxCharID = *(LPWORD)(pbTName + 2) / 2;
    for (ULONG i = 0; i != dwCount; ++i)
    {
        wsprintfW(szKey, L"CharID_%d", i);
        dwCharID = GetPrivateProfileIntW(CONFIG_SECTION_NAME, szKey, dwMaxCharID + 1, szConfig);
        if (dwCharID > dwMaxCharID)
            continue;

        pbChar = pbTName + *(LPWORD)(pbTName + 2 + dwCharID * 2);
        for (ULONG j = 0; j != 5; ++j)
        {
            static WCHAR *szKeyPrefix[] =
            {
                L"WalkCH_%d",
                L"WalkCP_%d",
                L"RunCH_%d",
                L"RunCP_%d",
                L"MSIndex_%d",
            };

            wsprintfW(szKey, szKeyPrefix[j], i);
            pbChar += 4;
            dwVal = GetPrivateProfileIntW(CONFIG_SECTION_NAME, szKey, *(LPDWORD)pbChar, szConfig);
            *(LPDWORD)pbChar = dwVal;
        }
    }

    WatchPatchFile();

    return 0;
}

ASM VOID SafeGetSize()
{
    __asm
    {
        mov  esi, edx;
        test edx, edx;
        je   NULL_DIR_POINT;
        mov  esi, dword ptr [edx+ecx*4+10h];
NULL_DIR_POINT:
        lea  ecx, dword ptr [edx+ecx*4];
        ret;
    }
}

// T_STATUS
ASM VOID CopyStatusData()
{
    __asm
    {
        mov    esi, pwTrueCharID;
//        cmp    word ptr [esi+edx*2], DEST_CHAR_ID;
//        je     SPEC_CHAR;
//        cmp    word ptr [esi+edx*2], 23h;
//        je     SPEC_CHAR;
        cmp    word ptr [esi+edx*2], 20h;
        jnb    SPEC_CHAR;
        movzx    esi, word ptr [ecx+edx*2];
        jmp    end;

SPEC_CHAR:
        mov    esi, 0F1CEh;

end:
        lea    edx, dword ptr [eax+eax*4-0Fh];
        add    ecx, esi;
        pop    esi;
        lea    eax, dword ptr [eax+edx*2-3];
        lea    eax, dword ptr [ecx+eax*2];
        ret;
    }
}

PBYTE CDECL GetStatusData(ULONG dwCharID, ULONG CharLevel)
{
    ULONG FileSize;
    PBYTE pbData;
    ED6_DIR_HEADER *pDirInfo;
    ED6_DIR_ENTRY  *pEntry;
    FDecompress pfDecompress = (FDecompress)0x48AD20;

    if (dwCharID > 0x12)
        return NULL;

    LOOP_ONCE
    {
        PBYTE pbSrc, pbDest, pbTemp;

        if (*(LPWORD)(pwTrueCharID + dwCharID * 2) < 0x20)
            break;

        pDirInfo = OpenPatchDir();
        if (pDirInfo == NULL)
            break;

        pEntry = FindFileInPatch("ZTSTATUS._DT", pDirInfo);
        if (pEntry == NULL)
            break;

        if (pEntry->Size == 0)
            break;

        pbSrc = (PBYTE)HeapAlloc(g_hHeap, 0, pEntry->Size);
        if (pbSrc == NULL)
            break;

        FileSize = ReadFileToBuffer(pbSrc, pEntry);
        if (FileSize == 0)
            break;

        pbData = *(PBYTE *)0x2DE8D54;

        pbDest = pbData;
        pbTemp = pbSrc;
        FileSize = pfDecompress(&pbDest, &pbTemp);
        HeapFree(g_hHeap, 0, pbSrc);

        if (FileSize > 0xF1CE)
            return pbData + 0xF1CE + ((CharLevel > 139 ? 139 : CharLevel) - 3) * 0x16;
    }

    CharLevel = CharLevel > 150 ? 150 : CharLevel < 3 ? 3 : CharLevel;
    pbData = *(PBYTE *)0x2DE9354;
    pbData = pbData + *(LPWORD)(pbData + dwCharID * 2) + (CharLevel - 3) * 0x16;
    return pbData;
}
/*
ASM VOID CheckCharID()
{
    __asm
    {
        mov     ecx, dword ptr [esp+108h];
        movzx   eax, word ptr [ecx+0Ah];
        cmp     eax, 12h;
        jbe     BELOW;
NO_SPEC:
        mov     eax, dwOrigProc;
        jmp     eax;
BELOW:
        mov     ecx, pwTrueCharID;
        cmp     word ptr [ecx+eax*2], DEST_CHAR_ID;
        jnz     NO_SPEC;
        mov     eax, 437B9Fh;
        jmp     eax;
    }
}
*/

// hook after equipment, orb, skip magic, craft, scraft
ASM VOID PreventCopyCharData()
{
    __asm
    {
        mov    eax, pwTrueCharID;
//        cmp    word ptr [eax+ebx*2], DEST_CHAR_ID;
        cmp    word ptr [eax+ebx*2], 20h;
        jnb    SPEC_CHAR;
//        cmp    word ptr [eax+ebx*2], 23h;
//        je     SPEC_CHAR;
        lea    eax, dword ptr [ebp+58Bh];
        inc    [esp];
        ret;

SPEC_CHAR:
        mov    dword ptr [esp], 41D29Dh;
        ret;
    }
}

ULONG dwBFaceIndex[] = {0x300026, 0, 0, 0x300009};

#if 0
ASM void UseCustomBFace()
{
    __asm
    {
        xchg [esp], ebp;
        push ebp;
        mov    ebp, [esp+4];
        mov    eax, pwTrueCharID;
        cmp    word ptr [eax+edx*2], DEST_CHAR_ID;
        je     SPEC_CHAR_KA;
        cmp    word ptr [eax+edx*2], 23h;
        je     SPEC_CHAR_LOWE;
        mov    eax, dword ptr [esp+edx*4+30h];
        ret;
/*
SPEC_CHAR:
        push edx;
        mov    dx, word ptr [eax+edx*2];
        lea    eax, dwBFaceIndex;
        mov    eax, [eax+edx*4-20h*4];
        pop    edx;
        ret;
*/
SPEC_CHAR_LOWE:
        mov    eax, 300009h;
        ret;
SPEC_CHAR_KA:
        mov    eax, 300026h;
        ret;

    }
}
#endif

ASM VOID UseCustomBFace(PBYTE pbBuffer, ULONG dwBFaceIndex, ULONG)
{
    UNREFERENCED_PARAMETER(pbBuffer);
    UNREFERENCED_PARAMETER(dwBFaceIndex);
    __asm
    {
        movzx eax, word ptr [ebx];
        cmp   eax, 12h;
        ja    END;
        cmp   word ptr [eax*2+pwTrueCharID], DEST_CHAR_ID;
        jnz   END;
        mov   dword ptr [esp+8], 300026h;
END:
        push ED6_LOAD_FILE;
        ret;
    }
}

PBYTE CDECL GetSkillData(ULONG SkillID)
{
    PBYTE pbTMagic;
    PBYTE pbCharSkillData;

    if (SkillID < 0x3E8)
    {
        pbTMagic = (PBYTE)*(LPDWORD)0x2DE9338;
        return pbTMagic + *(WORD *)(pbTMagic + SkillID * 2);
    }

    pbCharSkillData = (PBYTE)0x66E640 + *pbCurrentChar * LENGTH_OF_CHAR_DATA;
    return pbCharSkillData + (SkillID - 0x3E8) * 0x20 + 0xE78;
}

PBYTE CDECL MagicQueryTable(ULONG dwSkillID)
{
    PBYTE pbTMagic = (PBYTE)*(LPDWORD)0x2DE9378;

    if (dwSkillID < 0x3E8)
    {
        return pbTMagic + *(WORD *)(pbTMagic + dwSkillID * 2);
    }

//    static const WORD b[] = {0, -1, -1, -1, -1, -1, -1, -1};    return (PBYTE)b;
    return (PBYTE)0x66E630;
}

PBYTE CDECL GetMagicDescription(ULONG dwSkillID)
{
    if (dwSkillID < 0x3E8)
    {
        return ((FGetMagicDescription)0x49F500)(dwSkillID);
    }

    PBYTE pbCharSkillData;

    pbCharSkillData = (PBYTE)0x66E640 + *pbCurrentChar * LENGTH_OF_CHAR_DATA + 0x1078;
    return pbCharSkillData + (dwSkillID - 0x3E8) * 0x120;
}

ASM VOID FixMagicAsEffectIndex2()
{
    INLINE_ASM
    {
        movzx   eax, word ptr [esp + 18h];
        cmp     eax, 5;
        jnz     NORMAL_MAGIC;

        movzx   eax, [ebp]ED6_MONSTER_STATUS_DATA.CurrentCraftIndex;
        lea     eax, [eax * 8];
        lea     eax, [eax + eax * 2];
        lea     eax, [eax + ebp]ED6_MONSTER_STATUS_DATA.MagicAI + 5;
        movzx   eax, [eax];

        lea     edx, [edi + 4E20h];
        lea     ebx, [ebx + 60h];
        mov     [edx]ED6_AS_CRAFT_INFO.pbAsBase, ebx;
        movzx   edx, word ptr [ebx];
        lea     edx, [edx + eax * 2];
        lea     edx, [edx + ebx];
        movzx   edx, word ptr [edx];
        lea     edx, [edx + ebx];
        lea     ebx, [ebx - 60h];

NORMAL_MAGIC:
        mov     dword ptr [edi+4E20h], edx

        ret;
    }
}

ASM VOID FixMagicAsEffectIndex()
{
    INLINE_ASM
    {
        and  eax, 0xFFFF;
        cmp  eax, 5;
        jnz  NORMAL_MAGIC;

        movzx   eax, [edx]ED6_MONSTER_STATUS_DATA.CurrentCraftIndex;
        lea     eax, [eax * 8];
        lea     eax, [eax + eax * 2];
        lea     eax, [eax + edx]ED6_MONSTER_STATUS_DATA.MagicAI + 5;
        movzx   eax, [eax];

NORMAL_MAGIC:

        ret;
    }
}

BOOL FASTCALL LoadStatusData(PVOID pThis, PVOID, ULONG MsFileIndex, BYTE CharPosition)
{
    BYTE CurrentChar;
    typedef BOOL (FASTCALL *FLoadStatusData)(PVOID pThis, PVOID, ULONG MsFileIndex, BYTE CharPosition);
    FLoadStatusData pfLoadStatusData = (FLoadStatusData)ED6_LOAD_MONSTER_STATUS_FILE;

    CurrentChar = *pbCurrentChar;
    if (CurrentChar < 8)
        MsFileIndex = 0x300027;

    return pfLoadStatusData(pThis, 0, MsFileIndex, CharPosition);
}

ASM VOID SetEnemyFlag()
{
    __asm
    {
        add    [esp], 2;
        push eax;
        mov    eax, pbCurrentChar;
        cmp    byte ptr [eax], 8;
        mov    eax, 66E643h;
        jl     NOT_ENEMY;
        or     byte ptr [ebp+eax], 10h;
        jmp    end;

NOT_ENEMY:
        or     byte ptr [ebp+eax], 40h;
        add    eax, 53Dh;
        mov    byte ptr [ebp+eax], 0Fh;
        mov    byte ptr [ebp+eax+0Ch], 0FFh;
end:
        pop    eax;
        ret;
    }
}

ASM VOID UseGuard()
{
    __asm
    {
        mov    esi, pbCurrentChar;
        cmp    byte ptr [esi], 8;
        jl     NOT_ENEMY;
        cmp    dword ptr [esp+14h], 6;
        ret;

NOT_ENEMY:
        cmp eax, esp;
        ret;
    }
}

ASM VOID ForceATDelay()
{
    __asm
    {
        push        0FF888888h;
        push        005AEB58h;
        push        esi;
        mov         eax, FUNC_SHOW_CONDITIONMSG
        call        eax;
        lea         esi, dword ptr [esi+540h];
        mov         edx, dword ptr [esp+3C0h];
        movzx       ecx, word ptr [edx];
        mov         edx, dword ptr [esi];
        add         edx, ecx;
        cmp         edx, 270Fh;
        jbe         UP;
        mov         edx, 270Fh;
UP:
        mov         dword ptr [esi], edx;
        mov         al, 1;
        add         esp, 0Ch;
        pop         edi;
        pop         esi;
        pop         ebp;
        pop         ebx;
        add         esp, 394h;
        ret         10h;
    }
}

ASM VOID IsATDelay()
{
    __asm
    {
        cmp al, 62h;
        je    END;
        mov al, byte ptr [eax + 7h];
        cmp al, 7h;
        je    END;
        cmp al, 62h;
END:
        ret;
    }
}

ULONG ScraftNum;

ASM VOID FixSCraft()
{
    INLINE_ASM
    {
        test   eax, eax;
        jnz    NO_FIRST;
        mov    ScraftNum, edi;

NO_FIRST:

        mov    ebx, dword ptr [esp+24h];
        cmp    byte ptr [ebx], 7;
        jnz    NO_SCRAFT;
        lea    ecx, dword ptr [eax+0Ah];
        mov    ebx, ScraftNum;
        mov    byte ptr [2725520h+ebx], cl;
        inc    ScraftNum;

NO_SCRAFT:

        inc    edi;
        inc    eax;
        add    edx, 18h;
        ret;
    }
}

ASM VOID GetSBreak()
{
    __asm
    {
        push    40CBC0h;
        cmp     dword ptr [pwTrueCharID+eax*2], 20h;
        jnb     SPEC_CHAR;
        ret;
SPEC_CHAR:
        push    esi;
        push    ecx;
        xor     esi, esi;
        xor     ecx, ecx;
        lea     edx, dword ptr [edi+0DFEh];

GET_SCRAFT:
        cmp     word ptr [edx], 0;
        je      END;
        mov     ecx, dword ptr [edx-2];
        inc     esi;
        add     edx, 18h;
        cmp     esi, 5;
        jb      GET_SCRAFT;

END:

        mov     byte ptr [edi+0E73h], ch;
        shr     ecx, 16;
        mov     word ptr [edi+18Ah], cx;
        pop     ecx;
        pop     esi;
        ret;
    }
}

BYTE g_EnemyLastBattleMenuPos[8];

ASM VOID SetLastBattleMenuPosition()
{
    INLINE_ASM
    {
        cmp     ecx, 8;
        jb      NOT_EXCEEDED_BOUND;
        lea     ecx, [ecx - 8];
        and     ecx, 0Fh;
        mov     [g_EnemyLastBattleMenuPos + ecx], al;
        ret;

NOT_EXCEEDED_BOUND:
        mov     dword ptr [esi + ecx * 4 + 0x928], eax;
        ret;
    }
}

ASM VOID GetLastBattleMenuPosition()
{
    INLINE_ASM
    {
        cmp     eax, 8;
        jb      NOT_EXCEEDED_BOUND;
        lea     eax, [eax - 8];
        and     eax, 0Fh;
        movzx   eax, [g_EnemyLastBattleMenuPos + eax];
        ret;

NOT_EXCEEDED_BOUND:

        mov     eax, dword ptr [esi + eax * 4 + 0x928];
        ret;
    }
}

ASM VOID OldMagic134Status1Handler()
{
    ASM_DUMMY_AUTO();
}

ASM VOID Magic134Status1Handler()
{
    INLINE_ASM
    {
        push 01F4h;
        push 9;
        mov  ecx, esi;
        mov  eax, FUNC_SET_ANGLE;
        call eax;
        jmp  OldMagic134Status1Handler;
    }
}

ASM VOID OldMagic05Status1Handler()
{
    ASM_DUMMY_AUTO();
}

ASM VOID Magic05Status1Handler()
{
    INLINE_ASM
    {
        push 01F4h;
        push 9;
        mov  ecx, esi;
        mov  eax, FUNC_SET_ANGLE;
        call eax;
        jmp  OldMagic05Status1Handler;
    }
}

ULONG FASTCALL OldFindEmptyPosition2(CED6Battle *pBattleInfo)
{
    UNREFERENCED_PARAMETER(pBattleInfo);
    ASM_DUMMY_AUTO();
}

ULONG FASTCALL FindEmptyPosition2(CED6Battle *pBattleInfo)
{
    ULONG Index;
    ED6_MONSTER_STATUS_DATA *pMStatus;

    if (g_AvatarIndex != -1)
        return g_AvatarIndex;

    pMStatus = (ED6_MONSTER_STATUS_DATA *)0x66E640;
    Index    =  0;

    if (pBattleInfo != NULL)
    {
        pMStatus += 8;
        Index    += 8;
    }

    do
    {
        if (TEST_BITS(pMStatus->State, 0x80))
            return Index;

        ++pMStatus;
    } while (++Index < 15);

    return -1;
}

ULONG CED6Battle::ForceBeatBack()
{
    ULONG State2;
    ED6_MONSTER_STATUS_DATA *pSelf, *pTarget;

    INLINE_ASM
    {
        mov pSelf,   ebx;
        mov pTarget, esi;
    }

    State2 = pTarget->State2;
    if (m_pBattleInfo->FindCondition(pSelf->CharPosition, EX_CONDITION_GANG_KUI))
        State2 &= ~0x0200;

    return ~State2;
}

CUSTOM_BATTLE_INFO* CED6Battle::AllocBattleInfo()
{
    m_pBattleInfo = new CUSTOM_BATTLE_INFO;
    return m_pBattleInfo;
}

VOID CED6Battle::BattleEntryOutputLog()
{
    ZeroMemory(g_EnemyLastBattleMenuPos, sizeof(g_EnemyLastBattleMenuPos));

    if (m_pBattleInfo == NULL)
        return;

    m_pBattleInfo->Reset();
}

ASM BOOL CED6Battle::OldIsAvatarLoaded(ULONG AvatarIndex)
{
    UNREFERENCED_PARAMETER(AvatarIndex);
    ASM_DUMMY_AUTO();
}

BOOL CED6Battle::IsAvatarLoaded(ULONG AvatarIndex)
{
    return g_AvatarIndex == -1 ? OldIsAvatarLoaded(AvatarIndex) : TRUE;
}

ASM
VOID
THISCALL
CED6Battle::
OldProcessAttack(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget
)
{
    UNREFERENCED_PARAMETER(pSelf);
    UNREFERENCED_PARAMETER(pTarget);
    ASM_DUMMY_AUTO();
}

ULONG g_LastReflectDamage;

VOID
CED6Battle::
ProcessAttack(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget
)
{
    ULONG DamageNormal, DamageGangkui, DamageBlock;
    CUSTOM_CONDITION_INFO *pInfo;
    CUSTOM_ATTRIBUTE_ADDITION AddSelf, AddTarget, SelfBak, TargetBak;

    if (TEST_BITS(pSelf->State, 0x40) && !TEST_BITS(pSelf->State, 0x10) &&
        TEST_BITS(pTarget->State, 0x40) && !TEST_BITS(pTarget->State, 0x10))
    {
        OldProcessAttack(pSelf, pTarget);
        return;
    }

    m_pBattleInfo->GetAttributeAddition(pSelf->CharPosition, &AddSelf);
    m_pBattleInfo->GetAttributeAddition(pTarget->CharPosition, &AddTarget);

    SelfBak   = *(CUSTOM_ATTRIBUTE_ADDITION *)&pSelf->STR;
    TargetBak = *(CUSTOM_ATTRIBUTE_ADDITION *)&pTarget->STR;

    pSelf->DEF   += AddSelf.DEF;
    pSelf->ADF   += AddSelf.ADF;
    pInfo = m_pBattleInfo->FindCondition(pTarget->CharPosition, EX_CONDITION_GANG_KUI);
    if (pInfo == NULL)
    {
        pTarget->DEF += AddTarget.DEF;
        pTarget->ADF += AddTarget.ADF;
        OldProcessAttack(pSelf, pTarget);
        *(CUSTOM_ATTRIBUTE_ADDITION *)&pSelf->STR = SelfBak;
        *(CUSTOM_ATTRIBUTE_ADDITION *)&pTarget->STR = TargetBak;
        return;
    }

    ((FShowConditionMsg)(FUNC_SHOW_CONDITIONMSG))(pTarget, "KUI", RGBA(243, 123, 58, 255));

    pTarget->DEF += AddTarget.DEF;
    pTarget->ADF += AddTarget.ADF;
    DamageNormal = OldGetDamage(pSelf, pTarget, FALSE);

    pTarget->DEF += pInfo->wParam[0];
    pTarget->ADF += pInfo->wParam[1];
    DamageGangkui = OldGetDamage(pSelf, pTarget, FALSE);

    DamageBlock = DamageNormal - DamageGangkui;
//    DamageTargetSelf = OldGetDamage(pTarget, pTarget, FALSE);

    WCHAR Buf[200];
    wsprintfW(Buf, L"Gangkui = %d, Block = %d", DamageGangkui, DamageBlock);
    SetWindowTextW(*(HWND *)0x2DE92D0, Buf);

    if (DamageGangkui != 0)
    {
        pInfo->lParam[1] = GANGKUI_NOT_REFLECT;
        pInfo->lParam[0] = DamageGangkui;
        OldProcessAttack(pSelf, pTarget);
    }

    if (DamageBlock != 0)
    {
        g_LastReflectDamage = DamageBlock;
        pInfo->lParam[1] = GANGKUI_REFLECT;
    }
    else
    {
        pInfo->lParam[1] = GANGKUI_NOT_REFLECT_ONCE;
    }

    *(CUSTOM_ATTRIBUTE_ADDITION *)&pSelf->STR = SelfBak;
    *(CUSTOM_ATTRIBUTE_ADDITION *)&pTarget->STR = TargetBak;
}

// before -> GetDamage -> after

BOOL
CED6Battle::
GetTargetFrontCoordinate(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    FLOAT                   *pRecvCoord OPTIONAL
)
{
    FGetTargetFrontCoordinate pfGetCoord = CastMethodAddress<FGetTargetFrontCoordinate>(0x410900);
    return (this->*pfGetCoord)(pSelf, pTarget, pRecvCoord);
}

ASM
ULONG
CED6Battle::
OldGetDamage(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    BYTE                     Type
)
{
    UNREFERENCED_PARAMETER(pSelf);
    UNREFERENCED_PARAMETER(pTarget);
    UNREFERENCED_PARAMETER(Type);
    ASM_DUMMY_AUTO();
}

ULONG
CED6Battle::
GetDamage(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    BYTE                     Type
)
{
    ULONG Damage;
    CUSTOM_CONDITION_INFO *pInfo;

    if (pSelf == pTarget && g_LastReflectDamage != 0)
    {
        Damage = g_LastReflectDamage;
        g_LastReflectDamage = 0;
        return Damage;
    }

    pInfo = m_pBattleInfo->FindCondition(pTarget->CharPosition, EX_CONDITION_GANG_KUI);
    if (pInfo != NULL && pInfo->lParam[0] != 0)
    {
        Damage = pInfo->lParam[0];
        pInfo->lParam[0] = 0;
        return Damage;
    }

    return OldGetDamage(pSelf, pTarget, Type);
}

ASM bool CED6Battle::OldHasPhysicalReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget)
{
    UNREFERENCED_PARAMETER(pSelf);
    UNREFERENCED_PARAMETER(pTarget);
    ASM_DUMMY_AUTO();
}

ASM bool CED6Battle::OldHasMagicReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget)
{
    UNREFERENCED_PARAMETER(pSelf);
    UNREFERENCED_PARAMETER(pTarget);
    ASM_DUMMY_AUTO();
}

BOOL CED6Battle::HasPhysicalReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget)
{
    CUSTOM_CONDITION_INFO *pInfo;

    LOOP_ONCE
    {
        switch (pSelf->SkillType)
        {
            case SKILL_TYPE_NORMAL_ATTACK:
            case SKILL_TYPE_CRAFT:
            case SKILL_TYPE_SCRAFT:
            case 9:
                break;

            default:
                return OldHasPhysicalReflection(pSelf, pTarget);
        }

        pInfo = m_pBattleInfo->FindCondition(pTarget->CharPosition, EX_CONDITION_GANG_KUI);
        if (pInfo != NULL)
        {
            switch (pInfo->lParam[1])
            {
                case GANGKUI_REFLECT:
                    return TRUE;

                case GANGKUI_NOT_REFLECT_ONCE:
                    pInfo->lParam[1] = GANGKUI_REFLECT;
                    NO_BREAK;

                case GANGKUI_NOT_REFLECT:
                    break;
            }
        }
    }

    return OldHasPhysicalReflection(pSelf, pTarget);
}

BOOL CED6Battle::HasMagicReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget)
{
    CUSTOM_CONDITION_INFO *pInfo;

    LOOP_ONCE
    {
        if (pSelf->SkillType != SKILL_TYPE_MAGIC)
            break;

        pInfo = m_pBattleInfo->FindCondition(pTarget->CharPosition, EX_CONDITION_GANG_KUI);
        if (pInfo != NULL)
        {
            switch (pInfo->lParam[1])
            {
            case GANGKUI_REFLECT:
                return TRUE;

            case GANGKUI_NOT_REFLECT_ONCE:
                pInfo->lParam[1] = GANGKUI_REFLECT;
                NO_BREAK;

            case GANGKUI_NOT_REFLECT:
                break;
            }
        }
    }

    return OldHasMagicReflection(pSelf, pTarget);
}

ASM
VOID
CED6Battle::
OldProcessConditions(
    ED6_MONSTER_STATUS_DATA *pMStatus,
    ULONG                    ActionTime,
    BYTE                     Type,
    ULONG                    ConditionFlag
)
{
    UNREFERENCED_PARAMETER(pMStatus);
    UNREFERENCED_PARAMETER(ActionTime);
    UNREFERENCED_PARAMETER(Type);
    UNREFERENCED_PARAMETER(ConditionFlag);
    ASM_DUMMY_AUTO();
}

VOID
CED6Battle::
ProcessConditions(
    ED6_MONSTER_STATUS_DATA *pMStatus,
    ULONG                    ActionTime,
    BYTE                     Type,
    ULONG                    ConditionFlag
)
{
    enum { TYPE_SUB_AT, TYPE_DEC, TYPE_DEC_SPEC };

    OldProcessConditions(pMStatus, ActionTime, Type, ConditionFlag);
    if (Type != TYPE_SUB_AT)
        return;

    if (pMStatus->CharPosition > countof(m_pBattleInfo->m_MStatus))
        return;

    CUSTOM_MONSTER_STATUS *pCusMS;
    CUSTOM_CONDITION_INFO *pCondition;
    FFinishEffect          pfFinishEffect = (FFinishEffect)FUNC_FINISH_EFFECT;

    ConditionFlag = 1;
    pCusMS = &m_pBattleInfo->m_MStatus[pMStatus->CharPosition];
    for (ULONG Count = EX_CONDITION_NUMBER; Count; ConditionFlag <<= 1, --Count)
    {
        pCondition = m_pBattleInfo->FindCondition(pMStatus->CharPosition, ConditionFlag);
        if (pCondition == NULL)
            continue;

        pCondition->ATLeft -= min(ActionTime, pCondition->ATLeft);
        if (pCondition->ATLeft != 0)
            continue;

        if (TEST_BITS(pCondition->ConditionFlag, EX_CONDITION_GANG_KUI))
        {
            pfFinishEffect(&pMStatus->pPrivateEffectInfo[pCondition->wParam[3]]);
        }

        if (TEST_BITS(pCondition->ConditionFlag, EX_CONDITION_CHAR_SIZE))
        {
            *(PULONG)&pMStatus->CharSize = pCondition->Param[0];
        }

        ZeroMemory(pCondition, sizeof(*pCondition));
        pCusMS->m_ConditionFlags &= ~ConditionFlag;
    }
}

VOID CED6Battle::ExCondition(INSTRUCTION_8D *pInstruction, ED6_MONSTER_STATUS_DATA *pMStatus)
{
    ULONG ExConditionFlag;
    CUSTOM_CONDITION_INFO *pInfo;

    if (pMStatus->CharPosition > countof(m_pBattleInfo->m_MStatus) || m_pBattleInfo == NULL)
        return;

    switch ((ULONG)pInstruction->FunctionID)
    {
        case FUNC_CRAFT_REFLECT:
        case FUNC_ARTS_REFLECT:
        case FUNC_STR_UP:
        case FUNC_STR_DOWN:
        case FUNC_DEF_UP:
        case FUNC_DEF_DOWN:
        case FUNC_SPD_UP:
        case FUNC_SPD_DOWN:
        case FUNC_ADF_UP:
        case FUNC_ADF_DOWN:
        case FUNC_AGL_UP:
        case FUNC_AGL_DOWN:
        case FUNC_ATS_UP:
        case FUNC_ATS_DOWN:
        case FUNC_CHAR_SIZE:
        case FUNC_GANG_KUI:
            break;

        default:
            return;
    }

    ExConditionFlag = 1 << (pInstruction->FunctionID - 1);
    pInfo = m_pBattleInfo->FindCondition(pMStatus->CharPosition, ExConditionFlag);
    if (pInfo == NULL)
    {
        pInfo = m_pBattleInfo->FindCondition(pMStatus->CharPosition, 0);
        if (pInfo == NULL)
            return;
    }

    m_pBattleInfo->m_MStatus[pMStatus->CharPosition].m_ConditionFlags |= ExConditionFlag;

    pInfo->ConditionFlag    = ExConditionFlag;
    pInfo->Param[0]         = pInstruction->Param[0];
    pInfo->Param[1]         = pInstruction->Param[1];
    pInfo->ATLeft           = pInstruction->Param[2];
    pInfo->ByteParam        = pInstruction->ByteParam;

    switch (pInstruction->FunctionID)
    {
        case FUNC_CHAR_SIZE:
            Swap(pInfo->Param[0], *(PULONG)&pMStatus->CharSize);
            pMStatus->CharSize = *(PULONG)&pMStatus->CharSize * .4f;
            break;
    }
}

VOID
CED6Battle::
Putffect(
    CED6Effect             **pEffect,
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    FLOAT                   *pUnknown,
    ED6_MONSTER_STATUS_DATA *pSelf2,
    PULONG                   pUnknownDowrd3,
    FLOAT                   *pScale,
    FLOAT                   *pEffectSize,
    ULONG                    Zero4,
    PVOID                    pvEffectBuffer,
    ULONG                    Zero5,
    ULONG                    Zero6,
    ULONG                    One1,
    ULONG                    Zero7
)
{
    FPutEffect pfPutEffect = (FPutEffect)FUNC_PUT_EFFECT;
    pfPutEffect(
        pEffect,
        pSelf,
        pTarget,
        pUnknown,
        pSelf2,
        pUnknownDowrd3,
        pScale,
        pEffectSize,
        Zero4,
        pvEffectBuffer,
        Zero5,
        Zero6,
        One1,
        Zero7);
}

VOID
CED6Battle::
PutConditionEffect(
    ED6_MONSTER_STATUS_DATA *pTarget,
    ULONG                    PrivateEffectBufferIndex,
    ULONG                    PrivateEffectInfoIndex
)
{
    if (!TEST_BITS(PrivateEffectBufferIndex, 0xFF00))
        return;

    if (PrivateEffectInfoIndex > countof(pTarget->pPrivateEffectInfo))
        return;

    PrivateEffectBufferIndex &= 0xFF;
    if (PrivateEffectBufferIndex > countof(pTarget->pPrivateEffectBuffer))
        return;

    FLOAT Unknown[3] = { -0.f, 1.f, 0.f };
    FLOAT CharSize[3] = { pTarget->CharSize, pTarget->CharSize, pTarget->CharSize };
    FLOAT Unknown2[3] = { };

    Putffect(
        &pTarget->pPrivateEffectInfo[PrivateEffectInfoIndex],
        NULL,
        pTarget,
        Unknown,
        NULL,
        NULL,
        Unknown2,
        CharSize,
        NULL,
        pTarget->pPrivateEffectBuffer[PrivateEffectBufferIndex],
        0,
        0,
        1,
        0
    );
}

VOID
FASTCALL
CED6Battle::
Dispatch8D(
    ULONG                    Instruction8DParam1,
    ED6_AS_CRAFT_INFO       *pCraftInfo,
    ED6_MONSTER_STATUS_DATA *pMStatus
)
{
    INSTRUCTION_8D *pIns;
    const ULONG LengthOfInstruction8D = 1 + 1 + 4 * 4;

    if (Instruction8DParam1 != 0)
        return;

    pIns = (INSTRUCTION_8D *)&pCraftInfo->pbAsBuffer[-LengthOfInstruction8D];

    if (pIns->FunctionID >= FUNC_CONDITION_FIRST && pIns->FunctionID < FUNC_CONDITION_LAST)
    {
        ExCondition(pIns, pMStatus);
    }
    else switch ((ULONG)pIns->FunctionID)
    {
        case FUNC_AVATAR:
            Avatar(pIns, pMStatus);
            break;

        case FUNC_REPLACE_POS:
            ReplacePosition(pIns, pMStatus);
            break;
    }
}

VOID CED6Battle::ReplacePosition(INSTRUCTION_8D *pInstruction, ED6_MONSTER_STATUS_DATA *pMStatus)
{
    ULONG SrcPos, NewPos, X, Y;

    SrcPos = pInstruction->byParam[0];
    NewPos = pInstruction->byParam[1];

    switch (NewPos)
    {
        case POS_SELF:
            X = pMStatus->pControlInfo->X;
            Y = pMStatus->pControlInfo->Y;
            NewPos = MAKELONG(X, Y);
            break;

        case POS_SELFFRONT:
        {
            BOOL  Result;
            FLOAT Coord[3];
            ULONG SkillType, SkillInfoIndex;
            ED6_MS_CRAFT_INFO *pCraftInfo, CraftBak;

            pCraftInfo           = pMStatus->MSCraftInfo;
            CraftBak.Shape       = pCraftInfo->Shape;
            CraftBak.Flags       = pCraftInfo->Flags;
            CraftBak.ShapeRadius = pCraftInfo->ShapeRadius;

            pCraftInfo->Shape       = 1;
            pCraftInfo->Flags       = 0x112;
            pCraftInfo->ShapeRadius = 1;

            SkillInfoIndex = pMStatus->CurrentSkillInfoIndex;
            SkillType = pMStatus->SkillType;

            pMStatus->CurrentSkillInfoIndex = 0x3E8;
            pMStatus->SkillType = SKILL_TYPE_SCRAFT;

            Result = GetTargetFrontCoordinate(pMStatus, pMStatus, Coord);

            pCraftInfo->Shape       = CraftBak.Shape;
            pCraftInfo->Flags       = CraftBak.Flags;
            pCraftInfo->ShapeRadius = CraftBak.ShapeRadius;

            pMStatus->CurrentSkillInfoIndex = SkillInfoIndex;
            pMStatus->SkillType = SkillType;
            if (!Result)
                return;

            X = Coord[0];
            Y = Coord[2];
            NewPos = MAKELONG(X, Y);
            break;
        }

        default:
            return;
    }

    switch (SrcPos)
    {
        case POS_DEST:
            *(PULONG)&pMStatus->SelectedTargetX = NewPos;
            break;

        default:
            return;
    }
}

VOID CED6Battle::Avatar(INSTRUCTION_8D *pInstruction, ED6_MONSTER_STATUS_DATA *pMStatus)
{
    ULONG        MsFileIndex, CharPosition, TargetPos;
    ED6_AI_INFO *pAIInfo;

    FCloneMonsterStatusData2    pfCloneMSData       = CastMethodAddress<FCloneMonsterStatusData2>(FUNC_CLONE_MS_DATA);
    FLoadMonsterStatusData2     pfLoadMSData        = CastMethodAddress<FLoadMonsterStatusData2>(FUNC_LOAD_MS_DATA);
    FResetMSData2               pfResetCtrlData     = CastMethodAddress<FResetMSData2>(FUNC_RESET_CTRL_DATA);
    FResetMSData2               pfResetStatusData   = CastMethodAddress<FResetMSData2>(FUNC_RESET_MS_DATA);

    if (pMStatus->SkillType != SKILL_TYPE_CRAFT)
        return;

    MsFileIndex = pInstruction->Param[0];
    if (MsFileIndex == 0)
        return;

    CharPosition = FindEmptyPosition2(TEST_BITS(pMStatus->State, 0x40) ? NULL : this);
    if (CharPosition == -1)
        return;

    g_AvatarIndex = CharPosition;
    pAIInfo = (ED6_AI_INFO *)&pMStatus->CraftAI[pMStatus->CurrentCraftIndex];

    LOOP_ONCE
    {
        TargetPos = *(PULONG)&pMStatus->SelectedTargetX;
        if (!(this->*pfCloneMSData)(pMStatus, pMStatus->CurrentSkillInfoIndex, pAIInfo))
            break;

        *(PULONG)&pMStatus->SelectedTargetX = TargetPos;

        (this->*pfResetCtrlData)(CharPosition);
        (this->*pfResetStatusData)(CharPosition);
        if (!(this->*pfLoadMSData)(MsFileIndex, CharPosition))
            break;
    }

    g_AvatarIndex = -1;
}

ASM VOID OldDispatch8D()
{
    ASM_DUMMY_AUTO();
}

ASM VOID AsInstruction8D00()
{
    INLINE_ASM
    {
        lea  esp, [esp-0Ch];
        mov  [esp+0], eax;
        mov  [esp+4], ecx;
        mov  [esp+8], edx;

        push [esp + 108h + 0Ch];
        push eax;
        mov  edx, ecx;
        mov  ecx, edi;
        call CED6Battle::Dispatch8D;

        mov  eax, [esp+0];
        mov  ecx, [esp+4];
        mov  edx, [esp+8];
        lea  esp, [esp+0Ch];

        jmp  OldDispatch8D;
    }
}

FARPROC WINAPI MyGetProcAddress(HMODULE hModule, LPCSTR lpProcName)
{
    if ((ULONG_PTR)lpProcName & 0xFFFF0000)
    {
        switch (HashAPI(lpProcName))
        {
            case 0xFFADBAB0: return (FARPROC)MyPeekMessageA;
            case 0x5E207A27: return (FARPROC)MylstrcmpiA;
        }
    }

    return GetProcAddress(hModule, lpProcName);
}

VOID Init()
{
    BOOL  bIsJP3rd;
    ULONG OldProtection;

    if (!VirtualProtectEx(NtCurrentProcess(), (PVOID)0x487200, 4, PAGE_EXECUTE_READ, &OldProtection))
        return;

    bIsJP3rd = *(LPDWORD)0x487200 == 0x08244C8B;
    if (OldProtection != PAGE_EXECUTE_READ)
        VirtualProtectEx(NtCurrentProcess(), (PVOID)0x487200, 4, OldProtection, &OldProtection);

    if (!bIsJP3rd)
        return;

    HMODULE hModule;

    hModule = GetModuleHandleW(NULL);

    MEMORY_PATCH p[] =
    {
        { 0x90,                                 1, 0x03EC80 },      // damage max 99999
        { 0x90,                                 1, 0x03EC89 },      // damage max 99999
	    { 0x90,                                 1, 0x03F2D4 },      // damage max 99999
        { 0x07,                                 1, 0x147CDD },      // Debug Mode
        { (ULONG)ForceATDelay,                  4, 0x0291EC },
        { 0x61,                                 1, 0x027ACE },      // force at delay
        { 0x00,                                 1, 0x003EC6 },      // scraft
        { 0x436AF0,                             4, 0x1AFD68 },      // force use item
        { 0x00,                                 4, 0x0A0C3D },      // CreateWindowEx->Style
        { NEW_CHIP_BUF_SIZE,                    4, 0x01EDB6 },      // memory size
        { NEW_CHIP_BUF_SIZE,                    4, 0x03960A },      // memory size
        { NEW_CHIP_BUF_SIZE,                    4, 0x0888F3 },      // memory size
        { NEW_CHIP_BUF_SIZE,                    4, 0x088A13 },      // memory size
        { NEW_CHIP_BUF_SIZE,                    4, 0x0A0E48 },      // memory size
        { (ULONG)(NEW_CHIP_BUF_SIZE * 0.875),   4, 0x01F006 },      // memory size
        
        { 0x01869FB8,                           4, 0x00743A },      // max number
        { 0x0FC83B00,                           4, 0x00743E },      // max number
        { 0xC08BC84F,                           4, 0x007442 },      // max number
        { 0x0004C2,                             4, 0x009CB0 },      // emergency music

        { (ULONG)MylstrcmpiA,       4, IATLookupRoutineRVAByEntry(hModule, lstrcmpiA)       },
        { (ULONG)MyPeekMessageA,    4, IATLookupRoutineRVAByEntry(hModule, PeekMessageA)    },
//        { (ULONG)MyGlobalAlloc,     4, IATLookupRoutineRVAByEntry(hModule, GlobalAlloc)     },
//        { (ULONG)MyGetProcAddress,  4, IATLookupRoutineRVAByEntry(hModule, pvGetProcAddress)},
    };

    g_bForceHookIAT = p[countof(p) - 1].RVA == IMAGE_INVALID_RVA;

    MEMORY_FUNCTION_PATCH f[] =
    {
        { JUMP, 0x9FA50, GetStatusData                  },
        { CALL, 0x1CC6B, UseCustomBFace                 },
        { CALL, 0x1D20C, PreventCopyCharData,       1   },

        { CALL, 0x3E34F, IsATDelay                      },
        { CALL, 0x087F7, FixSCraft                      },
        { CALL, 0x02CB2, GetSBreak                      },
        { CALL, 0x45036, GetSkillData                   },
        { CALL, 0x4503E, MagicQueryTable                },
        { CALL, 0x451AD, GetMagicDescription            },

        // new
        { CALL, 0x29764, FindEmptyPosition2             },
        { CALL, 0x3A52E, FixMagicAsEffectIndex2,    1   },
        { CALL, 0xA0C62, ShowGameWindow                 },
        { CALL, 0x8721A, SafeGetSize,               2   },

//        { CALL, 0x14173, LoadStatusData             },
//        { CALL, 0x14298, UseGuard                   },
//        { CALL, 0x141A5, SetEnemyFlag             },
//        { CALL, 0x1414B, FindEmptyPosition        },
//        { CALL, 0x3A52E, UseCustomMagicAsEffect,  1 },

        { CALL, 0x499B9, GetLastBattleMenuPosition,         2   },
        { CALL, 0x49A3A, SetLastBattleMenuPosition,         2   },
        { CALL, 0x015C9, GET_METHOD(BattleEntryOutputLog)       },
        { CALL, 0x0E375, GET_METHOD(ForceBeatBack),         1   },  // 0042ABBF

//        { JUMP, 0x27340, Magic05Status1Handler,     0, OldMagic05Status1Handler                     },
        { JUMP, 0x26B69, Magic134Status1Handler,    0, OldMagic134Status1Handler                    },
        { JUMP, 0x36BC7, AsInstruction8D00,         0, OldDispatch8D                                },
        { JUMP, 0x87200, LoadFileByIndex,           0, OldLoadFileByIndex                           },
        { JUMP, 0x874B0, LoadFileByName,            2, OldLoadFileByName                            },

        { JUMP, 0x29D60, GET_METHOD(IsAvatarLoaded),        1, GET_METHOD(OldIsAvatarLoaded)        },
        { JUMP, 0x276B0, GET_METHOD(ProcessAttack),         0, GET_METHOD(OldProcessAttack)         },
        { JUMP, 0x1BE60, GET_METHOD(ProcessConditions),     1, GET_METHOD(OldProcessConditions)     },
        { JUMP, 0x2E0D0, GET_METHOD(HasPhysicalReflection), 0, GET_METHOD(OldHasPhysicalReflection) },
        { JUMP, 0x2E070, GET_METHOD(HasMagicReflection),    0, GET_METHOD(OldHasMagicReflection)    },
        { JUMP, 0x05730, GET_METHOD(GetDamage),             1, GET_METHOD(OldGetDamage)             },
    };

    PatchMemory(p, countof(p), f, countof(f), hModule);

    g_Count              = 4;
    g_AvatarIndex        = -1;
    g_bPatchFileModified = TRUE;
    g_PathLength = GetExecuteDirectoryW(g_szExePath, countof(g_szExePath));

    g_hHeap = HeapCreate(0, 0, 0);

    CED6Battle::AllocBattleInfo();

    ULONG PatchCount;

    lstrcpyW(g_szExePath + g_PathLength, CONFIG_FILE_NAME);
    PatchCount = GetPrivateProfileIntW(CONFIG_SECTION_NAME, L"Count", 0, g_szExePath);
    g_szExePath[g_PathLength] = 0;
    if (PatchCount)
        CreateThread(NULL, 0, PatchTName, (PVOID)PatchCount, 0, NULL);
}

LONG CALLBACK VectoredHandler(PEXCEPTION_POINTERS ExceptionInfo)
{
    WCHAR Buffer[0x400];
    SYSTEMTIME st;

    GetLocalTime(&st);
    swprintf(
        Buffer,
        L"%02d:%02d:%02d: code = %08X, addr = %08X\r\n",
        st.wHour, st.wMinute, st.wSecond,
        ExceptionInfo->ExceptionRecord->ExceptionCode,
        ExceptionInfo->ExceptionRecord->ExceptionAddress);
    MessageBoxW(NULL, Buffer, NULL, 64);

    return EXCEPTION_CONTINUE_SEARCH;
}

BOOL WINAPI DllMain(HINSTANCE hInstance, ULONG Reason, LPVOID lpReserved)
{
    UNREFERENCED_PARAMETER(lpReserved);

    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
//            AddVectoredExceptionHandler(TRUE, VectoredHandler);
            DisableThreadLibraryCalls(hInstance);
            InitializeCriticalSectionAndSpinCount(&g_cs, 4000);
            Init();
            break;

        case DLL_PROCESS_DETACH:
            DeleteCriticalSection(&g_cs);
            break;
    }

    return TRUE;
}

IDirect3D8* WINAPI MyDirect3DCreate8(UINT SDKVersion)
{
    ULONG   Length, Flags;
    WCHAR   szPath[MAX_PATH];
    HMODULE hModule;

    static IDirect3D8* (WINAPI *pfDirect3DCreate8)(UINT SDKVersion);

    if (pfDirect3DCreate8 == NULL)
    {
        if (g_bForceHookIAT)
        {
            hModule = GetModuleHandleW(NULL);

            MEMORY_PATCH p[] =
            {
                { (ULONG)MylstrcmpiA,       4, 0x19D02C },
                { (ULONG)MyPeekMessageA,    4, 0x19D248 },
            };

            PatchMemory(p, countof(p), NULL, 0, hModule);
        }

        Length = GetSystemDirectoryW(szPath, countof(szPath));
        if (Length == 0)
            return NULL;

        lstrcpyW(szPath + Length, L"\\d3d8.dll");

        hModule = LoadLibraryExW(szPath, 0, NULL);
        if (hModule == NULL)
            return NULL;

        Flags = GET_MODULE_HANDLE_EX_FLAG_PIN | GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS;
        GetModuleHandleExW(Flags, (LPWSTR)hModule, &hModule);

        *(FARPROC *)&pfDirect3DCreate8 = GetProcAddress(hModule, "Direct3DCreate8");
        if (pfDirect3DCreate8 == NULL)
            return NULL;

        hModuleD3D8 = hModule;

#if CONSOLE_DEBUG
        AllocConsole();
#endif
    }

    return pfDirect3DCreate8(SDKVersion);
}

VOID WINAPI MyDebugSetMute()
{
    static VOID (WINAPI *pfDebugSetMute)();

    if (pfDebugSetMute == NULL)
    {
        *(FARPROC *)&pfDebugSetMute = GetProcAddress(hModuleD3D8, "DebugSetMute");
        if (pfDebugSetMute == NULL)
            return;
    }

    return pfDebugSetMute();
}

HRESULT WINAPI MyValidatePixelShader(PVOID PixelShader, PVOID Reserved, BOOL b, PVOID toto)
{
    static HRESULT (WINAPI *pfValidatePixelShader)(PVOID, PVOID, BOOL, PVOID);

    if (pfValidatePixelShader == NULL)
    {
        *(FARPROC *)&pfValidatePixelShader = GetProcAddress(hModuleD3D8, "ValidatePixelShader");
        if (pfValidatePixelShader == NULL)
            return E_FAIL;
    }

    return pfValidatePixelShader(PixelShader, Reserved, b, toto);
}

HRESULT
WINAPI
MyValidateVertexShader(
    PVOID VertexShader,
    PVOID Reserved1,
    PVOID Reserved2,
    BOOL  b,
    PVOID toto
)
{
    static
    HRESULT
    (WINAPI
    *pfValidateVertexShader)(
        PVOID,
        PVOID,
        PVOID,
        BOOL,
        PVOID
    );

    if (pfValidateVertexShader == NULL)
    {
        *(FARPROC *)&pfValidateVertexShader = GetProcAddress(hModuleD3D8, "ValidateVertexShader");
        if (pfValidateVertexShader == NULL)
            return E_FAIL;
    }

    return pfValidateVertexShader(VertexShader, Reserved1, Reserved2, b, toto);
}