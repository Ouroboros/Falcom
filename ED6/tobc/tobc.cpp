///////////////////////////////////////////////////////////////////////////////
//    tobc.cpp (by dwing) [2009-02-28]
///////////////////////////////////////////////////////////////////////////////
/*
; for test
@_FILE    "test.bin"
@_DEFI    4
@_DEFF    4
@nop    [00]
@call    [ca 11]
@str    "str"
@num    12
@pi     3.14
call (p001-num+123-@:s,pi)    ;指定位数:b/s/t/i/f/d
    "AAA"
    'abc def\n'
    nop
#p001
    [12 cd 00]
*/

#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")
#define USE_CRT_ALLOC

#include <afx.h>
#include <afxtempl.h>
#include <afxcoll.h>
#include <stdio.h>
#include "my_headers.h"

OVERLOAD_OP_NEW

class CTobCompiler    // NOT object-thread-safe
{
public:
    enum EToken
    {
        ERR_SEVERE = -2,    // may not goon
        ERR_NORMAL = -1,    // may goon
        ERR_EOF = 0,        // end of file

        SYM_TOKEN,          // token word
        SYM_INT,            // integer number
        SYM_FLOAT,          // float number
        SYM_DEF,            // @
        SYM_LABEL,          // #
        SYM_BIN,            // [
        SYM_STR,            // ' "
        SYM_EXP_BEGIN,      // (
        SYM_ADD,            // +
        SYM_SUB,            // -
        SYM_TYPE,           // :
        SYM_NEXT,           // ,
        SYM_EXP_END,        // )
        SYM_UNKNWON,

        TOKEN_NOT_ID = 0,
        TOKEN_ID,
        TOKEN_OTHER,
        TOKEN_INVALID,
    };

private:
    typedef BOOL (CTobCompiler::*F_ErrorHandler)(const CString& err);
    struct SValueType
    {
        double  dval;
        int     ival;
        BOOL    isfloat;
        int     m_size;
        explicit SValueType(int i, int size = -1) : ival(i), dval(i), isfloat(FALSE), m_size(size) {}
        explicit SValueType(double d, int size = -1) : ival((int)d), dval(d), isfloat(TRUE), m_size(size) {}
    };
    struct SExpression
    {
        CStringArray    m_item;
        int             m_pos;
        int             m_line;
        int             m_size; // 1/2/3/4/-4/-8
        int             m_self;
        SExpression() : m_pos(0), m_line(0), m_self(0) {}
        SExpression(int pos, int line) : m_pos(pos), m_line(line), m_size(4), m_self(0) {}
    };

    typedef CMap<CString, LPCTSTR, CByteArray*, CByteArray*> BinaryMap;
    typedef CMap<CString, LPCTSTR, SValueType*, SValueType*> ValueMap;
    typedef CArray<SExpression*, SExpression*>               ExpressionArray;

    static const BYTE   ms_tokentable[256];
    static const BYTE   ms_hextable[256];
    int                 m_line;
    CString             m_err;
    CByteArray          m_bin;
    FILE*               m_fsrc;
    FILE*               m_fdst;
    BinaryMap           m_binmap;
    ValueMap            m_valmap;
    ExpressionArray     m_exparr;
    int                 m_errornum;
    struct
    {
        ULONG DefInt;
        ULONG DefFloat;
        BOOL  bIgnoreCase;
    } m_Option;

private:
    void        Reset();
    CString&    GetErrorString(CString& str);
    EToken      GetToken(CString& str);
    EToken      GetNumber(CString& str);
    EToken      GetString(CByteArray& str);
    EToken      GetBinary(CByteArray& bin);
    ULONG       GetSizeFromType(CHAR Type);
    EToken      CompilePass1();
    BOOL        CompilePass2(F_ErrorHandler ErrorHandler);

    static Void AddMap(BinaryMap &m, LPCTSTR k, CByteArray *v)
    {
        CByteArray* v_old;
        if (m.Lookup(k, v_old))
            delete v_old;
        m.SetAt(k, v);
    }

    static Void AddMap(ValueMap &m, LPCTSTR k, SValueType *v)
    {
        SValueType* v_old;
        if (m.Lookup(k, v_old))
            delete v_old;
        m.SetAt(k, v);
    }

public:
    CTobCompiler() : m_fsrc(NULL), m_fdst(NULL)
    {
        Reset();
    }

    ~CTobCompiler()
    {
        Reset();
    }

