import sqlite3

def cadastro1 (conn,login_name,login_senha):
        
        conn = sqlite3.connect("Loja_database")
        c = conn.cursor()

        c.execute (
        """INSERT INTO administrador (administrador_name,administrador_senha) VALUES (?,?)
        """,
        ["admin","admin"],
         )
        conn.commit()

        cursor = conn.cursor()
        sql = f"select * from administrador WHERE administrador_name='{login_name}' AND administrador_senha='{login_senha}'"
        cursor.execute(sql)
       
        return cursor.fetchall()




   



       