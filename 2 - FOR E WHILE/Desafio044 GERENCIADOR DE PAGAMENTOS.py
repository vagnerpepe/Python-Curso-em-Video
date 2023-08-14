# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

import os
os.system ('cls' if os.name == 'nt' else 'clear')

print('{:=^40}'.format(' LOJAS PÉPE '))
quantidade = float(input('Digite a quantidade: '))
valor = float(input('Digite o valor do produto R$ '))
subtotal = quantidade*valor
opcao1 = (subtotal*10)/100
opcao2 = (subtotal*5)/100
opcao4 = (subtotal*20)/100

print('Subtotal R$ {:.2f}'.format(subtotal))
print()
print('FORMAS DE PAGAMENTO:')
print('''\033[1;33m[ 1 ]\033[m - À vista dinheiro/cheque: 10% de desconto
\033[1;33m[ 2 ]\033[m - À vista no cartão      :  5% de desconto
\033[1;33m[ 3 ]\033[m - Em até 2x no cartão    :  Preço normal
\033[1;33m[ 4 ]\033[m - 3x ou mais no cartão   : 20% de juros''')
print()

condicao = int(input('Digite a opção de pagamento: '))

if condicao == 1:
    print('Subtotal R$ {:.2f}'.format(subtotal))
    print('Desconto R$ {:.2f}'.format(opcao1))
    print('Total    R$ {:.2f}'.format(subtotal-opcao1))
elif condicao == 2:
    print('Subtotal R$ {:.2f}'.format(subtotal))
    print('Desconto R$ {:.2f}'.format(opcao2))
    print('Total    R$ {:.2f}'.format(subtotal-opcao2))
elif condicao == 3:
    parcela = int(input('Quantas parcelas? '))
    print('Subtotal R$ {:.2f}'.format(subtotal))
    print('Juros    R$ 0,00')
    print('Total    R$ {:.2f}'.format(subtotal))
    print('Compra parcelada em {}x de R$ {:.2f}.'.format(parcela, subtotal/parcela))

if condicao == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Subtotal R$ {:.2f}'.format(subtotal))
    print('Juros    R$ {:.2f}'.format(opcao4))
    print('Total    R$ {:.2f}'.format(subtotal+opcao4))
    print('Compra parcelada em {}x de R$ {:.2f}.'.format(parcela, (subtotal+opcao4)/parcela))

while condicao <1 or condicao >4:
    print('Opção inválida.')
    condicao = int(input('Digite a opção de pagamento: '))
