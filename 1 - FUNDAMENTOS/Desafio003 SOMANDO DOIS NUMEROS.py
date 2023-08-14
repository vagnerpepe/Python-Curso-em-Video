#Crie um programa que leia dois números e mostre a soma entre eles.

valor1 = int(input('Digite o primeiro n°: \n'))
valor2 = int(input('Digite o segundo n°: \n'))
s = (valor1+valor2)

print('A soma entre {0} e {1} é {2}'.format(valor1, valor2, s))

#Segunda maneira de fazer:

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segunto número: '))
s1 = n1+n2
print('A soma vale {}'. format(s1))