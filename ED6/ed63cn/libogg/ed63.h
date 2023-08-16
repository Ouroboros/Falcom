#include <Windows.h>
#include <d3d8.h>
#include "my_headers.h"

#pragma pack(1)

/************************************************************************
  types
************************************************************************/

class CED6Effect
{

};

typedef struct
{
    CHAR  FileName[0xC];
    ULONG Unknown;
    ULONG Size;
    ULONG Unknown2[3];
    ULONG Offset;
} ED6_DIR_ENTRY;

typedef struct
{
    CHAR   Tag[6];
    USHORT MaxFile;
    USHORT FileCount;
    union
    {
        ULONG EntrySize;
        BYTE  Reserve[6];
    };
    ED6_DIR_ENTRY Entry[1];
} ED6_DIR_HEADER;

typedef struct
{
    PBYTE pbAsBuffer;
    ULONG Unknown[9];
    PBYTE pbAsBase;
} ED6_AS_CRAFT_INFO;

typedef struct
{
    BYTE    Condition;
    BYTE    Probability;
    BYTE    Target;
    BYTE    TargetCondition;
    BYTE    MagicChantAsEffectIndex;
    BYTE    AsEffectIndex;
    WORD    SkillInfoIndex;
    ULONG   Param[4];
} ED6_AI_INFO;

typedef struct
{
    USHORT  MagicEffectIndex;
    USHORT  Flags;
    DUMMY_STRUCT(1);
    BYTE    Shape;
    DUMMY_STRUCT(2);
    USHORT  ShapeRadius;
    USHORT  ReachRadius;
    DUMMY_STRUCT(0x2);
    USHORT  ATConst;
    USHORT  CPConst;
    DUMMY_STRUCT(2);
    USHORT  DamageModified;
    DUMMY_STRUCT(0xA);
} ED6_MS_CRAFT_INFO;

typedef struct
{
    CHAR Description[0x100];
    CHAR Name[0x20];
} ED6_CRAFT_NAME;

enum
{
    SKILL_TYPE_NORMAL_ATTACK,
    SKILL_TYPE_MOVE,
    SKILL_TYPE_MAGIC,
    SKILL_TYPE_CRAFT,
    SKILL_TYPE_SCRAFT,
    SKILL_TYPE_ITEM,
};

typedef struct
{
    CHAR    CharName[0x20];
    DUMMY_STRUCT(0x24);
    FLOAT   X;
    FLOAT   H;
    FLOAT   Y;
} ED6_MS_CTRL_INFO;

typedef struct
{
    ULONG               ConditionFlags;
    PVOID               pvEffect;
    BYTE                Unknown2[2];
    USHORT              ConditionRate;
    ULONG               ATLeft;
    ULONG               Unknown4;
} ED6_CONDITION_INFO;

