#include "SNDecompiler.h"
#include "my_mem.h"
#include "my_crt.h"

CSNDecompiler::CSNDecompiler()
{
    m_pbScript = NULL;
}

CSNDecompiler::~CSNDecompiler()
{
    Free();
}

Void CSNDecompiler::Reset()
{
    Free();
    file.Close();
}

Void CSNDecompiler::Free()
{
    mem.SafeFree(&m_pbScript);
}

Bool CSNDecompiler::DecompileFile(const char *pszSrcFile, const char *pszDestFile /* = NULL */)
{
    char szDestFile[MAX_PATH];

    Reset();

    if (file.Open(pszSrcFile) == False)
        return ERR_IO_SRC;

    m_dwScriptSize = file.GetSize();
    if (m_dwScriptSize == 0)
        return ERR_IO_SRC;

    m_pbScript = (PBYTE)mem.Alloc(m_dwScriptSize);
    if (m_pbScript == NULL)
        return ERR_MEM;

    if (file.Read(m_pbScript, m_dwScriptSize) == False)
        return ERR_IO_SRC;

    file.Close();
    if (IsScriptValid() == False)
        return ERR_INVALID;

    if (pszDestFile)
    {
        lstrcpyA(szDestFile, pszDestFile);
    }
    else
    {
        lstrcpyA(szDestFile, pszSrcFile);
        rmext(szDestFile);
        lstrcatA(szDestFile, ".txt");
    }

    fp = fopen(szDestFile, "w");
    if (fp == NULL)
        return ERR_IO_DEST;

    m_dwLabels = 0;
    DecompileHeader();
    InitLabel();
    DecompileEvent();

    fclose(fp);

    return ERR_SUCCESS;
}

Bool CSNDecompiler::IsScriptValid()
{
    SSNHeader *h = (SSNHeader *)m_pbScript;
    static char t[] = "@FileName";

    if (m_dwScriptSize <= sizeof(*h) ||
        h->wEventEndOffset + 9 > m_dwScriptSize ||
        memicmp(m_pbScript + h->wEventEndOffset, t, sizeof(t)))
        return False;

    return True;
}

Void CSNDecompiler::DecompileHeader()
{
    CHAR  szBuffer[0x2000];
    SSNHeader *h = (SSNHeader *)m_pbScript;

    fprintf(fp, "#Location ");
    strncpy(szBuffer, h->szLocation, sizeof(h->szLocation));
    fprintf(fp, "%s\n", szBuffer);

    fprintf(fp, "#Module ");
    strncpy(szBuffer, h->szModuleName, sizeof(h->szModuleName));
    fprintf(fp, "%s\n\n", szBuffer);

    BinToString(szBuffer, sizeof(h->unknown), h->unknown);
    fprintf(fp, "%s\n\n", szBuffer);

    fprintf(fp, "#MainIndex %08X\n", h->dwMainIndex);

    fprintf(fp, "#include %08X", h->dwReferenceIndex[0]);
    for (int i = 1; i != countof(h->dwReferenceIndex); ++i)
    {
        fprintf(fp, ", %08X", h->dwReferenceIndex[i]);
    }
    fprintf(fp, "\n\n");

    if (h->EntryChip.wCount)
    {
        PBYTE p = m_pbScript + h->EntryChip.wOffset;

        fprintf(fp, "#Chip %08X", *(LPDWORD)p);
        p += 4;
        for(int i = 0; i != h->EntryChip.wCount; ++i)
        {
            fprintf(fp, ", %08X", *(LPDWORD)p);
            p += 4;
        }
        fprintf(fp, "\n");
    }

    if (h->EntryPtn.wCount)
    {
        PBYTE p = m_pbScript + h->EntryPtn.wOffset;

        fprintf(fp, "#Ptn %08X", *(LPDWORD)p);
        p += 4;
        for(int i = 0; i != h->EntryPtn.wCount; ++i)
        {
            fprintf(fp, ", %08X", *(LPDWORD)p);
            p += 4;
        }
        fprintf(fp, "\n\n");
    }

    BinToString(szBuffer, h->EntryUnknown.wCount * Size_Event, m_pbScript + h->EntryUnknown.wOffset);
    fprintf(fp, "@Section_Unknown\n"
                "%s\n"
                "@End\n", szBuffer);

    for (int i = 0; i != countof(h->EntryEvent); ++i)
    {
        BinToString(szBuffer, h->EntryEvent[i].wCount * Size_Event, m_pbScript + h->EntryEvent[i].wOffset);
        fprintf(fp, "@Section_Event%04X\n"
                    "%s\n"
                    "@End\n", i, szBuffer);
    }
    fprintf(fp, "\n");
}

Void CSNDecompiler::InitLabel()
{
    ;
}

