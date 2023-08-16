// 3rdDlg.cpp : implementation file

#include "stdafx.h"
#include "3rd.h"
#include "3rdDlg.h"
#include <bitset>
#include <string>
#include "AS04540.h"
#include "AS04455.h"
#include "MS04450.h"
#include "MS04455.h"
#include "U7000.h"
#include "Length.h"
using std::bitset;
using std::string;

#pragma comment(linker,"/ALIGN:4096")

/*
#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif*/
//////////////////////////////////////////////////////////////////////////
const unsigned char Kuro[]="莱维";
bitset<8> EnemyNum(0);
//////////////////////////////////////////////////////////////////////////
CMy3rdDlg::CMy3rdDlg(CWnd* pParent)
: CDialog(CMy3rdDlg::IDD, pParent)
{
}

BEGIN_MESSAGE_MAP(CMy3rdDlg, CDialog)
ON_WM_TIMER()
ON_WM_DESTROY()
ON_LBN_SELCHANGE(IDC_LIST1, CMy3rdDlg::OnLbnSelchangeList1)
END_MESSAGE_MAP()

BOOL CMy3rdDlg::OnInitDialog()
{
	CDialog::OnInitDialog();
	isbattle=0;SBreak=0xFFFF;LastMem=0x10;_0Bstatus=0;RiesLen=0;
	RiesAdd=0;snadd=0;Dir30=0;YLen=0;KLen=0;YAdd=0;KAdd=0;MemberID=1;
	CListBox *pCtrl = (CListBox *)GetDlgItem(IDC_LIST1);
	pCtrl->AddString(_T("艾斯蒂尔")); 
	pCtrl->AddString(_T("约修亚")); 
	pCtrl->AddString(_T("雪拉扎德")); 
	pCtrl->AddString(_T("奥利维尔")); 
	pCtrl->AddString(_T("科洛蒂亚")); 
	pCtrl->AddString(_T("阿加特")); 
	pCtrl->AddString(_T("提妲")); 
	pCtrl->AddString(_T("金")); 
	pCtrl->AddString(_T("凯文")); 
	pCtrl->AddString(_T("亚妮拉丝")); 
	pCtrl->AddString(_T("乔斯特")); 
	pCtrl->AddString(_T("理查德")); 
	pCtrl->AddString(_T("穆拉")); 
	pCtrl->AddString(_T("尢莉亚")); 
	pCtrl->AddString(_T("莉丝")); 
	pCtrl->AddString(_T("铃")); 
	pCtrl->AddString(_T("无")); 
	pCtrl->SetCurSel(MemberID);
	pCtrl->SetColumnWidth(60);
	On_start();
	return TRUE;
}

void CMy3rdDlg::On_start()
{
	unsigned nIDEvent;
	for(nIDEvent=1;nIDEvent!=17;++nIDEvent)		//全16人正常使用S技
		SetTimer(nIDEvent,100,NULL);
	SetTimer(17,50,NULL);						//main
	SetTimer(101,200,NULL);						//SN file
}

void CMy3rdDlg::sora3(unsigned nIDEvent)
{
	WORD isbattle=0,next;
	DWORD Head=HeadAdd+(nIDEvent-1)*0x2490;
	ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x14),&isbattle,1,NULL);
	for(next=0;isbattle&&next<=0x18*5;next+=0x18)
	{
		WORD existcft,selcft,scftani,isscraft;
		ReadProcessMemory(hProcess,LPVOID(Head+0x18A),&selcft,2,NULL);//当前选中战技
		ReadProcessMemory(hProcess,LPVOID(Head+0xDFE+next),&existcft,2,NULL);//检测现有战技
		if(selcft==existcft&&selcft)
		{
			ReadProcessMemory(hProcess,LPVOID(Head+0xDFE+next-1),&scftani,1,NULL);
			WriteProcessMemory(hProcess,(void*)(Head+0xE73),(void*)&(scftani),1,NULL);
			if(ReadProcessMemory(hProcess,LPVOID(Head+0x17E),&isscraft,1,NULL),isscraft!=4)
				WriteProcessMemory(hProcess,(void*)(Head+0x17E),(void*)&(isscraft=0x04),1,NULL);//S技判定
			next=0x18*6;
		}
	}
}

