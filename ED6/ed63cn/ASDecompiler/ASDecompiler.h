#ifndef _ASDECOMPILER_H_
#define _ASDECOMPILER_H_

#include "pragma_once.h"
#include <afxtempl.h>
#include "my_headers.h"
#include "ASInstructions.h"

#define AS_FAILED(_Status) ((BOOL)((LONG)_Status < 0))
#define AS_SUCCESS(_Status) !AS_FAILED(_Status)
#define AS_IF_FAIL_RETURN(_Status) if (AS_FAILED(_Status)) return _Status
#define AS_IF_FAIL_BREAK(_Status) if (AS_FAILED(_Status)) break
#define AS_BREAK(_Status, __Status) { (_Status) = __Status; break; }

enum
{
    ASDECL_ERROR_SUCCESS = 0,
    ASDECL_ERROR_DUMPED,
    ASDECL_ERROR_INTERNAL_INSTRUCTION,

    ASDECL_ERROR_BASE = 0x80000000,

    ASDECL_ERROR_UNKNOWN = ASDECL_ERROR_BASE,
    ASDECL_ERROR_INVALID_FORMAT,
    ASDECL_ERROR_OUT_OF_RANGE,
    ASDECL_ERROR_NOT_IMPLEMENTED,
    ASDECL_ERROR_INVALID_PARAM_COUNT,
    ASDECL_ERROR_REFERENCE_INVALID_OFFSET,
    ASDECL_ERROR_UNKNOWN_INSTRUCTION,
    ASDECL_ERROR_OUT_OF_MEMORY,
    ASDECL_ERROR_CREATE_FILE,
    ASDECL_ERROR_WRITE_FILE,
};

typedef struct
{
    ULONG               Offset;
    ULONG               RefCount;
    ULONG               InstructionIndex;
    ED6_AS_CRAFT_INFO  *pCraftInfo;
} ED6_INSTRUCTION_RECORD;

#define DECL_HANDLER(func) LONG (func)(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)

typedef CMap<ULONG, ULONG, ED6_INSTRUCTION_RECORD, ED6_INSTRUCTION_RECORD&> DecompiledInstructionMap;
typedef CMap<ULONG, ULONG, PVOID, PVOID> InstructionMap;

struct ED6_AS_INSTRUCTION_MAP;

class CED6AsDecompiler
{
protected:
    CMem                        m_mem;
    BOOL                        m_bLastIsNewLine;
    DecompiledInstructionMap    m_DecompiledMap, m_FuntionMap;
    ED6_ACTION_SCRIPT_INFO      m_AsInfo;
    InstructionMap              m_InstructionMap;

public:
    CED6AsDecompiler();
    ~CED6AsDecompiler();

    BOOL DecompilerFile(LPWSTR pszAsFileName, LPWSTR pszOutput = NULL);
    VOID ShowError(LONG Status);
    static VOID ShowInstructionMapInfo();

protected:
    VOID  Reset(BOOL bDestroy = FALSE);
    LPSTR AllocString(LPSTR pString, ULONG Length = -1);
    BOOL  FreeString(PVOID  pString);

    LONG DecompilerFile(ED6_ACTION_SCRIPT_INFO *pAsInfo);
    LONG DecompileHeader(ED6_ACTION_SCRIPT_INFO *pAsInfo);
    LONG DecompileFunctions(ED6_ACTION_SCRIPT_INFO *pAsInfo);
    LONG DecompilerCrafts(ED6_ACTION_SCRIPT_INFO *pAsInfo);
    LONG DecompilerOneCraft(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_AS_CRAFT_INFO *pCraftInfo);
    LONG DecompileInstruction(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction);

    ED6_AS_INSTRUCTION_MAP* FindInstrctionMap(PBYTE pbBuffer, PBYTE pbEnd);
    ED6_AS_INSTRUCTION_MAP* FindInstrctionMapByCode(ULONG Code);

    LONG CreateDefinition(LPWSTR pszAsFile, LPSTR Buffer);
    LONG DumpToFile(ED6_ACTION_SCRIPT_INFO *pAsInfo, LPWSTR pszAsFile, LPWSTR pszOutput);
    LONG DumpCrafts(ED6_ACTION_SCRIPT_INFO *pAsInfo, CFileDisk &file, LPSTR Buffer);
    LONG DumpFunctions(ED6_ACTION_SCRIPT_INFO *pAsInfo, CFileDisk &file, LPSTR Buffer);

