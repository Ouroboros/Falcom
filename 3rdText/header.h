#pragma warning(disable:4309)

#include "inc_header.h"

typedef struct _tagArray_of_Data
{
	char *data;
	size_t nSize;
} tagArray_of_Data;

tagArray_of_Data Array_of_Data[] =
{
	{_DICT1_LZMA_, sizeof(_DICT1_LZMA_)},
	{_DICT2_LZMA_, sizeof(_DICT2_LZMA_)},
};