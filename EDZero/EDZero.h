#ifndef _EDZERO_H_e4bdac93_a0b3_452a_8f79_9914db2fbc35
#define _EDZERO_H_e4bdac93_a0b3_452a_8f79_9914db2fbc35

#include "pragma_once.h"

#include <Windows.h>
#include "my_headers.h"

#include <ft2build.h>
#include <freetype/freetype.h>
#include <freetype/ftglyph.h>

enum
{
    ITP_TYPE_UCI_32    = 0xFFFF0000,
};

#define UCL_COMPRESS_MAGIC TAG4('UCL4')

template<class ClassMethodType>
FORCEINLINE ULONG_PTR GetMethodAddress(ClassMethodType Method)
{
    union
    {
        ClassMethodType MethodAddress;
        ULONG_PTR       FuncAddress;
    };

    MethodAddress = Method;
    return FuncAddress;
}

template<class ClassMethodType>
FORCEINLINE ClassMethodType CastMethodAddress(ULONG_PTR Func)
{
    union
    {
        ClassMethodType MethodAddress;
        ULONG_PTR       FuncAddress;
    };

    FuncAddress = Func;
    return MethodAddress;
}

#define GET_METHOD1(Method)  (PVOID)GetMethodAddress(&CEDZero::Method)
#define GET_METHOD2(Method) (PVOID)GetMethodAddress(&CEDZeroFileStream::Method)
#define GET_METHOD3(Method) (PVOID)GetMethodAddress(&CEDZeroBattle::Method)

#pragma pack(1)

typedef struct
{
    ULONG Magic;
    ULONG CompressedSize;
} UCL_COMPRESS_HEADER;

#pragma pack()

class CEDZeroFileStream
{
public:
    ULONG Read(PVOID pvBuffer, ULONG Size, ULONG Count = 1, ULONG Unknown = 0, ULONG Unknown2 = 0);
    BOOL  Seek(LONG Offset, ULONG SeekMethod);
    ULONG Uncompress(PVOID pvOutput, ULONG BlockSize, ULONG BlockCount);

    ULONG OldUncompress(PVOID pvOutput, ULONG BlockSize, ULONG BlockCount);

    DUMMY_STRUCT(0x24);
    ULONG   m_Position;
    ULONG   m_Size;
    DUMMY_STRUCT(0x54);
    BYTE    m_BufferIndex;
    BYTE    m_BufferFlags;

//    static const PBYTE *m_pStaticBuffer = (PBYTE *)0xD3416C;
};

#define MAX_BATTLE_CHAR_NUMBER  0x17

#define GLOBAL_ED_ZERO_POINTER  (*(CEDZero **)0xB9A7F0)

#define ZERO_BATTLE_OFFSET_TO_BASE          0x38498
#define ZERO_BATTLE_MAPPED_ID_OFFSET        0x6074
#define LOAD_STATUS_MEM_OFFSET_TO_BASE      0x38FA8
#define LOAD_STATUS_MEM_OFFSET_TO_MS_DATA   0x4E40

typedef ULONG (THISCALL CEDZeroFileStream::*EDZero_ReadFunc)(PVOID pvBuffer, ULONG Size, ULONG Count, ULONG Unknown, ULONG Unknown2);
typedef ULONG (THISCALL CEDZeroFileStream::*EDZero_SeekFunc)(ULONG Offset, ULONG SeekMethod);
typedef ULONG (THISCALL CEDZeroFileStream::*EDZero_Uncompress)(PVOID pvBuffer, ULONG BlockSize, ULONG BlockCount);

class CEDZero
{
public:

    LONG LoadItp(PCHAR pszFileName, ULONG Index, ULONG Unknown1, ULONG Unknown2, CEDZeroFileStream *pStream, ULONG Unknown3, ULONG Unknown4);
//    BOOL ShowImage(LONG Width, LONG Height, PVOID pvRGB, PVOID pvAlpha, ULONG);

    // addition
    PVOID FormatSEPath(PCHAR pszPath, ULONG SEIndex);

    LONG    THISCALL OldLoadItp(PCHAR pszFileName, ULONG FileNameBufferIndex, ULONG Unknown1, ULONG Unknown2, CEDZeroFileStream *pStream, ULONG Unknown3, ULONG Unknown4);
    PVOID   THISCALL OldFormatSEPath(PCHAR pszPath, ULONG SEIndex);

