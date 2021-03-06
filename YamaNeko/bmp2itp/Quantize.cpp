#include "Quantize.h"

CQuantizer::CQuantizer(ULONG nMaxColors, ULONG nColorBits)
{
	m_nColorBits = nColorBits < 8 ? nColorBits : 8;

	m_pTree	= NULL;
	m_nLeafCount = 0;

    ZeroMemory(m_pReducibleNodes, sizeof(m_pReducibleNodes));

	m_nMaxColors = m_nOutputMaxColors = nMaxColors;

	if (m_nMaxColors < 16)
        m_nMaxColors = 16;
}

CQuantizer::~CQuantizer()
{
	if (m_pTree	!= NULL)
		DeleteTree(&m_pTree);
}

BOOL CQuantizer::ProcessImage(HANDLE hImage)
{
	BYTE r,	g, b, a;
	int	i, j;

	BITMAPINFOHEADER ds;
	memcpy(&ds,hImage, sizeof(ds));
	int effwdt = ((((ds.biBitCount * ds.biWidth ) + 31) / 32) * 4);

	int	nPad = effwdt - (((ds.biWidth *	ds.biBitCount) + 7) / 8);

	PBYTE pbBits = (PBYTE)hImage + *(DWORD*)hImage + ds.biClrUsed * sizeof(RGBQUAD);

	switch (ds.biBitCount)
    {
	    case 1:	// 1-bit DIB
	    case 4:	// 4-bit DIB
	    case 8:	// 8-bit DIB
		    for	(i = 0; i < ds.biHeight; i++)
            {
			    for	(j = 0; j<ds.biWidth; j++)
                {
				    BYTE idx = GetPixelIndex(j,i,ds.biBitCount,effwdt,pbBits);
				    PBYTE pal = (PBYTE)(hImage) + sizeof(BITMAPINFOHEADER);
				    LONG ldx = idx * sizeof(RGBQUAD);
				    b = pal[ldx];
				    g = pal[ldx+1];
				    r = pal[ldx+2];
				    a = pal[ldx+3];
				    AddColor (&m_pTree,	r, g, b, a, m_nColorBits, 0, &m_nLeafCount, m_pReducibleNodes);

				    while (m_nLeafCount	> m_nMaxColors)
					    ReduceTree (m_nColorBits, &m_nLeafCount, m_pReducibleNodes);
			    }
		    }
		    break;

	    case 24: //	24-bit DIB
		    for	(i = 0; i < ds.biHeight; i++)
            {
			    for	(j = 0; j < ds.biWidth; j++)
                {
				    b =	*pbBits++;
				    g =	*pbBits++;
				    r =	*pbBits++;

				    AddColor(&m_pTree, r, g, b, 0, m_nColorBits, 0, &m_nLeafCount, m_pReducibleNodes);
				    while (m_nLeafCount	> m_nMaxColors)
					    ReduceTree (m_nColorBits, &m_nLeafCount, m_pReducibleNodes);
			    }
			    pbBits += nPad;
		    }
		    break;

	    default: //	Unrecognized color format
		    return FALSE;
	}

	return TRUE;
}

HRESULT CQuantizer::ProcessRawData(IMG_BITMAP_HEADER *pBmp, PVOID pvRaw)
{
    LONG    Stride, BytesPad;
    PBYTE   pbRaw;

    Stride      = GetBitmapStride(pBmp->Info.dwWidth, pBmp->Info.wBit);
    BytesPad    = Stride - pBmp->Info.dwWidth * pBmp->Info.wBit / 8;
    pbRaw       = (PBYTE)pvRaw;

    switch (pBmp->Info.wBit)
    {
        case 32:
            for (ULONG Height = pBmp->Info.dwHeight; Height; --Height)
            {
                for (ULONG Width = pBmp->Info.dwWidth; Width; --Width)
                {
                    ULONG r, g, b, a;

                    b = *pbRaw++;
                    g = *pbRaw++;
                    r = *pbRaw++;
                    a = *pbRaw++;

                    AddColor(
                        &m_pTree,
                        r,
                        g,
                        b,
                        a,
                        m_nColorBits,
                        0,
                        &m_nLeafCount,
                        m_pReducibleNodes
                    );

                    while (m_nLeafCount	> m_nMaxColors)
                        ReduceTree(m_nColorBits, &m_nLeafCount, m_pReducibleNodes);
                }

                *(PULONG)&pbRaw += BytesPad;
            }
            break;

        default:
            return TYPE_E_UNSUPFORMAT;
    }

    return S_OK;
}

