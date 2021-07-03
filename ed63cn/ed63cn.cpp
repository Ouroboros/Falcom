#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker,"/MERGE:.text=.Amano /SECTION:.Amano,EWR")
#pragma comment(linker,"/MERGE:.rdata=.Amano")
#pragma comment(linker,"/MERGE:.data=.Amano")
#pragma comment(lib, "ucidec.lib")
#pragma comment(lib, "d3d8.lib")

#include "ed63cn.h"

HDC   g_hDC;
HFONT g_hFont[6];
/*
LGFont  **ppLGFont = NULL;
HANDLE    hGameThread;
//char szProfile[] = ".\\Font.ini";
//char *szSection = "Font";
*/
Bool  g_bShowExtraInfo = True;
DWORD dwCount;
const DWORD dwLineHeight = 0xC;
const DWORD dwLineNum = 0x8;
const LPVOID g_lpfnPrintText = (LPVOID)0x528A30;

LOGFONTW lf =
{
    8,
    0,
    0,
    0,
    FW_NORMAL,
    False,
    False,
    False,
    GB2312_CHARSET,
    OUT_DEFAULT_PRECIS,
    CLIP_DEFAULT_PRECIS,
    ANTIALIASED_QUALITY,
    FIXED_PITCH,
    L"黑体"
};

#define MAX_BUFFER_SIZE 0x1000000

ASM DWORD CDECL DecodeOrig(PBYTE *ppbDest, PBYTE *ppbSrc)
{
    ASM_DUMMY_AUTO();
/*
        sub  esp, 10h;
        push ebx;
        mov  ebx, dword ptr [esp+1Ch];
        mov  eax, 48AD28h;
        jmp  eax;
*/
}

ForceInline Void STDCALL Pixel32To4444(USHORT *dst, ULONG src)
{
    *dst  = (USHORT)((src >>  4) & 0xF);
    *dst |= (USHORT)((src >>  8) & 0xF0);
    *dst |= (USHORT)((src >> 12) & 0xF00);
    *dst |= (USHORT)((src >> 16) & 0xF000);
}

int STDCALL BMP32To4444(char *dst, char *src, int width, int height)
{
    char *p = dst;

    for (int h = 0; h != height; ++h)
    {
        for (int w = 0; w != width; ++w)
        {
            Pixel32To4444((USHORT *)dst, *(ULONG *)(src + h * 1024 + w * 4));
            dst += 2;
        }
    }

    return dst - p;
}

int STDCALL BMP4444ToCH(char *src, char **pCH, ULONG *pCHSize, DWORD dwAlphaNum)
{
    char *pCHBuf, *pBuf, *p1, *p2, *p;
    DWORD sum;

    pCHBuf = *pCH + *pCHSize;

    pBuf = src;
    p1 = src;

    for (int i = 0; i != 16; ++i)
    {
        CHAR *pBak = pBuf;

        for (int j = 0; j != 16; ++j)
        {
            sum = 0;
            p = pBuf;
            for (int k = 0; k != 16; ++k)
            {
                p2 = p;
                for (int l = 0; l != 4; ++l)
                {
                    sum += ((*(PWORD)p2   ) >> 12)
                        + (*(PWORD)(p2 + 2) >> 12)
                        + (*(PWORD)(p2 + 4) >> 12)
                        + (*(PWORD)(p2 + 6) >> 12);
                    p2 += 8;
                }
                p += 512;
            }
            if (!sum)
            {
            }
            else
            {
                ++dwAlphaNum;

                for (int a = 0; a != 16; ++a)
                {
                    memcpy(pCHBuf, pBuf, 32);
                    pCHBuf += 32;
                    pBuf += 512;
                }
                pBuf = pBak;
            }

            pBuf += 32;
            pBak = pBuf;
        }

        pBuf = p1 + 8192;
        p1 += 8192;
    }

    *pCHSize = pCHBuf - *pCH;
    *(LPWORD)(*pCH) = (WORD)dwAlphaNum;

    return dwAlphaNum;
}

