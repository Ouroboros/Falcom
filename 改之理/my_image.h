/*****************************************************************************
 *  图形图象公用头文件
 *
 *  2007-01-23  创建文件
 *  2008-03-30  增加像素转换函数
 *****************************************************************************/

#ifndef _MY_IMAGE_H_
#define _MY_IMAGE_H_

typedef unsigned char		byte_t;
typedef unsigned short		uint16;
typedef unsigned long		uint32;
#define INLINE				_inline

/*****************************************************************************
 *  像素格式转换组
 *****************************************************************************/

/* 查表法转换像素 */
static const byte_t     g_by02to256[2] =
{
    0x00, 0xFF
};

static const byte_t     g_by16to256[16] =
{
    0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77,
    0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF
};

static const byte_t     g_by32to256[32] =
{
    0x00, 0x08, 0x10, 0x19, 0x21, 0x29, 0x31, 0x3A,
    0x42, 0x4A, 0x52, 0x5A, 0x63, 0x6B, 0x73, 0x7B,
    0x84, 0x8C, 0x94, 0x9C, 0xA5, 0xAD, 0xB5, 0xBD,
    0xC5, 0xCE, 0xD6, 0xDE, 0xE6, 0xEF, 0xF7, 0xFF
};

static const byte_t     g_by64to256[64] =
{
    0x00, 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
    0x20, 0x24, 0x28, 0x2D, 0x31, 0x35, 0x39, 0x3D,
    0x41, 0x45, 0x49, 0x4D, 0x51, 0x55, 0x59, 0x5D,
    0x61, 0x65, 0x69, 0x6D, 0x71, 0x75, 0x79, 0x7D,
    0x82, 0x86, 0x8A, 0x8E, 0x92, 0x96, 0x9A, 0x9E,
    0xA2, 0xA6, 0xAA, 0xAE, 0xB2, 0xB6, 0xBA, 0xBE,
    0xC2, 0xC6, 0xCA, 0xCE, 0xD2, 0xD7, 0xDB, 0xDF,
    0xE3, 0xE7, 0xEB, 0xEF, 0xF3, 0xF7, 0xFB, 0xFF
};

/***************
    555to8888
****************/
INLINE void     Pixel555To32 (byte_t *dst, uint16 src)
{
    dst[0] = g_by32to256[ src        & 0x1F];
    dst[1] = g_by32to256[(src >>  5) & 0x1F];
    dst[2] = g_by32to256[(src >> 10) & 0x1F];
    dst[3] = 0xFF;
}

/***************
    565to8888
****************/
INLINE void     Pixel565To32 (byte_t *dst, uint16 src)
{
    dst[0] = g_by32to256[ src        & 0x1F];
    dst[1] = g_by64to256[(src >>  5) & 0x3F];
    dst[2] = g_by32to256[(src >> 11) & 0x1F];
    dst[3] = 0xFF;
}

/***************
    1555to8888
****************/
INLINE void     Pixel1555To32 (byte_t *dst, uint16 src)
{
    dst[0] = g_by32to256[ src        & 0x1F];
    dst[1] = g_by32to256[(src >>  5) & 0x1F];
    dst[2] = g_by32to256[(src >> 10) & 0x1F];
    dst[3] = g_by02to256[(src >> 15) & 0x01];
}

/***************
    4444to8888
****************/
INLINE void     Pixel4444To32 (byte_t *dst, uint16 src)
{
    dst[0] = g_by16to256[ src        & 0x0F];
    dst[1] = g_by16to256[(src >>  4) & 0x0F];
    dst[2] = g_by16to256[(src >>  8) & 0x0F];
    dst[3] = g_by16to256[(src >> 12) & 0x0F];
}


/***************
    8888to555
****************/
INLINE void     Pixel32To555 (uint16 *dst, uint32 src)
{
    *dst  = (uint16)((src >> 3) & 0x1F);
    *dst |= (uint16)((src >> 6) & 0x3E0);
    *dst |= (uint16)((src >> 9) & 0x7C00);
    *dst |= 0x8000;
}

/***************
    8888to565
****************/
INLINE void     Pixel32To565 (uint16 *dst, uint32 src)
{
    *dst  = (uint16)((src >> 3) & 0x1F);
    *dst |= (uint16)((src >> 5) & 0x7E0);
    *dst |= (uint16)((src >> 8) & 0xF800);
}

/***************
    8888to1555
****************/
INLINE void     Pixel32To1555 (uint16 *dst, uint32 src)
{
    *dst  = (uint16)((src >>  3) & 0x1F);
    *dst |= (uint16)((src >>  6) & 0x3E0);
    *dst |= (uint16)((src >>  9) & 0x7C00);
    *dst |= (uint16)((src >> 16) & 0x8000);
}

/***************
8888to4444
****************/
INLINE void     Pixel32To4444 (uint16 *dst, uint32 src)
{
    *dst  = (uint16)((src >>  4) & 0xF);
    *dst |= (uint16)((src >>  8) & 0xF0);
    *dst |= (uint16)((src >> 12) & 0xF00);
    *dst |= (uint16)((src >> 16) & 0xF000);
}

#endif  /* _MY_IMAGE_H_ */
