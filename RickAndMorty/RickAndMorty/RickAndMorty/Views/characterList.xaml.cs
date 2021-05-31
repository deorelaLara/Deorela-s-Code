using Xamarin.Forms;
using System;
using RickAndMorty.Models;

namespace RickAndMorty.Views
{
	//[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class characterList : ContentPage
	{
		public characterList()
		{
			InitializeComponent();
		}
		protected async override void OnAppearing()
		{
			base.OnAppearing();
			listaPersonajes.ItemsSource = await TodoREST.characManager.GetTaskAsync();
		}

		async void OnAddItemClicked(object sender, EventArgs e)
		{
			await Navigation.PushAsync(new characterPage(true)
			{
				BindingContext = new Characters
				{
					id = Guid.NewGuid().ToString()
				}
			});
		}
		async void OnItemSelected(object sender, SelectedItemChangedEventArgs e)
		{
			await Navigation.PushAsync(new characterPage
			{
				BindingContext = e.SelectedItem as Characters
			});
		}
	}
}