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
            usuario_autenticado = login_usuario (conn,
                                                 email,         senha)
            print(len(usuario_autenticado) > 0)
        elif opc == 3:
            print('Deslogado com Sucesso')
            break

def main_interno():

    global opc
    
    while (opc!=5):
        print('1- Cadastrar Produto\n2- Alterar Produto\n3- Remover Produto\n4- Buscar Produto\n5- Exibir 1 Produto')
        opc = int(input('Digite a opção: '))

        if opc == 1:
            nome = input ('Digite o nome do produto: ')
            cadastro_produto(conn,nome)
        elif opc == 2:
            id = int (input('Digite o id do Produto: '))
            novo_produto = input ('Digite o novo produto: ')
            atualizar_produto(conn,novo_produto,id)
        elif opc == 3:
            id = int (input('Digite o id para deletar: '))
            deletar_produto(conn,id)
        elif opc == 4:
            produtos = buscar_produto(conn)
            print(produtos)
            

main_inicial()
login_usuario()
main_interno()




