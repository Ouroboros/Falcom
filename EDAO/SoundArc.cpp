#include "SoundArc.h"

#define HANDLE_CTRL(_ctrl_code, fn)   case (_ctrl_code): return fn(Parameter)


CSoundPlayer *g_Player;

HWND THISCALL CSoundPlayer::GetSoundControlWindow()
{
    if (g_Player == nullptr)
    {
        CSoundPlayer *Player;

        Player = new CSoundPlayer;
        if (Player == nullptr)
            return nullptr;

        if (NT_FAILED(Player->Initialize(*(HWND *)PtrAdd(this, 0xB0))))
        {
            delete Player;
            return nullptr;
        }

        g_Player = Player;
    }

    return SOUND_CONTROL_WINDOW;
}

NTSTATUS CSoundPlayer::Initialize(HWND GameWindow)
{
    static PSTR FunctionNames[] =
    {
        "IInit",
        "IRelease",
        "MixOpen",
        "MixClose",

        "IPlayFade",
        "IFadeOut",
        "IPlayFadeB",
        "IPlaySE",
        "IPlaySEB",
        "IPlayFadeEx",
        "IPlayFadeBEx",
        "IPlay",
        "IPlayB",
        "ILoadSE",
        "IFadeOutEx",
        "IPlayStop",
        "IVolFade",
        "IStopAllSE",
        "IStopSE",
        "IGetPos",
        "ISetSEVol",
        "ISetBGMVol",
        "ISetMem",
        "ISetListen",
        "ISetSEPos",
        "IGetSECountByName",
        "IStopSEByName",
        "ISetSeVolByName",
        "IGetSECountAll",
        "IStopSEByLabel",
        "ISetSEVolByLabel",
        "ISetSEPosByLabel",
        "IIsPlaySEByLabel",
    };

    PSTR*   Name;
    PVOID*  Function;

    m_Sound3D = Ldr::LoadDll(L".\\dll\\sound3d.dll");
    if (m_Sound3D == nullptr)
        return STATUS_NOT_FOUND;

    Function = &this->FunctionTable;

    FOR_EACH_ARRAY(Name, FunctionNames)
    {
        *Function++ = GetRoutineAddress(m_Sound3D, *Name);
    }

    this->IInit(GameWindow);
    this->MixOpen();

    return STATUS_SUCCESS;
}

LRESULT NTAPI CSoundPlayer::StaticDispatchCtrlCode(HWND Window, UINT Message, WPARAM wParam, LPARAM lParam)
{
    return Window == SOUND_CONTROL_WINDOW ?
            g_Player->DispatchCtrlCode(Message, wParam, lParam) :
            StubStaticDispatchCtrlCode(Window, Message, wParam, lParam);
}

