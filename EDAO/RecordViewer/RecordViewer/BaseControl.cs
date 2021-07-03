using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecordViewer
{
    public class Tasks : System.Collections.ObjectModel.ObservableCollection<String>
    {
        public Tasks() : base()
        {
            Add("Groceries");
            Add("Laundry");
            Add("Email");
            Add("Clean");
            Add("Dinner");
            Add("Proposals");
            Add("Groceries");
            Add("Laundry");
            Add("Email");
            Add("Clean");
            Add("Dinner");
            Add("Proposals");
        }
    }

    class DefaultValues
    {
        public static String DefaultFontFamily = "Microsoft YaHei";
        public static Double DefaultFontSize = 14;

        static public void SetDefaultValues(System.Windows.Controls.Control ctrl)
        {
            ctrl.FontFamily = new System.Windows.Media.FontFamily(DefaultValues.DefaultFontFamily);
            ctrl.FontSize = DefaultValues.DefaultFontSize;
        }
    }

    public class RVButton : Fluent.Button
    {
        public RVButton()
        {
            DefaultValues.SetDefaultValues(this);
        }
    }

    public class RVTabItem : Fluent.RibbonTabItem
    {
        public RVTabItem()
        {
            DefaultValues.SetDefaultValues(this);
        }
    }

    public class RVBackstageTabItem : Fluent.BackstageTabItem
    {
        public RVBackstageTabItem()
        {
            DefaultValues.SetDefaultValues(this);
        }
    }

    public class PanelContext : System.Windows.Controls.Grid
    {
        Boolean ContextInitialized = false;

        virtual public void Refresh()
        {
            ShowContext();
        }

        public void ShowContext()
        {
            if (ContextInitialized)
                return;

            ContextInitialized = true;
        }
    }

    public class LowerPanel : System.Windows.Controls.Grid
    {
        public void SwapPanelContext(PanelContext context)
        {
            Children.Clear();
            if (context == null)
                return;

            Children.Add(context);
            context.Refresh();
        }
    }
}
