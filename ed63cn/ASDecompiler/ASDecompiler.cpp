//#pragma comment(linker, "/NODEFAULTLIB:msvcrt")
//#pragma comment(lib, "libcmt.lib")

#include "ASDecompiler.h"
#include "ASInstructions.h"
#include "DefInfo.h"

#define __WSTRING(str) L##str
#define WSTRING(str) __WSTRING(str)

OVERLOAD_CPP_NEW_WITH_HEAP(CMem::GetGlobalHeap())

CED6AsDecompiler::CED6AsDecompiler()
{
    ZeroMemory(&m_AsInfo, sizeof(m_AsInfo));
//    Reset();
}

CED6AsDecompiler::~CED6AsDecompiler()
{
    Reset(TRUE);
}

VOID CED6AsDecompiler::ShowInstructionMapInfo()
{
    ULONG UnknownCount;
    ED6_AS_INSTRUCTION_MAP *pMap;

    printf("Total:   %X(%u)\n", countof(g_InstructionMap), countof(g_InstructionMap));

    UnknownCount = 0;
    pMap = g_InstructionMap;
    for (ULONG Count = countof(g_InstructionMap); Count; ++pMap, --Count)
        UnknownCount += pMap->pszName == NULL;

    printf(
        "Known:   %X(%u)\n"
        "Unknown: %X(%u)\n",
        countof(g_InstructionMap) - UnknownCount, countof(g_InstructionMap) - UnknownCount,
        UnknownCount, UnknownCount);
}

VOID CED6AsDecompiler::Reset(BOOL bDestroy /* = FALSE */)
{
    m_bLastIsNewLine = FALSE;

    m_mem.Free(m_AsInfo.pbAsBuffer);
    m_mem.Free(m_AsInfo.pFunctionTable);

    if (m_AsInfo.pCraftInfo != NULL)
    {
        ED6_AS_CRAFT_INFO *pCraftInfo = m_AsInfo.pCraftInfo;
        for (ULONG i = m_AsInfo.CraftCount; i; ++pCraftInfo, --i)
        {
            ED6_INSTRUCTION *pInstruction = pCraftInfo->pInstruction;
            for (ULONG j = pCraftInfo->Count; j; ++pInstruction, --j)
            {
                for (ULONG k = 0; k != pInstruction->ParamNumber; ++k)
                {
                    if (pInstruction->Param[k].Length == INSTRUCTION_LENGTH_STRING)
                        FreeString((PVOID)pInstruction->Param[k].Value.LowPart);
                }
            }

            m_mem.Free(pCraftInfo->pInstruction);
        }

        m_mem.Free(m_AsInfo.pCraftInfo);
    }

    if (m_AsInfo.pFunctionInfo != NULL)
    {
        ED6_AS_CRAFT_INFO *pCraftInfo = m_AsInfo.pFunctionInfo;
        for (ULONG i = m_AsInfo.FunctionCount; i; ++pCraftInfo, --i)
        {
            ED6_INSTRUCTION *pInstruction = pCraftInfo->pInstruction;
            for (ULONG j = pCraftInfo->Count; j; ++pInstruction, --j)
            {
                for (ULONG k = 0; k != pInstruction->ParamNumber; ++k)
                {
                    if (pInstruction->Param[k].Length == INSTRUCTION_LENGTH_STRING)
                        FreeString((PVOID)pInstruction->Param[k].Value.LowPart);
                }
            }

            m_mem.Free(pCraftInfo->pInstruction);
        }

        m_mem.Free(m_AsInfo.pFunctionInfo);
    }

    ZeroMemory(&m_AsInfo, sizeof(m_AsInfo));
    m_DecompiledMap.RemoveAll();
    m_DecompiledMap.InitHashTable(0x511);
    m_FuntionMap.RemoveAll();
    m_FuntionMap.InitHashTable(0x511);
    m_InstructionMap.RemoveAll();
    m_InstructionMap.InitHashTable(countof(g_InstructionMap) * 6 / 5);

    ED6_AS_INSTRUCTION_MAP *pMap = g_InstructionMap;
    for (ULONG Count = countof(g_InstructionMap); Count; ++pMap, --Count)
    {
        PVOID p;
        if (m_InstructionMap.Lookup(pMap->Instruction, p))
        {
            printf("%02X: Instruction redefined\n", pMap->Instruction);
        }
        m_InstructionMap[pMap->Instruction] = pMap;
    }

    UNREFERENCED_PARAMETER(bDestroy);
}

VOID CED6AsDecompiler::ShowError(LONG Status)
{
    if (m_AsInfo.pbAsBuffer == NULL)
        return;

    printf("%08X: occur error at %08X @ %02X\n", Status, m_AsInfo.pbCurrent - m_AsInfo.pbAsBuffer, *m_AsInfo.pbCurrent);
}

LPSTR CED6AsDecompiler::AllocString(LPSTR pString, ULONG Length /* = -1 */)
{
    LPSTR pszBuffer, p;
    ULONG BaseLength, BackSlashCount;

    BackSlashCount = 0;
    pszBuffer  = pString;
    for (ULONG Len = Length; Len; ++pszBuffer, --Len)
    {
        if (*pszBuffer == 0)
            break;

        if (*pszBuffer < 0)
        {
            if (*++pszBuffer == 0)
                break;
            continue;
        }

        if (*pszBuffer == '\\')
            ++BackSlashCount;
    }

    BaseLength = pszBuffer - pString + BackSlashCount;

    pszBuffer = (LPSTR)m_mem.Alloc(BaseLength + 2);
    if (pszBuffer == NULL)
        return pszBuffer;

    for (p = pszBuffer; Length; --Length)
    {
        CHAR c = *pString++;

        *p++ = c;
        if (c == 0)
            break;

        if (c < 0)
        {
            c = *pString++;
            *p++ = c;
            if (c == 0)
                break;
        }

        else if (c == '\\')
        {
            *p++ = c;
        }
    }

    *p = 0;

    return pszBuffer;
}

