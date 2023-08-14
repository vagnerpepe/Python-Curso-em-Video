# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

import os
os.system ('cls' if os.name == 'nt' else 'clear')

nome = input('\033[1;32m Qual seu nome?\033[m ').strip()
print('\033[33m Olá {}, seja bem vindo! Faça agora mesmo um empréstimo para comprar sua casa nova!'.format(nome))
casa = float(input('\033[1;32m Qual o valor da casa?\033[m '))
salario = float(input('\033[1;32m Qual o valor do seu salário?\033[m '))
anos = int(input('\033[1;32m Em quantos anos pretende pagar?\033[m '))
meses = anos*12
prestacao = casa/meses
minimo = (30*salario)/100

if prestacao <= minimo:
    print('\033[33m Sua prestação mensal será de R$ {:.2f} durante {:.0f} anos que é igual a {:.0f} meses.\033[m'.format(prestacao, anos, meses))
    print('\033[33m Parabéns {}! Seu empréstimo foi aprovado!\033[m'.format(nome))
else:
    print('\033[31m Para pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R$ {:.2f}.\033[m'.format(casa, anos, prestacao))
    print('\033[31m Sinto muito {}, infelizmente seu empréstimo foi negado.\033[m'.format(nome))
    