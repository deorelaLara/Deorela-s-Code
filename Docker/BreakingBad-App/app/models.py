from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
    'breakingbad',
    port = 3306,
    user = 'root',
    passwd = 'admin1'
)

class Characters(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    birthday = CharField()
    occupation = CharField()
    img = CharField()
    status = CharField()
    nickname = CharField()
    portrayed = CharField()
    category = CharField

    class Meta:
        database = myDB
        db_table = 'characters'