    BOOL CompileFile(LPWSTR fsrcname, LPWSTR fdstname, F_ErrorHandler ErrorHandler);

    BOOL CTobCompiler::ErrorHandlerInternal(const CString& err);
};

// 0: 非标识符
// 1: 标识符首字符(字母,_,GBK中文)
// 2: 标识符非首字符(0~9,.)
// 3: 非法控制符
const BYTE CTobCompiler::ms_tokentable[256] =
{
    3,3,3,3,3,3,3,3, 3,0,0,3,3,0,3,3, // 0x
    3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, // 1x
    0,0,0,0,0,0,0,0, 0,0,0,0,0,0,2,0, // 2x
    2,2,2,2,2,2,2,2, 2,2,0,0,0,0,0,0, // 3x
    0,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // 4x
    1,1,1,1,1,1,1,1, 1,1,1,0,0,0,0,1, // 5x
    0,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // 6x
    1,1,1,1,1,1,1,1, 1,1,1,0,0,0,0,3, // 7x
    3,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // 8x
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // 9x
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // Ax
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // Bx
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // Cx
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // Dx
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // Ex
    1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,3, // Fx
};

const BYTE CTobCompiler::ms_hextable[256] =
{
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 0x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 1x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 2x
     0, 1, 2, 3, 4, 5, 6, 7,  8, 9,16,16,16,16,16,16, // 3x
    16,10,11,12,13,14,15,16, 16,16,16,16,16,16,16,16, // 4x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 5x
    16,10,11,12,13,14,15,16, 16,16,16,16,16,16,16,16, // 6x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 7x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 8x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // 9x
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // Ax
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // Bx
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // Cx
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // Dx
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // Ex
    16,16,16,16,16,16,16,16, 16,16,16,16,16,16,16,16, // Fx
};

void CTobCompiler::Reset()
{
    m_errornum = 0;
    m_line = 0;
    m_err.Empty();
    m_bin.RemoveAll();
    if (m_fsrc) { fclose(m_fsrc); m_fsrc = 0; }
    if (m_fdst) { fclose(m_fdst); m_fdst = 0; }

    POSITION p;
    CString str;

    p = m_binmap.GetStartPosition();
    CByteArray* bin;
    while(p)
    {
        m_binmap.GetNextAssoc(p, str, bin);
        delete bin;
    }
    m_binmap.RemoveAll();
    m_binmap.InitHashTable(251);

    p = m_valmap.GetStartPosition();
    SValueType* val;
    while(p)
    {
        m_valmap.GetNextAssoc(p, str, val);
        delete val;
    }
    m_valmap.RemoveAll();
    m_valmap.InitHashTable(251);

    for(int i = m_exparr.GetSize() - 1; i >= 0; --i)
        delete m_exparr.GetAt(i);
    m_exparr.RemoveAll();

    m_Option.DefInt = 4;
    m_Option.DefFloat = 4;
    m_Option.bIgnoreCase = FALSE;
}

inline CString& CTobCompiler::GetErrorString(CString& str)
{
    if (m_line > 0)    str.Format("ERROR(%d): %s", m_line, (LPCTSTR)m_err);
    else            str.Format("ERROR: %s", (LPCTSTR)m_err);
    m_err.Empty();
    return str;
}

