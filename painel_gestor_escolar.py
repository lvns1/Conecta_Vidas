import os
import json
from datetime import datetime

ARQUIVO_DADOS = "alunos.json"


def carregar_dados():
    """Carrega os alunos do arquivo JSON ao iniciar."""
    global alunos
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            alunos = json.load(f)


def salvar_dados():
    """Salva a lista de alunos no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, ensure_ascii=False, indent=4)


def exportar_relatorio():
    os.system("cls")
    header()

    print("                    EXPORTAR RELATÓRIO")
    print("=============================================================================\n")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado para exportar.")
        input("\nPressione Enter para voltar...")
        tela_Inicio()
        return

    agora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = f"relatorio_escolar_{agora}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("        RELATÓRIO ESCOLAR - CONECTA VIDAS\n")
        f.write(f"        Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        regulares = [a for a in alunos if a["faltas"] < 5]
        atencao   = [a for a in alunos if 5 <= a["faltas"] < 10]
        encaminhar = [a for a in alunos if a["faltas"] >= 10]

        f.write(f"RESUMO:\n")
        f.write(f"  Total de alunos:      {len(alunos)}\n")
        f.write(f"  Status Regular:       {len(regulares)}\n")
        f.write(f"  Status Atenção:       {len(atencao)}\n")
        f.write(f"  Para Encaminhar:      {len(encaminhar)}\n\n")
        f.write("=" * 60 + "\n\n")

        for a in alunos:
            if a["faltas"] >= 10:
                status = "ENCAMINHAR"
            elif a["faltas"] >= 5:
                status = "ATENÇÃO"
            else:
                status = "Regular"

            f.write(f"Nome:   {a['nome']}\n")
            f.write(f"Idade:  {a['idade']} anos\n")
            f.write(f"Turma:  {a['ano']}\n")
            f.write(f"Faltas: {a['faltas']}\n")
            f.write(f"Status: {status}\n")
            f.write("-" * 40 + "\n")

    print(f"Relatório exportado com sucesso: {nome_arquivo}")
    input("\nPressione Enter para voltar ao menu...")
    tela_Inicio()


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
    salvar_dados()

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
        salvar_dados()

    except:
        print("\nAluno inválido!")

    input("\nPressione Enter para voltar...")
    tela_Inicio()


def tela_Inicio():
    carregar_dados()
    os.system("cls")
    header()

    print("1 - Inserir dados de aluno")
    print("2 - Painel de encaminhamentos")
    print("3 - Listar encaminhamentos")
    print("4 - Editar encaminhamentos")
    print("5 - Exportar relatório (.txt)")
    print("6 - Finalizar sistema\n")

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
            exportar_relatorio()

        elif opcao == 6:
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