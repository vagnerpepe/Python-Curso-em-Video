# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Acima de 20 anos: SÊNIOR
# Acima: MASTER

import os
os.system ('cls' if os.name == 'nt' else 'clear')

import datetime

nascimento = int(input('Digite o seu ano de nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual-nascimento

if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MIRIM')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: SÊNIOR')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Classificação: MASTER')