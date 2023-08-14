#Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

valor = int(input('Digite um número: \n'))
print()
print ('O dobro de {} vale {}.'.format(valor, valor*2))
print ('O triplo de {} vale {}.'.format(valor, valor*3))
print ('A raiz quadrada de {} é igual a {:.2f}.'.format(valor, valor**(1/2)))
print ('A raiz quadrada de {} é igual a {:.2f}.'.format(valor, pow(valor,  1/2)))
