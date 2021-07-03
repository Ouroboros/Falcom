#pragma comment(lib, "gdiplus.lib")

#include "edao.h"

/************************************************************************
  EDAO
************************************************************************/

BOOL EDAO::CheckItemEquipped(ULONG ItemId, PULONG EquippedIndex)
{
    switch (ItemId)
    {
        case 0xB7:  // ú—Ä¿
        case 0xB8:  // ÌìÑÛ
        case 0xBB:  // Ì½Öª
            if (EquippedIndex != nullptr)
                *EquippedIndex = 0;

            return TRUE;
    }

    return (this->*StubCheckItemEquipped)(ItemId, EquippedIndex);
}

enum
{
    CHR_ID_LAZY             = 4,
    CHR_ID_YIN              = 5,

    CHR_ID_LAZY_KNIGHT      = 0x1F,
    CHR_ID_RIXIA            = 0x20,

    CHR_ID_LAZY_KNIGHT_NULL = 0x35B,
    CHR_ID_RIXIA_NULL       = 0x35C,
};

LONG CDECL EDAO::GetCampImage(PSTR Buffer, PCSTR Format, LONG ChrId)
{
    CHAR FullPath[MAX_NTPATH];

    sprintf(FullPath, "data/campimg/chrimg%02d.itp", ChrId);
    if (!AoIsFileExist(FullPath))
        ChrId = 9999;

    return sprintf(Buffer, Format, ChrId);
}

LONG CDECL EDAO::GetBattleFace(PSTR Buffer, PCSTR Format, PCSTR DataPath, LONG ChrId)
{
    LONG_PTR Length;

    Length = sprintf(Buffer, Format, DataPath, ChrId);
    if (!AoIsFileExist(Buffer))
        Length = sprintf(Buffer, Format, DataPath, 9999);

    return Length;
}

LONG CDECL EDAO::GetFieldAttackChr(PSTR Buffer, PCSTR Format, LONG ChrId)
{
    CHAR FullPath[MAX_NTPATH];

    sprintf(FullPath, "data/system/fachr%03d._bn", ChrId);
    if (!AoIsFileExist(FullPath))
        ChrId = 999;

    return sprintf(Buffer, Format, ChrId);
}

LONG FASTCALL EDAO::GetCFace(ULONG ChrId)
{
    ULONG PartyId;

    PartyId = GetSaveData()->GetPartyChipMap()[ChrId];
    if (PartyId >= MINIMUM_CUSTOM_CHAR_ID)
    {
        CHAR FaceFile[MAX_NTPATH];

        sprintf(FaceFile, "./data/campimg/cface%02d.itp", PartyId);
        if (AoIsFileExist(FaceFile))
            return PartyId;
    }

    switch (ChrId)
    {
        case CHR_ID_LAZY:
        case CHR_ID_LAZY_KNIGHT_NULL:
            return GetSaveData()->IsLazyKnight() ? CHR_ID_LAZY_KNIGHT : ChrId;

        case CHR_ID_YIN:
        case CHR_ID_RIXIA_NULL:
            return GetSaveData()->IsYinRixia() ? CHR_ID_RIXIA : ChrId;
    }

    return ChrId;
}

LONG FASTCALL EDAO::GetStatusIcon(ULONG ChrId)
{
    INLINE_ASM mov ChrId, eax;

    ULONG PartyId;

    switch (ChrId)
    {
        case CHR_ID_YIN:
            break;

        default:
            return ChrId;
    }

    PartyId = GetSaveData()->GetPartyChipMap()[ChrId];
    if (PartyId == CHR_ID_RIXIA)
        return 0xC;

    switch (ChrId)
    {
        case CHR_ID_YIN:
            return GetSaveData()->IsYinRixia() ? 0xC : ChrId;
    }

    return ChrId;
}

LONG FASTCALL EDAO::GetLeaderChangeVoice(ULONG PartyId)
{
    ULONG ChrId;

    ChrId = GetSaveData()->GetPartyList()[1];

    switch (ChrId)
    {
        case CHR_ID_YIN:
            break;

        default:
            return ChrId;
    }

    if (PartyId == CHR_ID_RIXIA)
        return 0xB;

    switch (ChrId)
    {
        case CHR_ID_YIN:
            return GetSaveData()->IsYinRixia() ? 0xB : ChrId;
    }

    return ChrId;
}

