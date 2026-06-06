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
    print("                        LISTA DE ENCAMINHAMENTOS            ")
    print("=============================================================================")
    if not encaminhamentos:
        print("\nNenhum encaminhamento cadastrado.\n")
        input("Pressione Enter para voltar...")
        tela_Inicio()
        return
    for i, e in enumerate(encaminhamentos, 1):
        print(f"\n  [{i}] Nome......: {e['nome']}")
        print(f"      Idade.....: {e['idade']} anos")
        print(f"      NIS.......: {e['nis']}")
        print(f"      Serviço...: {e['servico']}")
        print(f"      Motivo....: {e['motivo']}")
        print(f"      Situação..: {e['situacao']}")
        print("-----------------------------------------------------------------------------")
    input("\nPressione Enter para voltar ao menu...")
    tela_Inicio()


def editar_encaminhamentos():
    os.system("cls")
    header()
    print("                        EDITAR ENCAMINHAMENTO            ")
    print("=============================================================================")
    if not encaminhamentos:
        print("\nNenhum encaminhamento cadastrado.\n")
        input("Pressione Enter para voltar...")
        tela_Inicio()
        return
    for i, e in enumerate(encaminhamentos, 1):
        print(f"  [{i}] {e['nome']} - {e['servico']} - [{e['situacao']}]")
    print("-----------------------------------------------------------------------------")
    try:
        escolha = int(input("\nDigite o número do encaminhamento que deseja editar: "))
        if escolha < 1 or escolha > len(encaminhamentos):
            print("Número inválido.")
            input("Pressione Enter para voltar...")
            tela_Inicio()
            return
    except:
        print("Entrada inválida.")
        input("Pressione Enter para voltar...")
        tela_Inicio()
        return
    e = encaminhamentos[escolha - 1]
    os.system("cls")
    header()
    print(f"  Editando: {e['nome']}  (deixe em branco para manter o valor atual)\n")
    print("=============================================================================")
    novo_nome     = input(f"  Nome [{e['nome']}]: ").strip()
    nova_idade    = input(f"  Idade [{e['idade']}]: ").strip()
    novo_nis      = input(f"  NIS [{e['nis']}]: ").strip()
    novo_servico  = input(f"  Serviço [{e['servico']}]: ").strip()
    novo_motivo   = input(f"  Motivo [{e['motivo']}]: ").strip()
    nova_situacao = input(f"  Situação [{e['situacao']}]: ").strip()
    if novo_nome:     e["nome"]     = novo_nome
    if nova_idade:
        try:          e["idade"]    = int(nova_idade)
        except:       print("Idade inválida, mantido o valor anterior.")
    if novo_nis:      e["nis"]      = novo_nis
    if novo_servico:  e["servico"]  = novo_servico
    if novo_motivo:   e["motivo"]   = novo_motivo
    if nova_situacao: e["situacao"] = nova_situacao
    print("\n  Encaminhamento atualizado com sucesso!")
    input("  Pressione Enter para voltar ao menu...")
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
