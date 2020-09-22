from flask import Flask, render_template
from database import *
from peewee import *

app = Flask(__name__)

db = SqliteDatabase('AgeOfEmpII.db')

civ = civilization()
struct = structure()
tec = technology()
un = unit()


@app.route('/')
def index():
    db.connect()
    civilizations = civ.select()
    structure = struct.select()
    tech = tec.select()
    unit = un.select()
    return render_template('Information.html',
                           civilizations=civilizations,
                           structures=structure,
                           techs=tech,
                           units=unit)


if __name__ == "__main__":
    app.run(host="0.0.0.0")