    PUSHORT GetMappedCharId()
    {
        return (PUSHORT)(*(PBYTE *)((ULONG_PTR)this + ZERO_BATTLE_OFFSET_TO_BASE) + ZERO_BATTLE_MAPPED_ID_OFFSET);
    }

    // not standard this pointer

    VOID THISCALL Fade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6);
    VOID THISCALL OldFade(ULONG Param1, ULONG Param2, ULONG Param3, ULONG Param4, ULONG Param5, ULONG Param6);

public:

    DECL_ALIGN(1) struct YAMANEKO_IMAGE_OBJECT
    {
        DUMMY_STRUCT(0x14);
        USHORT  Unknown;        // 0x1F4E4
        DUMMY_STRUCT(0x5);
        BYTE    Unknown2;       // 0x1F4E9
        DUMMY_STRUCT(0x24);
    };

    DUMMY_STRUCT(0x1F4D0);

    YAMANEKO_IMAGE_OBJECT   m_ImageObject[0x200];
    CHAR                    m_ImageFileName[0x400][10];     // 0x274D0
    ULONG                   m_Unknown[1];                   // 0x29CD0
    DUMMY_STRUCT(0x552A4);
    USHORT                  m_SBreakTable[MAX_BATTLE_CHAR_NUMBER];  // 0x7EF78
    DUMMY_STRUCT(0x1CC6);
    class CEDZeroBattle    *m_Battle;                       // 0x80C6C
};

typedef LONG (THISCALL CEDZero::*EDZero_LoadItpFunc)(PCHAR pszFileName, ULONG FileNameBufferIndex, ULONG Unknown1, ULONG Unknown2, CEDZeroFileStream *pStream, ULONG Unknown3, ULONG Unknown4);
typedef BOOL (THISCALL CEDZero::*EDZero_ShowImageFunc)(LONG Width, LONG Height, PVOID pvRGB, PVOID pvAlpha, ULONG);

typedef PVOID (CDECL *EDZero_AllocFunc)(ULONG Size, PCHAR Useage, ULONG Unknown1, ULONG Unknown2, ULONG Unknown3, ULONG Unknown4);
typedef VOID  (CDECL *EDZero_FreeFunc)(PVOID pvMem);

#pragma pack(1)

typedef struct
{
    USHORT  Level;
    ULONG   HP;
    USHORT  STR;
    USHORT  DEF;
    USHORT  ATS;
    USHORT  ADF;
    USHORT  DEX;
    USHORT  AGL;
    USHORT  AGLAddition;
    USHORT  MOV;
    USHORT  SPD;
} T_STATUS_LEVEL_DATA;

typedef struct
{
    CHAR Description[0x100];
    CHAR Name[0x20];
} ED_ZERO_CRAFT_NAME;

typedef struct  // 0x18
{
    BYTE    Condition;
    BYTE    Probability;
    BYTE    Target;
    BYTE    TargetCondition;
    BYTE    MagicChantAsEffectIndex;
    BYTE    AsEffectIndex;
    WORD    SkillInfoIndex;
    ULONG   Param[4];
} ED_ZERO_AI_INFO;

typedef struct  // 0x20
{
    USHORT  MagicEffectIndex;       // 0x00
    USHORT  Flags;                  // 0x02
    BYTE    Attribute;              // 0x04 µØ ·ç...
    BYTE    Shape;                  // 0x05
    BYTE    Condition;              // 0x06
    DUMMY_STRUCT(1);                // 0x07
    USHORT  ShapeRadius;            // 0x08
    USHORT  ReachRadius;            // 0x0A
    DUMMY_STRUCT(0x2);              // 0x0C
    USHORT  ATConst;                // 0x0E
    USHORT  CPConst;                // 0x10
    DUMMY_STRUCT(2);                // 0x12
    USHORT  DamageModified;         // 0x14
    DUMMY_STRUCT(0xA);              // 0x16
} ED_ZERO_MS_CRAFT_INFO;

#pragma warning(push, 0)

