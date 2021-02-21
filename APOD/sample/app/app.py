from flask import Flask, render_template
from apod import APOD
import random
import datetime
from datetime import timedelta, date
import json


app = Flask(__name__)
api = APOD()

#PAGINA INICIO 
@app.route('/')
def index():
    return render_template('index.html')

#PAGINA PARA MOSTRAR INFO DE IMAGEN RANDON GENERADA POR LA FECHA
@app.route('/random/')
def apod():
    #GENERAMOS UNA FECHA ALEATORIA ENTRE UN RANGO DE 2 FECHAS ESTABLECIDAS
    start_date = datetime.date(2020, 12, 19)
    end_date = datetime.date(2020, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
    apod = api.getPicture(random_date)
    return render_template('random.html', apod = apod)

#LISTA DE TODAS LAS IMAGENES ENTRE EL RANGO DE FECHA ESTABLECIDO ARRIBA (2000-1-1 / 2020-12-31)
@app.route('/list/')
def lista():

    return render_template('list.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
