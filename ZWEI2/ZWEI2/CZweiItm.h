#ifndef _CZWEIITM_H_
#define _CZWEIITM_H_

#include <Windows.h>
#include "my_headers.h"

#pragma pack(1)
typedef struct
{
//    PByte data[size];
    BOOL   bEncrypt;       // 0:bmp 1:scp
    UInt32 uiCheckSum;
    UInt32 uiHash;
} TZwei2ItmTail;
#pragma pack()

class CZwei2Dec
{
public:
    CZwei2Dec(char *szFileName, void *pbSourceData, UInt32 uiSourceSize);

public:
    UInt32 STDCALL Decode(PByte pbDest = NULL, UInt32 uiDestSize = 0);

protected:
    void STDCALL DecodePass1(TZwei2ItmTail *pDecodeTail, BOOL bEncode = False);
    void STDCALL DecodePass2(BOOL bEncode = False);

protected:
    PByte  m_pbSourceData;
    UInt32 m_uiSourceSize, m_uiSizeToDecode;
    char  m_szFileName[MAX_PATH];
};

class CZwei2Enc : public CZwei2Dec
{
public:
    CZwei2Enc(char *szFileName, void *pbSourceData, UInt32 uiSourceSize);

public:
    const TZwei2ItmTail* GetTail();
    UInt32 STDCALL Encode(BOOL bEncrypt, PByte pbDest = NULL, UInt32 uiDestSize = 0);

private:
    TZwei2ItmTail m_EncodeTail;
};

#endif /* _CZWEIITM_H_ */