/************************************************************************
  CActor
************************************************************************/

ULONG FASTCALL CSSaveData::GetTeamAttackMemberId(ULONG ChrId)
{
    switch (ChrId)
    {
        case CHR_ID_LAZY:
        case CHR_ID_LAZY_KNIGHT_NULL:
            return IsLazyKnight() ? CHR_ID_LAZY_KNIGHT : ChrId;

        case CHR_ID_YIN:
        case CHR_ID_RIXIA_NULL:
            return IsYinRixia() ? CHR_ID_RIXIA : ChrId;
    }

    return ChrId;
}

/************************************************************************
  CScript
************************************************************************/

NAKED VOID CScript::NakedInheritSaveData()
{
    INLINE_ASM
    {
        mov     dword ptr [eax + 82BB4h], 0;
        lea     edx, dword ptr [ebp - 0x26454 + 0x1B008];
        mov     ecx, [ebp - 0Ch];
        jmp     CScript::InheritSaveData
    }
}

VOID FASTCALL CScript::InheritSaveData(PBYTE ScenarioFlags)
{
    ULONG_PTR CustomOffset[] =
    {
        0x212,
    };

    PULONG_PTR Offset;

    FOR_EACH(Offset, CustomOffset, countof(CustomOffset))
    {
        *(PBYTE)PtrAdd(this, 0x9C + *Offset) = ScenarioFlags[*Offset];
    }
}

BOOL THISCALL CScript::ScpSaveRestoreParty(PSCENA_ENV_BLOCK Block)
{
    BOOL   Result, NeedRefreshFA;
    USHORT Chr[8];

    enum { Save = 1, Restore = 2 };

    NeedRefreshFA = GetScenaTable()[Block->ScenaIndex][Block->CurrentOffset + 1] == Restore &&
                    RtlCompareMemory(GetSaveData()->GetPartyListSaved(), GetSaveData()->GetPartyList(), sizeof(Chr)) != sizeof(Chr);

    Result = (this->*StubScpSaveRestoreParty)(Block);

    if (NeedRefreshFA)
        GetEDAO()->LoadFieldAttackData();

    return Result;
}

/************************************************************************
  misc
************************************************************************/

VOID FASTCALL LoadSaveDataThumbFast(Gdiplus::Bitmap *bitmap, PBYTE RGBBuffer, PBYTE AlphaBuffer, LONG_PTR Stride)
{
    using namespace Gdiplus;

    PBYTE       RawBuffer;
    LONG_PTR    Width, Height;
    COLORREF    Color;
    BitmapData  bitmapData;

    Width = bitmap->GetWidth();
    Height = bitmap->GetHeight();

    Rect rect(0, 0, Width, Height);

    bitmap->LockBits(&rect, ImageLockModeRead, PixelFormat32bppARGB, &bitmapData);

    RawBuffer = (PBYTE)bitmapData.Scan0;
    Stride *= 3;

    for (LONG_PTR h = Height; h; --h)
    {
        PBYTE buf, rgb, alpha;

        buf = RawBuffer;
        rgb = RGBBuffer;
        alpha = AlphaBuffer;

        for (LONG_PTR w = Width; w; --w)
        {
            Color = *(LPCOLORREF)buf;

            rgb[0] = GetRValue(Color);
            rgb[1] = GetGValue(Color);
            rgb[2] = GetBValue(Color);

            alpha[0] = Color >> 24;
            alpha[1] = Color >> 24;
            alpha[2] = Color >> 24;

            buf     += 4;
            rgb     += 3;
            alpha   += 3;
        }

        RawBuffer   += bitmapData.Stride;
        RGBBuffer   += Stride;
        AlphaBuffer += Stride;
    }

    bitmap->UnlockBits(&bitmapData);
}

NAKED VOID EDAO::NakedLoadSaveDataThumb()
{
    INLINE_ASM
    {
        mov     edx, dword ptr [ebp - 0x350];
        push    dword ptr [ebp - 0x234];
        push    dword ptr [ebp - 0x35C];

        call    LoadSaveDataThumbFast
        or      eax, -1;
        ret;
    }
}

