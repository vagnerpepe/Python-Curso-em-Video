from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporaria = []
principal = []
pesada = leve = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        pesada = leve = temporaria[1]
    else:
        if temporaria[1] > pesada:
            pesada = temporaria[1]
        if temporaria[1] < leve:
            leve = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
    
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas. ')
print(f'O maior peso foi de {pesada} Kg. Peso de ', end='')
for p in principal:
    if p[1] == pesada:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {leve} Kg. Peso de ', end='')
for p in principal:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')
print()