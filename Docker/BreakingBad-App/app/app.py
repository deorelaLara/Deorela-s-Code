from flask import Flask, render_template
from models import *
from character import *


app = Flask(__name__)
api = Personaje()

@app.route('/')
def main():
    personaje = Characters.select()
    return render_template('index.html', personaje=personaje)



if __name__=='__main__':
    app.run(host='0.0.0.0', debug = True)
    myDB.close()