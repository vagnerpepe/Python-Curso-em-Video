import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o ususário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

maior18 = homens = mulhermenor = 0

while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulhermenor += 1
    print('-' * 25)
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        print(f'='*6, 'FIM DO PROGRAMA', '='*6)
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos.')
print()
