using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Fluent;

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for RecordViewerMainWindow.xaml
    /// </summary>
    public partial class RecordViewerMainWindow : Fluent.MetroWindow
    {
        Dictionary<RVTabItem, PanelContext> TabPanelMap;
        String OriginalTitle;

        public RecordViewerMainWindow()
        {
            InitializeComponent();

            Ribbon.Localization.Culture = new System.Globalization.CultureInfo("zh-CN");

            TabPanelMap = new Dictionary<RVTabItem, PanelContext>();

            TabPanelMap[tabBonusBox] = new BonusBoxHunter();

            ribbon.SelectedTabChanged += Ribbon_SelectedTabChanged;
            this.Drop += OnDrop;
            this.AllowDrop = true;

            OriginalTitle = this.Title;

            GlobalData.SaveDataChangeHandler = SaveDataChangeDelegate;
            this.saveDataList.Refresh();
        }

        void SaveDataChangeDelegate(EDAOSaveData NewSaveData, bool SwitchToMainWindow = false)
        {
            GlobalData.CurrentSaveData = NewSaveData;

            if (NewSaveData != null)
            {
                this.Title = this.OriginalTitle + ": " + NewSaveData.FileName;
            }

            if (SwitchToMainWindow)
                this.backstage.IsOpen = false;

            Ribbon_SelectedTabChanged(this.ribbon, null);
        }

        void OnDrop(object sender, DragEventArgs e)
        {
            System.IO.FileAttributes Attributes;
            String FileName = ((String[])e.Data.GetData(DataFormats.FileDrop))[0];

            try
            {
                Attributes = System.IO.File.GetAttributes(FileName);
            }
            catch
            {
                return;
            }

            if ((Attributes & System.IO.FileAttributes.Directory) != 0)
                FileName = FileName + "\\savedata.dat";

            GlobalData.NotifySaveDataChange(new EDAOSaveData(FileName));
        }

        void Ribbon_SelectedTabChanged(object sender, SelectionChangedEventArgs e)
        {
            var ribbon = sender as Ribbon;

            if (ribbon.SelectedTabItem == null)
                return;

            var tabitem = ribbon.SelectedTabItem as RVTabItem;
            bool containsKey = TabPanelMap.ContainsKey(tabitem);

            var context = containsKey ? TabPanelMap[tabitem] : null;

            lowerPanel.SwapPanelContext(context);
        }

        void OnBtnExit(object sender, RoutedEventArgs e)
        {
            Close();
        }

        private void RecordViewerMainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            this.MinWidth = this.Width;
            this.MinHeight = this.Height;

            this.Loaded -= RecordViewerMainWindow_Loaded;
        }
    }
}