typedef struct
{
    USHORT              CharPosition;
    DUMMY_STRUCT(1);
    BYTE                State;
    USHORT              State2;
    DUMMY_STRUCT(4);
    USHORT              CharID;
    DUMMY_STRUCT(4);
    USHORT              SymbolTextureFileIndex; // at face
    USHORT              SymbolTextureDatIndex;
    USHORT              MSFileIndex;
    USHORT              MSDatIndex;
    USHORT              ASFileIndex;
    USHORT              ASDatIndex;
    DUMMY_STRUCT(0x162);
    USHORT              SkillType;
    DUMMY_STRUCT(0x8);
    USHORT              WhoAttackMe;
    USHORT              CurrentSkillInfoIndex;
    USHORT              LastSkillInfoIndex;
    USHORT              CurrentCraftIndex;
    DUMMY_STRUCT(0x28);
    USHORT              CraftTargetCharPosition[16];
    BYTE                MaxTargetIndex;
    BYTE                CurrentTargetIndex;
    USHORT              SelectedTargetX;
    USHORT              SelectedTargetY;
    DUMMY_STRUCT(0x46);
    ED6_MS_CTRL_INFO   *pControlInfo;
    FLOAT               CharSize;   // 0.4 per grid
    ULONG               LevelInMS;
    ULONG               HPMaxInMS;
    ULONG               HPCurrentInMS;
    USHORT              EPMaxInMS;
    USHORT              EPCurrentInMS;
    USHORT              CPMaxInMS;
    USHORT              CPCurrentInMS;
    DUMMY_STRUCT(0x28);
    ULONG               Level;
    ULONG               HPMax;
    ULONG               HPCurrent;
    USHORT              EPMax;
    USHORT              EPCurrent;
    USHORT              CPCurrent;
    DUMMY_STRUCT(6);
    USHORT              STR;
    USHORT              DEF;
    USHORT              ATS;
    USHORT              ADF;
    USHORT              DEX;
    USHORT              AGL;
    USHORT              MOV;
    USHORT              SPD;
    USHORT              CPMax;
    DUMMY_STRUCT(0xA);
    ULONG               CurrentCondition;
    DUMMY_STRUCT(8);
    ED6_CONDITION_INFO  Condition[0x20];
    DUMMY_STRUCT(0x24);
    USHORT              AIType;
    DUMMY_STRUCT(0x22);
    ED6_AI_INFO         NormalAttackAI;
    ED6_AI_INFO         MagicAI[80];
    ED6_AI_INFO         CraftAI[10];
    ED6_AI_INFO         SCraftAI[5];
    USHORT              SelectedSkillInfoIndex;
    BYTE                MagicChantAsEffectIndex;
    BYTE                SelectedAsEffectIndex;
    DUMMY_STRUCT(4);
    ED6_MS_CRAFT_INFO   MSCraftInfo[16];
    ED6_CRAFT_NAME      CraftName[16];
    DUMMY_STRUCT(0x4B);
    BYTE                Sepith[7];
    DUMMY_STRUCT(4);
    USHORT              ResistanceUnknown;
    USHORT              Resistance[7];
    DUMMY_STRUCT(2);
    ULONG               StateResistanceFlags;
    DUMMY_STRUCT(8);
    PVOID               pPrivateEffectBuffer[16];
    CED6Effect         *pPrivateEffectInfo[16];
    DUMMY_STRUCT(0x104);
    ULONG               PillarCount;
    DUMMY_STRUCT(0x1C);
} ED6_MONSTER_STATUS_DATA;

#define CONDITION_POISON                0x00000001
#define CONDITION_FROZEN                0x00000002
#define CONDITION_LANDIFICATION         0x00000004
#define CONDITION_SLEEPING              0x00000008
#define CONDITION_NO_ARTS               0x00000010
#define CONDITION_DARKNESS              0x00000020
#define CONDITION_NO_CRAFT              0x00000040
#define CONDITION_CHAOS                 0x00000080
#define CONDITION_STUN                  0x00000100
#define CONDITION_SECOND_KILL           0x00000200
#define CONDITION_DEF_DOWN              0x00000400
#define CONDITION_RAGE                  0x00000800
#define CONDITION_ARTS_GUARD            0x00001000
#define CONDITION_CRAFT_GUARD           0x00002000
#define CONDITION_MOV_UP                0x00004000
#define CONDITION_MOV_DOWN              0x00008000
#define CONDITION_STR_UP                0x00010000
#define CONDITION_STR_DOWN              0x00020000
#define CONDITION_DEF_UP                0x00040000
#define CONDITION_DEF_DOWN2             0x00080000
#define CONDITION_SPD_UP                0x00100000
#define CONDITION_SPD_DOWN              0x00200000
#define CONDITION_ADF_UP                0x00400000
#define CONDITION_ADF_DOWN              0x00800000
#define CONDITION_AGL_UP                0x01000000
#define CONDITION_AGL_DOWN              0x02000000
#define CONDITION_MAX_GUARD             0x04000000
#define CONDITION_VANISH                0x08000000
#define CONDITION_CONDITION_GUARD       0x10000000
#define CONDITION_FAT                   0x20000000
#define CONDITION_ATS_UP                0x40000000
#define CONDITION_FORCE_SECOND_KILL     0x80000000    // only valid in AS file