DWORD STDCALL UCHDecode(PBYTE pbDest, PBYTE pbSrc)
{
    CHAR *pCHBuffer, *pBuffer, *pUCIBuffer, *p4Buffer;
    DWORD dwCHSize, dwAlphaNum, dw4Size;
    int   b, w, h, stride;

    dwCHSize   = 2;
    dwAlphaNum = 0;
    pUCIBuffer = (CHAR *)pbSrc;
    pCHBuffer  = (CHAR *)pbDest;
    p4Buffer   = (CHAR *)malloc(0x20000);

    *(LPDWORD)pCHBuffer = 0;

    while (*pUCIBuffer)
    {
        UCIDecode(pUCIBuffer, INT_MAX, (Void **)&pBuffer, &stride, &w, &h, &b);
        dw4Size = BMP32To4444(p4Buffer, pBuffer, 256, 256);
        dwAlphaNum = BMP4444ToCH(p4Buffer, &pCHBuffer, (ULONG *)&dwCHSize, dwAlphaNum);
        UCIFree(pBuffer);
        pUCIBuffer += *(LPDWORD)(pUCIBuffer + 0xC) + 0x10;
        pUCIBuffer += *(LPDWORD)pUCIBuffer + 4;
    }

    free(p4Buffer);

    return dwCHSize;
}

DWORD CDECL DecodeFile(PBYTE *ppbDest, PBYTE *ppbSrc)
{
    PBYTE pbSrc;
    DWORD dwHeader, dwDecodedSize;

    pbSrc = *ppbSrc;
    dwHeader = *(LPDWORD)pbSrc & 0x00FFFFFF;
    switch (dwHeader)
    {
    case 'ICU':     // UCI
        dwDecodedSize = 0;
        break;

    case 'HCU':     // UCH
        dwDecodedSize = UCHDecode(*ppbDest, pbSrc + 3);
        *ppbDest += dwDecodedSize;
        break;

    case 'ACU':     // UCA
        dwDecodedSize = 0;
        break;

    default:
        dwDecodedSize = DecodeOrig(ppbDest, ppbSrc);
    }

    return dwDecodedSize;
}

ASM Void FASTCALL OldGetCharSurface(PVOID pThis, PVOID, PWCHAR lpText, PBYTE pbSurface, DWORD dwStride, DWORD dwColorIndex)
{
    ASM_DUMMY_AUTO();
}