// 获取符号,数字或标识符
CTobCompiler::EToken CTobCompiler::GetToken(CString& str)
{
    EToken ret = ERR_EOF;
    BOOL comment = FALSE;
    str.Empty();
    for(;;)
    {
        int c = fgetc(m_fsrc);
        if (c == EOF)
        {
            if (!feof(m_fsrc))
            {
                m_err.Format("can not read src file at %p", ftell(m_fsrc));
                return ERR_SEVERE;
            }
            return str.IsEmpty() ? ERR_EOF : ret;
        }
        if (comment)
        {
            if (c == '\n') { ++m_line; comment = FALSE; }
            continue;
        }
        if (ret == ERR_EOF)
        {
            switch(c)
            {
            case ' ':
            case '\t':
            case '\r': continue;
            case '\n': ++m_line;        continue;
            case ';' : comment = TRUE;  continue;
            case '@' : return SYM_DEF;
            case '#' : return SYM_LABEL;
            case '[' : return SYM_BIN;
            case '\'':
            case '\"': return SYM_STR;
            case '(' : return SYM_EXP_BEGIN;
            case '+' : return SYM_ADD;
            case '-' : return SYM_SUB;
            case ':' : return SYM_TYPE;
            case ',' : return SYM_NEXT;
            case ')' : return SYM_EXP_END;
            default:
                switch(ms_tokentable[c])
                {
                    case TOKEN_NOT_ID:
                    case TOKEN_INVALID:
                        m_err.Format("found invalid char 0x%02X in src file at %p", c, ftell(m_fsrc)-1);
                        return ERR_NORMAL;

                    case TOKEN_ID:
                        ret = SYM_TOKEN;
                        break;

                    case TOKEN_OTHER:
                        if (fseek(m_fsrc, -1, SEEK_CUR))
                        {
                            m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                            return ERR_SEVERE;
                        }
                        return GetNumber(str);
                }
            }
        }
        else if (!ms_tokentable[c] || ms_tokentable[c] == 3)
        {
            if (fseek(m_fsrc, -1, SEEK_CUR))
            {
                m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                return ERR_SEVERE;
            }
            return ret;
        }
        if (c >= 0x81)
        {
            str += (TCHAR)c;
            c = fgetc(m_fsrc);
            if (c < 0)
            {
                if (!feof(m_fsrc))
                    m_err.Format("can not read src file at %p", ftell(m_fsrc));
                else
                    m_err = "found half wide char at the end of src file";
                return ERR_SEVERE;
            }
            if (c < 0x40)
            {
                if (fseek(m_fsrc, -1, SEEK_CUR))
                {
                    m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                    return ERR_SEVERE;
                }
                m_err.Format("found half wide char in src file at %p", ftell(m_fsrc)-1);
                return ERR_NORMAL;
            }
        }
        if (m_Option.bIgnoreCase)
            c = CHAR_LOWER(c);
        str += (TCHAR)c;
    }
}

CTobCompiler::EToken CTobCompiler::GetNumber(CString& str)
{
    BOOL dot = FALSE, ex = FALSE, number = FALSE, hex = FALSE;
    str.Empty();
    for(;;)
    {
        int c = fgetc(m_fsrc);
        if (c == EOF)
        {
            if (!feof(m_fsrc))
            {
                m_err.Format("can not read src file at %p", ftell(m_fsrc));
                return ERR_SEVERE;
            }
            if (str.IsEmpty())
                return ERR_EOF;

            c = (BYTE)str[str.GetLength() - 1];
            if (!number || (ms_tokentable[c] != TOKEN_OTHER && !IN_RANGE('A', c, 'Z')))
            {
                m_err = "found bad number";
                return ERR_NORMAL;
            }
            return (dot || ex) ? SYM_FLOAT : SYM_INT;
        }

        c = CHAR_UPPER(c);
begin_: if (c == '.')
        {
            if (dot)
            {
                m_err = "found more '.' in number";
                return ERR_NORMAL;
            }
            if (ex)
            {
                m_err = "found '.' after 'e/E' in number";
            }
            dot = TRUE;
        }
        else if (!hex && c == 'E')
        {
            if (ex)
            {
                m_err = "found more 'e/E' in number";
            }
            c = fgetc(m_fsrc);
            if (c < 0)
            {
                if (!feof(m_fsrc))
                {
                    m_err.Format("can not read src file at %p", ftell(m_fsrc));
                    return ERR_SEVERE;
                }
                else
                {
                    m_err = "found bad number at the end of src file";
                    return ERR_NORMAL;
                }
            }
            if (c != '+' && c != '-')
                goto begin_;
        }
        else
        {
            switch(ms_tokentable[c])
            {
                case TOKEN_NOT_ID:
                    if (c > ' ' && fseek(m_fsrc, -1, SEEK_CUR))
                    {
                        m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                        return ERR_SEVERE;
                    }

                    c = (BYTE)str[str.GetLength() - 1];
                    if (!number || (ms_tokentable[c] != TOKEN_OTHER && !IN_RANGE('A', c, 'Z')))
//                    if (!number || ms_tokentable[(BYTE)str[str.GetLength()-1]] != 2)
                    {
                        m_err = "found bad number";
                        return ERR_NORMAL;
                    }
                    return dot || ex ? SYM_FLOAT : SYM_INT;

                case TOKEN_ID:
                    if (!hex || !IN_RANGE('A', c, 'Z'))
                    {
                        m_err = "found bad number";
                        return ERR_NORMAL;
                    }

                case TOKEN_OTHER:
                    if (!number && !hex)
                    {
                        if (c == '0')
                        {
                            int c2 = fgetc(m_fsrc);
                            c2 = CHAR_UPPER(c2);
                            if (c2 == 'X')
                            {
                                hex = TRUE;
                                str += '0';
                                c = 'x';
                            }
                            else if (fseek(m_fsrc, -1, SEEK_CUR))
                            {
                                m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                                return ERR_SEVERE;
                            }
                        }
                    }

                    number = TRUE;
                    break;

                case TOKEN_INVALID:
                    m_err.Format("found invalid char 0x%02X in src file at %p", c, ftell(m_fsrc)-1);
                    return ERR_NORMAL;
            }
        }
        str += (TCHAR)c;
    }
}