VOID
CQuantizer::
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
)
{
	static BYTE	mask[8]	= {	0x80, 0x40,	0x20, 0x10,	0x08, 0x04,	0x02, 0x01 };

	// If the node doesn't exist, create it.
	if (*ppNode	== NULL)
		*ppNode	= (NODE*)CreateNode (nLevel, nColorBits, pLeafCount, pReducibleNodes);

	// Update color	information	if it's	a leaf node.
	if ((*ppNode)->bIsLeaf)	{
		(*ppNode)->nPixelCount++;
		(*ppNode)->nRedSum += r;
		(*ppNode)->nGreenSum +=	g;
		(*ppNode)->nBlueSum	+= b;
		(*ppNode)->nAlphaSum += a;
	} else {	// Recurse a level deeper if the node is not a leaf.
		int	shift =	7 -	nLevel;
		int	nIndex =(((r & mask[nLevel]) >> shift) << 2) |
					(((g & mask[nLevel]) >>	shift) << 1) |
					(( b & mask[nLevel]) >> shift);
		AddColor (&((*ppNode)->pChild[nIndex]),	r, g, b, a, nColorBits,
					nLevel + 1,	pLeafCount,	pReducibleNodes);
	}
}

VOID* CQuantizer::CreateNode (ULONG nLevel, ULONG	nColorBits,	ULONG* pLeafCount,
	NODE** pReducibleNodes)
{
	NODE* pNode = (NODE*)calloc(1,sizeof(NODE));

	if (pNode== NULL) return NULL;

	pNode->bIsLeaf = (nLevel ==	nColorBits)	? TRUE : FALSE;
	if (pNode->bIsLeaf) (*pLeafCount)++;
	else {
		pNode->pNext = pReducibleNodes[nLevel];
		pReducibleNodes[nLevel]	= pNode;
	}
	return pNode;
}

VOID CQuantizer::ReduceTree	(ULONG nColorBits, ULONG*	pLeafCount,
	NODE** pReducibleNodes)
{
	int i;
	// Find	the	deepest	level containing at	least one reducible	node.
	for	(i=nColorBits -	1; (i>0) &&	(pReducibleNodes[i]	== NULL); i--);

	// Reduce the node most	recently added to the list at level	i.
	NODE* pNode	= pReducibleNodes[i];
	pReducibleNodes[i] = pNode->pNext;

	ULONG nRedSum = 0;
	ULONG nGreenSum = 0;
	ULONG nBlueSum =	0;
	ULONG nAlphaSum = 0;
	ULONG nChildren = 0;

	for	(i=0; i<8; i++)	{
		if (pNode->pChild[i] !=	NULL) {
			nRedSum	+= pNode->pChild[i]->nRedSum;
			nGreenSum += pNode->pChild[i]->nGreenSum;
			nBlueSum +=	pNode->pChild[i]->nBlueSum;
			nAlphaSum += pNode->pChild[i]->nAlphaSum;
			pNode->nPixelCount += pNode->pChild[i]->nPixelCount;
			free(pNode->pChild[i]);
			pNode->pChild[i] = NULL;
			nChildren++;
		}
	}

	pNode->bIsLeaf = TRUE;
	pNode->nRedSum = nRedSum;
	pNode->nGreenSum = nGreenSum;
	pNode->nBlueSum	= nBlueSum;
	pNode->nAlphaSum	= nAlphaSum;
	*pLeafCount	-= (nChildren -	1);
}

