
from datetime import datetime


def cadastrar(compromissos, contatos):
    titulo = input("Título: ").strip()
    data = input("Data (DD/MM/AAAA): ").strip()
    hora = input("Horário (HH:MM): ").strip()
    descricao = input("Descrição: ").strip()
    cod = input("Código do contato (Enter se não tiver): ").strip()

    if not titulo:
        print("O título é obrigatório!")
        return

    try:
        datetime.strptime(data + " " + hora, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Data ou horário inválido!")
        return

    if cod and cod not in contatos:
        print("Contato não encontrado!")
        return

    compromisso = {
        "titulo": titulo,
        "data": data,
        "hora": hora,
        "descricao": descricao,
        "contato": cod
    }

    compromissos.append(compromisso)
    print("Compromisso cadastrado!")


def listar(compromissos, contatos):
    if not compromissos:
        print("Nenhum compromisso cadastrado.")
        return

    lista = sorted(
        compromissos,
        key=lambda c: datetime.strptime(
            c["data"] + " " + c["hora"], "%d/%m/%Y %H:%M"
        )
    )

    for i, c in enumerate(lista, 1):
        nome = contatos.get(c["contato"], ["Sem contato"])[0]
        print(f"{i} - {c['titulo']} | {c['data']} às {c['hora']} | Contato: {nome}")


def buscar(compromissos, contatos):
    termo = input("Digite a data ou o nome do contato: ").strip().lower()
    achou = False

    for c in compromissos:
        nome = contatos.get(c["contato"], [""])[0]

        if termo == c["data"] or termo in nome.lower():
            print(f"{c['titulo']} - {c['data']} às {c['hora']} | Contato: {nome or 'Não informado'}")
            achou = True

    if not achou:
        print("Compromisso não encontrado!")


def atualizar(compromissos, contatos):
    if not compromissos:
        print("Nenhum compromisso cadastrado.")
        return

    listar(compromissos, contatos)

    try:
        n = int(input("Número do compromisso: "))

        lista = sorted(
            compromissos,
            key=lambda c: datetime.strptime(
                c["data"] + " " + c["hora"], "%d/%m/%Y %H:%M"
            )
        )

        if n < 1 or n > len(lista):
            print("Número não encontrado!")
            return

        c = lista[n - 1]

        titulo = input("Novo título (Enter mantém): ").strip()
        data = input("Nova data (Enter mantém): ").strip()
        hora = input("Novo horário (Enter mantém): ").strip()
        descricao = input("Nova descrição (Enter mantém): ").strip()

        nova_data = data or c["data"]
        nova_hora = hora or c["hora"]

        datetime.strptime(
            nova_data + " " + nova_hora, "%d/%m/%Y %H:%M"
        )

        if titulo:
            c["titulo"] = titulo
        if descricao:
            c["descricao"] = descricao

        c["data"] = nova_data
        c["hora"] = nova_hora

        print("Compromisso atualizado!")

    except ValueError:
        print("Número, data ou horário inválido!")


def cancelar(compromissos, contatos):
    if not compromissos:
        print("Nenhum compromisso cadastrado.")
        return

    listar(compromissos, contatos)

    try:
        n = int(input("Número do compromisso: "))

        lista = sorted(
            compromissos,
            key=lambda c: datetime.strptime(
                c["data"] + " " + c["hora"], "%d/%m/%Y %H:%M"
            )
        )

        if 1 <= n <= len(lista):
            compromissos.remove(lista[n - 1])
            print("Compromisso cancelado!")
        else:
            print("Número não encontrado!")

    except ValueError:
        print("Digite um número válido!")