CTobCompiler::EToken CTobCompiler::GetBinary(CByteArray& bin)
{
    DWORD cache = 1;
    BOOL comment = FALSE;
    for(;;)
    {
        int c = fgetc(m_fsrc);
        if (c == EOF)
        {
            if (!feof(m_fsrc))
                m_err.Format("can not read src file at %p", ftell(m_fsrc));
            else
                m_err = "not found ']' at the end of src file";
            return ERR_SEVERE;
        }
        if (comment)
        {
            if (c == '\n') { ++m_line; comment = FALSE; }
            continue;
        }
        BYTE half = ms_hextable[c];
        if (half < 16)
        {
            cache = (cache << 4) + half;
            if (cache >= 0x100)
            {
                bin.Add((BYTE)cache);
                cache = 1;
            }
        }
        else if (c <= ' ') continue;
        else if (c == '\n') ++m_line;
        else if (c == ']')
        {
            if (cache != 1) bin.Add((BYTE)(cache & 0x0f));
            return SYM_BIN;
        }
        else if (c == ';') { comment = TRUE; continue; }
        else
        {
            m_err.Format("bad hex char 0x%02X", c);
            return ERR_NORMAL;
        }
    }
}

CTobCompiler::EToken CTobCompiler::GetString(CByteArray& bin)
{
    CByteArray temp;
    int c, d, e;
    for(;;)
    {
        if ((c = fgetc(m_fsrc)) < 0) break;
        if (c == '\n') ++m_line;
        else if (ms_tokentable[c] == 3)
        {
            m_err.Format("found invalid char 0x%02X in src file at %p", c, ftell(m_fsrc)-1);
            return ERR_NORMAL;
        }
        else if (c < ' ') continue;
        else if (c == '\'' || c == '"')
        {
            if ((d = fgetc(m_fsrc)) > 0)
            {
                if (d == ':')
                {
                    if ((d = fgetc(m_fsrc)) < 0) break;
                    e = GetSizeFromType(d);
                    if (e == -1)
                    {
                        m_err.Format("unknown type '%c' after ':'", d);
                        return ERR_NORMAL;
                    }

                    d = temp.GetSize();
                    for(int i = 0; i < e; ++i)
                        bin.Add(((BYTE*)&d)[i]);
                }
                else if (fseek(m_fsrc, -1, SEEK_CUR))
                {
                    m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                    return ERR_SEVERE;
                }
            }
            bin.Append(temp);
            if (c == '"')
                bin.Add(0);

            if (m_Option.bIgnoreCase)
                strlwr((LPSTR)bin.GetData());
            return SYM_STR;
        }
        else if (c == '\\')
        {
            if ((c = fgetc(m_fsrc)) < 0) break;
            switch(CHAR_UPPER(c))
            {
                case 'N': c = '\n';   break;
                case 'R': c = '\r';   break;
                case 'T': c = '\t';   break;
                case '0': c = '\0';   break;
                case '1': c = '\x01'; break;
                case '2': c = '\x02'; break;
                case '3': c = '\x03'; break;
                case '4': c = '\x04'; break;
                case '5': c = '\x05'; break;
                case '6': c = '\x06'; break;
                case '7': c = '\x07'; break;
                case '8': c = '\x08'; break;
                case '9': c = '\x09'; break;
                case 'A': c = '\x0a'; break;
                case 'B': c = '\x0b'; break;
                case 'C': c = '\x0c'; break;
                case 'D': c = '\x0d'; break;
                case 'E': c = '\x0e'; break;
                case 'F': c = '\x0f'; break;
                case 'X':
                {
                    if ((c = fgetc(m_fsrc)) < 0) goto end_;
                    BYTE b0 = ms_hextable[c];
                    if (b0 == 16)
                    {
                        m_err.Format("bad hex char 0x%02X after '\\x'", b0);
                        return ERR_NORMAL;
                    }
                    if ((c = fgetc(m_fsrc)) < 0) goto end_;
                    BYTE b1 = ms_hextable[c];
                    if (b1 == 16)
                    {
                        m_err.Format("bad hex char 0x%02X after '\\x'", b1);
                        return ERR_NORMAL;
                    }
                    temp.Add((BYTE)((b0<<4) + b1));
                }
            }
        }
        if (c >= 0x81)
        {
            if ((d = fgetc(m_fsrc)) < 0) break;
            if (d < 0x40)
            {
                if (fseek(m_fsrc, -1, SEEK_CUR))
                {
                    m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                    return ERR_SEVERE;
                }
                m_err.Format("found half wide char at %p", ftell(m_fsrc)-1);
                return ERR_NORMAL;
            }
            temp.Add((BYTE)c);
            temp.Add((BYTE)d);
        }
        else
        {
            temp.Add((BYTE)c);
        }
    }
end_:
    if (!feof(m_fsrc))
        m_err.Format("can not read src file at %p", ftell(m_fsrc));
    else
        m_err = "bad string at the end of src file";
    return ERR_SEVERE;
}

