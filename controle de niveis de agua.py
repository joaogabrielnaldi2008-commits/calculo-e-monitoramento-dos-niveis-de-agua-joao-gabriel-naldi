
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com as situações dos níveis de água
niveis_agua = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simulação do nível atual do reservatório
nivel_atual = 1

# Verifica se o nível é válido e exibe o alerta
if 1 <= nivel_atual <= len(niveis_agua):
    cor = definir_cor(nivel_atual)
    mensagem = niveis_agua[nivel_atual - 1]

    print(cor + mensagem + Style.RESET_ALL)
else:
    print("Nível inválido!")
