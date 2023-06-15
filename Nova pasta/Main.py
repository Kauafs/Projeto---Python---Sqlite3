import sqlite3
from functions.cad_usuarios import cadastro1
from functions.produto import cadastrar_produto, cadastrar_cliente,atualiza_produto,lista_produto,deleta_produto,buscar1_produto, venda_produtos, cadastro_funcionarios

conn = sqlite3.connect('Loja_database') 
c = conn.cursor()


def login():

    login_usuario = input('Digite seu email: ')
    senha_usuario = input('Digite sua senha: ')
    usuario_autenticado =  cadastro1(conn,login_usuario,senha_usuario)
    if len(usuario_autenticado) > 0:  
        print('Autenticado com Sucesso')
        crud_interno()
    print(len(usuario_autenticado) > 0 )

def main():

    cardapio = {
        
        1:login,
        2:exit,
    }
    while True:

        opc = int(input('\nBem Vindo!\nDigite 1 para realizar o login! \n1 - Login: '))
        if  opc not in cardapio:
            print('Opção inválida')
        else:
            cardapio[opc]()

def cadastro_produto():

    produto = input ('Digite o nome do Produto que deseja cadastrar: ')
    quantidade = int (input('Digite o estoque: '))
    marca = input('Digite a marca do produto: ')
    cadastrar_produto(conn,produto,quantidade,marca)

def cadastro_cliente():

    cliente = input ('Digite seu Nome: ')
    cidade = input ('Digite sua Cidade: ')
    telefone = int (input('Digite seu telefone: '))
    mail = input ('Digite seu email: ')
    password = input ('Digite sua senha: ')
    cadastrar_cliente(conn,cliente,cidade,telefone,mail,password)

def atualizar_produto ():

    id = int (input('Digite o id do Produto: '))
    novo_produto = input ('Digite o novo Produto: ')
    atualiza_produto(conn,id,novo_produto)

def listar_produto ():

    utensilio = lista_produto(conn)
    print(utensilio)

def deletar_produto():

    id = int(input('Digite o id do Produto para Deletar: '))
    deleta_produto(conn,id)

def buscar_nome ():

    busca = input ('Digite a letra ou nome do produto para buscar: ')
    buscar1_produto(conn,busca)

def venda_produto():

    data = (input('Digite a data da venda: '))
    id_produto = int(input('Digite o id do produto: '))
    id_funcionario = (input('Id do funcionario: '))
    id_cliente = int (input('Id do cliente: '))
    quantidade =  int(input('Digite a quantidade: '))
    print('Obrigado,volte sempre!')
    venda_produtos(conn,data,id_produto,id_funcionario,id_cliente,quantidade)

def cadastro_funcionario ():

    nome = input('Digite seu nome: ')
    email = input ('Digite sua email: ')
    senha = input ('Digite sua senha: ')
    endereco = input ('Digite seu endereço: ')
    cidade = input ('Digite sua cidade: ')
    telefone = int (input ('Digite seu telefone: '))
    cadastro_funcionarios(conn,nome,email,senha,endereco,cidade,telefone)
    print('Cadastrado com sucesso!')
 

def crud_interno():

    menu =  {
        1:cadastro_produto,
        2:cadastro_cliente,
        3:atualizar_produto,
        4:listar_produto,
        5:deletar_produto,
        6:buscar_nome,
        7:venda_produto,
        8:cadastro_funcionario,
        9:exit,
    }

    while True:
        
        opcao = int(input('\n1- Cadastro Produto\n2- Cadastro cliente\n3- Atualizar Prooduto\n4- Listar Produtoz\n5- Deletar Produto\n6- Buscar nome\n7- Venda Produto\n8- Cadastro funcionario\n9- Sair\nDigite uma opção do crud interno: '))
        if opcao not in menu:
            print('Opção inválida')
        else:
            menu[opcao]()

main()