BOOL CED6AsDecompiler::FreeString(PVOID pString)
{
    return pString == NULL ? FALSE : m_mem.Free(pString);
}

BOOL
CED6AsDecompiler::
AddFunction(
    ULONG               Offset,
    ULONG               RefCount            /* = 1 */,
    ULONG               InstructionIndex    /* = 0 */,
    ED6_AS_CRAFT_INFO  *pCraftInfo          /* = NULL */
)
{
    ED6_INSTRUCTION_RECORD Function = { Offset, RefCount, InstructionIndex, pCraftInfo };
    return AddFunction(Function);
}

LONG CED6AsDecompiler::AddInstrction(ED6_AS_CRAFT_INFO *pCraftInfo, ED6_INSTRUCTION *pInstrction)
{
    ED6_INSTRUCTION_RECORD Reference;

    if (pCraftInfo->pInstruction == NULL)
    {
        pCraftInfo->Count = 0;
        pCraftInfo->MaxCount = 10;
        pCraftInfo->pInstruction = (ED6_INSTRUCTION *)m_mem.Alloc(pCraftInfo->MaxCount * sizeof(*pCraftInfo->pInstruction));
        if (pCraftInfo->pInstruction == NULL)
            return ASDECL_ERROR_OUT_OF_MEMORY;
    }
    else if (pCraftInfo->Count == pCraftInfo->MaxCount)
    {
        pCraftInfo->MaxCount *= 2;
        pCraftInfo->pInstruction = (ED6_INSTRUCTION * )m_mem.ReAlloc(pCraftInfo->pInstruction, pCraftInfo->MaxCount * sizeof(*pCraftInfo->pInstruction));
        if (pCraftInfo->pInstruction == NULL)
            return ASDECL_ERROR_OUT_OF_MEMORY;
    }

    if (FindFunction(pInstrction->Offset, Reference))
        pInstrction->Flags |= INSTRUCTION_FLAG_LABEL;

    pCraftInfo->pInstruction[pCraftInfo->Count++] = *pInstrction;

    return ASDECL_ERROR_SUCCESS;
}

BOOL CED6AsDecompiler::FindDecompiled(ULONG Offset, ED6_INSTRUCTION_RECORD &Decompiled)
{
    return FindMapWorder(m_DecompiledMap, Offset, Decompiled);
}

BOOL CED6AsDecompiler::AddDecompiled(ED6_INSTRUCTION_RECORD &Compiled)
{
    return AddMapWorder(m_DecompiledMap, Compiled);
}

BOOL CED6AsDecompiler::FindFunction(ULONG Offset, ED6_INSTRUCTION_RECORD &Function)
{
    return FindMapWorder(m_FuntionMap, Offset, Function);
}

BOOL CED6AsDecompiler::AddFunction(ED6_INSTRUCTION_RECORD &Function)
{
    return AddMapWorder(m_FuntionMap, Function);
}

BOOL CED6AsDecompiler::AddMapWorder(DecompiledInstructionMap &Map, ED6_INSTRUCTION_RECORD &Instruction)
{
    ED6_INSTRUCTION_RECORD Ins;

    if (Map.Lookup(Instruction.Offset, Ins))
    {
        ++Ins.RefCount;
        Map[Ins.Offset] = Ins;
        return TRUE;
    }

    Map[Instruction.Offset] = Instruction;
    return TRUE;
}

BOOL
CED6AsDecompiler::
FindMapWorder(
    DecompiledInstructionMap   &Map,
    ULONG                       Offset,
    ED6_INSTRUCTION_RECORD     &Instruction
)
{
    return Map.Lookup(Offset, Instruction);
}

BOOL CED6AsDecompiler::DecompilerFile(LPWSTR pszAsFileName, LPWSTR pszOutput /* = NULL */)
{
    LONG Status;
    WCHAR szOutput[MAX_PATH];
    CFileDisk file;

    Reset();

    if (!file.Open(pszAsFileName))
        return FALSE;

    m_AsInfo.BufferSize = file.GetSize();
    m_AsInfo.pbAsBuffer = (PBYTE)m_mem.Alloc(m_AsInfo.BufferSize);
    if (m_AsInfo.pbAsBuffer == NULL)
        return FALSE;

    if (!file.Read(m_AsInfo.pbAsBuffer))
        return FALSE;

    Status = DecompilerFile(&m_AsInfo);
    if (Status != ASDECL_ERROR_UNKNOWN_INSTRUCTION)
        AS_IF_FAIL_RETURN(Status);

    if (pszOutput == NULL)
    {
        LPWSTR pszExtension;

        pszExtension = findextw(pszAsFileName);
        if (!StrICompareW(pszExtension, WSTRING(NAME_DEFAULT_EXTENSION)))
            pszExtension += countof(WSTRING(NAME_DEFAULT_EXTENSION)) - 1;

        lstrcpyW(szOutput, pszAsFileName);
        pszExtension = szOutput + (pszExtension - pszAsFileName);
        lstrcpyW(pszExtension, WSTRING(NAME_DEFAULT_EXTENSION));
        pszOutput = szOutput;
    }

    Status = DumpToFile(&m_AsInfo, pszAsFileName, pszOutput);

    return Status;
}

