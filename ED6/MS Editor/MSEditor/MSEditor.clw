; CLW file contains information for the MFC ClassWizard

[General Info]
Version=1
LastClass=CAIEditor
LastTemplate=CDialog
NewFileInclude1=#include "stdafx.h"
NewFileInclude2=#include "mseditor.h"
LastPage=0

ClassCount=11
Class1=CMSEditorApp
Class2=CMSEditorDlg
Class3=CPage_Item
Class4=CPage_Risist
Class5=CPage_Status
Class6=CPage_Trophy

ResourceCount=7
Resource1=IDD_PAGE_STATUS
Resource2=IDD_MSEDITOR
Resource3=IDD_PAGE_RISIST
Resource4=IDD_PAGE_SKILL
Resource5=IDD_PAGE_TROPHY
Class7=CPage_Magic
Class8=CPage_Skill
Class9=CMyClistCtrl
Class10=CMyListCtrl
Class11=CAIEditor
Resource6=IDD_PAGE_ITEM
Resource7=IDD_AIEDITOR

[CLS:CMSEditorApp]
Type=0
BaseClass=CWinApp
HeaderFile=MSEditor.h
ImplementationFile=MSEditor.cpp
LastObject=CMSEditorApp

[CLS:CMSEditorDlg]
Type=0
BaseClass=CDialog
HeaderFile=MSEditorDlg.h
ImplementationFile=MSEditorDlg.cpp
LastObject=CMSEditorDlg

[CLS:CPage_Item]
Type=0
BaseClass=CMyPropertyPage
HeaderFile=Page_Item.h
ImplementationFile=Page_Item.cpp

[CLS:CPage_Risist]
Type=0
BaseClass=CMyPropertyPage
HeaderFile=Page_Risist.h
ImplementationFile=Page_Risist.cpp
LastObject=IDC_RISIST_RESET
Filter=D
VirtualFilter=idWC

[CLS:CPage_Status]
Type=0
BaseClass=CMyPropertyPage
HeaderFile=Page_Status.h
ImplementationFile=Page_Status.cpp

[CLS:CPage_Trophy]
Type=0
BaseClass=CMyPropertyPage
HeaderFile=Page_Trophy.h
ImplementationFile=Page_Trophy.cpp
Filter=D
VirtualFilter=idWC
LastObject=IDC_TROPHY_SEPITH_CHI_SPIN

[DLG:IDD_MSEDITOR]
Type=1
Class=CMSEditorDlg
ControlCount=13
Control1=IDC_OPEN,button,1342246657
Control2=IDC_SAVE,button,1342246656
Control3=IDC_FILE,edit,1350633472
Control4=IDC_NAME,edit,1350631552
Control5=IDC_LEVEL,edit,1350639616
Control6=IDC_AS,edit,1350631552
Control7=IDC_EXP,edit,1350639744
Control8=IDC_S_NAME,static,1342308865
Control9=IDC_S_LEVEL,static,1342308865
Control10=IDC_S_AS,static,1342308865
Control11=IDC_S_EXP,static,1342308865
Control12=IDC_STATIC_FILE,button,1342177287
Control13=IDC_STATIC_DATA,button,1342177287

[DLG:IDD_PAGE_ITEM]
Type=1
Class=CPage_Item
ControlCount=21
Control1=IDCANCEL,button,1073807360
Control2=IDC_STATIC,button,1342177287
Control3=IDC_STATIC,button,1342177287
Control4=IDC_ITEM_EQUIP1,combobox,1344339970
Control5=IDC_ITEM_EQUIP2,combobox,1344339970
Control6=IDC_ITEM_EQUIP3,combobox,1344339970
Control7=IDC_ITEM_EQUIP4,combobox,1344339970
Control8=IDC_ITEM_EQUIP5,combobox,1344339970
Control9=IDC_ITEM_ORB1,combobox,1344339970
Control10=IDC_ITEM_ORB2,combobox,1344339970
Control11=IDC_ITEM_ORB3,combobox,1344339970
Control12=IDC_ITEM_ORB4,combobox,1344339970
Control13=IDC_ITEM_EQUIP_ID1,edit,1350631560
Control14=IDC_ITEM_EQUIP_ID2,edit,1350631560
Control15=IDC_ITEM_EQUIP_ID3,edit,1350631560
Control16=IDC_ITEM_EQUIP_ID4,edit,1350631560
Control17=IDC_ITEM_EQUIP_ID5,edit,1350631560
Control18=IDC_ITEM_ORB_ID1,edit,1350631560
Control19=IDC_ITEM_ORB_ID2,edit,1350631560
Control20=IDC_ITEM_ORB_ID3,edit,1350631560
Control21=IDC_ITEM_ORB_ID4,edit,1350631560

