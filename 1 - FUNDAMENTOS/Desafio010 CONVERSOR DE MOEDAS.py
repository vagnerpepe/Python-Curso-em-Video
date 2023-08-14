#Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere:
#US$ 1,00 = R$ 5,10 (Cotação feita em 26/01/2023)

dolar = 5.10

carteira = float(input('Quantos reais você tem na carteira?: R$ '))

print('Você pode comprar {:.0f} Dólares.'.format(carteira//dolar))

real = float(input('Quanto dinheiro você tem na carteira?: R$ '))
dolarr = real/5.10

print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(real, dolarr))