Void FASTCALL GetCharSurface(PVOID lpThis, PVOID, PWCHAR lpText, PBYTE pbSurface, DWORD dwStride, DWORD dwColorIndex)
{
    static LONG lLastIndex, Height[6] = { 0x8, 0xC, 0x10, 0x14, 0x18, 0x20 };

    int   x, y;
    UINT  uChar;
    LONG  lfHeight;
    DWORD dwSize, nBytesPerLine, dwColor;
    GLYPHMETRICS gm;

    dwColor = *(PDWORD)((ULONG_PTR)lpThis + 0x24);

    BYTE byBuffer[0x800], byOutline[0x400], *pbOutline, *pbBuffer;
    MAT2 mat = { { 0, 1 }, { 0, 0 }, { 0, 0 }, { 0, 1 } };

    if (g_hDC == NULL)
    {
        if ((GetVersion() & 0xFF) > 5)
        {
            lf.lfQuality = CLEARTYPE_QUALITY;
        }

        g_hDC = CreateCompatibleDC(NULL);
        if (g_hDC == NULL)
            return;

        for (int i = 0; i != countof(g_hFont); ++i)
        {
            lf.lfHeight = Height[i];
            g_hFont[i] = CreateFontIndirectW(&lf);
        }

        lLastIndex = -1;
    }

    lfHeight = Height[dwColor];
    if (lLastIndex != dwColor)
    {
        lLastIndex = dwColor;
        lf.lfHeight = lfHeight;
        SelectObject(g_hDC, g_hFont[dwColor]);
    }

    uChar = *lpText;

    if (uChar == TAG2('丂'))
    {
        uChar = '　';
    }
    else
    {
        static WCHAR cn[] = { TAG2('㈱'), TAG2('⊙'),  TAG2('≡'),  TAG2('◆'),  TAG2('━'),  TAG2('―') };
        static WCHAR jp[] = { TAG2('噴'), TAG2('侓'), TAG2('佀'), TAG2('仧'), TAG2('劒'), TAG2('乗') };

        for (UINT i = 0; i != countof(cn); ++i)
        {
            if (uChar == cn[i])
            {
                uChar = jp[i];
                OldGetCharSurface(lpThis, 0, (PWCHAR)&uChar, pbSurface, dwStride, dwColorIndex);
                return;
            }
        }
    }

    dwColor = 0;
    memset(byOutline, 0, lfHeight * lfHeight);
    if (uChar != '　')
    {
        UINT wChar;
        MultiByteToWideChar(936, 0, (LPSTR)&uChar, 2, (LPWSTR)&wChar, 1);
        dwSize = GetGlyphOutlineW(g_hDC,
                        wChar,
                        GGO_GRAY8_BITMAP,
                        &gm,
                        sizeof(byBuffer),
                        byBuffer,
                        &mat);
        if (dwSize != -1)
        {
            static WORD wColorTable[] =
            {
                0x0FFF, 0x0FC7, 0x0F52, 0x08CF, 0x0FB4, 0x08F9, 0x0888, 0x0FEE, 0x0853, 0x0333,
                0x0CA8, 0x0FDB, 0x0ACE, 0x0CFF, 0x056B, 0x0632, 0x0135, 0x0357, 0x0BBB, 0x0000,
                0x0BFB, 0x0FBB
            };

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

            nBytesPerLine = gm.gmBlackBoxX + 3 & ~3;
            x = lfHeight - gm.gmBlackBoxY;
            y = lfHeight - gm.gmptGlyphOrigin.y - 2;
            if (y > x) y = x;
            if (y < 0) y = 0;

            pbBuffer  = byBuffer;
            pbOutline = byOutline + y * lfHeight + gm.gmptGlyphOrigin.x;

            for (int j = 0; j != gm.gmBlackBoxY; ++j)
            {
                for (int i = 0; i != nBytesPerLine; ++i)
                {
                    char c = *pbBuffer++;
                    if (c && i < lfHeight)
                    {
                        c = byLumaTable[c];
                        if (c > 9 && c < 12) c += 1;
                        pbOutline[i] = c;
                    }
                }
                pbOutline += lfHeight;
            }

            dwColor = wColorTable[dwColorIndex >= countof(wColorTable) ? 0 : dwColorIndex];
        }
    }

    pbOutline = byOutline;
    for (int i = 0; i != lfHeight; ++i)
    {
        for (int j = 0; j != lfHeight; ++j)
        {
            DWORD c = *pbOutline++;
            if (c)
            {
                *(LPWORD)(pbSurface + j * 2) = (WORD)((c << 0xC)|dwColor);
            }
        }
        pbSurface += dwStride;
    }
}

