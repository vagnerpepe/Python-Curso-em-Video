from os import system, name
system ('cls' if name == 'nt' else 'clear')

valores = []
while True:
    novovalor = int(input('Digite um valor: '))
    if novovalor not in valores:
        print('Valor adicionado com sucesso...')
        valores.append(novovalor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    parar = ' '
    while parar not in 'SN':
        parar = input('Quer continuar? [S/N] ').upper().strip()
    if parar == 'N':
        break
valores.sort()
print('-=' * 30)
print(f'Você digitou os valores {valores}')

