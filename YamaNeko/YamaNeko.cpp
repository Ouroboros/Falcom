#include "YamaNeko.h"

BOOL CYamaNeko::Open(LPCWSTR pszFileName)
{
    if (!NT_SUCCESS(file.Open(pszFileName)))
        return FALSE;

    UNPACKER_FILE_INFO FileInfo;
    MY_FILE_ENTRY_BASE FileEntry;

    FileEntry.Size.QuadPart     = file.GetSize64();
    FileEntry.Offset.QuadPart   = 0;
    FileEntry.Flags             = 0;

    if (!GetFileData(&FileInfo, &FileEntry))
        return FALSE;

    LPWSTR szFile = FileEntry.FileName;

    wcscpy(FileEntry.FileName, pszFileName);

    if (FileInfo.FileType == UNPACKER_FILE_TYPE_BMP)
    {
        PWChar pszExtension;

        pszExtension = findextw(szFile);
        if (FileInfo.FileNum < 2)
        {
            wcscpy(pszExtension, L".bmp");
            if (NT_SUCCESS(file.Create(szFile)))
            {
                file.Write(FileInfo.BinData.pbBuffer, (ULong)FileInfo.BinData.BufferSize);
            }
        }
        else
        {
            UNPACKER_IMAGE_DATA *pImgData = FileInfo.pImgData;

            for (ULONG Index = 0, Count = (ULONG)FileInfo.FileNum; Count; --Count)
            {
                swprintf(pszExtension, L"_%06d%s", Index, L".bmp");
                if (NT_SUCCESS(file.Create(szFile)))
                {
                    file.Write(pImgData->pbBuffer, (ULONG)pImgData->BufferSize);
                }

                ++pImgData;
                ++Index;
            }
        }
    }

    FreeFileData(&FileInfo);

    return TRUE;
}

BOOL CYamaNeko::GetFileData(UNPACKER_FILE_INFO *pFileInfo, const MY_FILE_ENTRY_BASE *pBaseEntry)
{
    union
    {
        YAMANEKO_ITP_HEADER Itp;
        YAMANEKO_ITC_HEADER Itc;
    } Header;

    HRESULT hResult;

    if (!NT_SUCCESS(file.Read(&Header, sizeof(Header))))
        return FALSE;

    hResult = TYPE_E_UNSUPFORMAT;

    if (Header.Itc.Type == TAG4('V101') || Header.Itc.Type == TAG4('V102'))
    {
        hResult = UnpackItc(&Header.Itc, pFileInfo, pBaseEntry);
    }
    else
    {
        switch (Header.Itp.Type)
        {
            case ITP_TYPE_3E8:
            case ITP_TYPE_3EA:
            case ITP_TYPE_3EC:
            case ITP_TYPE_3ED:
            case ITP_TYPE_3EE:
                hResult = UnpackItp(&Header.Itp, pFileInfo, pBaseEntry);
                break;
        }
    }

    return SUCCEEDED(hResult);
}

HRESULT
CYamaNeko::
UnpackItc(
    YAMANEKO_ITC_HEADER         *pHeader,
    UNPACKER_FILE_INFO          *pFileInfo,
    const MY_FILE_ENTRY_BASE    *pBaseEntry
)
{
    switch (pHeader->Type)
    {
        case YAMANEKO_ITC_V101:
            return UnpackItc_V101(pFileInfo, pBaseEntry);

        case YAMANEKO_ITC_V102:
            return UnpackItc_V102(pFileInfo, pBaseEntry);
    }

    return TYPE_E_UNSUPFORMAT;
}

HRESULT
CYamaNeko::
UnpackItc_V101(
    UNPACKER_FILE_INFO          *pFileInfo,
    const MY_FILE_ENTRY_BASE    *pBaseEntry
)
{
    ULONG               FrameCount;
    HRESULT             hResult;
    Large_Integer       Offset;
    YAMANEKO_ITC_ENTRY *pItcEntry;
    YAMANEKO_ITC_ENTRY  ItcEntry[YAMANEKO_ITC_V101_ENTRY_SIZE / sizeof(YAMANEKO_ITC_ENTRY)];

    hResult = S_OK;
    LOOP_ONCE
    {
        Offset.QuadPart = pBaseEntry->Offset.QuadPart + sizeof(YAMANEKO_ITC_HEADER);
        if (!NT_SUCCESS(file.Seek(Offset.QuadPart, FILE_BEGIN)))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        if (!NT_SUCCESS(file.Read(ItcEntry, sizeof(ItcEntry))))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        FrameCount = 0;
        pItcEntry = ItcEntry;
        for (ULONG Count = countof(ItcEntry); Count; --Count)
        {
            if (pItcEntry->Offset == 0 && pItcEntry->Size == 0)
                break;

            ++pItcEntry;
            ++FrameCount;
        }

        if (FrameCount == 0)
        {
            TYPE_E_UNSUPFORMAT;
            break;
        }

        pFileInfo->FileType = UNPACKER_FILE_TYPE_BMP;
        pFileInfo->FileNum  = FrameCount;
        pFileInfo->pImgData = (UNPACKER_IMAGE_DATA *)Alloc(FrameCount * sizeof(*pFileInfo->pImgData), HEAP_ZERO_MEMORY);
        if (pFileInfo->pImgData == NULL)
        {
            hResult = E_OUTOFMEMORY;
            break;
        }

        UNPACKER_IMAGE_DATA *pImageData;
        MY_FILE_ENTRY_BASE FrameEntry;

        FrameEntry.Flags    = 0;
        pImageData          = pFileInfo->pImgData;
        pItcEntry           = ItcEntry;

        do
        {
            YAMANEKO_ITP_HEADER ItpHeader;
            UNPACKER_FILE_INFO  FrameInfo;

            FrameEntry.Size.QuadPart    = pItcEntry->Size;
            FrameEntry.Offset.QuadPart  = pItcEntry->Offset;

            if (!NT_SUCCESS(file.Seek(FrameEntry.Offset.QuadPart, FILE_BEGIN)))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            if (!NT_SUCCESS(file.Read(&ItpHeader, sizeof(ItpHeader))))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            hResult = UnpackItp(&ItpHeader, &FrameInfo, &FrameEntry);
            if (FAILED(hResult))
                break;

            *pImageData++ = FrameInfo.ImgData;
            ++pItcEntry;

        } while (--FrameCount);
    }

    if (FAILED(hResult))
        FreeFileData(pFileInfo);

    return hResult;
}