    LONG
    DumpOneCraft(
        ED6_ACTION_SCRIPT_INFO  *pAsInfo,
        ED6_AS_CRAFT_INFO       *pCraft,
        CFileDisk               &file,
        LPSTR                    Buffer
    );

    LONG
    DumpOneFunction(
        ED6_ACTION_SCRIPT_INFO  *pAsInfo,
        ED6_AS_CRAFT_INFO       *pCraft,
        CFileDisk               &file,
        LPSTR                    Buffer
    );

    LONG
    DumpInstrction(
        ED6_ACTION_SCRIPT_INFO  *pAsInfo,
        ED6_AS_CRAFT_INFO       *pCraft,
        ED6_INSTRUCTION         *pInstruction,
        CFileDisk               &file,
        LPSTR                    Buffer
    );

    LONG GetCraftName(ED6_ACTION_SCRIPT_INFO *pAsInfo, ULONG CraftIndex, LPSTR Buffer);
    LONG GetLabelName(ED6_ACTION_SCRIPT_INFO *pAsInfo, USHORT Offset, LPSTR Buffer);
    BOOL IsLabelNextInstruction(ED6_INSTRUCTION *pInstruction, ULONG Offset);

    LONG WriteText(CFileDisk &file, LPSTR Buffer, LPCSTR pszFormat, ...);

    ED6_INSTRUCTION* UnlinkInstruction(ED6_INSTRUCTION *pInstruction);

    LONG AddInstrction(ED6_AS_CRAFT_INFO *pCraftInfo, ED6_INSTRUCTION *pInstrction);

    BOOL
    AddFunction(
        ULONG               Offset,
        ULONG               RefCount            = 1,
        ULONG               InstructionIndex    = 0,
        ED6_AS_CRAFT_INFO  *pCraftInfo          = NULL
    );

    BOOL FindDecompiled(ULONG Offset, ED6_INSTRUCTION_RECORD &Decompiled);
    BOOL AddDecompiled(ED6_INSTRUCTION_RECORD &Compiled);
    BOOL FindFunction(ULONG Offset, ED6_INSTRUCTION_RECORD &Function);
    BOOL AddFunction(ED6_INSTRUCTION_RECORD &Function);

    BOOL AddMapWorder(DecompiledInstructionMap &Map, ED6_INSTRUCTION_RECORD &Instruction);
    BOOL FindMapWorder(DecompiledInstructionMap &Map, ULONG Offset, ED6_INSTRUCTION_RECORD &Instruction);

    LONG HandleNoParam(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction);

    LONG
    HandleFixedLengthParam(
        ED6_ACTION_SCRIPT_INFO  *pAsInfo,
        ED6_INSTRUCTION         *pInstruction,
        ULONG                    ParamCount,
        ULONG                    ParamLength,
        PULONG                   pParamFlags = NULL
    );

