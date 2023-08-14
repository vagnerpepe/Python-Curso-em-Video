import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Quer ver a tabuada de qual valor? \033[1;32m'))
    if num < 0:
        break
    print('\033[m-' * 35)
    for cont in range(1, 11):
        print(f'{num} x {cont:2} = {num * cont}')
    print('-' * 35)
print('\033[m-' * 35)
print('\033[31mPROGRAMA TABUADA ENCERRADO. Volte Sempre!\033[m')  
print()  
