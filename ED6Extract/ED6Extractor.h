#ifndef _Extractor_h_
#define _Extractor_h_

#include <Windows.h>
#include "my_headers.h"
#include "upk_common.h"

#pragma pack(1)

#define ED6_MAX_DECOMPRESS_SIZE 0x1000000L
#define ED6_DIR_EXTENSION       ".dir"
#define ED6_DAT_EXTENSION       ".dat"

#define ED6_DIR_MAGIC       TAG8('LB D', '\x0\x1ARI')
#define ED6_DIR_MAX_FILE    0xFA0

typedef struct
{
    UInt64 Magic;
    UInt32 FileCount;
    UInt32 Reserve;
} ED6_DIR_FILE_HEADER;

typedef struct
{
    CHAR  FileName[0x10];
    DWORD Size;
    DWORD Unknown[3];
    DWORD Offset;
} ED6_DIR_FILE_ENTRY;

struct MY_ED6_FILE_ENTRY : public MY_FILE_ENTRY_BASE
{
};

#pragma pack()

class CED6Unpacker : public CUnpackerImpl<CED6Unpacker>
{
protected:
    PVoid     m_pvCompressedBuffer, m_pvDecompressBuffer;
    UInt32    m_CompressedBufferSize;
    CFileDisk m_file;

public:
    CED6Unpacker();
    ~CED6Unpacker();

    DEFINE_AUTO_METHOD();

    Bool Open(PCWChar pszFileName);
    Bool GetFileData(SFileInfo *pFileInfo, const MY_FILE_ENTRY_BASE *pBaseEntry);

protected:
    Bool InitIndex(ED6_DIR_FILE_HEADER *pHeader);
    Bool IsUncompressed(PVoid pvBuffer, UInt32 Size);

    static UInt32 CDECL Decompress(PByte *ppbDecomressed, PByte *ppbComressed);
};

#endif /* _Extractor_h_ */