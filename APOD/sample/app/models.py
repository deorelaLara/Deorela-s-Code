from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
    'apod',
    host = 'apod',
    port = 'user',
    password = 'root'
)

class Pictures(Model):
    date = IntegerField(primary_key=True)
    name = CharField()
    media_type = CharField()
    url = CharField()

    class Meta:
        database = myDB
        db_table = 'pictures'
