from abc import ABC, abstractclassmethod
import requests

class Pokemon():
    def __init__(self, name, order):
        self.Name = name
        self.Order = order


class Pokedex(ABC):
    @abstractclassmethod
    def Search(id):
        pass

def getPokemon(id, bibliotec):
    p = bibliotec.Search(id)
    
    return p.Name, p.Order

class Poke(Pokedex):
    def __init__(self, url_base):
        self.url = url_base

    def Search(self, id):
        res = requests.get('{}/{}'.format(self.url, id))
        json = res.json()
        return Pokemon(json['name'], json['order'], json['pokemon']['name'])


if __name__ == "__main__":
    id = input('No Pokemon: ')
    pokemon = Poke('https://pokeapi.co/api/v2/pokemon-form')
    print(getPokemon(id, pokemon))

        