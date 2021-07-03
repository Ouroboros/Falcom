///////////////////////////////////////////////////////////////////////////////
//	tobc.cpp (by dwing) [2009-02-17]
///////////////////////////////////////////////////////////////////////////////
/*
;以下输出: 12 CD 00 11 00 00 00 61 62 63 01 64 65 66 41 41 41 00
.bit 32,32	;设置偏移地址长度的位数(全局统一值,以最后设置为准,只许8/16/24/32/48/64,32/64)
.maxc 6 	;限制半角字符在双引号或控制符(未替换)之间最长数量(赋值-1表示无限)
.maxw 24	;限制全角字符在双引号或控制符(未替换)之间最长数量
.maxs 24	;限制任何字符在双引号或控制符(未替换)之间最长数量(全角字符计为2)
.def end [00]
.change '\r' [] ;单引号的字符串忽略任何控制符(不含转义符),
.change '\n' [01]			  ;忽略字符替换,不受max长度限制
.change 'A' 'Ａ';一个字符替换成字符串(括号留空则取消替换)(替换之前判断限制)
[12 cd 00] @012
"abc
def"		;如果字符串两边同时用单引号和双引号,则在结尾加\0(对于.change无效)
'AAA'		;不会被替换的范围
#012		;定义标号
end
*/

#include <afx.h>
#include <afxtempl.h>
#include <afxcoll.h>
#include <stdio.h>
typedef unsigned char	U8;
typedef unsigned short	U16;
typedef unsigned int	U32;

class CTobCompiler	// NOT object-thread-safe
{
public:
	enum EType
	{
		TYPE_UNKNOWN = 0,	// unknown
		TYPE_BYTE,			// 1 byte integer
		TYPE_WORD,			// 2 byte integer
		TYPE_TRI,			// 3 byte integer
		TYPE_INT,			// 4 byte integer
		TYPE_HEX,			// 6 byte integer
		TYPE_QUAD,			// 8 byte integer
		TYPE_FLOAT, 		// 4 byte float
		TYPE_DOUBLE,		// 8 byte float
	};
private:
	enum EToken
	{
		ERR_SEVERE = -2,	// may not goon
		ERR_NORMAL = -1,	// may goon
		ERR_EOF = 0,		// end of file
		SYM_TOKEN,			// token word
		SYM_NUM,			// number
		SYM_KEY,			// .
		SYM_BIN,			// [
		SYM_STR,			// '
		SYM_STRING, 		// "
		SYM_LABEL,			// #
		SYM_ADDR,			// @
		SYM_EXP_BEGIN,		// (
		SYM_ADD,			// +
		SYM_SUB,			// -
		SYM_TYPE,			// :
		SYM_NEXT,			// ,
		SYM_EXP_END,		// )
	};
	typedef bool (*F_ErrorHandler)(const CString& err);
	struct SExpInfo
	{
		CStringArray	m_item;
		int 			m_pos;
		int 			m_line;
		EType			m_type;
		SExpInfo() : m_pos(0), m_line(0), m_type(TYPE_UNKNOWN) {}
		SExpInfo(int pos, int line) : m_pos(pos), m_line(line), m_type(TYPE_UNKNOWN) {}
	};
	static const U8 					ms_tokentable[256];
	static const U8 					ms_hextable[256];
	int 								m_line;
	CString 							m_err;
	CByteArray							m_bin;
	FILE*								m_fsrc;
	FILE*								m_fdst;
	CMap<CString, LPCTSTR, CByteArray*, CByteArray*> m_defbin;
	CMap<CString, LPCTSTR, int, int>	m_label;
	CArray<SExpInfo*, SExpInfo*>		m_exp;
	CMap<U16, U16, CString, LPCTSTR>	m_change;
	int 								m_bit_i;
	int 								m_bit_f;
	int 								m_maxc;
	int 								m_maxw;
	int 								m_maxs;
private:
	void		Reset();
	CString&	GetErrorString(CString& str);
	EToken		GetToken(CString& str);
	EToken		GetString(CString& str, bool change = false);
	EToken		GetBinary(CByteArray& bin);
	EToken		CompilePass1();
	bool		CompilePass2(F_ErrorHandler ErrorHandler);
public:
				CTobCompiler() : m_fsrc(0), m_fdst(0) { Reset(); }
				~CTobCompiler() { Reset(); }
	bool		CompileFile(LPCTSTR fsrcname, LPCTSTR fdstname, F_ErrorHandler ErrorHandler);
};

