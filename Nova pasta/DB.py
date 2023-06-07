import sqlite3

conn = sqlite3.connect('teste_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE usuarios(
            usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_name VARCHAR(25),
            usuario_senha VARCHAR(25)
          )
          ''')

conn.commit()

conn = sqlite3.connect('teste_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE produtos(
            produtos_id INTEGER PRIMARY KEY AUTOINCREMENT,
            produtos_name VARCHAR(150)
           
          )
          ''')

conn.commit()