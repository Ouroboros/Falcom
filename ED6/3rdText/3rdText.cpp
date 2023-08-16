#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Hiromi /SECTION:.Hiromi,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Hiromi")
#pragma comment(lib, "msvcrt.lib")
#pragma comment(lib, "psapi.lib")
#pragma comment(lib, "shlwapi.lib")
#pragma warning(disable:4309)

#include <Windows.h>
#include <Shlwapi.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include "getmainargs.h"
#include "my_mem.h"
#include "header.h"
//#include "Dict1.h"
//#include "Dict2.h"
extern "C"
{
#include "7zAlloc.h"
#include "LzmaDec.h"
    extern HANDLE hHeap = 0;
}

#define FILE_NAME lpFileName
enum FILETYPE {MS, AS, DT22, SN, UNKNOWN};
HANDLE g_hSemaphore;
PBYTE pbDict[2] = {(PBYTE)_DICT1_LZMA_, (PBYTE)_DICT2_LZMA_};

void  STDCALL ExtractDict(PBYTE *pbData);
DWORD WINAPI  Import(LPVOID lpParameter);
void  STDCALL ReplaceString(PBYTE *pbDict, PBYTE pbFile, DWORD dwSize);
DWORD STDCALL StringToAnsi(PBYTE pbFile, BYTE byFileType, DWORD dwSize);
FILETYPE STDCALL CheckFileType(PBYTE pbFile, DWORD dwSize, char *szFileName);

DWORD WINAPI Import(LPVOID lpParameter)
{
    BOOL   bIsDirectory;
    CHAR   szFileName[MAX_PATH];
    PBYTE  pbFile;
    LPSTR  lpPath, lpFileName;
    HANDLE hFile, hMap, hFind;
    DWORD  dwFileAttributes, dwSize, dwNewSize, dwCount, dwTotal;
    FILETYPE FileType;
    WIN32_FIND_DATA wfd;

    lpPath = (LPSTR)lpParameter;
    dwNewSize = dwCount = dwTotal = 0;
    dwFileAttributes = GetFileAttributes(lpPath);
    if (dwFileAttributes == INVALID_FILE_ATTRIBUTES)
    {
        return 0;
    }

    bIsDirectory = dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY;
    if (bIsDirectory)
    {
        sprintf(szFileName, "%s\\*.*", lpPath);
        hFind = FindFirstFile(szFileName, &wfd);
        if (hFind == INVALID_HANDLE_VALUE)
        {
            return 0;
        }
        lpFileName = szFileName;
    }
    else
    {
        lpFileName = lpPath;
    }

    while (ReleaseSemaphore(g_hSemaphore, 1, NULL) == FALSE)
    {
        Sleep(1);
    }

    do
    {
        if (bIsDirectory)
        {
            if (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)
            {
                continue;
            }
            sprintf(szFileName, "%s\\%s", lpPath, wfd.cFileName);
        }

        ++dwTotal;
        hFile = CreateFile(FILE_NAME,
            GENERIC_READ|GENERIC_WRITE,
            FILE_SHARE_READ|FILE_SHARE_WRITE,
            NULL,
            OPEN_EXISTING,
            FILE_ATTRIBUTE_NORMAL,
            NULL);
        if (hFile == INVALID_HANDLE_VALUE)
        {
            printf("CreateFile() failed: %s\n", FILE_NAME);
            continue;
        }

        dwSize = GetFileSize(hFile, NULL);

        if (dwSize != 0)
        {
            hMap = CreateFileMapping(hFile, NULL, PAGE_READWRITE, 0, dwSize, NULL);
            if (hMap == NULL)
            {
                printf("CreateFileMapping() failed: %s\n", FILE_NAME);
                CloseHandle(hFile);
                continue;
            }

            pbFile = (PBYTE)MapViewOfFile(hMap, FILE_MAP_ALL_ACCESS, 0, 0, 0);
            CloseHandle(hMap);
            if (pbFile == NULL)
            {
                printf("MapViewOfFile() failed: %s\n", FILE_NAME);
                CloseHandle(hFile);
                continue;
            }

            FileType = CheckFileType(pbFile, dwSize, PathFindFileName(FILE_NAME));
            if (FileType != UNKNOWN)
            {
                ReplaceString(pbDict, pbFile, dwSize);
                dwNewSize = StringToAnsi(pbFile, FileType, dwSize);
                ++dwCount;
            }

            UnmapViewOfFile(pbFile);
            if (dwNewSize != 0)
            {
                SetFilePointer(hFile, dwNewSize, 0, FILE_BEGIN);
                SetEndOfFile(hFile);
            }
        }
        CloseHandle(hFile);
    } while (bIsDirectory && FindNextFile(hFind, &wfd));

    if (bIsDirectory)
    {
        FindClose(hFind);
    }

    WaitForSingleObject(g_hSemaphore, INFINITE);
    return dwCount;
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    if (argc < 2) return;

    DWORD    dwMaxThread, dwExitCode, dwCount = 0, dwTotal = 0;
    LPHANDLE phThread;
    SYSTEM_INFO si;
    LARGE_INTEGER lFrequency, lStopCounter, lStartCounter;

    GetSystemInfo(&si);
    dwMaxThread = si.dwNumberOfProcessors << 1;
    g_hSemaphore = CreateSemaphore(NULL, 1, dwMaxThread, NULL);
    if (g_hSemaphore == NULL)
    {
        printf("CreateSemaphore() failed.\n");
    }
    else
    {
        QueryPerformanceFrequency(&lFrequency);
        QueryPerformanceCounter(&lStartCounter);
        hHeap = GetProcessHeap();
        ExtractDict(pbDict);
        phThread = (LPHANDLE)HeapAlloc(hHeap, HEAP_ZERO_MEMORY, (argc - 1) * sizeof(*phThread));
        for (DWORD i = 0; i != argc - 1; ++i)
            phThread[i] = CreateThread(NULL, 0, Import, (LPVOID)argv[i + 1], 0, NULL);

        WaitForMultipleObjectsEx(argc - 1, phThread, TRUE, INFINITE, FALSE);
        for (DWORD i = 0; i != argc - 1; ++i)
        {
            GetExitCodeThread(phThread[i], &dwExitCode);
            dwCount += dwExitCode;
        }

        for (char i = 0; i != countof(Array_of_Data); ++i)
        {
            HeapFree(hHeap, 0, pbDict[i]);
        }

        CloseHandle(g_hSemaphore);
        QueryPerformanceCounter(&lStopCounter);
        printf("Success: %d\n"
            "Elapsed time: %lf ms\n",
            dwCount,
            (lStopCounter.QuadPart - lStartCounter.QuadPart) * 1000.0 / lFrequency.QuadPart);
    }
}

