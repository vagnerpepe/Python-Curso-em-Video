import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$ 1.000.
# C) Qual é o nome do produto mais barato.

print('\033[34m-'*35)
print('{:^45}'.format('\033[m\033[31mLOJA PÉPE INFORMÁTICA\033[m'))
print('\033[34m-'*35)
total = caro = menor = cont = 0
barato = ''
while True:
    produto = input('\033[mNome do Produto: \033[32m').strip().capitalize()
    qtd = int(input('\033[mQuantidade: \033[32m'))
    preco = float(input('\033[mPreço: R$ \033[32m'))
    cont += 1
    total += qtd * preco 
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('\033[mQuer continuar? [\033[33mS\033[m/\033[33mN\033[m] \033[32m').upper().strip()[0]
    if continuar == 'N':
        print('\033[m\033[34m-\033[m'*9, '\033[31mFIM DO PROGRAMA\033[m', '\033[34m-\033[m'*9)
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menorpreco:.2f}')
print()
