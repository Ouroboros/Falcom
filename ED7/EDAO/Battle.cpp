#include "edao.h"

NAKED VOID CBattle::NakedCopyMagicAndCraftData()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        mov     edx, [ebp + 08h];
        and     dword ptr [ebp - 20h], 0;
        jmp     CBattle::CopyMagicAndCraftData
    }
}

VOID FASTCALL CBattle::CopyMagicAndCraftData(PMONSTER_STATUS MSData)
{
    PUSHORT         MagicList;
    ULONG_PTR       MaxMagicNumber;
    PCRAFT_AI_INFO  Magic;

    if (!IsCustomChar(MSData->CharID))
        return;

    MaxMagicNumber  = countof(MSData->ArtsAiInfo);
    Magic           = MSData->ArtsAiInfo;
    MagicList       = GetSaveData()->GetChrMagicList() + MSData->CharID * MaxMagicNumber;

    for (ULONG_PTR Count = countof(MSData->ArtsAiInfo); Count; --Count)
    {
        if (Magic->CraftIndex == 0)
            break;

        --MaxMagicNumber;
        ++Magic;
    }

    for (; MaxMagicNumber; ++Magic, ++MagicList, --MaxMagicNumber)
    {
        Magic->CraftIndex       = *MagicList;
        Magic->AriaActionIndex  = 6;
        Magic->ActionIndex      = 7;
        Magic->Condition        = 0;
    }

    *(PVOID *)_AddressOfReturnAddress() = (PVOID)0x9A37F4;
}

NAKED VOID CBattle::NakedOverWriteBattleStatusWithChrStatus()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        mov     edx, edi;
        push    eax;
        call    CBattle::OverWriteBattleStatusWithChrStatus
        ret;
    }
}

PMONSTER_STATUS FASTCALL CBattle::OverWriteBattleStatusWithChrStatus(PMONSTER_STATUS MSData, PCHAR_STATUS ChrStatus)
{
    MSData = PtrSub(MSData, FIELD_OFFSET(MONSTER_STATUS, ChrStatus[BattleStatusFinal].MaximumHP));

    PCHAR_STATUS Raw = &MSData->ChrStatus[BattleStatusRaw];
    PCHAR_STATUS Final = &MSData->ChrStatus[BattleStatusFinal];

    *Final = *ChrStatus;

    if (!IsCustomChar(MSData->CharID))
        return MSData;

    Final->MaximumHP    += Raw->MaximumHP   / 2;
    Final->InitialHP    += Raw->InitialHP   / 2;
    Final->MaximumEP    += Raw->MaximumEP   / 2;
    Final->InitialEP    += Raw->InitialEP   / 2;
    Final->STR          += Raw->STR         * 2 / 3;
    Final->DEF          += Raw->DEF         * 2 / 3;
    Final->ATS          += Raw->ATS         * 2 / 3;
    Final->ADF          += Raw->ADF         * 2 / 3;
    Final->DEX          += Raw->DEX         * 2 / 3;
    Final->AGL          += Raw->AGL         * 2 / 3;
    Final->MOV          += Raw->MOV         * 2 / 3;
    Final->SPD          += Raw->SPD         * 2 / 3;
    Final->RNG           = Raw->RNG + 1;

    return MSData;
}

NAKED VOID CBattle::NakedIsChrStatusNeedRefresh()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0Ch];
        mov     edx, dword ptr [ebp - 8Ch];
        push    dword ptr [ebp - 25E8h];
        push    eax;
        call    CBattle::IsChrStatusNeedRefresh
        neg     eax;
        ret;
    }
}

BOOL FASTCALL CBattle::IsChrStatusNeedRefresh(ULONG_PTR ChrPosition, PCHAR_STATUS CurrentStatus, LONG_PTR PrevLevel)
{
    PMONSTER_STATUS MSData;

    MSData = GetMonsterStatus() + ChrPosition;

    if (!IsCustomChar(MSData->CharID))
    {
        return CurrentStatus->Level != PrevLevel;
    }

    return TRUE;
}

NAKED ULONG CBattle::NakedGetChrIdForSCraft()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 08h];
        call    CBattle::GetSaveData
        mov     ecx, eax;
        call    CSSaveData::GetPartyChipMap
        mov     ecx, dword ptr [ebp - 14h];
        movzx   ecx, [ecx]MONSTER_STATUS.CharID;
        movzx   eax, [eax + ecx * 2];
        cmp     eax, MINIMUM_CUSTOM_CHAR_ID
        cmovae  ecx, eax;
        ret;
    }
}

ULONG FASTCALL CBattle::GetVoiceChrIdWorker(PMONSTER_STATUS MSData)
{
    ULONG ChrId, PartyId;

    ChrId = MSData->CharID;
    PartyId = GetSaveData()->GetPartyChipMap()[ChrId];

    return IsCustomChar(ChrId) ? PartyId : ChrId;
}

