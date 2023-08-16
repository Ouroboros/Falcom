#ifndef _SOUNDARC_H_857ceedf_b76c_4eaf_bead_f8a5b4e76f18_
#define _SOUNDARC_H_857ceedf_b76c_4eaf_bead_f8a5b4e76f18_

#include "edao.h"

#define SOUND_CONTROL_WINDOW    (HWND)0xFFEEDDCC

enum
{
    WM_CONTROL_SOUND                = WM_USER,
    WM_SET_SE_NAME                  = WM_COPYDATA,


    CTRL_MINIMUM                    = 0x200,

    CTRL_PLAY_FADE                  = 0x200,
    CTRL_PLAY_FADE_OUT              = 0x201,
    CTRL_PLAY_FADE_B                = 0x202,
    CTRL_PLAY_SE                    = 0x203,
    CTRL_PLAY_SE_B                  = 0x204,
    CTRL_PLAY_FADE_EX               = 0x205,
    CTRL_PLAY_FADE_B_EX             = 0x206,
    CTRL_PLAY                       = 0x207,
    CTRL_PLAY_B                     = 0x208,
    CTRL_LOAD_SE                    = 0x20D,
    CTRL_FADE_OUT_EX                = 0x212,
    CTRL_PLAY_STOP                  = 0x213,
    CTRL_VOL_FADE                   = 0x21C,
    CTRL_STOP_ALL_SE                = 0x221,
    CTRL_STOP_SE                    = 0x224,
    CTRL_GET_POS                    = 0x225,
    CTRL_SET_SE_VOL                 = 0x226,
    CTRL_SET_BGM_VOL                = 0x227,
    CTRL_SET_MEM                    = 0x230,
    CTRL_SET_LISTEN                 = 0x235,
    CTRL_SET_SE_POS                 = 0x267,
    CTRL_GET_SE_COUNT_BY_NAME       = 0x26C,
    CTRL_STOP_SE_BY_NAME            = 0x26D,
    CTRL_SET_SE_VOL_BY_NAME         = 0x26E,
    CTRL_GET_SE_COUNT_ALL           = 0x26F,
    CTRL_UNKNOWN                    = 0x276,
    CTRL_STOP_SE_BY_LABEL           = 0x28A,
    CTRL_SET_SE_VOL_BY_LABEL        = 0x28B,
    CTRL_SET_SE_POS_BY_LABEL        = 0x28C,
    CTRL_GET_SE_NAME_BY_LABEL       = 0x28D,
    CTRL_IS_PLAY_SE_BY_LABEL        = 0x28E,

    CTRL_MAXIMUM,

    CTRL_INIT_SOUND                 = 0x400,
    CTRL_RESET_GAME_WINDOW          = 0x401,
};

class CSoundPlayer
{
public:
    CSoundPlayer()
    {
        ZeroMemory(this, sizeof(*this));
    }

    ~CSoundPlayer()
    {
        if (m_Sound3D == nullptr)
            return;

        this->MixClose();
        this->IRelease();

        //Ldr::UnloadDll(m_Sound3D);  // todo: sometimes crash
    }

    NTSTATUS Initialize(HWND GameWindow);

    HWND THISCALL GetSoundControlWindow();

    static LRESULT NTAPI StaticDispatchCtrlCode(HWND Window, UINT Message, WPARAM MinorCtrlCode, LPARAM Parameter);

    DECL_STATIC_METHOD_POINTER(CSoundPlayer, StaticDispatchCtrlCode);

protected:
    LRESULT DispatchCtrlCode(ULONG_PTR Message, ULONG_PTR MinorCtrlCode, ULONG_PTR Parameter);

    /************************************************************************
      handler
    ************************************************************************/

    ForceInline PULONG_PTR AllocArgs(ULONG_PTR NumberOfArguments)
    {
        return (PULONG_PTR)AllocStack(NumberOfArguments * sizeof(ULONG_PTR));
    }

#define DECL_HNALDER(_name) LRESULT _name(ULONG_PTR Parameter);

