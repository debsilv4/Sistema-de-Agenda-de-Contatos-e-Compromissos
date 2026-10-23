
def gerar_relatorio(contatos, compromissos):
    print("\n--- RELATÓRIO DA AGENDA ---")
    print(f"Total de contatos: {len(contatos)}")
    print(f"Total de compromissos: {len(compromissos)}")

    if not contatos:
        print("Nenhum contato cadastrado.")
        return

    print("\nContatos por categoria:")

    for categoria in sorted(set(c[3] for c in contatos.values())):
        total = sum(
            1 for c in contatos.values()
            if c[3] == categoria
        )
        print(f"{categoria}: {total} contato(s)")