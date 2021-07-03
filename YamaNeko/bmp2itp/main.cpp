#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#define NRV2E

#include "MyLibrary.cpp"

ML_OVERLOAD_NEW

typedef struct
{
    PBYTE pbInput;
    PBYTE pbOutput;
    ULONG InputSize;
    ULONG OutputSize;

    PBYTE pbBits;
    ULONG BitCount;
    ULONG Bits;

} COMPRESS_INFO;

ULONG SetBit(COMPRESS_INFO *pInfo, ULONG Bit)
{
    ULONG Bits;

    if (pInfo->BitCount == bitsof(USHORT))
    {
        pInfo->BitCount = 0;
        *(PUSHORT)pInfo->pbBits = pInfo->Bits;
        pInfo->Bits = 0;
        pInfo->pbBits = pInfo->pbOutput;
        pInfo->pbOutput += sizeof(USHORT);
    }

    ++pInfo->BitCount;
    Bits = pInfo->Bits;
    Bits = (Bits << 1) | (Bit & 1);
    pInfo->Bits = Bits;

    return Bits;
}

ULONG SetBits(COMPRESS_INFO *pInfo, ULONG Bits, ULONG BitCount)
{
    for (; BitCount; --BitCount)
    {
        SetBit(pInfo, Bits >> (BitCount - 1));
    }

    return Bits;
}

ULONG CompressBlock(PVOID pvOutput, ULONG OutputSize, PVOID pvInput, ULONG InputSize)
{
    BYTE            Window[0x100];
    PBYTE           pbWindow, pbOutput;
    ULONG           WindowPos, b;
    COMPRESS_INFO   Info;

    WindowPos   = 0;
    pbWindow    = Window;
    pbOutput    = (PBYTE)pvOutput + 1;

    Info.pbInput    = (PBYTE)pvInput;
    Info.pbOutput   = pbOutput;
    Info.InputSize  = InputSize;
    Info.OutputSize = OutputSize;

    Info.BitCount   = bitsof(BYTE);
    Info.Bits       = 0;

    SetBit(&Info, 0);
    b = *Info.pbInput++;
    *Info.pbOutput++ = b;

    ++WindowPos;
    *pbWindow++ = b;

    LOOP_FOREVER
    {
        BOOL  bDulpicate;
        ULONG BytesRedundancy;

        bDulpicate = TRUE;
        b = pbWindow[-1];
        BytesRedundancy = 0;
    }

    return 0;
}

ULONG _Compress(PVOID pvOutput, ULONG OutBufferSize, PVOID pvInput, ULONG InputSize)
{
    PBYTE pbOutput, pbInput;
    ULONG CompresseBlockSize, BlockCount, InputBlockSize, OutputBlockSize;

    struct
    {
        ULONG CompressedSize;
        ULONG OriginalSize;
        ULONG BlockCount;
    } *pHeader;

    CompresseBlockSize = 0xE380;
    BlockCount = 0;

    *(PULONG_PTR)&pHeader = (ULONG_PTR)pvOutput;

    pbOutput    = (PBYTE)(pHeader + 1);
    pbInput     = (PBYTE)pvInput;

    pHeader->OriginalSize = InputSize;
    while (InputSize != 0)
    {
        ++BlockCount;
        InputBlockSize      = min(InputSize, CompresseBlockSize);
        OutputBlockSize     = CompressBlock(pbOutput + 2, OutBufferSize - 2, pbInput, InputBlockSize);
        OutBufferSize      += 2;
        *(PUSHORT)pbOutput  = OutputBlockSize;

        OutBufferSize  -= OutputBlockSize;
        pbOutput       += OutputBlockSize;
        pbInput        += InputBlockSize;

        *pbOutput++ = 1;

        InputSize      -= InputBlockSize;
    }

    *pbOutput++ = 0;

    pHeader->BlockCount = BlockCount;
    pHeader->CompressedSize = pbOutput - (PBYTE)pvOutput + sizeof(*pHeader) - sizeof(pHeader->OriginalSize);

    return pHeader->CompressedSize + sizeof(pHeader->OriginalSize);
}