LONG CED6AsDecompiler::DecompilerFile(ED6_ACTION_SCRIPT_INFO *pAsInfo)
{
    LONG Status;
    PEXCEPTION_POINTERS pException = NULL;

    SEH_TRY
    {
        Status = DecompileHeader(pAsInfo);
        AS_IF_FAIL_RETURN(Status);
        Status = DecompilerCrafts(pAsInfo);
        if (Status != ASDECL_ERROR_UNKNOWN_INSTRUCTION)
            AS_IF_FAIL_RETURN(Status);
        Status = DecompileFunctions(pAsInfo);
        if (Status != ASDECL_ERROR_UNKNOWN_INSTRUCTION)
            AS_IF_FAIL_RETURN(Status);
    }
    SEH_EXCEPT(pException = GetExceptionInformation(), EXCEPTION_EXECUTE_HANDLER)
    {
        switch (pException->ExceptionRecord->ExceptionCode)
        {
            case EXCEPTION_ACCESS_VIOLATION:
                Status = ASDECL_ERROR_INVALID_FORMAT;
                break;

            default:
                Status = ASDECL_ERROR_UNKNOWN;
                break;
        }
    }

    return Status;
}

LONG CED6AsDecompiler::DecompileHeader(ED6_ACTION_SCRIPT_INFO *pAsInfo)
{
    PBYTE pbBuffer;

    pbBuffer = pAsInfo->pbAsBuffer;
    pAsInfo->CraftOffsetTableOffset = *(PUSHORT)pbBuffer;
    pAsInfo->CraftOffsetTableEndOffset = *((PUSHORT)pbBuffer + 1);
    pAsInfo->Unknown = *((PUSHORT)pbBuffer + 2);
    pAsInfo->CraftCount = pAsInfo->CraftOffsetTableEndOffset - pAsInfo->CraftOffsetTableOffset;
    pAsInfo->CraftCount /= sizeof(((CRAFT_OFFSET_TABLE_BASE *)0)->MagicEffect);
    if (pAsInfo->CraftCount < INTRINSIC_CRAFT_COUNT)
        return ASDECL_ERROR_INVALID_FORMAT;

    pAsInfo->pCraftInfo = (ED6_AS_CRAFT_INFO *)m_mem.Alloc(pAsInfo->CraftCount * sizeof(*pAsInfo->pCraftInfo), HEAP_ZERO_MEMORY);
    if (pAsInfo->pCraftInfo == NULL)
        return ASDECL_ERROR_OUT_OF_MEMORY;

    pAsInfo->pCraftOffsetTable = (CRAFT_OFFSET_TABLE_BASE *)(pbBuffer + pAsInfo->CraftOffsetTableOffset);
    for (ULONG Count = 0; Count != pAsInfo->CraftCount; ++Count)
    {
        ED6_AS_CRAFT_INFO *pCraftInfo = &pAsInfo->pCraftInfo[Count];

        pCraftInfo->Count        = 0;
        pCraftInfo->MaxCount     = 0;
        pCraftInfo->pInstruction = NULL;
        pCraftInfo->Offset       = ((PUSHORT)pAsInfo->pCraftOffsetTable)[Count];
    }

    pAsInfo->ChrChipPtnCount = 0;
    pAsInfo->pChrChipPtnInfo = (CHAR_CHIP_PATTERN_INFO *)(pbBuffer + 6);
    for (CHAR_CHIP_PATTERN_INFO *pChrPtn = pAsInfo->pChrChipPtnInfo; pChrPtn->CHIndex != (USHORT)-1; ++pChrPtn)
        ++pAsInfo->ChrChipPtnCount;

    pAsInfo->pszXFileName = (LPSTR)(pAsInfo->pChrChipPtnInfo + pAsInfo->ChrChipPtnCount) + 4;

    return ASDECL_ERROR_SUCCESS;
}

LONG CED6AsDecompiler::DecompilerCrafts(ED6_ACTION_SCRIPT_INFO *pAsInfo)
{
    LONG Status;
    ED6_AS_CRAFT_INFO *pCraftInfo;

    pCraftInfo = pAsInfo->pCraftInfo;
    for (ULONG Count = pAsInfo->CraftCount; Count; --Count)
    {
        if (pCraftInfo->Offset == ED6_INVALID_OFFSET)
            continue;

        Status = DecompilerOneCraft(pAsInfo, pCraftInfo);
        if (Status != ASDECL_ERROR_OUT_OF_RANGE)
            AS_IF_FAIL_BREAK(Status);
        ++pCraftInfo;
    }

    return Status;
}

BOOL IsIncluded(ED6_AS_CRAFT_INFO *pCraft, ULONG Count, ULONG Offset)
{
    for (; Count; ++pCraft, --Count)
        if (pCraft->Offset == Offset)
            return TRUE;

    return FALSE;
}

