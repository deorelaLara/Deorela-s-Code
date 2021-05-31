using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RickAndMorty.Droid
{
	[Activity(Theme = "@style/SplashTheme", MainLauncher = true, NoHistory = true,
	ConfigurationChanges = Android.Content.PM.ConfigChanges.ScreenSize, Label = "Rick & Morty ")]

	class SplashActivity : Activity
	{
		protected override void OnCreate(Bundle savedInstanceState)
		{
			base.OnCreate(savedInstanceState);
			StartActivity(new Intent(ApplicationContext, typeof(MainActivity)));
			System.Threading.Thread.Sleep(100);
			//StartActivity(typeof(MainActivity));
			// Create your application here
		}
	}
}