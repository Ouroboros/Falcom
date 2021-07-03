#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Rimi /SECTION:.Rimi,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Rimi")
#pragma comment(linker,"/MERGE:.data=.Rimi")

#include <Windows.h>
#include <stdio.h>
#include <conio.h>

extern "C" __declspec(dllimport) void __getmainargs(int *argc, char ***argv, char ***envp, int, void *);

void main(int argc, char **argv)
{
	__getmainargs(&argc, &argv, &argv + 3, 0, &argv + 1);

	FILE *fp = fopen(argv[1], "rb");
	if (fp == NULL)
	{
		printf("Open src file error.\n");
		return;
	}

	char	*cBuffer, *p;
	WORD	wItemNum = 0, wItemIndex, wOldItemIndex = 0;
	DWORD	uiFileSize;

	fseek(fp, 0, SEEK_END);
	uiFileSize = ftell(fp);
	fseek(fp, 0, SEEK_SET);

	if (uiFileSize == 0)
	{
		printf("File size = 0.\n");
		return;
	}

	p = cBuffer = (char *)malloc(uiFileSize);
	if (cBuffer == NULL)
	{
		printf("Allocate memory error.\n");
		fclose(fp);
		return;
	}

	fread(cBuffer, uiFileSize, 1, fp);
	wItemNum = ((*(WORD *)cBuffer) >> 1) - 1;
	fclose(fp);

	for (WORD ix = 0; ix != wItemNum; ++ix)
	{
		p = cBuffer + *((WORD *)cBuffer + ix);
		wItemIndex = *(WORD *)p;
		if (wOldItemIndex != 0 && wItemIndex != wOldItemIndex + 1)
		{
			for (WORD ix = wOldItemIndex + 1; ix != wItemIndex; ++ix)
			{
				printf("\"ÎÞ´ËÄ§·¨\", \n");
			}
		}
		p += 4 + 0x18;
		p = cBuffer + *(WORD *)p;
		printf("\"%s\", \n", p);
		wOldItemIndex = wItemIndex;
	}

	free(cBuffer);
	_getch();
}