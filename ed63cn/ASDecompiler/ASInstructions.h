#ifndef _ASINSTRUCTIONS_H_
#define _ASINSTRUCTIONS_H_

#include "pragma_once.h"
#include "ASDecompiler.h"

enum ED6_AS_INSTRUCTION
{
    AS_END                  = 0x00,
    AS_GOTO                 = 0x01,
    AS_SELECT_SUB_CHIP      = 0x02,
    AS_DEG                  = 0x03,
    AS_04                   = 0x04,
    AS_05                   = 0x05,
    AS_SLEEP                = 0x06,
    AS_CLEAR_EFFECT         = 0x07,
    AS_TELEPORT             = 0x08,
    AS_09                   = 0x09,
    AS_0A                   = 0x0A,
    AS_TURN                 = 0x0B,
    AS_0C                   = 0x0C,
    AS_JUMP                 = 0x0D,
    AS_DROP_DOWN            = 0x0E,
    AS_JUMP_TO_TARGET       = 0x0F,
    AS_JUMP_BACK            = 0x10,
    AS_MOVE                 = 0x11,
    AS_ADD_EFFECT           = 0x12,
    AS_RELEASE_EFFECT       = 0x13,
    AS_14                   = 0x14,
    AS_WAIT_EFFECT          = 0x15,
    AS_FINISH_EFFECT        = 0x16,
    AS_CANCLE_EFFECT        = 0x17,
    AS_SHOW_EFFECT          = 0x18,
    AS_SHOW_3DEFFECT        = 0x19,
    AS_1A                   = 0x1A,
    AS_SELECT_CHIP          = 0x1B,
    AS_DAMAGE               = 0x1C,
    AS_DAMAGE_ANIME         = 0x1D,
    AS_1E                   = 0x1E,
    AS_1F                   = 0x1F,
    AS_20                   = 0x20,
    AS_21                   = 0x21,
    AS_BEGINTHREAD          = 0x22,
    AS_WAITTHREAD           = 0x23,
    AS_SET_CHIP_MODE_FLAG   = 0x24,
    AS_CLEAR_CHIP_MODE_FLAG = 0x25,
    AS_26                   = 0x26,
    AS_27                   = 0x27,
    AS_CHAR_SAY             = 0x28,
    AS_29                   = 0x29,
    AS_TIP_TEXT             = 0x2A,
    AS_2B                   = 0x2B,
    AS_SHADOW_BEGIN         = 0x2C,
    AS_SHADOW_END           = 0x2D,
    AS_SHAKE_CHAR           = 0x2E,
    AS_SUSPEND_THREAD       = 0x2F,
    AS_30                   = 0x30,
    AS_31                   = 0x31,
    AS_32                   = 0x32,
    AS_33                   = 0x33,
    AS_34                   = 0x34,
    AS_KEEP_ANGLE           = 0x35,
    AS_36                   = 0x36,
    AS_ROTATION_ANGLE       = 0x37,
    AS_ROTATION_ANGLE_V     = 0x38,
    AS_SET_ANGLE            = 0x39,
    AS_TILT_ANGLE           = 0x3A,
    AS_ROTATION_ANGLE_H     = 0x3B,
    AS_3C                   = 0x3C,
    AS_SHAKE_SCREEN         = 0x3D,
    AS_3E                   = 0x3E,
    AS_3F                   = 0x3F,
    AS_40                   = 0x40,
    AS_LOCK_ANGLE           = 0x41,
    AS_42                   = 0x42,
    AS_SET_BK_COLOR         = 0x43,
    AS_ZOOM_ANGLE           = 0x44,
    AS_45                   = 0x45,
    AS_46                   = 0x46,
    AS_47                   = 0x47,
    AS_48                   = 0x48,
    AS_SET_CONTROL          = 0x49,
    AS_4A                   = 0x4A,
    AS_RANDOM               = 0x4B,
    AS_LOOP_TARGET_BEG      = 0x4C,
    AS_RESET_LOOP_TARGET    = 0x4D,
    AS_LOOP_TARGET_END      = 0x4E,
    AS_4F                   = 0x4F,
    AS_CALL                 = 0x50,
    AS_RET                  = 0x51,
    AS_52                   = 0x52,
    AS_53                   = 0x53,
    AS_54                   = 0x54,
    AS_MAGIC_CAST_BEGIN     = 0x55,
    AS_MAGIC_CAST_END       = 0x56,
    AS_57                   = 0x57,
    AS_BEAT_BACK            = 0x58,
    AS_59                   = 0x59,
    AS_5A                   = 0x5A,
    AS_5B                   = 0x5B,
    AS_SHOW                 = 0x5C,
    AS_HIDE                 = 0x5D,
    AS_5E                   = 0x5E,
    AS_5F                   = 0x5F,
    AS_60                   = 0x60,
    AS_SET_BATTLE_SPEED     = 0x61,
    AS_62                   = 0x62,
    AS_63                   = 0x63,
    AS_SOUND_EFFECT         = 0x64,
    AS_SOUND_EFFECTEX       = 0x65,
    AS_66                   = 0x66,
    AS_SCRAFT_CUT_IN        = 0x67,
    AS_68                   = 0x68,
    AS_RELEASE_TEXTURE      = 0x69,
    AS_LOAD_SCHIP           = 0x6A,
    AS_RESET_SCRAFT_CHIP    = 0x6B,
    AS_DIE                  = 0x6C,
    AS_6D                   = 0x6D,
    AS_6E                   = 0x6E,
    AS_6F                   = 0x6F,
    AS_70                   = 0x70,
    AS_71                   = 0x71,
    AS_72                   = 0x72,
    AS_73                   = 0x73,
    AS_74                   = 0x74,
    AS_75                   = 0x75,
    AS_76                   = 0x76,
    AS_77                   = 0x77,
    AS_SET_EFF_STATE        = 0x78,
    AS_79                   = 0x79,
    AS_CRAFT_END            = 0x7A,
    AS_SET_CRAFT_END_FLAG   = 0x7B,
    AS_7C                   = 0x7C,
    AS_7D                   = 0x7D,
    AS_7E                   = 0x7E,
    AS_BLUR_SCREEN          = 0x7F,
    AS_80                   = 0x80,
    AS_81                   = 0x81,
    AS_82                   = 0x82,
    AS_SORT_TARGET          = 0x83,
    AS_ROTATE_CHAR          = 0x84,
    AS_85                   = 0x85,
    AS_86                   = 0x86,
    AS_87                   = 0x87,
    AS_VOICE                = 0x88,
    AS_SAVE_CUR_POS         = 0x89,
    AS_CLONE                = 0x8A,
    AS_USE_ITEM_BEGIN       = 0x8B,
    AS_USE_ITEM_END         = 0x8C,
    AS_ZOOM                 = 0x8D,
    AS_LOAD_X_FILE          = 0x8E,
    AS_8F                   = 0x8F,
    AS_90                   = 0x90,
    AS_91                   = 0x91,
    AS_92                   = 0x92,
    AS_93                   = 0x93,
    AS_94                   = 0x94,
    AS_95                   = 0x95,
    AS_SET_ANGLE_TARGET     = 0x96,
    AS_MOVE_ANGLE           = 0x97,
    AS_98                   = 0x98,
    AS_99                   = 0x99,
    AS_9A                   = 0x9A,
    AS_9B                   = 0x9B,
    AS_RESET_CHIP_STATUS    = 0x9C,
    AS_9D                   = 0x9D,
    AS_SET_TIMER            = 0x9E,
    AS_SET_BATTLE_MODE      = 0x9F,
    AS_A0                   = 0xA0,
    AS_A1                   = 0xA1,
    AS_A2                   = 0xA2,
    AS_A3                   = 0xA3,
    AS_A4                   = 0xA4,
    AS_A5                   = 0xA5,
    AS_A6                   = 0xA6,
    AS_BATTLE_EFFECT_END    = 0xA7,
    AS_DAMAGE_VOICE         = 0xA8,
    AS_A9                   = 0xA9,
    AS_AA                   = 0xAA,
    AS_AB                   = 0xAB,
    AS_AC                   = 0xAC,
    AS_AD                   = 0xAD,
    AS_AE                   = 0xAE,
    AS_AF                   = 0xAF,
    AS_B0                   = 0xB0,
    AS_B1                   = 0xB1,

