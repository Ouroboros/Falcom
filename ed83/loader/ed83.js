Interceptor.attach(Module.getExportByName('kernel32.dll', 'CreateFileW'), {
  onEnter(args) {
    console.log(`[*] CreateFileW("${args[0].readUtf16String()}")`);
  }
});
Interceptor.attach(Module.getExportByName('kernel32.dll', 'CloseHandle'), {
  onEnter(args) {
    console.log(`[*] CloseHandle(${args[0]})`);
  }
});