/*++

  mov     word ptr [ebp-const], r16
  mov     r32, const
  mov     word ptr [ebp-const], r16
  mov     r32, const
  mov     word ptr [ebp-const], r16
  mov     r32, [ebp+8]
  movzx   r32, [r32+0A]

--*/

NAKED VOID CBattle::NakedGetTurnVoiceChrId()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 0Ch];
        mov     edx, [ebp + 08h];
        call    CBattle::GetVoiceChrIdWorker;
        mov     ecx, eax;
        ret;
    }
}

NAKED VOID CBattle::NakedGetReplySupportVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetRunawayVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetTeamRushVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetUnderAttackVoiceChrId()
{
    INLINE_ASM
    {
        call    CBattle::NakedGetTurnVoiceChrId
        mov     dword ptr [ebp-0xF8], eax;
        ret;
    }
}

NAKED VOID CBattle::NakedGetUnderAttackVoiceChrId2()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

NAKED VOID CBattle::NakedGetSBreakVoiceChrId()
{
    INLINE_ASM
    {
        jmp CBattle::NakedGetTurnVoiceChrId;
    }
}

VOID FASTCALL CBattle::HandleBattleState(ULONG_PTR CurrentState)
{
    static ULONG_PTR PreviousState;

    if (PreviousState == CurrentState)
        return;

    PreviousState = CurrentState;
    if (CurrentState != 0x12)
        return;

    PAT_BAR_ENTRY*  Entry;
    BOOLEAN         Flags[0x20];
    ULONG_PTR       Count;
    PMONSTER_STATUS MSData, MSDataList[countof(Flags)];

    ZeroMemory(Flags, sizeof(Flags));

    Count = 0;

    FOR_EACH(Entry, GetBattleATBar()->EntryPointer, countof(GetBattleATBar()->EntryPointer))
    {
        MSData = Entry[0]->MSData;
        if (MSData == nullptr)
            continue;

        if (Entry[0]->IsSBreaking && !MSData->IsChrEnemy())
            return;

        if (Flags[MSData->CharPosition])
            continue;

        Flags[MSData->CharPosition] = TRUE;

        if (!ThinkSBreak(MSData, Entry[0]))
            continue;

        MSDataList[Count++] = MSData;
    }

    if (Count == 0)
        return;

    GetEDAO()->GetSound()->PlaySound(506);

    for (PMONSTER_STATUS *MSData = MSDataList; Count; ++MSData, --Count)
    {
        (*MSData)->AT = 0;
        GetBattleATBar()->AdvanceChrInATBar(*MSData, IsForceInsertToFirst());
    }
}

NAKED VOID CBattle::NakedGetBattleState()
{
    static ULONG PreviousState;

    INLINE_ASM
    {
        mov     dword ptr [ebp - 294h], ecx;
        mov     edx, dword ptr [eax + 113078h];
        mov     ecx, eax;
        jmp     CBattle::HandleBattleState
    }
}

NAKED LONG CBattle::NakedEnemyThinkAction()
{
    INLINE_ASM
    {
        mov     dword ptr [ebp - 114h], eax;
        mov     edx, [ebp + 08h];
        mov     ecx, [ebp - 0Ch];
        call    CBattle::EnemyThinkAction
        or      eax, eax;
        mov     eax, 991CBDh;
        cmove   eax, [esp];
        mov     [esp], eax;
        ret;
    }
}

VOID THISCALL CBattle::SetCurrentActionChrInfo(USHORT Type, PMONSTER_STATUS MSData)
{
    PTEB_ACTIVE_FRAME Frame;

    Frame = FindThreadFrame(THINK_SBREAK_FILTER);

    if (Frame != nullptr && Frame->Data == (ULONG_PTR)MSData)
        return;

    return (this->*StubSetCurrentActionChrInfo)(Type, MSData);
}

