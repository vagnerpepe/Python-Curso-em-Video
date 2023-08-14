#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import os
os.system('cls' if os.name == 'nt' else 'clear')

n1 = int(input('Digite o 1° n° '))
n2 = int(input('Digite o 2° n° '))
n3 = int(input('Digite o 3° n° '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O maior n° é {}.'.format(maior))
print('O menor n° é {}.'.format(menor))

if n1>n2 and n1>n3:
    print ('O maior n° é {}.'.format(n1))
elif n2>n1 and n2>n3:
    print ('O maior n° é {}.'.format(n2))
elif n3>n1 and n3>n2:
    print ('O maior n° é {}.'.format(n3))

if n1<n2 and n1<n3:
    print ('O menor n° é {}.'.format(n1))
elif n2<n1 and n2<n3:
     print ('O menor n° é {}.'.format(n2))
elif n3<n1 and n3<n2:
     print ('O menor n° é {}.'.format(n3))