Void STDCALL SetFrameSize(DWORD x, DWORD y, DWORD w, DWORD h)
{
    DWORD dwBak, dwAttCount;
    PBYTE pbCharData;

    __asm
    {
        mov dwBak, ecx;
        mov pbCharData, edi;
        mov ax, word ptr [esi + 6150h];
        and eax, 200h;
        neg eax;
        sbb eax, eax;
        and eax, 3;
        add eax, 4;
        mov dwAttCount, eax;
    }

    DWORD H1 = 0x3E, H2 = 0x72, dwHCondition = 0x22;

    if (g_bShowExtraInfo && *(DWORD *)0x275DF08)
    {
        WORD wWord;

        h += dwLineNum - 2;
        y -= 0x18;
        H1 += dwLineHeight * dwLineNum;
        H2 += dwLineNum + 7 * 0xC;
        dwHCondition += dwLineHeight * dwLineNum;
        pbCharData = PBYTE(0x66E640 + *(LPDWORD)(pbCharData + 0x98D64) * 0x2490 + 0x2370);
        while (LOBYTE(wWord = *(WORD *)pbCharData))
        {
            ++pbCharData;
            if (wWord == TAG2('\\n'))
            {
                ++h;
            }
        }
    }

    *(DWORD *)0x44A203 = H1;
    *(DWORD *)0x44A266 = H1;
    *(DWORD *)0x44A330 = H2;
    *(DWORD *)0x44A085 = dwHCondition;

    __asm
    {
        push h;
        push w;
        push y;
        push x;
        mov  ecx, dwBak;
        mov  eax, 526D00h;
        call eax;
    }
}

Void STDCALL PrintText(int x, int y, LPSTR lpText, int dwColor, int fnWeight)
{
    DWORD dwBak;

    __asm mov dwBak, ecx;
    if (g_bShowExtraInfo && *(DWORD *)0x275DF08)
    {
        y += dwLineHeight * dwLineNum;
    }

    __asm
    {
        push fnWeight;
        push dwColor;
        push lpText;
        push y;
        push x;
        mov  ecx, dwBak;
        call g_lpfnPrintText;
    }
}

Void STDCALL DisplayStatus()
{
    if (g_bShowExtraInfo == False)
    {
        return;
    }

    int dwVPos, dwBak;
    char szBuffer[1000];
    PBYTE pbCharStatus;
    LPVOID lpfnPrintText;
    static char *szText = "CP:";
    static char *s_szStatus[] = { "LV ", "STR", "DEF", "ATS", "ADF", "SPD", "MOV" };
    static DWORD s_dwOffset[] = { LV, STR, DEF, ATS, ADF, SPD, MOV };

    __asm
    {
        mov  pbCharStatus, ebx;
        mov  eax, g_lpfnPrintText;
        mov  lpfnPrintText, eax;
        mov  dwBak, esi;
        push lf.lfWeight;
        push 0Bh;
        push szText;
        push 22h;
        push 0;
        mov  ecx, dwBak;
        call eax;
    }

    dwVPos = 0x22;
    wsprintfA(szBuffer, "%6d／%6d", *(pbCharStatus + CP_CUR), *(pbCharStatus + CP_UP));
//    wsprintfA(szBuffer, "%6d乛%6d", *(pbCharStatus + CP_CUR), *(pbCharStatus + CP_UP));

    __asm
    {
        push lf.lfWeight;
        push 0;
        lea  eax, szBuffer;
        push eax;
        push dwVPos;
        push 2Ah;
        mov ecx, dwBak;
        call lpfnPrintText;
    }

    for (BYTE i = 0; i != sizeof(s_dwOffset) / sizeof(*s_dwOffset); ++i)
    {
        dwVPos += dwLineHeight;

        wsprintfA(szBuffer, "%s", s_szStatus[i]);
        __asm
        {
            push lf.lfWeight;
            push 0Bh;
            lea  eax, szBuffer;
            push eax;
            push dwVPos;
            push 0;
            mov ecx, dwBak;
            call lpfnPrintText;
        }

        wsprintfA(szBuffer, "%6d", *(WORD *)(pbCharStatus + s_dwOffset[i]));
        __asm
        {
            push lf.lfWeight;
            push 0;
            lea  eax, szBuffer;
            push eax;
            push dwVPos;
            push 59h;
            mov  ecx, dwBak;
            call lpfnPrintText;
        }
    }
}