HRESULT
CYamaNeko::
UnpackItc_V102(
    UNPACKER_FILE_INFO          *pFileInfo,
    const MY_FILE_ENTRY_BASE    *pBaseEntry
)
{
    ULONG               FrameCount, PaletteCount, Palette[256];
    HRESULT             hResult;
    Large_Integer       Offset;
    YAMANEKO_ITC_ENTRY *pItcEntry;
    YAMANEKO_ITC_ENTRY  ItcEntry[YAMANEKO_ITC_V102_ENTRY_SIZE / sizeof(YAMANEKO_ITC_ENTRY)];

    hResult = S_OK;
    LOOP_ONCE
    {
        Offset.QuadPart = pBaseEntry->Offset.QuadPart + sizeof(YAMANEKO_ITC_HEADER);
        if (!NT_SUCCESS(file.Seek(Offset.QuadPart, FILE_BEGIN)))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        if (!NT_SUCCESS(file.Read(ItcEntry, sizeof(ItcEntry))))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        FrameCount = 0;
        pItcEntry = ItcEntry;
        for (ULONG Count = countof(ItcEntry); Count; --Count)
        {
            if (pItcEntry->Offset == 0 && pItcEntry->Size == 0)
                break;

            ++pItcEntry;
            ++FrameCount;
        }

        if (FrameCount == 0)
        {
            TYPE_E_UNSUPFORMAT;
            break;
        }

        Offset.QuadPart = YAMANEKO_ITC_V102_SCALE_INFO_SIZE;
        if (!NT_SUCCESS(file.Seek(Offset.QuadPart, FILE_BEGIN)))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        if (!NT_SUCCESS(file.Read(&PaletteCount, sizeof(PaletteCount))))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        if (PaletteCount != 0 && !NT_SUCCESS(file.Read(Palette, PaletteCount * sizeof(Palette[0]))))
        {
            hResult = TYPE_E_IOERROR;
            break;
        }

        pFileInfo->FileType = UNPACKER_FILE_TYPE_BMP;
        pFileInfo->FileNum  = FrameCount;
        pFileInfo->pImgData = (UNPACKER_IMAGE_DATA *)Alloc(FrameCount * sizeof(*pFileInfo->pImgData), HEAP_ZERO_MEMORY);
        if (pFileInfo->pImgData == NULL)
        {
            hResult = E_OUTOFMEMORY;
            break;
        }

        UNPACKER_IMAGE_DATA *pImageData;
        MY_FILE_ENTRY_BASE FrameEntry;

        for (ULONG Count = PaletteCount, *p = Palette; Count; ++p, --Count)
            *p = (Bswap(*p) >> 8) | (*p & 0xFF000000);

        FrameEntry.Flags    = 0;
        pImageData          = pFileInfo->pImgData;
        pItcEntry           = ItcEntry;

        do
        {
            YAMANEKO_ITP_HEADER ItpHeader;
            UNPACKER_FILE_INFO  FrameInfo;

            FrameEntry.Size.QuadPart    = pItcEntry->Size;
            FrameEntry.Offset.QuadPart  = pItcEntry->Offset;

            if (!NT_SUCCESS(file.Seek(FrameEntry.Offset.QuadPart, FILE_BEGIN)))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            if (!NT_SUCCESS(file.Read(&ItpHeader, sizeof(ItpHeader))))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            hResult = UnpackItp(&ItpHeader, &FrameInfo, &FrameEntry, PaletteCount != 0 ? Palette : NULL);
            if (FAILED(hResult))
                break;

            *pImageData++ = FrameInfo.ImgData;
            ++pItcEntry;

        } while (--FrameCount);
    }

    if (FAILED(hResult))
        FreeFileData(pFileInfo);

    return hResult;
}