[DLG:IDD_PAGE_RISIST]
Type=1
Class=CPage_Risist
ControlCount=38
Control1=IDC_RISIST_POISON,button,1342242819
Control2=IDC_RISIST_FREEZE,button,1342242819
Control3=IDC_RISIST_PETRIFACTION,button,1342242819
Control4=IDC_RISIST_SLEEP,button,1342242819
Control5=IDC_RISIST_NOMAG,button,1342242819
Control6=IDC_RISIST_DARK,button,1342243075
Control7=IDC_RISIST_NOCFT,button,1342242819
Control8=IDC_RISIST_CHAOS,button,1342242819
Control9=IDC_RISIST_FAINT,button,1342242819
Control10=IDC_RISIST_ONEHIT,button,1342242819
Control11=IDC_RISIST_DEFDOWN,button,1342242819
Control12=IDC_RISIST_ANGER,button,1342242819
Control13=IDC_RISIST_ARTSGUARD,button,1342242819
Control14=IDC_RISIST_CRAFTGUARD,button,1342242819
Control15=IDC_RISIST_MOVUP,button,1342242819
Control16=IDC_RISIST_MOVDOWN,button,1342242819
Control17=IDC_RISIST_STRUP,button,1342242819
Control18=IDC_RISIST_STRDOWN,button,1342242819
Control19=IDC_RISIST_DEFUP,button,1342242819
Control20=IDC_RISIST_DEFDOWN2,button,1342242819
Control21=IDC_RISIST_SPDUP,button,1342242819
Control22=IDC_RISIST_SPDDOWN,button,1342242819
Control23=IDC_RISIST_ADFUP,button,1342242819
Control24=IDC_RISIST_ADFDOWN,button,1342242819
Control25=IDC_RISIST_AGLUP,button,1342242819
Control26=IDC_RISIST_AGLDOWN,button,1342242819
Control27=IDC_RISIST_MAXGUARD,button,1342242819
Control28=IDC_RISIST_VANISH,button,1342242819
Control29=IDC_RISIST_CG,button,1342242819
Control30=IDC_RISIST_FAT,button,1342242819
Control31=IDC_RISIST_ATSUP,button,1342242819
Control32=IDC_RISIST_FORCEDEAD,button,1476460547
Control33=IDCANCEL,button,1073807360
Control34=IDC_RISIST_SELALL,button,1342242816
Control35=IDC_RISIST_SELNONE,button,1342242816
Control36=IDC_RISIST_CUSTOM,button,1342242816
Control37=IDC_RISIST_CUS,edit,1082195976
Control38=IDC_RISIST_RESET,button,1342242816

[DLG:IDD_PAGE_STATUS]
Type=1
Class=CPage_Status
ControlCount=49
Control1=IDC_STATUS_HP_UP,edit,1350639744
Control2=IDC_STATUS_EP_UP,edit,1350639744
Control3=IDC_STATUS_CP_UP,edit,1350639744
Control4=IDC_STATUS_HP_DEF,edit,1350631552
Control5=IDC_STATUS_EP_DEF,edit,1350631552
Control6=IDC_STATUS_CP_DEF,edit,1350631552
Control7=IDC_STATUS_STR,edit,1350639744
Control8=IDC_STATUS_DEF,edit,1350639744
Control9=IDC_STATUS_ATS,edit,1350639744
Control10=IDC_STATUS_ADF,edit,1350631552
Control11=IDC_STATUS_SPD,edit,1350631552
Control12=IDC_STATUS_DEX,edit,1350631552
Control13=IDC_STATUS_AGL,edit,1350639744
Control14=IDC_STATUS_MOV,edit,1350639744
Control15=IDC_STATUS_RNG,edit,1350639744
Control16=IDC_STATUS_MOVSPD,edit,1350631552
Control17=IDC_STATUS_S_HP_UP,static,1342308864
Control18=IDC_STATUS_S_EP_UP,static,1342308865
Control19=IDC_STATUS_S_CP_UP,static,1342308865
Control20=IDC_STATUS_S_HP_DEF,static,1342308865
Control21=IDC_STATUS_S_EP_DEF,static,1342308865
Control22=IDC_STATUS_S_CP_DEF,static,1342308865
Control23=IDC_STATUS_S_STR,static,1342308865
Control24=IDC_STATUS_S_DEF,static,1342308865
Control25=IDC_STATUS_S_ATS,static,1342308865
Control26=IDC_STATUS_S_ADF,static,1342308865
Control27=IDC_STATUS_S_SPD,static,1342308865
Control28=IDC_STATUS_S_DEX,static,1342308865
Control29=IDC_STATUS_S_AGL,static,1342308865
Control30=IDC_STATUS_S_MOV,static,1342308865
Control31=IDC_STATUS_S_RNG,static,1342308865
Control32=IDC_STATUS_S_MOVSPD,static,1342308865
Control33=IDCANCEL,button,1073807360
Control34=IDC_STATIC,button,1342177287
Control35=IDC_STATIC,button,1342177287
Control36=IDC_STATUS_CHI_SPIN,msctls_updown32,1342177318
Control37=IDC_STATUS_CHI,edit,1350631552
Control38=IDC_STATUS_MIZU,edit,1350631552
Control39=IDC_STATUS_HI_SPIN,msctls_updown32,1342177318
Control40=IDC_STATUS_HI,edit,1350631552
Control41=IDC_STATUS_KAZE_SPIN,msctls_updown32,1342177318
Control42=IDC_STATUS_KAZE,edit,1350631552
Control43=IDC_STATUS_TOKI_SPIN,msctls_updown32,1342177318
Control44=IDC_STATUS_TOKI,edit,1350631552
Control45=IDC_STATUS_SORA_SPIN,msctls_updown32,1342177318
Control46=IDC_STATUS_SORA,edit,1350631552
Control47=IDC_STATUS_GEN_SPIN,msctls_updown32,1342177318
Control48=IDC_STATUS_GEN,edit,1350631552
Control49=IDC_STATUS_MIZU_SPIN,msctls_updown32,1342177318

