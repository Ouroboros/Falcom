#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kanade /SECTION:.Kanade,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kanade")
#pragma comment(linker,"/MERGE:.data=.Kanade")

#include <Windows.h>
#include "crt_h.h"
#include "my_crt.h"
#include "my_common.h"
#include <set>

using std::set;

Bool WINAPI IsShiftJIS(UINT Byte)
{
    if ((Byte >= 0x8140 && Byte <= 0x9F7E) || (Byte >= 0xE080 && Byte <= 0xEFFC))
        return True;

    return False;
}

ForceInline void main2(int argc, char **argv)
{
    FILE *fp;
    char szOutFile[MAX_PATH], buf[0x1024];

    for (int i = 1; i != argc; ++i)
    {
        fp = fopen(argv[i], "rb");

        if (!fp) continue;

        set<wchar_t> sc;
        int c = 0;
        while (fgets(buf, countof(buf), fp))
        {
            if (buf[0] == ';')
                continue;

            if (++c != 4)
                continue;
            c = 0;

            u32 v, len = strlen(buf);

            for (int j = 0; j <= len; ++j)
            {
                v = (Byte)buf[j];
                if (v < 0x80)
                {
                    continue;
                }

                v = (v << 8) | (Byte)buf[++j];
                if (IsShiftJIS(v))
                    sc.insert(HIBYTE(v)|(LOBYTE(v)) << 8);
            }
        }

        fclose(fp);

        strcpy(szOutFile, argv[i]);
        rmext(szOutFile);
        strcat(szOutFile, "_sc.txt");
        fp = fopen(szOutFile, "wb+");
        if (!fp)
        {
            continue;
        }

        c = 0;
        fprintf(fp, "static WCHAR spec[] = \n"
                    "{\n"
                    "    ");
        for (set<wchar_t>::iterator it = sc.begin(); it != sc.end(); ++it)
        {
//            fputc('\'', fp);
            fprintf(fp, "case (WChar)TAG2('");
            fwrite(&*it, 2, 1, fp);
            fprintf(fp, "'): ");
            if (++c == 10)
            {
                c = 0;
                fprintf(fp, "\r\n    ");
            }
        }
        fprintf(fp, "%c};", c ? '\n' : 0);

        fclose(fp);
    }
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}