    LONG
    HandleDynamicLengthParam(
        ED6_ACTION_SCRIPT_INFO  *pAsInfo,
        ED6_INSTRUCTION         *pInstruction,
        ULONG                    ParamCount,
        PULONG                   pParamLength,
        PULONG                   pParamFlags = NULL
    );

public:
    DECL_HANDLER(Handle00);
    DECL_HANDLER(Handle01);
    DECL_HANDLER(Handle02);
    DECL_HANDLER(Handle03);
    DECL_HANDLER(Handle04);
    DECL_HANDLER(Handle05);
    DECL_HANDLER(Handle06);
    DECL_HANDLER(Handle07);
    DECL_HANDLER(Handle08);
    DECL_HANDLER(Handle09);
    DECL_HANDLER(Handle0A);
    DECL_HANDLER(Handle0B);
    DECL_HANDLER(Handle0C);
    DECL_HANDLER(Handle0D);
    DECL_HANDLER(Handle0E);
    DECL_HANDLER(Handle0F);
    DECL_HANDLER(Handle10);
    DECL_HANDLER(Handle11);
    DECL_HANDLER(Handle12);
    DECL_HANDLER(Handle13);
    DECL_HANDLER(Handle14);
    DECL_HANDLER(Handle15);
    DECL_HANDLER(Handle16);
    DECL_HANDLER(Handle17);
    DECL_HANDLER(Handle18);
    DECL_HANDLER(Handle19);
    DECL_HANDLER(Handle1A);
    DECL_HANDLER(Handle1B);
    DECL_HANDLER(Handle1C);
    DECL_HANDLER(Handle1D);
    DECL_HANDLER(Handle1E);
    DECL_HANDLER(Handle1F);
    DECL_HANDLER(Handle20);
    DECL_HANDLER(Handle21);
    DECL_HANDLER(Handle22);
    DECL_HANDLER(Handle23);
    DECL_HANDLER(Handle24);
    DECL_HANDLER(Handle25);
    DECL_HANDLER(Handle26);
    DECL_HANDLER(Handle27);
    DECL_HANDLER(Handle28);
    DECL_HANDLER(Handle29);
    DECL_HANDLER(Handle2A);
    DECL_HANDLER(Handle2B);
    DECL_HANDLER(Handle2C);
    DECL_HANDLER(Handle2D);
    DECL_HANDLER(Handle2E);
    DECL_HANDLER(Handle2F);
    DECL_HANDLER(Handle30);
    DECL_HANDLER(Handle31);
    DECL_HANDLER(Handle32);
    DECL_HANDLER(Handle33);
    DECL_HANDLER(Handle34);
    DECL_HANDLER(Handle35);
    DECL_HANDLER(Handle36);
    DECL_HANDLER(Handle37);
    DECL_HANDLER(Handle38);
    DECL_HANDLER(Handle39);
    DECL_HANDLER(Handle3A);
    DECL_HANDLER(Handle3B);
    DECL_HANDLER(Handle3C);
    DECL_HANDLER(Handle3D);
    DECL_HANDLER(Handle3E);
    DECL_HANDLER(Handle3F);
    DECL_HANDLER(Handle40);
    DECL_HANDLER(Handle41);
    DECL_HANDLER(Handle42);
    DECL_HANDLER(Handle43);
    DECL_HANDLER(Handle44);
    DECL_HANDLER(Handle45);
    DECL_HANDLER(Handle46);
    DECL_HANDLER(Handle47);
    DECL_HANDLER(Handle48);
    DECL_HANDLER(Handle49);
    DECL_HANDLER(Handle4A);
    DECL_HANDLER(Handle4B);
    DECL_HANDLER(Handle4C);
    DECL_HANDLER(Handle4D);
    DECL_HANDLER(Handle4E);
    DECL_HANDLER(Handle4F);
    DECL_HANDLER(Handle50);
    DECL_HANDLER(Handle51);
    DECL_HANDLER(Handle52);
    DECL_HANDLER(Handle53);
    DECL_HANDLER(Handle54);
    DECL_HANDLER(Handle55);
    DECL_HANDLER(Handle56);
    DECL_HANDLER(Handle57);
    DECL_HANDLER(Handle58);
    DECL_HANDLER(Handle59);
    DECL_HANDLER(Handle5A);
    DECL_HANDLER(Handle5B);
    DECL_HANDLER(Handle5C);
    DECL_HANDLER(Handle5D);
    DECL_HANDLER(Handle5E);
    DECL_HANDLER(Handle5F);
    DECL_HANDLER(Handle60);
    DECL_HANDLER(Handle61);
    DECL_HANDLER(Handle62);
    DECL_HANDLER(Handle63);
    DECL_HANDLER(Handle64);
    DECL_HANDLER(Handle65);
    DECL_HANDLER(Handle66);
    DECL_HANDLER(Handle67);
    DECL_HANDLER(Handle68);
    DECL_HANDLER(Handle69);
    DECL_HANDLER(Handle6A);
    DECL_HANDLER(Handle6B);
    DECL_HANDLER(Handle6C);
    DECL_HANDLER(Handle6D);
    DECL_HANDLER(Handle6E);
    DECL_HANDLER(Handle6F);
    DECL_HANDLER(Handle70);
    DECL_HANDLER(Handle71);
    DECL_HANDLER(Handle72);
    DECL_HANDLER(Handle73);
    DECL_HANDLER(Handle74);
    DECL_HANDLER(Handle75);
    DECL_HANDLER(Handle76);
    DECL_HANDLER(Handle77);
    DECL_HANDLER(Handle78);
    DECL_HANDLER(Handle79);
    DECL_HANDLER(Handle7A);
    DECL_HANDLER(Handle7B);
    DECL_HANDLER(Handle7C);
    DECL_HANDLER(Handle7D);
    DECL_HANDLER(Handle7E);
    DECL_HANDLER(Handle7F);
    DECL_HANDLER(Handle80);
    DECL_HANDLER(Handle81);
    DECL_HANDLER(Handle82);
    DECL_HANDLER(Handle83);
    DECL_HANDLER(Handle84);
    DECL_HANDLER(Handle85);
    DECL_HANDLER(Handle86);
    DECL_HANDLER(Handle87);
    DECL_HANDLER(Handle88);
    DECL_HANDLER(Handle89);
    DECL_HANDLER(Handle8A);
    DECL_HANDLER(Handle8B);
    DECL_HANDLER(Handle8C);
    DECL_HANDLER(Handle8D);
    DECL_HANDLER(Handle8E);
    DECL_HANDLER(Handle8F);
    DECL_HANDLER(Handle90);
    DECL_HANDLER(Handle91);
    DECL_HANDLER(Handle92);
    DECL_HANDLER(Handle93);
    DECL_HANDLER(Handle94);
    DECL_HANDLER(Handle95);
    DECL_HANDLER(Handle96);
    DECL_HANDLER(Handle97);
    DECL_HANDLER(Handle98);
    DECL_HANDLER(Handle99);
    DECL_HANDLER(Handle9A);
    DECL_HANDLER(Handle9B);
    DECL_HANDLER(Handle9C);
    DECL_HANDLER(Handle9D);
    DECL_HANDLER(Handle9E);
    DECL_HANDLER(Handle9F);
    DECL_HANDLER(HandleA0);
    DECL_HANDLER(HandleA1);
    DECL_HANDLER(HandleA2);
    DECL_HANDLER(HandleA3);
    DECL_HANDLER(HandleA4);
    DECL_HANDLER(HandleA5);
    DECL_HANDLER(HandleA6);
    DECL_HANDLER(HandleA7);
    DECL_HANDLER(HandleA8);
    DECL_HANDLER(HandleA9);
    DECL_HANDLER(HandleAA);
    DECL_HANDLER(HandleAB);
    DECL_HANDLER(HandleAC);
    DECL_HANDLER(HandleAD);
    DECL_HANDLER(HandleAE);
    DECL_HANDLER(HandleAF);
    DECL_HANDLER(HandleB0);
    DECL_HANDLER(HandleB1);
};