void CMy3rdDlg::sora3_fenshen()
{
	ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x14),&isbattle,1,NULL);
	if(isbattle) ((CListBox *)GetDlgItem(IDC_LIST1))->EnableWindow(0);
	else ((CListBox *)GetDlgItem(IDC_LIST1))->EnableWindow(1);
	WORD ChkMem=0,Chksn=0;
	if(MemberID!=0x10)
		for(;Chksn!=4;++Chksn)
		{
			ReadProcessMemory(hProcess,LPVOID(MemberAdd+4*Chksn),&ChkMem,2,NULL);
			if(MemberID==ChkMem) break;
		}
	if(!Dir30)
		ReadProcessMemory(hProcess,LPVOID(DirAdd+0x30*4),&Dir30,4,NULL);
	if(LastMem!=MemberID)
	{
		if(!KLen)
		{			
			ReadProcessMemory(hProcess,LPVOID(Dir30+0x5E24),&KLen,4,NULL);	//黑骑士长度
			ReadProcessMemory(hProcess,LPVOID(Dir30+0x5E34),&KAdd,4,NULL);	//黑骑士地址
		}
		if(LastMem!=0x10&&YLen)
		{
			if(LastMem==0x0E)
			{
				WriteProcessMemory(hProcess,(void*)(Dir30+0xC220),(void*)&RiesLen,4,NULL);
				WriteProcessMemory(hProcess,(void*)(Dir30+0xC230),(void*)&RiesAdd,4,NULL);
			}
			WriteProcessMemory(hProcess,(void*)(Dir30+located[LastMem]),(void*)&YLen,4,NULL);//还原长度
			WriteProcessMemory(hProcess,(void*)(Dir30+located[LastMem]+0x10),(void*)&YAdd,4,NULL);//还原地址
		}
		if(MemberID!=0x10)
		{
			if(MemberID==0x0E)
			{
				ReadProcessMemory(hProcess,LPVOID(Dir30+0xC220),&RiesLen,4,NULL);	//备份长度
				ReadProcessMemory(hProcess,LPVOID(Dir30+0xC230),&RiesAdd,4,NULL);	//备份地址
				WriteProcessMemory(hProcess,(void*)(Dir30+0xC220),(void*)&KLen,4,NULL);
				WriteProcessMemory(hProcess,(void*)(Dir30+0xC230),(void*)&KAdd,4,NULL);
			}
			ReadProcessMemory(hProcess,LPVOID(Dir30+located[MemberID]),&YLen,4,NULL);	//备份长度
			ReadProcessMemory(hProcess,LPVOID(Dir30+located[MemberID]+0x10),&YAdd,4,NULL);	//备份地址
			WriteProcessMemory(hProcess,(void*)(Dir30+located[MemberID]),(void*)&KLen,4,NULL);//写入长度
			WriteProcessMemory(hProcess,(void*)(Dir30+located[MemberID]+0x10),(void*)&KAdd,4,NULL);//写入地址
		}
		LastMem=MemberID;
	}
	if(MemberID!=0x10)
	{
	if(MemberID==ChkMem)
	{
		static bool fen=0;
		BYTE writed;
		ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x14),&isbattle,1,NULL);
		if(isbattle)
		{
			WORD SBrk=0x3E9;
			DWORD Head=HeadAdd+0x2490*Chksn;
			if(SBreak==0xFFFF)
				ReadProcessMemory(hProcess,LPVOID(MemberAdd+0x8C80+MemberID*2),&SBreak,2,NULL);
			WriteProcessMemory(hProcess,(void*)(MemberAdd+0x8C80+MemberID*2),(void*)&SBrk,2,NULL);
			for(size_t index=0;index!=8;++index)
			{
				BYTE chkemy=0;
				ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x12480+0x3+0x2490*index),&chkemy,1,NULL);
				if(chkemy!=0x80) EnemyNum.set(index);
				else EnemyNum.reset(index);
			}
			BYTE selcft;
			ReadProcessMemory(hProcess,LPVOID(Head+0x224),&NameAdd,4,NULL);
			while(ReadProcessMemory(hProcess,LPVOID(Head+0xD0E),&writed,1,NULL),
				writed!=MS04450[0xD0E])
			{
				WriteProcessMemory(hProcess,(void*)(HeadAdd-0xA13B8+0x4F10*Chksn),(void*)AS04450,sizeof(AS04450),NULL);
				WriteProcessMemory(hProcess,(void*)(Head+0x230),(void*)(MS04450+0x26C),0x8,NULL);
				WriteProcessMemory(hProcess,(void*)(Head+0x26C),(void*)(MS04450+0x26C),0x220,NULL);
				WriteProcessMemory(hProcess,(void*)(Head+0xD08),(void*)(MS04450+0xD08),0x16AF,NULL);
				WriteProcessMemory(hProcess,(void*)(NameAdd),(void*)Kuro,5,NULL);
			}
			BYTE tmpbyte=0;
			DWORD tmpval=0;
			static WORD place=0,ctrl=0;
			if( (ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x12494),&tmpval,4,NULL),tmpval!=0x3003BB)
				&&( (ReadProcessMemory(hProcess,LPVOID(Head+0x18A),&selcft,1,NULL),selcft==MS04450[0xD9E])
				&& (EnemyNum.count()<7||(EnemyNum.count()!=8 && EnemyNum.test(3))) )
				|| (ReadProcessMemory(hProcess,LPVOID(Head+0x2470),&ctrl,1,NULL),ctrl==1)
				)
			{
				if(!fen)
				{
					WriteProcessMemory(hProcess,(void*)(HeadAdd-0xA13B8+0x4F10*Chksn+0x73),(void*)&(tmpval=0x27102150),4,NULL);
					WriteProcessMemory(hProcess,(void*)(Xor),(void*)&(tmpval=0x89088A40),4,NULL);
					WriteProcessMemory(hProcess,(void*)(MSFile),(void*)&(tmpval=0x30056D),4,NULL);
					fen=1;
				}
				if(ReadProcessMemory(hProcess,LPVOID(Head+0x2470),&ctrl,1,NULL),ctrl==0)	//未分身
				{
					for(size_t index=0;index!=EnemyNum.size();++index)
					{
						if(index!=3&&!EnemyNum.test(index)) {place=index;break;}
						if(index==3&&!EnemyNum.test(index))
						{	//保存0B的状态
							if(!_0Bstatus)
								ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x19233),&_0Bstatus,4,NULL);
							WriteProcessMemory(hProcess,(void*)(HeadAdd+0x19233),(void*)&(tmpbyte=0x10),1,NULL);
						}
					}
				}
				else	//已分身
				{
					WORD clean=0;
					while(ReadProcessMemory(hProcess,LPVOID(HeadAdd+0x12480+place*0x2490+0xD56),&ctrl,1,NULL),ctrl!=MS04455[0xDE])
					{
						Sleep(200);
						WriteProcessMemory(hProcess,(void*)(HeadAdd-0xA13B8+8*0x4F10+place*0x4F10),(void*)AS04455,sizeof(AS04455),NULL);//AS
						WriteProcessMemory(hProcess,(void*)(HeadAdd+0x12480+place*0x2490+0x274),(void*)(MS04450+0x274),4,NULL);//EP
						WriteProcessMemory(hProcess,(void*)(HeadAdd+0x129CC+place*0x2490),(void*)MS04455,0x80,NULL);//Magic
						WriteProcessMemory(hProcess,(void*)(HeadAdd+0x12480+place*0x2490+0xD08),(void*)(MS04455+0x90),0xC70,NULL);//Craft
						Sleep(300);
					}
					if(_0Bstatus)
						WriteProcessMemory(hProcess,(void*)(HeadAdd+0x19233),(void*)&_0Bstatus,4,NULL);
					WriteProcessMemory(hProcess,(void*)(Head+0x18A),(void*)&clean,2,NULL);
					WriteProcessMemory(hProcess,(void*)(Head+0x2470),(void*)&(ctrl=0),1,NULL);
					_0Bstatus=0;
				}
			}
			else if(fen)
			{
				WriteProcessMemory(hProcess,(void*)(HeadAdd-0xA13B8+0x4F10*Chksn+0x73),(void*)&(tmpval=0x27102D50),4,NULL);
				WriteProcessMemory(hProcess,(void*)(Xor),(void*)&(tmpval=0x89088A10),4,NULL);
				WriteProcessMemory(hProcess,(void*)(MSFile),(void*)&(tmpval=0x3003BC),4,NULL);
				if(_0Bstatus)
				{
					WriteProcessMemory(hProcess,(void*)(HeadAdd+0x19233),(void*)&_0Bstatus,4,NULL);
					_0Bstatus=0;
				}
				fen=0;
			}
		}
		else if(SBreak!=0xFFFF)
		{
			WriteProcessMemory(hProcess,(void*)(MemberAdd+0x8C80+LastMem*2),(void*)&SBreak,2,NULL);//还原SBreak
			SBreak=0xFFFF;
		}
	}
	}
}