typedef struct  // 0x243C
{
    union
    {
        DUMMY_STRUCT(0x243C);
        struct
        {
            USHORT                  CharPosition;               // 0x00
            USHORT                  State;                      // 0x02
            USHORT                  State2;                     // 0x04
            DUMMY_STRUCT(4);                                    // 0x06
            USHORT                  CharID;                     // 0x0A
            DUMMY_STRUCT(4);                                    // 0x0C
            USHORT                  SymbolTextureFileIndex;     // 0x10     AT face
            USHORT                  SymbolTextureDatIndex;      // 0x12
            USHORT                  MSFileIndex;                // 0x14
            USHORT                  MSDatIndex;                 // 0x16
            USHORT                  ASFileIndex;                // 0x18
            USHORT                  ASDatIndex;                 // 0x1A
            DUMMY_STRUCT(0x156);
            USHORT                  SkillType;                  // 0x172
            DUMMY_STRUCT(0x8);
            USHORT                  WhoAttackMe;                // 0x17C
            USHORT                  CurrentSkillInfoIndex;      // 0x17E
            USHORT                  LastSkillInfoIndex;         // 0x180
            USHORT                  CurrentCraftIndex;          // 0x182
            DUMMY_STRUCT(0x26);
            USHORT                  CraftTargetCharPosition[16];// 0x1AA
            BYTE                    MaxTargetIndex;             // 0x1CA
            BYTE                    CurrentTargetIndex;         // 0x1CB
            COORD                   CraftTargetPosition;        // 0x1CC
            DUMMY_STRUCT(0xB30);
            ED_ZERO_AI_INFO         Craft[10];                  // 0xD00
            ED_ZERO_AI_INFO         SCraft[8];                  // 0xDF0
            USHORT                  SelectedSkillInfoIndex;     // 0xEB0
            BYTE                    MagicChantAsEffectIndex;    // 0xEB2
            BYTE                    SelectedAsEffectIndex;      // 0xEB3
            DUMMY_STRUCT(4);
            ED_ZERO_MS_CRAFT_INFO   CraftInfo[16];              // 0xEB8
            ED_ZERO_CRAFT_NAME      CraftName[16];              // 0xFB8
        };
    };
} ED_ZERO_MONSTER_STATUS_DATA;

#pragma warning(pop)


/************************************************************************
  8D
************************************************************************/

enum
{
    SKILL_TYPE_NORMAL_ATTACK,
    SKILL_TYPE_MOVE,
    SKILL_TYPE_MAGIC,
    SKILL_TYPE_CRAFT,
    SKILL_TYPE_SCRAFT,
    SKILL_TYPE_ITEM,
};

enum
{
    FUNC_AVATAR,

    FUNC_CONDITION_FIRST = 1,

    FUNC_CRAFT_REFLECT = 1,
    FUNC_ARTS_REFLECT,
    FUNC_STR_UP,
    FUNC_STR_DOWN,
    FUNC_DEF_UP,
    FUNC_DEF_DOWN,
    FUNC_SPD_UP,
    FUNC_SPD_DOWN,
    FUNC_ADF_UP,
    FUNC_ADF_DOWN,
    FUNC_AGL_UP,
    FUNC_AGL_DOWN,
    FUNC_ATS_UP,
    FUNC_ATS_DOWN,
    FUNC_CHAR_SIZE,

    FUNC_GANG_KUI = 32,

    FUNC_CONDITION_LAST,

    FUNC_REPLACE_POS = FUNC_CONDITION_LAST,
};

typedef struct
{
    BYTE    Instruction;    // 0x8D
    BYTE    AlwaysZerio;    // 00
    USHORT  FunctionID;
    BYTE    Operation;
    union
    {
        ULONG   Param[3];
        USHORT  wParam[6];
        BYTE    byParam[12];
    };
    BYTE    ByteParam;
} AS_8D;

#pragma pack()


/************************************************************************
  pCharTrueID = [g_pCEDZero]+38498 + 0x6074

  243C bytes per ms
  +0x544 AI
************************************************************************/

#define MAX_CUSTOM_CHAR_ID      0x1F
#define TURN_VOICE_COUNT        6
#define TURN_VOICE_MAP_PATH     "./data/text/voicemap.bin"
#define CHAR_STATUS_INCRESE_FACTOR          3

#define IS_CHAR_CUSTOM(id)  ((id) > 0xC && (id) < 0x15)

