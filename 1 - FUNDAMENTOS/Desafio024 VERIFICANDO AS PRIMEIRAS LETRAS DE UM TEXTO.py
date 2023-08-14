#Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome ''SANTO''.

import os
os.system('cls' if os.name=='nt'else'clear')

nome = input('Digite o nome da cidade: ').strip()
print('Sua cidade começa com a palavra Santo?: {}'.format(nome[:5].upper() == 'SANTO'))
