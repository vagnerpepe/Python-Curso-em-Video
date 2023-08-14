# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes 

import os
os.system ('cls' if os.name == 'nt' else 'clear')

print ('Informe o comprimento de 3 retas para descobrir se é possível formar um triângulo com essas medidas.')
reta1 = float(input('Informe o comprimento da reta n° 1: '))
reta2 = float(input('Informe o comprimento da reta n° 2: '))
reta3 = float(input('Informe o comprimento da reta n° 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('SIM, é possível formar um triângulo com essas medidas.')
    if reta1 == reta2 and reta2 == reta3:
        print('Tipo do Triângulo: Equilátero.')
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print('Tipo do Triângulo: Escaleno.')
    elif reta1 == reta2 and reta3 < reta1+reta2 or reta2 == reta3 and reta1 < reta2+reta3 or reta3 == reta1 and reta2 < reta1+reta3:
        print('Tipo do Triângulo: Isósceles.')
else:
    print('NÃO, não é possível formar um triângulo com essas medidas.')


