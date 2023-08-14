from os import system, name
from time import sleep
system ('cls' if name == 'nt' else 'clear')

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    maior = 0
    for valor in valores:
        print(f'{valor} ', end='')
        sleep(0.3)
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()