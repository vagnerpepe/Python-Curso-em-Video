#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome
import os
os.system('cls' if os.name=='nt' else'clear')

nome = input('Digite seu nome completo: ').strip()
print ('Em letras maiúsculas: {}'.format(nome.upper()))
print ('Em letras minúsculas: {}'.format(nome.lower()))
print ('Total de letras ao todo sem espaços: {}'.format(len(nome)-nome.count(' ')))
print ('Total de letras no 1° nome: {}'.format(nome.find(' ')))

#outra maneira de descobrir o total de letras no 1° nome:

separa = nome.split()
print ('Seu 1° nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