const U8 CTobCompiler::ms_tokentable[256] =	// 数字,字母,_,$
{
	3,3,3,3,3,3,3,3, 3,0,0,3,3,0,3,3, // 0x
	3,3,3,3,3,3,3,3, 3,3,3,3,3,3,3,3, // 1x
	0,0,0,0,1,0,0,0, 0,0,0,0,0,0,0,0, // 2x
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

const U8 CTobCompiler::ms_hextable[256] =
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
	if(m_fsrc) { fclose(m_fsrc); m_fsrc = 0; }
	if(m_fdst) { fclose(m_fdst); m_fdst = 0; }

	POSITION p = m_defbin.GetStartPosition();
	CString str;
	CByteArray* bin;
	while(p)
	{
		m_defbin.GetNextAssoc(p, str, bin);
		delete bin;
	}
	m_defbin.RemoveAll();
	m_defbin.InitHashTable(251);

	m_label.RemoveAll();
	m_label.InitHashTable(251);
	for(int i = m_exp.GetSize() - 1; i >= 0; --i)
		delete m_exp.GetAt(i);
	m_exp.RemoveAll();
	m_change.RemoveAll();
	m_change.InitHashTable(251);
	m_bit_i = 32;
	m_bit_f = 32;
	m_maxc = -1;
	m_maxw = -1;
	m_maxs = -1;
}

CString& CTobCompiler::GetErrorString(CString& str)
{
	if(m_line > 0)	str.Format("ERROR(%d): %s", m_line, (LPCTSTR)m_err);
	else			str.Format("ERROR: %s", (LPCTSTR)m_err);
	m_err.Empty();
	return str;
}

CTobCompiler::EToken CTobCompiler::GetToken(CString& str)
{
	EToken ret = ERR_EOF;
	bool comment = false;
	str.Empty();
	for(;;)
	{
		int c = fgetc(m_fsrc);
		if(c < 0)
		{
			if(!feof(m_fsrc))
			{
				m_err.Format("can not read src file at %p", ftell(m_fsrc));
				return ERR_SEVERE;
			}
			return str.IsEmpty() ? ERR_EOF : ret;
		}
		if(comment)
		{
			if(c == '\n') { ++m_line; comment = false; }
			continue;
		}
		if(ret == ERR_EOF)
		{
			switch(c)
			{
			case '\n': ++m_line;		continue;
			case ';' : comment = true;	continue;
			case '.' : return SYM_KEY;
			case '#' : return SYM_LABEL;
			case '[' : return SYM_BIN;
			case '\'': return SYM_STR;
			case '\"': return SYM_STRING;
			case '@' : return SYM_ADDR;
			case '(' : return SYM_EXP_BEGIN;
			case '+' : return SYM_ADD;
			case '-' : return SYM_SUB;
			case ':' : return SYM_TYPE;
			case ',' : return SYM_NEXT;
			case ')' : return SYM_EXP_END;
			default:   switch(ms_tokentable[c])
					   {
					   case 1:  ret = SYM_TOKEN; break;
					   case 2:  ret = SYM_NUM;   break;
					   case 3:  m_err.Format("found invalid char 0x%02X in src file at %p",
											 c, ftell(m_fsrc)); return ERR_NORMAL;
					   default: continue;
					   }
			}
		}
		else if(!ms_tokentable[c])
		{
			if(fseek(m_fsrc, -1, SEEK_CUR))
			{
				m_err.Format("can not seek src file at %p", ftell(m_fsrc));
				return ERR_SEVERE;
			}
			return ret;
		}
		if(c >= 0x81)
		{
			str += c;
			c = fgetc(m_fsrc);
			if(c < 0)
			{
				if(!feof(m_fsrc))
					m_err.Format("can not read src file at %p", ftell(m_fsrc));
				else
					m_err = "found half wide char at the end of src file";
				return ERR_SEVERE;
			}
			if(c < 0x40)
			{
				if(fseek(m_fsrc, -1, SEEK_CUR))
				{
					m_err.Format("can not seek src file at %p", ftell(m_fsrc));
					return ERR_SEVERE;
				}
				m_err.Format("found half wide char in src file at %p", ftell(m_fsrc));
				return ERR_NORMAL;
			}
		}
		else if(ret == SYM_NUM && ms_tokentable[c] == 1)
			ret = SYM_TOKEN;
		str += c;
	}
}

