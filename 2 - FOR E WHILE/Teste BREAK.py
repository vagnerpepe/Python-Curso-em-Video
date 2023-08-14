import os
os.system ('cls' if os.name == 'nt' else 'clear')

'''
enquanto Verdadeiro:                  while True:
    se chão                              if chão:
       passo                                passo
    se buraco                            if buraco:
       pula                                 pula
    se moeda                             if moeda:
       pega                                 pega
    se troféu                            if troféu:
       pula                                 pula
       interrompa                           break
pega                                  pega'''

'''cont = 1
while cont <= 10:
    print(cont, '-> ', end= '')
    cont += 1
print('Acabou')'''

num = s = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s += num
#print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')

nome = 'Vagner'
idade = 32
salario = 987.3
print(f'O {nome:20} tem {idade} anos e ganha R$ {salario:.2f}.')# :20 significa 20 espaços
print(f'O {nome:^20} tem {idade} anos e ganha R$ {salario:.2f}.')# ^ alinhar centralizado
print(f'O {nome:->20} tem {idade} anos e ganha R$ {salario:.2f}.')# -^ alinhar a direita com traços
print(f'O {nome:-<20} tem {idade} anos e ganha R$ {salario:.2f}.')# -^ alinhar a esquerda com traços
print(f'O {nome:-^20} tem {idade} anos e ganha R$ {salario:.2f}.')# -^ alinhar centralizado com traços
print('{:-^40}'.format('LOJA PÉPE INFORMÁTICA'))# centralizar