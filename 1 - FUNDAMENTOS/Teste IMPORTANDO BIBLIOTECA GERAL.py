import math
num = int(input('Digite um número inteiro: '))
raiz = math.sqrt(num)

print ('A raiz de {} é igual a {:.2f}.'.format(num, raiz))
print ('A raiz de {} é igual a {}.'.format(num, math.ceil(raiz)))
print ('A raiz de {} é igual a {}.'.format(num, math.floor(raiz)))

print()

import random
num = random.randint(1, 10)
print (num)

import emoji
print (emoji.emojize('Olá Mundo :sunglasses:', use_aliases=True))