import os
import json
from datetime import datetime

ARQUIVO_DADOS = "encaminhamentos_saude.json"


def carregar_dados():
    """Carrega os encaminhamentos do arquivo JSON ao iniciar."""
    global encaminhamentos
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            encaminhamentos = json.load(f)


def salvar_dados():
    """Salva os encaminhamentos no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(encaminhamentos, f, ensure_ascii=False, indent=4)


def exportar_relatorio():
    os.system("cls")
    header()

    print("EXPORTAR RELATÓRIO\n")

    if len(encaminhamentos) == 0:
        print("Nenhum encaminhamento para exportar.")
        input("Pressione Enter para voltar...")
        tela_Inicio()
        return

    agora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = f"relatorio_saude_{agora}.txt"

    urgentes = [e for e in encaminhamentos if e["situacao"].lower() == "urgente"]
    medios   = [e for e in encaminhamentos if e["situacao"].lower() == "média"]
    leves    = [e for e in encaminhamentos if e["situacao"].lower() == "leve"]

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("        RELATÓRIO DE ENCAMINHAMENTOS - UBS IBURA II\n")
        f.write(f"        Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        f.write("RESUMO:\n")
        f.write(f"  Total de encaminhamentos: {len(encaminhamentos)}\n")
        f.write(f"  Urgentes: {len(urgentes)}\n")
        f.write(f"  Médios:   {len(medios)}\n")
        f.write(f"  Leves:    {len(leves)}\n\n")
        f.write("=" * 60 + "\n\n")

        # Urgentes primeiro
        for e in sorted(encaminhamentos, key=lambda x: {"urgente": 0, "média": 1, "leve": 2}.get(x["situacao"].lower(), 3)):
            f.write(f"Nome:     {e['nome']}\n")
            f.write(f"Idade:    {e['idade']} anos\n")
            f.write(f"NIS:      {e['nis']}\n")
            f.write(f"Serviço:  {e['servico']}\n")
            f.write(f"Motivo:   {e['motivo']}\n")
            f.write(f"Situação: {e['situacao']}\n")
            f.write("-" * 40 + "\n")

    print(f"\nRelatório exportado com sucesso: {nome_arquivo}")
    input("Pressione Enter para voltar ao menu...")
    tela_Inicio()


def header():
    print("                            CONECTAVIDAS")
    print("=============================================================================")
    print("                         SAÚDE - UBS Ibura II")
    print("=============================================================================")

encaminhamentos = [
    {
        "nome": "Jorge",
        "idade": 19,
        "nis": "123.45678.90-1",
        "servico": "Oftalmologista",
        "motivo": "Dores de cabeça constante",
        "situacao": "Média"
    },
    {
        "nome": "Marcos",
        "idade": 42,
        "nis": "234.56789.01-2",
        "servico": "Ressonância Magnética",
        "motivo": "Suspeita de Apendicite",
        "situacao": "Urgente"
    }
]


def cadastro_encaminhamento():
    os.system("cls")
    header()

    print("CADASTRO DE ENCAMINHAMENTO\n")

    nome = input("Nome do paciente: ")
    idade = int(input("Idade: "))
    nis = input("Número de Identificação Social (NIS): ")
    servico = input("Serviço do encaminhamento: ")
    motivo = input("Motivo do encaminhamento: ")
    situacao = input("Situação (Leve, Média, Urgente): ")

    perfil_encaminhamento = {
        "nome": nome,
        "idade": idade,
        "nis": nis,
        "servico": servico,
        "motivo": motivo,
        "situacao": situacao
    }

    encaminhamentos.append(perfil_encaminhamento)
    salvar_dados()

    print("\nEncaminhamento registrado com sucesso!")
    input("Pressione Enter para voltar ao menu...")
    tela_Inicio()


def painel_encaminhamentos():
    os.system("cls")
    header()

    print("PAINEL DE ENCAMINHAMENTOS")
    print("-----------------------------------------------------------------------------")

    for encaminhamento in encaminhamentos:
        L = 35

        nome = encaminhamento["nome"]
        servico = encaminhamento["servico"]
        situacao = encaminhamento["situacao"]

        linha1 = nome
        linha2 = f"{servico} - [{situacao}]"

        print(f"┌{'─' * L}┐")
        print(f"│ {linha1.ljust(L - 2)} │")
        print(f"│ {linha2.ljust(L - 2)} │")
        print(f"└{'─' * L}┘")

    input("\nPressione Enter para voltar ao menu...")
    tela_Inicio()


def listar_encaminhamentos():
    os.system("cls")
    header()

    print("LISTA DE ENCAMINHAMENTOS\n")

    if len(encaminhamentos) == 0:
        print("Nenhum encaminhamento cadastrado.")
    else:
        for e in encaminhamentos:
            print("------------------------")
            print("Nome:", e["nome"])
            print("Idade:", e["idade"])
            print("NIS:", e["nis"])
            print("Serviço:", e["servico"])
            print("Motivo:", e["motivo"])
            print("Situação:", e["situacao"])

    input("\nPressione Enter para voltar...")
    tela_Inicio()


def editar_encaminhamentos():
    os.system("cls")
    header()

    print("EDITAR ENCAMINHAMENTO\n")

    for i in range(len(encaminhamentos)):
        print(f"{i + 1} - {encaminhamentos[i]['nome']}")

    opcao = int(input("\nEscolha o número: "))

    e = encaminhamentos[opcao - 1]

    novo_nome = input("Novo nome: ")
    novo_servico = input("Novo serviço: ")
    nova_situacao = input("Nova situação: ")

    if novo_nome != "":
        e["nome"] = novo_nome

    if novo_servico != "":
        e["servico"] = novo_servico

    if nova_situacao != "":
        e["situacao"] = nova_situacao

    print("\nEncaminhamento atualizado!")
    salvar_dados()
    input("Pressione Enter para voltar...")
    tela_Inicio()


def tela_Inicio():
    carregar_dados()
    os.system("cls")
    header()

    print("1 - Cadastro de encaminhamento")
    print("2 - Painel de encaminhamentos")
    print("3 - Listar encaminhamentos")
    print("4 - Editar encaminhamentos")
    print("5 - Exportar relatório (.txt)")
    print("6 - Finalizar sistema\n")

    try:
        funcao = int(input("Digite o que deseja visualizar/fazer: "))

        if funcao == 1:
            cadastro_encaminhamento()

        elif funcao == 2:
            painel_encaminhamentos()

        elif funcao == 3:
            listar_encaminhamentos()

        elif funcao == 4:
            editar_encaminhamentos()

        elif funcao == 5:
            exportar_relatorio()

        elif funcao == 6:
            os.system("cls")
            print("Sistema finalizado.")
            return

        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
            tela_Inicio()

    except:
        print("Entrada inválida.")
        input("Pressione Enter para continuar...")
        tela_Inicio()


if __name__ == "__main__":
    tela_Inicio()