bool __stdcall IsAsciiString(PBYTE pbFile)
{
    for (int i = 0; i != 4; ++i)
    {
        if (*pbFile >= 'G' || *pbFile < '0' || *pbFile == '@')
            return false;
        ++pbFile;
    }
    return true;
}

void __stdcall ConvertStringToAnsi(PBYTE &pbSrc, PBYTE &pbDest, char *szAscii)
{
    ++pbSrc;
    *(DWORD *)szAscii = *(WORD *)pbSrc << 16 | *(WORD *)(pbSrc + 2);
    *(WORD *)pbDest = (WORD)strtoul(szAscii, 0, 16);
    pbDest += 2;
    pbSrc  += 4;
}

DWORD __stdcall StringToAnsi(PBYTE pbFile, BYTE byFileType, DWORD dwSize)
{
    char	szAscii[5];
    PBYTE	pbSrc, pbDest, pbEnd = pbFile + dwSize;
    DWORD	dwChangeSize = 0;

    szAscii[4] = 0;
    pbSrc = pbDest = pbFile;
    while (pbSrc <= pbEnd)
    {
        if (*pbSrc != '|' || IsAsciiString(pbSrc + 1) == false)
        {
            *pbDest++ = *pbSrc++;
            continue;
        }

        if (byFileType == SN || byFileType == AS)
        {
            BYTE byJmpMark;
            WORD wEndMark;

            wEndMark = (byFileType == SN ? 0x0002 : 0x0000);
            byJmpMark = byFileType;
            do
            {
                if (*pbSrc == '|' && IsAsciiString(pbSrc + 1) == true)
                {
                    ConvertStringToAnsi(pbSrc, pbDest, szAscii);
                }
                else
                {
                    *pbDest++ = *pbSrc++;
                }

                if (byFileType == AS)
                {
                    if (*(WORD *)pbSrc == 0x0000)
                    {
                        if (*(pbDest - 3) != 0)
                        {
                            if (*(pbDest - 2) == 0)
                            {
                                *pbDest++ = *pbSrc++;
                            }
                        }
                        break;
                    }
                }
                else
                {
                    if (*(WORD *)pbSrc == 0x0002 ||
                        *(WORD *)pbSrc == 0x0001)
                    {
                        break;
                    }
                    else if (pbSrc > pbEnd)
                    {
                        return pbDest - pbFile;
                    }
                }
            } while (1);

            *(WORD *)pbDest = *(WORD *)pbSrc;
            pbDest += 2;
            pbSrc  += 2;
            *pbDest++ = byJmpMark;
            *(WORD *)pbDest = pbSrc - pbFile;

            pbDest += 2;
            while (pbDest != pbSrc)
            {
                *pbDest++ = 0;
            }
            pbDest = pbSrc;
        }
        else if (byFileType == MS)
        {
            do
            {
                if (*pbSrc == '|' && IsAsciiString(pbSrc + 1) == true)
                {
                    ConvertStringToAnsi(pbSrc, pbDest, szAscii);
                }
                else
                {
                    *pbDest++ = *pbSrc++;
                }
            } while (pbSrc <= pbEnd);

            while (*--pbDest == 0);
            ++pbDest;

            dwChangeSize = pbDest - pbFile;
        }
        else /* if (byFileType == DT22) */
        {
            do
            {
                if (*pbSrc == '|' && IsAsciiString(pbSrc + 1) == true)
                {
                    ConvertStringToAnsi(pbSrc, pbDest, szAscii);
                }
                else
                {
                    *pbDest++ = *pbSrc++;
                }
            } while (*pbSrc);

            *pbDest++ = *pbSrc++;
            while (pbDest != pbSrc)
            {
                *pbDest++ = 0;
            }
        }
    }
    return dwChangeSize;
}