#define EX_CONDITION_CRAFT_REFLECT      0x00000001
#define EX_CONDITION_ARTS_REFLECT       0x00000002
#define EX_CONDITION_STR_UP             0x00000004
#define EX_CONDITION_STR_DOWN           0x00000008
#define EX_CONDITION_DEF_UP             0x00000010
#define EX_CONDITION_DEF_DOWN           0x00000020
#define EX_CONDITION_SPD_UP             0x00000040
#define EX_CONDITION_SPD_DOWN           0x00000080
#define EX_CONDITION_ADF_UP             0x00000100
#define EX_CONDITION_ADF_DOWN           0x00000200
#define EX_CONDITION_AGL_UP             0x00000400
#define EX_CONDITION_AGL_DOWN           0x00000800
#define EX_CONDITION_ATS_UP             0x00001000
#define EX_CONDITION_ATS_DOWN           0x00002000
#define EX_CONDITION_CHAR_SIZE          0x00004000
#define EX_CONDITION_GANG_KUI           0x80000000

#define EX_CONDITION_NUMBER             32

#define MAX_CHAR_POSITION               15
#define MAX_CHAR_NUMBER                 (MAX_CHAR_POSITION + 1)

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

enum
{
    OP_SET,
    OP_GET,
    OP_XCHG,
    OP_ADD,
    OP_SUB,
    OP_MUL,
    OP_DIV,
};

enum
{
    POS_SELF        = 0xFF,
    POS_DEST        = 0xFB,
    POS_TARGET      = 0xFE,
    POS_FRONT       = 0xEB,
    POS_SELFFRONT   = 0x8B,
};

enum
{
    GANGKUI_REFLECT,
    GANGKUI_NOT_REFLECT,
    GANGKUI_NOT_REFLECT_ONCE,
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
} INSTRUCTION_8D;

typedef struct
{
    ULONG               ConditionFlag;
    ULONG               ATLeft;
    union
    {
        ULONG           Param[2];
        USHORT          wParam[4];
        BYTE            byParam[8];
    };
    ULONG               ByteParam;
    LPARAM              lParam[2];
} CUSTOM_CONDITION_INFO;

typedef struct
{
    ULONG                   m_ConditionFlags;
    CUSTOM_CONDITION_INFO   m_Conditions[32];
} CUSTOM_MONSTER_STATUS;

typedef struct
{
    USHORT STR;
    USHORT DEF;
    USHORT ATS;
    USHORT ADF;
    USHORT DEX;
    USHORT AGL;
    USHORT MOV;
    USHORT SPD;
} CUSTOM_ATTRIBUTE_ADDITION;

struct CUSTOM_BATTLE_INFO
{
    CUSTOM_MONSTER_STATUS m_MStatus[MAX_CHAR_NUMBER];

    CUSTOM_BATTLE_INFO()
    {
        Reset();
    }

    VOID Reset()
    {
        ZeroMemory(m_MStatus, sizeof(m_MStatus));
    }

    NoInline CUSTOM_CONDITION_INFO* FindCondition(ULONG CharPosition, ULONG Condition)
    {
        CUSTOM_MONSTER_STATUS *pMStatus;
        CUSTOM_CONDITION_INFO *pCondition;

        pMStatus = &m_MStatus[CharPosition];
        pCondition = pMStatus->m_Conditions;
        if (Condition == 0)
        {
            for (ULONG Count = countof(m_MStatus->m_Conditions); Count; ++pCondition, --Count)
                if (pCondition->ConditionFlag == Condition)
                    return pCondition;

            return NULL;
        }

        if (!TEST_BITS(pMStatus->m_ConditionFlags, Condition))
            return NULL;

        for (ULONG Count = countof(m_MStatus->m_Conditions); Count; ++pCondition, --Count)
            if (pCondition->ConditionFlag & Condition)
                return pCondition;

        return NULL;
    }

