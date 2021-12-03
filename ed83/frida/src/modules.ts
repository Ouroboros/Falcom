const modules = Process.enumerateModules();

export const Modules = {
    KERNEL32    : Process.getModuleByName('KERNEL32.dll'),
    USER32      : Process.getModuleByName('USER32.dll'),
    ucrtbase    : Process.getModuleByName('ucrtbase.dll'),
    ED83        : modules[0],
    ED84        : modules[0],
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