    AS_CUSTOM_8B            = 0xB2,

    AS_INTERNAL_BASE        = 0x80000000,
    AS_INTERNAL_GOTO        = AS_INTERNAL_BASE,
};

#define ED6_INVALID_INDEX      (~0)
#define ED6_INVALID_OFFSET     ((USHORT)(-1))

#pragma pack(1)

typedef struct
{
    USHORT CHIndex;
    USHORT CHDatIndex;
    USHORT CPIndex;
    USHORT CPDatIndex;
} CHAR_CHIP_PATTERN_INFO;

typedef struct
{
    USHORT CraftOffsetTableOffset;
    USHORT CraftOffsetTableEndOffset;
    USHORT Unknown;
    CHAR_CHIP_PATTERN_INFO ChrChipPtnInfo[1];  // end with 0xFFFFFFFF, generally 2d-char is 7, 3d-char is 0
    CHAR   XFileName[1];        // sth. like boss32200\CH32200.x
    USHORT CraftOffsetTable[1]; // 31 ~ 33 entries ?
} _ED6_ACTION_SCRIPT_STRICT;

typedef struct
{
    USHORT MagicEffect;     // 1
    USHORT Stand;           // 2
    USHORT Move;            // 3
    USHORT UnderAttack;     // 4
    USHORT Dead;            // 5
    USHORT NormalAttack;    // 6
    USHORT MagicSpell;      // 7
    USHORT MagicCast;       // 8
    USHORT Win;             // 9
    USHORT Unknown;         // 10
    USHORT UseItem;         // 11
    USHORT Coma;            // 12
    USHORT UserDefined[1];
//    USHORT Reserve1;        // 13
//    USHORT Reserve2;        // 14
//    USHORT Reserve3;        // 15
//    USHORT Reserve4;        // 16
//    USHORT Craft[10];       // 17 - 26
//    USHORT SCraft[5];       // 27 - 31
} CRAFT_OFFSET_TABLE_BASE;

