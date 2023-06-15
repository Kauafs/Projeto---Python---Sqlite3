def cadastrar_produto(conexao, produto,quantidade,marca):
       
        cursor = conexao.cursor()
        sql = f'INSERT INTO produtos (produtos_name,produtos_marca,produtos_estoque) VALUES (?,?,?)'
        cursor.execute(sql, [produto,quantidade,marca])
        conexao.commit()
    
        return True

def cadastrar_cliente(conexao,cliente,cidade,telefone,mail,password):
        
        cursor = conexao.cursor()
        sql = f'INSERT INTO clientes(clientes_nome, cliente_cidade, cliente_telefone, clientes_email, cliente_senha) VALUES (?,?,?,?,?)'
        cursor.execute(sql, [cliente,cidade,telefone,mail,password])
        conexao.commit()
    
        return True

def atualiza_produto(conexao,novo_produto,id):
       
        sql = 'UPDATE produtos SET produtos_name =? WHERE produtos_id =?'
        cursor = conexao.cursor()
        cursor.execute(sql,[id,novo_produto])
        conexao.commit()

def lista_produto(conexao):
       
        sql = 'SELECT*FROM produtos'
        cursor = conexao.cursor()
        cursor.execute(sql)
        return  cursor.fetchall()

def deleta_produto(conexao,id):
        
        sql = 'DELETE FROM produtos WHERE produtos_id=?'
        cursor = conexao.cursor()
        cursor.execute (sql,[id])
        conexao.commit() 


def buscar1_produto(conn,busca):
        
        sql = 'select*from produtos WHERE produtos_name LIKE ? '
        cursor = conn.cursor()
        cursor.execute(sql,[f'%{busca}%'])
        produto = cursor.fetchall()
        print(produto)

def venda_produtos(conexao,data,id_produto,id_funcionario,id_cliente,quantidade):
    
        cursor = conexao.cursor()
        sql = f'INSERT INTO vendas (vendas_data,produtos_id,funcionario_id,clientes_id,vendas_quantidade) VALUES (?,?,?,?,?)'
        cursor.execute(sql,[data,id_produto,id_funcionario,id_cliente,quantidade])
        conexao.commit()
        return True 

def cadastro_funcionarios (conexao,nome,email,senha,endereco,cidade,telefone):
      
        cursor = conexao.cursor()
        sql = f'INSERT INTO funcionarios(nome,email,password,endereco,cidade,telefone) VALUES (?,?,?,?,?,?)'
        cursor.execute(sql,[nome,email,senha,endereco,cidade,telefone])
        conexao.commit()
