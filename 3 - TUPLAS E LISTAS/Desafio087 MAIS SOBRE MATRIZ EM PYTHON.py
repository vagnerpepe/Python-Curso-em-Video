from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)

par = coluna3 = maior2linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]:^5} ] ', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {par}.')
for linha in range(0, 3):
    coluna3 += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {coluna3}.')
for c in range (0, 3):
    if c == 0 or matriz[1][c] > maior2linha:
        maior2linha = matriz[1][c]
print(f'O maior valor da segunda linha é {maior2linha}.')
print()