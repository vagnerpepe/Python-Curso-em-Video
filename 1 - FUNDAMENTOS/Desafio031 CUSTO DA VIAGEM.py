#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Viagens abaixo de 200Km - Passagem = R$ 0,50 por Km')
print('Viagens acima de 200Km - Passagem = R$ 0,45 por Km')
distancia = float(input('Qual a distância em Km? '))
if distancia <= 200:
    print('O valor da passagem é R$ {:.2f}.'.format(distancia*0.50))
else:
    print('O valor da passagem é R$ {:.2f}.'.format(distancia*0.45))