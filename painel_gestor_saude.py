import os

def header():
    print("                            CONECTAVIDAS                                     ")
    print("=============================================================================")
    print("                         SAÚDE  - UBS Ibura II                               ")
    print("=============================================================================")

encaminhamentos = [
    {"nome": "Jorge", "idade": 19, "nis": "123.45678.90-1",  "servico": "Oftalmologista", "motivo": "Dores de cabeças constante", "situacao": "Média"},
    {"nome": "Marcos", "idade": 42, "nis": "234.56789.01-2", "servico": "Ressonância Magnética", "motivo": "Suspeita de Apendicite", "situacao": "Urgente"}
    ]


def cadastro_encaminhamento():
    os.system("cls")
    header()
    print("                         Cadastro encaminhamento                               \n")
    nome = input("Nome do paciente: ")    
    idade = int(input("Idade: "))
    nis = input("Número de Identificação Social (NIS): ")
    servico = input("Serviço do encaminhamento: ")
    motivo = input("Motivo do encaminhamento: ")
    situacao = input("Situação (Leve, Médio , Urgente): ")
    perfil_encaminhamento = {
        "nome": nome,
        "idade": idade,
        "nis": nis, 
        "servico": servico, 
        "motivo": motivo, 
        "situacao": situacao
        }
    encaminhamentos.append(perfil_encaminhamento)
    print("Encaminhamento registrado com sucesso!")
    input("\nPressione Enter para voltar ao menu...")
    tela_Inicio()


def painel_encaminhamentos():
    os.system("cls")
    header()
    print("                        PAINEL ENCAMINHAMENTOS            ")
    print("-----------------------------------------------------------------------------")
    for encaminhamento in encaminhamentos:
        L = 35
        nome = encaminhamento["nome"]
        situacao = encaminhamento["situacao"]
        servico  = encaminhamento["servico"]
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

    print("LISTA DE ENCAMINHAMENTOS")

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

    print("EDITAR ENCAMINHAMENTO")

    for i in range(len(encaminhamentos)):
        print(i + 1, "-", encaminhamentos[i]["nome"])

    opcao = int(input("Escolha o número: "))

    e = encaminhamentos[opcao - 1]

    novo_nome = input("Novo nome: ")
    nova_idade = input("Nova idade:")
    novo_nis = input("Novo NIS: ")
    novo_servico = input("Novo serviço: ")
    nova_situacao = input("Nova situação: ")
    novo_motivo = input ("Novo motivo: ")

    if novo_nome != "":
        e["nome"] = novo_nome

    if nova_idade != "":
        e["idade"] = nova_idade

    if novo_nis != "":
        e["nis"] = novo_nis
 
    if novo_servico != "":
        e["servico"] = novo_servico

    if novo_motivo != "":
        e["motivo"] = novo_motivo

    if nova_situacao != "":
        e["situacao"] = nova_situacao

    print("Encaminhamento atualizado!")
    input("Pressione Enter para voltar...")
    tela_Inicio()


def tela_Inicio():
    os.system("cls")
    header()
    print("1 - Cadastro de encaminhamento\n")
    print("2 - Painel de encaminhamentos\n")
    print("3 - Listar encaminhamentos\n")
    print("4 - Editar encaminhamentos\n")
    print("5 - Finalizar sistema\n")
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
            os.system("cls")
            print("Sistema finalizado.")
        else:
            print("Opção inválida, escolha entre 1 - 5.\n")
            tela_Inicio()
    except:
        print("Opção inválida, escolha entre 1 - 5.\n")
        tela_Inicio()        


tela_Inicio()