LONG CED6AsDecompiler::DecompileFunctions(ED6_ACTION_SCRIPT_INFO *pAsInfo)
{
    LONG        Status;
    ULONG       FunctionCount;
    POSITION    Pos;
    ED6_AS_CRAFT_INFO *pFunction;

    pAsInfo->FunctionCount = m_FuntionMap.GetCount();
    if (pAsInfo->FunctionCount == 0)
        return ASDECL_ERROR_SUCCESS;

    pFunction = (ED6_AS_CRAFT_INFO *)m_mem.Alloc(pAsInfo->FunctionCount * sizeof(*pFunction), HEAP_ZERO_MEMORY);
    if (pFunction == NULL)
        return ASDECL_ERROR_OUT_OF_MEMORY;

    pAsInfo->pFunctionInfo = pFunction;
    Pos = m_FuntionMap.GetStartPosition();
    do
    {
        ULONG Offset;
        ED6_INSTRUCTION_RECORD Function;

        m_FuntionMap.GetNextAssoc(Pos, Offset, Function);
        pFunction->Offset = Offset;
        ++pFunction;
    } while (Pos != NULL);

    pFunction = pAsInfo->pFunctionInfo;
    FunctionCount = pAsInfo->FunctionCount;
    LOOP_ALWAYS
    {
        for (ULONG Count = FunctionCount; Count; --Count)
        {
            Status = DecompilerOneCraft(pAsInfo, pFunction);
            if (Status != ASDECL_ERROR_UNKNOWN_INSTRUCTION)
                AS_IF_FAIL_RETURN(Status);
            ++pFunction;
        }

        FunctionCount = m_FuntionMap.GetCount();
        if (pAsInfo->FunctionCount == FunctionCount)
            break;

        pFunction = (ED6_AS_CRAFT_INFO *)m_mem.ReAlloc(pAsInfo->pFunctionInfo, FunctionCount * sizeof(*pFunction), HEAP_ZERO_MEMORY);
        if (pFunction == NULL)
            return ASDECL_ERROR_OUT_OF_MEMORY;

        pAsInfo->pFunctionInfo = pFunction;

        pFunction += pAsInfo->FunctionCount;
        Pos = m_FuntionMap.GetStartPosition();
        do
        {
            ULONG Offset;
            ED6_INSTRUCTION_RECORD Function;

            m_FuntionMap.GetNextAssoc(Pos, Offset, Function);
            if (IsIncluded(pAsInfo->pFunctionInfo, pAsInfo->FunctionCount, Offset))
                continue;

            pFunction->Offset = Offset;
            ++pFunction;

        } while (Pos != NULL);

        pFunction = pAsInfo->pFunctionInfo + pAsInfo->FunctionCount;

        Swap(FunctionCount, pAsInfo->FunctionCount);
        FunctionCount = pAsInfo->FunctionCount - FunctionCount;
    }

    ED6_AS_CRAFT_INFO **pTable;

    pTable = (ED6_AS_CRAFT_INFO **)m_mem.Alloc(pAsInfo->FunctionCount * sizeof(*pTable));
    if (pTable == NULL)
        return ASDECL_ERROR_OUT_OF_MEMORY;

    pAsInfo->pFunctionTable = pTable;
    pFunction = pAsInfo->pFunctionInfo;
    for (ULONG Count = pAsInfo->FunctionCount; Count; --Count)
        *pTable++ = pFunction++;

    pTable = pAsInfo->pFunctionTable;
    for (ULONG i = pAsInfo->FunctionCount; i; --i)
    {
        for (ULONG j = 0; j != i - 1; ++j)
        {
            if (pTable[j]->Offset > pTable[j + 1]->Offset)
                Swap(pTable[j], pTable[j + 1]);
        }
    }

    return Status;
}

LONG CED6AsDecompiler::DecompilerOneCraft(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_AS_CRAFT_INFO *pCraftInfo)
{
    LONG Status;
    ED6_INSTRUCTION Instruction;
    ED6_INSTRUCTION_RECORD Decompiled;

    pAsInfo->pbCurrent = pAsInfo->pbAsBuffer + pCraftInfo->Offset;
    if (pAsInfo->pbCurrent >= pAsInfo->pbAsBuffer + pAsInfo->BufferSize)
        return ASDECL_ERROR_OUT_OF_RANGE;

    LOOP_ALWAYS
    {
        if (FindDecompiled(pAsInfo->pbCurrent - pAsInfo->pbAsBuffer, Decompiled))
        {
            ZeroMemory(&Instruction, sizeof(Instruction));
            Instruction.Code = AS_INTERNAL_GOTO;
            Instruction.Offset = Decompiled.Offset;
            Instruction.Flags |= INSTRUCTION_FLAG_LINK;
            AddInstrction(pCraftInfo, &Instruction);
            return ASDECL_ERROR_SUCCESS;
        }

        Status = DecompileInstruction(pAsInfo, &Instruction);
        AS_IF_FAIL_BREAK(Status);

        Status = AddInstrction(pCraftInfo, &Instruction);
        AS_IF_FAIL_BREAK(Status);

        Decompiled.RefCount = 0;
        Decompiled.pCraftInfo = pCraftInfo;
        Decompiled.Offset = Instruction.Offset;
        Decompiled.InstructionIndex = pCraftInfo->Count - 1;
        AddDecompiled(Decompiled);

        if (Instruction.Code == AS_END ||
            Instruction.Code == AS_RET)
            break;
    }

    return Status;
}

LONG
CED6AsDecompiler::
DecompileInstruction(
    ED6_ACTION_SCRIPT_INFO  *pAsInfo,
    ED6_INSTRUCTION         *pInstruction
)
{
    LONG Status;
    PBYTE pbCurrent, pbEnd;
    ED6_AS_INSTRUCTION_MAP *pInsMap;

    ZeroMemory(pInstruction, sizeof(*pInstruction));

    pbCurrent = pAsInfo->pbCurrent;
    pbEnd     = pAsInfo->pbAsBuffer + pAsInfo->BufferSize;

//    printf("%08X: %02X\n", pbCurrent - pAsInfo->pbAsBuffer, *pbCurrent);
    pInsMap = FindInstrctionMap(pbCurrent, pbEnd);
    if (pInsMap == NULL)
        return ASDECL_ERROR_UNKNOWN_INSTRUCTION;
    if (pInsMap->Handler == NULL)
        return ASDECL_ERROR_SUCCESS;

    pInstruction->Offset = pAsInfo->pbCurrent - pAsInfo->pbAsBuffer;
    Status = (this->*pInsMap->Handler)(pAsInfo, pInstruction);

    return Status;
}

