#pragma comment(linker,"/ALIGN:0x1000 /NODEFAULTLIB:LIBC /ENTRY:Entry")
#pragma comment(linker, "/MERGE:.text=.Angel /SECTION:.Angel,ERW")
#pragma comment(linker, "/MERGE:.rdata=.Angel")
#pragma comment(linker, "/MERGE:.data=.Angel")

#define UNICODE
#define _UNICODE

#include <windows.h>
#include <tchar.h>
#include <stdio.h>
#include "Link.h"

char Usage[] = 
"Usage: ZWEI2Scp [-option] input.ext output.ext\n\
	-o Export text from input.ext to output.ext.\n\
	-i Import text from input.ext to output.ext.\n\
	-c Convert Shift-JIS to GBK.\n";
/*
BOOL MByteToWChar(LPCSTR lpcszStr, LPWSTR lpwszStr, DWORD dwSize)
{
    DWORD dwMinSize;
    dwMinSize = MultiByteToWideChar (936, 0, lpcszStr, -1, NULL, 0);
	if(dwSize < dwMinSize)
    {
		return FALSE;
    }
	MultiByteToWideChar (932, 0, lpcszStr, -1, lpwszStr, dwMinSize); 
    return TRUE;
}

BOOL WCharToMByte(LPCWSTR lpcwszStr, LPSTR lpszStr, DWORD dwSize)
{
	DWORD dwMinSize;
	dwMinSize = WideCharToMultiByte(936,NULL,lpcwszStr,-1,NULL,0,NULL,FALSE);
	if(dwSize < dwMinSize)
	{
		return FALSE;
	}
	WideCharToMultiByte(936,NULL,lpcwszStr,-1,lpszStr,dwSize,NULL,FALSE);
	return TRUE;
}
*/
void Scp_ReadFile(Link &Script,FILE *file,BOOL bExport = 0)
{
	char text[1024], *ptext = text;
	unsigned linenum = 0;
	while (1)
	{
		fread(ptext,1,1,file);
		if (feof(file))
			break;
		if (0x0D == *ptext)
		{
			fread(++ptext,1,1,file);
			if (0x0A == *ptext)
			{
				++linenum;
				*++ptext = 0;
				if (bExport == 1)
					for (char *p = text;p != ptext;++p)
					{
						if ((!strncmp(p,"MES(",4) ||
							!strncmp(p,"MES_pos(",8) ||
							!strncmp(p,"chr_rename",10)) &&
							(0x09 == *(p - 1) || 0x0A == *(p - 1)))
							Link_Pushback(Script,linenum,text);
					}
				else
					Link_Pushback(Script,linenum,text);
				ptext = text;
			}
			else
				++ptext;
		}
		else
			++ptext;
	}
}

void main(int argc,TCHAR **argv)
{
	if (argc != 4 || '-' != *argv[1])
	{
		printf(Usage);
		return;
	}
	FILE *inscp = _wfopen(argv[2],__T("rb")),*outscp = NULL;
	if (!inscp)
	{
		printf("Can't open \"%s\".\r\n",argv[2]);
		return;
	}
	Link Script = NULL;
	unsigned linenum = 0;
	switch (towlower(argv[1][1]))
	{
/*	case 'c':{
		Scp_ReadFile(Script,inscp);
		outscp = fopen(argv[3],"wb");
		while (Script)
		{
			wchar_t *wText = new wchar_t[strlen(Script->text) * 2 + 1];
//			for (unsigned ix = 0;ix != strlen(Script->text) +1;++ix)
//				wText[ix] = 0;
//			char sText[1000]= "";
//			strcpy(sText,Script->text);
			if (strncmp(Script->text,"[FILENAME]",10))
			{
				MByteToWChar(Script->text,wText,(strlen(Script->text) * 2 + 1)/sizeof(wText[0]));
				WCharToMByte(wText,Script->text,(strlen(Script->text) + 1)/sizeof(Script->text[0]));
			}
			fprintf(outscp,"%s",Script->text);
//			printf(Script->text);
//			system("pause");
			delete []wText;
			Script = Script->next;
		}
		fclose(inscp);
		fclose(outscp);
		break;}
*/	case 'o':
		outscp = _wfopen(argv[3],__T("ab"));
		Scp_ReadFile(Script,inscp,1);
		while (Script)
		{
			fprintf(outscp,"%u--------%s",Script->line - 1,Script->text);
			Script = Script->next;
		}
		fclose(inscp);
		fclose(outscp);
		break;
	case 'i':{
		Link outScript = NULL;
		outscp = _wfopen(argv[3],__T("rb"));
		if (!outscp)
		{
			printf("Can't open \"%s\".\r\n",argv[3]);
			return;
		}
		fseek(inscp,0,SEEK_END);
		unsigned filesize = ftell(inscp);
		fseek(inscp,0,SEEK_SET);
		char text[1024],*ptext = text;
		while (1)
		{
			while (1)
			{
				fread(ptext,1,1,inscp);
				if (feof(inscp))
					break;
				if (isdigit(*ptext))
					++ptext;
				else
				{
					*ptext = 0;
					linenum = atoi(text);
					while (fread(ptext,1,1,inscp),'-' == *ptext);
					fseek(inscp,-1,SEEK_CUR);
					ptext = text;
					break;
				}
			}
			while (1)
			{
				fread(ptext,1,1,inscp);
				if (feof(inscp))
					break;
				if (0x0D == *ptext)
				{
					fread(++ptext,1,1,inscp);
					if (0x0A == *ptext)
					{
						*++ptext = 0;
						Link_Pushback(Script,linenum,text);
						ptext = text;
						break;
					}
					else
						++ptext;
				}
				else
					++ptext;
			}
			if (ftell(inscp) == filesize)
				break;
		}
		Scp_ReadFile(outScript,outscp);
		fclose(inscp);
		fclose(outscp);
		outscp = _wfopen(argv[3],__T("wb"));
		fseek(outscp,0,SEEK_SET);
		while (outScript)
		{
			if (Script != NULL && (Script->line + 1 == outScript->line))
			{
				fprintf(outscp,"%s",Script->text);
				Script = Script->next;
			}
			else
			{
				fprintf(outscp,"%s",outScript->text);
			}
			outScript = outScript->next;
		}
/*		while (outScript)
		{
			printf("%d\t",outScript->line);
			outScript = outScript->next;
			system("pause");
			printf("%d\t",Script->line);
			system("pause");
			Script = Script->next;
		}
*/		fclose(outscp);
		break;}
	default:wprintf(__T("Unknown option \"%s\".\n"),argv[1]);
			return;
	}
}

void Entry()
{
	int argc;
	TCHAR **argv = CommandLineToArgvW(GetCommandLine(),&argc);
	ExitProcess(main(argc,argv));
}