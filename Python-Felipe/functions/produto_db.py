
def cadastro_produto(conexao,nome,qtd,marca,preco):
    cursor = conexao.cursor()
    sql = f'INSERT INTO produto (produto_nome,produto_qtd,produto_marca,produto_preco) VALUES (?,?,?,?)'
    cursor.execute(sql,[nome,qtd,marca,preco])
    conexao.commit()
    return True

def atualizar_produto(conexao,novo_produto,id):
    sql = 'UPDATE produto SET produto_nome=? WHERE produto_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql,[id,novo_produto])
    conexao.commit()

def deletar_produto(conexao,id):
    sql = 'DELETE FROM produto WHERE produto_id=?'
    cursor = conexao.cursor()
    cursor.execute (sql, [id])
    conexao.commit() 

def listar_produto(conexao):
    sql = 'SELECT*FROM produto'
    cursor = conexao.cursor()
    cursor.execute(sql)
    return  cursor.fetchall()

def buscar1_produto(conn,busca_name):
    sql = 'select*from produto WHERE produto_nome LIKE ? '
    cursor = conn.cursor()
    cursor.execute(sql,[f'%{busca_name}%'])
    produto = cursor.fetchall()
    print(produto)

def venda_produto(conexao,venda,nick_produto,id_produto,quantidade,valor):
    
    cursor = conexao.cursor()
    sql = f'INSERT INTO venda (venda_data,produto_id,clientes_id,venda_qtd,venda_total) VALUES (?,?,?,?,?)'
    cursor.execute(sql,[venda,nick_produto,id_produto,quantidade,valor])
    conexao.commit()
    return True
    

