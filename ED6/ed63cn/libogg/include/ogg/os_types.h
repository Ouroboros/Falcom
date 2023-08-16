/********************************************************************
 *                                                                  *
 * THIS FILE IS PART OF THE OggVorbis SOFTWARE CODEC SOURCE CODE.   *
 * USE, DISTRIBUTION AND REPRODUCTION OF THIS LIBRARY SOURCE IS     *
 * GOVERNED BY A BSD-STYLE SOURCE LICENSE INCLUDED WITH THIS SOURCE *
 * IN 'COPYING'. PLEASE READ THESE TERMS BEFORE DISTRIBUTING.       *
 *                                                                  *
 * THE OggVorbis SOURCE CODE IS (C) COPYRIGHT 1994-2002             *
 * by the Xiph.Org Foundation http://www.xiph.org/                  *
 *                                                                  *
 ********************************************************************

 function: #ifdef jail to whip a few platforms into the UNIX ideal.
 last mod: $Id: os_types.h 14997 2008-06-04 03:27:18Z ivo $

 ********************************************************************/
#ifndef _OS_TYPES_H
#define _OS_TYPES_H

/* make it easy on the folks that want to compile the libs with a
   different malloc than stdlib */

/*
#define _ogg_malloc  malloc
#define _ogg_calloc  calloc
#define _ogg_realloc realloc
#define _ogg_free    free
*/
#include "nt_api.h"
#include "my_mem.h"

#define _ogg_malloc(s)		HeapAlloc(RtlGetProcessHeap(), 0, s)
#define _ogg_calloc         HeapAlloc(RtlGetProcessHeap(), HEAP_ZERO_MEMORY s)
#define _ogg_realloc(p, s)	HeapReAlloc(RtlGetProcessHeap(), HEAP_ZERO_MEMORY, p, s)
#define _ogg_free(p)		HeapFree(RtlGetProcessHeap(), 0, p)

/* MSVC/Borland */
typedef __int64 ogg_int64_t;
typedef __int32 ogg_int32_t;
typedef unsigned __int32 ogg_uint32_t;
typedef __int16 ogg_int16_t;
typedef unsigned __int16 ogg_uint16_t;

#endif  /* _OS_TYPES_H */
