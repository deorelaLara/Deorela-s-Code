using RickAndMorty.Data;
using RickAndMorty.Views;
using Xamarin.Forms;

namespace RickAndMorty
{
	public class TodoREST : Application
	{
		public static CharacterManager characManager { get; private set; }

		public TodoREST()
		{
			characManager = new CharacterManager(new RestService());
			//pagina de inicio 
			MainPage = new NavigationPage(new Welcome());
			//MainPage = new NavigationPage(new characterList());
		}
		protected override void OnStart()
		{
			// Handle when your app starts
		}

		protected override void OnSleep()
		{
			// Handle when your app sleeps
		}

		protected override void OnResume()
		{
			// Handle when your app resumes
		}
	}
}
