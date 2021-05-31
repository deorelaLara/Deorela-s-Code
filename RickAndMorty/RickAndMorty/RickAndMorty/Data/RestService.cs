using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using RickAndMorty.Models;

namespace RickAndMorty.Data
{
	public class RestService : IRestService
	{
        HttpClient client;
        JsonSerializerOptions serializerOptions;

        public List<Characters> characters { get; private set; }

        public RestService()
        {
            client = new HttpClient();
            serializerOptions = new JsonSerializerOptions
            {
                PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
                WriteIndented = true
            };
        }

        public async Task<List<Characters>> RefreshDataAsync()
        {
            characters = new List<Characters>();

            Uri uri = new Uri(string.Format(Constants.RestUrl, string.Empty));
            try
            {
                HttpResponseMessage response = await client.GetAsync(uri);
                if (response.IsSuccessStatusCode)
                {
                    string content = await response.Content.ReadAsStringAsync();
                    characters = JsonSerializer.Deserialize<List<Characters>>(content, serializerOptions);
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(@"\tERROR {0}", ex.Message);
            }

            return characters;
        }

        public async Task SaveCharacterAsync(Characters charac, bool isNewCharacter = false)
        {
            Uri uri = new Uri(string.Format(Constants.RestUrl, string.Empty));

            try
            {
                string json = JsonSerializer.Serialize<Characters>(charac, serializerOptions);
                StringContent content = new StringContent(json, Encoding.UTF8, "application/json");

                HttpResponseMessage response = null;
                if (isNewCharacter)
                {
                    response = await client.PostAsync(uri, content);
                }
                else
                {
                    response = await client.PutAsync(uri, content);
                }

                if (response.IsSuccessStatusCode)
                {
                    Debug.WriteLine(@"\tTodoItem successfully saved.");
                }

            }
            catch (Exception ex)
            {
                Debug.WriteLine(@"\tERROR {0}", ex.Message);
            }
        }

        public async Task DeleteCharacterAsync(string id)
        {
            Uri uri = new Uri(string.Format(Constants.RestUrl, id));

            try
            {
                HttpResponseMessage response = await client.DeleteAsync(uri);

                if (response.IsSuccessStatusCode)
                {
                    Debug.WriteLine(@"\tTodoItem successfully deleted.");
                }

            }
            catch (Exception ex)
            {
                Debug.WriteLine(@"\tERROR {0}", ex.Message);
            }
        }


    }
}
