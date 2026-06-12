import os




def header():
    print("                           CONECTAVIDAS")
    print("=============================================================================")
    print("                      EDUCAÇÃO - GESTOR ESCOLAR")
    print("=============================================================================")

alunos = [
    {"nome": "João", "idade": 7, "ano": "3º Ano", "faltas": 12},
    {"nome": "Maria", "idade": 8, "ano": "4º Ano", "faltas": 6},
    {"nome": "Pedro", "idade": 6, "ano": "1º Ano", "faltas": 15}
]


def inserir_dados():
    os.system("cls")
    header()

    print("                       CADASTRO DE ALUNO")
    print("=============================================================================\n")

    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    ano = input("Ano/Turma: ")
    faltas = int(input("Quantidade de faltas: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "ano": ano,
        "faltas": faltas
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")
    input("\nPressione Enter para voltar ao menu...")
    tela_Inicio()


def painel_encaminhamento():
    os.system("cls")
    header()

    print("                    PAINEL DE ENCAMINHAMENTOS")
    print("=============================================================================\n")

    for aluno in alunos:

        if aluno["faltas"] >= 10:
            status = "Encaminhar"
        elif aluno["faltas"] >= 5:
            status = "Atenção"
        else:
            status = "Regular"

        print(f"┌──────────────────────────────────────────────┐")
        print(f"│ Nome: {aluno['nome']:<37}│")
        print(f"│ Idade: {str(aluno['idade']) + ' anos':<36}│")
        print(f"│ Turma: {aluno['ano']:<36}│")
        print(f"│ Faltas: {str(aluno['faltas']):<35}│")
        print(f"│ Status: {status:<35}│")
        print(f"└──────────────────────────────────────────────┘\n")

    input("Pressione Enter para voltar ao menu...")
    tela_Inicio()


def listar_encaminhamentos():
    os.system("cls")
    header()

    print("                    LISTA DE ALUNOS")
    print("=============================================================================\n")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Turma: {aluno['ano']}")
            print(f"Faltas: {aluno['faltas']}")
            print("-" * 40)

    input("\nPressione Enter para voltar...")
    tela_Inicio()


def editar_encaminhamentos():
    os.system("cls")
    header()

    print("                    EDITAR ALUNO")
    print("=============================================================================\n")

    for i, aluno in enumerate(alunos, start=1):
        print(f"{i} - {aluno['nome']}")

    try:
        opcao = int(input("\nEscolha o número do aluno: "))

        aluno = alunos[opcao - 1]

        novo_nome = input("Novo nome: ")
        nova_idade = input("Nova idade: ")
        novo_ano = input("Nova turma: ")
        novas_faltas = input("Nova quantidade de faltas: ")

        if novo_nome != "":
            aluno["nome"] = novo_nome

        if nova_idade != "":
            aluno["idade"] = int(nova_idade)

        if novo_ano != "":
            aluno["ano"] = novo_ano

        if novas_faltas != "":
            aluno["faltas"] = int(novas_faltas)

        print("\nAluno atualizado com sucesso!")

    except:
        print("\nAluno inválido!")

    input("\nPressione Enter para voltar...")
    tela_Inicio()


def tela_Inicio():
    os.system("cls")
    header()

    print("1 - Inserir dados de aluno")
    print("2 - Painel de encaminhamentos")
    print("3 - Listar encaminhamentos")
    print("4 - Editar encaminhamentos")
    print("5 - Finalizar sistema\n")

    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            inserir_dados()

        elif opcao == 2:
            painel_encaminhamento()

        elif opcao == 3:
            listar_encaminhamentos()

        elif opcao == 4:
            editar_encaminhamentos()

        elif opcao == 5:
            os.system("cls")
            print("Sistema finalizado.")
            return

        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")
            tela_Inicio()

    except:
        print("\nEntrada inválida!")
        input("Pressione Enter para continuar...")
        tela_Inicio()


if __name__ == "__main__":
    tela_Inicio()