BOOL FASTCALL CBattle::EnemyThinkAction(PMONSTER_STATUS MSData)
{
    PUSHORT         Target;
    PAT_BAR_ENTRY   Entry;

    Entry = GetBattleATBar()->EntryPointer[0];

    if (!MSData->IsChrEnemy() ||
        Entry == nullptr ||
        Entry->MSData != MSData ||
        !Entry->IsSBreaking)
    {
        return FALSE;
    }

    ULONG_PTR Index, AliveCount, AliveTarget[countof(MSData->Target)];

    AliveCount = 0;

    FOR_EACH(Target, MSData->Target, (ULONG_PTR)MSData->TargetCount)
    {
        if (*Target == 0xFF)
            continue;

        if (FLAG_ON(GetMonsterStatus()[*Target].ChrStatus[BattleStatusFinal].ConditionFlags, CraftConditions::Dead))
            continue;

        AliveTarget[AliveCount++] = *Target;
    }

    MSData->TargetCount = AliveCount;

    //AliveCount = 0;

    if (AliveCount == 0)
    {
        ShowConditionText(MSData, "SBREAK FAILED");

        MSData->SelectedActionType = 8;
        MSData->CurrentCraftIndex = 9;

        SetCurrentActionChrInfo(0x16, MSData);

        return TRUE;
    }

    Index = 0;

    FOR_EACH(Target, MSData->Target, countof(AliveTarget))
    {
        if (AliveCount == 0)
        {
            *Target = 0xFF;
        }
        else
        {
            --AliveCount;
            *Target = AliveTarget[Index++];
        }
    }

    SetCurrentActionChrInfo(0xA, MSData);

    return TRUE;
}

BOOL CBattle::ThinkSBreak(PMONSTER_STATUS MSData, PAT_BAR_ENTRY Entry)
{
    BOOL Success;

    //TYPE_OF(&CBattle::ThinkSBreak) ThinkMagicEveryChrAction;
    //*(PULONG_PTR)&ThinkMagicEveryChrAction = 0x9926E0;

    TYPE_OF(&CBattle::ThinkSCraft) ThinkSCraft;
    *(PULONG_PTR)&ThinkSCraft = 0x98E730;

    if (Entry->IsSBreaking)
        return FALSE;

    if (!MSData->IsChrCanThinkSCraft())
        return FALSE;

    ULONG_PTR Conditions =  CraftConditions::Frozen         |
                            CraftConditions::Landification  |
                            CraftConditions::Sleeping       |
                            CraftConditions::Stun           |
                            CraftConditions::BanCraft       |
                            CraftConditions::Confusion      |
                            CraftConditions::OnehitKill     |
                            CraftConditions::Vanish         |
                            CraftConditions::GreenPepper    |
                            CraftConditions::Dead;

    if (FindEffectInfoByCondition(MSData, Conditions) != nullptr)
        return FALSE;

    struct
    {
        USHORT                          ActionType;
        USHORT                          CurrentCraftIndex;
        USHORT                          CurrentAiIndex;
        TYPE_OF(MSData->SelectedCraft)  SelectedCraft;

    } SavedData;

    SavedData.ActionType        = MSData->SelectedActionType;
    SavedData.CurrentCraftIndex = MSData->CurrentCraftIndex;
    SavedData.CurrentAiIndex    = MSData->CurrentAiIndex;
    SavedData.SelectedCraft     = MSData->SelectedCraft;

    TEB_ACTIVE_FRAME Frame;

    Frame.Context   = THINK_SBREAK_FILTER;
    Frame.Data      = (ULONG_PTR)MSData;
    Frame.Push();

    Success = TRUE;
    Success = (this->*ThinkSCraft)(MSData);

    Frame.Pop();

    if (!Success)
    {
        MSData->SelectedActionType  = SavedData.ActionType;
        MSData->CurrentCraftIndex   = SavedData.CurrentCraftIndex;
        MSData->CurrentAiIndex      = SavedData.CurrentAiIndex;
        MSData->SelectedCraft       = SavedData.SelectedCraft;
        return FALSE;
    }

    if (MSData->CurrentActionType == ACTION_ARIA_ARTS ||
        MSData->CurrentActionType == ACTION_ARIA_CRAFT ||
        MSData->PreviousActionType == ACTION_ARIA_ARTS ||
        MSData->PreviousActionType == ACTION_ARIA_CRAFT)
    {
        CancelAria(MSData, TRUE);
    }

    return TRUE;
}

VOID
THISCALL
CBattle::
ExecuteActionScript(
    PMONSTER_STATUS MSData,
    PBYTE           ActionScript,
    BYTE            ChrThreadId,
    USHORT          ScriptOffset,
    ULONG           Unknown1,
    ULONG           Unknown2,
    ULONG           Unknown3
)
{
    if (ScriptOffset == 0xFFFF)
    {
        ULONG_PTR Offset = 0;
        while (ActionScript[Offset] != 0)
            ++Offset;

        ScriptOffset = Offset;
    }

    return (this->*StubExecuteActionScript)(MSData, ActionScript, ChrThreadId, ScriptOffset, Unknown1, Unknown2, Unknown3);
}

NAKED VOID CBattle::NakedAS8DDispatcher()
{
    INLINE_ASM
    {
        push    ecx;
        mov     ecx, [ebp - 0Ch];
        mov     edx, [ebp + 08h];
        mov     eax, [ebp + 0Ch];
        mov     eax, [eax + 20h];
        lea     eax, [eax - 12h];
        push    eax;
        call    CBattle::AS8DDispatcher
        pop     ecx;
        cmp     ecx, 0x62;
        ret;
    }
}

