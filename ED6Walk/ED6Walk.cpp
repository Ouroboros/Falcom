#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kaede /SECTION:.Kaede,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kaede")
#pragma comment(linker,"/MERGE:.data=.Kaede")

#include <Windows.h>
#include <stdio.h>
#include <malloc.h>
#include "getmainargs.h"
#include "my_image.h"

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

    for (int h = height; h; )
    {
        --h;
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
    pCPBuf = *pCP;

    dwMaxCHSize = _msize(pCHBuf);
    dwMaxCPSize = _msize(pCPBuf);

    if ((DWORD)(*pCPSize + srclen) > dwMaxCPSize)
    {
        dwMaxCPSize += dwMaxCPSize >> 1;
        *pCP = (char *)realloc(*pCP, dwMaxCPSize);
        pCPBuf = *pCP;
    }
    if ((DWORD)(*pCHSize + srclen) > dwMaxCHSize)
    {
        dwMaxCHSize += dwMaxCHSize >> 1;
        *pCH = (char *)realloc(*pCH, dwMaxCHSize);
        pCHBuf = *pCH;
    }

    pCHBuf += *pCHSize;
    pCPBuf += *pCPSize;

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
                    sum += ((*(PWORD)p2    ) >> 12)
                        + (*(PWORD)(p2 + 2) >> 12)
                        + (*(PWORD)(p2 + 4) >> 12)
                        + (*(PWORD)(p2 + 6) >> 12);
                    p2 += 8;
                }
                p += 512;
            }
            if (!sum)
            {
                *(LPWORD)pCPBuf = (WORD)-1;
                pCPBuf += 2;
            }
            else
            {
                *(LPWORD)pCPBuf = (WORD)dwAlphaNum;
                pCPBuf += 2;
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
    *pCPSize = pCPBuf - *pCP;
    *(LPWORD)(*pCH) = (WORD)dwAlphaNum;
    ++*(LPWORD)(*pCP);

    return dwAlphaNum;
}

FORCEINLINE void STDCALL main2(int argc, char **argv)
{
    BOOL bError;
    FILE *fCH, *fCP, *fsrc;
    CHAR  szFileName[MAX_PATH];
    CHAR *pCPBuffer, *pCHBuffer, *p32Buffer, *p4Buffer;
    DWORD dwCHSize, dwCPSize, dwFrameNum, dwAlphaNum;
    DWORD dwSize, dw4Size;
    TBitMapHeader h;

    bError = FALSE;
    dwFrameNum = 0;
    dwAlphaNum = 0;

    dwCPSize = 2;
    dwCHSize = 2;
    pCHBuffer = (CHAR *)malloc(0x20002);
    pCPBuffer = (CHAR *)malloc(0x20002);
    *(LPDWORD)pCPBuffer = 0;
    *(LPDWORD)pCHBuffer = 0;

    while (1)
    {
        sprintf(szFileName, "%s_%04u.bmp", argv[1], dwFrameNum++);

        fsrc = fopen(szFileName, "rb");
        if (fsrc == NULL)
        {
            break;
        }

        if (fread(&h, sizeof(h), 1, fsrc) != 1)
        {
            printf("Can't read %s\n", szFileName);
            fclose(fsrc);
            break;
        }

        if (h.wTag != 'MB')
        {
            bError;
            printf("%s is not a valid BMP file.\n", szFileName);
            fclose(fsrc);
            break;
        }

        if (h.Info.wBit !=32 || h.Info.dwHeight != 256 || h.Info.dwWidth != 256)
        {
            bError = TRUE;
            printf("Input BMP \"%s\" must be 256x256x32.\n", szFileName);
            fclose(fsrc);
            break;
        }
        fseek(fsrc, 0, SEEK_END);
        dwSize = ftell(fsrc);
        fseek(fsrc, 0, SEEK_SET);

        p32Buffer = (char *)malloc(dwSize);
        fread(p32Buffer, dwSize, 1, fsrc);
        fclose(fsrc);

        dw4Size = (dwSize - 0x36) >> 1;

        p4Buffer = (char *)malloc(dw4Size);
        dwSize = BMP32To4444(p4Buffer, p32Buffer + 0x36, 256, 256);
        free(p32Buffer);

        dwAlphaNum = BMP4444ToCH(p4Buffer, dw4Size, &pCHBuffer, &dwCHSize, &pCPBuffer, &dwCPSize, dwAlphaNum);

        free(p4Buffer);
    }

    if (bError == FALSE)
    {
        dwSize = sprintf(szFileName, "%s._CH");
        fCP = fopen(szFileName, "wb");
        if (fCP)
        {
            szFileName[dwSize - 1] = 'P';
            fCH = fopen(szFileName, "wb");
            if (fCH)
            {
                fwrite(pCPBuffer, dwCPSize, 1, fCP);
                fwrite(pCHBuffer, dwCHSize, 1, fCH);
                fclose(fCH);
            }
            else
            {
                printf("Can't create %s\n", szFileName);
            }
            fclose(fCP);
        }
        else
        {
            printf("Can't create %s\n", szFileName);
        }
    }

    free(pCHBuffer);
    free(pCPBuffer);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    if (argc >= 2)
    {
        main2(argc, argv);
    }
    exit(0);
}