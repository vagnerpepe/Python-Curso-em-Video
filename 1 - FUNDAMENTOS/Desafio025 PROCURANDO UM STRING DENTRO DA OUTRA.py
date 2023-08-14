#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

import os
os.system('cls' if os.name=='nt'else'clear')

nome = input('Digite o nome completo: ').strip()
print('Seu nome tem Silva?: {}'.format('silva' in nome.lower()))