ED6_AS_INSTRUCTION_MAP* CED6AsDecompiler::FindInstrctionMap(PBYTE pbBuffer, PBYTE pbEnd)
{
    UNREFERENCED_PARAMETER(pbEnd);
    return FindInstrctionMapByCode(*pbBuffer);
}

ED6_AS_INSTRUCTION_MAP* CED6AsDecompiler::FindInstrctionMapByCode(ULONG Code)
{
    PVOID pMap;
    return m_InstructionMap.Lookup(Code, pMap) ? (ED6_AS_INSTRUCTION_MAP *)pMap : NULL;
}

LONG
CED6AsDecompiler::
WriteText(
    CFileDisk  &file,
    LPSTR       Buffer,
    LPCSTR      Format,
    ...
)
{
    LONG    Length;
    va_list args;
    CHAR    Buffer[0x400];

    if (m_bLastIsNewLine)
    {
        if (Format == (LPCSTR)"\n")
            return ASDECL_ERROR_SUCCESS;
        else
            m_bLastIsNewLine = FALSE;
    }
    else if (Format == (LPCSTR)"\n")
    {
        m_bLastIsNewLine = TRUE;
    }

    UNREFERENCED_PARAMETER(Buffer);
    va_start(args, Format);

    Length = vsprintf(
                Buffer,
                Format,
                args);

    if (Length == -1)
        return ASDECL_ERROR_WRITE_FILE;

    return file.Write(Buffer, Length) ? ASDECL_ERROR_SUCCESS : ASDECL_ERROR_WRITE_FILE;
}

#define WriteScr(...) { Status = WriteText(file, Buffer, __VA_ARGS__); AS_IF_FAIL_RETURN(Status); }

ED6_INSTRUCTION* CED6AsDecompiler::UnlinkInstruction(ED6_INSTRUCTION *pInstruction)
{
    ED6_INSTRUCTION_RECORD Refer;

    if (pInstruction == NULL)
        return pInstruction;

    while (TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_LINK))
    {
        if (!FindDecompiled(pInstruction->Offset, Refer))
            break;
        pInstruction = &Refer.pCraftInfo->pInstruction[Refer.InstructionIndex];
    }

    return pInstruction;
}

LONG CED6AsDecompiler::GetCraftName(ED6_ACTION_SCRIPT_INFO *pAsInfo, ULONG CraftIndex, LPSTR Buffer)
{
    LONG Length;

    UNREFERENCED_PARAMETER(pAsInfo);

    if (CraftIndex < countof(g_szIntrinsicCraft))
    {
        Length = sprintf(Buffer, "%s", g_szIntrinsicCraft[CraftIndex]);
    }
    else
    {
        Length = sprintf(Buffer, "Craft_%02X", CraftIndex);
    }

    return Length;
}

LONG CED6AsDecompiler::GetLabelName(ED6_ACTION_SCRIPT_INFO *pAsInfo, USHORT Offset, LPSTR Buffer)
{
    ED6_AS_CRAFT_INFO *pCraft = pAsInfo->pCraftInfo;

    for (ULONG Count = pAsInfo->CraftCount; Count; ++pCraft, --Count)
    {
        if (pCraft->Offset != Offset)
            continue;

        return GetCraftName(pAsInfo, pCraft - pAsInfo->pCraftInfo, Buffer);
    }

    return sprintf(Buffer, "%s%04X", NAME_CRAFT_LABEL_PREFIX, Offset);
}

LONG CED6AsDecompiler::DumpCrafts(ED6_ACTION_SCRIPT_INFO *pAsInfo, CFileDisk &file, LPSTR Buffer)
{
    LONG Status;
    PULONG pCraftIndex;
    ED6_AS_CRAFT_INFO *pCraft;

    pCraftIndex = (PULONG)AllocStack(pAsInfo->CraftCount * sizeof(*pCraft));
    for (ULONG Index = 0, Count = pAsInfo->CraftCount; Count; --Count)
    {
        pCraftIndex[Index] = Index;
        ++Index;
    }

    for (ULONG i = pAsInfo->CraftCount; i; --i)
    {
        for (ULONG j = 0; j != i - 1; ++j)
        {
            if (pAsInfo->pCraftInfo[pCraftIndex[j]].Offset > pAsInfo->pCraftInfo[pCraftIndex[j + 1]].Offset)
                Swap(pCraftIndex[j], pCraftIndex[j + 1]);
        }
    }

    pCraft = pAsInfo->pCraftInfo;
    for (ULONG Count = pAsInfo->CraftCount; Count; --Count)
    {
        Status = DumpOneCraft(pAsInfo, &pCraft[*pCraftIndex++], file, Buffer);
        AS_IF_FAIL_BREAK(Status);
    }

    return Status;
}

