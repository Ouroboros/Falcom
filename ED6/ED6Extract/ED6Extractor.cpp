#pragma comment(lib, "Shlwapi.lib")

#include "ED6Extractor.h"
#include <Shlwapi.h>

CED6Unpacker::CED6Unpacker()
{
    m_pvCompressedBuffer = NULL;
    m_pvDecompressBuffer = NULL;
}

CED6Unpacker::~CED6Unpacker()
{
    SafeFree(&m_pvCompressedBuffer);
    SafeFree(&m_pvDecompressBuffer);
}

Bool CED6Unpacker::Open(PCWChar pszFileName)
{
    WChar szFile[MAX_PATH], *pszExtension;
    ED6_DIR_FILE_HEADER header;

    lstrcpyW(szFile, pszFileName);
    pszExtension = findextw(szFile);
    lstrcpyW(pszExtension, MAKE_WSTRING(ED6_DIR_EXTENSION));

    if (!m_file.Open(szFile))
        return False;

    if (!m_file.Read(&header, sizeof(header)))
        return False;

    if (header.Magic != ED6_DIR_MAGIC)
        return False;

    if (!InitIndex(&header))
        return False;

    lstrcpyW(pszExtension, MAKE_WSTRING(ED6_DAT_EXTENSION));
    return m_file.Open(szFile);
}

Bool CED6Unpacker::InitIndex(ED6_DIR_FILE_HEADER *pHeader)
{
    Bool                 Result;
    Int32                Size;
    PVoid                pvEntry;
    MY_ED6_FILE_ENTRY   *pEntry;
    ED6_DIR_FILE_ENTRY  *pDirEntry;

    if (pHeader->FileCount == 0)
        return False;

    Size = m_file.GetSize() - sizeof(*pHeader);
    if (Size <= 0)
        return False;

    m_Index.cbEntrySize = sizeof(*pEntry);
    pEntry = (MY_ED6_FILE_ENTRY *)Alloc(pHeader->FileCount * m_Index.cbEntrySize);
    if (pEntry == NULL)
        return False;

    m_Index.pEntry = pEntry;

    pDirEntry = (ED6_DIR_FILE_ENTRY *)Alloc(Size);
    if (pDirEntry == NULL)
        return False;

    pvEntry = pDirEntry;
    Result = False;

    LOOP_ONCE
    {
        if (!m_file.Read(pDirEntry, Size))
            break;

        m_Index.FileCount.QuadPart = 0;
        for (UInt32 Count = Size / sizeof(*pDirEntry); Count; ++pDirEntry, --Count)
        {
            if (pDirEntry->FileName[0] == '/')
                continue;

            Size = MultiByteToWideChar(
                        CP_ACP,
                        0,
                        pDirEntry->FileName,
                        countof(pDirEntry->FileName),
                        pEntry->FileName,
                        countof(pEntry->FileName));

            pEntry->FileName[Size] = 0;
            pEntry->Offset.QuadPart         = pDirEntry->Offset;
            pEntry->Size.QuadPart           = pDirEntry->Size;
            pEntry->CompressedSize.QuadPart = pDirEntry->Size;

            ++m_Index.FileCount.LowPart;
            ++pEntry;
        }

        Result = True;
    }

    Free(pvEntry);

    return Result;
}

