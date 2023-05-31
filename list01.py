"""
Programa de Jokenpô utilizando tratamento de dados 
com try_except, listas, biblioteca random e funções
Retornando a jogada do player e da máquina
ao final mostra o placar de vitórias da máquina, do player e de empates
"""

import random

moves = ["Pedra", "Papel", "Tesoura"]
results = []
PLAYER_VICTORIES = 0
MACHINE_VICTORIES = 0
EMPATE = 0


def menu():
    """
    Exibe o menu do jogo Jokenpô.
    """
    print("Jokenpô.\nEscolha uma das alternativas:")
    print("0 - Sair")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")


def get_player_choice():
    """
    Solicita ao jogador que faça uma escolha e retorna o valor escolhido.

    Returns:
        int: Valor escolhido pelo jogador.
    """
    while True:
        try:
            choice = int(input("Nº: "))
            if choice in [0, 1, 2, 3]:
                return choice
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def evaluate_round(gamer, bot):
    """
    Avalia o resultado de uma rodada do jogo Jokenpô.

    Args:
        gamer (int): Escolha do jogador.
        bot (int): Escolha da máquina.

    Returns:
        str: Resultado da rodada.
    """
    if gamer == bot:
        return "Empate"
    elif (
        (gamer == 1 and bot == 3)
        or (gamer == 2 and bot == 1)
        or (gamer == 3 and bot == 2)
    ):
        return "Player ganhou a rodada"
    else:
        return "A máquina ganhou!"


def print_results():
    """
    Exibe os resultados do jogo Jokenpô.
    """
    print(f"Total de rodadas: {len(results)}")
    print(f"Player: {PLAYER_VICTORIES} vitórias")
    print(f"Máquina: {MACHINE_VICTORIES} vitórias")
    print(f"Empates: {EMPATE}")


menu()
player = get_player_choice()

while player != 0:
    machine = random.randint(1, 3)
    print(f"A máquina jogou: {machine} -> {moves[machine - 1]}")
    RESULT = evaluate_round(player, machine)
    print(RESULT)

    if RESULT == "Empate":
        EMPATE += 1
    elif RESULT == "Player ganhou a rodada":
        PLAYER_VICTORIES += 1
    else:
        MACHINE_VICTORIES += 1

    results.append((machine, player))
    menu()
    player = get_player_choice()

print("Obrigado por jogar!")
print_results()