LONG
CED6AsDecompiler::
DumpOneCraft(
    ED6_ACTION_SCRIPT_INFO  *pAsInfo,
    ED6_AS_CRAFT_INFO       *pCraft,
    CFileDisk               &file,
    LPSTR                    Buffer
)
{
    LONG Status;
    ULONG CraftIndex, Offset;
    ED6_INSTRUCTION     *pInstruction;
    ED6_AS_CRAFT_INFO   *pFunction;

    pInstruction = pCraft->pInstruction;
    if (pInstruction == NULL ||
        TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_LINK) ||
        TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_DUMPED))
    {
/*
        ED6_AS_INSTRUCTION_MAP *pMap;
        pMap = FindInstrctionMapByCode(AS_JUMP);
        WriteScr("%s ( %s%04X )\n", pMap->pszName, NAME_CRAFT_LABEL_PREFIX, pInstruction->Offset);
*/
        return ASDECL_ERROR_DUMPED;
    }

    pFunction = pAsInfo->pFunctionInfo;
    Offset = pCraft->Offset;
    for (LONG FuncCount = pAsInfo->FunctionCount; FuncCount; ++pFunction, --FuncCount)
    {
        if (Offset >= pFunction->Offset)
        {
            Status = DumpOneFunction(pAsInfo, pFunction, file, Buffer);
            AS_IF_FAIL_BREAK(Status);
//            if (Status != ASDECL_ERROR_DUMPED)
                WriteScr("\n");
        }
    }

    CraftIndex = pCraft - pAsInfo->pCraftInfo;

    if (!TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_UNLABEL))
    {
        GetCraftName(pAsInfo, CraftIndex, Buffer);
        WriteScr("\n@_MOD 16\n#%s\n", Buffer);
        pInstruction->Flags |= INSTRUCTION_FLAG_UNLABEL;
    }

    for (ULONG InsCount = pCraft->Count; InsCount; ++pInstruction, --InsCount)
    {
        Offset = pInstruction->Offset;
        pFunction = pAsInfo->pFunctionInfo;
        for (LONG FuncCount = pAsInfo->FunctionCount; FuncCount; ++pFunction, --FuncCount)
        {
            if (Offset >= pFunction->Offset)
            {
                Status = DumpOneFunction(pAsInfo, pFunction, file, Buffer);
                AS_IF_FAIL_RETURN(Status);
            }
        }

        Status = DumpInstrction(pAsInfo, pCraft, pInstruction, file, Buffer);
        AS_IF_FAIL_BREAK(Status);
    }

    WriteScr("\n");

    return Status;
}

LONG
CED6AsDecompiler::
DumpFunctions(
    ED6_ACTION_SCRIPT_INFO *pAsInfo,
    CFileDisk              &file,
    LPSTR                   Buffer
)
{
    LONG Status;
    ED6_AS_CRAFT_INFO **pTable;

    pTable = pAsInfo->pFunctionTable;
    if (pTable == NULL)
        return ASDECL_ERROR_UNKNOWN;

    for (ULONG Count = pAsInfo->FunctionCount; Count; ++pTable, --Count)
    {
        if (*pTable == NULL)
            continue;

        Status = DumpOneFunction(pAsInfo, *pTable, file, Buffer);
        AS_IF_FAIL_BREAK(Status);
    }

    WriteScr("\n");
    return Status;
}

LONG
CED6AsDecompiler::
DumpOneFunction(
    ED6_ACTION_SCRIPT_INFO  *pAsInfo,
    ED6_AS_CRAFT_INFO       *pFunction,
    CFileDisk               &file,
    LPSTR                    Buffer
)
{
    LONG Status;
    ED6_INSTRUCTION *pInstruction;

    pInstruction = pFunction->pInstruction;
    if (pInstruction == NULL ||
        TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_LINK) ||
        TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_DUMPED))
    {
        return ASDECL_ERROR_DUMPED;
    }

    for (ULONG InsCount = pFunction->Count; InsCount; ++pInstruction, --InsCount)
    {
        Status = DumpInstrction(pAsInfo, pFunction, pInstruction, file, Buffer);
        AS_IF_FAIL_BREAK(Status);
    }

    WriteScr("\n");
    return Status;
}

BOOL CED6AsDecompiler::IsLabelNextInstruction(ED6_INSTRUCTION *pInstruction, ULONG Offset)
{
    ED6_INSTRUCTION_RECORD Ref;

    if (!FindDecompiled(Offset, Ref))
        return FALSE;

    if (Ref.InstructionIndex == 0)
        return FALSE;

    if (&Ref.pCraftInfo->pInstruction[Ref.InstructionIndex - 1] != pInstruction)
        return FALSE;

    return TRUE;
}

