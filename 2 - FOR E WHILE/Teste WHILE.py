import os
os.system ('cls' if os.name == 'nt' else 'clear')

'''enquanto não maçã:                    while not maçã:
    passo                                   passo
pega                                  pega

enquanto não maçã:                    while not maçã:
    se tiver chão                        if chão:
       passo                                passo
    se tiver buraco                      if tiver buraco:
       pula                                 pula
    se tiver moeda                       if tiver moeda:
       pega                                 pega
pega                                  pega

for c in range(1, 10):
    print(c)
print('Fim')

c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

for c in range(1, 3):
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar? [S/N] ').upper()
print('Fim')''' 

n = 1
par = impar = 0
while n!= 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1        
print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))