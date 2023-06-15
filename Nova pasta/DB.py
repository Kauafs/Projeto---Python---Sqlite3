import sqlite3

conn = sqlite3.connect('Loja_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE administrador(
            administrador_id INTEGER PRIMARY KEY AUTOINCREMENT,
            administrador_name VARCHAR(25),
            administrador_senha VARCHAR(25)
          )
          ''')

conn.commit()

conn = sqlite3.connect('Loja_database')
c = conn.cursor()

c.execute('''
            CREATE TABLE funcionarios(
            funcionarios_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR (150),
            cidade VARCHAR (150),
            telefone NUMERIC (22),
            email VARCHAR (22),
            password VARCHAR (150),
            endereco VARCHAR (150)
            
            )

        ''')
conn.commit()


conn = sqlite3.connect('Loja_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE clientes(
            clientes_id INTEGER PRIMARY KEY AUTOINCREMENT,
            clientes_nome VARCHAR (150),
            cliente_cidade VARCHAR (150),
            cliente_telefone NUMERIC (22),
            clientes_email VARCHAR(150),
            cliente_senha VARCHAR(150)
          )
          ''')

conn.commit()

conn = sqlite3.connect('Loja_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE produtos(
            produtos_id INTEGER PRIMARY KEY AUTOINCREMENT,
            produtos_name VARCHAR(150),
            produtos_marca VARCHAR (150),
            produtos_estoque NUMERIC (22)
           
          )
          ''')

conn.commit()



conn = sqlite3.connect('Loja_database')
c = conn.cursor()

c.execute('''
            CREATE TABLE vendas(
            vendas_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vendas_data VARCHAR (150),
            vendas_quantidade  NUMERIC (22),
            funcionario_id INTEGER NOT NULL REFERENCES funcionario(funcionario_id),
            produtos_id INTEGER NOT NULL REFERENCES produto(produto_id),
            clientes_id INTEGER NOT NULL REFERENCES clientes(clientes_id)
            )
        
        ''')
conn.commit()
