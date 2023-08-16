#ifndef _YAMANEKO_H_6b905f5b_9bb4_498d_ab28_50d1eaa249e9
#define _YAMANEKO_H_6b905f5b_9bb4_498d_ab28_50d1eaa249e9

#include "pragma_once.h"
#include "my_headers.h"
#include "upk_common.h"

#pragma pack(1)

#define YAMANEKO_CCPI_MAGIC                     TAG4('CCPI')
#define YAMANEKO_ITC_V101                       TAG4('V101')
#define YAMANEKO_ITC_V102                       TAG4('V102')
#define YAMANEKO_ITC_V101_ENTRY_SIZE            0x500
#define YAMANEKO_ITC_V101_SCALE_INFO_SIZE       0x800
#define YAMANEKO_ITC_V102_ENTRY_SIZE            0x500
#define YAMANEKO_ITC_V102_SCALE_INFO_SIZE       0x800

enum
{
    ITP_TYPE_3E8 = 0x3E8,
    ITP_TYPE_3EA = 0x3EA,
    ITP_TYPE_3EC = 0x3EC,
    ITP_TYPE_3ED = 0x3ED,
    ITP_TYPE_3EE = 0x3EE,
};

enum
{
    ITP_FRAME_FILE_NAME_LENGTH = 8,
};

enum
{
    ITP_CCPI_FLAG_CONTAIN_FILE_NAME     = 0x02,
    ITP_CCPI_FLAG_COMPRESS              = 0x80,
};

// Compressed Color Palette Index

struct YAMANEKO_ITP_CCPI
{
    ULONG   Magic;      // YAMANEKO_CCPI_MAGIC
    USHORT  Version;    // 6 or 7
    USHORT  PalCount;
    BYTE    ColumnStrideBit;
    BYTE    RowStrideBit;
    SHORT   Width;
    SHORT   Height;
    BYTE    Unknown;
    BYTE    Flags;
};

typedef struct
{
    ULONG   OriginalSize;
    ULONG   BlockCount;
    BYTE    Data[1];
} *PYAMANEKO_COMPRESS_DATA;

typedef struct
{
    PBYTE pbInput;
    PBYTE pbOutput;
    ULONG InputSize;
    ULONG OutputSize;

    ULONG UnpackSize;
    ULONG BlockCount;

    ULONG BlockSize;
    ULONG BitCount;
    ULONG Bits;

} DECOMPRESS_INFO;

struct YAMANEKO_ITP_HEADER
{
    ULONG Type;
};

struct YAMANEKO_ITP_3E8 : public YAMANEKO_ITP_HEADER
{
};

struct YAMANEKO_ITP_3EA : public YAMANEKO_ITP_HEADER
{
};

struct YAMANEKO_ITP_3EE : public YAMANEKO_ITP_HEADER
{
    ULONG               OriginalSize;
    YAMANEKO_ITP_CCPI   CCPI;
};

struct YAMANEKO_ITC_ENTRY
{
    ULONG Offset;
    ULONG Size;
};

struct YAMANEKO_ITC_HEADER : public YAMANEKO_ITP_HEADER
{
};

#pragma pack()

class CYamaNeko : public CUnpackerImpl<CYamaNeko>
{
protected:
    CNtFileDisk file;

public:
    BOOL Open(LPCWSTR pszFileName);
    BOOL GetFileData(UNPACKER_FILE_INFO *pFileInfo, const MY_FILE_ENTRY_BASE *pBaseEntry);

    HRESULT
    UnpackItp(
        YAMANEKO_ITP_HEADER         *pHeader,
        UNPACKER_FILE_INFO          *pFileInfo,
        const MY_FILE_ENTRY_BASE    *pBaseEntry,
        PULONG                       pExtraPalette = NULL
    );

    HRESULT
    UnpackItc(
        YAMANEKO_ITC_HEADER         *pHeader,
        UNPACKER_FILE_INFO          *pFileInfo,
        const MY_FILE_ENTRY_BASE    *pBaseEntry
    );

protected:
    HRESULT
    UnpackItp_3EE(
        YAMANEKO_ITP_HEADER         *pHeader,
        UNPACKER_FILE_INFO          *pFileInfo,
        const MY_FILE_ENTRY_BASE    *pBaseEntry,
        PULONG                       pExtraPalette = NULL
    );

    HRESULT
    UnpackItp_3E8_3EA_3EC_3ED(
        YAMANEKO_ITP_HEADER         *pHeader,
        UNPACKER_FILE_INFO          *pFileInfo,
        const MY_FILE_ENTRY_BASE    *pBaseEntry,
        PULONG                       pExtraPalette = NULL
    );

    HRESULT UnpackItc_V101(UNPACKER_FILE_INFO *pFileInfo, const MY_FILE_ENTRY_BASE *pBaseEntry);
    HRESULT UnpackItc_V102(UNPACKER_FILE_INFO *pFileInfo, const MY_FILE_ENTRY_BASE *pBaseEntry);

    HRESULT Uncompress(DECOMPRESS_INFO *pInfo);
    HRESULT UncompressBlock(DECOMPRESS_INFO *pInfo);
    ULONG   GetBit(DECOMPRESS_INFO *pInfo);
    ULONG   GetBits(DECOMPRESS_INFO *pInfo, ULONG BitCount);

    HRESULT UnknownFunction(PVOID pvOutput, PVOID pvInput, LONG Width, LONG Height, LONG BitsPerPixel);

    HRESULT
    UnknownFuckingFunction(
        PULONG  pPalette,
        PVOID   pvEncodedIndex,
        PVOID   pvOutput,
        LONG    Width,
        LONG    Height
    );

    HRESULT
    UnpackColorPaletteIndex(
        YAMANEKO_ITP_CCPI  *pCcpi,
        PULONG              pPalette,
        PVOID               pvBitmap,
        ULONG               BitmapSize
    );

    HRESULT
    Convert256To32Bit(
        PVOID   pvBuffer,
        LONG    Width,
        LONG    Height,
        LONG    Stride,
        PVOID   pvColorIndex,
        PULONG  pPalette
    );
};

#endif // _YAMANEKO_H_6b905f5b_9bb4_498d_ab28_50d1eaa249e9
