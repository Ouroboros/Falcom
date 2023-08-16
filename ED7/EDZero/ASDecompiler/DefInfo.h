#ifndef _DEFINFO_H_
#define _DEFINFO_H_

#include "pragma_once.h"

#pragma pack(1)

typedef struct
{
    USHORT ParamIndex;
    USHORT Length;
    ULONG  Value;
    LPSTR  pszDescription;
} ED6_INSTRUCTION_PARAM_DESC;

struct ED6_AS_INSTRUCTION_MAP
{
    DECL_HANDLER(CED7AsDecompiler::*Handler);
    ED6_AS_INSTRUCTION          Instruction;
    LPCSTR                      pszName;
    ULONG                       DescCount;
    ED6_INSTRUCTION_PARAM_DESC *pParamDesc;
};

#pragma pack()

#define SET_HANDLER(handler, ins, ...) \
            { &CED7AsDecompiler::handler, ins, __VA_ARGS__ }
#define SET_DESC(_Name) countof(_Name), _Name

#define PARAM_DESC(_Name, ...) \
            ED6_INSTRUCTION_PARAM_DESC _Name[] = \
            { \
                __VA_ARGS__ \
            }

#define COMMON_PARAM_TARGET(_Index) \
            { _Index, 1, 0xFF, "Self" }, \
            { _Index, 1, 0xFE, "Target" }, \
            { _Index, 1, 0xFB, "Dest" }, \
            { _Index, 1, 0x11, "Clone1" }, \
            { _Index, 1, 0x12, "Clone2" }

#define COMMON_PARAM_THREAD(_Index) \
            { _Index, 1, 0xFF, "MainThread" }, \
            { _Index, 1, 0x00, "CurThread" }, \
            { _Index, 1, 0x01, "Thread1" }, \
            { _Index, 1, 0x02, "Thread2" }, \
            { _Index, 1, 0x03, "Thread3" }

PARAM_DESC(Desc02, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc03, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc04, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc05, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc08, COMMON_PARAM_TARGET(0), COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc0A, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc0C, COMMON_PARAM_TARGET(0), COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc0D, COMMON_PARAM_TARGET(0), COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc0E, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc11, COMMON_PARAM_TARGET(0), COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc15, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc16, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc17, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc18, COMMON_PARAM_TARGET(2));
PARAM_DESC(Desc19, COMMON_PARAM_TARGET(2));
PARAM_DESC(Desc1B, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc1C, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc1D, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc20, COMMON_PARAM_TARGET(0), COMMON_PARAM_THREAD(1));
PARAM_DESC(Desc21, COMMON_PARAM_THREAD(1));
PARAM_DESC(Desc22, COMMON_PARAM_TARGET(0), COMMON_PARAM_THREAD(1));
PARAM_DESC(Desc23, COMMON_PARAM_TARGET(0), COMMON_PARAM_THREAD(1));
PARAM_DESC(Desc24, COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc25, COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc28, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc2C, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc2D, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc2E, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc2F, COMMON_PARAM_TARGET(0), COMMON_PARAM_THREAD(1));
PARAM_DESC(Desc35, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc3F, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc41, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc45, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc46, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc47, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc48, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc49, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc5C, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc5D, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc5F, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc84, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc85, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc89, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc8A, COMMON_PARAM_TARGET(0), COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc8D, COMMON_PARAM_TARGET(1));
PARAM_DESC(Desc95, COMMON_PARAM_TARGET(0));
PARAM_DESC(Desc9C, COMMON_PARAM_TARGET(0));
PARAM_DESC(DescA8, { 0, 1, 0xFE, "Target" });

