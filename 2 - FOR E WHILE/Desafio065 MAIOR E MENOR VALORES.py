import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores lidos e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = 0
resp = 'S'
soma = quant = media = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = input('Quer continuar? [ S/N ]\n''').upper().strip()[0]
media = soma/quant
print('Você digitou {} números e a média foi {:.2f}.'.format(quant, media))
print('O maior valor é {} e o menor valor é {}.'.format(maior, menor))
