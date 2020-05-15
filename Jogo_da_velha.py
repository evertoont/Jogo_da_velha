import random
import os

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


def checar_espaco(tabuleiro, posicao):

    return tabuleiro[posicao] == ' '


def checagem_empate(tabuleiro):
    for i in range(1, 10):
        if checar_espaco(tabuleiro, i):
            return False
    return True


def escolha_jogada(tabuleiro, jogador):

    posicao = ' '
    while posicao not in '1 2 3 4 5 6 7 8 9'.split() or not checar_espaco(tabuleiro, int(posicao)):

        posicao = input(f'{jogador} escolha sua jogada entre 1-9:')

    return int(posicao)


def replay():

    return input('Você quer jogar novamente? SIM ou NÃO?').lower().startswith('s')


while True:

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Bem vindo ao jogo da velha!')

    tabuleiro = [' '] * 10
    jogador_1, jogador_2 = escolher_marcador()
    turno_jogador = primeiro_jogar()
    print(turno_jogador, 'começa!')
    status_jogo = True

    while status_jogo:

        if turno_jogador == 'Jogador 1':
            printar_tabuleiro(tabuleiro)
            posicao_jogada = escolha_jogada(tabuleiro, turno_jogador)
            marcar_posicao(tabuleiro, jogador_1, posicao_jogada)

            if checar_vitoria(tabuleiro, jogador_1):
                printar_tabuleiro(tabuleiro)
                print("Parabéns você ganhou a partida!")
                status_jogo = False
            else:
                if checagem_empate(tabuleiro):
                    printar_tabuleiro(tabuleiro)
                    print("O jogo empatou !!!")
                    break
                else:
                    turno_jogador = 'Jogador 2'

        else:
            printar_tabuleiro(tabuleiro)
            posicao_jogada = escolha_jogada(tabuleiro, turno_jogador)
            marcar_posicao(tabuleiro, jogador_2, posicao_jogada)

            if checar_vitoria(tabuleiro, jogador_2):
                printar_tabuleiro(tabuleiro)
                print("Parabéns você ganhou a partida!")
                status_jogo = False
            else:
                if checagem_empate(tabuleiro):
                    printar_tabuleiro(tabuleiro)
                    print("O jogo empatou !!!")
                    break
                else:
                    turno_jogador = 'Jogador 1'


    if not replay():
        break
