import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range(1,7):
    numero = int(input('Digite o {}° número: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Você informou {} números PARES e a soma deles foi {}.'.format(cont, soma))