#define UCL_COMPRESS_MAGIC TAG4('UCL4')

ULONG Compress(PVOID pvOutput, ULONG OutBufferSize, PVOID pvInput, ULONG InputSize)
{
    LONG Result;
    ucl_compress_config_t UclConfig;

    struct
    {
        ULONG Magic;
        ULONG CompressedSize;
    } *pHeader;

    FillMemory(&UclConfig, sizeof(UclConfig), (BYTE)-1);
    UclConfig.bb_endian  = 0;
    UclConfig.bb_size    = 32;
    UclConfig.max_offset = 0x3FFFFF;

    *(PULONG_PTR)&pHeader = (ULONG_PTR)pvOutput;
    pHeader->CompressedSize = OutBufferSize - sizeof(*pHeader);

    //PVOID WorkSpace;
    //ULONG CompressBufferWorkSpaceSize, CompressFragmentWorkSpaceSize;
    //RtlGetCompressionWorkSpaceSize(3, &CompressBufferWorkSpaceSize, &CompressFragmentWorkSpaceSize);
    //WorkSpace = AllocateMemoryP(CompressBufferWorkSpaceSize + CompressFragmentWorkSpaceSize);
    //RtlCompressBuffer(COMPRESSION_FORMAT_DEFAULT, pvInput, InputSize, (PUCHAR)(pHeader + 1), OutBufferSize, 0, &pHeader->CompressedSize, WorkSpace);

    Result = UCL_NRV2E_Compress(pvInput, InputSize, pHeader + 1, &pHeader->CompressedSize);

    pHeader->Magic = UCL_COMPRESS_MAGIC;

    return pHeader->CompressedSize + sizeof(*pHeader);
}

#undef UCL_COMPRESS_MAGIC

#pragma pack(1)

typedef struct
{
    ULONG Magic;
    ULONG Width;
    ULONG Height;
} ITP_3E9_HEADER;

#pragma pack()

typedef struct
{
    ULONG Color;
    union
    {
        ULONG RefCount;
        ULONG Index;
    };
} COLOR_REF;

int CDECL compare(COLOR_REF *p1, COLOR_REF *p2)
{
    if (p1->RefCount > p2->RefCount)
        return -1;

    if (p1->RefCount == p2->RefCount)
        return 0;

    return 1;
}

HRESULT InitPaletteColors(COLOR_REF *pColor, PULONG pColorCount, IMAGE_BITMAP_HEADER *pBmp, PVOID pvRaw)
{
    LONG Stride, ColorCount;
    PULONG pRaw, pRawBase;
    COLOR_REF *p;

    ColorCount = 0;
    Stride = (pBmp->Info.Width * pBmp->Info.Bit / 8 + 3) & ~3;

    pRawBase = (PULONG)pvRaw;
    for (ULONG Height = pBmp->Info.Height; Height; --Height)
    {
        pRaw = pRawBase;
        for (ULONG Width = pBmp->Info.Width; Width; --Width)
        {
            LONG  Index;
            ULONG Color;

            Color = *pRaw++;
            Index = 0;
            for (p = pColor; Index != ColorCount; ++Index)
                if (Color == p->Color)
                    break;
                else
                    ++p;

            if (Index == ColorCount)
            {
                p->Color = Color;
                p->RefCount = 1;
                ++ColorCount;
            }
            else
            {
                ++p->RefCount;
            }
        }

        *(PULONG)&pRawBase += Stride;
    }

    qsort(pColor, ColorCount, sizeof(*pColor), (int (__cdecl *)(const void*,const void*))compare);

    p = pColor;
    for (ULONG Index = 0, Count = MY_MIN(ColorCount, 256); Count; --Count)
        p++->Index = Index++;

    if (ColorCount > 256)
    {
        p = pColor + 256;
        for (ULONG Count = ColorCount - 256; Count; ++p, --Count)
        {
            LONG  Diff, NearestIndex;
            ULONG Color = p->Color;
            COLOR_REF *p2 = pColor;

            NearestIndex = 0;
            Diff = 0x7FFFFFFF;
            for (ULONG Count = 256; Count; ++p2, --Count)
            {
                LONG diff2, r, g, b, a;

                diff2 = Color - p2->Color;
                r = GetRValue(diff2);
                g = GetGValue(diff2);
                b = GetBValue(diff2);
                a = diff2 >> 24;

                if (r < 0) r = -r;
                if (g < 0) g = -g;
                if (b < 0) b = -b;
                if (a < 0) a = -a;

                diff2 = r + g + b + a;
                if (diff2 < Diff)
                {
                    Diff = diff2;
                    NearestIndex = p2->Index;
                }
            }

            p->Index = NearestIndex;
        }
    }

    *pColorCount = ColorCount;

    return S_OK;
}

