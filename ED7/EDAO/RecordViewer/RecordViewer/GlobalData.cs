using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RecordViewer
{
    public class GlobalData
    {
        public static String SavePath = @"J:\Falcom\ED_AO\savedata";

        public delegate void SaveDataChangeDelegate(EDAOSaveData NewSaveData, bool SwitchToMainWindow = false);
        public static SaveDataChangeDelegate SaveDataChangeHandler;

        public static EDAOSaveData CurrentSaveData { get; set; }

        public static void NotifySaveDataChange(EDAOSaveData NewSaveData, bool SwitchToMainWindow = false)
        {
            SaveDataChangeHandler(NewSaveData, SwitchToMainWindow);
        }
    }
}