LRESULT CSoundPlayer::DispatchCtrlCode(ULONG_PTR Message, ULONG_PTR CtrlCode, ULONG_PTR Parameter)
{
    switch (Message)
    {
        case WM_CONTROL_SOUND:
            if (CtrlCode < CTRL_MINIMUM)
            {
                m_UnknownF[CtrlCode] = Parameter;
                break;
            }

            //DebugPrint(L"%X", CtrlCode);

            switch (CtrlCode)
            {
                HANDLE_CTRL(CTRL_PLAY_FADE,                 PlayFade);
                HANDLE_CTRL(CTRL_PLAY_FADE_B,               PlayFadeB);
                HANDLE_CTRL(CTRL_PLAY_SE,                   PlaySE);
                HANDLE_CTRL(CTRL_PLAY_SE_B,                 PlaySEB);
                HANDLE_CTRL(CTRL_PLAY_FADE_EX,              PlayFadeEx);
                HANDLE_CTRL(CTRL_PLAY_FADE_B_EX,            PlayFadeBEx);
                HANDLE_CTRL(CTRL_PLAY,                      Play);
                HANDLE_CTRL(CTRL_PLAY_B,                    PlayB);
                HANDLE_CTRL(CTRL_LOAD_SE,                   LoadSe);
                HANDLE_CTRL(CTRL_FADE_OUT_EX,               FadeOutEx);
                HANDLE_CTRL(CTRL_PLAY_STOP,                 PlayStop);
                HANDLE_CTRL(CTRL_VOL_FADE,                  VolFade);
                HANDLE_CTRL(CTRL_STOP_ALL_SE,               StopAllSE);
                HANDLE_CTRL(CTRL_STOP_SE,                   StopSE);
                HANDLE_CTRL(CTRL_GET_POS,                   GetPos);
                HANDLE_CTRL(CTRL_SET_SE_VOL,                SetSeVol);
                HANDLE_CTRL(CTRL_SET_BGM_VOL,               SetBGMVol);
                HANDLE_CTRL(CTRL_SET_MEM,                   SetMem);
                HANDLE_CTRL(CTRL_SET_LISTEN,                SetListen);
                HANDLE_CTRL(CTRL_SET_SE_POS,                SetSEPos);
                HANDLE_CTRL(CTRL_GET_SE_COUNT_BY_NAME,      GetSECountByName);
                HANDLE_CTRL(CTRL_STOP_SE_BY_NAME,           StopSEByName);
                HANDLE_CTRL(CTRL_SET_SE_VOL_BY_NAME,        SetSEVolByName);
                HANDLE_CTRL(CTRL_GET_SE_COUNT_ALL,          GetSECountAll);
                HANDLE_CTRL(CTRL_UNKNOWN,                   Unknown);
                HANDLE_CTRL(CTRL_STOP_SE_BY_LABEL,          StopSEByLabel);
                HANDLE_CTRL(CTRL_SET_SE_VOL_BY_LABEL,       SetSEVolByLabel);
                HANDLE_CTRL(CTRL_SET_SE_POS_BY_LABEL,       SetSEPosByLabel);
                HANDLE_CTRL(CTRL_GET_SE_NAME_BY_LABEL,      GetSENameByLabel);
                HANDLE_CTRL(CTRL_IS_PLAY_SE_BY_LABEL,       IsPlaySEByLabel);
            }

            break;

        case WM_SET_SE_NAME:
        {
            PCOPYDATASTRUCT CopyDataStruct;

            CopyDataStruct = (PCOPYDATASTRUCT)Parameter;
            StrCopyA(m_SeName, (PCSTR)CopyDataStruct->lpData);

            DebugPrint(L"set se: %S\n", m_SeName);

            break;
        }

        case WM_CLOSE:
            SafeDeleteT(g_Player);
            break;
    }

    return 0;
}

/************************************************************************
  handler
************************************************************************/

LRESULT CSoundPlayer::PlayFade(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(6);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)m_SeName;
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];

    return this->IPlayFade();
}

LRESULT CSoundPlayer::FadeOut(ULONG_PTR Parameter)
{
    DebugPrint(L"FadeOut: %d", m_UnknownF[0]);

    return this->IFadeOut(m_UnknownF[0]);
}

LRESULT CSoundPlayer::PlayFadeB(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(6);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)m_SeName;
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];

    return this->IPlayFadeB();
}

LRESULT CSoundPlayer::PlaySE(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(11);

    if (m_UnknownF[4] != 0)
    {
        Arguments[0]            = (ULONG_PTR)m_SeName;
        Arguments[1]            = (ULONG_PTR)&m_UnknownF[1];
        Arguments[2]            = (ULONG_PTR)&m_UnknownF[2];
        Arguments[3]            = (ULONG_PTR)&m_UnknownF[3];
        Arguments[4]            = m_UnknownF[4];
        Arguments[5]            = m_UnknownF[0];
        *(PFLOAT)&Arguments[6]  = *(PFLOAT)&m_UnknownF[5];
        Arguments[7]            = m_UnknownF[6];
        *(PFLOAT)&Arguments[8]  = *(PFLOAT)&m_UnknownF[7];
        Arguments[9]            = m_UnknownF[8];
        *(PFLOAT)&Arguments[10] = *(PFLOAT)&m_UnknownF[9];
    }
    else
    {
        Arguments[0]            = (ULONG_PTR)m_SeName;
        Arguments[1]            = 0;
        Arguments[2]            = 0;
        Arguments[3]            = 0;
        Arguments[4]            = m_UnknownF[4];
        Arguments[5]            = m_UnknownF[0];
        *(PFLOAT)&Arguments[6]  = *(PFLOAT)&m_UnknownF[5];
        Arguments[7]            = m_UnknownF[6];
        *(PFLOAT)&Arguments[8]  = 0.f;
        Arguments[9]            = m_UnknownF[8];
        *(PFLOAT)&Arguments[10] = *(PFLOAT)&m_UnknownF[9];
    }

    return this->IPlaySE();
}

