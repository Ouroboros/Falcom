#include "TextHandler.h"
#include "my_mem.h"
#include "aes.h"
#include "EncryptText/sha2.h"

CText::CText()
{
    m_pbBuffer = NULL;
    m_pIndex   = NULL;
    m_dwBufferSize = 0;
    m_dwIndexCount = 0;
    m_dwMaxIndexCount = 80000;
    m_dwKey = (DWORD)ReadTimeStampCounter();
    m_hHeap = GetProcessHeap();
}

CText::~CText()
{
    if (m_pbBuffer) HeapFree(m_hHeap, 0, m_pbBuffer);
    if (m_pIndex) HeapFree(m_hHeap, 0, m_pIndex);
}

Bool CText::Init(PVoid lpBuffer, DWORD dwBufferSize)
{
    DWORD dwTextLength;
    TTextHeader *h;

    if (dwBufferSize == 0)
        return False;

    m_pbBuffer = (PBYTE)HeapAlloc(m_hHeap, 0, dwBufferSize);
    if (m_pbBuffer == NULL)
        return False;
    m_pIndex = (TTextHeader **)HeapAlloc(m_hHeap, 0, m_dwMaxIndexCount * sizeof(*m_pIndex));
    if (m_pIndex == NULL)
        return False;

    m_dwBufferSize = dwBufferSize;
    memcpy(m_pbBuffer, lpBuffer, dwBufferSize);

    for (DWORD i = 0, j = dwBufferSize; i < j; )
    {
        h = (TTextHeader *)&m_pbBuffer[i];
        dwTextLength = h->dwHash[2] ^ h->dwHash[0] ^ h->dwTextLength;
        if (m_dwIndexCount == m_dwMaxIndexCount)
        {
            TTextHeader **p;
            m_dwMaxIndexCount += m_dwMaxIndexCount / 2;
            p = (TTextHeader **)HeapReAlloc(m_hHeap, 0, m_pIndex, m_dwMaxIndexCount * sizeof(*m_pIndex));
            if (p == NULL)
                return False;
            m_pIndex = p;
        }

        m_pIndex[m_dwIndexCount] = (TTextHeader *)((DWORD)h ^ m_dwKey * (m_dwIndexCount + 1));
        ++m_dwIndexCount;
        i += ((dwTextLength + 3) & ~3) + sizeof(*h);
    }

    return True;
}

int CText::GetText(Void *lpOutBuffer, LPCSTR lpSrcText, Bool bRemove)
{
    PBYTE   pbOutBuffer;
    int     i, j;
    UCHAR   szText[0x400];
    DWORD   dwTextLength, dwHash[4], dwSrcHash[8];
    LPDWORD pdwEncryptText;
    TTextHeader *pHeader;
    aes_encrypt_ctx ctx;

    sha256((PBYTE)lpSrcText, lstrlenA(lpSrcText), (PBYTE)dwSrcHash);
    dwHash[0] = dwSrcHash[0] ^ dwSrcHash[4];
    dwHash[1] = dwSrcHash[1] ^ dwSrcHash[5];
    dwHash[2] = dwSrcHash[2] ^ dwSrcHash[6];
    dwHash[3] = dwSrcHash[3] ^ dwSrcHash[7];

    pHeader = FindTextPos(dwHash);
    if (pHeader == NULL || bRemove)
        return (int)pHeader;

    dwTextLength = pHeader->dwTextLength ^ pHeader->dwHash[0] ^ pHeader->dwHash[2];
    aes_encrypt_key128((PBYTE)&dwSrcHash[4], &ctx);

    pbOutBuffer = szText;
    pdwEncryptText = (LPDWORD)(pHeader + 1);

    for (i = 0, j = dwTextLength; j > 4; j -= 16, i += 4)
    {
        aes_encrypt((PBYTE)dwSrcHash, (PBYTE)dwSrcHash, &ctx);
        *((LPDWORD)pbOutBuffer + 0) = pdwEncryptText[0] ^ dwSrcHash[0];
        *((LPDWORD)pbOutBuffer + 1) = pdwEncryptText[1] ^ dwSrcHash[1];
        *((LPDWORD)pbOutBuffer + 2) = pdwEncryptText[2] ^ dwSrcHash[2];
        *((LPDWORD)pbOutBuffer + 3) = pdwEncryptText[3] ^ dwSrcHash[3];
        dwSrcHash[0] = pdwEncryptText[0];
        dwSrcHash[1] = pdwEncryptText[1];
        dwSrcHash[2] = pdwEncryptText[2];
        dwSrcHash[3] = pdwEncryptText[3];

        pbOutBuffer += 16;
        pdwEncryptText += 4;
    }

    if (j > 0)
    {
        aes_encrypt((PBYTE)dwSrcHash, (PBYTE)dwSrcHash, &ctx);
        *(LPDWORD)pbOutBuffer = pdwEncryptText[0] ^ dwSrcHash[0];
    }

    szText[dwTextLength] = 0;
    memcpy(lpOutBuffer, szText, dwTextLength + 1);

    return dwTextLength;
}

int CText::GetText(Void *lpOutBuffer, LPCSTR lpSrcText)
{
    return GetText(lpOutBuffer, lpSrcText, False);
}

TTextHeader* CText::RemoveText(LPCSTR lpSrcText)
{
    return (TTextHeader *)GetText(NULL, lpSrcText, True);
}

TTextHeader* CText::FindTextPos(DWORD dwHash[4], Bool bRemove /* = False */)
{
    DWORD l, r, m;
    TTextHeader *h;

    l = 0;
    r = m_dwIndexCount;

    while (l < r)
    {
        m = (l + r) / 2;

        h = (TTextHeader *)((u32)m_pIndex[m] ^ m_dwKey * (m + 1));
        if (h == NULL)
            return NULL;
/*
        DWORD i;
        for (i = 0; i != 4; ++i)
        {
            if (h->dwHash[i] < dwHash[i])
            {
                l = m + 1;
                break;
            }
            else if (h->dwHash[i] > dwHash[i])
            {
                r = m;
                break;
            }
        }

        if (i == 4)
            return h;
*/
        if (h->dwHash[0] < dwHash[0])
        {
            l = m + 1;
            continue;
        }
        else if (h->dwHash[0] > dwHash[0])
        {
            r = m;
            continue;
        }

        if (h->dwHash[1] < dwHash[1])
        {
            l = m + 1;
            continue;
        }
        else if (h->dwHash[1] > dwHash[1])
        {
            r = m;
            continue;
        }

        if (h->dwHash[2] < dwHash[2])
        {
            l = m + 1;
            continue;
        }
        else if (h->dwHash[2] > dwHash[2])
        {
            r = m;
            continue;
        }

        if (h->dwHash[3] < dwHash[3])
        {
            l = m + 1;
            continue;
        }
        else if (h->dwHash[3] > dwHash[3])
        {
            r = m;
            continue;
        }

        if (bRemove)
            m_pIndex[m] = NULL;

        return h;

    }

    return NULL;
}