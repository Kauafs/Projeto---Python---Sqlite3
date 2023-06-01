import sqlite3
from functions.usuario_db import cadastro_usuario, login_usuario
from functions.produto_db import cadastro_produto, atualizar_produto, deletar_produto, buscar_produto

conn = sqlite3.connect('sistema_database')
c = conn.cursor()

opc = 0

def main_inicial():

    global opc
    
    while(opc !=2):
        print('1 - Cadastrar Usuário\n2 - Realizar login\n3 - Sair do sistema')
        opc = int(input('Digite a opção: '))

        if opc == 1:
            name = input('Digite seu email: ')
            password = input ('Digite sua senha: ')
            cadastro_usuario(conn,name,password)
          
        elif opc == 2:             
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            
            usuario_autenticado = login_usuario (conn,email,senha)
            print(len(usuario_autenticado) > 0)
        else:
                print('Deslogado com Sucesso')
                break

def main_interno():

    menu = {
        1: cadastro_produto,
        2: atualizar_produto,
        3: deletar_produto,
        4: buscar_produto,
    }

    while True:
        opcao = int(input('Digite a opção que deseja: '))
        menu[opcao]()



       

      
       
       
       
     
       

        


main_inicial()
main_interno()