Void ChangeFont()
{
//    char        szBuffer[LF_FACESIZE];
//    DWORD        dwKeysValues[COUNT_OF_KEYS];
    CHOOSEFONTW    chf;

    memset(&chf, 0, sizeof(chf));
    chf.lStructSize = sizeof(CHOOSEFONTA);
    chf.lpLogFont   = &lf;
    chf.hwndOwner   = *(HWND *)0x2DE92D0;
    chf.nSizeMax    = 20;
    chf.nSizeMin    = 5;
    chf.Flags       = CF_BOTH|CF_TTONLY|CF_INITTOLOGFONTSTRUCT|CF_LIMITSIZE;
    lf.lfHeight     += 3;

    if (ChooseFontW(&chf))
    {
        if (g_hDC)
        {
            DeleteDC(g_hDC);
            g_hDC = NULL;
            lf.lfQuality = ANTIALIASED_QUALITY;
            for (int i = 0; i != countof(g_hFont); ++i)
            {
                HFONT hFont = g_hFont[i];
                if (hFont) DeleteObject(hFont);
            }
        }
        if (lf.lfHeight < 0)
        {
            lf.lfHeight = -lf.lfHeight;
        }

        lf.lfHeight -=3;
/*
        GetLogFontData(dwKeysValues, &lf);
        for (int i = 0; i != COUNT_OF_KEYS; ++i)
        {
            wsprintfA(szBuffer, "%d", dwKeysValues[i]);
            WritePrivateProfileStringA(szSection, szConfigKeys[i], szBuffer, szProfile);
        }
        WritePrivateProfileStringA(szSection, "FontName", lf.lfFaceName, szProfile);
*/
    }
    else
    {
        lf.lfHeight -= 3;
    }
}

BOOL __cdecl ShowGameWindow(BOOL bShow)
{
    HWND hWnd = *(HWND *)0x2DE92D0;

    if (bShow == False)
    {
        SetWindowLongW(hWnd, GWL_STYLE, WS_VISIBLE|WS_POPUP);
        return True;
    }

    int  x, y, w, h;
    RECT rcWorkArea, rcGame = {0, 0, *(int *)0x5B8644, *(int *)0x5B8648};

    SetWindowLongW(hWnd, GWL_STYLE, WS_POPUP|WS_CAPTION|WS_SYSMENU|WS_GROUP);
    AdjustWindowRectEx(&rcGame, GetWindowLongW(hWnd, GWL_STYLE), False, GetWindowLongW(hWnd, GWL_EXSTYLE));

    SystemParametersInfoW(SPI_GETWORKAREA, 0, &rcWorkArea, 0);
    w = rcGame.right - rcGame.left;
    h = rcGame.bottom - rcGame.top;
    x = ((rcWorkArea.right - rcWorkArea.left) - w) >> 1;
    y = ((rcWorkArea.bottom - rcWorkArea.top) - h) >> 1;
    SetWindowPos(hWnd, HWND_TOP, x, y, w, h, SWP_SHOWWINDOW);
//    CreateThread(NULL, 0, MyThread, 0, 0, NULL);
    return True;
}

BOOL WINAPI MyPeekMessageA(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg)
{
    BOOL bResult = PeekMessageA(lpMsg, hWnd, wMsgFilterMin, wMsgFilterMax, wRemoveMsg);

    if (bResult == False)
    {
        DWORD dwTickCount;
        static DWORD dwLastTickCount;

        dwTickCount = GetTickCount();
        if (dwTickCount - dwLastTickCount < 10 && --dwCount == 0)
        {
            dwCount = 4;
            SleepEx(1, FALSE);
        }
        dwLastTickCount = dwTickCount;
    }
    else if (lpMsg->message == WM_KEYDOWN)
    {
/*
        switch (lpMsg->wParam)
        {
            case VK_F1:
                ChangeFont();
                break;

            case VK_F2:
                g_bShowExtraInfo = True;
                break;

            case VK_F3:
                g_bShowExtraInfo = False;
                break;
        }
*/
    }

    return bResult;
}

HANDLE WINAPI MyOpenMutexA(DWORD dwDesiredAccess, BOOL bInheritHandle, LPCSTR lpName)
{
    return NULL;
}

