#include "DWriteRender.h"

static BYTE FontLumaTable[] =
{
    0x00, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
    0x01, 0x01, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02, 0x02,
    0x02, 0x02, 0x02, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03, 0x03,
    0x03, 0x03, 0x03, 0x03, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04,
    0x04, 0x04, 0x04, 0x04, 0x04, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x05,
    0x05, 0x05, 0x05, 0x05, 0x05, 0x05, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06,
    0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x06, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08,
    0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09,
    0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x09, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A,
    0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0A, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B,
    0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0C, 0x0C, 0x0C, 0x0C,
    0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0D, 0x0D, 0x0D,
    0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0D, 0x0E, 0x0E,
    0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0E, 0x0F,
    0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F, 0x0F,
};

VOID DWriteRender::SaveToBmpFile()
{
    HDC dc = this->renderTarget->GetMemoryDC();

    PBYTE buffer;
    HBITMAP bitmap = (HBITMAP)GetCurrentObject(dc, OBJ_BITMAP);
    BITMAP bmp;
    IMAGE_BITMAP_HEADER header;
    BITMAPINFO bmi;

    GetObjectW(bitmap, sizeof(bmp), &bmp);
    InitBitmapHeader(&header, bmp.bmWidth, bmp.bmHeight, bmp.bmBitsPixel);

    bmi.bmiHeader.biSize = sizeof(bmi.bmiHeader);
    bmi.bmiHeader.biWidth = bmp.bmWidth;
    bmi.bmiHeader.biHeight = bmp.bmHeight;
    bmi.bmiHeader.biPlanes = bmp.bmPlanes;
    bmi.bmiHeader.biBitCount = bmp.bmBitsPixel;
    bmi.bmiHeader.biClrUsed = 0;
    bmi.bmiHeader.biCompression = BI_RGB;
    bmi.bmiHeader.biSizeImage = header.FileSize;
    bmi.bmiHeader.biClrImportant = 0;

    buffer = (PBYTE)AllocStack(header.FileSize);

    GetDIBits(dc, bitmap, 0, bmp.bmHeight, buffer, &bmi, DIB_RGB_COLORS);

    NtFileDisk bin;
    bin.Create(L"d:\\desktop\\picture.bmp");
    bin.Write(&header, sizeof(header));
    bin.Write(buffer, header.FileSize);
    bin.Seek(header.FileSize);
    bin.SetEndOfFile();
}

DWriteRender::DWriteRender()
{
    this->renderTarget = nullptr;
    this->renderingParams = nullptr;
    this->fontFace = nullptr;
}

DWriteRender::~DWriteRender()
{
    SafeReleaseT(this->renderTarget);
    SafeReleaseT(this->renderingParams);
    SafeReleaseT(this->fontFace);
}

