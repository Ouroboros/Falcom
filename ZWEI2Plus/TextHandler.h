#ifndef _TEXTHANDLER_H_
#define _TEXTHANDLER_H_

#include <Windows.h>
#include "my_headers.h"

#pragma pack(1)

typedef struct
{
    DWORD dwHash[4];
    DWORD dwTextLength;
} TTextHeader;

#pragma pack()

class CText
{
public:
    CText();
    ~CText();

    Bool         Init(Void *lpBuffer, DWORD dwBufferSize);
    int          GetText(Void *lpOutBuffer, LPCSTR lpSrcText);
    TTextHeader* RemoveText(LPCSTR lpSrcText);
    Void         Dump(LPSTR *lpFileName);

protected:
    int          GetText(Void *lpOutBuffer, LPCSTR lpSrcText, Bool bRemove);
    TTextHeader* FindTextPos(DWORD dwHash[4], Bool bRemove = False);

protected:
    PBYTE   m_pbBuffer;
    TTextHeader **m_pIndex;
    DWORD   m_dwBufferSize, m_dwKey, m_dwIndexCount, m_dwMaxIndexCount;
    HANDLE  m_hHeap;
};

#endif /* _TEXTHANDLER_H_ */