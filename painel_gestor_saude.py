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

    tela_Inicio()


def painel_encaminhamentos():
    # mostrar os encaminhamentos (nome, serviço, gravidade/situação)
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
    
    


def listar_encaminhamentos():
    # listar os encaminhamentos com todas as informações (nome, idade, NIS, serviço, motivo, gravidade/situação)
    pass


def editar_encaminhamentos():
    pass


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
            print("listar")
        elif funcao == 4:
            print("editar")
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
