from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from uteis import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)