#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

import os
os.system ('cls' if os.name == 'nt' else 'clear')

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

if n1 > n2:
    print('O 1° número é maior.')
    print('O 2° número é menor')
elif n2 > n1:
    print('O 2° número é maior.')
    print('O 1° número é menor.')
else:
    print('Não existe valor maior, os dois são iguais.')