ED6_AS_INSTRUCTION_MAP g_InstructionMap[] =
{
    SET_HANDLER(Handle00, AS_END,               "End"),
    SET_HANDLER(Handle01, AS_GOTO,              "Goto"),
    SET_HANDLER(Handle02, AS_SELECT_SUB_CHIP,   "SubChip",          SET_DESC(Desc02)),
    SET_HANDLER(Handle03, AS_DEG,               NULL,               SET_DESC(Desc03)),
    SET_HANDLER(Handle04, AS_04,                NULL,               SET_DESC(Desc04)),
    SET_HANDLER(Handle05, AS_05,                NULL,               SET_DESC(Desc05)),
    SET_HANDLER(Handle06, AS_SLEEP,             "Sleep"),
    SET_HANDLER(Handle07, AS_CLEAR_EFFECT,      "Update"),
    SET_HANDLER(Handle08, AS_TELEPORT,          "Teleport",         SET_DESC(Desc08)),
    SET_HANDLER(Handle09, AS_09,                NULL),
    SET_HANDLER(Handle0A, AS_0A,                NULL,               SET_DESC(Desc0A)),
    SET_HANDLER(Handle0B, AS_TURN,              NULL),
    SET_HANDLER(Handle0C, AS_0C,                "TurnDirection",    SET_DESC(Desc0C)),
    SET_HANDLER(Handle0D, AS_JUMP,              "Jump",             SET_DESC(Desc0D)),
    SET_HANDLER(Handle0E, AS_DROP_DOWN,         "DropDown",         SET_DESC(Desc0E)),
    SET_HANDLER(Handle0F, AS_JUMP_TO_TARGET,    "JumpToTarget"),   // WORD Height, WORD Speed
    SET_HANDLER(Handle10, AS_JUMP_BACK,         "JumpBack"),       // WORD Height, WORD Speed
    SET_HANDLER(Handle11, AS_MOVE,              "Move",             SET_DESC(Desc11)),
    SET_HANDLER(Handle12, AS_ADD_EFFECT,        "AddEff"),
    SET_HANDLER(Handle13, AS_RELEASE_EFFECT,    "ReleaseEff"),
    SET_HANDLER(Handle14, AS_14,                NULL),
    SET_HANDLER(Handle15, AS_WAIT_EFFECT,       "WaitEff",          SET_DESC(Desc15)),  // BYTE Target, BYTE Layer
    SET_HANDLER(Handle16, AS_FINISH_EFFECT,     "FinishEff",        SET_DESC(Desc16)),
    SET_HANDLER(Handle17, AS_CANCLE_EFFECT,     "CancelEff",        SET_DESC(Desc17)),
    SET_HANDLER(Handle18, AS_SHOW_EFFECT,       "ShowEff",          SET_DESC(Desc18)),  // BYTE EffPos, BYTE ??, BYTE Target, WORD EffIndex, LONG X, LONG Y, LONG H, WORD ?, WORD ScaleX, ScaleY, ScaleH, BYTE LayerIndex
    SET_HANDLER(Handle19, AS_SHOW_3DEFFECT,     "Show3DEff",        SET_DESC(Desc19)),
    SET_HANDLER(Handle1A, AS_1A,                NULL),
    SET_HANDLER(Handle1B, AS_SELECT_CHIP,       "SelectChip",       SET_DESC(Desc1B)),
    SET_HANDLER(Handle1C, AS_DAMAGE,            "Damage",           SET_DESC(Desc1C)),
    SET_HANDLER(Handle1D, AS_DAMAGE_ANIME,      "DamageAnime",      SET_DESC(Desc1D)),
    SET_HANDLER(Handle1E, AS_1E,                NULL),
    SET_HANDLER(Handle1F, AS_1F,                NULL),
    SET_HANDLER(Handle20, AS_20,                NULL,               SET_DESC(Desc20)),
    SET_HANDLER(Handle21, AS_21,                NULL,               SET_DESC(Desc21)),
    SET_HANDLER(Handle22, AS_BEGINTHREAD,       "BeginThread",      SET_DESC(Desc22)),
    SET_HANDLER(Handle23, AS_WAITTHREAD,        "WaitThread",       SET_DESC(Desc23)),
    SET_HANDLER(Handle24, AS_SET_CHIP_MODE_FLAG,    "SetChipModeFlag",      SET_DESC(Desc24)),
    SET_HANDLER(Handle25, AS_CLEAR_CHIP_MODE_FLAG,  "ClearChipModeFlag",    SET_DESC(Desc25)),
    SET_HANDLER(Handle26, AS_26,                NULL),
    SET_HANDLER(Handle27, AS_27,                NULL),
    SET_HANDLER(Handle28, AS_CHAR_SAY,          "Say",              SET_DESC(Desc28)),
    SET_HANDLER(Handle29, AS_29,                NULL),
    SET_HANDLER(Handle2A, AS_TIP_TEXT,          "TipText"),
    SET_HANDLER(Handle2B, AS_2B,                NULL),
    SET_HANDLER(Handle2C, AS_SHADOW_BEGIN,      "ShadowBegin",      SET_DESC(Desc2C)),
    SET_HANDLER(Handle2D, AS_SHADOW_END,        "ShadowEnd",        SET_DESC(Desc2D)),
    SET_HANDLER(Handle2E, AS_SHAKE_CHAR,        "ShakeChar",        SET_DESC(Desc2E)),
    SET_HANDLER(Handle2F, AS_SUSPEND_THREAD,    "SuspendThread",    SET_DESC(Desc2F)),

    SET_HANDLER(Handle31, AS_31,                NULL),
    SET_HANDLER(Handle32, AS_32,                NULL),
    SET_HANDLER(Handle33, AS_33,                NULL),
    SET_HANDLER(Handle34, AS_34,                NULL),
    SET_HANDLER(Handle35, AS_KEEP_ANGLE,        "KeepAngle",        SET_DESC(Desc35)),
    SET_HANDLER(Handle36, AS_36,                NULL),


    SET_HANDLER(Handle39, AS_SET_ANGLE,         "SetAngle"),    // int angle, int time
    SET_HANDLER(Handle3A, AS_TILT_ANGLE,        "TiltAngle"),
    SET_HANDLER(Handle3B, AS_ROTATION_ANGLE_H,  "RotationAngleHorz"),
    SET_HANDLER(Handle3C, AS_3C,                NULL),
    SET_HANDLER(Handle3D, AS_SHAKE_SCREEN,      "ShakeScreen"),
    SET_HANDLER(Handle3E, AS_3E,                NULL),
    SET_HANDLER(Handle3F, AS_3F,                NULL,               SET_DESC(Desc3F)),
    SET_HANDLER(Handle40, AS_40,                NULL),
    SET_HANDLER(Handle41, AS_LOCK_ANGLE,        "LockAngle",        SET_DESC(Desc41)),
    SET_HANDLER(Handle42, AS_42,                NULL),
    SET_HANDLER(Handle43, AS_SET_BK_COLOR,      "SetBkColor"),  // byte 0, int, COLORREF
    SET_HANDLER(Handle44, AS_ZOOM_ANGLE,        "ZoomAngle"),
    SET_HANDLER(Handle45, AS_45,                NULL,               SET_DESC(Desc45)),
    SET_HANDLER(Handle46, AS_46,                NULL,               SET_DESC(Desc46)),
    SET_HANDLER(Handle47, AS_47,                NULL,               SET_DESC(Desc47)),
    SET_HANDLER(Handle48, AS_48,                NULL,               SET_DESC(Desc48)),
    SET_HANDLER(Handle49, AS_SET_CONTROL,       NULL,               SET_DESC(Desc49)),
    SET_HANDLER(Handle4A, AS_4A,                NULL),
    SET_HANDLER(Handle4B, AS_CONDITION,         "Condition"),
    SET_HANDLER(Handle4C, AS_LOOP_TARGET_BEG,   "LoopTargetBegin"),
    SET_HANDLER(Handle4D, AS_RESET_LOOP_TARGET, "ResetLoopTarget"),
    SET_HANDLER(Handle4E, AS_LOOP_TARGET_END,   "LoopTargetEnd"),
    SET_HANDLER(Handle4F, AS_4F,                NULL),
    SET_HANDLER(Handle50, AS_CALL,              "Call"),
    SET_HANDLER(Handle51, AS_RET,               "Ret"),
    SET_HANDLER(Handle52, AS_52,                NULL),
    SET_HANDLER(Handle53, AS_53,                NULL),
    SET_HANDLER(Handle54, AS_54,                NULL),  // SetState
    SET_HANDLER(Handle55, AS_MAGIC_CAST_BEGIN, "MagicCastBegin"),
    SET_HANDLER(Handle56, AS_MAGIC_CAST_END,   "MagicCastEnd"),
    SET_HANDLER(Handle57, AS_57,                NULL),
    SET_HANDLER(Handle58, AS_BEAT_BACK,         "BeatBack"),
    SET_HANDLER(Handle59, AS_59,                NULL),
    SET_HANDLER(Handle5A, AS_5A,                NULL),
    SET_HANDLER(Handle5B, AS_5B,                NULL),
    SET_HANDLER(Handle5C, AS_SHOW,              "Show",             SET_DESC(Desc5C)),
    SET_HANDLER(Handle5D, AS_HIDE,              "Hide",             SET_DESC(Desc5D)),
    SET_HANDLER(Handle5E, AS_5E,                NULL),
    SET_HANDLER(Handle5F, AS_5F,                NULL,               SET_DESC(Desc5F)),
    SET_HANDLER(Handle60, AS_60,                NULL),
    SET_HANDLER(Handle61, AS_SET_BATTLE_SPEED,  "SetBattleSpeed"),  // int time
    SET_HANDLER(Handle62, AS_Voice,             "Voice"),

    SET_HANDLER(Handle64, AS_SOUND_EFFECT,      "SE"),
    SET_HANDLER(Handle65, AS_SOUND_EFFECTEX,    "SeEx"),
    SET_HANDLER(Handle66, AS_66,                NULL),
    SET_HANDLER(Handle67, AS_SCRAFT_CUT_IN,     "ScraftCutIn"),
    SET_HANDLER(Handle68, AS_68,                NULL),

    SET_HANDLER(Handle6A, AS_LOAD_SCHIP,        "LoadSChip"),
    SET_HANDLER(Handle6B, AS_RESET_SCRAFT_CHIP, "ResetSCraftChip"),
    SET_HANDLER(Handle6C, AS_DIE,               "Die"),
    SET_HANDLER(Handle6D, AS_6D,                NULL),
    SET_HANDLER(Handle6E, AS_6E,                NULL),
    SET_HANDLER(Handle6F, AS_6F,                NULL),
    SET_HANDLER(Handle70, AS_70,                NULL),
    SET_HANDLER(Handle71, AS_71,                NULL),
    SET_HANDLER(Handle72, AS_72,                NULL),
    SET_HANDLER(Handle73, AS_73,                NULL),



    SET_HANDLER(Handle77, AS_77,                NULL),
    SET_HANDLER(Handle78, AS_SET_EFF_STATE,     NULL),
    SET_HANDLER(Handle79, AS_79,                NULL),
    SET_HANDLER(Handle7A, AS_CRAFT_END,         "CraftEnd"),
    SET_HANDLER(Handle7B, AS_SET_CRAFT_END_FLAG,"CraftEndFlag"),
    SET_HANDLER(Handle7C, AS_7C,                NULL),
    SET_HANDLER(Handle7D, AS_7D,                NULL),
    SET_HANDLER(Handle7E, AS_7E,                NULL),
    SET_HANDLER(Handle7F, AS_BLUR_SCREEN,       "Blur"),
    SET_HANDLER(Handle80, AS_80,                NULL),      // set blur duration

    SET_HANDLER(Handle82, AS_82,                NULL),
    SET_HANDLER(Handle83, AS_SORT_TARGET,       "SortTarget"),
    SET_HANDLER(Handle84, AS_ROTATE_CHAR,       "RotateChar",       SET_DESC(Desc84)),
    SET_HANDLER(Handle85, AS_SETUSERDATA,       "SetUserData",      SET_DESC(Desc85)),

    SET_HANDLER(Handle87, AS_87,                NULL),
//    SET_HANDLER(Handle88, AS_VOICE,             "Voice"),
    SET_HANDLER(Handle89, AS_SAVE_CUR_POS,      "SaveCurPos",       SET_DESC(Desc89)),  // set fly point
    SET_HANDLER(Handle8A, AS_CLONE,             "Clone",            SET_DESC(Desc8A)),
    SET_HANDLER(Handle8B, AS_USE_ITEM_BEGIN,    "UseItemBegin"),
    SET_HANDLER(Handle8C, AS_USE_ITEM_END,      "UseItemEnd"),
    SET_HANDLER(Handle8D, AS_ZOOM,              NULL,               SET_DESC(Desc8D)),
    SET_HANDLER(Handle8E, AS_LOAD_X_FILE,       "LoadXFile"),
    SET_HANDLER(Handle8F, AS_8F,                NULL),

    SET_HANDLER(Handle91, AS_91,                NULL),
    SET_HANDLER(Handle92, AS_92,                NULL),
    SET_HANDLER(Handle93, AS_93,                NULL),
    SET_HANDLER(Handle94, AS_94,                NULL),
    SET_HANDLER(Handle95, AS_95,                NULL),
    SET_HANDLER(Handle96, AS_SET_ANGLE_TARGET,  "SetAngleTarget",   SET_DESC(Desc95)),
    SET_HANDLER(Handle97, AS_MOVE_ANGLE,        "MoveAngle"),       // BYTE Dest, WORD Height, Height?

    SET_HANDLER(Handle99, AS_99,                NULL),
    SET_HANDLER(Handle9A, AS_9A,                NULL),
    SET_HANDLER(Handle9B, AS_9B,                NULL),
    SET_HANDLER(Handle9C, AS_RESET_CHIP_STATUS, "ResetChipStatus",  SET_DESC(Desc9C)),

    SET_HANDLER(Handle9E, AS_SET_TIMER,         NULL),
    SET_HANDLER(Handle9F, AS_SET_BATTLE_MODE,   "SetBattleMode"),
    SET_HANDLER(HandleA0, AS_A0,                NULL),
    SET_HANDLER(HandleA1, AS_A1,                NULL),




    SET_HANDLER(HandleA6, AS_A6,                NULL),
    SET_HANDLER(HandleA7, AS_BATTLE_EFFECT_END, "BattleEffEnd"),
    SET_HANDLER(HandleA8, AS_DAMAGE_VOICE,      "DamageVoice",      SET_DESC(DescA8)),
    SET_HANDLER(HandleA9, AS_A9,                NULL),
    SET_HANDLER(HandleAA, AS_AA,                NULL),

    SET_HANDLER(HandleAC, AS_AC,                NULL),
    SET_HANDLER(HandleAD, AS_AD,                NULL),
    SET_HANDLER(HandleAE, AS_AE,                NULL),
    SET_HANDLER(HandleAF, AS_AF,                NULL),
    SET_HANDLER(HandleB0, AS_B0,                NULL),
    SET_HANDLER(HandleB1, AS_B1,                NULL),
    SET_HANDLER(HandleB2, AS_B2,                NULL),
    SET_HANDLER(HandleB3, AS_B3,                NULL),
    SET_HANDLER(HandleB4, AS_B4,                NULL),
    SET_HANDLER(HandleB5, AS_B5,                NULL),
    SET_HANDLER(HandleB6, AS_B6,                NULL),
    SET_HANDLER(HandleB7, AS_B7,                NULL),
    SET_HANDLER(HandleB8, AS_B8,                NULL),
};

