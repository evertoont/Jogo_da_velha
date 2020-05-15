import random

def printar_tabuleiro(tabuleiro):

    print('     |     |       ')
    print(f'  {tabuleiro[1]}  |  {tabuleiro[2]}  |  {tabuleiro[3]}')
    print('     |     |       ')
    print('------------------')
    print('     |     |       ')
    print(f'  {tabuleiro[4]}  |  {tabuleiro[5]}  |  {tabuleiro[6]}')
    print('     |     |       ')
    print('------------------')
    print('     |     |       ')
    print(f'  {tabuleiro[7]}  |  {tabuleiro[8]}  |  {tabuleiro[9]}')
    print('     |     |       ')


def escolher_marcador():

    marcador = ''
    while not (marcador == 'X' or marcador == 'O'):
        marcador = input('Player 1: Você quer ser X ou O?').upper()

    if marcador == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def marcar_posicao(tabuleiro, marcador, posicao):

    tabuleiro[posicao] = marcador


def checar_vitoria(tabuleiro, marcador):

    return (
        (tabuleiro[1] == marcador and tabuleiro[2] == marcador and tabuleiro[3] == marcador) or
        (tabuleiro[4] == marcador and tabuleiro[5] == marcador and tabuleiro[6] == marcador) or
        (tabuleiro[7] == marcador and tabuleiro[8] == marcador and tabuleiro[9] == marcador) or
        (tabuleiro[1] == marcador and tabuleiro[4] == marcador and tabuleiro[7] == marcador) or
        (tabuleiro[2] == marcador and tabuleiro[5] == marcador and tabuleiro[8] == marcador) or
        (tabuleiro[3] == marcador and tabuleiro[6] == marcador and tabuleiro[9] == marcador) or
        (tabuleiro[1] == marcador and tabuleiro[5] == marcador and tabuleiro[9] == marcador) or
        (tabuleiro[7] == marcador and tabuleiro[5] == marcador and tabuleiro[3] == marcador)
    )


def primeiro_jogar():

    if random.randint(0, 1) == 0:
        return 'Jogador 1'
    else:
        return 'Jogador 2'