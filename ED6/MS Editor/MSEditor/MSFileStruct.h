#ifndef _MSFILESTRUCT_H_
#define _MSFILESTRUCT_H_

#if _MSC_VER > 1000
#pragma once
#endif

#pragma warning(disable:4305)
#pragma warning(disable:4309)

#define LEN_OF_AIDATA       0x18
#define LEN_OF_SKILLDATA    0x1C
#define MAX_CRAFT_NAME      0x20
#define MAX_CRAFT_DES       0x100
#define MAX_NAME            0x15
#define MAX_DESCRIPTION     0x53
#define MAX_SEPITH_KIND     0x7
#define MAX_SEPITH_DROP     0xFF
#define MAX_CONDITION       0xFF
#define MAX_MAGIC_NUM       0x80
#define MAX_CRAFT_NUM       0x10
#define MAX_SKILL_NUM       0x10
#define CUSTOM_SKILL_BASE   0x3E8
#define CUSTOM_SKILL_MAX    0x3F8

#pragma pack(1)

typedef struct _tagAIData
{
    BYTE byCondition;
    BYTE byProbability;
    BYTE byTarget;
    BYTE byTargetCondition;
    WORD wEffectIndex;
    WORD wSkillDataIndex;
    CHAR cParam1[8];
    CHAR cParam2[8];
} TAIData, *LPAIData;

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
} ED6_CRAFT_AI_INFO;

typedef struct
{
    ULONG               ASFileIndex;            // 0x00     LOWORD = FileIndex, HIWORD = DAT Index
    USHORT              Level;                  // 0x04
    ULONG               HPMax;                  // 0x06
    ULONG               HPInitial;              // 0x0A
    USHORT              EPMax;                  // 0x0E
    USHORT              EPInitial;              // 0x10
    USHORT              CPMax;                  // 0x12
    USHORT              CPInitial;              // 0x14
    USHORT              SPD;                    // 0x16
    USHORT              MoveSPD;                // 0x18     移动速度
    USHORT              MOV;                    // 0x1A
    USHORT              STR;                    // 0x1C
    USHORT              DEF;                    // 0x1E
    USHORT              ATS;                    // 0x20
    USHORT              ADF;                    // 0x22
    USHORT              DEX;                    // 0x24
    USHORT              AGL;                    // 0x26
    USHORT              RGN;                    // 0x28
    DUMMY_STRUCT(2);
    USHORT              EXP;                    // 0x2C     经验值,(敌方等级-已方等级) * EXP
    DUMMY_STRUCT(2);
    USHORT              AIType;                 // 0x30     // 00 01 02 10 13 14
    DUMMY_STRUCT(6);
    BYTE                Flags;                  // 0x38     0x10: 敌人 0x40: 己方
    BYTE                DeathFlags;             // 0x39     0x04 死后留在战场上
    BYTE                UnderAttackFlags;       // 0x3A     0x08 Risist ATDelay 0x02 不被击退 0x01 被攻击不转身(3D)
    DUMMY_STRUCT(5);
    BYTE                SEX;                    // 0x40     0: 女 1: 男
    DUMMY_STRUCT(9);
    USHORT              CharSize;               // 0x4A     占 CharSize / 2 / 400 格
    DUMMY_STRUCT(0xA);
    ULONG               SymbolTextureFileIndex; // 0x56     AT条头像
    ULONG               Resistance;             // 0x5A     异常状态抗性
    DUMMY_STRUCT(0xB);
    ULONG               ConditionResistance[7]; // 0x69     属性攻击抗性
    BYTE                Sepith[7];              // 0x77     掉落耀晶片
    DUMMY_STRUCT(6);
    WORD                Equip[5];               // 0x84     装备
    WORD                Orb[4];                 // 0x8E     回路

    ED6_CRAFT_AI_INFO   NormalAttack;           // 0x96     ??
    DUMMY_STRUCT(8);
    BYTE                MagicCount;
    ED6_CRAFT_AI_INFO   Magic[MagicCount];      // 魔法使用表, 最多80个
    BYTE                CraftCount;
    ED6_CRAFT_AI_INFO   Craft[CraftCount];      // 战技使用表, 最多10个
    BYTE                SCraftCount;
    ED6_CRAFT_AI_INFO   SCraft[SCraftCount];    // S技使用表, 最多5个
    BYTE                MagicTableCount;        // 魔法表数
    // .........
} ED6_MONSTER_STATUS;

