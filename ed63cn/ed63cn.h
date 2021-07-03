#include <Windows.h>
#include <Shlwapi.h>
#include "my_headers.h"

#define CP_CUR	0x278
#define CP_UP	0x290
#define LV		0x268
#define STR		0x280
#define DEF		0x282
#define ATS		0x284
#define ADF		0x286
#define SPD		0x28E
#define MOV		0x28C

#pragma pack(1)
typedef struct
{
	CHAR  szName[MAX_PATH];
	struct
	{
		BYTE by_Number_of_Characters;
		BYTE by_Color_Map_Type;
		BYTE by_Image_Type_Code;
		WORD w_Color_Map_Origin;
		WORD w_Color_Map_Length;
		BYTE by_Color_Map_Entry_Size;
		WORD w_X_of_Image;
		WORD w_Y_of_Image;
		WORD wWidth;
		WORD wHeight;
		BYTE by_Image_Pixel_Size;
		BYTE by_Image_Descriptor;
	} TTGAHeader;
	WORD  wReserve;
	DWORD dwVal1;
	DWORD dwVal2;
	DWORD dwVal[4];
	PBYTE pbFont[3];
	CHAR  cReserve[0x144];
} LGFont;
#pragma pack()

Void  WINAPI SafeGetSize();
DWORD CDECL  DecodeFile(PBYTE *ppbDest, PBYTE *ppbSrc);
DWORD CDECL  DecodeOrig(PBYTE *ppbDest, PBYTE *ppbSrc);
BOOL  CDECL  ShowGameWindow(BOOL bShow);

Void  WINAPI DisplayStatus();
Void  WINAPI SetFrameSize(DWORD x, DWORD y, DWORD w, DWORD h);
Void  WINAPI PrintText(int x, int y, LPSTR lpText, int dwColor, int fnWeight);

Void  SetLogFontData(DWORD *dwArray, PLOGFONT pLogfont);
Void  GetLogFontData(DWORD *dwArray, PLOGFONT pLogfont);
LONG  InitLGFont(CHAR *szFontName, LGFont *pLGFont, bool bRead);
DWORD ReadFileToBuffer(LPSTR szName, PBYTE pbBuffer, DWORD dwOffset, DWORD nBytesToRead, LPVOID, LPVOID, LPVOID, LPVOID, LPVOID);
Void  ChangeFont();

int    CDECL  mysprintf(char *szDest, const char *szFormat, DWORD dwIndex);
HANDLE WINAPI MyOpenMutexA(DWORD dwDesiredAccess, BOOL bInheritHandle, LPCSTR lpName);
BOOL   WINAPI MyPeekMessageA(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg);

/*
char *szConfigKeys[] =
{
	"Height",
	"Width",
	"Escapement",
	"Orientation",
	"Weight",
	"Italic",
	"Underline",
	"StrikeOut",
	"CharSet",
	"OutPrecision",
	"ClipPrecision",
	"Quality",
	"PitchAndFamily",
};
*/