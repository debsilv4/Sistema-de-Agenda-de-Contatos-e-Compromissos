
def cadastrar(contatos):
    cod = input("Código do contato: ").strip()

    if not cod:
        print("O código é obrigatório!")
        return

    if cod in contatos:
        print("Esse código já existe!")
        return

    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    categoria = input("Categoria: ").strip()

    if not nome:
        print("O nome é obrigatório!")
        return

    contatos[cod] = [nome, telefone, email, categoria]
    print("Contato cadastrado!")


def listar(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for cod, c in contatos.items():
        print(f"Código: {cod} | Nome: {c[0]} | Telefone: {c[1]} | E-mail: {c[2]} | Categoria: {c[3]}")


def buscar(contatos):
    termo = input("Digite o nome ou código: ").strip().lower()
    achou = False

    for cod, c in contatos.items():
        if termo in cod.lower() or termo in c[0].lower():
            print(f"Código: {cod} | Nome: {c[0]} | Telefone: {c[1]} | E-mail: {c[2]} | Categoria: {c[3]}")
            achou = True

    if not achou:
        print("Contato não encontrado!")


def atualizar(contatos):
    cod = input("Código do contato que deseja atualizar: ").strip()

    if cod not in contatos:
        print("Contato não encontrado!")
        return

    c = contatos[cod]

    nome = input("Novo nome (Enter mantém): ").strip()
    telefone = input("Novo telefone (Enter mantém): ").strip()
    email = input("Novo e-mail (Enter mantém): ").strip()
    categoria = input("Nova categoria (Enter mantém): ").strip()

    if nome:
        c[0] = nome
    if telefone:
        c[1] = telefone
    if email:
        c[2] = email
    if categoria:
        c[3] = categoria

    print("Contato atualizado!")


def remover(contatos):
    cod = input("Código do contato que deseja remover: ").strip()

    if cod in contatos:
        del contatos[cod]
        print("Contato removido!")
    else:
        print("Contato não encontrado!")


def sem_email(contatos):
    encontrou = False

    for cod, c in contatos.items():
        if not c[2]:
            print(f"{cod} - {c[0]}")
            encontrou = True

    if not encontrou:
        print("Todos os contatos possuem e-mail.")


def categorias(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    for categoria in sorted(set(c[3] for c in contatos.values())):
        print(categoria)
