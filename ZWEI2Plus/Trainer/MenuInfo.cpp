#include "CWindow.h"

TMenuItem Menu_Lock[] =
{
    { ID_LOCK_HP,   MF_ENABLED, "锁定HP\tF5",   NULL },
    { ID_LOCK_MP,   MF_ENABLED, "锁定MP\tF6",   NULL },
    { ID_LOCK_OUGI, MF_ENABLED, "锁定奥义\tF5", NULL },
};

TMenuItem Menu_Modify_Ski[] =
{
    { ID_SKI_LV1, MF_ENABLED, "Lv.1 通过", NULL },
    { ID_SKI_LV2, MF_ENABLED, "Lv.2 通过", NULL },
    { ID_SKI_LV3, MF_ENABLED, "Lv.3 通过", NULL },
    { ID_SKI_LV4, MF_ENABLED, "Lv.4 通过", NULL },
};

TMenuItem Menu_Max_EventItem[] =
{
    { ID_MAX_EVENTITEM, MF_ENABLED, "事件道具", NULL },
    { ID_MAX_CD,        MF_ENABLED, "CD光盘",   NULL },
    { ID_MAX_TREASURE,  MF_ENABLED, "谜之宝箱", NULL },
};

TMenuItem Menu_Modify[] =
{
    { ID_GOLD,  MF_ENABLED, "金钱",     NULL,     0 },
    { ID_STEP,  MF_ENABLED, "总步数",   NULL,     0 },
    { ID_POPUP, MF_POPUP,   "滑雪结果", Menu_Modify_Ski, countof(Menu_Modify_Ski) },
};

TMenuItem Menu_Maximum[] =
{
    { ID_MAX_GOLD,            MF_ENABLED, "金钱\tCtrl+A",   NULL },
    { ID_POPUP,               MF_POPUP,   "事件道具",       Menu_Max_EventItem, countof(Menu_Max_EventItem) },
    { ID_MAX_ITEM,            MF_ENABLED, "道具\tCtrl+E",   NULL },
    { ID_MAX_FOOD,            MF_ENABLED, "食物\tCtrl+F",   NULL },
    { ID_MAX_EQUIPMENT,       MF_ENABLED, "武器\tCtrl+G",   NULL },
    { ID_MAX_ACCESSORYSOCKET, MF_ENABLED, "饰品孔\tCtrl+A", NULL },
    { ID_MAX_OUGI,            MF_ENABLED, "奥义\tCtrl+H",   NULL },
    { ID_MAX_CLOTHES,         MF_ENABLED, "衣服\tCtrl+I",   NULL },
    { ID_MAX_ACCESSORY,       MF_ENABLED, "饰品\tCtrl+J",   NULL },
    { ID_MAX_GADGET,          MF_ENABLED, "挂件\tCtrl+K",   NULL },
    { ID_MAX_PET,             MF_ENABLED, "宠物\tCtrl+L",   NULL },
    { ID_MAX_CHAR,            MF_ENABLED, "人物\tCtrl+M",   NULL },
    { ID_MAX_MONSTER,         MF_ENABLED, "魔物\tCtrl+N",   NULL },
};

TMenuItem Menu_Joy_Ragna[] =
{
    { ID_JOY_RAGNA_ORIGIN,          MF_ENABLED, "拉古那·原服版\tCtrl+F1", NULL },
    { ID_JOY_RAGNA_BLUEHAIR,        MF_ENABLED, "拉古那·蓝发版",          NULL },
    { ID_JOY_RAGNA_NOEYEPATCH,      MF_ENABLED, "拉古那·无眼罩",          NULL },
    { ID_JOY_RAGNA_EYEPATCH,        MF_ENABLED, "拉古那·戴眼罩",          NULL },
    { ID_JOY_RAGNA_HOTSPRING,       MF_ENABLED, "拉古那·温泉装",          NULL },
    { ID_JOY_RAGNA_TAPEUP,          MF_ENABLED, "拉古那·包扎版",          NULL },
    { ID_JOY_RAGNA_ERMINE,          MF_ENABLED, "拉古那·白貂服",          NULL },
    { ID_JOY_RAGNA_ALWENORIGIN,     MF_ENABLED, "艾雯·原服版",            NULL },
    { ID_JOY_RAGNA_ALWENREDHAIR,    MF_ENABLED, "艾雯·红发版",            NULL },
    { ID_JOY_RAGNA_ALWENHOTSPRING,  MF_ENABLED, "艾雯·温泉装",            NULL },
    { ID_JOY_RAGNA_ALWENSAILORSUIT, MF_ENABLED, "艾雯·水手服",            NULL },
    { ID_JOY_RAGNA_SUBARUORIGIN,    MF_ENABLED, "死八路·原服版",          NULL },
    { ID_JOY_RAGNA_SUBARUNOSHOE,    MF_ENABLED, "死八路·脱鞋版",          NULL },
    { ID_JOY_RAGNA_SUBARUHOTSPRING, MF_ENABLED, "死八路·温泉装",          NULL },
    { ID_JOY_RAGNA_SUBARUTAPEUP,    MF_ENABLED, "死八路·包扎版",          NULL },
};

