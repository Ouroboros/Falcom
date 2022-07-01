#pragma comment(linker, "/ENTRY:main")
#pragma comment(linker, "/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker, "/SECTION:.Asuna,ERW /MERGE:.text=.Asuna")

#include "ml.cpp"

FORCEINLINE void STDCALL Pixel32To4444(USHORT *dst, ULONG src)
{
    *dst  = (USHORT)((src >>  4) & 0xF);
    *dst |= (USHORT)((src >>  8) & 0xF0);
    *dst |= (USHORT)((src >> 12) & 0xF00);
    *dst |= (USHORT)((src >> 16) & 0xF000);
}

int STDCALL BMP32To4444(PBYTE dst, PBYTE src, int width, int height)
{
    PBYTE p = dst;

    for (int h = height; h; )
    {
        --h;
        for (int w = 0; w != width; ++w)
        {
            Pixel32To4444((USHORT *)dst, *(ULONG *)(src + h * 1024 + w * 4));
            dst += 2;
        }
    }

    return dst - p;
}

int STDCALL BMP4444ToCH(PBYTE src, int srclen, PBYTE *pCH, ULONG *pCHSize, PBYTE *pCP, ULONG *pCPSize, DWORD dwAlphaNum)
{
    PBYTE pCPBuf, pCHBuf, pBuf, p1, p2, p;
    DWORD sum;
    DWORD dwMaxCPSize, dwMaxCHSize;

    pCHBuf = *pCH;
    pCPBuf = *pCP;

    dwMaxCHSize = _msize(pCHBuf);
    dwMaxCPSize = _msize(pCPBuf);

    if ((DWORD)(*pCPSize + srclen) > dwMaxCPSize)
    {
        dwMaxCPSize += dwMaxCPSize >> 1;
        *pCP = (PBYTE)realloc(*pCP, dwMaxCPSize);
        pCPBuf = *pCP;
    }
    if ((DWORD)(*pCHSize + srclen) > dwMaxCHSize)
    {
        dwMaxCHSize += dwMaxCHSize >> 1;
        *pCH = (PBYTE)realloc(*pCH, dwMaxCHSize);
        pCHBuf = *pCH;
    }

    pCHBuf += *pCHSize;
    pCPBuf += *pCPSize;

    pBuf = src;
    p1 = src;

    for (int i = 0; i != 16; ++i)
    {
        PBYTE pBak = pBuf;

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

ForceInline VOID main2(LONG_PTR argc, PWSTR *argv)
{
    BOOL bError;
    FILE *fCH, *fCP, *fsrc;
    WCHAR  szFileName[MAX_PATH];
    PBYTE pCPBuffer, pCHBuffer, p32Buffer, p4Buffer;
    DWORD dwCHSize, dwCPSize, dwFrameNum, dwAlphaNum;
    DWORD dwSize, dw4Size;
    IMAGE_BITMAP_HEADER h;

    if (argc < 2)
    {
        wprintf(L"%s ch04250", argv[0]);
        return;
    }

    bError = FALSE;
    dwFrameNum = 0;
    dwAlphaNum = 0;

    dwCPSize = 2;
    dwCHSize = 2;
    pCHBuffer = (PBYTE)malloc(0x20002);
    pCPBuffer = (PBYTE)malloc(0x20002);
    *(LPDWORD)pCPBuffer = 0;
    *(LPDWORD)pCHBuffer = 0;

    while (1)
    {
        swprintf(szFileName, L"%s_%04u.bmp", argv[1], dwFrameNum++);

        fsrc = _wfopen(szFileName, L"rb");
        if (fsrc == NULL)
        {
            break;
        }

        if (fread(&h, sizeof(h), 1, fsrc) != 1)
        {
            wprintf(L"Can't read %s\n", szFileName);
            fclose(fsrc);
            break;
        }

        if (h.Tag != 'MB')
        {
            bError;
            wprintf(L"%s is not a valid BMP file.\n", szFileName);
            fclose(fsrc);
            break;
        }

        if (h.Info.Bit !=32 || h.Info.Height != 256 || h.Info.Width != 256)
        {
            bError = TRUE;
            wprintf(L"Input BMP \"%s\" must be 256x256x32.\n", szFileName);
            fclose(fsrc);
            break;
        }
        fseek(fsrc, 0, SEEK_END);
        dwSize = ftell(fsrc);
        fseek(fsrc, 0, SEEK_SET);

        p32Buffer = (PBYTE)malloc(dwSize);
        fread(p32Buffer, dwSize, 1, fsrc);
        fclose(fsrc);

        dw4Size = (dwSize - 0x36) >> 1;

        p4Buffer = (PBYTE)malloc(dw4Size);
        dwSize = BMP32To4444(p4Buffer, p32Buffer + 0x36, 256, 256);
        free(p32Buffer);

        dwAlphaNum = BMP4444ToCH(p4Buffer, dw4Size, &pCHBuffer, &dwCHSize, &pCPBuffer, &dwCPSize, dwAlphaNum);

        free(p4Buffer);
    }

    if (bError == FALSE)
    {
        swprintf(szFileName, L"%s._CH", argv[1]);
        fCH = _wfopen(szFileName, L"wb");
        if (fCH)
        {
            swprintf(szFileName, L"%sP._CP", argv[1]);
            fCP = _wfopen(szFileName, L"wb");
            if (fCP)
            {
                fwrite(pCPBuffer, dwCPSize, 1, fCP);
                fwrite(pCHBuffer, dwCHSize, 1, fCH);
                fclose(fCP);
            }
            else
            {
                wprintf(L"Can't create %s\n", szFileName);
            }
            fclose(fCH);
        }
        else
        {
            wprintf(L"Can't create %s\n", szFileName);
        }
    }

    free(pCHBuffer);
    free(pCPBuffer);
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}