ULONG CTobCompiler::GetSizeFromType(CHAR Type)
{
    ULONG Length;
    switch(CHAR_UPPER(Type))
    {
        case 'B': Length = 1;  break;
        case 'S': Length = 2;  break;
        case 'T': Length = 3;  break;
        case 'Q':
        case 'I': Length = 4;  break;
        case 'F': Length = -4; break;
        case 'D': Length = -8; break;
        default:  Length = -1;  break;
    }

    return Length;
}

CTobCompiler::EToken CTobCompiler::CompilePass1()
{
    EToken r, LastToken;
    CString str, buf, sizebuf;
    CByteArray* bin;
    SValueType* val;
    SExpression* exp;

    for(;;)
    {
        BOOL bSkipGetToken = FALSE;
        if ((r = GetToken(str)) <= 0) return r;
_SkipGetToken:
        if (r == SYM_DEF)
        {
/*
            if (m_bin.GetSize() > 0)
            {
                m_err = "const token can not defined after data";
                return ERR_NORMAL;
            }
*/
            if ((r = GetToken(str)) < 0) return r;
            if (r != SYM_TOKEN)
            {
                m_err = "not found token after '@'";
                return ERR_NORMAL;
            }

            if (str == "_IGNORECASE")
            {
                m_Option.bIgnoreCase = TRUE;
                continue;
            }

            if ((r = GetToken(buf)) < 0) return r;
            if (r == SYM_BIN)
            {
                bin = new CByteArray;
                if ((r = GetBinary(*bin)) < 0) { delete bin; return r; }
                AddMap(m_binmap, str, bin);
            }
            else if (r == SYM_STR)
            {
                bin = new CByteArray;
                if ((r = GetString(*bin)) < 0) { delete bin; return r; }
                AddMap(m_binmap, str, bin);
            }
            else if (r == SYM_INT)
            {
                ULONG Length;
                BOOL bHex = (buf[0] == '0' && buf[1] == 'x');

                r = GetToken(sizebuf);
                LastToken = r;
                if (r == SYM_TYPE)
                {
                    r = GetToken(sizebuf);
                    if (r != SYM_TOKEN)
                    {
                        m_err = "not found type after ':'";
                        return ERR_NORMAL;
                    }

                    Length = GetSizeFromType(sizebuf[0]);
                    if (Length == -1)
                    {
                        m_err.Format("unknown type '%c' after ':'", sizebuf[0]);
                        return ERR_NORMAL;
                    }
                }
                else
                {
                    Length = -1;
                }
                val = new SValueType((int)strtoul(buf, NULL, bHex ? 16 : 10), Length);
                AddMap(m_valmap, str, val);

                if (Length == -1)
                    bSkipGetToken = TRUE;

                r = SYM_INT;
            }
            else if (r == SYM_FLOAT)
            {
                AddMap(m_valmap, str, new SValueType(atof(buf)));
            }
            else
            {
                m_err.Format("not found '[' or ''' or '\"' or number after '@%s'", (LPCTSTR)str);
                return ERR_NORMAL;
            }

            if (m_Option.bIgnoreCase)
                str.MakeUpper();

            if (str == "_DEFI")
            {
                if (r != SYM_INT || val->ival < 1 || val->ival > 4)
                {
                    m_err = "_DEFI must be 1/2/3/4";
                    return ERR_NORMAL;
                }
                m_Option.DefInt = val->ival;
            }
            else if (str == "_DEFF")
            {
                if (r != SYM_INT || val->ival != 4 && val->ival != 8)
                {
                    m_err = "_DEFF must be 4/8";
                    return ERR_NORMAL;
                }
                m_Option.DefFloat = val->ival;
            }
            else if (str == "_MOD")
            {
                if (r != SYM_INT)
                {
                    m_err = "_MOD must be number";
                    return ERR_NORMAL;
                }

                while (m_bin.GetSize() % val->ival)
                    m_bin.Add(0);
            }
            else if (str == "_INCLUDE")
            {
                FILE *fsrc;
                WCHAR szPath[MAX_PATH];
                CByteArray *bin;

                if (m_Option.bIgnoreCase)
                    str.MakeLower();

                if (!m_binmap.Lookup(str, bin))
                    continue;

                m_binmap.RemoveKey(str);

                MultiByteToWideChar(
                    CP_GB2312,
                    0,
                    (LPSTR)bin->GetData(),
                    -1,
                    szPath,
                    countof(szPath));

                delete bin;

                fsrc = m_fsrc;
                m_fsrc = _wfopen(szPath, L"rb");
                if (m_fsrc == NULL)
                {
                    m_fsrc = fsrc;
                    m_err.Format("can't open include file '%S'", szPath);
                    return ERR_SEVERE;
                }
                else
                {
                    EToken r;
                    for(;;)
                    {
                        r = CompilePass1();
                        if (r == ERR_EOF)
                            break;

                        if (r < 0)
                        {
                            if (!ErrorHandlerInternal(GetErrorString(m_err)))
                                break;
                        }

                        if (r == ERR_SEVERE)
                            break;
                    }

                    fclose(m_fsrc);
                    m_fsrc = fsrc;
                    if (r < 0)
                        return r;
                }
            }

            if (bSkipGetToken)
            {
                str = sizebuf;
                r = LastToken;
                goto _SkipGetToken;
            }
        }
        else if (r == SYM_BIN)
        {
            if ((r = GetBinary(m_bin)) < 0) return r;
        }
        else if (r == SYM_STR)
        {
            if ((r = GetString(m_bin)) < 0) return r;
        }
        else if (r == SYM_TOKEN)
        {
            if (!m_binmap.Lookup(str, bin))
            {
                m_err.Format("unknown token '%s'", (LPCTSTR)str);
                return ERR_NORMAL;
            }
            m_bin.Append(*bin);
        }
        else if (r == SYM_LABEL)
        {
            if ((r = GetToken(str)) < 0) return r;
            if (r != SYM_TOKEN)
            {
                m_err = "not found token after '#'";
                return ERR_NORMAL;
            }
            if (m_valmap.Lookup(str, val))
            {
                m_err.Format("already defined label token '%s'", (LPCTSTR)str);
                return ERR_NORMAL;
            }
            m_valmap.SetAt(str, new SValueType(m_bin.GetSize()));
        }
        else if (r == SYM_EXP_BEGIN)
        {
            int i = m_exparr.GetSize();
            do
            {
                int len = m_Option.DefInt;
                BOOL hastype = FALSE;
                exp = new SExpression(m_bin.GetSize(), m_line);
                for(;;)
                {
                    if ((r = GetToken(buf)) < 0)
                    {
                        delete exp;
                        return r;
                    }

                    if (r == SYM_TOKEN)
                    {
                        val = NULL;
                        if (!hastype && len > 0 && m_valmap.Lookup(buf, val) && val->isfloat)
                            len = -m_Option.DefFloat;
                        exp->m_item.Add(buf);
                        if (val != NULL && val->m_size != -1)
                            len = val->isfloat ? -val->m_size : val->m_size;
                    }
                    else if (r == SYM_ADD)
                    {
                        exp->m_item.Add("+");
                    }
                    else if (r == SYM_SUB)
                    {
                        exp->m_item.Add("-");
                    }
                    else if (r == SYM_DEF)
                    {
                        exp->m_item.Add("@");
                    }
                    else if (r == SYM_INT)
                    {
                        exp->m_item.Add(buf);
                    }
                    else if (r == SYM_FLOAT)
                    {
                        if (!hastype && len > 0)
                            len = -m_Option.DefFloat;
                        exp->m_item.Add(buf);
                    }
                    else if (r == SYM_TYPE)
                    {
                        int newlen;
                        if ((r = GetToken(buf)) < 0) { delete exp; return r; }
                        if (r != SYM_TOKEN)
                        {
                            delete exp;
                            m_err = "not found type after ':'";
                            return ERR_NORMAL;
                        }

                        newlen = GetSizeFromType(buf[0]);
                        if (newlen == -1)
                        {
                            delete exp;
                            m_err.Format("unknown type '%c' after ':'", buf[0]);
                            return ERR_NORMAL;
                        }

                        if (hastype && newlen != len)
                        {
                            delete exp;
                            m_err = "found different types in one expression";
                            return ERR_NORMAL;
                        }
                        hastype = TRUE;
                        len = newlen;
                    }
                    else if (r == SYM_BIN)
                    {
                        if (exp->m_item.GetSize() > 0)
                        {
                            delete exp;
                            m_err = "found different types in one expression";
                            return ERR_NORMAL;
                        }
                        if ((r = GetBinary(m_bin)) < 0) { delete exp; return r; }
                    }
                    else if (r == SYM_STR)
                    {
                        if (exp->m_item.GetSize() > 0)
                        {
                            delete exp;
                            m_err = "found different types in one expression";
                            return ERR_NORMAL;
                        }
                        if ((r = GetString(m_bin)) < 0) { delete exp; return r; }
                    }
                    else if (r == SYM_NEXT || r == SYM_EXP_END)
                    {
                        break;
                    }
                    else
                    {
                        delete exp;
                        m_err.Format("unknown or bad symbol1 '%s' in expression", (LPCTSTR)str);
                        return ERR_NORMAL;
                    }
                }
                if (exp->m_item.GetSize() <= 0)
                {
                    delete exp;
                }
                else
                {
                    exp->m_size = len;
                    m_exparr.Add(exp);
                    if (len < 0) len = -len;
                    while(len--)
                        m_bin.Add(0);
                }
            }
            while(r != SYM_EXP_END);
            for(int j = m_exparr.GetSize(); i < j; ++i)
                m_exparr[i]->m_self = m_bin.GetSize();
        }
        else
        {
            m_err.Format("unknown or bad symbol2 '%s'", (LPCTSTR)str);
            return ERR_NORMAL;
        }
    }
}

