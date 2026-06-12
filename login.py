import os
import time
import painel_assistente
import painel_gestor_escolar
import painel_gestor_saude

def limpar_tela():
    """Limpa o terminal independentemente do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe cabeçalho do Conecta Vidas."""
    print("=" * 54)
    print(" " * 19 + "CONECTA VIDAS")
    print("   Prefeitura do Recife - Integração Inteligente")
    print("\nAcessos de demonstração:")
    print("  assistente / assistente  [Social]")
    print("  saude      / saude       [Saúde]")
    print("  escolar    / escolar     [Escolar]")
    print("=" * 54)

# ==========================================
# BRECHAS PARA AS FUTURAS TELAS (MÓDULOS)
# ==========================================


def tela_saude():
    limpar_tela()
    exibir_cabecalho()
    print("\n" + " " * 14 + "[ MÓDULO SAÚDE ]")
    print("\nBem-vindo(a), Profissional de Saúde!")
    print("-> Aqui você visualizará os dados do e-SUS.")

    input()

def tela_educacao():
    limpar_tela()
    exibir_cabecalho()
    print("\n" + " " * 13 + "[ MÓDULO EDUCAÇÃO ]")
    print("\nBem-vindo(a), Gestor(a) Escolar!")
    print("-> Aqui você fará o controle de evasão e frequência.")
    print("\n[ Funcionalidades em desenvolvimento... ]")
    print("\nPressione ENTER para sair do sistema...")
    input()

# ==========================================
# TELA DE LOGIN PRINCIPAL
# ==========================================

def iniciar_sistema():
    while True:
        limpar_tela()
        exibir_cabecalho()

        print("\n" + " " * 18 + "Acesso ao Sistema\n")

        # Captura de dados (Usamos strip e lower para evitar erros de digitação)
        usuario = input("  Usuário: ").strip().lower()
        senha = input("  Senha: ").strip().lower()

        print("\n  [Autenticando na base de dados...]")
        time.sleep(1.5) # Pausa para simular carregamento

        # Roteamento de Usuários
        if usuario == "assistente" and senha == "assistente":
             print("\nLogin realizado com sucesso!!\n")
             painel_assistente.abrir_painel()

        elif usuario == "saude" and senha == "saude":
            painel_gestor_saude.tela_Inicio()

        elif usuario == "educacao" and senha == "educacao":
            painel_gestor_escolar.tela_Inicio()

        # Adicionado suporte extra para "escolar" caso alguém leia o rodapé da imagem
        elif usuario == "escolar" and senha == "escolar":
            painel_gestor_escolar.tela_Inicio()

        else:
            print("\n  [!] Erro: Usuário ou senha incorretos.")
            print("  Por favor, tente novamente.")
            time.sleep(2) # Espera 2 segundos antes de limpar e pedir de novo

if __name__ == "__main__":
    iniciar_sistema()