Bool CED6Unpacker::GetFileData(SFileInfo *pFileInfo, const MY_FILE_ENTRY_BASE *pBaseEntry)
{
    UInt32              Size;
    PByte               pbBuffer, pbCompressed, pbDecompressed;
    MY_ED6_FILE_ENTRY  *pEntry;

    pEntry = (MY_ED6_FILE_ENTRY *)pBaseEntry;

    if (!m_file.SeekEx(m_file.FILE_SEEK_BEGIN, pEntry->Offset))
        return False;

    if (m_pvCompressedBuffer == NULL)
    {
        m_CompressedBufferSize = pEntry->Size.LowPart;
        m_pvCompressedBuffer = Alloc(m_CompressedBufferSize);
    }
    else if (m_CompressedBufferSize < pEntry->Size.LowPart)
    {
        m_CompressedBufferSize = pEntry->Size.LowPart;
        m_pvCompressedBuffer = ReAlloc(m_pvCompressedBuffer, m_CompressedBufferSize);
    }

    if (m_pvCompressedBuffer == NULL)
        return False;

    if (!m_file.Read(m_pvCompressedBuffer, pEntry->Size.LowPart))
        return False;

    if (m_pvDecompressBuffer == NULL)
    {
        m_pvDecompressBuffer = Alloc(ED6_MAX_DECOMPRESS_SIZE);
        if (m_pvDecompressBuffer == NULL)
            return False;
    }

    if (!IsUncompressed(m_pvCompressedBuffer, pEntry->Size.LowPart))
    {
        pbCompressed    = (PByte)m_pvCompressedBuffer;
        pbDecompressed  = (PByte)m_pvDecompressBuffer;

        Size = Decompress(&pbDecompressed, &pbCompressed);
        pbDecompressed = (PByte)m_pvDecompressBuffer;
    }
    else
    {
        pbDecompressed = (PByte)m_pvCompressedBuffer;
        Size = pEntry->Size.LowPart;
    }

    pbBuffer = (PByte)Alloc(Size);
    if (pbBuffer == NULL)
        return False;

    CopyMemory(pbBuffer, pbDecompressed, Size);

    pFileInfo->FileType             = UNPACKER_FILE_TYPE_BIN;
    pFileInfo->BinData.pbBuffer     = pbBuffer;
    pFileInfo->BinData.BufferSize   = Size;

    return True;
}

Bool CED6Unpacker::IsUncompressed(PVoid pvBuffer, UInt32 Size)
{
    SWaveHeader *pWave;

    if (Size < 4)
        return False;

    pWave = (SWaveHeader *)pvBuffer;
    return pWave->RIFF == TAG4('RIFF') && pWave->fmt == TAG4('fmt ') && pWave->WAVE == TAG4('WAVE');
}

