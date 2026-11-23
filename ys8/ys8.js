const ImageBase = ptr(0x140000000);
const Addrs = {
    CheckDLC        : ptr(0x14016BCE0).add(-ImageBase),
    CreateFile      : ptr(0x140342870).add(-ImageBase),
    SteamInitialize : ptr(0x14016C240).add(-ImageBase),
    SteamFinalize   : ptr(0x14016C170).add(-ImageBase),
};

const API = {
    GetFileAttributesA: new NativeFunction(Process.getModuleByName('KERNEL32.dll').getExportByName('GetFileAttributesA'), 'uint32', ['pointer']),
    SetProcessDpiAwarenessContext: new NativeFunction(Process.getModuleByName('USER32.dll').getExportByName('SetProcessDpiAwarenessContext'), 'uint32', ['int64']),
};

const INVALID_FILE_ATTRIBUTES = 0xFFFFFFFF;

function isPathExists(path) {
    return API.GetFileAttributesA(Memory.allocAnsiString(path)) != INVALID_FILE_ATTRIBUTES;
}

(function() {
    (new NativeFunction(Process.getModuleByName('KERNEL32.dll').getExportByName('AllocConsole'), 'bool', []))();

    const DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE = -3;
    API.SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE);

    const exe = Process.enumerateModules()[0];
    const exePath = exe.path.split('\\').slice(0, -1).join('/').toLocaleLowerCase() + '/';
    const chtPath = exePath + 'ys8_cht/';

    /*
        YS08JPDLC00N0000
        YS08JPDLC00N0002
    */
    Interceptor.replace(exe.base.add(Addrs.CheckDLC), new NativeCallback(() => {return 1;}, 'int', []));
    // Interceptor.replace(exe.base.add(Addrs.SteamInitialize), new NativeCallback(() => {}, 'void', []));
    // Interceptor.replace(exe.base.add(Addrs.SteamFinalize), new NativeCallback(() => {}, 'void', []));

    Interceptor.attach(exe.base.add(Addrs.CreateFile), {
        onEnter: function(args) {
            const path = ptr(args[1]).readAnsiString();
            const write = args[2] != 0;
            if (write)
                return;

            if (path.startsWith(exePath)) {
                const newPath = path.replace(exePath, chtPath);
                if (isPathExists(newPath)) {
                    // console.log(`redirect: ${path} -> ${newPath}`);
                    this.path = Memory.allocAnsiString(newPath);
                    args[1] = this.path;
                }
            }
        },
    });
})()