#define LABEL_CRAFT_OFFSET_TABLE        "CraftOffsetTable"
#define LABEL_CRAFT_OFFSET_TABLE_END    "CraftOffsetTableEnd"

#define NAME_HEADER_UNKNOWN             "UnknownFlag_0x04"

#define NAME_DEFAULT_EXTENSION          ".asm"
#define NAME_DEFINITION_FILE            "as_def.txt"
#define NAME_CRAFT_LABEL_PREFIX         "loc_"
#define NAME_DEFAULT_INSTRUCTION_PREFIX "OP_"

#define NAME_NOP_CRAFT                  "NopCraft"
#define NAME_INTRINSIC_CRAFT1           "SysCraft_MagicEffect"
#define NAME_INTRINSIC_CRAFT2           "SysCraft_Stand"
#define NAME_INTRINSIC_CRAFT3           "SysCraft_Move"
#define NAME_INTRINSIC_CRAFT4           "SysCraft_UnderAttack"
#define NAME_INTRINSIC_CRAFT5           "SysCraft_Dead"
#define NAME_INTRINSIC_CRAFT6           "SysCraft_NormalAttack"
#define NAME_INTRINSIC_CRAFT7           "SysCraft_MagicChant"
#define NAME_INTRINSIC_CRAFT8           "SysCraft_MagicCast"
#define NAME_INTRINSIC_CRAFT9           "SysCraft_Win"
#define NAME_INTRINSIC_CRAFT10          "SysCraft_Unknown"
#define NAME_INTRINSIC_CRAFT11          "SysCraft_UseItem"
#define NAME_INTRINSIC_CRAFT12          "SysCraft_Stun"
#define NAME_INTRINSIC_CRAFT13          "SysCraft_Unknown2"
#define INTRINSIC_CRAFT_COUNT  (13L)

#endif // _ASDECOMPILER_H_