ASM UInt32 CDECL CED6Unpacker::Decompress(PByte *ppbDecomressed, PByte *ppbComressed)
{
    UNREFERENCED_PARAMETER(ppbComressed);
    UNREFERENCED_PARAMETER(ppbDecomressed);
    INLINE_ASM
    {
        sub     esp, 010h
        push    ebx
        mov     ebx, dword ptr [esp+01Ch]
        push    esi
        push    edi
        mov     edi, dword ptr [esp+020h]
        xor     esi, esi
        mov     dword ptr [esp+014h], esi
        mov     eax, dword ptr [edi]
        mov     dword ptr [esp+0Ch], eax
        mov     eax, dword ptr [ebx]
        mov     dword ptr [esp+010h], eax

ed6_win3_0048AD40:

        mov     cx, word ptr [eax]
        add     eax, 2
        mov     word ptr [esp+018h], cx
        mov     edx, dword ptr [esp+018h]
        and     edx, 0FFFFh
        mov     dword ptr [esp+010h], eax
        mov     cl, byte ptr [eax]
        add     esi, edx
        test    cl, cl
        jnz     ed6_win3_0048AD6D
        lea     eax, dword ptr [esp+0Ch]
        push    eax
        call    ed6_win3_0048B070           ;<= Jump/Call 地址无法决定
        jmp     ed6_win3_0048AD77

ed6_win3_0048AD6D:

        lea     ecx, dword ptr [esp+0Ch]
        push    ecx
        call    ed6_win3_0048ADA0           ;<= Jump/Call 地址无法决定

ed6_win3_0048AD77:

        mov     eax, dword ptr [esp+014h]
        add     esp, 4
        inc     esi
        mov     dl, byte ptr [eax]
        inc     eax
        test    dl, dl
        mov     dword ptr [esp+010h], eax
        jnz     ed6_win3_0048AD40
        mov     ecx, dword ptr [esp+0Ch]
        mov     dword ptr [edi], ecx
        pop     edi
        mov     dword ptr [ebx], eax
        mov     eax, dword ptr [esp+010h]
        pop     esi
        pop     ebx
        add     esp, 010h
        ret                                  ;<= Procedure End



ed6_win3_0048B070:                          ;<= Procedure Start

        sub     esp, 010h
        push    ebx
        push    ebp
        mov     ebp, dword ptr [esp+01Ch]
        push    esi
        push    edi
        mov     edi, 4
        mov     eax, dword ptr [ebp+4]
        mov     dword ptr [esp+010h], edi
        mov     dl, 8
        movzx   cx, byte ptr [eax+1]
        add     eax, 2
        mov     word ptr [esp+024h], cx
        mov     dword ptr [ebp+4], eax

ed6_win3_0048B099:

        test    dl, dl
        jnz     ed6_win3_0048B0B7
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B0B7:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        jnz     ed6_win3_0048B0F0
        mov     eax, dword ptr [ebp+4]
        mov     ecx, dword ptr [ebp]
        mov     al, byte ptr [eax]
        mov     byte ptr [ecx], al
        mov     ebx, dword ptr [ebp]
        mov     esi, dword ptr [ebp+4]
        mov     ecx, dword ptr [ebp+8]
        inc     ebx
        inc     esi
        inc     ecx
        inc     edi
        mov     dword ptr [ebp], ebx
        mov     dword ptr [ebp+4], esi
        mov     dword ptr [ebp+8], ecx
        mov     dword ptr [esp+010h], edi
        jmp     ed6_win3_0048B099

ed6_win3_0048B0F0:

        test    dl, dl
        jnz     ed6_win3_0048B10E
        mov     eax, dword ptr [ebp+4]
        mov     dl, 010h
        mov     cx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], cx
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B10E:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        jnz     ed6_win3_0048B13B
        mov     eax, dword ptr [ebp+4]
        movzx   cx, byte ptr [eax]
        inc     eax
        inc     edi
        mov     word ptr [esp+014h], cx
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi
        jmp     ed6_win3_0048B2B3

ed6_win3_0048B13B:

        xor     ecx, ecx
        mov     esi, 5

ed6_win3_0048B142:

        shl     ecx, 1
        test    dl, dl
        jnz     ed6_win3_0048B15E
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        add     edi, 2

ed6_win3_0048B15E:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        add     ecx, eax
        dec     esi
        jnz     ed6_win3_0048B142
        mov     eax, dword ptr [ebp+4]
        mov     dword ptr [esp+010h], edi
        shl     ecx, 8
        movzx   si, byte ptr [eax]
        add     ecx, esi
        inc     eax
        cmp     cx, 1
        mov     dword ptr [ebp+4], eax
        ja      ed6_win3_0048B2AF
        jnz     ed6_win3_0048B6C5
        test    dl, dl
        jnz     ed6_win3_0048B1AC
        mov     cx, word ptr [eax]
        add     eax, 2
        mov     word ptr [esp+024h], cx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        add     edi, 2

ed6_win3_0048B1AC:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        jnz     ed6_win3_0048B1FD
        xor     ecx, ecx
        mov     esi, 4

ed6_win3_0048B1C6:

        shl     ecx, 1
        test    dl, dl
        jnz     ed6_win3_0048B1E2
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        add     edi, 2

ed6_win3_0048B1E2:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        add     ecx, eax
        dec     esi
        jnz     ed6_win3_0048B1C6
        mov     eax, ecx
        lea     ecx, dword ptr [edi+ecx+0Fh]
        jmp     ed6_win3_0048B249

ed6_win3_0048B1FD:

        xor     ecx, ecx
        mov     esi, 4

ed6_win3_0048B204:

        shl     ecx, 1
        test    dl, dl
        jnz     ed6_win3_0048B220
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        add     edi, 2

ed6_win3_0048B220:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        add     ecx, eax
        dec     esi
        jnz     ed6_win3_0048B204
        mov     esi, dword ptr [ebp+4]
        shl     ecx, 8
        movzx   ax, byte ptr [esi]
        add     ecx, eax
        inc     esi
        mov     eax, ecx
        mov     dword ptr [ebp+4], esi
        lea     ecx, dword ptr [edi+eax+010h]

ed6_win3_0048B249:

        mov     esi, dword ptr [ebp+4]
        mov     dword ptr [esp+010h], ecx
        and     eax, 0FFFFh
        mov     edi, dword ptr [ebp]
        mov     cl, byte ptr [esi]
        mov     dword ptr [esp+014h], eax
        mov     byte ptr [esp+018h], cl
        lea     ecx, dword ptr [eax+0Eh]
        mov     eax, dword ptr [esp+018h]
        inc     esi
        and     eax, 0FFh
        mov     dword ptr [ebp+4], esi
        mov     bl, al
        mov     esi, ecx
        mov     bh, bl
        mov     eax, ebx
        shl     eax, 010h
        mov     ax, bx
        shr     ecx, 2
        rep     stos dword ptr es:[edi]
        mov     ecx, esi
        and     ecx, 3
        rep     stos byte ptr es:[edi]
        mov     eax, dword ptr [esp+014h]
        mov     esi, dword ptr [ebp]
        mov     edi, dword ptr [esp+010h]
        lea     ecx, dword ptr [eax+0Eh]
        add     eax, 0Eh
        add     esi, ecx
        mov     ecx, dword ptr [ebp+8]
        add     ecx, eax
        mov     dword ptr [ebp], esi
        mov     dword ptr [ebp+8], ecx
        jmp     ed6_win3_0048B099

ed6_win3_0048B2AF:

        mov     dword ptr [esp+014h], ecx

ed6_win3_0048B2B3:

        mov     ebx, dword ptr [ebp]
        mov     ecx, dword ptr [esp+014h]
        and     ecx, 0FFFFh
        mov     esi, ebx
        sub     esi, ecx
        mov     dword ptr [esp+01Ch], ebx
        test    dl, dl
        jnz     ed6_win3_0048B2E3
        mov     dx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B2E3:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        je      ed6_win3_0048B339
        mov     eax, 2
        cmp     word ptr [esp+014h], ax
        jb      ed6_win3_0048B31E
        mov     cx, word ptr [esi]
        mov     word ptr [ebx], cx
        mov     ecx, dword ptr [ebp]
        add     ecx, eax
        mov     eax, dword ptr [ebp+8]
        add     eax, 2
        mov     dword ptr [ebp], ecx
        mov     dword ptr [ebp+8], eax
        jmp     ed6_win3_0048B099

ed6_win3_0048B31E:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     eax
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B31E
        add     dword ptr [ebp+8], 2
        jmp     ed6_win3_0048B099

ed6_win3_0048B339:

        test    dl, dl
        jnz     ed6_win3_0048B357
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B357:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        je      ed6_win3_0048B3B8
        cmp     word ptr [esp+014h], 2
        jb      ed6_win3_0048B398
        mov     ax, word ptr [esi]
        mov     word ptr [ebx], ax
        mov     ecx, dword ptr [ebp]
        mov     al, byte ptr [esi+2]
        mov     byte ptr [ecx+2], al
        mov     eax, dword ptr [ebp]
        add     eax, 3
        mov     dword ptr [ebp], eax
        mov     eax, dword ptr [ebp+8]
        add     eax, 3
        mov     dword ptr [ebp+8], eax
        jmp     ed6_win3_0048B099

ed6_win3_0048B398:

        mov     eax, 3

ed6_win3_0048B39D:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     eax
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B39D
        add     dword ptr [ebp+8], 3
        jmp     ed6_win3_0048B099

ed6_win3_0048B3B8:

        test    dl, dl
        jnz     ed6_win3_0048B3D6
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B3D6:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        je      ed6_win3_0048B42A
        mov     eax, 4
        cmp     word ptr [esp+014h], ax
        jb      ed6_win3_0048B40F
        mov     ecx, dword ptr [esi]
        mov     dword ptr [ebx], ecx
        mov     ecx, dword ptr [ebp]
        add     ecx, eax
        mov     eax, dword ptr [ebp+8]
        add     eax, 4
        mov     dword ptr [ebp], ecx
        mov     dword ptr [ebp+8], eax
        jmp     ed6_win3_0048B099

ed6_win3_0048B40F:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     eax
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B40F
        add     dword ptr [ebp+8], 4
        jmp     ed6_win3_0048B099

ed6_win3_0048B42A:

        test    dl, dl
        jnz     ed6_win3_0048B448
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B448:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        je      ed6_win3_0048B4A5
        mov     eax, 5
        cmp     word ptr [esp+014h], ax
        jb      ed6_win3_0048B48A
        mov     ecx, dword ptr [esi]
        mov     dword ptr [ebx], ecx
        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi+4]
        mov     byte ptr [ecx+4], bl
        mov     ecx, dword ptr [ebp]
        add     ecx, eax
        mov     eax, dword ptr [ebp+8]
        add     eax, 5
        mov     dword ptr [ebp], ecx
        mov     dword ptr [ebp+8], eax
        jmp     ed6_win3_0048B099

