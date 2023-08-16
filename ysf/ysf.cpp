#include "ysf.h"

Void* CYSF::Alloc(u32 dwSize)
{
    return HeapAlloc(m_hHeap, 0, dwSize);
}

Void* CYSF::ReAlloc(LPVOID lpMem, u32 dwSize)
{
    LPVOID lpRealloc =  HeapReAlloc(m_hHeap, 0, lpMem, dwSize);
    
    if (lpRealloc == NULL)
    {
        Free(lpMem);
    }
    
    return lpRealloc;
}

Void CYSF::Free(Void *lpMem)
{
    HeapFree(m_hHeap, 0, lpMem);
}

CYSF::CYSF()
{
    m_hHeap = GetProcessHeap();
    memset(&m_index, 0, sizeof(m_index));
}

CYSF::~CYSF()
{
    Close();
}

Void CYSF::Close()
{
    if (m_index.pIndex)
    {
        Free(m_index.pIndex);
        m_index.pIndex = NULL;
    }
    if (m_index.names)
    {
        Free(m_index.names);
        m_index.names = NULL;
    }

    file.Close();
}

Bool CYSF::Open(TCHAR *szIndexFile, TCHAR *szDataFile)
{
    if (!szIndexFile)
        return False;

    u8  *pbBuffer;
    u32  dwSize, dwIndexSize;
    TNiHeader header;

    if (file.Open(szIndexFile) == False)
        return False;

    if (file.Read(&header, sizeof(header)) == False)
    {
        return False;
    }

    dwIndexSize = header.files * sizeof(TNiIndex);
    dwSize = file.GetSize() - sizeof(header);
    if (header.tag != TAG3('NNI') || dwIndexSize + header.SizeofNames > dwSize)
    {
        return False;
    }

    m_index.names = (char **)Alloc(header.files * sizeof(*m_index.names));
    if (m_index.names == NULL)
        return False;
    
    pbBuffer = (u8 *)Alloc(dwSize);
    if (pbBuffer == NULL)
        return False;

    if (file.Read(pbBuffer, dwSize) == False)
    {
        Free(pbBuffer);
        return False;
    }

    file.Close();
    DecryptIndex(pbBuffer, dwIndexSize);

    m_index.files = header.files;
    m_index.pIndex = (TNiIndex *)pbBuffer;

    pbBuffer += dwIndexSize;
    DecryptIndex(pbBuffer, header.SizeofNames);
    for (u32 i = 0; i != header.files; ++i)
    {
        m_index.names[i] = (char *)pbBuffer;
        while (*pbBuffer++);
    }

    return True;
}

Void CYSF::DecryptIndex(u8 *pbBuffer, u32 dwSize)
{
    u32 seed = 0x7C53F961;

    for (u32 i = 0; i != dwSize; ++i)
        pbBuffer[i] -= (seed *= 0x3D09) >> 16;
}