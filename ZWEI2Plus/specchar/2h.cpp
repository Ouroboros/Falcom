#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kanade /SECTION:.Kanade,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kanade")
#pragma comment(linker,"/MERGE:.data=.Kanade")

#include <Windows.h>
#include <set>
#include "crt_h.h"
#include "my_crt.h"
#include "my_common.h"

using std::set;

ForceInline void main2(int argc, char **argv)
{
    FILE *fp;
    s32 size;
    uchar *p;
    wchar_t *pw;
    char name[MAX_PATH];

    if (argc == 1)
        return;

    fp = fopen(argv[1], "rb");
    if (!fp)
        return;
    size = fsize(fp);
    p = new uchar[size];
    fread(p, size, 1, fp);
    fclose(fp);

    int c = 0;
    set<wchar_t> wset;
    pw = (wchar_t *)p;

    while (size > 0)
    {
        wset.insert(*pw++);
        size -= 2;
    }

    delete[] p;

    strcpy(name, argv[1]);
    rmext(name);
    strcat(name, ".h");
    fp = fopen(name, "wb");
    if (!fp)
        return;

    fprintf(fp, "static WCHAR spec[] = \n"
                "{\n"
                "    ");
    for (set<wchar_t>::iterator it = wset.begin(); it != wset.end(); ++it)
    {
        fputc('\'', fp);
        fwrite(&*it, 2, 1, fp);
        fprintf(fp, "', ");
        if (++c == 10)
        {
            c = 0;
            fprintf(fp, "\r\n    ");
        }
    }
    fprintf(fp, "%c}", c ? '\n' : 0);
    fclose(fp);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}