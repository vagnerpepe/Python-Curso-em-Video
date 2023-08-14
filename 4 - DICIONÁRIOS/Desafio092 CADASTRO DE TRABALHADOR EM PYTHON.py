from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule o acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - anoNascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
print()