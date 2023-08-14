from os import system, name
system ('cls' if name == 'nt' else 'clear')

#dicionário pode ser declarado de duas formas:
#list = dict() ou
#list = {}

dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
dados['sexo'] = 'M'
print(dados)
print(dados['sexo'])
del dados['idade']
print(dados)

filme = {'título':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}
print(filme.values()) # Imprime somente os valores que são: 'Star Wars', 1977, 'George Lucas'
print(filme.keys()) # Imprime somente as chaves que são: 'título', 'ano', 'diretor'
print(filme.items()) # Imprime tanto os valores quanto as chaves que são: 'título', 'Star Wars', 'ano', 1977, 'diretor', 'George Lucas'
for k, v in filme.items():
    print(f'O {k} é {v}')
    #O título é Star Wars
    #O ano é 1977
    #O diretor é George Lucas

# ************************************************************************************************************************************

# ***** CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA 1 *****:

locadora = [{'título':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}, {'título':'Avangers', 'ano':2012, 'diretor':'Joss Whedon'},{'título':'Matrix', 'ano':1999, 'diretor':'Wachowski'}]
print(locadora[0]['ano']) # 1977
print(locadora[2]['título']) # Matrix

# ************************************************************************************************************************************

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
print(pessoas) #{'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}
print(pessoas['nome']) #Gustavo
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #O Gustavo tem 22 anos.
print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #dict_values(['Gustavo', 'M', '22'])
print(pessoas.items()) #dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', '22')])
for k in pessoas.keys():
    print(k) #nome | sexo | idade
for k in pessoas.values():
    print(k) #Gustavo | M | 22
for k, v in pessoas.items():
    print(f'{k} = {v}') #nome = Gustavo | sexo = M | idade = 22

del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}') #nome = Gustavo | idade = 22

pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}') #nome = Leandro | sexo = M | idade = 22

pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}') #nome = Leandro | sexo = M | idade = 22 | peso = 98.5

# ************************************************************************************************************************************

# ***** CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA 2 *****:

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil) #[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(estado1) #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2) #{'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]) #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1]) #{'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf']) #Rio de Janeiro
print(brasil[1]['sigla']) #SP

# ************************************************************************************************************************************

# ***** CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA 3 *****:

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil) #[{'uf': 'Minas Gerais', 'sigla': 'MG'}, {'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}]

for e in brasil:
    print(e) #{'uf': 'Rio', 'sigla': 'RJ'} | {'uf': 'Sampa', 'sigla': 'SP'} | {'uf': 'Paraná', 'sigla': 'PR'}

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
        #O campo uf tem valor Rio de Janeiro.
        #O campo sigla tem valor RJ.
        #O campo uf tem valor São Paulo.
        #O campo sigla tem valor SP.
        #O campo uf tem valor Goiás.
        #O campo sigla tem valor GO.

for e in brasil:
    for v in e.values():
        print(v)
        #Rio
        #RJ
        #Sampa
        #SP
        #Bahia
        #BA
        
for e in brasil:
    for v in e.values():
        print(v, end='')
    print()
        #AcreAC
        #AmazonasAM
        #ParáPA

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
        #Acre AC
        #Amazonas AM
        #Pará PA