VOID FASTCALL CBattle::AS8DDispatcher(PMONSTER_STATUS MSData, PAS_8D_PARAM Parameter)
{
    if (MSData == nullptr)
        return;

    if (Parameter->Function < AS_8D_FUNCTION_MINIMUM)
        return;

    switch (Parameter->Function)
    {
        case AS_8D_FUNCTION_REI_JI_MAI_GO:
        {
            LONG Initial, Increment, TargetCount;

            TargetCount = MSData->TargetCount;
            TargetCount = TargetCount >= 3 ? 4 : TargetCount;

            Initial = MSData->ChrStatus[BattleStatusFinal].InitialHP;
            Increment = MSData->ChrStatus[BattleStatusFinal].MaximumHP;

            if (TargetCount != 4)
                Increment = Increment / 4 * TargetCount;

            if (Initial >= Increment)
                return;

            MSData->ChrStatus[BattleStatusFinal].InitialHP = Increment;
            Increment -= Initial;

            UpdateHP(MSData, Increment, Initial);
        }
        break;

        case AS_8D_FUNCTION_AVATAR:
            HandleAvatar(MSData, Parameter);
            break;
    }
}

VOID CBattle::HandleAvatar(PMONSTER_STATUS MSData, PAS_8D_PARAM Parameter)
{
    ULONG           MSFileIndex, CharPosition;
    COORD           TargetPos;
    PCRAFT_AI_INFO  AIInfo;
    MONSTER_STATUS  AvatarBackup;
    BattleCtrlData  CtrlDataBackup;

    if (MSData->SelectedActionType != ACTION_CRAFT)
        return;

    MSFileIndex = Parameter->Param[0];
    if (MSFileIndex == 0)
        return;

    CharPosition = FindEmptyPosition(FLAG_OFF(MSData->State, CHR_FLAG_PARTY));
    if (CharPosition == -1)
        return;

    TEB_ACTIVE_FRAME Frame(FIND_EMPTY_POSITION_FILTER);

    Frame.Data = CharPosition;
    Frame.Push();

    AIInfo = &MSData->CraftAiInfo[MSData->CurrentAiIndex];
    AvatarBackup = GetMonsterStatus()[AVATAR_CHR_POSITION];
    CtrlDataBackup = this->CtrlData[AVATAR_CHR_POSITION];

    LOOP_ONCE
    {
        TargetPos = MSData->SelectedTargetPos;

        GetMonsterStatus()[AVATAR_CHR_POSITION].State = MSData->State;
        CLEAR_FLAG(this->CtrlData[AVATAR_CHR_POSITION].Flags, 0x80);

        //if (this->LoadMSData(MSFileIndex, AVATAR_CHR_POSITION) == FALSE)
        //    break;

        if (this->CloneMSData(MSData, MSData->CurrentCraftIndex, AIInfo) == FALSE)
            break;

        MSData->SelectedTargetPos = TargetPos;

        this->ResetCtrlData(CharPosition);
        this->ResetMSData(CharPosition);
        if (this->LoadMSData(MSFileIndex, CharPosition) == FALSE)
            break;

        this->SummonX = TargetPos.X;
        this->SummonY = TargetPos.Y;

        this->CtrlData[CharPosition].PositionData.X = TargetPos.X;
        this->CtrlData[CharPosition].PositionData.Y = TargetPos.Y;

        GetMonsterStatus()[CharPosition].State = MSData->State;

        //MSData->Target[0] = CharPosition;
        //MSData->TargetCount = 1;

        //MSData = GetMonsterStatus() + CharPosition;
        //UpdateHP(MSData, 0, MSData->ChrStatus[BattleStatusFinal].InitialHP);
    }

    GetMonsterStatus()[AVATAR_CHR_POSITION] = AvatarBackup;
    this->CtrlData[AVATAR_CHR_POSITION] = CtrlDataBackup;
}

ULONG CBattle::FindEmptyPosition(BOOL FindEnemyOnly /* = FALSE */)
{
    ULONG_PTR           Index, ValidPosition;
    PMONSTER_STATUS     MSData;
    PTEB_ACTIVE_FRAME   Frame;

    Frame = FindThreadFrame(FIND_EMPTY_POSITION_FILTER);
    if (Frame != nullptr)
        return Frame->Data;

    Index           = FindEnemyOnly ? 8 : 0;
    MSData          = this->GetMonsterStatus() + Index;
    ValidPosition   = (1 << 0) | (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) |
                      (1 << 8) | (1 << 9) | (1 << 0xA) | (1 << 0xB) | (1 << 0xC) | (1 << 0xD) | (1 << 0xE) | (1 << 0xF);

    if (FindEnemyOnly)
        ValidPosition = 0xFF00;

    for (; Index != MAXIMUM_CHR_NUMBER_IN_BATTLE; ++MSData, ++Index)
    {
        if (FLAG_ON(MSData->State, CHR_FLAG_EMPTY) && FLAG_ON(ValidPosition, 1 << Index))
            return Index;
    }

    return -1;
}

