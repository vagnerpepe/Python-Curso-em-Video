import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < peso:
            menor = peso
print('O maior peso lido doi de {} Kg.'.format(maior))
print('O menor peso lido doi de {} Kg.'.format(menor))