ed6_win3_0048B48A:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     eax
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B48A
        add     dword ptr [ebp+8], 5
        jmp     ed6_win3_0048B099

ed6_win3_0048B4A5:

        test    dl, dl
        jnz     ed6_win3_0048B4C3
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        add     edi, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        mov     dword ptr [esp+010h], edi

ed6_win3_0048B4C3:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        test    ax, ax
        jnz     ed6_win3_0048B5AA
        mov     ecx, dword ptr [ebp+4]
        movzx   ax, byte ptr [ecx]
        inc     ecx
        add     eax, 0Eh
        inc     edi
        cmp     word ptr [esp+014h], ax
        mov     dword ptr [ebp+4], ecx
        mov     dword ptr [esp+010h], edi
        jb      ed6_win3_0048B502
        and     eax, 0FFFFh
        mov     edi, ebx
        mov     ecx, eax
        jmp     ed6_win3_0048B606

ed6_win3_0048B502:

        cmp     word ptr [esp+014h], 4
        jb      ed6_win3_0048B583
        and     eax, 0FFFFh
        mov     ecx, eax
        shr     ecx, 4
        mov     ebx, ecx
        dec     ecx
        test    ebx, ebx
        jbe     ed6_win3_0048B551
        inc     ecx

ed6_win3_0048B51C:

        mov     edi, dword ptr [ebp]
        mov     ebx, dword ptr [esi]
        add     esi, 010h
        mov     dword ptr [edi], ebx
        mov     edi, dword ptr [ebp]
        mov     ebx, dword ptr [esi-0Ch]
        mov     dword ptr [edi+4], ebx
        mov     edi, dword ptr [ebp]
        mov     ebx, dword ptr [esi-8]
        mov     dword ptr [edi+8], ebx
        mov     edi, dword ptr [ebp]
        mov     ebx, dword ptr [esi-4]
        mov     dword ptr [edi+0Ch], ebx
        mov     edi, dword ptr [ebp]
        add     edi, 010h
        dec     ecx
        mov     dword ptr [ebp], edi
        jnz     ed6_win3_0048B51C
        mov     edi, dword ptr [esp+010h]

