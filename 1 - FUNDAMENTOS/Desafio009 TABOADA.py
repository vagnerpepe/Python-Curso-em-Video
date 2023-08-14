#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua taboada.

valor = int(input('Digite um número para ver sua taboada: '))
print ('Segue abaixo a taboada do número {}:'.format(valor))
print('-'*12)
if (valor >=0):
    print ('{} x 1 = {}'.format(valor, valor*1))
    print ('{} x 2 = {}'.format(valor, valor*2))
    print ('{} x 3 = {}'.format(valor, valor*3))
    print ('{} x 4 = {}'.format(valor, valor*5))
    print ('{} x 5 = {}'.format(valor, valor*5))
    print ('{} x 6 = {}'.format(valor, valor*6))
    print ('{} x 7 = {}'.format(valor, valor*7))
    print ('{} x 8 = {}'.format(valor, valor*8))
    print ('{} x 9 = {}'.format(valor, valor*9))
    print ('{} x 10 = {}'.format(valor, valor*10))
    print ('-'*12)
else: print ('Erro! Tente novamente digitando um número inteiro.')

#Segunda maneira de fazer:

print ('{} x {:2} = {:3}'.format(valor, 1, valor*1))
print ('{} x {:2} = {:3}'.format(valor, 2, valor*2))
print ('{} x {:2} = {:3}'.format(valor, 3, valor*3))
print ('{} x {:2} = {:3}'.format(valor, 4, valor*4))
print ('{} x {:2} = {:3}'.format(valor, 5, valor*5))
print ('{} x {:2} = {:3}'.format(valor, 6, valor*6))
print ('{} x {:2} = {:3}'.format(valor, 7, valor*7))
print ('{} x {:2} = {:3}'.format(valor, 8, valor*8))
print ('{} x {:2} = {:3}'.format(valor, 9, valor*9))
print ('{} x {:2} = {:3}'.format(valor, 10, valor*10))
print ('-'*12)