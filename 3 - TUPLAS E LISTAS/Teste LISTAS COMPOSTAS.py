from os import system, name
system ('cls' if name == 'nt' else 'clear')

dados = []
dados.append('Pedro') # Adicionando Pedro na lista
dados.append(25) # Adicionando 25 na lista
print(dados[0]) # Print apenas Pedro que está na posição 0
print(dados[1]) # Print apenas 25 que está na posição 1
dados1 = []
dados1.append('Maria')
dados1.append(19)
dados2 = []
dados2.append('João')
dados2.append(32)
pessoas = []
pessoas.append(dados[:])
print(pessoas[0][0]) # = Pedro

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera: # pra cada pessoa in galera
    print(p) # ele vai printar uma lista: ['João', 19]
                                         #['Ana', 33]
                                         #['Joaquim', 13]
                                         #['Maria', 45]
for p in galera: # pra cada pessoa in galera
    print(p[0]) # ele vai printar só os nomes: João
                                              #Ana
                                              #Joaquim
                                              #Maria
for p in galera: # pra cada pessoa in galera
    print(p[1]) # ele vai printar só a idade: 19
                                             #33
                                             #13
                                             #45
for p in galera: # pra cada pessoa in galera
    print(f'{p[0]} tem {p[1]} anos de idade.') # ele vai printar só os nomes e as idades:
                                                                #João tem 19 anos de idade.
                                                                #Ana tem 33 anos de idade.
                                                                #Joaquim tem 13 anos de idade.
                                                                #Maria tem 45 anos de idade.
galera = []
dado = []
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # [:] cópia de dado
    dado.clear()
print(galera)

maior = menor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Temos {maior} maiores e {menor} menores de idade.')