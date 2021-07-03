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

#include <afx.h>
#include <afxtempl.h>
#include <afxcoll.h>
#include <stdio.h>

class CTobCompiler    // NOT object-thread-safe
{
public:
    enum EToken
    {
        ERR_SEVERE = -2,    // may not goon
        ERR_NORMAL = -1,    // may goon
        ERR_EOF = 0,        // end of file
        SYM_TOKEN,            // token word
        SYM_INT,            // integer number
        SYM_FLOAT,            // float number
        SYM_DEF,            // @
        SYM_LABEL,            // #
        SYM_BIN,            // [
        SYM_STR,            // ' "
        SYM_EXP_BEGIN,        // (
        SYM_ADD,            // +
        SYM_SUB,            // -
        SYM_TYPE,            // :
        SYM_NEXT,            // ,
        SYM_EXP_END,        // )
        SYM_UNKNWON,
    };
private:
    typedef bool (*F_ErrorHandler)(const CString& err);
    struct SValueType
    {
        double    dval;
        int     ival;
        bool isfloat;
        explicit SValueType(int i) : ival(i), dval(i), isfloat(false) {}
        explicit SValueType(double d) : ival((int)d), dval(d), isfloat(true) {}
    };
    struct SExpression
    {
        CStringArray    m_item;
        int             m_pos;
        int             m_line;
        int             m_size; // 1/2/3/4/-4/-8
        int                m_self;
        SExpression() : m_pos(0), m_line(0), m_self(0) {}
        SExpression(int pos, int line) : m_pos(pos), m_line(line), m_size(4), m_self(0) {}
    };
    static const BYTE                                    ms_tokentable[256];
    static const BYTE                                    ms_hextable[256];
    int                                                 m_line;
    CString                                             m_err;
    CByteArray                                            m_bin;
    FILE*                                                m_fsrc;
    FILE*                                                m_fdst;
    CMap<CString, LPCTSTR, CByteArray*, CByteArray*>    m_binmap;
    CMap<CString, LPCTSTR, SValueType*, SValueType*>    m_valmap;
    CArray<SExpression*, SExpression*>                    m_exparr;
    int                                                 m_defi, m_deff;
private:
    void        Reset();
    CString&    GetErrorString(CString& str);
    EToken        GetToken(CString& str);
    EToken        GetNumber(CString& str);
    EToken        GetString(CByteArray& str);
    EToken        GetBinary(CByteArray& bin);
    EToken        CompilePass1();
    bool        CompilePass2(F_ErrorHandler ErrorHandler);
    static AddMap(CMap<CString, LPCTSTR, CByteArray*, CByteArray*>& m, LPCTSTR k, CByteArray* v)
    {
        CByteArray* v_old;
        if (m.Lookup(k, v_old))
            delete v_old;
        m.SetAt(k, v);
    }
    static AddMap(CMap<CString, LPCTSTR, SValueType*, SValueType*>& m, LPCTSTR k, SValueType* v)
    {
        SValueType* v_old;
        if (m.Lookup(k, v_old))
            delete v_old;
        m.SetAt(k, v);
    }
public:
                CTobCompiler() : m_fsrc(0), m_fdst(0) { Reset(); }
                ~CTobCompiler() { Reset(); }
    bool        CompileFile(const CString& fsrcname, CString& fdstname, F_ErrorHandler ErrorHandler);
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
    2,2,2,2,2,2,2,2, 2,2,0,0,0,0,0,0, // 0x
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

