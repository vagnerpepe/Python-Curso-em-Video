import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 = 120

# Maneira simples de resolver:
'''import math

num = int(input('Digite um número para calcular o seu fatorial: '))
f = math.factorial(num)
print('O fatorial de {} é {}.'.format(num, f))'''

# Segunda maneira de resolver:
'''num = int(input('Digite um número para calcular o seu fatorial: '))
cont = num-1
multiplicador = num

while cont > 0:
    multiplicador *= cont
    cont -= 1
    print('{}'.format(cont), end=' ')
    print('x' if cont > 1 else '=', end= ' ')
print('Calculando {}! = {}'.format(num, num))    
print('O fatorial do n° {} é {}.'.format(num, multiplicador))'''

# Terceira maneira de resolver:
num = int(input('Digite um número para calcular o seu fatorial: '))
cont = num
multiplicacao = 1
print('Calculando {}! = '.format(num), end= '')
while cont > 0:
    print('{}'.format(cont), end=' ')
    print('x' if cont > 1 else '=', end= ' ')
    multiplicacao *= cont
    cont -= 1
print('{}'.format(multiplicacao))


