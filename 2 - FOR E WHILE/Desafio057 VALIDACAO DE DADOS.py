import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''sexo = ''
mas = 'M'
while sexo != mas:
    sexo = input('Informe o seu sexo [M/F]: ').upper().strip()[0]
    if sexo == 'F':
        mas = 'F'
print('Sexo {} registrado com sucesso.'.format(mas))'''

sexo = input('Informe o seu sexo [M/F]: ').upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
