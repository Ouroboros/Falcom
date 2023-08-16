#ifndef _ZWEI2PLUS_H_
#define _ZWEI2PLUS_H_

#include "MyLibrary.h"

typedef struct
{
    WChar Orig;
    WChar Relpace;
} TCharMap;

Void  Init();
DWORD CDECL  Mystrncpy(LPSTR lpDest, LPSTR lpSource, DWORD dwLength);
Void  WINAPI ProcessCharName(LPSTR lpString1, LPCSTR lpString2);
Void  WINAPI ProcessNiikki(LPSTR lpString1, LPCSTR lpString2);
LPSTR CDECL  ProcessBuildingName(LPSTR pbBuffer);
int   CDECL  Mywvsprintf(LPSTR *lpOutput, LPSTR lpFmt, va_list arglist);
BOOL  WINAPI MySetWindowPos(HWND hWnd, HWND hWndInsertAfter, int X, int Y, int cx, int cy, UINT uFlags);
BOOL  WINAPI MyPeekMessageA(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg);
DWORD WINAPI GetCharSurface(PBYTE pbSurface, LONG lHeight, int iOffset, UINT uChar, DWORD dwColor, DWORD dwColor2);
HANDLE  WINAPI MyCreateFileA(LPSTR lpFileName, DWORD dwDesiredAccess, DWORD dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, DWORD dwCreationDisposition, DWORD dwFlagsAndAttributes, HANDLE hTemplateFile);


#endif /* _ZWEI2PLUS_H_ */