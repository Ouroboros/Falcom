#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kanade /SECTION:.Kanade,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kanade")
#pragma comment(linker,"/MERGE:.data=.Kanade")
#pragma comment(lib, "ntdll.lib")
#pragma comment(lib, "msvcrt.lib")

#include <Windows.h>
#include "crt_h.h"
#include "my_common.h"
#include "ysf.h"

ForceInline void main2(int argc, char **argv)
{
    for (u32 i = 1; i != argc; ++i)
    {
        CYSF ysf;

        if (ysf.Open(argv[i], NULL))
        {
            ;
        }
    }
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}