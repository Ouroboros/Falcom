#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kanade /SECTION:.Kanade,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kanade")
#pragma comment(linker,"/MERGE:.data=.Kanade")
#pragma comment(lib, "ntdll.lib")

#include "SNDecompiler.h"
#include "crt_h.h"
#include "my_crt.h"
#include "my_common.h"

ForceInline void main2(int argc, char **argv)
{
    CSNDecompiler decl;

    for (int i = 1; i != argc; ++i)
    {
        decl.DecompileFile(argv[i]);
    }
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}