import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
# No final, mostre os 10 primeiros termos dessa progressao.

print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end= ' → ')
print('ACABOU')