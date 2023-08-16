
#pragma comment(linker, "/ENTRY:WinMain")
#pragma comment(linker, "/MERGE:.text=.Hiromi /SECTION:.Hiromi,ERW")
#pragma comment(linker, "/MERGE:.rdata=.Hiromi")
#pragma comment(lib, "shlwapi.lib")
#pragma warning(disable:4309)

#include <Windows.h>
#include <Shlwapi.h>
#include "my_mem.h"
#include "AllocPieces/header.h"
#include "ED63Loader.h"

extern "C"
{
	#include "LzmaDec.h"
	#include "7zAlloc.h"
	extern HANDLE hHeap = INVALID_HANDLE_VALUE;
}

BOOL CALLBACK EnumWindowsProc(HWND hWnd,LPARAM lParam);
void WritePieces(HANDLE hProcess);
void CenterWindow(HANDLE hProcess);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmd, int nShow)
{
	{
		char szPath[MAX_PATH];
		GetModuleFileNameA(NULL, szPath, sizeof(szPath));
		*(PathFindFileNameA(szPath)) = 0;
//		*StrRChrA(szPath, NULL, '\\') = 0;
		SetCurrentDirectoryA(szPath);
	}

	lpCmd = GetCommandLineA() + 1;
	while (*lpCmd++ != '"');
	STARTUPINFOA si;
	PROCESS_INFORMATION pi;

	Zero_Memory(&si, sizeof(si));
	si.cb = sizeof(si);
	if ( !CreateProcessA("ed6_win3.bin", lpCmd, NULL,
				NULL, TRUE, CREATE_SUSPENDED, NULL, NULL, &si, &pi) )
	{
		return 0;
	}

//	WritePieces(pi.hProcess);

	DWORD	dwBaseAddress;
	Byte	*pbyOutBuffer;
	SizeT	sizeMaxSize = 0, outSize = 0;

	hHeap		 = GetProcessHeap();
	pbyOutBuffer = (Byte *)HeapAlloc(hHeap, 0, 0);

	UInt64	outSize64;
	SizeT	inSize;
	Byte	*inBuffer;

	for (size_t ix = 0; ix != sizeof(Array_of_Data) / sizeof(tagArray_of_Data); ++ix)
	{
		Lzma86_GetUnpackSize((Byte *)(Array_of_Data[ix].data),
						Array_of_Data[ix].nSize,
						&outSize64);

		outSize = (SizeT)outSize64;
		if (outSize > sizeMaxSize)
		{
			sizeMaxSize = outSize;
			pbyOutBuffer = (Byte *)HeapReAlloc(hHeap, 0, pbyOutBuffer, sizeMaxSize);
		}

		inSize   = Array_of_Data[ix].nSize;
		inBuffer = (Byte *)Array_of_Data[ix].data;
		Lzma86_Decode(pbyOutBuffer, &outSize, inBuffer, &inSize);

		dwBaseAddress = *(DWORD *)pbyOutBuffer;
		outSize -= 4;
		dwBaseAddress = (DWORD)VirtualAllocEx(pi.hProcess,
				(LPVOID)dwBaseAddress,
				outSize,
				MEM_COMMIT|MEM_RESERVE,
				PAGE_EXECUTE_READWRITE);

		if (dwBaseAddress)
		{
			WriteProcessMemory(pi.hProcess,
				(LPVOID)dwBaseAddress,
				pbyOutBuffer + 4,
				outSize,
				0);
		}
	}

	for (WORD ix = 0; ix != sizeof(WriteData) / sizeof(tagWriteData); ++ix)
	{
		WriteProcessMemory(pi.hProcess, (LPVOID)WriteData[ix].dwAddress,
			WriteData[ix].data, WriteData[ix].dwSize, NULL);
	}

	HeapFree(hHeap, 0, pbyOutBuffer);

	ResumeThread(pi.hThread);
//	CenterWindow(pi.hProcess);
//	EnumWindows(&EnumWindowsProc,0);
	return 0;
}

void WritePieces(HANDLE hProcess)
{
	DWORD	dwBaseAddress;
	Byte	*pbyOutBuffer;
	SizeT	sizeMaxSize = 0, outSize = 0;

	hHeap		 = GetProcessHeap();
	pbyOutBuffer = (Byte *)HeapAlloc(hHeap, 0, 0);

	UInt64	outSize64;
	SizeT	inSize;
	Byte	*inBuffer;

	for (size_t ix = 0; ix != sizeof(Array_of_Data) / sizeof(tagArray_of_Data); ++ix)
	{
		Lzma86_GetUnpackSize((Byte *)(Array_of_Data[ix].data),
			Array_of_Data[ix].nSize,
			&outSize64);

		outSize = (SizeT)outSize64;
		if (outSize > sizeMaxSize)
		{
			sizeMaxSize = outSize;
			pbyOutBuffer = (Byte *)HeapReAlloc(hHeap, 0, pbyOutBuffer, sizeMaxSize);
		}

		inSize   = Array_of_Data[ix].nSize;
		inBuffer = (Byte *)Array_of_Data[ix].data;
		Lzma86_Decode(pbyOutBuffer, &outSize, inBuffer, &inSize);

		dwBaseAddress = *(DWORD *)pbyOutBuffer;
		outSize -= 4;
		dwBaseAddress = (DWORD)VirtualAllocEx(hProcess,
			(LPVOID)dwBaseAddress,
			outSize,
			MEM_COMMIT|MEM_RESERVE,
			PAGE_EXECUTE_READWRITE);

		if (dwBaseAddress)
		{
			WriteProcessMemory(hProcess,
				(LPVOID)dwBaseAddress,
				pbyOutBuffer + 4,
				outSize,
				0);
		}
	}
	WriteProcessMemory(hProcess, (LPVOID)0x54A6DD, "\x7", 1, NULL);
	HeapFree(hHeap, 0, pbyOutBuffer);
}

void CenterWindow(HANDLE hProcess)
{
	DWORD dwRead;
	WORD wCount = 0;
	HWND hWnd;
	do
	{
		Sleep(100);
		if (wCount == 0x7FFF) return;
		ReadProcessMemory(hProcess, (LPVOID)0x2E0E250, &hWnd, sizeof(HWND), &dwRead);
		++wCount;
	} while (hWnd == NULL);

	int		x, y;
	RECT	rcGame, rcSys;

	SystemParametersInfoA(SPI_GETWORKAREA, 0, &rcSys, 0);
	GetWindowRect(hWnd, &rcGame);
	x = ((rcSys.right - rcSys.left) - (rcGame.right - rcGame.left)) >> 1;
    y = ((rcSys.bottom - rcSys.top) - (rcGame.bottom - rcGame.top)) >> 1;
	SetWindowPos(hWnd, HWND_TOP, x, y, 0, 0, SWP_NOSIZE);
}


/*
BOOL CALLBACK EnumWindowsProc(HWND hWnd,LPARAM lParam)
{
	if (GetWindowThreadProcessId(hWnd, NULL) == pi.dwThreadId)
	{
		hShareWnd = hWnd;
	}
	return TRUE;
}
*/