HRESULT
CYamaNeko::
UnpackItp(
    YAMANEKO_ITP_HEADER         *pHeader,
    UNPACKER_FILE_INFO          *pFileInfo,
    const MY_FILE_ENTRY_BASE    *pBaseEntry,
    PULONG                       pExtraPalette /* = NULL*/
)
{
    HRESULT hResult;

    switch (pHeader->Type)
    {
        case ITP_TYPE_3E8:
        case ITP_TYPE_3EA:
        case ITP_TYPE_3EC:
        case ITP_TYPE_3ED:
            hResult = UnpackItp_3E8_3EA_3EC_3ED(pHeader, pFileInfo, pBaseEntry, pExtraPalette);
            break;

        case ITP_TYPE_3EE:
            hResult = UnpackItp_3EE(pHeader, pFileInfo, pBaseEntry, pExtraPalette);
            break;

        default:
            hResult = TYPE_E_UNSUPFORMAT;
            break;
    }

    return hResult;
}

HRESULT
CYamaNeko::
UnpackItp_3E8_3EA_3EC_3ED(
    YAMANEKO_ITP_HEADER         *pHeader,
    UNPACKER_FILE_INFO          *pFileInfo,
    const MY_FILE_ENTRY_BASE    *pBaseEntry,
    PULONG                       pExtraPalette /* = NULL*/
)
{
    PVOID           pvColorIndex, pvBuffer;
    ULONG           PaletteSize, Palette[256], *pPalette;
    ULONG           Type, Width, Height, BufferSize, CompressedPaletteSize, CompressedIndexSize;
    HRESULT         hResult;
    Large_Integer   Offset;
    DECOMPRESS_INFO DecompressInfo;

    Offset.QuadPart = pBaseEntry->Offset.QuadPart + sizeof(YAMANEKO_ITP_HEADER);

    if (!NT_SUCCESS(file.Seek(Offset.QuadPart, FILE_BEGIN)))
        return TYPE_E_IOERROR;

    if (!NT_SUCCESS(file.Read(&Width, sizeof(Width))))
        return TYPE_E_IOERROR;

    if (Width == 0)
    {
        ULONG MetaInfoSize;

        if (!NT_SUCCESS(file.Read(&MetaInfoSize, sizeof(MetaInfoSize))))
            return TYPE_E_IOERROR;

        Offset.QuadPart = MetaInfoSize;
        if (!NT_SUCCESS(file.Seek(Offset.QuadPart, FILE_BEGIN)))
            return TYPE_E_IOERROR;

        if (!NT_SUCCESS(file.Read(&Width, sizeof(Width))))
            return TYPE_E_IOERROR;
    }

    if (!NT_SUCCESS(file.Read(&Height, sizeof(Height))))
        return TYPE_E_IOERROR;

    hResult                 = S_OK;
    pvColorIndex            = NULL;
    pvBuffer                = NULL;
    BufferSize              = 0;
    CompressedIndexSize     = 0;
    CompressedPaletteSize   = 0;
    pPalette                = Palette;
    PaletteSize             = sizeof(Palette);

    Type = pHeader->Type;
    switch (Type)
    {
        case ITP_TYPE_3EC:
        case ITP_TYPE_3ED:
            if (!NT_SUCCESS(file.Read(&PaletteSize, sizeof(PaletteSize))))
                return TYPE_E_IOERROR;

            PaletteSize *= 4;       // count * 4
            if (PaletteSize > sizeof(Palette))
            {
                pPalette = (PULONG)Alloc(PaletteSize);
                if (pPalette == NULL)
                    return E_OUTOFMEMORY;
            }
            else
            {
                PaletteSize = sizeof(Palette);
            }

            NO_BREAK;

        case ITP_TYPE_3EA:
            if (!NT_SUCCESS(file.Read(&CompressedPaletteSize, sizeof(CompressedPaletteSize))))
                return TYPE_E_IOERROR;

            BufferSize = CompressedPaletteSize;
            pvBuffer = Alloc(BufferSize);
            if (pvBuffer == NULL)
                return E_OUTOFMEMORY;
            break;

        case ITP_TYPE_3E8:
            break;

        default:
            return TYPE_E_UNSUPFORMAT;
    }

    if (pExtraPalette != NULL)
        pPalette = pExtraPalette;

    LOOP_ONCE
    {
        INT32 Stride, ColorIndexSize;
        PBYTE pbBitmap;
        IMG_BITMAP_HEADER BmpHeader;

        ColorIndexSize = Width * Height;
        pvColorIndex = Alloc(ColorIndexSize);
        if (pvColorIndex == NULL)
        {
            hResult = E_OUTOFMEMORY;
            break;
        }

        if (Type == ITP_TYPE_3EA ||
            Type == ITP_TYPE_3EC ||
            Type == ITP_TYPE_3ED)
        {
            if (!NT_SUCCESS(file.Read(pvBuffer, CompressedPaletteSize)))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            DecompressInfo.pbInput      = (PBYTE)pvBuffer;
            DecompressInfo.InputSize    = CompressedPaletteSize;
            DecompressInfo.pbOutput     = (PBYTE)pPalette;
            DecompressInfo.OutputSize   = PaletteSize;

            hResult = Uncompress(&DecompressInfo);
            if (FAILED(hResult))
                break;

            if (Type == ITP_TYPE_3ED)
            {
                ULONG OriginalColorIndexSize;
                if (!NT_SUCCESS(file.Read(&OriginalColorIndexSize, sizeof(OriginalColorIndexSize))))
                {
                    hResult = TYPE_E_IOERROR;
                    break;
                }
            }

            if (!NT_SUCCESS(file.Read(&CompressedIndexSize, sizeof(CompressedIndexSize))))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            if (CompressedIndexSize > BufferSize)
            {
                BufferSize = CompressedIndexSize;
                pvBuffer = ReAlloc(pvBuffer, BufferSize);
                if (pvBuffer == NULL)
                {
                    hResult = E_OUTOFMEMORY;
                    break;
                }
            }

            if (!NT_SUCCESS(file.Read(pvBuffer, CompressedIndexSize)))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            DecompressInfo.pbInput      = (PBYTE)pvBuffer;
            DecompressInfo.InputSize    = CompressedIndexSize;
            DecompressInfo.pbOutput     = (PBYTE)pvColorIndex;
            DecompressInfo.OutputSize   = ColorIndexSize;

            hResult = Uncompress(&DecompressInfo);
            if (FAILED(hResult))
                break;

            if (Type == ITP_TYPE_3ED)
            {
                PULONG p = pPalette + 1;

                for (ULONG Count = PaletteSize / sizeof(*pPalette) - 1; Count; ++p, --Count)
                    p[0] += p[-1];

                if (DecompressInfo.OutputSize > BufferSize)
                {
                    BufferSize = DecompressInfo.OutputSize;
                    pvBuffer = ReAlloc(pvBuffer, BufferSize);
                    if (pvBuffer == NULL)
                    {
                        hResult = E_OUTOFMEMORY;
                        break;
                    }
                }

                CopyMemory(pvBuffer, pvColorIndex, DecompressInfo.OutputSize);
                UnknownFuckingFunction(pPalette, pvBuffer, pvColorIndex, Width, Height);
            }

            if (Type == ITP_TYPE_3ED || Type == ITP_TYPE_3EC)
            {
                if (ColorIndexSize > BufferSize)
                {
                    BufferSize = ColorIndexSize;
                    pvBuffer = ReAlloc(pvBuffer, BufferSize);
                    if (pvBuffer == NULL)
                    {
                        hResult = E_OUTOFMEMORY;
                        break;
                    }
                }

                CopyMemory(pvBuffer, pvColorIndex, ColorIndexSize);
                UnknownFunction(pvColorIndex, pvBuffer, Width, Height, 8);
            }
        }
        else if (Type == ITP_TYPE_3E8)
        {
            if (!NT_SUCCESS(file.Read(pPalette, PaletteSize)) ||
                !NT_SUCCESS(file.Read(pvColorIndex, ColorIndexSize)))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }
        }

        InitBitmapHeader(&BmpHeader, Width, Height, 32, &Stride);

        pbBitmap = (PBYTE)Alloc(BmpHeader.dwFileSize);
        if (pbBitmap == NULL)
        {
            hResult = E_OUTOFMEMORY;
            break;
        }

        pFileInfo->FileType             = UNPACKER_FILE_TYPE_BMP;
        pFileInfo->FileNum              = 1;
        pFileInfo->ImgData.pbBuffer     = pbBitmap;
        pFileInfo->ImgData.BufferSize   = BmpHeader.dwFileSize;
        pFileInfo->ImgData.Width        = Width;
        pFileInfo->ImgData.Heigth       = Height;
        pFileInfo->ImgData.BitsPerPixel = 32;

        *(IMG_BITMAP_HEADER *)pbBitmap = BmpHeader;
        pbBitmap += sizeof(BmpHeader);

        Convert256To32Bit(pbBitmap, Width, Height, Stride, pvColorIndex, pPalette);
    }

    if (pPalette != Palette)
        Free(pPalette);

    Free(pvBuffer);
    Free(pvColorIndex);

    if (FAILED(hResult))
        FreeFileData(pFileInfo);

    return hResult;
}

