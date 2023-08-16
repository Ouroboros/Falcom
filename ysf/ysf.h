#ifndef _CYSF_H_
#define _CYSF_H_

#include <Windows.h>
#include <tchar.h>
#include "my_common.h"
#include "FileDisk.h"

typedef struct
{
    u32  tag;
    u32  files;
    u32  SizeofNames;
    Bool bIsPak;
} TNiHeader;

typedef struct
{
    u32 index;
    u32 size;
    u32 offset;
    u32 unknown;
} TNiIndex;

typedef struct
{
    u32 files;
    TNiIndex *pIndex;
    char **names;
} TMyIndex;

class CYSF
{
public:
    CYSF();
    ~CYSF();

    Bool Open(TCHAR *szIndexFile, TCHAR *szDataFile);
    Void Close();

protected:
    Bool InitIndex();
    Void DecryptIndex(u8 *pbBuffer, u32 dwSize);

    Void* Alloc(u32 dwSize);
    Void* ReAlloc(LPVOID lpMem, u32 dwSize);
    Void  Free(Void *lpMem);

protected:
    HANDLE m_hHeap;
    TMyIndex m_index;
    CFileDisk file;
};

#endif /* _CYSF_H_ */