#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para salários inferiores a R$ 1.250,00, calcule um aumento de 15%.

import os
os.system ('cls' if os.name == 'nt' else 'clear')

salario = float(input('Qual o valor do seu salário? R$ '))

if salario > 1250.00:
    print('Seu salário de R$ {:.2f} passou a ser de R$ {:.2f} com um aumento de 10%.'.format(salario, salario+((salario*10)/100)))
else:
    print('Seu salário de R$ {:.2f} passou a ser de R$ {:.2f} com um aumento de 15%.'.format(salario, salario+((salario*15)/100)))