HRESULT
CYamaNeko::
UnpackItp_3EE(
    YAMANEKO_ITP_HEADER         *pHeader,
    UNPACKER_FILE_INFO          *pFileInfo,
    const MY_FILE_ENTRY_BASE    *pBaseEntry,
    PULONG                       pExtraPalette /* = NULL*/
)
{
    HRESULT     hResult;
    ULONG       BitmapSize;
    PVOID       pvCcpi, pvBuffer;
    YAMANEKO_ITP_3EE Itp;

    UNREFERENCED_PARAMETER(pHeader);

    if (!NT_SUCCESS(file.Seek(pBaseEntry->Offset.QuadPart, FILE_BEGIN)))
        return TYPE_E_IOERROR;

    if (!NT_SUCCESS(file.Read(&Itp, sizeof(Itp))))
        return TYPE_E_IOERROR;

    if (Itp.CCPI.Width < 16 || Itp.CCPI.Height < 16)
        return TYPE_E_UNSUPFORMAT;

    pvCcpi = Alloc(Itp.OriginalSize);
    if (pvCcpi == NULL)
        return E_OUTOFMEMORY;

    pvBuffer = NULL;
    hResult  = S_OK;

    LOOP_ONCE
    {
        if (TEST_BITS(Itp.CCPI.Flags, ITP_CCPI_FLAG_COMPRESS))
        {
            ULONG           ComperssedSize;
            DECOMPRESS_INFO Info;

            if (!NT_SUCCESS(file.Read(&ComperssedSize, sizeof(ComperssedSize))))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            pvBuffer = Alloc(ComperssedSize + 0x10, HEAP_ZERO_MEMORY);
            if (pvBuffer == NULL)
            {
                hResult = E_OUTOFMEMORY;
                break;
            }

            if (!NT_SUCCESS(file.Read(pvBuffer, ComperssedSize)))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }

            Info.pbInput    = (PBYTE)pvBuffer;
            Info.pbOutput   = (PBYTE)pvCcpi + sizeof(Itp.CCPI);
            Info.InputSize  = ComperssedSize;
            Info.OutputSize = Itp.OriginalSize - sizeof(Itp.CCPI);

            hResult = Uncompress(&Info);
            if (FAILED(hResult))
                break;
        }
        else
        {
            if (!NT_SUCCESS(file.Read((PBYTE)pvCcpi + sizeof(Itp.CCPI), Itp.OriginalSize - sizeof(Itp.CCPI))))
            {
                hResult = TYPE_E_IOERROR;
                break;
            }
        }

        *(YAMANEKO_ITP_CCPI *)pvCcpi = Itp.CCPI;

        BitmapSize = ((Itp.CCPI.Width * 4 + 3) & ~3) * Itp.CCPI.Height + sizeof(IMG_BITMAP_HEADER);
        pFileInfo->ImgData.pbBuffer = (PBYTE)Alloc(BitmapSize);
        if (pFileInfo->ImgData.pbBuffer == NULL)
        {
            hResult = E_OUTOFMEMORY;
            break;
        }

        pFileInfo->FileType             = UNPACKER_FILE_TYPE_BMP;
        pFileInfo->FileNum              = 1;
        pFileInfo->ImgData.BitsPerPixel = 32;
        pFileInfo->ImgData.BufferSize   = BitmapSize;
        pFileInfo->ImgData.Width        = Itp.CCPI.Width;
        pFileInfo->ImgData.Heigth       = Itp.CCPI.Height;

        hResult = UnpackColorPaletteIndex(
                        (YAMANEKO_ITP_CCPI *)pvCcpi,
                        pExtraPalette == NULL ? (PULONG)((YAMANEKO_ITP_CCPI *)pvCcpi + 1) : pExtraPalette,
                        pFileInfo->ImgData.pbBuffer,
                        BitmapSize
                  );
    }

    Free(pvBuffer);
    Free(pvCcpi);

    if (FAILED(hResult))
        FreeFileData(pFileInfo);

    return hResult;
}