LONG
CED6AsDecompiler::
DumpInstrction(
    ED6_ACTION_SCRIPT_INFO  *pAsInfo,
    ED6_AS_CRAFT_INFO       *pCraft,
    ED6_INSTRUCTION         *pInstruction,
    CFileDisk               &file,
    LPSTR                    Buffer
)
{
    LONG Status;
    CHAR szParamLengthTable[] = { 'b', 's', 't', 'i' };
    ED6_INSTRUCTION_PARAM       *pParam;
    ED6_AS_INSTRUCTION_MAP      *pMap;
    ED6_INSTRUCTION_RECORD       Ref;

    if (TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_LINK))
    {
        if (pInstruction != pCraft->pInstruction)
            WriteScr("\n");

        return ASDECL_ERROR_DUMPED;
    }

    pMap = FindInstrctionMapByCode(pInstruction->Code);
    if (pMap == NULL)
        return ASDECL_ERROR_UNKNOWN_INSTRUCTION;

    pInstruction->Flags |= INSTRUCTION_FLAG_DUMPED;
    if (!TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_UNLABEL))
    {
        if (TEST_BITS(pInstruction->Flags, INSTRUCTION_FLAG_LABEL) ||
            FindFunction(pInstruction->Offset, Ref))
        {
            pInstruction->Flags |= INSTRUCTION_FLAG_UNLABEL;
            GetLabelName(pAsInfo, pInstruction->Offset, Buffer);
//            if (pInstruction != pCraft->pInstruction)
            WriteScr("\n");
            WriteScr("#%s\n", Buffer);
        }
    }

    if (pInstruction->Code == AS_GOTO)
    {
//        if (IsLabelNextInstruction(pInstruction, pInstruction->Param->Value.LowPart))
//            return ASDECL_ERROR_SUCCESS;
    }

    if (pMap->pszName != NULL)
    {
        WriteScr("%s", pMap->pszName);
    }
    else
    {
        WriteScr("%s%X", NAME_DEFAULT_INSTRUCTION_PREFIX, pMap->Instruction);
    }

    AS_IF_FAIL_RETURN(Status);

    if (pInstruction->ParamNumber == 0)
    {
        WriteScr("\n");
        m_bLastIsNewLine = FALSE;
        return ASDECL_ERROR_SUCCESS;
    }

    WriteScr("(");
    pParam = pInstruction->Param;
    for (ULONG Count = 0; Count != pInstruction->ParamNumber; ++pParam, Count++)
    {
        LPSTR pszParamDesc = NULL;
        ED6_INSTRUCTION_PARAM_DESC *pDesc = NULL;

        if (Count != 0)
        {
            WriteScr(", ");
        }

        pDesc = pMap->pParamDesc;
        for (ULONG i = pMap->DescCount; i; ++pDesc, --i)
        {
            if (pDesc->pszDescription == NULL)
                continue;

            if (Count != pDesc->ParamIndex)
                continue;

            if (pDesc->Value != pParam->Value.LowPart)
                continue;

            pszParamDesc = pDesc->pszDescription;
            break;
        }

        if (pszParamDesc != NULL)
        {
            WriteScr("%s", pszParamDesc);
            if (pParam->Length != pDesc->Length)
                WriteScr(":%c", szParamLengthTable[pParam->Length - 1]);
            continue;
        }

        if (TEST_BITS(pParam->Flags, INSTRUCTION_FLAG_FLOAT))
        {
            WriteScr("%f:f", pParam->Value.LowPart);
            continue;
        }

        if (!TEST_BITS(pParam->Flags, INSTRUCTION_PARAM_FLAG_ADDRESS))
        {
            if (pParam->Length <= countof(szParamLengthTable))
            {
                WriteScr("0x%X:%c", pParam->Value.LowPart, szParamLengthTable[pParam->Length - 1]);
            }
            else if (pParam->Length == INSTRUCTION_LENGTH_STRING)
            {
                WriteScr("\"%s\"", pParam->Value.LowPart ? (LPSTR)pParam->Value.LowPart : "");
            }
            else
            {
                PBYTE pbParam = (PBYTE)&pParam->Value;

                WriteScr("[%02X", *pbParam++);
                for (ULONG Length = pParam->Length - 1; Length; --Length)
                    WriteScr(" %02X", *pbParam++);
                WriteScr("]");
            }
        }
        else
        {
            GetLabelName(pAsInfo, pParam->Value.LowPart, Buffer);
            WriteScr("%s:s", Buffer);
        }
    }

    WriteScr(")\n");

    return Status;
}

LONG CED6AsDecompiler::CreateDefinition(LPWSTR pszAsFile, LPSTR Buffer)
{
    WCHAR szPath[MAX_PATH];
    LPWSTR pszFileName;

    lstrcpyW(szPath, pszAsFile);
    pszFileName = findnamew(szPath);
    if (pszFileName != szPath)
        *pszFileName = 0;

    lstrcpyW(pszFileName, WSTRING(NAME_DEFINITION_FILE));
    if (IsPathExistsW(szPath))
        return ASDECL_ERROR_SUCCESS;

    LONG                        Status;
    CFileDisk                   file;
    ED6_AS_INSTRUCTION_MAP     *pMap;
    ED6_INSTRUCTION_PARAM_DESC *pDesc;
    CHAR szParamLengthTable[] = { 'b', 's', 't', 'i' };

    if (!file.Create(szPath))
        return ASDECL_ERROR_CREATE_FILE;

    WriteScr(
        "@_DEFI 4\n"
        "@_DEFF 4\n"
        "@_IGNORECASE\n"
        "\n"
    );

    pMap = g_InstructionMap;
    for (ULONG Count = countof(g_InstructionMap); Count; ++pMap, --Count)
    {
        if (pMap->pszName != NULL)
        {
            WriteScr("@%s [%02X]\n", pMap->pszName, pMap->Instruction);
        }
        else
        {
//            WriteScr("@%s%X [%02X]\n", NAME_DEFAULT_INSTRUCTION_PREFIX, pMap->Instruction, pMap->Instruction);
        }

        pDesc = pMap->pParamDesc;
        for (ULONG DescCount = pMap->DescCount; DescCount; pDesc++, --DescCount)
        {
            if (pDesc->pszDescription == NULL)
                continue;
#if 0
            if (pDesc->Length > 4)
            {
                PBYTE  pbBuffer;
                WriteScr("    @%s [", pDesc->pszDescription);
                pbBuffer = (PBYTE)&pDesc->Value;
                for (ULONG Length = pDesc->Length; ; )
                {
                    WriteScr("%02X", *pbBuffer++);
                    if (--Length == 0)
                        break;
                    WriteScr(" ");
                }
                WriteScr("]\n");
            }
            else
#endif
            {
                WriteScr(
                    "    @%s 0x%X:%c\n",
                    pDesc->pszDescription,
                    pDesc->Value,
                    szParamLengthTable[pDesc->Length - 1]
                );
            }
        }
    }

    WriteScr("\n");
    pMap = g_InstructionMap;
    for (ULONG Count = countof(g_InstructionMap); Count; ++pMap, --Count)
    {
        WriteScr("@%s%X [%02X]\n", NAME_DEFAULT_INSTRUCTION_PREFIX, pMap->Instruction, pMap->Instruction);
    }

    return 0;
}

