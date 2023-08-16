#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/SECTION:.text,ERW /MERGE:.rdata=.text /MERGE:.data=.text")
#pragma comment(linker,"/SECTION:.Amano,ERW /MERGE:.text=.Amano")

#include <Windows.h>
#include "my_headers.h"
#include "YamaNeko.h"
#include "my_commsrc.h"

INIT_CONSOLE_HANDLER

ForceInline Void main2(Int argc, WChar **argv)
{
    if (argc == 1)
        return;

    CYamaNeko yn;

//    setlocale(LC_ALL, ".936");
    while (--argc)
    {
        PrintConsoleW(L"Processing %s ... ", *++argv);
        PrintConsoleW(L"%s\n", yn.Open(*argv) ? L"OK" : L"failed");
    }
}

void __cdecl main(Int argc, WChar **argv)
{
    TEB_BASE *Teb = Nt_CurrentTeb();

    argv = CmdLineToArgvW(Teb->ProcessEnvironmentBlock->ProcessParameters->CommandLine.Buffer, &argc);
    main2(argc, argv);
    Nt_ExitProcess(0);
}