    NoInline BOOL GetAttributeAddition(ULONG CharPosition, CUSTOM_ATTRIBUTE_ADDITION *pAddition)
    {
        CUSTOM_CONDITION_INFO *pInfo;
        CUSTOM_MONSTER_STATUS *pMStatus;

        if (CharPosition > countof(m_MStatus))
            return FALSE;

        ZeroMemory(pAddition, sizeof(*pAddition));
        pMStatus = m_MStatus + CharPosition;
        pInfo = FindCondition(CharPosition, EX_CONDITION_CRAFT_REFLECT);
        if (pInfo != NULL)
            pAddition->DEF += pInfo->wParam[0];

        pInfo = FindCondition(CharPosition, EX_CONDITION_ARTS_REFLECT);
        if (pInfo != NULL)
            pAddition->ADF += pInfo->wParam[0];
/*
        pInfo = FindCondition(CharPosition, EX_CONDITION_GANG_KUI);
        if (pInfo != NULL)
        {
            pAddition->DEF += pInfo->wParam[0];
            pAddition->ADF += pInfo->wParam[1];
        }
*/
        return TRUE;
    }
};

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

class CED6Battle
{
protected:
    static CUSTOM_BATTLE_INFO *m_pBattleInfo;

public:
    static CUSTOM_BATTLE_INFO* AllocBattleInfo();
    static VOID BattleEntryOutputLog();
    static ULONG ForceBeatBack();

    VOID
    FASTCALL
    Dispatch8D(
        ULONG                    Instruction8DParam1,
        ED6_AS_CRAFT_INFO       *pCraftInfo,
        ED6_MONSTER_STATUS_DATA *pMStatus
    );

    VOID Avatar(INSTRUCTION_8D *pInstruction, ED6_MONSTER_STATUS_DATA *pMStatus);
    VOID ExCondition(INSTRUCTION_8D *pInstruction, ED6_MONSTER_STATUS_DATA *pMStatus);
    VOID ReplacePosition(INSTRUCTION_8D *pInstruction, ED6_MONSTER_STATUS_DATA *pMStatus);

    bool
    CloneMonsterStatusData(
        ED6_MONSTER_STATUS_DATA *pMStatus,
        USHORT                   SkillInfoIndex,
        ED6_AI_INFO             *pCraftAI
    );

    BOOL IsAvatarLoaded(ULONG AvatarIndex);
    BOOL OldIsAvatarLoaded(ULONG AvatarIndex);

    bool LoadMonsterStatusData(ULONG MSFileIndex, ULONG CharPosition);
    VOID ResetMSData(PVOID pBattleInfo, PVOID, ULONG CharPosition);
    VOID SetAngle(PVOID pBattleInfo, PVOID, ULONG FunctionID, ULONG Param);

    VOID
    ProcessAttack(
        ED6_MONSTER_STATUS_DATA *pSelf,
        ED6_MONSTER_STATUS_DATA *pTarget
    );

    VOID
    THISCALL
    OldProcessAttack(
        ED6_MONSTER_STATUS_DATA *pSelf,
        ED6_MONSTER_STATUS_DATA *pTarget
    );

    VOID
    ProcessConditions(
        ED6_MONSTER_STATUS_DATA *pMStatus,
        ULONG                    ActionTime,
        BYTE                     Type,          // 0: -= at  1: dec  2: if == cf then dec
        ULONG                    ConditionFlag
    );

    VOID
    THISCALL
    OldProcessConditions(
        ED6_MONSTER_STATUS_DATA *pMStatus,
        ULONG                    ActionTime,
        BYTE                     Type,
        ULONG                    ConditionFlag
    );