LONG CED6AsDecompiler::DumpToFile(ED6_ACTION_SCRIPT_INFO *pAsInfo, LPWSTR pszAsFile, LPWSTR pszOutput)
{
    LONG        Status;
    CHAR        Buffer[0x400];
    CFileDisk   file;

    Status = CreateDefinition(pszAsFile, Buffer);
    AS_IF_FAIL_RETURN(Status);

    Status = ASDECL_ERROR_UNKNOWN;
    LOOP_ONCE
    {
        if (!file.Create(pszOutput))
            AS_BREAK(Status, ASDECL_ERROR_CREATE_FILE);

        _wsetlocale(LC_CTYPE, L"");
        WriteScr(
            "@_FILE \"debug_%S\"\n"
            "@_INCLUDE \"%s\"\n"
            "\n",
            findnamew(pszAsFile), NAME_DEFINITION_FILE);

        WriteScr(
            "@%s %d\n"
            "\n",
            NAME_HEADER_UNKNOWN,
            pAsInfo->Unknown);

        WriteScr(
            "(%s:s)\n"
            "(%s:s)\n"
            "(%s:s)\n"
            "\n",
            LABEL_CRAFT_OFFSET_TABLE,
            LABEL_CRAFT_OFFSET_TABLE_END,
            NAME_HEADER_UNKNOWN);

        WriteScr("; Char chip pattern info  CH_Index, CH_DAT_Index, CP_Index, CP_DAT_Index\n");

        CHAR_CHIP_PATTERN_INFO *pChipPtn = pAsInfo->pChrChipPtnInfo;
        for (ULONG Index = 0, Count = pAsInfo->ChrChipPtnCount; Count; ++Index, --Count)
        {
            WriteScr(
                " (0x%04X:s, 0x%04X:s, 0x%04X:s, 0x%04X:s)",
                pChipPtn->CHIndex,
                pChipPtn->CHDatIndex,
                pChipPtn->CPIndex,
                pChipPtn->CPDatIndex);
            ++pChipPtn;

            if (Index & 1)
                WriteScr("\n");
        }
        WriteScr("\n[FF FF FF FF]\n\n");

        WriteScr("; 3d model file\n");

        for (LPSTR pszX3FileName = pAsInfo->pszXFileName; ; )
        {
            LPSTR pString;
            ULONG Length;

            Length  = StrLengthA(pszX3FileName) + 1;
            pString = *pszX3FileName == 0 ? NULL : AllocString(pszX3FileName, Length);
            WriteScr("\"%s\"\n", pString == NULL ? pszX3FileName : pString);
            FreeString(pString);

            if (*pszX3FileName == 0)
            {
                if (pszX3FileName != pAsInfo->pszXFileName)
                    WriteScr("[%02X %02X]\n", pszX3FileName[1], pszX3FileName[2]);
                break;
            }

            pszX3FileName += Length;
        }

        WriteScr("\n#%s\n", LABEL_CRAFT_OFFSET_TABLE);

        ED6_AS_CRAFT_INFO *pCraft;
        ED6_INSTRUCTION   *pInstruction;

        pCraft = pAsInfo->pCraftInfo;
        for (ULONG Index = 0, Count = pAsInfo->CraftCount; Count; ++pCraft, ++Index, --Count)
        {
            ULONG TrueIndex;

            if (pCraft->Offset == ED6_INVALID_OFFSET)
            {
                PBYTE p = (PBYTE)&pCraft->Offset;

                WriteScr("[%02X", *p++);
                for (ULONG Len = sizeof(ED6_INVALID_OFFSET) - 1; Len; --Len)
                    WriteScr(" %02X", *p++);
                WriteScr("]\n");

                continue;
            }

            pInstruction = UnlinkInstruction(pCraft->pInstruction);
            if (pInstruction == NULL)
                continue;

            TrueIndex = Index;
            for (ULONG i = 0; i != Index; ++i)
            {
                if (pInstruction->Offset == pAsInfo->pCraftInfo[i].Offset)
                {
                    TrueIndex = i;
                    break;
                }
            }

            GetCraftName(pAsInfo, TrueIndex, Buffer);
            WriteScr(" (%s:s)", Buffer);

            if (Index >=countof(g_szIntrinsicCraft) && (Index + 1 - countof(g_szIntrinsicCraft)) % 5 != 0)
                continue;

            WriteScr("\n");
        }
        WriteScr("\n#%s\n\n", LABEL_CRAFT_OFFSET_TABLE_END);

        PBYTE pbFlags = pAsInfo->pbAsBuffer + pAsInfo->CraftOffsetTableEndOffset;
        WriteScr(
            "[%02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X %02X]\n\n",
            pbFlags[0], pbFlags[1], pbFlags[2], pbFlags[3], pbFlags[4],
            pbFlags[5], pbFlags[6], pbFlags[7], pbFlags[8], pbFlags[9],
            pbFlags[10], pbFlags[11], pbFlags[12], pbFlags[13], pbFlags[14],
            pbFlags[15], pbFlags[16]);

        Status = DumpCrafts(pAsInfo, file, Buffer);
        AS_IF_FAIL_BREAK(Status);

        Status = DumpFunctions(pAsInfo, file, Buffer);
    }

    return Status;
}