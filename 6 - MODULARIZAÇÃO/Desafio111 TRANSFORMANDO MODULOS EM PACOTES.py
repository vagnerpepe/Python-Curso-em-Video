from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todos as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from uteis import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 12)