    BOOL HasPhysicalReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget);
    BOOL HasMagicReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget);

    bool  OldHasPhysicalReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget);
    bool  OldHasMagicReflection(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget);

    ULONG GetDamage(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget, BYTE Type);
    ULONG OldGetDamage(ED6_MONSTER_STATUS_DATA *pSelf, ED6_MONSTER_STATUS_DATA *pTarget, BYTE Type);

    BOOL
    GetTargetFrontCoordinate(
        ED6_MONSTER_STATUS_DATA *pSelf,
        ED6_MONSTER_STATUS_DATA *pTarget,
        FLOAT                   *pRecvCoord OPTIONAL
    );

    VOID
    SetCondition(
        ED6_MONSTER_STATUS_DATA    *pMStatus,
        ULONG                       Unknwon,
        ULONG                       Condition,
        ULONG                       Unknwon2,
        ULONG                       Unknwon3
    );

    static
    VOID
    CDECL
    Putffect(
        CED6Effect             **pEffect,
        ED6_MONSTER_STATUS_DATA *pSelf OPTIONAL,
        ED6_MONSTER_STATUS_DATA *pTarget,
        FLOAT                   *pUnknown,      // float[3]
        ED6_MONSTER_STATUS_DATA *pSelf2 OPTIONAL,
        PULONG                   pUnknownDowrd3 OPTIONAL,   // always zero ?
        FLOAT                   *pScale,       //  float[3] 18 first 3 short
        FLOAT                   *pEffectSize,   // float[3] { CharSize, CharSize, CharSize
        ULONG                    Zero4,
        PVOID                    pvEffectBuffer,
        ULONG                    Zero5,
        ULONG                    Zero6,
        ULONG                    One1,
        ULONG                    Zero7
    );

    VOID
    PutConditionEffect(
        ED6_MONSTER_STATUS_DATA *pTarget,
        ULONG                    PrivateEffectBufferIndex,
        ULONG                    PrivateEffectInfoIndex
    );
};

typedef
bool
(CED6Battle::
*FCloneMonsterStatusData2)(
    ED6_MONSTER_STATUS_DATA *pMStatus,
    USHORT                   SkillInfoIndex,
    ED6_AI_INFO             *pCraftAI
);

typedef BOOL (CED6Battle::*FIsAvatarLoaded)(ULONG AvatarIndex);
typedef bool (CED6Battle::*FOldIsAvatarLoaded)(ULONG AvatarIndex);
typedef bool (CED6Battle::*FLoadMonsterStatusData2)(ULONG MSFileIndex, ULONG CharPosition);
typedef VOID (CED6Battle::*FResetMSData2)(ULONG CharPosition);
typedef VOID (CED6Battle::*FSetAngle2)(ULONG FunctionID, ULONG Param);

typedef
VOID
(CED6Battle::
*FProcessAttack)(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget
);

typedef
VOID
(CED6Battle::
 *FProcessConditions)(
    ED6_MONSTER_STATUS_DATA *pMStatus,
    ULONG                    ActionTime,
    BYTE                     Type,          // 0: -= at  1: dec  2: if == cf dec
    ULONG                    ConditionFlag
);

typedef
ULONG
(CED6Battle::
*FGetDamage)(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    BYTE                     Type
);

typedef
bool
(CED6Battle::
*FGetTargetFrontCoordinate)(
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    FLOAT                   *pRecvCoord OPTIONAL
);

typedef
VOID
(CDECL
*FPutEffect)(
    CED6Effect             **pEffect,
    ED6_MONSTER_STATUS_DATA *pSelf,
    ED6_MONSTER_STATUS_DATA *pTarget,
    FLOAT                   *pUnknown,
    ED6_MONSTER_STATUS_DATA *pSelf2,
    PULONG                   pUnknownDowrd3,
    FLOAT                   *pScale,
    FLOAT                   *pEffectSize,
    ULONG                    Zero4,
    PVOID                    pvEffectBuffer,
    ULONG                    Zero5,
    ULONG                    Zero6,
    ULONG                    One1,
    ULONG                    Zero7
);

