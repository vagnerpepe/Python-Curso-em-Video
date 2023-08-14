#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

import os
os.system('cls' if os.name == 'nt'else'clear')

numero = int(input('Digite um número: '))
par = numero%2

if par >0:
    print('O número {} é Ímpar.'.format(numero))
else:
    print('O número {} é Par.'.format(numero))
