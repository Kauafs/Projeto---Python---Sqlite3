import sqlite3
from functions.cad_usuarios import cadastrar_usuario,autenticar
from functions.produto import cadastrar_produto

conn = sqlite3.connect('teste_database') 
c = conn.cursor()

opc = 0

def main():

    global opc
    
    while(opc != 3):
        print("1- Cadastro usuario\n2- Realizar login")
        opc = int(input("Digite a opção: "))
        
        if opc == 1:
            nome = input("Digite o novo usuário: ")
            senha = input("Digite a nova senha: ")
            cadastrar_usuario(conn, nome, senha)

        elif opc == 2:
            usuario = input("Digite usuario: ")
            senha = input("Digite senha: ")
            usuario_autenticado = autenticar(conn,usuario,senha)
            if len(usuario_autenticado) > 0:
                crud_interno()
            print(len(usuario_autenticado) > 0)
        else:
            print('Número inválido. Tente mais um vez')
            main()

def cadastro():

    produto = input ('Digite o nome do Produto que deseja cadastrar: ')
    cadastrar_produto(conn,produto)



def crud_interno():

    menu =  {
        1:cadastro,

    }

    while True:
        
        opcao = int(input('Digite uma opção do crud interno: '))
        menu[opcao]()

main()