CTobCompiler::EToken CTobCompiler::GetBinary(CByteArray& bin)
{
	U32 cache = 1;
	bool comment = false;
	for(;;)
	{
		int c = fgetc(m_fsrc);
		if(c<0)
		{
			if(!feof(m_fsrc))
				m_err.Format("can not read src file at %p", ftell(m_fsrc));
			else
				m_err = "not found ']' at the end of src file";
			return ERR_SEVERE;
		}
		if(comment)
		{
			if(c == '\n') { ++m_line; comment = false; }
			continue;
		}
		U8 half = ms_hextable[c];
		if(half < 16)
		{
			cache = (cache<<4) + half;
			if(cache >= 0x100) { bin.Add((U8)cache); cache = 1; }
		}
		else if(c == '\n') ++m_line;
		else if(c <= ' ') continue;
		else if(c == ']')
		{
			if(cache != 1) bin.Add((U8)cache & 0x0f);
			return SYM_BIN;
		}
		else if(c == ';') { comment = true; continue; }
		else
		{
			m_err.Format("bad hex char 0x%02X", c);
			return ERR_NORMAL;
		}
	}
}

// 返回SYM_STR表示不加"\0",否则加"\0"
CTobCompiler::EToken CTobCompiler::GetString(CString& str, bool change)
{
	str.Empty();
	int c, d;
	int numc = 0;
	int numw = 0;
	int nums = 0;
	CString chg;
	for(;;)
	{
		if((c = fgetc(m_fsrc)) < 0) break;
		if(c == '\n') ++m_line;
		if(!change && c < ' ') continue;
		if(c == '\'')
		{
			return change ? SYM_STRING : SYM_STR;
		}
		else if(c == '"')
		{
			if(change)
			{
				if(m_maxc >= 0 && numc > m_maxc)
				{
					m_err.Format("exceed '.maxc %d' < %d", m_maxc, numc);
					return ERR_NORMAL;
				}
				if(m_maxw >= 0 && numw > m_maxw)
				{
					m_err.Format("exceed '.maxw %d' < %d", m_maxw, numw);
					return ERR_NORMAL;
				}
				if(m_maxs >= 0 && nums > m_maxs)
				{
					m_err.Format("exceed '.maxs %d' < %d", m_maxs, nums);
					return ERR_NORMAL;
				}
			}
			return change ? SYM_STR : SYM_STRING;
		}
		else if(c == '\\')
		{
			if((c = fgetc(m_fsrc)) < 0) break;
			switch(c)
			{
			case 'n': c = '\n';   break;
			case 'r': c = '\r';   break;
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
			}
		}
		if(c >= 0x80)
		{
			if((d = fgetc(m_fsrc)) < 0) break;
			if(d < 0x40)
			{
				if(fseek(m_fsrc, -1, SEEK_CUR))
				{
					m_err.Format("can not seek src file at %p", ftell(m_fsrc));
					return ERR_SEVERE;
				}
				m_err.Format("found half wide char at %p", ftell(m_fsrc));
				return ERR_NORMAL;
			}
			if(change && m_change.Lookup(((U16)c<<16) + d, chg))
			{
				str += chg;
			}
			else
			{
				str += (TCHAR)c;
				str += (TCHAR)d;
			}
			numw += 1;
			nums += 2;
		}
		else
		{
			if(change && m_change.Lookup((U16)c, chg))
			{
				str += chg;
			}
			else
			{
				str += (TCHAR)c;
			}
			if(c >= ' ')
			{
				numc += 1;
				nums += 1;
			}
			else numc = numw = nums = 0;
		}
	}
	if(!feof(m_fsrc))
		m_err.Format("can not read src file at %p", ftell(m_fsrc));
	else if(!change)
		m_err = "not found ''' at the end of src file";
	else
		m_err = "not found '\"' at the end of src file";
	return ERR_SEVERE;
}