[DLG:IDD_PAGE_TROPHY]
Type=1
Class=CPage_Trophy
ControlCount=19
Control1=IDCANCEL,button,1073807360
Control2=IDC_TROPHY_SEPITH_CHI_SPIN,msctls_updown32,1342177318
Control3=IDC_TROPHY_SEPITH_CHI,edit,1350631552
Control4=IDC_TROPHY_SEPITH_MIZU,edit,1350631552
Control5=IDC_TROPHY_SEPITH_HI_SPIN,msctls_updown32,1342177318
Control6=IDC_TROPHY_SEPITH_HI,edit,1350631552
Control7=IDC_TROPHY_SEPITH_KAZE_SPIN,msctls_updown32,1342177318
Control8=IDC_TROPHY_SEPITH_KAZE,edit,1350631552
Control9=IDC_TROPHY_SEPITH_TOKI_SPIN,msctls_updown32,1342177318
Control10=IDC_TROPHY_SEPITH_TOKI,edit,1350631552
Control11=IDC_TROPHY_SEPITH_SORA_SPIN,msctls_updown32,1342177318
Control12=IDC_TROPHY_SEPITH_SORA,edit,1350631552
Control13=IDC_TROPHY_SEPITH_GEN_SPIN,msctls_updown32,1342177318
Control14=IDC_TROPHY_SEPITH_GEN,edit,1350631552
Control15=IDC_TROPHY_SEPITH_MIZU_SPIN,msctls_updown32,1342177318
Control16=65535,button,1342177287
Control17=65535,button,1342177287
Control18=IDC_TROPHY_DROP1,edit,1350631552
Control19=IDC_TROPHY_DROP2,edit,1350631552

[CLS:CPage_Magic]
Type=0
HeaderFile=Page_Magic.h
ImplementationFile=Page_Magic.cpp
BaseClass=CPropertyPage
Filter=D
LastObject=IDC_LIST1
VirtualFilter=idWC

[CLS:CPage_Skill]
Type=0
HeaderFile=Page_Skill.h
ImplementationFile=Page_Skill.cpp
BaseClass=CPropertyPage
Filter=D
LastObject=IDC_SKILL_EDIT
VirtualFilter=idWC

[DLG:IDD_PAGE_SKILL]
Type=1
Class=CPage_Magic
ControlCount=7
Control1=IDC_SKILL_ADD,button,1342242816
Control2=IDC_SKILL_EDIT,button,1342242816
Control3=IDC_SKILL_DELETE,button,1342242816
Control4=IDC_SKILL_MOVEUP,button,1342242816
Control5=IDC_SKILL_MOVEDOWN,button,1342242816
Control6=IDC_SKILL_LIST,SysListView32,1350664205
Control7=IDCANCEL,button,1073807360

[CLS:CMyClistCtrl]
Type=0
HeaderFile=MyClistCtrl.h
ImplementationFile=MyClistCtrl.cpp
BaseClass=CListCtrl
Filter=W
LastObject=CMyClistCtrl

[CLS:CMyListCtrl]
Type=0
HeaderFile=MyListCtrl.h
ImplementationFile=MyListCtrl.cpp
BaseClass=CListCtrl
Filter=W
LastObject=CMyListCtrl

[CLS:CAIEditor]
Type=0
HeaderFile=AIEditor.h
ImplementationFile=AIEditor.cpp
BaseClass=CDialog
Filter=D
LastObject=IDC_SKILL_PROPERTY
VirtualFilter=dWC

[DLG:IDD_AIEDITOR]
Type=1
Class=?
ControlCount=17
Control1=IDC_SKILL_PROPERTY,combobox,1344348482
Control2=IDOK,button,1342242817
Control3=IDCANCEL,button,1342242816
Control4=IDC_STATIC,button,1342177287
Control5=IDC_STATIC,button,1342177287
Control6=IDC_SKILL_ID,combobox,1344348418
Control7=IDC_SKILL_NAME,edit,1350631552
Control8=IDC_STATIC,static,1342308865
Control9=IDC_SKILL_CONDITION,combobox,1344340226
Control10=IDC_SKILL_PARAM1,edit,1350631552
Control11=IDC_STATIC,static,1342308865
Control12=IDC_SKILL_PARAM1_ISHEX,button,1342242819
Control13=IDC_STATIC,static,1342308865
Control14=IDC_SKILL_TARGET,combobox,1344340226
Control15=IDC_SKILL_PARAM2,edit,1350631552
Control16=IDC_STATIC,static,1342308865
Control17=IDC_SKILL_PARAM2_ISHEX,button,1342242819
