using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.IO;

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for SaveDataList.xaml
    /// </summary>
    public partial class SaveDataList : PanelContext
    {
        public SaveDataList()
        {
            InitializeComponent();

            saveDataPathTextBox.Text = GlobalData.SavePath;

            RefreshSaveData();
        }

        List<String> QuerySaveDatas(String SaveDataPath)
        {
            return new List<String>(Directory.EnumerateDirectories(SaveDataPath));
        }

        override public void Refresh()
        {
            saveDataPathTextBox.Text = GlobalData.SavePath;
            RefreshSaveData();
        }

        void RefreshSaveData()
        {
            List<String> list;

            saveDataList.Items.Clear();

            try
            {
                list = QuerySaveDatas(GlobalData.SavePath);
            }
            catch
            {
                return;
            }

            foreach (var save in list)
            {
                try
                {
                    EDAOSaveData savedata = new EDAOSaveData(save + "\\savedata.dat");

                    var item = new SaveDataListItem(savedata);
                    this.saveDataList.Items.Add(item);
                }
                catch
                {
                }
            }
        }

        private void saveDataPath_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            try
            {
                var dialog = new Microsoft.WindowsAPICodePack.Dialogs.CommonOpenFileDialog();

                dialog.IsFolderPicker = true;
                dialog.InitialDirectory = GlobalData.SavePath;
                dialog.DefaultFileName = GlobalData.SavePath;

                var result = dialog.ShowDialog();

                if (result != Microsoft.WindowsAPICodePack.Dialogs.CommonFileDialogResult.Ok)
                    return;

                GlobalData.SavePath = dialog.FileName;
            }
            catch (System.PlatformNotSupportedException)
            {
                var dialog = new System.Windows.Forms.FolderBrowserDialog();

                dialog.SelectedPath = GlobalData.SavePath;

                var result = dialog.ShowDialog();

                if (result != System.Windows.Forms.DialogResult.OK)
                    return;

                GlobalData.SavePath = dialog.SelectedPath;
            }

            saveDataPathTextBox.Text = GlobalData.SavePath;
        }

        private void refreshSaveList_Click(object sender, RoutedEventArgs e)
        {
            GlobalData.SavePath = saveDataPathTextBox.Text;

            RefreshSaveData();
        }
    }
}
