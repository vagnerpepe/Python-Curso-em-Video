#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import os
from time import sleep
os.system ('cls' if os.name == 'nt' else 'clear')

import random

numero = (random.randint(0,5)) #Faz o computador pensar
print('-=-'*20)
print('Computador pensando em um número de 0 a 5.')
print('-=-'*20)
usuario = int(input('Qual foi o n° escolhido pelo computador? ')) #Usuário tenta adivinhar
print('Processando...')
sleep(2)
print('Parabéns, você acertou!!!' if usuario == numero else 'Que pena, tente novamente!')
print('-=-'*20)
if usuario == numero:
    print ('Parabéns, você acertou!!!')
else: print ('Que pena, tente novamente!')