BOOL CTobCompiler::CompilePass2(F_ErrorHandler ErrorHandler)
{
    BOOL haserr = FALSE;
    int i, j, m, n = m_exparr.GetSize();
    int pos, len, factor;
    double v;
    BYTE* b; float f;
    SValueType* val;
    CString err;

    m_line = 0;
    for(i = 0; i < n; ++i)
    {
        v = 0.0;
        factor = 1;
        const SExpression* exp = m_exparr.ElementAt(i);
        m = exp->m_item.GetSize();
        pos = exp->m_pos;
        len = exp->m_size;
        if (len < 0) len = -len;
        for(j = 0; j < m; ++j)
        {
            const CString& str = exp->m_item[j];
            if (str == "+")
            {
                factor = 1;
            }
            else if (str == "-")
            {
                factor = -1;
            }
            else if (str == "@")
            {
                v += exp->m_self * factor;
                factor = 1;
            }
            else
            {
                TCHAR c = str[0];
                if ((c >= '0' && c <= '9') || c == '.')
                {
                    BOOL bHex = (c == '0' && str[1] == 'x');
                    if (bHex)
                        v += strtoul(str, NULL, 16) * factor;
                    else
                        v += atof(str) * factor;
                }
                else
                {
                    if (m_valmap.Lookup(str, val))
                    {
                        v += val->dval * factor;
                        if (val->m_size != -1)
                            len = val->m_size;
                    }
                    else
                    {
                        m_err.Format("not found token '%s' at line %d", (LPCTSTR)str, exp->m_line);
                        haserr = TRUE;
                        if (!(this->*ErrorHandler)(GetErrorString(err)))
                            return FALSE;
                    }
                }
                factor = 1;
            }
        }
        if (exp->m_size > 0)
        {
            m = (int)v;
            b = (BYTE*)&m;
            len = min(len, sizeof(m));
        }
        else if (exp->m_size == -4)
        {
            f = (float)v;
            b = (BYTE*)&f;
            len = min(len, sizeof(f));
        }
        else
        {
            b = (BYTE*)&v;
            len = min(len, sizeof(f));
        }
        memcpy(&m_bin[pos], b, len);
/*
        for(j = len - 1; j >= 0; --j)
            m_bin[pos + j] = b[j];
*/
    }
    return !haserr;
}

