using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace RecordViewer
{
    public class EDAOSaveData
    {
        byte[] saveData;

        public String FileName { get; set; }
        public int index { get; private set; }
        public String thumb { get; private set; }
        public String chapter { get; private set; }
        public String saveTime { get; private set; }
        public String position { get; private set; }
        public String playTime { get; private set; }

        public List<String> characters { get; private set; }
        public List<String> levels { get; private set; }

        const int ScenaFlagsOffset = 0x1B008;

        public EDAOSaveData(String SaveDataPath)
        {
            FileName = SaveDataPath;

            characters = new List<String>();
            levels = new List<String>();

            using (System.IO.FileStream fs = new System.IO.FileStream(SaveDataPath, System.IO.FileMode.Open))
            {
                using (System.IO.BinaryReader br = new System.IO.BinaryReader(fs))
                {
                    saveData = br.ReadBytes((int)fs.Length);
                }
            }

            var dir = Path.GetDirectoryName(SaveDataPath);
            var index = dir.ToUpper().LastIndexOf("\\SAV");

            this.index = Int32.Parse(dir.Substring(index + 4));

            thumb = dir + "\\icon0.png";
            String info = dir + "\\info.txt";

            using (System.IO.FileStream fs = new System.IO.FileStream(info, System.IO.FileMode.Open))
            {
                using (System.IO.BinaryReader br = new System.IO.BinaryReader(fs))
                {
                    var game = System.Text.Encoding.GetEncoding(936).GetString(br.ReadBytes(0x80)).Split('\x0')[0];
                    var chapter = System.Text.Encoding.GetEncoding(936).GetString(br.ReadBytes(0x80)).Split('\x0')[0];
                    var other = System.Text.Encoding.GetEncoding(936).GetString(br.ReadBytes(0x400)).Split('\x0')[0];
                    var savetime = System.Text.Encoding.GetEncoding(936).GetString(br.ReadBytes(0x20)).Split('\x0')[0];

                    var lines = new List<String>(other.Split('\n'));
                    var position = lines[0];
                    var playtime = lines[1];

                    this.chapter = chapter;
                    this.saveTime = savetime;
                    this.position = position;
                    this.playTime = playtime;

                    foreach (var sub in lines.GetRange(2, lines.Count - 2))
                    {
                        foreach (var chrinfo in sub.Split(new String[] { "　" }, StringSplitOptions.RemoveEmptyEntries))
                        {
                            var s = chrinfo.Split(new String[] {"Lv"}, StringSplitOptions.RemoveEmptyEntries);
                            characters.Add(s[0].Trim());
                            levels.Add(s.Length == 2 ? ("Lv " + s[1].Trim()) : "");
                        }
                    }
                }
            }

            while (this.characters.Count != 8)
            {
                this.characters.Add("");
                this.levels.Add("");
            }
        }

        int MakeScenarioFlags(int Offset, int Bit)
        {
            return (Offset << 3) | (Bit & 7);
        }

        public Boolean TestScenaFlag(int Offset, int Bit)
        {
            if (Offset >= 0x220 || Offset < 0)
                return false;

            return (saveData[ScenaFlagsOffset + Offset] & (1 << Bit)) != 0;
        }
    }
}
