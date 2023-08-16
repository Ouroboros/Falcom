/* === C R E D I T S  &  D I S C L A I M E R S ==============
 * Permission is given by the author to freely redistribute and include
 * this code in any program as long as this credit is given where due.
 *
 * CQuantizer (c)  1996-1997 Jeff Prosise
 *
 * 31/08/2003 Davide Pizzolato - www.xdp.it
 * - fixed minor bug in ProcessImage when bpp<=8
 * - better color reduction to less than 16 colors
 *
 * COVERED CODE IS PROVIDED UNDER THIS LICENSE ON AN "AS IS" BASIS, WITHOUT WARRANTY
 * OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES
 * THAT THE COVERED CODE IS FREE OF DEFECTS, MERCHANTABLE, FIT FOR A PARTICULAR PURPOSE
 * OR NON-INFRINGING. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE COVERED
 * CODE IS WITH YOU. SHOULD ANY COVERED CODE PROVE DEFECTIVE IN ANY RESPECT, YOU (NOT
 * THE INITIAL DEVELOPER OR ANY OTHER CONTRIBUTOR) ASSUME THE COST OF ANY NECESSARY
 * SERVICING, REPAIR OR CORRECTION. THIS DISCLAIMER OF WARRANTY CONSTITUTES AN ESSENTIAL
 * PART OF THIS LICENSE. NO USE OF ANY COVERED CODE IS AUTHORIZED HEREUNDER EXCEPT UNDER
 * THIS DISCLAIMER.
 *
 * Use at your own risk!
 * ==========================================================
 */

#include <Windows.h>
#include "my_headers.h"

class CQuantizer
{
    typedef struct _NODE
    {
        BOOL bIsLeaf;               // TRUE if node has no children
        ULONG nPixelCount;           // Number of pixels represented by this leaf
        ULONG nRedSum;               // Sum of red components
        ULONG nGreenSum;             // Sum of green components
        ULONG nBlueSum;              // Sum of blue components
        ULONG nAlphaSum;             // Sum of alpha components
        struct _NODE* pChild[8];    // Pointers to child nodes
        struct _NODE* pNext;        // Pointer to next reducible node
    } NODE;

protected:
    NODE    *m_pTree;
    ULONG    m_nLeafCount;
    NODE    *m_pReducibleNodes[9];
    ULONG    m_nMaxColors;
    ULONG    m_nOutputMaxColors;
    ULONG    m_nColorBits;

public:
    CQuantizer(ULONG nMaxColors, ULONG nColorBits);
    ~CQuantizer();

    BOOL    ProcessImage(HANDLE hImage);
    HRESULT ProcessRawData(IMG_BITMAP_HEADER *pBmp, PVOID pvRaw);
    ULONG   GetColorCount();
    VOID    SetColorTable(RGBQUAD* prgb);

protected:
    VOID
    AddColor(
        NODE  **ppNode,
        BYTE    r,
        BYTE    g,
        BYTE    b,
        BYTE    a,
        ULONG   nColorBits,
        ULONG   nLevel,
        ULONG  *pLeafCount,
        NODE  **pReducibleNodes
    );

    PVOID
    CreateNode(
        ULONG   nLevel,
        ULONG   nColorBits,
        ULONG  *pLeafCount,
        NODE  **pReducibleNodes
    );

    VOID
    ReduceTree(
        ULONG   nColorBits,
        PULONG  pLeafCount,
        NODE  **pReducibleNodes
    );

    VOID DeleteTree(NODE** ppNode);
    VOID GetPaletteColors(NODE* pTree, RGBQUAD* prgb, ULONG* pIndex, ULONG* pSum);
	BYTE GetPixelIndex(LONG x,LONG y, int nbit, LONG effwdt, BYTE *pimage);
};