CTobCompiler::EToken CTobCompiler::CompilePass1()
{
	EToken r;
	CString str, buf;
	CByteArray* bin = 0;

	for(;;)
	{
		if((r = GetToken(str)) <= 0) return r;
		if(r == SYM_KEY)
		{
			if((r = GetToken(str)) < 0) return r;
			if(r != SYM_TOKEN)
			{
				m_err = "not found keyword after '.'";
				return ERR_NORMAL;
			}
			if(str == "def")
			{
				if((r = GetToken(str)) < 0) return r;
				if(r != SYM_TOKEN)
				{
					m_err = "not found token after '.def'";
					return ERR_NORMAL;
				}
				if((r = GetToken(buf)) < 0) return r;
				if(r == SYM_BIN)
				{
					bin = new CByteArray;
					if((r = GetBinary(*bin)) < 0) { delete bin; return r; }
				}
				else if(r == SYM_STR)
				{
					if((r = GetString(buf, false)) < 0) return r;
					bin = new CByteArray;
					for(LPCTSTR p = buf; *p; ++p) bin->Add(*(U8*)p);
					if(r == SYM_STRING) bin->Add(0);
				}
				else if(r == SYM_STRING)
				{
					if((r = GetString(buf, true)) < 0) return r;
					bin = new CByteArray;
					for(LPCTSTR p = buf; *p; ++p) bin->Add(*(U8*)p);
					if(r == SYM_STRING) bin->Add(0);
				}
				else
				{
					m_err = "not found '[' or ''' or '\"' after '.def <token>''";
					return ERR_NORMAL;
				}
				m_defbin.SetAt(str, bin);
				bin = 0;
			}
			else if(str == "change")
			{
				if((r = GetToken(str)) < 0) return r;
				if(r != SYM_STR)
				{
					m_err = "not found ''' after '.change'";
					return ERR_NORMAL;
				}
				if((r = GetString(str, false)) < 0) return r;
				if( str.IsEmpty() || str.GetLength()>2 || str.GetLength() == 2 && (U8)str[0]<0x80)
				{
					m_err = "only one character is allowed after '.change'";
					return ERR_NORMAL;
				}
				U16 c = (U8)str[0];
				if(str.GetLength() == 2) c = (c<<8) + (U8)str[1];
				if((r = GetToken(str)) < 0) return r;
				if(r == SYM_BIN)
				{
					CByteArray tmp;
					if((r = GetBinary(tmp)) < 0) return r;
					buf.Empty();
					int i, n = tmp.GetSize();
					for(i = 0; i < n; ++i)
					{
						U8 b = tmp.GetAt(i);
						if(!b) break;
						buf += (TCHAR)b;
					}
				}
				else if(r == SYM_STR)
				{
					if((r = GetString(buf, false)) < 0) return r;
				}
				else if(r == SYM_STRING)
				{
					if((r = GetString(buf, true)) < 0) return r;
				}
				else
				{
					m_err = "not found ''' or '\"' after '.change <char>'";
					return ERR_NORMAL;
				}
				m_change.SetAt(c, buf);
			}
			else if(str == "bit")
			{
				if((r = GetToken(str)) < 0) return r;
				if(r != SYM_TOKEN)
				{
					m_err = "not found parameter after '.bit'";
					return ERR_NORMAL;
				}
				int bit = atoi(str);
				if(bit!=8 && bit!=16 && bit!=24 && bit!=32)
				{
					m_err = "only '.bit 8/16/24/32' is available";
					return ERR_NORMAL;
				}
				m_bit_i = bit;
			}
			else if(str == "maxc")
			{
				if((r = GetToken(str)) < 0) return r;
				if(r != SYM_TOKEN)
				{
					m_err = "not found parameter after '.maxc'";
					return ERR_NORMAL;
				}
				m_maxc = atoi(str);
			}
			else if(str == "maxw")
			{
				if((r = GetToken(str)) < 0) return r;
				if(r != SYM_TOKEN)
				{
					m_err = "not found parameter after '.maxw'";
					return ERR_NORMAL;
				}
				m_maxw = atoi(str);
			}
			else if(str == "maxs")
			{
				if((r = GetToken(str)) < 0) return r;
				if(r != SYM_TOKEN)
				{
					m_err = "not found parameter after '.maxs'";
					return ERR_NORMAL;
				}
				m_maxs = atoi(str);
			}
			else
			{
				m_err.Format("unknwon keyword '%s' after '.'", (LPCTSTR)str);
				return ERR_NORMAL;
			}
		}
		else if(r == SYM_BIN)
		{
			if((r = GetBinary(m_bin)) < 0) return r;
		}
		else if(r == SYM_STR)
		{
			if((r = GetString(buf, false)) < 0) return r;
			for(LPCTSTR p=buf;* p; ++p) m_bin.Add(*(U8*)p);
			if(r == SYM_STRING) m_bin.Add(0);
		}
		else if(r == SYM_STRING)
		{
			if((r = GetString(buf, true)) < 0) return r;
			for(LPCTSTR p=buf;* p; ++p) m_bin.Add(*(U8*)p);
			if(r == SYM_STRING) m_bin.Add(0);
		}
		else if(r == SYM_TOKEN)
		{
			if(!m_defbin.Lookup(str, bin))
			{
				m_err.Format("not defined token '%s'", (LPCTSTR)str);
				return ERR_NORMAL;
			}
			m_bin.Append(*bin);
			bin = 0;
		}
		else if(r == SYM_ADDR)
		{
			if((r = GetToken(str)) < 0)
				return r;
			SExpInfo* ti = new SExpInfo(m_bin.GetSize(), m_line);
			if(r == SYM_EXP_BEGIN)
			{
				for(;;)
				{
					if((r = GetToken(buf)) < 0)
					{
						delete ti;
						return r;
					}
					if(r == SYM_TOKEN || r == SYM_NUM)
						ti->m_item.Add(buf);
					else if(r == SYM_ADD)
						ti->m_item.Add("+");
					else if(r == SYM_SUB)
						ti->m_item.Add("-");
					else if(r == SYM_ADDR)
						ti->m_item.Add("@");
					else if(r == SYM_EXP_END)
						break;
					else
					{
						delete ti;
						m_err.Format("found unknown token '%s' in expression", (LPCTSTR)buf);
						return ERR_NORMAL;
					}
				}
			}
			else if(r == SYM_TOKEN)
				ti->m_item.Add(str);
			else
			{
				delete ti;
				m_err = "not found token or expression after '@'";
				return ERR_NORMAL;
			}
			m_exp.Add(ti);
			for(int i = m_bit_i/8; i--;)
				m_bin.Add(0);
		}
		else if(r == SYM_LABEL)
		{
			if((r = GetToken(str)) < 0) return r;
			if(r != SYM_TOKEN)
			{
				m_err = "not found label after '#'";
				return ERR_NORMAL;
			}
			m_label.SetAt(str, m_bin.GetSize());
		}
		else
		{
			m_err = "unknown or bad symbol";
			return ERR_NORMAL;
		}
	}
}