NTSTATUS DWriteRender::Initialize(PCWSTR FontPath, PCWSTR FaceName, ULONG_PTR FontSize)
{
    NTSTATUS                hr;
    UINT16                  glyphIndice;
    UINT32                  codePoint;
    ID2D1Factory*           factory;
    IDWriteFactory*         dwrite;
    IDWriteGdiInterop*      gdiInterop;
    IDWriteRenderingParams* renderingParams;
    IDWriteFont*            font;
    IDWriteFontFile*        fontFile;

    factory         = nullptr;
    dwrite          = nullptr;
    gdiInterop      = nullptr;
    fontFile        = nullptr;
    font            = nullptr;

    hr = S_OK;

    LOOP_ONCE
    {
        hr = D2D1CreateFactory(D2D1_FACTORY_TYPE_SINGLE_THREADED, &factory);
        FAIL_BREAK(hr);

        factory->GetDesktopDpi(&this->dpiX, &this->dpiY);

        hr = DWriteCreateFactory(DWRITE_FACTORY_TYPE_SHARED, __uuidof(IDWriteFactory), (IUnknown **)&dwrite);
        FAIL_BREAK(hr);

        hr = dwrite->GetGdiInterop(&gdiInterop);
        FAIL_BREAK(hr);

        if (FaceName != nullptr)
        {
            LOGFONTW lf;

            ZeroMemory(&lf, sizeof(lf));

            lf.lfHeight = -PixelsToDipsY(FontSize);
            CopyMemory(lf.lfFaceName, FaceName, sizeof(lf.lfFaceName));

            hr = gdiInterop->CreateFontFromLOGFONT(&lf, &font);
            FAIL_BREAK(hr);

            hr = font->CreateFontFace(&this->fontFace);
            FAIL_BREAK(hr);
        }
        else
        {
            BOOL isSupportedFontType;
            UINT faceCount;
            DWRITE_FONT_FILE_TYPE fontType;
            DWRITE_FONT_FACE_TYPE faceType;

            hr = dwrite->CreateFontFileReference(FontPath, nullptr, &fontFile);
            FAIL_BREAK(hr);

            hr = fontFile->Analyze(&isSupportedFontType, &fontType, &faceType, &faceCount);
            FAIL_BREAK(hr);

            if (isSupportedFontType == FALSE)
            {
                hr = DWRITE_E_FILEFORMAT;
                break;
            }

            hr = dwrite->CreateFontFace(faceType, 1, &fontFile, 0, DWRITE_FONT_SIMULATIONS_NONE, &this->fontFace);
            FAIL_BREAK(hr);
        }

        this->fontEmSize = PixelsToDipsY(FontSize);
        this->fontHeight = FontSize;

        this->fontFace->GetMetrics(&this->fontMetrics);
        this->ratio = this->fontEmSize / this->fontMetrics.designUnitsPerEm;

        codePoint = L'国';
        this->fontFace->GetGlyphIndices(&codePoint, 1, &glyphIndice);
        this->fontFace->GetDesignGlyphMetrics(&glyphIndice, 1, &this->glyphMetrics, FALSE);

        hr = gdiInterop->CreateBitmapRenderTarget(nullptr, FontSize, FontSize * 2, &this->renderTarget);
        FAIL_BREAK(hr);

        hr = dwrite->CreateRenderingParams(&renderingParams);
        FAIL_BREAK(hr);

        hr = dwrite->CreateCustomRenderingParams(
                renderingParams->GetGamma(),
                renderingParams->GetEnhancedContrast(),
                renderingParams->GetClearTypeLevel(),
                DWRITE_PIXEL_GEOMETRY_FLAT,
                DWRITE_RENDERING_MODE_NATURAL_SYMMETRIC,
                &this->renderingParams
            );

        SafeReleaseT(renderingParams);
    }

    SafeReleaseT(fontFile);
    SafeReleaseT(factory);
    SafeReleaseT(dwrite);
    SafeReleaseT(gdiInterop);
    SafeReleaseT(font);

    return hr;
}

NTSTATUS DWriteRender::DrawRenderTarget(UINT16 glyphIndice, PRECT blackBox)
{
    DWRITE_GLYPH_RUN        rune;
    HDC                     dc;
    SIZE                    size;
    FLOAT                   advance;
    DWRITE_GLYPH_METRICS    glyphMetrics;

    this->fontFace->GetDesignGlyphMetrics(&glyphIndice, 1, &glyphMetrics, FALSE);

    advance = glyphMetrics.advanceWidth * this->ratio;

    rune.fontFace       = this->fontFace;
    rune.fontEmSize     = this->fontEmSize;
    rune.glyphCount     = 1;
    rune.glyphIndices   = &glyphIndice;
    rune.glyphAdvances  = &advance;
    rune.glyphOffsets   = nullptr;
    rune.isSideways     = FALSE;
    rune.bidiLevel      = 0;

    dc = this->renderTarget->GetMemoryDC();
    this->renderTarget->GetSize(&size);

    SetDCBrushColor(dc, RGB(0, 0, 0));
    SelectObject(dc, GetStockObject(BLACK_PEN));
    SelectObject(dc, GetStockObject(DC_BRUSH));
    Rectangle(dc, 0, 0, size.cx + 1, size.cy + 1);

    FAIL_RETURN(this->renderTarget->DrawGlyphRun(
        0,
        this->glyphMetrics.verticalOriginY * this->ratio,
        DWRITE_MEASURING_MODE_NATURAL,
        &rune,
        this->renderingParams,
        RGB(255, 255, 255),
        blackBox
    ));

    return STATUS_SUCCESS;
}

