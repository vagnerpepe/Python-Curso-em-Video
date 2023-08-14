#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

import os
os.system('cls' if os.name=='nt'else 'clear')

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))
