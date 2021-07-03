#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text /MERGE:.text1=.text /SECTION:.idata,ERW")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")
#pragma comment(lib, "d3d8.lib")

#include "ZWEI2Plus.h"
#include "MyLibrary.cpp"

ML_OVERLOAD_NEW

DWORD dwCount;

BOOL WINAPI MySetWindowPos(HWND hWnd, HWND hWndInsertAfter, int X, int Y, int cx, int cy, UINT uFlags)
{
    RECT rcDesktop;

    SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcDesktop, 0);
    X = ((rcDesktop.right - rcDesktop.left) - cx) >> 1;
    Y = ((rcDesktop.bottom - rcDesktop.top) - cy) >> 1;
    return SetWindowPos(hWnd, hWndInsertAfter, X, Y, cx, cy, uFlags&~SWP_NOMOVE);
}

BOOL WINAPI MyPeekMessageA(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg)
{
    BOOL bResult = PeekMessageA(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax, wRemoveMsg);

    if (bResult == False)
    {
        DWORD dwTickCount;
        static DWORD dwLastTickCount;

        dwTickCount = NtGetTickCount();
        if (dwTickCount - dwLastTickCount < 10 && --dwCount == 0)
        {
            dwCount = 4;
            Ps::Sleep(1);
        }
        dwLastTickCount = dwTickCount;
    }
    else
    {
        switch (lpMsg->message)
        {
            case WM_KEYUP:
                switch (lpMsg->wParam)
                {
                    case 0:
                        break;
                    default:
                        break;
                    break;
                }
        }
    }

    return bResult;
}

HANDLE WINAPI MyCreateFileA(LPSTR lpFileName, DWORD dwDesiredAccess, DWORD dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, DWORD dwCreationDisposition, DWORD dwFlagsAndAttributes, HANDLE hTemplateFile)
{
    CHAR szFileName[MAX_PATH];
    LPSTR lpFile;
    DWORD  dwLength, dwLength2;
    static CHAR szPath[] = "DATA\\S??\\";

    dwLength = StrLengthA(lpFileName);
    lpFile = lpFileName + dwLength;

    for (Int i = 0; i != 3 && dwLength-- >= 4; ++i)
        while (dwLength-- >= 4 && *--lpFile != '\\');

    if (dwLength >= 3)
    {
        Int i;

        for (i = 0; i != sizeof(szPath) - 1; ++i)
        {
            if (szPath[i] == '?')
            {
                if (*++lpFile == 0)
                    break;

                continue;
            }
            if (((*++lpFile ^ szPath[i]) & 0xDF) != 0)
                break;
        }

        if (i == sizeof(szPath) - 1)
        {
            lpFile -= 4;
            dwLength2 = lpFile - lpFileName;
            CopyMemory(szFileName, lpFileName, dwLength2);
            *(LPDWORD)&szFileName[dwLength2] = TAG4('_sc\\');
            dwLength2 += 4;

            StrCopyA(&szFileName[dwLength2], lpFile);

            if (Io::IsPathExists(ml::String::Decode(szFileName, StrLengthA(szFileName), CP_ACP)))
                lpFileName = szFileName;
        }
    }

    return CreateFileA(lpFileName, dwDesiredAccess, dwShareMode, lpSecurityAttributes, dwCreationDisposition, dwFlagsAndAttributes, hTemplateFile);
}

UINT GetChar(UINT uChar)
{
    Int32 flag;
    uChar = HIBYTE(uChar)|(LOBYTE(uChar) << 8);

    if (uChar >= '０' && uChar <= '９')
    {
        uChar = uChar - '０' + '侽';
        flag = 0x80000000;
    }
    else if (uChar >= 'Ａ' && uChar <= 'Ｚ')
    {
        uChar = uChar - 'Ａ' + '俙';
        flag = 0x80000000;
    }
    else if (uChar >= 'ａ' && uChar <= 'ｚ')
    {
        uChar = uChar - 'ａ' + '倎';
        flag = 0x80000000;
    }
    else if (uChar == '噵')  // full width space
    {
        flag = 0x80000000;
    }
    else
    {
        TCharMap CharMap[] =
        {
            { '’', '乫' },
        };

        flag = 0;
        for (DWORD i = 0; i != countof(CharMap); ++i)
        {
            if (uChar == CharMap[i].Orig)
            {
                uChar = CharMap[i].Relpace;
                break;
            }
        }
    }

    return HIBYTE(uChar)|(LOBYTE(uChar) << 8)|flag;
}