COLOR_REF* FindColorIndex(COLOR_REF *pColor, ULONG ColorCount, ULONG ColorToFind)
{
    for (; ColorCount; ++pColor, --ColorCount)
        if (pColor->Color == ColorToFind)
            return pColor;

    return pColor;
}

HRESULT
GenerateItp3E8(
    PVOID       pvItp,
    PULONG      pFileSize,
    COLOR_REF  *pColor,
    ULONG       ColorCount,
    PVOID       pvRaw,
    LONG        Width,
    LONG        Height,
    LONG        Stride
)
{
    PBYTE           pbBuffer;
    PULONG          pBase, pBmp;
    COLOR_REF      *p;
    ITP_3E9_HEADER *pHeader;

    pbBuffer = (PBYTE)pvItp;
    pHeader  = (ITP_3E9_HEADER *)pbBuffer;

    pHeader->Magic  = 0x3E8;
    pHeader->Width  = Width;
    pHeader->Height = Height;

    pbBuffer = (PBYTE)(pHeader + 1);
//    *(PULONG)pbBuffer = MY_MIN(ColorCount, 256);        // Palette Count
//    pbBuffer += 4;

    p = pColor;
    for (ULONG Count = *(PULONG)&pbBuffer[-4]; Count; --Count)
    {
        *(PULONG)pbBuffer = (Bswap(p->Color) >> 8) | (p->Color & 0xFF000000);
        pbBuffer += 4;
        ++p;
    }

    pBase = (PULONG)((ULONG_PTR)pvRaw + (Height - 1) * Stride);
    for (ULONG h = Height; h; --h)
    {
        pBmp = pBase;
        for (ULONG w = Width; w; --w)
        {
            ULONG Color = *pBmp++;

            p = FindColorIndex(pColor, ColorCount, Color);
            *pbBuffer++ = p->Index;
        }

        *(PULONG)&pBase -= Stride;
    }

    *pFileSize = (ULONG_PTR)pbBuffer - (ULONG_PTR)pvItp;

    return S_OK;
}

