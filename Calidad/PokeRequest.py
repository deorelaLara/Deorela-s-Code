import requests
payload = {'name': venusaur}
r = requests.get('https://pokeapi.co/api/v2/pokemon', params=payload)

print(r.text)