ed6_win3_0048B551:

        mov     ecx, eax
        and     ecx, 0Fh
        mov     ebx, ecx
        dec     ecx
        test    ebx, ebx
        jbe     ed6_win3_0048B5A2
        lea     edi, dword ptr [ecx+1]

ed6_win3_0048B560:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     edi
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B560
        mov     ecx, dword ptr [ebp+8]
        mov     edi, dword ptr [esp+010h]
        add     ecx, eax
        mov     dword ptr [ebp+8], ecx
        jmp     ed6_win3_0048B099

ed6_win3_0048B583:

        and     eax, 0FFFFh
        jbe     ed6_win3_0048B5A2
        mov     edi, eax

ed6_win3_0048B58C:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     edi
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B58C
        mov     edi, dword ptr [esp+010h]

ed6_win3_0048B5A2:

        add     dword ptr [ebp+8], eax
        jmp     ed6_win3_0048B099

ed6_win3_0048B5AA:

        xor     ecx, ecx
        mov     dword ptr [esp+010h], 3

ed6_win3_0048B5B4:

        shl     ecx, 1
        test    dl, dl
        jnz     ed6_win3_0048B5D0
        mov     eax, dword ptr [ebp+4]
        mov     dx, word ptr [eax]
        add     eax, 2
        mov     word ptr [esp+024h], dx
        mov     dl, 010h
        mov     dword ptr [ebp+4], eax
        add     edi, 2

ed6_win3_0048B5D0:

        mov     al, byte ptr [esp+024h]
        shr     word ptr [esp+024h], 1
        and     eax, 1
        dec     dl
        add     ecx, eax
        mov     eax, dword ptr [esp+010h]
        dec     eax
        mov     dword ptr [esp+010h], eax
        jnz     ed6_win3_0048B5B4
        lea     eax, dword ptr [ecx+6]
        mov     ecx, dword ptr [esp+014h]
        cmp     cx, ax
        mov     dword ptr [esp+010h], edi
        jb      ed6_win3_0048B62D
        mov     edi, dword ptr [esp+01Ch]
        and     eax, 0FFFFh
        mov     ecx, eax

