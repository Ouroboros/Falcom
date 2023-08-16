#include "ed6fc.h"

using ml::String;

NTSTATUS
PatchAllReference(
    PVOID       startAddress,
    ULONG_PTR   searchRange,
    PVOID       textVa,
    PCSTR       newText,
    ULONG_PTR   length,
    BOOL        isDataSection
)
{
    PVOID endAddress;
    PBYTE reference;
    BOOL patched = FALSE;

    SEARCH_PATTERN_DATA stub[] =
    {
        ADD_PATTERN(&textVa),
    };

    endAddress = PtrAdd(startAddress, searchRange);

    while (startAddress < endAddress)
    {
        reference = (PBYTE)SearchPattern(stub, countof(stub), startAddress, PtrOffset(endAddress, startAddress));
        if (reference == nullptr)
            break;

        // mov r32, const
        // push const
        // mov dword ptr [r32+const], const
        if (isDataSection == TRUE ||
            (reference[-1] & 0xF0) == 0xB0 ||
            reference[-1] == 0x68 ||
            *(PUSHORT)&reference[-4] == 0x44C7)
        {
            *(PCSTR *)reference = newText;
            patched = TRUE;
        }

        startAddress = reference + sizeof(PVOID);
    }

    return patched ? STATUS_SUCCESS : STATUS_NOT_FOUND;
}

NTSTATUS PatchExeText(PVOID BaseAddress)
{
    NTSTATUS        status;
    ULONG           count, textProtection, dataProtection;
    PBYTE           buffer;
    PVOID           startAddress, dataAddress;
    ULONG_PTR       searchRange, dataRange;
    NtFileMemory*   textbin;

    PIMAGE_NT_HEADERS     ntHeaders   = ImageNtHeadersFast(BaseAddress);
    PIMAGE_SECTION_HEADER textSection = IMAGE_FIRST_SECTION(ntHeaders);
    PIMAGE_SECTION_HEADER dataSection = nullptr;

    static CHAR dataSectionName[sizeof(dataSection->Name)] = ".data";

    startAddress = PtrAdd(BaseAddress, textSection->VirtualAddress);
    searchRange = textSection->SizeOfRawData;

    dataAddress = 0;
    dataRange = 0;

    ++textSection;
    for (ULONG_PTR n = ntHeaders->FileHeader.NumberOfSections - 1; n; ++textSection, --n)
    {
        if (textSection->Characteristics == (IMAGE_SCN_CNT_INITIALIZED_DATA | IMAGE_SCN_MEM_READ | IMAGE_SCN_MEM_WRITE) ||
            RtlCompareMemory(textSection->Name, dataSectionName, sizeof(dataSectionName)) == sizeof(dataSectionName))
        {
            dataSection = textSection;
            dataAddress = PtrAdd(BaseAddress, dataSection->VirtualAddress);
            dataRange = dataSection->SizeOfRawData;
            break;
        }
    }

    status = Mm::ProtectMemory(CurrentProcess, startAddress, searchRange, PAGE_EXECUTE_READWRITE, &textProtection);
    FAIL_RETURN(status);

    SCOPE_EXIT
    {
        Mm::ProtectMemory(CurrentProcess, startAddress, searchRange, textProtection);
    }
    SCOPE_EXIT_END;

    status = Mm::ProtectMemory(CurrentProcess, dataAddress, dataRange, PAGE_EXECUTE_READWRITE, &dataProtection);
    FAIL_RETURN(status);

    SCOPE_EXIT
    {
        Mm::ProtectMemory(CurrentProcess, dataAddress, dataRange, dataProtection);
    }
    SCOPE_EXIT_END;

    textbin = new NtFileMemory();
    if (textbin == nullptr)
        return STATUS_NO_MEMORY;

    status = textbin->Open(L"ed6fc.text");
    if (NT_FAILED(status))
    {
        delete textbin;
        return status;
    }

    buffer = (PBYTE)textbin->GetBuffer();

    count = *(PULONG)buffer;
    buffer += sizeof(count);

    for (; count; count--)
    {
        ULONG_PTR rva, length;

        rva = *(PULONG)buffer;
        buffer += sizeof(ULONG);

        length = *(PULONG)buffer;
        buffer += sizeof(PULONG);

        if (rva & 0x80000000)
        {
            *(PVOID *)PtrAdd(BaseAddress, rva & 0x7FFFFFFF) = buffer;
        }
        else if (rva != 0)
        {
            PatchAllReference(
                startAddress,
                searchRange,
                PtrAdd(BaseAddress, rva),
                (PCSTR)buffer,
                length,
                FALSE
            );

            if (dataSection != nullptr)
            {
                PatchAllReference(
                    dataAddress,
                    dataRange,
                    PtrAdd(BaseAddress, rva),
                    (PCSTR)buffer,
                    length,
                    TRUE
                );
            }
        }

        buffer += (length + 3) & ~3;
    }

    return status;
}