Void GetLogFontData(DWORD *dwArray, PLOGFONT pLogfont)
{
    dwArray[0]    = pLogfont->lfHeight;
    dwArray[1]    = pLogfont->lfWidth;
    dwArray[2]    = pLogfont->lfEscapement;
    dwArray[3]    = pLogfont->lfOrientation;
    dwArray[4]    = pLogfont->lfWeight;
    dwArray[5]    = pLogfont->lfItalic;
    dwArray[6]    = pLogfont->lfUnderline;
    dwArray[7]    = pLogfont->lfStrikeOut;
    dwArray[8]    = pLogfont->lfCharSet;
    dwArray[9]    = pLogfont->lfOutPrecision;
    dwArray[10]    = pLogfont->lfClipPrecision;
    dwArray[11]    = pLogfont->lfQuality;
    dwArray[12]    = pLogfont->lfPitchAndFamily;
}

Void SetLogFontData(DWORD *dwArray, PLOGFONT pLogfont)
{
    pLogfont->lfHeight            = dwArray[0];
    pLogfont->lfWidth            = dwArray[1];
    pLogfont->lfEscapement        = dwArray[2];
    pLogfont->lfOrientation        = dwArray[3];
    pLogfont->lfWeight            = dwArray[4];
    pLogfont->lfItalic            = (BYTE)dwArray[5];
    pLogfont->lfUnderline        = (BYTE)dwArray[6];
    pLogfont->lfStrikeOut        = (BYTE)dwArray[7];
    pLogfont->lfCharSet            = (BYTE)dwArray[8];
    pLogfont->lfOutPrecision    = (BYTE)dwArray[9];
    pLogfont->lfClipPrecision    = (BYTE)dwArray[10];
    pLogfont->lfQuality            = (BYTE)dwArray[11];
    pLogfont->lfPitchAndFamily    = (BYTE)dwArray[12];
}

DWORD ReadFileToBuffer(LPSTR szName, PBYTE pbBuffer, DWORD dwOffset, DWORD nBytesToRead, LPVOID, LPVOID, LPVOID, LPVOID, LPVOID)
{
    if (szName == NULL)
    {
        return -1;
    }

    DWORD   dwSize, dwRead;
    HANDLE  hFile;
    LRESULT lResult;

    hFile = CreateFileA(szName,
                    GENERIC_READ,
                    FILE_SHARE_READ,
                    NULL,
                    OPEN_EXISTING,
                    FILE_ATTRIBUTE_NORMAL,
                    NULL);
    if (hFile == INVALID_HANDLE_VALUE)
    {
        return -1;
    }

    dwSize = GetFileSize(hFile, NULL);
    SetFilePointer(hFile, dwOffset, NULL, FILE_BEGIN);
    if (nBytesToRead == 0)
    {
        nBytesToRead = dwSize - dwOffset;
    }

    if (pbBuffer == NULL)
    {
        CloseHandle(hFile);
        return dwSize;
    }

    lResult = ReadFile(hFile, pbBuffer, nBytesToRead, &dwRead, NULL) ? dwRead : -1;
    CloseHandle(hFile);
    return lResult;
}

