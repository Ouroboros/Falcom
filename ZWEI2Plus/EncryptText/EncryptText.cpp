#pragma comment(linker,"/ENTRY:main")
#pragma comment(linker,"/MERGE:.text=.Angel /SECTION:.Angel,ERW")
#pragma comment(linker,"/MERGE:.rdata=.Angel")
#pragma comment(linker,"/MERGE:.data=.Angel")

#include <Windows.h>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include "sha2.h"
#include "aes.h"
#include "my_headers.h"

using std::set;
using std::vector;
using std::string;

typedef struct
{
    u32 hash[4];
    u32 len;
} TTextHeader;

int cmp(TTextHeader *t1, TTextHeader *t2);

ForceInline void main2(int argc, char **argv)
{
    if (argc < 2)
        return;

    char  buf[0x1024];
    UChar *p;
    u32   len, state, ohash[4], hash[8], *ptext;
    FILE *fp, *fo;

    fp = fopen(argv[1], "r");
    if (!fp)
        return;

    strcpy(buf, argv[1]);
    rmname(buf);
    strcat(buf, "scp.sc");
    fo = fopen(buf, "wb+");
    if (!fo)
    {
        fclose(fp);
        return;
    }

    string str;
    set<string> h;

    ptext = (pu32)buf;
    p = (UChar *)&hash;
    while (1)
    {
        fgets(buf, sizeof(buf), fp);
        if (feof(fp))
            break;

        switch (buf[0])
        {
        case '=': state = 0;
        case ';': continue;
        case '-':
            if (state != -1)
                state = 1;
            continue;
        }

        if (state == -1)
            continue;

        len = strlen(buf);
        if (buf[len - 1] == '\n')
            buf[--len] = 0;

        if (state)
        {
            u32 i, j;
            aes_encrypt_ctx ctx;

            aes_encrypt_key128((UChar *)&hash[4], &ctx);

            j = len;
            for (i = 0; j >= Block_Length; j -= Block_Length, i += 4)
            {
                aes_encrypt((UChar *)hash, (UChar *)hash, &ctx);
                hash[0] = ptext[i + 0] ^= hash[0];
                hash[1] = ptext[i + 1] ^= hash[1];
                hash[2] = ptext[i + 2] ^= hash[2];
                hash[3] = ptext[i + 3] ^= hash[3];
            }

            if (j)
            {
                aes_encrypt((UChar *)hash, (UChar *)hash, &ctx);
                if (len &3)
                    memset(&buf[len], 0, 4 - (len & 3));
                ptext[i    ] ^= hash[0];
                ptext[i + 1] ^= hash[1];
                ptext[i + 2] ^= hash[2];
                ptext[i + 3] ^= hash[3];
            }

            putw(len, fo);
            fwrite(buf, (len + 3) & ~3, 1, fo);
        }
        else
        {
            sha256((UChar *)buf, len, p);

            ++len;
            sprintf(&buf[len], "%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X\n", 
                p[0],  p[1],  p[2],  p[3],  p[4],  p[5],  p[6],
                p[7],  p[8],  p[9],  p[10], p[11], p[12], p[13],
                p[14], p[15], p[16], p[17], p[18], p[19], p[20],
                p[21], p[22], p[23], p[24], p[25], p[26], p[27],
                p[28], p[29], p[30], p[31]);

            str = &buf[len];
            if (h.count(str))
            {
//                printf(buf + len);
                state = -1;
            }
            else
            {
                h.insert(str);
                for (u32 i = 0; i != 4; ++i)
                    ohash[i] = hash[i] ^ hash[i + 4];
                fwrite(ohash, 16, 1, fo);
            }
        }
    }
    fclose(fp);

    h.empty();

    fflush(fo);
    fseek(fo, 0, SEEK_SET);
    len = fsize(fo);
    p = new UChar[len];
    fread(p, len, 1, fo);

    vector<TTextHeader*> vec;

    for (u32 i = 0; i < len; )
    {
        TTextHeader *header = (TTextHeader *)&p[i];
        vec.push_back(header);
        i += ((header->len + 3) & ~3) + sizeof(*header);
    }

    std::sort(vec.begin(), vec.end(), cmp);

    fseek(fo, 0, SEEK_SET);
    for (u32 i = 0, j = vec.size(); i != j; ++i)
    {
        fwrite(vec[i]->hash, 16, 1, fo);
//        fwrite(&vec[i]->len, 4, 1, fo);
        putw(vec[i]->len ^ vec[i]->hash[0] ^ vec[i]->hash[2], fo);
        fwrite((UChar *)&vec[i]->len + 4, (vec[i]->len + 3) & ~3, 1, fo);
    }

    delete[] p;
    fclose(fo);
}

int cmp(TTextHeader *t1, TTextHeader *t2)
{
    for (u32 i = 0; i != 4; ++i)
    {
        if (t1->hash[i] > t2->hash[i])
            return False;
        else if (t1->hash[i] < t2->hash[i])
            return True;
    }

    return True;
}

void __cdecl main(int argc, char **argv)
{
    getargs(&argc, &argv);
    main2(argc, argv);
    exit(0);
}