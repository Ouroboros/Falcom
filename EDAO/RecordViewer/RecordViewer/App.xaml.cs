using System;
using System.Reflection;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        public App()
        {
            AppDomain.CurrentDomain.UnhandledException += new UnhandledExceptionEventHandler(CurrentDomain_UnhandledException);
            AppDomain.CurrentDomain.AssemblyResolve += new ResolveEventHandler(CurrentDomain_AssemblyResolve);
        }

        static void CurrentDomain_UnhandledException(object sender, UnhandledExceptionEventArgs e)
        {
            System.Windows.MessageBox.Show(e.ExceptionObject.ToString());
        }

        byte[] LoadEmbededResource(String Name)
        {
            var assembly = Assembly.GetExecutingAssembly();
            var assemblyName = assembly.FullName.Split(',')[0];
            var resourceName = assemblyName + "." + Name;
            var stream = assembly.GetManifestResourceStream(resourceName);
            var buffer = new byte[stream.Length];

            stream.Read(buffer, 0, (int)stream.Length);

            return buffer;
        }

        Assembly CurrentDomain_AssemblyResolve(Object sender, ResolveEventArgs args)
        {
            try
            {
                return Assembly.Load(LoadEmbededResource(args.Name.Split(',')[0] + ".dll"));
            }
            catch
            {
                return null;
            }
        }
    }
}
