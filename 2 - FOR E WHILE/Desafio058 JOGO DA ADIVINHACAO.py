import os
from time import sleep
os.system ('cls' if os.name == 'nt' else 'clear')

# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

computador = (random.randint(0,10)) #Faz o computador pensar
print('-=-'*20)
print('Computador pensando em um número de 0 a 10.')
print('-=-'*20)
'''usuario = int(input('Qual foi o n° escolhido pelo computador? ')) #Usuário tenta adivinhar

if usuario == computador:
    print('Parabéns, você acertou de primeira!!!')
print('-=-'*20)

cont = 1
while usuario != computador:
    if computador > usuario:
        print('É mais...Tente mais uma vez.')
    else:
        print('É menos...Tente mais uma vez.')
    usuario = int(input('Qual seu palpite? '))
    cont += 1
    if usuario == computador:
        print('Parabéns, você acertou!!!')
print('-=-'*20)
print('Foram necessários {} palpites para você vencer.'.format(cont))'''

acertou = False
palpites = 0
while not acertou:
    usuario = int(input('Qual foi o n° escolhido pelo computador? '))
    palpites += 1
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('É mais...Tente mais uma vez.')
        elif usuario > computador:
            print('É menos...Tente mais uma vez.')
print('Parabéns, você acertou!!!')
print('Foram necessários {} palpites para você vencer.'.format(palpites))

