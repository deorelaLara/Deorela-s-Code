import requests
import json
import random
import datetime
from datetime import timedelta, date


class APOD(object):
    def __init__(self):
        self.ENDPOINT = 'https://api.nasa.gov/planetary/apod?api_key=VyX9fdgowmpkxXikiRM9OUJD69cgQKdfjIrEh3kP'

    def getPicture(self, x):
        uri = f'{self.ENDPOINT}&date={x}'
        req = requests.get(uri)
        data = req.json()

        return {
            'title' : data.get('title'),
            'url' : data.get('url'),
            'explanation': data.get('explanation'),
            'date': data.get('date'),
            'media_type': data.get('media_type'),
        }

"""
#Clase con funciones para hacer nuestro request
api = APOD()

#GENERAMOS UNA FECHA ALEATORIA DADO UN RANGO DE 2 FECHAS ESTABLECIDAS
start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 12, 31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
#print(random_date)

#GENERAMOS UNA LISTA CON LAS FECHAS ALEATORIAS
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2000, 1, 1)
end_dt = date(2020, 12, 31)
for dt in daterange(start_dt, end_dt):
    #print(dt.strftime("%Y-%m-%d"))
    print(json.dumps(api.getPicture(dt.strftime("%Y-%m-%d")), indent=2))

#date = input('Insert date: ')
#print(json.dumps(api.getPicture(date), indent=2))
#print(json.dumps(api.getPicture(random_date), indent=2))

"""