void CMy3rdDlg::DebugMenu()
{
	DWORD  Check=0;
	string SNname(5,'0');
	ReadProcessMemory(hProcess,LPVOID(SNPtr),&snadd,4,NULL);
	if((ReadProcessMemory(hProcess,LPVOID(snadd+0xA),
		static_cast<void*>(const_cast<char*>(SNname.c_str())),5,NULL),SNname=="U7000")
		&& (ReadProcessMemory(hProcess,LPVOID(snadd+0xDAE),&Check,4,NULL),Check==0x15F0C40))
	{
		DWORD Point;
		WriteProcessMemory(hProcess,(void*)(snadd+0xDAE),(void*)&(Point=0x15F2285),4,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0x20BF),(void*)&(Point=0x23702250),4,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0x2250),(void*)U7000,0x1D6,NULL);
	}
	else if(SNname=="T0001"
		&& (ReadProcessMemory(hProcess,LPVOID(snadd+0x8EF),&Check,4,NULL),Check==0x051392))
	{
		DWORD Point;
		WriteProcessMemory(hProcess,(void*)(snadd+0x8EF),(void*)&(Point=0x51840),4,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0xA37),(void*)&(Point=0xBB1850),4,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0x1840),(void*)&(Point=0x2103B906),4,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0x1845),(void*)&(Point=0x68),1,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0x1850),(void*)&(Point=0x0300015F),4,NULL);
		WriteProcessMemory(hProcess,(void*)(snadd+0x1855),(void*)&(Point=0x6F9),2,NULL);
	}
}