    m_defi = 32;
    m_deff = 32;
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
    bool comment = false;
    str.Empty();
    for(;;)
    {
        int c = fgetc(m_fsrc);
        if (c < 0)
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
            if (c == '\n') { ++m_line; comment = false; }
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
            case ';' : comment = true;    continue;
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
            default:   switch(ms_tokentable[c])
                       {
                       case 0:
                       case 3:    m_err.Format("found invalid char 0x%02X in src file at %p",
                                             c, ftell(m_fsrc)-1); return ERR_NORMAL;
                       case 1:    ret = SYM_TOKEN; break;
                       case 2:    if (fseek(m_fsrc, -1, SEEK_CUR))
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
        str += (TCHAR)c;
    }
}

CTobCompiler::EToken CTobCompiler::GetNumber(CString& str)
{
    bool dot = false, ex = false, number = false;
    str.Empty();
    for(;;)
    {
        int c = fgetc(m_fsrc);
        if (c < 0)
        {
            if (!feof(m_fsrc))
            {
                m_err.Format("can not read src file at %p", ftell(m_fsrc));
                return ERR_SEVERE;
            }
            if (str.IsEmpty()) return ERR_EOF;
            if (!number || ms_tokentable[(BYTE)str[str.GetLength()-1]] != 2)
            {
                m_err = "found bad number";
                return ERR_NORMAL;
            }
            return dot || ex ? SYM_FLOAT : SYM_INT;
        }
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
            dot = true;
        }
        else if (c == 'e' || c == 'E')
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
            if (c != '+' && c != '-') goto begin_;
        }
        else
        {
            switch(ms_tokentable[c])
            {
            case 0: if (c > ' ' && fseek(m_fsrc, -1, SEEK_CUR)) 
                    {
                        m_err.Format("can not seek src file at %p", ftell(m_fsrc));
                        return ERR_SEVERE;
                    }
                    if (!number || ms_tokentable[(BYTE)str[str.GetLength()-1]] != 2)
                    {
                        m_err = "found bad number";
                        return ERR_NORMAL;
                    }
                    return dot || ex ? SYM_FLOAT : SYM_INT;
            case 1: m_err = "found bad number"; return ERR_NORMAL;
            case 2: number = true; break;
            case 3:    m_err.Format("found invalid char 0x%02X in src file at %p",
                                 c, ftell(m_fsrc)-1); return ERR_NORMAL;
            }
        }
        str += (TCHAR)c;
    }
}