void __stdcall ReplaceString(PBYTE *pbDict, PBYTE pbFile, DWORD dwSize)
{
    BYTE	byDict, byTemp;
    LPSTR	lpszText;
    DWORD	dwTextOffset, dwTextLen;
    PBYTE	pbEnd;

    pbEnd = pbFile + dwSize;

    while (pbFile <= pbEnd)
    {
        //		if (*pbFile++ == 'x' && *pbFile++ == 'f')
        if (*(WORD *)pbFile++ == 'fx')
        {
            ++pbFile;
            switch (*pbFile++)
            {
            case '1': byDict = 0; break;
            case '2': byDict = 1; break;
            default : --pbFile; continue;
            }

            byTemp = pbFile[7];
            pbFile[7] = 0;
            dwTextOffset = atoi((char *)pbFile) << 2;
            pbFile[7] = byTemp;
            if (dwTextOffset > *(DWORD *)pbDict[byDict])
            {
                --pbFile;
                continue;
            }

            lpszText = LPSTR(pbDict[byDict] + *(DWORD *)(pbDict[byDict] + dwTextOffset));
            dwTextLen = lstrlenA(lpszText);
            pbFile -= 3;
            memcpy(pbFile, lpszText, dwTextLen);
            pbFile += dwTextLen;
        }
    }
}

FILETYPE STDCALL CheckFileType(PBYTE pbFile, DWORD dwSize, char *szFileName)
{
    bool	bBreak = false;
    PBYTE	pbTemp, pbEnd = pbFile + dwSize;

    pbTemp = pbFile + *(WORD *)pbFile;
    if (pbTemp <= pbEnd)
    {
        if (pbTemp - 5 > pbFile)
            if (*(DWORD *)(pbTemp - 5) == -1 || *(DWORD *)(pbFile + 6) == -1)
                return AS;
    }

    if (dwSize > 0x5A)
    {
        pbTemp = pbFile + *(WORD *)(pbFile + 0x5A);

        if (pbTemp + 9 <= pbEnd && !memicmp(pbTemp, "@filename", 9))
        {
            return SN;
        }
    }

    do if (dwSize > 0xB6)
    {
        pbTemp = pbFile + 0xB6;

        if (*pbTemp > 0x80)			// 最大魔法数
            break;

        for (BYTE i = 0; i != 3 && pbTemp < pbEnd; ++i)
        {
            if (*pbTemp > 0x12)		// 最大战技数
            {
                bBreak = true;
                break;
            }
            pbTemp += *pbTemp * 0x18 + 1;
        }
        if (bBreak == true || *pbTemp > 0x12)
            break;

        if (pbTemp < pbEnd)
        {
            for (BYTE i = 0, e = *pbTemp++; i != e && pbTemp < pbEnd; ++i)
            {
                pbTemp += 0x1C;
                for (BYTE str = 0; str != 2; ++str)
                    pbTemp += lstrlenA((LPSTR)pbTemp) + 1;
            }
            if (pbTemp - 2 <= pbEnd)
            {
                if (*(WORD *)szFileName != '_T')
                    return MS;
            }
        }
    } while(0);	// check for MS

    if (*(WORD *)szFileName == '_T')
        return DT22;

    return UNKNOWN;
}

void __stdcall ExtractDict(PBYTE *pbDict)
{
    UInt64	outSize64;
    Byte	*inBuffer;
    SizeT	inSize, outSize;

    for (char i = 0; i != countof(Array_of_Data); ++i)
    {
        Lzma86_GetUnpackSize((Byte *)(Array_of_Data[i].data),
            Array_of_Data[i].nSize, &outSize64);

        outSize = (SizeT)outSize64;
        pbDict[i] = (PBYTE)HeapAlloc(hHeap, 0, outSize);

        inSize   = Array_of_Data[i].nSize;
        inBuffer = (Byte *)Array_of_Data[i].data;
        Lzma86_Decode(pbDict[i], &outSize, inBuffer, &inSize);
    }
}