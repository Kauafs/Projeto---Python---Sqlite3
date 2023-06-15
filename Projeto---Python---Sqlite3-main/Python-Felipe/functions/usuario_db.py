def login_usuario(conexao, email, senha):
    cursor = conexao.cursor()
    sql = (
        sql
    ) = f"INSERT INTO login(login_email,login_password) VALUES (?,?)"
    cursor.execute(sql, [email, senha])

    return cursor.fetchall()