HRESULT ConvertBmp32ToItp(PWCHAR pszFileName)
{
    WCHAR szFile[MAX_PATH];
    PVOID pvBitmap, pvItp;
    ULONG FileSize, ColorCount;
    FILE *fp;
    COLOR_REF *pColors;
    IMAGE_BITMAP_HEADER Bmp;

    fp = _wfopen(pszFileName, L"rb");
    if (fp == NULL)
        return TYPE_E_IOERROR;

    fread(&Bmp, sizeof(Bmp), 1, fp);
    if (Bmp.Tag != TAG2('BM') || Bmp.Info.Bit != 32)
    {
        PrintConsoleW(L"%s: 32-bit bmp only\n", pszFileName);
        fclose(fp);
        return TYPE_E_UNSUPFORMAT;
    }

    FileSize = Bmp.FileSize - sizeof(Bmp);
    pvBitmap = new BYTE[FileSize];
    if (pvBitmap == NULL)
    {
        fclose(fp);
        return E_OUTOFMEMORY;
    }

    fread(pvBitmap, FileSize, 1, fp);
    fclose(fp);
/*
    if (Bmp.Info.dwWidth < 0)
        Bmp.Info.dwWidth = -Bmp.Info.dwWidth;
    if (Bmp.Info.dwHeight < 0)
        Bmp.Info.dwHeight = -Bmp.Info.dwHeight;
*/
    pColors = new COLOR_REF[Bmp.Info.Width * Bmp.Info.Height];
    InitPaletteColors(pColors, &ColorCount, &Bmp, pvBitmap);

    //  Header + PaletteCount + Palette + ColorIndex
    FileSize = sizeof(ITP_3E9_HEADER) + sizeof(ULONG) + 256 * sizeof(ULONG) + Bmp.Info.Width * Bmp.Info.Height;
    pvItp = new BYTE[FileSize];

    GenerateItp3E8(
        pvItp,
        &FileSize,
        pColors,
        ColorCount,
        pvBitmap,
        Bmp.Info.Width,
        Bmp.Info.Height,
        (Bmp.Info.Width * Bmp.Info.Bit / 8 + 3) & ~3
    );

    StrCopyW(szFile, pszFileName);
    StrCopyW(findextw(szFile), L".itp");
    fp = _wfopen(szFile, L"wb");
    if (fp != NULL)
    {
        fwrite(pvItp, FileSize, 1, fp);
        fclose(fp);
    }

    delete[] pColors;
    delete[] pvItp;
    delete[] pvBitmap;

    return S_OK;
}

VOID MergeAlpha(PVOID pv8Bit, PVOID pv32Bit)
{
    IMAGE_BITMAP_HEADER *p8, *p32;
    PBYTE   pb8, pb32, pb32Base;
    LONG    Stride, Height, Width;
    PULONG  pPalette;

    p8  = (IMAGE_BITMAP_HEADER *)pv8Bit;
    p32 = (IMAGE_BITMAP_HEADER *)pv32Bit;

    pb8     = (PBYTE)p8 + p8->RawOffset;
    pb32    = (PBYTE)p32 + p32->RawOffset;
    pPalette = (PULONG)(p8 + 1);

    Stride = GetBitmapStride(p32->Info.Width, 32);
    Height = p8->Info.Height;
    Width  = p8->Info.Width;

    pb32Base = pb32 + (Height - 1) * Stride;

    for (LONG h = 0; h != Height; ++h)
    {
        pb32 = pb32Base;
        for (LONG w = 0; w != Width; ++w)
        {
            ULONG Index = *pb8++;

            ULONG Alpha = *(PULONG)pb32 & 0xFF000000;
            ULONG Color = pPalette[Index] & 0x00FFFFFF;

            if (h != 0 && w != 0 && abs((LONG)(Alpha - Color)) > 0x30000000)
            {
                PrintConsoleW(L"x = %d, y = %d\n", w, h);

//                Alpha = *(PULONG)&pb32[-Stride] & 0xFF000000;
//                Color = pPalette[pb8[-Width]] & 0x00FFFFFF;
            }

            pPalette[Index] = Color | Alpha;
            pb32 += 4;
        }

        pb32Base -= Stride;
    }
}

ULONG Pixel32To1555(ULONG src)
{
    ULONG _1555;

    _1555  = (ULONG)((src >>  3) & 0x1F);
    _1555 |= (ULONG)((src >>  6) & 0x3E0);
    _1555 |= (ULONG)((src >>  9) & 0x7C00);
    _1555 |= (ULONG)((src >> 16) & 0x8000);

    return _1555;
}