HRESULT
CYamaNeko::
UnpackColorPaletteIndex(
    YAMANEKO_ITP_CCPI  *pCcpi,
    PULONG              pPalette,
    PVOID               pvBitmap,
    ULONG               BitmapSize
)
{
    INT32               Stride;
    PVOID               pvIndexBuffer;
    PBYTE               pbCcpiBuffer, pbBitmap, pbIndex, pbCompressedPalette;
    ULONG               Width, Height, RowStride, ColumnStride, CurRow, CurColumn, NextRow, NextColumn;
//    PULONG              pPalette;
    IMG_BITMAP_HEADER  *pBitMapHeader;
    BYTE                CompressedPalette[0x400 * 4];

    switch (pCcpi->Version)
    {
        case 6:
        case 7:
            break;

        default:
            return TYPE_E_UNSUPFORMAT;
    }

    Width  = pCcpi->Width;
    Height = pCcpi->Height;

    pvIndexBuffer = Alloc(Width * Height);
    if (pvIndexBuffer == NULL)
        return E_OUTOFMEMORY;

//    FillMemory(pvIndexBuffer, Width * Height, -2);

    pBitMapHeader   = (IMG_BITMAP_HEADER *)pvBitmap;
    InitBitmapHeader(pBitMapHeader, Width, Height, 32, &Stride);
    if (pBitMapHeader->dwFileSize > BitmapSize)
    {
        Free(pvIndexBuffer);
        return TYPE_E_BUFFERTOOSMALL;
    }

    if (pCcpi->PalCount != 0)
        pPalette = (PULONG)(pCcpi + 1);

//    pPalette = (PULONG)(pCcpi + 1);
    pbCcpiBuffer = (PBYTE)((PULONG)(pCcpi + 1) + pCcpi->PalCount);
    pbCcpiBuffer += TEST_BITS(pCcpi->Flags, ITP_CCPI_FLAG_CONTAIN_FILE_NAME) ? 8 : 0;

    RowStride       = 1 << pCcpi->RowStrideBit;
    ColumnStride    = 1 << pCcpi->ColumnStrideBit;
    CurRow          = 0;
    NextRow         = min(RowStride, Height);

//    FillMemory(CompressedPalette, sizeof(CompressedPalette), 0xCC);

    for (ULONG HeightCount = (Height + RowStride - 1) / RowStride; HeightCount; --HeightCount)
    {
        CurColumn   = 0;
        NextColumn  = min(ColumnStride, Width);

        for (ULONG WidthCount = (Width + ColumnStride - 1) / ColumnStride; WidthCount; --WidthCount)
        {
            ULONG Length, n = *pbCcpiBuffer++;

            if (pCcpi->Version >= 7)
            {
                PULONG p, p1, p2, p3, p4;

                Length = min(0xFF, n * 4);

                p  = (PULONG)pbCcpiBuffer;
                p1 = (PULONG)CompressedPalette;
                p2 = p1 + n;
                p3 = p2 + n;
                p4 = p3 + n;

                for (LONG Count = n; Count; --Count)
                {
                    ULONG Index, Index2;

                    Index  = *p++;
                    Index2 = SWAP2((ULONG)LOWORD(Index)) | (((ULONG)SWAP2(HIWORD(Index)) << 16));

                    *p1 = Index;
                    *p4 = Bswap(Index);
                    *p2 = Index2;
                    *p3 = Bswap(Index2);

                    ++p1;
                    ++p2;
                    ++p3;
                    ++p4;
                }

                pbCompressedPalette = CompressedPalette;
            }
            else
            {
                pbCompressedPalette = pbCcpiBuffer;
            }

            pbCcpiBuffer += n * 4;
            pbIndex = (PBYTE)((ULONG_PTR)pvIndexBuffer + CurRow * Width + CurColumn);

            for (ULONG Row = CurRow; Row < NextRow; Row += 2)
            {
                for (ULONG Column = CurColumn; Column < NextColumn && Row < NextRow; Column += 2)
                {
                    ULONG IndexCount, Index;
                    PBYTE p;

                    Index = *pbCcpiBuffer;
                    if (Index == 0xFF)
                    {
                        p = pbCompressedPalette + 4 * pbCcpiBuffer[-1];
                        IndexCount = pbCcpiBuffer[1];
                        ++pbCcpiBuffer;
                    }
                    else
                    {
                        p = pbCompressedPalette + Index * 4;
                        IndexCount = 1;
                    }

                    LOOP_FOREVER
                    {
                        if (NextRow - Row == 1)
                        {
                            *pbIndex++ = *p++;
                            if (NextColumn - Column == 1)
                                ++p;
                            else
                                *pbIndex++ = *p++;

                            p += 2;
                        }
                        else if (NextColumn - Column == 1)
                        {
                            pbIndex[0]      = *p++;
                            pbIndex[Width]  = *p++;
                            ++pbIndex;
                            p += 2;
                        }
                        else
                        {
                            pbIndex[0]          = *p++;
                            pbIndex[1]          = *p++;
                            pbIndex[Width]      = *p++;
                            pbIndex[Width + 1]  = *p++;

                            pbIndex += 2;
                        }

                        if (--IndexCount == 0)
                            break;

                        p -= 4;
                        Column += 2;
                        if (Column >= NextColumn)
                        {
                            Column = CurColumn;
                            if (NextRow - Row != 1)
                                pbIndex += 2 * Width - (NextColumn - CurColumn);

                            Row += 2;
                        }
                    }

                    ++pbCcpiBuffer;
                }

                if (NextRow - Row != 1)
                    pbIndex += Width * 2 - (NextColumn - CurColumn);
            }

            CurColumn += ColumnStride;
            NextColumn = min(NextColumn + ColumnStride, Width);
        }

        CurRow += RowStride;
        NextRow = min(NextRow + RowStride, Height);
    }

    pbBitmap = (PBYTE)((ULONG_PTR)pBitMapHeader + pBitMapHeader->dwRawOffset);
    Convert256To32Bit(pbBitmap, Width, Height, Stride, pvIndexBuffer, pPalette);

//    pBitMapHeader->Info.dwHeight = -pBitMapHeader->Info.dwHeight;

    Free(pvIndexBuffer);

    return S_OK;
}