ed6_win3_0048B606:

        mov     ebx, ecx
        shr     ecx, 2
        rep     movs dword ptr es:[edi], dword ptr [esi]
        mov     ecx, ebx
        and     ecx, 3
        rep     movs byte ptr es:[edi], byte ptr [esi]
        mov     ecx, dword ptr [ebp]
        mov     edi, dword ptr [esp+010h]
        add     ecx, eax
        mov     dword ptr [ebp], ecx
        mov     ecx, dword ptr [ebp+8]
        add     ecx, eax
        mov     dword ptr [ebp+8], ecx
        jmp     ed6_win3_0048B099

ed6_win3_0048B62D:

        cmp     cx, 4
        jb      ed6_win3_0048B695
        and     eax, 0FFFFh
        mov     ecx, eax
        shr     ecx, 2
        mov     ebx, ecx
        dec     ecx
        test    ebx, ebx
        jbe     ed6_win3_0048B65F
        inc     ecx

ed6_win3_0048B645:

        mov     edi, dword ptr [ebp]
        mov     ebx, dword ptr [esi]
        add     esi, 4
        mov     dword ptr [edi], ebx
        mov     edi, dword ptr [ebp]
        add     edi, 4
        dec     ecx
        mov     dword ptr [ebp], edi
        jnz     ed6_win3_0048B645
        mov     edi, dword ptr [esp+010h]

ed6_win3_0048B65F:

        mov     ecx, eax
        and     ecx, 3
        mov     ebx, ecx
        dec     ecx
        test    ebx, ebx
        jbe     ed6_win3_0048B5A2
        lea     edi, dword ptr [ecx+1]

ed6_win3_0048B672:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     edi
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B672
        mov     ecx, dword ptr [ebp+8]
        mov     edi, dword ptr [esp+010h]
        add     ecx, eax
        mov     dword ptr [ebp+8], ecx
        jmp     ed6_win3_0048B099

ed6_win3_0048B695:

        and     eax, 0FFFFh
        jbe     ed6_win3_0048B5A2
        mov     edi, eax

ed6_win3_0048B6A2:

        mov     ecx, dword ptr [ebp]
        mov     bl, byte ptr [esi]
        mov     byte ptr [ecx], bl
        mov     ecx, dword ptr [ebp]
        inc     ecx
        inc     esi
        dec     edi
        mov     dword ptr [ebp], ecx
        jnz     ed6_win3_0048B6A2
        mov     ecx, dword ptr [ebp+8]
        mov     edi, dword ptr [esp+010h]
        add     ecx, eax
        mov     dword ptr [ebp+8], ecx
        jmp     ed6_win3_0048B099

ed6_win3_0048B6C5:

        pop     edi
        pop     esi
        pop     ebp
        pop     ebx
        add     esp, 010h
        ret                                  ;<= Procedure End


ed6_win3_0048ADA0:                          ;<= Procedure Start

        sub     esp, 8
        push    ebx
        push    ebp
        mov     ebp, dword ptr [esp+014h]
        push    esi
        push    edi
        mov     ebx, 2

ed6_win3_0048ADB0:

        cmp     word ptr [ebp+0Ch], bx
        je      ed6_win3_0048B05D
        mov     esi, dword ptr [ebp+4]
        mov     al, byte ptr [esi]
        inc     esi
        inc     ebx
        mov     dword ptr [ebp+4], esi
        test    al, 080h
        je      ed6_win3_0048AEF2
        movzx   dx, byte ptr [esi]
        mov     cl, al
        and     cl, 01Fh
        movzx   cx, cl
        shl     ecx, 8
        add     ecx, edx
        lea     edx, dword ptr [esi+1]
        mov     esi, dword ptr [ebp]
        mov     edi, ecx
        and     edi, 0FFFFh
        mov     dword ptr [ebp+4], edx
        shr     eax, 5
        sub     esi, edi
        and     eax, 3
        inc     ebx
        add     eax, 4
        cmp     word ptr [ebp+0Ch], bx
        mov     dword ptr [esp+01Ch], eax
        je      ed6_win3_0048AE2E
        mov     dl, byte ptr [edx]
        mov     al, dl
        and     al, 0E0h
        cmp     al, 060h
        jnz     ed6_win3_0048AE2E

