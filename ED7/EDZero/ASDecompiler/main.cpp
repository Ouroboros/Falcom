#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include "ASDecompiler.h"
#include <stdio.h>
#include "Mem.cpp"

ForceInline Void main2(Int argc, WChar **argv)
{
    if (argc == 1)
    {
        CED7AsDecompiler::ShowInstructionMapInfo();
        return;
    }

    CED7AsDecompiler asdecl;

    while (--argc)
    {
        LONG Status = asdecl.DecompilerFile(*++argv);
        asdecl.ShowError(Status);
    }
}

void __cdecl main(Int argc, WChar **argv)
{
    getargsW(&argc, &argv);
//    argv = CmdLineToArgvW(GetCommandLineW(), &argc);
    main2(argc, argv);
//    ExitProcess(0);
    exit(0);
}