#laço c no intervalo(1,10):            for c in range(1,10):
#    passo                                  passo
#pega                                  pega


#laço c no intervalo(0,3):             for c in range(0,3):
#    passo                                  passo
#    pulo                                   pulo  
#passo                                 passo
#pega                                  pega


#laço c no intervalo(0,3):             for c in range(0,3):
#    se (moeda)                        if (moeda)
#        pega                                   pega
#    passo                                  passo
#    pulo                                   pulo  
#passo                                 passo
#pega                                  pega

import os
os.system ('cls' if os.name == 'nt' else 'clear')

for c in range(0, 7, 2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores {}.'.format(s))