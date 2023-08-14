import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range(2, 51, 2):
    print(c, end=' ')
print('FIM')

for c in range(1, 51):
    if c % 2 == 0:
      print(c, end=' ')
print('ACABOU')


