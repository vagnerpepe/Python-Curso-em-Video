from os import system, name
from random import randint
from time import sleep
system ('cls' if name == 'nt' else 'clear')

# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for valor in range(0, 5):
        sorteando = randint(1, 10)
        lista.append(sorteando)
        sleep(0.3)
        print(f'{sorteando} ', end='')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = [] #lista
sorteia(numeros)
somaPar(numeros)