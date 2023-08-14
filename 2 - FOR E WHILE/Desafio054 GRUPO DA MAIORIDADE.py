import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere a maioridade com 21 anos.

import datetime

anoatual = datetime.date.today().year
contmenores = 0
contmaiores = 0

for pessoas in range(1, 8):
    nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = anoatual-nascimento
    if idade < 21:
        contmenores += 1
    elif idade >= 21:
        contmaiores += 1
print('{} pessoas ainda não atingiram a maioridade e {} pessoas já são maiores.'.format(contmenores, contmaiores))
