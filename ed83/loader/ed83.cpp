//#pragma comment(linker, "/ENTRY:DllMain")
#pragma comment(linker, "/EXPORT:DirectInput8Create=dinput8.DirectInput8Create")
#pragma comment(linker, "/EXPORT:Direct3DCreate9=d3d9.Direct3DCreate9")
#pragma comment(linker, "/EXPORT:D3D11CreateDevice=d3d11.D3D11CreateDevice")
#pragma comment(linker, "/EXPORT:D3D11CreateDeviceAndSwapChain=d3d11.D3D11CreateDeviceAndSwapChain")
#pragma comment(linker, "/EXPORT:DirectDrawCreate=DDRAW.DirectDrawCreate")
#pragma comment(linker, "/EXPORT:AlphaBlend=MSIMG32.AlphaBlend")
#pragma comment(linker, "/EXPORT:GradientFill=MSIMG32.GradientFill")
#pragma comment(linker, "/EXPORT:TransparentBlt=MSIMG32.TransparentBlt")
#pragma comment(linker, "/EXPORT:CoTaskMemFree=ole32.CoTaskMemFree")

#include "ml.cpp"
#include "frida-core.h"

ML_OVERLOAD_NEW

#define DBG(...) { PrintConsole(__VA_ARGS__); }
//#define DBG(...) 

class FridaLoader
{
protected:
    HANDLE      InitEvent;
    HANDLE      ExitEvent;
    PSTR        Script = nullptr;
    HANDLE      ThreadHandle = nullptr;
    GMainLoop*  Loop;

public:
    FridaLoader();
    ~FridaLoader();
    
    NTSTATUS Load(PSTR Script);
    NTSTATUS Stop();

    NTSTATUS WaitForInit()
    {
        return NtWaitForSingleObject(this->InitEvent, FALSE, nullptr);
    }

    NTSTATUS WaitForExit()
    {
        LARGE_INTEGER Timeout;
        FormatTimeOut(&Timeout, 1);
        return NtWaitForSingleObject(this->ExitEvent, FALSE, &Timeout);
    }

protected:
    NTSTATUS FridaThread();
};

FridaLoader* gFrida;

FridaLoader::FridaLoader()
{
    NtCreateEvent(&this->InitEvent, EVENT_ALL_ACCESS, nullptr, SynchronizationEvent, FALSE);
    NtCreateEvent(&this->ExitEvent, EVENT_ALL_ACCESS, nullptr, SynchronizationEvent, FALSE);
}

FridaLoader::~FridaLoader()
{
    this->Stop();
    NtClose(this->ExitEvent);
    NtClose(this->InitEvent);
    FreeMemoryP(this->Script);
}

NTSTATUS FridaLoader::Load(PSTR Script)
{
    ULONG_PTR   Length;
    NTSTATUS    Status;

    FAIL_RETURN(this->Stop());

    Length = StrLengthA(Script) + 1;
    this->Script = (PSTR)ReAllocateMemoryP(this->Script, Length);
    RtlCopyMemory(this->Script, Script, Length);

    FAIL_RETURN(Ps::CreateThreadT(
        ThreadCallbackM(FridaLoader* Loader)
        {
            NTSTATUS Status = Loader->FridaThread();

            if (NT_FAILED(Status))
                NtSetEvent(Loader->InitEvent, nullptr);

            return Status;
        },
        this,
        FALSE,
        Ps::CurrentProcess,
        &this->ThreadHandle
    ));

    return this->WaitForInit();
}

NTSTATUS FridaLoader::Stop()
{
    if (this->ThreadHandle == nullptr)
        return STATUS_SUCCESS;

    NTSTATUS Status;

    NtSetEvent(this->ExitEvent, nullptr);
    Status = NtWaitForSingleObject(this->ThreadHandle, FALSE, nullptr);
    NtClose(this->ThreadHandle);
    this->ThreadHandle = nullptr;

    return Status;
}