HRESULT Bitmap32ToItp3E9(PVOID pv32Bit, PVOID pvItp)
{
    LONG    Stride, Width, Height;
    PBYTE   pbItp, pb32Bit, pb32BitBase;
    IMAGE_BITMAP_HEADER *pHeader;

    pHeader = (IMAGE_BITMAP_HEADER *)pv32Bit;
    pbItp   = (PBYTE)pvItp;

    Width   = pHeader->Info.Width;
    Height  = pHeader->Info.Height;

    *(PULONG)&pbItp[0] = 0x3E9;
    *(PULONG)&pbItp[4] = Width;
    *(PULONG)&pbItp[8] = Height;

    pbItp += 0xC;

    LONG w, h;

    Stride      = GetBitmapStride(Width, 32);
    pb32BitBase = (PBYTE)pHeader + pHeader->RawOffset + (Height - 1) * Stride;

    h = Height;
    do
    {
        w = Width;
        pb32Bit = pb32BitBase;

        do
        {
            ULONG Color = *(PULONG)pb32Bit;
            *(PUSHORT)pbItp = Pixel32To1555((Bswap(Color) >> 8) | (Color & 0xFF000000));

            pbItp += 2;
            pb32Bit += 4;

        } while (--w);

        pb32BitBase -= Stride;

    } while (--h);

    return S_OK;
}

#if !defined(BMP_TO_ITC)

ForceInline Void main2(Int argc, WChar **argv)
{
    FILE *fp;
    PVOID pvBuffer, pvOutput, pvCompressed;
    ULONG BufferSize, OutBufferSize, CompressedBufferSize, FileSize, OutSize;
    WCHAR file[MAX_PATH];

    BufferSize              = 0x100000;
    OutBufferSize           = BufferSize;
    CompressedBufferSize    = BufferSize;
    pvBuffer                = AllocateMemoryP(BufferSize);
    pvOutput                = AllocateMemoryP(OutBufferSize);
    pvCompressed            = AllocateMemoryP(CompressedBufferSize);

    while (--argc)
    {
        IMAGE_BITMAP_HEADER *pHeader;

        fp = _wfopen(*++argv, L"rb");
        if (fp == NULL)
            continue;

        FileSize = fsize(fp);
        if (FileSize > BufferSize)
        {
            BufferSize  = FileSize;
            pvBuffer    = ReAllocateMemoryP(pvBuffer, BufferSize);
        }

        fread(pvBuffer, FileSize, 1, fp);
        fclose(fp);

        StrCopyW(file, *argv);
        StrCopyW(findextw(file), L".itp");
        fp = _wfopen(file, L"wb");
        if (fp == NULL)
            continue;

        pHeader = (IMAGE_BITMAP_HEADER *)pvBuffer;

        OutSize  = 4 + sizeof(pHeader->Info.Width) + sizeof(pHeader->Info.Height);
        OutSize += pHeader->Info.Width * pHeader->Info.Height * 2;

        if (OutSize > OutBufferSize)
        {
            OutBufferSize = OutSize;
            pvOutput = ReAllocateMemoryP(pvOutput, OutBufferSize);
        }

        Bitmap32ToItp3E9(pvBuffer, pvOutput);

        if (CompressedBufferSize < OutSize * 4)
        {
            CompressedBufferSize = OutSize * 4;
            pvCompressed = ReAllocateMemoryP(pvCompressed, CompressedBufferSize);
        }

        ITP_3E9_HEADER *pItpHeader = (ITP_3E9_HEADER *)pvOutput;

        OutSize = Compress(
                    pvCompressed,
                    CompressedBufferSize,
                    pItpHeader + 1,
                    OutSize - sizeof(*pItpHeader)
                  );

        fwrite(pItpHeader, sizeof(*pItpHeader), 1, fp);
        fwrite(pvCompressed, OutSize, 1, fp);
        fclose(fp);
    }

    FreeMemoryP(pvBuffer);
    FreeMemoryP(pvOutput);
    FreeMemoryP(pvCompressed);
}

#else

#pragma pack(1)

typedef struct
{
    ULONG Offset;
    ULONG Size;
} ITC_ENTRY;

#pragma pack()

// 1.f

static ULONG ScaleInfo[512] =
{
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000,
    0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000, 0x3F800000
};

