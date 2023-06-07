def cadastrar_usuario(conexao, nome, senha):
        cursor = conexao.cursor()

        sql = f'INSERT INTO usuarios(usuario_name, usuario_senha) VALUES (?, ?)'
        cursor.execute(sql, [nome, senha])
        conexao.commit()
    
        return True

def autenticar(conexao, usuario, senha):
        cursor = conexao.cursor()
        sql = 'select * from usuarios WHERE usuario_name=? and usuario_senha=?'
        cursor.execute(sql, [
        usuario, senha
    ])
        return cursor.fetchall()