Void CSNDecompiler::DecompileEvent()
{
    CHAR  szBuffer[0x2000];
    DWORD dwEventCount;
    LPWORD pEntryIndex;
    SSNHeader *h = (SSNHeader *)m_pbScript;

    pEntryIndex = (LPWORD)(m_pbScript + h->wEventIndexOffset);
    dwEventCount = *(LPWORD)(m_pbScript + h->wEventIndexSize) / 2;

    for (DWORD i = 0; i != dwEventCount; ++i)
    {
        DWORD dwLength;
        PBYTE pbEvent = m_pbScript + pEntryIndex[i];

        while (dwLength = DecompileCode(pbEvent, szBuffer))
        {
            if (dwLength == -1)
                return;

            pbEvent += dwLength;
        }
    }
}

Void CSNDecompiler::PrintError(PBYTE pbScript, LPSTR lpFormat, ...)
{
    CHAR    szBuffer[0x1000];
	va_list pArgList;

    va_start(pArgList, lpFormat);
    vsprintf(szBuffer, lpFormat, pArgList);
    printf("Error at %X: %s\n", pbScript - m_pbScript, szBuffer);
}

DWORD CSNDecompiler::DecompileCode(PBYTE pbEvent, LPSTR lpBuffer)
{
    BYTE code, *p;
    DWORD dwLength, v;

    p = pbEvent;

    switch (code = *p++)
    {
        case 0:
            break;

        case 0x02:
            v = *p++;
            if (v > 0x23)
            {
                PrintError(pbEvent, "Invalid param %X of Code %02X, must between 0 and 0x23", v, code);
                goto fail;
            }
            return DecompileCode1E(pbEvent, lpBuffer);

        case 0x03:
            v = *(LPWORD)p;
            p += 2;
            m_mapLabel.SetAt(v, m_dwLabels++);
            break;

        case 0x10:
            p += 2;
            break;

        case 0x16:
            v = *p++;
            if (v > 2)
            {
                PrintError(pbEvent, "Invalid param %X of Code %02X, must be 0, 1, 2", v, code);
                goto fail;
            }
            if (v == 2) p += 0x10;
            break;
    }

    dwLength = p - pbEvent;
    if (lpBuffer)
    {
        BinToString(lpBuffer, dwLength, pbEvent);
        fprintf(fp, "%s\n", lpBuffer);
    }

    return dwLength;
fail:
    return -1;
}

DWORD CSNDecompiler::DecompileCode1E(PBYTE pbEvent, LPSTR lpBuffer)
{
    DWORD param, v;
    PBYTE p;
    POSITION pos;

    p = pbEvent--;
    while ((param = *p++) != 1)
    {
        switch (param)
        {
            case 0:
                break;

            case 0x1E:
                param = *(LPWORD)p;
                p += 2;
                break;
        }
    }
    
    param = *(LPWORD)p;
    if (lpBuffer)
    {
        pos = m_mapLabel.GetStartPosition();
        m_mapLabel.GetNextAssoc(pos, param, v);
        if (pos)
        {
            fprintf(fp, "jmp Label%u\n");
        }

        v = p - pbEvent - 1;
        BinToString(lpBuffer, v, pbEvent);
        fprintf(fp, "%s\n", lpBuffer);
    }
    else
    {
        m_mapLabel.SetAt(param, m_dwLabels++);
    }

    p += 2;
    v = DecompileCode(p, lpBuffer);
    if (v == -1)
        return -1;

    if (lpBuffer)
    {
        pos = m_mapLabel.GetStartPosition();
        m_mapLabel.GetNextAssoc(pos, param, v);
        if (pos)
            fprintf(fp, "Label%u:\n", v);
    }

    v = DecompileCode(m_pbScript + param, lpBuffer);
    if (v == -1)
        return -1;

    return p - pbEvent;
}

int CSNDecompiler::BinToString(LPSTR lpBuffer, DWORD cbBinSize, LPVOID lpBin)
{
    PBYTE pbBin = (PBYTE)lpBin;
    LPSTR p;

    p = lpBuffer;
    *p = 0;
    for (DWORD i = 0; i != cbBinSize; ++i)
    {
        lpBuffer += sprintf(lpBuffer, "\\x%02X", *pbBin++);
    }

    return lpBuffer - p;
}

int CSNDecompiler::BinToFloat(LPSTR lpBuffer, DWORD cbBinSize, LPVOID lpBin)
{
    PBYTE pbBin = (PBYTE)lpBin;
    LPSTR p;

    p = lpBuffer;
    *p = 0;
    for (DWORD i = 0; i != cbBinSize; ++i)
    {
        if (i)
        {
            lpBuffer += sprintf(lpBuffer, ", ");
        }

        lpBuffer += sprintf(lpBuffer, "%f", *(PFLOAT)pbBin);
        pbBin += sizeof(FLOAT);
    }

    return lpBuffer - p;
}