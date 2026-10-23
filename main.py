
from contatos import (
    cadastrar, listar, buscar, atualizar,
    remover, sem_email, categorias
)

from compromissos import (
    cadastrar as cadastrar_compromisso,
    listar as listar_compromissos,
    buscar as buscar_compromisso,
    atualizar as atualizar_compromisso,
    cancelar
)

from relatorios import gerar_relatorio


contatos = {}
compromissos = []

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1 - Cadastrar contato")
    print("2 - Listar contatos")
    print("3 - Buscar contato")
    print("4 - Atualizar contato")
    print("5 - Remover contato")
    print("6 - Cadastrar compromisso")
    print("7 - Listar compromissos")
    print("8 - Buscar compromisso")
    print("9 - Atualizar compromisso")
    print("10 - Cancelar compromisso")
    print("11 - Relatório")
    print("12 - Contatos sem e-mail")
    print("13 - Categorias")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar(contatos)
    elif op == "2":
        listar(contatos)
    elif op == "3":
        buscar(contatos)
    elif op == "4":
        atualizar(contatos)
    elif op == "5":
        remover(contatos)
    elif op == "6":
        cadastrar_compromisso(compromissos, contatos)
    elif op == "7":
        listar_compromissos(compromissos, contatos)
    elif op == "8":
        buscar_compromisso(compromissos, contatos)
    elif op == "9":
        atualizar_compromisso(compromissos, contatos)
    elif op == "10":
        cancelar(compromissos, contatos)
    elif op == "11":
        gerar_relatorio(contatos, compromissos)
    elif op == "12":
        sem_email(contatos)
    elif op == "13":
        categorias(contatos)
    elif op == "0":
        print("Agenda encerrada!")
        break
    else:
        print("Opção inválida!")