NTSTATUS
DWriteRender::
DrawRune(
    WCHAR       ch,
    ULONG_PTR   color,
    PVOID       output,
    ULONG_PTR   outputStride,
    PULONG_PTR  runeWidth
)
{
    UINT32      codePoint;
    UINT16      glyphIndice;
    RECT        blackBox;
    LONG_PTR    stride, width, height, x, y, fontSize;
    PBYTE       outline, out, pixels;
    HDC         dc;
    HBITMAP     bitmap;
    BITMAP      bmp;
    IMAGE_BITMAP_HEADER header;

    BOOL dbg = FALSE;

    //ch = L'。';

    codePoint = ch;
    FAIL_RETURN(this->fontFace->GetGlyphIndices(&codePoint, 1, &glyphIndice));
    FAIL_RETURN(this->DrawRenderTarget(glyphIndice, &blackBox));

    //SaveToBmpFile();
    //return 0;

    if (dbg)
    {
        PrintConsole(L"rawrc = {%d %d %d %d}\n", blackBox);
    }

    dc = this->renderTarget->GetMemoryDC();

    bitmap = (HBITMAP)(HBITMAP)GetCurrentObject(dc, OBJ_BITMAP);
    GetObjectW(bitmap, sizeof(bmp), &bmp);
    InitBitmapHeader(&header, bmp.bmWidth, bmp.bmHeight, bmp.bmBitsPixel, &stride);

    pixels = (PBYTE)AllocStack(header.FileSize);

    GetDIBits(dc, bitmap, 0, bmp.bmHeight, pixels, (PBITMAPINFO)&header.Info, DIB_RGB_COLORS);

    //blackBox.top = ML_MAX(0, blackBox.top);
    //blackBox.left = ML_MAX(0, blackBox.left);
    blackBox.right = ML_MIN(blackBox.right, header.Info.Width);
    blackBox.bottom = ML_MIN(blackBox.bottom, header.Info.Height);

    width = blackBox.right - blackBox.left;
    height = blackBox.bottom - blackBox.top;

    *runeWidth = blackBox.right + abs(blackBox.left);
    *runeWidth = width;

    fontSize = this->fontHeight;

    if (dbg)
    {
        SaveToBmpFile();
        PrintConsole(L"rc = {%d %d %d %d} stride = %d w = %d h = %d fs = %d\n", blackBox, stride, width, height, fontSize);
    }

    outline = (PBYTE)AllocStack(fontSize * fontSize * 2);
    ZeroMemory(outline, fontSize * fontSize);

    pixels += (bmp.bmHeight - 1) * stride;
    out = outline;

    width = fontSize;
    height = fontSize;

    if (blackBox.bottom > fontSize)
    {
        //pixels -= (blackBox.bottom - fontSize) * stride;
    }

    for (LONG_PTR h = height; h != 0; --h)
    {
        COLORREF* i = (COLORREF *)pixels;
        PBYTE o = out;

        for (LONG_PTR w = width; w != 0; ++i, --w)
        {
            *o++ = FontLumaTable[((RGBA_GetRValue(*i) * 19595 + RGBA_GetGValue(*i) * 38469 + RGBA_GetBValue(*i) * 7472) >> 16) & 0xFF];
        }

        pixels -= stride;
        out += fontSize;

        if (o > out)
        {
            ExceptionBox(L"out of range");
            Ps::ExitProcess(0);
        }
    }

    out = (PBYTE)output + outputStride * 1;
    for (LONG_PTR h = fontSize; h != 0; --h)
    {
        PUSHORT o = (PUSHORT)out - 1;
        for (LONG_PTR w = fontSize; w != 0; --w)
        {
            ULONG c = *outline++;

            ++o;
            if (c == 0)
                continue;

            *o = (c << 12) | color;
        }

        out += outputStride;
        if ((PBYTE)o > out)
        {
            ExceptionBox(L"out of range 2");
            Ps::ExitProcess(0);
        }
    }

    return STATUS_SUCCESS;
}
