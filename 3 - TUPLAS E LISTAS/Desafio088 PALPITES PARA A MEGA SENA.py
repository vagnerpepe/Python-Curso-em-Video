from os import system, name
from time import sleep
system ('cls' if name == 'nt' else 'clear')

# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = list()
jogos = list()
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtdJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {qtdJogos} JOGOS', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
print('-=' * 5, f'< BOA SORTE! >', '-=' * 5)
print()