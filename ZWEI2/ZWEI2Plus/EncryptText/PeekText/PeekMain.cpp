#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kanade /SECTION:.Kanade,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kanade")
#pragma comment(linker,"/MERGE:.data=.Kanade")

#include <Windows.h>
#include "crt_h.h"
#include "my_crt.h"
#include "my_common.h"
#include "PeekText.h"

ForceInline void main2(int argc, char **argv)
{
    if (argc < 3)
        return;

    FILE *fp;
    char szOutput[MAX_PATH];
    vector<string> vecJP, vecCN, vecJPConv;
    CRipZwei2Text rztJP, rztCN;

    if (!rztJP.Open(argv[1]) || !rztCN.Open(argv[2]))
    {
        printf("open failed\n");
        return;
    }

    rztJP.GetAllText(vecJP);
    if (vecJP.size() == 0)
    {
        printf("%s empty\n", argv[1]);
        return;
    }

    rztCN.GetAllText(vecCN);
    if (vecCN.size() == 0)
    {
        printf("%s empty\n", argv[2]);
        return;
    }

    if (argc > 3 && rztJP.Open(argv[3]))
        rztJP.GetAllText(vecJPConv);

    if (argc > 4)
    {
        strcpy(szOutput, argv[4]);
    }
    else
    {
        strcpy(szOutput, argv[1]);
        rmext(szOutput);
        strcat(szOutput, "_");
        strcat(szOutput, findname(argv[2]));
    }

    fp = fopen(szOutput, "ab");
    if (!fp)
    {
        printf("create \"%s\" failed\n", szOutput);
        return;
    }

    fprintf(fp, ";%s\n", findname(argv[1]));
    if (vecJP.size() > vecCN.size())
        fprintf(fp, ";> %d\n", vecJP.size() - vecCN.size());
    else if (vecJP.size() < vecCN.size())
        fprintf(fp, ";< %d\n", vecJP.size() - vecCN.size());

    for (u32 i = 0, j = min(vecJP.size(), vecCN.size()); i != j; ++i)
    {
        if (vecJPConv.size() && vecJPConv[i] == vecCN[i])
            continue;
        else if (vecJP[i] == vecCN[i])
            continue;

        fprintf(fp, "==========================================\n");
        fprintf(fp, "%s\n", vecJP[i].c_str());
        fprintf(fp, "----------------------------------\n");
        fprintf(fp, "%s\n", vecCN[i].c_str());
    }

    fclose(fp);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}