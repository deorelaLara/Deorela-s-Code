using Xamarin.Forms;
using System;
using RickAndMorty.Models;
using System.Text.RegularExpressions;

namespace RickAndMorty.Views
{
	//[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class characterPage : ContentPage
	{
		bool isNewCharacter;
		public characterPage(bool isNew = false)
		{
			InitializeComponent();
			isNewCharacter = isNew;
		}

		async void OnSaveButtonClicked(object sender, EventArgs e)
		{
			var todoCharacter = (Characters)BindingContext;
			//await TodoREST.characManager.SaveTaskAsync(todoCharacter, isNewCharacter);
			//await Navigation.PopAsync();
			string caractEspecial ="^[^ ][a-zA-Z ]+[^ ]$";
			bool res = Regex.IsMatch(idEntry.Text, caractEspecial, RegexOptions.IgnoreCase);
			bool res1 = Regex.IsMatch(nameEntry.Text, caractEspecial, RegexOptions.IgnoreCase);
			bool res2= Regex.IsMatch(statusEntry.Text, caractEspecial, RegexOptions.IgnoreCase);
			bool res3 = Regex.IsMatch(speciesEntry.Text, caractEspecial, RegexOptions.IgnoreCase);
			bool res4 = Regex.IsMatch(typeEntry.Text, caractEspecial, RegexOptions.IgnoreCase);
			bool res5 = Regex.IsMatch(locationEntry.Text, caractEspecial, RegexOptions.IgnoreCase);

			//VALIDACIONES
			//Sirve para validar que no se encuentren campos vacios
			if ((String.IsNullOrEmpty(idEntry.Text) || String.IsNullOrEmpty(nameEntry.Text) || String.IsNullOrEmpty(statusEntry.Text) || String.IsNullOrEmpty(speciesEntry.Text) || String.IsNullOrEmpty(typeEntry.Text) || String.IsNullOrEmpty(locationEntry.Text)))
			{
				await this.DisplayAlert("Warning", "Please check the information some options are empty ", "OK");
			} //validamos que no encuentre caracteres especiales 
			else if (!res || !res1 || !res2 || !res3 || !res4 || !res5)
			{
				await this.DisplayAlert("Warning", "Special Characters are not accepted", "OK");

			}
			else
			{
				await TodoREST.characManager.SaveTaskAsync(todoCharacter, isNewCharacter);
				await Navigation.PopAsync();
			}
			

		}
		async void OnDeleteButtonClicked(object sender, EventArgs e)
		{
			var todoCharacter = (Characters)BindingContext;
			await TodoREST.characManager.DeleteTaskAsync(todoCharacter);
			await Navigation.PopAsync();
		}

		async void OnCancelButtonClicked(object sender, EventArgs e)
		{
			await Navigation.PopAsync();
		}
	}
}