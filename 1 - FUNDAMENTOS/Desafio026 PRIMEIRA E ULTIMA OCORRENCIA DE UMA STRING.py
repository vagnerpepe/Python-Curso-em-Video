#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra ''A''
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

import os
os.system('cls' if os.name=='nt'else 'clear')

frase = str(input('Digite uma frase: ')).strip().upper()
print ('A letra A aparece {} vezes na frase.'.format(frase.count('0')))
print ('A primeira letra A apareceu na posição {}.'.format(frase.find('0')+1))
print ('A última letra A apareceu na posição {}.'.format(frase.rfind('0')+1))
