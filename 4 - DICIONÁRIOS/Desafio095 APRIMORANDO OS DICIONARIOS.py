from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = {}
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('\033[mNome do jogador: \033[32m'))
    qtdPartidas = int(input(f'\033[mQuantas partidas {jogador["nome"]} jogou? \033[32m'))
    partidas.clear()
    for c in range(0, qtdPartidas):
        partidas.append(int(input(f'   \033[mQuantos gols na partida {c+1}? \033[32m')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('\033[mQuer continuar? [S/N] \033[32m')).upper()[0]
        if resposta in '\033[mSN':
            break
        print('\033[mERRO! Responda apenas S ou N. \033[32m')
    if resposta == 'N':
        break
print('\033[m-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('\033[mMostrar dados de qual jogador? [999 para PARAR] \033[32m'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\033[mERRO! Não existe jogador com código {busca}!')
    else:
        print(f'\033[m -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('\033[m<< VOLTE SEMPRE >>')
print()