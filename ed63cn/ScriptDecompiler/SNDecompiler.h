#ifndef _SNDECOMPILER_H_
#define _SNDECOMPILER_H_
#pragma warning(disable:4530)
#pragma warning(disable:4018)

#include <map>
#include <vector>
#include "my_common.h"
#include "FileDisk.h"
#include "Mem.h"

using std::vector;
using std::map;

class CSNDecompiler
{
public:
    enum ESymbol
    {
        ERR_INVALID = -4, 
        ERR_MEM, 
        ERR_IO_SRC,
        ERR_IO_DEST, 
        ERR_NORMAL  = False, 
        ERR_SUCCESS = True, 

        SYM_JMP              = 0x03, 
        SYM_MENU_TITLE_BEGIN = 0x54,
        SYM_MENU_TITLE       = 0x5A,
        SYM_TALK_BEGIN       = 0x5B,
        SYM_TALK_END         = 0x58,
        SYM_MENU_START       = 0x5D,
        SYM_MENU_END         = 0x5E,
        SYM_MENU_TITLE_TEXT  = 0x60,
    };

    enum ESize
    {
        Size_Offset = 0x02, 
        Size_Event  = 0x20, 
        Size_Chip   = 0x04, 
        Size_Ptn    = 0x04, 
    };

private:

#pragma pack(1)

typedef struct
{
    WORD wOffset;
    WORD wCount;
} SEntry;

typedef struct
{
    CHAR   szLocation[0xA];
    CHAR   szModuleName[0xE];
    UCHAR  unknown[8];
    DWORD  dwMainIndex;
    DWORD  dwReferenceIndex[7];
    WORD   wReserve;
    SEntry EntryChip;
    SEntry EntryPtn;
    SEntry EntryUnknown;
    SEntry EntryEvent[3];
    WORD   wEventEndOffset;
    WORD   wEventBeginOffset;
    WORD   wUnknown;
    WORD   wEventIndexOffset;
    WORD   wEventIndexSize;
    BYTE   byUnknown[0x44];
} SSNHeader;

typedef struct
{
    Byte   op;
    UInt32 offset;
    UInt32 next;        // specify the index of the next code for jmp
    Bool   bRefered;
    UInt32 ParamLength;
    PByte  param;
} SCode;

#pragma pack()

private:
    PBYTE m_pbScript;
    DWORD m_dwScriptSize, m_dwLabels;

    FILE *fp;
    CMem  mem;
    CFileDisk file;

public:
    CSNDecompiler();
    ~CSNDecompiler();

    Bool DecompileFile(const char *pszSrcFile, const char *pszDestFile = NULL);

private:
    int   BinToString(LPSTR lpBuffer, DWORD cbBinSize, LPVOID lpBin);
    int   BinToFloat (LPSTR lpBuffer, DWORD cbBinSize, LPVOID lpBin);

    Void  Free();
    Void  Reset();

    Bool  IsScriptValid();
    Void  PrintError(PBYTE pbScript, LPSTR lpFormat, ...);

    Void  DecompileHeader();
    Void  InitLabel();
    Void  DecompileEvent();
    DWORD DecompileCode(PBYTE pbEvent, LPSTR lpBuffer);
    DWORD DecompileCode1E(PBYTE pbEvent, LPSTR lpBuffer);
};

#endif /* _SNDECOMPILER_H_ */