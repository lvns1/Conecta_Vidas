import time
import json
import os
from datetime import datetime

# Arquivo de persistência
ARQUIVO_DADOS = "atendimentos.json"

# ''banco de dados''
atendimentos = []


# ==========================================
# MANIPULAÇÃO DE ARQUIVOS
# ==========================================

def carregar_dados():
    """Carrega os atendimentos do arquivo JSON ao iniciar o painel."""
    global atendimentos
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            atendimentos = json.load(f)


def salvar_dados():
    """Salva os atendimentos no arquivo JSON sempre que houver alteração."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(atendimentos, f, ensure_ascii=False, indent=4)


def exportar_relatorio():
    """Exporta todos os atendimentos para um arquivo .txt formatado."""
    if len(atendimentos) == 0:
        print("\nNenhum atendimento para exportar.")
        return

    agora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = f"relatorio_cras_{agora}.txt"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("   RELATÓRIO DE ATENDIMENTOS - CRAS\n")
        f.write(f"   Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n")
        f.write("=" * 50 + "\n\n")

        for i, a in enumerate(atendimentos, start=1):
            f.write(f"{i}. Nome:   {a['nome']}\n")
            f.write(f"   CPF:    {a['cpf']}\n")
            f.write(f"   Motivo: {a['motivo']}\n")
            f.write(f"   Status: {a['status']}\n")
            f.write(f"   Data:   {a.get('data', 'Não registrada')}\n")
            f.write("-" * 50 + "\n")

        f.write(f"\nTotal de atendimentos: {len(atendimentos)}\n")

    print(f"\nRelatório exportado com sucesso: {nome_arquivo}")


def limpar():
    print("\n" * 50)


def menu():
    print("=" * 45)
    print("======================================")
    print("   PAINEL ASSISTENTE SOCIAL - CRAS")
    print("======================================")
    print("=" * 45)
    print("1 - Registrar atendimento")
    print("2 - Listar atendimentos")
    print("3 - Buscar atendimento por nome")
    print("4 - Estatísticas rápidas")
    print("5 - Exportar relatório (.txt)")
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
        "status": "Em análise",
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    atendimentos.append(atendimento)
    salvar_dados()

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
    carregar_dados()
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
        elif opcao == "5":
            exportar_relatorio()
        elif opcao == "0":
            limpar()
            print("\nSaindo do painel...")
            time.sleep(1)
            break
        else:
            print("Opção inválida!")

        input("\nPressione ENTER para continuar...")