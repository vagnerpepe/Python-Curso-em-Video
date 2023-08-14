import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Faça um programa que calcule a soma entre todas os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de {} valores solicitados é {}.'.format(cont, soma))

#Também pode ser feito assim:
#for c in range(1, 501, 2):
    #if c % 3 == 0:
        #cont += + 1
        #soma += c
#print('A soma de {} valores solicitados é {}.'.format(cont, soma))