BOOL CBattle::IsAvatarLoaded(ULONG AvatarIndex)
{
    if (FindThreadFrame(FIND_EMPTY_POSITION_FILTER) != nullptr)
        return TRUE;

    PMONSTER_STATUS MSData;

    MSData = this->GetMonsterStatus() + AvatarIndex + 0x14;
    if (FLAG_ON(MSData->State, CHR_FLAG_EMPTY))
        return FALSE;

    return FLAG_OFF(*(PBYTE)PtrAdd(this, 0x7C8 + AvatarIndex * 0x31C), 0x80);     // ??
}

NAKED VOID CBattle::NakedNoResistConditionUp()
{
    enum
    {
        Conditions =    CraftConditions::StrUp |
                        CraftConditions::DefUp |
                        CraftConditions::AtsUp |
                        CraftConditions::AdfUp |
                        CraftConditions::DexUp |
                        CraftConditions::AglUp |
                        CraftConditions::MovUp |
                        CraftConditions::SpdUp,
    };

    INLINE_ASM
    {
        mov     edx, [ebp-0x15C];
        test    edx, Conditions;
        je      _RET2;

        and     ecx, edx;
        je      _RET;

        mov     eax, [ebp + 0x18];
        and     eax, 1 << 15;

_RET:
        ret;

_RET2:
        and     ecx, edx;
        ret;

    }
}

VOID FASTCALL FindReplaceChr(PMONSTER_STATUS MSData, PULONG RandomChrIndex)
{
    if (!MSData->IsChrEnemy(FALSE))
        return;

    FOR_EACH(RandomChrIndex, RandomChrIndex, 8)
    {
        *RandomChrIndex += 8;
    }
}

NAKED VOID CBattle::NakedFindReplaceChr()
{
    INLINE_ASM
    {
        mov     dword ptr [ebp - 24h], 0;
        mov     ecx, [ebp + 8h];
        lea     edx, [ebp - 70h];
        call    FindReplaceChr
        ret;
    }
}

ULONG_PTR FASTCALL CheckPartyCraftTargetBits(PMONSTER_STATUS MSData, PCRAFT_INFO CraftInfo)
{
    return (-FLAG_ON(CraftInfo->Target, CraftInfoTargets::OtherSide) & CHR_FLAG_ENEMY) | (-FLAG_ON(CraftInfo->Target, CraftInfoTargets::SelfSide) & CHR_FLAG_PARTY);
}

NAKED VOID CBattle::NakedCheckCraftTargetBits()
{
    INLINE_ASM
    {
        mov     ecx, [ebp - 044h];
        mov     edx, [ebp - 12Ch];
        call    CheckPartyCraftTargetBits
        mov     [ebp - 0CCh], eax;
        ret;
    }
}

VOID THISCALL CBattle::GetConditionIconPosByIndex(Gdiplus::PointF *Position, PMS_EFFECT_INFO EffectInfo, ULONG_PTR ConditionIndex)
{
    static BYTE PositionMap[] =
    {
        0x00,       // 0x00
        0xD0,       // 0x01
        0xD1,       // 0x02
        0xD2,       // 0x03
        0xD3,       // 0x04
        0xE6,       // 0x05
        0xE7,       // 0x06
        0xE8,       // 0x07
        0xE9,       // 0x08
        0xEA,       // 0x09
        0xEB,       // 0x0A
        0xB8,       // 0x0B
        0x00,       // 0x0C
        0xFB,       // 0x0D
        0xFC,       // 0x0E
        0xFA,       // 0x0F
        0xEE,       // 0x10
        0xF1,       // 0x11
        0xF3,       // 0x12
        0xE3,       // 0x13
        0xF7,       // 0x14
        0xE5,       // 0x15
        0xF9,       // 0x16
        0xE1,       // 0x17
        0xF5,       // 0x18
        0xB7,       // 0x19
        0xB6,       // 0x1A
        0xED,       // 0x1B
        0xB9,       // 0x1C
        0x00,       // 0x1D
        0xBA,       // 0x1E
        0xFD,       // 0x1F
        0x00,       // 0x20
    };

    if (ConditionIndex == countof(PositionMap))
    {
        Position->X = 64;
        Position->Y = 208;

        return;
    }
    else if (ConditionIndex > countof(PositionMap))
    {
        Position->X = 0;
        Position->Y = 0;

        return;
    }

    Position->X = (PositionMap[ConditionIndex] & 0x0F) * 16;
    Position->Y = ((PositionMap[ConditionIndex] & 0xF0) >> 4) * 16;

    if (EffectInfo != nullptr && EffectInfo->ConditionRate > 0 && FLAG_ON(EffectInfo->ConditionFlags, 0xFF0000))
    {
        Position->X -= 16;
    }
}

