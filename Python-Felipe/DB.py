import sqlite3 

conn = sqlite3.connect('sistema_database')
c = conn.cursor()

c.execute('''
            CREATE TABLE clientes(
            clientes_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_email VARCHAR(150),
            cliente_password VARCHAR (150)
            )

        ''')
conn.commit()


conn = sqlite3.connect('sistema_database')
c = conn.cursor()

c.execute('''
            CREATE TABLE produto(
            produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_nome VARCHAR(150)
            )

        ''')
conn.commit()