BOOL CTobCompiler::CompileFile(LPWSTR fsrcname, LPWSTR fdstname, F_ErrorHandler ErrorHandler)
{
    WChar szOutput[MAX_PATH];
    CString err;
    BOOL haserr = FALSE;

    Reset();

    m_line = 1;

    m_fsrc = _wfopen(fsrcname, L"rb");
    if (!m_fsrc)
    {
        m_err.Format("can't open src file '%S'", fsrcname);
        (this->*ErrorHandler)(GetErrorString(err));
        return FALSE;
    }

    for(;;)
    {
        EToken r = CompilePass1();
        if (r == ERR_EOF)
            break;

        if (r < 0)
        {
            haserr = TRUE;
            if (!(this->*ErrorHandler)(GetErrorString(err)))
                return FALSE;
        }

        if (r == ERR_SEVERE)
            return FALSE;
    }

    fclose(m_fsrc);
    m_fsrc = 0;

    if (!CompilePass2(ErrorHandler) || haserr)
        return FALSE;

    if (fdstname == NULL)
    {
        CByteArray* bin;
        if (m_binmap.Lookup("_FILE", bin) && bin->GetSize() > 0)
        {
            MultiByteToWideChar(
                CP_GB2312,
                0,
                (LPSTR)bin->GetData(),
                bin->GetSize(),
                szOutput,
                countof(szOutput));
            fdstname = szOutput;
        }
        else
        {
            LPWSTR pszExtension;

            lstrcpyW(szOutput, fsrcname);
            pszExtension = findextw(szOutput);
            !lstrcmpiW(pszExtension, L".bin") ? lstrcatW(pszExtension, L".bin") : lstrcpyW(pszExtension, L".bin");
            fdstname = szOutput;
        }
    }

    m_fdst = _wfopen(fdstname, L"wb");
    if (m_fdst == NULL)
    {
        m_err.Format("can't create dst file '%S'", fdstname);
        (this->*ErrorHandler)(GetErrorString(err));
        return FALSE;
    }

    if (m_bin.GetSize() > 0 && fwrite(m_bin.GetData(), m_bin.GetSize(), 1, m_fdst) != 1)
    {
        fclose(m_fdst); m_fdst = 0;
        m_err.Format("can't write dst file '%S'", fdstname);
        (this->*ErrorHandler)(GetErrorString(err));
        return FALSE;
    }

    fclose(m_fdst);
    m_fdst = NULL;

    return TRUE;
}

