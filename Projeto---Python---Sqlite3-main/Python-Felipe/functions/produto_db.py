
def cadastro_produto(conexao,nome,qtd,marca,preco):
    cursor = conexao.cursor()
    sql = f'INSERT INTO produto (produto_nome,produto_qtd,produto_marca,produto_preco) VALUES (?,?,?,?)'
    cursor.execute(sql,[nome,qtd,marca,preco])
    conexao.commit()
    return True

def atualizar_produto(conexao,novo_produto,id,quantidade):
    sql = 'UPDATE produto SET produto_nome=?,produto_qtd=? WHERE produto_id=?'
    cursor = conexao.cursor()
    cursor.execute(sql,[id,novo_produto,quantidade])
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

def cadastro_usuario (conexao,name,password,endereco,cliente,telefone):
    
    cursor = conexao.cursor()
    sql = f'INSERT INTO clientes(cliente_email,cliente_password,cliente_endereco,cliente_nome,cliente_telefone) VALUES (?,?,?,?,?)'
    cursor.execute(sql,[name,password,endereco,cliente,telefone])
    conexao.commit()

def cad_funci (conexao,funcionario,senha1,endere,tele,nom):
      
    cursor = conexao.cursor()
    sql = f'INSERT INTO funcionario(funcionario_email,funcionario_password,funcionario_endereco,funcionario_nome,funcionario_telefone) VALUES (?,?,?,?,?)'
    cursor.execute(sql,[funcionario,senha1,endere,tele,nom])
    conexao.commit()


    

