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