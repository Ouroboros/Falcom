/* 7zAlloc.c -- Allocation functions
2008-10-04 : Igor Pavlov : Public domain */

#include "7zAlloc.h"

/* #define _SZ_ALLOC_DEBUG */
/* use _SZ_ALLOC_DEBUG to debug alloc/free operations */

#include <Windows.h>

extern HANDLE hHeap;

void *SzAlloc(void *p, size_t size)
{
	return HeapAlloc(hHeap, 0, size);
}

void SzFree(void *p, void *address)
{
	HeapFree(hHeap, 0, address);
}