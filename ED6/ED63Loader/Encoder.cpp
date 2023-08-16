#pragma comment(linker, "/ENTRY:main")
#pragma comment(lib, "Shlwapi.lib ")
#pragma comment(linker,"/MERGE:.text=.Kaede /SECTION:.Kaede,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kaede")
#pragma comment(linker,"/MERGE:.data=.Kaede")

#include <Shlwapi.h>
#include "my_headers.h"

#include "LZMA/7zVersion.h"
#include "LZMA/Alloc.h"
#include "LZMA/Lzma86.h"

void main(int argc, char **argv)
{
	getargs(&argc, &argv);
	if (argc < 3)
	{
		return;
	}

	FILE *fp = fopen(argv[1], "rb");
	if (fp == NULL)
	{
		printf("open src error.\n");
		return;
	}

	SizeT fileSize, outsize;
	fseek(fp, 0, SEEK_END);
	fileSize = ftell(fp);
	fseek(fp, 0, SEEK_SET);
	outsize = fileSize / 20 * 21 + (1 << 16) + 4;

	unsigned int iAddress;
//	Byte *srcBuffer = (Byte *)MyAlloc(fileSize + 4);
	Byte *srcBuffer = (Byte *)MyAlloc(fileSize);

//	sscanf(PathFindFileNameA(argv[1]), "0x%p.bin", &iAddress);
//	*(unsigned int *)srcBuffer = iAddress;
//	fread(srcBuffer + 4, fileSize, 1, fp);
	fread(srcBuffer, fileSize, 1, fp);
	fclose(fp);

	Byte *outBuffer = (Byte *)MyAlloc(outsize);
	if (outBuffer == NULL)
	{
		printf("Can't allocate.\n");
		return;
	}

//	Lzma86_Encode(outBuffer, &outsize, srcBuffer, fileSize + 4, 9, 1 << 26, 0);
	Lzma86_Encode(outBuffer, &outsize, srcBuffer, fileSize, 9, 1 << 27, 2);
	MyFree(srcBuffer);

	fp = fopen(argv[2], "wb");
	if (fp == NULL)
	{
		printf("open dest error.\n");
	}
	else
	{
		fwrite(outBuffer, outsize, 1, fp);
		fclose(fp);
	}
	MyFree(outBuffer);
	return;
}