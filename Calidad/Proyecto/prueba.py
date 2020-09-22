import sqlite3
import os

APP_PATH = os.getcwd()
DB_PATH = APP_PATH + '/my_database.db'

con = sqlite3.connect(DB_PATH)
cursor = con.cursor()
cursor.execute("""
               CREATE TABLE persona(
                   ID INT PRIMARE KEY NOT NULL,
                   NOMBRE TEXT NOT NULL,
                   EDAD INT
               )
               """
    
)
con.close()