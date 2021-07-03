#include "ASDecompiler.h"

FORCEINLINE LONG CED7AsDecompiler::HandleNoParam(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleDynamicLengthParam(pAsInfo, pInstruction, 0, NULL, NULL);
}

LONG
CED7AsDecompiler::
HandleFixedLengthParam(
    ED6_ACTION_SCRIPT_INFO  *pAsInfo,
    ED6_INSTRUCTION         *pInstruction,
    ULONG                    ParamCount,
    ULONG                    ParamLength,
    PULONG                   pParamFlags /* = NULL */
)
{
    ULONG _ParamLength[INSTRUCTION_MAX_PARAM];
    memset4(_ParamLength, ParamLength, ParamCount * 4);
    return HandleDynamicLengthParam(pAsInfo, pInstruction, ParamCount, _ParamLength, pParamFlags);
}

LONG
CED7AsDecompiler::
HandleDynamicLengthParam(
    ED6_ACTION_SCRIPT_INFO  *pAsInfo,
    ED6_INSTRUCTION         *pInstruction,
    ULONG                    ParamCount,
    PULONG                   pParamLength,
    PULONG                   pParamFlags /* = NULL */
)
{
    PBYTE pbEnd;
    ED6_INSTRUCTION_PARAM *pParam;

    if (ParamCount > INSTRUCTION_MAX_PARAM)
        return ASDECL_ERROR_INVALID_PARAM_COUNT;

    pbEnd = pAsInfo->pbAsBuffer + pAsInfo->BufferSize;
    pInstruction->Code = *pAsInfo->pbCurrent++;
    pInstruction->ParamNumber = ParamCount;

    pParam = pInstruction->Param;
    for (; ParamCount; ++pParam, --ParamCount)
    {
        ULONG Length = *pParamLength++;

        pParam->Length = Length;
        if (Length == INSTRUCTION_LENGTH_STRING)
        {
            Length = StrLengthA((LPSTR)pAsInfo->pbCurrent);
            if (Length == 0)
                pParam->Value.LowPart = NULL;
            else
                pParam->Value.LowPart = (ULONG)AllocString((LPSTR)pAsInfo->pbCurrent, Length + 1);
            ++Length;
        }
        else if (Length >= pAsInfo->BufferSize)
        {
            return ASDECL_ERROR_REFERENCE_INVALID_OFFSET;
        }
        else
        {
            pParam->Value.QuadPart = 0;
            CopyMemory(&pParam->Value, pAsInfo->pbCurrent, Length);
        }
        pAsInfo->pbCurrent += Length;

        if (pParamFlags != NULL)
        {
            pParam->Flags |= *pParamFlags++;
            if (TEST_BITS(pParam->Flags, INSTRUCTION_PARAM_FLAG_ADDRESS))
            {
                ED6_INSTRUCTION_RECORD Ref;

                AddFunction((USHORT)pParam->Value.LowPart);
                if (!FindDecompiled((USHORT)pParam->Value.LowPart, Ref))
                    continue;

                Ref.pCraftInfo->pInstruction[Ref.InstructionIndex].Flags |= INSTRUCTION_FLAG_LABEL;
            }
        }
    }

    return ASDECL_ERROR_SUCCESS;
}