NTSTATUS FridaLoader::FridaThread()
{
    GMainLoop*          loop;
    FridaDeviceManager* manager;
    FridaDeviceList*    devices;
    FridaDevice*        localDevice;
    GError*             error;

    DBG(L"FridaThread\n");

    error       = nullptr;
    localDevice = nullptr;
    manager     = nullptr;
    loop        = nullptr;

    SCOPE_EXIT
    {
        if (error != nullptr)
        {
            WCHAR Buffer[0x1000];

            swprintf(Buffer, L"domain = %d\ncode = %d\n%S", error->domain, error->code, error->message);
            ExceptionBox(Buffer);
            g_error_free(error);
        }

        if (localDevice != nullptr)
            frida_unref(localDevice);

        if (manager != nullptr)
        {
            frida_device_manager_close_sync(manager, NULL, NULL);
            frida_unref(manager);
        }

        if (loop != nullptr)
            g_main_loop_unref(loop);

        this->Loop = nullptr;
    }
    SCOPE_EXIT_END;

    frida_init();

    loop    = g_main_loop_new(nullptr, TRUE);
    manager = frida_device_manager_new();

    this->Loop = loop;

    error = nullptr;
    localDevice = frida_device_manager_find_device_by_type_sync(manager, FRIDA_DEVICE_TYPE_LOCAL, 0, nullptr, &error);
    if (error != nullptr)
        return STATUS_DEVICE_NOT_READY;

    if (localDevice == nullptr)
        return STATUS_DEVICE_DOES_NOT_EXIST;

    FridaSessionOptions* sessionOptions = frida_session_options_new();
    frida_session_options_set_realm(sessionOptions, FRIDA_REALM_NATIVE);
    FridaSession* session = frida_device_attach_sync(localDevice, (guint)Ps::CurrentPid(), sessionOptions, nullptr, &error);
    g_clear_object(&sessionOptions);

    if (error != nullptr)
        return STATUS_ALREADY_DISCONNECTED;

    FridaScriptOptions* scriptOptions = frida_script_options_new();

    frida_script_options_set_name(scriptOptions, "script");
    frida_script_options_set_runtime(scriptOptions, FRIDA_SCRIPT_RUNTIME_V8);

    FridaScript* script = frida_session_create_script_sync(session, this->Script, scriptOptions, nullptr, &error);
    g_clear_object(&scriptOptions);

    if (error != nullptr)
        return STATUS_INVALID_PARAMETER;

    g_signal_connect(
        script,
        "message",
        G_CALLBACK(LambdaCastHelper<void (*CDECL)(FridaScript*, const gchar*, GBytes*, gpointer)>::FUNC(
            [](
                FridaScript*    script,
                const gchar*    message,
                GBytes*         data,
                gpointer        user_data
            )
            {
                JsonParser * parser;
                JsonObject * root;
                const gchar * type;

                parser = json_parser_new();
                json_parser_load_from_data(parser, message, -1, NULL);
                root = json_node_get_object(json_parser_get_root (parser));

                type = json_object_get_string_member(root, "type");
                if (strcmp(type, "log") == 0)
                {
                    const gchar * log_message = json_object_get_string_member(root, "payload");
                    DBG(L"%S\n", log_message);
                }
                else
                {
                    DBG(L"on_message: %S\n", message);
                }

                g_object_unref(parser);
            }
        )),
        nullptr
    );

    frida_script_load_sync(script, NULL, &error);
    if (error != nullptr)
        return STATUS_ALREADY_DISCONNECTED;

    g_idle_add(
        [](gpointer user_data) -> gboolean
        {
            NtSetEvent(((FridaLoader *)user_data)->InitEvent, nullptr);
            return G_SOURCE_REMOVE;
        },
        this
    );

    g_idle_add(
        [](gpointer user_data) -> gboolean
        {
            FridaLoader* Loader = (FridaLoader *)user_data;

            if (Loader->WaitForExit() == STATUS_SUCCESS)
            {
                g_main_loop_quit(Loader->Loop);
                return G_SOURCE_REMOVE;
            }

            return G_SOURCE_CONTINUE;
        },
        this
    );

    g_main_loop_run(loop);

    frida_script_unload_sync(script, nullptr, nullptr);
    frida_unref(script);

    frida_session_detach_sync(session, nullptr, nullptr);
    frida_unref(session);

    g_print("exit\n");

    return STATUS_SUCCESS;
}

PSTR LoadScript()
{
    NTSTATUS        Status;
    PLDR_MODULE     Exe;
    PSTR            Script;
    PWSTR           ScriptName;
    NtFileDisk      ScriptFile;

    Exe = Ldr::FindLdrModuleByHandle(nullptr);

    ScriptName = (PWSTR)AllocStack(Exe->FullDllName.Length + sizeof(*ScriptName) * 3);
    RtlCopyMemory(ScriptName, Exe->FullDllName.Buffer, Exe->FullDllName.Length);
    ScriptName[Exe->FullDllName.Length / sizeof(*ScriptName)] = 0;

    *(PULONG64)findextw(ScriptName) = TAG3W('.js');

    Status = ScriptFile.Open(ScriptName);
    if (NT_FAILED(Status))
        return nullptr;

    Script = (PSTR)AllocateMemoryP((ULONG_PTR)(ScriptFile.GetSize64() + 1));
    if (Script == nullptr)
        return nullptr;

    Status = ScriptFile.Read(Script);
    if (NT_FAILED(Status))
    {
        FreeMemoryP(Script);
        Script = nullptr;
    }
    else
    {
        Script[ScriptFile.GetSize64()] = 0;
    }

    return Script;
}

NTSTATUS InitalizeFridaCore(PVOID, PVOID, PVOID)
{
    PSTR        Script;
    NTSTATUS    Status;

    Script = LoadScript();
    if (Script == nullptr)
        return STATUS_NOT_FOUND;

    gFrida = new FridaLoader;

    Status = gFrida->Load(Script);
    FreeMemoryP(Script);

    if (NT_FAILED(Status))
    {
        SafeDeleteT(gFrida);
        return Status;
    }

    return STATUS_SUCCESS;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    SafeDeleteT(gFrida);
    ml::MlUnInitialize();
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    ml::MlInitialize();
    return NT_SUCCESS(NtQueueApcThread(Ps::CurrentThread, (PKNORMAL_ROUTINE)InitalizeFridaCore, 0, 0, 0));
}

BOOL WINAPI DllMain(PVOID BaseAddress, ULONG Reason, PVOID Reserved)
{
    switch (Reason)
    {
        case DLL_PROCESS_ATTACH:
            return Initialize(BaseAddress) || UnInitialize(BaseAddress);

        case DLL_PROCESS_DETACH:
            UnInitialize(BaseAddress);
            break;
    }

    return TRUE;
}

ForceInline VOID main2(LONG_PTR argc, PWSTR *argv)
{
    Initialize(0);
    NtTestAlert();

    fclose(fopen("E:\\Game\\swd3\\Env.dat", "rb+"));
    Ps::Sleep(1000 * 5);

    UnInitialize(0);
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    main2(argc, argv);
    //Ps::ExitProcess(0);
}
