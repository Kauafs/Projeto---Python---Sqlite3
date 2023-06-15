import sqlite3

conn = sqlite3.connect("sistema_database")
c = conn.cursor()

c.execute(
    """
            CREATE TABLE login(
            login_id INTEGER PRIMARY KEY AUTOINCREMENT,
            login_email VARCHAR(150),
            login_password VARCHAR (150)
            )

        """
)
conn.commit()


conn = sqlite3.connect("sistema_database")
c = conn.cursor()

c.execute(
    """
            CREATE TABLE funcionario(
            funcionario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            funcionario_email VARCHAR(150),
            funcionario_password VARCHAR (150),
            funcionario_endereco VARCHAR (150),
            funcionario_nome VARCHAR (150),
            funcionario_telefone NUMERIC (22)
            )

        """
)
conn.commit()


conn = sqlite3.connect("sistema_database")
c = conn.cursor()

c.execute(
    """
            CREATE TABLE clientes(
            clientes_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_email VARCHAR(150),
            cliente_password VARCHAR (150),
            cliente_endereco VARCHAR (150),
            cliente_nome VARCHAR (150),
            cliente_telefone NUMERIC (22)
            )

        """
)
conn.commit()


conn = sqlite3.connect("sistema_database")
c = conn.cursor()

c.execute(
    """
            CREATE TABLE produto(
            produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_nome VARCHAR(150),
            produto_qtd NUMERIC (22),
            produto_marca VARCHAR (150),
            produto_preco NUMERIC (22)
            )

        """
)
conn.commit()


conn = sqlite3.connect("sistema_database")
c = conn.cursor()

c.execute(
    """
            CREATE TABLE venda(
            venda_id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_data VARCHAR (150),
            venda_qtd  NUMERIC (22),
            venda_total NUMERIC (22),
            produto_id INTEGER NOT NULL REFERENCES produto(produto_id),
            clientes_id INTEGER NOT NULL REFERENCES clientes(clientes_id)
            )
        
        """
)

conn.commit()
