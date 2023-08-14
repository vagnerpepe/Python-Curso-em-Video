# Crie um programa que faça o computador jogar Jokenpô com você.

import os
from time import sleep
os.system ('cls' if os.name == 'nt' else 'clear')

import random

itens = ('Pedra', 'Papel', 'Tesoura')
print('Vai começar o jogo!!!')
computador = random.randint(0,2)
print('O computador escolheu sua jogada.')
print('Sua vez...')
print('''Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=-'*11)
print('O computador jogou {}.'.format(itens[computador]))
print('E você jogou {}.'.format(itens[jogador]))
print('-=-'*11)
if computador == 0:# Se o computador jogou Pedra
    if jogador == 0:
        print('Eita, vocês empataram!!!')
    elif jogador == 1:
        print('Parabéns!!! Você ganhou!!!')
    elif jogador == 2:
        print('Que pena, você perdeu.')
        print('Jogue novamente!')
    else:
        ('Jogada inválida.')
elif computador == 1:# Se o computador jogou Papel
    if jogador == 1:
        print('Eita, vocês empataram!!!')
    elif jogador == 2:
        print('Parabéns!!! Você ganhou!!!')
    elif jogador == 0:
        print('Que pena, você perdeu.')
        print('Jogue novamente!')
    else:
        ('Jogada inválida.')
elif computador == 2:# Se o computador jogou Tesoura
    if jogador == 2:
        print('Eita, vocês empataram!!!')
    elif jogador == 0:
        print('Parabéns!!! Você ganhou!!!')
    elif jogador == 1:
        print('Que pena, você perdeu.')
        print('Jogue novamente!')
    else:
        ('Jogada inválida.')
