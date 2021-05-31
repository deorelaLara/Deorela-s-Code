using System.Collections.Generic;
using System.Threading.Tasks;
using RickAndMorty.Models;

namespace RickAndMorty.Data
{
	public interface IRestService
	{
		Task<List<Characters>> RefreshDataAsync();

		Task SaveCharacterAsync(Characters charac, bool isNewCharacter);

		Task DeleteCharacterAsync(string id);
	}
}