bool CTobCompiler::CompilePass2(F_ErrorHandler ErrorHandler)
{
	bool haserr = false;
	int i, j, m, n = m_exp.GetSize();
	int pos, val, temp, factor;
	int len = m_bin.GetSize();
	CString err;
	m_line = 0;
	for(i = 0; i < n; ++i)
	{
		val = 0;
		factor = 1;
		const SExpInfo* ti = m_exp.ElementAt(i);
		m = ti->m_item.GetSize();
		pos = ti->m_pos;
		for(j = 0; j < m; ++j)
		{
			CString& str = ti->m_item[j];
			if(str == "+")
				factor = 1;
			else if(str == "-")
				factor = -1;
			else if(str == "@")
			{
				val += (pos + m_bit_i/8) * factor;
				factor = 1;
			}
			else
			{
				char c = str[0];
				if(c == '$')
				{
					str.Delete(0);
					c = str[0];
				}
				if(c >= '0' && c <= '9')
					val += atoi(str) * factor;
				else
				{
					if(m_label.Lookup(str, temp))
						val += temp * factor;
					else
					{
						m_err.Format("not found token '%s' at line %d", (LPCTSTR)str, ti->m_line);
						haserr = true;
						if(!ErrorHandler(GetErrorString(err))) return false;
					}
				}
				factor = 1;
			}
		}
		if(pos + m_bit_i/8 > len)
		{
			m_err.Format("internal compiler error %d > %d", pos + m_bit_i/8, len);
			haserr = true;
			ErrorHandler(GetErrorString(err));
			return false;
		}
		if(m_bit_i < 32 && val >= (1<<m_bit_i))
		{
			m_err.Format("overflow address (%p) when setting '.bit %u'", val, m_bit_i);
			haserr = true;
			if(!ErrorHandler(GetErrorString(err))) return false;
		}
						  m_bin[pos    ] =	val 	   & 255;
		if(m_bit_i >= 16) m_bin[pos + 1] = (val >>	8) & 255;
		if(m_bit_i >= 24) m_bin[pos + 2] = (val >> 16) & 255;
		if(m_bit_i >= 32) m_bin[pos + 3] =	val >> 24;
	}
	return !haserr;
}