HRESULT
CYamaNeko::
Convert256To32Bit(
    PVOID   pvBuffer,
    LONG    Width,
    LONG    Height,
    LONG    Stride,
    PVOID   pvColorIndex,
    PULONG  pPalette
)
{
    PBYTE pbIndex, pbBitmap;

    pbIndex = (PBYTE)pvColorIndex;
    pbBitmap = (PBYTE)((ULONG_PTR)pvBuffer + (Height - 1) * Stride);

    for (; Height; --Height)
    {
        PULONG p = (PULONG)pbBitmap;

        for (ULONG w = Width; w; --w)
        {
            ULONG Color = pPalette[*pbIndex++];
//            *p++ = RGBA(GetBValue(Color), GetGValue(Color), GetRValue(Color), (Color >> 24));
            *p++ = (Bswap(Color) >> 8) | (Color & 0xFF000000);
        }

        pbBitmap -= Stride;
    }

    return S_OK;
}

HRESULT CYamaNeko::Uncompress(DECOMPRESS_INFO *pInfo)
{
    ULONG   UnpackSize;
    PBYTE   pbInput, pbOutputBase;
    HRESULT hResult;

    hResult             = S_OK;
    pbOutputBase        = pInfo->pbOutput;
    pInfo->UnpackSize   = *(PULONG)pInfo->pbInput;
    pInfo->BlockCount   = *(PULONG)(pInfo->pbInput + 4);

    pInfo->pbInput += 8;

    UnpackSize  = pInfo->UnpackSize;
    pbInput     = pInfo->pbInput;

    for (ULONG Count = pInfo->BlockCount; Count; --Count)
    {
        pInfo->BlockSize = *(PUSHORT)pInfo->pbInput;
        pInfo->pbInput += 2;

        hResult = UncompressBlock(pInfo);
        if (FAILED(hResult))
            break;

        if (UnpackSize <= pInfo->pbOutput - pbOutputBase)
            break;

        if (*pInfo->pbInput++ == 0)
            break;
    }

    pInfo->OutputSize = MY_MIN(pInfo->pbOutput - pbOutputBase, UnpackSize);

    return hResult;
}