LONG CED7AsDecompiler::Handle00(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle01(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    LONG  Status;
    ULONG AsInfoFlags, Offset, Length[] = { 2 };
    ULONG Flags[]  = { INSTRUCTION_PARAM_FLAG_ADDRESS };
    Status = HandleDynamicLengthParam(pAsInfo, pInstruction, 1, Length, Flags);
    AS_IF_FAIL_RETURN(Status);

    AsInfoFlags = ASINFO_FLAG_LOOPBEG | ASINFO_FLAG_LOOPEND;

    if ((pAsInfo->Flags & AsInfoFlags) == AsInfoFlags)
    {
        pAsInfo->Flags &= ~AsInfoFlags;
        Offset = (USHORT)pAsInfo->lParam;
    }
    else
    {
        Offset = (USHORT)pInstruction->Param[0].Value.LowPart;
    }

    pAsInfo->pbCurrent = pAsInfo->pbAsBuffer + Offset;

    return Status;
}

LONG CED7AsDecompiler::Handle02(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle03(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle04(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle05(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle06(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle07(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle08(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle09(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle0A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle0B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle0C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG  Count;
    PULONG pLength;

    if (pAsInfo->pbCurrent[2] == 0xFC)
    {
        ULONG Length[] = { 1, 1, 4, 4, 4, 2, 2, 1 };

        pLength = Length;
        Count = countof(Length);
    }
    else
    {
        ULONG Length[] = { 1, 1, 2, 2, 1 };

        pLength = Length;
        Count = countof(Length);
    }

    return HandleDynamicLengthParam(pAsInfo, pInstruction, Count, pLength);
}

LONG CED7AsDecompiler::Handle0D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle0E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle0F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle10(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle11(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle12(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle13(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle14(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle15(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle16(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle17(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle18(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle19(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, INSTRUCTION_LENGTH_STRING, 2, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle1A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle1B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle1C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle1D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle1E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle1F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle20(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle21(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle22(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2, 1 };
    ULONG Flags[]  = { 0, 0, INSTRUCTION_PARAM_FLAG_ADDRESS, 0 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, Flags);
}

LONG CED7AsDecompiler::Handle23(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle24(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle25(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle26(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle27(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle28(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle29(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle2A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { INSTRUCTION_LENGTH_STRING, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle2B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo,pInstruction);
}

LONG CED7AsDecompiler::Handle2C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle2D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle2E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle2F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle31(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle32(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle33(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle34(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle35(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle36(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle39(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2, 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle3A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle3B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle3C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle3D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle3E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle3F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle40(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle41(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle42(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle43(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle44(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle45(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle46(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle47(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle48(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle49(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle4A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle4B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 2 };
    ULONG Flags[]  = { 0, 0, 0, INSTRUCTION_PARAM_FLAG_ADDRESS };

    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, Flags);
}

// below check to ret

LONG CED7AsDecompiler::Handle4C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    LONG  Status;
    ULONG Length[] = { 2 };
    ULONG Flags[]  = { INSTRUCTION_PARAM_FLAG_ADDRESS };

    pInstruction->Flags |= INSTRUCTION_FLAG_LOOP;
    Status = HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, Flags);
    AS_IF_FAIL_RETURN(Status);

    pAsInfo->Flags |= ASINFO_FLAG_LOOPBEG;
    pAsInfo->lParam = (USHORT)pInstruction->Param->Value.LowPart;

    return Status;
}

LONG CED7AsDecompiler::Handle4D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle4E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    pAsInfo->Flags |= ASINFO_FLAG_LOOPEND;
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle4F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle50(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    ULONG Flags[]  = { INSTRUCTION_PARAM_FLAG_ADDRESS };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, 1, Length, Flags);
}

LONG CED7AsDecompiler::Handle51(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle52(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle53(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle54(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle55(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle56(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle57(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle58(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle59(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle5A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle5B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle5C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle5D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle5E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle5F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle60(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle61(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle62(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2, 2, 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle64(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle65(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle66(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

// ---------------------------- above not check strcpy

LONG CED7AsDecompiler::Handle67(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle68(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle6A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle6B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle6C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle6D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle6E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle6F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle70(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2, 2, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle71(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle72(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle73(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle77(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle78(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle79(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle7A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle7B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle7C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle7D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle7E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle7F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle80(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED7AsDecompiler::Handle82(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle83(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle84(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2, 2, 2, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle85(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle87(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle89(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle8A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle8B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle8C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle8D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle8E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG  Count;
    PULONG pLength;

    if (pAsInfo->pbCurrent[1] == 1)
    {
        ULONG Length[] = { 1, 1, INSTRUCTION_LENGTH_STRING };
        pLength = Length;
        Count   = countof(Length);
    }
    else if (pAsInfo->pbCurrent[1] == 0xD)
    {
        ULONG Length[] = { 1, 1, 4, 4, 4, 4, 4 };
        pLength = Length;
        Count   = countof(Length);
    }
    else
    {
        ULONG Length[] = { 1, 1, 4, 4, 4, 4 };
        pLength = Length;
        Count   = countof(Length);
    }

    return HandleDynamicLengthParam(pAsInfo, pInstruction, Count, pLength);
}

LONG CED7AsDecompiler::Handle8F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle91(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG  Count;
    PULONG pLength;

    if (pAsInfo->pbCurrent[1] != 0)
    {
        ULONG Length[] = { 1 };
        pLength = Length;
        Count   = countof(Length);
    }
    else
    {
        PBYTE p;
        ULONG Length[] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        pLength = Length;
        Count   = 2;

        p = pAsInfo->pbCurrent + 2;
        for (ULONG n = 10; n; --n)
        {
            ++Count;
            if (*p++ == 0xFF)
                break;
        }
    }

    return HandleDynamicLengthParam(pAsInfo, pInstruction, Count, pLength);
}

LONG CED7AsDecompiler::Handle92(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4, 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle93(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle94(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle95(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::Handle96(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle97(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle99(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle9A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle9B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle9C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle9E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::Handle9F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleA0(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleA1(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 2, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleA6(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleA7(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 2, 2, 2, 2, 2, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleA8(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleA9(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleAA(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleAC(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleAD(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleAE(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleAF(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB0(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB1(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Count, *pLength;
    PBYTE p;

    p = pAsInfo->pbCurrent + 1;
    p += StrLengthA((PCHAR)p) + 1;
    if (*p == 2)
    {
        ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 1, 4, INSTRUCTION_LENGTH_STRING };
        pLength = Length;
        Count = countof(Length);
    }
    else
    {
        ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 1, 4 };
        pLength = Length;
        Count = countof(Length);
    }

    return HandleDynamicLengthParam(pAsInfo, pInstruction, Count, pLength);
}

LONG CED7AsDecompiler::HandleB2(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB3(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB4(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB5(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 2, 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB6(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 2, 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED7AsDecompiler::HandleB7(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED7AsDecompiler::HandleB8(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}
