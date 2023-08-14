import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = cont = soma = 0
num = int(input('Digite um número ou [999 para parar]: '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número ou [999 para parar]: '))
print('Foram digitados {} números '.format(cont), end='')
print('e a soma deles foi {}.'.format(soma))
