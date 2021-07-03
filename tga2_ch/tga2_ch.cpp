#pragma comment(linker,"/ENTRY:main")
#pragma comment(lib,"msvcrt6.lib")
#pragma comment(linker, "/MERGE:.text=.index /SECTION:.index,ERW")
#pragma comment(linker, "/MERGE:.data=.index")
#pragma comment(linker, "/MERGE:.rdata=.index")

#include <windows.h>
#include <locale.h>
#include <tchar.h>
#include <stdio.h>
#include <getmainargs.h>

char usage[] = "Usage: tga2_ch 4|5 src.tga dst._ch\n";

void __cdecl main(int argc, TCHAR **argv)
{
	getmainargs(&argc, &argv);
	if (argc != 4)
	{
		printf(usage);
		return;
	}
	register unsigned mode = _ttoi(argv[1]);
	if (mode !=4 && mode !=5)
	{
		printf("Unknown mode \"%d\".\n", mode);
		return;
	}
	FILE *src = _tfopen(argv[2],_T("rb")),
		 *dst = _tfopen(argv[3],_T("wb"));
	if (!src)
	{
		_tprintf(_T("Can't open %s.\n"),argv[2]);
		return;
	}
	if (!dst)
	{
		_tprintf(_T("Can't create %s.\n"),argv[3]);
		return;
	}
	char data[4];
	unsigned vedx,FileSize,Left;
	fseek(src,0xC,SEEK_SET);
	fread(data,4,1,src);
	Left = FileSize = *(unsigned short *)data * (*(unsigned short *)(data +2));
	fseek(src,0x12,SEEK_SET);
	_tprintf(TEXT("%s => %s ... "),argv[2],argv[3]);
	while (Left)
	{
		if (!fread(data,4,1,src))
		{
			break;
		}
		--Left;
		__asm
		{
			mov eax,dword ptr [data];
			mov ecx,eax;
			mov edx,eax;
			cmp mode,4;
			je _4444;
			shr edx,13h;
			shr ecx,0Bh;
			and edx,01Fh;
			and ecx,01Fh;
			shl edx,5h;
			add edx,ecx;
			mov ecx,eax;
			shr ecx,3h;
			shr eax,10h;
			shl edx,5h;
			and ecx,01Fh;
			and eax,8000h;
			jmp end;
_4444:		shr edx,14h;
			shr ecx,0Ch;
			and edx,0Fh;
			and ecx,0Fh;
			shl edx,4h;
			add edx,ecx;
			mov ecx,eax;
			shr ecx,10h;
			shr eax,4h;
			shl edx,4h;
			and ecx,0F000h;
			and eax,0Fh;
end:		add edx,ecx;
			add edx,eax;
			mov vedx,edx;
		}
		fwrite((char *)&vedx,2,1,dst);
	}
	fclose(dst);
	fclose(src);
	printf("done.\n");
}