ed6_win3_0048AE0F:

        mov     eax, dword ptr [esp+01Ch]
        and     edx, 01Fh
        add     eax, edx
        mov     dword ptr [esp+01Ch], eax
        mov     eax, dword ptr [ebp+4]
        inc     eax
        inc     ebx
        mov     dword ptr [ebp+4], eax
        mov     dl, byte ptr [eax]
        mov     al, dl
        and     al, 0E0h
        cmp     al, 060h
        je      ed6_win3_0048AE0F

ed6_win3_0048AE2E:

        mov     eax, dword ptr [esp+01Ch]
        mov     edx, dword ptr [ebp+8]
        add     edx, eax
        cmp     edi, eax
        mov     dword ptr [ebp+8], edx
        jb      ed6_win3_0048AE59
        mov     edi, dword ptr [ebp]
        mov     ecx, eax
        mov     edx, ecx
        shr     ecx, 2
        rep     movs dword ptr es:[edi], dword ptr [esi]
        mov     ecx, edx
        and     ecx, 3
        rep     movs byte ptr es:[edi], byte ptr [esi]
        add     dword ptr [ebp], eax
        jmp     ed6_win3_0048AEE3

ed6_win3_0048AE59:

        cmp     cx, 4
        jb      ed6_win3_0048AECD
        cdq
        and     edx, 0Fh
        add     eax, edx
        sar     eax, 4
        mov     ecx, eax
        dec     eax
        test    ecx, ecx
        jle     ed6_win3_0048AEA1
        inc     eax

ed6_win3_0048AE70:

        mov     edx, dword ptr [ebp]
        mov     ecx, dword ptr [esi]
        add     esi, 010h
        mov     dword ptr [edx], ecx
        mov     edx, dword ptr [ebp]
        mov     ecx, dword ptr [esi-0Ch]
        mov     dword ptr [edx+4], ecx
        mov     edx, dword ptr [ebp]
        mov     ecx, dword ptr [esi-8]
        mov     dword ptr [edx+8], ecx
        mov     edx, dword ptr [ebp]
        mov     ecx, dword ptr [esi-4]
        mov     dword ptr [edx+0Ch], ecx
        mov     edi, dword ptr [ebp]
        add     edi, 010h
        dec     eax
        mov     dword ptr [ebp], edi
        jnz     ed6_win3_0048AE70

ed6_win3_0048AEA1:

        mov     eax, dword ptr [esp+01Ch]
        and     eax, 08000000Fh
        jns     ed6_win3_0048AEB1
        dec     eax
        or      eax, 0FFFFFFF0h
        inc     eax

ed6_win3_0048AEB1:

        mov     edx, eax
        dec     eax
        test    edx, edx
        jle     ed6_win3_0048AEE3
        inc     eax

ed6_win3_0048AEB9:

        mov     ecx, dword ptr [ebp]
        mov     dl, byte ptr [esi]
        mov     byte ptr [ecx], dl
        mov     edi, dword ptr [ebp]
        inc     edi
        inc     esi
        dec     eax
        mov     dword ptr [ebp], edi
        jnz     ed6_win3_0048AEB9
        jmp     ed6_win3_0048AEE3

ed6_win3_0048AECD:

        test    eax, eax
        jle     ed6_win3_0048AEE3

ed6_win3_0048AED1:

        mov     ecx, dword ptr [ebp]
        mov     dl, byte ptr [esi]
        mov     byte ptr [ecx], dl
        mov     edi, dword ptr [ebp]
        inc     edi
        inc     esi
        dec     eax
        mov     dword ptr [ebp], edi
        jnz     ed6_win3_0048AED1

ed6_win3_0048AEE3:

        cmp     word ptr [ebp+0Ch], bx
        je      ed6_win3_0048B05D
        jmp     ed6_win3_0048ADB0

