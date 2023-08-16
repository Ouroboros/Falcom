#ifndef _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_
#define _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_

#include "ml.h"
#include <d2d1.h>
#include <dwrite.h>

class DWriteRenderer
{
public:
    DWriteRenderer();
    ~DWriteRenderer();

public:
    NTSTATUS Initialize(PCWSTR FontPath, PCWSTR FaceName, ULONG_PTR FontSize);
    NTSTATUS DrawRune(WCHAR ch, ULONG_PTR Color, PVOID Buffer, ULONG_PTR OutputStride, PULONG_PTR runeWidth);

    template <typename T>
    FLOAT PixelsToDipsX(T x)
    {
        return x * 96.0 / this->dpiX;
    }

    template <typename T>
    FLOAT PixelsToDipsY(T y)
    {
        return y * 96.0 / this->dpiY;
    }

    LONG_PTR DipsToPixelsX(FLOAT x)
    {
        FLOAT pixels = x * this->dpiX * (1 / 96.0);
        return (LONG_PTR)((pixels + 0.5));
    }

    LONG_PTR DipsToPixelsY(FLOAT y)
    {
        FLOAT pixels = y * this->dpiY * (1 / 96.0);
        return (LONG_PTR)((pixels + 0.5));
    }

protected:
    NTSTATUS DrawRenderTarget(UINT16 glyphIndice, PRECT blackBox);
    VOID SaveToBmpFile();

protected:
    IDWriteBitmapRenderTarget*  renderTarget;
    IDWriteRenderingParams*     renderingParams;
    IDWriteFontFace*            fontFace;
    DWRITE_FONT_METRICS         fontMetrics;
    DWRITE_GLYPH_METRICS        glyphMetrics;
    LONG_PTR                    fontHeight;
    FLOAT                       ratio;
    FLOAT                       fontEmSize;
    FLOAT                       dpiX, dpiY;
};

#endif // _DWRITERENDER_H_e14e1038_3d82_475d_96c6_c38253ae4232_