CTobCompiler::EToken CTobCompiler::GetBinary(CByteArray& bin)
{
    DWORD cache = 1;
    bool comment = false;
    for(;;)
    {
        int c = fgetc(m_fsrc);
        if (c < 0)
        {
            if (!feof(m_fsrc))
                m_err.Format("can not read src file at %p", ftell(m_fsrc));
            else
                m_err = "not found ']' at the end of src file";
            return ERR_SEVERE;
        }
        if (comment)
        {
            if (c == '\n') { ++m_line; comment = false; }
            continue;
        }
        BYTE half = ms_hextable[c];
        if (half < 16)
        {
            cache = (cache<<4) + half;
            if (cache >= 0x100) { bin.Add((BYTE)cache); cache = 1; }
        }
        else if (c <= ' ') continue;
        else if (c == '\n') ++m_line;
        else if (c == ']')
        {
            if (cache != 1) bin.Add((BYTE)(cache & 0x0f));
            return SYM_BIN;
        }
        else if (c == ';') { comment = true; continue; }
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
                    switch(d)
                    {
                    case '1':
                    case 'b': e = 1; break;
                    case '2':
                    case 's': e = 2; break;
                    case '3':
                    case 't': e = 3; break;
                    case '4':
                    case 'i': e = 4; break;
                    default: m_err.Format("unknown type 0x%02X after ':'", d);
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
            return SYM_STR;
        }
        else if (c == '\\')
        {
            if ((c = fgetc(m_fsrc)) < 0) break;
            switch(c)
            {
            case 'N':
            case 'n': c = '\n';   break;
            case 'R':
            case 'r': c = '\r';   break;
            case 'T':
            case 't': c = '\t';   break;
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
            case 'A':
            case 'a': c = '\x0a'; break;
            case 'B':
            case 'b': c = '\x0b'; break;
            case 'C':
            case 'c': c = '\x0c'; break;
            case 'D':
            case 'd': c = '\x0d'; break;
            case 'E':
            case 'e': c = '\x0e'; break;
            case 'F':
            case 'f': c = '\x0f'; break;
            case 'X':
            case 'x':
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

CTobCompiler::EToken CTobCompiler::CompilePass1()
{
    EToken r;
    CString str, buf;
    CByteArray* bin;
    SValueType* val;
    SExpression* exp;

    for(;;)
    {
        if ((r = GetToken(str)) <= 0) return r;
        if (r == SYM_DEF)
        {
            if (m_bin.GetSize() > 0)
            {
                m_err = "const token can not defined after data";
                return ERR_NORMAL;
            }
            if ((r = GetToken(str)) < 0) return r;
            if (r != SYM_TOKEN)
            {
                m_err = "not found token after '@'";
                return ERR_NORMAL;
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
                val = new SValueType(atoi(buf));
                AddMap(m_valmap, str, val);
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
            if (str == "_DEFI")
            {
                if (r != SYM_INT || val->ival < 1 || val->ival > 4)
                {
                    m_err = "_DEFI must be 1/2/3/4";
                    return ERR_NORMAL;
                }
                m_defi = val->ival;
            }
            else if (str == "_DEFF")
            {
                if (r != SYM_INT || val->ival != 4 && val->ival != 8)
                {
                    m_err = "_DEFF must be 4/8";
                    return ERR_NORMAL;
                }
                m_deff = val->ival;
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
                int len = m_defi; bool hastype = false;
                exp = new SExpression(m_bin.GetSize(), m_line);
                for(;;)
                {
                    if ((r = GetToken(buf)) < 0) { delete exp; return r; }
                    if (r == SYM_TOKEN)
                    {
                        if (!hastype && len > 0 && m_valmap.Lookup(buf, val) && val->isfloat)
                            len = -m_deff;
                        exp->m_item.Add(buf);
                    }
                    else if (r == SYM_ADD)
                        exp->m_item.Add("+");
                    else if (r == SYM_SUB)
                        exp->m_item.Add("-");
                    else if (r == SYM_DEF)
                        exp->m_item.Add("@");
                    else if (r == SYM_INT)
                        exp->m_item.Add(buf);
                    else if (r == SYM_FLOAT)
                    {
                        if (!hastype && len > 0)
                            len = -m_deff;
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
                        switch(buf[0])
                        {
                        case '1':
                        case 'b': newlen = 1; break;
                        case '2':
                        case 's': newlen = 2; break;
                        case '3':
                        case 't': newlen = 3; break;
                        case '4':
                        case 'i': newlen = 4; break;
                        case 'f': newlen = -4; break;
                        case 'd': newlen = -8; break;
                        default: delete exp;
                                 m_err.Format("unknown type 0x%02X after ':'", buf[0]);
                                 return ERR_NORMAL;
                        }
                        if (hastype && newlen != len)
                        {
                            delete exp;
                            m_err = "found different types in one expression";
                            return ERR_NORMAL;
                        }
                        hastype = true;
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
                        break;
                    else
                    {
                        delete exp;
                        m_err.Format("unknown or bad symbol '%s' in expression", (LPCTSTR)str);
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
                    while(len--) m_bin.Add(0);
                }
            }
            while(r != SYM_EXP_END);
            for(int j = m_exparr.GetSize(); i < j; ++i)
                m_exparr[i]->m_self = m_bin.GetSize();
        }
        else
        {
            m_err.Format("unknown or bad symbol '%s'", (LPCTSTR)str);
            return ERR_NORMAL;
        }
    }
}

bool CTobCompiler::CompilePass2(F_ErrorHandler ErrorHandler)
{
    bool haserr = false;
    int i, j, m, n = m_exparr.GetSize();
    int pos, len, factor; double v; BYTE* b; float f;
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
                factor = 1;
            else if (str == "-")
                factor = -1;
            else if (str == "@")
            {
                v += exp->m_self * factor;
                factor = 1;
            }
            else
            {
                TCHAR c = str[0];
                if (c >= '0' && c <= '9' || c == '.')
                    v += atof(str) * factor;
                else
                {
                    if (m_valmap.Lookup(str, val))
                        v += val->dval * factor;
                    else
                    {
                        m_err.Format("not found token '%s' at line %d", (LPCTSTR)str, exp->m_line);
                        haserr = true;
                        if (!ErrorHandler(GetErrorString(err))) return false;
                    }
                }
                factor = 1;
            }
        }
        if (exp->m_size > 0)
        {
            m = (int)v;
            b = (BYTE*)&m;
        }
        else if (exp->m_size == -4)
        {
            f = (float)v;
            b = (BYTE*)&f;
        }
        else
        {
            b = (BYTE*)&v;
        }
        for(j = len - 1; j >= 0; --j)
            m_bin[pos + j] = b[j];
    }
    return !haserr;
}

bool CTobCompiler::CompileFile(const CString& fsrcname, CString& fdstname, F_ErrorHandler ErrorHandler)
{
    Reset();
    CString err;
    bool haserr = false;
    m_line = 1;

    m_fsrc = fopen(fsrcname, "rb");
    if (!m_fsrc)
    {
        m_err.Format("can't open src file '%s'", fsrcname);
        ErrorHandler(GetErrorString(err));
        return false;
    }
    for(;;)
    {
        EToken r = CompilePass1();
        if (r == ERR_EOF) break;
        if (r < 0)
        {
            haserr = true;
            if (!ErrorHandler(GetErrorString(err))) return false;
        }
        if (r == ERR_SEVERE) return false;
    }
    fclose(m_fsrc); m_fsrc = 0;

    if (!CompilePass2(ErrorHandler) || haserr) return false;

    if (fdstname.IsEmpty())
    {
        CByteArray* bin;
        if (m_binmap.Lookup("_FILE", bin) && bin->GetSize() > 0)
        {
            CopyMemory(fdstname.GetBuffer(bin->GetSize() + 1), bin->GetData(), bin->GetSize());
            fdstname.ReleaseBuffer(bin->GetSize());
        }
        else
        {
            int i = fsrcname.ReverseFind('.');
            if (i < 0) fdstname = fsrcname + ".bin";
            else fdstname = fsrcname.Mid(0, i);
        }
        if (fdstname.IsEmpty()) fdstname = "out.bin";
    }

    m_fdst = fopen(fdstname, "wb");
    if (!m_fdst)
    {
        m_err.Format("can't create dst file '%s'", fdstname);
        ErrorHandler(GetErrorString(err));
        return false;
    }
    if (m_bin.GetSize() > 0 && fwrite(m_bin.GetData(), m_bin.GetSize(), 1, m_fdst) != 1)
    {
        fclose(m_fdst); m_fdst = 0;
        m_err.Format("can't write dst file '%s'", fdstname);
        ErrorHandler(GetErrorString(err));
        return false;
    }
    fclose(m_fdst); m_fdst = 0;
    return true;
}

bool ErrorHandler(const CString& err)
{
    static int errnum = 0;
    if (errnum == 0) printf("\n");
    printf("%s\n", (LPCTSTR)err);
    if (++errnum >= 20)
    {
        printf("(maybe more errors)\n");
        return false;
    }
    return true;
}

int main(int argc, char** argv)
{
    if (argc != 2 && argc != 3)
    {
        printf("ToB (Text of Binary) Compiler 0.3 [by dwing] 2009-02-28\n"
               "Usage: tobc <src_file> [dst_file]\n");
        return 1;
    }

    CString fsrcname = argv[1];
    CString fdstname;
    fsrcname.TrimLeft();
    fsrcname.TrimRight();
    if (argc == 3)
    {
        fdstname = argv[2];
        fdstname.TrimLeft();
        fdstname.TrimRight();
    }

    printf("Compiling %s ... ", (LPCTSTR)fsrcname);
    CTobCompiler compiler;
    if (!compiler.CompileFile(fsrcname, fdstname, ErrorHandler)) return -1;
    printf("%s OK!\n", (LPCTSTR)fdstname);
    return 0;
}
