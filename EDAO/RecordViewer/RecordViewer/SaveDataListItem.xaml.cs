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

namespace RecordViewer
{
    /// <summary>
    /// Interaction logic for SaveDataListItem.xaml
    /// </summary>
    public partial class SaveDataListItem : PanelContext
    {
        public EDAOSaveData saveData { get; private set; }

        public SaveDataListItem(EDAOSaveData saveData)
        {
            InitializeComponent();

            this.Height = 220;

            this.saveData = saveData;

            try
            {
                this.thumb.Source = new BitmapImage(new Uri(saveData.thumb));
            }
            catch
            {
            }

            this.Index.Text = String.Format("{0:D4}", saveData.index);
            this.SaveTime.Text = saveData.saveTime;
            this.Chapter.Text = saveData.chapter;
            this.Position.Text = saveData.position;
            this.PlayTime.Text = saveData.playTime;

            this.CharacterName1.Text = saveData.characters[0];
            this.CharacterLevel1.Text = saveData.levels[0];
            this.CharacterName2.Text = saveData.characters[1];
            this.CharacterLevel2.Text = saveData.levels[1];

            this.CharacterName3.Text = saveData.characters[2];
            this.CharacterLevel3.Text = saveData.levels[2];
            this.CharacterName4.Text = saveData.characters[3];
            this.CharacterLevel4.Text = saveData.levels[3];

            this.CharacterName5.Text = saveData.characters[4];
            this.CharacterLevel5.Text = saveData.levels[4];
            this.CharacterName6.Text = saveData.characters[5];
            this.CharacterLevel6.Text = saveData.levels[5];
            
            this.CharacterName7.Text = saveData.characters[6];
            this.CharacterLevel7.Text = saveData.levels[6];
            this.CharacterName8.Text = saveData.characters[7];
            this.CharacterLevel8.Text = saveData.levels[7];
        }

        private void SaveDataListItem_MouseDoubleClick(object sender, MouseButtonEventArgs e)
        {
            GlobalData.NotifySaveDataChange(this.saveData, true);
        }
    }
}
