#Escreva um progrma que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

import os
from time import sleep
os.system ('cls' if os.name == 'nt' else 'clear')

numero = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão:
[ 1 ]: BINÁRIO
[ 2 ]: OCTAL
[ 3 ]: HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print('Convertendo...')
    sleep(1)
    print('BINÁRIO: {}'.format(bin(numero)[2:]))
elif opcao == 2:
    print('Convertendo...')
    sleep(1)
    print('OCTAL: {}'.format(oct(numero)[2:]))
elif opcao == 3:
    print('Convertendo...')
    sleep(1)
    print('HEXADECIMAL: {}'.format(hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente!')