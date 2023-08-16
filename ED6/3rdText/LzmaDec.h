
#ifndef __7Z_LZMADEC_H
#define __7Z_LZMADEC_H

#include "LZMA/Types.h"
#include "LZMA/LzmaDec.h"
#include "7zAlloc.h"

SRes Lzma86_GetUnpackSize(const Byte *src, SizeT srcLen, UInt64 *unpackSize);
SRes Lzma86_Decode(Byte *dest, SizeT *destLen, const Byte *src, SizeT *srcLen);

#endif