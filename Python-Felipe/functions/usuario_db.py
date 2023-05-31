def cadastro_usuario (conexao,name,password):
    cursor = conexao.cursor()
    
    sql = f'INSERT INTO clientes(cliente_email,cliente_password) VALUES (?,?)'
    cursor.execute(sql,[name,password])
    conexao.commit()

def login_usuario(conexao,email,senha):
    cursor = conexao.cursor()
    sql = 'select * from clientes WHERE cliente_email=? and cliente_password=?'
    cursor.execute(sql,
                   [email,senha
    ])
    return cursor.fetchall()
