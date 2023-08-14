from os import system, name
system ('cls' if name == 'nt' else 'clear')

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picolé'
print(lanche) # Listas são mutáveis, por isso podem ser mofificadas
lanche.append('Cookie') # O comando append serve para adicionar um item na lista
print(lanche)
lanche.insert(0, 'Cachorro-quente') # O comando insert serve para criar um item em determinada posição na lista,
# no caso, eu adicionei o Cachorro-quente na posição 0
print(lanche)

del lanche[3] # O comando del é utilizado para apagar um determinado elemento da lista ou a lista toda
lanche.pop(3) / lanche.pop # O comando pop é utilizado para apagar últim item da lista, porém posso determinar índice pra ele eliminar
lanche.remove('Pizza') # O comando remove, eu não vou indicar o índice que quero eliminar mas o valor
# Importante: o remove vai eliminar o primeiro elemente que ele encontrar partindo do índice 0
print(lanche) # Note que a pizza que era o 3° item foi apagado
if 'Pizza' in lanche:
    lanche.remove('Pizza') # Se houver pizza em lanche, remova-a

valores = list(range(4, 11)) # Irá criar uma lista chamada valores com os números 4,5,6,7,8,9,10 sendo o n° 4 o índice 0
valores = [8,2,5,4,9,3,0]
valores.sort() # O comando sort coloca a lista em ordem
valores.sort(reverse=True) # O comando sort(reverse=True) coloca a lista na ordem inversa
print(valores)
print(len(valores)) # O comando len conta quantos itens tem na lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

# Criando uma ligação entre A e B, quando altero o B, também altero o A:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Criando uma cópia de A em B, fazendo assim com que B tenha apenas uma cópia de A e não uma ligação:
a = [2, 3, 4, 7]
b = a[:] # Cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')