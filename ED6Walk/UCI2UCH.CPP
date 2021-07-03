#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kaede /SECTION:.Kaede,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kaede")
#pragma comment(linker,"/MERGE:.data=.Kaede")

#include <Windows.h>
#include <stdio.h>
#include "getmainargs.h"

FORCEINLINE void STDCALL main2(int argc, char **argv)
{
    FILE *fp, *fCH;
    int  srclen, index, header;
    CHAR *src;
    CHAR szFileName[MAX_PATH];

    index = 0;
    header = 'HCU';
    sprintf(szFileName, "%s.CH", argv[1]);
    fCH = fopen(szFileName, "wb");
    fwrite(&header, 3, 1, fCH);

    while (1)
    {
        sprintf(szFileName, "%s_%04u.uci", argv[1], index++);
        fp = fopen(szFileName, "rb");
        if (fp == NULL)
        {
            break;
        }

        fseek(fp, 0, SEEK_END);
        srclen = ftell(fp);
        fseek(fp, 0, SEEK_SET);
        src = (CHAR *)malloc(srclen);
        fread(src, srclen, 1, fp);
        fclose(fp);
        fwrite(src, srclen, 1, fCH);
        free(src);
    }

    fputc(0, fCH);
    fclose(fCH);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    if (argc >= 2)
    {
        main2(argc, argv);
    }
    exit(0);
}