#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Angel /SECTION:.Angel,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Angel")
#pragma comment(linker,"/MERGE:.data=.Angel")

#define ZLIB_DLL

#include "CZweiItm.h"
#include "zlib/zlib.h"

enum MODE { NONE, ENCODE, DECODE, DECODE_YWT };

Void DecodeYWT(PChar pszInput, PByte pbInputBuffer, UInt32 Size)
{
    ULong   BufferSize;
    PByte   pbBuffer, pbBuffer2;
    HMODULE hZLib;

    int (__cdecl *uncompress)(Bytef *dest, uLongf *destLen, const Bytef *source, uLong sourceLen);

    hZLib = LoadLibraryExW(L"zlib1.dll", 0, NULL);
    if (hZLib == NULL)
        return;

    *(FARPROC *)&uncompress = GetProcAddress(hZLib, "uncompress");
    if (uncompress == NULL)
        return;

    pbBuffer = pbInputBuffer;
    BufferSize = Size;
    if (BufferSize != 0) do
    {
        *(PUInt32)pbBuffer++ ^= 0x5D0C5053;
    } while (--BufferSize);

    BufferSize = Size / 2;
    pbBuffer  = pbInputBuffer;
    pbBuffer2 = pbBuffer + BufferSize;

    if (BufferSize != 0) do
    {
        *pbBuffer2 ^= *pbBuffer;
        *pbBuffer++ ^= *pbBuffer2++;
    } while (--BufferSize);

    BufferSize = *(PUInt32)pbInputBuffer + 100;
    pbInputBuffer += 4;
    pbBuffer = (PByte)malloc(BufferSize);
    if (uncompress(pbBuffer, &BufferSize, pbInputBuffer, Size - 4) == Z_OK)
    {
        FILE *fp = fopen(pszInput, "wb");
        if (fp != NULL)
        {
            fwrite(pbBuffer, BufferSize, 1, fp);
            fclose(fp);
        }
    }

    FreeLibrary(hZLib);
}

ForceInline void main2(int argc, char **argv)
{
    if (argc < 2)
    {
        printf("Usage: \n"
               "\n"
               "%s input options\n"
               "\n"
               "Available Options:\n"
               "    -o Specify the output file, optional\n"
               "    -e Encode input file\n"
               "    -d Decode input file\n"
               "\n", 
               findname(argv[0]));
        return;
    }

    FILE *fp;
    char *pInput, *pOutput, szOutput[MAX_PATH];
    PByte  pBuffer;
    UInt32 uiParam, uiMode, uiSize;

    uiMode = NONE;
    pInput  = NULL;
    pOutput = NULL;
    for (int i = 1; i < argc; ++i)
    {
        if (argv[i][0] && argv[i][0] != '-')
        {
            pInput = argv[i];
            continue;
        }

        uiParam = 0;
        strlwr(&argv[i][1]);

        for (int j = 1; argv[i][j]; ++j)
        {
            uiParam = uiParam << 8 | (char)argv[i][j];
        }

        switch (uiParam)
        {
        case 'o':
            if (++i < argc)
                pOutput = argv[i];
            break;

        case 'e':
            uiMode = ENCODE;
            break;

        case 'd':
            uiMode = DECODE;
            break;

        case 'dy':
            uiMode = DECODE_YWT;
            break;

        default:
            printf("Unknown option \"%s\"\n", argv[i]);
        }
	}

    if (pInput == NULL)
    {
        printf("Please specify one input file.\n");
        return;
    }
    else if (uiMode == NONE)
    {
        printf("Please specify one mode (decode or encode).\n");
        return;
    }

    fp = fopen(pInput, "rb");
    if (fp == NULL)
    {
        printf("Can't open \"%s\"\n", pInput);
        perror(NULL);
        return;
    }

    uiSize = fsize(fp);
    pBuffer = (PByte)malloc(uiSize + 4);
    if (pBuffer == NULL)
    {
        printf("Can't allocate memory for input file\n");
        fclose(fp);
        return;
    }

    uiParam = fread(pBuffer, uiSize, 1, fp);
    fclose(fp);
    if (uiParam == 0)
    {
        printf("Can't read input file\n");
        perror(NULL);
        delete[] pBuffer;
    }

    if (uiMode == ENCODE)
    {
        strcpy(szOutput, pOutput ? pOutput : pInput);
        rmext(szOutput);

        BOOL bEncrypt;
        CZwei2Enc ze(szOutput, pBuffer, uiSize);

        bEncrypt = *(PUInt16)pBuffer != 'MB';
        uiSize = ze.Encode(bEncrypt);
        if (uiSize)
        {
            if (pOutput == NULL)
            {
                strcat(szOutput, ".itm");
                pOutput = szOutput;
            }
            fp = fopen(pOutput, "wb");
            if (fp)
            {
                fwrite(pBuffer, uiSize, 1, fp);
                fwrite(ze.GetTail(), sizeof(TZwei2ItmTail), 1, fp);
                fclose(fp);
            }
            else
            {
                printf("Can't create \"%s\"\n", pOutput);
            }
        }
        else
        {
            printf("Encode \"%s\" failed.\n", pInput);
        }
    }
    else if (uiMode == DECODE)
    {
        CZwei2Dec zd(pInput, pBuffer, uiSize);

        uiSize = zd.Decode();
        if (uiSize)
        {
            if (pOutput == NULL)
            {
                strcpy(szOutput, pInput);
                rmext(szOutput);
                strcat(szOutput, *(PUInt16)pBuffer == 'MB' ? ".bmp" : ".txt");
                pOutput = szOutput;
            }

            fp = fopen(pOutput, "wb");
            if (fp)
            {
                fwrite(pBuffer, uiSize, 1, fp);
                fclose(fp);
            }
            else
            {
                printf("Can't create \"%s\"\n", pOutput);
            }
        }
        else
        {
            printf("Decode \"%s\" failed.\n", pInput);
        }
    }
    else if (uiMode == DECODE_YWT)
    {
        DecodeYWT(pInput, pBuffer, uiSize);
    }

    free(pBuffer);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}