VOID FASTCALL SetSaveDataScrollStep(ULONG_PTR RetryCount)
{
    PBOOLEAN ScrollUp10             = (PBOOLEAN)0xDCFA15;
    PBOOLEAN ScrollDown10           = (PBOOLEAN)0xDCFA16;

    PBOOLEAN ScrollUp100            = (PBOOLEAN)0xDCFA1F;
    PBOOLEAN ScrollDown100          = (PBOOLEAN)0xDCFA20;

    PLONG   SaveDataToReadUp        = (PLONG)0xDCF9F8;
    PLONG   SaveDataToReadDown      = (PLONG)0xDCF9F4;

    PLONG   CurrentSaveDataIndex    = (PLONG)0xDCDFD0;
    PLONG   MaximumSaveDataIndex    = (PLONG)0xDCDFFC;

    PLONG   KeyPressCount           = (PLONG)0xDCDFDC;

    LONG MaximumSaveDataToRead = 10;
    LONG Extra = 0;

    static ULONG64 PressTimestamp;

    LOOP_ONCE
    {
        if (*ScrollUp100 | *ScrollUp10)
        {
            if (*CurrentSaveDataIndex == 0)
                continue;

            switch (*SaveDataToReadUp)
            {
                case 10:
                case 100:
                    break;

                default:
                    continue;
            }

            PressTimestamp = NtGetTickCount();

            *CurrentSaveDataIndex = ML_MAX(*CurrentSaveDataIndex - *SaveDataToReadUp, 0) + MaximumSaveDataToRead + Extra;
            *SaveDataToReadUp = MaximumSaveDataToRead + Extra;
            continue;
        }

        if (*ScrollDown100 | *ScrollDown10)
        {
            if (*CurrentSaveDataIndex == *MaximumSaveDataIndex - 1)
                continue;

            switch (*SaveDataToReadDown)
            {
                case 10:
                case 100:
                    break;

                default:
                    continue;
            }

            PressTimestamp = NtGetTickCount();

            *CurrentSaveDataIndex = ML_MIN(*CurrentSaveDataIndex + *SaveDataToReadDown, *MaximumSaveDataIndex - 1) - MaximumSaveDataToRead - Extra;
            *SaveDataToReadDown = MaximumSaveDataToRead + Extra;
            continue;
        }

        return;
    }

    if (RetryCount == 0 && NtGetTickCount() - PressTimestamp > 150)
        *KeyPressCount = 0;
}

NAKED VOID EDAO::NakedSetSaveDataScrollStep()
{
    INLINE_ASM
    {
        mov     dword ptr [ebp-0x174], eax;
        mov     ecx, dword ptr [ebp-0x24]
        jmp     SetSaveDataScrollStep
    }
}


/************************************************************************
  keyboard input
************************************************************************/

