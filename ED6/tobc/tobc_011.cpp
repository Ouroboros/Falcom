///////////////////////////////////////////////////////////////////////////////
//	tobc.cpp (by dwing) [2007-12-18]
///////////////////////////////////////////////////////////////////////////////
/*
\-以下输出: 12 CD 00 0E 00 00 00 61 62 63 0A 64 65 66 65 65 65
\$n[0a]
\!A(Ａ) 	\-一个字符替换成字符串(括号留空则取消替换)(替换之前判断限制)
\.bit(16)	\-设置偏移地址长度的位数(全局统一值,以最后设置的值为准,只许16或32)
\.maxc(3)	\-限制半角字符在转义符'\'(不包括'\\')之间最长数量(括号留空则无限制)
\.maxw(24)	\-限制全角字符在转义符'\'(不包括'\\')之间最长数量
\.maxs(24)	\-限制任何字符在转义符'\'(不包括'\\')之间最长数量(全角字符计为2)
\.change(1) \-设置是否替换(0:不替换,1:替换)
\.trimleft(0)\-不过滤每行左边的空格或控制符
\[12 cd 00]
\@012@
abc\ndef
\(AAA)		\-不会被替换的范围
\#012#		\-定义标号
*/
///////////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;
typedef unsigned char U8;
typedef unsigned short U16;
///////////////////////////////////////////////////////////////////////////////
class CTobCompiler // NOT object-thread-safe
{
	typedef bool				(*FErrorHandler)(const string &err);
	typedef basic_string<U8>	binstring;
	struct STokenInfo
	{
		string					m_name;
		int 					m_pos;
		int 					m_line;
		STokenInfo(const string &name, int pos, int line):
					m_name(name), m_pos(pos), m_line(line) {}
	};
	int 						m_line;
	ostringstream				m_err;
	binstring					m_bin;
	ifstream					m_fsrc;
	ofstream					m_fdst;
	map<string,binstring>		m_defstr;
	map<string,int> 			m_tab;
	vector<STokenInfo>			m_addr;
	map<U16,string> 			m_change;
	int 						m_bit;
	int 						m_maxc,m_nowc;
	int 						m_maxw,m_noww;
	int 						m_maxs,m_nows;
	bool						m_stat_bin;
	bool						m_stat_def;
	bool						m_stat_change;
	bool						m_ischange;
	bool						m_trimleft;
private:
	void		Reset();
	bool		istokenchar(U8 c) const
	{
		static const U8 s_tokentable[256]=
		{
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // 0x
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // 1x
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // 2x
			1,1,1,1,1,1,1,1, 1,1,0,0,0,0,0,0, // 3x
			0,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // 4x
			1,1,1,1,1,1,1,1, 1,1,1,0,0,0,0,1, // 5x
			0,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, // 6x
			1,1,1,1,1,1,1,1, 1,1,1,0,0,0,0,0, // 7x
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // 8x
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // 9x
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // Ax
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // Bx
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // Cx
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // Dx
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // Ex
			0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, // Fx
		};
		return s_tokentable[c] == 1;
	}
	const U8*	GetString(const U8 *pos, string &str) const;
	void		TrimLine(string &line) const;
	string		GetErrorString();
	bool		CompileLine(const string &line);
	bool		FillAddress(FErrorHandler ErrorHandler);
public:
	bool		Compile(const char *fsrcname,
						const char *fdstname,
						FErrorHandler ErrorHandler);
};
///////////////////////////////////////////////////////////////////////////////
void CTobCompiler::Reset()
{
	m_line = 0;
	m_err.str("");
	m_bin.erase();
	m_fsrc.close();
	m_fsrc.clear();
	m_fdst.close();
	m_fdst.clear();
	m_defstr.clear();
	m_tab.clear();
	m_addr.clear();
	m_change.clear();
	m_bit=32;
	m_maxc=-1; m_nowc=0;
	m_maxw=-1; m_noww=0;
	m_stat_bin = false;
	m_stat_def = false;
	m_stat_change = false;
	m_ischange = false;
	m_trimleft = true;
}
///////////////////////////////////////////////////////////////////////////////
const U8* CTobCompiler::GetString(const U8 *pos, string &str) const
{
	const U8 *p=pos;
	while(istokenchar(*p)) ++p; // read alpha/number string
	str.erase();
	str.append((char*)pos, p-pos);
	return p;
}
///////////////////////////////////////////////////////////////////////////////
void CTobCompiler::TrimLine(string &line) const
{
	int p = 0, q = line.length()-1, t;
	// filter any front char <=0x20
	if(m_trimleft)
	{
		while(p<=q) if((U8)line[p] <= 0x20) ++p; else break;
	}
	// filter any comment after "\-"
	for(t=p; t<q; ++t)
	{
		if(line[t]<0) ++t;
		else if(line[t]=='\\' && line[t+1]=='-') q = t-1;
	}
	// filter any rear char <=0x20
	while(p<=q) if((U8)line[q] <= 0x20) --q; else break;
	if(p>q || p==q && line[p]=='\\') q=p-1;
	line = line.substr(p, q-p+1);
}
///////////////////////////////////////////////////////////////////////////////
string CTobCompiler::GetErrorString()
{
	if(m_err.tellp() < 0) return "";
	ostringstream err;
	err << "ERROR";
	if(m_line>0) err << '(' << m_line << ')';
	err << ": " << m_err.str();
	m_err.str("");
	return err.str();
}
///////////////////////////////////////////////////////////////////////////////
bool CTobCompiler::CompileLine(const string &str)
{
	static const U8 s_hextable[256]=
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
	const U8 *p=(const U8*)(str.c_str());
	U8 half=16;
	string buf;
	binstring bin;
	while(*p)
	{
		if(m_stat_bin)
		{
			if(*p<=0x20);
			else if(*p==']')
			{
				m_stat_bin = false;
				if(half!=16)
				{
					m_err << "found only half hex number before ']'";
					return false;
				}
			}
			else if(s_hextable[*p]==16)
			{
				m_err << "bad hex char 0x" << uppercase << hex << (int)*p;
				return false;
			}
			else
			{
				if(half==16) half = s_hextable[*p];
				else
				{
					half = (half<<4)+s_hextable[*p];
					m_bin.append(&half, 1);
					half = 16;
				}
			}
			++p;
		}
		else if(m_stat_def)
		{
			if(*p<=0x20);
			else if(*p==']')
			{
				m_stat_def = false;
				if(half!=16)
				{
					m_err << "found only half hex number before ']'";
					return false;
				}
				m_defstr.insert(make_pair(buf, bin));
				buf.erase();
				bin.erase();
			}
			else if(s_hextable[*p]==16)
			{
				m_err << "bad hex char 0x" << uppercase << hex << (int)*p;
				return false;
			}
			else
			{
				if(half==16) half = s_hextable[*p];
				else
				{
					half = (half<<4)+s_hextable[*p];
					bin.append(&half, 1);
					half = 16;
				}
			}
			++p;
		}
		else if(m_stat_change)
		{
			if(*p<0x20)
			{
				m_err << "illegal char 0x" << uppercase << hex << p << "in '\\(...)'";
				return false;
			}
			else if(*p<0x80)
			{
				if(*p=='\\')
				{
					if(p[1]<0x20 || p[1]>=0x80)
					{
						m_err << "illegal char 0x" << uppercase << hex << p[1] << "after '\\(...\\'";
						return false;
					}
					++p;
				}
				else if(*p==')') m_stat_change = false;
				else m_bin.append(p, 1);
				p+=1;
			}
			else
			{
				if(p[1]<0x20)
				{
					m_err << "illegal char 0x" << uppercase << hex << p[1] << "in '\\(...)'";
					return false;
				}
				m_bin.append(p, 2);
				p+=2;
			}
		}
		else if(p[0]=='\\')
		{
			switch(p[1])
			{
			case '[': m_stat_bin=true; p+=2; break;
			case '(': m_stat_change=true; p+=2; break;						  
			case '$':
			{
				p=GetString(p+2, buf);
				if(buf.empty())
				{
					m_err << "not found token after '\\$'";
					return false;
				}
				map<string,binstring>::const_iterator it;
				for(it=m_defstr.begin(); it!=m_defstr.end(); ++it)
				{
					int a = it->first.length();
					int b = buf.length();
					if(strncmp(it->first.c_str(), buf.c_str(), a<b?a:b) == 0)
					{
						m_err << "found similar token '" << buf
							  << "' with '" << it->first << '\'';
						return false;
					}
				}
				if(*p!='[')
				{
					m_err << "not found '[' after '\\$" << buf << '\'';
					return false;
				}
				m_stat_def = true;
				++p; break;
			}
			case '!':
			{
				p+=2;
				U16 c=(U16)*p;
				if(c<0x20)
				{
					m_err << "illegal char 0x" << uppercase << hex << c << "after '\\!'";
					return false;
				}
				else if(c>=0x80)
				{
					c=(c<<8)+*++p;
					if(*p<0x20)
					{
						m_err << "illegal char 0x" << uppercase << hex << c << "after '\\!'";
						return false;
					}
				}
				if(*++p!='(')
				{
					if(c<0x100) m_err << "not found '(' after '\\!" << (char)c << '\'';
					else m_err << "not found '(' after '\\!" << (char)p[-2] << (char)p[-1] << '\'';
					return false;
				}
				string s;
				for(++p;;)
				{
					if(*p==0)
					{
						m_err << "not found ')' before end of the line";
						return false;
					}
					if(*p<0x20)
					{
						m_err << "illegal char 0x" << uppercase << hex << p << "after '(...'";
						return false;
					}
					else if(*p<0x80)
					{
						if(*p=='\\')
						{
							if(p[1]<0x20 || p[1]>=0x80)
							{
								m_err << "illegal char 0x" << uppercase << hex << p[1] << "after '(...\\'";
								return false;
							}
							++p;
						}
						else if(*p==')') break;
						s+=(char)*p; p+=1;
					}
					else
					{
						if(p[1]<0x20)
						{
							m_err << "illegal char 0x" << uppercase << hex << p[1] << "after '(...'";
							return false;
						}
						s.append((char*)p,2); p+=2;
					}
				}
				if(s.empty()) m_change.erase(c);
				else m_change.insert(make_pair(c, s));
				++p; break;
			}
			case '#':
			{
				p=GetString(p+2, buf);
				if(buf.empty())
				{
					m_err << "not found token after '\\#'";
					return false;
				}
				if(*p!='#')
				{
					m_err << "not found '#' after '\\#" << buf << '\'';
					return false;
				}
				m_tab.insert(make_pair(buf, m_bin.length()));
				++p; break;
			}
			case '@':
			{
				p=GetString(p+2, buf);
				if(buf.empty())
				{
					m_err << "not found token after '\\#'";
					return false;
				}
				if(*p!='@')
				{
					m_err << "not found '@' after '\\@" << buf << '\'';
					return false;
				}
				STokenInfo ti(buf, m_bin.length(), m_line);
				m_addr.push_back(ti);
				m_bin.append((const U8*)"\0\0\0", m_bit/8);
				++p; break;
			}
			case '.':
			{
				p=GetString(p+2, buf);
				if(buf.empty())
				{
					m_err << "not found keyword after '\\.'";
					return false;
				}
				if(buf == "bit")
				{
					if(*p!='(')
					{
						m_err << "not found '(' after '\\.bit'";
						return false;
					}
					p=GetString(p+1, buf);
					int bit = (buf.empty() ? -1 : atoi(buf.c_str()));
					if(*p!=')')
					{
						m_err << "not found ')' after '\\.bit(" << buf << '\'';
						return false;
					}
					if(!m_addr.empty())
					{
						m_err << "\\.bit(x) must be set before \\@";
						return false;
					}
					if(bit!=16 && bit!=32)
					{
						m_err << "only bit(16) or bit(32) is available";
						return false;
					}
					m_bit = bit;
				}
				else if(buf == "maxc")
				{
					if(*p!='(')
					{
						m_err << "not found '(' after '\\.maxc'";
						return false;
					}
					p=GetString(p+1, buf);
					m_maxc = (buf.empty() ? -1 : atoi(buf.c_str()));
					if(*p!=')')
					{
						m_err << "not found ')' after '\\.maxc(" << buf << '\'';
						return false;
					}
				}
				else if(buf == "maxw")
				{
					if(*p!='(')
					{
						m_err << "not found '(' after '\\.maxw'";
						return false;
					}
					p=GetString(p+1, buf);
					m_maxw = (buf.empty() ? -1 : atoi(buf.c_str()));
					if(*p!=')')
					{
						m_err << "not found ')' after '\\.maxw(" << buf << '\'';
						return false;
					}
				}
				else if(buf == "maxs")
				{
					if(*p!='(')
					{
						m_err << "not found '(' after '\\.maxs'";
						return false;
					}
					p=GetString(p+1, buf);
					m_maxs = (buf.empty() ? -1 : atoi(buf.c_str()));
					if(*p!=')')
					{
						m_err << "not found ')' after '\\.maxs(" << buf << '\'';
						return false;
					}
				}
				else if(buf == "change")
				{
					if(*p!='(')
					{
						m_err << "not found '(' after '\\.change'";
						return false;
					}
					p=GetString(p+1, buf);
					m_ischange=(atoi(buf.c_str()) != 0);
					if(*p!=')')
					{
						m_err << "not found ')' after '\\.change(" << buf << '\'';
						return false;
					}
				}
				else if(buf == "trimleft")
				{
					if(*p!='(')
					{
						m_err << "not found '(' after '\\.trimleft'";
						return false;
					}
					p=GetString(p+1, buf);
					m_trimleft=(atoi(buf.c_str()) != 0);
					if(*p!=')')
					{
						m_err << "not found ')' after '\\.trimleft(" << buf << '\'';
						return false;
					}
				}
				else
				{
					m_err << "unknown keyword '\\." << buf << '\'';
					return false;
				}
				++p; break;
			}
			case '\0': ++p; break;
			case '\\': ++p; goto char_;
			default:
			{
				++p;
				if(!istokenchar(*p)) break;
				string str;
				map<string,binstring>::const_iterator it;
				for(;;)
				{
					str.append((char*)p++, 1);
					it = m_defstr.find(str);
					if(it != m_defstr.end()) break;
					if(!istokenchar(*p))
					{
						m_err << "not defined token '\\" << str << '\'';
						return false;
					}
				}
				m_bin.append(it->second.data(), it->second.length());
			}
			}
			m_nowc = m_noww = m_nows = 0;
		}
		else if(p[0]<0x80)
		{
char_:		if(m_maxc>=0 && (m_nowc+=1) > m_maxc)
			{
				m_err << "exceed .maxc(" << m_maxc << ')';
				return false;
			}
			if(m_maxs>=0 && (m_nows+=1) > m_maxs)
			{
				m_err << "exceed .maxs(" << m_maxs << ')';
				return false;
			}
			if(m_ischange)
			{
				map<U16,string>::const_iterator it=m_change.find((U16)p[0]);
				if(it == m_change.end()) m_bin.append(p, 1);
				else m_bin.append((const U8*)it->second.c_str(), it->second.length());
			}
			else m_bin.append(p, 1);
			++p;
		}
		else
		{
			if(p[1]==0)
			{
				m_err << "found only half wide char at the end";
				return false;
			}
			else if(p[1]<0x20)
			{
				m_err << "illegal char 0x" << uppercase << hex << ((U16)p[0]<<8)+(U16)p[1];
				return false;
			}
			if(m_maxw>=0 && (m_noww+=1) > m_maxw)
			{
				m_err << "exceed .maxw(" << m_maxw << ')';
				return false;
			}
			if(m_maxs>=0 && (m_nows+=2) > m_maxs)
			{
				m_err << "exceed .maxs(" << m_maxs << ')';
				return false;
			}
			if(m_ischange)
			{
				map<U16,string>::const_iterator it=m_change.find(((U16)p[0]<<8)+(U16)p[1]);
				if(it == m_change.end()) m_bin.append(p, 2);
				else m_bin.append((const U8*)it->second.c_str(), it->second.length());
			}
			else m_bin.append(p, 2);
			p+=2;
		}
	}
	if(half!=16)
	{
		m_err << "found only half hex number before end of the line";
		return false;
	}
	return true;
}
///////////////////////////////////////////////////////////////////////////////
bool CTobCompiler::FillAddress(FErrorHandler ErrorHandler)
{
	bool haserr = false;
	vector<STokenInfo>::const_iterator it_addr;
	map<string,int>::const_iterator it_tab;
	for(it_addr=m_addr.begin(); it_addr!=m_addr.end(); ++it_addr)
	{
		it_tab = m_tab.find(it_addr->m_name);
		if(it_tab!=m_tab.end())
		{
			int pos = it_addr->m_pos;
			int val = it_tab->second;
			m_bin[pos  ] =	val 	&255;
			m_bin[pos+1] = (val>> 8)&255;
			if(m_bit==32)
			{
				m_bin[pos+2] = (val>>16)&255;
				m_bin[pos+3] = (val>>24)&255;
			}
			else if(val>=0x10000)
			{
				m_err << "address exceed 0xffff when set bit(16)";
				haserr = true;
				if(!ErrorHandler(GetErrorString())) return false;
			}
		}
		else
		{
			m_err << "not found token '" << it_addr->m_name
				  << "' at line " << it_addr->m_line;
			haserr = true;
			if(!ErrorHandler(GetErrorString())) return false;
		}
	}
	return !haserr;
}
///////////////////////////////////////////////////////////////////////////////
bool CTobCompiler::Compile(const char *fsrcname,
						   const char *fdstname,
						   FErrorHandler ErrorHandler)
{
	Reset();

	m_fsrc.open(fsrcname);
	if(!m_fsrc.is_open())
	{
		m_err << "can't open source file (" << fsrcname << ')';
		m_fsrc.clear();
		ErrorHandler(GetErrorString());
		return false;
	}

	bool haserr = false;
	string line;
	while(getline(m_fsrc, line))
	{
		++m_line;
		TrimLine(line);
		if(!CompileLine(line))
		{
			haserr = true;
			if(!ErrorHandler(GetErrorString())) return false;
			m_nowc = m_noww = m_nows = 0;
		}
	}
	if(!m_fsrc.eof() && m_fsrc.fail())
	{
		m_err << "can't read source file at byte " << (void*)(int)m_fsrc.tellg();
		m_fsrc.close();
		m_fsrc.clear();
		ErrorHandler(GetErrorString());
		return false;
	}
	m_fsrc.close();
	m_fsrc.clear();
	m_line = 0;

	if(!FillAddress(ErrorHandler)) return false;
	if(haserr) return false;

	m_fdst.open(fdstname, ios::out|ios::binary);
	if(!m_fdst.is_open())
	{
		m_err << "can't create destination file (" << fdstname << ')';
		m_fdst.clear();
		ErrorHandler(GetErrorString());
		return false;
	}
	m_fdst.write((char*)m_bin.data(), m_bin.length());
	if(m_fdst.fail())
	{
		m_err << "can't write destination file at byte " << (void*)(int)m_fdst.tellp();
		m_fdst.close();
		m_fdst.clear();
		ErrorHandler(GetErrorString());
		return false;
	}
	m_fdst.close();
	m_fdst.clear();
	return true;
}
///////////////////////////////////////////////////////////////////////////////
bool ErrorHandler(const string &err)
{
	static int errnum = 0;
	if(errnum == 0) cerr << endl;
	cerr << err << endl;
	if(++errnum >= 20)
	{
		cerr << "(maybe more errors)" << endl;
		return false;
	}
	return true;
}
///////////////////////////////////////////////////////////////////////////////
int main(int argc,char *argv[])
{
	if(argc!=2 && argc!=3)
	{
		cerr << "<Text Of Binary Compiler> 0.11 --- by dwing --- 2008-01-19" << endl
			 << "Usage: tobc <source-file> [destination-file]" << endl;
		return 1;
	}

	string fsrcname = argv[1];
	string fdstname;
	if(argc==3) fdstname = argv[2];
	else
	{
		string::size_type i = fsrcname.rfind('.');
		if(i==string::npos) fdstname = fsrcname + ".bin";
		else fdstname = fsrcname.substr(0, i);
	}

	cerr << "Compiling " << fsrcname << " => " << fdstname << " ... ";
	int errnum = 0;
	CTobCompiler compiler;
	if(!compiler.Compile(fsrcname.c_str(), fdstname.c_str(), ErrorHandler)) return -1;
	cerr << "OK!" << endl;
	return 0;
}
///////////////////////////////////////////////////////////////////////////////
