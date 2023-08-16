#include "CZweiItm.h"

char gszDict1[] = "!~_Q#xDRgd-d&yfg&'(8)(5(594er2f4asf5f6e5f4s5fvwyjk%fgqTUCFD4568r";
char gszDict2[] = "GURUguruMinmIN_";

/************************************************************************/
/* Decoder                                                              */
/************************************************************************/

CZwei2Dec::CZwei2Dec(char *szFileName, void *pbSourceData, UInt32 uiSourceSize)
{
    strcpy(m_szFileName, findname(szFileName));
    rmext(m_szFileName);
    strupr(m_szFileName);
    m_pbSourceData = (PByte)pbSourceData;
    m_uiSourceSize = uiSourceSize;
    m_uiSizeToDecode = uiSourceSize - sizeof(TZwei2ItmTail);
}

void STDCALL CZwei2Dec::DecodePass1(TZwei2ItmTail *pDecodeTail, BOOL bEncode/* = False*/)
{
    PByte   pbSource;
    UInt32  uiCheckSum, uiHash;
    char     szDict1[sizeof(gszDict1)];
    char     szDict2[sizeof(gszDict2)];

    pbSource = m_pbSourceData;
    memcpy(szDict1, gszDict1, sizeof(szDict1));
    memcpy(szDict2, gszDict2, sizeof(szDict2));
    strncpy(szDict1 + 8, m_szFileName, 8);

    uiCheckSum = 0;
    uiHash = 0xDE2F;
    if (bEncode)
    {
        for (UInt32 i = 0; i != m_uiSizeToDecode; ++i)
        {
            uiCheckSum += *pbSource;
            uiHash ^= *pbSource;
            *pbSource = (Byte)( ~*pbSource ^ ( ( (i & 7) + szDict2[i % 0xF] ) * szDict1[i & 0x3F] ) );
            ++pbSource;
        }
    }
    else
    {
        for (UInt32 i = 0; i != m_uiSizeToDecode; ++i)
        {
            *pbSource = (Byte)( ~*pbSource ^ ( ( (i & 7) + szDict2[i % 0xF] ) * szDict1[i & 0x3F] ) );
            uiCheckSum += *pbSource;
            uiHash ^= *pbSource;
            ++pbSource;
        }
    }

    pDecodeTail->uiCheckSum = uiCheckSum;
    pDecodeTail->uiHash = uiHash;
}

void STDCALL CZwei2Dec::DecodePass2(BOOL bEncode/* = False*/)
{
    Byte c, *pbSource = m_pbSourceData;

    if (bEncode)
    {
        for (UInt32 i = 0; i != m_uiSizeToDecode; ++i)
        {
            c = *pbSource;
            c = (c >> 4) | (c << 4);
            *pbSource++ = (Byte)(~c ^ i);
        }
    }
    else
    {
        for (UInt32 i = 0; i != m_uiSizeToDecode; ++i)
        {
            c = (Byte)(~*pbSource ^ i);
            *pbSource++ = (c << 4) | (c >> 4);
        }
    }
}

UInt32 STDCALL CZwei2Dec::Decode(PByte pbDest/* = NULL*/, UInt32 uiDestSize/* = 0*/)
{
    TZwei2ItmTail *pSrcTail, DecodeTail;

    pSrcTail = (TZwei2ItmTail *)(m_pbSourceData + m_uiSourceSize - sizeof(*pSrcTail));
    DecodePass1(&DecodeTail);

    if (DecodeTail.uiCheckSum != pSrcTail->uiCheckSum || DecodeTail.uiHash != pSrcTail->uiHash)
        return 0;

    if (pSrcTail->bEncrypt)
        DecodePass2();

    return m_uiSourceSize - sizeof(*pSrcTail);
}

/************************************************************************/
/* Encoder                                                              */
/************************************************************************/

CZwei2Enc::CZwei2Enc(char *szFileName, void *pbSourceData, UInt32 uiSourceSize)
 : CZwei2Dec(szFileName, pbSourceData, uiSourceSize + sizeof(TZwei2ItmTail))
{
    memset(&m_EncodeTail, 0, sizeof(m_EncodeTail));
}

UInt32 STDCALL CZwei2Enc::Encode(BOOL bEncrypt, PByte pbDest /* = NULL */, UInt32 uiDestSize /* = 0 */)
{
    if (m_EncodeTail.bEncrypt = bEncrypt)
        DecodePass2(True);
    DecodePass1(&m_EncodeTail, True);

    return m_uiSizeToDecode;
}

const TZwei2ItmTail* CZwei2Enc::GetTail()
{
    return &m_EncodeTail;
}
/*
void STDCALL CZwei2Enc::EncodePass1(TZwei2ItmTail *pEncodeTail)
{
    PByte   *pbSource;
    UInt32  uiCheckSum, uiHash;
    char     szDict1[sizeof(gszDict1)];
    char     szDict2[sizeof(gszDict2)];

    pbSource = m_pbSourceData;
    memcpy(szDict1, gszDict1, sizeof(szDict1));
    memcpy(szDict2, gszDict2, sizeof(szDict2));
    strncpy(szDict1 + 8, m_szFileName, 8);

    uiCheckSum = 0;
    uiHash = 0xDE2F;
    for (UInt32 i = 0; i != m_uiSizeToDecode; ++i)
    {
        uiCheckSum += *pbSource;
        uiHash ^= *pbSource;
        *pbSource = (PByte)( ~*pbSource ^ ( ( (i & 7) + szDict2[i % 0xF] ) * szDict1[i & 0x3F] ) );
        ++pbSource;
    }

    pEncodeTail->uiCheckSum = uiCheckSum;
    pEncodeTail->uiHash = uiHash;
}

void STDCALL CZwei2Enc::EncodePass2()
{
    PByte c, *pbSource = m_pbSourceData;

    for (UInt32 i = 0; i != m_uiSizeToDecode; ++i)
    {
        c = *pbSource;
        c = (c >> 4) | (c << 4);
        *pbSource++ = (PByte)(~c ^ i);
    }
}
*/
