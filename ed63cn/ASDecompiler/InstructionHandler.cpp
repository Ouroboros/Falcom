#include "ASDecompiler.h"

FORCEINLINE LONG CED6AsDecompiler::HandleNoParam(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleDynamicLengthParam(pAsInfo, pInstruction, 0, NULL, NULL);
}

LONG
CED6AsDecompiler::
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
CED6AsDecompiler::
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

LONG CED6AsDecompiler::Handle00(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle01(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
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

LONG CED6AsDecompiler::Handle02(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleFixedLengthParam(pAsInfo, pInstruction, 2, 1);
}

LONG CED6AsDecompiler::Handle03(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle04(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle05(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle06(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleFixedLengthParam(pAsInfo, pInstruction, 1, 4);
}

LONG CED6AsDecompiler::Handle07(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle08(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle09(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle0A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle0B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle0C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle0D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle0E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle0F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle10(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle11(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle12(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle13(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle14(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle15(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle16(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle17(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle18(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle19(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, INSTRUCTION_LENGTH_STRING, 2, 4, 4, 4, 2, 2, 2, 2, 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle1A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle1B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle1C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle1D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle1E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle1F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle20(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle21(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle22(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2, 1 };
    ULONG Flags[]  = { 0, 0, INSTRUCTION_PARAM_FLAG_ADDRESS, 0 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, Flags);
}

LONG CED6AsDecompiler::Handle23(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle24(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle25(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle26(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle27(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle28(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle29(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle2A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { INSTRUCTION_LENGTH_STRING, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle2B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo,pInstruction);
}

LONG CED6AsDecompiler::Handle2C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle2D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle2E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle2F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle30(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    UNREFERENCED_PARAMETER(pAsInfo);
    UNREFERENCED_PARAMETER(pInstruction);
    return ASDECL_ERROR_NOT_IMPLEMENTED;
}

LONG CED6AsDecompiler::Handle31(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle32(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle33(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle34(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle35(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle36(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle37(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle38(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle39(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle3A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle3B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle3C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle3D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle3E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle3F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle40(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle41(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle42(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle43(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle44(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle45(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle46(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle47(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle48(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle49(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle4A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle4B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 2 };
    ULONG Flags[]  = { 0, 0, 0, INSTRUCTION_PARAM_FLAG_ADDRESS };

    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, Flags);
}

LONG CED6AsDecompiler::Handle4C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
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

LONG CED6AsDecompiler::Handle4D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle4E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    pAsInfo->Flags |= ASINFO_FLAG_LOOPEND;
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle4F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle50(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    ULONG Flags[]  = { INSTRUCTION_PARAM_FLAG_ADDRESS };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, 1, Length, Flags);
}

LONG CED6AsDecompiler::Handle51(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle52(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle53(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle54(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle55(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle56(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle57(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle58(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle59(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle5A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle5B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle5C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle5D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle5E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle5F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle60(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle61(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle62(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle63(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle64(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle65(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle66(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle67(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle68(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle69(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle6A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle6B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle6C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle6D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle6E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle6F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle70(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle71(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle72(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle73(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle74(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle75(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle76(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle77(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle78(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle79(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle7A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle7B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle7C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle7D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle7E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle7F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4, 4, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle80(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length, NULL);
}

LONG CED6AsDecompiler::Handle81(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle82(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle83(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle84(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2, 2, 2, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle85(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle86(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 2, 2, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle87(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle88(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle89(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle8A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle8B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle8C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle8D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle8E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG  Count;
    PULONG pLength;

    if (pAsInfo->pbCurrent[1] == 1)
    {
        ULONG Length[] = { 1, 1, INSTRUCTION_LENGTH_STRING };
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

LONG CED6AsDecompiler::Handle8F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle90(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle91(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle92(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4, 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle93(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle94(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle95(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    return HandleNoParam(pAsInfo, pInstruction);
}

LONG CED6AsDecompiler::Handle96(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, INSTRUCTION_LENGTH_STRING, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle97(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 2, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle98(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle99(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle9A(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle9B(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle9C(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle9D(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle9E(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::Handle9F(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA0(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4, 2, INSTRUCTION_LENGTH_STRING };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA1(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA2(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA3(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA4(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG  Count;
    PULONG pLength;

    if (pAsInfo->pbCurrent[1] == 2)
    {
        ULONG Length[] = { 1, 2 };
        pLength = Length;
        Count = countof(Length);
    }
    else
    {
        ULONG Length[] = { 1 };
        pLength = Length;
        Count = countof(Length);
    }

    return HandleDynamicLengthParam(pAsInfo, pInstruction, Count, pLength);
}

LONG CED6AsDecompiler::HandleA5(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA6(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1, 4, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA7(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA8(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleA9(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleAA(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleAB(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleAC(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 1 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleAD(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleAE(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 2, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleAF(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 1, 4, 4, 4 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleB0(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}

LONG CED6AsDecompiler::HandleB1(ED6_ACTION_SCRIPT_INFO *pAsInfo, ED6_INSTRUCTION *pInstruction)
{
    ULONG Length[] = { 1, 2 };
    return HandleDynamicLengthParam(pAsInfo, pInstruction, countof(Length), Length);
}
