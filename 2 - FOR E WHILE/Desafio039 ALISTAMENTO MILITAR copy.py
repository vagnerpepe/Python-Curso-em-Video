# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import os
os.system ('cls' if os.name == 'nt' else 'clear')

import datetime

anoatual = datetime.date.today().year

nascimento = int(input('Digite seu ano de nascimento: '))

idade = anoatual-nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))

if idade == 18:
    print('É hora de se alistar.')
elif idade < 18:
    saldo = 18-idade
    ano = anoatual+saldo
    print('Você ainda vai se alistar ao serviço militar.')
    print('Falta {} anos para você se alistar.'.format(saldo))
    print('Você se alistará em {}.'.format(ano))
elif idade > 18:
    saldo = idade-18
    print('Já passou do tempo do alistamento.')
    print('Você está a {} anos fora do prazo.'.format(saldo))
