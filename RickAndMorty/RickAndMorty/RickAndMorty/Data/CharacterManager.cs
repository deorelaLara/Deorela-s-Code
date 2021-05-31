using System.Collections.Generic;
using System.Threading.Tasks;
using RickAndMorty.Models;

namespace RickAndMorty.Data
{
	public class CharacterManager
	{
		IRestService restService;

		public CharacterManager(IRestService service)
		{
			restService = service;
		}

		public Task<List<Characters>> GetTaskAsync()
		{
			return restService.RefreshDataAsync();
		}

		public Task SaveTaskAsync(Characters charac, bool isNewCharacter = false)
		{
			return restService.SaveCharacterAsync(charac, isNewCharacter);
		}

		/*public Task DeleteTaskAsync(Characters character)
		{
			return restService.DeleteCharcterAsync(character.id);
		}*/

		public Task DeleteTaskAsync(Characters item)
		{
			return restService.DeleteCharacterAsync(item.id);
		}
	}
}