LRESULT InitLGFont(CHAR *szFontName, LGFont *pLGFont, bool bRead)
{
    PBYTE   pbBuffer;
    DWORD   dwRead;
    HANDLE  hFile, hHeap;
    DWORD   dwWidth, dwHeight;
    LONG64  l64Temp;
    LRESULT lResult;

    hFile = CreateFileA(szFontName,
                    GENERIC_READ,
                    FILE_SHARE_READ,
                    NULL,
                    OPEN_EXISTING,
                    FILE_ATTRIBUTE_NORMAL,
                    NULL);
    if (hFile == INVALID_HANDLE_VALUE)
    {
        return False;
    }

    lResult = ReadFile(hFile, &pLGFont->TTGAHeader, sizeof(pLGFont->TTGAHeader), &dwRead, NULL);
    if (lResult == False)
    {
        CloseHandle(hFile);
        return -1;
    }

    pLGFont->dwVal1 = pLGFont->dwVal2 = 0x200;
    dwWidth  = pLGFont->TTGAHeader.wWidth;
    dwHeight = pLGFont->TTGAHeader.wHeight;

    l64Temp  = dwWidth * 0xAC769185ll;
    dwWidth  = (INT32)(l64Temp >> 32) + dwWidth;
    dwWidth -= pLGFont->TTGAHeader.wWidth;
    dwWidth  = (INT32)dwWidth >> 7;
    dwWidth  = (dwWidth >> 0x1F) + dwWidth;

    l64Temp  = dwHeight * 0x82082083ll;
    dwHeight = (INT32)(l64Temp >> 32) + dwHeight;
    dwHeight-= pLGFont->TTGAHeader.wHeight;
    dwHeight = (INT32)dwHeight >> 6;
    dwHeight = (dwHeight >> 0x1F) + dwHeight;

    pLGFont->dwVal[0] = dwWidth;
    pLGFont->dwVal[1] = dwHeight;
    pLGFont->dwVal[2] = pLGFont->dwVal1 / dwWidth;
    pLGFont->dwVal[3] = pLGFont->dwVal2 / dwHeight;

    hHeap = GetProcessHeap();

    pbBuffer =
    pLGFont->pbFont[0] = (PBYTE)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, ((dwWidth * dwHeight) + 1) * 0x1A);
    if (pbBuffer == NULL)
    {
        return False;
    }

    pLGFont->pbFont[1] = (PBYTE)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, pLGFont->dwVal2 * pLGFont->dwVal1 * 4);
    if (bRead == false)
    {
        pLGFont->pbFont[2] = NULL;
        lResult = True;
    }
    else
    {
        dwWidth  = pLGFont->TTGAHeader.wWidth;
        dwHeight = pLGFont->TTGAHeader.wHeight;
        dwRead = dwWidth * dwHeight * 4;
        pLGFont->pbFont[2] = (PBYTE)HeapAlloc(hHeap, 0, dwRead + 4);
        lResult = ReadFile(hFile, pLGFont->pbFont[2], dwRead, &dwRead, NULL);
        *(LPDWORD)(pLGFont->pbFont[2] + dwRead) = 0;
    }

    CloseHandle(hFile);
    return lResult;
}

int CDECL mysprintf(char *szDest, const char *szFormat, DWORD dwIndex)
{
    int n;
    char *szPath[] = { "dat\\FC", "dat\\SC", "." };

    for (UINT i = 0; i != countof(szPath); ++i)
    {
        n = wsprintfA(szDest, "%s\\ED6_DT%02X.dat", szPath[i], dwIndex);
        if (GetFileAttributesA(szDest) != -1)
            break;
    }

    return n;
}

ASM Void WINAPI SafeGetSize()
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

