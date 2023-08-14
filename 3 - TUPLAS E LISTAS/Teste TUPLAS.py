from os import system, name
system ('cls' if name == 'nt' else 'clear')

'''
lanche = hamburguer, suco, pizza, pudim
   Índices:  0         1     2      3

print(lanche[2])  vai printar pizza
print(lanche[0:2]) vai printar do hambuerguer até suco, porque ele desconsidera o último
print(lanche[1:]) vai printar do suco até o último item, que no caso é o pudim
print(lanche[-1]) vai printar o último elemento, que no caso é o pudim
print(lanche[-2]) vai printar o penúltimo elemento, que no caso é a pizza
print(lanche[-3]) vai printar o antipenúltimo elemento, que no caso é o suco
print(lanche[-4]) vai printar o hamburguer, ou seja, posso acessar o hamburguer de duas maneiras, ou ele é o
lanche [0] ou ele é o lanche[-4].

len(lanche) resposta = 4  :  'len vai mostrar quantos elementos tem dentro de lanche, no caso é 4'

for c in lanche: #Note que não tem o range                       
    print(c)              print(c) = hamburguer      'ou seja, depois de printar hamburguer,
                          print(c) = suco            ele vai ficar num laço printando linha por linha
                          print(c) = pizza           o que tiver na variável composta lanche'
                          print(c) = pudim

IMPORTANTE: As tuplas são imutáveis, ou seja, não é possível alterá-las depois de definilas.
            Toda tupla é feita entre parenteses (     )
'''
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(len(lanche))

for comida in lanche:
    print(f'Eu vou querer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou querer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou querer {comida}, na posição {pos}')

print(sorted(lanche)) #Aparece os itens da variável lanche organizados por ordem alfabética

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c) 
print(c.index(5)) # Mostra em que posição está o 5
print(c.index(5, 1)) # Mostra em que posição está o 5 a partir da posição 1 (pra no caso de haver mais de um 5)
print(len(c)) # Mostra quantos elementos tem dentro da variável
print(c.count(5)) # Mostra quantas vezes está aparecendo o número 5 dentro da variável 'c'
print(sorted(c)) # Mostra a variável 'c' na ordem numérica no caso por se tratar de números

pessoa = ('Vagner', 32, 'M', 99.88)
del(pessoa) #Eu posso deletar uma tupla, mas não alterá-la e nem excluir apenas um item da tupla
print(pessoa)