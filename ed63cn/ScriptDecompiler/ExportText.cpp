#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Kaede /SECTION:.Kaede,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Kaede")
#pragma comment(linker,"/MERGE:.data=.Kaede")

#include <Windows.h>
#include "crt_h.h"
#include "my_common.h"
#include "FileType.h"

uchar   *gpbBuffer;
int_32  iBufferSize;

uchar* Export(uchar *pbBuffer, uchar *pStart, FILE *fp)
{
    int i, iOffset;
    char buffer[0x1000];
    uchar ch;

    i = 0;
    iOffset = pbBuffer - pStart;
    while (*(puint_16)pbBuffer != 0x0002 && *(puint_16)pbBuffer != 0x0001)
    {
        ch = *pbBuffer++;
        if (ch < ' ')
        {
            i += sprintf(&buffer[i], "\\x%02X", ch);
        }
        else
        {
            buffer[i++] = ch;
        }
    }
    i += sprintf(&buffer[i], "\\x%02X\\x%02X//", *pbBuffer, *(pbBuffer + 1));
    pbBuffer += 2;
    for (int j = 0; j != 0x20; ++j)
    {
        i += sprintf(&buffer[i], "%02X", pbBuffer[j]);
    }
    fprintf(fp, "==================================================%04X\n", iOffset);
    fprintf(fp, "%s\n--------------------------------------\n\n", buffer);

    fflush(fp);
    return pbBuffer;
}

uchar* Export2(uchar *pbBuffer, uchar *pStart, FILE *fp)
{
    int i, iOffset;
    char buffer[0xFFF];
    uchar ch;

    i = 0;
    iOffset = pbBuffer - pStart;
    while (*pbBuffer)
    {
        ch = *pbBuffer++;
        if (ch < ' ')
        {
            i += sprintf(&buffer[i], "\\x%02X", ch);
        }
        else
        {
            buffer[i++] = ch;
        }
    }
    i += sprintf(&buffer[i], "\\x%02X//", *pbBuffer, *(pbBuffer + 1));
    ++pbBuffer;
    for (int j = 0; j != 0x20; ++j)
    {
        i += sprintf(&buffer[i], "%02X", pbBuffer[j]);
    }
    fprintf(fp, "==================================================%04X\n", iOffset);
    fprintf(fp, "%s\n--------------------------------------\n\n", buffer);

    fflush(fp);
    return pbBuffer;
}

void ExportText(FILE *fp, uchar *pbBuffer, int_32 uiSize)
{
    uchar *p, *pEnd, *pTemp, ch;
    uint_16 u16;

    p = pbBuffer;
    pEnd = pbBuffer + uiSize;
    pbBuffer += 0x60;
    while (pbBuffer <= pEnd)
    {
        switch (*pbBuffer++)
        {
        case MENU_TITLE:
            break;
            pTemp = pbBuffer + 8;
            if (*pTemp++ == MENU_TITLE_START)
            {
                ch = *pTemp;
                if (ch < ' ')
                {
                    ++pTemp;
                    switch (ch)
                    {
                    case 0x1F:
                        ++pTemp;
                    case 7:
                        ++pTemp;
                        break;
                    }
                }

                pbBuffer = Export(pTemp + 2, p, fp);
            }
            else if (*pTemp == MENU_TITLE_STR)
            {
                pbBuffer = Export2(pbBuffer + 9, p, fp);
                if (*pbBuffer == MENU_TITLE_START)
                {
                    pbBuffer = Export(pbBuffer + 3, p, fp);
                }
            }
            break;

        case MENU_TITLE_START:
            ch = *pbBuffer;
            if (ch < ' ')
            {
                pTemp = pbBuffer + 1;
                switch (ch)
                {
                case 0x1F:
                    ++pTemp;
                case 7:
                    ++pTemp;
                    break;
                }

                pTemp += strlen((char *)pTemp) - 1;
                u16 = *(puint_16)pTemp;
                if (u16 != 1 && u16 != 2)
                    break;

                pbBuffer = Export(pbBuffer + 1, p, fp);
            }
            break;

        case MENU_START:
            if (*(puint_16)pbBuffer > 0x10)
            {
                break;
            }

            u16 = *(puint_16)(pbBuffer + 2);
            if (u16 != 0xFFFF && u16 > 0xF0)
            {
                break;
            }

            u16 = *(puint_16)(pbBuffer + 4);
            if (u16 != 0xFFFF && u16 > 0xF0)
            {
                break;
            }

            ch = *(pbBuffer + 6);
            if ((ch == 0 || ch == 1))
            {
                pTemp = pbBuffer + 7;
                pTemp += strlen((char *)pTemp) + 1;
                while (*pTemp == 3)
                {
                    pTemp = p + *(puint_16)(pTemp + 1);
                }
                if (*pTemp != MENU_END)
                    break;

                pbBuffer = Export(pbBuffer + 7, p, fp);
            }

            break;

        case TALK_START:
            if (*(pint_16)pbBuffer <= 0x80)
            {
                pTemp = pbBuffer + 2;
                pTemp += strlen((char *)pTemp) + 1;
                while (*pTemp == 3)
                {
                    pTemp = p + *(puint_16)(pTemp + 1);
                }
                if (*pTemp != TALK_END)
                    break;

                pbBuffer = Export(pbBuffer + 2, p, fp);
            }
        }
    }
}