BOOL CTobCompiler::ErrorHandlerInternal(const CString& err)
{
    if (m_errornum == 0)
        printf("\n");

    printf("%08X: %s\n", ftell(m_fsrc), (LPCTSTR)err);
    if (++m_errornum >= 20)
    {
        printf("(maybe more errors)\n");
        return FALSE;
    }
    return TRUE;
}

ForceInline Int main2(Int argc, WChar **argv)
{
    if (argc == 1)
    {
        printf("ToB (Text of Binary) Compiler 0.3 [by dwing] 2009-02-28\n"
               "Usage: tobc <src_file> [dst_file]\n");
        return 1;
    }

    BOOL   Result;
    WCHAR  szCurPath[MAX_PATH], szScriptPath[MAX_PATH];
    LPWSTR fsrcname, fdstname;

    fsrcname = argv[1];
    fdstname = argc > 2 ? argv[2] : NULL;

    lstrcpyW(szScriptPath, fsrcname);
    rmnamew(szScriptPath);
    GetCurrentDirectoryW(countof(szCurPath), szCurPath);
    SetCurrentDirectoryW(szScriptPath);

    setlocale(LC_CTYPE, ".936");
    printf("Compiling %S ... ", (LPCTSTR)fsrcname);

    CTobCompiler compiler;

    Result = compiler.CompileFile(fsrcname, fdstname, &CTobCompiler::ErrorHandlerInternal);
    SetCurrentDirectoryW(szCurPath);
    if (!Result)
        return -1;

    fdstname = fdstname == NULL ? L"" : fdstname;
    printf("%S OK!\n", (LPCTSTR)fdstname);
    return 0;
}

void __cdecl main(Int argc, WChar **argv)
{
    getargsW(&argc, &argv);
    exit(main2(argc, argv));
}