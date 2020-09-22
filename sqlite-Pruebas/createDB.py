import os
import sqlite3

db_name = 'Prueba.db'

db_is_new = not os.path.exists(db_name)
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
if db_is_new:
    print('Need to create schema')
else:
    print('Database exists, assume schema does, too.')

conn.close()