class ZWEI2_CHAR_SURFACE
{
public:
    DWORD THISCALL GetCharSurfaceHeight(PBYTE pbSurface, LONG lHeight, int iOffset, UINT uChar, DWORD dwColor, DWORD dwColor2)
    {
        return GetCharSurface(pbSurface, lHeight, iOffset, uChar, dwColor, dwColor2);
    }

    DWORD THISCALL GetCharSurface(PBYTE pbSurface, LONG lHeight, int iOffset, UINT uChar, DWORD dwColor, DWORD dwColor2)
    {
        static HDC hDC;
        static MAT2 mat = { { 0, 1 }, { 0, 0 }, { 0, 0 }, { 0, 1 } };
        static BYTE byLumaTable[] =
        {
            0x00, 0x01, 0x01, 0x02, 0x02, 0x03, 0x03, 0x04, 0x04, 0x04,
            0x05, 0x05, 0x05, 0x06, 0x06, 0x06, 0x07, 0x07, 0x07, 0x08,
            0x08, 0x08, 0x09, 0x09, 0x09, 0x09, 0x0A, 0x0A, 0x0A, 0x0A,
            0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C,
            0x0C, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0E, 0x0E,
            0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0F, 0x0F, 0x0F, 0x0F,
            0x0F, 0x0F, 0x0F, 0x0F, 0x0F
        };

        int    x, y;
        BYTE   byBuffer[0x800], byOutline[0x400], *pbOutline, *pbBuffer;
        UINT   uCodePage, uWideChar, uHighByte;
        LONG   lfHeight, lfAlphaHeight;
        DWORD  dwSize, nBytesPerLine;
        LPVOID lpThis;
        GLYPHMETRICS gm;

        uChar = GetChar(uChar);

        if ((Int32)uChar < 0)
        {
            uChar &= 0xFFFF;

            if (pbSurface == nullptr)
            {
                return (this->*StubGetCharSurfaceHeight)(pbSurface, lHeight, iOffset, uChar, dwColor, dwColor2);
            }
            else
            {
                return (this->*StubGetCharSurface)(pbSurface, lHeight, iOffset, uChar, dwColor, dwColor2);
            }
        }

        lfHeight = 0x11;
        if (pbSurface == nullptr)
        {
            return lfHeight;
        }
        else if (hDC == nullptr)
        {
            HFONT  hFont, hOldFont;
            DWORD iQuality;
            PWSTR lpFaceName;

            hDC = CreateCompatibleDC(nullptr);
            if (hDC == nullptr)
                return 0;

            iQuality = CurrentPeb()->OSMajorVersion >= 5 ? CLEARTYPE_QUALITY : ANTIALIASED_QUALITY;

            GetPrivateProfileStringW(L"Kanade", L"FileName", L"Font.ttf", (PWSTR)byBuffer, sizeof(byBuffer), L".\\Font.ini");
            if (AddFontResourceExW((PWSTR)byBuffer, FR_PRIVATE, nullptr) != 0)
            {
                GetPrivateProfileStringW(L"Kanade", L"FaceName", L"黑体", (PWSTR)byBuffer, sizeof(byBuffer), L".\\Font.ini");
                lpFaceName = (PWSTR)byBuffer;
            }
            else
            {
                lpFaceName = L"黑体";
            }

            hFont = CreateFontW(
                        lfHeight,
                        0, 0, 0,
                        FW_NORMAL,
                        0, 0, 0,
                        GB2312_CHARSET,
                        0, 0,
                        iQuality,
                        FIXED_PITCH,
                        lpFaceName
                    );

            hOldFont = (HFONT)SelectObject(hDC, hFont);
    /*
            GetTextFaceA(hDC, sizeof(byOutline), (LPSTR)byOutline);
            if (StrCompareA((LPSTR)byOutline, lpFaceName))
            {
                DeleteObject(hFont);
                hFont = CreateFontA(lfHeight,
                    0, 0, 0,
                    FW_NORMAL,
                    0, 0, 0,
                    GB2312_CHARSET,
                    0, 0,
                    iQuality,
                    FIXED_PITCH,
                    "黑体");
                SelectObject(hDC, hFont);
            }
    */
        }

        if (uChar != '　' && uChar != 0xDFA3)   // '＿'
        {
            UINT ch;

            ch = GetChar(uChar);

            ml::String WdieChar = ml::String::Decode(&ch, 2, CP_GB2312);

            //uCodePage = 936;
            //MultiByteToWideChar(uCodePage, 0, (LPSTR)&ch, 2, (LPWSTR)&uWideChar, 1);

            dwSize = GetGlyphOutlineW(
                        hDC,
                        WdieChar[0],
                        GGO_GRAY8_BITMAP,
                        &gm,
                        sizeof(byBuffer),
                        byBuffer,
                        &mat
                    );
        }
        else
        {
            dwSize = ~0u;
        }

        memset(byOutline, 0, lfHeight * lfHeight);
        if (dwSize != -1)
        {
            nBytesPerLine = (gm.gmBlackBoxX + 3) & ~3;
            x = lfHeight - gm.gmBlackBoxY;
            y = lfHeight - gm.gmptGlyphOrigin.y - 2;
            if (y > x) y = x;
            if (y < 0) y = 0;

            pbBuffer  = byBuffer;
            pbOutline = byOutline + y * lfHeight + gm.gmptGlyphOrigin.x;

            for (UINT j = 0; j != gm.gmBlackBoxY; ++j)
            {
                for (UINT i = 0; i != nBytesPerLine; ++i)
                {
                    BYTE c = *pbBuffer++;
                    if (c && i < lfHeight)
                    {
                        pbOutline[i] = byLumaTable[c];
                    }
                }
                pbOutline += lfHeight;
            }
        }

        pbOutline = byOutline;
        pbSurface += (lHeight + (iOffset << 9)) * 2;
        for (int i = 0; i != lfHeight; ++i)
        {
            for (int j = 0; j != lfHeight; ++j)
            {
                DWORD c = *pbOutline++;
                *(LPWORD)(pbSurface + j * 2) =  c ? (WORD)((c << 0xC)|dwColor) : (WORD)dwColor;
            }
            pbSurface += 0x400;
        }

        return lfHeight;
    }

