#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

import os
os.system ('cls' if os.name == 'nt' else 'clear')

print ('Informe o comprimento de 3 retas para descobrir se é possível formar um triângulo com essas medidas.')
reta1 = float(input('Informe o comprimento da reta n° 1: '))
reta2 = float(input('Informe o comprimento da reta n° 2: '))
reta3 = float(input('Informe o comprimento da reta n° 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print ('SIM, é possível formar um triângulo com essas medidas.')
else:
    print ('NÃO, não é possível formar um triângulo com essas medidas.')