DECL_ALIGN(1) class CEDZeroBattle
{
public:

    BOOL THISCALL IsCharControllable(ULONG CharID);
    bool THISCALL OldIsCharControllable(ULONG CharID);

    T_STATUS_LEVEL_DATA* THISCALL CalcCharStatusData(ULONG CharID, ULONG Level);
    T_STATUS_LEVEL_DATA* THISCALL OldCalcCharStatusData(ULONG CharID, ULONG Level);

    BOOL THISCALL   SkipCopyCharStatusData(ED_ZERO_MONSTER_STATUS_DATA *pMsData);
    VOID            NakedSkipCopyCharStatusData();
    VOID            GetCraftData();

    ULONG   THISCALL    GetTurnVoice(ULONG CharID, ULONG RandomIndex);
    ULONG               NakedGetTurnVoice();
    PUSHORT FASTCALL    GetUnderAttackVoice(ED_ZERO_MONSTER_STATUS_DATA *pMSData);
    PUSHORT             NakedGetUnderAttackVoice();

    ULONG64 THISCALL GetBFaceIndex();

    PVOID   THISCALL GetMagicInfo(ULONG MagicIndex);
    PVOID   THISCALL GetMagicQueryTable(ULONG MagicIndex);
    PVOID   THISCALL GetMagicDescription(ULONG MagicIndex);

    ULONG   FASTCALL FindEmptyPosition(BOOL FindEnemyOnly = TRUE);
    bool    THISCALL OldIsAvatarLoaded(ULONG AvatarIndex);
    bool    THISCALL IsAvatarLoaded(ULONG AvatarIndex);
    VOID    FASTCALL AS8DHandler(ULONG Param1, PBYTE pbAsBuffer, ED_ZERO_MONSTER_STATUS_DATA *pMsData);
    VOID    FASTCALL Avatar(AS_8D *pIns, ED_ZERO_MONSTER_STATUS_DATA *pMStatus);

    PUSHORT GetMappedCharId()
    {
        return (PUSHORT)(this->m_pbInfo1 + ZERO_BATTLE_MAPPED_ID_OFFSET);
    }

    CEDZeroBattle* PtrToZeroBattle1(PVOID Pointer)
    {
        PVOID g_pCEDZero;
        g_pCEDZero = *(PVOID *)((ULONG_PTR)Pointer + LOAD_STATUS_MEM_OFFSET_TO_BASE);
        Pointer = (PVOID )((ULONG_PTR)g_pCEDZero + ZERO_BATTLE_OFFSET_TO_BASE);

        return (CEDZeroBattle *)Pointer;
    }

    static VOID FASTCALL GetSBreak(ULONG CharID, ED_ZERO_MONSTER_STATUS_DATA *pMSData);

    PBYTE m_pbInfo1;
    DUMMY_STRUCT(0x4E3C);
    ED_ZERO_MONSTER_STATUS_DATA m_MsData[MAX_BATTLE_CHAR_NUMBER];     // 0x4E40     0x243C * 0x17 = 0x34164

    PVOID   m_Pointer;      // 0x38FA4
    CEDZero *m_EDZero;      // 0x38FA8

    DUMMY_STRUCT(0xAF764);
    ULONG m_CurrentCharIndex;                       // 0xE8708

    static ULONG m_AvatarIndex;
    const static ULONG m_kMaxAsBufferSize = 0x42B0;
};

typedef BOOL (CEDZeroBattle::*LoadMsDataFunc)(ULONG MSFileIndex, ULONG CharPosition);
typedef VOID (CEDZeroBattle::*ResetMSDataFunc)(ULONG CharPosition);
typedef VOID (CEDZeroBattle::*SetAngleFunc)(ULONG FunctionID, ULONG Param);
typedef
BOOL
(CEDZeroBattle::
*CloneMsDataFunc)(
    ED_ZERO_MONSTER_STATUS_DATA *pMStatus,
    USHORT                       SkillInfoIndex,
    ED_ZERO_AI_INFO             *pCraftAI
);


#define FUNC_READ               0x6585A0
#define FUNC_SEEK               0x65B971
#define FUNC_SHOWIMAGE          0x65E81A
#define FUNC_LOADITP            0x7C1DD0
#define FUNC_ALLOC              0x659AAE
#define FUNC_FREE               0x6609BC
#define FUNC_UNCOMPRESS         0x659FAE

#define FUNC_CLONE_MS_DATA      0x6606EC
#define FUNC_RESET_CTRL_DATA    0x65981A
#define FUNC_RESET_MS_DATA      0x65F143
#define FUNC_LOAD_MS_FILE       0x658E92
#define FUNC_SET_ANGLE          0x65E658

#endif // _EDZERO_H_e4bdac93_a0b3_452a_8f79_9914db2fbc35
