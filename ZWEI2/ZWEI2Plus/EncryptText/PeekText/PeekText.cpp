#include "PeekText.h"
#include "my_crtadd.h"

char *szTableTag[] =
{
    NULL,
    "#ItemTable",
    "#StageTable",
    "#ShopTable",
    "#CharNoteTable",
    "#MailTable",
    "#NikkiTable",
    "#MapTable",
    "#CCTable",
    "#LVTable",
    "#TAKARATable",
    "#CharTable",
    "#ScriptTable",
    "#CharMotTable",
};

CRipZwei2Text::CRipZwei2Text()
{
    m_pScpBuffer = NULL;
    m_u32ScpSize = 0;
    m_bEndOfScp = False;
    m_bMultiLineComment = False;
    m_u32ScpType = None;
}

CRipZwei2Text::~CRipZwei2Text()
{
    Free();
}

Void CRipZwei2Text::Free()
{
    if (m_pScpBuffer)
    {
        delete[] m_pScpBuffer;
        m_pScpBuffer = NULL;
    }
}

Bool CRipZwei2Text::Open(char *szFileName)
{
    Free();

    FILE *fp = fopen(szFileName, "rb");

    if (!fp) return False;

    m_u32ScpSize = fsize(fp);
    m_pScpBuffer = new char[m_u32ScpSize + 1];
    fread(m_pScpBuffer, m_u32ScpSize, 1, fp);
    fclose(fp);

    m_u32Cursor = 0;
    m_pEndOfScript = m_pScpBuffer + m_u32ScpSize;
    m_pScpBuffer[m_u32ScpSize] = 0;

    return True;
}

char* CRipZwei2Text::GetCommentEndPos(char *pLine)
{
    char ch, *pEnd;

    pEnd = m_pEndOfScript;

    if (m_u32ScpType != EndOfTable && m_u32ScpType != None)
    {
        if (pLine[0] != '/' || pLine + 1 >= pEnd)
        {
            if ((uchar)pLine[0] > 0x80) ++pLine;
            return pLine;
        }

        ch = pLine[1];
        if (ch == '/')
        {
            while (pLine[0] != '\n' && pLine < pEnd)
            {
                if ((uchar)pLine[0] > 0x80) ++pLine;
                ++pLine;
            }

            if (pLine >= pEnd)
                return NULL;
        }
        else if (ch == '*')
        {
            pLine += 2;
            while (pLine < pEnd)
            {
                while (pLine[0] != '*' && pLine < pEnd)
                {
                    if ((uchar)pLine[0] > 0x80) ++pLine;
                    ++pLine;
                }

                if (pLine >= pEnd)
                    return NULL;

                if (pLine[1] == '/')
                {
                    pLine += 2;
                    if (pLine >= pEnd)
                        return NULL;

                    break;
                }
                ++pLine;
            }
        }
    }
    while ((*pLine == ' ' || *pLine == '\t') && pLine < m_pEndOfScript)
    {
        if ((uchar)pLine[0] > 0x80) ++pLine;
        ++pLine;
    }
    if (pLine >= m_pEndOfScript)
        return NULL;

    return pLine;
}

char* CRipZwei2Text::GetNextLinePos()
{
    char *pLine = m_pScpBuffer + m_u32Cursor, *p;

    while ((*pLine == ' ' || *pLine == '\t') && pLine < m_pEndOfScript) ++pLine;
    if (pLine >= m_pEndOfScript)
        return NULL;

    while (*pLine == '\r' && pLine < m_pEndOfScript)
    {
        if ((uchar)pLine[0] > 0x80) ++pLine;
        ++pLine;
    }
    if (pLine >= m_pEndOfScript)
        return NULL;

    if (*pLine != '\n')
    {
        char *pTemp;

        do
        {
            pTemp = GetCommentEndPos(pLine);
            if (pTemp == NULL)
                return NULL;

            if (pLine == pTemp)
            {
                pLine = pTemp;
                break;
            }

            pLine = pTemp;
        } while (1);
    }

    p = pLine;
    while (*p != '\n' && p < m_pEndOfScript)
    {
        if (*p == '\r') *p = 0;
        else if (*(uchar *)p > 0x80) ++p;
        ++p;
    }

    if (p < m_pEndOfScript)
    {
        *p++ = 0;
    }
    m_u32Cursor = p - m_pScpBuffer;

    return pLine;
}

u32 GetScriptType(char *pLine)
{
    u32 len;

    for (u32 i = 1; i != countof(szTableTag); ++i)
    {
        if (!stricmp(pLine, szTableTag[i]))
            return i;
    }

    if (strnicmp(pLine, "#End", 4))
        return None;

    len = strlen(pLine);
    if (len < 10)
        return None;

    return stricmp(&pLine[len - 5], "Table") ? None : EndOfTable;
}

