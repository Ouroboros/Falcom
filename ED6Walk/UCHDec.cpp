#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kaede /SECTION:.Kaede,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kaede")
#pragma comment(linker,"/MERGE:.data=.Kaede")
#pragma comment(lib, "ucidec.lib")

#include <Windows.h>
#include <stdio.h>
#include <malloc.h>
#include "getmainargs.h"
#include "my_common.h"

extc int WINAPI UCIDecode(const void *src, int srclen, void** dst, int* stride, int* w, int* h, int* b);
extc int WINAPI UCIFree(void* p);

FORCEINLINE void STDCALL Pixel32To4444(uint_16 *dst, uint_32 src)
{
    *dst  = (uint_16)((src >>  4) & 0xF);
    *dst |= (uint_16)((src >>  8) & 0xF0);
    *dst |= (uint_16)((src >> 12) & 0xF00);
    *dst |= (uint_16)((src >> 16) & 0xF000);
}

int STDCALL BMP32To4444(char *dst, char *src, int width, int height)
{
    char *p = dst;

    for (int h = 0; h != height; ++h)
    {
        for (int w = 0; w != width; ++w)
        {
            Pixel32To4444((uint_16 *)dst, *(uint_32 *)(src + h * 1024 + w * 4));
            dst += 2;
        }
    }

    return dst - p;
}

int STDCALL BMP4444ToCH(char *src, int srclen, char **pCH, uint_32 *pCHSize, char **pCP, uint_32 *pCPSize, DWORD dwAlphaNum)
{
    char *pCPBuf, *pCHBuf, *pBuf, *p1, *p2, *p;
    DWORD sum;
    DWORD dwMaxCPSize, dwMaxCHSize;

    pCHBuf = *pCH;

    dwMaxCHSize = _msize(pCHBuf);
    if ((DWORD)(*pCHSize + srclen) > dwMaxCHSize)
    {
        dwMaxCHSize += srclen;
        *pCH = (char *)realloc(*pCH, dwMaxCHSize);
        pCHBuf = *pCH;
    }
    pCHBuf += *pCHSize;

    if (pCP != NULL)
    {
        pCPBuf = *pCP;
        dwMaxCPSize = _msize(pCPBuf);
        if ((DWORD)(*pCPSize + srclen) > dwMaxCPSize)
        {
            dwMaxCPSize += srclen;
            *pCP = (char *)realloc(*pCP, dwMaxCPSize);
            pCPBuf = *pCP;
        }
        pCPBuf += *pCPSize;
    }

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
                if (pCP != NULL)
                {
                    *(LPWORD)pCPBuf = (WORD)-1;
                    pCPBuf += 2;
                }
            }
            else
            {
                if (pCP != NULL)
                {
                    *(LPWORD)pCPBuf = (WORD)dwAlphaNum;
                    pCPBuf += 2;
                }
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

    if (pCP != NULL)
    {
        *pCPSize = pCPBuf - *pCP;
        ++*(LPWORD)(*pCP);
    }

    return dwAlphaNum;
}

FORCEINLINE void STDCALL main2(int argc, char **argv)
{
    FILE *fp;
    CHAR *pCHBuffer, *pCPBuffer, *pBuffer, *pUCIBuffer, *p4Buffer, *p;
    DWORD dwCHSize, dwCPSize, dwAlphaNum, dwSize, dw4Size;
    int   b, w, h, stride;

    fp = fopen("1.UCH", "rb");
    fseek(fp, 0, SEEK_END);
    dwSize = ftell(fp);
    fseek(fp, 0, SEEK_SET);
    pBuffer = (CHAR *)malloc(dwSize);
    fread(pBuffer, dwSize, 1, fp);
    fclose(fp);
    
    dwCPSize   = 2;
    dwCHSize   = 2;
    dwAlphaNum = 0;
    pUCIBuffer = pBuffer + 3;
    pCPBuffer  = (CHAR *)malloc(0x20002);
    pCHBuffer  = (CHAR *)malloc(0x20002);
    p4Buffer   = (CHAR *)malloc(0x20000);
    
    *(LPDWORD)pCPBuffer = 0;
    *(LPDWORD)pCHBuffer = 0;

    while (*pUCIBuffer)
    {
        UCIDecode(pUCIBuffer, INT_MAX, (void **)&p, &stride, &w, &h, &b);
        dw4Size = BMP32To4444(p4Buffer, p, 256, 256);
        dwAlphaNum = BMP4444ToCH(p4Buffer, dw4Size, &pCHBuffer, &dwCHSize, &pCPBuffer, &dwCPSize, dwAlphaNum);
        UCIFree(p);
        pUCIBuffer += *(LPDWORD)(pUCIBuffer + 0xC) + 0x10;
        pUCIBuffer += *(LPDWORD)pUCIBuffer + 4;
    }

    fp = fopen("1.CH", "wb");
    fwrite(pCHBuffer, dwCHSize, 1, fp);
    fclose(fp);
    fp = fopen("1.CP", "wb");
    fwrite(pCPBuffer, dwCPSize, 1, fp);
    fclose(fp);
    free(pCHBuffer);
    free(pCPBuffer);
    free(p4Buffer);
    free(pBuffer);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
//    if (argc >= 2)
    {
        main2(argc, argv);
    }
    exit(0);
}