ed6_win3_0048AEF2:

        test    al, 040h
        je      ed6_win3_0048AFC5
        test    al, 010h
        je      ed6_win3_0048AF67
        movzx   cx, byte ptr [esi]
        and     al, 0Fh
        mov     edi, dword ptr [ebp+8]
        movzx   ax, al
        shl     eax, 8
        inc     esi
        add     ebx, 2
        mov     dword ptr [ebp+4], esi
        lea     ecx, dword ptr [eax+ecx+4]
        mov     dl, byte ptr [esi]
        inc     esi
        mov     byte ptr [esp+010h], dl
        and     ecx, 0FFFFh
        mov     eax, dword ptr [esp+010h]
        mov     dword ptr [ebp+4], esi
        and     eax, 0FFh
        mov     dword ptr [esp+01Ch], ecx
        mov     dl, al
        add     edi, ecx
        mov     dh, dl
        mov     esi, ecx
        mov     eax, edx
        mov     dword ptr [ebp+8], edi
        mov     edi, dword ptr [ebp]
        shl     eax, 010h
        mov     ax, dx
        shr     ecx, 2
        rep     stos dword ptr es:[edi]
        mov     ecx, esi
        and     ecx, 3
        rep     stos byte ptr es:[edi]
        mov     ecx, dword ptr [ebp]
        mov     eax, esi
        add     ecx, eax
        mov     dword ptr [ebp], ecx
        jmp     ed6_win3_0048ADB0

ed6_win3_0048AF67:

        mov     cl, byte ptr [esi]
        and     al, 0Fh
        add     al, 4
        mov     byte ptr [esp+014h], cl
        mov     byte ptr [esp+010h], al
        mov     eax, dword ptr [esp+014h]
        mov     ecx, dword ptr [esp+010h]
        mov     edi, dword ptr [ebp+8]
        and     eax, 0FFh
        inc     esi
        mov     dl, al
        and     ecx, 0FFh
        mov     dh, dl
        mov     dword ptr [ebp+4], esi
        mov     eax, edx
        mov     dword ptr [esp+01Ch], ecx
        add     edi, ecx
        mov     esi, ecx
        shl     eax, 010h
        mov     dword ptr [ebp+8], edi
        mov     edi, dword ptr [ebp]
        mov     ax, dx
        inc     ebx
        shr     ecx, 2
        rep     stos dword ptr es:[edi]
        mov     ecx, esi
        and     ecx, 3
        rep     stos byte ptr es:[edi]
        mov     ecx, dword ptr [ebp]
        mov     eax, esi
        add     ecx, eax
        mov     dword ptr [ebp], ecx
        jmp     ed6_win3_0048ADB0

ed6_win3_0048AFC5:

        mov     cl, al
        and     cl, 01Fh
        test    al, 020h
        mov     byte ptr [esp+010h], cl
        je      ed6_win3_0048B01D
        xor     ax, ax
        mov     edi, dword ptr [ebp+8]
        mov     al, cl
        movzx   cx, byte ptr [esi]
        shl     eax, 8
        add     eax, ecx
        inc     esi
        mov     dword ptr [ebp+4], esi
        lea     ebx, dword ptr [ebx+eax+1]
        and     eax, 0FFFFh
        mov     ecx, eax
        add     edi, eax
        mov     edx, ecx
        mov     dword ptr [ebp+8], edi
        mov     edi, dword ptr [ebp]
        shr     ecx, 2
        rep     movs dword ptr es:[edi], dword ptr [esi]
        mov     ecx, edx
        and     ecx, 3
        rep     movs byte ptr es:[edi], byte ptr [esi]
        mov     edx, dword ptr [ebp]
        mov     ecx, dword ptr [ebp+4]
        add     edx, eax
        add     ecx, eax
        mov     dword ptr [ebp], edx
        mov     dword ptr [ebp+4], ecx
        jmp     ed6_win3_0048ADB0

ed6_win3_0048B01D:

        xor     ax, ax
        mov     edi, dword ptr [ebp+8]
        mov     al, cl
        add     ebx, eax
        mov     eax, dword ptr [esp+010h]
        and     eax, 0FFh
        mov     ecx, eax
        add     edi, eax
        mov     edx, ecx
        mov     dword ptr [ebp+8], edi
        mov     edi, dword ptr [ebp]
        shr     ecx, 2
        rep     movs dword ptr es:[edi], dword ptr [esi]
        mov     ecx, edx
        and     ecx, 3
        rep     movs byte ptr es:[edi], byte ptr [esi]
        mov     edx, dword ptr [ebp]
        mov     ecx, dword ptr [ebp+4]
        add     edx, eax
        add     ecx, eax
        mov     dword ptr [ebp], edx
        mov     dword ptr [ebp+4], ecx
        jmp     ed6_win3_0048ADB0

ed6_win3_0048B05D:

        pop     edi
        pop     esi
        pop     ebp
        pop     ebx
        add     esp, 8
        ret                                  ;<= Procedure End
    }
}