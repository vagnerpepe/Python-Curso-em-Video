import os
from time import sleep
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Informe o \033[1;33m1°\033[m valor: \033[1;32m'))
n2 = int(input('\033[mInforme o \033[1;33m2°\033[m valor: \033[1;32m'))

opcao = 0

while opcao != 5:
    print('''\n\033[mOPÇÕES:
    \033[1;33m[ 1 ]\033[m Somar
    \033[1;33m[ 2 ]\033[m Multiplicar
    \033[1;33m[ 3 ]\033[m Maior
    \033[1;33m[ 4 ]\033[m Novos Números
    \033[1;31m[ 5 ]\033[m Sair do Programa\n\033[m''')
    opcao = int(input('Escolha a opção desejada: \033[1;32m'''))
    if opcao == 1:
        print('\n\033[mA soma de {} + {} é igual a {}.'.format(n1, n2, n1 + n2))     
    elif opcao == 2:
        print('\n\033[mA multiplicação de {} x {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('\n\033[mO maior valor entre {} e {} é {}.'.format(n1, n2, n1))
        elif n1 < n2:
            print('\n\033[mO maior valor entre {} e {} é {}.'.format(n1, n2, n2))
        else:
            print('\n\033[mNão há valor maior, pois os valores {} e {} são iguais.'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('\033[mInforme o 1° valor: \033[1;32m'))
        n2 = int(input('\033[mInforme o 2° valor: \033[1;32m'))
    elif opcao == 5:
        print('\033[m\033[1;31mFinalizando...\033[m')
    else:
        print('Opção inválida. Tente novamente.') 
    print('=-='*10)   
sleep(1)
print('Fim do programa! Volte sempre!')