BOOL THISCALL CBattle::IsTargetCraftReflect(PMONSTER_STATUS Self, PMONSTER_STATUS Target, ULONG_PTR ActionType)
{
    BOOL    Success, CanRefect;
    USHORT  Orbment;

    CanRefect = FindEffectInfoByCondition(Target, CraftConditions::CraftReflect) != nullptr;

    if (CanRefect)
    {
        Orbment = 0xCD;
        Swap(Target->Orbment[0], Orbment);
    }

    Success = (this->*StubIsTargetCraftReflect)(Self, Target, ActionType);

    if (CanRefect)
        Swap(Target->Orbment[0], Orbment);

    return Success;
}

VOID THISCALL CBattle::OnSetChrConditionFlag(PMONSTER_STATUS MSData, ULONG Param2, ULONG ConditionFlag, USHORT Param4, USHORT Param5)
{
    PMS_EFFECT_INFO EffectInfo;

    (this->*StubOnSetChrConditionFlag)(MSData, Param2, ConditionFlag, Param4, Param5);

    if (ConditionFlag != CraftConditions::CraftReflect)
        return;

    ShowConditionText(MSData, "CRAFT REFLECT");

    FOR_EACH_ARRAY(EffectInfo, MSData->EffectInfo)
    {
        if (EffectInfo->ConditionFlags == 0)
            break;
    }

    --EffectInfo;
    if (FLAG_OFF(EffectInfo->ConditionFlags, ConditionFlag))
        return;

    if (EffectInfo->ATLeft == 9999)
        return;

    EffectInfo->CounterType = EffectInfo->CounterTypes::ByTimes;
}

BOOL FASTCALL CBattle::UpdateCraftReflectLeftTime(BOOL CanNotReflect, PMONSTER_STATUS MSData)
{
    if (!CanNotReflect)
        UpdateEffectLeftTime(MSData, 0, MS_EFFECT_INFO::CounterTypes::ByTimes, CraftConditions::CraftReflect);

    return CanNotReflect;
}

NAKED VOID CBattle::NakedUpdateCraftReflectLeftTime()
{
    INLINE_ASM
    {
        push    [ebp - 020h];
        mov     ecx, [ebp - 08h];
        movzx   edx, al;
        call    UpdateCraftReflectLeftTime
        test    eax, eax;
        ret;
    }
}

/************************************************************************
  EDAO
************************************************************************/

NAKED VOID EDAO::NakedGetChrSBreak()
{
    INLINE_ASM
    {
        mov     ecx, eax;
        jmp     EDAO::GetChrSBreak;
    }
}

VOID FASTCALL EDAO::GetChrSBreak(PMONSTER_STATUS MSData)
{
    PCRAFT_AI_INFO Craft;

    if (!IsCustomChar(MSData->CharID))
    {
        MSData->CurrentCraftIndex = GetSBreakList()[MSData->CharID];
        return;
    }

    Craft = MSData->SCraftAiInfo;
    for (ULONG_PTR Count = countof(MSData->SCraftAiInfo); Count; ++Craft, --Count)
    {
        if (Craft->CraftIndex == 0)
            break;
    }

    //Craft = Craft == MSData->SCraftAiInfo ? Craft : (Craft - 1);
    Craft = PtrSub(Craft, ((Craft == MSData->SCraftAiInfo) - 1) & sizeof(*Craft));

    MSData->SelectedCraft.AriaActionIndex   = Craft->AriaActionIndex;
    MSData->SelectedCraft.ActionIndex       = Craft->ActionIndex;
    MSData->CurrentCraftIndex               = Craft->CraftIndex;
}

/************************************************************************
  CGlobal
************************************************************************/

PCRAFT_INFO CGlobal::GetMagicData(USHORT MagicId)
{
    if (MagicId < MINIMUM_CUSTOM_CRAFT_INDEX)
        return (this->*StubGetMagicData)(MagicId);

    CBattle*        Battle;
    PMONSTER_STATUS MSData;

    Battle = GetEDAO()->GetBattle();

    MSData = &Battle->GetMonsterStatus()[Battle->GetCurrentChrIndex()];

    return &MSData->CraftInfo[MagicId - MINIMUM_CUSTOM_CRAFT_INDEX];
}

