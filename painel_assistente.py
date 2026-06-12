import time

# ''banco de dados''
atendimentos = []

def limpar():
    print("\n" * 50)


def menu():
    print("=" * 45)
    print("   PAINEL ASSISTENTE SOCIAL - CRAS")
    print("=" * 45)
    print("1 - Registrar atendimento")
    print("2 - Listar atendimentos")
    print("3 - Buscar atendimento por nome")
    print("4 - Estatísticas rápidas")
    print("0 - Sair")
    print("=" * 45)


def registrar_atendimento():
    print("\n--- NOVO ATENDIMENTO ---")
    nome = input("Nome do cidadão: ").strip()
    cpf = input("CPF: ").strip()
    motivo = input("Motivo do atendimento: ").strip()

    atendimento = {
        "nome": nome,
        "cpf": cpf,
        "motivo": motivo,
        "status": "Em análise"
    }

    atendimentos.append(atendimento)

    print("\nRegistrando atendimento...")
    time.sleep(1)

    print("Atendimento registrado com sucesso!")


def listar_atendimentos():
    print("\n--- LISTA DE ATENDIMENTOS ---")

    if len(atendimentos) == 0:
        print("Nenhum atendimento registrado.")
        return

    for i, a in enumerate(atendimentos, start=1):
        print(f"\n{i}. Nome: {a['nome']}")
        print(f"   CPF: {a['cpf']}")
        print(f"   Motivo: {a['motivo']}")
        print(f"   Status: {a['status']}")


def buscar_atendimento():
    nome_busca = input("\nDigite o nome para busca: ").strip().lower()

    encontrados = [
        a for a in atendimentos
        if nome_busca in a["nome"].lower()
    ]

    if not encontrados:
        print("Nenhum atendimento encontrado.")
        return

    print("\n--- RESULTADOS ---")
    for a in encontrados:
        print(f"Nome: {a['nome']} | CPF: {a['cpf']} | Status: {a['status']}")


def estatisticas():
    print("\n--- ESTATÍSTICAS ---")
    print(f"Total de atendimentos: {len(atendimentos)}")

    if len(atendimentos) > 0:
        print("Sistema ativo e recebendo registros.")
    else:
        print("Sistema ainda sem registros.")


def abrir_painel():
    while True:
        limpar()
        menu()

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            registrar_atendimento()
        elif opcao == "2":
            listar_atendimentos()
        elif opcao == "3":
            buscar_atendimento()
        elif opcao == "4":
            estatisticas()
        elif opcao == "0":
            limpar()
            print("\nSaindo do painel...")
            time.sleep(1)
            break
        else:
            print("Opção inválida!")

        input("\nPressione ENTER para continuar...")