ULONG CYamaNeko::GetBit(DECOMPRESS_INFO *pInfo)
{
    ULONG Bit;

    if (pInfo->BitCount == 0)
    {
        pInfo->Bits = *(PUSHORT)pInfo->pbInput;
        pInfo->pbInput += 2;
        pInfo->BitCount = bitsof(USHORT);
    }

    --pInfo->BitCount;
    Bit = pInfo->Bits & 1;
    pInfo->Bits >>= 1;

    return Bit;
}

ULONG CYamaNeko::GetBits(DECOMPRESS_INFO *pInfo, ULONG BitCount)
{
    ULONG Bits = 0;

    for (; BitCount; --BitCount)
        Bits = (Bits << 1) | GetBit(pInfo);

    return Bits;
}

HRESULT CYamaNeko::UncompressBlock(DECOMPRESS_INFO *pInfo)
{
    PBYTE   pbBuffer;
    PBYTE   pbOutputBase, pbOutput;
    HRESULT hResult;

    pInfo->BitCount  = bitsof(BYTE);
    pInfo->Bits      = pInfo->pbInput[1];
    pInfo->pbInput  += 2;

    pbOutput         = pInfo->pbOutput;
    pbOutputBase     = pbOutput;
    hResult          = E_FAIL;

    LOOP_FOREVER
    {
        ULONG BackwardOffset, BytesDuplicate;

        while (GetBit(pInfo) == 0)
        {
            *pbOutput++ = *pInfo->pbInput++;
        }

        if (GetBit(pInfo) == 0)
        {
            BackwardOffset = *pInfo->pbInput++;
        }
        else
        {
            BackwardOffset  = GetBits(pInfo, 5) << 8;
            BackwardOffset |= *pInfo->pbInput++;
            if (BackwardOffset == 0)
            {
                hResult = S_OK;
                break;
            }

            if (BackwardOffset == 1)
            {
                ULONG Length;

                if (GetBit(pInfo) == 0)
                {
                    Length = GetBits(pInfo, 4);
                }
                else
                {
                    Length  = GetBits(pInfo, 4) << 8;
                    Length |= *pInfo->pbInput++;
                }

                Length += 0xE;
                FillMemory(pbOutput, Length, *pInfo->pbInput);
                ++pInfo->pbInput;
                pbOutput += Length;

                continue;
            }
        }

        BytesDuplicate = 0;
        LOOP_ONCE
        {
            if (GetBit(pInfo) != 0)
            {
                BytesDuplicate = 2;
                break;
            }

            if (GetBit(pInfo) != 0)
            {
                BytesDuplicate = 3;
                break;
            }

            if (GetBit(pInfo) != 0)
            {
                BytesDuplicate = 4;
                break;
            }

            if (GetBit(pInfo) != 0)
            {
                BytesDuplicate = 5;
                break;
            }

            if (GetBit(pInfo) == 0)
            {
                BytesDuplicate = *pInfo->pbInput++ + 0xE;
            }
            else
            {
                BytesDuplicate = GetBits(pInfo, 3) + 6;
            }
        }

        if (pbOutput - pbOutputBase > 0x3FFF0 ||
            pbOutput - pbOutputBase > pInfo->OutputSize)
        {
            break;
        }

        pbBuffer = pbOutput - BackwardOffset;
        for (; BytesDuplicate; --BytesDuplicate)
            *pbOutput++ = *pbBuffer++;
    }

    pInfo->pbOutput = pbOutput;

    return hResult;
}