typedef struct
{
    DWORD   MsFileSize;             // MS文件大小
    DWORD   ASIndex;                // 使用的AS文件
    WORD    Level;                  // 等级
    DWORD   HPMax;                  // HP上限
    DWORD   HPDefault;              // 缺省HP
    WORD    EPMax;                  // EP上限
    WORD    EPDefault;              // 缺省EP
    WORD    CPMax;                  // CP上限
    WORD    CPDefault;              // 缺省CP
    WORD    SPD;                    // 速度
    WORD    MoveSPD;                // 移动速度
    WORD    MOV;                    // 移动距离
    WORD    STR;                    // 物理攻击力
    WORD    DEF;                    // 物理防御力
    WORD    ATS;                    // 魔法攻击力
    WORD    ADF;                    // 魔法防御力
    WORD    DEX;                    // 敏捷
    WORD    AGL;                    // 回避
    WORD    RNG;                    // 攻击距离
    WORD    EXP;                    // 经验值,(敌方等级-已方等级) * Exp
    BYTE    DeathFlag;              // 0x04 死后留在战场上
    BYTE    UnderAttackFlag;        // 0x08 Risist ATDelay 0x02 不被击退 0x01 被攻击不转身(3D)
    DWORD   Resistance;             // 异常状态免疫
    WORD    ConditionGuard[7];      // 属性有效率
    BYTE    Sepith[7];              // 掉落耀晶片
    WORD    Equip[5];               // 装备
    WORD    Orb[4];                 // 回路
    BYTE    MagicCount;             // 魔法数
    PBYTE   pbMagic;                // 魔法数据起始地址
    BYTE    CraftCount;             // 普通战技数
    PBYTE   pbCraft;                // 普通战技数据起始地址
    BYTE    SCraftCount;            // S技数
    PBYTE   pbSCraft;               // S技数据起始地址
    BYTE    SkillDataCount;         // 魔法&战技(>0x3E8)数
    PBYTE  *pbSKillData;            // 魔法&战技(>0x3E8)数据地址
    LPSTR  *lpSkillName;            // 魔法&战技(>0x3E8)名称数组
    LPSTR  *lpSkillDescription;     // 魔法&战技(>0x3E8)说明数组
    LPSTR   lpName;                 // 人物名字
    LPSTR   lpDescription;          // 人物说明
} MSFileInfo, *LPMSFileInfo;

#pragma pack()

typedef struct _tagAI_Item
{
    CHAR   *szDescription;
    BYTE    nBytesOfParam;
    DWORD   dwParam1;
    DWORD   dwParam2;
} TAI_Item;

static TAI_Item condition[] =
{
    {"0%的概率",                            0, 0, 0},
    {"100%的概率",                            0, 0, 0},
    {"无条件",                                0, 0, 0},
    {"自身HP少于(%)",                        1, 0, 0},
    {"刚受到伤害",                            4, 0x040000, 0},
    {"上次成功造成伤害",                    4, 0, 0},
    {"距离内有目标",                        2, 0, 0},
    {"距离外有目标",                        2, 0, 0},
    {"计时器超时则使用",                    8, 0, 0},
    {"未知",                                0, 0, 0},
    {"CP不小于",                            1, 0, 0},
    {"无",                                    4, 0, 0},
    {"无",                                    4, 0, 0},
    {"有目标HP小于(%)",                        1, 0, 0},
    {"战斗不能人数超过",                    1, 0, 0},
    {"有目标正在驱动",                        0, 0, 0},
    {"无",                                    4, 0, 0},
    {"无",                                    4, 0, 0},
    {"无",                                    4, 0, 0},
    {"有目标中了特定状态",                    4, 0, 0},
    {"有目标没中特定状态",                    4, 0, 0},
    {"指定目标没中特定状态",                8, 0, 0},
    {"(魔法专用)自身HP少于(%)",                1, 0, 0},
    {"(魔法专用)使用指定技能后立刻使用",    2, 0, 0},
    {"未知",                                0, 0, 0},
    {"有目标正在驱动魔法",                    0, 0, 0},
    {"很奇怪，看不出来……",                0, 0, 0},
    {"有目标cp达到指定值",                    1, 0, 0},
};

static TAI_Item target[] =
{
    {"最近的",                        0, 0, 0},
    {"分身用",                        0, 0, 0},
    {"女性",                        0, 0, 0},
    {"最近的",                        0, 0, 0},
    {"随机并锁定",                    0, 0, 0},
    {"受伤且HP最少",                0, 0, 0},
    {"HP最多",                        0, 0, 0},
    {"范围内目标不少于",            1, 0, 0},
    {"随机",                        0, 0, 0},
    {"最远的",                        0, 0, 0},
    {"AT栏最前",                    0, 0, 0},
    {"驱动中",                        0, 0, 0},
    {"自己",                        0, 0, 0},
    {"HP百分比最低的",                8, 0, 0},
    {"以自己为圆心目标不少于",        1, 0, 0},
    {"AT栏最底",                    0, 0, 0},
    {"未知",                        0, 0, 0},
    {"战斗不能的",                    0, 0, 0},
    {"无条件",                        0, 0, 0},
    {"中了特定状态的",                4, 0, 0},
    {"CP最多的",                    0, 0, 0},
    {"指定距离外的",                4, 0, 0},
    {"古代龙喷火专用",                1, 0, 0},
    {"随机地点",                    0, 0, 0},
    {"没中特定状态的",                4, 0, 0},
    {"范围内目标不少于(直线)",        1, 0, 0},
};

#endif /* _MSFILESTRUCT_H_ */