Bool CRipZwei2Text::GetAllText(vector<string> &vec)
{
    u32 u32ScpType;
    char *pLine;

    while (1)
    {
        pLine = GetNextLinePos();
        if (pLine == NULL || pLine >= m_pEndOfScript)
            break;

        if (*pLine == '\n' || *pLine == 0)
            continue;

        if (*pLine == '#')
        {
            u32ScpType = GetScriptType(pLine);
            if (u32ScpType != None)
            {
                m_u32ScpType = u32ScpType;
                continue;
            }
        }

        switch (m_u32ScpType)
        {
        case None:
        case EndOfTable:
            continue;

        case ItemTable:
            RipItemTable(vec, pLine);
            break;

        case StageTable:
            RipStageTable(vec, pLine);
            break;

        case CharNoteTable:
            RipCharNoteTable(vec, pLine);
            break;

        case MailTable:
            RipMailTable(vec, pLine);
            break;

        case NikkiTable:
            RipNikkiTable(vec, pLine);
            break;

        case MapTable:
            RipMapTable(vec, pLine);
            break;

        case TAKARATable:
            RipTAKARATable(vec, pLine);
            break;

        case CharTable:
            RipCharTable(vec, pLine);
            break;

        case ScriptTable:
            RipScripTable(vec, pLine);
            break;

        case CharMotTable:
            RipCharMotTable(vec, pLine);
            break;
        }
    }

    return True;
}

typedef struct
{
    char *szStartWord;
    u32   u32StartCount;
} TFilter;

char* STDCALL my_strchr(char *s, int ch)
{
    uchar c, *str;

    str = (uchar *)s;
    while (c = *str++)
    {
        if (c == ch) return (char *)str - 1;
        else if (c > 0x80) ++str;
    }

    return NULL;
}

Void CRipZwei2Text::RipScripTable(vector<string> &vec, char *pLine)
{
    u32 i = 0;
    char *pStart, *pEnd;

    static TFilter Filter[] =
    {
        { "set_chr(",    1 }, 
        { "MES(",        1 }, 
        { "MES_pos(",    1 }, 
        { "chr_rename(", 1 }, 
        { "menuTXT(",    1 }, 
        { "menuEVENT",   5 }, 
    };

    for (i = 0; i != countof(Filter); ++i)
    {
        if (!strncmp(pLine, Filter[i].szStartWord, strlen(Filter[i].szStartWord)))
            break;
    }
    if (i == countof(Filter))
        return;

    pStart = pLine;
    for (u32 j = 0; j != Filter[i].u32StartCount; ++j)
    {
        pStart = my_strchr(pStart, '"');
        if (pStart == NULL)
            return;
        ++pStart;
    }

    if (pStart[0] == '"')
        return;

    if (i)
    {
        pEnd = my_strchr(pStart, '"');
        if (pEnd == NULL)
            return;
    }
    else
    {
        uchar ch;
        while (1)
        {
            ch = *pStart++;
            if (ch == 0 || ch == '"') return;
            else if (ch == '[') break;
            else if (ch > 0x80) ++pStart;
        }
        while (1)
        {
            ch = *pStart++;
            if (ch < '0' || ch > '9')
                break;
            else if (ch == 0 || ch == ']')
                return;
            else if (ch > 0x80) ++pStart;
        }

        pEnd = my_strchr(--pStart, ']');
        if (pEnd == NULL)
            return;
    }

    vec.push_back(string(pStart, pEnd));
}

Void CRipZwei2Text::RipItemTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 1);
    GetColumnText(vec, pLine, 11);
}

Void CRipZwei2Text::RipCharTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 1);
    GetColumnText(vec, pLine, 20);
}

Void CRipZwei2Text::RipStageTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 3);
    GetColumnText(vec, pLine, 16);
}

Void CRipZwei2Text::RipCharNoteTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 2);
}

Void CRipZwei2Text::RipMailTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 4);
}

Void CRipZwei2Text::RipNikkiTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 1);
}

Void CRipZwei2Text::RipMapTable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 13);
}

Void CRipZwei2Text::RipTAKARATable(vector<string> &vec, char *pLine)
{
    GetColumnText(vec, pLine, 1);
}

Void CRipZwei2Text::RipCharMotTable(vector<string> &vec, char *pLine)
{
    if (!strncmp(pLine, "TEXT", 4))
        GetColumnText(vec, pLine, 7);
}

Void CRipZwei2Text::GetColumnText(vector<string> &vec, char *pLine, u32 uColumn)
{
    char *pEnd = pLine + strlen(pLine);

    while (uColumn--)
    {
        while (pLine[0] != ' ' && pLine[0] != '\t' && pLine < pEnd)
        {
            if ((uchar)pLine[0] > 0x80) ++pLine;
            ++pLine;
        }
        if (pLine >= pEnd)
            return;

        while ((pLine[0] == ' ' || pLine[0] == '\t') && pLine < pEnd)
        {
            if ((uchar)pLine[0] > 0x80) ++pLine;
            ++pLine;
        }
        if (pLine >= pEnd)
            return;
    }

    pEnd = pLine;
    while (pEnd[0] != ' ' && pEnd[0] != '\t' && pEnd[0] && pEnd[0] != '/')
    {
        if ((uchar)pEnd[0] > 0x80) ++pEnd;
        ++pEnd;
    }

    string str(pLine, pEnd);

    ++pEnd;
    if (pEnd[0] == '/' && pEnd[1] == '*')
    {
        pEnd = GetCommentEndPos(pEnd);
        m_u32Cursor = pEnd - m_pScpBuffer;
    }

    if (str == "°°" || str == "Å@" || str == "£ﬂ" || str == "ÅQ")
        return;

    for (u32 i = 0; i != str.length(); ++i)
    {
        if ((str.c_str())[i] != '-')
        {
            vec.push_back(str);
            return;
        }
    }
}