VOID HandleSingleKey(ULONG_PTR KeyCode, BOOL KeyPress)
{
    FLOAT   Delta;
    ULONG   Index;

    enum { X = 0, Y = 1, Z = 2, Z2 = 42 };
    enum
    {
        V = FIELD_OFFSET(CAMERA_INFO, Vertical),
        O = FIELD_OFFSET(CAMERA_INFO, Obliquity),
        H = FIELD_OFFSET(CAMERA_INFO, Horizon),
        D = FIELD_OFFSET(CAMERA_INFO, Distance),
    };

    switch (KeyPress)
    {
        case TRUE:
            switch (KeyCode)
            {
                case DIK_NUMPAD4:   Index = X; Delta = -.5f; goto CHANGE_CHR_COORD;
                case DIK_NUMPAD6:   Index = X; Delta = +.5f;  goto CHANGE_CHR_COORD;

                case DIK_NUMPAD2:   Index = Y; Delta = -.5f; goto CHANGE_CHR_COORD;
                case DIK_NUMPAD8:   Index = Y; Delta = +.5f;  goto CHANGE_CHR_COORD;

                case DIK_NUMPAD7:   Index = Z; Delta = +1.f;  goto CHANGE_CHR_COORD;
                case DIK_NUMPAD9:   Index = Z; Delta = -1.f;  goto CHANGE_CHR_COORD;

CHANGE_CHR_COORD:
                {
                    EDAO*   edao;
                    PFLOAT  Coord;

                    edao = EDAO::GlobalGetEDAO();
                    Coord = edao->GetChrCoord();

                    PtrAdd(Coord, 0x80)[Index] += Delta;
                    edao->UpdateChrCoord(*(PVOID *)PtrAdd(edao, 0x78F78));
                    break;
                }

                case DIK_INSERT:    Index = H; Delta = -1.f; goto CHANGE_CAMERA_DEGREE;
                case DIK_DELETE:    Index = H; Delta = +1.f; goto CHANGE_CAMERA_DEGREE;

                case DIK_HOME:      Index = V; Delta = +1.f; goto CHANGE_CAMERA_DEGREE;
                case DIK_END:       Index = V; Delta = -1.f; goto CHANGE_CAMERA_DEGREE;

                case DIK_PRIOR:     Index = O; Delta = -1.f; goto CHANGE_CAMERA_DEGREE;
                case DIK_NEXT:      Index = O; Delta = +1.f; goto CHANGE_CAMERA_DEGREE;

                case DIK_NUMPAD1:   Index = D; Delta = -1.f; goto CHANGE_CAMERA_DEGREE;
                case DIK_NUMPAD3:   Index = D; Delta = +1.f; goto CHANGE_CAMERA_DEGREE;

CHANGE_CAMERA_DEGREE:

                    *(PFLOAT)PtrAdd(EDAO::GlobalGetEDAO()->GetScript()->GetCamera()->GetCameraInfo(), Index) += Delta;
                    break;

                case DIK_LCONTROL:
                case DIK_RCONTROL:
                {
                    CHAR            Buffer[0x200];
                    PFLOAT          Coord;
                    LONG            Integer, Decimal;
                    EDAO           *edao;

                    edao = EDAO::GlobalGetEDAO();
                    Coord = PtrAdd(edao->GetChrCoord(), 0x80);
                    if (Coord == (PFLOAT)0x80)
                        break;

                    Integer = Coord[X];
                    Decimal = (fabs(Coord[X]) - abs(Integer)) * 1000;
                    sprintf(Buffer, "X: %d.%d", Integer, Decimal);
                    edao->DrawText(Buffer, 0, 0, 8, -1, -1, -1);

                    Integer = Coord[Y];
                    Decimal = (fabs(Coord[Y]) - abs(Integer)) * 1000;
                    sprintf(Buffer, "Y: %d.%d", Integer, Decimal);
                    edao->DrawText(Buffer, 0, 15, 8, -1, -1, -1);

                    Integer = Coord[Z];
                    Decimal = (fabs(Coord[Z]) - abs(Integer)) * 1000;
                    sprintf(Buffer, "Z: %d.%d", Integer, Decimal);
                    edao->DrawText(Buffer, 0, 30, 8, -1, -1, -1);

                    break;
                }
            }
    }
}

VOID THISCALL CInput::HandleMainInterfaceInputState(PVOID Parameter1, CInput *Input, PVOID Parameter3)
{
    CHAR                    *Key, KeyState[0x100];
    HRESULT                 Result;
    LPDIRECTINPUTDEVICE8A   InputDevice;

    (this->*StubHandleMainInterfaceInputState)(Parameter1, Input, Parameter3);

    if (*(PCHAR)PtrAdd(EDAO::GlobalGetEDAO(), 0xA7071) != 1)
        return;

    InputDevice = Input->GetDInputDevice();
    if (InputDevice == nullptr)
        return;

    Result = InputDevice->GetDeviceState(sizeof(KeyState), KeyState);
    if (FAILED(Result))
        return;

#if D3D9_VER

    BYTE ShiftKeys[] =
    {
        DIK_LCONTROL,
        DIK_RCONTROL,
        DIK_LSHIFT,
        DIK_RSHIFT,
        DIK_LMENU,
        DIK_RMENU,
    };

    PBYTE ShiftKey;

    FOR_EACH_ARRAY(ShiftKey, ShiftKeys)
    {
        if (KeyState[*ShiftKey] < 0)
            break;
    }

    if (ShiftKey == &ShiftKeys[countof(ShiftKeys)])
        return;

#endif // d3d9v

    FOR_EACH_ARRAY(Key, KeyState)
    {
        if (*Key < 0)
            HandleSingleKey(Key - KeyState, TRUE);
    }
}