void CMy3rdDlg::OnTimer(UINT nIDEvent)
{
	HWND hWnd =::FindWindow(__T("Falcom"),NULL);
	DWORD openProcId;
	GetWindowThreadProcessId(hWnd,&openProcId);	
	hProcess = OpenProcess(PROCESS_ALL_ACCESS|PROCESS_TERMINATE|PROCESS_VM_OPERATION|PROCESS_VM_READ|PROCESS_VM_WRITE,FALSE,openProcId);
	if(hWnd)
	{
		push=0;
		ReadProcessMemory(hProcess,LPVOID(0x401027),&push,2,NULL);
		if(push==0x1953)
		{
			Xor=0x4145FB;
			MSFile=0x4144D0;
			MemberAdd=0x2D9177C;
			DirAdd=0x2CCE4B8;
			HeadAdd=0x6935C0;
			SNPtr=0x2CCD354;
		}
		else if(push==0x18AC)
		{
			Xor=0x4141AB;
			MSFile=0x414080;
			MemberAdd=0x2D6C7FC;
			DirAdd=0x2CA9538;
			HeadAdd=0x66E640;
			SNPtr=0x2CA83D4;
		}
		if(push==0x18AC||push==0x1953)
			if(nIDEvent&&nIDEvent<17) sora3(nIDEvent);
			else if(nIDEvent==17) sora3_fenshen();
//			else if(nIDEvent==101) DebugMenu();		
	}
	else
	{
		_0Bstatus=0;isbattle=0;SBreak=0xFFFF;Dir30=0;
		LastMem=0x10;
		YAdd=YLen=KLen=KAdd=0;
		((CListBox *)GetDlgItem(IDC_LIST1))->EnableWindow(1);
	}
	CDialog::OnTimer(nIDEvent);
}

void CMy3rdDlg::OnDestroy() 
{
	DWORD tmpval;
	WriteProcessMemory(hProcess,(void*)(HeadAdd-0xA13B8+0x73),(void*)&(tmpval=0x27102D50),4,NULL);
	WriteProcessMemory(hProcess,(void*)(Xor),(void*)&(tmpval=0x89088A10),4,NULL);
	WriteProcessMemory(hProcess,(void*)(MSFile),(void*)&(tmpval=0x3003BC),4,NULL);
	if(YLen)
	{
		WriteProcessMemory(hProcess,(void*)(Dir30+located[MemberID]),(void*)&YLen,4,NULL);//还原长度
		WriteProcessMemory(hProcess,(void*)(Dir30+located[MemberID]+0x10),(void*)&YAdd,4,NULL);//还原地址
	}
	if(SBreak!=0xFFFF)
		WriteProcessMemory(hProcess,(void*)(MemberAdd+0x8C80+MemberID*2),(void*)&SBreak,2,NULL);//还原SBreak
	if(_0Bstatus)
		WriteProcessMemory(hProcess,(void*)(HeadAdd+0x19233),(void*)&_0Bstatus,4,NULL);
	CDialog::OnDestroy();	
}

void CMy3rdDlg::OnLbnSelchangeList1()
{
	MemberID=((CListBox *)GetDlgItem(IDC_LIST1))->GetCurSel();
}