PCSTR CGlobal::GetMagicDescription(USHORT MagicId)
{
    if (MagicId < MINIMUM_CUSTOM_CRAFT_INDEX)
        return (this->*StubGetMagicDescription)(MagicId);

    CBattle*        Battle;
    PMONSTER_STATUS MSData;

    Battle = GetEDAO()->GetBattle();

    MSData = &Battle->GetMonsterStatus()[Battle->GetCurrentChrIndex()];

    return MSData->CraftDescription[MagicId - MINIMUM_CUSTOM_CRAFT_INDEX].Description;
}

PBYTE CGlobal::GetMagicQueryTable(USHORT MagicId)
{
    if (MagicId < MINIMUM_CUSTOM_CRAFT_INDEX)
        return (this->*StubGetMagicQueryTable)(MagicId);

    static BYTE StaticMagicQueryTable[7] = { /* 233, 233, 233, 233, 233, 233, 233, 233 */ };

    return StaticMagicQueryTable;
}

PBYTE THISCALL CGlobal::FixWeaponShapeAndRange(USHORT ItemId)
{
    PMONSTER_STATUS MSData;

    AllocStack(16);

    MSData = *(PMONSTER_STATUS *)PtrAdd(*(PVOID *)PtrSub(_AddressOfReturnAddress(), sizeof(PVOID)), 8);

    if (IsCustomChar(MSData->CharID))
    {
        ItemId = 0;
        MSData->ChrStatus[BattleStatusRaw].RNG = MSData->ChrStatus[BattleStatusFinal].RNG;
    }

    return (this->*StubFixWeaponShapeAndRange)(ItemId);
}

/************************************************************************
  info box
************************************************************************/

VOID THISCALL CBattleInfoBox::SetMonsterInfoBoxSize(LONG X, LONG Y, LONG Width, LONG Height)
{
    TYPE_OF(&CBattleInfoBox::SetMonsterInfoBoxSize) StubSetBoxSize;

    *(PVOID *)&StubSetBoxSize = (PVOID)0x67302C;

    return (this->*StubSetBoxSize)(X, Y, 120, Height);
}