ForceInline Void main2(Int argc, WChar **argv)
{
    FILE *fp, *fitc;
    PVOID pvBuffer, pvOutput, pvCompressed;
    ULONG BufferSize, OutBufferSize, CompressedBufferSize, FileSize, OutSize;
    WCHAR file[MAX_PATH];

    ITC_ENTRY Entry[160], *pEntry;

    BufferSize              = 0x100000;
    OutBufferSize           = BufferSize;
    CompressedBufferSize    = BufferSize;
    pvBuffer                = AllocateMemoryP(BufferSize);
    pvOutput                = AllocateMemoryP(OutBufferSize);
    pvCompressed            = AllocateMemoryP(CompressedBufferSize);

    while (--argc)
    {
        ULONG               Header, Offset, Index;
        PWCHAR              pszUnderLine, pszIndex;
        IMAGE_BITMAP_HEADER  *pHeader;

        ++argv;
        pszUnderLine = wcsrchr(*argv, '_');
        if (pszUnderLine == NULL)
            continue;

        CopyMemory(file, *argv, (pszUnderLine - *argv) * sizeof(WCHAR));

        pszIndex    = file + (pszUnderLine - *argv);

        StrCopyW(pszIndex, L".itc");
        fitc = _wfopen(file, L"wb+");
        if (fitc == NULL)
            continue;

        Index   = 0;
        Offset  = sizeof(Header) + sizeof(Entry) + sizeof(ScaleInfo);
        pEntry  = Entry;

        fseek(fitc, Offset, SEEK_SET);
        ZeroMemory(Entry, sizeof(Entry));

        LOOP_FOREVER
        {
            swprintf(pszIndex, L"_%06d.bmp", Index++);
            fp = _wfopen(file, L"rb");
            if (fp == NULL)
                break;

            FileSize = fsize(fp);
            if (FileSize > BufferSize)
            {
                BufferSize  = FileSize;
                pvBuffer    = ReAllocateMemoryP(pvBuffer, BufferSize);
            }

            fread(pvBuffer, FileSize, 1, fp);
            fclose(fp);

            pHeader = (IMAGE_BITMAP_HEADER *)pvBuffer;

            OutSize  = 4 + sizeof(pHeader->Info.dwWidth) + sizeof(pHeader->Info.dwHeight);
            OutSize += pHeader->Info.dwWidth * pHeader->Info.dwHeight * 2;

            if (OutSize > OutBufferSize)
            {
                OutBufferSize = OutSize;
                pvOutput = ReAllocateMemoryP(pvOutput, OutBufferSize);
            }

            Bitmap32ToItp3E9(pvBuffer, pvOutput);

            if (CompressedBufferSize < OutSize * 4)
            {
                CompressedBufferSize = OutSize * 4;
                pvCompressed = ReAllocateMemoryP(pvCompressed, CompressedBufferSize);
            }

            ITP_3E9_HEADER *pItpHeader = (ITP_3E9_HEADER *)pvOutput;

            OutSize = Compress(
                        pvCompressed,
                        CompressedBufferSize,
                        pItpHeader + 1,
                        OutSize - sizeof(*pItpHeader)
                      );

            fwrite(pItpHeader, sizeof(*pItpHeader), 1, fitc);
            fwrite(pvCompressed, OutSize, 1, fitc);

            OutSize += sizeof(*pItpHeader);

            pEntry->Size   = OutSize;
            pEntry->Offset = Offset;
            Offset        += OutSize;
            ++pEntry;
        }

        fseek(fitc, 0, SEEK_SET);

        Header = TAG4('V101');
        fwrite(&Header, 4, 1, fitc);
        fwrite(Entry, sizeof(Entry), 1, fitc);
        fwrite(ScaleInfo, sizeof(ScaleInfo), 1, fitc);
        fclose(fitc);
    }

    FreeMemoryP(pvBuffer);
    FreeMemoryP(pvOutput);
    FreeMemoryP(pvCompressed);
}

#endif

int __cdecl main(Long_Ptr argc, wchar_t **argv)
{
    ml::MlInitialize();
    getargsW(&argc, &argv);
    main2(argc, argv);
    ReleaseArgv(argv);
    Ps::ExitProcess(0);
}

