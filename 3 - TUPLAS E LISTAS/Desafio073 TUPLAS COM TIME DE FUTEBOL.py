from os import system, name
system ('cls' if name == 'nt' else 'clear')

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 
'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
'''for t in times:
    print(t)'''
print('-=' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')
print()