VOID THISCALL CBattleInfoBox::DrawMonsterStatus()
{
    if (GetBattle()->GetCurrentTargetIndex() > MAXIMUM_CHR_NUMBER_IN_BATTLE ||
        GetBattle()->GetCurrentTargetIndex() < 0)
    {
        return;
    }

    BOOL                ShowInfo, ShowByOrbment;
    ULONG_PTR           BackgroundColor;
    MONSTER_INFO_FLAGS  Flags;
    PCOORD              UpperLeft;
    RECT                Rect;
    PMONSTER_STATUS     MSData;

    MSData = GetBattle()->GetMonsterStatus() + GetBattle()->GetCurrentTargetIndex();

    if (!IsTargetEnemy() || MSData->MSFileIndex == 0x30090011)
    {
        SetTargetIsEnemy(TRUE);
        SetMonsterInfoFlags(~0u);
    }

    (this->*StubDrawMonsterStatus)();

    Flags = GetMonsterInfoFlags();
    ShowInfo = Flags.AllValid();
    ShowByOrbment = !ShowInfo && Flags.IsShowByOrbment();
    ShowInfo = ShowInfo || ShowByOrbment;

    UpperLeft = GetUpperLeftCoord();

    RECT debug = { 284, 12, 128, 100 };

    Rect.left   = UpperLeft->X + debug.left;
    Rect.top    = UpperLeft->Y + debug.top;
    Rect.right  = Rect.left + debug.right;
    Rect.bottom = Rect.top + debug.bottom;

    BackgroundColor = (GetBackgroundColor() & 0xA0000000) | 0x00101020;

    GetEDAO()->DrawRectangle(Rect.left, Rect.top, Rect.right, Rect.bottom, BackgroundColor, BackgroundColor);

    typedef struct
    {
        PCSTR   Text;
        LONG    Value;

        ULONG_PTR (*Format)(PMONSTER_STATUS MSData, PSTR Buffer);

    } STATUS_ENTRY;

    STATUS_ENTRY *Entry, Status[] =
    {
        { "HP:", 0, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { ULONG Current = MSData->ChrStatus[BattleStatusFinal].InitialHP, Maximum = MSData->ChrStatus[BattleStatusFinal].MaximumHP; return sprintf(Buffer, "%d/%d %d", Current, Maximum, Maximum == 0 ? 0 :(Current * 100 / Maximum)); }  },
        { "EP:", 0, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { return sprintf(Buffer, "%d/%d", MSData->ChrStatus[BattleStatusFinal].InitialEP, MSData->ChrStatus[BattleStatusFinal].MaximumEP); }  },
        { "CP:", 0, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { return sprintf(Buffer, "%d/%d", MSData->ChrStatus[BattleStatusFinal].InitialCP, MSData->ChrStatus[BattleStatusFinal].MaximumCP); }  },

        { "STR:", MSData->ChrStatus[BattleStatusFinal].STR },
        { "DEF:", MSData->ChrStatus[BattleStatusFinal].DEF },
        { "ATS:", MSData->ChrStatus[BattleStatusFinal].ATS },
        { "ADF:", MSData->ChrStatus[BattleStatusFinal].ADF },
        { "DEX:", MSData->ChrStatus[BattleStatusFinal].DEX, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { return sprintf(Buffer, "%-3d %-2d", MSData->ChrStatus[BattleStatusFinal].DEX, MSData->ChrStatus[BattleStatusFinal].DEXRate); } },
        { "AGL:", MSData->ChrStatus[BattleStatusFinal].AGL, [](PMONSTER_STATUS MSData, PSTR Buffer) -> ULONG_PTR { return sprintf(Buffer, "%-3d %-2d", MSData->ChrStatus[BattleStatusFinal].AGL, MSData->ChrStatus[BattleStatusFinal].AGLRate); } },
        { "MOV:", MSData->ChrStatus[BattleStatusFinal].MOV },
        { "SPD:", MSData->ChrStatus[BattleStatusFinal].SPD },
        { "RNG:", MSData->ChrStatus[BattleStatusFinal].RNG },
    };

    CHAR        Buffer[0x200];
    LONG_PTR    X, Y, ValueX, ValueY, BoxWidth;
    ULONG_PTR   ValueColor;
    EDAO*       edao;

    POINT debug2 = { -11, -14 };

    edao = GetEDAO();

    BoxWidth = Rect.right - Rect.left;

    X = Rect.left - UpperLeft->X + debug2.x;
    Y = Rect.top - UpperLeft->Y + debug2.y;

    ValueY = Rect.top - UpperLeft->Y + 24;
    ValueColor = (ShowByOrbment ? 0xFF8020 : 0xFFFFFF) | (GetBackgroundColor() & 0xFF000000);

    FOR_EACH(Entry, Status, countof(Status))
    {
        ULONG_PTR Length;

        DrawSimpleText(X, Y, Entry->Text, COLOR_GOLD);

        if (ShowInfo)
        {
            Length = Entry->Format == nullptr ? sprintf(Buffer, "%d", Entry->Value) : Entry->Format(MSData, Buffer);
            edao->DrawNumber(X + 69, ValueY, Buffer, ValueColor);
            if (Entry == Status)
            {
                ULONG Color = ShowByOrbment ? COLOR_RED : COLOR_WHITE;
                ULONG PercentLength;

                PercentLength = 0;
                while (Buffer[Length - 1] != ' ')
                {
                    --Length;
                    ++PercentLength;
                }

                Length *= 6;
                PercentLength *= 6;

                DrawSimpleText(X + Length + 19, Y, "(", Color);
                DrawSimpleText(X + Length + 26 + PercentLength, Y, "%", Color);
                DrawSimpleText(X + Length + 26 + PercentLength + 6, Y, ")", Color);
            }
        }
        else
        {
            DrawSimpleText(X + 26, Y, "?", COLOR_WHITE);
        }

        Y += 13;
        ValueY += 13;
    }
}

/************************************************************************
  battle tweak
************************************************************************/

LONG CDECL CBattle::FormatBattleChrAT(PSTR Buffer, PCSTR Format, LONG Index, LONG No, LONG IcoAT, LONG ObjAT, LONG Pri)
{
    return sprintf(Buffer, "%d", IcoAT);
}

LONG CDECL CBattle::ShowSkipCraftAnimeButton(...)
{
    AllocStack(16);

    CBattle *Battle;

    Battle = *(CBattle **)(*(PULONG_PTR)PtrSub(_AddressOfReturnAddress(), sizeof(PVOID)) - 0xC);
    Battle->ShowSkipAnimeButton();

    return 0;
}


/************************************************************************
  at bar
************************************************************************/

PAT_BAR_ENTRY THISCALL CBattleATBar::LookupReplaceAtBarEntry(PMONSTER_STATUS MSData, BOOL IsFirst)
{
    PAT_BAR_ENTRY   FirstEntry, *Entry;
    PMONSTER_STATUS NewMSData;

    AllocStack(16);

    NewMSData = *(PMONSTER_STATUS *)(*(PULONG_PTR)PtrSub(_AddressOfReturnAddress(), sizeof(PVOID)) - 0x44);

    FirstEntry = nullptr;
    FOR_EACH(Entry, EntryPointer, countof(EntryPointer))
    {
        if (!FLAG_ON(Entry[0]->Flags, 0x20))
            continue;

        if (Entry[0]->MSData != MSData)
            continue;

        if (FirstEntry == nullptr)
            FirstEntry = *Entry;

        Entry[0]->MSData = NewMSData;
    }

    return FirstEntry;
}