bool CTobCompiler::CompileFile(LPCTSTR fsrcname, LPCTSTR fdstname, F_ErrorHandler ErrorHandler)
{
	Reset();
	CString err;
	bool haserr = false;
	m_line = 1;

	m_fsrc = fopen(fsrcname, "rb");
	if(!m_fsrc)
	{
		m_err.Format("can't open src file '%s'", fsrcname);
		ErrorHandler(GetErrorString(err));
		return false;
	}
	for(;;)
	{
		EToken r = CompilePass1();
		if(r == ERR_EOF) break;
		if(r < 0)
		{
			haserr = true;
			if(!ErrorHandler(GetErrorString(err))) return false;
		}
		if(r == ERR_SEVERE) return false;
	}
	fclose(m_fsrc); m_fsrc = 0;

	if(!CompilePass2(ErrorHandler) || haserr) return false;

	m_fdst = fopen(fdstname, "wb");
	if(!m_fdst)
	{
		m_err.Format("can't create dst file '%s'", fdstname);
		ErrorHandler(GetErrorString(err));
		return false;
	}
	if(m_bin.GetSize() > 0 && fwrite(m_bin.GetData(), m_bin.GetSize(), 1, m_fdst) != 1)
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
	if(errnum == 0) printf("\n");
	printf("%s\n", (LPCTSTR)err);
	if(++errnum >= 20)
	{
		printf("(maybe more errors)\n");
		return false;
	}
	return true;
}

int main(int argc, char** argv)
{
	if(argc != 2 && argc != 3)
	{
		printf("ToB (Text of Binary) Compiler 0.23 [by dwing] 2009-02-17\n"
			   "Usage: tobc <src_file> [dst_file]\n");
		return 1;
	}

	CString fsrcname = argv[1];
	CString fdstname;
	fsrcname.TrimLeft();
	fsrcname.TrimRight();
	if(argc == 3)
	{
		fdstname = argv[2];
		fdstname.TrimLeft();
		fdstname.TrimRight();
	}
	else
	{
		int i = fsrcname.ReverseFind('.');
		if(i < 0) fdstname = fsrcname + ".bin";
		else fdstname = fsrcname.Mid(0, i);
	}
	if(fdstname.IsEmpty()) fdstname = "out.bin";

	printf("Compiling %s => %s ... ", (LPCTSTR)fsrcname, (LPCTSTR)fdstname);
	CTobCompiler compiler;
	if(!compiler.CompileFile(fsrcname, fdstname, ErrorHandler)) return -1;
	printf("OK!\n");
	return 0;
}
