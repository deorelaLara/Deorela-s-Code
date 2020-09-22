import os 
import sqlite3

db_name = 'Prueba.db'
schema_name = 'schema.sql'

db_is_new = not os.path.exists(db_name)

with sqlite3.connect(db_name) as conn:
    if db_is_new:
        print('Creatin schema')
        with open(schema_name,'rt') as f:
            schema = f.read()
        conn.executescripts(schema)
        
        print('Inserting initial data')
        
        conn.executescript("""
        insert into project (name, description, deadline)
        values ('pymotw', 'Python Module of the Week',
                '2016-11-01');

        insert into task (details, status, deadline, project)
        values ('write about select', 'done', '2016-04-25',
                'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about random', 'waiting', '2016-08-22',
                'pymotw');

        insert into task (details, status, deadline, project)
        values ('write about sqlite3', 'active', '2017-07-31',
                'pymotw');
        """)
        
    else:
        print('Database exists, assume does, too')