void ProcessFile(char *szName)
{
    FILE   *fp;
    int_32  iSize;
    uchar  *pbBuffer;
    char   *pExtension, szText[MAX_PATH];
    TSNHeader *h;

    fp = fopen(szName, "rb");
    if (fp == NULL)
    {
        printf("Can't open \"%s\"\n", szName);
        perror(NULL);
        return;
    }

    iSize = fsize(fp);
    if (iSize == 0)
    {
        printf("Empty file \"%s\"\n", szName);
        fclose(fp);
        return;
    }
    else if (iSize < sizeof(*h))
    {
        printf("Invalid sn file \"%s\"\n", szName);
        fclose(fp);
        return;
    }

    pbBuffer = gpbBuffer;
    if (iSize > iBufferSize)
    {
        iBufferSize = iSize;
        pbBuffer = (uchar *)realloc(pbBuffer, iSize);
        if (pbBuffer == NULL)
        {
            fclose(fp);
            return;
        }
        gpbBuffer = pbBuffer;
    }

    fread(pbBuffer, iSize, 1, fp);
    fclose(fp);

    h = (TSNHeader *)pbBuffer;
    if (h->wEndOffset + 9 > iSize || memicmp(pbBuffer + h->wEndOffset, "@FileName", 9))
    {
        printf("Invalid sn file \"%s\"\n", szName);
        return;
    }

    strcpy(szText, szName);
    pExtension = findext(szText);
    if (pExtension)
    {
        strcpy(pExtension, ".txt");
    }
    else
    {
        strcat(szText, ".txt");
    }

    fp = fopen(szText, "wb");
    if (fp == NULL)
    {
        printf("Can't open \"%s\"\n", szText);
        perror(NULL);
        return;
    }

    printf("Exporting \"%s\" ... \n", szName);
    fprintf(fp, ";%s\n", findname(szName));
    ExportText(fp, pbBuffer, iSize);

    fclose(fp);
}

void ProcessDirectory(char *szPath)
{
    char szCurPath[MAX_PATH];
    intptr_t hFind;
    __finddata64_t fd;

    strcpy(szCurPath, szPath);
    strcat(szCurPath, "\\*.*");
    hFind = _findfirst64(szCurPath, &fd);
    if (hFind == -1)
        return;

    do
    {
        if (fd.attrib & _A_SUBDIR)
        {
            if (strcmp(fd.name, ".") && strcmp(fd.name, ".."))
            {
                sprintf(szCurPath, "%s\\%s", szPath, fd.name);
                ProcessDirectory(szCurPath);
            }
        }
        else
        {
            sprintf(szCurPath, "%s\\%s", szPath, fd.name);
            ProcessFile(szCurPath);
        }
    } while (_findnext64(hFind, &fd) != -1);

    _findclose(hFind);
}

ForceInline void main2(int argc, char **argv)
{
    if (argc < 2)
        return;

    char *path;
    intptr_t hFind;
    __finddata64_t fd;

    iBufferSize = 0x3000;
    gpbBuffer = (uchar *)malloc(iBufferSize);

    for (int i = 1; i != argc; ++i)
    {
        hFind = _findfirst64(argv[i], &fd);
        if (hFind == -1)
            continue;

        do
        {
            path = findpath(argv[i]);
            if (path) *path = 0;

            if (fd.attrib & _A_SUBDIR)
            {
                if (strcmp(fd.name, ".") && strcmp(fd.name, ".."))
                {
                    int j;

                    if (path)
                    {
                        j = strlen(argv[i]);
                        strcpy(&fd.name[j + 1], fd.name);
                        strcpy(fd.name, argv[i]);
                        fd.name[j] = '\\';
                    }

                    ProcessDirectory(fd.name);

                    if (path) *path = '\\';
                }
            }
            else
            {
                int j;

                if (path)
                {
                    j = strlen(argv[i]);
                    strcpy(&fd.name[j + 1], fd.name);
                    strcpy(fd.name, argv[i]);
                    fd.name[j] = '\\';
                }

                ProcessFile(fd.name);

            }

            if (path) *path = '\\';
        } while (_findnext64(hFind, &fd) != -1);
    }

    _findclose(hFind);
    free(gpbBuffer);
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}