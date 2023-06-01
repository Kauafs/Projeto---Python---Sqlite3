def cadastro_produto(conexao,nome):
    cursor = conexao.cursor()

    sql = f'INSERT INTO produto (produto_nome) VALUES (?)'
    cursor.execute(sql,[nome])
    conexao.commit()
    return True

def atualizar_produto(conexao,novo_produto,id):
    sql = 'UPDATE produto SET produto_nome=? WHERE produto_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql,[novo_produto,id])
    conexao.commit()

def deletar_produto(conexao,id):
    sql = 'DELETE FROM produto WHERE produto_id=?'
    cursor = conexao.cursor()
    cursor.execute (sql, [id])
    conexao.commit() 

def buscar_produto(conexao):
    sql = 'SELECT*FROM produto'
    cursor = conexao.cursor()
    cursor.execute(sql)
    return  cursor.fetchall()
    

