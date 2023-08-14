from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numeros = []
par = []
impar = []

for c in range(1,8):
    valores = (int(input(f'Digite o {c}° valor: ')))
    numeros.append(valores)
    if valores % 2 == 0:
        par.append(valores)
    else:
        impar.append(valores)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')
print()

#Outra maneira de resolver:

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')
print()