import sqlite3
from functions.usuario_db import login_usuario
import popular_banco
from functions.produto_db import (
    cadastro_produto,
    atualizar_produto,
    deletar_produto,
    listar_produto,
    buscar1_produto,
    venda_produto,
    cadastro_usuario,
    cad_funci,
)


conn = sqlite3.connect("sistema_database")
c = conn.cursor()


def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    popular_banco(conn, email, senha)
    main_interno()


def main_inicial():
    lista = {
        1: login,
        2: exit,
    }

    while True:
        opc = int(input("1- login\n2- Sair \nDigite uma opção: "))
        if opc not in lista:
            print("Opção Inválida.Tente de Novo!")
        else:
            lista[opc]()


def cadastrar():
    nome = input("Digite o nome do produto que deseja Cadastrar: ")
    qtd = int(input("Digite o estoque: "))
    marca = input("Digite a marca do produto: ")
    preco = input("Digite o preço: ")
    cadastro_produto(conn, nome, qtd, marca, preco)


def atualizar():
    id = int(input("Digite o id do Produto: "))
    novo_produto = input("Digite o novo nome do Produto: ")
    quantidade = int(input("Digite o a nova quantidade: "))
    atualizar_produto(conn, id, novo_produto, quantidade)


def buscar():
    produto = listar_produto(conn)
    print(produto)


def deletar():
    id = input("Digite o id do Produto para Deletar: ")
    deletar_produto(conn, id)


def buscar1():
    busca_name = input("Digite o nome do produto para buscar: ")
    buscar1_produto(conn, busca_name)


def venda():
    venda = input("Digite a data da venda: ")
    id_produto = int(input("Digite o id do produto: "))
    id_cliente = input("Digite o id do cliente: ")
    quantidade = int(input("Digite a quantidade: "))
    valor = input("Insira o total da compra: ")
    print("Obrigado,volte sempre!")
    venda_produto(conn, venda, id_produto, id_cliente, quantidade, valor)


def cadastro():
    name = input("Digite seu email: ")
    password = input("Digite sua senha: ")
    endereco = input("Digite seu endereço: ")
    cliente = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    print("Cadastrado com sucesso!")
    cadastro_usuario(conn, name, password, endereco, cliente, telefone)


def cadastro_funcionario():
    funcionario = input("Digite o nome do funcionario: ")
    senha1 = input("Digite sua senha: ")
    endere = input("Digite seu endreço: ")
    tele = int(input("Digite seu telefone: "))
    nom = input("Digite seu nome: ")
    cad_funci(conn, funcionario, senha1, endere, tele, nom)


def main_interno():
    menu = {
        1: cadastrar,
        2: cadastro,
        3: cadastro_funcionario,
        5: atualizar,
        6: buscar,
        7: deletar,
        8: buscar1,
        9: venda,
        10: exit,
    }

    while True:
        opcao = int(
            input(
                "\n1- Cadastrar Produto\n2- Atualizar Produto\n3- Listar Produtos\n4- Deletar Produto\n5- Buscar 1 produto\n6- Venda\n7- Sair\nDigite a opção que deseja: "
            )
        )
        if opcao not in menu:
            print("Opção Inválida. Tente novamente!")
        else:
            menu[opcao]()


main_inicial()
