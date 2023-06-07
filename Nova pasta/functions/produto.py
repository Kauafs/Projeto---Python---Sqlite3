def cadastrar_produto(conexao, produto):
        cursor = conexao.cursor()

        sql = f'INSERT INTO produtos (produtos_name) VALUES (?)'
        cursor.execute(sql, [produto])
        conexao.commit()
    
        return True