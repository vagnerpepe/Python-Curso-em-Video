import os
os.system ('cls' if os.name == 'nt' else 'clear')

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final, o programa mostre:
# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

media = 0
idadehomemvelho = 0
nomehomemvelho = ''
cont = 0

for pessoas in range(1, 5):
    print('------------ {}ª ------------'.format(pessoas))
    nome = input('Informe o nome da {}ª pessoa: '.format(pessoas)).strip()
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo, sendo M (masculino) e F (feminino): ').upper().strip()
    media = media + idade
    if sexo == 'M' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
    elif sexo == 'F' and idade < 20:
        cont += 1
print()
print('A média de idade do grupo é de {:.1f} anos.'.format(media/pessoas))
print('{} é o homem mais velho do grupo e tem {} anos.'.format(nomehomemvelho, idadehomemvelho))
print('Ao todo, são {} mulher(res) com menos de 20 anos.'.format(cont))
