from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# 0 | x | x | x |
# 1 | x | x | x |
# 2 | x | x | x |
#   | 0 | 1 | 2 |
# No final, mostre a matriz na tela com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]:^5} ] ', end='')
    print()
print()