    DECL_HNALDER(PlayFade);
    DECL_HNALDER(FadeOut);
    DECL_HNALDER(PlayFadeB);
    DECL_HNALDER(PlaySE);
    DECL_HNALDER(PlaySEB);
    DECL_HNALDER(PlayFadeEx);
    DECL_HNALDER(PlayFadeBEx);
    DECL_HNALDER(Play);
    DECL_HNALDER(PlayB);
    DECL_HNALDER(LoadSe);
    DECL_HNALDER(FadeOutEx);
    DECL_HNALDER(PlayStop);
    DECL_HNALDER(VolFade);
    DECL_HNALDER(StopAllSE);
    DECL_HNALDER(StopSE);
    DECL_HNALDER(GetPos);
    DECL_HNALDER(SetSeVol);
    DECL_HNALDER(SetBGMVol);
    DECL_HNALDER(SetMem);
    DECL_HNALDER(SetListen);
    DECL_HNALDER(SetSEPos);
    DECL_HNALDER(GetSECountByName);
    DECL_HNALDER(StopSEByName);
    DECL_HNALDER(SetSEVolByName);
    DECL_HNALDER(GetSECountAll);
    DECL_HNALDER(Unknown);
    DECL_HNALDER(StopSEByLabel);
    DECL_HNALDER(SetSEVolByLabel);
    DECL_HNALDER(SetSEPosByLabel);
    DECL_HNALDER(GetSENameByLabel);
    DECL_HNALDER(IsPlaySEByLabel);

protected:

    enum { BGMBuffer1 = 0, BGMBuffer2 = 1, MaxBuffer };

    PVOID   m_Sound3D;
    ULONG   m_UnknownF[0x100];
    CHAR    m_SeName[MAX_NTPATH];

    ULONG   m_FadeOutTime[2];
    ULONG   m_FadeOutTimeStamp[2];

    union
    {
        PVOID FunctionTable;
        struct
        {
            LRESULT (CDECL *IInit)(HWND Window);
            LRESULT (CDECL *IRelease)();
            LRESULT (CDECL *MixOpen)();
            LRESULT (CDECL *MixClose)();

            LRESULT (CDECL *IPlayFade)();
            LRESULT (CDECL *IFadeOut)(ULONG_PTR Index);
            LRESULT (CDECL *IPlayFadeB)();
            LRESULT (CDECL *IPlaySE)();
            LRESULT (CDECL *IPlaySEB)();
            LRESULT (CDECL *IPlayFadeEx)();
            LRESULT (CDECL *IPlayFadeBEx)();
            LRESULT (CDECL *IPlay)();
            LRESULT (CDECL *IPlayB)();
            LRESULT (CDECL *ILoadSE)(PCSTR SeName);
            LRESULT (CDECL *IFadeOutEx)(ULONG_PTR Index, ULONG_PTR Time);
            LRESULT (CDECL *IPlayStop)(ULONG_PTR Index);
            LRESULT (CDECL *IVolFade)();
            LRESULT (CDECL *IStopAllSE)();
            LRESULT (CDECL *IStopSE)(ULONG_PTR Index);
            LRESULT (CDECL *IGetPos)(ULONG_PTR Index);
            LRESULT (CDECL *ISetSEVol)(ULONG_PTR Index);
            LRESULT (CDECL *ISetBGMVol)(ULONG_PTR Index);
            LRESULT (CDECL *ISetMem)();
            LRESULT (CDECL *ISetListen)();
            LRESULT (CDECL *ISetSEPos)();
            LRESULT (CDECL *IGetSECountByName)(PCSTR SeName);
            LRESULT (CDECL *IStopSEByName)();
            LRESULT (CDECL *ISetSeVolByName)();
            LRESULT (CDECL *IGetSECountAll)();
            LRESULT (CDECL *IStopSEByLabel)(ULONG_PTR Label);
            LRESULT (CDECL *ISetSEVolByLabel)(ULONG_PTR Label, FLOAT Volume);
            LRESULT (CDECL *ISetSEPosByLabel)();
            LRESULT (CDECL *IIsPlaySEByLabel)(ULONG_PTR Label);
        };
    };
};


INIT_STATIC_MEMBER(CSoundPlayer::StubStaticDispatchCtrlCode);

#endif // _SOUNDARC_H_857ceedf_b76c_4eaf_bead_f8a5b4e76f18_