VOID Init()
{
    static BOOL bWrite = False;

    if (!bWrite)
    {
//        DWORD dwKeysValues[COUNT_OF_KEYS];

        DWORD dwOld;

        bWrite = True;
        if (!VirtualProtectEx((HANDLE)-1, (LPVOID)0x401000, 0x19C000, PAGE_EXECUTE_READWRITE, &dwOld))
            return;

        BYTE byInstruction[] =
        {
            0x33, 0xC9, 0x51, 0x8A, 0xAE, 0x51, 0x61, 0x00, 0x00, 0x80,
            0xE5, 0x02, 0xF7, 0xD9, 0x1B, 0xC9, 0x83, 0xE1, 0x26, 0x8D,
            0xB9, 0x72, 0x00, 0x00, 0x00, 0x8B, 0xCE
        };

        dwCount = 4;
        CopyMemory((LPVOID)0x44A31B, byInstruction, sizeof(byInstruction));

        MEMORY_PATCH patch[] =
        {
//	{0xE9,          1, 0x0A09F0},		// 边界
//	{0x00,          1, 0x061CB8},		// 分辨率4:3
            {0x07,          1, 0x09BEF7},		// 边界
            {0x07,          1, 0x0A09F7},		// 边界
            {0x0404,        2, 0x132DE2},		// unknown
//	{0x00,          1, 0x006175},		// force ShowInfo
//	{0x54,          1, 0x0A4CF5},		// OpenMutex failed
            {0x00,          4, 0x0A0C3D},		// CreateWindowEx->Style
            {0xC3FFC883,    4, 0x086DD0},		// 存档目录
            {0x07,          1, 0x147CDD},		// 开启DebugMode

            // IAT Hook
            {(DWORD)MyPeekMessageA, 4, 0x19D248},		// PeekMessageA
//	        {(DWORD)MyOpenMutexA,   4, 0x19D0D8},		// OpenMutexA
        };

        MEMORY_FUNCTION_PATCH funcpatch[] =
        {
            { JUMP, 0x09C150, GetCharSurface, 0x01 , OldGetCharSurface },
//    { CALL, 0x04A04B, PrintText,      0x00 },
//    { CALL, 0x04A108, PrintText,      0x00 },
//    { CALL, 0x04A1A1, PrintText,      0x00 },
//    { CALL, 0x049EE6, SetFrameSize,   0x00 },
//    { CALL, 0x04A2BE, DisplayStatus,  0x58 },
            { CALL, 0x0A0C62, ShowGameWindow, 0x00 },
//    { CALL, 0x0870ED, mysprintf,      0x00 },
            { CALL, 0x08721A, SafeGetSize,    0x02 },
//    { JUMP, 0x08AD20, DecodeFile,     0x03, DecodeOrig },
        };

        PatchMemoryNoVP(patch, countof(patch), funcpatch, countof(funcpatch), GetModuleHandleW(NULL));
        return;

        {
/*
            GetLogFontData(dwKeysValues, &lf);
            for (int i = 0; i != COUNT_OF_KEYS; ++i)
            {
                dwKeysValues[i] = GetPrivateProfileInt(szSection, szConfigKeys[i], dwKeysValues[i], szProfile);
            }
            SetLogFontData(dwKeysValues, &lf);
            GetPrivateProfileStringA(szSection, "FontName", lf.lfFaceName, lf.lfFaceName, LF_FACESIZE, szProfile);
*/
/*
            DuplicateHandle((HANDLE)-1,
                (HANDLE)-2,
                (HANDLE)-1,
                &hGameThread,
                0,
                FALSE,
                DUPLICATE_SAME_ACCESS);
*/
//            CreateThread(NULL, 0, MyThread, 0, 0, NULL);

//            return True;
/*
            bool   bRead[] = {0, 1, 1, 0, 0, 0};
            HANDLE hHeap;
            const static DWORD dwFontNum = 6;

            hHeap = GetProcessHeap();
            ppLGFont = (LGFont **)HeapAlloc(hHeap, 0, dwFontNum * sizeof(*ppLGFont));
            for (int i = 0; i != dwFontNum; ++i)
            {
                ppLGFont[i] = (LGFont *)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, sizeof(**ppLGFont));
            }

            for (int i = 0; i != dwFontNum; ++i)
            {
                wsprintfA(ppLGFont[i]->szName, "LG_Font%.2d.tga", i + 1);
                if (InitLGFont(ppLGFont[i]->szName, ppLGFont[i], bRead[i]) == FALSE)
                {
                    wsprintfA(szProfile, "%s 初始化失败！", ppLGFont[i]->szName);
                    MessageBox(NULL, szProfile, "Nagisa", 0x40);
                    ExitProcess(0);
                }
            }
*/
        }
    }
}

BOOL WINAPI DllMain(HINSTANCE hInstance, ULONG Reason, LPVOID lpReserved)
{
    UNREFERENCED_PARAMETER(lpReserved);

    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            DisableThreadLibraryCalls(hInstance);
            Init();
            break;

        case DLL_PROCESS_DETACH:
            break;
    }

    return TRUE;
}
