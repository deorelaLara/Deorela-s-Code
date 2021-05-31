using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Essentials;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace RickAndMorty.Views
{
	//[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class Welcome : ContentPage
	{
		public Welcome()
		{
			InitializeComponent();
		}

		void btn_Navegador(object sender, EventArgs e)
		{
			Browser.OpenAsync("https://rickandmorty.fandom.com/wiki/Rickipedia", BrowserLaunchMode.SystemPreferred);
		}

        void OnLight(object sender, EventArgs e)
        {
            LayoutRoot.BackgroundColor = Color.White;

            welclabel.TextColor = Color.Black;
            txtlabel.TextColor = Color.Black;

        }

        void OnDark(object sender, EventArgs e)
        {
            LayoutRoot.BackgroundColor = Color.Black;

            welclabel.TextColor = Color.White;
            txtlabel.TextColor = Color.White;
        }

        void CRUD(object sender, EventArgs e)
        {
            Navigation.PushAsync(new characterList());
        }
        void Characters(object sender, EventArgs e)
		{
            Navigation.PushAsync(new characters());
		}
        void Locations(object sender, EventArgs e)
		{
            Navigation.PushAsync(new locations());
		}

    }
}