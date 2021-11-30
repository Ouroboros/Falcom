export const Modules = {
    KERNEL32    : Process.getModuleByName('KERNEL32.dll'),
    USER32      : Process.getModuleByName('USER32.dll'),
    ucrtbase    : Process.getModuleByName('ucrtbase.dll'),
    ED83        : Process.getModuleByName('ed8_3_PC.exe'),
};

export const API = {
    crt: {
        fopen           : new NativeFunction(Modules.ucrtbase.getExportByName('fopen'), 'pointer', ['pointer', 'pointer'], 'win64'),
        fread           : new NativeFunction(Modules.ucrtbase.getExportByName('fread'), 'size_t', ['pointer', 'size_t', 'size_t', 'pointer'], 'win64'),
        fclose          : new NativeFunction(Modules.ucrtbase.getExportByName('fclose'), 'void', ['pointer'], 'win64'),
        _fileno         : new NativeFunction(Modules.ucrtbase.getExportByName('_fileno'), 'int32', ['pointer'], 'win64'),
        _filelengthi64  : new NativeFunction(Modules.ucrtbase.getExportByName('_filelengthi64'), 'uint64', ['int32'], 'win64'),
    },

    WIN32: {
        GetFileAttributesA: new NativeFunction(Modules.KERNEL32.getExportByName('GetFileAttributesA'), 'uint32', ['pointer']),
    },
};

export const Addrs = {
    LoadTableData           : Modules.ED83.base.add(0x2817F0),
    ScriptLoad              : Modules.ED83.base.add(0x3C91B0),
    ScriptVMExecute         : Modules.ED83.base.add(0x3C6DA0),
    ScriptGetFunctionByName : Modules.ED83.base.add(0x3C7FF0),
    Logger_Output           : Modules.ED83.base.add(0x11D160),

    BlowFish_Decode         : Modules.ED83.base.add(0x20CAA0),

    File_Open               : Modules.ED83.base.add(0xF5920),

    DLC_Check               : Modules.ED83.base.add(0x3A8359),
};