#define INSTRUCTION_LENGTH_STRING (-1L)
#define INSTRUCTION_PARAM_FLAG_ADDRESS  0x00000001

typedef struct
{
    ULONG           Length;
    ULONG           Flags;
    LARGE_INTEGER   Value;
} ED6_INSTRUCTION_PARAM;

#define INSTRUCTION_MAX_PARAM       15
#define INSTRUCTION_FLAG_LABEL      0x00000001
#define INSTRUCTION_FLAG_ADDRESS    0x00000002
#define INSTRUCTION_FLAG_LINK       0x00000004
#define INSTRUCTION_FLAG_FLOAT      0x00000008
#define INSTRUCTION_FLAG_LOOP       0x00000010
#define INSTRUCTION_FLAG_DUMPED     0x10000000
#define INSTRUCTION_FLAG_UNLABEL    0x20000000

typedef struct _tagED6Instruction
{
    ULONG                       Code;
    ULONG                       Offset;
    ULONG                       ParamNumber;
    ULONG                       Flags;
    ED6_INSTRUCTION_PARAM       Param[INSTRUCTION_MAX_PARAM];
} ED6_INSTRUCTION;

typedef struct
{
    ULONG Count;
    ULONG MaxCount;
    ULONG Offset;
    ED6_INSTRUCTION *pInstruction;
} ED6_AS_CRAFT_INFO;

#define ASINFO_FLAG_LOOPBEG     0x00000001
#define ASINFO_FLAG_LOOPEND     0x00000002

typedef struct
{
    PBYTE                   pbAsBuffer;
    PBYTE                   pbCurrent;
    ULONG                   BufferSize;
    ULONG                   CraftOffsetTableOffset;
    ULONG                   CraftOffsetTableEndOffset;
    ULONG                   Unknown;
    LPSTR                   pszXFileName;
    ULONG                   ChrChipPtnCount;
    ULONG                   CraftCount;
    ULONG                   FunctionCount;
    ED6_AS_CRAFT_INFO       *pCraftInfo;
    ED6_AS_CRAFT_INFO       *pFunctionInfo;
    ED6_AS_CRAFT_INFO      **pFunctionTable;
    CHAR_CHIP_PATTERN_INFO  *pChrChipPtnInfo;
    CRAFT_OFFSET_TABLE_BASE *pCraftOffsetTable;
    ULONG                   Flags;
    ULONG                   lParam;
} ED6_ACTION_SCRIPT_INFO;

#pragma pack()

#endif // _ASINSTRUCTIONS_H_