#pragma comment(linker, "/ENTRY:main")
#pragma comment(lib,"msvcrt6.lib")
#pragma comment(linker, "/MERGE:.text=.Sharu /SECTION:.Sharu,ERW")
#pragma comment(linker, "/MERGE:.rdata=.Sharu")
#pragma comment(linker, "/MERGE:.data=.Sharu")

#include <windows.h>
#include <stdio.h>
#include <getmainargs.h>

char DirHead[] = {0x4C,0x42,0x20,0x44,0x49,0x52,0x1A,0x0},
	 DatHead[] = {0x4C,0x42,0x20,0x44,0x41,0x54,0x1A,0x0};

void main(int argc,char **argv)
{
	getmainargs(&argc, &argv);
	if (3 != argc) return;
	FILE *dat = fopen(argv[1],"rb+"),
		 *import = fopen(argv[2],"rb");
/*	if (!import)
	{
		printf("Can't open %s.\n",argv[2]);
		return;
	}

*/	if (!dat)
	{
		dat = fopen(argv[1],"wb+");
		fwrite(DatHead,sizeof(char),sizeof(DatHead),dat);
		for (unsigned i = 0;i != 8 + 79990;++i)
			fwrite(DatHead + 7,sizeof(char),1,dat);
//		dat = fopen(argv[1],"rb+");
	}
	char *ext = NULL,*name;
	for (name = argv[1] + strlen(argv[1]);(*(name - 1) != '\\')&&name != argv[1];--name)
		if ('.' == *name) ext = name;
	char *dirname = new char[strlen(argv[1]) + 5];
	if (ext)
	{
		strncpy(dirname,argv[1],ext - argv[1]);
		dirname[ext - argv[1]] = 0;
	}
	else
	{
		strncpy(dirname,argv[1],strlen(argv[1]));
		dirname[strlen(argv[1])] = 0;
	}
	strcat(dirname,".dir");
	for (name = argv[2] + strlen(argv[2]);(*(name - 1) != '\\')&&name != argv[2];--name)
		if ('.' == *name) ext = name;
	unsigned DirFileNum;
	unsigned FileSize,LastIndex = 0,CurPos;
	fseek(dat,0,SEEK_END);
	FileSize = ftell(dat);
	FILE *dir = fopen(dirname,"rb+");
	if (!dir)
	{
//		printf("Can't open %s.\n",dirname);
//		return;
		dir = fopen(dirname,"wb+");
		fwrite(DirHead,sizeof(char),sizeof(DirHead),dir);
		for (unsigned i = 0;i != 8;++i)
			fwrite(DirHead + 7,sizeof(char),1,dir);
//		dir = fopen(dirname,"rb+");
//		fseek(dir,0,SEEK_END);
	}
	fseek(dat,0x10,SEEK_SET);
	while (FileSize)
	{
		unsigned ix = getw(dat);
		if (0 == ix)
		{
			fseek(dir,8,SEEK_SET);
			DirFileNum = (unsigned)getw(dir);
			fseek(dir,0,SEEK_END);
			if ((unsigned)((ftell(dir) - 0x10) / 0x24) >= DirFileNum)
				DirFileNum = (unsigned)((ftell(dir) - 0x10) / 0x24 + 1);
			LastIndex = ftell(dat) - 4;
			break;
		}
	}
	fseek(dir,0,SEEK_END);
	fseek(dat,0,SEEK_END);
	if (import)
	{
		fseek(import,0,SEEK_END);
		FileSize = ftell(import);
		fseek(import,0,SEEK_SET);
	}
	else FileSize = 0;
	for (unsigned ix = 0x10 - ftell(dat) % 0x10 + 0x50;import&&ix;--ix)		//ÏòdatÐ´Èë¿ÕÏ¶
		fprintf(dat,"%c",'\0');
	fwrite(name,strlen(name) - (strlen(name) > 12 ? strlen(name) % 12 : 0),1,dir);
	for (unsigned ix = 12 - strlen(name);strlen(name) < 12&&ix != 0;--ix)
		fprintf(dir," ");
	for (unsigned ix = 0;ix != 0x4;++ix)
		fprintf(dir,"%c",'\0');
	putw((unsigned)FileSize,dir);
	for (unsigned ix = 0;ix != 0xC;++ix)
		fprintf(dir,"%c",'\0');
	putw(ftell(dat),dir);
	fseek(dir,8,SEEK_SET);
	putw(DirFileNum,dir);
	fclose(dir);
	if (!import)
	{
		printf("empty file %s.\n",argv[2]);
		return;
	}

	CurPos = ftell(dat);
	fseek(dat,8,SEEK_SET);
	putw((unsigned short)DirFileNum,dat);
	fseek(dat,LastIndex,SEEK_SET);
	putw(CurPos,dat);
	fseek(dat,CurPos,SEEK_SET);

	char *imdata = new char[FileSize];		//Ð´ÈëDAT
	fread(imdata,FileSize,1,import);
	fwrite(imdata,FileSize,1,dat);
	fclose(dat);
}