TMenuItem Menu_Joy_Alwen[] =
{
    { ID_JOY_ALWEN_ORIGIN,          MF_ENABLED, "艾雯·原服版\tCtrl+F2", NULL },
    { ID_JOY_ALWEN_REDHAIR,         MF_ENABLED, "艾雯·红发版",          NULL },
    { ID_JOY_ALWEN_HOTSPRING,       MF_ENABLED, "艾雯·温泉装",          NULL },
    { ID_JOY_ALWEN_SAILORSUIT,      MF_ENABLED, "艾雯·水手服",          NULL },
    { ID_JOY_ALWEN_RAGNAORIGIN,     MF_ENABLED, "拉古那·原服版",        NULL },
    { ID_JOY_ALWEN_RAGNABLUEHAIR,   MF_ENABLED, "拉古那·蓝发版",        NULL },
    { ID_JOY_ALWEN_RAGNANOEYEPATCH, MF_ENABLED, "拉古那·无眼罩",        NULL },
    { ID_JOY_ALWEN_RAGNAEYEPATCH,   MF_ENABLED, "拉古那·戴眼罩",        NULL },
    { ID_JOY_ALWEN_RAGNAHOTSPRING,  MF_ENABLED, "拉古那·温泉装",        NULL },
    { ID_JOY_ALWEN_RAGNATAPEUP,     MF_ENABLED, "拉古那·包扎版",        NULL },
    { ID_JOY_ALWEN_RAGNAERMINE,     MF_ENABLED, "拉古那·白貂服",        NULL },
    { ID_JOY_ALWEN_SUBARUORIGIN,    MF_ENABLED, "死八路·原服版",        NULL },
    { ID_JOY_ALWEN_SUBARUNOSHOE,    MF_ENABLED, "死八路·脱鞋版",        NULL },
    { ID_JOY_ALWEN_SUBARUHOTSPRING, MF_ENABLED, "死八路·温泉装",        NULL },
    { ID_JOY_ALWEN_SUBARUTAPEUP,    MF_ENABLED, "死八路·包扎版",        NULL },
};

TMenuItem Menu_Joy_Servant[] =
{
    { ID_JOY_FOLLOW_NONE, MF_ENABLED, "无",   NULL },
    { ID_JOY_FOLLOW_LUE,  MF_ENABLED, "露",   NULL },
    { ID_JOY_FOLLOW_MIA,  MF_ENABLED, "米娅", NULL },
};

TMenuItem Menu_Joy[] =
{
    { ID_POPUP, MF_POPUP, "拉古娜", Menu_Joy_Ragna,   countof(Menu_Joy_Ragna) },
    { ID_POPUP, MF_POPUP, "艾雯",   Menu_Joy_Alwen,   countof(Menu_Joy_Alwen) },
    { ID_POPUP, MF_POPUP, "跟随",   Menu_Joy_Servant, countof(Menu_Joy_Servant) },
};

TMenuItem Menu_Other[] =
{
    { ID_OTHER_UNDEAD,        MF_ENABLED, "无敌\tShift+F1",             NULL },
    { ID_OTHER_ONEFOODLVUP,   MF_ENABLED, "吃一个食物就升级\tShift+F2", NULL },
    { ID_OTHER_ONEHIT,        MF_ENABLED, "一击必杀\tShift+F3",         NULL },
    { ID_OTHER_QSPS,          MF_ENABLED, "快速蓄力\tShift+F4",         NULL },
    { ID_OTHER_UNLIMITEDJUMP, MF_ENABLED, "无限跳跃\tShift+F5",         NULL },
    { ID_OTHER_FASTMOVE,      MF_ENABLED, "高速移动\tShift+F6",         NULL },
    { ID_OTHER_EVAPLAT,       MF_ENABLED, "评价为白金\tShift+F7",       NULL },
    { ID_OTHER_FIGURE,        MF_ENABLED, "必掉手办\tShift+F8",         NULL },
};

TMenuItem Menu_Item[] =
{
    { ID_POPUP, MF_POPUP, "锁定",   Menu_Lock,    countof(Menu_Lock)    },
    { ID_POPUP, MF_POPUP, "修改",   Menu_Modify,  countof(Menu_Modify)  },
    { ID_POPUP, MF_POPUP, "最大化", Menu_Maximum, countof(Menu_Maximum) },
    { ID_POPUP, MF_POPUP, "娱乐",   Menu_Joy,     countof(Menu_Joy)     },
    { ID_POPUP, MF_POPUP, "其它",   Menu_Other,   countof(Menu_Other)   },
};

TMenuItem Menu_File[] =
{
    { ID_REFRESHDATA,    MF_ENABLED, "刷新数据\tF5" },
    { ID_OPENSAVEFOLDER, MF_ENABLED, "打开存档文件夹" },
    { ID_EXIT,           MF_ENABLED, "退出\tEsc" },
};

TMenuItem Menu_Main[] =
{
    { ID_POPUP, MF_POPUP,   "文件(&F)", Menu_File, countof(Menu_File) },
    { ID_POPUP, MF_POPUP,   "项目(&I)", Menu_Item, countof(Menu_Item) },
    { ID_ABOUT, MF_ENABLED, "关于(&A)", NULL,      0 },
};

DWORD dwMenuCount = countof(Menu_Main);