HRESULT
CYamaNeko::
UnknownFuckingFunction(
    PULONG  pPalette,
    PVOID   pvEncodedIndex,
    PVOID   pvOutput,
    LONG    Width,
    LONG    Height
)
{
    int v6;
    int k;
    int Val;
    int v9;
    int v10;
    int l;
    int j;
    int m;
    int v14;
    int ColorIndex;
    int v16;
    LPVOID pIndexPointer;
    LPVOID v18;
    int v19;
    int i;
    int v21;
    int v22;
    size_t *v23;
    int v24;
    void *Dst;
    int v26;
    int v27;
    int pbInput;
    SIZE_T size;
    int Palette;

    Palette = (int)pPalette;
    size = Height * Width >> 7;
    pbInput = (int)pvEncodedIndex;
    if ( Height * Width >> 8 <= 1 )
        v6 = 1;
    else
        v6 = (signed int)size >> 1;
    v27 = v6 + pbInput;
    Dst = pvOutput;
    v24 = pbInput;
    v22 = 0;
    v18 = Alloc(size);
    pIndexPointer = Alloc(4 * size);
    v16 = v27;
    ColorIndex = 0;
    for ( i = 0; i < 256; ++i )                   // find alpha
    {
        if ( !*(PBYTE)(Palette + 4 * i + 3) )
        {
            ColorIndex = i;
            break;
        }
    }
    for ( i = 0; i < (signed int)size; ++i )
    {
        if ( v22 )                                  // low 4 bit
        {
            v19 = *(PBYTE)v24 & 0xF;
            if ( v19 )
                *((PBYTE)v18 + i) = v19 + 1;
            else
                *((PBYTE)v18 + i) = 0;
            v22 = 0;
            ++v24;
        }
        else                                        // high 4 bit first
        {
            v19 = (*(PBYTE)v24 & 0xF0) >> 4;
            if ( v19 )
                *((PBYTE)v18 + i) = v19 + 1;
            else
                *((PBYTE)v18 + i) = 0;
            v22 = 1;
        }
        *((PULONG)pIndexPointer + i) = v16;
        v16 += *((PBYTE)v18 + i);
    }
    v24 = pbInput;
    v14 = *(PBYTE)v16++;
    v26 = v16;
    v23 = (size_t *)v16;
    for ( i = 0; i < (signed int)size; ++i )
    {
        if ( *((PBYTE)v18 + i) )
        {
            v21 = 0;
            if ( v14 )
            {
                if ( v14 == 1 )
                {
                    for ( j = 0; j < 128; ++j )
                    {
                        *(PBYTE)Dst = *(PBYTE)(*(PBYTE)v23 + *((PULONG)pIndexPointer + i));
                        v23 = (size_t *)((char *)v23 + 1);
                        Dst = (char *)Dst + 1;
                    }
                }
                else
                {
                    if ( *(PBYTE)v23 )
                    {
                        if ( *(PBYTE)v23 == 1 )
                        {
                            v23 = (size_t *)((char *)v23 + 1);
                            v9 = 0;
                            for ( k = 0; k < 16; ++k )
                            {
                                v10 = 0;
                                Val = *(PBYTE)(*((PULONG)pIndexPointer + i) + k);
                                while ( *(PBYTE)v23 != 255 )
                                {
                                    if ( v9 )
                                    {
                                        memset((char *)Dst + v10, Val, *(PBYTE)v23);
                                        v10 += *(PBYTE)v23;
                                        v9 = 0;
                                    }
                                    else
                                    {
                                        v10 += *(PBYTE)v23;
                                        v9 = 1;
                                    }
                                    v23 = (size_t *)((char *)v23 + 1);
                                }
                                v23 = (size_t *)((char *)v23 + 1);
                            }
                            Dst = (char *)Dst + 128;
                        }
                    }
                    else
                    {
                        v23 = (size_t *)((char *)v23 + 1);
                        for ( l = 0; l < 128; ++l )
                        {
                            *(PBYTE)Dst = *(PBYTE)(*(PBYTE)v23 + *((PULONG)pIndexPointer + i));
                            v23 = (size_t *)((char *)v23 + 1);
                            Dst = (char *)Dst + 1;
                        }
                    }
                }
            }
            else
            {
                for ( m = 0; m < 128; ++m )
                {
                    if ( v21 )
                    {
                        *(PBYTE)Dst = *(PBYTE)((*(PBYTE)v23 & 0xF) + *((PULONG)pIndexPointer + i));
                        v23 = (size_t *)((char *)v23 + 1);
                        v21 = 0;
                    }
                    else
                    {
                        *(PBYTE)Dst = *(PBYTE)(((*(PBYTE)v23 & 0xF0) >> 4) + *((PULONG)pIndexPointer + i));
                        v21 = 1;
                    }
                    Dst = (char *)Dst + 1;
                }
            }
        }
        else
        {
            memset(Dst, ColorIndex, 0x80u);
            Dst = (char *)Dst + 128;
        }
    }
    Free(v18);
    Free(pIndexPointer);

    return S_OK;
}

HRESULT
CYamaNeko::
UnknownFunction(
    PVOID   pvOutput,
    PVOID   pvInput,
    LONG    Width,
    LONG    Height,
    LONG    BitsPerPixel
)
{
    int v11;
    PBYTE pbOutput;
    PBYTE pbInput;

    if (BitsPerPixel == 16)
        Width /= 2;
    else if (BitsPerPixel == 8)
        Width /= 4;

    pbInput = (PBYTE)pvInput;
    pbOutput = (PBYTE)pvOutput;
    v11 = 0;

    FillMemory(pvOutput, Width * Height, -2);
    for (LONG h = 0; h < Height; h += 8)
    {
        for (LONG w = 0; w < Width; w += 4)
        {
            PBYTE p;

            v11 = w + Width * h;
            p = pbOutput + 4 * v11;

            for (ULONG Count = 8; Count; --Count)
            {
                CopyStruct(p, pbInput, 0x10);
                p       += 4 * Width;
                pbInput += 0x10;
            }
        }
    }

    return S_OK;
}
