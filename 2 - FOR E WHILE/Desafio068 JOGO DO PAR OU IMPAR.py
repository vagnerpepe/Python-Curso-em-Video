import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vitoria = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    print('-'*30)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador+computador} ', end= '')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('-'*30)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-'*15)
        else:
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('-'*30)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-'*15)
        else:
            break
    vitoria += 1
print('-'*30)
print('Você PERDEU!')
print('=-'*15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
print()
