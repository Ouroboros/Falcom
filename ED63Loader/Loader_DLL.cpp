#pragma comment(linker, "/ENTRY:DllEntryPoint")
#pragma comment(linker, "/MERGE:.text=.Rimi /SECTION:.Rimi,ERW")
#pragma comment(linker, "/MERGE:.rdata=.Rimi")
#pragma comment(lib, "shlwapi.lib")
#pragma comment(lib, "d3d8.lib")
#pragma warning(disable:4309)

#include <Windows.h>
#include <Shlwapi.h>
#include <d3d8.h>
#include "AllocPieces/header.h"

extern "C" {

#include "LzmaDec.h"
#include "7zAlloc.h"
HANDLE hHeap = INVALID_HANDLE_VALUE;

}

void WritePieces(HANDLE hProcess);

int WINAPI DllEntryPoint(HINSTANCE hinst, unsigned long reason, void* lpReserved)
{
	WritePieces(HANDLE(-1));
	return 1;
}

void WritePieces(HANDLE hProcess)
{
	DWORD	dwBaseAddress, dwOld;
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
		VirtualAllocEx(hProcess,
			(LPVOID)dwBaseAddress,
			outSize,
			MEM_COMMIT,
			PAGE_EXECUTE_READWRITE);

		VirtualProtectEx(hProcess, (LPVOID)dwBaseAddress,
			outSize, PAGE_EXECUTE_READWRITE, &dwOld);

		WriteProcessMemory(hProcess,
				(LPVOID)dwBaseAddress,
				pbyOutBuffer + 4,
				outSize,
				0);
	}
	WriteProcessMemory(hProcess, (LPVOID)0x54A6DD, "\x7", 1, NULL);
	HeapFree(hHeap, 0, pbyOutBuffer);
}