VOID CQuantizer::DeleteTree	(NODE**	ppNode)
{
	for	(int i=0; i<8; i++)	{
		if ((*ppNode)->pChild[i] !=	NULL) DeleteTree (&((*ppNode)->pChild[i]));
	}
	free(*ppNode);
	*ppNode	= NULL;
}

VOID CQuantizer::GetPaletteColors (NODE* pTree,	RGBQUAD* prgb, ULONG* pIndex, ULONG* pSum)
{
	if (pTree){
		if (pTree->bIsLeaf)	{
			prgb[*pIndex].rgbRed   = (BYTE)min(255,0.5f + ((float)pTree->nRedSum)   / pTree->nPixelCount);
			prgb[*pIndex].rgbGreen = (BYTE)min(255,0.5f + ((float)pTree->nGreenSum) / pTree->nPixelCount);
			prgb[*pIndex].rgbBlue  = (BYTE)min(255,0.5f + ((float)pTree->nBlueSum)  / pTree->nPixelCount);
			prgb[*pIndex].rgbReserved =	(BYTE)min(255,0.5f + ((float)pTree->nAlphaSum) / pTree->nPixelCount);
			if (pSum) pSum[*pIndex] = pTree->nPixelCount;
			(*pIndex)++;
		} else {
			for	(int i=0; i<8; i++)	{
				if (pTree->pChild[i] !=	NULL)
					GetPaletteColors (pTree->pChild[i],	prgb, pIndex, pSum);
			}
		}
	}
}

ULONG CQuantizer::GetColorCount ()
{
	return m_nLeafCount;
}

VOID CQuantizer::SetColorTable (RGBQUAD* prgb)
{
	ULONG nIndex	= 0;
	if (m_nOutputMaxColors<16){
		ULONG nSum[16];
		RGBQUAD tmppal[16];
		GetPaletteColors (m_pTree, tmppal, &nIndex, nSum);
		if (m_nLeafCount>m_nOutputMaxColors) {
			ULONG j,k,nr,ng,nb,na,ns,a,b;
			for (j=0;j<m_nOutputMaxColors;j++){
				a=(j*m_nLeafCount)/m_nOutputMaxColors;
				b=((j+1)*m_nLeafCount)/m_nOutputMaxColors;
				nr=ng=nb=na=ns=0;
				for (k=a;k<b;k++){
					nr+=tmppal[k].rgbRed * nSum[k];
					ng+=tmppal[k].rgbGreen * nSum[k];
					nb+=tmppal[k].rgbBlue * nSum[k];
					na+=tmppal[k].rgbReserved * nSum[k];
					ns+= nSum[k];
				}
				prgb[j].rgbRed   = (BYTE)min(255,0.5f + ((float)nr)/ns);
				prgb[j].rgbGreen = (BYTE)min(255,0.5f + ((float)ng)/ns);
				prgb[j].rgbBlue  = (BYTE)min(255,0.5f + ((float)nb)/ns);
				prgb[j].rgbReserved = (BYTE)min(255,0.5f + ((float)na)/ns);
			}
		} else {
			memcpy(prgb,tmppal,m_nLeafCount * sizeof(RGBQUAD));
		}
	} else {
		GetPaletteColors (m_pTree, prgb, &nIndex, 0);
	}
}

BYTE CQuantizer::GetPixelIndex(LONG x, LONG y, int nbit, LONG effwdt, BYTE *pimage)
{
	if (nbit==8){
		return pimage[y*effwdt + x];
	} else {
		BYTE pos;
		BYTE iDst= pimage[y*effwdt + (x*nbit >> 3)];
		if (nbit==4){
			pos = (BYTE)(4*(1-x%2));
			iDst &= (0x0F<<pos);
			return (iDst >> pos);
		} else if (nbit==1){
			pos = (BYTE)(7-x%8);
			iDst &= (0x01<<pos);
			return (iDst >> pos);
		}
	}
	return 0;
}
