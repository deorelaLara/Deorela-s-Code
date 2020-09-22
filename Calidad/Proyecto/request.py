import requests
import json


print('*****Astronomy Picture Of The Day******')
#FECHA QUE DESEAMOS BUSCAR 
date =input('Fecha:')
#URL Y KEY
url = 'https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP'

#PARAMETROS QUE RECIBE Y REQUESTS
param = {
         'date': date
         }
resp = requests.get(url, params=param).json()
#INFORMACION OBTENIDA
print(resp["title"])
print(resp["date"])
print(resp["explanation"])
print(resp['media_type'])
print(resp['hdurl'])