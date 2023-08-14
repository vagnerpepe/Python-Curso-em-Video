from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# No final, mostre o conteúdo das três listas geradas.

listacompleta = []
listapar = []
listaimpar = []

while True:
    valor = int(input('Digite um número: '))
    listacompleta.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {listacompleta}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
print()

# Outra maneira de fazer:

'''listacompleta = []
listapar = []
listaimpar = []

while True:
    listacompleta.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
for i, v in enumerate(listacompleta):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print('-=' * 30)
print(f'A lista completa é {listacompleta}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
print()'''