/************************************************************************
  Jump(0D)
  Jump(Self, Clone1, 0x0:i, 0x0:i, 0x0:i, 0xBB8:s, 0x3E8:s)
  BYTE Target, BYTE Pos, LONG OffsetX, LONG OffsetH, LONG OffsetY, WORD Height, WORD Speed

  Teleport(11):
  Teleport(Clone1, Self, 0:i, 0:i, 2000:i)
  BYTE Target, BYTE Pos, LONG OffsetX, LONG OffsetH, LONG OffsetY

  18:
  bool  IsOnTheFloor
  BYTE  Option   // 0xF2, 0xF3, 0xFB, 0xFD
  BYTE  Target
  DWORD Unknown[3]
  WORD  X
  WORD  Y
  WORD  Z
  WORD  XFactor
  WORD  YFactor
  WORD  ZFactor
  BYTE  ??

  RotateChar(84)
  BYTE Target, WORD Unknwon1, WORD Unknwon2, WORD Angle, WORD TimeToRotate

  8D:
  BYTE Type     // 01 - 2E

  8D 07:
  Zoom ._CH size
  
  exp:
  ins_8D(0x7:b, 0xFC:i, 0x3E8:i, 0x384:i, 0x3E8:i)
  0xFC: 范围内所有目标
  0x3E8: Width
  0x384: Height
  0x3E8: ??

  8D 09: move target to

  exp:                 speed
  ins_8D(0x9:b, 0x3:i, 0x3E8:i, 0x0:i, 0x0:i)

  param1:
  1: 绕指定地点转小圈
  2: 绕指定地点转大圈
  3: 移动到指定地点
  4: 移动到指定地点并吸进去
  8: 自己死亡
  9: 偷窃

  8D 0A
  exp:      no param
  ins_8D(0xA:b, 0:i, 0:i, 0x0:i, 0x0:i)
  WaitFor8D09

  SetBattleMode(9F)
  exp:
  SetBattleMode(0x2:b, 0x400:i)

  0: set flag1
  1: clear flag1

  2: set flag2
  3: clear flag2

  0x00000001    人物黑色
  0x00000002    只能用逃跑
  0x00000010    黑屏
  0x00000400    反色

************************************************************************/

CHAR *g_szIntrinsicCraft[INTRINSIC_CRAFT_COUNT] =
{
    NAME_INTRINSIC_CRAFT1,
    NAME_INTRINSIC_CRAFT2,
    NAME_INTRINSIC_CRAFT3,
    NAME_INTRINSIC_CRAFT4,
    NAME_INTRINSIC_CRAFT5,
    NAME_INTRINSIC_CRAFT6,
    NAME_INTRINSIC_CRAFT7,
    NAME_INTRINSIC_CRAFT8,
    NAME_INTRINSIC_CRAFT9,
    NAME_INTRINSIC_CRAFT10,
    NAME_INTRINSIC_CRAFT11,
    NAME_INTRINSIC_CRAFT12,
    NAME_INTRINSIC_CRAFT13,
    NAME_INTRINSIC_CRAFT14,
    NAME_INTRINSIC_CRAFT15,
    NAME_INTRINSIC_CRAFT16,
};

#endif // _DEFINFO_H_