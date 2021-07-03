//#pragma comment(linker, "/ENTRY:DllMain")

#include "ml.cpp"
#include "frida-core.h"

class FridaLoader
{
protected:
    HANDLE      InitEvent;
    HANDLE      ExitEvent;
    GMainLoop*  Loop;

public:
    FridaLoader();
    ~FridaLoader();
    
    NTSTATUS Load();
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

FridaLoader::FridaLoader()
{
    NtCreateEvent(&this->InitEvent, EVENT_ALL_ACCESS, nullptr, SynchronizationEvent, FALSE);
    NtCreateEvent(&this->ExitEvent, EVENT_ALL_ACCESS, nullptr, SynchronizationEvent, FALSE);
}

FridaLoader::~FridaLoader()
{
    NtClose(this->ExitEvent);
    NtClose(this->InitEvent);
}

NTSTATUS FridaLoader::Load()
{
    Ps::CreateThreadT(
        ThreadCallbackM(FridaLoader* Loader)
        {
            NTSTATUS Status = Loader->FridaThread();

            if (NT_FAILED(Status))
                NtSetEvent(Loader->InitEvent, nullptr);

            return Status;
        },
        this
    );

    return this->WaitForInit();
}

NTSTATUS FridaLoader::Stop()
{
    NtSetEvent(this->ExitEvent, nullptr);
    return NtWaitForSingleObject(this->InitEvent, FALSE, nullptr);
}

NTSTATUS FridaLoader::FridaThread()
{
    GMainLoop*          loop;
    FridaDeviceManager* manager;
    FridaDeviceList*    devices;
    FridaDevice*        localDevice;
    GError*             error;

    error       = nullptr;
    localDevice = nullptr;
    manager     = nullptr;
    loop        = nullptr;

    SCOPE_EXIT
    {
        if (error != nullptr)
            g_error_free(error);

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

    FridaSession* session = frida_device_attach_sync(localDevice, (guint)Ps::CurrentPid(), FRIDA_REALM_NATIVE, nullptr, &error);
    if (error != nullptr)
        return STATUS_ALREADY_DISCONNECTED;

    FridaScriptOptions* options = frida_script_options_new();

    frida_script_options_set_name(options, "example");
    frida_script_options_set_runtime(options, FRIDA_SCRIPT_RUNTIME_QJS);

    FridaScript* script = frida_session_create_script_sync(session,
        "Interceptor.attach(Module.getExportByName('kernel32.dll', 'CreateFileW'), {\n"
        "  onEnter(args) {\n"
        "    console.log(`[*] CreateFileW(\"${args[0].readUtf16String()}\")`);\n"
        "  }\n"
        "});\n"
        "Interceptor.attach(Module.getExportByName('kernel32.dll', 'CloseHandle'), {\n"
        "  onEnter(args) {\n"
        "    console.log(`[*] CloseHandle(${args[0]})`);\n"
        "  }\n"
        "});",
        options,
        nullptr,
        &error
    );

    g_clear_object(&options);

    frida_script_load_sync(script, NULL, &error);
    if (error != nullptr)
        return STATUS_ALREADY_DISCONNECTED;

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
                    g_print("%s\n", log_message);
                }
                else
                {
                    g_print("on_message: %s\n", message);
                }

                g_object_unref(parser);
            }
        )),
        nullptr
    );

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

    NtSetEvent(this->InitEvent, nullptr);

    g_print("exit\n");

    return STATUS_SUCCESS;
}

BOOL UnInitialize(PVOID BaseAddress)
{
    return FALSE;
}

BOOL Initialize(PVOID BaseAddress)
{
    NTSTATUS    Status;
    FridaLoader frida;

    Status = frida.Load();
    if (NT_FAILED(Status))
        return FALSE;

    fclose(fopen("E:\\Game\\swd3\\Env.dat", "rb+"));

    Ps::Sleep(1000 * 10);

    frida.Stop();

    return TRUE;
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
}

int __cdecl main(LONG_PTR argc, PWSTR *argv)
{
    main2(argc, argv);
    //Ps::ExitProcess(0);
}