typedef VOID (CDECL *FFinishEffect)(CED6Effect **pEffect);

//////////////////////////////////////////////////////////////////////////

typedef PBYTE (CDECL  *FGetMagicDescription)(ULONG dwSkillID);
typedef bool  (CDECL  *FReadFileToBuffer)(PBYTE pbBuffer, ULONG dwDatSN, ULONG dwOffset, ULONG dwDestFileSize);
typedef ULONG (CDECL  *FDecompress)(PBYTE *ppbDest, PBYTE *ppbSrc);

//typedef DWORD (CDECL  *ReadFace)(PBYTE pbBuffer, DWORD dwFaceIndex, DWORD);
//typedef VOID  (CDECL  *ShowFace)(PBYTE pbBuffer, DWORD *, DWORD, LPVOID, DWORD *);
//typedef bool  (WINAPI *FLoadStatusData)(DWORD dwMsFileIndex, BYTE byPosition);
//typedef VOID  (WINAPI *CreateTexture)(DWORD, DWORD, DWORD, DWORD, DWORD, DWORD, IDirect3DBaseTexture8 **);

typedef
bool
(FASTCALL
*FCloneMonsterStatusData)(
    PVOID                    pBattleInfo,
    PVOID,
    ED6_MONSTER_STATUS_DATA *pMStatus,
    USHORT                   SkillInfoIndex,
    ED6_AI_INFO             *pCraftAI
);

typedef
bool
(FASTCALL
*FLoadMonsterStatusData)(
    PVOID pBattleInfo,
    PVOID,
    ULONG MSFileIndex,
    ULONG CharPosition
);

typedef VOID (FASTCALL *FResetMSData)(PVOID pBattleInfo, PVOID, ULONG CharPosition);
typedef VOID (FASTCALL *FSetAngle)(PVOID pBattleInfo, PVOID, ULONG FunctionID, ULONG Param);
typedef VOID (CDECL *FShowConditionMsg)(ED6_MONSTER_STATUS_DATA *pTarget, LPCSTR pszMsg, COLORREF TextColor);

#pragma pack()

#define GET_METHOD(Method) (PVOID)GetMethodAddress(&CED6Battle::Method)

#define MAX_BUFFER_SIZE     0x1000000
#define LENGTH_OF_AI        0x18
#define LENGTH_OF_AS        0x4F10
#define LENGTH_OF_CHAR_DATA 0x2490
#define DEST_CHAR_ID        20h

#define OLD_CHIP_BUF_SIZE 0x2000000
#define NEW_CHIP_BUF_SIZE 0x3000000
#define BUF_SIZE NEW_CHIP_BUF_SIZE // HIBYTE(HIWORD(NEW_BUF_SIZE)) * 0x10


#define pwTrueCharID 0x2D754DE
#define lpszGameDirectory (LPSTR)0x2DE90A8

#define ED6_LOAD_FILE                   0x487240
#define ED6_LOAD_MONSTER_STATUS_FILE    0x41D5D0

#define PATCH_DIR_NAME L"Patch.dir"
#define PATCH_DAT_NAME L"Patch.dat"
#define CONFIG_SECTION_NAME L"Nagisa"
#define CONFIG_FILE_NAME L"TName.ini"

#define FUNC_CLONE_MS_DATA      0x429220
#define FUNC_LOAD_MS_DATA       0x41D5D0
#define FUNC_RESET_CTRL_DATA    0x41E7A0
#define FUNC_RESET_MS_DATA      0x41E960
#define FUNC_SET_ANGLE          0x418270
#define FUNC_PUT_EFFECT         0x442700
#define FUNC_FINISH_EFFECT      0x443EE0
#define FUNC_GET_DAMAGE         0x405730
#define FUNC_SHOW_CONDITIONMSG  0x43F7E0