LRESULT CSoundPlayer::PlaySEB(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(11);

    if (m_UnknownF[4] != 0)
    {
        Arguments[0]            = (ULONG_PTR)m_SeName;
        Arguments[1]            = (ULONG_PTR)&m_UnknownF[1];
        Arguments[2]            = (ULONG_PTR)&m_UnknownF[2];
        Arguments[3]            = (ULONG_PTR)&m_UnknownF[3];
        Arguments[4]            = m_UnknownF[4];
        Arguments[5]            = m_UnknownF[0];
        *(PFLOAT)&Arguments[6]  = *(PFLOAT)&m_UnknownF[5];
        Arguments[7]            = m_UnknownF[6];
        *(PFLOAT)&Arguments[8]  = *(PFLOAT)&m_UnknownF[7];
        Arguments[9]            = m_UnknownF[8];
        *(PFLOAT)&Arguments[10] = *(PFLOAT)&m_UnknownF[9];
    }
    else
    {
        Arguments[0]            = (ULONG_PTR)m_SeName;
        Arguments[1]            = 0;
        Arguments[2]            = 0;
        Arguments[3]            = 0;
        Arguments[4]            = m_UnknownF[4];
        Arguments[5]            = m_UnknownF[0];
        *(PFLOAT)&Arguments[6]  = *(PFLOAT)&m_UnknownF[5];
        Arguments[7]            = m_UnknownF[6];
        *(PFLOAT)&Arguments[8]  = 0.f;
        Arguments[9]            = m_UnknownF[8];
        *(PFLOAT)&Arguments[10] = *(PFLOAT)&m_UnknownF[9];
    }

    return this->IPlaySEB();
}

LRESULT CSoundPlayer::PlayFadeEx(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(7);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)m_SeName;
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];
    Arguments[6] = m_UnknownF[5];

    return this->IPlayFadeEx();
}

LRESULT CSoundPlayer::PlayFadeBEx(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(7);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)m_SeName;
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];
    Arguments[6] = m_UnknownF[5];

    return this->IPlayFadeBEx();
}

LRESULT CSoundPlayer::Play(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(6);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)m_SeName;
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];

    return this->IPlay();
}

LRESULT CSoundPlayer::PlayB(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(6);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)m_SeName;
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];

    return this->IPlayB();
}

LRESULT CSoundPlayer::LoadSe(ULONG_PTR Parameter)
{
    return this->ILoadSE(m_SeName);
}

LRESULT CSoundPlayer::FadeOutEx(ULONG_PTR Parameter)
{
    LRESULT Result;
    ULONG_PTR Index, Time;

    Index   = m_UnknownF[0];
    Time    = m_UnknownF[1];

    DebugPrint(L"FadeOutEx: %d, %d", Index, Time);

    Result = this->IFadeOutEx(Index, Time);

    if (Time != 0)
    {
        m_FadeOutTime[Index] = Time;
        m_FadeOutTimeStamp[Index] = (ULONG)NtGetTickCount();
    }

    return Result;
}

LRESULT CSoundPlayer::PlayStop(ULONG_PTR Parameter)
{
    return this->IPlayStop(m_UnknownF[0]);
}

LRESULT CSoundPlayer::VolFade(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(3);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = m_UnknownF[1];
    Arguments[2] = m_UnknownF[2];

    return this->IVolFade();
}

LRESULT CSoundPlayer::StopAllSE(ULONG_PTR Parameter)
{
    return this->IStopAllSE();
}

LRESULT CSoundPlayer::StopSE(ULONG_PTR Parameter)
{
    return this->IStopSE(Parameter);
}

LRESULT CSoundPlayer::GetPos(ULONG_PTR Parameter)
{
    return this->IGetPos(Parameter);
}

LRESULT CSoundPlayer::SetSeVol(ULONG_PTR Parameter)
{
    return this->ISetSEVol(Parameter);
}

