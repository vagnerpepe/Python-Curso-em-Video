from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de idade do grupo. C) Uma lista com todas as mulheres. D) Uma lista com todas as pessoas com idade acima da média.

lista = list()
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
print(f'A) O grupo tem {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'c) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) As pessoas acima que estão acima da média são: ')
for p in lista:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
print()