    static API_POINTER(ZWEI2_CHAR_SURFACE::GetCharSurface) StubGetCharSurface;
    static API_POINTER(ZWEI2_CHAR_SURFACE::GetCharSurfaceHeight) StubGetCharSurfaceHeight;
};

TYPE_OF(ZWEI2_CHAR_SURFACE::StubGetCharSurface) ZWEI2_CHAR_SURFACE::StubGetCharSurface = nullptr;
TYPE_OF(ZWEI2_CHAR_SURFACE::StubGetCharSurfaceHeight) ZWEI2_CHAR_SURFACE::StubGetCharSurfaceHeight = nullptr;

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    LdrDisableThreadCalloutsForDll(BaseAddress);
    ml::MlInitialize();

    MEMORY_PATCH p[] =
    {
        PATCH_MEMORY(0xEB,  1, 0x02509D),   // 路牌边界检查
        PATCH_MEMORY(0x6,   1, 0xD43FF),    // dinput 屏蔽win
        // #define DISCL_EXCLUSIVE     0x00000001
        // #define DISCL_NONEXCLUSIVE  0x00000002
        // #define DISCL_FOREGROUND    0x00000004
        // #define DISCL_BACKGROUND    0x00000008
        // #define DISCL_NOWINKEY      0x00000010

        // text offset patch
        PATCH_MEMORY(ULONG_PTR("Ｒａｎｋ　%s"),                                                       sizeof(PVOID), 0x0857A),
        PATCH_MEMORY(ULONG_PTR("Ｒａｎｋ　%s"),                                                       sizeof(PVOID), 0x0859F),
        PATCH_MEMORY(ULONG_PTR("Ｒａｎｋ　%s"),                                                       sizeof(PVOID), 0x085BF),
        PATCH_MEMORY(ULONG_PTR("Ｒａｎｋ　%s"),                                                       sizeof(PVOID), 0x085DC),
        PATCH_MEMORY(ULONG_PTR("Ｔｉｍｅ　%02d：%02d"),                                               sizeof(PVOID), 0x086CA),
        PATCH_MEMORY(ULONG_PTR("ＬＶ：s070∞\\nＲａｎｋ：s070%s\\nＴｉｍｅ：s070∞"),                   sizeof(PVOID), 0x30BC4),
        PATCH_MEMORY(ULONG_PTR("ＬＶ：s070%s\\nＲａｎｋ：s070%s\\nＴｉｍｅ：s070－－：－－"),         sizeof(PVOID), 0x309E9),
        PATCH_MEMORY(ULONG_PTR("ＬＶ：s070%d\\nＲａｎｋ：s070%s\\nＴｉｍｅ：s070%d：%02d"),           sizeof(PVOID), 0x30A34),
        PATCH_MEMORY(ULONG_PTR("ＬＶ：s070－－\\nＲａｎｋ：s070－－－－\\nＴｉｍｅ：s070－－：－－"), sizeof(PVOID), 0x30CC2),
        PATCH_MEMORY(ULONG_PTR("Ｒｅｔｒｙ"),                                                         sizeof(PVOID), 0x29ED3),
        PATCH_MEMORY(ULONG_PTR("Ｓｅｃｒｅｔ：拉格那－护目镜装"),                                     sizeof(PVOID), 0x2A7B0),
        PATCH_MEMORY(ULONG_PTR("Ｓｅｃｒｅｔ：米娅－小孩"),                                           sizeof(PVOID), 0x2A83D),
        PATCH_MEMORY(ULONG_PTR("时装商店　《Ａｎｎｅｔｔｅ》"),                                       sizeof(PVOID), 0x3CC6D),
        PATCH_MEMORY(ULONG_PTR("工房　《Ｇａｒａｇｅ·Ｇａｓｈｌｅｒ》"),                              sizeof(PVOID), 0x3CC8D),
        PATCH_MEMORY(ULONG_PTR("%s的等级达到%d\n学会了『不可思议的舞蹈』技能！！"),                   sizeof(PVOID), 0x0AE19),

        // IAT Hook
        PATCH_MEMORY((ULONG_PTR)MySetWindowPos, sizeof(PVOID), 0x1732CC),
        PATCH_MEMORY((ULONG_PTR)MyPeekMessageA, sizeof(PVOID), 0x173278),
        PATCH_MEMORY((ULONG_PTR)MyCreateFileA,  sizeof(PVOID), 0x1731C0),
    };

    MEMORY_FUNCTION_PATCH f[] =
    {
        INLINE_HOOK_JUMP_RVA(0xD9C40, PtrAdd(nullptr, &ZWEI2_CHAR_SURFACE::GetCharSurface), ZWEI2_CHAR_SURFACE::StubGetCharSurface),
        INLINE_HOOK_JUMP_RVA(0xD9BC0, PtrAdd(nullptr, &ZWEI2_CHAR_SURFACE::GetCharSurfaceHeight), ZWEI2_CHAR_SURFACE::StubGetCharSurfaceHeight),
    };

    Nt_PatchMemory(p, countof(p), f, countof(f), GetExeModuleHandle());

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