LRESULT CSoundPlayer::SetBGMVol(ULONG_PTR Parameter)
{
    ULONG_PTR TimeStamp, Elapsed;

    TimeStamp = NtGetTickCount();

    for (ULONG_PTR Index = 0; Index != MaxBuffer; ++Index)
    {
        if (m_FadeOutTimeStamp[Index] != 0)
        {
            Elapsed = TimeStamp - m_FadeOutTimeStamp[Index];

            DebugPrint(L"SetBGMVol(%d): %d, %d", Index, m_FadeOutTime[Index], Elapsed);

            if (Elapsed < m_FadeOutTime[Index])
                return TRUE;

            m_FadeOutTimeStamp[Index] = 0;
        }
    }

    return this->ISetBGMVol(Parameter);
}

LRESULT CSoundPlayer::SetMem(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(2);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = m_UnknownF[1];

    return this->ISetMem();
}

LRESULT CSoundPlayer::SetListen(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(10);

    Arguments[0] = m_UnknownF[9];
    Arguments[1] = m_UnknownF[0];
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];
    Arguments[4] = m_UnknownF[3];
    Arguments[5] = m_UnknownF[4];
    Arguments[6] = m_UnknownF[5];
    Arguments[7] = m_UnknownF[6];
    Arguments[8] = m_UnknownF[7];
    Arguments[9] = m_UnknownF[8];

    return this->ISetListen();
}

LRESULT CSoundPlayer::SetSEPos(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(7);

    Arguments[0] = m_UnknownF[0];
    Arguments[1] = (ULONG_PTR)&m_UnknownF[1];
    Arguments[2] = (ULONG_PTR)&m_UnknownF[2];
    Arguments[3] = (ULONG_PTR)&m_UnknownF[3];
    Arguments[4] = (ULONG_PTR)&m_UnknownF[4];
    Arguments[5] = (ULONG_PTR)&m_UnknownF[5];
    Arguments[6] = (ULONG_PTR)&m_UnknownF[6];

    return this->ISetSEPos();
}

LRESULT CSoundPlayer::GetSECountByName(ULONG_PTR Parameter)
{
    return this->IGetSECountByName(m_SeName);
}

LRESULT CSoundPlayer::StopSEByName(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(4);

    Arguments[0] = (ULONG_PTR)m_SeName;
    Arguments[1] = m_UnknownF[0];
    Arguments[2] = m_UnknownF[1];
    Arguments[3] = m_UnknownF[2];

    return this->IStopSEByName();
}

LRESULT CSoundPlayer::SetSEVolByName(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(2);

    Arguments[0]            = (ULONG_PTR)m_SeName;
    *(PFLOAT)&Arguments[1]  = *(PFLOAT)&m_UnknownF[0];

    return this->ISetSeVolByName();
}

LRESULT CSoundPlayer::GetSECountAll(ULONG_PTR Parameter)
{
    return this->IGetSECountAll();
}

LRESULT CSoundPlayer::Unknown(ULONG_PTR Parameter)
{
    return (m_UnknownF[0] & 0xFFFF0000) == 0x10000;
}

LRESULT CSoundPlayer::StopSEByLabel(ULONG_PTR Parameter)
{
    return this->IStopSEByLabel(Parameter);
}

LRESULT CSoundPlayer::SetSEVolByLabel(ULONG_PTR Parameter)
{
    return this->ISetSEVolByLabel(Parameter, m_UnknownF[0]);
}

LRESULT CSoundPlayer::SetSEPosByLabel(ULONG_PTR Parameter)
{
    PULONG_PTR Arguments;

    Arguments = AllocArgs(7);

    Arguments[0] = Parameter;
    Arguments[1] = (ULONG_PTR)&m_UnknownF[0];
    Arguments[2] = (ULONG_PTR)&m_UnknownF[1];
    Arguments[3] = (ULONG_PTR)&m_UnknownF[2];
    Arguments[4] = (ULONG_PTR)&m_UnknownF[3];
    Arguments[5] = (ULONG_PTR)&m_UnknownF[4];
    Arguments[6] = (ULONG_PTR)&m_UnknownF[5];

    return this->ISetSEPosByLabel();
}

LRESULT CSoundPlayer::GetSENameByLabel(ULONG_PTR Parameter)
{
    return 0;
}

LRESULT CSoundPlayer::IsPlaySEByLabel(ULONG_PTR Parameter)
{
    return this->IIsPlaySEByLabel(Parameter);
}
