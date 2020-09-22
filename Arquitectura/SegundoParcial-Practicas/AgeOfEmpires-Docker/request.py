import requests
import json

url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/'
resp = requests.get(url).json()

print(resp['description'])
